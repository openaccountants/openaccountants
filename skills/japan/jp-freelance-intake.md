---
name: jp-freelance-intake
description: ALWAYS USE THIS SKILL when a user asks for help preparing their Japanese tax returns AND mentions freelancing, self-employment, 個人事業主, フリーランス, sole proprietorship, or kojin jigyounushi. Trigger on phrases like "確定申告を手伝って", "help me file my kakutei shinkoku", "I'm a freelancer in Japan", "prepare my blue return", "I'm self-employed in Japan", or any similar phrasing where the user is a Japan-resident self-employed individual needing tax return preparation. This is the REQUIRED entry point for the Japanese self-employed tax workflow -- every other skill in the stack (japan-consumption-tax, jp-income-tax, jp-social-insurance, jp-return-assembly) depends on this skill running first to produce a structured intake package. Uses upload-first workflow -- the user dumps all their documents and the skill infers as much as possible before asking questions. Uses ask_user_input_v 0 for structured questions instead of one-at-a-time prose. Built for speed. Japan full-year residents only; self-employed individuals and sole proprietors (個人事業主).
version: 1.1
jurisdiction: JP
tax_year: 2026
last_updated: 2026-11-14
category: orchestrator
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: filing-howto
job: freelance-document-intake
---

# Japan freelance intake v1.1

> **General reference only.** This skill prepares AI-assisted working papers. A qualified 税理士 must review the facts, elections, computations and current forms before filing, paying or taking a tax position.

## Scope

Required entry point for full-year Japan-resident self-employed individuals/sole proprietors preparing 2026 working papers. Collect records, reconcile facts and hand off to `jp-return-assembly`; do not compute a final return here. Final 2025 forms are identified as the 2025-2026 filing cycle, separate from 2026 planning/preparation. Corporation, non-resident, agriculture, estate/gift and complex property/treaty matters need a separate specialist scope. Contributor: Open Accountants Community.

### Answer layer

| Fact that changes routing | Evidence and rule | Official source |
|---|---|---|
| Current JCT status | Base-period taxable sales <=JPY 10,000,000 (source: 1,000万円) can be exempt only after specified-period, registration/election and other statutory tests; current turnover alone cannot decide | [Consumption Tax Act arts.9,9-2; NTA 6501](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6501.htm) |
| Simplified JCT | Base-period taxable sales <=JPY 50,000,000 (source: 5,000万円) plus effective election and no restriction; use `jp-consumption-tax` | [Act art.37; NTA 6505](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6505.htm) |
| Blue deduction, not intake default | Up to JPY 550,000 (source: 55万円) under regular-bookkeeping/timely-statement conditions; JPY 650,000 (source: 65万円) additionally timely e-Tax OR qualifying excellent electronic books/notice; otherwise eligible blue deduction up to JPY 100,000 (source: 10万円); limited by relevant positive income | [Special Measures Act art.25-2; NTA 2072](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2072.htm) |
| Medical screening, normal deduction | Paid eligible medical expense less related reimbursement less JPY 100,000 (source: 10万円), or 5% of総所得金額等 if below JPY 2,000,000 (source: 200万円); cap JPY 2,000,000 (source: 200万円); compare qualifying self-medication alternative separately | [Income Tax Act art.73; NTA 1120](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1120.htm) |

Use upload-first, infer-then-confirm, then missing facts only. Do not re-ask facts answered by records. Use the available structured-question tool for related choices; the legacy `ask_user_input_v0` name is not a guarantee that the host exposes it. If absent, batch concise questions in normal text. Never invent a tool call. Process all evidence before asking tax details; preserve a short scope refusal check where essential. No workflow pacing questions or verbose phase narration.

## Ask the client first

- Which year, full-year residence, individual/corporate status and activity; identify separable out-of-scope work.
- Blue approval, bookkeeping method and intended supported filing route; opening notice is evidence, not proof of business-income classification.
- Prior-year returns, notices/elections, base/specified-period figures and invoice registration dates.
- Other income, spouse/dependents' exact ages/income/residence and any overseas facts.
- Missing business-use evidence and certificates only after checking documents.

