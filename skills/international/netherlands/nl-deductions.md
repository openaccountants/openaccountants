---
name: nl-deductions
description: Use this skill whenever asked about Dutch tax deductions and special schemes (aftrekposten en regelingen) beyond self-employed deductions. Trigger on phrases like "aftrekposten", "belastingaftrek", "deductions Netherlands", "hypotheekrenteaftrek", "mortgage interest deduction", "eigenwoningforfait", "specifieke zorgkosten", "giftenaftrek", "studiekosten", "alimentatie aftrek", "persoonsgebonden aftrek", "partnerregeling", "heffingskorting", "ouderenkorting", "jonggehandicaptenkorting", "levensloopvrijstelling", "box 3 vrijstelling", "groene belegging", "ANBI", "kom ik in aanmerking", "tax deduction check NL", or any question about Dutch individual or business tax deductions, credits, or special regimes. This skill covers persoonsgebonden aftrek, hypotheekrenteaftrek, zorgkosten, giften, heffingskortingen, and business investment schemes. ALWAYS read this skill before advising on Dutch deduction eligibility.
version: 1.0
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

# Netherlands: income tax deductions for individuals (aftrekposten) 2026

## Scope

Figures are for tax year 2026 unless the 2025 column or section says otherwise. Missing evidence stays unresolved; do not assume zero deductions or a completed return. 

This Guide covers the main deductions a Dutch resident individual claims in the income tax return
(aangifte inkomstenbelasting). The primary year is **2026** (calendar year 1 January to 31 December 2026).
There is a short dated section for **2025**, the returns being filed now.

Covered:

- **Own home (eigen woning):** mortgage interest deduction (hypotheekrenteaftrek), the imputed
  rental value (eigenwoningforfait), and the deduction for no or a small home debt (Wet Hillen).
- **The capped deduction rate (tariefsaanpassing):** above the top-bracket threshold, deductions
  give relief at a lower rate than the top rate.
- **Personal deductions (persoonsgebonden aftrek):** paid partner alimony (partneralimentatie),
  specific care costs (specifieke zorgkosten), gifts (giften), weekend costs for severely
  disabled persons, and the remnant of the study-costs deduction.
- **Tax credits (heffingskortingen)** and the **box 3** tax-free allowance and green-investment
  exemption, in outline, because they interact with the deductions.

Not covered here:

- **Entrepreneur deductions** (zelfstandigenaftrek, startersaftrek, mkb-winstvrijstelling, the
  hours test): use the **nl-zzp-deductions** Guide. The investment deductions (KIA, EIA, MIA,
  Vamil) and R&D relief are business matters: route ordinary deductions to that method and refer specialist schemes. Qualifying self-employed S&O relief can be an income-tax deduction; WBSO is not solely a payroll measure. [Income-tax R&D relief](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/ondernemersaftrek_en_investeringsaftrek)
- **Company tax** for a BV: use **nl-corporate-tax**.
- Non-residents, except the pointer in "When to refuse or refer".

