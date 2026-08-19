"""Regression tests for a corpus the server cannot read.

Dropping the container to an unprivileged UID (the USER line in the Dockerfile)
makes EACCES reachable on an operator-supplied packages path. Path.is_dir() and
Path.rglob() both swallow PermissionError, so an unreadable corpus used to
produce the same empty catalogue as a correct one, pinned for the life of the
process by lru_cache(maxsize=1), where the former root process returned the
full corpus.

Permissions are simulated rather than chmod-ed so the tests mean the same thing
on every platform the server is developed on.
"""

from __future__ import annotations

import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from openaccountants_mcp import server


SKILL = """---
name: probe-skill
jurisdiction: XX
category: international
tier: 2
---

# Probe

Body.
"""


class UnreadableCorpusTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.packages = Path(self._tmp.name) / "packages"
        (self.packages / "xx").mkdir(parents=True)
        (self.packages / "xx" / "probe.md").write_text(SKILL, encoding="utf-8")
        self.addCleanup(server._index.cache_clear)
        patcher = mock.patch.object(server, "PACKAGES_DIR", self.packages)
        patcher.start()
        self.addCleanup(patcher.stop)
        server._index.cache_clear()

    def test_a_readable_corpus_still_indexes(self) -> None:
        self.assertIn("probe-skill", server._index())

    def test_an_absent_corpus_is_named_as_absent(self) -> None:
        with mock.patch.object(server, "PACKAGES_DIR", self.packages / "missing"):
            server._index.cache_clear()
            with self.assertRaisesRegex(RuntimeError, "No skill corpus at"):
                server._index()

    def test_an_unreadable_corpus_root_is_reported_not_emptied(self) -> None:
        with mock.patch.object(server.os, "stat", side_effect=PermissionError(13, "denied")):
            server._index.cache_clear()
            with self.assertRaisesRegex(RuntimeError, "not accessible to this process"):
                server._index()

    def test_a_corpus_root_without_read_permission_is_reported(self) -> None:
        with mock.patch.object(server.os, "access", return_value=False):
            server._index.cache_clear()
            with self.assertRaisesRegex(RuntimeError, "not readable by this process"):
                server._index()

    def test_all_files_denied_is_reported_not_an_empty_catalogue(self) -> None:
        def denied(self_path, *args, **kwargs):
            raise PermissionError(13, "Permission denied")

        with mock.patch.object(Path, "read_text", denied):
            server._index.cache_clear()
            with self.assertRaisesRegex(RuntimeError, "permission denied"):
                server._index()

    def test_the_failure_is_not_cached(self) -> None:
        """lru_cache does not store exceptions, so a fixed mount recovers
        without restarting the process."""
        with mock.patch.object(server.os, "access", return_value=False):
            server._index.cache_clear()
            with self.assertRaises(RuntimeError):
                server._index()

        self.assertIn("probe-skill", server._index())


if __name__ == "__main__":
    unittest.main()
