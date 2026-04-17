# OpenAccountants

Open-source tax computation skills for AI. **371 skills across 134 countries.**

Upload to Claude, ChatGPT, or any LLM with your bank statement. Get a working paper ready for your accountant — and **cut your accounting bill by 80%.**

Your accountant charges by the hour. Most of that time is classifying transactions and filling forms. These skills do that work before the meeting. Your accountant reviews and signs off in 20 minutes instead of 3 hours.

**Website:** [openaccountants.com](https://openaccountants.com)

---

## Quick start (60 seconds)

### 1. Find your country

**Most countries (130+):** everything you need is in one place under `packages/`. Upload every file in that folder.

```
packages/
├── malta/           ← 9 files (VAT + income tax + SSC + guided intake)
├── uk/              ← 8 files
├── germany/         ← 7 files
├── australia/       ← 9 files
├── canada/          ← 12 files
├── india/           ← 7 files
├── spain/           ← 7 files
├── ... 126 more countries
```

**United States:** there is **no** `packages/us/` folder. US tax work is split across **modular skills** under `skills/` (federal forms, orchestrators that sequence them, and per-state sales tax). That matches how US compliance layers (federal vs 50 states) rather than a single “country bundle” like Malta.

| What you need | Where it lives |
|----------------|----------------|
| Federal workflow base (how the AI should work) | [`skills/foundation/us-tax-workflow-base.md`](skills/foundation/us-tax-workflow-base.md) |
| Federal content (Schedule C/SE, QBI, estimated tax, bookkeeping, etc.) | [`skills/federal/`](skills/federal/) — upload **all** `.md` files here |
| Orchestration (intake, return assembly, cross-form checks) | [`skills/orchestrator/`](skills/orchestrator/) — include the `us-*.md` files that match your situation (e.g. `us-federal-return-assembly.md`; California freelancers also use `us-ca-*.md`) |
| State sales / use tax | [`skills/us-states/`](skills/us-states/) — pick your state folder and add those `.md` files if sales tax applies |
| Selected states with extra local files | [`skills/florida/`](skills/florida/), [`skills/texas/`](skills/texas/), [`skills/newyork/`](skills/newyork/), [`skills/washington/`](skills/washington/) when relevant |

For a typical **US freelance federal return**, start with `us-tax-workflow-base.md`, everything in `skills/federal/`, and the `us-*.md` files in `skills/orchestrator/` your case needs; add state pieces only if they apply.

Contributors: international packages are generated from `skills/international/` via `scripts/build-packages.py`. US skills are edited directly under `skills/` until a single generated US package exists.

### 2. Upload to your LLM

**International:** open the folder for your country under `packages/`. Upload **all** `.md` files.

**United States:** collect the `.md` files from the paths in the table above (same workflow below).

Upload to:
- **Claude.ai** → Create a Project, add files as Project Knowledge
- **ChatGPT** → Attach files to a conversation or create a Custom GPT
- **Any other LLM** → Attach or paste the files

### 3. Attach your bank statement and go

Say:

```
Help me with my 2025 taxes. Here's my bank statement.
```

The AI will ask a few questions, classify every transaction, and produce a working paper for your accountant.

---

## What's in each package

Every country folder contains:

| File | What it does | Same everywhere? |
|------|-------------|-----------------|
| `foundation.md` | Tells the AI HOW to work — conservative defaults, output format, classification contract | Yes |
| `intake.md` | Onboarding questions, refusal checks, document inference | Yes (country name filled in) |
| `[country]-vat.md` | VAT/GST/sales tax rules, supplier pattern library, form mappings | No — country-specific |
| `[country]-income-tax.md` | Income tax brackets, deductions, transaction patterns | No — country-specific |
| `[country]-ssc.md` | Social security / pension contributions | No — country-specific |
| `[country]-guided-intake.md` | Full guided experience with detailed inference (if available) | No — 8 countries have this |
| `[country]-return-assembly.md` | Cross-checks between VAT, IT, and SSC (if available) | No — 8 countries have this |

**Not every country has every file.** Some have only VAT. Some have VAT + income tax + SSC. Eight countries have the full guided experience. Check the README inside each country folder.

---

## Coverage

### Full guided experience (8 countries)

Upload all files, say "help me with my taxes," and the AI walks you through everything:

| Country | What you get |
|---------|-------------|
| **Malta** | VAT3 + TA24 income tax + Class 2 SSC + provisional tax |
| **United Kingdom** | VAT100 + SA103/SA100 + NIC + student loan |
| **Germany** | UStVA + Einkommensteuer + Sozialversicherung |
| **Australia** | BAS + ITR + super + Medicare levy |
| **Canada** | GST/HST + T1/T2125 + CPP/EI |
| **India** | GST + ITR-3/4 + advance tax |
| **Spain** | IVA + IRPF + RETA |
| **United States (CA)** | 1040 + Schedule C/SE + CA 540 |

### Multi-skill countries (27 countries)

VAT + income tax + social contributions. No guided intake, but the AI uses the universal intake flow:

Austria, Belgium, Brazil, Chile, Colombia, Czech Republic, Denmark, France, Greece, Hungary, Ireland, Italy, Japan, Kenya, Mexico, Netherlands, New Zealand, Nigeria, Norway, Poland, Portugal, Romania, Singapore, South Africa, South Korea, Sweden, Switzerland

### VAT/GST only (99 countries)

Consumption tax classification with country-specific supplier pattern libraries. From Albania to Zimbabwe.

---

## How the skills work

### The supplier pattern library

Every country skill contains a lookup table of local vendors. When the AI sees "BANK OF VALLETTA" or "DEUTSCHE TELEKOM" or "STRIPE PAYMENTS UK LTD" on your bank statement, it already knows the classification — no guessing.

### Three outcomes per transaction

| Outcome | What it means | What happens |
|---------|--------------|-------------|
| **Classified** | Documents carry enough info | Applied automatically, no flag |
| **Assumed** | Data missing, conservative default applied | Flagged for your reviewer with the assumption disclosed |
| **Needs Input** | Can't proceed without asking you | One targeted question |

### Conservative defaults

When uncertain, the system always assumes MORE tax, never less. Your accountant can override a conservative position. They can't easily undo an aggressive one.

---

## Quality tiers

| Tier | What it means |
|------|--------------|
| **Q1 — Battle-tested** | Run against real bank statements. Multiple iterations. Practitioner signed off. |
| **Q2 — Research-verified** | Every rate verified against tax authority websites. Not yet tested on real data. |
| **Q3 — AI-drafted** | Full structure and citations. Not independently verified. |

---

## For developers

### Clone the repo

```bash
git clone https://github.com/openaccountants/openaccountants.git
```

### Repo structure

```
openaccountants/
├── packages/              ← Ready-to-use jurisdiction packages (START HERE for non-US)
│   ├── malta/
│   ├── uk/
│   ├── germany/
│   └── ... 130 more
├── skills/                ← Source files (for contributors); START HERE for United States
│   ├── foundation/        ← Universal workflow base + us-tax-workflow-base.md
│   ├── federal/           ← US federal income tax / Schedule C / SE / QBI / etc.
│   ├── international/     ← Country-specific content (feeds build-packages.py)
│   ├── orchestrator/      ← Intake + assembly (incl. us-federal-return-assembly, us-ca-*)
│   ├── us-states/         ← US state sales & use tax skills
│   ├── cross-border/      ← Reverse charge, WHT, PE risk
│   ├── intelligence/      ← Deadlines, thresholds, optimisation
│   └── patterns/          ← Global vendor patterns
├── scripts/               ← Build tools
│   └── build-packages.py  ← Generates packages/ from skills/
└── docs/                  ← Planning docs, architecture, roadmaps
```

### Rebuild packages after editing skills

```bash
python3 scripts/build-packages.py
```

---

## Contribute

### Think your country's skill is wrong? Prove it.

Use Claude's deep research to verify rates against your tax authority's website. If you find an error — and you will — submit a PR. We've found errors in every single country we've verified. Yours probably has some too.

```
Prompt for deep research:
"Search [your country] tax authority website for the current VAT/GST rate,
registration threshold, and filing deadline. Compare against this skill file."
```

### Build a skill for your country

Most countries have VAT but no income tax skill. Here's how to add one:

1. Open any existing income tax skill (e.g., `skills/international/malta/malta-income-tax.md`)
2. Follow the same structure — quick reference, transaction pattern library, tier 1/tier 2 rules
3. Add your country's local bank patterns (how do transactions appear on YOUR bank statement?)
4. Submit a PR — your name goes on the skill as the author
5. An accountant verifies it → it goes live on [openaccountants.com](https://openaccountants.com)

### Improve the supplier pattern library

Know how your local bank formats statements? Know what "ENERGA SA" or "COUPANG" looks like on a bank CSV? That one line you add saves every user in your country from a misclassification.

### Get credited

Every skill you write, verify, or improve — your name is on it publicly. Contributors build a profile at [openaccountants.com](https://openaccountants.com).

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full guide.

**Pull requests:** contributions are accepted under the [Contributor License Agreement (CLA.md)](CLA.md). You explicitly agree by ticking the CLA box in the [pull request template](.github/PULL_REQUEST_TEMPLATE.md) when you open a PR.

---

## Disclaimer

All skills and outputs are for informational and computational purposes only. Not tax advice. Not a replacement for professional judgment. All outputs must be reviewed by a qualified professional before filing.

The most up-to-date, verified version is maintained at [openaccountants.com](https://openaccountants.com).

## Contact

**info@openaccountants.com**

## License

Dual-licensed: [AGPL-3.0](LICENSE) for open-source use, [commercial license](COMMERCIAL_LICENSE.md) for proprietary products.

Contributions are licensed to the project under the [Contributor License Agreement](CLA.md); see [CONTRIBUTING.md](CONTRIBUTING.md) and the PR template for how you opt in.
