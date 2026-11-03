"""Independent frozen-pack metadata, integrity, arithmetic and scoped checks."""
from pathlib import Path
import hashlib
import importlib.util
import json
import math
import re
import subprocess
import sys
import yaml

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
BASE = "aec6ba04066bb69d1168c8028ba11dd65cb90505"
FREEZE = "0c5d4df4fbf8b4ff9696178f6383fe03cf80024b"
sys.path.insert(0, str(ROOT / "scripts"))
lines = []
def log(value):
    lines.append(str(value))
    print(value)

assert subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT).decode().strip() == FREEZE
files = sorted((ROOT / "skills/togo").glob("tg-*.md"))
platform = {"review_status", "license", "authored_by", "trust_label", "drafted_by", "approved_by", "validation_status", "validated", "verified_by", "reviewed_by"}
cases = 0
for p in files:
    text = p.read_text()
    fm = yaml.safe_load(text.split("---", 2)[1])
    words = len(fm["description"].split())
    assert 80 <= words <= 150
    assert fm["tier"] == 2 and fm["tax_year"] == 2026 and fm["jurisdiction"] == "TG"
    assert float(fm["version"]) == 1.0
    assert re.search(r"^# .+ v1\.0$", text, re.M)
    assert "**General reference only.** This skill is general tax/accounting reference material" in text
    rel = str(p.relative_to(ROOT))
    old = subprocess.run(["git", "show", BASE + ":" + rel], cwd=ROOT, capture_output=True)
    if old.returncode == 0:
        previous = old.stdout.decode()
        previous_fm = yaml.safe_load(previous.split("---", 2)[1])
        assert {k: fm[k] for k in platform if k in fm} == {k: previous_fm[k] for k in platform if k in previous_fm}
        marker = "<!-- openaccountants-cta-block -->"
        assert text[text.index(marker):] == previous[previous.index(marker):]
        assert len(text) >= len(previous) * .75
        integrity = "old platform keys / entire CTA exact"
    else:
        assert not (set(fm) & platform)
        assert "<!-- openaccountants-cta-block -->" not in text
        integrity = "new; no platform/trust/attribution keys or copied CTA"
    log(f"{p.name}: {words} description words; metadata/title/notice PASS; {integrity}; sha256 {hashlib.sha256(p.read_bytes()).hexdigest()}")
    for block in re.findall(r"```oa-check\n(.*?)```", text, re.S):
        data = yaml.safe_load(block)
        values = dict(data["inputs"])
        values.update(floor=math.floor, min=min, max=max)
        for step in data["steps"]:
            for key, expression in step.items():
                values[key] = eval(str(expression), {"__builtins__": {}}, values)
        assert all(abs(values[key] - expected) < 1e-6 for key, expected in data["expected"].items())
        cases += 1
        log("Independent recomputation PASS: " + data["name"] + " " + str({key: values[key] for key in data["expected"]}))
assert len(files) == 8 and cases == 16
readme = yaml.safe_load((ROOT / "skills/togo/README.md").read_text().split("---", 2)[1])
assert len(readme["partial"]) == 7
for slug in readme["covered_by"].values():
    assert (ROOT / "skills/togo" / (slug + ".md")).is_file()
log("README: seven applicable domains remain partial; all routes resolve")
for row in json.loads((ROOT / "docs/research/2026-11-01-togo-pack/old-hashes.json").read_text()):
    old = subprocess.check_output(["git", "show", BASE + ":" + row["path"]], cwd=ROOT)
    assert hashlib.sha256(old).hexdigest() == row["sha256"]
    assert subprocess.check_output(["git", "rev-parse", BASE + ":" + row["path"]], cwd=ROOT).decode().strip() == row["git_blob"]
log("Six pinned old Guide blobs and SHA256 values independently match")
topics = [line for line in (ROOT / "docs/research/2026-11-01-togo-pack/old-topics.md").read_text().splitlines() if line.startswith("| tg-")]
assert len(topics) == 65
log("65 old-topic destination rows; six retained source Guides; no shrink over 25%")
for name in ("validate-guides", "skill_checks"):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if name == "validate-guides":
        errors, warnings = [], []
        module.check_guides(module.load_build_index(), errors, warnings, only_files={str(p.relative_to(ROOT)) for p in files})
        log(f"Scoped validator: errors={errors}; warnings={warnings}")
        assert not errors and not warnings
    else:
        for p in files:
            text = p.read_text()
            fm = yaml.safe_load(text.split("---", 2)[1])
            results = module.run_checks(str(p), text, fm)
            log(p.name + " skill checks: " + str(results))
            assert all(value is None or value is True or value == [] or value == "pass" for value in results.values()), results
(OUT / "independent-validation.txt").write_text("\n".join(lines) + "\n")
