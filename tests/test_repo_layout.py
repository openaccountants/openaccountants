import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import repo_layout  # noqa: E402


class RepoLayoutTests(unittest.TestCase):
    def test_country_and_topic_paths(self):
        self.assertTrue(repo_layout.is_country_path("skills/malta/malta-vat-return.md"))
        self.assertTrue(repo_layout.is_country_path("skills/us/states/tx/tx-sales-tax.md"))
        self.assertFalse(repo_layout.is_country_path("skills/cross-border/eu-oss-digital.md"))
        self.assertFalse(repo_layout.is_country_path("skills/COUNTRIES.md"))

    def test_topic_folders_are_not_countries(self):
        names = {p.name for p in repo_layout.country_dirs()}
        self.assertIn("malta", names)
        self.assertFalse(names & repo_layout.TOPIC_DIRS)

    def test_only_an_exact_move_with_the_same_filename_is_skipped(self):
        status = (
            "R100\tskills/international/mt/a.md\tskills/mt/a.md\n"
            "R100\tskills/mt/old.md\tskills/mt/new.md\n"
            "R097\tskills/international/mt/b.md\tskills/mt/b.md\n"
            "M\tskills/mt/c.md\n"
        )
        self.assertEqual(repo_layout.pure_moves(status), {"skills/mt/a.md"})


if __name__ == "__main__":
    unittest.main()
