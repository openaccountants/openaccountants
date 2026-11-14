---
name: us-1099-nec-issuance
description: Decide which 2026 payments by a US sole proprietor or single-member LLC to contractors need a Form 1099-NEC, and produce the forms on time. Covers the USD 2,000 threshold for payments made after 31 December 2025 (raised from USD 600 by Public Law 119-21 section 70433 and indexed from 2027), the corporate exception and its carve-outs for attorneys and medical payments, Form W-9 collection, 24% backup withholding, the 31 January due date (1 February 2027 for 2026 forms), the 10-return e-file rule and IRIS replacing FIRE, the section 6721 and 6722 penalties for returns due in 2027, B-notices and state filing. Trigger on "1099-NEC", "do I need to send a 1099", "contractor 1099", "W-9", "backup withholding", "1099 penalty", "1099 threshold 2026". Payments by card or payment app go on Form 1099-K instead (us-1099-k-and-payment-processors). Federal only.
version: "1.0"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: situation-rules
---

# US Form 1099-NEC issuance, payments made in 2026

> **Source-cited draft.** Built from Rev. Proc. 2025-32, Public Law 119-21 sections 70432 and 70433, the Instructions for Forms 1099-MISC and 1099-NEC (Rev. December 2026), Pub. 1099 (2026), Pub. 1281 and 26 U.S.C. 3406, 6041A, 6045, 6050W, 6071, 6011, 6721, 6722, 6724 and 7503, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** For payments made in 2026, a business files Form 1099-NEC for each non-corporate contractor it paid **USD 2,000** or more for services during the year (it was USD 600 for 2025 payments). Attorneys get one whatever their entity type. Payments by credit card, debit card or a payment app such as PayPal Goods and Services are reported by the processor on Form 1099-K, not on 1099-NEC. The 2026 forms are due to the IRS and the contractor by **Monday 1 February 2027** (31 January 2027 is a Sunday), with no automatic extension. A business filing 10 or more information returns of all kinds must e-file, and from the 2027 filing season the IRS accepts e-filed information returns only through IRIS (FIRE is retired). If a contractor gives no taxpayer identification number, the payer must withhold 24%.

## Scope and who this is for

In scope: a US sole proprietor filing Schedule C, or a single-member LLC treated as disregarded, that pays non-employees for services in the course of its trade or business in calendar 2026. The skill decides, for each payee, whether a 1099-NEC is required; captures the data for boxes 1a, 2 and 4; flags missing W-9s and the backup withholding duty; works out penalties for late or missing forms; tests the e-file requirement; and flags state filing. It produces working papers for a credentialed reviewer (EA, CPA or attorney). It does not file the forms; that is done in IRIS, through an IRS-approved provider, or on paper.

The expense is deductible on Schedule C whether or not the 1099-NEC is issued; failing to issue it brings penalties and audit risk, not loss of the deduction.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Payments by card, payment app or marketplace, and reconciling a Form 1099-K received | `us-1099-k-and-payment-processors` |
| Classifying the business's transactions into Schedule C lines | `us-sole-prop-bookkeeping` |
| The Schedule C deduction and self-employment tax of the person who receives the 1099-NEC | `us-schedule-c-and-se-computation` |
| Employees (Form W-2, payroll withholding, Forms 941 and 940) | `us-form-941-940-payroll` |
| Nonresident alien payees (Form 1042-S, W-8BEN, 30% withholding) | refer |
| Form 1099-MISC boxes other than the overlaps named below, 1099-INT, 1099-DIV | refer |
| Worker classification (employee or contractor) | flagged for the reviewer, not decided here |
| State information returns beyond the Combined Federal/State Filing Program | the state's skill |

## Ask the client first

