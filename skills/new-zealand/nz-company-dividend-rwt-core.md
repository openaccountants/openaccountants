---
name: nz-company-dividend-rwt-core
description: "Use for selected New Zealand company cash dividends to resident shareholders in 2026-27. Trigger on dividend RWT, attached imputation credits, gross versus net dividend, benchmark ratios, dividend information or shareholder statements. Covers the ordinary cash formula, exact attachment ceiling, monthly reporting and remittance, statement triggers and record clocks. Requires confirmed company and recipient status, valid credits, payment character and applicable exclusions. Keeps fractional-cent amounts, special regimes and incomplete corporate work held. Supplies synthetic controls and working-paper requirements for qualified review. It cannot authorise a distribution, complete an IR4 or ICA return, file information or make a payment."
jurisdiction: NZ
category: international
tier: 2
review_status: pending_review
tax_year: 2027
tax_year_notes: "Selected 2026-27 payment rules, checked 14 November 2026. Establish actual payment/income periods. No 2027 annual IR4/IR4J return or future-law assurance."
last_updated: 2026-11-14
version: 0.1
depends_on:
  - workflow-base
  - corporate-income-tax-workflow-base
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# New Zealand company cash dividends and RWT v0.1

## Scope and source period

This selected corporate companion addresses an ordinary domestic New Zealand resident company paying a cash dividend in NZD to an established New Zealand resident shareholder. Establish the legal dividend, payer, recipient capacity, source, dates, ICA status, valid attached credits and relevant exclusions before computing. Incorporation, an accounts label or a shareholder address does not establish the tax result. Separate professional clearance of distribution authority, share rights and solvency is required; this guide supplies no company-law approval.

Load workflow-base and corporate-income-tax-workflow-base. Retain their intake, inferred and confirmed profile, source/period gates, refusal catalogues, substantive order, ambiguity checkpoint, required outputs and checks. Payer withholding is separate from its own company income-tax charge and the shareholder's final tax. If the request includes a complete company computation or IR4, keep that scope and obtain complete period-appropriate country companions. The existing nz-company-income-tax-ir4 covers 2025-26; it is not a verified 2027 return companion.

The selected Income Tax Act consolidation is dated **4 September 2026** and the Tax Administration Act consolidation **1 October 2026**, checked on **14 November 2026**. Their warning lists contain 13 and 6 instruments respectively, 14 distinct. The retained selected-provision review found no unresolved direct amendment to this ordinary formula, maximum attachment ratio or selected reporting clauses. This is not whole-Act assurance. Recheck later law and the actual payment period. [ITA][A03], [TAA][R01].

The warning review retains special branches: 2023 DRCD changes, 2024 co-operative/top-up-credit provisions, 2025 partnership/custodian changes and the 2026 repeal of CW 39(3)'s exclusion for amounts received in trust are not general ordinary-company permissions. The 2026 Budget family-residence definition change is future and limited; it does not replace the general residence test used here. Named SOE schedule changes, insurance, greyhound, deposit-taker, employment, minimum-family-credit and planning amendments establish no ordinary eligibility. The TAA Gambling amendment concerns confidentiality. Do not describe whole Acts as uncommenced because selected consequential items await commencement. [W01], [W02], [W03], [W04], [W05], [W06], [W07], [W08], [W09], [W10], [W11], [W12], [W13], [W14], [CW 39][P05].

## Period figures and clocks

These selected 2026-27 figures remain conditional on the source scope below. They are not a complete corporate rate or annual-return table.

| Item | Selected figure or rule | Authority/condition |
| --- | --- | --- |
| Ordinary cash-dividend RWT | 33% within RE 13's formula | [RE 13][A03], [Schedule 1 Part D clause 5][A06] |
| Ordinary attachment basis/ceiling | 28%; exact I/D ≤ 28/72 or I/G ≤ 28% | Ordinary company-rate status, valid credits and other attachment conditions required. [OA 18][A11], [OB 60][A04], [Schedule 1 Part A clause 2][A06] |
| Dividend information/remittance | Monthly; nominal 20th of following month | Distinct information and payment duties and special timing/working-day conditions. [TAA 25G][R01], [RE 20][R02], [RE 21][R03], [RA 15][P10] |
| Ordinary section 29 statement | At payment when its RWT-or-imputation trigger applies | [TAA 29][R01] |
| Section 22AAB records | Generally 7 years after payment; its own notified extension up to 3 further years | Liability, record scope and statutory extension grounds required. [TAA][R01] |
| Section 22 business records | Generally at least 7 years after the relevant income-year end | Retain statutory conditions/exceptions and possible notified extension up to 3 further years. [TAA 22][R01] |
| Section 22(2)(k) memorandum-account/attached-credit records | At least 7 years after the relevant tax or income-year end, as applicable | Identify the ICA tax year separately from the company income year; retain statutory conditions/exceptions and possible notified extension. [TAA 22][R01], [OB 1][P08], [ICA year][I05] |
| Reviewer attention floor | NZ$0 | Internal policy in this guide, not a statutory threshold |
| 2027 IR4/annual ICA return dates | Not established here | Obtain a current period-specific companion; do not reuse IR4JG 2026 |

