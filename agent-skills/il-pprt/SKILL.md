---
name: il-pprt
description: "Compute Illinois corporate income tax and Personal Property Replacement Income Tax for 2026. C corporations pay 7% income tax plus 2.5% replacement tax on Form IL-1120 (9.5% together); S corporations (IL-1120-ST), partnerships (IL-1065) and trusts pay 1.5% replacement tax; sole proprietors and disregarded single-member LLCs owned by individuals pay none. Covers base income, the single sales factor with market sourcing and throwback, the $1,000 standard exemption (zero for corporations), the $500,000 corporate net loss cap for 2026, the partnership subtraction for partner compensation, due dates, the $400 corporate estimated tax test, and the elective 4.95% pass-through entity tax with its owner credit and $500 estimated tax test. Trigger on \"Illinois corporate income tax\", \"Illinois replacement tax\", \"PPRT\", \"IL-1120\", \"IL-1120-ST\", \"IL-1065\", \"Illinois PTE tax\", \"Illinois SALT workaround\"."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/il-pprt"
  jurisdiction: "US-IL"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Illinois corporate income tax and replacement tax (IL-1120, IL-1120-ST, IL-1065), tax year 2026

> **Source-cited draft.** Built from 35 ILCS 5/201, 5/203, 5/204, 5/207, 5/304, 5/505, 5/803 and 5/804 (Illinois General Assembly), IDOR Informational Bulletin FY 2026-15 and IDOR Publication 105, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** Illinois taxes a C corporation's net income at **7%** income tax (35 ILCS 5/201(b)(14)) plus **2.5%** Personal Property Replacement Income Tax (201(c), (d)), **9.5%** in total, on Form IL-1120. S corporations, partnerships and trusts pay no income tax at the entity level but pay **1.5%** replacement tax on their net income (201(d)); the owners pay Illinois income tax on their shares. Sole proprietors, and single-member LLCs disregarded into an individual, pay no replacement tax. Business income is apportioned by the **sales factor alone** (304(h)(3)). A C corporation's net loss carryover deduction is capped at **$500,000** for a 2026 calendar year (207(d)(3)). A partnership or S corporation may elect the **4.95%** pass-through entity tax, which gives each owner an equal credit and moves the state tax into a federal business deduction.

## Scope and who this is for

In scope: tax year 2026 Illinois returns of C corporations (IL-1120), S corporations (IL-1120-ST) and partnerships including multi-member LLCs (IL-1065): which taxes apply, the base, apportionment, the standard exemption, net losses, due dates, estimated tax and the pass-through entity tax election.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Federal corporate taxable income (Form 1120) | `us-form-1120-c-corp` |
| Federal partnership return (Form 1065) | `us-form-1065-partnership` |
| Whether to elect S corporation status | `us-s-corp-election-decision` |
| State pass-through entity taxes in other states | `us-pte-state-matrix` |
| The owner's Illinois Form IL-1040 | `il-income-tax` |
| Federal bonus depreciation figures | `us-section-179-and-bonus-depreciation` |
| Unitary combined returns (Schedule UB), insurance, financial and transportation companies | refer (see the refusal table) |

## Ask the client first

