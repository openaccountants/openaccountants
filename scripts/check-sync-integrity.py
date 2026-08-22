#!/usr/bin/env python3
"""Detect stale or conflicting writes to hand-maintained ``skills/**`` guides.

The public audit mode compares two Git revisions.  The private platform exporter
can use strict sync mode before committing its rendered worktree.  Strict mode
requires a provenance file whose ``expected_repo_blob`` values are optimistic-
concurrency tokens captured from the last successfully ingested/exported guide.

This is deliberately a source-guide guard.  Generated ``packages/**``,
``index.json`` and ``llms-full.txt`` remain the responsibility of the normal
generation pipeline.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path, PurePosixPath
from typing import Any, Iterable

from frontmatter_yaml import load_frontmatter


SYNC_BOT_NAMES = {"openaccountants-sync[bot]"}
SYNC_BOT_EMAILS = {"sync@openaccountants.com"}
SOURCE_PREFIX = "skills/"
VERSION_RE = re.compile(r"^\d+(?:\.\d+)*$")
HEADING_VERSION_RE = re.compile(r"\bv(\d+(?:\.\d+)+)\b", re.IGNORECASE)
UNCERTAINTY_PATTERNS = (
    re.compile(r"_unsure_", re.IGNORECASE),
    re.compile(r"\(\s*unsure\s*\)", re.IGNORECASE),
    re.compile(r"\b(?:TODO|TBD)\b"),
    re.compile(r"\[citation needed\]", re.IGNORECASE),
)


@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    path: str
    message: str


@dataclass(frozen=True)
class Guide:
    fields: dict[str, str]
    body: str
    last_updated: date | None
    version: tuple[int, ...] | None
    version_text: str | None
    heading_version: tuple[int, ...] | None
    heading_version_text: str | None


@dataclass(frozen=True)
class Change:
    status: str
    before_path: str | None
    after_path: str | None

    @property
    def display_path(self) -> str:
        if self.status == "R":
            return f"{self.before_path} -> {self.after_path}"
        return self.after_path or self.before_path or "<unknown>"


class IntegrityError(RuntimeError):
    """Raised for invocation or repository errors, not content findings."""


def run_git(
    repo: Path,
    *args: str,
    input_bytes: bytes | None = None,
    allow_failure: bool = False,
) -> bytes:
    result = subprocess.run(
        ["git", *args],
        cwd=repo,
        input=input_bytes,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode and not allow_failure:
        stderr = result.stderr.decode("utf-8", errors="replace").strip()
        raise IntegrityError(f"git {' '.join(args)} failed: {stderr}")
    return result.stdout


def git_text(repo: Path, *args: str, allow_failure: bool = False) -> str:
    return run_git(repo, *args, allow_failure=allow_failure).decode(
        "utf-8", errors="replace"
    )


def repository_root(candidate: Path) -> Path:
    root = git_text(candidate, "rev-parse", "--show-toplevel").strip()
    return Path(root).resolve()


def validate_source_path(path: str) -> str:
    normalized = path.replace("\\", "/")
    pure = PurePosixPath(normalized)
    if pure.is_absolute() or ".." in pure.parts:
        raise IntegrityError(f"unsafe repository path: {path!r}")
    if not normalized.startswith(SOURCE_PREFIX) or not normalized.endswith(".md"):
        raise IntegrityError(f"not a source-guide path: {path!r}")
    return normalized


def parse_name_status(raw: str) -> list[Change]:
    tokens = raw.split("\0")
    if tokens and tokens[-1] == "":
        tokens.pop()

    changes: list[Change] = []
    index = 0
    while index < len(tokens):
        status_token = tokens[index]
        index += 1
        status = status_token[:1]
        if status in {"R", "C"}:
            if index + 1 >= len(tokens):
                raise IntegrityError("malformed rename/copy output from git diff")
            old_path = validate_source_path(tokens[index])
            new_path = validate_source_path(tokens[index + 1])
            index += 2
            changes.append(Change("R", old_path, new_path))
        elif status in {"A", "M", "D", "T"}:
            if index >= len(tokens):
                raise IntegrityError("malformed path output from git diff")
            path = validate_source_path(tokens[index])
            index += 1
            normalized_status = "M" if status == "T" else status
            changes.append(
                Change(
                    normalized_status,
                    None if normalized_status == "A" else path,
                    None if normalized_status == "D" else path,
                )
            )
        else:
            raise IntegrityError(f"unsupported git change status: {status_token!r}")
    return changes


def changed_guides(repo: Path, base: str, head: str | None) -> list[Change]:
    args = ["diff", "--name-status", "-z", "--find-renames", base]
    if head is not None:
        args.append(head)
    args.extend(["--", "skills/**/*.md", "skills/*.md"])
    changes = parse_name_status(git_text(repo, *args))

    if head is None:
        tracked = {change.after_path or change.before_path for change in changes}
        untracked = git_text(
            repo,
            "ls-files",
            "--others",
            "--exclude-standard",
            "-z",
            "--",
            "skills/**/*.md",
            "skills/*.md",
        )
        for path in filter(None, untracked.split("\0")):
            normalized = validate_source_path(path)
            if normalized not in tracked:
                changes.append(Change("A", None, normalized))

    return sorted(changes, key=lambda change: change.display_path)


def read_revision_file(repo: Path, revision: str, path: str) -> str | None:
    result = subprocess.run(
        ["git", "show", f"{revision}:{path}"],
        cwd=repo,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode:
        return None
    return result.stdout.decode("utf-8", errors="replace")


def read_worktree_file(repo: Path, path: str) -> str | None:
    normalized = validate_source_path(path)
    candidate = (repo / Path(*PurePosixPath(normalized).parts)).resolve()
    try:
        candidate.relative_to(repo)
    except ValueError as exc:
        raise IntegrityError(f"path escapes repository: {path!r}") from exc
    if not candidate.is_file():
        return None
    return candidate.read_text(encoding="utf-8")


def scalar_value(raw: str) -> str:
    value = raw.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1].strip()
    return value.split(" #", 1)[0].strip()


def parse_version(raw: str | None) -> tuple[int, ...] | None:
    if raw is None:
        return None
    value = scalar_value(raw)
    if not VERSION_RE.fullmatch(value):
        return None
    parts = [int(part) for part in value.split(".")]
    while len(parts) > 1 and parts[-1] == 0:
        parts.pop()
    return tuple(parts)


def parse_date(raw: str | None) -> date | None:
    if raw is None:
        return None
    try:
        return date.fromisoformat(scalar_value(raw))
    except ValueError:
        return None


def parse_guide(text: str, *, strict_yaml: bool = True) -> Guide:
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = normalized.split("\n")
    if not lines or lines[0].strip() != "---":
        raise ValueError("missing opening frontmatter delimiter")

    try:
        end = next(index for index in range(1, len(lines)) if lines[index].strip() == "---")
    except StopIteration as exc:
        raise ValueError("missing closing frontmatter delimiter") from exc

    if strict_yaml:
        load_frontmatter("\n".join(lines[1:end]))

    fields: dict[str, str] = {}
    for line in lines[1:end]:
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if match:
            fields[match.group(1)] = match.group(2)

    body = "\n".join(lines[end + 1 :])
    heading_text: str | None = None
    heading_version: tuple[int, ...] | None = None
    for line in body.splitlines()[:50]:
        if not re.match(r"^\s{0,3}#{1,6}\s+", line):
            continue
        match = HEADING_VERSION_RE.search(line)
        if match:
            heading_text = match.group(1)
            heading_version = parse_version(heading_text)
            break

    version_raw = fields.get("version")
    return Guide(
        fields=fields,
        body=body,
        last_updated=parse_date(fields.get("last_updated")),
        version=parse_version(version_raw),
        version_text=scalar_value(version_raw) if version_raw is not None else None,
        heading_version=heading_version,
        heading_version_text=heading_text,
    )


def is_guide_document(text: str | None) -> bool:
    """Match the repository validator: Markdown without frontmatter is a doc."""
    return text is not None and text.startswith("---")


def normalize_body(body: str) -> str:
    return "\n".join(line.rstrip() for line in body.splitlines()).strip("\n")


def short_body_hash(body: str) -> str:
    return hashlib.sha256(normalize_body(body).encode("utf-8")).hexdigest()[:12]


def uncertainty_count(body: str) -> int:
    return sum(len(pattern.findall(body)) for pattern in UNCERTAINTY_PATTERNS)


def version_label(value: tuple[int, ...] | None, raw: str | None) -> str:
    if raw is not None:
        return raw
    if value is None:
        return "<missing>"
    return ".".join(str(part) for part in value)


def compare_existing_guides(
    path: str,
    before_text: str,
    after_text: str,
    mode: str,
    strict_metadata: bool = False,
) -> list[Finding]:
    findings: list[Finding] = []
    try:
        before = parse_guide(before_text)
    except ValueError as exc:
        # A malformed legacy base must be repairable.  Parse its simple scalar
        # metadata with the established tolerant reader so the normal date,
        # version and body-change guards still apply, while requiring the
        # candidate itself to pass strict YAML below.
        try:
            before = parse_guide(before_text, strict_yaml=False)
        except ValueError:
            return [Finding("error", "invalid-base", path, f"base guide is invalid: {exc}")]
        findings.append(
            Finding(
                "notice",
                "frontmatter-repaired",
                path,
                f"candidate repairs invalid base frontmatter: {exc}",
            )
        )
    try:
        after = parse_guide(after_text)
    except ValueError as exc:
        return [Finding("error", "invalid-candidate", path, f"candidate guide is invalid: {exc}")]

    if before.last_updated is not None and after.last_updated is not None:
        if after.last_updated < before.last_updated:
            findings.append(
                Finding(
                    "error",
                    "date-regression",
                    path,
                    f"last_updated moved backwards: {before.last_updated} -> {after.last_updated}",
                )
            )
    elif before.last_updated is not None and after.last_updated is None:
        findings.append(
            Finding("error", "date-removed", path, "last_updated was removed or became invalid")
        )

    if before.version is not None and after.version is not None:
        if after.version < before.version:
            findings.append(
                Finding(
                    "error",
                    "version-regression",
                    path,
                    "frontmatter version moved backwards: "
                    f"{version_label(before.version, before.version_text)} -> "
                    f"{version_label(after.version, after.version_text)}",
                )
            )
    elif before.version is not None and after.version_text is not None and after.version is None:
        findings.append(
            Finding(
                "error",
                "version-became-unordered",
                path,
                f"numeric frontmatter version {before.version_text!r} became "
                f"non-numeric {after.version_text!r}",
            )
        )
    elif before.version_text is not None and after.version_text is None:
        findings.append(
            Finding("error", "version-removed", path, "frontmatter version was removed")
        )
    elif after.version_text is not None and after.version is None:
        findings.append(
            Finding(
                "warning",
                "version-unordered",
                path,
                f"frontmatter version {after.version_text!r} is not numerically orderable",
            )
        )

    if before.heading_version is not None and after.heading_version is not None:
        if after.heading_version < before.heading_version:
            findings.append(
                Finding(
                    "error",
                    "heading-version-regression",
                    path,
                    "body heading version moved backwards: "
                    f"v{before.heading_version_text} -> v{after.heading_version_text}",
                )
            )

    before_mismatch = (
        before.version is not None
        and before.heading_version is not None
        and before.version != before.heading_version
    )
    after_mismatch = (
        after.version is not None
        and after.heading_version is not None
        and after.version != after.heading_version
    )
    if after_mismatch and not before_mismatch:
        findings.append(
            Finding(
                "error",
                "version-mismatch",
                path,
                f"frontmatter version {after.version_text} disagrees with body heading "
                f"v{after.heading_version_text}",
            )
        )

    body_changed = normalize_body(before.body) != normalize_body(after.body)
    date_advanced = (
        before.last_updated is not None
        and after.last_updated is not None
        and after.last_updated > before.last_updated
    )
    version_advanced = (
        before.version is not None
        and after.version is not None
        and after.version > before.version
    )
    if body_changed and not date_advanced and not version_advanced:
        severity = "error" if mode == "sync" or strict_metadata else "warning"
        findings.append(
            Finding(
                severity,
                "unversioned-body-change",
                path,
                "body changed without advancing last_updated or version "
                f"({short_body_hash(before.body)} -> {short_body_hash(after.body)})",
            )
        )

    before_uncertainty = uncertainty_count(before.body)
    after_uncertainty = uncertainty_count(after.body)
    if after_uncertainty > before_uncertainty:
        findings.append(
            Finding(
                "warning",
                "uncertainty-increase",
                path,
                f"uncertainty markers increased: {before_uncertainty} -> {after_uncertainty}",
            )
        )

    return findings


def validate_new_guide(path: str, text: str) -> list[Finding]:
    try:
        guide = parse_guide(text)
    except ValueError as exc:
        return [Finding("error", "invalid-new-guide", path, f"new guide is invalid: {exc}")]

    findings: list[Finding] = []
    if guide.version_text is not None and guide.version is None:
        findings.append(
            Finding(
                "error",
                "version-unordered",
                path,
                f"new guide version {guide.version_text!r} must be a numeric dotted value",
            )
        )
    if guide.version is not None and guide.heading_version is not None:
        if guide.version != guide.heading_version:
            findings.append(
                Finding(
                    "error",
                    "version-mismatch",
                    path,
                    f"frontmatter version {guide.version_text} disagrees with body heading "
                    f"v{guide.heading_version_text}",
                )
            )
    return findings


def revision_blob(repo: Path, revision: str, path: str) -> str | None:
    output = git_text(repo, "rev-parse", f"{revision}:{path}", allow_failure=True).strip()
    return output or None


def worktree_blob(repo: Path, path: str) -> str | None:
    normalized = validate_source_path(path)
    candidate = repo / Path(*PurePosixPath(normalized).parts)
    if not candidate.is_file():
        return None
    # --path applies the repository's clean filters (notably core.autocrlf), so
    # this is the blob Git would store rather than a hash of platform bytes.
    return run_git(
        repo,
        "hash-object",
        f"--path={normalized}",
        "--stdin",
        input_bytes=candidate.read_bytes(),
    ).decode("ascii", errors="replace").strip()


def load_provenance(path: Path) -> dict[str, dict[str, Any]]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise IntegrityError(f"cannot read provenance file {path}: {exc}") from exc
    if not isinstance(payload, dict):
        raise IntegrityError("provenance must be a JSON object keyed by skills/** path")

    normalized: dict[str, dict[str, Any]] = {}
    for raw_path, entry in payload.items():
        if not isinstance(raw_path, str) or not isinstance(entry, dict):
            raise IntegrityError("each provenance entry must be an object keyed by a path")
        normalized[validate_source_path(raw_path)] = entry
    return normalized


def validate_content_revision(path: str, entry: dict[str, Any]) -> list[Finding]:
    revision = entry.get("content_revision")
    if isinstance(revision, bool) or not isinstance(revision, int) or revision < 0:
        return [
            Finding(
                "error",
                "invalid-content-revision",
                path,
                "content_revision must be a non-negative integer",
            )
        ]
    return []


def validate_provenance_entry(
    path: str,
    entry: dict[str, Any],
    expected_blob: str | None,
) -> list[Finding]:
    findings: list[Finding] = []
    provided_blob = entry.get("expected_repo_blob", "<missing>")

    if provided_blob == "<missing>":
        findings.append(
            Finding("error", "missing-cas-token", path, "provenance lacks expected_repo_blob")
        )
    elif provided_blob != expected_blob:
        findings.append(
            Finding(
                "error",
                "cas-conflict",
                path,
                "expected_repo_blob does not match the current base blob "
                f"({provided_blob!r} != {expected_blob!r})",
            )
        )

    findings.extend(validate_content_revision(path, entry))
    return findings


def apply_provenance_checks(
    repo: Path,
    base: str,
    changes: Iterable[Change],
    provenance: dict[str, dict[str, Any]],
) -> list[Finding]:
    findings: list[Finding] = []
    changed_paths: set[str] = set()

    for change in changes:
        path = change.after_path or change.before_path
        assert path is not None
        changed_paths.add(path)
        entry = provenance.get(path)
        if entry is None:
            findings.append(
                Finding(
                    "error",
                    "missing-provenance",
                    path,
                    "strict sync mode requires provenance for every changed source guide",
                )
            )
            continue

        expected = None if change.status == "A" else revision_blob(repo, base, change.before_path or path)
        findings.extend(validate_provenance_entry(path, entry, expected))

    # A no-op candidate may legitimately repair stale platform sync state.  It is
    # safe only when the rendered worktree already equals the current repo blob.
    for path, entry in provenance.items():
        if path in changed_paths:
            continue
        current_blob = revision_blob(repo, base, path)
        if current_blob is None:
            findings.append(
                Finding(
                    "error",
                    "provenance-path-missing",
                    path,
                    "provenance names a path absent from both the base and rendered changes",
                )
            )
            continue
        provided_blob = entry.get("expected_repo_blob", "<missing>")
        if provided_blob == current_blob:
            findings.extend(validate_content_revision(path, entry))
        elif provided_blob != "<missing>":
            candidate_blob = worktree_blob(repo, path)
            if candidate_blob == current_blob:
                findings.extend(validate_content_revision(path, entry))
                findings.append(
                    Finding(
                        "notice",
                        "idempotent-state-repair",
                        path,
                        "rendered content already equals the repository; sync state may adopt "
                        f"blob {current_blob}",
                    )
                )
            else:
                findings.extend(validate_provenance_entry(path, entry, current_blob))
        else:
            findings.extend(validate_provenance_entry(path, entry, current_blob))

    return findings



REVIEWER_METADATA_KEYS = ("reviewed_by", "verified_by", "review_status")


def _is_reviewer_metadata_only_change(before_text, after_text):
    """True when the only difference between two guide revisions is the value or
    presence of the governed reviewer-metadata frontmatter keys, with the body
    byte-identical. Used to allow the sync bot's privacy edits (name withheld /
    name stripped) without opening the door to unattributed content changes."""
    if before_text is None or after_text is None:
        return False

    def split_doc(text):
        if not text.startswith("---"):
            return None, text
        end = text.find("\n---", 3)
        if end < 0:
            return None, text
        return text[3:end], text[end + 4 :]

    fm_before, body_before = split_doc(before_text)
    fm_after, body_after = split_doc(after_text)
    if fm_before is None or fm_after is None:
        return False
    if body_before != body_after:
        return False

    def strip_governed(fm):
        kept = []
        for line in fm.splitlines():
            key = line.split(":", 1)[0].strip().lower() if ":" in line else ""
            if key in REVIEWER_METADATA_KEYS:
                continue
            kept.append(line)
        return "\n".join(kept)

    if strip_governed(fm_before) != strip_governed(fm_after):
        return False
    # The governed lines must actually differ, or this is a no-op commit that
    # should never have been flagged in the first place (still fine to allow).
    return True


def bot_authorship_findings(repo: Path, base: str, head: str) -> list[Finding]:
    findings: list[Finding] = []
    commits = filter(None, git_text(repo, "rev-list", "--reverse", f"{base}..{head}").splitlines())
    for commit in commits:
        identity = git_text(repo, "show", "-s", "--format=%an%x00%ae", commit).rstrip("\n")
        name, _, email = identity.partition("\0")
        if name not in SYNC_BOT_NAMES and email not in SYNC_BOT_EMAILS:
            continue

        raw_changes = git_text(
            repo,
            "diff-tree",
            "--root",
            "--no-commit-id",
            "--name-status",
            "-z",
            "-r",
            "--find-renames",
            commit,
            "--",
            "skills/**/*.md",
            "skills/*.md",
        )
        for change in parse_name_status(raw_changes):
            if change.status == "A":
                continue
            before_text = (
                read_revision_file(repo, f"{commit}^", change.before_path)
                if change.before_path is not None
                else None
            )
            after_text = (
                read_revision_file(repo, commit, change.after_path)
                if change.after_path is not None
                else None
            )
            if not is_guide_document(before_text) and not is_guide_document(after_text):
                continue
            # Reviewer-privacy exemption (maintainer decision, 2026-08-21). The sync
            # bot is ALLOWED to change the governed reviewer-metadata keys without a
            # CAS preflight: when an accountant hides their public profile, the bot
            # must strip or withhold their name here, and there is no human actor to
            # attribute that edit to. The exemption is deliberately narrow — the
            # commit's per-file change must be confined to the reviewer keys
            # (reviewed_by / verified_by / review_status) with the BODY untouched.
            # Anything more still requires the preflight and still goes red.
            if _is_reviewer_metadata_only_change(before_text, after_text):
                findings.append(
                    Finding(
                        "notice",
                        "bot-reviewer-metadata-update",
                        change.display_path,
                        f"sync bot commit {commit[:12]} updated reviewer-privacy metadata only "
                        "(reviewed_by/verified_by/review_status); body unchanged — allowed",
                    )
                )
                continue
            findings.append(
                Finding(
                    "error",
                    "aggregate-bot-source-write",
                    change.display_path,
                    f"aggregate sync bot authored commit {commit[:12]} that changed an existing "
                    "source guide; accountant-attributed edits require a successful CAS preflight",
                )
            )
    return findings


def run_integrity_check(
    repo: Path,
    base: str,
    head: str | None,
    mode: str,
    provenance: dict[str, dict[str, Any]] | None = None,
    strict_metadata: bool = False,
) -> tuple[list[Finding], int]:
    changes = changed_guides(repo, base, head)
    findings: list[Finding] = []
    guide_changes: list[Change] = []

    for change in changes:
        before_text = (
            read_revision_file(repo, base, change.before_path)
            if change.before_path is not None
            else None
        )
        after_text = (
            read_revision_file(repo, head, change.after_path)
            if head is not None and change.after_path is not None
            else read_worktree_file(repo, change.after_path)
            if change.after_path is not None
            else None
        )
        before_is_guide = is_guide_document(before_text)
        after_is_guide = is_guide_document(after_text)
        if not before_is_guide and not after_is_guide:
            continue

        guide_changes.append(change)
        if change.status in {"D", "R"} or (before_is_guide and not after_is_guide):
            severity = "error" if mode == "sync" or strict_metadata else "warning"
            findings.append(
                Finding(
                    severity,
                    "source-removal-needs-review",
                    change.display_path,
                    "source-guide deletion or rename requires an explicit human-reviewed migration",
                )
            )
            continue

        path = change.after_path
        assert path is not None

        if after_text is None:
            findings.append(
                Finding("error", "candidate-missing", path, "candidate source guide cannot be read")
            )
        elif not before_is_guide:
            findings.extend(validate_new_guide(path, after_text))
        else:
            assert before_text is not None
            findings.extend(
                compare_existing_guides(
                    path,
                    before_text,
                    after_text,
                    mode,
                    strict_metadata=strict_metadata,
                )
            )

    if mode == "sync":
        if provenance is None:
            findings.append(
                Finding(
                    "error",
                    "provenance-required",
                    "<sync>",
                    "strict sync mode requires --provenance with per-guide CAS tokens",
                )
            )
        else:
            findings.extend(apply_provenance_checks(repo, base, guide_changes, provenance))
    elif head is not None:
        findings.extend(bot_authorship_findings(repo, base, head))

    order = {"error": 0, "warning": 1, "notice": 2}
    findings.sort(key=lambda item: (order.get(item.severity, 9), item.path, item.code))
    return findings, len(guide_changes)


def annotation_escape(value: str, property_value: bool = False) -> str:
    escaped = value.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
    if property_value:
        escaped = escaped.replace(":", "%3A").replace(",", "%2C")
    return escaped


def print_finding(finding: Finding) -> None:
    if os.environ.get("GITHUB_ACTIONS") == "true":
        command = "error" if finding.severity == "error" else "warning" if finding.severity == "warning" else "notice"
        path = annotation_escape(finding.path, property_value=True)
        message = annotation_escape(f"[{finding.code}] {finding.message}")
        print(f"::{command} file={path}::{message}")
    else:
        print(f"{finding.severity.upper():7} {finding.path}: [{finding.code}] {finding.message}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd(), help="repository path")
    parser.add_argument("--base", required=True, help="base Git revision")
    target = parser.add_mutually_exclusive_group()
    target.add_argument("--head", default=None, help="candidate Git revision (default: HEAD)")
    target.add_argument(
        "--worktree",
        action="store_true",
        help="compare the rendered working tree, including untracked guides",
    )
    parser.add_argument("--mode", choices=("audit", "sync"), default="audit")
    parser.add_argument(
        "--strict-metadata",
        action="store_true",
        help="fail body changes that advance neither last_updated nor version",
    )
    parser.add_argument(
        "--provenance",
        type=Path,
        help="JSON file containing expected_repo_blob and content_revision per path",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.mode == "sync" and not args.worktree:
        parser.error("--mode sync requires --worktree so it can guard a pre-push render")
    if args.provenance is not None and args.mode != "sync":
        parser.error("--provenance is only valid with --mode sync")

    try:
        repo = repository_root(args.repo.resolve())
        head = None if args.worktree else (args.head or "HEAD")
        git_text(repo, "rev-parse", "--verify", f"{args.base}^{{commit}}")
        if head is not None:
            git_text(repo, "rev-parse", "--verify", f"{head}^{{commit}}")
        provenance = load_provenance(args.provenance.resolve()) if args.provenance else None
        findings, change_count = run_integrity_check(
            repo=repo,
            base=args.base,
            head=head,
            mode=args.mode,
            provenance=provenance,
            strict_metadata=args.strict_metadata,
        )
    except IntegrityError as exc:
        print(f"sync-integrity invocation failed: {exc}", file=sys.stderr)
        return 2

    for finding in findings:
        print_finding(finding)

    errors = sum(item.severity == "error" for item in findings)
    warnings = sum(item.severity == "warning" for item in findings)
    notices = sum(item.severity == "notice" for item in findings)
    print(
        f"Sync integrity checked {change_count} source guide(s): "
        f"{errors} error(s), {warnings} warning(s), {notices} notice(s)."
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
