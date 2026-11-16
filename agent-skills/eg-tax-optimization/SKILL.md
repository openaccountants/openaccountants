---
name: eg-tax-optimization
description: "Use this skill whenever asked about legitimate tax optimization, tax planning, or how to legally reduce tax for self-employed people, freelancers, professionals, sole proprietors, and small businesses in Egypt. Trigger on phrases like \"reduce tax Egypt\", \"save tax freelancer Egypt\", \"simplified vs general Egypt\", \"Egypt tax planning\", \"SME regime worth it Egypt\", \"lower my tax bill Egypt\", \"is the simplified regime cheaper\", \"تخطيط ضريبي مصر\", \"تقليل الضرائب مصر\", \"النظام المبسط أم العام\", \"هل النظام المبسط أوفر\", \"توفير ضرائب\". Covers the choice between the turnover-based simplified SME regime (Law No. 6 of 2025) and the general progressive income-tax system, the break-even logic, e-invoicing as a deductibility lever, VAT threshold management, and the Law No. 5 of 2025 dispute-settlement / amnesty facilities. LEGAL planning only , never tax evasion. AI replies in the user's language (English or Arabic)."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/eg-tax-optimization"
  jurisdiction: "EG"
  tax_year: "2026"
  last_updated: "2026-11-16"
---

# EG Tax Optimization v1.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

The decision layer for lawful tax planning by self-employed people and small businesses in Egypt, tax year 2026, law as read on 16 November 2026. It loads on `income-tax-workflow-base` and produces a side-by-side computation for a reviewer. Reply in the user's language, English or Arabic. Planning only: never concealment, fake invoices or sham entities.

**Answer first.** The main choice is the turnover regime of Law 6 of 2025 (tax on turnover, 0.4% to 1.5%, turnover up to EGP 20 million, locked for five years) against the general system (bands up to 27.5% on profit). Compute both before recommending. The Law 5 of 2025 relief windows have all closed; for old disputes, the dispute committees take new requests until 31 December 2026, and non-final 2023 to early 2025 periods of businesses up to EGP 10 million can be settled on turnover under Law 151 of 2026.

## Scope

- **Covers:** the regime choice, records and e-invoicing as levers, VAT registration timing, reliefs, settlement and dispute windows.
- **Mechanics sit elsewhere:** turnover regime in `eg-sme-tax`; bands, costs and losses in `eg-income-tax`; VAT in `egypt-vat`; books and e-documents in `eg-bookkeeping`.
- **Out:** companies' planning beyond the regime choice, cross-border structuring, transfer pricing, and anything needing concealment.

## Ask the client first

1. Turnover this year and last, and the expected turnover for the next five years.
2. Net profit, and how well costs are documented (e-invoices, regular books).
3. Is the client already in Law 6 (request date), or moved over from Law 152 of 2020?
4. If consulting: share of turnover from the top one or two clients.
5. Customers: businesses that recover VAT, or consumers?
6. Any unfiled year, open examination, dispute or ETA notice?

## The method, step by step

### Figures this skill owns

Band tables live in `eg-income-tax` and `eg-sme-tax`.

| Item | Amount | Conditions | Official URL |
|---|---|---|---|
| Dispute committees | Open to new requests until 31 December 2026 | Law 152 of 2026 art. 1 renews Law 79 of 2016; committees keep deciding pending requests | https://eta.gov.eg/sites/default/files/2026-08/law.no_.152.of_.2026.pdf |
| Dispute application | On the form to the ETA (or the Real Estate Tax Authority), or free of charge on its portal | MoF Decision 450 of 2026 art. 1, issued 16 August 2026 | https://eta.gov.eg/sites/default/files/2026-08/mof.qarar_.no_.450.of_.2026.pdf |
| Past-period turnover settlement | Turnover up to EGP 10 million a year (in words on the page) | Law 151 of 2026 art. 4: taxes not final on 29 July 2026, periods from 1 January 2023 (corrected from 2022 by the notice of 8 August 2026) to the last period before March 2025; never below the tax in the returns; the taxpayer may choose Law 91 instead; bands in `eg-sme-tax` | https://eta.gov.eg/sites/default/files/2026-08/law.no_.151.of_.2026.pdf |
| Same, correction | Start year 2023 | Correction notice, Official Gazette 32 bis, 8 August 2026 | https://eta.gov.eg/sites/default/files/2026-08/law.no_.149.150.151.of_.2026.retractation.pdf |
| Ceiling on delay charge or additional tax | 100% of the principal tax | Law 206 of 2020 new art. 45 bis, added by Law 7 of 2025 | https://eta.gov.eg/sites/default/files/2025-02/law_no.7.of_.2025.pdf |
| Turnover regime ceiling and tolerance | EGP 20 million (in words on the page); over by no more than 20%, once in five years, stays in at 1.5% | Law 6 art. 10 last para.; a larger or second overshoot ends the regime from the following year | https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf |

