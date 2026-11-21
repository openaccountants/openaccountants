---
name: eg-investment-incentives
description: "Egyptian investment incentives for tax year 2026 under Investment Law No. 72 of 2017 as amended by Law No. 160 of 2023, with its executive regulations. Covers the general incentives (stamp tax and notary fee exemption for five years, the 2% unified customs rate on equipment), the special incentive (a deduction from taxable profit of 50% of investment costs in sector A or 30% in sector B, capped at 80% of paid-in capital and seven years), the new cash incentive of 35% to 55% of the income tax paid for listed industries, the additional incentives, the single approval for strategic projects (Golden License) and the free zone fees. Trigger on: Egypt investment incentives, special incentive Egypt, sector A sector B, cash incentive Egypt, golden license Egypt, حوافز الاستثمار, الرخصة الذهبية, free zone fee Egypt. Out of scope: the company tax computation (eg-corporate-tax), customs procedure (eg-customs), VAT (egypt-vat)."
jurisdiction: EG
tax_year: 2026
last_updated: 2026-11-21
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: corporate-tax
category: international
type: computation
version: 1.0
---

# Egypt Investment Incentives v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Work out which incentives of the Investment Law No. 72 of 2017 a project can claim in 2026, and how much they are worth. Law No. 160 of 2023 (Official Gazette 29 bis, 25 July 2023, in force from 26 July 2023 under its art. 3, corrected in Gazette 32, 10 August 2023) replaced arts. 1 (definition of special incentives), 9, 11 first para. item 1, 12 first para. item 2, 13, 14 first para., 17, 20, 34 and 40 second and third paras., and added art. 11 bis (the cash incentive). The General Authority for Investment and Free Zones (GAFI) runs the law and issues the incentive certificate. Reply in the user's language, English or Arabic. Amounts are in EGP.

The incentives sit on top of the ordinary taxes. Compute the company's profit and tax in `eg-corporate-tax`, then apply the deduction or cash incentive here. Customs procedure is in `eg-customs`; VAT, including free zone treatment, in `egypt-vat`; stamp tax in `eg-stamp-duty`. Customs Law 207 of 2020 keeps the Investment Law's customs rules (its issuing art. 1 item 4).

## Ask the client first

1. Is the project under the Investment Law, and under which system: inland investment, investment zone, technology zone or free zone (free zone projects get none of the general incentives, art. 9)?
2. Is it a new company or establishment founded for the project, when was it founded, and when did it start activity (the GAFI start-date report)? Or is it an expansion of an existing project?
3. Where is it and what does it do: sector A or sector B under the Prime Minister's sector decree and Regulations art. 10?
4. Investment costs (equity plus long-term liabilities invested in fixed and paid intangible assets plus working capital), and paid-in capital up to the start of activity?
5. For the cash incentive: is the industry and area on the Cabinet decree under art. 11 bis, and was at least 50% of funding to the start of activity foreign currency from abroad?
6. Did any shareholder bring in physical assets of a company that existed when the Investment Law took effect, or liquidate one to set up this project (art. 12 item 4)?

## The method, step by step

### Key figures [Investment Law 72/2017 as amended](https://www.customs.gov.eg/Upload/ECAAdminace/ECAAdminace316621937.pdf)

