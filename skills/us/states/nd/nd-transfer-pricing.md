---
name: nd-transfer-pricing
description: >-
  Use when a corporate group with North Dakota nexus needs the 2026 answer
  on ND connected-party and unitary rules: combined reporting for unitary
  businesses under N.D.C.C. § 57-38.1-19 (Joyce/Finnigan allocation
  questions), the water's-edge election with its 3.5% additional tax under
  § 57-38.4-02(3), the equally weighted three-factor formula with
  single-sales-factor election, and alternative apportionment under
  § 57-38.1-18 -- against the graduated 1.41%/3.55%/4.31% corporate
  brackets. Trigger on North Dakota combined return, ND unitary, water's
  edge surtax, 57-38.1-19, 57-38.4-02, Schedule SA, ND addback.
  Source-cited draft; ndlegis.nd.gov unreachable 2026-10-25, statute text
  carried from the existing nd-corporate-tax skill with VERIFY flags.
jurisdiction: US-ND
type: decision
category: transfer-pricing
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-11-14
version: 0.5
---

# North Dakota transfer pricing (combined reporting, water's edge, apportionment)

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Who this applies to

C corporations filing North Dakota Form 40 that are members of a controlled or unitary group with intercompany debt, intangibles, management fees, or factoring flows -- and any multinational choosing between worldwide and water's-edge unitary reporting. North Dakota is a **combined-reporting state**: a corporation that is part of a unitary business must file a combined Form 40 reflecting the group's combined income with ND apportionment on the combined basis. _(N.D.C.C. § 57-38.1-19 per the existing `nd-corporate-tax` skill §10.6, carried with [VERIFY]; ndlegis.nd.gov DNS failure 2026-10-25 -- statute text unverified this run.)_

### 2. Core rules and rates

