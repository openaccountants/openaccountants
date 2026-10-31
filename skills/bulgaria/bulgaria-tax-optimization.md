---
name: bulgaria-tax-optimization
description: Use this skill whenever asked about reducing tax in Bulgaria, tax planning, or legal strategies to minimise tax for a freelancer, sole trader, or small company in Bulgaria, for tax year 2026 (in euro). Trigger on phrases like "reduce tax Bulgaria", "10% flat tax", "Bulgaria freelancer 7.5%", "svobodna profesiya", "normative expense deduction", "sole trader vs EOOD", "Bulgaria dividends 5%", "save tax Bulgaria", "Bulgaria tax haven", "tax planning Bulgaria". This skill covers the freelancer statutory deduction (25%, or 40% for some professions) that taxes 75% of income at 10%, so 7.5% of gross before contributions; the choice between freelancer, sole trader (15%) and EOOD (10% plus 5% dividend tax, 14.5% on distributed profit); the self-insured contribution base and its annual reconciliation; voluntary insurance and other reliefs; and the anti-avoidance red lines. Out of scope, handled by sibling skills; computing the return (bulgaria-income-tax, bg-corporate-income-tax), contributions in detail (bulgaria-social-contributions), VAT (bulgaria-vat-return), cross-border moves (bg-cross-border). ALWAYS read this skill before advising on any Bulgarian tax optimisation.
version: 0.2
jurisdiction: BG
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: tax-optimization
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bulgaria Tax Optimization

## Bulgaria Tax Optimization Skill v0.2

Tier 2. Built from the Bulgarian acts read on 30 October 2026 (listed under Sources). Figures must agree with `bulgaria-income-tax.md` and `bulgaria-social-contributions.md`; where they differ, those skills win. Not yet signed off by a Bulgarian tax adviser. Aggressive positions are never advised; every suggestion must be reviewed.

## Section 1 -- Quick Reference

**Section 1 Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Republic of Bulgaria |
| Currency | EUR from 1 January 2026. Lev amounts still in the laws convert at BGN 1.95583 = EUR 1 (Euro Introduction Act arts. 11(2), 12, 13) |
| Headline levers | Freelancer statutory deduction of 25% (40% for some professions), so **7.5%** of gross before contributions (6% at 40%); freelancer vs sole trader vs EOOD; 5% dividend tax |
| Personal income tax | **10% flat** on the general annual base (ZDDFL art. 48(1)); **15%** for sole traders (art. 48(2)) |
| Corporate tax (EOOD) | **10%** (ZKPO art. 20); dividend tax **5%** (ZDDFL arts. 38(1), 46(3)), so **14.5%** in total on profit that is fully paid out |
| Anti-avoidance | Deals that lead to tax evasion are disregarded (ZKPO art. 16(1)); a freelancer must not be disguised employment |

The Bulgarian headline is the FREELANCER regime (свободна професия, and also income under non-employment contracts). The law deducts a fixed share of income for costs, with no need to prove them: 25% for most liberal professions and contract income (ZDDFL art. 29(1)(3)). Only 75% of gross is taxable, and it is taxed at 10% (art. 48(1)), which is 7.5% of gross. The person's own social and health contributions then come off the base (art. 30(1)), so the tax is lower than 7.5% of gross. Authors, performing artists, crafts outside the patent tax, lawyers and notaries get 40% (art. 29(1)(2)), which gives 6% of gross before contributions.

## Section 2 -- Regime Election (the core decision)

**Regime election comparison table**

| Structure | Income tax | Best when |
| --- | --- | --- |
| **Freelancer** (свободна професия, self-insured) | 10% on gross less the 25% (or 40%) statutory deduction, less own contributions = **7.5% of gross** (6% at 40%) before contributions; real expenses are not deducted (ZDDFL arts. 29(1), 30(1), 48(1)) | Solo professionals and consultants with low real expenses |
| **Sole trader** (ET, едноличен търговец) | **15%** on the tax profit worked out under the Corporate Income Tax Act (real expenses), less own contributions (arts. 26(1), 28(1), 48(2)) | Rarely better than freelancer for solo work; the 15% rate is above the EOOD's 10% |
| **EOOD** (single-member limited company) | **10% CIT** (ZKPO art. 20), then **5%** dividend tax on what is paid out (ZDDFL arts. 38(1), 46(3)) = **14.5%** of profit if all is paid out | Real expenses are high, profit is kept in the company, there is a team, or liability and credibility matter |

