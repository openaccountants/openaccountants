"""Safety withdrawal is not permission to publish oversized changed guidance."""
import builtins
import contextlib
import gzip
import hashlib
import importlib.util
import io
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
spec = importlib.util.spec_from_file_location("protective_hold_validator", ROOT / "scripts/validate-guides.py")
vg = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vg)

REL = "skills/malta/fictional-vat.md"
OLD = ("---\nname: fictional-vat\ndescription: A complete fictional input fixture, never legal guidance.\n"
       "jurisdiction: MT\ntier: 2\nlast_updated: 2026-11-12\n"
       "---\n\n# Fictional source\n" + "Unchanged fictional guidance.\n" * 4500)
HELD = OLD.replace("name: fictional-vat\n", "name: fictional-vat\nstatus: needs_sources\n", 1)


class ProtectiveHold(unittest.TestCase):
    def check(self, old, new, rel=REL):
        def prior(*args, **kwargs):
            if old is None:
                raise subprocess.CalledProcessError(128, "git show")
            return SimpleNamespace(stdout=old if kwargs.get("text") else old.encode())

        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / rel
            source.parent.mkdir(parents=True)
            source.write_bytes(new if isinstance(new, bytes) else new.encode())
            errors, warnings = [], []
            with patch.object(vg, "REPO_ROOT", directory), patch.object(vg.subprocess, "run", side_effect=prior):
                vg.check_deliverable(errors, warnings, [rel])
            return errors, warnings

    def test_only_new_protective_flag_can_pass_the_existing_oversize_gate(self):
        self.assertGreater(len(OLD.encode()), vg.PLATFORM_MAX_SKILL_BYTES)
        self.assertEqual(self.check(OLD, HELD), ([], []))
        prior_status = OLD.replace("tier: 2", "status: draft\ntier: 2")
        self.assertEqual(self.check(prior_status, prior_status.replace("status: draft", "status: needs_sources")), ([], []))

    def test_new_missing_or_unreadable_base_does_not_get_an_exemption(self):
        self.assertTrue(any("bytes" in e for e in self.check(None, HELD)[0]))
        malformed = OLD.replace("tier: 2", "tier: 2\ntier: 1")
        self.assertTrue(any("bytes" in e for e in self.check(malformed, HELD)[0]))

    def test_hold_removal_and_already_held_edits_still_fail(self):
        for old, new in ((HELD, OLD), (HELD, HELD), (HELD, HELD + "More guidance.\n")):
            with self.subTest(new=new[-40:]):
                self.assertTrue(any("bytes" in e for e in self.check(old, new)[0]))
        self.assertTrue(any("bytes" in e for e in self.check(HELD.replace("needs_sources", '"NEEDS_SOURCES"'), HELD)[0]))

    def test_invalid_utf8_cannot_equal_a_replacement_character_after_decoding(self):
        old = OLD.replace("# Fictional source", "# Fictional source \ufffd")
        held = old.replace("name: fictional-vat\n", "name: fictional-vat\nstatus: needs_sources\n")
        self.assertTrue(any("bytes" in e for e in self.check(old, held.encode().replace(b"\xef\xbf\xbd", b"\xff"))[0]))

    def test_raw_body_changes_are_not_hidden_by_legacy_label_or_whitespace_normalization(self):
        for new in (HELD + "More guidance.\n", HELD.rstrip("\n"), HELD.replace("# Fictional source", "# Different source"),
                    HELD + "> Contributed by Fictional person.\n", HELD.replace("\n# Fictional source", "\n\n# Fictional source"),
                    HELD.replace("\n", "\r\n")):
            with self.subTest(ending=repr(new[-40:])):
                self.assertTrue(any("bytes" in e for e in self.check(OLD, new)[0]))

    def test_every_other_metadata_field_stays_unchanged(self):
        for new in (HELD.replace("tier: 2", "tier: 1"), HELD.replace("jurisdiction: MT", "jurisdiction: IE"),
                    HELD.replace("name: fictional-vat", "name: another-vat"),
                    HELD.replace("description: A complete", "description: A revised"),
                    HELD.replace("2026-11-12", "2026-11-13"),
                    HELD.replace("tier: 2", "depends_on: [another-skill]\ntier: 2"),
                    HELD.replace("tier: 2", "reviewed_by: Fictional person\ntier: 2")):
            with self.subTest(metadata=new.split("---", 2)[1]):
                self.assertTrue(any("bytes" in e for e in self.check(OLD, new)[0]))

    def test_status_aliases_and_ambiguous_yaml_cannot_hide_other_metadata_changes(self):
        old = OLD.replace("tier: 2", "status: &state draft\ncustom: *state\ntier: 2")
        new = old.replace("&state draft", "&state needs_sources")
        for prior, current in ((old, new), (OLD, HELD.replace("tier: 2", "status: draft\ntier: 2")),
                               (OLD, HELD.replace("status:", "source_status:"))):
            self.assertTrue(any("bytes" in e for e in self.check(prior, current)[0]))

    def test_the_exception_does_not_hide_other_deliverability_failures(self):
        old = OLD.replace("A complete fictional input fixture, never legal guidance.", "Short")
        new = old.replace("name: fictional-vat\n", "name: fictional-vat\nstatus: needs_sources\n")
        errors, _ = self.check(old, new, "skills/malta/Bad Name.md")
        self.assertTrue(any("description" in e for e in errors))
        self.assertTrue(any("lowercase" in e for e in errors))
        self.assertFalse(any("bytes" in e for e in errors))

    def test_exact_historical_za_flag_passes_actual_validator_main_with_legacy_warnings(self):
        rel = "skills/south-africa/za-vat-return.md"
        # Preserve the real pre-hold bytes without depending on clone depth or
        # today's main, which now correctly contains the protective flag.
        old_bytes = gzip.decompress((Path(__file__).parent / "fixtures" / "za-vat-return-before-source-hold.md.gz").read_bytes())
        self.assertEqual(hashlib.sha256(old_bytes).hexdigest(),
                         "2bc2ed41aebf88283c5ce284420e4452a9dd251c397a3d65b5a4622b6c998fce")
        old = old_bytes.decode("utf-8")
        new = old.replace("name: za-vat-return\n", "name: za-vat-return\nstatus: needs_sources\n", 1)
        original_open, original_size, original_bytes = builtins.open, vg.os.path.getsize, Path.read_bytes
        original_run = vg.subprocess.run

        def historical_base(args, *positional, **kwargs):
            if list(args) == ["git", "show", f"origin/main:{rel}"]:
                return SimpleNamespace(stdout=old if kwargs.get("text") else old_bytes,
                                       stderr="" if kwargs.get("text") else b"", returncode=0)
            return original_run(args, *positional, **kwargs)

        def read(file, *args, **kwargs):
            if str(file) == str(ROOT / rel):
                return io.StringIO(new)
            return original_open(file, *args, **kwargs)

        def size(file):
            return len(new.encode()) if str(file) == str(ROOT / rel) else original_size(file)

        def raw(file):
            return new.encode() if str(file) == str(ROOT / rel) else original_bytes(file)

        log = io.StringIO()
        with patch.object(vg, "added_or_edited_vs_main", return_value=[rel]), \
             patch.object(vg, "changed_files_vs_main", return_value=[rel]), \
             patch.object(vg.subprocess, "run", side_effect=historical_base), \
             patch.object(builtins, "open", side_effect=read), patch.object(vg.os.path, "getsize", side_effect=size), \
             patch.object(Path, "read_bytes", raw), \
             patch.object(sys, "argv", ["validate-guides.py", "--changed-only", "--no-index-check"]), \
             contextlib.redirect_stdout(log):
            vg.main()
        self.assertNotIn("ERROR:", log.getvalue())
        self.assertIn("rates_rows_sourced", log.getvalue())
        self.assertIn("canonical_headings", log.getvalue())
        self.assertIn("validation passed", log.getvalue())


if __name__ == "__main__":
    unittest.main()
