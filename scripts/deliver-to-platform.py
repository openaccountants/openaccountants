#!/usr/bin/env python3
"""Plan GitHub skill delivery offline; --send also ingests and verifies each batch."""

from __future__ import annotations

import argparse
import base64
from datetime import datetime, timedelta, timezone
import json
import os
from pathlib import Path
import re
import subprocess
import time
import urllib.error
import urllib.request
import zlib

PLATFORM = "https://www.openaccountants.com/api/cron/github-ingest"
SYNC_BOT = "sync@openaccountants.com"
BATCH_SIZE = 200
WORK_LIST_MARKER = r"<!-- oa-delivery-work-list-v1:([A-Za-z0-9+/=]+) -->"
WORK_LIST_STATES = {"pending", "held", "mismatch", "failed", "superseded"}


def work_list_body(pending: dict[str, str], head: str) -> str:
    # Compression keeps a full-library write-ahead record below GitHub's issue limit.
    payload = base64.b64encode(zlib.compress(json.dumps(pending, sort_keys=True).encode())).decode()
    counts = {state: list(pending.values()).count(state) for state in sorted(set(pending.values()))}
    lines = ["Persistent platform delivery work list. The workflow owns this record.",
             "Paths stay here until the platform verifies a match against current source.",
             f"\nOutstanding: **{len(pending)}**. Last planned source: `{head}`.",
             f"States: `{json.dumps(counts, sort_keys=True)}`.",
             "\nHeld = needs review; failed/mismatch/pending = needs recovery. See the latest ingest run for details.",
             "\n```json", json.dumps(dict(sorted(pending.items())[:50]), indent=2), "```",
             "\nThe machine record below contains every outstanding path, including any beyond the first 50.",
             f"<!-- oa-delivery-work-list-v1:{payload} -->"]
    body = "\n".join(lines)
    if len(body.encode()) > 65_000:
        raise ValueError("Delivery work list exceeds GitHub's issue limit; no delivery was started")
    return body


def parse_work_list(body: str) -> dict[str, str]:
    markers = re.findall(WORK_LIST_MARKER, body)
    if len(markers) != 1:
        raise ValueError("Delivery work list has no unambiguous machine record")
    try:
        pending = json.loads(zlib.decompress(base64.b64decode(markers[0], validate=True)))
    except (ValueError, zlib.error) as error:
        raise ValueError("Delivery work list is unreadable") from error
    if not isinstance(pending, dict) or any(
        not isinstance(path, str) or not is_skill(path)
        or any(part in {"", ".", ".."} for part in path.split("/"))
        or not isinstance(state, str) or state not in WORK_LIST_STATES
        for path, state in pending.items()
    ):
        raise ValueError("Delivery work list contains an invalid path or state")
    return pending


def issue_api(method: str, payload: dict | None = None) -> dict:
    repo = os.environ.get("GITHUB_REPOSITORY", "")
    issue = os.environ.get("DELIVERY_WORK_LIST_ISSUE", "")
    if repo != "openaccountants/openaccountants" or not issue.isdecimal():
        raise ValueError("Delivery work list repository/issue is not configured")
    command = ["gh", "api", "--method", method, f"repos/{repo}/issues/{issue}"]
    if payload is not None:
        command += ["--input", "-"]
    result = subprocess.run(command, input=json.dumps(payload) if payload is not None else None,
                            text=True, capture_output=True, check=True)
    response = json.loads(result.stdout)
    if not isinstance(response, dict) or response.get("number") != int(issue) or "pull_request" in response:
        raise ValueError("GitHub did not confirm the delivery work list issue")
    return response


def read_work_list() -> dict[str, str]:
    return parse_work_list(issue_api("GET").get("body") or "")


def save_work_list(pending: dict[str, str], head: str) -> None:
    body = work_list_body(pending, head)
    saved = issue_api("PATCH", {"body": body})
    if saved.get("body") != body:
        raise ValueError("GitHub did not confirm the saved delivery work list")


def git(repo: Path, *args: str) -> str:
    return subprocess.check_output(
        ["git", "-C", str(repo), *args], encoding="utf-8", stderr=subprocess.PIPE
    )


def is_skill(path: str) -> bool:
    if not re.fullmatch(r"skills/.+/[^/]+\.md", path):
        return False
    basename = path.rsplit("/", 1)[-1].lower()
    return not (basename.startswith("readme") or basename == "references.md"
                or re.search(r"/_?templates/", path))


def author(name: str, email: str) -> dict:
    match = re.fullmatch(r"(?:\d+\+)?([^@]+)@users\.noreply\.github\.com", email, re.I)
    return {"name": name or None, "email": email or None,
            "login": match[1] if match else None}


def require_full_history(repo: Path) -> None:
    if git(repo, "rev-parse", "--is-shallow-repository").strip() == "true":
        raise ValueError("Full Git history is required; fetch the missing history first")