- **Where the lines cross (before contributions).** With gross income G and real costs C:
  - Freelancer at 25%: tax = 10% x 75% x G = 7.5% of G.
  - EOOD, all profit paid out: tax = 10% x (G - C) + 5% x 90% x (G - C) = 14.5% of (G - C). This beats the freelancer only when real costs exceed about 48.3% of gross (1 - 7.5 / 14.5).
  - EOOD, all profit kept: tax = 10% of (G - C). This beats the freelancer once real costs exceed 25% of gross.
  - Sole trader: tax = 15% of (G - C). This beats the freelancer only when real costs exceed 50% of gross.
  - Example: gross EUR 50,000, real costs EUR 10,000. Freelancer EUR 3,750 (7.5% x 50,000). EOOD paying out everything EUR 5,800 (14.5% x 40,000). EOOD keeping everything EUR 4,000. Sole trader EUR 6,000.
- **Contributions change the result.** These lines ignore social and health contributions. A freelancer pays them on 75% of gross, within the monthly minimum and maximum (KSO art. 6(8), (9)). An owner who works in the EOOD is self-insured as well (KSO art. 4(3)(2)), and a company manager is insured for all risks, like an employee (art. 4(1)(7)). Model both structures with the contributions in `bulgaria-social-contributions.md` before choosing. We give no fixed revenue tipping point.

## Section 3 -- Dividends & Profit Extraction (EOOD)

- **EOOD profit taxation.** EOOD profit is taxed at 10% CIT (ZKPO art. 20). The 5% dividend tax arises only when a dividend is paid out, so profit kept in the company carries 10% until it is distributed (ZDDFL arts. 38(1), 46(3)).
- **Dividend tax.** 5% final tax on dividends and liquidation shares paid to an individual (ZDDFL arts. 38(1), 46(3)). The company withholds it and pays it by the end of the month after the quarter in which the dividend was voted (art. 65(2)). Fully paid out, profit bears 14.5% in total.
- **Manager remuneration.** A manager under a management contract is insured for all risks (KSO art. 4(1)(7)). An owner who works in the company is self-insured (art. 4(3)(2)). A modest manager's remuneration can carry the social insurance while the rest is taken as dividends, but the role and the pay must be genuine. The minimum insurable income for a manager is not yet confirmed (see Not yet confirmed).

## Section 4 -- Deductions & Contributions

**Deductions and contributions table**

| Item | Treatment |
| --- | --- |
| Freelancer statutory deduction | 25% of gross (40% or 60% for the categories in ZDDFL art. 29(1)(1), (2)); no documents needed; real expenses cannot be deducted on top, because the law fixes the cost deduction (art. 29(1)). |
| EOOD real expenses | Business costs reduce the 10% CIT base under the Corporate Income Tax Act; see `bg-corporate-income-tax.md` for what is not deductible. |
| Social and health contributions | The contributions a self-insured person must pay for the year come off the taxable income (ZDDFL art. 30(1) for freelancers, art. 28(1) for sole traders). During the year the self-insured pay advances on a monthly income they choose between the minimum and maximum (KSO art. 6(8)). For 2026: minimum EUR 550.66 (1 January to 31 July) and EUR 620.20 (1 August to 31 December); maximum EUR 2,111.64 and then EUR 2,300 (2026 State Social Insurance Budget Act art. 9). After the year, the final insurable income is fixed from the annual tax return, within the same minimum and maximum, and the difference is paid (KSO art. 6(9)). So choosing the minimum lowers the advances, not the final bill, unless actual income is at the minimum. See `bulgaria-social-contributions.md`. |
| Voluntary pension, health and life insurance | Personal contributions to voluntary supplementary pension insurance: deductible up to 10% of the annual bases. Personal voluntary health insurance contributions and life insurance premiums: deductible up to a further 10% (ZDDFL art. 19(1); for sole traders art. 28(2)(1)). |

## Section 5 -- Reliefs

**Reliefs table**

