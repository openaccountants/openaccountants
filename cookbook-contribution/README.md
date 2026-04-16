# Cookbook contribution — Example 4: Composing Skills for Regulated Domains

This folder is a self-contained, drop-in contribution to [`anthropics/claude-cookbooks`](https://github.com/anthropics/claude-cookbooks). It adds a fourth example to `skills/notebooks/03_skills_custom_development.ipynb` demonstrating **skill composition for regulated-domain safety**, with US Schedule C transaction classification as the worked example.

## What's in here

```
cookbook-contribution/
├── README.md                                                   # This file
├── custom_skills/
│   ├── tax-workflow-base/
│   │   └── SKILL.md                                            # ~2,275 tokens. Workflow only, no tax content.
│   └── classifying-tax-transactions/
│       └── SKILL.md                                            # ~2,210 tokens. Schedule C rules only, no workflow.
└── notebook_cells.json                                         # 15 cells (markdown + code) to insert into Notebook 3
```

Each skill folder mirrors the existing convention in `skills/custom_skills/` (single `SKILL.md`, kebab-case directory name). The notebook cells extend Examples 1–3 without redefining any helper functions.

## Why this contribution

The three existing examples in Notebook 3 — financial ratio analyser, brand guidelines, financial modelling suite — each ship a **single** skill that does its job end-to-end. None of them demonstrate **skill composition**: two skills loaded together where one supplies the workflow architecture and the other supplies the substantive rules. Composition is briefly hinted at in Example 3 (which loads the financial modelling skill alongside the built-in `xlsx` skill) but not developed as a pattern.

This contribution develops it into a pattern. The architectural move is to split the safety story into a **reusable workflow base** (three-state contract, conservative-defaults principle, citation discipline, structured-question form, reviewer-brief spec) and a **swappable content skill** (jurisdiction-specific vendor patterns, conservative defaults, refusal triggers, form lines). Loaded together they produce a complete classifier; the workflow base alone refuses to operate; the same workflow base composes with any other jurisdiction's content skill (UK VAT, Malta TA24, Slovak DPH, etc.) without modification.

The Schedule C skill is the demonstration; the composition pattern is the contribution. It generalises directly to medical coding, legal classification, trade compliance, and regulatory filings — anywhere wrong answers are auditable and silent failure is dangerous.

## How to merge into the cookbook fork

```bash
# In your fork of anthropics/claude-cookbooks
cd <your-fork>/skills/

# 1. Copy both skill folders
cp -R /path/to/cookbook-contribution/custom_skills/tax-workflow-base custom_skills/
cp -R /path/to/cookbook-contribution/custom_skills/classifying-tax-transactions custom_skills/

# 2. Insert the notebook cells (see notebook_cells.json)
#    The JSON file lists the exact insertion point and renumbering required.
#    You can paste the cells through the Jupyter UI, or splice them in with the
#    snippet at the bottom of this README.
```

### Insertion point in Notebook 3

- Insert **after** existing cell `[24]` (the Example 3 DCF test code cell)
- Insert **before** existing cell `[25]` (`## 6. Skill Management & Versioning`)
- Renumber downstream sections:
  - `## 6. Skill Management & Versioning` → `## 7.`
  - `## 7. Best Practices & Production Tips` → `## 8.`
- Add to the Table of Contents cell at index `[1]`:
  - `6. [Example 4: Composing Skills for Regulated Domains](#tax-classification)`
  - increment existing entries 6 and 7 to 7 and 8

### Splice helper (optional)

```python
import json
from pathlib import Path

NOTEBOOK = Path("skills/notebooks/03_skills_custom_development.ipynb")
INSERT_AFTER_CELL_INDEX = 24  # the Example 3 DCF test code cell

nb = json.loads(NOTEBOOK.read_text())
new = json.loads(Path("notebook_cells.json").read_text())["cells"]

nb["cells"] = (
    nb["cells"][: INSERT_AFTER_CELL_INDEX + 1]
    + new
    + nb["cells"][INSERT_AFTER_CELL_INDEX + 1 :]
)

NOTEBOOK.write_text(json.dumps(nb, indent=1))
print(f"Inserted {len(new)} cells. Remember to renumber sections 6/7 to 7/8.")
```

## Verification before opening a PR

| Check | Status |
|---|---|
| `tax-workflow-base` frontmatter — `name` 17 chars (≤64), `description` 600 chars (≤1024) | ✓ |
| `classifying-tax-transactions` frontmatter — `name` 28 chars (≤64), `description` 595 chars (≤1024) | ✓ |
| `tax-workflow-base` token budget — ~2,275 tokens (under 5K limit, under 3K target) | ✓ |
| `classifying-tax-transactions` token budget — ~2,210 tokens (under 5K limit, under 3K target) | ✓ |
| Display titles unique vs existing 3 — `"Tax Workflow Base"` and `"Schedule C Classifier"` (no collision) | ✓ |
| Uses existing `create_skill()` and `test_skill()` helpers from cell 7 — no redefinition | ✓ |
| Composition tests use the canonical `client.beta.messages.create` form with `betas` and `container` — same pattern as cell 24 in the existing notebook (which composes a custom skill with `xlsx`) | ✓ |
| End-to-end runnable — every code cell executes against the live API and produces output | ✓ |
| No PII / sensitive data / commercial wrappers — generic vendor names, synthetic amounts | ✓ |
| Splices into real notebook 3 cleanly — simulated to a 52-cell valid notebook | ✓ |

## What the notebook section demonstrates, in order

1. **Why this matters** — the failure mode (LLM tells freelance dev Netflix is a business expense).
2. **Why composition** — universal workflow vs jurisdiction-specific rules.
3. **The composition pattern** — Mermaid diagram showing how the two skills compose into the three-state contract.
4. **Upload the workflow base.**
5. **Confirm the workflow base alone refuses to operate** — proves the slot contract is enforced at runtime.
6. **Upload the content skill.**
7. **Test 1 — both loaded, Tier 1 deterministic match** — clean classification, no flags.
8. **Test 2 — both loaded, Tier 2 conservative defaults** — flags, citations, consolidated question list.
9. **Test 3 — both loaded, out-of-scope refusal** — verbatim refusal, no partial classification.
10. **Why composition is the architectural move** — generalisation to medical / legal / trade-compliance / regulatory domains, with one footnote link to OpenAccountants as the production reference (134 jurisdictions, 371 content skills).

## Voice and structural alignment

- Markdown cells follow the cookbook's understated, technical voice (light "Let's", sparingly used ✓ ✅ ⚠️). No marketing language. No mentions of any commercial product in the notebook prose.
- Section heading uses the cookbook pattern: `## N. Title {#anchor}`.
- Composition tests mirror the verbose `client.beta.messages.create` pattern used in Example 3 cell 24 — so the new section feels like a natural extension of an in-notebook pattern rather than a new convention.
- Single foot-link at the end of the section pointing at the OpenAccountants repo. One link, no pitch.

## What this skill pair is *not*

- Not tax advice. The skills are classification aids for review by a human professional credentialed under Treasury Department Circular 230 (Enrolled Agent, CPA, or attorney).
- Not multi-jurisdiction. The content skill is US federal Schedule C only, sole proprietors and single-member LLCs, tax year 2025. The workflow base is jurisdiction-agnostic by design but is paired here with one jurisdiction.
- Not a return preparer. Neither skill produces Schedule C totals, Schedule SE, QBI, retirement contributions, or quarterly estimated tax. Those are separate concerns.
- Not a wrapper on a commercial API. Both skills are pure rules + citations and run entirely inside the Anthropic skills runtime.

## License

Submitted under the cookbook's MIT licence. The author retains attribution under standard cookbook contributor terms.