### Steps

1. Get turnover, profit, the state of the cost documents, and plans for five years (the Law 6 lock-in, art. 5).
2. Compute the general tax on profit with the `eg-income-tax` row table: total net income picks the row, rounded down to EGP 10.
3. Compute turnover times the `eg-sme-tax` band rate. Check the art. 3 conditions (returns on time; joined to the e-invoice or e-receipt system under the phase decisions and issuing documents) and the art. 4 exclusions (90% consultancy; improper entry, including splitting).
4. Add the non-rate effects of Law 6: no stamp duty or development fee, no notarisation or registration fees on formation, credit and land contracts (art. 7); no tax on gains from disposing of fixed assets (art. 8) or on dividends from the activity (art. 9); outside withholding and advance payments both ways (art. 11); quarterly VAT and only the annual payroll settlement (art. 12); examination only after five years (art. 12); simplified records (art. 13).
5. Weigh the general system's own levers: losses carried forward (`eg-income-tax`), depreciation, documented costs, and the cost of the regular books every taxpayer keeps from 29 July 2026 (Law 206 art. 38 as replaced by Law 150 of 2026).
6. Show both numbers, then recommend. Never recommend in the abstract, and never assert a saving without the computation.

### Why margin decides it

The turnover regime taxes turnover; the general system taxes profit. The decision turns on the profit margin (صافي الربح ÷ رقم الأعمال). The turnover regime is cheaper when turnover times the band rate is below the general tax on profit, so the break-even margin is about the band rate divided by the effective general rate on that profit.

- **High margin, few costs** (a freelance developer or consultant): profit is close to turnover, the general system taxes nearly all of it at up to 27.5%, and the turnover regime at 1.5% or less is far cheaper.
- **Thin margin** (trading or reselling): a small percentage of a large turnover can exceed the income tax on a small profit. Run the numbers.
- **Losses:** turnover tax is due even in a loss year; the general system charges nothing and carries the loss forward.

| Situation | Direction |
|---|---|
| Few costs, turnover up to EGP 20 million | Turnover regime, unless 90% or more of turnover is consulting for one or two persons |
| Thin margin, heavy documented costs | Compute: the general system often wins |
| Losses expected | General: turnover tax is due on a loss; losses carry forward (`eg-income-tax`) |
| Turnover above EGP 20 million outside the one-time tolerance | General is the only option |
| Plans to pass EGP 24 million, or a second breach within five years | General, or model the exit from the following year |
| Needs freedom to change within five years | General: no exit from Law 6 for five years |
| Poor cost documents | Fix the documents, then compare both |

### E-invoices and records

- **Turnover regime:** joining the ETA e-invoice or e-receipt system under the phase decisions and issuing the documents is a condition of the regime (Law 6 art. 3). Records are the MoF 420 simplified set.
- **General system:** costs are supported by regular books backed by documents (`eg-income-tax`). Input VAT on purchases needs an e-invoice from the supplier (`eg-bookkeeping`, from the ETA e-receipt FAQ).
- **Actions:** register on the ETA e-invoice or e-receipt system when named in a phase decision (check the inquiry lists in `eg-bookkeeping`); ask suppliers for e-invoices before paying; reconcile e-invoices to the books monthly.

### VAT registration timing

- The limit is EGP 500,000 of taxable and exempt sales (VAT Law 67 of 2016 art. 16; `egypt-vat`). It counts gross sales, not profit: a business with EGP 520,000 of sales and EGP 20,000 of profit is in.
- Monitor cumulative sales monthly and register within 30 days of reaching the limit. Voluntary early registration can pay where customers recover VAT and the business wants input credit on its costs (`egypt-vat`, Example 2).
- In the turnover regime, VAT returns are quarterly (Law 6 art. 12), a real compliance saving.

### Old periods and disputes

