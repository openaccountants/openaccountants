---
name: au-smsf
description: "Use this skill whenever asked about Australian self-managed superannuation funds -- SMSF accounting, the SMSF annual return (SAR), supervisory levy, fund tax at 15%, exempt current pension income (ECPI), actuarial certificates, non-arm's length income or expenses (NALI/NALE), contribution caps and acceptance rules, minimum pension drawdowns, transfer balance cap and TBAR reporting, SMSF audits, in-house assets, LRBA safe harbour rates, or Division 296. Trigger on phrases like \"SMSF\", \"self-managed super\", \"SAR\", \"supervisory levy\", \"actuarial certificate\", \"ECPI\", \"NALI\", \"TBAR\", \"minimum pension\", \"bare trust\", or \"SMSF audit\". ALWAYS read this skill before touching any SMSF work."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/au-smsf"
  jurisdiction: "AU"
  tax_year: "2026"
  last_updated: "2026-11-12"
---

# Australia Self-Managed Super Funds (SMSF) -- Accounting, Tax & Compliance Skill v1.0

## Scope

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Law changes relevant to 2026-27.** Division 296 applies from 2026-27. The ATO assesses the tax to the member. The SMSF has separate earnings, attribution and reporting duties in section 5.3. For payday super, the fund must ordinarily receive the contribution within 7 business days after the employee is paid qualifying earnings for it to count towards that payday. Confirm any exception under [SGAA 1992 s 18C](https://www.legislation.gov.au/C2004A04402/2026-07-01/2026-07-01/text/original/pdf) and check the fund's electronic service address and bank details. The general expense NALE rules in the Treasury Laws Amendment (Support for Small Business and Charities and Other Measures) Act 2024 limit the amount included as NALI to twice the expense shortfall from 2018-19. Use this guide for SMSF accounting, tax and compliance (see R-AU-SF-1 for the financial advice boundary).

### Quick reference

**Read this whole guide before computing or classifying anything.**

**Quick reference**

| Field | Value |
| --- | --- |
| Country | Australia |
| Primary legislation | Superannuation Industry (Supervision) Act 1993 (SIS Act) + SIS Regulations 1994; ITAA 1997 Div 295 |
| Regulator | ATO (SMSFs); ASIC (approved SMSF auditors, trustee companies) |
| Income year | 2026-27 (1 July 2026 -- 30 June 2027) |
| Fund tax rate (complying) | 15% on the low-tax component of taxable income. [Rates Act s 26(1)(a)](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html) and [ITAA 1997 s 295-545](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_6/document_6.html). |
| Discounted capital gains | One-third discount for an eligible discount capital gain, generally requiring acquisition at least 12 months before the CGT event. Applied at the 15% low-tax rate, this gives 10% on the gain remaining before discount; apply losses first. [ITAA 1997 ss 102-5 and 115-10 to 115-100](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html) and [Rates Act s 26](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html). |
| ECPI (retirement-phase earnings) | Exempt to the eligible extent under the segregated or proportionate method. Check method and pension conditions; assessable contributions and NALI are excluded. [ITAA 1997 ss 295-385 and 295-390](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_6/document_6.html). |
| NALI / non-complying fund | 45% on the non-arm's length component, or on taxable income of a non-complying fund. [Rates Act s 26(1)(b) and (2)](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html) and [ITAA 1997 s 295-545](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_6/document_6.html). |
| No-TFN contributions | Additional 32% on no-TFN contributions income of a complying fund; statutory exceptions apply. [Rates Act s 29](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html) and [ITAA 1997 ss 295-605 and 295-610](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_6/document_6.html). |
| Supervisory levy | $259 a year, paid in advance; a newly registered continuing fund pays $518 with its first SAR. A new fund winding up pays $259; an existing winding-up fund generally owes nil if the current-year levy was paid previously. [ATO levy, continuing/winding-up sections](https://www.ato.gov.au/api/public/content/0-7bc41a06-65a9-4e45-a959-165424670af5). |
| SAR due dates | Self-lodgers: new/overdue 31 October, payment 1 December; others lodge/pay 28 February unless advised otherwise. First-year return through a tax agent, including the first return after RNN: 28 February, or 31 October if notified after registration review. Continuing agent clients must check earlier income/status dates and the conditional 5 June concession; 15 May is the residual date. Weekend/public-holiday dates move to the next business day. [ATO lodge/pay](https://www.ato.gov.au/api/public/content/0-42064e26-5e71-4fce-8ca5-a244fc3c6d69) and [2026-27 agent program](https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/prepare-and-lodge/registered-agent-lodgment-program/due-dates-by-obligation-type/super-lodgment). |
| Audit | ASIC-registered approved SMSF auditor appointed at least 45 days before the SAR due date; audit finalised before lodgment. [ATO appointment and annual return sections](https://www.ato.gov.au/api/public/content/0-42064e26-5e71-4fce-8ca5-a244fc3c6d69). |
| Max members | 6 since 1 July 2021. [SIS Act s 17A(1)(a)](https://www.legislation.gov.au/C2004A04633/2026-08-10/2026-08-10/text/original/epub/OEBPS/document_1/document_1.html) and [2021 amending Act s 2 and Schedule 1 item 1](https://www.legislation.gov.au/C2021A00047/asmade/2021-06-22/text/original/epub/OEBPS/document_1/document_1.html). |
| Concessional cap (2026-27) | $32,500 general cap; eligible unused amounts from the prior 5 years can increase it if TSB < $500,000 at prior 30 June. [ITAA 1997 s 291-20](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_6/document_6.html) and [ATO cap table 1.1](https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds/contributions-caps). |
| Non-concessional cap (2026-27) | $130,000 general cap; nil where prior-30-June TSB is at least the general TBC. Check first-year bring-forward eligibility and existing arrangements under Rule 8. [ITAA 1997 s 292-85](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_6/document_6.html) and [ATO cap table 4](https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds/contributions-caps). |
| General transfer balance cap | $2,100,000 (2025-26: $2.0m); personal caps vary with prior use and proportional indexing. [ATO TBC table 26](https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds/transfer-balance-cap) and [ITAA 1997 ss 294-35 and 294-40](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_6/document_6.html). |
| Minimum pension drawdowns | 4% (under 65) to 14% (95+), using the higher of the account balance and full commutation withdrawal benefit; no reduction in 2026-27. [SIS Regulations 1994, Schedule 7 clauses 1 and 3-5](https://www.legislation.gov.au/F1996B00580/2026-07-01/2026-07-01/text/1/epub/OEBPS/document_2/document_2.html). |
| TBAR | Most events are due 28 days after quarter end for all SMSFs. Excess-determination voluntary commutations and commutation-authority responses have earlier/special deadlines; see section 6.2. [ATO TBAR, when to report](https://www.ato.gov.au/api/public/content/0-42064e26-5e71-4fce-8ca5-a244fc3c6d69). |
| LRBA safe harbour rate (PCG 2016/5) | 2026-27 annual variable benchmark: 9.35% real property and 11.35% listed shares or units (2025-26: 8.95% and 10.95%). Fixed-rate and remaining-term conditions apply; new real-property arrangements may require business real property. See section 7. [ATO table 28](https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds/other-super-rates-and-thresholds) and [PCG tables 1-2](https://www.ato.gov.au/law/view/document?docid=COG/PCG20165/NAT/ATO/00001&PiT=20261019000001). |
| Division 296 | First year 2026-27. The ATO assesses the member. Reconcile the fund earnings, attribution and reporting inputs under section 5.3. [Member liability, ITAA 1997 s 296-15](https://www.legislation.gov.au/C2026A00008/asmade/2026-03-13/text/original/epub/OEBPS/document_1/document_1.html) and [first-year rule, Transitional Provisions Act s 296-1](https://www.legislation.gov.au/C2004A05128/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html). |
| ASIC proprietary special purpose trustee company review fee | $70/year from 1 July 2026 for an eligible proprietary special purpose company; corporate trusteeship alone is insufficient. [ASIC fee A58](https://download.asic.gov.au/asic-nga/data/fees-data-current.json) and [eligibility](https://www.asic.gov.au/for-business-and-companies/companies/register-a-company/special-purpose-companies). |
| Contributor | Open Accountants |

## Ask the client first

### Required inputs

**Minimum viable** -- trust deed and member list, trustee type (individual vs corporate), member ages and account phases (accumulation / retirement), trial balance or bank statements, prior-year SAR, each member's TSB at 30 June 2026, and pension account balances and full commutation withdrawal benefits at 1 July or commencement.

**Recommended** -- actuarial certificate (if proportionate), 30 June market valuations with evidence, contribution and pension payment schedules per member, TBAR lodgment history, LRBA loan agreement and amortisation schedule, investment strategy with last review date.

**Ideal** -- signed trustee declarations (NAT 71089), audit workpapers and prior auditor management letters, deed history including pension documentation, lease agreements for any related-party tenancy, insurance policy schedule.

## The method, step by step

### Section 3 -- Fund structure and registration

#### 3.1 Definition of an SMSF (SIS Act s 17A)

- **Maximum members** -- Maximum 6 members (up from 4 on 1 July 2021).  _(SIS Act s 17A)_
- **Individual trustees** -- Individual trustees: every member is a trustee and every trustee is a member. Single-member fund: 2 individual trustees (the member + 1 other).  _(SIS Act s 17A)_
- **Corporate trustee** -- Corporate trustee: every member is a director and every director is a member. Single-member fund: sole director, or member + 1 other director.  _(SIS Act s 17A)_
- **Employee of another member** -- No member may be the employee of another member unless they are relatives.  _(SIS Act s 17A)_
- **Remuneration** -- Trustees/directors must not be remunerated for trustee duties (arm's-length professional services in another capacity are permitted, s 17B).  _(SIS Act s 17B)_
- **Disqualified persons** -- Disqualified persons (s 120: undischarged bankrupts, dishonesty convictions, civil penalty orders) can never act -- check the ATO disqualified trustees register at onboarding.  _(SIS Act s 120)_
- **Minors / lacking capacity** -- Minors and members lacking capacity act through a legal personal representative or parent/guardian (s 17A(3)); an enduring power of attorney can stand in for a member.  _(SIS Act s 17A(3))_

#### 3.2 Individual vs corporate trustee

**Individual vs corporate trustee**

| Factor | Individual trustees | Corporate trustee |
| --- | --- | --- |
| Ongoing cost | Nil | $70/year from 1 July 2026 only for an eligible proprietary special purpose company; otherwise check the applicable ASIC company fee. [ASIC A58/A52/A53](https://download.asic.gov.au/asic-nga/data/fees-data-current.json) and [eligibility](https://www.asic.gov.au/for-business-and-companies/companies/register-a-company/special-purpose-companies). |
| Trustees/directors change | Update each asset's ownership documents when individual trustees change. [ATO comparison, ownership row](https://smallbusiness.taxsuperandyou.gov.au/setting-up-a-self-managed-super-fund-smsf/how-the-smsf-structures-compare). | Company remains trustee; update director details. [ATO comparison](https://smallbusiness.taxsuperandyou.gov.au/setting-up-a-self-managed-super-fund-smsf/how-the-smsf-structures-compare). |
| s 166 administrative penalties | Each individual trustee who contravenes is personally liable. [SIS Act s 166](https://www.legislation.gov.au/C2004A04633/2026-08-10/2026-08-10/text/original/epub/OEBPS/document_2/document_2.html). | Penalty on company; directors are jointly and severally liable. [SIS Act ss 166 and 169](https://www.legislation.gov.au/C2004A04633/2026-08-10/2026-08-10/text/original/epub/OEBPS/document_2/document_2.html). |
| Single-member fund | 2 trustees, including the member; relative/employment conditions apply. [SIS Act s 17A(2)(b)](https://www.legislation.gov.au/C2004A04633/2026-08-10/2026-08-10/text/original/epub/OEBPS/document_1/document_1.html). | Member may be sole director; if another director acts, relative/employment conditions apply. [SIS Act s 17A(2)(a)](https://www.legislation.gov.au/C2004A04633/2026-08-10/2026-08-10/text/original/epub/OEBPS/document_1/document_1.html). |
| Succession on death/incapacity | Replacement trustee may be needed; representative exceptions and temporary relief can apply. [SIS Act ss 17A(3)-(5)](https://www.legislation.gov.au/C2004A04633/2026-08-10/2026-08-10/text/original/epub/OEBPS/document_1/document_1.html). | Company continues; maintain eligible directorship and succession arrangements. The same statutory exceptions/relief can apply. [SIS Act ss 17A(3)-(5)](https://www.legislation.gov.au/C2004A04633/2026-08-10/2026-08-10/text/original/epub/OEBPS/document_1/document_1.html). |

Under SIS Act s 17A(3), eligible legal personal representatives can act for deceased or legally disabled members, or under an enduring power of attorney, subject to the statutory conditions. Where s 17A(4) applies, temporary SMSF status ends at the earlier of appointment of an RSE licensee and 6 months after status would otherwise cease. Subsection (5) excludes specified failures involving admission of new members. These rules can apply to individual trustees and corporate directors. [SIS Act ss 17A(3)-(5)](https://www.legislation.gov.au/C2004A04633/2026-08-10/2026-08-10/text/original/epub/OEBPS/document_1/document_1.html).

For the lower ASIC fee, the company's sole purpose must be trusteeship of a regulated superannuation fund and its constitution must prohibit distributions of income or property to members. Notify ASIC before the next annual review date if special purpose status starts or stops. [ASIC special purpose companies](https://www.asic.gov.au/for-business-and-companies/companies/register-a-company/special-purpose-companies).

For one applicable contravention of SIS Act s 65(1), 67(1) or 84(1), s 166 sets an administrative penalty of 60 units. At $364/unit from 1 July 2026, that is $21,840 for each liable individual trustee, or $43,680 if 2 individual trustees each contravene. A corporate trustee incurs the penalty once; its directors are jointly and severally liable. Fund assets must not pay or reimburse it. Determine the contravention date and liable persons, rather than treating this as a total for every breach. [SIS Act ss 166, 168 and 169](https://www.legislation.gov.au/C2004A04633/2026-08-10/2026-08-10/text/original/epub/OEBPS/document_2/document_2.html) and [2026 penalty-unit instrument, ss 2 and 5](https://www.legislation.gov.au/F2026N00424/asmade/2026-06-16/text/original/pdf).

#### 3.3 Registration checklist (new fund)

1. Execute trust deed, appoint trustees, hold initial assets (fund is not legally established until it holds assets).
2. Each trustee/director signs the **ATO trustee declaration (NAT 71089)** within 21 days of appointment; retain 10 years.
3. Register with the ATO within 60 days: **TFN + ABN**, electing regulation under SIS s 19 (irrevocable).
4. Open a fund bank account in the fund/trustee name (asset separation, SIS Reg 4.09A).
5. Obtain an **ESA (electronic service address)** -- required for SuperStream employer contributions (critical under payday super) and for ALL rollovers in/out (SuperStream v3).
6. Prepare the investment strategy (SIS Reg 4.09) BEFORE investing.
7. First-year fund with no assets: request cancellation or 'return not necessary' -- otherwise the SAR is due.

### Section 4 -- Fund taxation (ITAA 1997 Div 295)

#### 4.1 Rate structure

**Rate structure**

| Income class | Rate | Notes |
| --- | --- | --- |
| Assessable contributions (ss 295-160 and 295-190) | 15% | Employer contributions, including salary sacrifice; personal contributions covered by a valid, acknowledged s 290-170 notice. [ITAA 1997 ss 295-160 and 295-190](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_6/document_6.html) and [Rates Act s 26](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html). |
| Ordinary earnings on accumulation assets | 15% | Taxable accumulation earnings within the low-tax component. [ITAA 1997 s 295-545(3)](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_6/document_6.html) and [Rates Act s 26(1)(a)](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html). |
| Discounted capital gains | 10% effective at the 15% low-tax rate | Derived from the one-third discount on eligible gains after losses. The holding period alone does not establish eligibility. [ITAA 1997 ss 102-5 and 115-10 to 115-100](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html) and [Rates Act s 26](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html). |
| ECPI (retirement-phase earnings) | Exempt to the eligible extent | Method and minimum-payment conditions apply; assessable contributions and NALI are excluded. [ITAA 1997 ss 295-385 and 295-390](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_6/document_6.html). |
| NALI / NALC | 45% | Rate applies to the non-arm's length component determined under s 295-545, not necessarily every gross amount described as NALI. [Rates Act s 26(1)(b)](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html) and [ITAA 1997 s 295-545(2)-(2A)](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_6/document_6.html). |
| Non-complying fund | 45% | Taxable income. If the fund was complying in the preceding income year, include the amount calculated under s 295-325; a first non-complying year alone does not establish that trigger. [Rates Act s 26(2)](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html) and [ITAA 1997 s 295-320 table item 2 and s 295-325](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_6/document_6.html). |
| No-TFN contributions | Additional 32% for a complying fund | A refundable offset can arise when a member first quotes their TFN in the current income year for no-TFN tax payable in one of the preceding 3 income years. Successor-fund rules and other conditions apply. [Rates Act s 29](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html), [ITAA 1997 ss 295-675 and 295-680](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_6/document_6.html) and [s 67-23 table item 15](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html). |

Franking credits offset fund tax and are refundable. Capital losses offset only capital gains (carry forward; losses on segregated pension assets are disregarded entirely).

For no-TFN tax, test assessable contributions under Subdivision 295-C, the contribution date and whether the member quoted their TFN by year end. Section 295-610 has a limited exception for an interest existing before 1 July 2007 where the relevant assessable contributions do not exceed $1,000. The additional rate is 45% + 2% - 15% = 32% for a complying fund; a non-complying fund instead has an additional 2%. For a first TFN quotation in 2026-27, the preceding 3 income years are 2023-24, 2024-25 and 2025-26, subject to section 295-675 and successor-fund conditions. [Rates Act s 29](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html) and [ITAA 1997 ss 295-605, 295-610 and 295-675 to 295-680](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_6/document_6.html).

#### 4.2 ECPI -- exempt current pension income

- **Segregated method** -- **Segregated method** (ss 295-385): specific assets documented as solely supporting retirement-phase pensions; ALL income (and gains/losses -- disregarded) from those assets is exempt. No actuarial certificate needed for periods of full segregation. A fund 100% in retirement phase at ALL times in the year is deemed segregated for the whole year -- no certificate.  _(ITAA 1997 ss 295-385)_
- **Proportionate method** -- **Proportionate method** (s 295-390): an actuary certifies the exempt proportion of unsegregated income based on average retirement-phase liabilities. **Actuarial certificate required every year the method is used -- obtain it BEFORE lodging the SAR.** Assessable contributions and NALI are never ECPI. Deductions must be apportioned; expenses of gaining ECPI are non-deductible.  _(ITAA 1997 s 295-390)_
- **Disregarded small fund assets** -- **Disregarded small fund assets (s 295-387):** the fund CANNOT use the segregated method (must use proportionate + certificate) when, just before the start of the income year, any member receiving a retirement-phase income stream (from any provider) had a **TSB over $1.6 million**. The $1.6m trigger is a fixed statutory figure -- it has NOT indexed with the transfer balance cap. Exception: a fund 100% in retirement phase at all times in the year escapes the rule (from 2021-22).  _(ITAA 1997 s 295-387)_
- **Minimum-payment condition** -- **Minimum-payment condition:** ECPI for an account-based pension is only available if the SIS minimum was actually paid for the year (Section 6.1; Example 4).  _(Section 6.1)_

#### 4.3 NALI and NALE -- **AUDIT FLASH POINT**

- **NALI definition** -- Income is NALI (s 295-550, taxed at 45%) where it exceeds an arm's-length amount from a non-arm's-length scheme, where a private company dividend or non-fixed trust distribution is involved, or -- since 1 July 2018 -- where the fund incurred **non-arm's-length expenditure** (NALE: expenses lower than arm's length, including nil).  _(ITAA 1997 s 295-550)_
- **Specific expense** -- **Specific expense** (tied to a particular asset, e.g. cut-price property maintenance by a related builder): ALL income from that asset is NALI -- including the eventual capital gain.  _(ITAA 1997 s 295-550 (Treasury Laws Amendment (Support for Small Business and Charities and Other Measures) Act 2024))_
- **General expense (twice the shortfall)** -- **General expense** (e.g. accounting or admin fees): NALI is capped at **2 x (arm's-length expense − actual expense)** -- the "twice the shortfall" rule for SMSFs and small APRA funds.  _(ITAA 1997 s 295-550 (Treasury Laws Amendment (Support for Small Business and Charities and Other Measures) Act 2024))_
- **Large APRA funds carve-out** -- Large APRA-regulated funds are carved out of NALE entirely.  _(ITAA 1997 s 295-550)_
- **NALC overall cap** -- The overall non-arm's-length component cannot exceed the fund's assessable income less deductions, excluding assessable contributions and their deductions.  _(ITAA 1997 s 295-550)_
- **Trustee-capacity services** -- Trustee-capacity services (unpaid, own equipment, not through a business) are NOT NALE; discounted services through the trustee's firm ARE (LCR 2021/2). PCG 2020/5's transitional relief for general expenses ended 30 June 2023.  _(LCR 2021/2; PCG 2020/5)_

### Section 5 -- Contributions

#### 5.1 Acceptance (SIS Reg 7.04)

**Acceptance by member age**  _(SIS Reg 7.04)_

| Member age | Fund may accept |
| --- | --- |
| Under 75 | All contribution types -- no work test for acceptance |
| 75+ (from 28 days after the end of the month of the 75th birthday) | Mandated employer (SG) and downsizer ONLY |
| Any age, no TFN quoted | Do not accept member contributions other than PPL superannuation contributions without a TFN. If an inconsistent amount is received, return it within 30 days of becoming aware, unless the TFN is quoted within 30 days of receipt. Assess employer contributions under section 4.1's no-TFN tax rules, including fund status and statutory exceptions. [SIS Regulations 7.04(2) and (4)](https://www.legislation.gov.au/F1996B00580/2026-07-01/2026-07-01/text/1/epub/OEBPS/document_1/document_1.html) and [ITAA 1997 ss 295-605 and 295-610](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_6/document_6.html). |

- **Work test (67-74)** -- **Work test (67-74):** 40 hours in 30 consecutive days -- required only to CLAIM A DEDUCTION for personal contributions (s 290-165), not for acceptance. One-off exemption for recent retirees with TSB < $300,000.  _(ITAA 1997 s 290-165)_
- **Downsizer** -- **Downsizer (s 292-102):** age 55+, up to **$300,000 per person** from sale of a home owned 10+ years, contributed within 90 days of settlement with the ATO form; excluded from both caps and acceptance limits; once only; counts to TSB.  _(ITAA 1997 s 292-102)_

**CGT cap:** small business 15-year/retirement exemption proceeds excluded from the NCC cap by election, lifetime limit $1,935,000 (2026-27).

#### 5.2 Caps (2026-27)

- **Rule 8 -- caps and bring-forward** -- **Rule 8 -- caps and bring-forward.** Concessional $32,500 (2025-26: $30,000); carry-forward of up to 5 prior years' unused cap only if TSB < $500,000 at 30 June 2026. Non-concessional $130,000 (4 x concessional). Bring-forward by TSB at 30 June 2026: < $1.84m -> $390,000 over 3 years; $1.84m to < $1.97m -> $260,000 over 2 years; $1.97m to < $2.1m -> $130,000 only; >= $2.1m -> nil. Bring-forward access requires being under 75 at some time in the first year, contributions that trigger the arrangement and no existing arrangement determining that year's cap; check contribution acceptance separately. The bands are derived from the 2026-27 general TBC and annual cap. [ITAA 1997 ss 291-20 and 292-85](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_6/document_6.html), [ATO annual caps](https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds/contributions-caps) and [general TBC table 26](https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds/transfer-balance-cap).

**Excess flows:** excess concessional -> included in the member's assessable income at marginal rates less a 15% offset; may elect to release up to 85%; unreleased excess counts to the NCC cap (no excess concessional charge since 2021-22). Excess non-concessional -> release + associated earnings taxed at marginal rates, or (if retained) 47% on the excess. The FUND's accounting never changes -- assessable contributions stay taxed at 15% in the fund; the excess consequences land on the member.

#### 5.3 Member surcharges and Division 296 fund reporting

- **Division 293.** If Division 293 income plus low-tax contributions exceeds $250,000, the ATO assesses the member at 15% of the lesser of the excess and their low-tax contributions. See Rule 10 in [au-super-guarantee](au-super-guarantee.md) for the income and contribution definitions. [ITAA 1997 s 293-20](https://www.legislation.gov.au/C2026C00471/latest/text) and [Imposition Act s 5](https://www.legislation.gov.au/C2013A00087/asmade), read 10 November 2026.
- **Division 296 member assessment.** For 2026-27, use the member's total superannuation balance at 30 June 2027 across relevant interests. Later years generally use the greater of the opening and closing balances. In both cases exclude the limited recourse borrowing add-back under paragraph 307-230(1)(d). Check the exceptions for child recipients of super income streams, structured settlement contributions and members who die by the end of the first year. Confirm other super interests even if the member's SMSF balance is below the threshold. Use [the rates card](au-rates-2026-27.md) and flag the member liability for review. [ITAA 1997 ss 296-15 to 296-25, 296-40, 296-45 and 296-260](https://www.legislation.gov.au/C2026A00008/asmade/2026-03-13/text/original/epub/OEBPS/document_1/document_1.html) and [first-year rules, s 296-1](https://www.legislation.gov.au/C2004A05128/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html).
- **Fund earnings and reporting.** Reconcile Division 296 fund earnings, attribute relevant superannuation earnings for each reportable interest and report the amounts required by Schedule 1 paragraph 390-5(9)(ba) of the Taxation Administration Act 1953, regardless of whether the member is liable for Division 296 tax. Exclude amounts taken to be nil under ITAA 1997 subsection 296-55(2). Use the separate rule for prescribed and defined benefit interests. For interests under regulation 296-65.03, obtain the actuarial certificate unless fund earnings are nil or all statutory sole-member conditions are met. From 2026-27, the ATO directs SMSFs to report relevant earnings for in-scope members in the SMSF annual return. If the ATO identifies an omitted in-scope member, amend the return. Check the approved return labels and instructions before filing. [ITAA 1997 ss 296-60 to 296-70](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_6/document_6.html) · [Regulation 296-65.03](https://www.legislation.gov.au/F2021L00206/2026-06-27/2026-06-27/text/original/epub/OEBPS/document_1/document_1.html) · [Taxation Administration Act 1953, Schedule 1 s 390-5](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html) · [ATO SMSF reporting guidance](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/self-managed-super-funds-smsf/smsf-newsroom/division-296-tax-the-latest-for-smsfs).
- **Transitional CGT choice.** Preserve 30 June 2026 market values and cost-base records. A qualifying small fund can make an irrevocable choice in the approved form by the 2026-27 return due date. The choice covers all CGT assets held at 30 June 2026 and the adjustment applies to Division 296 fund earnings for an asset held continuously to its CGT event. The ATO’s 24 September 2026 notice said the approved form was forthcoming and allowed the same information in another format. The election need not be sent to the ATO. [ATO administration guidance](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/self-managed-super-funds-smsf/smsf-administration-and-reporting/about-division-296-tax-for-smsfs). Confirm the current approved form and required information before making it. [Transitional provisions, ss 296-50 and 296-55](https://www.legislation.gov.au/C2004A05128/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) · [ATO September SMSF election notice](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/self-managed-super-funds-smsf/smsf-newsroom/division-296-tax-the-latest-for-smsfs).
- **Transitional CGT records.** Keep the choice and, for each affected asset, each element of its adjusted cost base and reduced cost base. Records must be in English or readily accessible and convertible into English. Retain each record until the end of 5 years after it becomes certain that no CGT event or further CGT event can happen for which the record could reasonably be expected to be relevant to the fund’s Division 296 fund earnings. The 5-year period starts only once that certainty is reached. [Transitional provisions, s 296-55](https://www.legislation.gov.au/C2004A05128/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) · [ATO SMSF CGT adjustment and records guidance](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/self-managed-super-funds-smsf/smsf-administration-and-reporting/about-division-296-tax-for-smsfs).

### Section 6 -- Pensions

#### 6.1 Account-based pension minimums (SIS Reg 1.06(9A), Sch 7)

**Account-based pension minimums**  _(SIS Reg 1.06(9A), Sch 7)_

| Age at 1 July (or commencement) | Minimum % of calculation base | Source |
| --- | --- | --- |
| Under 65 | 4% | [SIS Regulations 1994, Schedule 7 clauses 1 and 3-5](https://www.legislation.gov.au/F1996B00580/2026-07-01/2026-07-01/text/1/epub/OEBPS/document_2/document_2.html) |
| 65-74 | 5% | [SIS Regulations 1994, Schedule 7 clauses 1 and 3-5](https://www.legislation.gov.au/F1996B00580/2026-07-01/2026-07-01/text/1/epub/OEBPS/document_2/document_2.html) |
| 75-79 | 6% | [SIS Regulations 1994, Schedule 7 clauses 1 and 3-5](https://www.legislation.gov.au/F1996B00580/2026-07-01/2026-07-01/text/1/epub/OEBPS/document_2/document_2.html) |
| 80-84 | 7% | [SIS Regulations 1994, Schedule 7 clauses 1 and 3-5](https://www.legislation.gov.au/F1996B00580/2026-07-01/2026-07-01/text/1/epub/OEBPS/document_2/document_2.html) |
| 85-89 | 9% | [SIS Regulations 1994, Schedule 7 clauses 1 and 3-5](https://www.legislation.gov.au/F1996B00580/2026-07-01/2026-07-01/text/1/epub/OEBPS/document_2/document_2.html) |
| 90-94 | 11% | [SIS Regulations 1994, Schedule 7 clauses 1 and 3-5](https://www.legislation.gov.au/F1996B00580/2026-07-01/2026-07-01/text/1/epub/OEBPS/document_2/document_2.html) |
| 95+ | 14% | [SIS Regulations 1994, Schedule 7 clauses 1 and 3-5](https://www.legislation.gov.au/F1996B00580/2026-07-01/2026-07-01/text/1/epub/OEBPS/document_2/document_2.html) |

Use the higher of the pension account balance and the withdrawal benefit payable on full commutation, measured at 1 July or, in the commencement year, on the commencement day. Select the age factor at the same date. No reduced ("COVID-halved") rates are in force in 2026-27. For a mid-year commencement, apply the factor proportionally to the days including and following commencement; no payment is required in that year if commencement is on or after 1 June. Round the resulting amount to the nearest $10, with an exact $5 rounded up. [SIS Regulations 1994, Schedule 7 clauses 1 and 3-5](https://www.legislation.gov.au/F1996B00580/2026-07-01/2026-07-01/text/1/epub/OEBPS/document_2/document_2.html). Payment must LEAVE the fund by 30 June -- journal entries are not payments. Transition-to-retirement income streams (not in retirement phase): 10% maximum applies and the fund earns NO ECPI on them.

**Shortfall consequence:** if the minimum is not met, the pension is taken to have ceased at the start of the income year -- the fund loses ECPI for that pension for the WHOLE year, payments made are treated as lump sums, and a new pension (new documents, new TBC credit, TBAR events) must be commenced to resume. **Catch-up exception** (once only, self-assessed): honest mistake or matters outside trustee control, shortfall <= 1/12 of the annual minimum, caught up as soon as practicable (generally within 28 days of becoming aware) -- then ECPI continues as if paid. Larger or repeat shortfalls need the Commissioner's discretion.

#### 6.2 Transfer balance cap and TBAR

- General TBC 2026-27: **$2.1m**. Personal caps differ per member (proportional indexing of unused cap space) -- read the member's ATO TB account, never assume the general cap.
- **Ordinary TBAR events:** due 28 days after quarter end for all SMSFs: 28 October, 28 January, 28 April and 28 July. The old TSB-based annual concession ended on 1 July 2023. No nil report is needed where there is no reportable event. Check the specific excess-balance deadlines below. [ATO TBAR, when to report](https://www.ato.gov.au/api/public/content/0-42064e26-5e71-4fce-8ca5-a244fc3c6d69) and [agent program, event-based reporting](https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/prepare-and-lodge/registered-agent-lodgment-program/due-dates-by-obligation-type/super-lodgment).
- Report: retirement-phase pension commencements and their value, commutations (including commutations to fix excess TB), certain LRBA repayment value-shifts, structured settlement contributions. Pension payments themselves and investment earnings are NOT TB events.
- **Excess transfer balance:** a voluntary commutation in response to an excess transfer balance determination must be reported within 10 business days after the end of the month of commutation. A response to a commutation authority must be reported within 60 days of its issue date. Do not defer these events to the ordinary quarterly deadline; comply with the determination/authority and correct incomplete reporting promptly. [ATO TBAR, exceeding the personal transfer balance cap](https://www.ato.gov.au/api/public/content/0-42064e26-5e71-4fce-8ca5-a244fc3c6d69).

### Section 7 -- Investment and prohibited-transaction rules

- **Sole purpose test** -- **Sole purpose test (s 62):** fund maintained solely for retirement/death benefits -- any current-day member benefit (use of the holiday house, art on the wall, wine in the cellar) breaches it.  _(SIS Act s 62)_
- **No loans to members** -- **s 65 -- no loans or financial assistance to members/relatives.** Ever, in any amount. 60 penalty units per trustee.  _(SIS Act s 65)_
- **In-house assets** -- **In-house assets (Part 8, s 71):** loans to, investments in, or leases to related parties capped at **5% of fund market value** (measured at acquisition and each 30 June). Exceeding at 30 June -> written disposal plan executed before the end of the NEXT year (s 82). Business real property leased at market rent is excluded.  _(SIS Act Part 8, s 71; s 82)_
- **Related-party acquisitions** -- **s 66 -- acquisitions from related parties prohibited**, except listed securities at market value, business real property at market value, and in-house assets within the 5% limit.  _(SIS Act s 66)_
- **Borrowing and LRBA.** Borrowing is prohibited under s 67 except for its exceptions, including a compliant LRBA under ss 67A-67B. The single acquirable asset is held in a separate holding trust and lender recourse is limited to that asset. From 10 August 2026, a real-property LRBA arrangement within the new rule must acquire business real property as defined by s 66. The amendment applies to arrangements entered into from that date under which money is borrowed, or borrowings maintained, to acquire assets. It does not apply to the relevant extent where the arrangement maintains or refinances borrowing under a pre-commencement arrangement, or the asset acquisition occurs under a pre-commencement arrangement, including later settlement. Check the actual arrangements before relying on this saving. [SIS Act ss 66, 67 and 67A](https://www.legislation.gov.au/C2004A04633/2026-08-10/2026-08-10/text/original/epub/OEBPS/document_1/document_1.html) and [2026 amending Act, commencement table and Schedule 5 items 1-2](https://www.legislation.gov.au/C2026A00049/asmade/2026-06-26/text/1/epub/OEBPS/document_1/document_1.html).
- **LRBA arm's-length terms.** PCG 2016/5 is an income-tax compliance safe harbour; it does not replace the SIS borrowing requirements. Missing a safe-harbour condition does not automatically deem income NALI. Obtain evidence of actual arm's-length terms where the safe harbour is unavailable. For 2026-27 the annual variable benchmarks are **9.35%** for real property and **11.35%** for listed shares or units; for 2025-26 they are 8.95% and 10.95%. [ATO table 28](https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds/other-super-rates-and-thresholds) and [PCG 2016/5 paragraphs 1-9, tables 1-2 and footnote 1](https://www.ato.gov.au/law/view/document?docid=COG/PCG20165/NAT/ATO/00001&PiT=20261019000001).
- **Safe-harbour loan conditions.** Property: maximum 70% aggregate LVR and 15-year original term; listed shares/units: maximum 50% aggregate LVR and 7-year original term. On refinancing, subtract the duration of previous relevant loans from that maximum term. Test market value at origination or refinancing. Variable interest uses each year's applicable benchmark. A rate fixed at commencement may remain fixed for up to 5 years for property or 3 years for listed shares/units, then must become variable within the maximum total term. Both require monthly principal-and-interest repayments, registered asset security and a written executed loan agreement. Check the complete table and any applicable historic transition; these terms do not validate an otherwise prohibited borrowing. [PCG 2016/5 tables 1-2](https://www.ato.gov.au/law/view/document?docid=COG/PCG20165/NAT/ATO/00001&PiT=20261019000001).
- **Valuations** -- **Valuations (SIS Reg 8.02B):** all assets at market value each 30 June, on objective supportable evidence -- unlisted trusts, private companies and property are the perennial audit qualification triggers.  _(SIS Reg 8.02B)_
- **Investment strategy** -- **Investment strategy (SIS Reg 4.09):** must address risk, return, liquidity, diversification and insurance for members; review REGULARLY -- document a review at least annually and on any significant event (new member, pension commencement, LRBA, market dislocation).  _(SIS Reg 4.09)_

## Boundary and exception table

### Conservative defaults

| Ambiguity | Default |
| --- | --- |
| Unknown ECPI method | Assume proportionate -- actuarial certificate REQUIRED before claiming |
| Unknown whether minimum pension paid | Do NOT claim ECPI until payments verified against SIS Reg Sch 7 minimum |
| Unknown member TSB | Assume caps/bring-forward/carry-forward unavailable; ask for TSB at 30 June 2026 |
| Related-party transaction in the file | Escalate -- s 65 / s 66 / Part 8 / NALI screen before classifying |
| Unknown asset valuation support | Flag audit risk -- market value at 30 June required (SIS Reg 8.02B) |
| Contribution credited near 30 June | Date RECEIVED by the fund governs the year and the cap |
| Unknown auditor appointment date | Check the 45-day rule now -- late appointment jeopardises lodgment |
| Unknown member age | Ask -- age drives acceptance rules AND pension minimums |
| Payment to a member with no documented condition of release | Treat as potential illegal early access; escalate (never classify as a benefit) |

### Common breach patterns

**Common breach patterns**

| Pattern in the file | Provision | Consequence | Action |
| --- | --- | --- | --- |
| EFT to member tagged "loan"/"temporary" | s 65 | 60 units per applicable s 166 contravention and liable trustee ($21,840 at $364/unit); check auditor reporting obligations. [SIS Act s 166](https://www.legislation.gov.au/C2004A04633/2026-08-10/2026-08-10/text/original/epub/OEBPS/document_2/document_2.html) | Repay + interest; escalate; never reclassify as benefit without condition of release |
| Related-party investments/lease > 5% at 30 June | s 71/s 84 | 60 PU; ATO enforceable undertaking | Written disposal plan before next 30 June end |
| Borrowing outside LRBA (overdraft, margin loan) | s 67 | 60 PU | Clear immediately; document |
| TBAR lodged late/never | TBC reporting | Excess TB determinations off stale data; FTL penalties | Lodge all missed events now; reconcile TB account |
| Proportionate ECPI claimed, no actuarial certificate | s 295-390 | ECPI claim invalid -- amend SAR, tax at 15% | Obtain certificate BEFORE lodgment, always |
| Contributions over caps | Div 291/292 | Member-level ECC/ENCC assessments, release authorities | Check carry-forward/bring-forward eligibility; action release elections in 60 days |
| Benefit paid, no condition of release | s 62 / SIS Reg 6.17 | Illegal early access: marginal tax + penalties, disqualification, possible fund non-compliance (45%) | Refuse to classify as benefit; escalate (R-AU-SF-5) |
| Fund asset used personally (holiday house week) | s 62 sole purpose | Compliance action; NALI risk on related income | Escalate; document cessation |

## Worked cases

### Example 1 -- Fund tax on mixed income with ECPI and a discounted gain (2026-27)

Two-member fund, one accumulation, one account-based pension; unsegregated; actuary certifies **60% exempt proportion**. Income: rent $32,000, interest $8,000, unfranked dividends $10,000 (= $50,000 ordinary); gross capital gain $30,000 on shares held 3 years; employer + salary-sacrifice contributions $30,000; general admin expenses $4,000.

```
Net capital gain      = $30,000 x (1 - 1/3)           = $20,000
Non-contribution base = $50,000 + $20,000             = $70,000
ECPI                  = 60% x $70,000                 = $42,000
Deductible expenses   = 40% x $4,000                  = $1,600   (ECPI share non-deductible)
Taxable income        = $30,000 + $70,000 - $42,000 - $1,600 = $56,400
Gross tax             = 15% x $56,400                 = $8,460
Payable with SAR      = $8,460 + $259 levy            = $8,719
```

The gain's effective rate here: net gain $20,000, taxed share 40% = $8,000, tax $1,200 = 4.0% of the gross $30,000 (10% without ECPI). Contributions are NEVER sheltered by ECPI.

### Example 2 -- NALE on a general expense (2x rule)

The trustee's accounting firm charges the fund $1,000 for 2026-27 administration; the arm's-length fee is $3,500. This is a non-arm's-length GENERAL expense.

```
Shortfall = $3,500 - $1,000 = $2,500
NALI      = 2 x $2,500      = $5,000
Tax       = 45% x $5,000    = $2,250  (vs $750 at 15% -- a $1,500 penalty effect)
```

Cap check: NALC cannot exceed assessable income less deductions excluding contributions -- here $60,000, so not binding. Contrast: if the discount had been a SPECIFIC expense on a rental property, ALL of that property's income AND its eventual capital gain would be NALI at 45%. Unpaid trustee-capacity work with the trustee's own equipment is not NALE (LCR 2021/2).

### Example 3 -- Excess concessional contributions flow

Member (TSB $600,000 -- no carry-forward) receives SG + salary sacrifice totalling $40,000 in 2026-27 against the $32,500 cap.

```
Fund:   taxes all $40,000 at 15%                        = $6,000  (unchanged)
Excess  = $40,000 - $32,500                             = $7,500
Member: assessable at marginal 39% (37% + 2% Medicare)  = $2,925
        less 15% offset ($7,500 x 15%)                  = -$1,125
        net extra personal tax                          = $1,800
```

Member may elect to release up to 85% of the excess ($6,375) from the fund; unreleased excess also counts toward the $130,000 NCC cap. Nothing is amended in the fund's SAR.

### Example 4 -- Minimum pension shortfall kills ECPI

Member aged 76 at 1 July 2026; pension account balance $480,000 and full commutation withdrawal benefit no greater than that balance. Minimum = 6% x $480,000 = **$28,800**. The fund pays only $22,000 by 30 June 2027 -- shortfall $6,800.

The self-assessed catch-up exception is unavailable: $6,800 exceeds 1/12 of the minimum ($2,400). Result: the pension is taken to have ceased 1 July 2026; the fund claims NO ECPI for that interest all year; the $22,000 paid is treated as lump sums; restarting requires fresh pension documents, a new TBC credit and TBAR events (cessation/commencement). Had the shortfall been <= $2,400 from an honest mistake and topped up within about 28 days of discovery, the trustee could self-assess the exception -- once ever; anything else needs the Commissioner's discretion.

### Example 5. Division 293 taxable contributions

Assume Division 293 income of $245,000 and low-tax contributions of $20,000. The combined amount exceeds the $250,000 threshold by $15,000. The ATO assesses 15% of $15,000, or $2,250. [ITAA 1997 s 293-20](https://www.legislation.gov.au/C2026C00471/latest/text) and [Imposition Act s 5](https://www.legislation.gov.au/C2013A00087/asmade).

```oa-check
name: Division 293 taxable contributions are capped by the excess
inputs:
  division_293_income: 245000
  low_tax_contributions: 20000
  threshold: 250000
steps:
  - excess: max(division_293_income + low_tax_contributions - threshold, 0)
  - taxable_contributions: min(low_tax_contributions, excess)
  - tax: pct(taxable_contributions, 15)
expected:
  taxable_contributions: 15000
  tax: 2250
```

### Example 6. Division 296 first-year balance

A member has Division 296 balances of $3.5 million at 30 June 2026 and $2.9 million at 30 June 2027 after any required adjustment. The first year uses the $2.9 million closing balance, below the $3 million threshold, so there is no member tax for that year. Keep the member balance and fund records for reporting. [Income Tax (Transitional Provisions) Act 1997, s 296-1](https://www.legislation.gov.au/C2004A05128/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html).

```oa-check
name: Division 296 uses the closing balance in 2026-27
inputs:
  opening_balance: 3500000
  closing_balance: 2900000
  threshold: 3000000
steps:
  - above_threshold: max(closing_balance - threshold, 0)
  - excess_using_higher_balance: max(max(opening_balance, closing_balance) - threshold, 0)
expected:
  above_threshold: 0
  excess_using_higher_balance: 500000
```

### Example 7. Pension minimum with a higher withdrawal benefit

A member is aged 65 at 1 July 2026. The pension account balance is $100,000 and the full commutation withdrawal benefit is $120,100. The calculation base is $120,100, so 5% is $6,005. Round the exact $5 upward: the minimum is $6,010. Using only the account balance would give $5,000 and understate the minimum by $1,010. [SIS Regulations 1994, Schedule 7 clauses 1 and 3-5](https://www.legislation.gov.au/F1996B00580/2026-07-01/2026-07-01/text/1/epub/OEBPS/document_2/document_2.html).

If those values instead apply at commencement on 1 January 2027, use the 181 days including commencement through 30 June, then round: $6,005 x 181 / 365 gives a $2,980 minimum.

```oa-check
name: Pension minimum uses the higher withdrawal benefit and statutory rounding
inputs:
  account_balance: 100000
  withdrawal_benefit: 120100
  age_factor: 5
  days_from_commencement: 181
  days_in_year: 365
steps:
  - calculation_base: max(account_balance, withdrawal_benefit)
  - annual_unrounded: pct(calculation_base, age_factor)
  - annual_minimum: round(annual_unrounded, -1)
  - commencement_minimum: round(annual_unrounded * days_from_commencement / days_in_year, -1)
  - account_only_minimum: round(pct(account_balance, age_factor), -1)
  - understatement: annual_minimum - account_only_minimum
expected:
  calculation_base: 120100
  annual_unrounded: 6005
  annual_minimum: 6010
  commencement_minimum: 2980
  account_only_minimum: 5000
  understatement: 1010
```

## When to refuse or refer

- **R-AU-SF-1 -- Financial product / investment advice (AFSL boundary)** -- *Trigger:* asked to recommend investments, whether to start/commute a pension, how much to contribute, or whether an SMSF suits the client. *Message:* "That is personal financial product advice requiring an Australian Financial Services Licence (the accountants' exemption ended 1 July 2016). I can handle SMSF accounting, tax and compliance only. Refer to a licensed financial adviser." HARD refusal -- no exceptions.
- **R-AU-SF-2 -- In-specie contribution / off-market transfer valuations** -- *Trigger:* asked to set the value of an asset contributed or transferred in-specie. *Message:* "Contribution value must be market value with qualified valuation evidence; s 66 acquisition rules also apply. Obtain an independent valuation and escalate."
- **R-AU-SF-3 -- LRBA structuring** -- *Trigger:* asked to establish a bare/holding trust, draft loan terms, or design a related-party LRBA. *Message:* "LRBA establishment is legal and financial advice. I can classify payments on an EXISTING documented LRBA and check the PCG 2016/5 safe harbour only. Escalate."
- **R-AU-SF-4 -- Related-party acquisitions** -- *Trigger:* proposed purchase from / lease to a member or related party. *Message:* "s 66 prohibits most related-party acquisitions (exceptions: listed securities and business real property at market value, within in-house limits). Transaction design must be escalated before any step is taken."
- **R-AU-SF-5 -- Early-access schemes** -- *Trigger:* any request to pay benefits without a documented condition of release, or to 'temporarily borrow' fund money. *Message:* "Illegal early access -- taxed at marginal rates plus penalties, trustee disqualification, potential fund non-compliance (45% on assets), and promoter penalties. Refuse and warn; compassionate release runs through the ATO only."
- **R-AU-SF-6 -- Wind-ups** -- *Trigger:* asked to wind up a fund. *Message:* "Wind-up sequencing (benefit payments/rollovers, final audit, final SAR with levy adjustment, deregistration) is judgment work with irreversible steps. Escalate to a qualified practitioner."
- **R-AU-SF-7 -- Death benefit disputes / BDBNs** -- *Trigger:* death benefit payment directions, binding death benefit nomination validity, or competing claims. *Message:* "Legal advice. Escalate to an estate/superannuation lawyer."

## Filing and payment

### Section 8 -- Compliance calendar (2025-26 SAR season, 2026-27 year)

**Compliance calendar**

| Date | Obligation |
| --- | --- |
| 28 July / 28 October / 28 January / 28 April | Ordinary TBAR events for the preceding quarter. Excess-determination voluntary commutations and authority responses use the section 6.2 deadlines. [ATO TBAR](https://www.ato.gov.au/api/public/content/0-42064e26-5e71-4fce-8ca5-a244fc3c6d69). |
| At least 45 days before SAR due | Appoint the ASIC-registered approved SMSF auditor. [ATO appointment requirement](https://www.ato.gov.au/api/public/content/0-42064e26-5e71-4fce-8ca5-a244fc3c6d69). |
| Before lodgment | Audit finalised. Auditor provides the IAR within 28 days of receiving all relevant documents; trustees provide requested information within 14 days of a written request. Obtain any required actuarial certificate before the SAR. [ATO auditor reporting requirements](https://www.ato.gov.au/api/public/content/0-187b178f-76e3-4e8a-9900-70be06e9f1a4) and [ITAA 1997 s 295-390](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_6/document_6.html). |
| 31 October 2026 | 2025-26 SAR: newly registered or overdue self-lodgers, excluding deferrals; payment 1 December. Also check the agent program for prior outstanding returns, prosecution or an advised early date; reviewed new registrants use the ATO-notified date. [ATO self-lodger rule](https://www.ato.gov.au/api/public/content/0-42064e26-5e71-4fce-8ca5-a244fc3c6d69) and [agent categories](https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/prepare-and-lodge/registered-agent-lodgment-program/due-dates-by-obligation-type/super-lodgment). |
| 28 February 2027 | 2025-26 SAR: other self-lodgers unless advised otherwise; newly registered funds using an agent and first agent lodgment after RNN unless an earlier date applies. Payment, if required, is also due. [ATO self-lodger/first-return rules](https://www.ato.gov.au/api/public/content/0-42064e26-5e71-4fce-8ca5-a244fc3c6d69) and [agent program](https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/prepare-and-lodge/registered-agent-lodgment-program/due-dates-by-obligation-type/super-lodgment). |
| 31 January / 28 February 2027 | Agent program: taxable large/medium funds generally lodge 31 January, with payment 1 December 2026; non-taxable large/medium funds and relevant new registrants lodge 28 February. Confirm classification and any earlier requirement. [ATO agent program](https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/prepare-and-lodge/registered-agent-lodgment-program/due-dates-by-obligation-type/super-lodgment). |
| 31 March 2027 | Agent program: funds with total income above $2m in the latest year lodged, excluding large/medium taxpayers; lodge and pay if required. [ATO agent program](https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/prepare-and-lodge/registered-agent-lodgment-program/due-dates-by-obligation-type/super-lodgment). |
| 15 May / 5 June 2027 | Agent program: 15 May applies if not required earlier and not eligible for the 5 June concession. The concession is limited to eligible 15 May funds with a non-taxable/refund latest lodged return and non-taxable/refund current return; it excludes large/medium funds and earlier dates. [ATO agent program](https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/prepare-and-lodge/registered-agent-lodgment-program/due-dates-by-obligation-type/super-lodgment). |
| With the SAR | Supervisory levy $259 in advance. For a continuing new fund add $259, totalling $518. The approved 2026 SAR uses label L for the $259 levy, N for the new-fund adjustment and M for wind-ups; an existing fund with the current-year levy already paid generally owes nil, while a newly registered winding-up fund owes $259. These labels and the 4 cases are verified in [2026 instructions, table 9](https://www.ato.gov.au/forms-and-instructions/self-managed-superannuation-fund-annual-return-2026-instructions/instructions-to-complete-your-smsf-annual-return-2026/section-d-income-tax-calculation-statement-item-13). Confirm the 2026-27 form before filing that year’s return. [ATO levy and SAR adjustment rules](https://www.ato.gov.au/api/public/content/0-42064e26-5e71-4fce-8ca5-a244fc3c6d69) and [levy examples](https://www.ato.gov.au/api/public/content/0-7bc41a06-65a9-4e45-a959-165424670af5). |
| 30 June 2027 | Minimum pensions PAID OUT of the bank; market valuations; in-house asset 5% test; TSB snapshots for caps, DSFA and Div 296 |

These are the program's base dates. If a due date falls on a weekend or public holiday, lodge or pay on the next business day; verify the applicable date and any ATO-notified deferral before acting. A fund without assets in its first registered year must request cancellation or RNN treatment under the ATO conditions, rather than lodge a zero-asset return. [ATO SAR, when to lodge and funds without assets](https://www.ato.gov.au/api/public/content/0-42064e26-5e71-4fce-8ca5-a244fc3c6d69).

If the SAR is more than 2 weeks overdue, Super Fund Lookup status may change to 'regulation details removed', restricting contributions and rollovers. Confirm the actual status and catch-up requirements. [ATO SAR, failure to lodge](https://www.ato.gov.au/api/public/content/0-42064e26-5e71-4fce-8ca5-a244fc3c6d69).

## Completion checklist

- NEVER give investment, product or contribution-strategy advice (R-AU-SF-1 -- AFSL boundary)
- Flag Division 293 and Division 296 member liabilities for review. Complete the separate Division 296 fund reporting work in section 5.3.
- NEVER claim ECPI without checking method eligibility, minimum payments, and (proportionate) the actuarial certificate
- NEVER apply the individuals' 50% CGT discount to a fund (1/3 only)
- NEVER treat NALI as 15% income, or net capital losses against segregated-asset gains
- NEVER accept a related-party transaction value without qualified market evidence
- NEVER classify a payment to a member as a benefit without a documented condition of release
- NEVER assume the general $2.1m TBC applies to a member -- personal caps differ
- NEVER lodge (or treat as lodgeable) a SAR before the audit is finalised
- NEVER present figures as definitive

### References by topic

**Provenance**

| Topic | Source |
| --- | --- |
| Fund definition, trustee rules | SIS Act s 17A, s 17B, s 120 (disqualified persons), s 104A (trustee declaration) |
| Sole purpose; lending; acquisitions; borrowing; in-house assets | SIS Act ss 62, 65, 66, 67, 67A-67B, Part 8 (ss 71, 82-85); penalties s 166 ($364/penalty unit from 1 July 2026, Crimes Act s 4AA) |
| Audit and SAR | SIS Act ss 35C, 35D; ato.gov.au "Your SMSF auditor" (45-day appointment); "Lodge SMSF annual returns" (QC 23331) |
| Supervisory levy amount and advance mechanics | ato.gov.au "SMSF supervisory levy" (QC 35359); SAR 2026 instructions label L ($259) |
| Fund tax, contributions, no-TFN, CGT discount | ITAA 1997 Div 295 (s 295-160 assessable contributions); ato.gov.au "How SMSFs are taxed" (QC 23341) |
| ECPI methods, DSFA $1.6m trigger | ITAA 1997 ss 295-385, 295-387, 295-390; ato.gov.au "Exempt current pension income" (QC 21546); TD 2014/7 |
| NALI/NALE 2x general-expense design | ITAA 1997 s 295-550 as amended by Treasury Laws Amendment (Support for Small Business and Charities and Other Measures) Act 2024; LCR 2021/2; PCG 2020/5 (transition ended 30 June 2023) |
| Contribution acceptance, caps, downsizer | SIS Reg 7.04; ITAA 1997 Divs 290-293 (ss 290-150, 290-165), Subdivs 291/292, s 292-102; ato.gov.au contribution caps pages |
| Division 296 | [Enabling Act, Schedule 1](https://www.legislation.gov.au/C2026A00008/asmade/2026-03-13/text/original/epub/OEBPS/document_1/document_1.html) and [regulation 296-65.03](https://www.legislation.gov.au/F2021L00206/2026-06-27/2026-06-27/text/original/epub/OEBPS/document_1/document_1.html), read 2026-11-10. Schedule 1 item 91 of the enabling Act sets the reporting requirement. |
| Pension minimums and shortfall exception | SIS Reg 1.06(9A), Sch 7; ato.gov.au "Income stream (pension) rules and payments" + "Exception to minimum pension payment requirements" |
| TBC / TBAR | ITAA 1997 Div 294; ato.gov.au "When to lodge a transfer balance account report for SMSFs" (quarterly, 28 days) |
| LRBA legal scope and safe harbour | [SIS Act ss 67-67B](https://www.legislation.gov.au/C2004A04633/2026-08-10/2026-08-10/text/original/epub/OEBPS/document_1/document_1.html); [Schedule 5 transition](https://www.legislation.gov.au/C2026A00049/asmade/2026-06-26/text/1/epub/OEBPS/document_1/document_1.html); [PCG 2016/5 tables 1-2](https://www.ato.gov.au/law/view/document?docid=COG/PCG20165/NAT/ATO/00001&PiT=20261019000001) and [ATO table 28](https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds/other-super-rates-and-thresholds). Annual variable benchmarks and fixed/remaining-term conditions differ. |
| Valuations; investment strategy; separation | SIS Regs 8.02B, 4.09, 4.09A; ato.gov.au "Guide to valuing SMSF assets" |
| Deductions (audit, actuarial, levy) | TR 93/17 |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, tax agent, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

> Contributed by Ryan Duguid.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Income Tax Rates Act 1986, ss 26 and 29. Read low-tax/non-arm's-length components, non-complying rate and no-TFN rate formula. | https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html | 2026-11-12 |
| ITAA 1997, ss 295-160, 295-190, 295-320, 295-325, 295-385, 295-390 and 295-545 to 295-680. Read tax bases, ECPI, status-change inclusion, no-TFN exceptions and preceding-income-year offset. | https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_6/document_6.html | 2026-11-12 |
| ITAA 1997, s 290-170. Read the valid acknowledged notice required for deductible personal contributions. | https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_6/document_6.html | 2026-11-12 |
| ITAA 1997, ss 102-5 and 115-10 to 115-100. Read losses-first, CGT discount eligibility and the complying-super one-third discount. | https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html | 2026-11-12 |
| ITAA 1997, s 67-23 table item 15. Read the refundable no-TFN offset treatment. | https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html | 2026-11-12 |
| SIS Act, s 17A. Read single-member conditions, legal personal representatives, temporary relief and exclusions. | https://www.legislation.gov.au/C2004A04633/2026-08-10/2026-08-10/text/original/epub/OEBPS/document_1/document_1.html | 2026-11-12 |
| ATO trustee-structure comparison, asset ownership and trustee/director changes. | https://smallbusiness.taxsuperandyou.gov.au/setting-up-a-self-managed-super-fund-smsf/how-the-smsf-structures-compare | 2026-11-12 |
| SIS Regulations, reg 7.04(2) and (4). Read PPL exception, inconsistent receipts, 30-day return and TFN quotation exception. | https://www.legislation.gov.au/F1996B00580/2026-07-01/2026-07-01/text/1/epub/OEBPS/document_1/document_1.html | 2026-11-12 |
| ATO SMSF administration PDF, Lodge SMSF annual returns (updated 24 August 2026) and When to lodge a TBAR (updated 2 April 2025). Read self/agent dates, payment, weekends, quarterly reporting and earlier excess-balance exceptions. | https://www.ato.gov.au/api/public/content/0-42064e26-5e71-4fce-8ca5-a244fc3c6d69 | 2026-11-12 |
| ATO 2026-27 super lodgment program, updated 1 July 2026. Read earlier fund categories and the conditional 5 June concession. | https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/prepare-and-lodge/registered-agent-lodgment-program/due-dates-by-obligation-type/super-lodgment | 2026-11-12 |
| ATO approved-auditor responsibilities. Read 28 days after all documents, trustee written-request response and pre-lodgment audit. | https://www.ato.gov.au/api/public/content/0-187b178f-76e3-4e8a-9900-70be06e9f1a4 | 2026-11-12 |
| ATO supervisory levy, continuing and winding-up funds. Read $259 in advance, new-fund $518 and winding-up adjustments. | https://www.ato.gov.au/api/public/content/0-7bc41a06-65a9-4e45-a959-165424670af5 | 2026-11-12 |
| SIS Act current compilation 131, ss 66, 67 and 67A. Read the real-property borrowing restriction alongside the amending transition. | https://www.legislation.gov.au/C2004A04633/2026-08-10/2026-08-10/text/original/epub/OEBPS/document_1/document_1.html | 2026-11-12 |
| SIS Act current compilation 131, ss 166, 168 and 169. Read listed administrative penalties, fund-payment prohibition and corporate-director liability. | https://www.legislation.gov.au/C2004A04633/2026-08-10/2026-08-10/text/original/epub/OEBPS/document_2/document_2.html | 2026-11-12 |
| Treasury Laws Amendment (Tax Reform No. 1) Act 2026, commencement table and Schedule 5 items 1-2. Read 10 August commencement, new arrangements and both pre-commencement savings. | https://www.legislation.gov.au/C2026A00049/asmade/2026-06-26/text/1/epub/OEBPS/document_1/document_1.html | 2026-11-12 |
| PCG 2016/5, 19 October 2026 version, paragraphs 1-9, tables 1-2 and footnote 1. Read legal scope, arm's-length evidence, variable/fixed rates, LVR and remaining loan terms. | https://www.ato.gov.au/law/view/document?docid=COG/PCG20165/NAT/ATO/00001&PiT=20261019000001 | 2026-11-12 |
| ATO other super rates, table 28. Read published 2025-26 and 2026-27 LRBA rates. | https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds/other-super-rates-and-thresholds | 2026-11-12 |
| ASIC 2026 fee dataset, YEARFEE and A52/A53/A58/I02; special purpose page, trustee constitution, sole purpose and status notification. | https://download.asic.gov.au/asic-nga/data/fees-data-current.json | 2026-11-12 |
| ASIC special purpose companies, superannuation trustee companies, governance and fees. Read eligibility and notification before annual review. | https://www.asic.gov.au/for-business-and-companies/companies/register-a-company/special-purpose-companies | 2026-11-12 |
| Crimes (Amount of a Penalty Unit) Instrument 2026, ss 2 and 5. Read commencement, $364 and offences from 1 July 2026. | https://www.legislation.gov.au/F2026N00424/asmade/2026-06-16/text/original/pdf | 2026-11-12 |
| ATO contributions caps. Read 2026-27 general caps, carry-forward conditions and TSB restriction. | https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds/contributions-caps | 2026-11-12 |
| ATO transfer balance cap, table 26. Read the general caps for 2025-26 and 2026-27. | https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds/transfer-balance-cap | 2026-11-12 |
| ITAA 1997, ss 291-20, 292-85 and 294-35 to 294-40. Read carry-forward, bring-forward, prior-year TSB and personal TBC conditions. | https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_6/document_6.html | 2026-11-12 |
| SIS Regulations 1994, Schedule 7 clauses 1 and 3-5 and the age-factor table. Read for the higher withdrawal benefit, age/date, proration, June exception, ended reductions and rounding. | https://www.legislation.gov.au/F1996B00580/2026-07-01/2026-07-01/text/1/epub/OEBPS/document_2/document_2.html | 2026-11-12 |
| SIS Regulations 1994, regulation 1.06(9A)(a). Read for account-based pension payments and the link to Schedule 7 clause 1. | https://www.legislation.gov.au/F1996B00580/2026-07-01/2026-07-01/text/1/epub/OEBPS/document_1/document_1.html | 2026-11-12 |
| ITAA 1997, s 293-20. Read for the Division 293 taxable contributions calculation. | https://www.legislation.gov.au/C2026C00471/latest/text | 2026-11-10 |
| Superannuation (Sustaining the Superannuation Contribution Concession) Imposition Act 2013, s 5. Read for the Division 293 tax rate. | https://www.legislation.gov.au/C2013A00087/asmade | 2026-11-10 |
| ITAA 1997, ss 296-40, 296-45 and 296-60 to 296-70. Read for the Division 296 balance, earnings and attribution rules. | https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_6/document_6.html | 2026-11-10 |
| Division 296 enabling Act, Schedule 1. Read ss 296-15 to 296-25 and 296-260 for the member exceptions and LRBA adjustment, and item 91 for the reporting requirement. | https://www.legislation.gov.au/C2026A00008/asmade/2026-03-13/text/original/epub/OEBPS/document_1/document_1.html | 2026-11-11 |
| Taxation Administration Act 1953, Schedule 1 s 390-5. Read for the approved form and relevant earnings by reportable interest. | https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html | 2026-11-11 |
| Income Tax (Transitional Provisions) Act 1997, ss 296-1, 296-50 and 296-55. Read for the first-year balance, transitional CGT choice and event-related record retention. | https://www.legislation.gov.au/C2004A05128/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html | 2026-11-12 |
| ATO’s 24 September 2026 SMSF notice, complete 3-page official print PDF. Read the annual return channel, transitional CGT election deadline and forthcoming-form qualification. | https://www.ato.gov.au/api/public/content/0-a41dabd1-939c-489a-8fb7-72d6988aa65d | 2026-11-12 |
| ATO SMSF Division 296 administration guidance. Read that the election need not be provided to the ATO, its scope and the required records and retention trigger. | https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/self-managed-super-funds-smsf/smsf-administration-and-reporting/about-division-296-tax-for-smsfs | 2026-11-12 |
| ATO approved 2026 SAR, NAT 71226-06.2026, and Section D instructions, table 9. Read labels L/M/N and all 4 levy cases for 2025-26 returns; these do not verify the 2026-27 form. | https://www.ato.gov.au/forms-and-instructions/self-managed-superannuation-fund-annual-return-2026-instructions/instructions-to-complete-your-smsf-annual-return-2026/section-d-income-tax-calculation-statement-item-13 | 2026-11-12 |
| Income Tax Assessment (1997 Act) Regulations 2021, reg 296-65.03. Read for small-fund attribution and actuarial certificate exceptions. | https://www.legislation.gov.au/F2021L00206/2026-06-27/2026-06-27/text/original/epub/OEBPS/document_1/document_1.html | 2026-11-10 |
| Superannuation Guarantee (Administration) Act 1992, s 18C. Read for the ordinary contribution deadline and exceptions. | https://www.legislation.gov.au/C2004A04402/2026-07-01/2026-07-01/text/original/pdf | 2026-11-10 |

The 2026-27 SMSF annual return labels and instructions, the final approved transitional CGT choice form and current source links and read dates for the remaining rows are not yet confirmed.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-12. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `au-smsf` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/au-smsf. If neither is available, confirm every figure against the official source pages cited above before relying on it.
