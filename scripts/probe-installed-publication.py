"""Prove installed-wheel eligibility against the complete source graph."""

import argparse
import json
from pathlib import Path
import sys

parser = argparse.ArgumentParser()
mode = parser.add_mutually_exclusive_group(required=True)
mode.add_argument("--write-expected", type=Path)
mode.add_argument("--check", type=Path)
args = parser.parse_args()

if args.write_expected:
    # Only this branch imports repository code. The installed probe below must
    # run outside the checkout, without inserting a source package path.
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from skill_dependencies import publication_catalogue

    root = Path(__file__).resolve().parents[1]
    _all, targets, held, errors = publication_catalogue(root)
    assert not errors, errors
    standards = [name for name, skill in targets.items()
                 if json.loads(skill.context).get("domain") == "financial-reporting"]
    assert standards, "The non-tax standards population must not disappear"
    args.write_expected.write_text(json.dumps({
        "usable": sorted(targets), "held": held,
        "positive_reads": ["workflow-base", sorted(standards)[0]],
    }, indent=2) + "\n")
else:
    from openaccountants_mcp import server

    expected = json.loads(args.check.read_text())
    assert server.PACKAGES_DIR.is_relative_to(server._MODULE_DIR), server.PACKAGES_DIR
    actual = {row["slug"] for row in server.list_skills()["skills"]}
    assert actual == set(expected["usable"]), {
        "missing": sorted(set(expected["usable"]) - actual),
        "extra": sorted(actual - set(expected["usable"])),
    }
    for name in expected["held"]:
        for read in (server.get_skill, server.get_skill_sections):
            try:
                read(name)
            except server.ToolInputError:
                pass
            else:
                raise AssertionError(f"Installed wheel served held guidance: {name}")
    for name in expected["positive_reads"]:
        assert server.get_skill(name)["markdown"]
    print(f"Installed wheel: {len(actual)} usable names; {len(expected['held'])} holds enforced; "
          "workflow and non-tax standard remain readable")
