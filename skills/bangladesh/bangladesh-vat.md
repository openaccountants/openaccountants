---
name: bangladesh-vat
description: "Bangladesh 2026 VAT/turnover-tax working papers, registration, classification, input-credit conditions and Mushak return preparation. Corrected current law replaces the old deterministic supplier-rate and form-part map."
version: 2.1
jurisdiction: BD
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: computation
category: international
---

# Bangladesh VAT and turnover tax working papers v2.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Standard VAT-registered and turnover-tax-enlisted businesses. Load vat-workflow-base for document ingestion and review architecture. This file prepares transaction and return working papers; sector relief/SROs, EPZ/SEZ, separate-BIN consolidation, supplementary duty, VDS agents and refund claims require specialist review. Rules below state the law read on 14 November 2026; older 2026 filing periods need their applicable versions.

## Ask the client first

- Actual and expected turnover, excluded turnover categories, activity and registration/enlistment certificate/BIN.
- Complete period statements, sales and purchase invoices, customs goods declarations and bank service-import challans.
- Domestic/export/exempt activity, supplier legal entity and any sector SRO.
- Prior credit, credit/debit notes, taxable/business use, payment channel and special-regime flags.

## The method, step by step

### Quick reference and rates, bands and thresholds

| Item and complete condition | Current amount/rate/time | Official source |
|---|---|---|
| Ordinary taxable import/supply, no applicable exception | 15% (source prints ১৫ শতাংশ) | Act section 15: https://bdlaws.minlaw.gov.bd/act-1106/section-42308.html |
| Qualifying zero-rated export/service, with actual section conditions met | 0%; distinguish exemption and input-credit restrictions | Sections 23-24; service text: https://bdlaws.minlaw.gov.bd/act-1106/section-42317.html |
| General registration threshold | Turnover over BDT 5,000,000 (50 lakh, in words on the page) in the relevant rolling/expected 12-month test; excluded values and activity-independent registration apply | Sections 2(57) and 4: https://bdlaws.minlaw.gov.bd/act-print-1106/section-print-42295.html; https://bdlaws.minlaw.gov.bd/act-print-1106/section-print-42297.html |
| Turnover-tax enlistment | Over BDT 3,000,000 (30 lakh, in words on the page) but not over registration threshold, subject to activity rules; application within 30 days of crossing | Sections 2(48), 10: https://bdlaws.minlaw.gov.bd/act-print-1106/section-print-42295.html; https://bdlaws.minlaw.gov.bd/act-1106/section-42303.html |
| Turnover tax before a relevant region/activity-specific fixed-amount notification is made | 4%; section 63 permits specified fixed amounts up to BDT 200,000 (2 lakh, in words on the page), so check notification before using the fallback | Section 63(1): https://bdlaws.minlaw.gov.bd/act-1106/section-42359.html |
| Tax period | Calendar month; current return rule effective 1 October 2026 is for each tax period | Sections 2(30), 64: https://bdlaws.minlaw.gov.bd/act-print-1106/section-print-42295.html; https://bdlaws.minlaw.gov.bd/act-1106/section-42360.html |
| Ordinary filing | Within 15 days after period end; next working day if the last day is a government holiday | Section 64(1): https://bdlaws.minlaw.gov.bd/act-1106/section-42360.html |
| Government/semi-government/autonomous bodies, banks, insurers and nil filers | May file within 20 days after period end; Board extensions must be evidenced | Section 64(1)-(2): https://bdlaws.minlaw.gov.bd/act-1106/section-42360.html |
| Input-credit time limit, subject to all conditions | Acquisition/invoice or goods-declaration period or next 6 tax periods | Section 46(1)(c): https://bdlaws.minlaw.gov.bd/act-1106/section-42342.html |
| Taxable supply payment over BDT 100,000 (1 lakh, in words on the page) | Banking/mobile-banking payment condition; same-owner registered supply exception in statute | Section 46(1)(a): https://bdlaws.minlaw.gov.bd/act-1106/section-42342.html |