| Item | Rate or amount | Conditions | Official URL |
|---|---|---|---|
| Special incentive, sector A | 50% of investment costs, deducted from net taxable profit | New project under the investment map in the areas most in need of development (art. 11 item 1, replaced by Law 160/2023) | https://www.customs.gov.eg/Upload/ECAAdminace/ECAAdminace999139060.pdf |
| Special incentive, sector B | 30% of investment costs, deducted from net taxable profit | Listed project types in the rest of Egypt (art. 11 item 2) | https://www.customs.gov.eg/Upload/ECAAdminace/ECAAdminace316621937.pdf |
| Special incentive cap | 80% of paid-in capital to the start of activity; seven years from start | Art. 11 | same |
| Cash incentive (art. 11 bis) | 35% to 55% of the income tax paid with the return on the project's income | Listed industrial activities and areas; not taxable income; paid within 45 days after the return deadline | https://www.customs.gov.eg/Upload/ECAAdminace/ECAAdminace999139060.pdf |
| Cash incentive funding test | At least 50% foreign currency from abroad | Funding to the start of activity (art. 11 bis) | same |
| Cash incentive start window | Activity within six years from 26 July 2023, extendable by up to six years | Art. 11 bis | same |
| Cash incentive period | Up to ten years per industry or area | Set by Cabinet decree (art. 11 bis) | same |
| Unified customs rate | 2% of value | Machinery, equipment and devices needed to set up the company; also public utility projects (art. 10) | https://www.customs.gov.eg/Upload/ECAAdminace/ECAAdminace316621937.pdf |
| Stamp tax and notary fee exemption | Five years from commercial register entry | Incorporation contracts and linked credit facility and mortgage contracts (art. 10) | same |
| Infrastructure contribution relief | Up to 50% | Art. 13, by Prime Minister decree | https://www.customs.gov.eg/Upload/ECAAdminace/ECAAdminace999139060.pdf |
| Treasury share of utility consumption | Up to 50%, for up to ten years | Art. 13 | same |
| Social responsibility spending | Up to 10% of annual net profit is deductible | Art. 15, through Income Tax Law art. 23 item 8 | https://www.customs.gov.eg/Upload/ECAAdminace/ECAAdminace316621937.pdf |

### 1. General incentives for every project [arts. 9, 10](https://www.customs.gov.eg/Upload/ECAAdminace/ECAAdminace999139060.pdf)

Every investment project under the law, whether set up before or after it and under any legal system, gets the general incentives, except projects under the free zone system (art. 9, replaced by Law 160/2023). They are (art. 10):
- exemption from stamp tax and from notarisation and registration fees on company and establishment incorporation contracts and on credit facility and mortgage contracts linked to their business, for five years from entry in the commercial register, and on land registration contracts needed to set up the company (details in `eg-stamp-duty`);
- a unified customs rate of 2% of value on all machinery, equipment and devices imported to set up the company, and on those imported by companies working in public utility projects to set them up or complete them;
- for industrial projects, import of moulds, dies and similar production items free of customs duty for temporary use in making products and re-export.

### 2. The special incentive: a deduction from taxable profit [arts. 11, 12; Regulations arts. 10, 11](https://www.customs.gov.eg/Upload/ECAAdminace/ECAAdminace316621937.pdf)

Projects set up after the law took effect, in line with the investment map, get an investment incentive deducted from net taxable profit (art. 11):
- **Sector A: 50% of investment costs.** The areas most in need of development under the investment map, on the data of the Central Agency for Public Mobilisation and Statistics and the development plan (art. 11 item 1 as replaced by Law 160/2023). Regulations art. 10 (as replaced by PM Decree 2467 of 2020) names the Suez Canal Economic Zone, the Golden Triangle Economic Zone, the New Administrative Capital and other areas the Cabinet names on development indicators.
- **Sector B: 30% of investment costs**, in the rest of Egypt, for: labour-intensive projects; small and medium projects; projects using or producing new and renewable energy; national and strategic projects and tourism projects named by the Supreme Council; electricity generation and distribution projects named by Prime Minister decree; projects exporting their output (Regulations art. 10: at least 50%); cars and feeder industries; wood, furniture, printing, packaging and chemicals; antibiotics, oncology drugs and cosmetics; food, agricultural crops and agricultural waste recycling; engineering, metal, textile and leather industries (art. 11 item 2); and, in the Regulations, information and communication technology industries.
- **Labour-intensive** means at least 500 Egyptian workers on the employer's social insurance form and direct wages over 30% of operating cost (Regulations art. 11).
- **Investment cost** means equity plus long-term liabilities invested in tangible fixed assets, intangible assets paid in cash, and working capital (Regulations art. 11).
- **Caps:** the incentive may not exceed 80% of paid-in capital up to the start of activity, and the deduction may not run more than seven years from the start of activity (art. 11).

