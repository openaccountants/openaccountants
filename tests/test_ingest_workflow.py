"""Exercise the ingestion shell with the file-free Actions push payload."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import unittest

import yaml


@unittest.skipUnless(shutil.which("bash") and shutil.which("jq"), "requires bash and jq")
class IngestWorkflowTests(unittest.TestCase):
    def run_workflow(self, api_failure=False):
        workflow = Path(__file__).resolve().parents[1] / ".github/workflows/ingest-to-platform.yml"
        script = yaml.safe_load(workflow.read_text(encoding="utf-8"))["jobs"]["ring"]["steps"][0]["run"]
        commits = [
            {"id": "human", "author": {"name": "Contributor", "email": "person@example.test", "username": "contributor"}},
            {"id": "bot", "author": {"name": "Sync", "email": "sync@openaccountants.com"}},
        ]
        pages = [
            {"files": [{"filename": "skills/example.md", "status": "modified"},
                       {"filename": "skills/removed.md", "status": "removed"},
                       {"filename": "README.md", "status": "modified"}]},
            {"files": [{"filename": "skills/example.md", "status": "modified"},
                       {"filename": "skills/new.md", "status": "added"},
                       {"filename": "skills/renamed.md", "status": "renamed"}]},
        ]
        # Stub only network boundaries. Run the workflow's Bash and jq unchanged.
        stubs = r'''
        gh() {
          [ "$API_FAILURE" = "0" ] || return 1
          [ "$3" = "repos/example/guides/commits/human" ] || return 2
          printf '%s\n' "$API_PAGES" | jq "$5"
        }
        curl() {
          out=/dev/stdout; fmt=""; body=""
          while [ "$#" -gt 0 ]; do
            case "$1" in
              -o) out="$2"; shift ;;
              -w) fmt="$2"; shift ;;
              -d) body="$2"; shift ;;
            esac
            shift
          done
          [ -n "$body" ] || return 3
          printf 'CAPTURED_BODY=%s\n' "$body" >&2
          printf '{}' > "$out"
          [ -z "$fmt" ] || printf '200'
        }
        '''
        if os.name == "nt":
            # Match the Ubuntu runner's LF output when using native Windows jq.
            stubs = 'jq() { command jq --binary "$@"; }\n' + stubs
        env = {**os.environ, "SECRET": "synthetic-test-value", "PAYLOAD": json.dumps(commits),
               "HEAD_SHA": "head", "GITHUB_REPOSITORY": "example/guides",
               "API_PAGES": "\n".join(json.dumps(page) for page in pages),
               "API_FAILURE": "1" if api_failure else "0"}
        return subprocess.run([shutil.which("bash"), "--noprofile", "--norc"],
                              input=stubs + script, env=env, text=True, capture_output=True)

    def test_human_commit_without_file_attributes_reaches_platform(self):
        result = self.run_workflow()
        self.assertEqual(result.returncode, 0, result.stderr)
        bodies = [line.removeprefix("CAPTURED_BODY=") for line in result.stderr.splitlines()
                  if line.startswith("CAPTURED_BODY=")]
        self.assertEqual(len(bodies), 1, result.stdout)
        body = json.loads(bodies[0])
        self.assertEqual(body["headSha"], "head")
        self.assertEqual(body["paths"], ["skills/example.md", "skills/new.md", "skills/renamed.md"])

    def test_commit_lookup_failure_does_not_send_partial_ingestion(self):
        result = self.run_workflow(api_failure=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn("CAPTURED_BODY=", result.stderr)


if __name__ == "__main__":
    unittest.main()
