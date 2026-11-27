---
name: nl-deductions
description: "Compute Dutch resident individual deductions for 2026: own-home interest and forfait, Hillen, high-income rate adjustment, maintenance, care costs, gifts and weekend care. Includes original cases and explicit holds for special situations and earlier years. Trigger: aftrekposten, hypotheekrenteaftrek, zorgkosten, giftenaftrek, partneralimentatie, studiekosten. Business deductions route to nl-zzp-deductions; full tax and credits to nl-income-tax."
version: 1.5
jurisdiction: NL
tax_year: 2026
last_updated: 2026-11-27
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Netherlands: income tax deductions for individuals (aftrekposten) 2026

## Who this applies to

European Netherlands residents throughout 2026. Establish residence, fiscal partnership (including any whole-year election), age at 1 January, income in each box, payment dates and supporting records before calculating. Missing facts mean a hold, not an assumed zero deduction.

Personal deductions comprise maintenance obligations, specific care costs, weekend costs for disabled persons and gifts, plus unused personal deductions from earlier years (Wet IB arts. 6.1–6.2a). Own-home costs are a separate box 1 computation. This Guide does not determine the final tax bill.

## Rates, bands and thresholds

Amounts are EUR; D means verzamelinkomen before personal deductions. Use joint D where the whole-year partner rules apply. The following are 2026 values, not figures for an open 2025 return.

| Item | Amount and operative condition | Official source |
|---|---|---|
| Annual ordinary eigenwoningforfait | WOZ at most 12,500: nil; over 12,500 through 25,000: 0.10%; over 25,000 through 50,000: 0.20%; over 50,000 through 75,000: 0.25%; over 75,000 through 1,350,000: 0.35%; above 1,350,000: 4,725 plus 2.35% of excess. Apply only for the qualifying period. | Wet IB art. 3.112; https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml |
| Ordinary Hillen deduction | 71.867% of positive forfait less attributable deductible home costs; partners combined. | Wet IB art. 3.123a; https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml |
| High-income adjustment | 11.94% × min(covered deductions, max(taxable box 1 income + covered deductions − 78,426, 0)); derived top-band relief 49.50% − 11.94% = 37.56%. | Wet IB art. 2.10(1)–(3); https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml |
| Care-cost increase | D at most 41,123: add 40% of eligible costs, or 113% if taxpayer or qualifying whole-year partner reached AOW age at 1 January. Medical/surgical help and sick-visit travel excluded from increase. | Wet IB arts. 2.10a and 6.19; https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml |
| Care threshold without whole-year partner | D at most 9,680: 166; over 9,680 through 51,411: 1.65% × D; above 51,411: 1.65% × 51,411 plus 5.75% × excess. Deduct only costs above threshold, after increase. | Wet IB art. 6.20(1); https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml |
| Care threshold with whole-year partner/election | Joint costs and D; replace 9,680 with 19,360 and 166 with 332; middle and upper formulas unchanged. | Wet IB art. 6.20(2); https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml |
| Ordinary gifts | Deduct qualifying gifts above max(60, 1% × D), capped at 10% × D, with cultural adjustment below; joint gifts and D for whole-year partners/election. | Wet IB art. 6.39; https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml |
| Periodic gifts | Qualifying deed for at least annual fixed equal payments over at least 5 years, ending no later than death; no floor, annual total cap 1,500,000 (whole-year partners/election together). | Wet IB arts. 6.34 and 6.38; https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml |
| Cultural ANBI uplift | Add 25%, at most 1,250 across ordinary and periodic gifts together, shared by whole-year partners/election; ordinary-gift ceiling rises by the ordinary-gift uplift only. | Wet IB art. 6.39a; https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml |
| Qualifying car travel | 0.25 per km for care travel, weekend transport and waived volunteer travel costs under the 2026 approval. Underlying eligibility conditions still apply. | Decision §2.2, retrospective from 1 January 2026, expiry 1 January 2027 (§3); https://zoek.officielebekendmakingen.nl/stcrt-2026-18302.html |

## The taxable base