- **Corporate brackets (graduated):** 1.41% on the first $25,000 of ND taxable income; 3.55% on the next $25,000 (to $50,000); 4.31% above $50,000 -- i.e. $352.50 at $25,000, $1,240 at $50,000, then $1,240 + 4.31% × (income − $50,000). _(US-ND-t57c38.pdf.pdf, N.D.C.C. § 57-38-30: rates stated as "one and forty-one hundredths percent", "three and fifty-five hundredths percent", "four and thirty-one hundredths percent"; US-ND-dr-ndcorp.txt: "Corporate tax rates have remained unchanged since 2015.")_
- **Combined reporting.** Unitary groups file combined Form 40; Joyce/Finnigan allocation questions apply and current ND rule needs confirmation. _(§ 57-38.1-19 [VERIFY])_
- **Water's-edge election + 3.5% surtax.** A corporation electing water's-edge apportionment (excluding certain foreign affiliates from the unitary group) pays an **additional 3.5% of ND taxable income** as a surtax. The election trades worldwide inclusion for a flat surcharge. _(US-ND-dr-ndcorp.txt: "If a corporation elects to use the water's edge method to apportion its income, the corporation will be subject to an additional 3.5% surtax on its North Dakota taxable income."; US-ND-dr-form40-2025-form.pdf line 17: "Surtax on water's edge method election (3.5% of line 15)". Note: the archived N.D.C.C. § 57-38.1-15 is the sales-factor section (US-ND-dr-t57c38-1.pdf) -- the surtax cite should be re-verified against the water's-edge provisions.)_
- **Apportionment formula.** Three equally weighted factors, (property + payroll + sales) / 3, by default; for taxable years after 2018 a taxpayer that is not a passthrough entity may elect the **single sales factor**, binding for five consecutive years and for the whole unitary group. _(N.D.C.C. § 57-38.1-09(1) and (4), https://ndlegis.gov/cencode/t57c38-1.pdf, read 2026-11-13.)_
- **Alternative apportionment.** A taxpayer (or the Commissioner) may seek an alternative method under § 57-38.1-18 where the statutory formula does not "fairly represent" ND activity -- the Commissioner's tool against engineered IP/financing footprints. _(existing `nd-corporate-tax` skill §, carried with [VERIFY].)_
- **No PTET.** ND offers no pass-through entity tax election, so S-corp/partnership owners have no entity-level SALT workaround (existing `nd-corporate-tax` skill).

### 3. Base and adjustments

1. Start from federal taxable income (ND starts from FTI per the existing skill).
2. On a combined basis: eliminate/adjust intercompany transactions per the unitary-combination rules (US-ND-dr-form40-2025.pdf: combined filers use "the pro forma federal taxable income amount for the combined group members" with "consolidating adjustments/eliminations from" a pro forma separate-company return or by-company schedule).
3. Apply the water's-edge election if made; if made, add the 3.5% surtax on top of the normal bracket tax (US-ND-dr-ndcorp.txt: "additional 3.5% surtax on its North Dakota taxable income").
4. Apportion on the combined basis: equally weighted three-factor default, single-sales-factor election if made, subject to § 57-38.1-18 modification.
5. ND has no separate corporate franchise tax -- the bracket tax is the only entity-level income charge.

### 4. Deadlines

- Form 40 (combined where required): 15th day of the 4th month after year end (Apr 15 calendar filers).
- Estimated payments: quarterly installments per the existing `nd-estimated-tax` skill (corporate estimates on Form 40 ES; confirm current schedule).
- Water's-edge election timing and duration: "The water's edge election must be made on the return as originally filed and is binding for five consecutive tax years" (US-ND-dr-form40-2025.pdf, Water's Edge Election).

### 5. Penalties and interest

- Underpayment of estimates: interest on the shortfall -- "Interest is calculated at the rate of 12% per annum from the installment due date to the earlier of the date the estimated tax is paid or the due date (without extension) of the return" (US-ND-dr-form40es2026.pdf).
- Late filing/failure to file: Chapter 57-38 penalties; exact 2026 percentages: see "Not yet confirmed:" in Sources.
- Intercompany intangible/management-fee stripping is a named multistate audit theme; the Commissioner more often imposes unitary computation against aggressive separate-entity filers (existing skill § on alternative apportionment).

### 6. Cross-border and federal overlay

- Foreign affiliates: the water's-edge election is the principal gate between worldwide and US-only unitary reporting; the 3.5% surtax is its price (US-ND-dr-ndcorp.txt: "additional 3.5% surtax on its North Dakota taxable income").
- Federal §267 related-party deferrals and §163(j) interest limits change the federal deduction and therefore the ND starting point.
- Treaty analysis is federal (see federal skills); ND conforms to federal taxable income as its starting line.
- Joyce/Finnigan: whether a non-unitary-but-affiliated member's factors enter the ND fraction is a live ND question -- flag for a multistate specialist (existing skill refusal catalogue).

### 7. Worked examples

**Example 1 -- standalone bracket tax, $100,000 ND taxable income.** No water's-edge election, fully ND-apportioned.

```oa-check
name: nd corp bracket tax 100k
inputs:
  ti: 100000
steps:
  - b1: 352.50
  - b2: (min(ti, 50000) - 25000) * 0.0355
  - b3: (ti - 50000) * 0.0431
  - tax: b1 + b2 + b3
expected:
  tax: 3395.00
```

**Example 2 -- water's-edge elector, $200,000 ND taxable income.** Bracket tax plus the 3.5% water's-edge additional tax under § 57-38.4-02(3).

```oa-check
name: nd waters edge surtax 200k
inputs:
  ti: 200000
steps:
  - base: (ti - 50000) * 0.0431 + 1240
  - sur: ti * 0.035
  - total: base + sur
expected:
  base: 7705.00
  sur: 7000.00
  total: 14705.00
```

(The surtax nearly doubles the bill at this income level -- the election's price must be modeled, not assumed.)

### 8. Ask the client first

1. Is the group unitary under ND's definition -- common control plus functional/economic integration?
2. Worldwide or water's-edge? Has the election been made, and when does it expire/renew?
3. Are intercompany interest, royalties, and management fees arm's-length and documented?
4. Has the group made the single-sales-factor election, and when does its five-year binding period end?
5. Any non-ND states with conflicting combined-reporting regimes that create double inclusion (keep both returns in the file)?

### 9. Sources

- Existing `nd-corporate-tax` skill -- bracket table, § 57-38.4-02(3) water's-edge additional tax, § 57-38.1-18 alternative apportionment, § 57-38.1-19 combined reporting (all carried with the skill's own [VERIFY] flags): read 2026-10-25.
- ND Office of State Tax Commissioner -- individual/estimated pages (interest on underpaid estimates): <https://www.tax.nd.gov/individual-income-tax> -- 200 with text, 2026-10-25.
- N.D.C.C. §§ 57-38-30, 57-38.1-09, 57-38.1-15, 57-38.1-18, 57-38.1-19 statute text: archived as US-ND-t57c38.pdf.pdf (ch. 57-38) and US-ND-dr-t57c38-1.pdf (ch. 57-38.1); note § 57-38.1-15 is the sales-factor section, so the water's-edge surtax statute cite needs re-verification -- see the "Not yet confirmed:" paragraph below.
- Form 40 booklet combined-computation mechanics: archived as US-ND-dr-form40-2025.pdf (combined report method, water's-edge election, Schedule WW).

<!-- openaccountants-cta-block -->

---

### Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at the OpenAccountants network.

- Use it in your AI: 
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min

## Who this applies to

No figures stated in this section.

## Rates, bands and thresholds

No figures stated in this section.

## The taxable base

No figures stated in this section.

## Deadlines and filing

No figures stated in this section.

## Penalties and interest

No figures stated in this section.

## Cross-border points

No figures stated in this section.

## Worked examples

No figures stated in this section.

## Ask the client first

No figures stated in this section.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Legacy listed citation only, not re-read in this repair: US-ND-dr-nd-booklet2024.pdf | https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2024-iit/2024-individual-income-tax-booklet.pdf | 2026-10-28 |
| Legacy listed citation only, not re-read in this repair: US-ND-dr-nd-withholding-2025.pdf | https://www.tax.nd.gov/sites/www/files/documents/misc-discuss-folder/Final_2025%20Income%20Tax%20Withholding%20Rates%20%20Instructions.pdf | 2026-10-28 |
| Legacy listed citation only, not re-read in this repair: US-ND-dr-ndwr.pdf | https://www.tax.nd.gov/sites/www/files/documents/forms/business/ndwrfillable.pdf | 2026-10-28 |
| Legacy listed citation only, not re-read in this repair: US-ND-dr-nd-walsh-county-notice-2026.pdf | https://www.tax.nd.gov/sites/www/files/documents/forms/business/sales-use/local-jurisdiction-rates/2026-jurisdiction/notice-to-walsh-county-permit-holders.pdf | 2026-10-28 |
| Legacy listed citation only, not re-read in this repair: US-ND-dr-t57c51-1.pdf | https://ndlegis.gov/cencode/t57c51-1.pdf | 2026-10-28 |
| Legacy listed citation only, not re-read in this repair: US-ND-dr-usc26-1.txt | https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section1&num=0&edition=prelim | 2026-10-28 |
| Legacy listed citation only, not re-read in this repair: US-ND-dr-ndcc-57-39-2.pdf | https://ndlegis.gov/cencode/t57c39-2.pdf | 2026-10-28 |
| Legacy listed citation only, not re-read in this repair: US-ND-tap.html | https://tap.tax.nd.gov/?Check=1 | 2026-10-28 |

Not yet confirmed: figures in this skill lack archived line-citations.
- Exact 2026 Chapter 57-38 late-filing / failure-to-file penalty percentages (ndlegis.nd.gov DNS failure 2026-10-25).


| Source | URL | Read on |
| --- | --- | --- |
| (see "Not yet confirmed:" paragraph) | Not read: legacy placeholder, no source URL | 2026-10-28 |

No figures stated in this section.


### Source maintenance, 14 November 2026

This is a source-table repair, not a fresh approval of the legacy body. The figures independently re-read here are the ordinary corporate rate table, the water's-edge additional tax/election period, and the apportionment/election and alternative-method provisions. The current `nd-corporate-tax` owner holds the broader corporate computation. In particular, section 57-38.1-19 is **Purpose**, not the combined-reporting authority; the legacy references to it do not support that proposition. The blanket PTET-absence claim and specialist Joyce/Finnigan treatment remain unconfirmed and must not determine a filing without current source review.

| Source and actual read scope | URL | Read on |
| --- | --- | --- |
| Corporate overview. Read for ordinary rate brackets and water's-edge surtax; not a comprehensive PTET-absence audit. | https://www.tax.nd.gov/corporate-income-tax | 2026-11-14 |
| NDCC 57-38.1. Read for sections 09(1)/(4), 18 and 19: factors, election, alternative methods and the actual Purpose heading. | https://ndlegis.gov/cencode/t57c38-1.pdf | 2026-11-14 |
| NDCC 57-38.4. Read for section 02 water's-edge five-year election and additional tax. | https://ndlegis.gov/cencode/t57c38-4.pdf | 2026-11-14 |
| 2025 Form 40 instructions, 2025-2026 filing cycle. Read for combined-report definition, pro forma federal starting income, water's-edge election and original-return timing; not final 2026 form mapping. | https://www.tax.nd.gov/sites/default/files/documents/forms/business/corporate-income/2025-corp/28714-corp-income-tax-booklet-2025.pdf | 2026-11-14 |

Source quotes read today: section 57-38.4-02(1)(b), "The water's edge election is binding for five consecutive taxable years after making the election." Section 57-38.4-02(3), "an additional tax of three and one-half percent of taxable income". Section 57-38.1-18, "do not fairly represent the extent of the taxpayer's business activity in this state". Section 57-38.1-19, "Purpose."

Not yet confirmed: full legacy-body legal verification, comprehensive 2026 PTET absence, specialist combined-report attribution, final 2026 Form 40 mapping and unused inherited bibliography. Historical rows above retain their inherited listed dates as provenance, not evidence that they were opened in this repair.

## Talk to a verified accountant

No figures stated in this section.
