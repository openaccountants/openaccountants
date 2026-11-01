---
name: md-property-tax
description: >
  Calculate Moldova's 2026 local immovable-property and land taxes and prepare
  the applicable BIJ17, unified-return or individual-notice workflow. Establish
  the liable owner or user, cadastral valuation status, locality, ownership dates,
  land category and fertility index before selecting a base and rate. Covers
  evaluated buildings and land, unevaluated property under Law 1056, fractional
  and undivided ownership, new and transferred objects, exemptions, municipal
  decisions, IT-park transitions and separate filing/payment cutoffs. Maps the
  actual BIJ17 main calculation and locality/relief annexes, individual notice
  fields and public payment entry. Use for annual property tax, land tax,
  September/March filing or checking a municipal notice. Wealth tax, rental
  income and disposal gains use their own connected methods.
jurisdiction: MD
category: international
job: property-tax
tax_year: 2026
last_updated: 2026-10-31
tier: 2
version: "0.2"
---

# Moldova immovable-property and land tax, 2026 v0.2

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Identify the taxable object, liable person and municipality before calculating. Code 277 covers resident and nonresident owners, specified holders of possession/management/use rights over public property, tenants of property from public authorities/budget institutions, finance lessees, lessees of private agricultural property unless the contract provides otherwise, and tenants of private nonresident-owned property unless the contract provides otherwise. Absence of a title or registration does not remove liability for actual possession, use or disposal. Public bodies must give their covered tenants the estimated/accounting value without charge by **25 May**. [Code 276–278][code].

Fractional common owners account for their shares. For undivided common ownership, one is taxpayer by agreement and all are jointly liable. Taxable objects include land inside/outside settlements, buildings, houses, apartments and isolated premises, including unfinished construction at least **50% complete** and still unfinished **3 years** after construction began. The statutory expert/competent-authority completion assessment controls. [Code 277(3)–(4),278][code].

Separate assessed objects under Title VI from objects **not evaluated for tax by the cadastral authority**, which use Law 1056, article 4 and annexes 1–2. The transitional law continues **until 1 January 2028**. Its historic rollout dates do not permit an unevaluated object to be treated as evaluated: article 4(3¹) expressly retains the unevaluated branch. [Law 1056 article 4(2)–(3¹)][transition].

## Rates, bands and thresholds

