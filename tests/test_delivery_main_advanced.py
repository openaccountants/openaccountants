"""A batch refused because main moved on is not retried (14 Nov 2026)."""
import importlib.util
import io
import sys
import unittest
import urllib.error
from pathlib import Path
from unittest import mock

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
spec = importlib.util.spec_from_file_location("deliver_main_advanced", SCRIPTS / "deliver-to-platform.py")
deliver = importlib.util.module_from_spec(spec)
sys.modules["deliver_main_advanced"] = deliver
spec.loader.exec_module(deliver)


def http_error(code: int, body: str) -> urllib.error.HTTPError:
    return urllib.error.HTTPError("https://example.invalid", code, "x", {}, io.BytesIO(body.encode()))


class MainAdvancedTests(unittest.TestCase):
    batch = {"headSha": "a" * 40, "paths": ["skills/x/y.md"], "authors": []}

    def test_main_moved_on_stops_without_retrying(self):
        refusal = '{"error": "Source commit is not confirmed as current main; retry from the latest main"}'
        with mock.patch.object(deliver, "post", side_effect=http_error(503, refusal)) as post, \
                mock.patch.object(deliver.time, "sleep") as sleep:
            with self.assertRaises(deliver.MainAdvanced):
                deliver.send_batch(self.batch, "secret")
        self.assertEqual(post.call_count, 1)
        sleep.assert_not_called()

    def test_a_busy_platform_is_still_retried(self):
        with mock.patch.object(deliver, "post", side_effect=[http_error(503, "busy"), {"ok": True}]) as post, \
                mock.patch.object(deliver.time, "sleep"):
            self.assertEqual(deliver.send_batch(self.batch, "secret"), {"ok": True})
        self.assertEqual(post.call_count, 2)


if __name__ == "__main__":
    unittest.main()
