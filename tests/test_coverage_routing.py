import importlib.util
import os
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))


def load_script(name, filename):
    spec = importlib.util.spec_from_file_location(
        name, os.path.join(HERE, "..", "scripts", filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


cr = load_script("coverage_report", "coverage-report.py")
oci = load_script("open_coverage_issues", "open-coverage-issues.py")


class TexasCoverageRoutingTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.texas = next(row for row in cr.build_report()["rows"]
                         if row["code"] == "US-TX")

    def test_report_routes_texas_to_state_pack(self):
        self.assertEqual(self.texas["dir"], "skills/us-states/tx")
        self.assertTrue(os.path.isfile(os.path.join(
            cr.REPO_ROOT, self.texas["dir"], "README.md")))

    def test_issue_body_points_contributors_to_texas_pack_readme(self):
        body = oci.body_for(self.texas)
        self.assertIn("Pack: `skills/us-states/tx`", body)
        self.assertIn("`skills/us-states/tx/README.md`", body)
        self.assertNotIn("skills/orchestrator", body)


if __name__ == "__main__":
    unittest.main()
