---
name: pk-return-assembly
description: Use for pakistan annual return assembly and reconciliation. Read the stated period, eligibility conditions, evidence requirements, owner skills and unresolved boundaries before calculating or preparing a return.
version: 1.1
jurisdiction: PK
tax_year: 2026
last_updated: 2026-11-14
depends_on:
  - pk-freelance-intake
category: orchestrator
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: router
---

# Pakistan annual return assembly and reconciliation v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Capstone for an annual Pakistan individual/AOP or resident-company reviewer package, using `pk-freelance-intake` and applicable computation skills. Normal tax year 2026 is 1 July 2025 through 30 June 2026; approved special years require their own dates under s.74. Read available upstream work and produce the complete supported package without re-asking whether it is wanted. Do not submit to IRIS, execute payments or sign a professional attestation. [ITO ss.74,114,116,118](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).

Quick answer: reconcile the supported computations, credits, wealth and payment records, identify every unresolved item, and prepare the workbook, reviewer brief and taxpayer action list. A failed check does not erase supported work, but an unresolved material error prevents a filing-ready sign-off. No rates are made current merely by assembling an upstream output.

## Ask the client first

Read the intake, every available upstream schedule and source record first. Reconcile disagreements; ask only facts missing from those records. Capture taxpayer/entity/registration, business address, principal activity, authorised representative identity/NIC, period/residence, applicable forms, actual payments/withholding, income/assets/liabilities and supporting accounts. Record IRIS access status; do not put credentials in the working paper. Missing identifiers get visible placeholders while reconstruction continues, and prevent final submission readiness where required.

## The method, step by step

### Phase 1: scope and upstream manifest

Record each skill's version, tax year, source-check/review status, output and open items. Do not blindly trust an approved but stale sibling or an unreviewed new draft. Individual/AOP returns are under s.114; resident-individual wealth/reconciliation is s.116. Its first proviso also requires every AOP member's wealth/reconciliation statements with the AOP's income return; these statements are distinct from that s.114 return and from the five income heads. Companies have a separate return and accounts analysis. Test company residence under s.83: incorporation/formation under Pakistan law; control and management situated wholly in Pakistan at any time in the year; or the provincial/local-government branch. Do not substitute the AOP’s wholly-or-partly test. [ss.11,83,114,116](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).

| Upstream owner | Consume and reconcile |
|---|---|
| `pk-income-tax` / `pk-it-export-tax` | Salary/property/business/other-source income, ordinary/separate/final classification, table tax, surcharge/credits; export finality and domestic split |
| `pk-corporate-tax` | Book-to-tax adjustments, applicable company rate, depreciation/initial allowance/WDV/losses, minimum/ACT/super-tax calculations and accounts evidence; confirm current source law before reliance |
| `pk-withholding-tax` | Suffered tax and each agent obligation, section, recipient, base, rate, nature, certificate, PSID/CPR and actual payment |
| `pk-sales-tax-federal` / `pk-sales-tax-services` | Goods/services turnover, tax-exclusive revenue, timing, output/input, exemption/export and authority-specific returns; cross-check without merging their liabilities into income tax |
| `pk-payroll-eobi` / `pk-payroll` / `pk-social-contributions` | Salary cost, employee withholding, employer/employee contributions, coverage/bases and distinct statements/remittances |
| `pk-cgt` / `pk-crypto-tax` | Securities/property/other disposal schedules, acquisition/holding/ATL/certificates, unresolved virtual-asset classification |
| `pk-formation` / `pk-financial-statements` / `pk-bookkeeping` | Legal form/CUIN/directors/AOP shares/registrations, accounts/framework/audit/filing, bank/asset/expense records |

### Phase 2: income and accounts

Reconcile the 5 statutory heads: Salary, Property, Business, Capital Gains, Other Sources; foreign income belongs within its head. For companies retain revenue/costs, adjustments, depreciation, initial allowance, losses and gains with source-law references. Tie bank/platform gross receipts to ledger revenue, distinguishing sales tax, transfers, refunds and timing. Final-tax streams stay separately identified and cannot be silently added to ordinary income or omitted from the financial/wealth reconciliation. [ITO ss.11,114,116](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).