### Computation order and partners

1. Establish box 1 income, including business results from **nl-zzp-deductions**, then add the own-home balance below.
2. Apply personal deductions first against box 1, then box 3, then box 2, each no lower than nil; use specific care costs first. Obtain the inspector's appealable decision for unused deductions carried forward (Wet IB arts. 6.1–6.2a).
3. Calculate tax, apply any high-income adjustment, then calculate the applicable credits through **nl-income-tax**. Keep deductions and credits separate.

Personal deductions generally count when paid, set off, made available or made interest-bearing; the last route does not apply to gifts (art. 6.40). Do not allocate a payment to an earlier return simply because it remains open.

Whole-year fiscal partners, or eligible part-year partners jointly electing whole-year treatment, choose the allocation of common own-home income and personal deductions (art. 2.17); the combined allocation must total 100%. Apply joint care/gift thresholds before allocation. Immigration, emigration or uncertainty about the election: Check this point with one of our partner accountants.

### Own home

Establish an eligible main residence: ordinary ownership requires the taxpayer or partner to bear costs/risks and substantially participate in changes in value (art. 3.111). A mortgage secured on a house is not by itself deductible. Establish the eligible loan principal under art. 3.119a, including acquisition/improvement/maintenance or ground-lease buy-out purpose, financing limits, own-home-reserve and exempt-gift reductions and excluded debts.

For ordinary post-2012 debt, the contract and actual repayments must meet at least annuity repayment within the remaining maximum 360 months, and any applicable annual loan-data reporting duty. Linear repayment can meet that test. Refinancing does not automatically restart the term (arts. 3.119a, 3.119c and 3.119g). Pre-2013 debt, arrears, reserve/gift adjustments, family/BV/employer/foreign loans and detailed information requirements: establish eligibility before using an example. Check this point with one of our partner accountants.

Eligible own-home costs are interest (including qualifying penalty interest), financing costs and periodic erfpacht/opstal/beklemming payments (arts. 3.119a(9), 3.120). A ground-lease lump-sum buy-out or building insurance is not itself one of these deductible payments. Borrowing for a qualifying ground-lease buy-out is a separate debt-purpose test. Origination fees, prepaid/late interest, interest refunds, refinancing, transitional debt, residual debt from a sale in 2012–2017 and its deduction term: do not use a blanket deduction or spreading rule. Check this point with one of our partner accountants.

Add the ordinary forfait using the WOZ value for the tax year and qualifying period (art. 3.112). Moving, empty/building homes, rental, multiple homes, separation, business use, bijleenregeling and inherited rights: do not assume that all homes qualify, or that only one can ever qualify. Check this point with one of our partner accountants.

For ordinary Hillen, deduct 71.867% of positive forfait minus attributable costs. Combine partners' income and costs. Costs are allocated to the periods they relate to, subject to the statutory origination-fee exception (art. 3.123a). Timing, employer loans and multiple-home allocation: Check this point with one of our partner accountants.

### High-income rate adjustment

Use the table's formula (art. 2.10). Covered items are entrepreneur deductions, the MKB exemption only where aggregate profit after entrepreneur deductions is positive, the tbs exemption only where the relevant aggregate result is positive, art. 3.120 own-home costs and personal deductions. The adjustment concerns the amount actually deducted; it is not a universal flat deduction rate. Full bands, AOW tax, premiums, credits and other box calculations: **nl-income-tax**; Check this point with one of our partner accountants.

### Maintenance obligations

Periodic payments under a directly arising family-law maintenance obligation can qualify, excluding payments to direct-line relatives or second-degree collateral relatives; child maintenance is excluded (art. 6.3(1)(a)). Retain the arrangement and proof of payment. Lump sums, former cohabitants/moral obligations, social-assistance recovery, pension or annuity settlements, passed-on pensions, legal costs and providing an ex-partner with housing: no automatic award from the relationship label. Check this point with one of our partner accountants.

### Specific care costs

