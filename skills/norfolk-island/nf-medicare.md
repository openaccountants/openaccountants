---
name: nf-medicare
description: >
  Establish Norfolk Island individual Medicare levy and surcharge treatment
  for 2026–27 using Australian legislation and current authority guidance.
  Covers ordinary low-income relief, family reductions, prescribed-person
  exemptions, part-year days, surcharge income tiers, hospital cover and
  reportable fringe benefits. Use for Norfolk Medicare tax, health levy,
  private hospital cover, family thresholds or surcharge questions. Includes
  statutory formulas, fictional computations and reviewer checks. Residence,
  dependency, cover and income adjustments require separate evidence. This
  source-cited reference preserves unresolved special cases and filing
  mechanics; it does not complete an individual return or the country pack.
jurisdiction: NF
category: international
tax_year: 2026
tax_year_notes: "Australian 2026–27 income year; low-income figures are those enacted for 2025–26 and later years, checked on 17 October 2026 and subject to later amendment"
tier: 2
last_updated: 2026-10-17
version: 0.1
review_status: pending_review
depends_on:
  - workflow-base
  - income-tax-workflow-base
  - social-contributions-workflow-base
---

# Norfolk Island: Medicare levy and surcharge

Use `nf-tax-system` for the post-2016 reforms and `nf-income-tax` for
residence, ordinary income tax and selected offsets. Norfolk residence does
not supply a blanket Medicare levy exemption. The ATO Norfolk page says a
person entitled to Medicare benefits may have to pay the levy; establish
the actual statutory position rather than treating that statement as a
calculation. [NORFOLK]

Load `workflow-base`, `income-tax-workflow-base` and
`social-contributions-workflow-base`. Preserve their source and period
gates, confirmed profile, refusals, universal outputs and all domain
outputs and checks. This reference does not fill every country slot.
Required missing facts remain Needs Input; unresolved rules remain on hold.
Do not collect or submit Medicare numbers, identity evidence or returns.

## Charge, residence and exemptions

Income Tax Assessment Act 1936 section 251S generally imposes the levy on
an individual's taxable income where the person was an Australian resident
at any time during the income year. It contains separate trustee branches
and a specified superannuation adjustment. It is additional to income tax.
The Medicare Levy Act supplies the rates and reductions. [ASSESS,
section 251S][ASSESS]; [LEVY, sections 4–6][LEVY]

Section 251T excludes the ordinary levy for an individual who was a
prescribed person throughout the year. Section 251U supplies conditional
categories, including specified comprehensive medical-treatment rights,
certain pension categories, non-resident periods, specified diplomatic
circumstances and a Health Minister certification of Medicare ineligibility.
Merely not using Medicare, lacking a card, travelling or buying insurance
does not establish a statutory exemption. [ASSESS]

Dependency matters: subsection 251U(2) generally requires all dependants
to have the relevant prescribed status. Subsection (3) provides a half-period
rule for specified categories when the dependency condition prevents full
status. Section 251R defines relevant family relationships, maintenance
and dependant conditions and includes special family-agreement rules.
Establish the actual category and days rather than assigning an exemption
from a short label such as pensioner or defence employee. [ASSESS]

The surcharge has different dependency and prescribed-person rules.
Sections 251V and 251VA prevent specified ordinary-levy dependency
exclusions and the half-period exemption from automatically transferring
to surcharge treatment. The fringe-benefits surcharge Act separately
modifies those definitions. A half ordinary-levy exemption is not proof of
a half surcharge exemption. [ASSESS]; [FRINGE, sections 5–8][FRINGE]

## Ordinary levy and low-income relief

The general individual rate is **2% of taxable income**, subject to the
applicable adjustments, reductions and exemptions. It is separate from
ordinary income tax and the zone offset. A non-refundable income-tax
offset does not automatically remove the levy; special offsets need their
own priority rules. [LEVY, sections 5–9A][LEVY]; `nf-income-tax`