## Engagement and completion gates

Use redacted summaries and stable fictional or reviewer-held references. The professional retains legal identities, tax numbers, addresses, bank details, authentication and signing credentials and performs any submission/payment. Do not query a real exemption register through this guide.

Establish and record:

- Requested obligation, payment and income periods, NZD basis, tax residence, ordinary company-rate and ICA-company status, special/sector/group overlays and any dispute.
- Approved distribution/share rights, cash character, actual declaration, record, derivation and payment dates, shares and recipients. A tax calculation does not establish legal authority.
- Recipient residence/capacity, company/group relationships and any claimed RE 2 exclusion or RE 27 exemption, including applicable changes at payment.
- Dividend before withholding, attached credit, gross amount and net cash. Credit validity/provenance, benchmark history, ratio-change evidence and ICA movements/effective dates.
- Actual RWT account readiness, information/reporting period, current specification, mandatory-field readiness, remittance dates, records and later delivery/payment evidence.

Unknown mandatory facts remain **Needs Input**, with affected computation/output, responsible person and next evidence. This guide authorises no missing-fact default for status, character, exemption, credits, dates, shares or rounding. Unknown is not zero or inapplicable. Ask remaining factual questions at the bases' shared checkpoint; confirmation does not establish unknown law.

### Conservative defaults

| Missing or conflicting item | Permitted treatment |
| --- | --- |
| Residence, entity/regime, dividend character or exclusion | No default. Needs Input; establish the applicable legal/factual scope before computing |
| Credit validity/provenance, ICA or benchmark/change evidence | No zero, maximum-credit or positive-balance assumption. Hold the affected attachment/result |
| D/I, shares, applicable mandatory dates or field mapping | No invented value or aggregate substitute. Obtain/reconcile source evidence |
| Fractional-cent treatment or operative law | No rounding/truncation or higher-tax default. Hold the affected final amount |
| Actual registration, filing, delivery, payment or practitioner sign-off | No completion assumption. Obtain the reviewer's evidence |

These are T3 holds, not authorised T2 defaults. The universal base mentions an excessive-ambiguity refusal beyond 10 grouped factual questions without defining its code/message. If more than 10 grouped factual questions remain and no applicable loaded catalogue supplies both, retain Needs Input for the configuration gap; do not invent a code or continue to a deliverable result.

| Corporate country-slot group | Contribution and remaining requirement |
| --- | --- |
| Regime, authority, form and calendar | Selected dividend duties below; actual status and all IR4/annual ICA calendars need current evidence |
| Rates/overlays | Selected 33% cash-dividend RWT and ordinary 28% attachment basis only; no company income-tax charge, branch, reduced or sector-rate conclusion |
| Adjustments/losses | No complete deduction, exemption, depreciation, interest-limit, continuity or group-relief analysis |
| Credits | Selected payer attachment/withholding bridge; no shareholder credit entitlement, company refund, foreign-credit or incentive determination |
| Filing support/audit | Selected information/statement/record controls; no complete IR4, IR4J, accounts, audit or supporting package |
| Anti-avoidance/cross-border/Pillar Two | No complete local applicability or operative rule set; retain the bases' intake, refusals and specialist companions |

Retain all 4 universal outputs: recalculated Excel working paper, reviewer brief, action list and review checklist. Retain every corporate domain output and supporting component, including return/forms, tax provision, payment schedules and documentation index. This guide alone is an incomplete corporate companion. Missing mandatory source conditions, country slots or outputs prevent a deliverable company financial result or completion claim. A supported dividend schedule may contribute to the eventual package; it cannot certify remaining work.

### Refusals and holds

Run all loaded refusal catalogues before classification/computation. A current tax audit or notice of deficiency fires R-CIT-6; a related-party dividend alone does not establish that trigger. Use each base's canonical code/message verbatim and follow its stop. A reviewer flag cannot override a refusal.