### Phase 3: tax and legal classification

Consume the actual owner computations, separately identifying ordinary tax, s.4AB surcharge, s.4C super tax, s.113 minimum tax and company s.113C ACT. Do not invent a universal higher-of formula that combines different statutory bases. Keep dividends/debt/exports and other separate, minimum, final or adjustable regimes under their own conditions. Section 154 goods exports must not automatically inherit section 154 A services finality. Donation/pension/foreign credits have separate requirements; the old statement that the pension credit was largely repealed is not relied on. [ITO ss.4,61,63,103,113,147,154 A,168](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).

### Phase 4: credits and payments

Create a taxpayer/section/period/payment register. Reconcile actual s.147 advances and legally adjustable s.168 withholding to CPR/certificates and upstream amounts; distinguish tax withheld by this employer from tax suffered by this taxpayer. Mark each credit's statutory nature before subtraction. Section 4(3) orders foreign, Part X and then ss.147/168 credits; no double credit of final tax or employer remittances. A negative arithmetic balance is a potential refund subject to the legal rules and s.170 process, not a promised immediate payment. [ss.4(3),103,147,168,170](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).

### Phase 5: all cross-skill reconciliations

Preserve the original checks, with evidence, result and unresolved delta:

1. Revenue: ledger/P&L versus federal/provincial monthly turnover, bank receipts and timing/tax-exclusive adjustments.
2. Salary/EOBI: gross salary to accounts, employee withholding to payroll and quarterly statements, distinct employer contributions to actual payments, employee certificates to their own income schedules.
3. Agent withholding: deductions by section to deposited CPRs and statements; deducted-not-deposited, deposited-not-reported and reported-not-deducted differences stay explicit.
4. Advance tax: each quarter's actual payment to its legal schedule/formula, not the old single individual calendar for every company/AOP or a rough turnover estimate.
5. Gains: securities/property/other categories and certificates to the return; seller's 236 C and buyer's 236 K must not be interchanged.
6. Regime classification: ordinary/separate/final/minimum and adjustable payments consistently treated across income, tax and credit schedules.
7. Wealth: for every required individual and AOP-member statement, opening net assets plus supported taxable/exempt/final income and capital receipts, less supported outflows/expenses/tax, reconciled to closing net assets, avoiding double-counted gifts/transfers.
8. Review tolerances: the old PKR 100 individual and PKR 1,000 company tolerances are internal reconciliation flags, **not tax-law exemptions**. Show every difference. Above PKR 10,000 use Needs Input before sign-off; smaller material/classification errors also require resolution. Never round or plug an s.111 issue. [Wealth duties ss.111,116](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).

### Phase 6: payment and filing action register

For each liability record authority, taxpayer, tax head/section, actual year/period, amount, due date and source, status, PSID and CPR. Federal income/sales tax, provincial services tax and EOBI/ESSI have separate channels; the old suggestion every payment uses IRIS is wrong. A PSID is a payment instruction, a CPR records payment, and an IRIS acknowledgement records filing. Do not promise a universal PSID validity or auto-feed delay; inspect actual records.

The taxpayer/authorised filer generates the correct payment instruction, pays the applicable channel, verifies the CPR against taxpayer/head/period/amount, checks prefilled return data against this paper, completes the applicable income/credit/separate-tax schedules and required accounts/individual and AOP-member wealth/foreign-asset attachments, resolves validation errors and retains the submission acknowledgement. Current menu/box/form identifiers must be checked, not guessed from historic annex letters.

### Phase 7: assemble the deliverables

Produce these 3 files in the task's authorised output directory, with working formulas and links to source evidence:

- `[taxpayer_slug]_TY2026_pk_master.xlsx`: Cover/sign-off, Identification, Income, Tax/charges, Adjustable Tax, Advances, Credits, Wealth/Wealth Reconciliation, Gains, company Depreciation/WDV, Salary, Sales Tax Cross-check, Payment Register, Cross-Check Summary and next-year Planning sheets.
- `reviewer_brief.md`: executive tax/payment result, computation walk-through, legal positions/sources, each check/delta, assumptions/defaults, missing computations, source period/version risks and blank attestation.
- `taxpayer_action_list.md`: immediate filing/payment/evidence tasks with actual due-date source and responsible person, ongoing payroll/withholding/sales-tax/EOBI/ESSI calendar, advance-tax plan, ATL follow-up and retention.