Only illness/disability costs in the statutory categories, borne by the taxpayer and reasonably compelled, qualify (arts. 6.1, 6.16–6.18). They may concern the taxpayer, partner, children under 27, severely disabled household members aged at least 27, and resident care-dependent parents/siblings. For those other than the taxpayer/partner, establish inability to pay their own costs. Medical evidence of disability/dependency is needed where applicable. Reimbursement eligibility must be checked. Special allowances, unreceived special assistance and conscientious-objector cases have distinct rules: Check this point with one of our partner accountants.

- **Medical help and medicines:** treatment by a doctor; paramedical treatment prescribed and supervised by a doctor, or designated paramedics meeting the statement rules; medicines prescribed by a doctor (art. 6.17). Dentist costs can qualify. Remove reimbursable amounts, basic-package exclusions, statutory contributions and mandatory/voluntary own-risk amounts before calculating.
- **Aids:** predominantly for sick/disabled people; ordinary glasses/contact lenses and vision-support aids, replacement laser treatment, scooters, wheelchairs and home adaptations are excluded (arts. 6.17–6.18). Insoles, prostheses, trained assistance/guide/signal/therapy dogs, hearing-aid extra prices and non-vision-supporting prism aids require item-specific assessment. Likewise prevention/vaccinations and under-18 mental-health or dyslexia care: Check this point with one of our partner accountants.
- **Treatment/medicine/aids travel and sick visits:** eligible car travel uses 0.25 per km under Decision §2.2; treatment travel additionally allows parking, ferry and tolls; taxi/other transport uses actual costs under art. 6.17(6). Sick visits require regular visits to someone nursed more than a month, a shared household at the start of nursing, and usual one-way distance over 10 km (art. 6.17(1)(i)). Repeated admissions: Check this point with one of our partner accountants.
- **Other transport:** 925 per year only with written evidence that illness/disability prevents independently walking more than 100 metres, even with aids; deduct relevant reimbursements (art. 6.17(1)(c),(7)).
- **Extra household help:** dated invoices with helper's name/address; count only expenses above the separate threshold: 0% of D through 39,701; 1% over 39,701 through 59,549; 2% over 59,549 through 79,387; 3% above. Whole-year partners/election combine help costs and D before this test (art. 6.17(3)–(5)), then apply the general increase/threshold.
- **Diet:** doctor/dietitian prescription and the regulation's listed diet amount; other diets yield nil. Exact matching, overlapping diets, prescription particulars and part-year amounts require the art. 37 rules. Check this point with one of our partner accountants.
- **Extra clothing/bedding:** 330, or 825 if proven extra expenses exceed 660; illness/disability must last or be expected to last at least a year and the person must belong to the taxpayer's household. Prorate if conditions hold for only part of the year (regulation art. 38).

Apply the table's increase only to art. 6.17(1)(b)–(h) costs, then the income-dependent threshold. The high-income threshold component is the statutory 1.65% × 51,411, not an intermediate rounded 848. Do not duplicate weekend costs in care costs (art. 6.18(1)(j)). A separate low-income tegemoetkoming is not guaranteed solely because credits are unused: Check this point with one of our partner accountants.

### Gifts

A gift requires no direct consideration. Ordinary gifts qualify to ANBIs or recognised SBBI support foundations, not an SBBI merely because of that status (arts. 6.33, 6.35). Check recipient registration and keep written proof. Cash gifts and gifts paid/set off/made available at or after death (or a connected time) are excluded (art. 6.37). Apply the table's floor and ceiling.

Periodic gifts require a qualifying ANBI or qualifying association, fixed equal payments ending no later than death, and a notarial/private deed binding at least annual payments for at least five years (arts. 6.33–6.38). Use the annual cap in the table. Qualifying-association status, foreign recipients, early termination, gifts in kind/claim waivers and required valuation evidence: do not approve on a recipient's label, informal valuation or unsigned intention. Check this point with one of our partner accountants.