| Code | Trigger | Exact message |
| --- | --- | --- |
| R-NZ-DIV-SPECIAL | Requested result requires unsupported non-cash/combined, foreign, DRCD/dual-resident, special-entity, intermediary or other special dividend treatment | This selected cash-dividend guide cannot compute the requested special treatment. Obtain the applicable current source chain and qualified specialist review before continuing. |
| R-NZ-DIV-INCOMPLETE | Complete company tax, IR4 or ICA result requested whilst mandatory applicable companion content or outputs remain unsupported | This selected dividend schedule is an incomplete corporate companion. Do not deliver a complete company result or mark the workflow complete. Establish every mandatory source condition, country slot and required output first. |

A missing fact or fractional-cent authority gap is Needs Input, not a new refusal code. Hold the affected result. If a loaded refusal fires, follow its full stop and do not produce partial computed work. Record cleared/fired codes and exact messages in the reviewer brief, or the reply when refusal precedes a brief.

The reviewer attention threshold is **NZ$0**: flag every classification, credit, exemption, reporting, date and rounding condition, every non-zero discrepancy including NZ$0.01 and every unquantified impact. This is internal review policy, not statutory materiality or permission to ignore non-monetary defects.

## Classify the payment first

CD 1/CD 3 lead into the dividend rules. CD 4's transfer-of-company-value framework, CD 5's transfer rules and CD 6's shareholding connection need actual facts. [CD 4(1)(b)][A19] requires that none of the CD 22–37 exclusions applies. A capital distribution, shareholder current-account entry, repayment, bonus issue or benefit is not automatically an ordinary cash dividend. The complete exclusion/transaction analysis is not supplied here; hold the affected payment until its source chain is established. [CD 1][A17], [CD 3][A18], [CD 4][A19], [CD 5][P01], [CD 6][P02].

RE 2 includes dividends in resident passive income subject to overrides. Its exclusions include specified exempt equity income, PIE dividends, RE 27-exempt recipients, non-resident passive income, specified non-resident amounts, same-group company dividends and a fully imputed intercompany dividend **where the payer chooses the exclusion**. Other fund, retirement, LTC, trustee and anti-avoidance cases have their own conditions. Fully imputed does not make every dividend RWT-free. Recipient-company status or a general income-tax exemption does not prove a specific RE 2 exclusion. [RE 2][A02], [RE 27][A15], [CW 39][P05], [HA 15][P06].

RE 3 links withholding/payment to RE 4 and RE 5/6 exceptions. RE 4 requires relevant payer and payment conditions and expressly includes a resident payer's dividend. RE 5 requires established exemption conditions. RE 6 concerns specified persons/circumstances, not a general option to ignore uncertainty. Agents, bare trustees, partnerships and custodians need their own supported treatment. [RE 3][A07], [RE 4][A13], [RE 5][A08], [RE 6][A14], [RE 29][A16], [RE 31][P12].

RE 13 addresses dividends other than non-cash dividends, with a specific combined-payment election exception. Non-cash/combined arrangements need the relevant RE 14-series analysis. Foreign-company dividends also have a foreign-tax limb in RE 13. Do not omit those facts and reuse this ordinary domestic computation. [RE 13][A03].

## Ordinary formula and exact denominators

After the scope and credit gates are established:

| Symbol | Meaning |
| --- | --- |
| D | Dividend paid **before RWT is determined**, excluding attached imputation; includes the amount later withheld, not just net cash |
| I | Valid imputation credit attached by the relevant ICA company; no foreign-tax component assumed in this domestic case |
| G | Gross dividend for this bridge: D + I |
| W | RE 13 RWT: 0.33 × (D + I) − I |
| C | Cash remaining after RWT: D − W |

RE 13 refers to Schedule 1 Part D clause 5's **33%** basic rate. CD 15's general imputation gross-up expressly does not apply for Part R, so do not add that credit a second time inside RE 13. G = C + W + I and D = C + W. Do not use G or C as D or reduce gross income by a credit twice. The shareholder's marginal rate and missing-IRD-number interest rule do not replace this dividend rate. [RE 13][A03], [Schedule 1][A06], [CD 15][A12], [IRD rates][D3], [IR284][R04].