If an output is incomplete, label the specific file/schedule partial. Do not let context exhaustion or missing upstream data turn a partial computation into a completed return.

## Filing and payment

| Obligation | Ordinary legal rule, subject to actual extension/special status | Source |
|---|---|---|
| Individual/AOP annual return | 30 September after year-end; tax-year 2026 ordinary date 30 September 2026 (derived), extension must be checked | [s.118(3)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Company tax year ending January-June | 31 December next following tax-year-end; June 2026 gives 31 December 2026 (derived) | [s.118(2)(a)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Other company tax-year end | 30 September next following year-end; no universal 6-month rule | [s.118(2)(b)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Resident individual's and AOP-member wealth/reconciliation | Resident individual with own return; every AOP member also with the AOP's income return; notice cases by notice date | [ss.116,118(4)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Return-balance payment | By return due date; actual filing/payment records reconciled separately | [s.137(1)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Quarterly withholding statements | Quarters ending March/June/September/December:20 April/20 July/20 October/20 January, subject to any applicable later law/notice | [s.165(2)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Individual advances | 15 September,15 December,15 March,15 June; individual formula/exclusions apply | [s.147(4 B)-(5)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| AOP/company advances | 25 September,25 December,25 March,15 June; separate turnover/estimate provisions apply | [s.147(4),(5 A)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Income-tax records | 6 years from tax-year-end (in words on the page), pending proceedings until final decision and s.111(2)(ii) limitation exception | [s.174(3)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |

Extension under s.119 is an application with statutory conditions, not an assumed 15-30-day entitlement. Annual accounts, federal/provincial sales-tax payment and filing, withholding deposits, contribution and certificate deadlines come from their specific owner/source; do not reuse the old universal 7th/15th/18th/30-day calendar. A later filing extension may not postpone all payment consequences. Do not state a penalty without the law applicable to the default date.

For next-year planning, use tax year 2027's operative law and current evidence. Preserve the advance-tax, withholding-agent, sales-tax, sector and ATL planning jobs without copying prior-year numerical tables. Capture event-date ATL, prior compliance and current late-entry requirements; no guaranteed weekly refresh, March-to-February period or retrospective rate/refund promise is given.

## Worked cases

Inputs are example amounts from hypothetical supported upstream outputs; no legal rate is invented here. These are reconciliation/completion tests, not replacement tax computations.

```oa-check
name: Adjustable payments reconciled to tax liability
inputs:
  supported_tax_liability: 300000
  supported_adjustable_withholding: 180000
  supported_advances: 90000
  recorded_balance: 30000
steps:
  - computed_balance: supported_tax_liability - supported_adjustable_withholding - supported_advances
  - difference: recorded_balance - computed_balance
expected:
  computed_balance: 30000
  difference: 0
```

```oa-check
name: Wealth reconciliation leaves material unexplained gap
inputs:
  opening_net_assets: 1000000
  supported_income: 800000
  supported_gift: 100000
  personal_outflows: 500000
  tax_paid: 100000
  reported_closing_net_assets: 1350000
steps:
  - supported_closing: opening_net_assets + supported_income + supported_gift - personal_outflows - tax_paid
  - unexplained_difference: reported_closing_net_assets - supported_closing
expected:
  supported_closing: 1300000
  unexplained_difference: 50000
```

The 50,000 difference exceeds the internal 10,000 escalation flag and needs evidence before sign-off. Do not fabricate income, gift or expense to balance it.

## When to refuse or refer

Preserve R-PK-ASM-1 through 8: missing upstream output (name it and continue supported work); failed upstream check (specific flag); material unreconciled delta; specialist regimes; non-residence/mixed-residence/expatriate packages; incomplete intake (placeholder but no final readiness); request to submit (authorised filer after professional review); and unsupported rates (return to the owner/source).

Specialist regimes remain petroleum/oil/gas concessions, insurance, banking, modarabas, mutual funds, group taxation ss.59AA/59 B, CFC s.109A, transfer-pricing/local/master/CbCR files, Second Schedule holidays, special zones including Gwadar and KP zones, provincial agricultural tax and other provincial taxes, capital value tax, WWF and WPPF. Refer these; do not silently compute them or imply the pack fully covers them. PDF/XML return generation and ERP integration remain outside the assembly output. The practitioner/taxpayer supplies required audit attachments; this workflow does not create an auditor's opinion.

A blank reviewer attestation must state name, professional body/membership number/practising status, review date, schedules/evidence reviewed, unresolved matters, and sign-off. It covers income/charges, credits/CPRs, sales-tax/payroll/gains/entity/wealth cross-checks, citations, deadlines and ATL follow-up. Do not prefill a confirmation that a return is ready. Appropriate local professional review remains distinct from AI source checking. Verify the practitioner’s actual Pakistan practising/representation authority; an ICAP, ICMAP or ACCA membership label alone is not that authority.

## Completion checklist

Preserve all original completion tests: upstream manifest/gaps; revenue; actual credit/payment totals; advances; payroll/contributions; company book-to-tax adjustments; gains split; tax nature; wealth; super/surcharge; minimum/ACT; actual ATL implication; sourced date; retention exceptions; every legal position's source; acknowledgements; required professional sign-off; and unconfirmed payment/screen labels. Record any failed test in the brief and action list. Deliver the supported package while keeping filing readiness unresolved until material gaps are cleared.


### Current late-entry ATL route, November 2026

Current s.182A surcharge amounts are company 100,000/AOP 50,000/individual 25,000; these are current-action amounts, not the historical 20,000/10,000/1,000 table. For a late individual, r 81 B(2 B)-(2D) now allows IRIS **Form ATL-U** undertaking instead of the surcharge: the 6-month period starts from successful IRIS acknowledgment, with an undertaking not to purchase, acquire or otherwise obtain ownership or a beneficial interest in any property during that period. An established breach after electronic hearing withdraws the benefit from the breach date and ordinary rules then govern. Do not promise this route to an AOP/company or describe filing alone as automatic fee-free entry. Dated event status and actual charge conditions still control withholding. [Current ITO s.182A](https://download1.fbr.gov.pk/Docs/2026724177725705IncomeTaxOrdinanace2001.pdf); [signed 10 November 2026 SRO 2097](https://download1.fbr.gov.pk/SROs/202611101511326308SRO2097of2026.pdf), read 2026-11-14 for the operative rule/form.

For the actual tax-year-2026 filing cycle, FBR Circular 04 of 2026-27 dated 15 October 2026 extends the filing date to **31 October 2026** for persons originally due 30 September 2026 and previously extended to 15 October. It does not extend every company return. Apply any individual further order only on its evidence; this circular does not itself state a general payment extension. [Official circular](https://download1.fbr.gov.pk/Docs/20261015221039470Extension.pdf), read and scanned page inspected 2026-11-14.

## Sources

| Source and actual portions read | Official URL | Read on |
|---|---|---|
| Read for Circular 04 of 2026-27, 15 October 2026, the 31 October extension for the original 30 September cohort; scanned signed page inspected | https://download1.fbr.gov.pk/Docs/20261015221039470Extension.pdf | 2026-11-14 |
| Read for ITO ss.4,11,71/74,82/84,92,103,111,114/116,118/119,137,147,154 A,165/168/170,174 and relevant ordinary deadlines/retention/credit-order provisions | https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf | 2026-11-14 |

Not yet confirmed: exact current NPO/simplified return identifiers, manual-paper exceptions, electronic-record/location/accessibility permissions and requirements, foreign-income/asset attachment triggers and identifiers, any further case-specific tax-year-2026 extension beyond Circular 04, current IRIS screens/box identifiers and PSID heads/validity, case-specific ATL event/refresh dates and transaction rates, later default-date penalties, exact provincial/contribution calendars and all special-regime computations. Historical super-tax/banking/dividend/export/minimum/ACT rate tables are not repeated as current law here; their named owners must provide operative-source computations. No universal 6-month company deadline, quarterly 30-day statement deadline,7th-of-month withholding deposit or automatic ATL activation promise survives as usable guidance.
