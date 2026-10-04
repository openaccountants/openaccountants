---
name: nl-zzp-deductions
description: Use this skill whenever asked about Dutch self-employed (zzp) tax deductions. Trigger on phrases like "zelfstandigenaftrek", "startersaftrek", "MKB-winstvrijstelling", "urencriterium", "1225 hours", "KIA", "kleinschaligheidsinvesteringsaftrek", "FOR", "fiscale oudedagsreserve", "meewerkaftrek", "willekeurige afschrijving", "zzp deductions", "Dutch freelancer deductions", "Netherlands self-employed tax benefits", or any question about tax deductions available to Dutch sole proprietors (eenmanszaak) and freelancers (zzp'ers). This skill covers all major ondernemersaftrek components, the MKB-winstvrijstelling, investment deductions, the hours criterion, and their interaction with Box 1 computation. ALWAYS read this skill before touching any Dutch self-employed deduction work.
version: 2.0
jurisdiction: NL
tax_year: 2026
last_updated: 2026-09-28
authored_by: OpenAccountants team
review_status: pending_review
trust_label: Written by the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Netherlands self-employed deductions — 2025 and 2026

## Scope and who this is for

Figures are for tax year 2025 or tax year 2026 as explicitly labelled; do not mix columns.

Use this method for the business-profit deductions of a Netherlands-resident individual who qualifies as an entrepreneur for income tax. The ordinary computation below covers a domestic sole proprietor with reconciled fiscal profit. It screens partnership and specialist relief but refers allocation, international and cessation calculations. It does not calculate the complete personal tax bill, tax credits or healthcare contribution. A deduction reduces taxable profit; it is not a cash payment or necessarily an equal reduction in tax. [Entrepreneur assessment](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/wanneer_bent_u_ondernemer_voor_de_inkomstenbelasting/) [MKB exemption](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/mkb_winstvrijstelling)

Select the income year first. Use the 2025 column for a 2025 return prepared later, and the 2026 column for 2026 profit. Future-year announcements and proposed changes are outside these calculations; recheck enacted provisions and the annual guidance before extending this method. [2025 rules](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/verandering_inkomstenbelasting_vorige_jaren/veranderingen-inkomstenbelasting-2025/ondernemersaftrek-2025/zelfstandigenaftrek-2025) [2026 rules](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/ondernemersaftrek-2026/zelfstandigenaftrek-2026)

## Ask the client first

- Income year, legal form, residence and nature of each activity; evidence supporting income-tax entrepreneur status, distinct from VAT registration and employment classification.
- Fiscal profit before ondernemersaftrek, with the cost, depreciation, private-use, reserve and investment adjustments identified. Do not start from bank deposits or turnover.
- Actual annual business hours and other working hours, supporting records, pregnancy interruption, and related-person partnership arrangements.
- Entrepreneur status and use of zelfstandigenaftrek in each of the preceding five years; relevant tax-neutral return from a company; whether pension age was reached at the start of the income year.
- Unused zelfstandigenaftrek decisions by origin year, utilisation and remaining amount; earlier business-loss decisions are a separate ledger.
- Qualifying investment obligations, invoices, recoverable VAT, payments, first-use dates and disposals; connected-party purchases and assets made available to others.
- Fiscal partner's work, hours and remuneration; a disability benefit, R&D certificate, cessation, business transfer or existing FOR reserve.

Missing structure, profit, hours or prior-year decisions remain unknown. Continue computations that do not depend on the missing fact, but do not turn an unknown into a confirmed zero or award.

## The method, step by step

1. Confirm the income source using the evidence and conditions below.
2. Establish the hours result using the evidence and conditions below.
3. Reconcile fiscal profit and investments using the evidence and conditions below.
4. Apply zelfstandigenaftrek and starter supplement using the evidence and conditions below.
5. Assess other relief before MKB using the evidence and conditions below.
6. Apply MKB to the remaining enterprise result using the evidence and conditions below.
7. Preserve FOR and depreciation boundaries using the evidence and conditions below.

### Step 1: Confirm the income source

Assess income-tax entrepreneurship from the actual commercial activity. A registered business, a VAT number or meeting the hours threshold alone is insufficient. Employment and income from other work do not acquire entrepreneurial relief simply because the person invoices. A passive co-entitlement or lending return does not qualify for ondernemersaftrek or MKB exemption; assess investment relief separately under its own conditions. [Income sources](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/wanneer_bent_u_ondernemer_voor_de_inkomstenbelasting/) [Relief scope](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/ondernemersaftrek_en_investeringsaftrek)

### Step 2: Establish the hours result

The ordinary urencriterium requires at least 1,225 business hours in the calendar year. Usually more working time must be spent on the enterprise than on other work. The latter comparison is waived if the individual was not an entrepreneur in at least one of the preceding five years; the annual hours threshold remains. Do not prorate for a partial year. [Hours](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/voorwaarden_urencriterium)

Actual work includes administration, quotations and business website work, not just invoiced hours. Mere standby availability does not count. Keep a defensible record using calendars, invoices, timesheets and quotations. Assess claimed travel against actual business work and evidence; do not impose the old guide's blanket exclusion of every travel hour. Pregnancy interruption has a specific 16-week allowance. In a related-person partnership, the exclusions include an unusual arrangement with at least 70% supporting work and work for a connected person's enterprise from which the taxpayer does not themselves derive entrepreneur profit. Refer uncertain allocations. [Hours evidence and exclusions](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/voorwaarden_urencriterium)

Failing this hours test does not itself change business income into other-work income. It can block particular deductions while MKB relief and qualifying KIA remain separately assessable. [Entrepreneur assessment](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/wanneer_bent_u_ondernemer_voor_de_inkomstenbelasting/) [MKB](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/mkb_winstvrijstelling) [KIA](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/investeringsaftrek_en_desinvesteringsbijtelling/kleinschaligheidsinvesteringsaftrek_kia)

### Step 3: Reconcile fiscal profit and investments

Business expenditure must satisfy the business-purpose test. Recoverable VAT is excluded from the cost basis; irrecoverable VAT is included where the underlying expenditure is otherwise allowable, with capitalisation and private-use restrictions still applying. Supplier names do not determine deductibility or KIA. [Business costs](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/zakelijke_kosten) [Excluded investments](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/investeringsaftrek_en_desinvesteringsbijtelling/geen_recht_op_investeringsaftrek)

Identify depreciation, investment deductions, disinvestment additions and reserve movements before recording profit before ondernemersaftrek. Keep each adjustment visible and prevent duplicate deductions. KIA is additional to eligible depreciation, not a substitute for capitalising an asset. Do not subtract the asset price as a current expense merely because KIA applies. [Investment method](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/investeringsaftrek_en_desinvesteringsbijtelling/voorwaarden_investeringsregelingen) [Starter depreciation](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/afschrijving/willekeurige_afschrijving/startende_ondernemer)

### Step 4: Apply zelfstandigenaftrek and starter supplement

The ordinary deduction requires entrepreneur status and the hours test. Use the annual amount below, adjusted for pension age at the beginning of that year. For a non-starter, the deduction cannot exceed profit before ondernemersaftrek; unused relief has its own carryforward. A current ordinary deduction cannot create or deepen a loss in this branch. [Self-employed deduction](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/ondernemersaftrek/zelfstandigenaftrek1/)

The startersaftrek increases the zelfstandigenaftrek where the taxpayer qualifies for it, was not an entrepreneur in at least one of the preceding five years, and had zelfstandigenaftrek applied no more than twice in those years. The tax-neutral-return-from-a-company exclusion must also be checked for the current and preceding five years. If entitled, the supplement accompanies the ordinary deduction; it is not an elective amount to save for another year. The combined current-year deduction may exceed profit and create a loss. Use the actual lookback, not “first three years” or registration age alone. A year in which the ordinary deduction was reduced to nil by the profit cap still counts as a year of application for this lookback. [Starter conditions](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/ondernemersaftrek/startersaftrek) [Current statute, zelfstandigenaftrek](https://wetten.overheid.nl/BWBR0011353)

Where profit limitation leaves unused zelfstandigenaftrek, preserve the amount established by assessment. It can be used in the following nine years, subject to eligibility and available profit above the current-year deduction. The taxpayer must track and enter utilisation, using the oldest origin-year amount first; it is not simply lost or automatically claimed. Obtain the decisions before using an opening amount. A special death/cessation exception needs separate review. [Carryforward](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/ondernemersaftrek/zelfstandigenaftrek1/verrekenen_niet_gerealiseerde_zelfstandigenaftrek)

### Step 5: Assess other relief before MKB

For meewerkaftrek, the entrepreneur must themselves satisfy the hours test. Their fiscal partner must work at least 525 hours for no remuneration or remuneration below €5,000. The partner's hours must be evidenced. Apply the table below to qualifying profit, excluding the special expropriation, cessation and foreign-transfer profit components specified by the source. [Meewerkaftrek rules](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/ondernemersaftrek_en_investeringsaftrek)

A payment below €5,000 is not deductible as partner remuneration and is not taxable to the partner under this rule. At €5,000 or more, the remuneration route may apply: the payment is deductible from business profit and taxable to the partner, with the real work and arrangement documented. Do not also claim meewerkaftrek for that work. [Partner remuneration](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/arbeidsbeloning_aan_fiscale_partner)

Screen separately for disability starter relief, certified research/development work and cessation relief. They have distinct conditions; they are not automatically part of the ordinary calculation. A qualifying self-employed R&D deduction exists within income tax; it is not solely an employer payroll subsidy. Refer these claims with the certificate, hours, benefit or cessation evidence. [Other entrepreneur deductions](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/ondernemersaftrek_en_investeringsaftrek)

### Step 6: Apply MKB to the remaining enterprise result

For eligible entrepreneur profit, apply the MKB percentage after ondernemersaftrek, aggregating qualifying enterprises where necessary. No urencriterium condition applies. The exemption also reduces a loss, so do not switch it off merely because the result is negative. It does not apply to a passive co-entitlement or lending return. [MKB exemption](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/mkb_winstvrijstelling) [Scope](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/ondernemersaftrek_en_investeringsaftrek)

The practical calculation is: fiscal enterprise profit after business adjustments, minus allowable ondernemersaftrek and eligible carryforward, then subtract the MKB percentage of that remaining result. A negative MKB amount reduces the loss rather than increasing it. Apply the annual benefit-rate limitation in the full income-tax calculation; do not multiply every deduction by the taxpayer's highest marginal rate. [MKB](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/mkb_winstvrijstelling) [Annual deduction limits](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/verandering_inkomstenbelasting_vorige_jaren/veranderingen-inkomstenbelasting-2025/ondernemersaftrek-2025/zelfstandigenaftrek-2025) [2026](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/ondernemersaftrek-2026/zelfstandigenaftrek-2026)

### Step 7: Preserve FOR and depreciation boundaries

No new FOR additions are allowed from 2023 onward. An existing reserve may remain but is not guaranteed to stay unchanged while a business continues. Check whether it exceeds business equity and the relevant cessation, pension-age or consecutive-year hours condition; conversion and death have separate rules. Release normally increases enterprise profit; an eligible annuity payment is a separate private deduction. Refer conversion eligibility and timing instead of assuming ordinary pension allowance limits or a generic conversion deadline settle it. [FOR](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/fiscale_reserves/oudedagsreserve)

Starter accelerated depreciation can apply to eligible assets bought in years of starter entitlement or the preceding startup year, subject to its exclusions and annual investment ceiling. The KIA minimum annual investment threshold does not itself block this depreciation. The book value must not fall below residual value. Retain first-use and payment evidence; refer buildings for the separate statutory floor-value rules, and special assets or recapture rather than promise unrestricted immediate write-off. [Residual-value rule](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/winst_en_verliesrekening_en_balans) [Starter depreciation](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/afschrijving/willekeurige_afschrijving/startende_ondernemer)

## Figures by year

### Ordinary deductions

| Item | 2025 | 2026 | Conditions/source |
| --- | --- | --- | --- |
| Zelfstandigenaftrek before pension-age adjustment ([2025](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/verandering_inkomstenbelasting_vorige_jaren/veranderingen-inkomstenbelasting-2025/ondernemersaftrek-2025/zelfstandigenaftrek-2025), [2026](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/ondernemersaftrek-2026/zelfstandigenaftrek-2026)) | €2,470 | €1,200 | Entrepreneur and hours tests; profit cap except qualifying starter |
| Ordinary startersaftrek supplement | €2,123 | €2,123 | Full lookback and exclusion tests |
| Pension age reached at start of year | 50% of the applicable ordinary deduction and supplement | 50% of the applicable ordinary deduction and supplement | Use return rounding; do not assess age at filing date |
| MKB exemption | 12.7% | 12.7% | After ondernemersaftrek; applies to loss too |
| Maximum rate used for benefit of ordinary deduction/MKB | 37.48% | 37.56% | Full tax calculation must implement rate limitation |

[2025 annual rules](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/verandering_inkomstenbelasting_vorige_jaren/veranderingen-inkomstenbelasting-2025/ondernemersaftrek-2025/zelfstandigenaftrek-2025) [2026 annual rules](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/ondernemersaftrek-2026/zelfstandigenaftrek-2026) [MKB rates](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/mkb_winstvrijstelling)

### Meewerkaftrek — both years

| Evidenced partner hours in the year | Percentage of qualifying profit |
| --- | --- |
| Below 525 | None ([official bands](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/ondernemersaftrek_en_investeringsaftrek)) |
| At least 525, below 875 | 1.25% |
| At least 875, below 1,225 | 2% |
| At least 1,225, below 1,750 | 3% |
| At least 1,750 | 4% |

The entrepreneur's own hours test and partner remuneration conditions still apply. [2025](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2025/ondernemersaftrek_en_investeringsaftrek) [2026](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/ondernemersaftrek_en_investeringsaftrek)

### KIA annual table

The following published ranges use whole-euro amounts. Use the filing software's applicable rounding; do not invent treatment of a fractional amount between displayed ranges. [2025 KIA](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/verandering_inkomstenbelasting_vorige_jaren/veranderingen-inkomstenbelasting-2025/investeringsaftrek-2025/kleinschaligheidsinvesteringsaftrek-2025) [2026 KIA](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/investeringsaftrek-2026/kleinschaligheidsinvesteringsaftrek-2026)

| 2025 qualifying investment | KIA |
| --- | --- |
| Not more than €2,900 | None ([source](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/verandering_inkomstenbelasting_vorige_jaren/veranderingen-inkomstenbelasting-2025/investeringsaftrek-2025/kleinschaligheidsinvesteringsaftrek-2025)) |
| €2,901 through €70,602 | 28% of investment |
| €70,603 through €130,744 | €19,769 |
| €130,745 through €392,230 | €19,769 minus 7.56% of investment above €130,744 |
| More than €392,230 | None |

| 2026 qualifying investment | KIA |
| --- | --- |
| Not more than €2,900 | None ([source](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/investeringsaftrek-2026/kleinschaligheidsinvesteringsaftrek-2026)) |
| €2,901 through €71,683 | 28% of investment |
| €71,684 through €132,746 | €20,072 |
| €132,747 through €398,236 | €20,072 minus 7.56% of investment above €132,746 |
| More than €398,236 | None |

An individual qualifying asset must cost at least €450 on the appropriate VAT basis. Ordinary passenger cars not intended for professional transport are excluded regardless of their price; there is no general cheap-car allowance. Check other exclusions, including land, residential property, goodwill, private assets transferred into the business, connected-party transactions and assets predominantly for rental or foreign use. Exemption requests and special environmental schemes need separate assessment. [Excluded investments](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/investeringsaftrek_en_desinvesteringsbijtelling/geen_recht_op_investeringsaftrek)

Investment generally concerns the binding obligation or production costs, not simply payment date. If an asset is not yet in use, the current deduction is limited by payments, with remaining deduction subject to later-use rules. Partnership KIA is based on joint investment and allocation rules, not independent application of this table to each partner. [Timing](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/investeringsaftrek_en_desinvesteringsbijtelling/voorwaarden_investeringsregelingen) [Partnership allocation](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/investeringsaftrek_en_desinvesteringsbijtelling/kleinschaligheidsinvesteringsaftrek_kia)

On disposal within five years from the beginning of the investment year, check disinvestment if aggregate disposal value exceeds €2,900 under the current guidance for these years. Use the original effective deduction percentage and cap the addition at the deduction previously received. Private transfer, rental conversion and delayed use/payment can also trigger deemed disposal. Do not treat every sale as automatic clawback or ignore an asset that was gifted. [Disinvestment](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/investeringsaftrek_en_desinvesteringsbijtelling/desinvesteringsbijtelling)

## Boundary and exception table

| Situation | Result |
| --- | --- |
| Below ordinary hours threshold but entrepreneur status established | No ordinary hours-dependent deduction; MKB and qualifying KIA remain separate |
| Exactly 1,225 hours | Threshold met, but the other-work comparison and exclusions still need review |
| Current-year profit too low, no starter supplement | Limit current deduction and preserve assessment-based unused amount |
| Qualifying starter with low profit | Full current ordinary deduction plus supplement can create loss; MKB then reduces that loss |
| Partner remuneration exactly €5,000 | Remuneration route; no meewerkaftrek ([source](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/arbeidsbeloning_aan_fiscale_partner)) |
| Partner hours exactly 875 | Use the 2% band if all other conditions hold |
| Investment exactly €2,900 | No KIA under either annual table |
| Eligible asset exactly €450 | Not excluded by the per-asset minimum, but annual total and other rules remain |
| Ordinary passenger car below a supposed price cap | Still excluded from KIA unless the professional-transport exception applies |
| Existing FOR and ongoing activity | Assess release triggers; continuation alone does not prevent release |

## Worked cases

The arithmetic below is illustrative, assumes the facts stated, and keeps cents for transparency. It is not a substitute for return-specific rounding or a complete tax calculation.

### Ordinary profitable entrepreneur, 2026

Assume a sole proprietor below pension age at the start of the year, established entrepreneur status and hours-test eligibility, no starter entitlement, no carryforward or other deductions, and fiscal profit before ondernemersaftrek of €50,000. Subtract €1,200, leaving €48,800. The MKB exemption is €6,197.60, leaving taxable enterprise profit of €42,602.40. These are profit figures, not tax due. [2026 deduction](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/ondernemersaftrek-2026/zelfstandigenaftrek-2026) [MKB](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/mkb_winstvrijstelling)

### Non-starter with limited profit, 2025

Use the authority's carryforward example: eligible profit €1,500 and ordinary entitlement €2,470. Current deduction is €1,500, remaining profit is nil, and unused relief is €970, recorded by assessment. It is not lost. If the eligible 2026 profit is €50,000, current deduction €1,200 leaves €48,800; using the €970 carryforward leaves €47,830 before MKB. [Carryforward example](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/ondernemersaftrek/zelfstandigenaftrek1/verrekenen_niet_gerealiseerde_zelfstandigenaftrek)

### Low-profit qualifying starter, 2026

Assume profit before ondernemersaftrek of €2,000, full ordinary and starter eligibility, no pension-age adjustment and no other deductions. The current combined deduction is €3,323; the result before MKB is a loss of €1,323. MKB reduces that loss by €168.021, giving a result of negative €1,154.979 before filing rounding (illustratively negative €1,154.98 to cents). [Starter](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/ondernemersaftrek/startersaftrek) [2026](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/ondernemersaftrek-2026/zelfstandigenaftrek-2026) [MKB](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/mkb_winstvrijstelling)

### Nil deduction in the starter lookback

A taxpayer has three preceding years in which ordinary zelfstandigenaftrek applied, including one where the profit cap reduced the amount to nil. That nil-benefit year still counts. Do not treat this as only two applications or award the starter supplement on that basis. [Statutory application rule](https://wetten.overheid.nl/BWBR0011353)

### Investment and hours boundary

An established entrepreneur who does not meet the hours test invests exactly €2,900 in otherwise eligible assets. No KIA is available under either table, and no ordinary zelfstandigenaftrek. MKB remains separately assessable on enterprise profit. Neither registration nor the purchase repairs the missing hours condition. [KIA tables](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/verandering_inkomstenbelasting_vorige_jaren/veranderingen-inkomstenbelasting-2025/investeringsaftrek-2025/kleinschaligheidsinvesteringsaftrek-2025) [2026](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/investeringsaftrek-2026/kleinschaligheidsinvesteringsaftrek-2026) [Hours](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/voorwaarden_urencriterium) [MKB](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/mkb_winstvrijstelling)

### Partner and reserve decisions

A partner performs 875 evidenced hours unpaid, but the entrepreneur fails their own hours test. Do not claim meewerkaftrek despite reaching the partner band. Separately, an ongoing business with an old FOR exceeding equity and failure of the hours test in both the current and preceding year needs a reserve-release calculation; “still trading” is insufficient. [Meewerkaftrek](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/ondernemersaftrek_en_investeringsaftrek) [FOR](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/fiscale_reserves/oudedagsreserve)

## When to refuse or refer

- Refer unresolved entrepreneur/employment status, connected-person partnership hours, partnership KIA allocation, cross-border activity, company transition, disability starter relief, R&D certificates, cessation, death, FOR conversion and property/special-asset depreciation. Preserve documents and ordinary calculations that remain independent, but do not label a dependent tax figure final.

Use `nl-freelance-intake` for the evidence handoff. When passing taxable business profit to `nl-income-tax` or `nl-return-assembly`, send the complete adjustment ledger, origin-year carryforwards and open issues. Check the actual dependent method and annual sources: do not import an old MKB percentage, abandoned FOR addition, or treat business profit as the whole personal-tax or healthcare-contribution base.

## Completion checklist

- [ ] Income year and entrepreneur status supported separately from hours and VAT status.
- [ ] Profit reconciled; costs, depreciation, KIA and reserve changes not double counted.
- [ ] Hours threshold, other-work comparison and special exclusions checked.
- [ ] Starter lookback, company-return exclusion and pension-age date checked.
- [ ] Profit cap and unused deduction ledger correctly separated from loss relief.
- [ ] Partner's and entrepreneur's conditions both checked before meewerkaftrek.
- [ ] Correct annual investment table, exclusions, timing and disposal rules applied.
- [ ] MKB applied after deductions, including the loss branch; rate limitation passed downstream.
- [ ] No new FOR; old reserve assessed for release triggers.
- [ ] Complete calculation and unresolved matters handed off without implying submission or accountant attestation.

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