The checked Act gives these individual limits:

| Statutory category | No ordinary levy at or below | Phase-in limit |
|---|---|---|
| Ordinary individual category | $28,011 | $35,013 |
| Entitled to the section 160AAAA seniors/pensioners rebate | $44,268 | $55,335 |

Between the threshold and phase-in limit, section 7(2) caps the levy before
family and prescribed-person reductions at **10% of the excess over the
threshold**. Above the phase-in limit the ordinary 2% rate applies, still
subject to other relief. Do not replace the enacted phase-in limit with a
calculated fraction of the threshold, or select the seniors/pensioners
category from age alone. [LEVY, sections 3, 6 and 7][LEVY]

These amounts were enacted by the 2026 Efficient and Trusted Tax System
Act, effective 1 July 2026, with Schedule 5 expressly applying to
**2025–26 and later assessments**. They are the enacted amounts checked for
2026–27 on 17 October, not a forecast that later legislation will leave
them unchanged. Recheck before an actual assessment. [AMEND, section 2 and
Schedule 5][AMEND]

### Family reduction

Section 8 requires the person to be married on the year's last day or
entitled to one of the specified actual/notional child-related offsets.
Its family income generally combines the couple's taxable incomes when
married on that day; it is not the surcharge income measure. Marriage,
separation and death have statutory rules. [LEVY, sections 3 and 8][LEVY]

The ordinary family threshold is **$47,238**, replaced with **$61,623** for
the specified section 160AAAA entitlement. Add **$4,338** only for each
qualifying person covered by the statutory notional-offset conditions.
For a person not married on the last day, subsection (6) adds a family-tax-
benefit condition. Do not add a child amount solely because a child lives
in the household. [LEVY, section 8(5)–(7)][LEVY]

For an eligible person, no ordinary levy is payable where family income
does not exceed the applicable family threshold. Above it, section 8(2)
calculates a potential reduction using:

`2% × family threshold − 8% × (family income − family threshold)`.

Use only a positive reduction and apply subsections (3)–(4): where the
spouse is also liable before these family and part-year reductions, the
person's reduction is reduced in proportion to the spouse's taxable income
over family income; excess reduction can affect the spouse's levy. Do not
give both spouses the full family reduction or treat the result as a
refundable credit. [LEVY, section 8][LEVY]

### Part-year periods and special receipts

Section 9 reduces the ordinary levy in the proportion that established
prescribed-person days bear to actual days in the income year. It expressly
excludes the surcharge increase, whose own period rules must be applied.
Use dates and the actual year length, not months divided by 12. [LEVY]

Section 9A has separate eligible-lump-sum-arrears conditions, including the
10% test and prior accrual-year circumstances. It can adjust the person's
levy base and family analysis without necessarily adjusting the spouse's
family-income calculation. Do not remove arrears, a super receipt or
foreign exempt income from the base without the complete applicable rule.
Those special calculations remain held here. [LEVY]; [ASSESS]

## Medicare levy surcharge: income, cover and period

The surcharge is additional to the ordinary levy. Establish the person's
single/married/dependant status, prescribed status and appropriate cover
for each relevant period before choosing a charge. Medicare Levy Act
sections 8B–8D and fringe Act sections 12–16 contain different single,
single-with-dependants and married branches. [LEVY]; [FRINGE]

The **2026–27** tier boundaries published by the ATO are:

| Tier | Single income for surcharge purposes | Family income for surcharge purposes, before child increases | Surcharge rate when liable |
|---|---|---|---|
| Base | At or below $105,000 | At or below $210,000 | Nil |
| 1 | Over $105,000 to $123,000 | Over $210,000 to $246,000 | 1% |
| 2 | Over $123,000 to $164,000 | Over $246,000 to $328,000 | 1.25% |
| 3 | Over $164,000 | Over $328,000 | 1.5% |

