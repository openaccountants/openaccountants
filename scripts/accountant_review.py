#!/usr/bin/env python3
"""Approvals an accountant gives signed in on openaccountants.com.

An accountant reviews a skill claim by claim on the website: every figure,
method step and worked example, each marked right or wrong with a fix. The
website keeps that review as a record. This repository then needs two things:

1. ``stage``: the accountant-review workflow (.github/workflows/accountant-review.yml)
   reads submitted reviews from the website (GET /api/reviews/pending, with the
   REVIEW_PROOF_SECRET bearer token) and stages one change per review: the skill
   file with `tier: 1`, `reviewed_by`, `reviewed_on` and the accountant's fixes.
   It stages a review only if main still holds the exact file the accountant
   reviewed, and only if the new file hashes to the hash the review approved.
   A later step, which runs no code from this repository, commits and opens the
   pull request.

2. ``check_pull_request`` (called by scripts/validate-guides.py): a pull request
   from a branch ``accountant-review/<id>``, or labelled ``accountant-review``,
   passes only if the website's signed proof for that review
   (GET /api/reviews/<id>/proof, HMAC-SHA256 under REVIEW_PROOF_SECRET) names the
   one skill file the PR changes, the name in its `reviewed_by`, the date in its
   `reviewed_on`, the file the PR started from and the file it carries.

This is what lets "an AI commit under a person's identity does not establish
approval" stay true: the commit here is the bot's; the approval is the signed
review record. The message format must match src/lib/review/proof.ts on the
website.
"""

from __future__ import annotations

import argparse
import hashlib
import hmac
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import urllib.error
import urllib.request

SITE = os.environ.get("OA_SITE", "https://www.openaccountants.com")
PROOF_VERSION = "oa-review-proof-v1"
BRANCH_PREFIX = "accountant-review/"
LABEL = "accountant-review"
FIELDS = ("id", "slug", "github_path", "reviewer_name", "reviewed_on",
          "file_sha", "result_sha", "submitted_at", "status")
LIVE_STATES = {"submitted", "pr_open", "merged", "live"}
UUID = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")
SHA = re.compile(r"^[0-9a-f]{40}$")
SKILL_PATH = re.compile(r"^skills/[A-Za-z0-9._/-]+\.md$")
REPO_ROOT = Path(__file__).resolve().parents[1]


def blob_sha(data: bytes) -> str:
    """Git's blob SHA-1, what GitHub reports as a file's sha."""
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def proof_message(proof: dict) -> str:
    return "\n".join([PROOF_VERSION, *(str(proof.get(f, "")) for f in FIELDS)])


def signature_ok(proof: dict, secret: str) -> bool:
    sig = str(proof.get("signature", ""))
    if not secret or not re.fullmatch(r"[0-9a-f]{64}", sig):
        return False
    want = hmac.new(secret.encode(), proof_message(proof).encode("utf-8"), hashlib.sha256).hexdigest()
    return hmac.compare_digest(want, sig)


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None  # never send the bearer token to another host


