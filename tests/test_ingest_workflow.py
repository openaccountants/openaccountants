"""Exercise real Git collection and the workflow entry point, with HTTP stubbed."""
from contextlib import redirect_stdout
from datetime import datetime, timedelta, timezone
import importlib.util
import io
import json
import os
from pathlib import Path
import shlex
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
import urllib.error

import yaml

ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "scripts/deliver-to-platform.py"
spec = importlib.util.spec_from_file_location("delivery_runner", RUNNER)
delivery = importlib.util.module_from_spec(spec)
spec.loader.exec_module(delivery)


class GitFixture:
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name) / "repo"
        self.repo.mkdir()
        self.git("init", "--initial-branch=main")
        self.git("config", "user.name", "Fixture Maintainer")
        self.git("config", "user.email", "maintainer@example.test")
        self.git("config", "commit.gpgsign", "false")
        hooks = self.repo / ".git/empty-hooks"
        hooks.mkdir()
        self.git("config", "core.hooksPath", str(hooks))
        (self.repo / "scripts").mkdir()
        shutil.copyfile(RUNNER, self.repo / "scripts/deliver-to-platform.py")
        self.base = self.commit({"README.md": "Fixture only"}, "Setup", "setup@example.test")

    def git(self, *args, env=None):
        return subprocess.check_output(["git", "-C", str(self.repo), *args],
                                       env=env, encoding="utf-8", stderr=subprocess.PIPE).strip()

    def commit(self, files, name="Alice Writer", email="alice@example.test", committer=None, date=None):
        for path, text in files.items():
            target = self.repo / path
            target.parent.mkdir(parents=True, exist_ok=True)
            if text is None:
                target.unlink()
            else:
                target.write_text(text, encoding="utf-8")
        self.git("add", "-A")
        env = {**os.environ, "GIT_AUTHOR_NAME": name, "GIT_AUTHOR_EMAIL": email,
               "GIT_COMMITTER_NAME": name, "GIT_COMMITTER_EMAIL": committer or email}
        if date:
            env.update(GIT_AUTHOR_DATE=date, GIT_COMMITTER_DATE=date)
        self.git("commit", "-m", "Fictional test fixture", env=env)
        return self.git("rev-parse", "HEAD")

    def plan(self, since=None, head="HEAD"):
        return delivery.collect_batches(self.repo, since or self.base, head)