The private health insurance Act provides indexed thresholds and doubled
family thresholds. For MLS, apply the modified family-tier tests in levy
section 3A and fringe section 6, rather than importing every private-health-
rebate family rule unchanged. Increase all three family thresholds by
**$1,500 for each MLS dependent child after the first**. This is distinct
from the ordinary levy family's $4,338 component. [PHI, sections 22-30–22-45][PHI];
[LEVY]; [FRINGE]; [ATO-RATES]

Income for surcharge purposes selects entitlement and the rate. It includes
the statutory taxable-income measure, reportable fringe benefits,
reportable super contributions and total net investment loss, with specific
FHSS, superannuation and other adjustments. Spouse trust income and exempt
foreign employment require further analysis. Do not equate salary,
taxable income, family income and surcharge income. [DICT, section 995-1][DICT];
[ATO-RATES]

The **amount charged** uses the applicable statutory bases. Section 8B's
ordinary single-person branch applies the selected percentage to taxable
income, not merely the excess over the tier threshold. The fringe Act
imposes a separate charge on the reportable fringe benefits total. The ATO
also identifies amounts subject to family trust distribution tax as part
of the surcharge calculation. Actual trust, exempt-foreign-income and
other special-base cases remain held until all governing rules are loaded.
Do not apply the selected rate indiscriminately to every amount used in
the tier test. [LEVY]; [FRINGE, sections 10–12][FRINGE]; [ATO-PAYING]

Appropriate cover requires the statutory complying hospital policy and
excess conditions. Section 45-1's maximum excess is **$750 in any 12-month
period for a policy insuring one person**, or **$1,500 for another policy**.
An extras-only, overseas-visitors/student or unregistered-insurer policy
is not automatically qualifying hospital cover. Confirm required
dependants' cover, period changes and exceptions as well as the person's
own policy. A premium payment alone does not prove continuous qualifying
cover. [LEVY, section 3(5)][LEVY]; [FRINGE, section 4][FRINGE]; [PHI]; [GOV-MLS]

For a whole-year married person, the combined tier threshold and the
person's own **$28,011** surcharge-income condition are distinct gates.
The part-year-marriage branch uses different conditions; do not carry the
whole-year low-income gate into it without checking section 8D(4) and
fringe section 16. Actual surcharge periods are day based. [LEVY]; [FRINGE]

The ATO paying page checked in this batch still displays older $27,222
and 2025–26 tier figures. Use the later enacted $28,011 condition and the
period-labelled 2026–27 tier page. Its general explanation of charge bases
does not make its older numeric examples current. [AMEND]; [ATO-PAYING]; [ATO-RATES]

## Fictional calculations and review patterns

Amounts below exclude other taxes and assume all unmentioned special
adjustments are absent. They are component examples, not return balances.

| Stipulated facts | Component result |
|---|---|
| Ordinary category, no family/prescribed reduction, taxable income $28,011 | Ordinary levy nil. |
| Same scope, taxable income $30,000 | 10% × ($30,000 − $28,011) = **$198.90**, below the $600 ordinary-rate amount. |
| Same scope, taxable income $35,013 | Phase-in cap **$700.20**, rather than $700.26. At $35,014, outside that limit, 2% is **$700.28**. |
| Ordinary scope at $73,000; exactly 100 established prescribed days in 2026–27; no other reduction | Before the day reduction: $1,460. Reduction: $1,460 × 100 / 365 = **$400**. Remaining ordinary levy **$1,060**; surcharge separately analysed. |
| Eligible ordinary family, year-end married; one person's taxable income $50,000 and spouse nil; no children, other reduction or special income | Family threshold $47,238; potential reduction $944.76 − $220.96 = **$723.80**. The first person's $1,000 ordinary levy becomes **$276.20**; no spouse levy requires proportional splitting. |
| Established 2026–27 family-tier case with three MLS dependent children | Add $3,000 to each family threshold: **$213,000, $249,000 and $331,000**. |
| Established single/no-dependant/no-cover/no-exemption full-year case; taxable and surcharge income both $105,001 | Tier 1 taxable-income surcharge component **$1,050.01**, not 1% of only the $1 excess. |
| Same full-year ordinary single scope; taxable income $120,000 plus $20,000 reportable super contributions; no fringe benefits or other adjustments | Surcharge income $140,000 selects Tier 2. Taxable-income surcharge component: $120,000 × 1.25% = **$1,500**. Do not charge 1.25% on $140,000 merely because it selected the tier. |
| Same full-year single scope; taxable income $100,000 and reportable fringe benefits $10,000; no other adjustment | Tier 1; taxable-income component **$1,000** plus fringe-benefits component **$100** = **$1,100**. |
| Ordinary single taxable-income surcharge branch applies for exactly 73 days of a 365-day year; annual taxable income $110,000, Tier 1; no other base | $1,100 × 73 / 365 = **$220** for that component. The tier test is not prorated to 73 days. |
| A half ordinary-levy exemption or an employee's own cover is supplied, with dependant facts missing | Needs Input. Neither item alone settles surcharge treatment. |