- **Law 5 of 2025 windows are closed.** The law took effect on 13 February 2025 (art. 11). Non-filers for periods from 2020 had six months to file original or amended returns without penalties (art. 3). Unregistered persons who applied to register within three months, extendable once by the Minister, were not assessed for earlier periods for income tax, VAT, stamp duty or the development fee, provided no ETA action had been taken and all documents were filed on every e-system (art. 2). Disputes over periods ended before 1 January 2020 had three months, extendable once for an equal period, to apply (art. 6): estimated assessments settled by paying 30% of the tax in the return, or the last agreement plus 40% where no return, a nil return or a loss return was filed, in four quarterly instalments of 25% with no delay charge (art. 4); regular-books assessments settled with 100% of delay charges and additional tax waived if the principal was paid within three months (art. 5). Individuals with real estate or unlisted share disposals had six months (art. 7). Every window, at its longest, ended by 13 August 2025.
- **Now:** use the dispute committees for requests filed until 31 December 2026 (Law 152 of 2026), or the Law 151 art. 4 turnover settlement if eligible. Late payment charges cannot exceed 100% of the principal (Law 7 of 2025).
- **Listed shares:** gains on Egyptian listed securities are exempt from 29 July 2026 and losses are neither deductible nor carried forward, unless the disposal delists the company (Income Tax Law art. 31 item 7, added by Law 151 of 2026 art. 2; `eg-income-tax`).
- **Band steps:** total net income just over EGP 600,000, 700,000, 800,000, 900,000 or 1,200,000 loses a lower band (`eg-income-tax`). Lawful timing of a real receipt or a real expense can matter; invented timing cannot.

## Boundary and exception table

| Situation | Rule | Source |
|---|---|---|
| Request form 10/1 not filed | Not in the turnover regime; general system | Law 6 art. 1; MoF 420 art. 1 |
| Wants out of Law 6 within five years | Not possible; form 11/1 only after five years from the day after the request | Law 6 art. 5; MoF 420 art. 1 |
| Consultant, 90% or more from one or two persons | Outside Law 6 unless the Minister excepts the activity | Law 6 art. 4(1) |
| One business split with no economic reason to stay under EGP 20 million | Outside Law 6; the ETA bears the burden of proof. Do not design it | Law 6 art. 4(2) |
| Turnover over EGP 20 million by no more than 20%, first time in five years | Stays in at 1.5% | Law 6 art. 10 |
| Over by more than 20%, or a second time | Regime ends from the following year | Law 6 art. 10 |
| Law 6 taxpayer files late or leaves the e-systems | Breaks the art. 3 conditions | Law 6 art. 3 |
| Asks about the Law 5 of 2025 relief | Closed by 13 August 2025 at the latest; use Law 152 committees or Law 151 art. 4 | Law 5 arts. 2, 3, 6, 7; Law 152; Law 151 |

## Worked cases

**Case A. Decision: developer, turnover EGP 1,800,000, costs EGP 200,000, profit EGP 1,600,000.** General: top row, 25% on 1,200,000 plus 27.5% on 400,000 = 410,000. Turnover regime: 0.5% = 9,000. The turnover regime saves 401,000, if the 90% consultancy test is passed and the five-year lock-in is accepted.

```oa-check
name: Developer regime decision
inputs:
  turnover: 1800000
  profit: 1600000
steps:
  - general: 1200000 * 0.25 + (profit - 1200000) * 0.275
  - simplified: turnover * 0.005
  - saving: general - simplified
expected:
  general: 410000.00
  simplified: 9000.00
  saving: 401000.00
```

**Case B. Decision the other way: trader, turnover EGP 9,000,000, profit EGP 350,000.** Turnover regime: 1% = 90,000. General, row "up to 600,000": 1,500 + 2,250 + 26,000 + 33,750 = 63,500. The general system saves 26,500, but only if every cost (about EGP 8.65 million) is documented by e-invoices and regular books. At a profit of EGP 600,000 the general tax is 124,750 and the turnover regime wins by 34,750: model the margin carefully.

```oa-check
name: Thin-margin trader decision
inputs:
  turnover: 9000000
  profit: 350000
steps:
  - simplified: turnover * 0.01
  - general: 1500 + 2250 + 26000 + (profit - 200000) * 0.225
  - general_saves: simplified - general
expected:
  simplified: 90000.00
  general: 63500.00
  general_saves: 26500.00
```

**Case C. New consultant, turnover EGP 240,000 in the first year, high margin.** Below the EGP 500,000 VAT limit, so registration is not yet required, but the e-invoice or e-receipt duty and any phase decision must still be checked. Compare the regimes now: 0.4% is EGP 960 against the general bands on profit. Monitor sales monthly and register for VAT within 30 days of reaching the limit. If growth is expected, weigh the five-year lock-in before filing form 10/1.

**Case D. Old dispute and unfiled amended returns for periods before 2020.** The Law 5 of 2025 windows closed by 13 August 2025. Use a dispute committee request filed by 31 December 2026, or the Law 151 art. 4 settlement if the business is eligible. If a Law 5 settlement was already accepted, pay the instalments on its schedule. Evaluate the regimes for current years separately.

## When to refuse or refer

Refuse, and offer a lawful alternative (the genuinely cheaper regime, better e-invoice documentation, timely registration, a dispute committee request or a settlement), when asked to:

