# OpenAccountants

Open-source tax computation skills for AI. **371 skills across 134 countries.**

Upload to Claude, ChatGPT, or any LLM with your bank statement. Get a working paper ready for your accountant — and **cut your accounting bill by 80%.**

Your accountant charges by the hour. Most of that time is classifying transactions and filling forms. These skills do that work before the meeting. Your accountant reviews and signs off in 20 minutes instead of 3 hours.

**Website:** [openaccountants.com](https://openaccountants.com)

---

## Quick start (60 seconds)

### 1. Find your country

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

### 2. Upload to your LLM

Open the folder for your country. Upload ALL `.md` files to:
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
├── packages/              ← Ready-to-use jurisdiction packages (START HERE)
│   ├── malta/
│   ├── uk/
│   ├── germany/
│   └── ... 130 more
├── skills/                ← Source files (for contributors)
│   ├── foundation/        ← Universal workflow base
│   ├── international/     ← Country-specific content
│   ├── orchestrator/      ← Intake + assembly skills
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

### Verify a skill for your country

Open any skill file, check the rates against current law, submit a PR with corrections. Your name goes on it as the verifier.

### Write a skill for a new obligation

Most countries have VAT but no income tax skill. Adding one = following the pattern in any existing income tax skill.

### Improve the supplier pattern library

Know how your local bank formats statements? Know what "ENERGA SA" or "COUPANG" looks like on a bank CSV? Add it to the pattern library.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full guide.

---

## Disclaimer

All skills and outputs are for informational and computational purposes only. Not tax advice. Not a replacement for professional judgment. All outputs must be reviewed by a qualified professional before filing.

The most up-to-date, verified version is maintained at [openaccountants.com](https://openaccountants.com).

## Contact

**info@openaccountants.com**

## License

Dual-licensed: [AGPL-3.0](LICENSE) for open-source use, [commercial license](COMMERCIAL_LICENSE.md) for proprietary products.

## Built by

[Glimpse Ltd](https://accora.ai) (trading as Accora) — open-source accounting tools for AI.