Cultural uplift uses one cap across both kinds of gifts and qualifying partners; only the ordinary cultural uplift raises the ordinary ceiling (art. 6.39a). Waived volunteer allowances require an ANBI statement, actual entitlement, ability and willingness to pay and the volunteer's freedom to receive the payment. Waived actual costs must be of a kind normally reimbursed; car costs use 0.25 per km under Decision §2.2. If both allowance and actual costs are waived at the same institution, count actual costs additionally only above the allowance (art. 6.36). Retroactive withdrawal of ANBI/cultural status: Check this point with one of our partner accountants.

### Weekend care and study costs

Weekend care requires extra costs for a severely disabled child/sibling or a person under the taxpayer's mentorship/curatorship (personal interests), aged at least 21 and normally in an institution (art. 6.25). Establish severe-disability status; count only from the 21st birthday. Eligible unreimbursed extra costs use 13 per care day including collection/return days and 0.25 per car kilometre on the normal home–institution distance, under regulation art. 40 and Decision §2.2. Where both partners claim for the same person, each statutory amount is half, rounded up to a whole euro if necessary; then apply any permitted common-deduction allocation. No double claim of the same cost as specific care costs.

Study-cost deduction sections are repealed. A new private course in 2026 is not an ordinary study deduction. The old performance-grant transition (pre-1 July 2015 grant, extended diploma term, 2026 conversion to loan; original study years 2010/2011–2014/2015), exact award and STAP/non-tax successor claims are held: Check this point with one of our partner accountants. A substantiated business-course cost is a separate **nl-zzp-deductions** question.

## Deadlines and filing

Claim in the annual income-tax return; use Mijn Belastingdienst with DigiD. An invited taxpayer must file by the actual invitation deadline, or the granted extension date. Do not assume 1 May 2027 or 1 September 2027 is every taxpayer's date. No invitation, paper/non-resident filing or an outstanding 2025 return: Check this point with one of our partner accountants.

## Penalties and interest

For an ordinary late return, a reminder precedes the formal demand; the authority allows 10 working days from the demand date. After that the standard default penalty is 469, potentially up to 6,709 for repeated lateness; no penalty where there is no fault at all. Interest, estimated assessments, intentional/grossly negligent errors, additional assessments and stopping refunds/allowances need separate analysis: Check this point with one of our partner accountants.

## Cross-border points

Non-residence/part-year residence, qualifying foreign taxpayers, treaty exceptions (including Belgium, Suriname and Aruba), foreign homes/lenders and foreign associations/ANBIs: do not apply a blanket qualifying-taxpayer-only rule. Use **nl-cross-border** and Check this point with one of our partner accountants.

Full credits (general, labour, IACK, elderly, single elderly, young disabled, green and old levensloop credits), box 3 debt/allowances/green investments and actual returns: use **nl-income-tax** / **nl-income-tax-special-groups**. Business investment deductions (KIA/EIA/MIA/Vamil), FOR and S&O/WBSO: **nl-zzp-deductions**. Their previous 2025/2026 tables are not entitlements here. Check this point with one of our partner accountants. Objections route to **nl-tax-objection**, BV tax to **nl-corporate-tax**, and detailed own-home work to **netherlands-owner-occupied-home-tax-scheme**.

## Worked examples

**Example 1: mortgage interest with the tariefsaanpassing.** 2026 resident throughout, below AOW age, no partner or other deductions; main home owned and occupied all year, debt eligibility and remaining repayment/deduction term established. WOZ value EUR 400,000; interest EUR 12,000 on a qualifying annuity loan; salary EUR 95,000. Forfait 0.35% x 400,000 = EUR 1,400. Taxable box 1 income 95,000 + 1,400 - 12,000 = EUR 84,400. Test: 84,400 + 12,000 - 78,426 = EUR 17,974, positive. The adjustment applies to the lower of 12,000 and 17,974, so EUR 12,000. Extra tax 11.94% x 12,000 = EUR 1,432.80. The interest gets relief at 37.56%.

```oa-check
name: Mortgage interest with the 2026 tariefsaanpassing
inputs:
  woz: 400000
  interest: 12000
  salary: 95000
steps:
  - forfait: woz * 0.0035
  - taxable_box1: salary + forfait - interest
  - test_amount: taxable_box1 + interest - 78426
  - adj_base: min(interest, max(test_amount, 0))
  - extra_tax: adj_base * 0.1194
expected:
  forfait: 1400.00
  taxable_box1: 84400.00
  test_amount: 17974.00
  extra_tax: 1432.80
```

