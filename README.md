# OpenAccountants

Open-source accounting skills for AI. Tax rules written as code, verified by real accountants, usable by anyone.

**Website:** [openaccountants.com](https://openaccountants.com)

---

## What this is

Every tax rule that touches your return is a readable markdown file in this repo. IRC citations, dollar thresholds, computation logic — it's all here. Licensed accountants verify each section. You run the skills in Claude, upload the output, and get a human review before you file.

This is **not** tax advice. These are computation tools. Always have a qualified professional review your return before filing.

## Skills

```
skills/
├── foundation/
│   └── us-tax-workflow-base.md              # Workflow runbook, conservative defaults, output spec
├── federal/
│   ├── us-sole-prop-bookkeeping.md          # Transaction → Schedule C line items (115K chars)
│   ├── us-schedule-c-and-se-computation.md  # Net profit, home office, SE tax (75K chars)
│   ├── us-self-employed-retirement.md       # Solo 401(k), SEP-IRA, SIMPLE, traditional IRA
│   ├── us-self-employed-health-insurance.md # IRC §162(l) deduction
│   ├── us-qbi-deduction.md                 # §199A with cliff and phase-in
│   ├── us-quarterly-estimated-tax.md        # 1040-ES, safe harbor, underpayment penalty
│   ├── us-1099-nec-issuance.md             # Contractor payment matrix, $600 threshold
│   └── us-s-corp-election-decision.md       # S-Corp election analysis
├── california/
│   ├── ca-540-individual-return.md          # Form 540 + Schedule CA
│   ├── ca-estimated-tax-540es.md            # 30/40/0/30 installment schedule
│   ├── ca-smllc-form-568.md                # $800 franchise tax, LLC return
│   └── ca-form-3853-coverage.md             # Health coverage mandate
└── orchestrator/
    ├── us-ca-freelance-intake.md            # Entry point — document parsing, eligibility
    ├── us-federal-return-assembly.md        # Assembles federal package
    └── us-ca-return-assembly.md             # Final assembly — federal + California
```

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

After installing, send Claude this message with your documents attached:

```
I need help preparing my 2025 federal and California tax return.
I'm a freelance software developer, single-member LLC in California.
Here are my documents.
```

Attach: bank statement CSV (full year), 1099-NEC PDFs, prior year return. Optionally: Solo 401(k) statement, 1095-A, W-9s from contractors you paid.

## What you get

**Worksheet** — Schedule C totals, SE tax, QBI deduction, retirement contributions, estimated payments, California adjustments. Every figure with an IRC citation.

**Review report** — Self-checks and flags. What looks right, what needs human review, what the accountant should double-check.

## Get it reviewed

Upload your outputs at [openaccountants.com](https://openaccountants.com). A verified accountant (CPA or EA) reviews against a structured checklist, leaves comments, and signs a digital attestation.

## Contribute

We have California covered. Every other state is wide open.

**If you know your state's tax code, write a skill for it.**

1. Download the [skill template](skill-template.md)
2. Follow the structure of the existing CA skills
3. Submit via [openaccountants.com/contribute](https://openaccountants.com/contribute) or open a PR here
4. An accountant verifies each section → your skill goes live

Contributors get:
- Your name on the skill
- Public contributor profile at [openaccountants.com/contributors](https://openaccountants.com/contributors)
- Accountant verification of your work

### States we need

| State | Forms | Status |
|-------|-------|--------|
| New York | IT-201, IT-2, IT-215 | **Needed** |
| Texas | Franchise tax (05-158-A) | **Needed** |
| Florida | LLC annual report | **Needed** |
| Washington | B&O tax, WA-BTA | **Needed** |
| Illinois | IL-1040, Schedule NR | **Needed** |
| Your state | You tell us | **Open** |

## What these skills catch

Real scenarios from the Alex Chen test persona ($185K/yr freelance developer, San Francisco):

- QBI cliff near $191,950 — phases out deduction, costs thousands
- Solo 401(k) excess contribution — penalties if over the limit
- COBRA → Covered California mid-year — affects health insurance deduction
- 1099-NEC issuance matrix — corps excluded, sole props required
- Estimated tax underpayment — safe harbor rules, penalty computation
- California decoupling — CA doesn't conform to OBBBA provisions
- $800 LLC franchise tax — due even if you lost money
- Home office — actual vs simplified method decision
- SE tax — 92.35% adjustment, Additional Medicare Tax
- Retirement limits — employee + employer sides of Solo 401(k)
- Health insurance eligibility — SE health vs marketplace subsidy interaction
- S-Corp election — when it saves money vs when it doesn't
- Multi-form assembly — 8+ forms that need to tie together

## License

MIT

## Built by

[Accora](https://accora.ai) — open-source accounting tools for AI.