def get_json(url: str, token: str | None = None) -> dict:
    headers = {"Accept": "application/json", "User-Agent": "openaccountants-accountant-review"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.build_opener(NoRedirect()).open(request, timeout=30) as response:
        data = json.load(response)
    if not isinstance(data, dict):
        raise ValueError("the website's reply is not an object")
    return data


def frontmatter_value(text: str, key: str) -> str:
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        return ""
    v = re.search(rf"^{key}:[ \t]*(.*?)[ \t]*$", m.group(1), re.M)
    return v.group(1).strip().strip("\"'") if v else ""


def review_id_for(head_ref: str, labels: list[str], body: str) -> str | None:
    """The review record a PR claims: its branch name first, else its body."""
    if head_ref.startswith(BRANCH_PREFIX):
        return head_ref[len(BRANCH_PREFIX):]
    if LABEL in labels:
        m = re.search(r"Review record: `([0-9a-f-]{36})`", body or "")
        return m.group(1) if m else ""
    return None


def problems_for(proof: dict, *, review_id: str, changed: list[str], base_text: bytes | None,
                 main_text: bytes | None, head_text: bytes | None, secret: str) -> list[str]:
    """Why a PR does not match its review record. Empty list = it matches. Pure."""
    if not signature_ok(proof, secret):
        return ["the website's proof is not signed with REVIEW_PROOF_SECRET (or the secret is not set)"]
    out = []
    if proof.get("id") != review_id:
        out.append("the proof is for a different review record")
    if proof.get("status") not in LIVE_STATES:
        out.append(f"the review record is {proof.get('status')!r}, not an open review")
    path = proof.get("github_path", "")
    if changed != [path]:
        out.append(f"the PR must change exactly {path}; it changes {', '.join(changed) or 'nothing'}")
        return out
    if head_text is None:
        return out + [f"{path} is missing from the PR"]
    head = head_text.decode("utf-8", errors="replace")
    if frontmatter_value(head, "tier") != "1":
        out.append("`tier` must be 1")
    if frontmatter_value(head, "reviewed_by") != proof.get("reviewer_name"):
        out.append(f"`reviewed_by` must be exactly {proof.get('reviewer_name')!r}, the name on the review record")
    if frontmatter_value(head, "reviewed_on") != proof.get("reviewed_on"):
        out.append(f"`reviewed_on` must be {proof.get('reviewed_on')}, the day of the review")
    if base_text is None or blob_sha(base_text) != proof.get("file_sha"):
        out.append("the PR did not start from the file the accountant reviewed")
    if main_text is None or blob_sha(main_text) != proof.get("file_sha"):
        out.append("main has changed this file since the review; the accountant must review the new version")
    if blob_sha(head_text) != proof.get("result_sha"):
        out.append("the file in the PR is not the file the accountant approved (one character is enough)")
    return out


def _git_show(ref: str, path: str) -> bytes | None:
    try:
        return subprocess.run(["git", "show", f"{ref}:{path}"], cwd=REPO_ROOT,
                              capture_output=True, check=True).stdout
    except Exception:
        return None


def _event() -> dict | None:
    path = os.environ.get("GITHUB_EVENT_PATH")
    if not path or not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as fh:
        return json.load(fh).get("pull_request")


def check_pull_request(errors: list[str], changed: list[str] | None, pr: dict | None = None,
                       fetch=get_json, show=_git_show) -> None:
    """validate-guides.py line 12. Adds an ERROR for an accountant-review PR that does
    not match its signed review record. Any other PR is untouched."""
    pr = _event() if pr is None else pr
    if not pr:
        return
    head_ref = (pr.get("head") or {}).get("ref", "") or ""
    labels = [l.get("name", "") for l in pr.get("labels") or []]
    review_id = review_id_for(head_ref, labels, pr.get("body") or "")
    if review_id is None:
        return
    if not UUID.match(review_id):
        errors.append("accountant review: the branch or body names no review record id")
        return
    try:
        proof = fetch(f"{SITE}/api/reviews/{review_id}/proof")
    except (urllib.error.URLError, TimeoutError, ValueError) as error:
        errors.append(f"accountant review: the proof for {review_id} could not be read from the website ({error})")
        return
    changed = sorted(changed or [])
    path = proof.get("github_path", "")
    base = subprocess.run(["git", "merge-base", "origin/main", "HEAD"], cwd=REPO_ROOT,
                          capture_output=True, text=True).stdout.strip() or "origin/main"
    found = problems_for(
        proof, review_id=review_id, changed=changed,
        base_text=show(base, path) if SKILL_PATH.match(path) else None,
        main_text=show("origin/main", path) if SKILL_PATH.match(path) else None,
        head_text=show("HEAD", path) if SKILL_PATH.match(path) else None,
        secret=os.environ.get("REVIEW_PROOF_SECRET", ""),
    )
    errors.extend(f"accountant review {review_id}: {p}" for p in found)


def stage(out_dir: Path, fetch=get_json, show=_git_show) -> list[dict]:
    """Write one folder per review that can become a PR now: file, title, body.
    Skips (and reports) any review whose file moved on main or whose content does
    not hash to the approved result. Never writes into the repository."""
    secret = os.environ.get("REVIEW_PROOF_SECRET", "")
    if not secret:
        raise ValueError("REVIEW_PROOF_SECRET is not configured")
    reply = fetch(f"{SITE}/api/reviews/pending", token=secret)
    reviews = reply.get("reviews")
    if not isinstance(reviews, list):
        raise ValueError("the website returned no review list")
    staged = []
    out_dir.mkdir(parents=True, exist_ok=True)
    for review in reviews:
        rid = str(review.get("id", ""))
        path = str(review.get("path", ""))
        content = review.get("content")
        if not UUID.match(rid) or not SKILL_PATH.match(path) or ".." in path or not isinstance(content, str):
            print(json.dumps({"message": "Skipped a malformed review", "id": rid}))
            continue
        if review.get("branch") != f"{BRANCH_PREFIX}{rid}" or not SHA.match(str(review.get("file_sha"))) or not SHA.match(str(review.get("result_sha"))):
            print(json.dumps({"message": "Skipped a malformed review", "id": rid}))
            continue
        # The workflow checks out main, so HEAD is main as it is now.
        current = show("HEAD", path)
        if current is None or blob_sha(current) != review["file_sha"]:
            print(json.dumps({"message": "Skipped: main changed the file after the review", "id": rid, "path": path}))
            continue
        data = content.encode("utf-8")
        if blob_sha(data) != review["result_sha"]:
            print(json.dumps({"message": "Skipped: the file does not hash to the approved result", "id": rid}))
            continue
        folder = out_dir / rid
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "file").write_bytes(data)
        (folder / "path").write_text(path, encoding="utf-8")
        (folder / "title").write_text(str(review.get("title", f"Accountant review {rid}"))[:250], encoding="utf-8")
        (folder / "body.md").write_text(str(review.get("body", "")), encoding="utf-8")
        staged.append({"id": rid, "path": path})
        print(json.dumps({"message": "Staged", "id": rid, "path": path}))
    return staged


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)
    s = sub.add_parser("stage", help="stage submitted reviews as files for the PR step")
    s.add_argument("--out", required=True, type=Path)
    args = parser.parse_args(argv)
    if args.command == "stage":
        stage(args.out)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, urllib.error.URLError, TimeoutError) as error:
        print(json.dumps({"message": "Stage failed", "error": str(error)}))
        raise SystemExit(1)