For an established ordinary **28%** company-rate basis, OA 18/OB 60 cap I/D at **0.28/0.72**, equivalently I/G ≤ 0.28. Preserve the exact ratio. The upload specification's displayed **38.89%** is an encoding example, not a replacement ceiling. For non-negative D/I, test I × 72 ≤ D × 28 without dividing by zero; D = 0 permits no positive credit under that inequality. A ratio test proves neither that a dividend exists nor that credits are valid. [OA 18][A11], [OB 60][A04], [Schedule 1][A06], [specification][R07].

Within that valid ordinary ceiling W is non-negative; at maximum attachment it is 5% of G. This is an algebraic consequence, not a new rate or exemption. If supplied amounts exceed the ceiling or produce a negative result, stop and reconcile classification, inputs and credit authority. No general max(W, 0) correction is established. [RE 13][A03], [OA 18][A11].

### Fractional cents remain held

The sources do **not** establish a dividend RWT rounding/truncation mode, tie rule or per-payment versus aggregate method. RE 13 supplies the formula. The February 2026 V1.6 specification encodes money as integer cents; a format does not supply a computation rule. A current Part R search located provisional-tax truncation and related GST-ratio rounding provisions, not adopted as dividend authority. [RE 13][A03], [specification][R07], [Part R][PART-R].

Keep exact algebra and source precision. Do not round D, use a rounded ceiling, invent a policy or silently convert fractional W/C into payable/filed cents. Record Needs Input and obtain current primary authority/applicable treatment before finalising affected amounts. Cent-exact examples do not resolve this for other values. An unestablished rule is not a finding that none exists.

## ICA and benchmark gates

Establish ICA-company status under OB 1, attachment rules, credit provenance and transactions/effective dates. An accounts credit or company tax payment alone does not prove a valid attachment. Consolidated/Australian accounts, sector entities, top-up tax and special credit sources need separate analysis. Do not derive shareholder credit entitlement or an ICA refund from payer attachment. [OB 1][P08], [OA 5][P07], [OB 60][A04], [CD 16][P03], [CD 17][P04], [IR274][I08].

OB 61 identifies the benchmark dividend and ratio rules. Reconcile the first relevant dividend and full imputation-year history, including exceptions, before a later attachment. IRD's published ratio-change process requires the declaration before the subsequent differently imputed dividend and a basis for the required no-tax-advantage statement. OB 61(6) also permits a later date if the Commissioner allows; obtain evidence of that permission before relying on it. A draft IR407, late declaration alone or maximum-ratio test does not prove compliance. [OB 61][A05], [benchmark][I01], [ratio change][I04].

Reconcile ICA opening, evidenced credits/debits, effective dates, dividend debit and closing. IR274 distinguishes an in-year debit from year-end consequences; do not invent a blanket positive-balance-at-payment test. That distinction does not validate credits or excuse benchmark, closing or further-income-tax duties. Annual/interim returns and cessation require separate verified periods/application. IR4JG 2026 covers 2025-26; its dates do not establish 2026-27 annual completion. IR274's old section 67 company-statement procedure supplies no current duty: TAA section 67 is repealed. [ICA][I03], [memorandum accounts][I05], [annual return][I06], [interim return][I07], [IR274][I08], [IR4JG 2026][I09], [TAA][R01].

## Registration, monthly information and payment

IRD distinguishes company dividends from the interest threshold: companies paying dividends are automatically registered as RWT payers. Verify actual account readiness; do not import the interest threshold to avoid a dividend duty. Public exemption instructions establish no actual recipient exemption. [Registration][D4], [exemption information][D5].

| Obligation | Selected rule and boundary |
| --- | --- |
| Investment information | Apply TAA 25C scope, 25E(1)(c)'s taxable-company-dividend trigger and 25G. Deliver applicable period information, not cumulative year-to-date figures, by the **20th of the following month**. Use prescribed electronic delivery under 25G unless an evidenced, operative Commissioner exemption under 25P applies; then establish and use the prescribed non-electronic form or delivery mode under 25Q. Verify the exemption's operative dates, any time limit and cancellation conditions. An electronic-delivery exemption does not itself remove information or payment duties; no actual payer exemption is established here. [TAA 25C–G/25P–Q][R01] |
| RWT remittance | RE 20/RE 21(6)/(7) and RA 15 establish monthly dividend remittance by the **20th following month end**. Interest instalment/threshold rules do not apply. [RE 20][R02], [RE 21][R03], [RA 15][P10] |
| Cessation/special timing | Establish RA 16 and any other special facts separately. Annual IR4 dates do not replace monthly RWT. [RA 16][P11] |
| Non-working day | IRD explains next-working-day treatment for a weekend/public holiday, with a separate provincial-anniversary electronic-payment rule. Establish the actual date/calendar/application evidence; no rendered calendar entry is adopted here. [Payment days][P14], [key-date rule][R05] |

