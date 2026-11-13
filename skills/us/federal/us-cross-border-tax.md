---
name: us-cross-border-tax
description: "Determine the ordinary US federal tax and filing route for inbound nonresidents, US citizens and residents with foreign income, and payers of US-source income to foreign persons. Covers residence, source, ECI versus FDAP, treaty documentation, individual foreign tax credits, foreign account reporting, and filing handoffs for 2026. Use before calculating a cross-border payment or deciding which US return and international schedules are needed."
type: situation-rules
version: 1.0
jurisdiction: US
category: federal
tax_year: 2026
tax_year_notes: "2026 rules; final 2025 individual publications supply continuing statutory procedures, not a claim that final 2026 form layouts have been released."
last_updated: 2026-11-13
tier: 2
domain: tax
---

# US cross-border income: status, withholding, relief and filing

## Scope

Use this guide to classify an ordinary cross-border income case and produce a documented US federal computation and filing handoff. It covers individual residents and nonresidents, and the ordinary chapter 3 withholding responsibilities of payers. Foreign corporate returns, partnership withholding, controlled foreign companies, passive foreign investment companies, foreign trusts and expatriation need the specialist work identified below.

The first question is citizenship and federal residence, followed by the income's source and character. A foreign address, foreign bank account or foreign payer does not alone determine the result. US citizens and resident aliens generally report worldwide income; a nonresident generally separates US-source nonbusiness income from effectively connected income (ECI). [IRS citizens abroad](https://www.irs.gov/individuals/international-taxpayers/us-citizens-and-resident-aliens-abroad); [Publication 519, introduction and chapters 2 and 4](https://www.irs.gov/publications/p519).