1. **Federal classification** of the entity (C corporation, S corporation, partnership, disregarded entity) and, for a disregarded entity, who owns it.
2. **Federal taxable income** (C corporation) or **ordinary income and separately stated items** (S corporation, partnership), and the federal return.
3. **Sales everywhere and sales sourced to Illinois**: goods shipped to Illinois customers, goods shipped from Illinois to the U.S. government or to states where the business is not taxable, and services received in Illinois.
4. **Illinois net loss carryovers** by year (C corporation).
5. **Partner compensation or personal service income** (partnership), and owners that are themselves subject to replacement tax.
6. **Bonus depreciation** claimed federally in 2026.
7. **Whether the partnership or S corporation wants the pass-through entity tax** for 2026, and the owners' residence states.
8. **Members of a unitary group** under common control.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Corporate income tax, taxable years beginning on or after 1 July 2017 | 7% | [35 ILCS 5/201(b)(14)](https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K201) |
| Replacement tax, corporations other than S corporations (from 1 January 1981) | 2.5% | [35 ILCS 5/201(d)](https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K201) |
| Replacement tax, partnerships, trusts and S corporations | 1.5% | [35 ILCS 5/201(d)](https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K201) |
| Pass-through entity tax, elective, partnerships (not publicly traded) and S corporations | 4.95% | [35 ILCS 5/201(p)(2)](https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K201) |
| Owner credit for pass-through entity tax: rate times distributive share of net income, capped at the tax actually paid | 4.95% | [35 ILCS 5/201(p)(4)](https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K201) |
| Standard exemption (basic amount), partnerships and trusts | $1,000 | [35 ILCS 5/204(b)](https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K204) |
| Standard exemption, corporations, tax years ending on or after 31 December 2003 | $0 | [35 ILCS 5/204(b)](https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K204) |
| Net loss carryover deduction cap, corporations other than S corporations, tax years ending on or after 31 December 2024 and before 31 December 2027 | $500,000 | [35 ILCS 5/207(d)(3)](https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K207) |
| Net loss carryover cap, tax years ending in 2027 (before 31 December 2028) | greater of 15% of net income or $500,000 | [35 ILCS 5/207(d)(4)](https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K207) |
| Net loss carryforward period, losses in tax years ending on or after 31 December 2021 | 20 years | [35 ILCS 5/207(a)(4)](https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K207) |
| Apportionment, tax years ending on or after 31 December 2000 | sales factor only | [35 ILCS 5/304(h)(3)](https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K304) |
| Corporate estimated tax required if expected tax is more than | $400 | [35 ILCS 5/803(a)](https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K803) |
| Pass-through entity tax estimated payments required if expected tax exceeds | $500 | [35 ILCS 5/201(p)(9)](https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K201) |
| Late estimated payment penalty: 1 to 30 days late; 31 days or later | 2%; 10% of the tax due | [IDOR Publication 105](https://tax.illinois.gov/research/publications/pubs/illinois-estimated-payments-requirements-for-individuals-and-businesses.html) |

All of these rates and caps are in the statute and are not indexed.

### Who pays what

| Entity (federal classification) | Illinois income tax | Replacement tax | Return |
| --- | --- | --- | --- |
| C corporation, including an LLC that elected corporate status | 7% | 2.5% | IL-1120 |
| S corporation, including an LLC that elected S status | none at entity level | 1.5% | IL-1120-ST |
| Partnership, including a multi-member LLC | none at entity level | 1.5% | IL-1065 |
| Trust | 4.95% on income taxed to the trust (201(b)(5.4)) | 1.5% | IL-1041 (refer) |
| Estate | 4.95% (201(b)(5.4)) | none: 201(c) reaches corporations, partnerships and trusts only | IL-1041 (refer) |
| Sole proprietor, or disregarded single-member LLC owned by an individual | owner's 4.95% on IL-1040 | none | IL-1040 (`il-income-tax`) |
| Disregarded single-member LLC owned by a corporation | in the owner's return | owner's rate | owner's return |

There is no credit against an owner's Illinois income tax for replacement tax paid by a partnership or S corporation: the old replacement tax credit in 201(i) applies only to tax years ending before 31 December 2003.

### From federal income to Illinois tax

1. **Base income** (35 ILCS 5/203): start from federal taxable income (C corporation) or the federal ordinary income and separately stated items (partnership, S corporation), then add and subtract the Schedule M items. Common ones: add back the bonus depreciation deduction taken under section 168(k) and, for taxable years 2026 and later, 168(n), and subtract the depreciation without bonus; a partnership subtracts the greater of its personal service income or a reasonable allowance for partner compensation (203(d)(2)(H)) and income distributable to partners that are themselves subject to replacement tax (203(d)(2)(I)); an S corporation subtracts income allocable to shareholders subject to replacement tax (203(b)(2)(S)).
2. **Allocate nonbusiness income** to the state named in Article 3, and **apportion business income** by the sales factor: Illinois sales / sales everywhere (304(a)(3)(A), 304(h)(3)).
   - Goods are in Illinois if delivered to a purchaser in Illinois (other than the U.S. government), or if shipped from Illinois and either the purchaser is the U.S. government or the seller is not taxable in the purchaser's state (throwback, 304(a)(3)(B)).
   - Services are in Illinois if received in Illinois. For a business customer, receipts are attributed only to a state where the customer has a fixed place of business; if that is not determinable, to the customer's ordering office, then to its billing office (304(a)(3)(C-5)(iv)).
   - Patents, copyrights and trademarks: where the item is used (304(a)(3)(B-1)).
3. **Net income** = Illinois business income + Illinois nonbusiness income - standard exemption ($1,000 for a partnership or trust; zero for a corporation) - net loss deduction (corporations other than S corporations: at most $500,000 in 2026).
4. **Tax**: C corporation 7% + 2.5% of net income; S corporation, partnership or trust 1.5% of net income.
5. **Pass-through entity tax, if elected** (201(p)): 4.95% of net income computed without the standard exemption, without the net loss deduction, and, for an S corporation, without 203(b)(2)(S), and for a partnership without 203(d)(2)(H) and (I). For taxable years ending on or after 31 December 2026, a partnership may choose each year between the full distributive share method (tax the full share of each Illinois resident partner; apportioned income only for nonresidents) and the Illinois-sourced income method (201(p)(2.1)). Each owner gets a credit of 4.95% of its distributive share, capped at its share of the tax actually paid; an excess over the owner's Illinois liability is an overpayment (refundable). The election is annual, made on the return, irrevocable for the year, and binds all owners. Pass-through withholding under 709.5 does not apply for an electing year. A nonresident owner whose only Illinois income is from electing entities, with credits covering the tax, need not file an Illinois return (201(p)(5)). The tax applies only for years in which the federal SALT deduction limit of section 164(b)(6) applies (201(p)(10)); IDOR reports that Public Act 104-0453 removed the earlier expiration date (Bulletin FY 2026-15).

### 2025 and 2026 changes for business returns (Bulletin FY 2026-15)

- For tax years beginning on or after 1 January 2026, Illinois decouples from federal 100% bonus depreciation claimed under section 168(n) as well as 168(k) (Public Act 104-0453; Form IL-4562 line 16).
- For tax years ending on or after 31 December 2025: unitary groups use the Finnigan method on Schedule UB; two safe harbor exceptions are removed from the 80/20 related-party interest and intangible expense add-backs; interest allocations follow the federal section 163(j) rules; the dividends received deduction for net CFC tested income (formerly GILTI) is limited to 50% of the amount recognized (Schedule J).
- For tax years ending on or after 16 June 2025, gain or loss on selling S corporation shares or partnership interests (other than investment partnerships) is allocable to Illinois if the entity is taxable in Illinois (Schedule NB line 9).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Schedule C sole proprietor, or single-member LLC disregarded into an individual | No replacement tax; only the owner's 4.95% (`il-income-tax`) |
| Same business taxed as an S corporation | Adds 1.5% replacement tax at the entity, with no owner credit for it |
| C corporation with an Illinois net loss carryover of more than $500,000 | Deduct at most $500,000 in 2026; the rest carries on (years with the cap applied are not counted against the 20) |
| S corporation with a net loss | The $500,000 cap does not apply (207(d) covers corporations other than S corporations) |
| Goods shipped from an Illinois warehouse into a state where the seller is not taxable | Illinois sale (throwback) |
| Services to a business customer with no fixed place of business where the service is received | Ordering office, then billing office |
| Service partnership with partner compensation | Subtract the greater of personal service income or reasonable partner compensation before the 1.5% (203(d)(2)(H)); this subtraction does not apply to the pass-through entity tax base |
| Pass-through entity tax electing year | Estimated payments required if the tax will exceed $500; no 709.5 withholding |
| Partnership or S corporation not electing the pass-through entity tax | No estimated tax requirement (803(a)) |
| Corporation with expected tax over $400 | Four estimated installments of 25%, due on the 15th of the 4th, 6th, 9th and 12th months; short years are not exempt |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Federal classification | Follow the federal return; do not reclassify |
| Customer location for services | Billing office, as the last fallback in 304(a)(3)(C-5)(iv) |
| Whether the seller is taxable in the destination state | Assume not taxable there (throwback applies) until nexus in that state is shown |
| Partner compensation figure | No subtraction until a reasonable-compensation analysis is documented |
| Pass-through entity tax election | Do not elect without the owners' written consent and a federal benefit computation |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| Apportionment factor near 0% or 100% for a multistate business | Often a sourcing error (throwback, services) |
| C corporation with large old losses | $500,000 cap in 2026; cap rules change from 2027 |
| Old plan assumes an owner credit for replacement tax | That credit ended in 2003 |
| Old plan applies a $1,000 exemption to a C corporation | Zero since 2003 |
| Federal bonus depreciation on qualified production property (168(n)) | Illinois add-back from 2026 |

## Worked cases

**Case 1, a C corporation with a capped net loss.** A calendar-year C corporation has 2026 base income of $900,000, all business income. Its sales are $5,000,000 everywhere and $3,000,000 in Illinois. It has an Illinois net loss carryover of $800,000.

Factor 60%. Illinois business income $540,000. Net loss deduction capped at $500,000. No standard exemption for a corporation. Net income $40,000. Income tax 7% = $2,800; replacement tax 2.5% = $1,000; total **$3,800**. Carryover left: $300,000.

```oa-check
name: Illinois C corporation with the 500,000 loss cap (2026)
inputs:
  base_income: 900000
  il_sales: 3000000
  total_sales: 5000000
  nol_carryover: 800000
  nol_cap: 500000
steps:
  - factor: il_sales / total_sales
  - il_income: base_income * factor
  - nol_used: min(nol_carryover, nol_cap, il_income)
  - net_income: il_income - nol_used
  - income_tax: net_income * 0.07
  - replacement_tax: net_income * 0.025
  - total_tax: income_tax + replacement_tax
  - nol_left: nol_carryover - nol_used
expected:
  factor: 0.6
  il_income: 540000.00
  net_income: 40000.00
  income_tax: 2800.00
  replacement_tax: 1000.00
  total_tax: 3800.00
  nol_left: 300000.00
```

**Case 2, a decision: should a two-partner partnership elect the 2026 pass-through entity tax?** A partnership owned 50/50 by two Illinois residents earns $200,000 of rental net income, all in Illinois, with no personal service income or partner compensation subtraction. Both partners itemize and are capped by the federal SALT limit, and each is in the 24% federal bracket.

Replacement tax either way: ($200,000 - $1,000) x 1.5% = $2,985. With the election, the partnership also pays 4.95% x $200,000 = $9,900 (no standard exemption in that base), and each partner gets a credit of 4.95% x $100,000 = $4,950, which wipes out the $4,950 Illinois income tax on the share. The Illinois cash cost is the same; the difference is federal: the $9,900 becomes a partnership deduction, cutting each partner's federal income by $4,950 and federal tax by about $1,188, about **$2,376** together. Recommend the election, made on the 2026 IL-1065, with estimated payments because the tax exceeds $500.

```oa-check
name: Illinois partnership, pass-through entity tax election (2026)
inputs:
  net_income: 200000
  partner_share: 0.5
  federal_rate: 0.24
steps:
  - replacement_tax: (net_income - 1000) * 0.015
  - pte_tax: net_income * 0.0495
  - credit_each: min(net_income * partner_share * 0.0495, pte_tax * partner_share)
  - partner_il_tax_each: net_income * partner_share * 0.0495
  - federal_saving_total: pte_tax * federal_rate
expected:
  replacement_tax: 2985.00
  pte_tax: 9900.00
  credit_each: 4950.00
  partner_il_tax_each: 4950.00
  federal_saving_total: 2376.00
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-CT-UB | Unitary business group, combined return (Schedule UB), Finnigan apportionment | Refer |
| R-CT-SPEC | Insurance company, financial organization, transportation company, federally regulated exchange | Refer: special apportionment |
| R-CT-TRUST | Trust or estate (IL-1041) | Refer |
| R-CT-TIER | Tiered partnerships with the pass-through entity tax | Refer: 201(p)(3)(B) |
| R-CT-NB | Nonbusiness income allocation, or the sale of an interest in an S corporation or partnership | Refer |
| R-CT-CRED | EDGE, REV, MICRO, AIM, film, research and other certificate credits | Refer |
| R-CT-709 | Pass-through withholding for nonresident owners of a non-electing entity (709.5) | Refer |

## Filing and payment

| Return | Due date for a calendar 2026 year | Source |
| --- | --- | --- |
| IL-1120 (C corporation) | 15th day of the third month, or the later federal due date: 15 April 2027 for a calendar-year C corporation | [35 ILCS 5/505(a)(1)](https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K505) |
| IL-1120-ST (S corporation) | 15th day of the third month: 15 March 2027 | 35 ILCS 5/505(a)(1) |
| IL-1065 (partnership) | 15th day of the fourth month: 15 April 2027 | [35 ILCS 5/505(a)(2)](https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K505) |

Extensions under 505 may not exceed 6 months in total; a federal extension filed with IDOR extends the Illinois date by the same period, plus one more month for corporations (505(b)). An extension of time to file does not extend the time to pay. Corporate estimated payments (expected tax over $400) and pass-through entity tax estimated payments (over $500) are due on the 15th day of the 4th, 6th, 9th and 12th months: 15 April, 15 June, 15 September and 15 December 2026 for a calendar year (803(d); Publication 105). Each is 25% of the lesser of 90% of the 2026 tax or 100% of a 12-month 2025 tax that showed a liability (804(c)). File and pay through MyTax Illinois or approved software; IL-1040-ES vouchers are not used by these filers.

## Completion checklist

- Federal classification confirmed; sole proprietors and individual-owned disregarded LLCs excluded.
- Base income built from the federal return with Schedule M items (bonus depreciation 168(k) and 168(n), partner compensation, 80/20 add-backs).
- Sales factor with throwback for goods and fixed-place-of-business sourcing for services.
- No standard exemption for a corporation; $1,000 for a partnership or trust.
- Corporate net loss deduction capped at $500,000.
- Pass-through entity tax decision documented, with owners' consent and estimated payments if over $500.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 35 ILCS 5/201 (Illinois General Assembly). Read for (b)(5.4) 4.95%, (b)(14) 7%, (c) the replacement tax on corporations, partnerships and trusts, (d) 2.5% and 1.5%, (i) the replacement tax credit ending in 2003, (p) the pass-through entity tax: (1), (2), (2.1), (3), (4), (5), (8), (9) $500, (10). | https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K201 | 2026-11-13 |
| 35 ILCS 5/203. Read for the bonus depreciation add-back and subtraction, (b)(2)(S) and (d)(2)(H) and (I). | https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K203 | 2026-11-13 |
| 35 ILCS 5/204. Read for (b) the $1,000 basic amount and zero for corporations from 2003. | https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K204 | 2026-11-13 |
| 35 ILCS 5/207. Read for (a)(4) 20 years and (d) the corporate caps: $500,000 to 2027, then 15% to 80% or $500,000. | https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K207 | 2026-11-13 |
| 35 ILCS 5/304. Read for (a)(3)(A) the sales factor, (B) goods and throwback, (B-1) intangibles, (C-5)(iv) services, (h)(3) sales factor only. | https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K304 | 2026-11-13 |
| 35 ILCS 5/505. Read for (a)(1) corporate and (a)(2) partnership due dates and (b) extensions. | https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K505 | 2026-11-13 |
| 35 ILCS 5/803. Read for (a) the $400 corporate test and the partnership and S corporation exclusion, (d) the December 15 corporate installment. | https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K803 | 2026-11-13 |
| 35 ILCS 5/804. Read for (c) 25%, 90% and 100%. | https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K804 | 2026-11-13 |
| IDOR Informational Bulletin FY 2026-15. Read for the 2025 and 2026 business changes (168(n), Finnigan, 80/20, 163(j), NCTI 50%, Schedule NB line 9, PTE expiration removed). | https://tax.illinois.gov/research/publications/bulletins/fy-2026-15.html | 2026-11-13 |
| IDOR Publication 105 (December 2025). Read for the $400 and $500 business tests, the business installment dates and the 2% and 10% penalty. | https://tax.illinois.gov/research/publications/pubs/illinois-estimated-payments-requirements-for-individuals-and-businesses.html | 2026-11-13 |

Illinois sites refused direct connections from this machine; every page above was read through a Firecrawl fetch of the official URL on 2026-11-13.

Not yet confirmed: whether an S corporation gets the $1,000 standard exemption (204(b) gives corporations zero; the IL-1120-ST instructions were not read, so no S corporation exemption is used above); the 2026 IL-1120, IL-1120-ST and IL-1065 instructions and line numbers (not read); IDOR's automatic extension practice for 2026 business returns; whether the pass-through entity tax deducted federally is added back in the entity's and owners' Illinois base income (assumed in Case 2, provision not read); the unitary 80% and 80/20 rules in 35 ILCS 5/1501(a)(27) (not read); the distribution of replacement tax revenue to local governments (30 ILCS 115/12, not read).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `il-pprt` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/il-pprt. If neither is available, confirm every figure against the official source pages cited above before relying on it.