@unittest.skipUnless(shutil.which("git") and shutil.which("bash"), "requires git and bash")
class IngestWorkflowTests(GitFixture, unittest.TestCase):
    def run_workflow(self, api_failure=False, event="push", stale_event_head=False):
        self.commit({"skills/mt/example.md": "old", "skills/mt/removed.md": "old",
                     "skills/mt/old-name.md": "old"})
        since = self.git("rev-parse", "HEAD")
        self.git("mv", "skills/mt/old-name.md", "skills/mt/renamed.md")
        self.commit({"skills/mt/example.md": "changed", "skills/mt/new.md": "new",
                     "skills/mt/removed.md": None, "README.md": "not a skill"})
        head = self.commit({"skills/mt/bot-only.md": "bot"}, "Sync", delivery.SYNC_BOT)
        workflow = yaml.safe_load((ROOT / ".github/workflows/ingest-to-platform.yml").read_text())
        script = workflow["jobs"]["ring"]["steps"][-1]["run"]
        harness = Path(self.temp.name) / "network-boundary.py"
        harness.write_text('''
import importlib.util,json,sys
spec=importlib.util.spec_from_file_location("runner",sys.argv[1])
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
def post(url,body,secret):
    if url==module.PLATFORM:
        print("CAPTURED_BODY="+json.dumps(body),file=sys.stderr)
        return {"ok":True,"accepted":len(body["paths"])}
    if url==module.PLATFORM+"/verify":
        return {"outcomes":[{"path":path,"status":"match"} for path in body["paths"]]}
    raise AssertionError("Unexpected network destination")
module.post=post
raise SystemExit(module.main(sys.argv[2:]))
''')
        # Execute the YAML Bash unchanged. Replace only the Python HTTP boundary;
        # collection still uses the real runner and a real repository.
        shim = "python3() { " + shlex.quote(sys.executable) + " " + shlex.quote(str(harness)) + ' "$@"; }\n'
        env = {**os.environ, "PLATFORM_INGEST_SECRET": "synthetic-test-value",
               "SINCE_SHA": "unreadable-commit" if api_failure else since,
               "HEAD_SHA": since if stale_event_head else head, "DELIVERY_EVENT": event,
               "PAYLOAD": json.dumps([{"id": head, "author": {"name": "Writer"}}])}
        return subprocess.run([shutil.which("bash"), "--noprofile", "--norc"],
                              input=shim + script, cwd=self.repo, env=env,
                              text=True, capture_output=True)

    def test_human_commit_without_file_attributes_reaches_platform(self):
        result = self.run_workflow()
        self.assertEqual(result.returncode, 0, result.stderr)
        bodies = [json.loads(line.removeprefix("CAPTURED_BODY="))
                  for line in result.stderr.splitlines() if line.startswith("CAPTURED_BODY=")]
        self.assertEqual(len(bodies), 1)
        self.assertEqual(bodies[0]["headSha"], self.git("rev-parse", "HEAD"))
        self.assertEqual(bodies[0]["paths"], ["skills/mt/example.md", "skills/mt/new.md", "skills/mt/old-name.md", "skills/mt/removed.md", "skills/mt/renamed.md"])
        self.assertEqual(bodies[0]["deletedPaths"], ["skills/mt/old-name.md", "skills/mt/removed.md"])
        self.assertEqual(bodies[0]["authors"][0]["email"], "alice@example.test")
        self.assertNotIn("synthetic-test-value", result.stdout + result.stderr)

    def test_commit_lookup_failure_does_not_send_partial_ingestion(self):
        result = self.run_workflow(api_failure=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn("CAPTURED_BODY=", result.stderr)

    def test_scheduled_sweep_runs_the_same_real_git_collector(self):
        result = self.run_workflow(api_failure=True, event="schedule")
        self.assertEqual(result.returncode, 0, result.stderr)
        bodies = [json.loads(line.removeprefix("CAPTURED_BODY="))
                  for line in result.stderr.splitlines() if line.startswith("CAPTURED_BODY=")]
        self.assertEqual(bodies[0]["headSha"], self.git("rev-parse", "HEAD"))
        self.assertEqual(bodies[0]["paths"], ["skills/mt/example.md", "skills/mt/new.md", "skills/mt/old-name.md", "skills/mt/removed.md", "skills/mt/renamed.md"])
        self.assertEqual(bodies[0]["deletedPaths"], ["skills/mt/old-name.md", "skills/mt/removed.md"])

    def test_queued_event_uses_the_actual_checkout_head(self):
        result = self.run_workflow(stale_event_head=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        bodies = [json.loads(line.removeprefix("CAPTURED_BODY="))
                  for line in result.stderr.splitlines() if line.startswith("CAPTURED_BODY=")]
        self.assertEqual(bodies[0]["headSha"], self.git("rev-parse", "HEAD"))

    def test_workflow_keeps_secret_scope_and_uses_one_shared_verified_entry(self):
        doc = yaml.safe_load((ROOT / ".github/workflows/ingest-to-platform.yml").read_text())
        self.assertEqual(doc["permissions"], {"contents": "read"})
        self.assertEqual(list(doc["jobs"]), ["ring"])
        job = doc["jobs"]["ring"]
        self.assertEqual(job["environment"], "production")
        self.assertEqual(job["if"], "github.ref == 'refs/heads/main'")
        self.assertEqual(job["steps"][0]["with"]["fetch-depth"], 0)
        self.assertFalse(job["steps"][0]["with"]["persist-credentials"])
        self.assertEqual(job["steps"][0]["with"]["ref"], "main")
        self.assertEqual(doc["concurrency"], {"group": "platform-skill-delivery", "queue": "max"})
        events = doc.get("on", doc.get(True))
        self.assertEqual(events["schedule"], [{"cron": "17 6 * * *"}])
        self.assertIn('--batch-size 20', job["steps"][-1]["run"])
        self.assertIn("--send", job["steps"][-1]["run"])
        self.assertEqual(job["steps"][-1]["env"]["SINCE_SHA"], "${{ github.event.before || inputs.since_sha }}")


class DeliveryPlanTests(GitFixture, unittest.TestCase):
    def old_base(self):
        date = (datetime.now(timezone.utc) - timedelta(days=30)).isoformat()
        self.git("commit", "--amend", "--no-edit", env={**os.environ, "GIT_AUTHOR_DATE": date, "GIT_COMMITTER_DATE": date})
        self.base = self.git("rev-parse", "HEAD")

    def test_scheduled_boundary_uses_main_history_and_keeps_an_older_merged_writer(self):
        self.old_base()
        self.git("checkout", "-b", "writer")
        old = (datetime.now(timezone.utc) - timedelta(days=20)).isoformat()
        self.commit({"skills/mt/older-branch.md": "writer"}, date=old)
        self.git("checkout", "main")
        self.commit({"docs/current.md": "current"})
        self.git("merge", "--no-ff", "writer", "-m", "Merge old writing today")
        since = delivery.lookback_since(self.repo, "HEAD", 7)
        self.assertEqual(since, self.base)
        self.assertEqual(self.plan(since)[0]["paths"], ["skills/mt/older-branch.md"])

    def test_recent_root_is_included_and_invalid_lookback_is_rejected(self):
        self.assertEqual(delivery.lookback_since(self.repo, "HEAD", 7), "0" * 40)
        with self.assertRaises(ValueError):
            delivery.lookback_since(self.repo, "HEAD", 0)

    def test_a_shallow_history_cannot_claim_a_complete_sweep(self):
        self.commit({"skills/mt/recent.md": "fixture"})
        shallow = Path(self.temp.name) / "shallow"
        subprocess.run(["git", "clone", "--depth=1", self.repo.as_uri(), str(shallow)], check=True, capture_output=True)
        with self.assertRaises(ValueError):
            delivery.lookback_since(shallow, "HEAD", 7)
        with self.assertRaises(ValueError):
            delivery.collect_batches(shallow, "0" * 40)

    def test_collection_needs_no_file_blobs_or_network_from_a_full_partial_clone(self):
        self.commit({"skills/mt/recent.md": "fixture"})
        self.git("config", "uploadpack.allowFilter", "true")
        partial = Path(self.temp.name) / "partial"
        subprocess.run(["git", "clone", "--filter=blob:none", "--no-checkout", self.repo.as_uri(), str(partial)], check=True, capture_output=True)
        subprocess.run(["git", "-C", str(partial), "remote", "set-url", "origin", (Path(self.temp.name) / "missing-source").as_uri()], check=True)
        batches = delivery.collect_batches(partial, self.base)
        self.assertEqual(batches[0]["paths"], ["skills/mt/recent.md"])
        self.assertEqual(batches[0]["authors"][0]["email"], "alice@example.test")

    def test_smaller_workflow_batches_preserve_every_path_and_author(self):
        paths = {f"skills/mt/topic-{i:04}.md": "Fictional test" for i in range(2210)}
        self.commit(paths)
        batches = delivery.collect_batches(self.repo, self.base, batch_size=20)
        self.assertEqual(len(batches), 111)
        self.assertEqual(sorted(path for batch in batches for path in batch["paths"]), sorted(paths))
        self.assertTrue(all(len(batch["paths"]) <= 20 and len(batch["authors"]) == 1 for batch in batches))
        for size in (0, -1, 201):
            with self.assertRaises(ValueError):
                delivery.collect_batches(self.repo, self.base, batch_size=size)

    def test_2210_file_change_has_twelve_complete_batches(self):
        paths = {f"skills/mt/topic-{i:04}.md": "Fictional test" for i in range(2210)}
        head = self.commit(paths)
        batches = self.plan()
        self.assertEqual(len(batches), 12)
        self.assertTrue(all(len(batch["paths"]) <= 200 and batch["headSha"] == head for batch in batches))
        delivered = [path for batch in batches for path in batch["paths"]]
        self.assertEqual(sorted(delivered), sorted(paths))
        self.assertEqual(len(set(delivered)), 2210)

    def test_last_human_writer_is_kept_separate_for_each_file(self):
        self.commit({"skills/mt/a.md": "Alice", "skills/mt/shared.md": "Alice"})
        self.commit({"skills/mt/b.md": "Bob", "skills/mt/shared.md": "Bob"}, "Bob Writer", "bob@example.test")
        owners = {path: batch["authors"][0]["email"] for batch in self.plan() for path in batch["paths"]}
        self.assertEqual(owners, {"skills/mt/a.md": "alice@example.test", "skills/mt/b.md": "bob@example.test", "skills/mt/shared.md": "bob@example.test"})
        self.assertTrue(all(len(batch["authors"]) == 1 for batch in self.plan()))

    def test_both_sync_bot_author_and_committer_are_excluded(self):
        self.commit({"skills/mt/human.md": "human"})
        self.commit({"skills/mt/author-bot.md": "bot"}, "Sync", delivery.SYNC_BOT)
        self.commit({"skills/mt/committer-bot.md": "bot"}, committer=delivery.SYNC_BOT)
        self.assertEqual(self.plan()[0]["paths"], ["skills/mt/human.md"])

    def test_removed_skills_are_delivered_but_non_skill_paths_are_not(self):
        self.commit({"skills/mt/removed.md": "old"})
        self.commit({"skills/mt/removed.md": None, "skills/mt/README.md": "index",
                     "skills/mt/references.md": "references", "skills/templates/a.md": "template",
                     "skills/_templates/b.md": "template", "skills/root.md": "index",
                     "skills/mt/real.md": "skill"})
        self.assertEqual(self.plan()[0]["paths"], ["skills/mt/real.md", "skills/mt/removed.md"])
        self.assertEqual(self.plan()[0]["deletedPaths"], ["skills/mt/removed.md"])

    def test_deletion_only_range_still_delivers_a_withdrawal(self):
        before = self.commit({"skills/mt/retired.md": "old"})
        head = self.commit({"skills/mt/retired.md": None})
        self.assertEqual(self.plan(before)[0], {
            "headSha": head, "paths": ["skills/mt/retired.md"],
            "deletedPaths": ["skills/mt/retired.md"],
            "authors": [delivery.author("Alice Writer", "alice@example.test")],
        })

    def test_a_readded_file_is_never_sent_as_a_withdrawal(self):
        self.commit({"skills/mt/readded.md": "old"})
        self.commit({"skills/mt/readded.md": None})
        self.commit({"skills/mt/readded.md": "new"})
        self.assertEqual(self.plan()[0]["paths"], ["skills/mt/readded.md"])
        self.assertNotIn("deletedPaths", self.plan()[0])

    def test_sparse_or_dirty_working_copy_does_not_hide_a_committed_file(self):
        self.commit({"skills/mt/a.md": "skill"})
        (self.repo / "skills/mt/a.md").unlink()
        self.assertEqual(self.plan()[0]["paths"], ["skills/mt/a.md"])

    def test_merge_keeps_writer_and_only_merge_created_files_use_maintainer(self):
        self.git("checkout", "-b", "writer")
        self.commit({"skills/mt/writer.md": "writer"})
        self.git("checkout", "main")
        self.commit({"docs/example.md": "main"}, "Maintainer", "maintainer@example.test")
        self.git("merge", "--no-ff", "--no-commit", "writer")
        self.commit({"skills/mt/merge-only.md": "merge-only"}, "Maintainer", "maintainer@example.test")
        owners = {path: batch["authors"][0]["email"] for batch in self.plan() for path in batch["paths"]}
        self.assertEqual(owners, {"skills/mt/writer.md": "alice@example.test", "skills/mt/merge-only.md": "maintainer@example.test"})

    def test_zero_before_sha_collects_initial_history(self):
        self.commit({"skills/mt/a.md": "skill"})
        self.assertEqual(self.plan("0" * 40)[0]["paths"], ["skills/mt/a.md"])

    def test_unrelated_or_missing_revision_fails_before_network(self):
        self.git("checkout", "--orphan", "unrelated")
        self.commit({"docs/other.md": "new root"})
        with self.assertRaises(subprocess.CalledProcessError):
            self.plan()
        with self.assertRaises(subprocess.CalledProcessError):
            self.plan("missing-revision")

    def test_filenames_are_literal_and_log_values_are_escaped(self):
        path = "skills/mt/a;$(touch SHOULD_NOT_EXIST)\n::error::.md"
        self.commit({path: "skill"})
        self.assertEqual(self.plan()[0]["paths"], [path])
        self.assertFalse((self.repo / "SHOULD_NOT_EXIST").exists())
        output = io.StringIO()
        with redirect_stdout(output):
            delivery.report("Path", path=path)
        self.assertEqual(len(output.getvalue().splitlines()), 1)
        self.assertEqual(json.loads(output.getvalue())["path"], path)

    def test_cli_defaults_to_offline_dry_run(self):
        self.commit({"skills/mt/a.md": "skill"})
        result = subprocess.run([sys.executable, str(RUNNER), "--since", self.base],
                                cwd=self.repo, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(json.loads(result.stdout)["dry_run"])

    def test_noreply_addresses_supply_the_github_login(self):
        self.assertEqual(delivery.author("Writer", "123+writer-name@users.noreply.github.com")["login"], "writer-name")
        self.assertEqual(delivery.author("Writer", "writer-name@users.noreply.github.com")["login"], "writer-name")
        self.assertIsNone(delivery.author("Writer", "writer@example.test")["login"])


class DeliveryVerificationTests(unittest.TestCase):
    def setUp(self):
        self.batch = {"headSha": "a" * 40, "paths": ["skills/mt/a.md"], "authors": [{"name": "Writer", "email": "writer@example.test", "login": None}]}
        self.ack = {"ok": True, "accepted": 1}

    def reply(self, state):
        return {"outcomes": [{"path": self.batch["paths"][0], "status": state}]}

    def run_delivery(self, *replies, attempts=3):
        with mock.patch.object(delivery, "post", side_effect=[self.ack, *replies]) as post, mock.patch.object(delivery.time, "sleep") as sleep, redirect_stdout(io.StringIO()):
            result = delivery.deliver(self.batch, "synthetic-secret", attempts=attempts)
        return result, post, sleep

    def test_only_an_actual_match_is_successful(self):
        for state in ("match",):
            with self.subTest(state=state):
                result, post, sleep = self.run_delivery(self.reply(state))
                self.assertTrue(result)
                self.assertEqual(post.call_count, 2)
                sleep.assert_not_called()

    def test_held_superseded_mismatch_and_failed_do_not_report_delivery(self):
        for state in ("held", "superseded", "mismatch", "failed"):
            with self.subTest(state=state):
                self.assertFalse(self.run_delivery(self.reply(state))[0])

    def test_pending_then_match_polls_without_resending(self):
        result, post, sleep = self.run_delivery(self.reply("pending"), self.reply("match"))
        self.assertTrue(result)
        self.assertEqual([call.args[0] for call in post.call_args_list], [delivery.PLATFORM, delivery.PLATFORM + "/verify", delivery.PLATFORM + "/verify"])
        sleep.assert_called_once_with(2)

    def test_withdrawal_must_be_verified_with_the_same_deleted_paths(self):
        self.batch["deletedPaths"] = self.batch["paths"]
        result, post, _ = self.run_delivery(self.reply("match"))
        self.assertTrue(result)
        self.assertEqual(post.call_args_list[1].args[1]["deletedPaths"], self.batch["deletedPaths"])

    def test_pending_timeout_is_a_failure(self):
        result, _, sleep = self.run_delivery(*[self.reply("pending")] * 3)
        self.assertFalse(result)
        self.assertEqual(sleep.call_args_list, [mock.call(2), mock.call(4)])

    def test_transient_verify_network_error_can_recover(self):
        result, _, sleep = self.run_delivery(urllib.error.URLError("offline"), self.reply("match"))
        self.assertTrue(result)
        sleep.assert_called_once_with(2)

    def test_missing_duplicate_extra_and_unknown_outcomes_fail_closed(self):
        path = self.batch["paths"][0]
        bad = [{}, {"outcomes": []}, {"outcomes": None}, {"outcomes": [None]},
               {"outcomes": [{"path": path, "status": "match"}] * 2},
               {"outcomes": [{"path": "skills/mt/other.md", "status": "match"}]},
               self.reply("unknown"), self.reply([])]
        for reply in bad:
            with self.subTest(reply=reply), self.assertRaises(ValueError):
                self.run_delivery(reply)

    def test_partial_or_malformed_ack_is_rejected(self):
        for ack in ({}, {"ok": True, "accepted": 0}, {"ok": True, "accepted": True}):
            with self.subTest(ack=ack), mock.patch.object(delivery, "post", return_value=ack), self.assertRaises(ValueError):
                delivery.deliver(self.batch, "synthetic-secret")

    def test_one_failed_batch_does_not_drop_independent_batches(self):
        with mock.patch.object(delivery, "collect_batches", return_value=[self.batch, self.batch]), mock.patch.object(delivery, "deliver", side_effect=[ValueError("bad reply"), True]) as send, mock.patch.dict(os.environ, {"PLATFORM_INGEST_SECRET": "synthetic-secret"}), redirect_stdout(io.StringIO()):
            result = delivery.main(["--since", "base", "--send"])
        self.assertEqual(result, 1)
        self.assertEqual(send.call_count, 2)

    def test_missing_secret_prevents_delivery(self):
        with mock.patch.object(delivery, "collect_batches", return_value=[self.batch]), mock.patch.object(delivery, "deliver") as send, mock.patch.dict(os.environ, {"PLATFORM_INGEST_SECRET": ""}), self.assertRaises(ValueError):
            delivery.main(["--since", "base", "--send"])
        send.assert_not_called()

    def test_http_json_must_be_an_object_and_redirects_are_not_followed(self):
        self.assertIsNone(delivery.NoRedirect().redirect_request(None, None, 302, "redirect", {}, "https://elsewhere.example"))
        with mock.patch.object(delivery.urllib.request, "build_opener") as opener:
            opener.return_value.open.return_value = io.BytesIO(b"[]")
            with self.assertRaises(ValueError):
                delivery.post(delivery.PLATFORM, {}, "synthetic-secret")
            request = opener.return_value.open.call_args.args[0]
            self.assertEqual(request.full_url, delivery.PLATFORM)
            self.assertEqual(request.get_header("Authorization"), "Bearer synthetic-secret")


if __name__ == "__main__":
    unittest.main()