The ordinary nonresident FDAP rate is **30% of gross US-source income**, subject to statutory exemptions and a documented treaty rate; ECI is taxed on a net basis. Do not apply 30% to every payment abroad. [IRS nonresident taxation](https://www.irs.gov/individuals/international-taxpayers/taxation-of-nonresident-aliens).

## Ask the client first

- What are all citizenships, immigration statuses, green-card dates, travel days and countries of tax residence? Did status change during the year, or is citizenship or green-card termination planned? These determine worldwide versus nonresident taxation and dual-status periods.
- Who legally and beneficially owns each payment? Is the recipient an individual, corporation, disregarded entity, partnership, trust or intermediary? Obtain the ownership chain before choosing a W-8.
- What income was earned, where was the work performed or property used, and on what dates? Obtain contracts, workday records and gross receipts, rather than inferring source from the bank account.
- What withholding certificates, treaty residence evidence, tax identification numbers and withholding statements are available? Record expiration dates and changes in circumstances.
- What foreign income taxes were legally owed, paid, refunded or disputed? Obtain foreign returns, payment evidence, prior foreign tax credit carryovers and exclusion elections. What returns, estimates and extensions have already been filed? Identify both countries' deadlines, unpaid liabilities and IRS notices.
- What foreign accounts, assets, entities, pensions, trusts and gifts exist? Obtain maximum and year-end values and exchange-rate records. Income-tax relief does not settle information-return obligations.

## The method, step by step

### 1. Establish status and the taxable base [Publication 519](https://www.irs.gov/publications/p519)

1. For a US citizen, start with worldwide income. For a noncitizen, use [US tax residency](../us-tax-residency.md) to document the green-card and substantial-presence tests, excluded days, closer-connection claims, residence dates and any treaty tie-breaker.
2. For a resident period, compute worldwide income through the [individual return guide](us-federal-income-tax-return-1040.md), then apply eligible foreign relief. Foreign wages do not disappear merely because another country taxed them.
3. For a nonresident period, identify US-source income and any foreign-source income treated as ECI. Separate gross-basis FDAP from net-basis ECI before deductions, rates or withholding credits.
4. Treat dual-status years, residence elections with a spouse, treaty residence claims and termination of long-term residence as separate decisions. A treaty residence position can have expatriation consequences; use [US expatriation and exit tax](us-expatriation-exit-tax.md) before making it.

### 2. Source and characterize each item [Publication 519, table 2-1](https://www.irs.gov/publications/p519)

| Ordinary item | Starting source rule | Qualification | Official source |
|---|---|---|---|
| Wages and service fees | Where the services are performed | Allocate multijurisdiction work; special compensation and treaty rules need their own analysis | [Pub. 519, personal services](https://www.irs.gov/publications/p519) |
| Interest | Residence of payer | Statutory exceptions can change source or exemption; US source is not itself proof of taxability | [Pub. 519, interest](https://www.irs.gov/publications/p519) |
| Dividends | Whether the paying corporation is US or foreign | Check the foreign-corporation exception and dividend-equivalent rules | [Pub. 519, dividends](https://www.irs.gov/publications/p519) |
| Rent and real-property gain | Location of property | Real-property gains and rental ECI elections have separate rules | [Pub. 519, rents and real property](https://www.irs.gov/publications/p519) |
| Intellectual-property royalties | Where the property is used | Allocate multiterritory rights using the agreement and actual use | [Pub. 519, royalties](https://www.irs.gov/publications/p519) |
| Inventory and other property sales | Depends on purchased versus produced inventory and the applicable property rule | Do not substitute the customer address for production, sale, tax-home and office rules | [Pub. 519, business income and property](https://www.irs.gov/publications/p519) |

For an individual nonresident, ECI is generally taxed at graduated individual rates after allowable connected deductions. Non-ECI FDAP generally has no deduction against the gross base. A fully withheld investment payment does not automatically require Form 1040-NR, but US business activity, unsatisfied tax, a refund or a deduction claim can require a return. [IRS nonresident taxation](https://www.irs.gov/individuals/international-taxpayers/taxation-of-nonresident-aliens).

### 3. Establish withholding and treaty entitlement [Publication 515](https://www.irs.gov/publications/p515)

| Rule or amount | Conditions and year | Official source and wording |
|---|---|---|
| Default FDAP withholding: 30% | 2026, taxable US-source FDAP paid to a foreign beneficial owner; first test exemptions and treaty entitlement | [IRS nonresident taxation](https://www.irs.gov/individuals/international-taxpayers/taxation-of-nonresident-aliens): "flat 30 percent" |
| UK treaty portfolio dividend: 15% | Ordinary dividend beneficially owned by a qualifying UK-resident individual; no US citizenship/residence saving-clause obstacle, permanent-establishment attribution or special pooled-vehicle issue | [US-UK treaty, art. 10(2)(b)](https://home.treasury.gov/system/files/131/Treaty-UK-7-24-2001.pdf): "15 per cent. of the gross amount"; also arts. 1, 4 and 23 |
| Individual treaty-disclosure failure: USD 1,000 per failure | Only where Form 8833 disclosure is required; exemptions and reasonable-cause relief must be checked | [IRS treaty claims, penalties](https://www.irs.gov/individuals/international-taxpayers/claiming-tax-treaty-benefits): "penalty of $1,000 for each failure" |

Give the payer Form W-8BEN for an individual foreign beneficial owner, W-8BEN-E for an entity, or the appropriate intermediary form where the payee is not the owner. A US person generally documents status on Form W-9. For a treaty claim, establish residence, beneficial ownership, the exact income article, any limitation-on-benefits test, and the required tax identification number. A mailing address alone is insufficient. Read the treaty together with applicable protocols, then the saving clause and its exceptions; many treaties preserve US taxation of citizens and residents. [IRS treaty claims](https://www.irs.gov/individuals/international-taxpayers/claiming-tax-treaty-benefits); [US-UK treaty, arts. 1 and 23, as an example](https://home.treasury.gov/system/files/131/Treaty-UK-7-24-2001.pdf).

Form W-8ECI generally documents qualifying ECI withholding relief. It does not replace individual personal-service withholding, partnership section 1446 withholding or FIRPTA. Treaty-exempt individual services may instead require Form 8233. For entities, separately establish chapter 4 status; an income-tax treaty does not by itself satisfy FATCA documentation. [Publication 515, documentation and ECI withholding exceptions](https://www.irs.gov/publications/p515).

Retain the signed certificate, validation and payment record. Apply the permitted rate only while the certificate and underlying facts support it; refer uncertain or contradictory documentation before payment. Review Form 8833 reporting separately from the payer's certificate. [IRS treaty claims](https://www.irs.gov/individuals/international-taxpayers/claiming-tax-treaty-benefits).

### 4. Relieve double taxation without double relief [Publication 514](https://www.irs.gov/publications/p514)

For an ordinary individual foreign tax credit, establish a qualifying tax imposed on the taxpayer and its legally owed amount. Taxes exceeding the treaty amount are not automatically creditable just because withheld. Choose credit or deduction consistently and exclude taxes attributable to income excluded under the foreign earned income or housing exclusions. Corporations use Form 1118 rather than the individual Form 1116. [IRS foreign tax credit](https://www.irs.gov/individuals/international-taxpayers/foreign-tax-credit).

Allocate expenses, classify each foreign income basket, and calculate its limitation separately:

`FTC limit = pre-credit US income tax × foreign-source taxable income in the basket / total taxable income`.

Use the smaller of qualifying available foreign tax and the limitation, subject to the form's adjustments. Preferentially taxed gains/dividends, losses, treaty re-sourcing and AMT can change the inputs. An ordinary eligible unused credit may carry back **1 tax year** and forward **10 tax years**; special categories and the election to claim without Form 1116 have different restrictions. [Publication 514, limit and carryback/carryover](https://www.irs.gov/publications/p514).

Use [US FEIE and foreign tax credit](us-feie-ftc.md) for exclusion eligibility, tax-home and time tests, stacking and the detailed election comparison. Do not combine an exclusion and a credit on the same income tax.

### 5. Screen foreign information returns [IRS comparison table](https://www.irs.gov/businesses/comparison-of-form-8938-and-fbar-requirements)

| Reporting trigger | Conditions | Official source |
|---|---|---|
| FBAR aggregate accounts exceed USD 10,000 at any time in the calendar year | US person with a financial interest or signature authority, subject to the applicable exceptions; aggregate accounts, not each account separately | [IRS FBAR comparison, reporting threshold](https://www.irs.gov/businesses/comparison-of-form-8938-and-fbar-requirements) |
| Form 8938, US-based individual: over USD 50,000 at year-end or USD 75,000 during year | Unmarried or married filing separately; specified assets and a required income-tax return | [IRS Form 8938 comparison](https://www.irs.gov/businesses/comparison-of-form-8938-and-fbar-requirements) |
| Form 8938, US-based joint return: over USD 100,000 / USD 150,000 | Year-end / during-year tests | [IRS Form 8938 comparison](https://www.irs.gov/businesses/comparison-of-form-8938-and-fbar-requirements) |
| Form 8938, qualifying individual abroad: over USD 200,000 / USD 300,000 | Year-end / during-year tests; unmarried or separate filer meeting the form's living-abroad definition | [IRS Form 8938 comparison](https://www.irs.gov/businesses/comparison-of-form-8938-and-fbar-requirements) |
| Form 8938, qualifying joint filers abroad: over USD 400,000 / USD 600,000 | Year-end / during-year tests; living-abroad definition must be met | [IRS Form 8938 comparison](https://www.irs.gov/businesses/comparison-of-form-8938-and-fbar-requirements) |

Form 8938 attaches to the income-tax return; FBAR is filed separately with FinCEN. One does not replace the other. Screen ownership and transactions for Forms 5471, 8865, 8858, 8621, 3520 and 3520-A as relevant, using each form's current instructions; a foreign pension is not automatically exempt. [IRS citizens abroad, foreign trusts and resources](https://www.irs.gov/individuals/international-taxpayers/us-citizens-and-resident-aliens-abroad).

## Boundary and exception table

| Situation | Required treatment or handoff |
|---|---|
| Remote work for a foreign employer while physically in the US | Source the services from actual work location and test residence; the foreign payer does not create an exclusion. [Pub. 519](https://www.irs.gov/publications/p519) |
| Nonresident US real estate | Separate rent, any net-income election, sale taxation and FIRPTA withholding; use [nonresident capital gains](../us-nonresident-cgt.md) and current Pub. 515 real-property provisions. |
| Foreign partner in a US partnership | Section 1446 can require withholding regardless of cash distributions; W-8ECI is not a general exemption. [Pub. 515](https://www.irs.gov/publications/p515) |
| Foreign corporation doing US business | Obtain a Form 1120-F and protective-return analysis, including branch taxes and treaty permanent establishment; do not use individual graduated rates. [Pub. 515, ECI](https://www.irs.gov/publications/p515) |
| Related-party cross-border payments | Also use [US transfer pricing](us-transfer-pricing.md); treaty withholding does not establish an arm's-length price. |
| Work abroad or temporary assignment | Income-tax treaties and social-security agreements are different tests. Use [US social contributions](us-social-contributions.md) for coverage and certificate-of-coverage analysis. |
| Puerto Rico or another US territory | Use territory-specific residence and source rules; this ordinary foreign-country method is not a substitute. [Pub. 519, territories](https://www.irs.gov/publications/p519) |
| Prior undisclosed accounts, treaty dispute, foreign entity or trust | Refer before filing or amending; preserve the evidence and applicable deadlines. Do not assume no income tax means no reporting penalty. |

## Worked cases

### A. Dividend payment with and without the treaty certificate

Assume a UK-resident individual beneficially owns an ordinary US corporation dividend of USD 1,000 in 2026. They are not a US citizen or resident, have no US permanent establishment, qualify under treaty article 23(2)(a), and satisfy article 10. The payer has a valid W-8BEN and no reason to doubt it. The treaty withholding is USD 150 and net payment USD 850. Without reliable documentation establishing a treaty claim, the ordinary withholding amount in this case is USD 300, leaving USD 700. The decision turns on documented eligibility, not a UK bank address. [US-UK treaty arts. 10 and 23](https://home.treasury.gov/system/files/131/Treaty-UK-7-24-2001.pdf); [IRS treaty claims](https://www.irs.gov/individuals/international-taxpayers/claiming-tax-treaty-benefits).

```oa-check
name: UK ordinary portfolio dividend, treaty certificate decision, 2026
inputs:
  gross_dividend: 1000
  domestic_rate: 0.30
  treaty_rate: 0.15
steps:
  - default_withholding: gross_dividend * domestic_rate
  - treaty_withholding: gross_dividend * treaty_rate
  - default_net: gross_dividend - default_withholding
  - treaty_net: gross_dividend - treaty_withholding
  - difference: default_withholding - treaty_withholding
expected:
  default_withholding: 300
  treaty_withholding: 150
  default_net: 700
  treaty_net: 850
  difference: 150
```

### B. Foreign tax exceeds the ordinary individual credit limit

Assume USD 120,000 total taxable income, of which USD 40,000 is foreign-source general-category taxable income after expense allocation. Pre-credit US income tax is an assumed USD 18,000; legally owed, qualifying foreign income tax is USD 8,500. There is no exclusion, preferential-rate income, loss adjustment, AMT, other basket or prior carryover. These are supplied case facts, not a computation of tax on USD 120,000.

The limitation is 18,000 × 40,000 / 120,000 = USD 6,000. Credit USD 6,000, leaving USD 12,000 US income tax and USD 2,500 unused foreign tax to test for permitted carryback/carryover. Crediting the entire USD 8,500 would overstate the credit by USD 2,500. [Publication 514, limit on the credit](https://www.irs.gov/publications/p514).

```oa-check
name: Individual ordinary foreign tax credit limitation, 2026
inputs:
  total_taxable_income: 120000
  foreign_basket_taxable_income: 40000
  us_tax_before_credit: 18000
  qualifying_foreign_tax: 8500
steps:
  - limit: us_tax_before_credit * foreign_basket_taxable_income / total_taxable_income
  - credit: min(qualifying_foreign_tax, limit)
  - residual_us_tax: us_tax_before_credit - credit
  - unused_foreign_tax: qualifying_foreign_tax - credit
expected:
  limit: 6000
  credit: 6000
  residual_us_tax: 12000
  unused_foreign_tax: 2500
```

## When to refuse or refer

Do not choose a treaty rate or certify a W-8 while beneficial ownership, residence, income character or limitation-on-benefits facts remain unresolved. Refer dual-status elections, a long-term green-card termination, foreign corporations/partnerships/trusts, CFC/PFIC inclusions, hybrid payments, disputed credits, late international information returns, treaty competent-authority relief and material prior omissions to a qualified US international-tax practitioner. **AUDIT FLASH POINT:** a treaty residence position that changes long-term resident status can engage expatriation rules; obtain advice before taking it.

State residence, state-source tax and foreign-country tax require separate guides. The federal treaty result is not a state exemption.

## Filing and payment

| Filing or payment | Ordinary deadline and action | Official source |
|---|---|---|
| Calendar-year 2026 Form 1040-NR with wages subject to US income-tax withholding | April 15, 2027, applying the 15th day of the 4th month rule; attach required schedules and claim documented withholding | [Pub. 519, chapter 7, when to file](https://www.irs.gov/publications/p519) |
| Other ordinary calendar-year 2026 Form 1040-NR filers | June 15, 2027, applying the 15th day of the 6th month rule; determine the applicable category rather than relying on nationality | [Pub. 519, chapter 7](https://www.irs.gov/publications/p519) |
| Individual filing extension | File Form 4868 by the applicable ordinary due date for a 6-month filing extension; it does not extend payment time | [Pub. 519, extensions](https://www.irs.gov/publications/p519) |
| Qualifying US citizens/residents abroad | Automatic 2-month filing/payment extension to June 15 when, on the ordinary due date, the taxpayer lives and has their main business/post of duty outside the US and Puerto Rico, or serves in the military/navy outside them; attach the eligibility statement. Further Form 4868 extension generally runs to October 15. Interest runs from the ordinary April due date | [IRS automatic extension abroad](https://www.irs.gov/individuals/international-taxpayers/us-citizens-and-resident-aliens-abroad-automatic-2-month-extension-of-time-to-file) and [IRS filing abroad](https://www.irs.gov/individuals/international-taxpayers/us-citizens-and-resident-aliens-abroad) |
| 2026 withholding reporting | Forms 1042 and 1042-S generally due March 15, 2027; zero withholding under a treaty can still require reporting. Deposit obligations arise earlier under the applicable schedule | [Pub. 515, returns required and deposits](https://www.irs.gov/publications/p515) |

Apply weekend/holiday and applicable disaster relief to the actual case. Do not confuse a filing extension with a withholding-deposit extension or a refund claim.

For an individual return, choose software supporting the required international schedules, reconcile Forms W-2 and 1042-S, complete ECI and non-ECI sections separately on Form 1040-NR, and attach Form 1116 or treaty disclosures where applicable. Use the **final form for the return's year** for field numbers and instructions. The publications read here include final 2025 individual editions; they do not establish final 2026 form layouts. Obtain the required signature and identity validation, transmit, retain the IRS acceptance or postal proof, and separately verify payment using the [IRS payment options](https://www.irs.gov/payments).

For withholding agents, map recipient, income code, gross income, exemption/rate and withheld-tax fields to the current Form 1042-S instructions. Reconcile recipient totals to Form 1042 and deposits; provide recipient copies. Publication 515 (2026) requires **IRIS for electronic 2026 Forms 1042-S**, replacing FIRE for filing season 2027. Form 1042 uses its own filing route. Retain accepted submissions and deposit references. [Pub. 515, what's new and returns required](https://www.irs.gov/publications/p515).

FBAR is generally due April 15 following the calendar year, with an automatic extension to October 15; apply weekend/holiday and applicable special relief. [FinCEN deadline clarification, continuing annual rule](https://www.fincen.gov/system/files/shared/FBAR_Due_Date_Clarification_PD02-02-2018.pdf). File FBAR separately through [FinCEN BSA E-Filing](https://bsaefiling.fincen.treas.gov/), retaining confirmation; test Form 8938 independently. Use current form instructions for their deadlines, valuations and any reporting exceptions. For late filing, payment or deposit, identify the precise form and period, then calculate the applicable penalty and quarterly interest from current IRS instructions; this guide does not supply a universal international-return penalty.

## Completion checklist

- Residence periods, source, income character and beneficial ownership are evidenced.
- Domestic tax, withholding and treaty relief reconcile; tax excluded from income is not also credited.
- Foreign tax credit baskets, allocations, carryovers and exchange rates have workpapers.
- Income-tax, withholding and foreign information returns have each been screened.
- The final return-year forms, actual due dates, acceptance evidence and payment references are recorded.
- Any specialist referral lists the unresolved facts and preserves the filing/payment deadlines.

This is general reference information, not individualized tax or legal advice. A practitioner giving written federal tax advice must establish the relevant facts, use reasonable assumptions and apply the law to those facts under [Circular 230, 31 CFR 10.37](https://www.ecfr.gov/current/title-31/subtitle-A/part-10/subpart-B/section-10.37). This tier 2 version has no accountant sign-off.

## Sources

| Primary source | Portion actually read | Read on |
|---|---|---|
| [IRS Publication 519, 2025 edition](https://www.irs.gov/publications/p519) | Read for introduction; chapter 2 table 2-1 and source rules; chapter 4 resident/nonresident base; chapter 7 deadlines, extensions, protective returns and territories. Continuing procedures, not 2026 form-line evidence | 2026-11-13 |
| [IRS nonresident alien taxation](https://www.irs.gov/individuals/international-taxpayers/taxation-of-nonresident-aliens) | Read for filing categories, ECI/FDAP distinction, gross rate, deductions and return choice | 2026-11-13 |
| [IRS Publication 515, 2026 edition](https://www.irs.gov/publications/p515) | Read for What's new (IRIS); documentation/W-8ECI exceptions; deposit penalties; returns required and due dates | 2026-11-13 |
| [IRS claiming treaty benefits](https://www.irs.gov/individuals/international-taxpayers/claiming-tax-treaty-benefits) | Read for withholding certificates, ownership/residence/LOB conditions, services, disclosure and individual failure penalty | 2026-11-13 |
| [US-UK income-tax convention](https://home.treasury.gov/system/files/131/Treaty-UK-7-24-2001.pdf) | Articles 1 (saving clause), 10 (dividends including exceptions), 23 (qualified persons); treaty published by the US Treasury and linked by the tax authority | 2026-11-13 |
| [US-UK protocol signed July 19, 2002](https://home.treasury.gov/system/files/131/Treaty-UK-Protocol-7-19-2002.pdf) | Read articles I-II, amendments to saving-clause exceptions and pooled-vehicle dividends; the ordinary portfolio rate used here is unchanged | 2026-11-13 |
| [IRS payment options](https://www.irs.gov/payments) | Read individual/business payment routes and confirmation-number lookup | 2026-11-13 |
| [IRS Publication 514, 2025 edition](https://www.irs.gov/publications/p514) | Read for how to figure the credit, limitation, separate categories, allocation and carryback/carryover. Ordinary continuing individual method only | 2026-11-13 |
| [IRS foreign tax credit](https://www.irs.gov/individuals/international-taxpayers/foreign-tax-credit) | Read for qualifying taxes, Form 1116/1118, excluded-income restriction and treaty overwithholding | 2026-11-13 |
| [IRS citizens and residents abroad](https://www.irs.gov/individuals/international-taxpayers/us-citizens-and-resident-aliens-abroad) | Read for worldwide income, foreign trusts/reporting resources, filing extension, e-file and taxpayer identification | 2026-11-13 |
| [IRS Form 8938/FBAR comparison](https://www.irs.gov/businesses/comparison-of-form-8938-and-fbar-requirements) | Read for separate filings, covered filers, thresholds, assets and signature-authority distinction; historical penalty figures were not adopted | 2026-11-13 |
| [IRS extensions abroad](https://www.irs.gov/individuals/international-taxpayers/us-citizens-and-resident-aliens-abroad-extensions-of-time-to-file) | Read for extension options and interest; detailed eligibility in the linked automatic-extension page | 2026-11-13 |
| [FinCEN FBAR](https://www.fincen.gov/report-foreign-bank-and-financial-accounts) | Read for reporting threshold and individual versus preparer e-filing | 2026-11-13 |
| [IRS automatic extension abroad](https://www.irs.gov/individuals/international-taxpayers/us-citizens-and-resident-aliens-abroad-automatic-2-month-extension-of-time-to-file) | Read for eligibility, joint/separate returns, payment interest and required attached statement | 2026-11-13 |
| [FinCEN deadline clarification](https://www.fincen.gov/system/files/shared/FBAR_Due_Date_Clarification_PD02-02-2018.pdf) | Read for the continuing annual April 15 deadline and automatic October 15 extension, not the historical 2017 calendar example | 2026-11-13 |
| [Circular 230, section 10.37](https://www.ecfr.gov/current/title-31/subtitle-A/part-10/subpart-B/section-10.37) | Read for reasonable facts, assumptions and application of law for written advice | 2026-11-13 |

Not yet confirmed: final 2026 Form 1040-NR and Form 1116 field numbering was not verified in this review; use the final return-year instructions before preparation. No unverified form-line numbers or future quarterly interest rates are supplied above.



