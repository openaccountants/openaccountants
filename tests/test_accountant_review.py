"""scripts/accountant_review.py: an approval given signed in on openaccountants.com.

The website signs a proof for each review (src/lib/review/proof.ts). These tests pin
the shared message format with a cross-language vector, and show that a PR passes
only when it matches its review record exactly.
"""

from __future__ import annotations

import hashlib
import hmac
import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))
spec = importlib.util.spec_from_file_location("accountant_review", REPO_ROOT / "scripts" / "accountant_review.py")
ar = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ar)

SECRET = "s3cret"
ID = "22222222-2222-4222-8222-222222222222"
PATH = "skills/malta/mt-freelance-intake.md"
BEFORE = b"---\nname: x\ntier: 2\n---\n\n# X\n\n| 18% | Standard |\n"
AFTER = b'---\nname: x\ntier: 1\nreviewed_by: "Maria Borg"\nreviewed_on: 2026-11-12\n---\n\n# X\n\n| 18% | Standard |\n'


def signed(**over):
    proof = {
        "id": ID, "slug": "mt-freelance-intake", "github_path": PATH, "reviewer_name": "Maria Borg",
        "reviewed_on": "2026-11-12", "file_sha": ar.blob_sha(BEFORE), "result_sha": ar.blob_sha(AFTER),
        "submitted_at": "2026-11-12T10:00:00.000Z", "status": "pr_open",
    }
    proof.update(over)
    proof["signature"] = hmac.new(SECRET.encode(), ar.proof_message(proof).encode(), hashlib.sha256).hexdigest()
    return proof


def problems(proof, *, changed=None, base=BEFORE, main=BEFORE, head=AFTER, secret=SECRET):
    return ar.problems_for(proof, review_id=ID, changed=[PATH] if changed is None else changed,
                           base_text=base, main_text=main, head_text=head, secret=secret)


class SignatureTests(unittest.TestCase):
    def test_matches_the_website_vector(self):
        # Same vector as src/lib/review/__tests__/proof.test.ts on the website.
        proof = {"id": ID, "slug": "mt-freelance-intake", "github_path": PATH, "reviewer_name": "Maria Borg",
                 "reviewed_on": "2026-11-12", "file_sha": "a" * 40, "result_sha": "b" * 40,
                 "submitted_at": "2026-11-12T10:00:00.000Z", "status": "submitted",
                 "signature": "96d9ac1665a96ec9372b329dc8ebe4dcfbf36f1b8757f39e169b9b9e2e812514"}
        self.assertTrue(ar.signature_ok(proof, SECRET))
        self.assertFalse(ar.signature_ok({**proof, "reviewer_name": "Someone Else"}, SECRET))
        self.assertFalse(ar.signature_ok(proof, "other"))
        self.assertFalse(ar.signature_ok(proof, ""))

    def test_blob_sha_is_gits(self):
        self.assertEqual(ar.blob_sha(b""), "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391")
        try:
            git = subprocess.run(["git", "hash-object", "--stdin"], input=AFTER, capture_output=True, check=True).stdout.decode().strip()
        except Exception:
            return
        self.assertEqual(ar.blob_sha(AFTER), git)


class PullRequestMatchTests(unittest.TestCase):
    def test_a_pr_that_matches_its_review_passes(self):
        self.assertEqual(problems(signed()), [])

    def test_a_forged_or_unsigned_proof_fails(self):
        forged = signed()
        forged["reviewer_name"] = "Someone Else"
        self.assertIn("not signed", problems(forged)[0])
        self.assertIn("not signed", problems(signed(), secret="")[0])

    def test_one_changed_character_fails(self):
        self.assertTrue(any("not the file the accountant approved" in p for p in problems(signed(), head=AFTER.replace(b"18%", b"19%"))))

    def test_another_name_or_date_fails(self):
        head = AFTER.replace(b"Maria Borg", b"Mario Borg")
        found = problems(signed(result_sha=ar.blob_sha(head)), head=head)
        self.assertTrue(any("`reviewed_by` must be exactly 'Maria Borg'" in p for p in found))
        head = AFTER.replace(b"2026-11-12", b"2026-11-13")
        self.assertTrue(any("`reviewed_on`" in p for p in problems(signed(result_sha=ar.blob_sha(head)), head=head)))

    def test_a_pr_from_another_starting_file_or_with_main_moved_fails(self):
        self.assertTrue(any("did not start from" in p for p in problems(signed(), base=b"other")))
        self.assertTrue(any("main has changed" in p for p in problems(signed(), main=b"other")))

    def test_the_pr_must_change_exactly_the_reviewed_file(self):
        found = problems(signed(), changed=[PATH, "skills/malta/other.md"])
        self.assertTrue(any("must change exactly" in p for p in found))
        self.assertTrue(any("must change exactly" in p for p in problems(signed(), changed=[])))

    def test_a_stale_record_fails(self):
        self.assertTrue(any("not an open review" in p for p in problems(signed(status="stale"))))