**Example 2: care costs and gifts together (edge: cash gift, cultural uplift, periodic gift).** 2026 resident throughout, below AOW age at 1 January, no partner, drempelinkomen EUR 35,000. Care: prescribed medicines EUR 800 and dentist EUR 1,500, nothing reimbursable, nothing under the own risk. All gifts other than the cash collection are bank transfers made during life, without consideration; recipient status and periodic-deed conditions above are established, with no other cultural or periodic gifts. Gifts: EUR 600 by transfer to an ANBI, EUR 400 to a cultural ANBI, EUR 100 cash to a street collection, EUR 1,200 under a 5-year private deed to an ANBI.

Care: the income is not above EUR 41,123, so the medicines get the 40% increase (EUR 320); the dentist is medical help and gets none. Total 2,620. Threshold 1.65% x 35,000 = EUR 577.50. Deduction EUR 2,042.50. Gifts: cash is out. Uplift 25% x 400 = EUR 100. Ordinary gifts counted 600 + 400 + 100 = EUR 1,100. Floor: the higher of EUR 60 and 1% x 35,000 = EUR 350. Excess EUR 750. Ceiling 10% x 35,000 + 100 = EUR 3,600, not reached. Periodic gift EUR 1,200 in full. Gifts EUR 1,950. Total personal deductions EUR 3,992.50.

```oa-check
name: Care costs and gifts, drempelinkomen EUR 35,000 (2026)
inputs:
  drempelinkomen: 35000
  medicines: 800
  dentist: 1500
  gift_anbi: 600
  gift_cultural: 400
  gift_cash: 100
  periodic: 1200
steps:
  - increase: medicines * 0.40
  - care_total: medicines + increase + dentist
  - care_threshold: drempelinkomen * 0.0165
  - care_deduction: max(care_total - care_threshold, 0)
  - uplift: min(gift_cultural * 0.25, 1250)
  - ordinary: gift_anbi + gift_cultural + uplift
  - floor: max(60, drempelinkomen * 0.01)
  - ceiling: drempelinkomen * 0.10 + uplift
  - ordinary_deduction: min(max(ordinary - floor, 0), ceiling)
  - gift_deduction: ordinary_deduction + periodic
  - total: care_deduction + gift_deduction
expected:
  care_deduction: 2042.50
  ordinary_deduction: 750.00
  gift_deduction: 1950.00
  total: 3992.50
```

### Earlier cases retained with their original inputs

**Mortgage nearly repaid (2026):** below AOW age, no partner, all-year eligible home; WOZ 300,000, interest 300, no other costs/timing issue. Forfait 1,050; difference 750; Hillen 750 × 0.71867 = 539.0025 (539.00 displayed); residual 210.9975 (211.00 displayed). Source: Wet IB arts. 3.112 and 3.123a.

```oa-check
name: Original 2026 Hillen case
inputs:
  woz: 300000
  interest: 300
steps:
  - forfait: woz * 0.0035
  - difference: forfait - interest
  - hillen: difference * 0.71867
  - residual: difference - hillen
expected:
  forfait: 1050
  difference: 750
  hillen: 539.0025
  residual: 210.9975
```

**Original gifts case (2026):** retain D 60,000, no partner, ANBI bank gift 600, cultural ANBI bank gift 400, cash collection 100 and periodic ANBI gift 1,200 under a five-year private deed. Use the same established eligibility/payment assumptions as Example 2. Cash excluded; uplift 100; ordinary total 1,100; floor 600; ordinary deduction 500; ceiling 6,100 not reached; periodic 1,200; total 1,700. Source: Wet IB arts. 6.33–6.39a.