- evade tax (التهرب الضريبي): under-report turnover or income, omit sales, keep two sets of books, or claim costs not incurred;
- issue or obtain fake, inflated or backdated invoices, or any document not reflecting a real transaction;
- split one business into sham entities to stay under EGP 20 million or the VAT limit, or to multiply access to low rates (Law 6 art. 4(2) excludes it, and late or avoided VAT registration is treated as evasion in `egypt-vat`);
- suppress or split turnover to avoid VAT registration;
- conceal assets, foreign income or related-party transactions, or pass private spending off as business cost;
- delay or skip filing to wait for the next amnesty.

When two readings of the law are possible, take the one that keeps the taxpayer compliant and safe on examination, even at a little more tax. Never present planning as guaranteed or as a substitute for a qualified reviewer. Refer open examinations, disputes, settlements, cross-border structures and company planning to a qualified Egyptian accountant.

## Filing and payment

Choosing the turnover regime: file form 10/1 طلبات on the ETA system (MoF 420 art. 1; steps in `eg-sme-tax`). Leaving after five years: form 11/1. Annual return dates are in `eg-income-tax` and `eg-sme-tax`. Dispute committee requests: on the form to the ETA, or free on its portal, until 31 December 2026.

## Completion checklist

- [ ] Inputs trace to documents; rates match 2026.
- [ ] Both systems computed; the row chosen on total net income.
- [ ] Law 6 conditions (art. 3) and exclusions (art. 4) checked; lock-in shown before recommending.
- [ ] No figure repeated from a sibling without its link.
- [ ] Old-period options checked against the current windows (Laws 151 and 152 of 2026), not Law 5.
- [ ] Nothing in the plan needs concealment.

## Sources

| Source | URL | Read on |
|---|---|---|
| Law 5 of 2025, arts. 1 to 11, whole text | https://eta.gov.eg/sites/default/files/2025-02/law_no.5.of_.2025.pdf | 2026-11-16 |
| Law 6 of 2025, arts. 1 to 16, whole text | https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf | 2026-11-16 |
| Law 7 of 2025, arts. 1 and 2 (new arts. 45 bis, 75 bis, 75 bis 1) | https://eta.gov.eg/sites/default/files/2025-02/law_no.7.of_.2025.pdf | 2026-11-16 |
| Law 151 of 2026, arts. 2, 4 to 7 | https://eta.gov.eg/sites/default/files/2026-08/law.no_.151.of_.2026.pdf | 2026-11-16 |
| Law 152 of 2026, arts. 1 and 2, whole text | https://eta.gov.eg/sites/default/files/2026-08/law.no_.152.of_.2026.pdf | 2026-11-16 |
| MoF Decision 450 of 2026, arts. 1 and 2 (page images read) | https://eta.gov.eg/sites/default/files/2026-08/mof.qarar_.no_.450.of_.2026.pdf | 2026-11-16 |
| Correction notice, Gazette 32 bis, 8 August 2026, page 8 table (page image read) | https://eta.gov.eg/sites/default/files/2026-08/law.no_.149.150.151.of_.2026.retractation.pdf | 2026-11-16 |
| Law 7 of 2024, art. 1 (Income Tax Law art. 8 bands) | https://eta.gov.eg/sites/default/files/2024-03/law_no.7-2024.pdf | 2026-11-16 |
| MoF Decision 420 of 2025, arts. 1 to 4 (page images read) | https://eta.gov.eg/sites/default/files/2025-12/mof.decision.no_.420.of_.2025.pdf | 2026-11-16 |
| VAT Law 67 of 2016, art. 16 (page image read) | https://eta.gov.eg/sites/default/files/2024-03/vat-law_no.67-2016.pdf | 2026-11-16 |
| Law 150 of 2026, art. 1 | https://eta.gov.eg/sites/default/files/2026-08/law.no_.150.of_.2026.pdf | 2026-11-16 |
| ETA list of VAT laws and decisions, list page read | https://eta.gov.eg/ar/content/qwanyn-aldrybt-ly-alqymt-almdaft | 2026-11-16 |

Not yet confirmed: the rule that, from 1 July 2023, only e-invoices prove costs for income tax for taxpayers on the e-invoice system. The reported cut of the VAT registration limit to EGP 250,000 under a Resolution 281 of 2025, with registration due before 31 March 2026 and a fine of EGP 20,000 plus EGP 1,000 a day: not in VAT Law art. 16 and not on the ETA VAT list read, so held (`egypt-vat` keeps 500,000). Whether MoF Decision 167 of 2025 extended the Law 5 art. 2 and art. 6 windows by three months from 13 May 2025 (the decision was not read; either way they ended by 13 August 2025). Whether any successor to Law 5 relief exists beyond Laws 151 and 152 of 2026.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-16. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `eg-tax-optimization` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/eg-tax-optimization. If neither is available, confirm every figure against the official source pages cited above before relying on it.