class CheckPullRequestTests(unittest.TestCase):
    def run_check(self, pr, proof=None, fail=False):
        errors = []
        def fetch(url, token=None):
            if fail:
                raise ValueError("down")
            self.assertEqual(url, f"https://www.openaccountants.com/api/reviews/{ID}/proof")
            return proof or signed()
        files = {("HEAD", PATH): AFTER, ("origin/main", PATH): BEFORE}
        show = lambda ref, path: files.get(("HEAD" if ref == "HEAD" else "origin/main", path))
        import os
        old = os.environ.get("REVIEW_PROOF_SECRET")
        os.environ["REVIEW_PROOF_SECRET"] = SECRET
        try:
            ar.check_pull_request(errors, [PATH], pr=pr, fetch=fetch, show=show)
        finally:
            if old is None:
                os.environ.pop("REVIEW_PROOF_SECRET", None)
            else:
                os.environ["REVIEW_PROOF_SECRET"] = old
        return errors

    def test_ordinary_prs_are_not_touched(self):
        self.assertEqual(self.run_check({"head": {"ref": "fix-malta"}, "labels": [], "body": ""}, fail=True), [])

    def test_review_branch_passes_with_a_matching_proof(self):
        self.assertEqual(self.run_check({"head": {"ref": f"accountant-review/{ID}"}, "labels": [], "body": ""}), [])

    def test_label_with_record_in_body_is_checked_too(self):
        pr = {"head": {"ref": "other"}, "labels": [{"name": "accountant-review"}], "body": f"Review record: `{ID}`"}
        self.assertEqual(self.run_check(pr), [])
        self.assertTrue(self.run_check({**pr, "body": "no id"}))

    def test_fails_closed_when_the_website_cannot_be_read(self):
        errors = self.run_check({"head": {"ref": f"accountant-review/{ID}"}, "labels": [], "body": ""}, fail=True)
        self.assertTrue(errors and "could not be read" in errors[0])


class StageTests(unittest.TestCase):
    def test_stages_only_reviews_whose_file_is_unchanged_and_whose_result_hashes(self):
        good = {"id": ID, "path": PATH, "branch": f"accountant-review/{ID}", "file_sha": ar.blob_sha(BEFORE),
                "result_sha": ar.blob_sha(AFTER), "content": AFTER.decode(), "title": "Approve X", "body": "Body"}
        moved = {**good, "id": "33333333-3333-4333-8333-333333333333", "branch": "accountant-review/33333333-3333-4333-8333-333333333333", "file_sha": "c" * 40}
        tampered = {**good, "id": "44444444-4444-4444-8444-444444444444", "branch": "accountant-review/44444444-4444-4444-8444-444444444444", "content": "changed"}
        escape = {**good, "id": "55555555-5555-4555-8555-555555555555", "branch": "accountant-review/55555555-5555-4555-8555-555555555555", "path": "skills/../.github/workflows/x.md"}
        import os
        os.environ["REVIEW_PROOF_SECRET"] = SECRET
        try:
            with tempfile.TemporaryDirectory() as tmp:
                out = Path(tmp)
                staged = ar.stage(out, fetch=lambda url, token=None: {"reviews": [good, moved, tampered, escape]},
                                  show=lambda ref, path: BEFORE if path == PATH else None)
                self.assertEqual([s["id"] for s in staged], [ID])
                self.assertEqual((out / ID / "file").read_bytes(), AFTER)
                self.assertEqual((out / ID / "path").read_text(), PATH)
        finally:
            os.environ.pop("REVIEW_PROOF_SECRET", None)

    def test_refuses_to_run_without_the_secret(self):
        import os
        os.environ.pop("REVIEW_PROOF_SECRET", None)
        with self.assertRaises(ValueError):
            ar.stage(Path(tempfile.mkdtemp()), fetch=lambda url, token=None: {"reviews": []})


if __name__ == "__main__":
    unittest.main()