A no-dividend month differs from a dividend month with zero RWT. IR284's blanket no-RWT/no-investment-information instruction is not adopted. Do not skip 25C/25E/25G solely because W = 0 or assert every RE 2-excluded/exempt payment is a taxable reportable dividend. Establish that branch's reporting scope separately. No payment due does not itself remove a statement/record duty. [TAA][R01], [IR284][R04], [dividend reporting][D2].

### Information readiness and file mapping

Under 25G, Schedule 6 rows 1–11, 14 and 16–22 apply as appropriate. Retain payer/payee identity/contact readiness, period income/withholding, credits, rate/ratio, shares, dates and applicable bonus/exchange fields. Preserve the investor IRD-number/birth-date qualifications and 25D's joint-owner/pre-April-2018 conditions; they do not make every field optional. [TAA 25D/25G and Schedule 6][R01].

Rows 17/18 give no general availability qualification for applicable shares or declaration/payment dates. D2's broad 'if available' wording does not establish a statutory waiver. The custodian held-information rule is not a general payer waiver. Obtain mandatory applicable fields or an established applicable variation; no general section 25R variation was established here. [TAA][R01], [dividend reporting][D2].

The current upload page links **February 2026 V1.6**. Its 'Gross dividend' is G in this ordinary bridge; DWT is W, cash C is separate and 'RWT rate' illustrates 3300 for 33%. Credit-ratio encoding 3889 represents displayed 38.89%, not permission to calculate credits at 0.3889. Money fields encode implied-decimal cents. These are format requirements, not proof of tax treatment, rounding or successful filing. [Upload page][R06], [specification][R07].

The field named 'Date Dividend Declared' requests the **record date where available**, otherwise declaration date. Preserve actual record, declaration, derivation and payment dates separately with evidence and the approved mapping. Do not overwrite the statutory declaration date, invent a record date or treat upload acceptance as Schedule 6 compliance. Missing/conflicting dates remain held; special custodian zeros/blanks do not generalise. [Specification][R07], [Schedule 6][R01].

## Shareholder statement and records

Section 29 applies to a company dividend, other than one treated as interest, where **RWT was withheld OR an imputation credit attached**. Ordinary timing is at payment; emigration/DRCD cases have separate provisions and remain outside this core. Zero RWT with a credit can still require a statement. IR284's RWT-only instruction is incomplete. With neither condition, no universal section 29 trigger is established here; assess other requirements separately. [TAA 29][R01], [IR284][R04].

Use a Commissioner-approved form with section 29 particulars: company/shareholder information, payment date, dividend, RWT/NRWT if any, imputation/aggregate amounts, applicable retirement-scheme/RSCT particulars and further required information. Give it through a permitted section 14F route to the shareholder or authorised person. A draft is not delivery evidence; the reviewer retains actual delivery proof and private identities. [TAA 14F/29][R01].

Keep record clocks separate. Section 22AAB applies to a person liable to withhold and generally retains relevant investment-income records **7 years after payment**. Section 22 business records generally require at least **7 years after the relevant income-year end**. Section 22(2)(k) memorandum-account and attached-credit records require at least **7 years after the relevant tax or income-year end, as applicable**. Identify the ICA tax year, **1 April to 31 March**, separately from the company's income year/balance date. Retain section 22's statutory exceptions and possible notified extension up to **3 further years**. Section 22AAB(4) has its own extension power: notice before the initial 7 years end can require specified records for up to **3 further years**, on its audit/investigation grounds. Those grounds include the affairs of a person to whom the records relate and the Commissioner's intended or actively considered investigation; do not confine them to an audit of the payer alone. Do not replace the separate clocks with seven-years-from-filing or infer early destruction authority. Preserve applicable ICA/attached-credit, statement, payment and reporting records under their own conditions. [TAA 22/22AAB][R01], [OB 1][P08], [ICA year][I05].

## Synthetic controls for the selected 2026-27 core

These fictional NZD cases assume ordinary legal, credit and period gates are independently established unless a diagnostic holds. They test arithmetic and boundaries, not actual classification, lawful distributions, filing or professional approval. Cent-exact examples do not resolve rounding for other values.

### Fully imputed ordinary dividend