| Relief | Detail |
| --- | --- |
| Children relief | For 2026 the annual base is reduced by EUR 3,067.75 for one child under 18, EUR 6,135.50 for two and EUR 9,203.25 for three or more; a child with 50% or more disability adds EUR 6,135.50 (ZDDFL arts. 22v, 22g, with the 2026 amounts set by the 2026 State Budget Act, transitional provisions § 3(1), (2)). Only one parent claims (ZDDFL art. 22v(4)). An employee may take EUR 255.65, 511.29 or 766.94 a month (EUR 511.29 for a disabled child) off the monthly employment base (§ 3(4)). Any part not used against the general base comes off a sole trader's base (§ 3(3)). How to claim is in `bulgaria-income-tax.md`. |
| Early-filing discount | 5% of the tax still due, if the return is filed electronically and the tax paid by 31 March, with no debts under enforcement. It applies to both the 10% and the 15% tax; the total discount is capped at BGN 500, which is EUR 255.65 (ZDDFL art. 53(6)). |
| Personal contributions | Mandatory contributions reduce the taxable base (ZDDFL arts. 28(1), 30(1)). |

## Section 6 -- Red Lines (do not cross)

- **Disguised employment.** A "freelancer" working for a single client under employer-like control can be treated as an employee. AUDIT FLASH POINT.
- **Substance requirement.** Where one or more deals, including between unrelated parties, lead to tax evasion, the tax base is set without regard to those deals, their terms or their legal form (ZKPO art. 16(1)). An EOOD used only to turn salary into dividends taxed at 5%, without a genuine business, can be challenged.
- **Minimum insurable income vs under-declaring.** Choosing the minimum monthly insurable income for advances is legal (KSO art. 6(8)). The final contributions still follow the income declared on the annual return (art. 6(9)). Under-declaring income is not legal.

## PROHIBITIONS

- **Combining deductions.** NEVER combine the statutory deduction with real-expense deductions. It is one or the other.
- **Disguised employment presentation.** NEVER present the freelancer regime for what is really single-client employment.
- **Under-declaring income.** NEVER advise under-declaring income to cut tax or contributions.
- **Contradicting rates.** NEVER contradict the rates in `bulgaria-income-tax.md` / `bulgaria-social-contributions.md`.
- **Unconfirmed points.** NEVER present a "Not yet confirmed" point as settled, nor optimisation as definitive advice. Route the client to a licensed Bulgarian tax adviser.

## Sources

| Source | URL | Read on |
|---|---|---|
| Personal Income Taxes Act (ZDDFL), consolidated to State Gazette 85/2026: arts. 19, 22v, 22g, 26, 28, 29, 30, 38, 46, 48, 53, 65 (art. 22v still prints the old lev amounts; the 2026 amounts come from the State Budget Act below) | https://lex.bg/laws/ldoc/2135538631 | 2026-10-30 |
| Corporate Income Tax Act (ZKPO), consolidated to State Gazette 55/2026: arts. 16, 20 | https://lex.bg/laws/ldoc/2135540562 | 2026-10-30 |
| Social Insurance Code (KSO), consolidated to State Gazette 68/2026: arts. 4, 6 | https://lex.bg/laws/ldoc/1597824512 | 2026-10-30 |
| State Social Insurance Budget Act for 2026, State Gazette 68/2026, art. 9 (copy published by the National Social Security Institute) | https://nssi.bg/wp-content/uploads/zbdoo-2026.pdf | 2026-10-30 |
| State Budget Act of the Republic of Bulgaria for 2026, State Gazette 69/2026, transitional and final provisions § 3 (2026 child relief amounts) | https://www.parliament.bg/bg/laws/ID/167157 | 2026-10-30 |
| Euro Introduction Act, arts. 11, 12, 13 | https://lex.bg/bg/laws/ldoc/2137244903 | 2026-10-30 |
| Bulgarian National Bank, National Euro Changeover Plan (the fixed rate BGN 1.95583 = EUR 1) | https://www.bnb.bg/bnbweb/groups/public/documents/bnb_download/eurochangeoverplan_en.pdf | 2026-10-30 |

Not yet confirmed: the minimum insurable income for a manager under a management contract; the Labour Code provision under which disguised employment is reclassified (not read); the old "EUR 100,000 to 150,000" freelancer-vs-EOOD tipping point (from a private adviser's site, no official source; replaced by the cost-share comparison in Section 2); the old claim that 7.5% is the lowest effective rate in the EU (no official source).

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed tax adviser in Bulgaria) before acting upon.

The most up-to-date version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