**Conditions** (art. 12): a new company or establishment set up for the project; set up within three years from the date the Regulations took effect, extendable by Cabinet decree for further periods whose total may not exceed nine years (item 2 as replaced by Law 160/2023); regular accounts, with separate accounts per area if it works in more than one; and no shareholder or owner may have contributed or used physical assets of a company existing when the law took effect, or liquidated one within the item 2 period, to set up the project, on pain of losing the incentive and paying all tax due. Expansions of existing projects (new assets that raise production capacity) may get the art. 11 and art. 13 incentives on Cabinet rules (art. 12 last para., added by Law 141 of 2019).

**Start of activity:** the company tells GAFI the start date within 90 days, with an auditor-certified statement of investment costs; a GAFI committee fixes the start date and investment costs in a report within 15 working days, open to grievance (Regulations art. 13). The GAFI chief executive issues the certificate for the incentives of arts. 10, 11, 11 bis and 13, which binds every other body (art. 14).

### 3. The cash incentive (art. 11 bis, added by Law 160 of 2023) [art. 11 bis](https://www.customs.gov.eg/Upload/ECAAdminace/ECAAdminace999139060.pdf)

On top of the other incentives, projects in industrial activities named under the article, and their expansions, get a cash investment incentive of at least 35% and at most 55% of the tax paid with the income tax return on the income from the project's activity. The Ministry of Finance pays it within 45 days from the end of the return deadline; if late, it owes a delay charge at the Central Bank credit and discount rate on the 1 January before the due date, dropping part months and pounds. The incentive is not taxable income.

Conditions: until the start of activity, at least 50% of the project's funding must be foreign currency from abroad; activity must start within six years from the date the article took effect (26 July 2023), extendable by Cabinet decree by up to six years. The Cabinet decree (on a joint proposal of the investment, industry and finance ministers) names the industries and areas, the period for each, up to ten years, and the conditions, rates and payment mechanics.

### 4. Additional incentives (art. 13, replaced by Law 160 of 2023) [art. 13](https://www.customs.gov.eg/Upload/ECAAdminace/ECAAdminace999139060.pdf)

The Cabinet may grant projects under arts. 11 and 11 bis: special customs outlets for their exports or imports; the State bearing all or part of the cost of connecting utilities, after operation starts; part of technical training costs; a refund of half the price of land for industrial projects that start production within two years of land handover; free land for some strategic activities; exemption from land usufruct charges for up to ten years from operation. The Prime Minister may exempt them from up to 50% of their contribution to infrastructure costs, and the treasury may bear up to 50% of their utility consumption for up to ten years, on Supreme Council rules. The Cabinet may create other non-tax incentives. To get any of them, the project must have started activity and meet one of the Regulations art. 12 tests (for example, export at least 50% of output, local content at least 50%, or funding from foreign currency transferred from abroad).

### 5. The single approval (Golden License) (art. 20, replaced by Law 160 of 2023) [art. 20 and Gazette correction](https://www.customs.gov.eg/Upload/ECAAdminace/ECAAdminace885813148.pdf)

By Cabinet decree, a company of any legal form, existing or being set up, for new investment projects, or strategic or national projects in fields and on criteria the Cabinet sets, or private and public partnership projects in utilities, infrastructure, renewable energy, roads and transport or ports, may get one approval to set up, run and manage the project, including building permits and land allocation, effective without any other step. The approval may extend one or more of the law's incentives to the project. GAFI monitors compliance; after a warning and time to cure, the project or its incentives may be suspended for up to one year, and a continuing breach may lead to the approval being cancelled. GAFI's portal for this is at goldenlicense.gov.eg. The correction of 10 August 2023 inserted "or" between "new investment projects" and "strategic or national projects": a project need not be both.

### 6. Free zones (arts. 34, 40, 41) [arts. 40, 41](https://www.customs.gov.eg/Upload/ECAAdminace/ECAAdminace316621937.pdf)

Free zone projects and the profits they distribute are outside Egyptian tax and duty laws, and pay instead (art. 41):

| Free zone project | Fee | Article |
|---|---|---|
| Public free zone, storage | 2% of the CIF value of goods on entry | 41 first item 1 |
| Public free zone, manufacturing and assembly | 1% of the FOB value of goods on exit | 41 first item 1 |
| Public free zone, activity not moving goods in or out | 1% of total revenue, from audited accounts | 41 first item 2 |
| Private free zone, manufacturing and assembly | 1% of total revenue on export abroad; 2% of total revenue when goods enter Egypt | 41 second item 1 |
| Private free zone, other projects | 2% of total revenue | 41 second item 2 |
| All free zone projects | Annual service charge of one per thousand of capital, at most EGP 100,000 | 41 |