1. **A list of every person or business paid for services in 2026**, with the total paid to each, and how each payment was made (check, ACH, wire, cash, Zelle, Venmo or PayPal personal, card, PayPal Goods and Services, Stripe, Square). Card and payment app payments drop out of the 1099-NEC count.
2. **A Form W-9 for each payee**, dated, with line 3 (tax classification) and the TIN. If any is missing, ask whether any payment was withheld on.
3. **Whether any payee is an attorney or law firm**, and whether any payment was a settlement paid to an attorney for a claimant (that is 1099-MISC box 10, not 1099-NEC).
4. **Medical or health care payments** (occupational health, drug testing): these go on 1099-MISC box 6.
5. **Direct sales:** did the business sell USD 5,000 or more of consumer products to anyone for resale outside a permanent retail establishment? That is 1099-NEC box 2 (or 1099-MISC box 7).
6. **Total information returns** the business will file for 2026 (1099-NEC, 1099-MISC, W-2 and others): 10 or more means e-file.
7. **Any CP2100 or CP2100A notice** received in 2026 (B-notice duty), and whether a second one arrived within 3 years.
8. **Foreign payees**, payees who died during the year, staffing agencies, joint ventures, and payments in virtual currency.
9. **The states** where the business and each payee are, for state filing.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount | Source |
| --- | --- | --- |
| Reporting threshold for payments made after 31 December 2025 (section 6041(a), applied to services by 6041A(a)(2)) | USD 2,000 | [Rev. Proc. 2025-32, section 2.15](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Threshold for payments made in 2025 (forms filed in early 2026) | USD 600 | [Public Law 119-21, section 70433(a)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Inflation indexing of the USD 2,000, rounded to the nearest USD 100 | Calendar years after 2026 | [Public Law 119-21, section 70433(b)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Direct sales of consumer products for resale (box 2) | USD 5,000 | [Instructions for Forms 1099-MISC and 1099-NEC (12-2026), box 2](https://www.irs.gov/pub/irs-pdf/i1099mec.pdf) |
| Gross proceeds paid to an attorney (1099-MISC box 10) | USD 600 | [Instructions for Forms 1099-MISC and 1099-NEC (12-2026)](https://www.irs.gov/pub/irs-pdf/i1099mec.pdf) |
| Medical and health care payments (1099-MISC box 6) | USD 2,000 | [Instructions for Forms 1099-MISC and 1099-NEC (12-2026), box 6](https://www.irs.gov/pub/irs-pdf/i1099mec.pdf) |
| Cash payments for fish bought for resale (1099-MISC box 11) | USD 600 | [Instructions for Forms 1099-MISC and 1099-NEC (12-2026), box 11](https://www.irs.gov/pub/irs-pdf/i1099mec.pdf) |
| Royalties (1099-MISC box 2) | USD 10 | [Instructions for Forms 1099-MISC and 1099-NEC (12-2026)](https://www.irs.gov/pub/irs-pdf/i1099mec.pdf) |
| Backup withholding rate | 24% | [26 U.S.C. 3406(a)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleC-chap24-sec3406.htm) |
| Due date to the IRS and to the payee | 31 January (no automatic extension) | [26 U.S.C. 6071(c)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partV-sec6071.htm) |
| Due date shift when the day is a weekend or holiday | Next business day | [26 U.S.C. 7503](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap77-sec7503.htm) |
| E-file required at this many information returns (all types aggregated) | 10 | [Pub. 1099 (2026), Reminders](https://www.irs.gov/pub/irs-pdf/p1099.pdf) |
| Penalty per return, corrected within 30 days of the due date (returns due 2027) | USD 60 | [Rev. Proc. 2025-32, section 4.57](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Penalty per return, corrected after 30 days but by 1 August | USD 130 | [Rev. Proc. 2025-32, section 4.57](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Penalty per return, general rule (after 1 August or never filed) | USD 340 | [Rev. Proc. 2025-32, section 4.57](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Calendar-year maximum, gross receipts USD 5,000,000 or less: 30-day tier / 1 August tier / general | USD 244,500 / USD 698,500 / USD 1,397,000 | [Rev. Proc. 2025-32, section 4.57(2)](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Calendar-year maximum, gross receipts over USD 5,000,000: 30-day tier / 1 August tier / general | USD 698,500 / USD 2,095,500 / USD 4,191,500 | [Rev. Proc. 2025-32, section 4.57(1)](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Intentional disregard, per return | Greater of USD 690 or 10% of the amounts required to be reported, no maximum | [Rev. Proc. 2025-32, section 4.57(3)](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Payee statement penalties (section 6722), statements due 2027 | Same amounts and maximums as section 6721 | [Rev. Proc. 2025-32, section 4.58](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Records: keep copies at least | 3 years (4 years if backup withholding was imposed) | [Pub. 1099 (2026), Keeping copies](https://www.irs.gov/pub/irs-pdf/p1099.pdf) |
| First B-notice: send to the payee within | 15 business days of the CP2100 or CP2100A | [Pub. 1281](https://www.irs.gov/pub/irs-pdf/p1281.pdf) |
| Start backup withholding if no response by | 30 business days after the CP2100 or CP2100A | [Pub. 1281](https://www.irs.gov/pub/irs-pdf/p1281.pdf) |

The USD 2,000 threshold also sets when backup withholding applies to payments reportable under section 6041 (section 3406(b)(6), as amended by section 70433(d)). The attorney gross proceeds and fish amounts stayed at USD 600 because they sit in other sections (6045(f) and 6050R) that Public Law 119-21 did not change.

### Step 1: list the payees and drop what is not a 1099-NEC payment

For each payee, total the 2026 payments for services in the course of the trade or business. Then remove:

- **Card and payment app payments.** Payments made with a credit, debit or gift card, and payments through a third party settlement organization (PayPal Goods and Services, Stripe, Square, and similar), "must be reported on Form 1099-K by the payment settlement entity under section 6050W and are not subject to reporting on Form 1099-MISC or Form 1099-NEC". Source: [Instructions for Forms 1099-MISC and 1099-NEC (12-2026)](https://www.irs.gov/pub/irs-pdf/i1099mec.pdf). Peer-to-peer transfers that are not a third party network transaction for the payee (Zelle, Venmo or Cash App personal, a bank transfer) stay with the payer.
- **Goods and merchandise.** Not services; not on 1099-NEC (rent and royalties are 1099-MISC).
- **Employees.** They get a Form W-2.
- **Personal payments.** Only trade or business payments are reportable.

### Step 2: apply the USD 2,000 test per payee

The threshold applies per payee per calendar year to the total paid, not per invoice. If the total reaches USD 2,000, the whole amount goes in box 1a, not just the excess. The test is "equals or exceeds" (section 6041A(a)(2) as amended): USD 2,000.00 is reportable, USD 1,999.99 is not. Source: [Public Law 119-21, section 70433(c)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).

Services include professional fees (accounting, legal, consulting, design, programming), contract labor and subcontractors, commissions to non-employees, fees to independent directors, prizes and awards for services to non-employees, and payments for parts and labor where the labor cannot be separated (report the full amount).

### Step 3: apply the corporate exception, then its carve-outs

- **Corporations are generally exempt.** Payments to a C corporation, an S corporation, or an LLC that elected to be taxed as one (Form W-9 line 3) need no 1099-NEC. Source: Treas. Reg. 1.6041-3(p), referred to in the [Instructions for Forms 1099-MISC and 1099-NEC](https://www.irs.gov/pub/irs-pdf/i1099mec.pdf).
- **Attorneys: always report.** Attorneys' fees for legal services of USD 2,000 or more go in 1099-NEC box 1a whatever the entity type (sole practitioner, partnership, professional corporation, S corporation, LLC). "The term 'attorney' includes a law firm or other provider of legal services." Gross proceeds paid to an attorney, for example a settlement paid for a claimant, go in 1099-MISC box 10 once they reach USD 600. Source: [26 U.S.C. 6045(f)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartB-sec6045.htm); [Instructions for Forms 1099-MISC and 1099-NEC](https://www.irs.gov/pub/irs-pdf/i1099mec.pdf).
- **Medical and health care payments:** 1099-MISC box 6 at USD 2,000 or more, including to a corporation. Not the owner's own health insurance (that is a deduction under section 162(l), not a 1099 matter).
- **Fish bought for resale:** cash payments of USD 600 or more, 1099-MISC box 11, regardless of corporate status. Rare for clients in scope.
- **Substitute payments in lieu of dividends or tax-exempt interest:** reportable regardless of corporate status (1099-MISC box 8). Rare for clients in scope.

### Step 4: W-9 and backup withholding

Before the first payment, collect Form W-9: legal name, business name, federal tax classification, exemption codes, TIN (SSN or EIN), and certification that the TIN is correct and the payee is not subject to backup withholding.

If the payee gives no TIN, or the IRS says the TIN is wrong, or the payee does not certify, the payer must withhold 24% from reportable payments. Source: [26 U.S.C. 3406(a)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleC-chap24-sec3406.htm). Mechanics: withhold 24% of each payment; deposit it as nonpayroll withholding; report it in 1099-NEC box 4; file Form 945 for the year by 31 January (1 February 2027 for 2026). Many small businesses never withheld: the skill records the gap for the reviewer rather than assuming it was done.

TIN matching: the IRS e-Services TIN Matching program checks a name and TIN pair before filing. Optional, recommended for unfamiliar payees.

B-notices: if the IRS sends a CP2100 or CP2100A listing a name and TIN mismatch, send the first B-notice with a new Form W-9 within 15 business days, and begin backup withholding if the payee has not responded within 30 business days. On a second notice for the same payee within 3 years, send the second B-notice; the payee must get validation from the IRS (Form 147C for an EIN) or the SSA, and a new W-9 alone is not enough. Source: [Pub. 1281](https://www.irs.gov/pub/irs-pdf/p1281.pdf).

### Step 5: complete the form

| Box | What goes in it |
| --- | --- |
| 1a | Nonemployee compensation of USD 2,000 or more, including attorneys' fees for services |
| 1b, 1c, 1d (new for 2026) | Cash tips included in box 1a, the Treasury Tipped Occupation Code, and qualified overtime, under Public Law 119-21 sections 70201 and 70202; rare for contractors in scope |
| 2 | Checkbox for direct sales of USD 5,000 or more of consumer products for resale |
| 3 | Excess golden parachute payments (moved here from 1099-MISC) |
| 4 | Federal income tax withheld (backup withholding) |
| 5 to 7 | State tax withheld, state number, state income |

Source: [Instructions for Forms 1099-MISC and 1099-NEC (12-2026)](https://www.irs.gov/pub/irs-pdf/i1099mec.pdf).

### Step 6: file and furnish

| Copy | Who gets it | When |
| --- | --- | --- |
| Copy A | IRS | 1 February 2027 for 2026 payments |
| Copy 1 | State tax department, if required | Varies by state |
| Copy B | Payee | 1 February 2027 |
| Copy 2 | Payee, for the state return | With Copy B |
| Copy C | Payer's records | Keep at least 3 years (4 if backup withholding was imposed) |

- **E-file or paper.** E-filing is required if the business files 10 or more information returns in the year, counted across all types (1099-NEC, 1099-MISC, W-2 and others). A business with 5 1099-NECs and 6 W-2s has 11 and must e-file everything. Source: [Pub. 1099 (2026)](https://www.irs.gov/pub/irs-pdf/p1099.pdf).
- **IRIS, not FIRE.** "Beginning tax year 2026/filing season 2027, the Information Returns Intake System (IRIS) will be the only intake system for information returns." FIRE is shut down at the end of 2026, including for corrections and prior years. A Transmitter Control Code application can take about 45 business days, so apply well before January. Source: [Pub. 1099 (2026), What's New](https://www.irs.gov/pub/irs-pdf/p1099.pdf).
- **Paper.** Under 10 returns, paper Copy A with Form 1096 as the transmittal, one Form 1096 per form type.
- **No automatic extension** for 1099-NEC. A 30-day extension is available only on request for extraordinary circumstances.

### Step 7: corrections

If a filed 1099-NEC is wrong, file a corrected return with the IRS and furnish it to the payee. Error Type 1 (wrong amount, code or checkbox): one corrected return. Error Type 2 (wrong payee name or TIN, or the wrong form): a return that zeroes out the incorrect one plus a new correct return. Do not check the VOID box on a paper correction. In IRIS, corrections follow Pub. 5718 or Pub. 5717. Source: [Instructions for Forms 1099-MISC and 1099-NEC (12-2026)](https://www.irs.gov/pub/irs-pdf/i1099mec.pdf); [Pub. 1099 (2026)](https://www.irs.gov/pub/irs-pdf/p1099.pdf).

### Step 8: state filing

The Combined Federal/State Filing Program forwards e-filed 1099 data to participating states. Many states with an income tax take part, but some require their own filing even so, and some have lower thresholds. States with no individual income tax on wages (Alaska, Florida, Nevada, New Hampshire, South Dakota, Tennessee, Texas, Washington, Wyoming) generally need no state copy. Flag every payee state for the reviewer; this skill does not track 50 state thresholds. Source: [Pub. 1099 (2026)](https://www.irs.gov/pub/irs-pdf/p1099.pdf).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Paid through PayPal Goods and Services, Stripe, Square or by card | No 1099-NEC from the payer; the processor reports on Form 1099-K. See `us-1099-k-and-payment-processors` |
| Paid through Zelle, Venmo or Cash App personal, or bank transfer | The payer keeps the 1099-NEC duty |
| Payment method unclear | Treat as reportable by the payer and flag |
| Single-member LLC payee, disregarded | Report in the owner's name and TIN as shown on the W-9 |
| LLC payee that elected S or C corporation status | Corporate exception, unless attorney or medical |
| Nonresident alien performing services in the US | Form 1042-S, W-8BEN, 30% withholding under section 1441 or the treaty rate. Refer |
| Payee died during the year | Payments before death in the decedent's name and TIN; payments after death to the estate under its EIN. Flag |
| Married couple's qualified joint venture (section 761(f)) | Report to each spouse for their share. Flag |
| Expense reimbursements paid to a contractor | Include in box 1a (accountable plans are for employees). Flag if large |
| Staffing agency supplies workers | The agency is the payee; corporate exception may apply. Collect its W-9 |
| Payments in virtual currency | Fair market value on the payment date counts toward USD 2,000 and is the amount reported. Flag for valuation |
| Legal settlement paid to an attorney's trust account | Gross amount on 1099-MISC box 10 (USD 600 or more), not 1099-NEC, unless purely for the payer's own legal services |
| A 2025 payment, form filed in early 2026 | Old USD 600 threshold and the 2026 penalty table apply; a late 2025 form filed now is outside the 2026 figures above |
| Payee is an employee, or may be | Do not issue a 1099-NEC to an employee. Worker classification is referred |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Payee entity type (no W-9) | Treat as non-corporate and issue the 1099-NEC; avoids the section 6721 penalty |
| Split between goods and services | Report the full amount on 1099-NEC |
| Payment method | Treat as paid by the payer (not by card or app) |
| TIN given but no signed W-9 | File with the TIN given; flag the missing W-9 |
| Payee total just under USD 2,000 | No form; keep the per-payee total in the file |
| Law firm is an S corporation | Issue the 1099-NEC: the attorney rule overrides the corporate exception |
| Number of other information returns | Ask; if unknown, plan to e-file in IRIS |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| Any payee with no W-9 | Backup withholding was due at 24%; Form 945 and penalty exposure |
| A contractor paid regularly, full time, under the client's control | Possible employee; refer for classification |
| No IRIS Transmitter Control Code yet and 10 or more returns | FIRE is gone; the TCC can take about 45 business days |
| Payments to an attorney not on the list | Attorneys are always reportable |
| A CP2100 or CP2100A notice received | B-notice clock of 15 and 30 business days |
| The client wants to pay contractors by card to avoid 1099s | Not a compliance strategy; the skill will not advise it |

## Worked cases

**Case 1, the threshold sort.** A designer's sole proprietorship paid four non-corporate contractors in 2026 by check or ACH, each with a W-9 on file: a copywriter USD 1,950, a developer USD 2,000, a photographer USD 8,500 and a dog walker USD 640 (eight payments of USD 80, for the business's office dog). Under the 2025 USD 600 rule all four would get a form. For 2026 only the developer (USD 2,000 reaches the threshold exactly) and the photographer need one: 2 forms, box 1a USD 2,000.00 and USD 8,500.00, due 1 February 2027.

```oa-check
name: 1099-NEC threshold sort, payments made in 2026
inputs:
  copywriter: 1950
  developer: 2000
  photographer: 8500
  dog_walker: 640
  threshold: 2000
steps:
  - copywriter_form: floor(min(copywriter, threshold) / threshold)
  - developer_form: floor(min(developer, threshold) / threshold)
  - photographer_form: floor(min(photographer, threshold) / threshold)
  - dog_walker_form: floor(min(dog_walker, threshold) / threshold)
  - forms_required: copywriter_form + developer_form + photographer_form + dog_walker_form
expected:
  copywriter_form: 0
  developer_form: 1
  photographer_form: 1
  dog_walker_form: 0
  forms_required: 2
```

**Case 2, a decision: six forms missed, file now or later?** A small business (gross receipts well under USD 5,000,000) finds on 20 February 2027 that it never filed or furnished six 2026 1099-NECs. Each late form carries both a section 6721 penalty (IRS copy) and a section 6722 penalty (payee copy). Filed and furnished by 3 March 2027 (within 30 days of 1 February) the exposure is 6 x USD 60 x 2 = USD 720. After that but by 1 August, 6 x USD 130 x 2 = USD 1,560. Later or never, 6 x USD 340 x 2 = USD 4,080. Recommend filing within the 30 days, and ask for a reasonable-cause waiver under section 6724 only if the facts support it. Also: if any of the six had no W-9, 24% backup withholding was due (on a USD 3,600 payee, USD 864) and Form 945 is owed.

```oa-check
name: Late 1099-NEC penalties for 2026 forms, small business
inputs:
  forms: 6
  tier_30_days: 60
  tier_aug_1: 130
  tier_general: 340
  unwithheld_payee: 3600
steps:
  - within_30_days: forms * tier_30_days * 2
  - by_aug_1: forms * tier_aug_1 * 2
  - after_aug_1: forms * tier_general * 2
  - saving_filing_now: after_aug_1 - within_30_days
  - backup_withholding_due: unwithheld_payee * 0.24
expected:
  within_30_days: 720
  by_aug_1: 1560
  after_aug_1: 4080
  saving_filing_now: 3360
  backup_withholding_due: 864.00
```

More test facts kept from the earlier version, updated for 2026:

| Facts | Result |
| --- | --- |
| Freelance graphic designer, individual, W-9 on file, paid USD 8,500 | 1099-NEC: box 1a USD 8,500.00, box 4 zero, due 1 February 2027 |
| IT firm, W-9 shows S corporation, paid USD 12,000 | No 1099-NEC (corporate exception); keep the W-9 |
| "Smith and Jones, P.C." (C corporation), contract review, USD 4,200 | 1099-NEC box 1a USD 4,200.00: attorney rule overrides the corporate exception |
| Handyman, no W-9, USD 3,600, nothing withheld | 1099-NEC box 1a USD 3,600.00, box 4 zero; flag USD 864 that should have been withheld and Form 945 |
| Virtual assistant paid USD 2,400 through PayPal Goods and Services | No 1099-NEC from the payer; PayPal's 1099-K duty depends on the payee's totals (see the 1099-K skill) |
| Attorney's law firm paid USD 1,500 for services | No 1099-NEC: under USD 2,000 (it would have been required for 2025 payments) |

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-NEC-FILE | Asked to transmit the forms to the IRS | Refuse: the skill prepares the data; the filer files in IRIS or on paper |
| R-NEC-CLASS | Is this worker an employee or a contractor? | Refer: common law test, Form SS-8, state ABC tests |
| R-NEC-AVOID | Pay by card to avoid issuing 1099s | Refuse to advise restructuring to avoid reporting |
| R-NEC-VERBAL | Payee says by phone or email that it is a corporation | Refuse to rely on it: get a W-9 |
| R-NEC-DOUBLE | Report the same card or app payment on both 1099-NEC and 1099-K | Refuse: the processor reports it on 1099-K only |
| R-NEC-BWH | Skip backup withholding because it is impractical | Refuse: the duty exists; record the gap |
| R-NEC-EMP | Issue a 1099-NEC to an employee | Refuse: employees get a W-2; misclassification brings section 3509 and FICA liability |
| R-NEC-FOREIGN | Nonresident alien payee | Refer: Form 1042-S regime |
| R-NEC-STATE | State thresholds and separate state filing | Flag for the reviewer, never ignore |

## Filing and payment

- **Forms 1099-NEC for 2026 payments:** file Copy A with the IRS and furnish Copy B by Monday 1 February 2027 (26 U.S.C. 6071(c) and 7503). E-file in IRIS at 10 or more returns.
- **Form 945** for any backup withholding in 2026: due 1 February 2027; deposits during the year under the deposit rules.
- **Penalty notices** (CP215 and letters proposing section 6721 and 6722 penalties): answer by the date shown; reasonable cause under 26 U.S.C. 6724.
- **Corrections:** as soon as an error is found; a correction within 30 days of the due date falls in the USD 60 tier.

## Completion checklist

- Every 2026 service payee listed with total paid and payment method.
- Card and payment app payments removed and noted as 1099-K.
- USD 2,000 test applied per payee for the calendar year.
- Corporate exception applied only from a W-9, with attorneys and medical payments carved out.
- Missing W-9s flagged, with the 24% backup withholding amount and Form 945.
- Information return count done; IRIS TCC in place if 10 or more.
- Forms filed and furnished by 1 February 2027; copies kept 3 years (4 with backup withholding).
- State filing flagged for each payee state.
- Any B-notice handled within 15 and 30 business days.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Rev. Proc. 2025-32. Read for section 2.15 (USD 2,000 base threshold for payments after 31 December 2025) and sections 4.57 and 4.58 (section 6721 and 6722 penalties for returns and statements due in 2027). | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-13 |
| Public Law 119-21 (govinfo). Read for section 70433 (USD 600 to USD 2,000, indexing after 2026, 6041A(a)(2) and 3406(b)(6) cross-references, payments after 31 December 2025) and section 70432 (Form 1099-K de minimis rule). | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-13 |
| Instructions for Forms 1099-MISC and 1099-NEC (Rev. December 2026). Read for What's New (USD 2,000, inflation from 2027, new boxes 1b to 1d, box 3 golden parachutes), Form 1099-K payments, attorneys, boxes 2, 6, 10 and 11, the 31 January date and corrections. | https://www.irs.gov/pub/irs-pdf/i1099mec.pdf | 2026-11-13 |
| Pub. 1099 (2026), General Instructions for Certain Information Returns. Read for IRIS replacing FIRE from filing season 2027, the 10-return e-file rule, keeping copies, and the Combined Federal/State Filing Program. | https://www.irs.gov/pub/irs-pdf/p1099.pdf | 2026-11-13 |
| Pub. 1281, Backup Withholding for Missing and Incorrect Name/TIN(s). Read for the 15 and 30 business day B-notice rules and the second B-notice. | https://www.irs.gov/pub/irs-pdf/p1281.pdf | 2026-11-13 |
| 26 U.S.C. 3406 (govinfo). Read for the 24% rate and the triggers in (a)(1). | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleC-chap24-sec3406.htm | 2026-11-13 |
| 26 U.S.C. 6041A (govinfo). Read for services reporting and direct sales; the 2024 edition shows the pre-2026 USD 600 text, amended by section 70433(c). | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartB-sec6041A.htm | 2026-11-13 |
| 26 U.S.C. 6045 (govinfo). Read for subsection (f), payments to attorneys. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartB-sec6045.htm | 2026-11-13 |
| 26 U.S.C. 6050W (govinfo). Read for the Form 1099-K regime that displaces 1099-NEC for card and network payments. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartB-sec6050W.htm | 2026-11-13 |
| 26 U.S.C. 6071 (govinfo). Read for (c), the 31 January date. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partV-sec6071.htm | 2026-11-13 |
| 26 U.S.C. 6011 (govinfo). Read for (e), electronic filing. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partII-subpartA-sec6011.htm | 2026-11-13 |
| 26 U.S.C. 6721, 6722 and 6724 (govinfo). Read for the penalty structure and the reasonable cause waiver. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapB-partII-sec6721.htm | 2026-11-13 |
| 26 U.S.C. 7503 (govinfo). Read for the next-business-day rule. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap77-sec7503.htm | 2026-11-13 |

Not yet confirmed: Rev. Proc. 2025-32 section 4.57 labels the middle penalty tier "on or before August 1, 2026" for returns required to be filed in 2027, which reads as a typo for 1 August 2027; this skill applies 1 August of the filing year as section 6721(b)(2) provides. The inflation-adjusted threshold for payments made in 2027 is not yet published. The 2026 Form W-9 revision was not re-read; Treas. Reg. 1.6041-3(p) and 1.6045-5 were not re-read on an official host this session.
