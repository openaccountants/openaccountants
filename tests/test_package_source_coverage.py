"""Real source skills must survive the package builder's old fixed routing list."""

import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from skill_dependencies import catalogue, read_skill  # noqa: E402

spec = importlib.util.spec_from_file_location("coverage_package_builder", ROOT / "scripts/build-packages.py")
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


def document(name, jurisdiction="GLOBAL", dependencies=(), body="Rule instructions."):
    dep = "depends_on:\n" + "".join(f"  - {d}\n" for d in dependencies) if dependencies else ""
    return f"---\nname: {name}\njurisdiction: {jurisdiction}\n{dep}---\n\n# {name}\n\n{body}\n"


class PackageSourceCoverageTests(unittest.TestCase):
    def test_consolidated_law_is_not_a_redirect(self):
        for rel in (
            "azerbaijan/az-company-formation.md",
            "bermuda/bm-corporate-income-tax.md",
            "georgia/ge-tax-overview.md",
            "reunion/re-octroi-producer-registration-and-returns.md",
        ):
            with self.subTest(path=rel):
                self.assertFalse(builder._is_redirect(str(ROOT / "skills" / rel)))

    def test_only_an_explicit_document_heading_is_a_redirect(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "stub.md"
            path.write_text("# Redirect\n\nMoved to another file.\n")
            self.assertTrue(builder._is_redirect(str(path)))
            path.write_text(document("example", body="Read the consolidated Act."))
            self.assertFalse(builder._is_redirect(str(path)))

    def test_unrouted_standards_and_nested_corridors_ship_with_exact_identity(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            def write(path, text):
                target = root / path
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(text)
                return target
            standard = write("skills/global/reporting/topic.md", document("reporting-topic", dependencies=["method"]))
            method = write("skills/global/methods/method.md", document("method"))
            corridor_a = write("skills/global/cross-border/eg-ae/dtt-summary.md", document("eg-ae-corridor", "EG-AE"))
            corridor_b = write("skills/global/cross-border/eg-sa/dtt-summary.md", document("eg-sa-corridor", "EG-SA"))
            write("skills/global/cross-border/_templates/dtt-template.md", document("dtt-template"))
            write("skills/global/reporting/references.md", document("references"))
            write("evidence/quarantine/held.md", document("held-treaty", "EG-AE"))
            manual = write("packages/us-federal/manual.md", document("manual", "US"))
            manual_before = manual.read_bytes()
            _skills, targets, errors = catalogue(root)
            self.assertEqual(errors, [])
            with patch.object(builder, "PACKAGES_DIR", str(root / "packages")), \
                 patch.object(builder, "dependency_targets", return_value=targets):
                builder.include_unshipped_sources()
            packaged = {s.name: s for p in (root / "packages").rglob("*.md") if (s := read_skill(p))}
            self.assertEqual(set(packaged), set(targets))
            for source in (standard, method, corridor_a, corridor_b):
                skill = read_skill(source)
                self.assertEqual(packaged[skill.name].path.read_bytes(), source.read_bytes())
                self.assertEqual(packaged[skill.name].jurisdiction, skill.jurisdiction)
            self.assertEqual(manual.read_bytes(), manual_before)
            self.assertNotIn("dtt-template", packaged)
            self.assertNotIn("references", packaged)
            self.assertNotIn("held-treaty", packaged)

    def test_existing_wrong_copy_fails_instead_of_silently_claiming_coverage(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / "skills/example/tax.md"
            source.parent.mkdir(parents=True)
            source.write_text(document("tax", "GA"))
            package = root / "packages/example/tax.md"
            package.parent.mkdir(parents=True)
            package.write_text(document("tax", "US-GA"))
            with patch.object(builder, "PACKAGES_DIR", str(root / "packages")), \
                 patch.object(builder, "dependency_targets", return_value=catalogue(root)[1]):
                with self.assertRaisesRegex(ValueError, "source guidance and metadata"):
                    builder.include_unshipped_sources()

    def test_same_body_with_different_prerequisites_does_not_claim_coverage(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / "skills/example/tax.md"
            source.parent.mkdir(parents=True)
            source.write_text(document("tax", dependencies=["method"]))
            (source.parent / "method.md").write_text(document("method"))
            package = root / "packages/example/tax.md"
            package.parent.mkdir(parents=True)
            package.write_text(document("tax"))
            with patch.object(builder, "PACKAGES_DIR", str(root / "packages")), \
                 patch.object(builder, "dependency_targets", return_value=catalogue(root)[1]):
                with self.assertRaisesRegex(ValueError, "source guidance and metadata"):
                    builder.include_unshipped_sources()


if __name__ == "__main__":
    unittest.main()