Transit trade with a set destination is exempt from the fees. Goods from a free zone into Egypt are imports under the general rules; for products with local and foreign parts, customs tax is on the foreign parts at their price when they leave the zone, capped at the tax on the finished product imported from abroad (art. 40). Waste from free zone projects may enter Egypt for safe disposal or recycling at the owner's cost; hazardous waste entering this way is not treated as an import from abroad (art. 40 paras. 2 and 3, replaced by Law 160/2023). After Supreme Energy Council approval, free zone projects may be licensed in petroleum manufacturing, fertilisers, iron and steel, gas liquefaction and transport and energy-intensive industries; never in alcohol, weapons, ammunition or explosives (art. 34, replaced by Law 160/2023).

### 7. State entities

Law 159 of 2023 cancels tax and fee exemptions given to State entities and State-owned companies for their economic or investment activities. See `eg-corporate-tax` for who counts as a State entity; check it before claiming an incentive for a company with any State shareholding.

## Boundary and exception table

| Situation | Treatment | Source |
|---|---|---|
| Free zone project | No general incentives (art. 9); pays the art. 41 fees instead of tax | Arts. 9, 41 |
| Existing company expanding | Expansion may get arts. 11 and 13 incentives on Cabinet rules; not a new company under art. 12 item 1 | Art. 12 last para. |
| Assets moved in from an existing company | Special incentive lost, all tax due | Art. 12 item 4 |
| Incentive larger than 80% of paid-in capital | Cut to 80% | Art. 11 |
| Profits in year 8 | No deduction left, even if the incentive is not used up | Art. 11 |
| Cash incentive and special incentive together | Allowed: art. 11 bis is "without prejudice" to the chapter's incentives | Art. 11 bis |
| Listing incentive of Law 151/2026 | Not combined with incentives under any other law | `eg-corporate-tax` |
| Project with a State shareholder | Check Law 159 of 2023 first | Law 159 art. 1 |

## Worked cases

All amounts are hypothetical inputs. The 22.5% company tax rate comes from `eg-corporate-tax`.

### Case 1: special incentive in sector A, capped by paid-in capital

A new company in the Suez Canal Economic Zone (sector A) has investment costs of EGP 100,000,000 and paid-in capital of EGP 50,000,000 at the start of activity. The incentive is 50% of investment costs, EGP 50,000,000, but the cap is 80% of paid-in capital, EGP 40,000,000. Taxable profit before the incentive is EGP 15,000,000 in year 1, EGP 20,000,000 in year 2 and EGP 25,000,000 in year 3. Deductions run 15,000,000, 20,000,000 and the remaining 5,000,000, all inside the seven years. Year 3 taxable profit is EGP 20,000,000. Tax saved over the three years is 40,000,000 x 22.5% = EGP 9,000,000.

```oa-check
name: Sector A special incentive with the 80% capital cap
inputs:
  investment_costs: 100000000
  paid_in_capital: 50000000
  profit_y1: 15000000
  profit_y2: 20000000
  profit_y3: 25000000
  cit_rate: 0.225
steps:
  incentive_before_cap: investment_costs * 0.50
  cap: paid_in_capital * 0.80
  incentive: min(incentive_before_cap, cap)
  used_y1: min(profit_y1, incentive)
  used_y2: min(profit_y2, incentive - used_y1)
  used_y3: min(profit_y3, incentive - used_y1 - used_y2)
  taxable_y3: profit_y3 - used_y3
  tax_saved: (used_y1 + used_y2 + used_y3) * cit_rate
expected:
  incentive_before_cap: 50000000
  cap: 40000000
  incentive: 40000000
  used_y3: 5000000
  taxable_y3: 20000000
  tax_saved: 9000000
```

### Case 2: decision, does the project qualify for the cash incentive, and what range