| Object or condition | 2026 calculation rule | Official source |
|---|---|---|
| Evaluated residential property/attached land, garages/land and garden-association lots with or without buildings | Minimum **0.05%** of estimated value; obtain the actual annual council rate | [Code 280(1)(a)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro) |
| Evaluated agricultural land with buildings | Minimum **0.1%** of estimated value; obtain actual annual council rate | [Code 280(1)(a¹)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro) |
| Evaluated other nonresidential/nonagricultural property, excluding garages and garden lots | **0.3%** of estimated value | [Code 280(1)(b)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro) |
| Neglected built-up property/land; agricultural land uncultivated for **2 consecutive years**, from the **third year** | Council can increase tax “până la **300%**”; use the actual decision, classification and prescribed percentage calculation, not an assumed universal multiplier | [Code 280(1¹)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro); [BIJ17 instruction I.6,III.10](https://www.legis.md/UserFiles/Image/RO/2024/mo459-461ro/anexa2_73.docx) |
| Unevaluated agricultural land, including separate hay/pasture categories | Council rate per degree-hectare if a cadastral fertility index exists; otherwise per hectare. Water-covered land uses its own per-hectare council rate | [Law 1056 annex 1 point 1](https://www.legis.md/cautare/getResults?doc_id=149718&lang=ro) |
| Unevaluated intravilan home/adjacent lots and other listed intravilan categories | Applicable council rate per **100 m²**; distinguish locality/category and specially allocated extravilan home plots | [Law 1056 annex 1 point 2](https://www.legis.md/cautare/getResults?doc_id=149718&lang=ro) |
| Unevaluated other extravilan land; land with buildings/quarries/production-damaged land | Separate council rates per hectare for annex 1 points **3** and **4** | [Law 1056 annex 1](https://www.legis.md/cautare/getResults?doc_id=149718&lang=ro) |
| Unevaluated buildings, including rural residences | Actual council percentage of accounting value for business taxpayers, or statutory cost/inventory value for other individuals; classify agricultural/other/residential categories separately | [Law 1056 article 4(5),(9),annex 2](https://www.legis.md/cautare/getResults?doc_id=149718&lang=ro) |
| Part-year object | Annual calculated amount ÷ **365/366** × actual days of ownership/possession/use/disposal; use **365** for 2026 | [BIJ17 instruction I.6](https://www.legis.md/UserFiles/Image/RO/2024/mo459-461ro/anexa2_73.docx) |
| Eligible unified-return taxpayer | Individual entrepreneur/farm, annual average staff at most **5**, not VAT-registered: identify the applicable UNIF25 branch; filing/payment ordinarily **25 March** next year | [Code 281¹(2),282(3)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro); [Law 1056 article 4(7)(d),(9)(c)](https://www.legis.md/cautare/getResults?doc_id=149718&lang=ro) |

The current Code supplies minimum rates for the first two evaluated categories, not the former blanket 0.4% ceiling. Council rates, relief limits and neglect decisions must be obtained for the object's actual locality and year. Law 1056 article 4(4¹) provides for publication of collected council-rate information by SFS; the underlying enacted decision determines the applicable amount. [Code 280][code]; [Law 1056 article 4(4)–(4¹)][transition].

## The base

Build one workpaper per object: cadastral identifier, locality/CUATM, property/use category, evaluated status and valuation date, estimated/accounting/inventory value or plot area, fertility index where applicable, ownership share and dates, actual council decision, relief evidence and filing class. For evaluated property use the cadastral estimated value. Cadastral bodies use statutory mass/individual valuation methods; article 279 provides revaluation every **3 years** under Government procedure. Do not replace the official tax value with purchase price. Supplying valuation data is required; refusal permits valuation by comparable objects. [Code 278–279,285][code].

For ordinary businesses, registered entrepreneurs and justice/health professionals, use the **1 January** value; new objects/new taxpayers start from registration or established actual rights. For an unevaluated business acquisition use accounting value at acquisition. Nonbusiness individuals' assessed base is ordinarily the 1 January estimate; if first cadastral valuation occurs before the notice is sent during the year, article 281(1) uses that registered estimate. For unevaluated nonbusiness property use cadastral archive documents and/or the municipality commission's inventory value. [Code 281][code]; [Law 1056 article 4(5),(9)(a)][transition].

Compute each plot/object separately when rates or fertility indices differ, then sum. For agricultural land with an index: hectares × fertility index × council rate per degree-hectare; without an index: hectares × the correct per-hectare rate. Convert an intravilan square-metre area to units of 100 m² before multiplying by its rate. Subtract only documented statutory/council relief. [Law 1056 article 4(7),annex 1][transition]; [BIJ17 instruction I.6,III.7–12][bijinstructions].

On a transfer, apportion the predecessor and successor's periods; the former taxpayer can request/recalculate the proportionate tax. Inheritance and gifts carry the predecessor's unpaid obligation under article 281(3). The inherited-property value cap applies to the inheritance branch, not automatically to a gift. A wholly demolished/destroyed object stops being taxed from registry cancellation or cessation of actual rights. For actual IT-park residents, property tax is included in the single tax; a mixed ordinary/park year uses the **number of ordinary-regime months**, a different allocation from ordinary daily ownership proration. [Code 281(2),(2¹),(3),(4),282¹][code].

### Exemption and council-relief decision

Article 283(1) covers public authorities/budget institutions; the specified blindness/deafness/disability societies and statutory enterprises; penitentiary enterprises; the named prosthetics/orthopaedic rehabilitation centre; civil-protection objects; worship property; diplomatic/consular/international missions subject to reciprocity/treaties; qualifying AOAM-funded public medical/family-doctor institutions; CNAM/agencies; BNM; property requisitioned in public interest for that period; and qualifying article-52 nonprofits operating social-assistance institutions. Match the precise institution and use, rather than exempting every nonprofit, clinic or religious-owned asset. [Code 283(1)][code].

Article 283(1)(h)–(l) separately covers statutory pension-age and specified disability/rehabilitated-repression groups; qualifying fallen-defender and Afghanistan-war families/dependants; families with disabled children up to **18** and family members who permanently maintain and care for persons with disabilities; and qualifying Chernobyl-death families/dependants. The home relief concerns registered domicile, or residence if no domicile, up to the council's approved value/cost limit. Until a local limit is fixed, use the **specific locality's Title VI annex limit**, not a universal allowance. The provision also identifies covered unevaluated homes/adjacent land. Entitlement begins/ends in the **month** the right arises/ceases. [Code 283(1)(h)–(l),(2)–(3) and Title VI annex][code].

Article 283(4) also covers the specified reserve/park/botanical land; forestry and water-fund land under the stated nonbusiness/management conditions; scientific/instructional agricultural/forestry use; perennial plantations before bearing fruit; the listed state/union-funded cultural, educational, medical, sporting/recreation and monument land, excluding balneal institutions; permanent railway/public-road/river-port/runway land; border/public-use land; restored damaged agricultural land for **5 years**; and Government-restricted polluted land. Free-zone administrations have article 283(5)'s exemption for land and plots while held in their management. Preserve the exact use and statutory conditions. [Code 283(4)–(5)][code].

From **30 October 2026**, article 283(6) exempts qualifying irrigation-user associations' central irrigation/drainage-system property held under free-use arrangements **only while the system is nonfunctional**. The competent National Land Improvement Agency director issues the annual functionality decision by **1 March**, based on the required report, and sends it to SFS/local authorities within **10 days**. Do not assume a functioning system is exempt or backdate this newly operative provision to the whole year. [Current Code 283(6) and LP235 commencement header][code].

Council relief under article 284 requires the actual decision: considerable disaster/fire damage, relocation of a polluting enterprise during the specified construction period, or long illness/death proved by medical/death certificate. Public-housing tenants' primary-home exemption is discretionary too. Preserve the commission assessment where required; decisions are transmitted to SFS within **10 days**. A circumstance alone is not a granted relief. [Code 284][code].

## Deadlines and filing

### Select the actual clock

The calendar year is the tax period. Do not use the assessed-property payment cutoff for the unevaluated branch. All deadlines below are subject to Code 129(8)'s first-following-working-day rule when the last day is a rest day. [Code 280¹,129(8)][code].

| Taxpayer/object branch | Filing/notice | Payment | Source |
|---|---|---|---|
| Ordinary self-calculator, evaluated property existing/acquired through **31 August** | BIJ17 by **25 September** current year | Through **25 September** acquisitions: **25 September** current year | [Code 281¹(1),282(1)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro) |
| Ordinary self-calculator, evaluated property acquired after **31 August** | BIJ17 by **25 March** next year | If acquired through **25 September**, pay **25 September** current year; if after **25 September**, pay **25 March** next year | [Code 281¹(1),282(1),(4)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro) |
| Unevaluated land, ordinary business/professional self-calculator, through **31 August** | BIJ17 by **25 September** current year | **25 September** current year | [Law 1056 article 4(7)(a)](https://www.legis.md/cautare/getResults?doc_id=149718&lang=ro) |
| Unevaluated land acquired after **31 August**, same class | BIJ17 **25 March** next year | **25 March** next year | [Law 1056 article 4(7)(a)](https://www.legis.md/cautare/getResults?doc_id=149718&lang=ro) |
| Unevaluated buildings, business/professional self-calculator | Through **31 August**: BIJ17 **25 September**; later acquisition: **25 March** next year | Same respective filing deadline | [Law 1056 article 4(9)(a)](https://www.legis.md/cautare/getResults?doc_id=149718&lang=ro) |
| Nonbusiness individual, objects existing/acquired through **31 March inclusive** | Municipal SCITL calculation/notice by **15 June** | **30 June** current year | [Code 281(1),282(1¹),286](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro); [Law 1056 article 4(7)(b)–(c),(9)(b)](https://www.legis.md/cautare/getResults?doc_id=149718&lang=ro) |
| Nonbusiness individual, acquisition after **31 March** | Notice by **1 February** next year | **25 March** next year | [Code 282(4¹),286](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro); [Law 1056 article 4(7)(b)–(c),(9)(b)](https://www.legis.md/cautare/getResults?doc_id=149718&lang=ro) |
| Peasant farm's unevaluated land | SCITL notice route under Law 1056 article 4(7)(b), rather than automatically the ordinary business BIJ17 route; confirm actual unified-return status and the form instructions | **30 June** or **25 March** next year according to acquisition date | [Law 1056 article 4(7)(a)–(d)](https://www.legis.md/cautare/getResults?doc_id=149718&lang=ro) |

For an eligible small individual entrepreneur/farm using UNIF25, use the [income-tax method's eligibility/transition test](moldova-income-tax.md#unif25-income-tax-worksheet) and [actual unified property tables 6–7](md-tax-overview.md#unif25-local-tax-and-property-reporting-interface). Retain the land-specific farm distinction above: Law 1056(7)(d) names individual entrepreneurs, while (9)(c) expressly names both entrepreneurs and farms for buildings. Do not silently expand a land exception or mistake inclusion of a form row for a new tax obligation. [Law 1056 article 4(7),(9)][transition]; [Order 300/2025 instructions](https://www.legis.md/UserFiles/Image/RO/2025/mo309-312ro/an2_300ro.docx).

### Prepare and submit BIJ17

1. **Select the reporting population.** Order 73's BIJ17 covers taxpayers required by Code 281¹/Law 1056. Fully exempt taxpayers in that population still file; no taxable objects means no calculation. Keep the unified-return exception above separate. [Current approval][bijorder]; [instruction I.1–3][bijinstructions].
2. **Access the taxpayer's filing service.** Use SFS's **Cabinetul personal al contribuabilului**, electronic-signature authentication and the authorised company/role, then **Declarație electronică** for the calculation. CTIF describes initial entry as the natural-person signatory followed by company/role selection; first access requires its connection agreement. Do not file under the signatory's personal taxpayer identity for a company. [CTIF official access instructions](https://ctif.gov.md/intrebari-frecvente); [AGE service](https://www.egov.md/ro/content/serviciul-declaratia-electronica); [Code 187][code].
3. **Enter the actual header.** Fiscal code, taxpayer name, headquarters CUATM, SFS subdivision, principal CAEM activity, period **A/2026**, submission date and the appropriate **25 September / 25 March** filing marker. Use the correct period even when filing next year. [Actual BIJ17][bijform]; [instruction II][bijinstructions].
4. **Prepare locality and relief annexes first when needed.** No objects outside headquarters locality and no relief: main calculation only. Outside-locality objects and/or relief: prepare annex **1**, and annex **2** for relief. Annex 1 records each locality's CUATM in column **2**, category bases in **3–9**, calculated taxes in **10–16**, relief in **17**, net taxes in **18–24**, locality total in **25**. Annex 2 records CUATM **2**, actual annex-3 relief code **3**, category reliefs **4–10** and locality relief total **11**. Number rows across all pages; total all columns and reconcile relief by locality. [Instructions I.4–5,IV–V][bijinstructions].
5. **Complete the seven main categories.** **R1** agricultural land, **R2** other land, **R3** hay/pasture, **R4** accounting-value immovable property, **R5** estimated-value Code 280(a), **R6** 280(a¹), **R7** 280(b). Column **5** is area for R1–R3, accounting value for R4, estimated value for R5–R7; include the base of exempt objects. Column **6** is the actual percentage/per-hectare rate; leave it blank when category rates differ. Column **7** is agricultural fertility index where applicable; leave blank when indices differ. Calculate each underlying plot separately. The printed generic header “5×6×7” does not require multiplying a building by a fictitious fertility index. [Actual form][bijform]; [instructions III.7–10][bijinstructions].
6. **Reconcile totals before signature.** Column **8** calculated tax, **9** relief, **10 = 8−9** net payable. **R8** sums R1–R7. R8 column 8 equals annex-1 total columns 10–16; R8 column 9 equals annex-1 column 17 and annex-2 column 11; R8 column 10 and **Suma de control** equal annex-1 column 25 and its total columns 18–24. Do not add land areas to money totals. Use annex-3 relief codes for the actual entitlement, not a similar institution's code. The generic “Alte înlesniri” entry does not itself prove a new statutory relief or the accepted electronic code for it. [Instructions III.10–14,IV.19–23,V.24–30][bijinstructions]; [actual annex 3][bijform].
7. **Sign, submit and retain acceptance.** Code 187 requires the prescribed electronic signature; keep the accepted electronic receipt, exact return/annexes and workpaper. Merely saving or signing a draft is not receipt by SFS. For an error, Code 188 uses the form/method valid for the corrected period, ordinarily within **6 years** of that return's due date, subject to the specific audit restrictions. Pay by the independently selected deadline and locality, not merely when the return is submitted. [Code 187(3)–(6),188,282][code]; [Law 1056 article 4(10)][transition].

### Check an individual's notice and pay

SCITL issues the nonbusiness calculation. The operative Order 17 attachments distinguish evaluated property through March (**annex 1**) / later acquisitions (**annex 5**) and unevaluated property/land through March (**annex 2**) / later acquisitions (**annex 6**). These are authority notices, not a BIJ17 to be self-filed by every homeowner. [Order 17][noticeorder].

For evaluated property, reconcile object columns **1–7**: cadastral number, address, share, estimated value, rate, tax, and the actual neglect/uncultivated increase. The settlement table separates principal debt/credit, late charge, current tax, relief and payable. For unevaluated notices, columns **1–7** are IBAN, principal debt/credit, late charge, base, calculated current tax, relief and total. Read area units carefully: the notice prints **ari**, whereas the business form uses hectares for land. The annex-6 Russian payable heading still prints **30 June** while Romanian prints **25 March**; the enacted late-acquisition rule above controls. [Actual annexes 1,2,5,6 linked in Order 17][noticeorder]; [Law 1056 article 4(7),(9)][transition].

On [MPay “Impozitul pe bunuri imobiliare (cu aviz de plata)”](https://mpay.gov.md/Order/Search/SFS03), the entry key is **Aviz nr.**, the notice number received from the municipality/SFS, followed by its **“Caută Aviz nr.”** action and terms/consent. The public page links electronic-signature holders to SFS's **Fișa imobilului** service for online notice generation. Reconcile the retrieved notice and payment reference; retain the receipt and account allocation. Do not use the wealth service's IDNP key for a property notice or send all localities' property taxes to headquarters. [Actual MPay entry][mpay]; [Code 282(1),(1¹)][code]; [Law 1056 article 4(10)][transition].

## Penalties and interest

For unpaid tax, apply Code 228's daily late charge from the day after the correct due date through actual payment inclusive, with its statutory exclusions; the [VAT method holds the sourced 2026 benchmark](moldova-vat.md#penalties-and-interest). BIJ17 reporting failures engage Code 260: the article-232(b) nonbusiness population has **MDL 200–400 per return**, maximum **2,000**, and the 232(a),(c) business/professional population **500–1,000**, maximum **10,000**, under the actual offence test. Do not apply a filing fine to a notice-only individual as though BIJ17 were required. For percentage-based tax, understatement through an untrue return under 261(4) is **20–30%** of understated tax; 261(4¹)'s voluntary truthful correction exception has its own conditions, and deliberate evasion is a different offence. Do not extend that percentage-tax offence automatically to a fixed land-tax calculation. [Code 228,232,260–261][code].

For an adverse SFS decision/action, the article-267¹ ordinary challenge clock is **30 days** from communication/notification, subject to its restoration test; file with SFS under 267² and retain proof. A municipal decision's actual competent appeal route must be established from that decision and governing procedure; do not label every SCITL/local-council act an SFS decision. [Code 267–267³][code].

## Cross-border points

Moldovan property liability expressly includes nonresidents. Inspect the actual private-nonresident rental contract to identify the liable tenant/owner under 277(1)(f); a foreign address does not exempt the object. Diplomatic/consular relief requires the statutory accreditation/reciprocity/treaty facts. Foreign income-tax credits, rental income and disposal gains are separate questions; the [wealth-tax method](md-wealth-tax.md) additionally tests individual residential holdings. [Code 277,283(1)(g)][code].

## Two worked examples that recompute

### 1. September purchase: payment precedes filing

Assume an ordinary company acquires and holds an evaluated office from **1 September through 31 December 2026**, 122 days, with official estimated base MDL 1,000,000, no relief, no neglect classification and the statutory other-property rate 0.3%. Annual tax is MDL 3,000; the part-year calculation is MDL 1,002.739726 before any actual accepted final rounding. Acquisition after 31 August makes the BIJ17 due **25 March 2027**, but acquisition before 25 September makes payment due **25 September 2026**. These are deliberately different clocks. [Code 280(b),281¹,282][code]; [BIJ17 I.6][bijinstructions].

```oa-check
name: Moldova evaluated office daily allocation and return reconciliation
tolerance: 0.0001
inputs:
  estimated_value: 1000000
  rate: 0.003
  held_days: 122
  year_days: 365
  relief: 0
steps:
  annual_tax: estimated_value * rate
  calculated: annual_tax / year_days * held_days
  payable: calculated - relief
  control_sum: payable
expected:
  annual_tax: 3000
  calculated: 1002.739726
  payable: 1002.739726
  control_sum: 1002.739726
```

### 2. Unevaluated agricultural plots: fertility, categories and relief

Use **Boscana only**, whose 2026 decision 6/3 annex sets MDL **2 per degree-hectare** for ordinary indexed agricultural land and **0.75** for indexed hay/pasture. Assume a full-year business with an ordinary 2-hectare plot at index 60 and a separate 1-hectare pasture at index 50. Gross amounts are MDL 240 and 37.50. Assume a documented, actually granted relief of MDL 60 on the first plot. BIJ17 R1/R3 gross total is 277.50, relief total 60 and net/control total 217.50. That relief is a hypothetical input, not an entitlement created by the example. Another municipality needs its own actual decision. [Boscana annex 1 section II.6][boscana]; [Law 1056 article 4(7),annex 1][transition]; [BIJ17 totals][bijinstructions].

```oa-check
name: Moldova Boscana unevaluated plots and relief reconciliation
tolerance: 0.0001
inputs:
  ordinary_hectares: 2
  ordinary_index: 60
  ordinary_rate: 2
  pasture_hectares: 1
  pasture_index: 50
  pasture_rate: 0.75
  authorised_relief: 60
steps:
  r1_gross: ordinary_hectares * ordinary_index * ordinary_rate
  r3_gross: pasture_hectares * pasture_index * pasture_rate
  r8_gross: r1_gross + r3_gross
  r1_net: r1_gross - authorised_relief
  r8_net: r1_net + r3_gross
  annex1_total: r8_gross - authorised_relief
  control_difference: r8_net - annex1_total
expected:
  r1_gross: 240
  r3_gross: 37.5
  r8_gross: 277.5
  r1_net: 180
  r8_net: 217.5
  annex1_total: 217.5
  control_difference: 0
```

## Ask the client first

1. Which objects, localities, rights, ownership shares and acquisition/disposal dates apply, including public/nonresident leases and unfinished construction?
2. Which objects have an official tax valuation, and what are the relevant estimated/accounting/inventory values, areas and fertility indices?
3. What enacted council rates, neglect/uncultivated decisions, exemption limits and individual relief decisions apply for 2026?
4. Are you a company, professional, nonbusiness individual, entrepreneur or farm, and what are the actual VAT/staffing and IT-park entry/exit facts?
5. What returns/notices, account balances, payment references, accepted corrections and dispute dates already exist, and who is authorised to file/pay?

## Sources

| Official source | Read scope | Read date |
|---|---|---|
| [Current Fiscal Code][code] | Complete Title VI articles 276–287 and annex; selected 129,187–188,228,232,260–261,267–267³; LP235 effective 30 October header | 2026-10-31 |
| [Law 1056/2000, operative 2026 version][transition] | Full article 4 and annexes 1–2, including 2028 continuation and unevaluated farm/deadline distinctions | 2026-10-31 |
| [SFS Order 73/2021][bijorder], [actual BIJ17 and three annexes][bijform], [current instructions][bijinstructions] | Full original form/instructions, all five/three rendered pages; original annex-3 code register | 2026-10-31 |
| [MF Order 17/2020, operative 2026 version][noticeorder] | Full approval; actual annexes 1,2,5,6, each original DOC/text/rendered page; annex-6 bilingual deadline discrepancy retained | 2026-10-31 |
| [CTIF official access FAQ](https://ctif.gov.md/intrebari-frecvente), [AGE service](https://www.egov.md/ro/content/serviciul-declaratia-electronica), [MPay property entry][mpay] | Public authentication/role guidance and entry fields; no authenticated taxpayer return or payment executed | 2026-10-31 |
| [Boscana 2026 council rates][boscana] | Actual decision 6/3 annex, four pages; only section II.6's indexed agricultural rates used in example | 2026-10-31 |
| [UNIF25 form/instructions](https://www.legis.md/cautare/getResults?doc_id=148910&lang=ro) | Previously read full official attachments and completed review reused through linked income/overview methods | 2026-10-31 |

Not yet confirmed: authenticated BIJ17/UNIF25 technical acceptance and final rounding beyond the stated approved calculations; accepted electronic relief code for the new article-283(6) irrigation exemption and its first-year decision implementation; a specific farm's interaction between the unevaluated-land SCITL rule and unified reporting; taxpayer-specific council-rate amendments, valuation corrections, local relief and municipal appeal route. The legal branches remain in scope; a missing input is not permission to assume a national rate or exclude that taxpayer. Independent review of this new method is pending and Moldova remains partial.

[code]: https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro
[transition]: https://www.legis.md/cautare/getResults?doc_id=149718&lang=ro
[bijorder]: https://www.legis.md/cautare/getResults?doc_id=145681&lang=ro
[bijform]: https://www.legis.md/UserFiles/Image/RO/2021/mo%2057-65%20md/anexa1_73.docx
[bijinstructions]: https://www.legis.md/UserFiles/Image/RO/2024/mo459-461ro/anexa2_73.docx
[noticeorder]: https://www.legis.md/cautare/getResults?doc_id=151864&lang=ro
[mpay]: https://mpay.gov.md/Order/Search/SFS03
[boscana]: https://boscana.sat.md/wp-content/uploads/sites/14/2026/02/Cotele-impozitului-funciar-si-pe-bunurile-imobiliare-2026.pdf