```oa-check
name: Original gifts at income 60000 in 2026
inputs:
  income: 60000
  anbi: 600
  cultural: 400
  cash: 100
  periodic: 1200
steps:
  - uplift: min(cultural * 0.25, 1250)
  - ordinary: anbi + cultural + uplift
  - floor: max(60, income * 0.01)
  - ceiling: income * 0.10 + uplift
  - ordinary_deduction: min(max(ordinary - floor, 0), ceiling)
  - total: ordinary_deduction + periodic
expected:
  ordinary_deduction: 500
  ceiling: 6100
  total: 1700
```

**Original separation case, non-usable tax conclusion:** 2026, separated less than two years, 50% ownership, ex occupies under an alimony arrangement, whole-home forfait input 1,200. Arithmetic 50% × 1,200 = 600 only. Own-home status, interest entitlement, housing-maintenance deduction and treatment after two years are held; no automatic 600 deduction is established. Check this point with one of our partner accountants.

**Original course case:** professional course paid in 2026, no pre-2015 performance grant. No ordinary private study deduction; business purpose goes to nl-zzp-deductions. No grant-transition entitlement is established. Source: Fiscale informatie 2026, study-cost chapter.

## Ask the client first

Use existing records first. Obtain the tax year, residence/partner history, AOW status, all-box income and unused-deduction decisions; WOZ and qualifying occupancy dates; each loan's purpose, start date, balance, repayments, past terms and lender reporting; invoices/payment dates and reimbursement decisions; recipient status, bank proofs and signed gift deeds; maintenance arrangements; and disability/institution/care-day/transport evidence. Clear each hold before presenting a filing position. Missing evidence never proves reimbursement, a stricter mortgage regime, nil entitlement or a regular rather than periodic gift.

## Sources

| Official source and provisions read | URL | Read on |
|---|---|---|
| Wet IB 2001: arts. 2.10, 2.10a, 2.17, 3.111–3.123a and chapter 6. Genuine XML, effective from 21 February; relevant early-2026 amounts checked against 1 January version. | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml | 2026-11-27 |
| Uitvoeringsregeling IB 2001: arts. 37, 38 and 40; diet, clothing/bedding and weekend amounts. | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0012031/2026-01-17_0/xml/BWBR0012031_2026-01-17_0.xml | 2026-11-27 |
| Published approval, Decision 2026-8260, §§2.2 and 3: 2026 mileage permission; not merely the pending bill. Recheck authority for later years. | https://zoek.officielebekendmakingen.nl/stcrt-2026-18302.html | 2026-11-27 |
| Fiscale informatie 2026: read for care conditions, ability to pay, reimbursements, excluded costs and special cases. | https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/aftrek_specifieke_zorgkosten | 2026-11-27 |
| Belastingdienst: read for care transport, actual taxi/public transport costs, parking/ferry/toll and 100-metre evidence. | https://www.belastingdienst.nl/wps/wcm/connect/nl/aftrek-en-kortingen/content/vervoerskosten-ziekte-invaliditeit-aftrekken | 2026-11-27 |
| Fiscale informatie 2026: read for gifts and shared cultural cap. | https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/aftrek_giften | 2026-11-27 |
| Fiscale informatie 2026: read for weekend eligibility, reimbursements and birthday. Statutory half/round-up rule read separately. | https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/aftrek_voor_tijdelijk_verblijf_thuis | 2026-11-27 |
| Fiscale informatie 2026: read for study-cost transition, not a general current course deduction. | https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/aftrek_studiekosten | 2026-11-27 |
| Invitation, filing extension and late-return/no-fault rules: completed reads reused for unchanged rules only. | https://www.belastingdienst.nl/wps/wcm/connect/nl/belastingaangifte/content/moet_ik_aangifte_doen ; https://www.belastingdienst.nl/wps/wcm/connect/nl/belastingaangifte/content/kan-ik-nog-uitstel-aanvragen-belastingaangifte ; https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/boete | 2026-11-22; applicability checked 2026-11-27 |

Not yet confirmed: individual outcomes in the explicit non-usable holds above. These also cover earlier-year figures, special mortgage/maintenance/gift/care cases, full credit/box 3 calculations, business schemes, cross-border cases, interest and future legislation. The former 2028-repeal assertion and bill-stage forecast are not usable 2026 law.