A listed industrial project pays EGP 10,000,000 income tax with its return on the project's income. If at least 50% of its funding to the start of activity was foreign currency from abroad, the cash incentive is between 35% and 55% of the tax paid, EGP 3,500,000 to EGP 5,500,000, the exact rate set by the Cabinet decree for its industry and area; the incentive is not taxable. If only 40% of funding came from abroad, it gets nothing under art. 11 bis. The figure that decides is the foreign funding share before the start of activity: raising it from 40% to 50% is worth at least EGP 3,500,000 a year in this case.

```oa-check
name: Cash incentive range and the 50% foreign funding test
inputs:
  tax_paid: 10000000
  foreign_share: 0.40
  foreign_share_if_raised: 0.50
steps:
  low: tax_paid * 0.35
  high: tax_paid * 0.55
  qualifies_now: min(1, floor(foreign_share / 0.50))
  low_now: low * qualifies_now
  qualifies_if_raised: min(1, floor(foreign_share_if_raised / 0.50))
  low_if_raised: low * qualifies_if_raised
expected:
  low: 3500000
  high: 5500000
  qualifies_now: 0
  low_now: 0
  low_if_raised: 3500000
```

## When to refuse or refer

- The cash incentive rate for an industry and the list of industries and areas depend on a Cabinet decree that was not read: give the 35% to 55% range, not a rate.
- Sector placement, start-of-activity date and investment costs are fixed by GAFI; refer disputes to GAFI's grievance committee (Investment Law art. 83) or an Egyptian adviser.
- Single approval, free zone licensing and land incentives are discretionary decisions of the Cabinet, Prime Minister or GAFI: say what the law allows, not that the client will get it.
- Do not help move old assets into a "new" company or split a business to claim the special incentive: art. 12 item 4 takes the incentive back.

## Sources

| Source | URL | Read on |
|---|---|---|
| Law 160 of 2023 amending the Investment Law, Gazette 29 bis, 25 Jul 2023, arts. 1 to 3 (page images read), published by the Egyptian Customs Authority | https://www.customs.gov.eg/Upload/ECAAdminace/ECAAdminace999139060.pdf | 2026-11-21 |
| Correction (استدراك) to Law 160 of 2023, Gazette 32, 10 Aug 2023: art. 20 first para. (page image read) | https://www.customs.gov.eg/Upload/ECAAdminace/ECAAdminace885813148.pdf | 2026-11-21 |
| Investment Law 72 of 2017 with its executive regulations (PM Decree 2310 of 2017), consolidated text published by the Egyptian Customs Authority with notes on Laws 141/2019 and 160/2023: law arts. 9 to 15, 20, 34, 35, 40, 41; regulations arts. 10 to 13 (text layer read) | https://www.customs.gov.eg/Upload/ECAAdminace/ECAAdminace316621937.pdf | 2026-11-21 |
| Egyptian Customs Authority laws list (read for the links to Law 160 of 2023, its correction and the consolidated Investment Law) | https://www.customs.gov.eg/Legislations/Manshorat?categoryId=2 | 2026-11-21 |
| ETA "income tax laws" page (read for the ETA's own copy list; Law 72/2017 is at eta.gov.eg/sites/default/files/2024-10/law-72-2017.pdf, used by `eg-stamp-duty`) | https://eta.gov.eg/ar/content/qwanyn-aldrybt-ly-aldkhl | 2026-11-21 |
| GAFI home page (read for the link to the Golden License portal) | https://gafi.gov.eg/en | 2026-11-21 |

Not yet confirmed: the Cabinet decree under art. 11 bis naming the industries and areas for the cash incentive, the rate for each within 35% to 55%, and the period for each; the Prime Minister's decree distributing sub-sectors between sectors A and B under art. 11; whether Regulations art. 10 (sector A areas) and arts. 11 to 13 were amended after PM Decree 2467 of 2020 to follow Law 160 of 2023 (the consolidated copy's notes stop at that decree for art. 10); the date the executive regulations took effect, which starts the art. 12 item 2 three-year period; the Cabinet rules for expansions (art. 12 last para.); the Supreme Council rules under art. 13; the free zone service charge rates (art. 41 says one per thousand of capital up to EGP 100,000 and prints the figure as 0.001%, so the Regulations rate table governs); whether the free zone fee rates in art. 41 were changed by any later law; GAFI's current procedure and fees for the Golden License.
