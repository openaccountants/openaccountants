---
name: hi-corporate-tax
description: "Compute Hawaii corporate income tax under HRS 235-71, the net-capital-gain alternative and sales-only election; prepare N-30 state adjustments, estimates and payment workflow for ordinary C corporations."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/hi-corporate-tax"
  jurisdiction: "US-HI"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Hawaii corporation income tax, tax year 2026

> **General reference only.** Built from the official sources identified below. Written by Codex. Not reviewed by an accountant. Obtain qualified professional review before filing, paying or taking a tax position.

> **Circular 230 section 10.37:** Apply this material to the taxpayer's actual facts and the law for the relevant period, evaluate reasonable assumptions and relevant circumstances, and obtain professional review of any federal tax implications. Federal computations belong to the linked federal skills.

**Answer first.** Hawaii has corporate income tax as well as GET. Ordinary C-corporation taxable income is taxed at 4.4% through USD 25,000, 5.4% in the next band through USD 100,000 and 6.4% above USD 100,000. A net-capital-gain alternative can reduce tax. GET on gross receipts remains a separate liability in `hi-sales-tax`. Sources: [HRS 235-71 and 235-71.5](https://files.hawaii.gov/tax/legal/hrs/hrs_235.pdf); [N-30 instructions, Schedule J line 15](https://files.hawaii.gov/tax/forms/current/n30ins.pdf).

## Scope

Ordinary domestic and foreign C corporations with Hawaii filing obligations use **N-30**. The instructions also cover regulated investment companies and REITs, which require specialist review. S corporations use N-35, not N-30. Banks and other chapter 241 entities and specified insurance/cooperative organizations are subject to separate regimes. Every domestic corporation and a foreign corporation with Hawaii-source gross income must test the filing requirement even where tax is zero. Sources: [Who Must File and Exemptions](https://files.hawaii.gov/tax/forms/current/n30ins.pdf); [HRS 235-92](https://files.hawaii.gov/tax/legal/hrs/hrs_235.pdf).

The **2025-2026 filing cycle** N-30 instructions and HRS compilation through 31 December 2025 were fetched. Statutory standing rates are presented for the 2026 pack; final 2026 return revisions and any later conformity changes remain unconfirmed below. Federal corporation computations and figures belong to `us-form-1120-c-corp`, with depreciation figures in `us-section-179-and-bonus-depreciation`.

## Ask the client first

1. Entity classification, domestic/foreign status, federal election, tax year and whether a bank, insurer, REIT or investment company.
2. Federal taxable income, Hawaii modifications, state depreciation/basis schedules and net capital gain.
3. All states of operation, unitary group relationships, property, payroll and sales sourcing.
4. Loss carryforwards, acquisition history, credits and supporting schedules.
5. Estimated payments, withholding, prior-year tax and whether a prior-year safe harbor is available.
6. For the sales-only election, Hawaii gross sales, in-state activities and any owned or rented real/tangible property.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount and conditions | Official source |
|---|---|---|
| Ordinary taxable income not over USD 25,000 | 4.4% of taxable income | [HRS 235-71(a)](https://files.hawaii.gov/tax/legal/hrs/hrs_235.pdf) |
| Ordinary taxable income over USD 25,000 through USD 100,000 | 5.4% of taxable income minus USD 250 | [Schedule J line 15](https://files.hawaii.gov/tax/forms/current/n30ins.pdf) |
| Ordinary taxable income over USD 100,000 | 6.4% of taxable income minus USD 1,250 | [Schedule J line 15](https://files.hawaii.gov/tax/forms/current/n30ins.pdf) |
| Net-capital-gain alternative | Ordinary tax on taxable income less net capital gain, plus 4% of eligible net capital gain, only if less than ordinary tax on all income | [HRS 235-71.5](https://files.hawaii.gov/tax/legal/hrs/hrs_235.pdf) |
| Narrow sales-only election | 0.5% (in words on the page: ".5 per cent") of annual Hawaii gross sales, no more than USD 100,000 gross sales, only in-state activity sales, no owned/rented real or tangible property, and other statutory conditions | [HRS 235-71(e)](https://files.hawaii.gov/tax/legal/hrs/hrs_235.pdf) |
| Estimated-tax floor | Tax liability below USD 500 excused from estimated tax | [HRS 235-97(a)(6)](https://files.hawaii.gov/tax/legal/hrs/hrs_235.pdf) |
| Post-2017 NOL deduction, verified filing-cycle rule | Generally capped at 80% of taxable income; indefinite carryforward, with farming carryback exception | [Amended Return and Schedule J loss instructions](https://files.hawaii.gov/tax/forms/current/n30ins.pdf) |

1. Establish N-30 obligation and separate in-state business from any unitary or consolidated group. Obtain the federal return and state-specific workpapers; merely attaching Form 1120 with a reference to it does not replace completing N-30. Source: [Filing Requirements](https://files.hawaii.gov/tax/forms/current/n30ins.pdf).
2. Prepare **Schedule J** adjustments to federal taxable income: identify federally deductible items not allowed in Hawaii, Hawaii-exempt income, dividends and state-specific depreciation. The verified instructions do not adopt federal bonus depreciation, require a separate state Form 4562 and basis reconciliation, and identify a separate Hawaii section 179 limit. That state limit must be checked against 2026 conformity before use; federal limits are not imported. Source: [Schedule J lines 1 to 12 and depreciation](https://files.hawaii.gov/tax/forms/current/n30ins.pdf).
3. Apply supported loss carryforwards and credits with their own conditions. For post-2017 NOLs, the verified instructions generally disallow carryback except farming, allow indefinite carryforward and cap deduction at 80% of taxable income. Preserve loss vintages and modifications. This is a 2025-2026 filing-cycle rule pending later conformity confirmation. Source: [Amended Return and Schedule J line 9 instructions](https://files.hawaii.gov/tax/forms/current/n30ins.pdf).
4. For a corporation operating only in Hawaii, Schedule J line 12 is the Hawaii taxable-income starting point for the tax calculation. Multi-state/unitary corporations require **Schedules O and P** and applicable allocation/apportionment rules. Do not use an assumed sales-only apportionment factor; separate the narrow statutory gross-sales election below. Source: [unitary business and Schedules O/P instructions](https://files.hawaii.gov/tax/forms/current/n30ins.pdf).
5. Compute ordinary tax using the three rows above. If eligible net capital gain exists, compare ordinary tax on the full base with ordinary tax on the non-capital-gain balance plus 4% of eligible gain; take the lower. Schedule J lines 13 to 15 identify the capital-gain calculation and line 16 totals tax for the relevant filer. Source: [Schedule J lines 13 to 16](https://files.hawaii.gov/tax/forms/current/n30ins.pdf).
6. If the corporation's only Hawaii activities are sales, it owns/rents no Hawaii real or tangible property, its annual Hawaii gross sales do not exceed USD 100,000 and it meets HRS 235-71(e), compare the elective 0.5% tax on Hawaii sales with the regular tax. This is not a general exemption from GET or a general corporate nexus threshold. Obtain a reviewer decision before electing. Source: [HRS 235-71(e)](https://files.hawaii.gov/tax/legal/hrs/hrs_235.pdf).
7. Transfer the supported tax, recaptures and credits to N-30; attach **Schedule CR** for claimed credits. Reconcile N-201V estimated/extension payments and other payments to the account, compute balance/refund and retain each supporting schedule. Sources: [N-30 line instructions and Schedule CR](https://files.hawaii.gov/tax/forms/current/n30ins.pdf).

## Boundary and exception table

| Situation | Treatment |
|---|---|
| Federal S election | File N-35 under the separate S-corporation rules |
| Partnership/disregarded LLC | Owner/partnership rules; not automatically an N-30 filer |
| Multi-state unitary group | Combined filing and Schedules O/P analysis required |
| Net capital gain | Compute the alternative and ordinary tax, choose lower |
| Sales-only corporation at USD 100,000 or less | Test every HRS 235-71(e) condition; gross-sales election is optional |
| Net loss | Review state basis, NOL vintage/limits and required return even if current tax zero |
| REIT, RIC, bank, insurance or special cooperative | Refer to special rules; ordinary C-corporation computation does not complete the job |
| GET license/account exists | Does not replace corporation income tax registration, return or estimated payment |

## Worked cases

**Case 1: ordinary Hawaii C corporation.** Invented corporation has USD 200,000 Hawaii taxable income after verified adjustments and losses, no capital gain or credits. Tax is USD 200,000 x 6.4% minus USD 1,250 = USD 11,550. Equivalently: USD 1,100 on first USD 25,000, USD 4,050 on next USD 75,000 and USD 6,400 on remaining USD 100,000.

```oa-check
name: Hawaii corporation ordinary tax
inputs:
  taxable: 200000
steps:
  - tax: taxable * 0.064 - 1250
  - bands: min(taxable,25000) * 0.044 + min(max(taxable-25000,0),75000) * 0.054 + max(taxable-100000,0) * 0.064
expected:
  tax: 11550
  bands: 11550
```

**Case 2, a decision: capital-gain alternative.** Invented corporation has taxable income USD 200,000 including eligible net capital gain USD 50,000. Ordinary tax is USD 11,550. Tax on ordinary balance USD 150,000 is USD 8,350, plus USD 2,000 on the gain = USD 10,350. Choose the alternative, saving USD 1,200 before credits. The capital-gain amount must be supported by Hawaii Schedule D, not taken unadjusted from federal gain.

```oa-check
name: Hawaii corporation capital gain alternative decision
inputs:
  taxable: 200000
  capital_gain: 50000
steps:
  - ordinary_tax: taxable * 0.064 - 1250
  - ordinary_balance: taxable - capital_gain
  - balance_tax: ordinary_balance * 0.064 - 1250
  - alternative: balance_tax + capital_gain * 0.04
  - chosen: min(ordinary_tax,alternative)
  - saving: ordinary_tax - chosen
expected:
  ordinary_tax: 11550
  ordinary_balance: 150000
  balance_tax: 8350
  alternative: 10350
  chosen: 10350
  saving: 1200
```

## When to refuse or refer

Refer apportionment, combined/unitary groups, foreign-income modifications, complex credits, reorganizations and losses, REIT/RIC or chapter 241 filers and uncertainty about 2026 conformity. Do not turn the verified 2025 state depreciation limit into an assumed 2026 amount.

## Filing and payment

Use **Hawaii Tax Online**, https://hitax.hawaii.gov/, choose corporation income, period and N-30. Complete the corporation identity and filing classification, Schedule J and relevant O/P/D/CR attachments, reconcile payments, submit and retain acceptance. Make payment separately as needed against the same tax period; **N-201V** is the business income-tax payment voucher. The verified N-30 instructions suspend the mandatory N-30 e-file penalty; verify any later notice before relying on that suspension. Source: [When and Where to File, Payment and EFT](https://files.hawaii.gov/tax/forms/current/n30ins.pdf).

Return and balance are due the twentieth day of the fourth month following year end, **20 April 2027** for calendar 2026. An automatic six-month filing extension does not extend payment; use N-201V by the regular due date, not federal Form 7004 as a substitute. Calendar-year estimated payments are due 20 April, 20 June, 20 September and 20 January after the tax year, with applicable nonbusiness-day relief. General corporate estimated-tax comparison is 100% current versus 100% prior-year tax, subject to prior-year and large-corporation limitations; annualization uses N-220. Sources: [HRS 235-97](https://files.hawaii.gov/tax/legal/hrs/hrs_235.pdf); [extension, estimates and line 17 instructions](https://files.hawaii.gov/tax/forms/current/n30ins.pdf).

The verified instructions impose late-filing penalty of 5% per month or part up to 25%; a timely filed return unpaid more than 60 days can incur 20% late-payment penalty; interest is two-thirds of 1% per month or part on unpaid tax and penalties. N-220 addresses corporate estimated underpayment. Source: [Penalties and Interest](https://files.hawaii.gov/tax/forms/current/n30ins.pdf).

## Completion checklist

- Entity and N-30 obligation established separately from GET and payroll.
- Hawaii modifications, depreciation, losses and any unitary allocation documented.
- Ordinary and eligible alternative calculations compared; credits supported on Schedule CR.
- Final-year form revision, deadlines, estimated payment credits and portal acceptance checked.

## Sources

| Source and scope actually read | URL | Read on |
|---|---|---|
| HRS chapter 235 compilation through December 31, 2025. Read sections 235-7, 235-71, 235-71.5, 235-92 and 235-97 for state base, corporate rates, sales-only election, alternative and filing obligations. | https://files.hawaii.gov/tax/legal/hrs/hrs_235.pdf | 2026-11-13 |
| N-30 Rev. 2025 instructions. Read Who Must File, Exemptions, When and Where to File, estimates, penalties, line instructions, Schedule J and Schedules O/P routing. 2025-2026 filing cycle. | https://files.hawaii.gov/tax/forms/current/n30ins.pdf | 2026-11-13 |

Not yet confirmed: final 2026 N-30 forms/instructions and any 2026 conformity amendments after the HRS compilation; the 2026 Hawaii section 179 amount (2025 instructions state USD 25,000) and related depreciation/contribution/foreign-income changes; final 2026 NOL changes; complete multi-state Schedules O/P factors and sourcing; specialist bank/franchise, REIT and insurance regimes. Do not apply these missing computations as though the ordinary C-corporation method covers them.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `hi-corporate-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/hi-corporate-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