The old BDT 30-50 lakh at 3% and 50 lakh-3 crore at 4% map is not current. No reduced/truncated or sector rate is assumed from a brand name. Read the specific schedule/SRO before using one.

### Establish registration and classification

1. Test actual and expected turnover and the statutory excluded amounts: exempt supplies, capital asset sales, business/part-business transfers and permanent-closure supplies. Section 4 also requires registration regardless of turnover for listed SD activity, tender/contract/work-order supply, import/export business, foreign offices, VAT agents and Board-specified cases. It also contains BIN/enlistment proof requirements for specified business services. Check the full provision, not only a numerical threshold (https://bdlaws.minlaw.gov.bd/act-print-1106/section-print-42297.html).
2. Apply for registration through https://vat.gov.bd within 15 days of the registration obligation: resident VAT-2.1 or nonresident VAT-2.2 under current Rule 4. The valid eVAT application leads to immediate online VAT-2.3 certificate after electronic verification, effective on issue, with the Rule's subsequent verification/dispute procedure. Keep the application, certificate and effective date. Enlistment is distinct: section 10 requires application within 30 days of threshold crossing (VAT-2.1/2.3 under Rule 5). Voluntary registration under section 8 brings the same VAT duties; cancellation cannot be sought until at least 1 year after voluntary registration, and the other cancellation conditions still apply. Sources: SRO 125 replacement Rules 4-5, https://nbr.gov.bd/uploads/sros/VAT_SRO-125.pdf; sections 8 and 10, https://bdlaws.minlaw.gov.bd/act-1106/section-42301.html; https://bdlaws.minlaw.gov.bd/act-1106/section-42303.html. A missing BIN does not remove a registration duty.
3. A full-period bank statement is the minimum ingestion input. With no statement, stop this bank-led workflow. A statement-only draft may proceed as a clearly provisional working paper; no input credit is signed off without compliant evidence. Obtain VAT-6.1 purchase and VAT-6.2 sale registers, or VAT-6.2.1 for goods resold without processing, invoices, BIN, customs declarations and prior return/credit before finalization. Current Rule 40 requires the specified ERP records, including VAT-6.3 after SRO 125; [invoicing](bd-einvoice.md) owns the full invoice, copy/serial and ERP instructions. The old recommendation to use Mushak-11 is replaced by current prescribed invoice evidence; see [invoicing](bd-einvoice.md).
4. Identify the actual supply, consideration, supplier/recipient legal entity, place and time. Standard VAT is not a conservative substitute for missing facts. Use section 33 for the earlier relevant delivery/supply, invoice or payment event and the periodic-supply exceptions; the old section 14 citation was wrong (https://bdlaws.minlaw.gov.bd/act-1106/section-42328.html).
5. Exports of goods and exported/qualifying overseas services need the actual section 23/24 conditions and evidence. For section 24(6), recipient is abroad when supplied and the service is not directly tied to Bangladesh land/goods or excluded roaming; rights/subsequent Bangladesh supply and other exceptions must be checked. A foreign payer alone does not establish zero rating (https://bdlaws.minlaw.gov.bd/act-1106/section-42317.html). EPZ/deemed-export or diplomatic treatment is not automatically the same as a standard export.
6. Exemption depends on the current First Schedule/SRO, not merely a health, education, financial or transport counterparty label. Separate exempt output and its attributable inputs; do not treat all bank fees, insurance, mobile-payment fees, regulatory charges or rent as exempt by name.

### Input credit, imports and adjustments

7. Check section 46 before recovery: economic-activity/taxable use, prescribed register, correct names/address/BIN, payment condition and claim window; additional import/guarantee/input-output-coefficient restrictions apply. Exempt activity, turnover tax, SD and many reduced/specific-rate supplies do not give ordinary credit. A banking/telco/utility bill can be the statutory evidence where section 46(3) says so; the bill must show actual VAT, not an assumed rate (https://bdlaws.minlaw.gov.bd/act-1106/section-42342.html).
8. Passenger vehicles, related repair/maintenance, entertainment and club membership have express restrictions. Vehicle trading/hire/transport and ordinary-course entertainment businesses have specified exceptions; mere documented business promotion does not automatically override the rule. Check the statutory input definition too. Lost/stolen/destroyed goods, free samples, capital goods and mixed-use changes require actual adjustment law, not the old automatic all-or-nothing rule. Apply current section 47 to credit allocation and the required increasing adjustment for the relevant tax period (https://bdlaws.minlaw.gov.bd/act-1106/section-42342.html; https://bdlaws.minlaw.gov.bd/act-1106/section-42343.html).
9. Import VAT on goods uses the statutory customs value plus relevant duties/taxes under section 28, not merely assessable value plus customs duty. Keep the customs goods declaration and evidence of tax paid before credit (https://bdlaws.minlaw.gov.bd/act-1106/section-42322.html). No SD or advance-tax computation is supplied here.
10. From the current section 20, imported services other than First-Schedule-exempt services are taxable at the statutory service-import rate. Recipient bears output liability; banks/financial institutions/authorized foreign-exchange dealers depositing VAT on payment provide the treasury challan as invoice evidence. Input credit requires the service to be a qualifying input and compliance with section 46. Display the imported-service output separately and do not double-pay or double-claim bank-collected VAT. The old section 18(3) citation and automatic zero net effect were wrong (https://bdlaws.minlaw.gov.bd/act-1106/section-42313.html).
11. Use compliant credit/debit notes and matched invoice references for increasing/decreasing adjustments under section 52; preserve both supplier and buyer entries. Do not use section 57 as the credit-note rule (https://bdlaws.minlaw.gov.bd/act-1106/section-42348.html). Carry excess credit through the applicable statutory process; this workflow does not file an automatic refund claim.
12. Turnover-tax filers have no input-VAT/turnover-tax credit under section 63(4). That does not establish a blanket exemption from imported-service VAT. Keep any separate imported-service liability under section 20 and refer where the process is unresolved (https://bdlaws.minlaw.gov.bd/act-1106/section-42359.html; https://bdlaws.minlaw.gov.bd/act-1106/section-42313.html).

### Supplier cues and exception questions

These preserve the old recognition vocabulary as investigation cues. A counterparty substring never overrides the actual invoice, supply and current schedule.

| Cue group | Patterns retained | Investigation and treatment control |
|---|---|---|
| Banks/finance | DUTCH-BANGLA, DUTCH BANGLA, DBBL, BRAC BANK, BRAC BNK, EASTERN BANK, EBL, CITY BANK, ISLAMI BANK, AB BANK, STANDARD CHARTERED BD, HSBC BD, UCBL, PRIME BANK, MUTUAL TRUST, INTEREST, MUNAFA, PROFIT, LOAN, REPAYMENT | Separate principal, interest and fee. Principal is not a sale; check actual fee VAT/exemption and bill, not blanket exclusion. |
| Government/regulators | NBR, NATIONAL BOARD OF REVENUE, VAT DEPARTMENT, MUSHAK, CUSTOMS, SHULKO, BIDA, BOI, RJSC, RAJUK, CDA, KDA, INCOME TAX, TAX DEDUCTED | Separate tax payment, statutory fee and an actual supply. Customs declaration may support import credit; payment text alone does not. |
| Utilities/telco | DESCO, DPDC, BPDB, NESCO, BREB, TITAS GAS, BAKHRABAD GAS, JALALABAD GAS, WASA, DHAKA WASA, CHITTAGONG WASA, GRAMEENPHONE, GP, ROBI, BANGLALINK, TELETALK | Read rate and VAT on the bill, service code, tax date, business use and SD. No universal utility VAT/SD rate is assigned. |
| Insurance/MFS | SADHARAN BIMA, JIBAN BIMA, GREEN DELTA, PRAGATI, PIONEER, METLIFE BD, GUARDIAN LIFE, BKASH, B-KASH, NAGAD, ROCKET, DBBL MOBILE, UPAY, SURE CASH | Separate the underlying sale/purchase, insurance or transaction fee; check the applicable schedule and evidence. |
| Payroll | SALARY, BETON, WAGES, PROVIDENT FUND, PF, GRATUITY | Genuine employee remuneration/fund movements are not ordinary supplier sales; confirm employment and purpose. |
| Overseas software/advertising | GOOGLE, GOOGLE ADS, MICROSOFT, AZURE, OFFICE 365, META, FACEBOOK ADS, AMAZON AWS, AWS, ZOOM, SLACK, DROPBOX, CANVA, FIGMA, NOTION | Read legal billing entity, country, VAT shown and any bank challan; apply imported-service and duplicate-payment checks. |
| Professional/property | CA FIRM, AUDIT, CHARTERED ACCOUNTANT, ADVOCATE, LAWYER, BARRISTER, CONSULTANT, ENGINEERING, RENT, BHARA, OFFICE RENT, HOUSE RENT, RESIDENTIAL | Confirm actual service/use, landlord/supplier status, schedule and invoice. No automatic professional-service credit or blanket residential exemption here. |
| Transfers/owner/cash | OWN TRANSFER, INTERNAL, ACCOUNT TRANSFER, DIVIDEND, CASH WITHDRAWAL, ATM, DIRECTOR FEE, PROPRIETOR DRAWING | Reconcile matched own-account/principal/drawings separately. Director business services need their statutory exception; a transfer label alone is insufficient. |

Retain questions for fuel/CNG (Padma Oil/Jamuna Oil), commercial versus passenger vehicles, entertainment/meals, ambiguous SaaS entity, round-number incoming capital versus sale/loan, transfers to/from individuals, cash withdrawals, mixed-use phone/internet, rent invoice and import-related LC/shipping/freight payments. Keep unresolved credits out of the claim; retain undecided output classifications visibly for reviewer resolution rather than silently treating them as exempt. Request a customs declaration for import taxes and previous-return proof for credit brought forward.

### Working-paper and filing sequence

13. Normalize source bank dates, debit/credit signs, currency and Bangla/transliterated descriptions. CSV delimiter/date/column formats vary; common Date/Description/Debit/Credit/Balance columns are cues, not guaranteed DBBL/BRAC schemas. Match internal transfers across bank/bKash accounts, distinguish proprietor drawings from wages, and classify the underlying MFS payment. Use documented transaction-date currency conversion; no fixed USD/BDT rate is supplied.
14. Keep a Transactions sheet with original line, date, counterparty, document reference, legal classification, net consideration, output VAT, eligible input VAT, import challan, adjustments and unresolved facts. Keep output and input in separate columns so a service-import row cannot disappear from a SUMIFS exact-text match.
15. Build Return Summary by summing those controlled columns and reconciling net liability/credit, SD (where externally computed), adjustments and prior credit. Return Form contains reviewed amounts and actual current form fields. The old synthetic Part 1-12 mapping and `Part 2 + Part 6` string formula are not verified current Mushak boxes and must not be used as filing instructions.
16. Current Rule 47, replaced by SRO 125 item 11 effective 1 July 2026, uses VAT-9.1 for registered manufacturers/service providers, VAT-9.1.1 for registered traders and VAT-9.2 for enlisted turnover-tax persons (https://nbr.gov.bd/uploads/sros/VAT_SRO-125.pdf). Use the actual current form at https://vat.gov.bd, confirm identity, registration, period and applicable output/input/adjustment fields, pay the amount due and retain challan/submission acknowledgement. The published 9.1.1 has taxpayer, submission, output, noncreditable local purchases, increasing/decreasing adjustment, net-tax, treasury-payment, closing and declaration parts; this is not a certified live portal field map.

    **Dated form/statute inconsistency:** the July replacement 9.2 form prints a January-December annual period, but current section 2(30) defines a calendar-month tax period and the later October replacement section 64 requires each period's return with the 15-/20-day conditioned deadlines above. Retain that later statutory monthly rule. Do not infer an annual deadline from the printed form; resolve the current 9.2 portal/instruction implementation before submitting an enlisted person's return. Earlier periods and Board extensions need their applicable instrument.
17. Escalate an unknown entity type, certificate/BIN, filing period, industry/exempt activity, export evidence or credit balance. The base workflow's materiality flags may prioritize review but do not turn unsourced old fixed red-flag amounts into statutory thresholds.

## Worked cases

### Domestic sale

ABC TECHNOLOGIES LTD pays gross BDT 115,000 for a documented standard-rated taxable supply. Net 100,000 and VAT 15,000 are derived using the statutory tax fraction; issue the current prescribed invoice. Do not apply the rate solely because the customer pays BDT.

```oa-check
name: Standard taxable domestic gross amount
inputs:
  gross: 115000
  rate: 0.15
steps:
  - net: gross / (1 + rate)
  - vat: gross - net
expected:
  net: 100000
  vat: 15000
```

### Purchase: evidence and input definition first

COMPUTER SOURCE BD invoice gross 23,000 contains 3,000 VAT and 20,000 net. Recovery is 3,000 only if this is a qualifying input used for taxable supply and all statutory conditions are established. The old office-supplies label alone did not prove credit.

```oa-check
name: Qualified purchase invoice arithmetic
inputs:
  gross: 23000
  rate: 0.15
steps:
  - net: gross / (1 + rate)
  - vat: gross - net
expected:
  net: 20000
  vat: 3000
```

### Service export

STUDIO KREBS GMBH pays 350,000 for a service proved to meet section 24's export conditions. VAT is 0 and consideration 350,000. The old assumed bank-realization deadline is not supplied as a condition here; obtain the applicable remittance rules separately.

```oa-check
name: Documented qualifying service export
inputs:
  consideration: 350000
  rate: 0
steps:
  - vat: consideration * rate
  - total: consideration + vat
expected:
  vat: 0
  total: 350000
```

### Imported service: credit is conditional

GOOGLE IRELAND LIMITED service value 2,800, with imported-service VAT 420 established under section 20 and matching bank challan. For a fully qualifying input, credit 420 offsets output 420; if wholly noncreditable, VAT cost is 420. Avoid duplicating VAT already deposited through the bank.

```oa-check
name: Imported service credit decision after bank challan
inputs:
  service_value: 2800
  rate: 0.15
steps:
  - output: service_value * rate
  - eligible_credit: output
  - fully_eligible_net: output - eligible_credit
  - noncreditable_net: output
expected:
  output: 420
  eligible_credit: 420
  fully_eligible_net: 0
  noncreditable_net: 420
```

### Passenger vehicle and bank-charge evidence

TOYOTA BANGLADESH passenger-car lease of 85,000 for a consultant, not a qualifying vehicle business: no input credit is signed off under section 46. DUTCH-BANGLA BANK fee 500: obtain the actual fee invoice and applicable schedule rather than assume exemption. Those cash amounts remain in the working paper; no invented embedded VAT is extracted.

```oa-check
name: Cash outlays with no evidenced credit signed off
inputs:
  car_cash: 85000
  bank_fee_cash: 500
  signed_off_credit: 0
steps:
  - cash_total: car_cash + bank_fee_cash
  - cash_after_signed_off_credit: cash_total - signed_off_credit
expected:
  cash_total: 85500
  cash_after_signed_off_credit: 85500
```

## When to refuse or refer

R-BD-1: do not claim input VAT for a turnover-tax filer. R-BD-2: refer EPZ/SEZ/bond/deemed-export regimes. R-BD-3: refer multi-establishment separate-BIN consolidation and VAT-6.5 branch/warehouse transfer documents; VAT-6.4 concerns contractual manufacturing, not those transfers. R-BD-4: refer product-specific supplementary duty. R-BD-5: refer designated VDS agent obligations, VAT-6.6 certificates and deposits; VAT-6.10 is purchase/sale information, not the withholding certificate. Also refer refunds, uncertain reduced/exempt rates, complex apportionment and unknown output classifications. With no complete bank statement stop this bank-led workflow; without invoices keep only a clearly provisional draft.

## Sources

| Source and sections actually read | Official URL | Read on |
|---|---|---|
| Read for definitions: economic activity/director exception, input scope, tax fraction/period, thresholds and excluded turnover | https://bdlaws.minlaw.gov.bd/act-print-1106/section-print-42295.html | 2026-11-14 |
| Read for section 4 complete registration and BIN-proof triggers | https://bdlaws.minlaw.gov.bd/act-print-1106/section-print-42297.html | 2026-11-14 |
| Read for section 8 voluntary registration, same duties and minimum year before cancellation application | https://bdlaws.minlaw.gov.bd/act-1106/section-42301.html | 2026-11-14 |
| Read for section 10 current enlistment/eVAT certificate | https://bdlaws.minlaw.gov.bd/act-1106/section-42303.html | 2026-11-14 |
| Read for section 15 standard rate and alternatives | https://bdlaws.minlaw.gov.bd/act-1106/section-42308.html | 2026-11-14 |
| Read for section 20 current imported-service charge, bank collection and conditional credit | https://bdlaws.minlaw.gov.bd/act-1106/section-42313.html | 2026-11-14 |
| Read for section 24 zero-rated service conditions and neighboring exceptions | https://bdlaws.minlaw.gov.bd/act-1106/section-42317.html | 2026-11-14 |
| Read for section 28 import valuation | https://bdlaws.minlaw.gov.bd/act-1106/section-42322.html | 2026-11-14 |
| Read for section 33 time of supply and periodic/other exceptions | https://bdlaws.minlaw.gov.bd/act-1106/section-42328.html | 2026-11-14 |
| Read for section 46 complete credit restrictions, evidence and time limit | https://bdlaws.minlaw.gov.bd/act-1106/section-42342.html | 2026-11-14 |
| Read for section 47 partial-credit rule | https://bdlaws.minlaw.gov.bd/act-1106/section-42343.html | 2026-11-14 |
| Read for section 52 credit/debit-note conditions | https://bdlaws.minlaw.gov.bd/act-1106/section-42348.html | 2026-11-14 |
| Read for section 63 turnover-tax fallback, fixed-amount power and no-credit rule | https://bdlaws.minlaw.gov.bd/act-1106/section-42359.html | 2026-11-14 |
| Read for section 64 current deadlines and exceptions, effective October 2026 | https://bdlaws.minlaw.gov.bd/act-1106/section-42360.html | 2026-11-14 |
| Read for VAT Rules 40-42 registers/ERP, invoice/adjustment/transfer/VDS document jobs; old Rule 47 superseded by SRO 125 | https://nbr.gov.bd/uploads/rules/Authentic_English_Text_VAT_Rules_2016.pdf | 2026-11-14 |

| Read for SRO 125 replacement Rules 4-5, items 10-11 invoice/ERP and return populations, replacement forms 9.1.1/9.2 and 1 July commencement | https://nbr.gov.bd/uploads/sros/VAT_SRO-125.pdf | 2026-11-14 |

Not yet confirmed: Current activity-specific fixed turnover-tax notifications, reduced/truncated rates (old 5%, 7.5%, 10% labels are not assigned to a supply), First-Schedule/sector exemptions, telecom SD, live Mushak-9.1/9.1.1/9.2 fields and the printed 9.2 annual-period/current monthly-statute inconsistency, EFD notifications, bank-realization deadlines, historical filing periods, VAT penalties/interest, exact mixed-use/annual-adjustment method and currency conversion requirements. The old fixed red-flag values were workflow choices, not sourced legal thresholds; use explicit reviewer policy. No automatic bank/insurance/MFS exemption or input credit is certified.