For D = $720 and valid I = $280, G = $1,000, W = $50 and C = $670. The credit is 28% of G but 28/72 of D. Full ordinary imputation does not remove the remaining RWT in this in-scope case. [RE 13][A03], [OA 18][A11].

```oa-check
name: nz-dividend-rwt-fully-imputed
tolerance: 0
inputs:
  dividend_before_rwt: 720
  imputation: 280
steps:
  gross: dividend_before_rwt + imputation
  rwt: gross * 0.33 - imputation
  cash: dividend_before_rwt - rwt
  ceiling_cross_difference: dividend_before_rwt * 28 - imputation * 72
expected:
  gross: 1000
  rwt: 50
  cash: 670
  ceiling_cross_difference: 0
```

### Partly imputed dividend

For D = $2,000 and valid I = $200, G = $2,200, W = $526 and C = $1,474. [RE 13][A03].

```oa-check
name: nz-dividend-rwt-partly-imputed
tolerance: 0
inputs:
  dividend_before_rwt: 2000
  imputation: 200
steps:
  gross: dividend_before_rwt + imputation
  rwt: gross * 0.33 - imputation
  cash: dividend_before_rwt - rwt
expected:
  gross: 2200
  rwt: 526
  cash: 1474
```

### Unimputed dividend

For separately confirmed unimputed D = $100, W = $33 and C = $67. Do not substitute the shareholder's marginal rate. [RE 13][A03], [Schedule 1][A06].

```oa-check
name: nz-dividend-rwt-unimputed
tolerance: 0
inputs:
  dividend_before_rwt: 100
  imputation: 0
steps:
  gross: dividend_before_rwt + imputation
  rwt: gross * 0.33 - imputation
  cash: dividend_before_rwt - rwt
expected:
  gross: 100
  rwt: 33
  cash: 67
```

### Trace cash without counting credits twice

The first example's $670 cash, $50 RWT and $280 credit reconcile to D = $720 and G = $1,000. Reapplying RE 13 uses D + I once. Using G as D would overstate withholding. A cash record alone does not establish W/I. [RE 13][A03], [CD 15][A12].

```oa-check
name: nz-dividend-rwt-cash-bridge
tolerance: 0
inputs:
  cash: 670
  withheld: 50
  imputation: 280
steps:
  dividend_before_rwt: cash + withheld
  gross: dividend_before_rwt + imputation
  recomputed_rwt: gross * 0.33 - imputation
  reconciliation_difference: recomputed_rwt - withheld
expected:
  dividend_before_rwt: 720
  gross: 1000
  recomputed_rwt: 50
  reconciliation_difference: 0
```

### Reject overattachment

D = $720 and proposed I = $281 fail I × 72 ≤ D × 28 by 72 in the cross-product test. Hold credit and computation; do not silently reduce I to $280. This is a failed-input diagnostic, not an allowable attachment or tax result. [OA 18][A11].

```oa-check
name: nz-dividend-rwt-overattachment-diagnostic
tolerance: 0
inputs:
  dividend_before_rwt: 720
  proposed_credit: 281
steps:
  excess_cross_product: proposed_credit * 72 - dividend_before_rwt * 28
expected:
  excess_cross_product: 72
```

### Reject the rounded display ratio as a calculation rate

Calculating at displayed 0.3889 produces $280.008 on D = $720, above the exact $280 ceiling. The specification grants no authority for that excess or a rounding policy. [OA 18][A11], [specification][R07].

```oa-check
name: nz-dividend-rwt-display-ratio-diagnostic
tolerance: 0
inputs:
  dividend_before_rwt: 720
steps:
  exact_ceiling: dividend_before_rwt * 28 / 72
  displayed_rate_product: dividend_before_rwt * 0.3889
  excess: displayed_rate_product - exact_ceiling
expected:
  exact_ceiling: 280
  displayed_rate_product: 280.008
  excess: 0.008
```

### Hold fractional cents

For D = $1.01 and I = 0, exact algebra gives W = $0.3333 and C = $0.6767. These are diagnostic values, not payable/file-ready currency amounts. Whether, how and at what aggregation level they become cents is unestablished. Record Needs Input; do not silently choose $0.33 or $0.34. [RE 13][A03], [specification][R07].

```oa-check
name: nz-dividend-rwt-fractional-cent-hold
tolerance: 0
inputs:
  dividend_before_rwt: 1.01
  imputation: 0
steps:
  exact_algebraic_rwt: (dividend_before_rwt + imputation) * 0.33 - imputation
  exact_algebraic_cash: dividend_before_rwt - exact_algebraic_rwt
expected:
  exact_algebraic_rwt: 0.3333
  exact_algebraic_cash: 0.6767
```