Check the year, residence and statutory category; ordinary versus surcharge
income and bases; family versus single gates; exact threshold equality;
the whole applicable base; qualifying policy and dependant periods; and
actual day counts. Reconcile components with `nf-income-tax` only after
all offsets, credits, prepayments and workflow requirements are resolved.

## Sources, currency and remaining coverage

Checked on 17 October 2026: selected Medicare Levy Act compilation 53 and
fringe Act compilation 42, both effective 1 July 2026, and private health
insurance Act compilation 42, effective 19 September 2026. Live Register
records identified each as latest. Read the cited 1936 Act provisions in
compilation 193 and the surcharge-income definition in 1997 compilation
267 with its recorded interval and later amendment review described in
`nf-income-tax`. A full text download is not a full-law read.

Native text omitted formula images. DOM alternative text recovered the
family reduction, surcharge day fractions and child-threshold formula.
The ATO tier page is dated 22 June 2026; its 2026–27 table is separate from
its prior-year tables. Current published figures do not establish an
actual taxpayer's profile or a future amendment outcome.

Actual Medicare eligibility/certification, complete dependant/notional
offset and family-agreement analysis, trustees, arrears, foreign-exempt
income, special bases, insurance grandfathering, private-health rebate,
all filing/payment/rounding mechanics and remaining workflow country slots
remain open. No actual return, complete Norfolk pack, independent model
engagement benchmark or accountant sign-off is claimed.

[LEVY]: https://www.legislation.gov.au/C2004A03351/2026-07-01/text
[ASSESS]: https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_4/document_4.html
[FRINGE]: https://www.legislation.gov.au/C2004A00412/2026-07-01/text
[PHI]: https://www.legislation.gov.au/C2007A00031/2026-09-19/text
[AMEND]: https://www.legislation.gov.au/C2026A00058/asmade
[DICT]: https://www.legislation.gov.au/C2004A05138/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_10/document_10.html
[NORFOLK]: https://www.ato.gov.au/norfolk-island/norfolk-island-residents-and-individual-tax
[ATO-RATES]: https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/medicare-levy-surcharge/medicare-levy-surcharge-income-thresholds-and-rates
[ATO-PAYING]: https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/medicare-levy-surcharge/paying-the-medicare-levy-surcharge
[GOV-MLS]: https://privatehealth.gov.au/health_insurance/surcharges_incentives/medicare_levy.htm

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained in the
[ryanduguid/openaccountants fork](https://github.com/ryanduguid/openaccountants).
Check its quality tier, recorded review status and cited sources before use.
Choose a practitioner whose credentials and engagement scope you have verified.
The links below are optional upstream services; they do not publish or verify
this fork's changes.

- Upstream connection service: https://www.openaccountants.com/connect
- Upstream accountant network: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
