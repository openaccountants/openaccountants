# OpenAccountants

Open-source tax computation skills for AI. **349 skills across 134+ countries.** Tax rules written as executable markdown, verified via deep research, reviewed by real accountants.

**Website:** [openaccountants.com](https://openaccountants.com)

---

## What this is

Every tax rule that touches your return is a readable markdown file in this repo. Statute citations, rate tables, computation logic, form mappings — it's all here. Skills are verified through deep research against tax authority websites and cross-referenced with PWC, KPMG, and Deloitte guides. Licensed accountants sign off on battle-tested skills. You run the skills in Claude, upload the output, and get a human review before you file.

This is **not** tax advice. These are computation tools. Always have a qualified professional review your return before filing.

## Quality tiers

Not all skills are equal. Every skill is labelled with its quality tier:

| Tier | Label | Count | What it means |
|------|-------|-------|--------------|
| **Q1** | Battle-tested | 7 | Run against real bank statements and real filings. Multiple iterations. Practitioner signed off. |
| **Q2** | Research-verified | ~136 | Deep research verified against tax authority websites. Q1 execution format. Not yet tested against real data. |
| **Q3** | AI-drafted | ~146 | Drafted by Claude with full structure. Facts not independently verified. |
| **Q4** | Stub | ~60 | Template structure with correct metadata. Computation rules empty. |

See [QUALITY-TIERS.md](QUALITY-TIERS.md) for the full quality framework.

## Repository structure

```
skills/
├── orchestrator/                              # Entry points & assembly
│   ├── global-freelance-router.md             # Universal entry point — detects jurisdiction
│   ├── us-ca-freelance-intake.md              # California freelancer intake (Q1)
│   ├── us-federal-return-assembly.md          # Federal return assembly (Q2)
│   ├── us-ca-return-assembly.md               # CA return assembly (Q2)
│   ├── mt-freelance-intake.md                 # Malta freelancer intake (Q2)
│   └── mt-return-assembly.md                  # Malta return assembly (Q2)
│
├── foundation/                                # Workflow infrastructure
│   ├── us-tax-workflow-base.md                # US income tax pipeline (Q1)
│   ├── vat-workflow-base.md                   # VAT/GST pipeline (Q2)
│   ├── gst-workflow-base.md                   # GST systems (stub)
│   ├── income-tax-workflow-base.md            # International income tax (stub)
│   └── social-contributions-workflow-base.md  # Social contributions (stub)
│
├── federal/                                   # US federal (8 skills)
│   ├── us-sole-prop-bookkeeping.md            # Transaction classification (Q1)
│   ├── us-schedule-c-and-se-computation.md    # Schedule C + SE tax (Q1)
│   ├── us-qbi-deduction.md                   # §199A QBI deduction
│   ├── us-self-employed-retirement.md         # Solo 401(k), SEP-IRA
│   ├── us-self-employed-health-insurance.md   # §162(l) deduction
│   ├── us-quarterly-estimated-tax.md          # Form 1040-ES
│   ├── us-1099-nec-issuance.md               # Contractor reporting
│   └── us-s-corp-election-decision.md         # S-Corp analysis
│
├── california/                                # California (5 skills)
├── newyork/                                   # New York (5 skills, Q2)
├── texas/                                     # Texas (3 skills)
├── florida/                                   # Florida (3 skills)
├── illinois/                                  # Illinois (4 skills)
├── washington/                                # Washington (3 skills)
├── us-states/                                 # 40 other US state sales tax skills
│
└── international/                             # 134 countries
    ├── eu/                                    # EU VAT Directive (Q2)
    ├── uk/                                    # UK (6 skills — SA100, SA103, NIC, VAT, etc.)
    ├── germany/                               # Germany (5 skills — VAT Q1, income tax, trade tax)
    ├── france/                                # France (4 skills — VAT Q2, income tax)
    ├── italy/                                 # Italy (5 skills — VAT Q2, income tax, INPS)
    ├── spain/                                 # Spain (5 skills — VAT Q2, IRPF, RETA)
    ├── malta/                                 # Malta (4 skills — IT Q1, VAT Q1, SSC Q1)
    ├── canada/                                # Canada (9 skills — GST/HST Q2, T1, provinces)
    ├── australia/                             # Australia (6 skills — GST Q2, income tax)
    ├── new-zealand/                           # New Zealand (5 skills — GST Q2)
    ├── india/                                 # India (5 skills — GST Q2, ITR)
    ├── japan/                                 # Japan (5 skills — consumption tax)
    ├── singapore/                             # Singapore (4 skills — GST Q2)
    ├── south-korea/                           # South Korea (4 skills — VAT Q2)
    ├── brazil/                                # Brazil (6 skills — indirect tax Q2)
    ├── mexico/                                # Mexico (6 skills — IVA Q2, ISR)
    ├── uae/                                   # UAE (3 skills — VAT Q2, corporate tax)
    ├── saudi-arabia/                          # Saudi Arabia (VAT Q2)
    └── ... 116 more countries                 # VAT/GST/consumption tax skills
```

## End-to-end jurisdictions

These jurisdictions have a complete flow — intake, classification, computation, assembly, reviewer output:

| Jurisdiction | Entry point | What it produces |
|-------------|------------|-----------------|
| **US — California** | `us-ca-freelance-intake` | Federal 1040 + Schedule C/SE + CA 540 + Form 568 + working paper + reviewer brief |
| **Malta** | `mt-freelance-intake` | TA24 income tax + VAT3 + Class 2 SSC + provisional tax + working paper + reviewer brief |

All other jurisdictions have content skills available but need intake + assembly orchestrators to enable the full flow.

## Install

### Claude Code

```bash
git clone https://github.com/michaelcutajar1995/openaccountants.git ~/.claude/skills/openaccountants
```

### Claude Desktop / Web

1. Go to claude.ai → Settings → Skills
2. Upload each `.md` file from `skills/` as a new skill
3. Start a conversation — the skills activate automatically

## Quick start

### California freelancer (complete flow)

```
I need help preparing my 2025 federal and California tax return.
I'm a freelance software developer, single-member LLC in California.
Here are my documents.
```

Attach: bank statement CSV (full year), 1099-NEC PDFs, prior year return. Optionally: Solo 401(k) statement, 1095-A, W-9s from contractors you paid.

### Malta self-employed (complete flow)

```
I need help with my 2025 TA24, VAT return, and SSC.
I'm self-employed in Malta, Article 10 VAT registered.
Here are my bank statements and invoices.
```

### Any other country (consumption tax skills available)

```
Help me classify transactions for my German VAT return.
```

```
I need to prepare my India GST return (GSTR-3B).
```

The global router will detect your jurisdiction and tell you exactly what's available.

## What you get

**Working paper** — Transaction-by-transaction classification, form line items, every figure with a statutory citation.

**Reviewer brief** — Positions taken, edge cases flagged, confidence tiers marked, what the reviewer should double-check.

**Action list** — Filing deadlines, payment amounts, what to do and when.

## Get it reviewed

Upload your outputs at [openaccountants.com](https://openaccountants.com). A verified accountant reviews against a structured checklist, leaves comments, and signs off.

## Contribute

We have **134+ countries** with consumption tax skills. Here's what's still needed:

### High-impact contributions needed

| Category | What's needed | Difficulty |
|----------|--------------|-----------|
| **Income tax skills** | UK SA100/SA103, German ESt, Australian ITR, Canadian T1 — full content for Q4 stubs | Medium — requires knowledge of local tax law |
| **Social contribution skills** | UK NIC, German SV, French URSSAF — full content for Q4 stubs | Medium |
| **Intake + assembly orchestrators** | UK, Germany, Australia, India, Canada — enable end-to-end flow | Easy — follow the US-CA/Malta pattern |
| **Practitioner verification** | Review any Q2/Q3 skill for your jurisdiction — confirm rates, forms, thresholds | Easy — reading and confirming, not writing |
| **Battle testing (Q1)** | Run a Q2 skill against real (anonymised) transaction data and report errors | High impact — requires real data |

### How to contribute

1. Download the [skill template](skill-template.md)
2. Pick a skill from the taxonomy — see [SKILL-TAXONOMY.md](SKILL-TAXONOMY.md)
3. Follow the Q1 Step format (see any Malta or Germany skill for examples)
4. Submit via [openaccountants.com/contribute](https://openaccountants.com/contribute) or open a PR
5. An accountant verifies each section → your skill gets a verified badge

Contributors get:
- Your name on the skill, linked to your contributor profile
- Public contributor profile at [openaccountants.com/contributors](https://openaccountants.com/contributors)
- Professional verification of your work

## Planning documents

| Document | What it covers |
|----------|---------------|
| [SKILL-TAXONOMY.md](SKILL-TAXONOMY.md) | Master skill map — every skill needed, by country, with status |
| [QUALITY-TIERS.md](QUALITY-TIERS.md) | Quality tier definitions, promotion criteria, deep research sources |
| [PROMOTION-PLAYBOOK.md](PROMOTION-PLAYBOOK.md) | How to move skills from Q3 → Q2 → Q1 |
| [GLOBAL-EXPANSION-PLAN.md](GLOBAL-EXPANSION-PLAN.md) | Phased rollout strategy for 40+ jurisdictions |
| [USER-STORIES.md](USER-STORIES.md) | User journey maps and orchestration gaps |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to write and submit a skill |

## Disclaimer

All skills and their outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of these skills. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## License

**Dual-licensed:**

- **AGPL-3.0** — Free for individuals, educators, open-source projects, and anyone willing to open-source their work. See [LICENSE](LICENSE).
- **Commercial License** — For businesses building proprietary products that incorporate these skills. See [COMMERCIAL_LICENSE.md](COMMERCIAL_LICENSE.md).

**In plain English:**
- Using the skills to do your own taxes? Free.
- Accountant using them to help clients? Free.
- Building a SaaS product with them? Either open-source your product under AGPL-3.0, or get a commercial license.

Contributors agree to the [Contributor License Agreement](CLA.md) when submitting a PR.

## Built by

[Glimpse Ltd](https://accora.ai) (trading as [Accora](https://accora.ai)) — open-source accounting tools for AI.