### Conditional workflow and reporting controls

| Case | Required result |
| --- | --- |
| Recipient company/full imputation but unestablished RE 2(5)(fb) payer choice | Needs Input; do not assume zero RWT |
| Separately verified RE 2 intercompany exclusion, W = 0 and I > 0 | Test section 29 independently: credit trigger remains. Establish information-reporting scope separately; no zero-RWT/no-report default |
| No dividend paid/derived in the period | Distinguish from a paid dividend with zero withholding; create no fictional dividend |
| Applicable shares or declaration date missing | Hold information completion; broad 'if available' guidance/upload acceptance is not a statutory waiver |
| Record date differs from declaration date | Retain both, apply specification field mapping and keep statutory particulars for reviewer resolution |
| Temporary ICA debit before a supported attachment | No automatic positive-at-payment test; still establish validity, benchmark and closing consequences |
| Later ratio differs without established pre-payment declaration or Commissioner-allowed later date | Needs Input; maximum-ratio arithmetic does not clear benchmark/change gates |
| Current tax audit or notice of deficiency | Fire R-CIT-6 with its canonical message and stop |
| Non-cash/foreign/special dividend result requested | Fire R-NZ-DIV-SPECIAL and stop until supported specialist content is available |
| Complete 2027 IR4/ICA requested using only this guide | Fire R-NZ-DIV-INCOMPLETE; retain all country slots/outputs, no completion claim |

These are conditional expected controls, not a recorded live workflow trial. The zero-RWT intercompany case is a separately established exclusion, not a zero produced by the ordinary RE 13 examples. Do not invent I = 33% of G to force an ordinary dividend's W to zero.

## Working-paper additions and checks

Retain a per-payment schedule with source references for D/I/G/W/C, exact ceiling cross-products, benchmark/change evidence, ICA movement references, period and separate date fields. Reconcile recipient rows to approved totals, statements, monthly information and remittance; no aggregate guess replaces a missing item. Mark each source item T1, an expressly authorised factual-default T2 or unresolved T3. This guide authorises no new T2 defaults.

Keep a field-readiness/mapping schedule without private identifiers, separate statement/information decisions, calendar evidence, record clocks and remaining corporate/ICA tasks. Read final reviewer figures from the recalculated workbook. Preserve every universal/domain output, flag, action owner and practitioner checklist sign-off. A schedule is not a filed return or paid tax.

## Review Checklist Items

Add every item below to practitioner review checklist Section D alongside the universal and corporate checks. Run both bases' checks and verify:

1. Profile/periods confirmed; source and credit conditions established; all refusal codes traced with exact messages for fired codes.
2. Evidenced ordinary RE 2/3/4/13 scope; each exclusion/special branch resolved or explicitly held.
3. D/C/G correctly labelled, valid I counted once, exact ceiling and benchmark gates passed and no negative result clamped.
4. Current applicable fractional-cent authority or held amounts; displayed ratios/integer-cent formats never determine unsupported amounts.
5. Separate reporting, remittance and statement tests, mandatory fields/qualifications, approved-form/delivery requirements and actual calendar evidence.
6. Separate ICA, record clocks and annual/interim handoffs; no 2025-26 annual dates imported into 2026-27.
7. Inputs, differences, unknowns, alternatives and NZ$0 review flags in all required output components.
8. All mandatory corporate slots, universal/domain outputs and professional review retained. No legal distribution, complete IR4/ICA, filing, payment, whole-topic completion or accountant review claimed from synthetic controls.

## Provenance and limitations

Selected primary clauses/application rules were checked on 14 November 2026. The 2022 RE 2 amendment's selected exemption/group changes apply for 2022-23 and later years; this establishes no earlier rule. [2022 Act section 160][A20]. IRD guidance supplements statute, with the 3 reporting conflicts above resolved against statutory conditions.

Native PDF extraction is not whole-document visual/legal assurance. IR274's empty native pages and IR4JG's unprocessed rotated page were not relied on. This Tier 2 guide awaits accountant review. Source/arithmetic checks do not establish taxpayer facts, a legal opinion, full current-law coverage or an engagement result. A locally qualified practitioner must review actual conditions, evidence, figures, forms and dates before reliance or action.

## Change log