## The method, step by step

1. Start briefly: identify the year, request the essential scope facts, say that a 税理士 must review the finished package. Do not ask whether the user is ready or how much preparation to do. The old time/turn targets were internal UX aims, never a promise; use document complexity to decide pace.
2. Compact scope sweep: business type (sole proprietor, freelance without opening notice, corporation, uncertain); blue/white/uncertain; actual year revenue range if unknown; residence and exceptional activities. Corporation stops this individual workflow. Freelance without開業届 can continue with a missing-notice/classification flag; neither notification nor a revenue band proves tax liability. If uncertain, inspect corporate registration/法人番号, opening/blue approval notices and prior return before asking.
3. Record invoice registration/opt-out intention, marital/dependent facts, other income (employment, rental, stocks/dividends, pension, crypto/miscellaneous), filing preference and prior estimated-tax notice/payments. Unregistered does not equal exempt; registration does not automatically qualify for 2割; cancellation does not necessarily restore exemption. Client/purchaser input credit can remain partly available under documented transition or books-only exceptions. [NTA 6498](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6498.htm).
4. Request a single document dump: full-year business bank statements CSV/PDF, sales invoices, expense receipts, accounting journal/general ledger exports, prior income return and blue statements/white収支内訳書,源泉徴収票 and支払調書/payment records, social/life/earthquake/mutual-aid/iDeCo certificates, municipality NHI notices/payments, pension certificates, estimated-tax notices/receipts, fixed-asset history and tax-office correspondence. Accept a partial dump and work with it; request specific gaps later. Do not demand duplicates already accessible.
5. Guided discovery if needed: bank downloads, freee/Money Forward/やよい journal exports, e-Tax prior returns,年金事務所/ねんきんネット pension certificate, municipality premium statement, insurance certificates and payer records. Search available user-authorised records for請求書,領収書,確定申告,税務署; no communication to third parties without authority. Allow the user to fetch missing records without unrelated questions.
6. Inference pass: distinguish sales receipts from transfers, loans and personal inflows; identify withholding withheld before cash receipt and platform fees. Parse business expenses, equipment, owner draws/contributions, tax/estimated payments, resident-tax payments, insurance, NHI/pension, mutual aid and iDeCo. Reconcile bank closing balance. From sales invoices record gross/net/JCT, buyer, dates, rate and registration. Foreign clients need export/service-place evidence. From purchases record expense type, business share, invoice evidence and asset candidate; immediate-expensing or pooled-asset eligibility comes from current `jp-income-tax`, never a price-band assumption. [NTA 6351](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6351.htm), [NTA 6551](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6551.htm).
7. Prior return inference: income by class, blue approval/deduction, prior final/estimated-tax assessment and actual payments, losses/carryforward, continuing depreciation, filing method and unresolved tax-office issues. Withholding records: payer, gross remuneration, actual amount withheld and bank net. For payment categories actually covered by Income Tax Act art.204, check the correct withholding rule; do not apply a professional-fee percentage to every freelancer. [NTA 2795](https://www.nta.go.jp/taxes/shiraberu/taxanswer/gensen/2795.htm).
8. Certificate inference: record actual payment date, category, amount, payer/person covered and certificate reference. Keep social insurance separate from小規模企業共済等掛金. Life insurance needs new/old contract categories, general/care/pension breakdown; earthquake old-contract distinctions remain for computation. Match actual paid pension/NHI rather than multiplying an obsolete monthly rate. Current basic/spouse/dependent deductions must be calculated by `jp-income-tax`; no fixed JPY 480,000 schema default. [NTA 1199](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1199.htm).
9. Present a compact source-labelled confirmation: identity/residence, business/blue/electronic status, invoice effective date, income by payer gross/net, expense categories and business shares, social/mutual-aid amounts, actual estimated payments, prior-year carryovers, JCT status/election evidence and open flags. Include no guessed deduction.
10. Ask gaps together: home-office room/total area and actual use/time, shared-room evidence; vehicle log; effective JCT election/2割 evidence; dependent age/income/living arrangements, spouse's exact income; medical payments and reimbursements; donations/furusato receipts; missing life/earthquake certificates. There is no universal accepted home-office percentage. Normal medical screening uses the 5% rule above, not the old 10% claim. Self-medication is an alternative, not an extra simultaneous normal-medical deduction. [NTA 1120](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1120.htm).
11. Show corrected facts once, record the user's confirmation and retain unresolved flags. Handoff explicitly to `jp-return-assembly`: consumption-tax classification/computation, income/blue or white return, social-insurance reconciliation and `jp-estimated-tax`, followed by workbook, reviewer brief and action calendar. Continue independently where evidence suffices; do not ask the user to approve workflow pacing.

### Structured intake contract

Keep these legacy keys for downstream compatibility. Unknown isnull, never zero/false. Retain raw evidence and derived values separately, with source document/page, tax year and confidence. Do not put credentials or taxpayer PINs in JSON. Collect sensitive identifiers only through an authorised secure destination when genuinely required for actual filing; preparation can use a redacted profile.

```json
{
  "jurisdiction": "JP",
  "tax_year": 2026,
  "taxpayer": {
    "name": null, "name_kana": null, "date_of_birth": null,
    "my_number": null, "marital_status": null, "spouse_income": null,
    "dependents": [], "residency": null, "address": null, "tax_office": null,
    "business_type": null, "blue_return": null,
    "blue_return_deduction_level": null, "invoice_registered": null,
    "invoice_registration_number": null, "filing_method": null
  },
  "income": {
    "jigyou_shotoku": {"uriage_zeikomi": null, "uriage_zeinuki": null,
      "consumption_tax_collected": null, "client_breakdown": [], "gensen_choushu_total": null},
    "other_income": {"kyuuyo_shotoku": null, "fudousan_shotoku": null,
      "haitou_shotoku": null, "zatsu_shotoku": null}
  },
  "expenses": {"keihi_by_category": {}, "kaji_anbun": {
    "rent_business_pct": null, "internet_business_pct": null,
    "phone_business_pct": null, "utilities_business_pct": null},
    "depreciation_assets": [], "shougaku_assets": []},
  "consumption_tax": {"filing_required": null, "method": null,
    "kani_gyoushu": null, "base_period_revenue": null,
    "was_menzei_before_invoice": null},
  "deductions": {"shakai_hokenryo": {"kokumin_kenko_hoken": null,
    "kokumin_nenkin": null, "other": null}, "shokibo_kigyou_kyousai": null,
    "ideco": null, "seimei_hokenryo": {"ippan": null, "kaigo_iryou": null,
    "kojin_nenkin": null}, "jishin_hokenryo": null, "iryouhi_koujo": null,
    "furusato_nouzei": null, "haigusha_koujo": null, "fuyou_koujo": null,
    "kiso_koujo": null},
  "estimated_tax": {"prior_year_shinkoku_nouzei": null,
    "yotei_nouzei_1st": null, "yotei_nouzei_2nd": null, "total_paid": null},
  "prior_year": {"jigyou_shotoku": null, "shinkoku_nouzei_gaku": null,
    "kurikoshi_songaku": null, "depreciation_schedule": []},
  "open_flags": [], "refusals_triggered": [], "documents_received": [],
  "evidence": [], "consumption_tax_status_tests": {}, "confirmation": null
}
```

## Boundary and exception table

| Intake issue | Routing boundary |
|---|---|
| Revenue under/over a threshold in current year | Collect base/specified-period/election evidence; do not announce exemption or compulsory JCT from this fact alone |
| Blue/white uncertain or no opening notice | Inspect approval and actual books; flag business-versus-miscellaneous classification for computation/reviewer |
| Other employment/rental/dividend/stock income | Record facts and load supported schedule; complex separate-tax capital gains require referral |
| Paper filing | Test excellent electronic-book route before limiting blue deduction; do not select a larger deduction merely for choosing e-Tax |
| Existing ID/password preference | Check live availability, do not promise a new ID/password issuance route |
| Medical or home-office uncertainty | Collect actual amounts/use, retain receipts/logs; no invented safe percentages |

For invoice cancellation, submit `適格請求書発行事業者の登録の取消しを求める旨の届出書` by the day 15 days before the desired next period starts. A later submission defers effect to the following period; no holiday extension applies to this cancellation deadline. Separate taxable-person-election and asset lock-ins still apply. An exempt operator registered under the transition outside the period containing 2023-10-01 remains taxable through the period containing the date 2 years after registration, even after cancellation. [NTA 6629, Act art.57-2 and notice exceptions](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6629.htm), [NTA registration lock-in FAQ](https://www.nta.go.jp/taxes/shiraberu/zeimokubetsu/shohi/keigenzeiritsu/pdf/sinkijigyousha/faq_k08.pdf).

For a 2026 business start, `個人事業の開業・廃業等届出書` goes to the competent tax office by the income-tax return deadline for the year containing the start, using e-Tax or paper; the current procedure replaces the old universal 1-month opening rule. Blue approval is a separate application and deadline. [Income Tax Act art.229; NTA A1-5](https://www.nta.go.jp/taxes/tetsuzuki/shinsei/annai/shinkoku/annai/04.htm).

## Worked cases

### Historical confirmation fixture, source-record facts only

The complete original fictional confirmation example is retained here for the **2025 package context**, with its 2024 prior-year record and April 2025 acquisition. These are historical illustrative record inputs, not current rates, certified payments, deduction entitlements or a real taxpayer's facts. Never copy them into a client record. Confirm them against the hypothetical documents before using even this example.

| Historical record group | Preserved facts / amounts | Source of fictional record |
|---|---|---|
| Identity and filing profile | 田中太郎 (Tanaka Taro), married, 1 dependent child; full-year Japan resident, Shibuya-ku, Tokyo; 個人事業主 with 開業届 filed; 青色申告 and intended e-Tax; invoice registration recorded as T1234567890123, a fictional identifier, not a checked registration  | [Original 2025 fixture](https://github.com/openaccountants/openaccountants/blob/f6e93f443e74613d48706e844d22d787c56b6875/skills/japan/jp-freelance-intake.md#section-5--the-confirmation) |
| Sales records, tax-excluded | JPY 12,500,000 total: ABC株式会社 monthly retainer JPY 6,000,000, DEF合同会社 project work JPY 4,000,000, various smaller clients JPY 2,500,000  | [Original 2025 fixture](https://github.com/openaccountants/openaccountants/blob/f6e93f443e74613d48706e844d22d787c56b6875/skills/japan/jp-freelance-intake.md#section-5--the-confirmation) |
| Invoice tax / withholding records | JPY 1,250,000 JCT collected on the recorded standard-rate invoices; ABC株式会社 withholding JPY 612,600, also the total withholding recorded; match gross invoices, net bank receipts and payer records before claiming credit  | [Original 2025 fixture](https://github.com/openaccountants/openaccountants/blob/f6e93f443e74613d48706e844d22d787c56b6875/skills/japan/jp-freelance-intake.md#section-5--the-confirmation) |
| Expense and asset records | Home-office rent JPY 720,000 and communication JPY 180,000 with business use unresolved; travel JPY 350,000, supplies JPY 120,000, books/subscriptions JPY 85,000, outsourcing JPY 800,000; MacBook Pro JPY 280,000 acquired April 2025. Raw sum JPY 2,535,000; the original “preliminary deductible” label is withdrawn, as explained in Case 2  | [Original 2025 fixture](https://github.com/openaccountants/openaccountants/blob/f6e93f443e74613d48706e844d22d787c56b6875/skills/japan/jp-freelance-intake.md#section-5--the-confirmation) |
| Payment/certificate records | NHI JPY 620,000; pension JPY 203,760 with the old source's arithmetic annotation JPY 16,980 × 12; small-enterprise mutual aid JPY 840,000 annotated JPY 70,000/month. Raw combined total JPY 1,663,760; pension/NHI and mutual aid remain separate deduction categories. These annotations are historical record data and are not a current pension rate or proof that every payment qualified  | [Original 2025 fixture](https://github.com/openaccountants/openaccountants/blob/f6e93f443e74613d48706e844d22d787c56b6875/skills/japan/jp-freelance-intake.md#section-5--the-confirmation) |
| Estimated-tax payment records | July JPY 250,000 and November JPY 250,000, total JPY 500,000; reconcile actual receipts. They are not amounts computed from the present year's sales  | [Original 2025 fixture](https://github.com/openaccountants/openaccountants/blob/f6e93f443e74613d48706e844d22d787c56b6875/skills/japan/jp-freelance-intake.md#section-5--the-confirmation) |
| 2024 prior return record | Business income JPY 8,200,000, final declared tax JPY 750,000, no loss carried forward, recorded blue deduction JPY 650,000. These are imported prior-return facts, not confirmation that the prior positions were legally correct  | [Original 2025 fixture](https://github.com/openaccountants/openaccountants/blob/f6e93f443e74613d48706e844d22d787c56b6875/skills/japan/jp-freelance-intake.md#section-5--the-confirmation) |
| Historical JCT status questions | The example asserted 2023 base-period revenue above JPY 10,000,000, without supplying the exact figure; invoice registration was recorded; 2割 eligibility and simplified election were both unresolved. Simplified ceiling JPY 50,000,000 is only one of the current conditions in the answer layer  | [Original 2025 fixture](https://github.com/openaccountants/openaccountants/blob/f6e93f443e74613d48706e844d22d787c56b6875/skills/japan/jp-freelance-intake.md#section-5--the-confirmation) |

Keep all five original attention flags: prove business use of rent/internet/phone; establish asset treatment from acquisition/in-service date, applicable dated regime and annual totals; reconcile ABC withholding; establish the effective JCT method/election; and map the actual sales year to future base/specified periods. The old automatic MacBook expensing conclusion is **not usable** merely because the price was below an old concession ceiling. The old statement that “JPY 12.5M means 2027 definitely requires filing” is also **not usable**: the historical sales year, taxable-sales definition and all status/registration tests must first be established. The example's 2023 base period belongs to its historical 2025 context, not a 2026 default. No deduction for the spouse or child follows from marital/dependent labels alone. Current pension rates must never be substituted for actual historical payments, or vice versa.

Case 1, receipt gross-up: hypothetical contractual net fee JPY 1,000,000, separately invoiced JCT JPY 100,000 and evidenced withholding JPY 102,100 give bank receipt JPY 997,900. Intake records fee, JCT and withholding separately; bank receipt alone understates invoice revenue. The withholding amount is a hypothetical payer record; eligibility/rate must be checked under actual payment category, not inferred from occupation. [NTA 2795](https://www.nta.go.jp/taxes/shiraberu/taxanswer/gensen/2795.htm).

```oa-check
name: Intake invoice withholding bank reconciliation
inputs:
  fee_net: 1000000
  invoice_jct: 100000
  withholding_record: 102100
  bank_receipt: 997900
steps:
  invoice_gross: fee_net + invoice_jct
  expected_receipt: invoice_gross - withholding_record
  mismatch: bank_receipt - expected_receipt
expected:
  invoice_gross: 1100000
  expected_receipt: 997900
  mismatch: 0
```

Case 2, evidence summary: the prior example's expense inputs were rent JPY 720,000, communication JPY 180,000, travel JPY 350,000, supplies JPY 120,000, books JPY 85,000, outsourcing JPY 800,000 and equipment JPY 280,000. Sum JPY 2,535,000 is a raw expense/asset total, not a deduction: equipment awaits current asset treatment and rent/communication business use still need proof. Removing that equipment candidate leaves JPY 2,255,000 before other tax adjustments. This catches a falsely definitive intake summary without inventing an asset rate.

```oa-check
name: Intake expenses versus unresolved capital item
inputs:
  rent: 720000
  communication: 180000
  travel: 350000
  supplies: 120000
  books: 85000
  outsourcing: 800000
  equipment: 280000
steps:
  raw_total: rent + communication + travel + supplies + books + outsourcing + equipment
  excluding_unresolved_asset: raw_total - equipment
expected:
  raw_total: 2535000
  excluding_unresolved_asset: 2255000
```

## When to refuse or refer

R-JP-1 corporation: corporate forms/rules require a corporate-tax practitioner. R-JP-2 agriculture: separate agricultural computation/statement outside this intake. R-JP-3 non-resident/part-year residence: different source/residence regime, refer. R-JP-4 estate/inheritance/gift: separate taxes outside scope. R-JP-5 property capital gains: separate taxation requires supported specialist schedule. R-JP-6 complex foreign-tax/treaty matters: record foreign-source facts but obtain an international-tax reviewer; basic credit is only supported when current computation skill covers it.

State the exact boundary briefly, stop the unsupported computation and continue only cleanly separable work with the omission visible. Do not work around refusals or coach answers to fit the scope.

## Filing and payment

Intake neither files nor pays. It records notices, payment evidence, filing method and intended calendar for `jp-etax-filing`. No user PIN collection, signature or final submission. Timely blue-return filing and statements matter under[NTA 2072](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2072.htm). Prior-year final cash tax is not automatically the statutory estimated-tax base; hand off the notice and adjustments to `jp-estimated-tax`.

## Completion checklist

Record the legacy IN 1-IN 13 controls: batched scope questions; available structured-input tool or clear fallback; upload-first; parsed documents before gaps; no repeat questions; all open flags; explicit assembly handoff; reviewer reminder; clean refusals; no phase narration; efficient turn count without arbitrary time promises; confirmed blue/white approval; JCT method either determined or visibly pending. Every inferred fact has evidence and period; unknown values remainnull; upstream consumers receive the complete contract, not just a prose summary.

## Sources

| Source | URL | Read on |
|---|---|---|
| NTA 6501: Read for liability test exceptions | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6501.htm | 2026-11-14 |
| NTA 6505: Read for method eligibility and elections | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6505.htm | 2026-11-14 |
| NTA blue: Read for deduction and electronic-book/timeliness conditions | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2072.htm | 2026-11-14 |
| NTA medical: Read for normal medical and self-medication alternatives | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1120.htm | 2026-11-14 |
| NTA 6498: Read for registration and credit exceptions | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6498.htm | 2026-11-14 |
| NTA 6351: Read for invoice gross/net reconciliation | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6351.htm | 2026-11-14 |
| NTA 6551: Read for export-service boundaries | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6551.htm | 2026-11-14 |
| NTA withholding: Read for covered remuneration and gross/net treatment | https://www.nta.go.jp/taxes/shiraberu/taxanswer/gensen/2795.htm | 2026-11-14 |
| NTA basic: Read for year-specific deduction reform | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1199.htm | 2026-11-14 |

| NTA 6629: Read for invoice cancellation deadline, no-holiday rule and election exceptions | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6629.htm | 2026-11-14 |
| NTA registration lock-in FAQ: Read for cancellation versus 2-year taxable status and first-period exception | https://www.nta.go.jp/taxes/shiraberu/zeimokubetsu/shohi/keigenzeiritsu/pdf/sinkijigyousha/faq_k08.pdf | 2026-11-14 |

| NTA A1-5: Read for current opening notification submission deadline and e-Tax/paper procedure | https://www.nta.go.jp/taxes/tetsuzuki/shinsei/annai/shinkoku/annai/04.htm | 2026-11-14 |

Not yet confirmed: Detailed 2026 spouse/dependent/life/earthquake/asset/carryforward amounts are delegated to current sourced jp-income-tax and cannot be copied from the old 2025 intake. No fixed basic deduction, fixed pension monthly amount or automatic home-office percentage is authorised. Final 2026 e-Tax screens and availability of host-specific interactive tools are not checked by this intake.