Law: Wet inkomstenbelasting 2001 (Wet IB 2001), chapter 3 section 3.6 (own home) and chapter 6
(personal deductions), as in force on 2026-02-21 ([Wet IB 2001](https://wetten.overheid.nl/BWBR0011353/2026-02-21)).
Practice: the Belastingdienst "Fiscale informatie 2026" chapters linked in each section.
Currency is euro. Figures below use a comma for thousands and a point for decimals; the
Belastingdienst writes them the other way round.

## Ask the client first

Ask these before you calculate anything. Missing answers change the result.

- **Which tax year?** 2026 (current) or 2025 (return due now or late)? Figures differ by year.
- **Resident all year?** Non-resident entitlement depends on the item, qualifying foreign-taxpayer status and any treaty/special rules. If not resident all year, refer the affected analysis.
- **Fiscal partner (fiscale partner)?** For the whole year, or part of the year with the
  choice to be partners all year? Partners combine care costs, gifts and the thresholds
  ([fiscal partnership](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/fiscaal_partnerschap)),
  and may split the combined deduction any way they like as long as the total is 100% ([gifts chapter](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/aftrek_giften)).
- **Box 1 income before deductions.** Is income from work and home, before deductions, above
  the top-bracket threshold? That decides whether the capped rate applies.
- **AOW age?** Reached at the start of the year or during it? It changes the care-cost
  increase percentage and the credits.
- **Home:** Is it the main residence (hoofdverblijf)? The WOZ value from the WOZ-beschikking
  for the year; the annual mortgage statement (jaaropgave); when each loan was first taken
  out, any refinancing and remaining deduction/repayment term, whether it was increased after 1 January 2013; whether the loan is annuity or
  linear; whether any loan is from family, a BV, an employer or a foreign bank.
- **Moved, sold or separated?** Old home empty and for sale, new home not yet lived in,
  divorce with an ex still living in the home, or a sale at a loss between 29 October 2012 and
  31 December 2017 (restschuld).
- **Care costs:** What was paid in the year, for whom, and what was or could be reimbursed by
  the health insurer or anyone else? Is anything own risk (eigen risico) or a statutory own
  contribution?
- **Gifts:** To whom (check ANBI status), how paid (cash is not deductible for ordinary gifts),
  any cultural ANBI, and is there a written periodic-gift agreement (notarial deed or private
  deed) for at least 5 years?
- **Alimony:** For the ex-partner or for children? Periodic or a lump sum? Is there a written
  arrangement?
- **Business income?** If the client is an entrepreneur, route the business deductions to
  nl-zzp-deductions first, then return here.

## The method, step by step

Work in this order. It follows how the Belastingdienst builds the assessment
([tax calculation 2026](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/belastingberekening)).

1. **Box 1 income** from work, including profit after entrepreneur deductions (see
   nl-zzp-deductions).
2. **Own home balance:** add the eigenwoningforfait; deduct mortgage interest and other
   deductible home costs; if the forfait is higher than the costs, apply the Hillen deduction.
3. **Personal deductions** (persoonsgebonden aftrek): alimony, care costs above the threshold,
   gifts above the floor and within the ceiling, weekend costs, any study-cost remnant. They
   reduce box 1 income first, then box 3 income, then box 2 income, each not below nil; care
   costs are used first (Wet IB art. 6.2).
4. **Tax per box** at the year's rates.
5. **Capped rate (tariefsaanpassing):** if box 1 income before deductions is above the top
   threshold, add back tax so that the relief on the deductions is capped.
6. **Tax credits** (heffingskortingen) reduce the tax.
7. **Low income check:** if care costs were deducted and credits could not be used as a
   result, the Belastingdienst may pay a separate care-cost allowance (tegemoetkoming
   specifieke zorgkosten) automatically.

### Step A: Mortgage interest (hypotheekrenteaftrek) ([source](https://www.belastingdienst.nl/wps/wcm/connect/nl/koopwoning/content/hypotheekrente-aftrekken))

Who and what:

- Only interest on the **eigenwoningschuld**: debt taken on to buy, improve or maintain the
  main residence, or to buy off ground lease, plus the financing costs borrowed with it
  ([chapter 10](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/eigen_woning_en_restschuld_vroegere)).
  Debt used for anything else (a car, a holiday, the part of a refinance that was spent
  elsewhere) is a box 3 debt, not an own-home debt.
- **Loans first taken on or after 1 January 2013:** at least annuity or linear repayment over
  no more than 30 years (360 months), agreed in the loan contract and actually met (Wet IB
  art. 3.119a). If the client falls behind on repayments, the deduction can be lost; check.
- **Loans from before 2013, not increased since:** the old conditions continue. Interest is
  deductible for at most 30 years; for a loan that existed before 1 January 2001 the 30 years
  started on 1 January 2001.
- **Loan increased on or after 1 January 2013:** the original part keeps its old terms; the
  increase normally needs the repayment test; preserve the remaining statutory term and check transitional exceptions rather than automatically restarting every loan term.
- Also deductible: financing costs (advice and arrangement fees, notary costs for the mortgage
  deed, valuation for the loan, NHG application), penalty interest (boeterente) when the loan
  is part of the own-home debt, and periodic ground-lease payments (erfpacht, opstal,
  beklemming) in proportion to the ownership share. Not deductible: a buy-out of ground lease
  paid as a lump sum, and building insurance.
- **Loan from family, a BV, an employer or a foreign bank:** still deductible, but the client
  must report the loan details in the return (start date, term in months, start amount,
  repayment method, interest rate, and the lender's name, address and BSN or RSIN).
- **Timing:** record payments and their contractual period. Contractually agreed 2026 prepayment for a period ending no later than 30 June 2027 can be fully deductible in 2026; voluntary payment for 2027 is treated differently. Longer prepayments require the source's allocation rules. Do not automatically spread every prepayment. Reconcile refunded interest against the current allowable deduction. Refer unusual timing or refinancing cases.

Home not lived in:

- **New home empty or being built:** interest is deductible if the client expects to move in
  within 3 years after the end of the tax year.
- **Old home empty and for sale:** it stays an own home in the year it became empty and the
  3 years after that. If it is let in that period, no interest deduction for the let months
  and the home falls in box 3 for that time.
- **Restschuld:** after a sale at a loss between 29 October 2012 and 31 December 2017, the
  interest on the remaining debt is deductible for 15 years.

### Step B: Eigenwoningforfait ([source](https://www.belastingdienst.nl/wps/wcm/connect/nl/koopwoning/content/hoe-werkt-eigenwoningforfait))

The forfait is a percentage of the home's WOZ value, added to box 1 income. It applies only to an
owner-occupied home that is the main residence. Use the WOZ value for the tax year (the WOZ
valuation letter). Table for **2026**:

| WOZ value more than | WOZ value not more than | Eigenwoningforfait 2026 |
| --- | --- | --- |
| nil | €12,500 | 0% |
| €12,500 | €25,000 | 0.10% |
| €25,000 | €50,000 | 0.20% |
| €50,000 | €75,000 | 0.25% |
| €75,000 | €1,350,000 | 0.35% |
| €1,350,000 | no limit | €4,725 plus 2.35% of the value above €1,350,000 |

If the home was the main residence for only part of the year (bought, sold or moved), let the
online return calculate the forfait for that part of the year, and check the result.

### Step C: No or a small home debt (Wet Hillen) ([source](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/woning/eigenwoningforfait/geen_of_een_kleine_eigenwoningschuld/geen_of_een_kleine_eigenwoningschuld))

If the forfait is higher than the deductible home costs, the client gets a deduction for part of
the difference (Wet IB art. 3.123a). The deduction is being phased out:

- **2026:** 71.867% of the difference is deducted; the rest stays taxable.
- **2025:** 76.667%.
- The deduction lapses entirely from 1 January 2041.

The client may not get this deduction where interest was paid in advance or in arrears, or where
the loan is from the employer. With more than one own home, all homes are looked at together.
Fiscal partners combine their forfait and costs for this test.

### Step D: The capped deduction rate (tariefsaanpassing) ([source](https://www.belastingdienst.nl/wps/wcm/connect/nl/aftrek-en-kortingen/content/afbouw-tarief-aftrekposten-bij-hoog-inkomen))

This is the "capped rate" for deductions. It is **not** a limit for everyone. It applies only when
income from work and home **before** deductions is more than **€78,426 in 2026** (€76,817 in 2025).
Then the relief on deductions that fall in the top bracket is cut:

- **2026:** the adjustment is 11.94%, so relief in the top bracket is at most **37.56%**
  (top rate 49.50% minus 11.94%). This equals the rate of the second bracket.
- **2025:** adjustment 12.02%, relief at most 37.48%.

It covers all of these: own-home costs (mortgage interest, ground-lease payments, financing costs,
interest on a restschuld), the personal deductions (alimony, weekend costs, gifts, care costs,
personal deductions carried from earlier years), and the entrepreneur reliefs (zelfstandigenaftrek,
startersaftrek bij arbeidsongeschiktheid, meewerkaftrek, R&D deduction, stakingsaftrek,
mkb-winstvrijstelling).

How it is calculated (worked example from the Belastingdienst page for Wet Hillen):

1. Take taxable box 1 income, add back the deductions covered by the adjustment, and subtract
   the top-bracket threshold (€78,426 for 2026). This is the test amount.
2. If the test amount is positive, the adjustment applies to the **lower** of the test amount
   and the deductions.
3. Extra tax = 11.94% (2026) of that amount.

The return software does this automatically. The assessment shows it as "tariefsaanpassing".

### Step E: Partner alimony and other maintenance (Wet IB art. 6.3) ([source](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/aftrek_betaalde_partneralimentatie))

Deductible:

- Periodic partner alimony (partneralimentatie) paid to an ex-spouse, ex-registered partner or
  former cohabitant, and to a spouse from whom the client lives permanently apart (duurzaam
  gescheiden). The payer deducts; the recipient is taxed on it.
- A lump sum buying off partner alimony paid to the **ex-spouse**, or a single premium for an
  annuity bought for this purpose. Not deductible if paid before the court dissolved the
  marriage, or where the client lives unmarried with the ex.
- Old-age pension paid on as alimony, settlement payments for pension rights and annuities
  whose premiums were deducted earlier, and social assistance given to the ex that the
  municipality recovers from the client.

Not deductible: **child maintenance** (kinderalimentatie), legal costs to reduce or end the
alimony, and settlement through an annuity whose premiums were already deducted.

Evidence: the Belastingdienst says it does not matter whether the alimony was set by the court or
agreed with the ex. A written, signed record of the arrangement is advised; keep proof of payment.

**Ex-partner stays in the home the client co-owns** under an alimony arrangement: for 2 years the
home still counts as the client's own home. The client deducts the interest on their share and
also deducts their share of the eigenwoningforfait as alimony. After 2 years the client's share
moves to box 3, but the share of the forfait is still deductible as alimony. Interest the client
pays on the ex-partner's share is usually deductible as alimony.

### Step F: Specific care costs (specifieke zorgkosten) ([source](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/aftrek_specifieke_zorgkosten))

**For whom:** the client and fiscal partner; children under 27 who cannot pay the costs
themselves; and, if they could not pay themselves, a seriously disabled person aged 27 or over in
the same household, and parents, brothers or sisters living in the home and dependent on the
client's care.

**Conditions:** only costs for illness or disability, only in the year paid, and only the part
that cannot be reimbursed by anyone (insurer, special assistance, parents). If a
reimbursement **could** be obtained but was not claimed, it normally reduces the deduction. Apply the official exceptions: specified general allowances are not deducted, and special assistance not received and not to be received is treated separately. Basic-package care is not deductible merely because the person chose not to take out health insurance and therefore received no reimbursement. The conscientious-objector rules are separate; refer that status instead of assuming the ordinary exclusion settles it.

**Deductible categories** (2026):

- Medical and surgical help (genees- en heelkundige hulp): GP, dentist, specialist, listed
  paramedics without referral (physio, dietitian, and others), treatment prescribed and
  supervised by a doctor.
- Medicines prescribed by a doctor.
- Certain aids and adaptations of movable items: for example insoles, prostheses, trained
  assistance dogs, some hearing-aid costs (only the extra cost of a functionally better device
  that the insurer partly covers).
- Transport: travel for treatment by car at €0.25 per km, taxi or public transport at actual
  cost; a flat €925 extra if the client cannot walk more than 100 metres, minus any
  reimbursement.
- Diet on the prescription of a doctor or dietitian, at the fixed amounts in the diet list
  (Bijlage I); diets not on the list give nothing.
- Extra household help because of illness or disability, with proper invoices. Apply its separate household-help threshold before adding the eligible cost to the general care-cost calculation; consult the annual chapter's dedicated table. Do not apply only the final general threshold.
- Extra clothing and bedding when the illness lasts or will last at least 1 year: a flat
  €330, or €825 if the client proves the extra spend was at least €660 above normal. These are full-year amounts: prorate for the relevant period, and for another person check the shared-household condition.
- Travel for visiting a sick household member who is nursed for more than 1 month more than
  10 km away: €0.25 per km by car. Check that the shared household existed when the illness began, visits are regular, and repeated admissions satisfy the source's same-illness and interval rules.

**Not deductible (main items):** health insurance premiums (basic and supplementary); costs under
the own risk (eigen risico); statutory own contributions (CAK, Zorgverzekeringswet); glasses,
ordinary vision-correcting contact lenses and eye laser treatment to replace them (separate disability aids and qualifying non-vision-supporting prism glasses require their own assessment); wheelchairs, mobility scooters,
rollators and other walking aids; adaptations to the home; care from a non-contracted provider
where a payment is due for basic-package care; mental-health care and dyslexia care for anyone
under 18; costs to prevent illness (travel vaccinations are the exception).

**Increase (verhoging) 2026:** if the drempelinkomen (combined with a whole-year fiscal partner)
is not more than **€41,123**, add **40%** of the increase-eligible costs, or **113%** if the client
or partner had reached AOW age at the start of the year. The increase does **not** apply to
medical and surgical help or to travel for sick visits.

**Threshold (drempel) 2026** (Wet IB art. 6.20), on drempelinkomen = total income in boxes 1, 2
and 3 before personal deductions ([2026 threshold](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/relatie_familie_en_gezondheid/gezondheid/aftrek_zorgkosten/hoe_berekent_u_uw_aftrek/drempelbedrag_berekenen/drempelbedrag-2026)):

| Drempelinkomen 2026 (no whole-year partner) | Threshold |
| --- | --- |
| up to €9,680 | €166 |
| above €9,680 through €51,411 | 1.65% of drempelinkomen |
| above €51,411 | €848 plus 5.75% of the part above €51,411 |

With a fiscal partner for the whole year, add both incomes and both sets of costs; the first band
becomes up to €19,360 with a threshold of €332; the other bands are the same.

Law in motion: on wetten.overheid.nl, art. 6.20 carries a note that a repeal has been enacted
without a commencement date. The deduction applies for 2026. Before using this for a later year,
check the year's Belastingdienst page.

### Step G: Gifts (giften) ([source](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/aftrek_giften))

**Ordinary gifts (gewone giften)** are deductible only if all of these hold:

- Paid to an institution registered by the Belastingdienst as an **ANBI**, or to a support
  foundation (steunstichting) for an SBBI. A gift to an SBBI itself is not deductible.
- The client can prove the gift, for example with bank statements. Ordinary gifts in kind whose aggregate annual market value exceeds €10,000 require an independent valuation report or qualifying invoice; whole-year fiscal partners aggregate them and use €20,000 (Wet IB article 6.39). Refer missing valuation evidence rather than approve from an informal estimate.
- There is no consideration in return (lottery tickets are not gifts).
- The gift was **not made in cash**.
- Total ordinary gifts exceed the **floor: 1% of drempelinkomen, at least €60**. Only the
  excess counts.
- The deduction cannot exceed the **ceiling: 10% of drempelinkomen**.

With a whole-year fiscal partner the floor and ceiling are based on the joint drempelinkomen.

**Periodic gifts (periodieke giften)** are deductible in full, with no floor and no 10% ceiling, if:

- Paid at least once a year to an ANBI, or to an association (vereniging) that is not an ANBI
  but has at least 25 members, full legal capacity, is not liable to corporate tax, and is
  established in the EU, the Caribbean parts of the Kingdom or a designated country.
- The amounts are the same each time and are recorded in a **notarial deed or a private deed
  of gift** (onderhandse akte; Belastingdienst model forms can be used).
- Paid for **at least 5 consecutive years**, subject to the agreement and statutory permitted termination rules; refer an early termination rather than assume death is the only possible exception.
- No consideration in return; cash gifts are excluded.
- **Cap:** periodic gifts count up to **€1,500,000 per calendar year** in total for the client
  and any fiscal partner (Wet IB art. 6.38). Older agreements can have transitional treatment; inspect the agreement date and current authority guidance before applying the cap mechanically. [Transitional gift rules](https://www.belastingdienst.nl/wps/wcm/connect/nl/aftrek-en-kortingen/content/verschil-periodieke-giften-gewone-giften)
- A periodic gift in kind is possible. For an obligation entered after 31 December 2023 with a
  value above €10,000 a year, an independent valuation or recent invoice is required. Under the statute, whole-year fiscal partners aggregate these gifts and use a €20,000 threshold; check the agreement and year rather than applying the individual threshold twice.

**Cultural ANBI uplift:** for gifts to a cultural ANBI, increase the gift by 25% when calculating
the deduction, capped at **€1,250** extra for ordinary and periodic gifts together. The uplift also
raises the 10% ceiling for ordinary gifts.

**Volunteers:** a waived ANBI allowance requires an actual arrangement, ability and intention to pay, and the volunteer's choice to waive. Qualifying unreimbursed costs have their own conditions. Prevent double counting when both allowance and costs are waived. Car costs not claimed count at €0.23 per km.

**ANBI status withdrawn:** a gift made before the withdrawal decision was known remains
deductible even if withdrawal is retroactive. Check status with the Belastingdienst "ANBI
opzoeken" tool.

### Step H: Weekend costs for severely disabled persons ([source](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/aftrek_voor_tijdelijk_verblijf_thuis))

For the client's severely disabled child, brother or sister, or a person for whom the client is
court-appointed mentor or curator, who is **21 or older** and usually lives in an institution
(often a Wlz institution) but is cared for by the client at weekends or holidays. Flat amounts per
person, 2026:

- **€13 per day** of the stay, including pick-up and drop-off days.
- **€0.25 per km** for fetching and returning by car, always using the home-to-institution distance.
- Minus reimbursements received or still to be received. If the person turns 21 during the year,
  count only from their 21st birthday.

### Step I: Study costs: abolished, one remnant ([source](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/aftrek_studiekosten))

The deduction for study costs no longer exists for current study. For **2026** a deduction is
possible only in this case: the client had a performance grant (prestatiebeurs) before 1 July
2015, got an extended diploma term because of special circumstances (for example medical reasons),
and that grant was definitively converted into a loan in 2026. That can only concern study years
2010/2011 to 2014/2015. The client may then deduct costs from earlier years that were blocked
because of the grant. Anything else labelled "study costs": no deduction; refer if the client
insists.

### Step J: Tax credits 2026 (heffingskortingen) ([source](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/heffingskortingen))

Credits reduce the tax, not the income. Figures for someone **below AOW age for all of 2026**:

- **General tax credit (algemene heffingskorting):** up to €3,115; reduced by 6.398% of
  verzamelinkomen above €29,736; nil above €78,426. (All of 2026 at AOW age: up to €1,556, reduced by 3.195%.)
- **Labour credit (arbeidskorting):** on work income; maximum €5,685 at work income of €45,592,
  then reduced by 6.510% of the excess; nil above €132,920.
- **Income-dependent combination credit (IACK):** work income above €6,239, a child born after 31
  December 2013 in the household for at least 6 months, and no fiscal partner or the lower work
  income of the two: 11.45% of work income above €6,239, maximum €3,032.
- **Elderly credit (ouderenkorting):** at AOW age at year end: €2,067 if verzamelinkomen is not
  above €46,002, reduced by 15% of the excess, nil above €59,782. **Single elderly credit
  (alleenstaandeouderenkorting):** €540.
- **Young disabled credit (jonggehandicaptenkorting):** €923 for qualifying Wajong benefit/work-support entitlement, provided the elderly credit does not apply.
- **Green investment credit:** 0.1% of the exempt green investments in box 3.

For IACK, also check co-parenting, the duration of fiscal partnership, and the equal-work-income tie rule; the older partner qualifies in the tie case if the remaining conditions hold. Use the annual chapter, not just this summary. The ordinary business hours test is not a universal IACK condition.

The employer or benefits agency may already apply the general, labour and elderly credits through
payroll tax; IACK and the green credit are claimed in the return.

### Step K: Box 3 points that touch deductions ([source](https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/heffingsvrij-vermogen))

- **Tax-free allowance (heffingsvrij vermogen) 2026:** €59,357 per person, €118,714 for fiscal
  partners (2025: €57,684 and €115,368). Under the actual-return route the allowance does not apply.
- **Green investments 2026:** exempt up to €26,715, or €53,430 with a whole-year fiscal partner
  ([box 3 chapter](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/bezittingen_en_schulden_box_3_)).
  The value above that is a box 3 asset.
- A debt that is not own-home debt (for example the non-qualifying part of a mortgage) is a box
  3 debt.
- Personal deductions not absorbed by box 1 income reduce box 3 income next, then box 2.

## Figures, with years ([source](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/belastingberekening))

| Item | 2026 | 2025 | Source |
| --- | --- | --- | --- |
| Box 1 rates below AOW age | 35.75% up to €38,883; 37.56% to €78,426; 49.50% above | not repeated here | Fiscale informatie 2026 ch. 29 |
| Top-bracket threshold for the capped rate | €78,426 | €76,817 | Tariefsaanpassing page |
| Adjustment percentage | 11.94% | 12.02% | Tariefsaanpassing page |
| Maximum relief in the top bracket | 37.56% | 37.48% | Tariefsaanpassing page |
| Hillen deduction share | 71.867% | 76.667% | Eigenwoningforfait page |
| Eigenwoningforfait, main band | 0.35% (€75,000 to €1,350,000) | 0.35% (€75,000 to €1,330,000) | Eigenwoningforfait page |
| Eigenwoningforfait, above villa threshold | €4,725 plus 2.35% | €4,655 plus 2.35% | Eigenwoningforfait page |
| Care-cost threshold, lowest band | €166 up to €9,680 | €164 up to €9,534 | Drempelbedrag pages |
| Care-cost threshold, top band starts above | €51,411 (€848 plus 5.75%) | €50,635 (€835 plus 5.75%) | Drempelbedrag pages |
| Care-cost increase income limit | €41,123 | €40,502 | Fiscale informatie ch. 17 |
| Gift floor / ceiling (ordinary) | 1%, at least €60 / 10% | same | Fiscale informatie ch. 16 |
| Periodic gift cap | €1,500,000 | €1,500,000 | Fiscale informatie ch. 16 |
| Cultural ANBI uplift | 25%, at most €1,250 | same | Fiscale informatie ch. 16 |
| Box 3 tax-free allowance | €59,357 (partners €118,714) | €57,684 (partners €115,368) | Heffingsvrij vermogen page |
| Green investment exemption | €26,715 (partners €53,430) | not repeated here | Fiscale informatie 2026 ch. 13 |

## Boundaries and exceptions ([source](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/eigen_woning_en_restschuld_vroegere))

| Situation | Rule | Result |
| --- | --- | --- |
| Income before deductions exactly €78,426 (2026) | Adjustment only if **more than** €78,426 | No adjustment |
| New loan in 2013 or later, interest-only | Check repayment requirement and transitional/bridging exceptions | No deduction if required conditions fail; refer exceptions |
| Pre-2013 loan increased in 2020 | Old part keeps old rules; increase needs annuity/linear | Split the loan |
| Loan from parents | Deductible if conditions met and loan reported in the return | Report lender details |
| Old home empty and for sale since 2024 | Own home for 2024 and the 3 years after | Deductible to 31 December 2027 unless let |
| Forfait higher than interest | Hillen share of the difference | 71.867% in 2026, ends 2041 |
| Care costs within own risk | Not deductible | Exclude |
| Glasses, wheelchair, home adaptation | Excluded items | Exclude |
| Drempelinkomen exactly €41,123 (2026) | Increase if **not more than** €41,123 | Increase applies |
| Cash donation to an ANBI | Ordinary gifts must not be cash | Exclude |
| Periodic gift without a deed | Needs notarial or private deed | Treat as ordinary gift |
| Gift to a non-ANBI | Ordinary and periodic routes have different recipient rules | Check qualifying SBBI-support foundations or associations before refusing |
| Child maintenance | Excluded | Not deductible |
| Lump sum to ex before the divorce is final | Excluded | Not deductible |
| Study course started in 2026 | Deduction abolished | Not deductible |
| Personal deductions exceed income | Box 1, then box 3, then box 2, not below nil | Unused part carried forward (restant persoonsgebonden aftrek) |

## Worked cases ([source](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/woning/eigenwoningforfait/geen_of_een_kleine_eigenwoningschuld/geen_of_een_kleine_eigenwoningschuld))

All cases are 2026, the client is below AOW age and has no fiscal partner unless stated. The
input amounts are assumptions for the example.

**Case 1: mortgage interest with the capped rate.** WOZ value €400,000; mortgage interest paid
€12,000 on a qualifying annuity loan; other box 1 income €95,000.

- Eigenwoningforfait: €400,000 x 0.35% = €1,400.
- Taxable box 1 income: €95,000 + €1,400 - €12,000 = €84,400.
- Test amount: €84,400 + €12,000 - €78,426 = €17,974. Positive, so the adjustment applies.
- The adjustment is on the lower of €12,000 and €17,974, so on €12,000.
- Extra tax: 11.94% x €12,000 = €1,432.80. In effect the interest gets relief at 37.56%.

**Case 2: mortgage nearly repaid (Wet Hillen).** WOZ value €300,000; interest €300.

- Forfait: €300,000 x 0.35% = €1,050. Difference with the interest: €750.
- Hillen deduction: €750 x 71.867% = €539.00.
- Net amount left in box 1 income: €211.00.

**Case 3: care costs with the increase.** Drempelinkomen €35,000. Prescribed medicines €800 and
dentist bills €1,500, none reimbursable and none under the own risk.

- Increase: drempelinkomen is not more than €41,123, so 40% of the medicines: €320. The
  dentist bills are medical help and get no increase.
- Total: €800 + €320 + €1,500 = €2,620.
- Threshold: 1.65% x €35,000 = €577.50.
- Deduction: €2,620 - €577.50 = €2,042.50.

**Case 4: gifts.** Drempelinkomen €60,000. Bank transfers of €600 to an ANBI and €400 to a
cultural ANBI; €100 in cash to a street collection; and €1,200 under a 5-year private deed of
periodic gift to an ANBI.

- Cash gift: excluded.
- Cultural uplift: 25% x €400 = €100 (below the €1,250 cap).
- Ordinary gifts counted: €600 + €400 + €100 = €1,100.
- Floor: 1% x €60,000 = €600. Excess: €500. Base ceiling 10% x €60,000 = €6,000, increased by the €100 cultural uplift to €6,100, not reached.
- Periodic gift: €1,200 in full.
- Total gift deduction: €1,700.

**Case 5: ex-partner stays in the home.** The client and the ex separated less than 2 years ago.
The client owns 50% of the home where the ex lives under an alimony arrangement. Forfait on the
whole home €1,200 (Belastingdienst example, [alimony chapter](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/aftrek_betaalde_partneralimentatie)).

- The client's share of the forfait, 50% x €1,200 = €600, is in box 1, and the client deducts the
  interest on their share.
- The client also deducts €600 as partner alimony.
- After 2 years the share goes to box 3, but the €600 share of the forfait remains deductible as alimony.

**Case 6: a course in 2026.** The client pays for a professional course in 2026 and has no
pre-2015 prestatiebeurs. No study-cost deduction. If the client is self-employed and the course
is for the business, that is a business-cost question for nl-zzp-deductions, not this Guide.

## When to refuse or refer

Refer to a Dutch tax adviser (belastingadviseur) when
([non-residents](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/u_woont_buiten_nederland)):

- The client lived outside the Netherlands for any part of the year, or claims these
  deductions as a non-resident. Deductions then depend on qualifying foreign taxpayer status
  and treaty position.
- There is more than one home, a home partly let or used for business, a sale with a loss
  (restschuld), the bijleenregeling after selling a home with a surplus, an inherited
  mortgage, or a divorce where debts move between partners.
- A loan is from the client's own BV or employer, or from abroad, and its terms are unclear.
- The mortgage does not meet the annuity or linear test or payments are in arrears.
- Care-cost claims are large or unusual, or the insurer reimbursement status is unknown.
- A periodic gift in kind above €10,000 a year ([gifts chapter](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/aftrek_giften)), or gifts to foreign institutions or associations.
- Alimony by lump sum, pension-rights settlements, or annuity buy-outs.
- The client is an entrepreneur: route the business deductions to nl-zzp-deductions first;
  refer investment deductions (KIA, EIA, MIA, Vamil) and WBSO to a specialist.
- The client wants to use actual box 3 returns (werkelijk rendement).

Refuse excluded claims such as child maintenance, cash gifts, health-insurance premiums, own-risk costs, ordinary vision-correcting glasses, wheelchairs or a new private study course. Do not automatically refuse every non-ANBI gift: qualifying support foundations and periodic gifts to qualifying associations have separate routes. Do not confuse a private study deduction with a substantiated business cost.

## Filing and payment ([source](https://www.belastingdienst.nl/wps/wcm/connect/nl/belastingaangifte/content/wat-gebeurt-er-als-ik-geen-aangifte-doe-of-te-laat-of-onvolledig))

- Deductions are claimed in the annual income tax return through Mijn Belastingdienst (DigiD).
  The online return calculates the forfait, the Hillen deduction, the thresholds, the
  increases and the tariefsaanpassing.
- **Deadline:** if the client received an invitation letter (aangiftebrief), the return is due by
  the date in the letter, usually 1 May of the following year. With an extension, the date in the
  confirmation letter, usually 1 September.
- **Late:** first a reminder, then a demand (aanmaning) with 10 working days to file. After that
  a default penalty (verzuimboete) of €469, rising to €6,709 for repeat lateness. Late filing may also
  lead to tax interest (belastingrente). Intentionally wrong returns can bring a higher penalty
  (vergrijpboete).

### Returns for 2025 being filed now ([source](https://www.belastingdienst.nl/wps/wcm/connect/nl/koopwoning/content/tariefsaanpassing-eigen-woning))

For a 2025 return, obtain the actual invitation and any extension confirmation. If the applicable deadline has passed, act promptly; the ordinary dates do not establish every taxpayer's deadline. Use **2025** figures:

- Capped rate: applies when income from work and home before deductions is more than **€76,817**;
  adjustment 12.02%; relief in the top bracket at most **37.48%**.
- Hillen share: **76.667%** of the difference.
- Eigenwoningforfait 2025: same bands as 2026 up to €75,000; 0.35% from €75,000 to
  **€1,330,000**; above that **€4,655** plus 2.35% of the excess
  ([forfait page](https://www.belastingdienst.nl/wps/wcm/connect/nl/koopwoning/content/hoe-werkt-eigenwoningforfait)).
- Care-cost threshold 2025, no whole-year partner: **€164** up to €9,534; 1.65% above €9,534 through
  €50,635; **€835** plus 5.75% above €50,635
  ([2025 threshold](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/relatie_familie_en_gezondheid/gezondheid/aftrek_zorgkosten/hoe_berekent_u_uw_aftrek/drempelbedrag_berekenen/drempelbedrag-2025)).
- Care-cost increase 2025: drempelinkomen not more than **€40,502**
  ([2025 chapter](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2025/aftrek_specifieke_zorgkosten)).
- Gifts 2025: same floor, ceiling, cash exclusion, cultural uplift and €1,500,000 periodic cap
  ([2025 gifts](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2025/aftrek_giften)).
- Box 3 tax-free allowance 2025: **€57,684** (partners €115,368).
- Tax credits 2025 differ from 2026: take them from Fiscale informatie 2025, chapter 21, or let
  the online return compute them.

## Completion checklist ([source](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/aftrek_giften))

- [ ] Tax year fixed and every figure taken from that year's table.
- [ ] Residence and fiscal partner status recorded; partner split of deductions chosen (total 100%).
- [ ] WOZ value, jaaropgave, loan start dates, increases and repayment type on file.
- [ ] Each loan tested: own-home purpose, 30-year period, annuity/linear if 2013 or later,
      non-bank loans reported.
- [ ] Forfait computed; Hillen deduction applied if the forfait exceeds the costs.
- [ ] Tariefsaanpassing checked against the year's threshold.
- [ ] Alimony: partner only, not children; written record and payment proof.
- [ ] Care costs: only non-reimbursable items; exclusions removed; increase checked; threshold
      applied on drempelinkomen.
- [ ] Gifts: ANBI status checked in "ANBI opzoeken"; no cash; floor and ceiling applied; periodic
      deed and 5-year term on file.
- [ ] Study costs: only the prestatiebeurs remnant, otherwise nil.
- [ ] Entrepreneur deductions routed to nl-zzp-deductions.
- [ ] Credits and box 3 allowance taken from the same year.
- [ ] Deadline and any extension noted; late-filing risk explained.
- [ ] Evidence kept: bank statements, invoices, insurer statements, deeds, court or written
      alimony arrangement, diet confirmation from doctor or dietitian.

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