- **0.1, 14 November 2026:** Initial selected 2026-27 domestic cash-dividend RWT reference, with exact credit/withholding controls, separate reporting/statement/record gates and an unresolved fractional-cent hold. Source-cited draft awaiting accountant review.

## Primary sources

[A03]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1520231/
[R01]: https://www.legislation.govt.nz/act/public/1994/166/en/latest/
[W01]: https://www.legislation.govt.nz/act/public/1999/65/en/latest/
[W02]: https://www.legislation.govt.nz/act/public/2012/44/en/latest/
[W03]: https://www.legislation.govt.nz/act/public/2024/11/en/latest/
[W04]: https://www.legislation.govt.nz/act/public/2024/47/en/latest/
[W05]: https://www.legislation.govt.nz/act/public/2026/12/en/latest/
[W06]: https://www.legislation.govt.nz/act/public/2023/35/en/latest/
[W07]: https://www.legislation.govt.nz/act/public/2026/8/en/latest/
[W08]: https://www.legislation.govt.nz/act/public/2026/25/en/latest/
[W09]: https://www.legislation.govt.nz/act/public/2026/48/en/latest/
[W10]: https://www.legislation.govt.nz/act/public/2023/5/en/latest/
[W11]: https://www.legislation.govt.nz/act/public/2025/9/en/latest/
[W12]: https://www.legislation.govt.nz/secondary-legislation/pco-drafted/2026/340/en/latest/
[W13]: https://www.legislation.govt.nz/act/public/2026/70/en/latest/
[W14]: https://www.legislation.govt.nz/act/public/2003/51/en/latest/
[A17]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1512540/
[A18]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1512545/
[A19]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1512548/
[P01]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1512550/
[P02]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1512553/
[A02]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1520194/
[A15]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1520294/
[P05]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1513263/
[P06]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1517160/
[A07]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1520198/
[A13]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1520200/
[A08]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1520202/
[A14]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1520206/
[A16]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1520298/
[P12]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS1427089/
[A06]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1523192/
[A12]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1512572/
[D3]: https://www.ird.govt.nz/income-tax/withholding-taxes/resident-withholding-tax-rwt/using-the-right-rwt-tax-rate
[R04]: https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir284/ir284.pdf?modified=20251030195459
[A11]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1518689/
[A04]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1518852/
[R07]: https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/iir-file-upload-specification/investment-income-reporting-file-upload-specification.pdf?modified=20260205005514
[PART-R]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/parts/DLM1519723/
[P08]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1518696/
[P07]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1518642/
[P03]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1512574/
[P04]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1512580/
[I08]: https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir274/ir274-2024.pdf?modified=20240604223621
[A05]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1518861/
[I01]: https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/income-tax-for-companies/imputation-for-companies/how-imputation-credits-work/benchmark-dividend
[I04]: https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/income-tax-for-companies/imputation-for-companies/how-imputation-credits-work/declare-a-ratio-change
[I03]: https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/income-tax-for-companies/imputation-for-companies/how-imputation-credits-work/imputation-credit-accounts
[I05]: https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/income-tax-for-companies/imputation-for-companies/how-imputation-credits-work/memorandum-accounts
[I06]: https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/income-tax-for-companies/imputation-for-companies/how-imputation-credits-work/file-an-annual-imputation-return-ir4j
[I07]: https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/income-tax-for-companies/imputation-for-companies/how-imputation-credits-work/file-an-interim-imputation-return---ir4j
[I09]: https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1---ir99/ir4jg/ir4jg.pdf?modified=20260331224857
[D4]: https://www.ird.govt.nz/income-tax/withholding-taxes/resident-withholding-tax-rwt/payers/registering-as-a-payer-of-resident-withholding-tax
[D5]: https://www.ird.govt.nz/income-tax/withholding-taxes/resident-withholding-tax-rwt/resident-withholding-tax-exemption-register
[R02]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1520277/
[R03]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1520279/
[P10]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519761/
[P11]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519764/
[P14]: https://www.ird.govt.nz/managing-my-tax/make-a-payment/when-to-pay
[R05]: https://www.ird.govt.nz/key-dates
[D2]: https://www.ird.govt.nz/income-tax/withholding-taxes/resident-withholding-tax-rwt/payers/investment-income-reporting/reporting-requirements/payers-of-dividends---reporting-requirements
[R06]: https://www.ird.govt.nz/file-upload-investment-income
[A20]: https://www.legislation.govt.nz/act/public/2022/10/en/latest/sections/LMS544158/

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
