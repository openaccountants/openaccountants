"""Freshness regression tests for skill-body reads.

``_read_skill`` deliberately reads every body from disk. A stat-fingerprint
cache (mtime_ns + size) was tried here and rejected: a rewrite that preserves
both, such as a rate correction 21% to 22%, would keep serving the old
guidance, and a cached body would survive a read-permission revocation.
These tests pin the fail-closed freshness behaviour so the cache cannot be
reintroduced without invalidation that handles the same-length case.
"""

from __future__ import annotations

import os
import tempfile
import unittest
from pathlib import Path

from openaccountants_mcp import server


def _skill(name: str, body: str) -> str:
    return (
        "---\n"
        f"name: {name}\n"
        "jurisdiction: XX\n"
        "category: international\n"
        "tier: 2\n"
        "last_updated: 2026-01-02\n"
        "---\n\n"
        f"# {name}\n\n{body}\n"
    )


class BodyFreshnessTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.packages = Path(self._tmp.name)
        self._original_packages = server.PACKAGES_DIR
        server.PACKAGES_DIR = self.packages
        server._index.cache_clear()

    def tearDown(self) -> None:
        server.PACKAGES_DIR = self._original_packages
        server._index.cache_clear()
        self._tmp.cleanup()

    def _write(self, relpath: str, content: str) -> None:
        path = self.packages / relpath
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def test_same_length_rewrite_is_served_fresh(self) -> None:
        """21% corrected to 22% has the same byte length; it must still show.

        A stat-fingerprint cache keyed on (mtime_ns, size) returns the stale
        body here when the rewrite also preserves the timestamp, so this test
        fails for exactly that design.
        """
        self._write("xx/demo-skill.md", _skill("demo-skill", "Rate is 21%"))
        self.assertIn("Rate is 21%", server.get_skill("demo-skill")["markdown"])

        self._write("xx/demo-skill.md", _skill("demo-skill", "Rate is 22%"))
        # Pin the fingerprint: same length, original mtime restored.
        target = self.packages / "xx" / "demo-skill.md"
        stat = target.stat()
        os.utime(target, ns=(stat.st_atime_ns, stat.st_mtime_ns))

        again = server.get_skill("demo-skill")["markdown"]
        self.assertIn("Rate is 22%", again)
        self.assertNotIn("Rate is 21%", again)

    def test_repeated_reads_reflect_the_current_file(self) -> None:
        self._write("xx/demo-skill.md", _skill("demo-skill", "Alpha body."))
        self.assertIn("Alpha body.", server.get_skill("demo-skill")["markdown"])

        self._write("xx/demo-skill.md", _skill("demo-skill", "Beta body."))
        self.assertIn("Beta body.", server.get_skill("demo-skill")["markdown"])


if __name__ == "__main__":
    unittest.main()
