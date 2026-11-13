"""Every startup package must carry the actual method its notice asks to load."""

import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from skill_dependencies import publication_catalogue  # noqa: E402

spec = importlib.util.spec_from_file_location("startup_builder", ROOT / "scripts/build-packages.py")
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


def document(name, jurisdiction="GLOBAL", status="", dependencies=()):
    return (
        f"---\nname: {name}\njurisdiction: {jurisdiction}\n"
        + (f"status: {status}\n" if status else "")
        + ("depends_on:\n" + "".join(f"  - {d}\n" for d in dependencies) if dependencies else "")
        + f"---\n\n# {name}\n\nFictional method or country instructions.\n"
    )


class StartupMethodPackageTests(unittest.TestCase):
    def test_all_three_builders_ship_exact_method_even_without_declared_country_dependency(self):
        for build, args in (("build_package", ("example",)),
                            ("build_us_state_package", ("ca",)),
                            ("build_canada_province_package", ("on",))):
            with self.subTest(builder=build), tempfile.TemporaryDirectory() as temp:
                root = Path(temp)
                skills = root / "skills"
                methods = skills / "global/methods"
                methods.mkdir(parents=True)
                method = methods / "workflow-base.md"
                method.write_text(document("workflow-base", dependencies=["method-evidence"]))
                (methods / "evidence.md").write_text(document("method-evidence"))
                for folder, name, jurisdiction in (("example", "example-tax", "XX"),
                                                   ("us/states/ca", "ca-tax", "US-CA"),
                                                   ("canada/ontario", "on-tax", "CA-ON")):
                    target = skills / folder / f"{name}.md"
                    target.parent.mkdir(parents=True)
                    target.write_text(document(name, jurisdiction))
                targets = publication_catalogue(root)[1]
                with patch.multiple(builder, REPO_ROOT=str(root), SKILLS_DIR=str(skills),
                                    METHODS_DIR=str(methods), PACKAGES_DIR=str(root / "packages"),
                                    US_FEDERAL_DIR=str(skills / "us/federal")), \
                     patch.object(builder, "dependency_targets", return_value=targets):
                    actual_args = (*args, str(skills / "example")) if build == "build_package" else args
                    result = getattr(builder, build)(*actual_args)
                package = root / "packages" / result.get("package_dir", "example")
                self.assertEqual((package / "workflow-base.md").read_bytes(), method.read_bytes())
                self.assertTrue((package / "method-evidence.md").is_file())
                self.assertIn("workflow-base.md", result["files"])
                self.assertIn("`workflow-base.md`", (package / "README.md").read_text())

    def test_missing_or_held_method_refuses_a_startup_package(self):
        for held in (False, True):
            with self.subTest(held=held), tempfile.TemporaryDirectory() as temp:
                root = Path(temp)
                source = root / "skills/example/tax.md"
                source.parent.mkdir(parents=True)
                source.write_text(document("example-tax"))
                if held:
                    (source.parent / "method.md").write_text(document("workflow-base", status="needs_sources"))
                targets = publication_catalogue(root)[1]
                with patch.multiple(builder, SKILLS_DIR=str(root / "skills"),
                                    METHODS_DIR=str(root / "skills/global/methods"),
                                    PACKAGES_DIR=str(root / "packages")), \
                     patch.object(builder, "dependency_targets", return_value=targets):
                    with self.assertRaisesRegex(ValueError, "required startup method.*workflow-base"):
                        builder.build_package("example", str(source.parent))

    def test_conflicting_local_method_is_not_overwritten_or_accepted(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / "skills/global/methods/method.md"
            source.parent.mkdir(parents=True)
            source.write_text(document("workflow-base"))
            (source.parent / "other.md").write_text(document("unrelated-file"))
            package = root / "packages/example"
            package.mkdir(parents=True)
            local = package / "workflow-base.md"
            local.write_text(document("unrelated-file"))
            before = local.read_bytes()
            with patch.object(builder, "dependency_targets", return_value=publication_catalogue(root)[1]):
                with self.assertRaisesRegex(ValueError, "startup method.*conflict"):
                    builder.include_dependencies(str(package), [local.name], required=("workflow-base",))
            self.assertEqual(local.read_bytes(), before)

    def test_notice_routes_to_local_method_and_keeps_useful_outputs_and_notices(self):
        notice = builder.build_foundation()
        self.assertIn("[workflow-base.md](workflow-base.md)", notice)
        for text in ("working paper", "reviewer brief", "action list", "review checklist",
                     "journal", "trial balance", "balance sheet", "payslip", "employer cost",
                     "filing summary", "primary", "code", "supplier", "OpenAccountants",
                     "github.com/openaccountants/openaccountants/issues", "before filing"):
            with self.subTest(topic=text):
                self.assertIn(text, notice)
        for unsafe in ("choose the treatment that costs more", "Conservative default applied",
                       "Process ALL data before", "The reviewer signs off", "Latest verified skills"):
            self.assertNotIn(unsafe, notice)


if __name__ == "__main__":
    unittest.main()