def lookback_since(repo: Path, head: str, days: int) -> str:
    if days < 1:
        raise ValueError("Lookback days must be positive")
    require_full_history(repo)
    sha = git(repo, "rev-parse", "--verify", "--end-of-options", f"{head}^{{commit}}").strip()
    cutoff = (datetime.now(timezone.utc) - timedelta(days=days)).isoformat()
    # Pick a boundary on main, then include its entire reachable Git range.
    # A branch written earlier but merged recently still belongs to the sweep.
    return git(repo, "rev-list", "--first-parent", "--max-count=1", f"--before={cutoff}", sha, "--").strip() or "0" * 40


def collect_batches(repo: Path, since: str, head: str = "HEAD", batch_size: int = BATCH_SIZE,
                    retry_paths: list[str] | None = None) -> list[dict]:
    if not 1 <= batch_size <= BATCH_SIZE:
        raise ValueError("Batch size must be between 1 and 200")
    require_full_history(repo)
    head_sha = git(repo, "rev-parse", "--verify", "--end-of-options", f"{head}^{{commit}}").strip()
    if re.fullmatch(r"0{40}|0{64}", since):
        revision_range = head_sha
    else:
        since_sha = git(repo, "rev-parse", "--verify", "--end-of-options", f"{since}^{{commit}}").strip()
        subprocess.run(["git", "-C", str(repo), "merge-base", "--is-ancestor", since_sha, head_sha],
                       check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        revision_range = f"{since_sha}..{head_sha}"

    # Read committed trees, never the working copy. A missing source is a
    # withdrawal, not a path to silently drop from the delivery plan.
    present = set(git(repo, "ls-tree", "-r", "--name-only", "-z", head_sha, "--", "skills/").split("\0"))
    owners: dict[str, dict] = {}
    merge_owners: dict[str, dict] = {}
    for sha in git(repo, "rev-list", "--date-order", revision_range).splitlines():
        name, email, committer, parents = git(
            repo, "log", "-1", "--no-notes", "--format=%an%x00%ae%x00%ce%x00%P", sha
        ).rstrip("\n").split("\0")
        if SYNC_BOT in (email.lower(), committer.lower()):
            continue
        person = author(name, email)
        # A conflict-free merge is the maintainer accepting the writer's work.
        # Prefer the writer's non-merge commit; only merge-created files fall
        # back to the merge author, matching the existing backfill policy.
        destination = merge_owners if len(parents.split()) > 1 else owners
        paths = git(repo, "diff-tree", "--root", "-m", "--first-parent", "-r",
                    "--no-commit-id", "--no-renames", "--name-only", "-z",
                    "--diff-filter=ACDMRT", sha, "--", "skills/").split("\0")
        for path in paths:
            if is_skill(path):
                destination.setdefault(path, person)

    for path in retry_paths or []:
        if path in owners or path in merge_owners:
            continue
        # A retry may predate the lookback. Recover today's last human writer
        # from full history; never replay the old body or guess its attribution.
        found = None
        ever = git(repo, "log", "-1", "--format=%H", head_sha, "--", path).strip()
        if not ever:
            # The path never existed on this branch (added and removed inside one
            # pull request before merge): nothing was ever delivered, so there is
            # nothing to retry or withdraw. Skip it rather than block every delivery.
            print(f"Skipping retry of a path that never existed on this branch: {path}")
            continue
        for kind in ("--no-merges", "--merges"):
            records = git(repo, "log", "-z", "--format=%an%x00%ae%x00%ce", kind,
                          "--no-renames", "--diff-filter=ACDMRT", head_sha, "--", path).split("\0")
            for offset in range(0, len(records) - 2, 3):
                name, email, committer = records[offset:offset + 3]
                if SYNC_BOT not in (email.lower(), committer.lower()):
                    found = author(name, email)
                    break
            if found:
                break
        if not found:
            raise ValueError(f"Outstanding path has no confirmed human writer: {path}")
        owners[path] = found

    groups: dict[tuple, dict] = {}
    for path in sorted(owners.keys() | merge_owners.keys()):
        person = owners.get(path) or merge_owners[path]
        key = (person["email"], person["login"], person["name"])
        groups.setdefault(key, {"author": person, "paths": []})["paths"].append(path)
    return [
        {"headSha": head_sha, "paths": batch, "authors": [group["author"]],
         **({"deletedPaths": deleted} if deleted else {})}
        for group in groups.values()
        for offset in range(0, len(group["paths"]), batch_size)
        for batch in [group["paths"][offset:offset + batch_size]]
        for deleted in [[path for path in batch if path not in present]]
    ]


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None  # Never forward the ingestion credential to a redirect.


def post(url: str, body: dict, secret: str) -> dict:
    request = urllib.request.Request(url, data=json.dumps(body).encode(), method="POST",
                                     headers={"Content-Type": "application/json",
                                              "Authorization": f"Bearer {secret}"})
    with urllib.request.build_opener(NoRedirect()).open(request, timeout=300) as response:
        result = json.load(response)
    if not isinstance(result, dict):
        raise ValueError("Platform reply must be an object")
    return result


def report(message: str, **fields) -> None:
    # Filenames/author names can contain newlines or Actions command syntax.
    # JSON escapes those values instead of interpreting them as workflow output.
    print(json.dumps({"message": message, **fields}), flush=True)


def deliver(batch: dict, secret: str, attempts: int = 20, observed: dict | None = None) -> bool:
    acknowledgement = post(PLATFORM, batch, secret)
    accepted = acknowledgement.get("accepted")
    if acknowledgement.get("ok") is not True or type(accepted) is not int or accepted != len(batch["paths"]):
        raise ValueError("Platform did not acknowledge every requested path")

    expected = set(batch["paths"])
    for attempt in range(attempts):
        try:
            verification = {"headSha": batch["headSha"], "paths": batch["paths"]}
            if batch.get("deletedPaths"):
                verification["deletedPaths"] = batch["deletedPaths"]
            reply = post(PLATFORM + "/verify", verification, secret)
            outcomes = reply.get("outcomes")
            if not isinstance(outcomes, list) or any(not isinstance(row, dict) for row in outcomes):
                raise ValueError("Verification omitted its outcomes")
            paths = [row.get("path") for row in outcomes]
            if len(paths) != len(expected) or any(not isinstance(path, str) for path in paths) or set(paths) != expected:
                raise ValueError("Verification did not cover exactly the requested paths")
            states = [row.get("status") for row in outcomes]
            if any(not isinstance(state, str) or state not in {"match", "superseded", "pending", "held", "mismatch", "failed"} for state in states):
                raise ValueError("Verification returned an unknown state")
            if observed is not None:
                observed.update({row["path"]: row["status"] for row in outcomes})
            if "pending" not in states:
                for row in outcomes:
                    report("Verified path", path=row["path"], status=row["status"])
                # A held proposal needs action; it is not a delivered skill.
                return all(state == "match" for state in states)
        except (urllib.error.URLError, TimeoutError) as error:
            report("Verification request failed", error=str(error))
        if attempt + 1 < attempts:
            time.sleep(min(2 ** (attempt + 1), 30))
    report("Verification did not settle", paths=batch["paths"])
    return False


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--since", help="Last delivered commit; excluded from the range")
    source.add_argument("--lookback-days", type=int, help="Sweep changes merged within this many days")
    parser.add_argument("--head", default="HEAD", help="Commit to deliver, default HEAD")
    parser.add_argument("--batch-size", type=int, default=BATCH_SIZE, help="Paths per writer batch, at most 200")
    parser.add_argument("--send", action="store_true", help="Send the complete plan and verify each batch")
    parser.add_argument("--work-list", action="store_true", help="Retain every unresolved path in the configured GitHub issue")
    args = parser.parse_args(argv)
    # Finish all Git reads before sending anything. An unreadable commit must
    # never cause partial delivery, and event payload file arrays are not needed.
    repo = Path.cwd()
    since = args.since if args.since is not None else lookback_since(repo, args.head, args.lookback_days)
    pending = read_work_list() if args.work_list else {}
    batches = collect_batches(repo, since, args.head, args.batch_size, list(pending))
    if not args.send:
        print(json.dumps({"dry_run": True, "batches": batches}, indent=2))
        return 0
    if not batches:
        report("No human-edited skill files in this range")
        return 0
    secret = os.environ.get("PLATFORM_INGEST_SECRET", "")
    if not secret:
        raise ValueError("PLATFORM_INGEST_SECRET is not configured")
    if args.work_list:
        # Write ahead: a timeout/crash must not erase either new work or retries.
        for batch in batches:
            for path in batch["paths"]:
                pending.setdefault(path, "pending")
        save_work_list(pending, batches[0]["headSha"])
    failed = 0
    for number, batch in enumerate(batches, 1):
        report("Delivering batch", number=number, total=len(batches), paths=len(batch["paths"]))
        observed: dict[str, str] = {}
        try:
            if not deliver(batch, secret, observed=observed):
                failed += 1
        except (urllib.error.URLError, TimeoutError, ValueError) as error:
            report("Batch failed", number=number, error=str(error))
            failed += 1
        if args.work_list:
            for path in batch["paths"]:
                state = observed.get(path, "failed")
                if state == "match":
                    pending.pop(path, None)
                else:
                    pending[path] = state
            save_work_list(pending, batch["headSha"])
    report("Delivery finished", batches=len(batches), failed=failed)
    return 1 if failed else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (subprocess.CalledProcessError, ValueError) as error:
        report("Delivery could not start", error=str(error))
        raise SystemExit(1)
