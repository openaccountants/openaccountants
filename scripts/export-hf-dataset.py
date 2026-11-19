#!/usr/bin/env python3
"""Build the Hugging Face dataset folder for openaccountants/tax-skills.

One JSON line per skill: the skill text exactly as it is in skills/, plus the fields a
reader needs to judge it (place, tax year, approval, official sources). The dataset is
published GATED on Hugging Face: downloading it means accepting the Open Accountants
Skills License v2.0, whose paid Data tier covers training, evaluation and redistribution
as a dataset (LICENSING.md). Nothing here changes a skill or anything the site reads.

    python3 scripts/export-hf-dataset.py --out /tmp/hf-tax-skills
    # then, with a Hugging Face write token for the openaccountants org:
    # hf upload openaccountants/tax-skills /tmp/hf-tax-skills . --repo-type dataset
"""
import argparse
import collections
import datetime
import importlib.util
import json
import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO_ROOT, "scripts"))
GITHUB = "https://github.com/openaccountants/openaccountants/blob/main/"
URL_RE = re.compile(r"https?://[^\s)<>\]|\"']+")


def load(module_name, file_name):
    spec = importlib.util.spec_from_file_location(module_name, os.path.join(REPO_ROOT, "scripts", file_name))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def official_sources(text):
    """Distinct URLs cited in the skill, in order of first appearance."""
    seen, out = set(), []
    for url in URL_RE.findall(text):
        url = url.rstrip(".,;:")
        if url not in seen and "openaccountants" not in url:
            seen.add(url)
            out.append(url)
    return out


def rows():
    index = load("build_index", "build-index.py").build_index()
    names = {}
    with open(os.path.join(REPO_ROOT, "scripts", "data", "jurisdictions.json"), encoding="utf-8") as fh:
        for j in json.load(fh):
            names[j["code"]] = j["name"]
    for g in sorted(index["guides"], key=lambda g: g["path"]):
        with open(os.path.join(REPO_ROOT, g["path"]), encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        approved = str(g.get("tier")) == "1" and bool(g.get("reviewed_by"))
        code = str(g.get("jurisdiction") or "").upper()
        yield {
            "slug": g["slug"],
            "jurisdiction": code,
            "place": names.get(code, code),
            "tax_year": str(g.get("tax_year") or ""),
            "last_updated": str(g.get("last_updated") or ""),
            "label": f"Approved by {g['reviewed_by']}" if approved else "Not yet approved",
            "approved_by": g.get("reviewed_by") if approved else None,
            "official_sources": official_sources(text),
            "path": g["path"],
            "url": GITHUB + g["path"],
            "text": text,
        }


CARD = """---
license: other
license_name: open-accountants-skills-license-2.0
license_link: https://github.com/openaccountants/openaccountants/blob/main/LICENSES/LicenseRef-OA-Guide-License-2.0.txt
language:
- en
pretty_name: OpenAccountants tax skills
size_categories:
- 1K<n<10K
task_categories:
- question-answering
- text-generation
tags:
- tax
- accounting
- vat
- payroll
- legal
- finance
- agent-skills
- mcp
extra_gated_heading: Access the OpenAccountants tax skills
extra_gated_prompt: >-
  This dataset is under the Open Accountants Skills License v2.0 (source-available).
  Reading and personal or small-business use (5 or fewer people) are free. Training,
  fine-tuning or evaluating models, building test sets, building the skills into a
  product, or redistributing them as a dataset needs a paid licence. Contact
  info@openaccountants.com.
extra_gated_fields:
  Name: text
  Company or organisation: text
  Country: country
  Intended use:
    type: select
    options:
      - Personal or own taxes
      - Small business (5 or fewer people)
      - Education or research
      - Commercial product or RAG
      - Model training or evaluation
      - Other
  I accept the Open Accountants Skills License v2.0: checkbox
---

# OpenAccountants tax skills

**{skills:,} tax skills for {places} countries, states and territories, written from the law.
{approved} are approved by {accountants} named, licensed accountants.** Each row is one skill:
the step-by-step method an AI follows for one tax task (a VAT return, how a freelancer is
taxed, payroll, company tax), with every rate, threshold and deadline linked to the official
page it came from.

This is the same library that ChatGPT, Claude, Cursor and other AI apps load through the
[OpenAccountants plugin](https://www.openaccountants.com/connect). Source of truth and
history: [github.com/openaccountants/openaccountants](https://github.com/openaccountants/openaccountants).

## Fields

| Field | What it is |
|---|---|
| `slug` | Skill id, as used by the plugin's `get_skill` |
| `jurisdiction`, `place` | ISO code (US states as `US-CA`) and name |
| `tax_year` | The tax year the figures are for |
| `last_updated` | Date of the last change to the skill |
| `label` | `Approved by [name]` or `Not yet approved` |
| `approved_by` | The approving accountant, from their own GitHub approval |
| `official_sources` | Official URLs the skill cites |
| `path`, `url` | File in the GitHub repo |
| `text` | The full skill, Markdown with YAML frontmatter |

## How the figures are kept honest

Every figure in a rates table links to its official source, and on every change a
figure check looks for the figure on that page. Worked examples are recomputed. An
approval counts only when the accountant approves the exact text from their own GitHub
account; any later change clears it until they approve again.

## Licence

[Open Accountants Skills License v2.0](https://github.com/openaccountants/openaccountants/blob/main/LICENSES/LicenseRef-OA-Guide-License-2.0.txt).
Free to read and to use for your own taxes, as a professional reference, in a business
of 5 or fewer people, and for education and research. A paid licence covers larger teams,
products and commercial RAG, and model training, evaluation or redistribution
([commercial licensing](https://github.com/openaccountants/openaccountants/blob/main/COMMERCIAL-LICENSING.md)).
Contact info@openaccountants.com.

General reference, not advice. Have a qualified professional review outputs before
filing, payment or action.

<sub>Built {built} from GitHub commit {commit}.</sub>
"""


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", required=True, help="Folder to write README.md and data/skills.jsonl into")
    ap.add_argument("--commit", default=os.environ.get("GITHUB_SHA", "local"))
    args = ap.parse_args(argv)
    os.makedirs(os.path.join(args.out, "data"), exist_ok=True)
    places, approvers, n, approved = set(), set(), 0, 0
    by_place = collections.Counter()
    with open(os.path.join(args.out, "data", "skills.jsonl"), "w", encoding="utf-8") as fh:
        for row in rows():
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")
            n += 1
            if row["place"] != row["jurisdiction"]:  # a real place in jurisdictions.json, not GLOBAL/EU
                places.add(row["jurisdiction"])
            by_place[row["jurisdiction"]] += 1
            if row["approved_by"]:
                approved += 1
                approvers.add(row["approved_by"].strip())
    card = CARD.format(skills=n, places=len(places), approved=approved, accountants=len(approvers),
                       built=datetime.date.today().isoformat(), commit=args.commit[:12])
    with open(os.path.join(args.out, "README.md"), "w", encoding="utf-8") as fh:
        fh.write(card)
    print(f"{n} skills, {len(places)} places, {approved} approved by {len(approvers)} accountants -> {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
