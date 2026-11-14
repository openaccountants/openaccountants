import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from professional_numbers import new_professional_numbers, professional_numbers


class ProfessionalNumberTests(unittest.TestCase):
    def test_identifiers_in_credit_and_explicit_labels(self):
        for text in (
            "> Contributed by Anthony Bandura, AL-10921.",
            "Michael Cutajar, CPA · Warrant No. 125122",
            "Approved by Jane Doe (CPA No. AB-12345)",
            "> Verified by Jane Doe (8907) on 2026-06-12.",
            "> Verified by Jane Doe (CRC-SP 312052/O-1) on 2026-06-12.",
            'reviewed_by: "Jane Doe, licence no. 12345"',
        ):
            with self.subTest(text=text):
                self.assertTrue(professional_numbers(text))

    def test_tax_figures_dates_sources_and_software_licences_are_not_numbers(self):
        text = ("Form 990, $200,000, 21%, §40-18-1.\nBusiness licence fee $100; software license: AGPL-3.0-only.\n"
                "Warrant requirement: Accountancy Profession Act, Cap. 281.\n"
                "Source: https://www.irs.gov/pub/irs-pdf/i990.pdf, read 2026-11-13.\n"
                "> Approved by Jane Doe on 2026-06-12 for Form 990.")
        self.assertFalse(professional_numbers(text))

    def test_existing_approved_source_can_stay_but_new_or_duplicated_ids_fail(self):
        old = (ROOT / "skills/us/federal/990-returns.md").read_text()
        self.assertTrue(professional_numbers(old))
        self.assertFalse(new_professional_numbers(old, old))
        self.assertTrue(new_professional_numbers(old + "\n> Contributed by Jane Doe, AL-12345.", old))
        self.assertTrue(new_professional_numbers(old + "\n> Contributed by Anthony Bandura, AL-10921.", old))

    def test_validator_enforces_new_numbers_and_keeps_backlog_advisory(self):
        spec = importlib.util.spec_from_file_location("validate_numbers", ROOT / "scripts/validate-guides.py")
        validator = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(validator)
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp, "skills/us/test.md")
            path.parent.mkdir(parents=True)
            path.write_text("> Contributed by Jane Doe, AL-12345.")
            with patch.object(validator, "REPO_ROOT", tmp):
                errors, warnings = [], []
                validator.check_professional_numbers(errors, warnings, ["skills/us/test.md"], lambda _: "# Older text")
                self.assertEqual(len(errors), 1)
                errors.clear()
                validator.check_professional_numbers(errors, warnings, ["skills/us/test.md"], lambda _: path.read_text())
                self.assertEqual(errors, [])
                validator.check_professional_numbers(errors, warnings)
                self.assertEqual(errors, [])
                self.assertEqual(len(warnings), 1)

    def test_shallow_checkout_needs_history_only_when_source_contains_identifiers(self):
        spec = importlib.util.spec_from_file_location("validate_shallow_numbers", ROOT / "scripts/validate-guides.py")
        validator = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(validator)
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp, "skills/us/test.md")
            path.parent.mkdir(parents=True)
            path.write_text("# Fictional skill\nApproved by Jane Doe.\n")
            with patch.object(validator, "REPO_ROOT", tmp), \
                 patch.object(validator.subprocess, "run", return_value=subprocess.CompletedProcess([], 128, "", "missing history")) as git:
                errors, warnings = [], []
                validator.check_professional_numbers(errors, warnings, ["skills/us/test.md"])
                self.assertEqual((errors, warnings), ([], []))
                git.assert_not_called()
                path.write_text("> Contributed by Jane Doe, AL-12345.\n")
                validator.check_professional_numbers(errors, warnings, ["skills/us/test.md"])
                self.assertEqual(len(errors), 1)
                self.assertIn("cannot confirm base", errors[0])


if __name__ == "__main__":
    unittest.main()
