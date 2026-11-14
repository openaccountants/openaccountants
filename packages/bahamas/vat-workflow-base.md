---
name: vat-workflow-base
description: "Shared 2026 VAT/GST return method: reconcile invoices, settlements and tax points, classify from actual law/evidence, preserve unresolved facts, build linked source/return allocations and recalculated workpapers, review every row and all fourteen checks, and deliver the workbook and reviewer brief. Bounded official UK/EU examples do not supply worldwide rates, boxes, supplier outcomes or filing approval."
version: 0.2.1
jurisdiction: GLOBAL
tax_year: 2026
type: cross-country-method
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
---

# VAT Workflow Base

## VAT Workflow Base Skill v0.2.1

## Scope

### What this file is, and what it is not

**This file is a shared method, not worldwide VAT law.** It retains evidence intake, classification, questions, workbook/formula controls, line-by-line review, fourteen self-checks and deliverables. Bounded official UK/EU illustrations below explain important method boundaries; the actual country/regime/period supplies rates, tax points, deduction conditions, return fields, documentation, exclusions and related duties. A bank description, a supplier name or an accountant's published method does not itself prove a transaction or approve this new return.

**Companions:** obtain the actual country law/method and the regional/directive instrument where applicable. A non-EU system does not need an invented EU regional layer. Load actual available slugs and versions, effective dates and approval labels, then read their evidence; source presence is not proof of live publication. Missing governing law or material facts holds a final return, while an explicitly incomplete source inventory and diagnostic workpaper can proceed.

**This file is the contract.** When a country skill or a regional skill says it conforms to v0.2.1 of this base, what they mean is: they fill the country slots specified in Section 7, they produce outputs in the format specified in Section 3, their classifications can be validated by the self-checks in Section 5, and they participate in the workflow in Section 1.

## The method, step by step

### Section 1: The workflow

You are helping a small business owner prepare a VAT return. The output will be reviewed by a warranted accountant before filing. Your job is to do the mechanical classification work and produce a working paper plus a reviewer brief that makes the human reviewer's job fast and accurate.

Execute these nine steps in order. Do not skip. Do not reorder. Do not start classifying transactions before step 4. Build evidence inventories as needed; do not call a return final before classification, unresolved-fact and formula checks are complete.

**Ordering principle:** read the complete existing record and source evidence, ask focused material factual questions before finalising affected classifications, then calculate/review/recalculate the workbook and brief. Earlier answers persist; do not request the same fact again. Workpapers can evolve when new evidence arrives. Neither a forced one-round confirmation nor a workbook built only once is a substitute for correct treatment. Retain a dated answer/change log so the human can see what changed and why.
### Step 1 , Confirm the companion skills are loaded

0. **Confirm companion skills:** establish legal entity/VAT registrations, jurisdiction/establishments, tax period and actual accounting scheme. Read current available country/region methods and actual official law, preserving their source/version/date/approval provenance. Identify the required invoices, records and filing structure. An unavailable companion does not authorise guessed law, another country's boxes or a blanket refusal of evidence preparation.

### Step 2 , Read the data

0. **Read the complete data:** read every provided bank/card/processor statement, sales/purchase invoice, credit note, cash record, prior return, VAT account and adjustment schedule. Preserve file/row IDs, currency, period, signs and counts, checking duplicates, truncated/unreadable records and missing accounts. Bank settlement date/amount is not generally the tax point, taxable consideration or input-tax evidence. Reconcile invoices and settlements without counting both; include unpaid invoices and non-cash/self-accounted events where the actual scheme requires them. Keep foreign-currency originals and obtain the official conversion method/date, not an automatic exclusion of useful data. Actual VAT records include more than bank lines. [HMRC records](https://www.gov.uk/charge-reclaim-record-vat/keeping-vat-records).

### Step 3 , Infer the client profile from the data

0. **Infer a profile as a hypothesis:** retain all nine signal families: entity type; location; tax IDs; period/frequency; business activity; employees; premises/property; cross-border activity; maturity/seasonality, plus description-level classification clues. Search the actual entity record, contracts, registration, prior return and invoices first. Drawings, wages, bank/IBAN country, supplier branding or a tax-reference fragment are leads, not proof of legal form, tax residence, business use or registration. Preserve the original category cues: Consulting/Beratung, Logo Design, Workshop, Renovierung Büro, Bewirtung/Geschäftsessen, Mobilfunk Rechnung Büro and shipped-to descriptions. They can identify a plausible goods/service/expense enquiry but cannot alone prove B2B status, place of supply, deduction entitlement or a return code. A UK/US consulting receipt does not automatically establish German Kz 45; a marketplace logo purchase does not itself prove business use or actual supplier VAT. [Commission place-of-taxation factors](https://taxation-customs.ec.europa.eu/taxation/vat/vat-directive/place-taxation_en). Record the supported profile, competing explanations and exact evidence still needed.

### Step 4 , Confirm the inferred profile (one round trip)

0. **Confirm only missing material profile facts:** give a concise evidence-based profile and ask focused corrections for entity/registration, period/scheme, activity or other material uncertainty. Use existing confirmations and records before a follow-up. Record answers and effective dates. Silence or 'don't know' does not prove a fact, nor does confirming a general profile confirm every supplier/customer/tax condition. Continue supported lines while holding the affected final result; avoid repeating a full onboarding questionnaire already answered.

### Step 5 , Run refusal checks

0. **Run actual refusal/scope checks:** read available applicable country/regional triggers and record each code with evidence, failed/unresolved/not-applicable status and affected scope. Do not invent a cleared refusal from absence of a bank description. If a genuine hard boundary applies, hold/refuse the affected task and state why; preserve lawful evidence inventory and correction/referral work where permitted. Complexity or missing source evidence does not justify fabricating a final return.

### Step 6 , Classify deterministically against the country skill

0. **Classify with evidence, preserving every source row:**
1. Exclusion enquiry: own-account transfers, drawings, payroll, tax payments, bank fees and statutory contributions remain explicit workstreams, but a name/pattern does not automatically exclude a taxable fee or a mixed transaction. Retain source amount and reason; exclusion from return allocations does not delete source data.
2. Supplier-pattern enquiry: use the country library as a documented hypothesis, matching actual invoicing legal entity, VAT IDs, product, establishment, dates and evidence. Contradictory invoices/law override the pattern. A familiar SaaS brand is not proof of Irish/Luxembourg billing or reverse charge.
3. Apply supported country/regional rules to actual supply/customer status, tax point, consideration, rate/liability, deduction/evidence and return field; distinguish zero-rated, exempt-with/without-deduction, outside-scope and self-accounted treatment.
4. Where a fact or law is unresolved, retain a linked Tier 2 evidence gap/scenario, not an invented higher-tax default. Ask only for facts the user can supply after records have been searched; research legal gaps from official sources.
Every source row has an explicit status: reconciled/excluded, supported classified allocation(s), or unresolved with evidence/task ownership. One payment may settle several invoices; one invoice may have several rates or legitimate boxes. Preserve source-to-allocation links and reconciliation totals rather than forcing exactly one return code per bank row. [UK reverse-charge multi-box mechanics](https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a), [EU return scope](https://taxation-customs.ec.europa.eu/taxation/vat/vat-directive/vat-returns_en).

### Step 6.5 , Ask the user about Tier 2 ambiguities via the question tool

0. **Resolve material Tier 2 questions before finalisation:**
- Review full records, descriptions and country evidence first. Descriptions can resolve the category they actually establish; they do not silently establish every tax condition.
- Group repeated questions (for example, actual business-use evidence for several mobile lines). Prioritise tax/filing impact and imminent deadlines. An optional internal EUR 50 presentation floor, where expressly adopted, is not law and never suppresses a required evidence, registration, exemption or filing check. Unknown impact is not zero.
- Use the runtime's actual available question interface, or concise text questions if it has none. Do not require `ask_user_input_v0`, claude.ai or a particular app. For a supported UI, respect its real schema and capacity; do not pretend a tool call occurred. A familiar design is one to three focused questions per batch and two to four mutually exclusive answers, adapted to the actual tool.
- Name the source line(s), ask the missing factual question, explain the supported cash/obligation consequences and state 'not yet computable' where necessary. Include 'don't know / evidence unavailable'; it preserves an unresolved status, not a locked tax treatment. A business-use percentage may require a precise follow-up, not invented midpoint percentages.
- Apply the no-effect filter only where all legally relevant consequences, tax point, boxes, eligibility, related filings and evidence duties are identical; equal immediate VAT alone is insufficient.
- Sequence batches after answers arrive and record question ID, source rows, actual answer, evidence and resulting treatment. The internal ten-question review trigger remains a complexity signal, not a law or a reason to end the conversation and abandon work. If an actually applicable companion defines R-EU-12, apply its real scope; otherwise stage or refer genuinely unresolved work.
- Preserve the original intra-Community-goods scenario: a French-customer shipment and EUR 15,000 consideration require actual parties, transport, VAT status/reporting and country exemption conditions. Do not assert a universal five-condition checklist or German code/rate, treat missing proof as zero-rated, or switch to domestic tax merely because the user clicks an option. Research the rule and hold the exact unresolved condition before a final return.
Output a complete answer/evidence log. Required unresolved conditions remain visible; skipped questions or items grouped below a presentation floor do not become verified facts.

### Step 7 , Build the outputs

0. **Build the deliverables, keeping calculation and evidence separate:**
**Artefact 1, workbook.** Preserve the Transactions, Box Summary and Return Form structure plus source reconciliation, invoice/settlement links and a one-to-many Return Allocations table where required. Use live formulas with explicit inputs, signs, bases, units, rates, eligibility, period and rounding; no unexplained hardcoded return totals. Country fields/boxes must match the actual return version. A tax return is not 'ready' merely because the workbook is valid.
- **7.1.a Write:** use available authorised spreadsheet/file tools to create a real `.xlsx` at an actual accessible output path named for country/period. `/mnt/user-data/outputs/` and `bash_tool`/`create_file` are examples from a historical runtime, not required paths/tools on every AI. If file creation is unavailable, state the artifact limitation and provide supported schedules/evidence without claiming a workbook was made.
- **7.1.b Recalculate:** run an actual supported spreadsheet calculation engine, preserving its version/log/output. The old `/mnt/skills/public/xlsx/scripts/recalc.py` may be used only if it exists and is appropriate. Saving formula text or setting automatic recalculation flags does not prove results were computed.
- **7.1.c Verify:** inspect actual evaluated/cached formula values, errors, links, signs and source-to-box/return totals. A tool-specific success JSON is evidence only if the tool actually ran; manually compare key totals with independent recomputation. Fix/recalculate until no unexplained formula errors or required mismatches remain. A self-consistent wrong formula must not 'win' over evidence.
**Artefact 2, reviewer brief.** Save the actual workbook result and status, jurisdiction/period/source versions, key risks, every unresolved/provisional item, question/answer changes, supported alternative/cash impact and specific invoices/official-law gaps. Keep the former four buckets visible: substantive user answers; don't-know/unresolved answers; optional presentation-floor grouped items; genuine no-effect questions not asked. None authorises unsupported tax. Use the country's actual final payable/refund box, not universal German Kz 83. The brief and verified workbook must agree; if not, investigate and correct the cause.
Record the actual write, recalc, inspection and brief steps rather than demanding a fixed count of tool calls. Present files only after the review/readiness checks, marking an incomplete artifact clearly if required evidence remains unresolved.

### Step 7.5 , Line-by-line review pass (in-conversation audit)

0. **Review every allocation/source row, without sampling:** this remains a second preparer self-review in the same engagement, not an independent accountant review. Preserve all six checks plus extra scrutiny of the ten largest absolute source amounts; the internal count does not exempt other rows.
1. Read date/tax point, actual invoice/issuer/recipient, source amounts, allocation, rate/liability, eligibility, status and evidence. Ordinary supplier-charged input VAT requires the actual applicable invoice/evidence conditions. However, reverse-charge/acquisition/import VAT may arise without supplier-charged VAT, with their own statutory evidence. Do not invent input VAT from a gross bank line or mechanically block self-accounted deductible tax because the supplier invoice shows none. [EU deductions](https://taxation-customs.ec.europa.eu/archives/taxable-persons/deductions_en), [HMRC reverse charge](https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a).
2. Re-read category clues: Consulting/Beratung, Workshop, Logo Design, Bewirtung/Geschäftsessen, Renovierung Büro, shipped-to, Kontoführungsgebühr, Mitgliedsbeitrag, Versicherung and Beitrag. Verify what they establish and what remains unknown. A supplier/category is not a universal zero-VAT conclusion: chamber/professional dues, public-body fees, government licensing, pensions, insurance/finance, healthcare/education, property/rent, postage, gambling, travel/international flights, donations/grants and statutory health charges all retain actual country/transaction enquiries, including mixed or optional-tax supplies.
3. Compare the actual country rule/pattern and record any departure with the invoice/legal reason. Evidence overrides an inaccurate or stale library; do not follow a brand pattern blindly.
4. Review actual cross-border goods/services, customer business status/establishment, movement, VAT IDs and reporting/evidence. Preserve non-EU consulting, intra-Community goods, Google/Microsoft/Adobe/Slack Irish billing and AWS branch cases as conditional enquiries, not predetermined Kz 45/41/81 or universal reverse charge. Resolve the actual issuer, supply type, place, taxable person and country scheme.
5. For each assumption/unresolved flag, check brief/evidence/answer coverage, actual supported alternative and meaningful cash/obligation delta. A wrong-law or unknown-rate issue cannot be solved by a generic higher-tax default. Distinguish tax invoice amounts from business/partial-exemption recovery and other adjustments.
6. For the highest-impact rows, read the relevant available country worked case and actual primary authority where needed: goods exemption, AWS branch billing, capital assets/capital-goods adjustment and other material categories. A model's training memory or resemblance to an example is not law verification.
Record failed/unresolved checks by source/allocated row, correction and source. Update workbook, recalculate, update brief and rerun affected/full integrity checks as appropriate. An empty arithmetic failure list does not hide unresolved legal/evidence conditions. Preserve equal attention for the original chamber-dues, international-flight, marketplace, high-value goods and capital-asset error families; no guessed input VAT on them. This self-review does not substitute for a separate source/pack review required for publication or a professional client's approval.

### Step 8 , Self-check before delivering

0. **Run all fourteen structural/substantive integrity checks** against the actual computed workbook, source/answer log and brief. Record pass/fail/unresolved/not applicable with evidence. Correct failures and repeat row review/recalculation as needed. An incomplete draft may retain precise gaps, but a required unresolved check blocks a final return-ready claim; do not silently tick it passed.

### Step 9 , Present the files and write the closing chat response

0. **Deliver actual files and the closing message:** use the runtime's supported attachment/link mechanism for the actual accessible `.xlsx` and reviewer brief, workbook first. `present_files` is not universally available, and saving to a path does not itself make a file accessible. Verify the user can access what was created.
State the verified payable/refundable amount, currency, period and actual final box, plus the material unresolved status if any, what each artifact contains and the highest-priority task. Do not invent a cached result, official submission, acceptance or accountant sign-off. Avoid repeating the full workbook/brief or re-asking already answered questions at delivery.
If the user supplies a correction/new evidence, preserve the change log and rerun affected classification, calculations, row review, fourteen checks and both artifacts. Revisions may also be necessary to correct a discovered error, not only when the user requests them. Deliver a proposed schedule/import for human approval; do not submit a live return or post journals merely because an output exists.

## Section 2 , Two-tier rule and conservative defaults

- **Two-tier classification rule:** Tier 1 means the actual governing rule and all material transaction facts/evidence are established; retain the source/rule/calculation trail without unnecessary narration or questions. Tier 2 means a missing fact or unsettled legal/source condition. State it, research official sources where possible, retain supported alternatives and ask only for genuinely missing user facts. Do not force a final default on a row merely because the user does not know. A presentation decision to group a question is not a tax determination.
- **Former default families, now evidence enquiries:** retain unknown sale rate; purchase VAT/evidence; counterparty country; B2B/B2C status; business-use proportion; blocked input; and in/out-of-scope treatment. Do not automatically choose standard rate, domestic, B2C, zero recovery or in-scope because it appears to cost more. Determine actual country law, recognition, evidence and relief/correction options; a voluntary overpayment may be irrecoverable or distort another obligation. [HMRC business-use/evidence rules as one country example](https://www.gov.uk/charge-reclaim-record-vat/reclaim-vat-business-expenses).
- **Question threshold:** the former EUR 50 floor may be retained only as an explicitly adopted internal optional-presentation setting, never a legal materiality rule or permission to omit a required condition. Missing rate/eligibility facts or tax/filing risks remain visible even when current cash impact is small, zero or unknown. No-effect filtering requires the entire legal/return/related-duty outcome to be unchanged.

## Section 3 , Output specification

Three outputs per VAT return. All three are mandatory. Never produce one without the others.

### Output 1 , Excel working paper

**Sheet "Transactions" column structure**  _(Black)_

**Sheet "Transactions" column structure**  _(Black)_

| Column | Content | Color convention |
| --- | --- | --- |
| A | Date | Black |
| B | Counterparty | Black |
| C | Description | Black |
| D | Original gross/source amount with currency and source ID; invoice/settlement bridge retained | Blue (supported source input) |
| E | Net amount | Black (formula or input) |
| F | VAT amount | Black (formula or input) |
| G | Rate applied | Black |
| H | Primary treatment / linked return allocation IDs; may map to several legitimate boxes | Black |
| I | Treatment label | Black |
| J | Provisional assumption / unresolved evidence? (Y/N) | Black, yellow background if Y |
| K | Question reference (linked to brief) | Black |
| L | Excluded? Reason if yes | Black |

The country skill provides a sheet structure template. The base requires the following minimum: Sheet "Transactions" and its source-reconciliation/allocation links preserve every source line and the actual split/combined transactions, with the columns above. Preserve every original source row in a reconciliation log and link it to each actual transaction/allocation. Split mixed rates/invoices and several settlements with stable IDs; do not require raw bank-row count to equal return-allocation count. Excluded source lines retain original amounts and a reason, with no unintended return allocation; do not replace a box identifier with numeric zero. Tier 2 rows retain Y in J and a question/evidence reference in K, including genuinely unresolved items. [HMRC record and invoice audit trail](https://www.gov.uk/guidance/record-keeping-for-vat-notice-70021).

Sheet "Box Summary": one row per actual return box, with formula totals from a linked Return Allocations table where one transaction legitimately affects several boxes. Preserve transaction/box/base/tax/recovery/sign IDs and prevent duplicate allocations, rather than forcing a single H value to represent a reverse charge. The country skill provides the list of valid box codes for that country. Formulas, not hardcoded values. Use the xlsx skill's color conventions: black text for formula cells.

Sheet "Return Form" , the final figures and readiness status, structured to match the country's actual return form layout. Cross-sheet references to the Box Summary sheet, in green text per xlsx convention. The bottom-line payable/refundable figure is a single labelled cell.

Color conventions (from the xlsx skill): Blue text: hardcoded inputs from the bank statement. Black text: formulas. Green text: cross-sheet references. Yellow background: cells requiring reviewer attention (any row where a default was applied).

After building the workbook, use the actual available calculation engine to recompute and inspect formulas/cached values, errors, source links and key independent totals. Record its output; do not claim the historical recalc.py or a success JSON ran if unavailable. Fix/recalculate errors before a final workbook, with legal/evidence readiness separately stated.

File delivery: save an actual `<country>-vat-<period>-working-paper.xlsx` in the runtime's accessible output location and attach/link it using supported tools, with complete/incomplete status.

### Output 2 , Reviewer brief (markdown)

A short narrative document that gives the human reviewer the context they need to verify the working paper efficiently. Follow this exact template:

```markdown
# [Country] VAT Return , Reviewer Brief
**Period:** [period]  
**Generated:** [date]  
**Source data:** [all bank/card/processor, invoice/credit-note, prior-return and adjustment sources with IDs]
**Underlying invoices seen:** [yes / no / partial]

## Bottom line
- **[Box code for final figure]**: [amount] [currency] [payable / refundable]
- Total output VAT: [amount]
- Total input VAT: [amount]
- Total transactions classified: [count]
- Of which Tier 2 provisional/unresolved: [count, linked to source/answer log]
- Of which excluded: [count]

## High flags (review first)
[Numbered list of items with cash impact > country skill's HIGH threshold, or Tier 2 defaults with potential swing > country skill's HIGH tax-delta threshold. Each item: one sentence what, one sentence why it matters, one sentence what the reviewer should do.]

## Medium flags
[Numbered list of secondary items: counterparty concentration above threshold, more than five provisional/unresolved items, items at category boundaries.]

## Low / informational flags
[Period total approaching review threshold, related filings triggered (e.g., EC Sales List equivalent), unusual but not high-impact patterns.]

## Assumptions and unresolved evidence
[For every Tier 2 item: source/transaction/allocation ID, actual date, amount, missing fact or law, evidence/answer, supported scenario or held conclusion, alternative and meaningful tax/obligation impact; do not imply an unanswered fact was confirmed.]

## Invoices the reviewer should pull
[List of specific invoices the reviewer needs to verify before signing off. Not generic "verify invoices" , specific items.]

## Refusal triggers checked and cleared
[Every actual applicable R-code, evidence and pass/fail/unresolved/not-applicable result, with the affected readiness/referral task. Absence of a bank clue is not proof of clearance.]
```

File delivery: save the actual `<country>-vat-<period>-reviewer-brief.md` next to the accessible workbook and attach/link it with the same version/status.

### Output 3 , Chat response

The chat response is short and serves three purposes: 1. Bottom-line summary. Two or three sentences. The figure (read from the workbook, not computed in the chat), the period, the most important caveat. 2. Pointers to the two files, attached/linked using the runtime's actual supported tools, with one sentence each on what they contain. 3. Optional one-line revision invitation. "If you need to change any of your earlier answers, tell me which question and I'll regenerate the workbook." This is the safety valve for the user-changes-their-mind case described in Step 9.3.

Use Step 6.5 for required factual questions before finalising affected treatments. The delivery response need not repeat earlier questions, but must state any unresolved evidence and actual artifact/readiness limitation; no forced question tool or false claim that all questions were answered.

Do not repeat the working paper contents in chat. Do not duplicate the reviewer brief. The chat response is a navigation aid, not a third copy of the output.

## Section 4 , The question form (tool-based, runs in Step 6.5)

Present focused factual questions in the runtime's available interactive tool where supported, or concise text if not. No product-specific interface is mandatory. Research legal issues from official sources and read existing answers/records first; the user is not asked to decide an unresolved statute. Ask before finalising the affected classification, preserve answer IDs and allow evidence-driven revisions. The original filtering, grouping, cash-impact priority and concise option design remain; they are presentation controls, not tax law.
### Filtering rules , which Tier 2 rows become questions

- **Filtering and grouping:** re-read actual category clues without inferring unsupported tax facts; distinguish a user fact from a legal/source gap; group repeated questions by evidence/decision; rank by supported tax/filing impact; retain an explicitly adopted optional presentation floor only as described in Step 6.5; suppress a redundant question only if the full legal/return/related-duty outcome is identical. Preserve all required gaps in the brief. The internal ten-question review trigger and any actual companion R-EU-12 scope prompt staging/referral, not fabricated defaults or abandoned source records.
### Tool call format

Inspect the actual available tool schema. Where appropriate, use one to three focused questions and two to four mutually exclusive options; support precise text follow-ups where the real fact requires them. These are presentation examples, not a universal runtime API contract.

**Format for each question:**
```yaml
question: "[Plain language question naming the line(s) by date/counterparty/amount, plus the cash impact of the most consequential answer]"
options:
  - "[Supported factual answer, with its actual conditional consequence]"
  - "[Second most likely answer , the cash impact of choosing this]"
  - "[Third option, if applicable]"
  - "[Don't know / evidence unavailable, keep unresolved]"
type: "single_select"
```

**Mandatory features of every question:**
- Name the line(s) explicitly. Never ask "what about that fuel transaction" , always "the four Aral fuel lines totalling €196.90 from January-March." The user needs to know which line is being asked about without scrolling through anything.
- Quantify a supported cash/obligation consequence, or say why it is not yet computable. Do not invent a rate or tax-inclusive price merely to make an option look precise. Immediate cash can be unchanged while evidence or another filing still matters.
- Include a genuine "don't know / evidence unavailable" option. Record it as unresolved, with the needed source/fact and affected readiness, rather than treating it as agreement to more tax or less recovery.
- Options are mutually exclusive. No "select all that apply" questions. If a row needs more than one decision, split it into two questions.

**Worked example (illustrative , NOT drawn from any test fixture):**

Retain the mobile-line business-use scenario: the actual invoices and country rule must establish any VAT and deduction method before a recovery amount is offered. A call/business-use record is relevant; a vehicle mileage log alone does not prove phone use. Ask the actual missing proportion/evidence, distinguish business-only, supported mixed use, personal/no eligible use and unknown. If a mixed percentage is needed, obtain a precise supported figure in a follow-up rather than choose an unproven range midpoint. A fixed gross amount does not itself prove an input VAT amount. The worked arithmetic below illustrates established facts without inventing them.
### Tool call sequencing

- **Sequencing:** respect the actual runtime capacity, wait for each required response, and group higher-impact/earlier-deadline questions first. Preserve the original one-to-three, four-to-six and seven-to-ten batching concepts where supported, adapting rather than pretending a specific tool exists. More than ten is an internal complexity/staging trigger; apply an actual companion refusal only when its conditions are met. No universal 'above ten, end conversation' rule applies.
- **Delivery ordering:** questions precede finalisation of their affected return entries, not necessarily every provisional evidence sheet. Do not re-ask them at delivery. Record question/answer/version changes; update/review/recalculate when the user supplies new evidence or an error is discovered.
- **No obsolete app requirement:** the earlier claude.ai-only, `ask_user_input_v0` and no-text-fallback instructions are superseded. Use the actual ChatGPT, Claude, Cursor, Slack or other supported environment capabilities honestly.
- **Reviewer invoice list:** keep specific invoice/customs/credit-note evidence requests in the brief with source IDs, not generic questions the user cannot answer. Grouping labels are optional presentation, not a legal classification mechanism.

## Section 5 , Self-check before output

Run these fourteen checks against your draft output before sending the chat response. If any fails, fix the output and re-run. Do not deliver a return that fails any check. These checks combine arithmetic/allocation integrity with documented evidence and actual country-rule conditions; they do not substitute for a separate qualified review. They are necessary but not sufficient. They are the cheapest reliability gain in the workflow and they must all pass.

### Structural integrity checks (always run first)

- **Check 1:** **Completeness:** every bank/card/processor/invoice/credit-note/source record is accounted for once in source reconciliation, with stable links to exclusion or actual allocation(s). Source counts need not equal allocation-row counts where split or combined settlements are legitimate; reconcile amounts and duplicates, not a forced seventy-three-row equality.
- **Check 2:** **Arithmetic integrity:** the final actual country return reconciles output/self-accounted tax, allowable input tax and every relevant country adjustment/credit/carried balance/rounding rule. Compare evaluated formulas to an independent source/box/return bridge; a formula that implements the wrong model does not pass merely because it recalculates.
- **Check 3:** **Actual calculation engine ran:** record the actual supported engine/tool, evaluated/cached results and zero unexplained formula/link errors. Do not substitute a non-existent recalc.py path, automatic-calculation flag or invented JSON. If calculation/file capability is missing, label the artifact incomplete, not verified.
- **Check 4:** **Exclusion consistency:** an excluded source line retains its amount/evidence/reason and no unintended return allocation. Mixed lines can have separate supported excluded and included allocations, reconciled to the source. Do not wipe the original amount or replace a box ID with numeric zero.
- **Check 5:** **No duplicate allocations:** each source-to-invoice/settlement and transaction-to-box allocation is uniquely identified and reconciled. A single transaction can legitimately affect several return boxes, especially reverse charge or gross/base/tax fields. Ban duplicate counting of the same measure, not all multi-box entries.

### Cross-document consistency checks

- **Check 6:** **Disclosure matches working paper:** every Y/assumption/unresolved status in J has a matching source ID, evidence/answer, alternative and actual affected result in the brief. Include grouped no-question items and unapplied scenarios, not only defaults actually calculated.
- **Check 7:** **Question/evidence coverage:** every Tier 2 item is covered by an actual answer, linked common question, specific outstanding evidence/official-law task or documented full-no-effect decision. No unresolved item disappears because a presentation cash floor was applied.
- **Check 8:** **Provisional treatment has authority:** no blanket standard-rate/domestic/B2C/zero-recovery/higher-tax default. A supported provisional rule must be current, applicable and factually established; otherwise hold the final treatment and show the exact gap/alternative.

### Country-skill compliance checks

- **Check 9:** **Supplier pattern evidence:** compare each matched supplier pattern with actual invoice issuer, product, establishment, date, legal VAT/evidence and deduction rule. Record supported departures; an inaccurate or stale library never overrides stronger actual evidence.
- **Check 10:** **Reverse-charge sides and recovery:** account for actual output self-assessment and separately allowable input recovery, including business/partial-exemption or blocked-input limits. Full recovery may net to zero, but not every reverse charge does. Reconcile all legitimate boxes and explain any non-recovered amount. [HMRC section 5.2 to 5.4](https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a).
- **Check 11:** **Related filings:** actual country transaction/box conditions trigger the specific informational, registration, customs or other return task and deadline, with evidence and owner. A zero current tax result does not remove a separate duty.
- **Check 12:** **Period boundary:** select the actual statutory tax/claim point and accounting scheme, not merely the bank date. Reconcile advance payments, unpaid/late invoices, credit notes and prior-period adjustments under the actual rules; preserve original dates plus the reason for this return inclusion.
- **Check 13:** **Currency consistency:** preserve original currencies, lawful reporting currency and actual tax conversion rule/rate/date/rounding. Reconcile converted allocations and settlement FX separately; foreign currency is not automatically excluded or silently treated as local.

### Refusal trace

- **Check 14:** **Refusal/evidence trace:** list each actual applicable country/regional R-code with pass/fail/unresolved/not-applicable, source/fact and affected task. A user profile confirmation or absence of an adverse bank clue is not automatic clearance.

### Failure handling

Correct failures and rerun affected row review/recalculation and all required integrity checks. Repeated failure holds the affected final return with precise evidence/correction and deadline tasks, not silent workaround. Label incomplete working papers explicitly; never mark a required unresolved check passed to deliver a filing-ready result.

## Section 6 , How this workflow base interacts with companion skills

This base coordinates actual country evidence and a regional/directive layer where one applies. The division of responsibility:

**This file (vat-workflow-base) owns:**
- The workflow runbook (Section 1)
- The two-tier rule and conservative defaults principle (Section 2)
- The output specification (Section 3)
- The structured question form template and rules (Section 4)
- The 14 self-checks (Section 5)
- The country slot contract (Section 7)
- The interaction model in this section (Section 6)

**The regional/directive layer owns:**
- The legal framework that applies across the region (e.g., the EU VAT Directive, Council Implementing Regulation)
- Harmonized concepts that exist at the regional level (place of supply rules, reverse charge mechanism, intra-Community framework, OSS/IOSS, related filings like EC Sales Lists)
- Refusals that derive from regional law (numbered R-EU-1, R-EU-2, etc. for the EU layer)
- Source citations to regional legislation

**The country-specific layer owns:**
- Standard and reduced VAT rates for that country
- The actual return form structure and box codes
- The supplier pattern library (the lookup table)
- Country-specific refusals (numbered R-XX-N where XX is the country code)
- Country-specific Tier 2 catalogue
- Worked examples drawn from a hypothetical client of that country
- The country-specific Excel template overlay
- Local-language bank statement reading guide
- Onboarding fallback questions (asked only when Step 3 inference fails)
- Red flag thresholds for the reviewer brief

**Conflict resolution:**

- **If country/regional sources conflict:** read the actual applicable law, national implementation, amendments and relevant binding interpretation; document the exact conflict and legal resolution. A file label does not decide legal precedence; if unresolved, hold the affected conclusion rather than choose the higher tax.
- **If a country file is silent:** research actual country/regional applicability and implementation; do not assume every optional directive provision applies identically.
- **If the country skill is silent on something this workflow base specifies:** apply this workflow base.
- **If the workflow base specifies a workflow step that the country skill describes differently:** follow this base's workflow order, but use the country skill's content within that step.
- **If the user's situation triggers regional and country-specific boundaries:** determine actual legal/scope applicability and preserve both findings; a narrower file label does not automatically clear the other boundary.

Retain this base's integrity/evidence controls while adapting the workbook, questions and mandatory country process to actual law/runtime capabilities. A country process difference is not automatically a bug; legal requirements cannot be overridden by this generic workflow.

## Section 7 , Country slot contract

Every country skill loaded alongside this workflow base MUST provide the following. The country skill is incomplete without all of these. This base is incomplete without a country skill.

### Mandatory slots

- **Mandatory slot 1 , Standard VAT rate(s)** , Standard VAT rate(s) as a single number or list.  _(Section 7, Mandatory slots)_
- **Mandatory slot 2 , Reduced VAT rate(s)** , Reduced VAT rate(s) with a brief description of what they apply to.  _(Section 7, Mandatory slots)_
- **Mandatory slot 3 , Return form name and field structure** , Return form name and field structure , the exact box codes and what each one represents.  _(Section 7, Mandatory slots)_
- **Mandatory slot 4 , Filing portal name** , Filing portal name (the digital filing system the country uses).  _(Section 7, Mandatory slots)_
- **Mandatory slot 5 , Filing deadlines** , Filing deadlines , the rules for monthly, quarterly, annual filings.  _(Section 7, Mandatory slots)_
- **Mandatory slot 6 , Supplier pattern library** , Supplier pattern library , a literal lookup table mapping common counterparty name patterns to their VAT treatment. Coverage must be comprehensive for the country's typical small-business counterparties. The historical twenty-five/thirty-entry targets are internal coverage goals, not statutory requirements or permission to fill rows with guessed tax outcomes. Mandatory categories: telecoms, utilities, banks, post and logistics, transport, food retail, fuel, restaurants, hotels, office supplies, coworking, government fees, insurance, major SaaS providers (Google, Microsoft, Adobe, Meta, AWS, Apple, Slack, Dropbox, Zoom, LinkedIn, Atlassian, Anthropic, OpenAI). The table is a hypothesis/evidence aid and never overrides actual law or transaction documents. Preserve all listed supplier/category enquiries without inventing a universal tax treatment.  _(Section 7, Mandatory slots)_
- **Supplier-pattern coverage target:** retain the historical twenty-five-entry/thirty-for-dense-ecosystems planning target only for evidenced useful patterns; a smaller truthful library is not proof of an incomplete legal return.
- **Mandatory slot 7 , Country-specific exclusion patterns** , Country-specific exclusion patterns , the local-language patterns that mark a line as excluded (owner draws, wages, tax authority payments, statutory contributions).  _(Section 7, Mandatory slots)_
- **Mandatory slot 8 , Country-specific refusal catalogue** , Country-specific refusal catalogue , refusals on top of the regional layer's catalogue. Numbered as R-XX-1, R-XX-2, ... where XX is the country code.  _(Section 7, Mandatory slots)_
- **Mandatory slot 9 , Tier 2 question catalogue** , Tier 2 question catalogue , for each ambiguity type, the question text, the evidence needed, any actual supported provisional treatment, and how the answer changes classification. Used to populate the structured question form.  _(Section 7, Mandatory slots)_
- **Mandatory slot 10: Unresolved/provisional treatment rules** - Actual country rules permitting provisional treatment, their conditions/evidence and the final-readiness hold for unresolved issues; no generic greater-tax default.  _(Section 7, Mandatory slots)_
- **Mandatory slot 11 , Worked examples** , Worked examples , minimum 6 fully worked transaction classifications drawn from realistic bank statement lines, each showing input → reasoning → output. These are pattern anchors for the model. Worked examples must be drawn from a hypothetical client, not from any real test bank statement that will be used to validate the skill , this prevents eval contamination.  _(Section 7, Mandatory slots)_
- **Worked examples minimum count** , 6 examples (minimum fully worked transaction classifications, drawn from a hypothetical client)  _(Section 7, Mandatory slots)_
- **Mandatory slot 12 , Excel template specification** , Excel template specification , the country-specific column structure for Sheet "Transactions" (which box codes are valid in column H), the box list for Sheet "Box Summary", and the layout of Sheet "Return Form".  _(Section 7, Mandatory slots)_
- **Mandatory slot 13 , Red flag thresholds** , Red flag thresholds , country slot values that feed the reviewer brief: HIGH single-transaction threshold, HIGH tax-delta threshold for a single default, MEDIUM counterparty concentration threshold, LOW absolute-position threshold.  _(Section 7, Mandatory slots)_
- **Mandatory slot 14 , Required inputs manifest** , Required inputs manifest , minimum / recommended / ideal inputs and the refusal policy if the minimum is not met (HARD STOP or SOFT WARN).  _(Section 7, Mandatory slots)_

### Optional slots

- **Optional slot 15 , Country-specific bank statement reading guide** , Country-specific bank statement reading guide , local CSV format conventions, common bank export quirks, language-specific field names.  _(Section 7, Optional slots)_
- **Optional slot 16 , Sectoral notes** , Sectoral notes , patterns specific to common business types in that country.  _(Section 7, Optional slots)_
- **Missing mandatory slot policy:** identify exact legal/calculation/input gaps and hold the affected final conclusion; continue supported evidence work. Internal library/example counts are not statutory eligibility tests or reasons to fabricate missing rules.

## Worked cases

### One reverse-charge service legitimately appears in multiple boxes

Assume a UK VAT-registered recipient receives a qualifying B2B service of GBP 1,000 from a non-UK supplier, with no relevant place-of-supply/exemption exception. Assume the actual service is standard-rated and actual supported input recovery is one half. Output self-assessment is GBP 200, allowable input is GBP 100 and net liability from this transaction is GBP 100. Under the cited UK mechanism, boxes one/four contain the respective tax amounts and boxes six/seven the GBP 1,000 service value: multiple linked entries are legitimate, not double-counting. The supported recovery fraction is a case fact, not a worldwide partial-exemption method. [HMRC section 5.2 to 5.4](https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a), [UK standard rate](https://www.gov.uk/vat-rates).

```oa-check
name: Reverse charge multiple return fields and partial recovery are legitimate
inputs:
  service_value: 1000
  actual_standard_rate: 0.20
  supported_recovery_fraction: 0.50
steps:
  - self_assessed_output_tax: service_value * actual_standard_rate
  - deductible_input_tax: self_assessed_output_tax * supported_recovery_fraction
  - net_tax_for_transaction: self_assessed_output_tax - deductible_input_tax
  - sales_value_box: service_value
  - purchase_value_box: service_value
expected:
  self_assessed_output_tax: 200
  deductible_input_tax: 100
  net_tax_for_transaction: 100
  sales_value_box: 1000
  purchase_value_box: 1000
```

### Tax point and cash settlement are not interchangeable

Assume an ordinary UK invoice-accounting purchase has net consideration GBP 1,000, correct standard-rate VAT GBP 200, an established March tax point and sufficient actual invoice/deduction evidence. It is paid in April. Subject to the actual claim timing and scheme rules, the bank payment month is not by itself the correct VAT period. A separate GBP 240 cash receipt in April settles a supported standard-rated gross sale: its net amount is GBP 200 and VAT GBP 40, not GBP 48 computed on gross. Under a cash-accounting scheme the actual timing test differs; do not elect one merely because a bank statement was supplied. [HMRC VAT records/tax point](https://www.gov.uk/charge-reclaim-record-vat/keeping-vat-records), [UK rate](https://www.gov.uk/vat-rates).

```oa-check
name: Gross inclusive VAT and invoice settlement reconciliation
inputs:
  purchase_net: 1000
  established_rate: 0.20
  gross_sale_receipt: 240
steps:
  - purchase_vat: purchase_net * established_rate
  - purchase_gross_settlement: purchase_net + purchase_vat
  - sale_net: gross_sale_receipt / (1 + established_rate)
  - sale_vat: gross_sale_receipt - sale_net
  - overstated_vat_if_rate_applied_to_gross: gross_sale_receipt * established_rate - sale_vat
expected:
  purchase_vat: 200
  purchase_gross_settlement: 1200
  sale_net: 200
  sale_vat: 40
  overstated_vat_if_rate_applied_to_gross: 8
```

## When to refuse or refer

Hold a final return when governing law/rates/boxes, actual registration/scheme, material invoice/evidence, customer/supply status, period/FX or required calculation remains unresolved. Do not fabricate VAT from supplier branding, bank gross amounts or an unanswered question. Preserve supported work and exact gap/referral tasks, especially partial exemption, capital-goods adjustments, property/option-to-tax, complex cross-border/chain/import or prior-period correction cases. A preparer self-review does not confer accountant approval; retain actual professional review/filing/sign-off evidence separately. No live filing or posting is performed by creating these files.

## Section 8 , Reference material

### Validation status

This file is v0.2.1 of `vat-workflow-base`, updated as a shared 2026 method. Its original architecture dates to April 2026. It was extracted from `eu-vat-base` v0.3 by separating the workflow content (which is jurisdiction-agnostic and lives here) from the EU directive content (which is jurisdiction-specific to the EU and now lives in `eu-vat-directive`). That historical extraction claim described the earlier version; v0.2.1 makes substantive corrections recorded above, not merely a structural refactor.

### Origin

This file inherits its content from `eu-vat-base` v0.3 Sections 1, 2, 3, 4, 5, 7, and 8. The country slot contract in Section 7 of this file is the same 14 mandatory + 2 optional slots specified in the v0.3 base. The 14 self-checks in Section 5 of this file are the same 14 self-checks added to the v0.3 base. The current Section 1 retains nine principal steps plus the factual-question and row-review substeps; the historical eight-step description is superseded.

The only deletions from the v0.3 base content are: references to EU-specific concepts (which moved to `eu-vat-directive`), the 12 EU-wide refusals (which moved to `eu-vat-directive`), and EU-specific source citations.

### Known gaps

1. The 14 self-checks are deterministic but not exhaustive. They catch errors of execution and integrity, not errors of conceptual understanding. They are the foundation of the eval loop, not its only component.
2. The cautious confirmation step (Step 4 of the workflow) costs one round trip. If MVP testing shows users dropping off at this step, consider an opt-out for clearly unambiguous profiles.
3. The structured question form's 10-question maximum is a heuristic, not a measured optimum.
4. The Excel template structure has not yet been validated against real practitioner feedback for legibility.
5. The supplier pattern library minimum (25 entries) is a starting threshold and may need to be raised once we see how it performs across countries.

### Historical change log, superseded where inconsistent with v0.2.1

The following entries record earlier designs. They are not operative instructions to invent tax, require a specific app/tool, refuse every non-Claude runtime, ignore actual invoices or enforce one-box-per-transaction. The current method above controls.

- **v0.2.1 (14 November 2026):** Corrects actual evidence/tax points, allocation multiplicity, supplier-name inference and unsafe defaults; supports real runtime capabilities while preserving all review/delivery controls, fourteen checks and sixteen country slots.

- **v0.2.0 (April 2026):** Major architectural restructure , questions now happen BEFORE the workbook is built, not after. This is a workflow reorder, not a patch. The previous v0.1.x sequence was Step 6 (classify) → Step 7 (build workbook with conservative defaults) → chat response containing free-text question form → user answers nowhere because the workflow ends. This produced a workbook that was structurally already obsolete by the time the user finished reading the questions, plus a free-text form that users were likely to skim or skip because it required typing in chat. The v0.2.0 sequence is Step 6 (classify) → Step 6.5 (ask questions via `ask_user_input_v0` tool, tappable buttons) → Step 7 (build workbook ONCE with the user's answers already incorporated) → Step 7.5 (line-by-line review) → Step 8 (structural self-check) → Step 9 (present files + brief delivery message). The changes: Step 6.5 is new and is the entire question-form mechanism, restructured around the tappable tool; Step 7 produces only two artefacts (workbook and brief), not three (the chat response moves to Step 9); Step 9 is new and handles file presentation plus the closing message; Section 4 is rewritten end-to-end to describe the tool format, the filtering rules, and the tool sequencing rather than the free-text form template; Output 3 in Section 3 is updated to drop the question form reference. The targeting is `claude.ai` and the official Claude apps only; the skill halts if `ask_user_input_v0` is unavailable rather than falling back to the v0.1.x free-text form. The architectural justification: the v0.1.x ordering produced double work (build workbook with defaults, then either throw it away when the user answers or leave the user holding a stale file) AND high user friction (typed answers in chat are skippable in a way tappable buttons are not). The v0.2.0 ordering builds once, asks via UI, and the user gets the final workbook directly. No previous patch in v0.1.x is invalidated , Step 3's nine inference categories, Step 7's recalc gate, Step 7.5's line-by-line review pass, Section 4's filtering rules (cash floor, no-effect rule, description-answered rule), and the 14 self-checks all carry over unchanged. What changed is *when* the question form runs and *how* it presents itself to the user.
- **v0.1.3 (April 2026):** Added Step 7.5 , line-by-line review pass , between Step 7 (build outputs) and Step 8 (structural self-check). Step 7.5 is a same-conversation, same-model, in-workflow review pass that walks every row of the Transactions sheet with adversarial intent and applies six explicit checks per row (would the invoice carry VAT, did the description carry information, does the Kz match the supplier pattern library, is cross-border treatment correct, was the conservative default applied and disclosed, and for top-10 cash impact rows, does the treatment match the relevant worked example). Step 7.5 must produce an empty failure list before Step 8 can begin. This patch is the response to the diagnosis that the IHK and Lufthansa errors in earlier reruns were *attention failures* not *knowledge failures* , the model knew the rules, it just didn't apply them to the specific medium-cash-impact rows because attention was on the high-cash-impact rows. Step 7.5 forces equal attention on every row regardless of cash impact, which is what catches that error class. Step 7.5 explicitly does NOT call external tools and does NOT verify against primary sources , those are future enhancements outside v0.1.3 scope. The honest scope of Step 7.5 is attention failures only; knowledge failures (where the model lacks the relevant fact entirely) require a different mechanism that isn't in this patch. This patch replaces the previously planned separate `vat-audit-base` skill, which was dropped because (a) Claude as auditor has the same training-data blind spots as Claude as classifier, so a separate auditor catches knowledge failures no better than an in-workflow review pass would, and (b) the separate auditor pattern encouraged checklist-writing which led directly to the eval contamination problem identified in the v0.1 auditor draft.
- **v0.1.2 (April 2026):** Step 7 hardened against the recalc-skip failure mode. The first rerun of v0.1.1 produced a structurally correct .xlsx file with 112 live formulas but skipped the recalc.py step, leaving the cached values empty. The file worked when opened in Excel (which auto-recalculates) but failed Check 3 of the self-check suite (which depends on cached values being present) and was technically "uncomputed" until a human opened it. This patch rewrites Step 7 as three explicit sub-steps (7.1.a write, 7.1.b recalc, 7.1.c verify) with each one a hard gate before the next. The recalc command is now part of the build sequence rather than a follow-up note. Step 7 is not complete until all three sub-steps have executed and recalc reports `total_errors: 0`. Also added a runtime check at 7.1.a: if `bash_tool` or `create_file` is unavailable, the model stops with a clear message rather than degrading to a markdown-only output. No structural changes to the workflow architecture, the question form rules, the conservative defaults principle, or the country slot contract.
- **v0.1.1 (April 2026):** Three targeted patches in response to first rerun feedback. (1) Section 1 Step 3 added a ninth inference category , "description-level classification signals" , making it explicit that words like "Consulting", "Logo Design", "Bewirtung", "shipped to [country]" in the transaction description are themselves classification signals and that the model should classify silently rather than asking when the description carries the answer. (2) Section 2's two-tier rule was rewritten to distinguish disclosure-in-the-brief (mandatory for every Tier 2 default) from question-on-the-form (conditional on cash impact and on whether the user genuinely has information the data does not contain). (3) Section 4 added two new rules to the question form: a minimum cash-impact floor (questions below the country skill's threshold, defaulting to €50, must not appear on the form) and an explicit prohibition on questions whose outcome does not affect the return. The first rerun produced a 10-question form where 3-5 questions failed at least one of these rules; the patches close those loopholes. No structural changes to the workflow, output specification, country slot contract, or self-checks.
- **v0.1 (April 2026):** Initial draft as part of the three-tier architecture split. Extracted from `eu-vat-base` v0.3. No substantive changes from v0.3 , this is a structural refactor that separates workflow architecture from regional legal content.

### Architecture recap, updated for v0.2.1

1. Workflow at top of file: yes (Section 1, before metadata).
2. Imperatives not descriptions: yes.
3. Output specification mandates Excel + markdown + chat: yes (Section 3).
4. Structured question form is a literal template: yes (Section 4).
5. Self-check before output: yes (Section 5, fourteen checks).
6. No worldwide country-rule claim: bounded actual UK/EU illustrations and sources are labelled; specific rates/boxes/eligibility still need the actual country/year evidence.
7. Country slots tightened: yes (Section 7, 14 mandatory + 2 optional).
8. Inferred-profile-first ordering: yes (Step 3 before Step 4 confirmation, no onboarding questionnaire upfront).
9. Loading model explicit: yes (Section 6).
10. Refusal handling delegated to companion skills: yes (this file contains no refusal catalogue , refusals are owned by the regional and country layers).
11. Reference material at bottom: yes (Section 8).

## End of VAT Workflow Base Skill v0.2.1

A final return needs actual current country law/method and a regional instrument where applicable. Preserve the source/version/approval and missing-evidence log; no app, supplier pattern or generic file hierarchy substitutes for those facts. Useful incomplete evidence preparation can continue without claiming readiness.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

## Sources

| Source and what was actually read | Official URL | Read on |
|---|---|---|
| HMRC records. Read for required invoices/credit notes/business/digital records, digital-link and VAT-account sections plus tax-point/period discussion; no general payment-date rule adopted | https://www.gov.uk/charge-reclaim-record-vat/keeping-vat-records | 2026-11-14 |
| HMRC reclaim business expenses. Read for opening business/personal-use evidence and partial-exemption distinctions; specialist vehicle/fuel/capital limits not certified here | https://www.gov.uk/charge-reclaim-record-vat/reclaim-vat-business-expenses | 2026-11-14 |
| HMRC Notice 741A. Read for section 5.1 to 5.5 actual reverse-charge scope, multiple return fields, partial recovery and exempt-service distinction; not the whole services manual | https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a | 2026-11-14 |
| HMRC Notice 700/21. Read for opening record classes, invoice primary-evidence and special margin/reverse-charge invoice distinctions; not every detailed invoice/retention exception | https://www.gov.uk/guidance/record-keeping-for-vat-notice-70021 | 2026-11-14 |
| HMRC MTD Notice. Read for section 3.2.1 electronic-account digital links and accepted transfer methods versus manual copy/paste; not every scheme exemption | https://www.gov.uk/government/publications/vat-notice-70022-making-tax-digital-for-vat/vat-notice-70022-making-tax-digital-for-vat | 2026-11-14 |
| Commission deductions guide. Read for opening deduction/partial recovery/chargeability and selected invoice/import/acquisition/reverse-charge evidence distinctions; national detailed exceptions still required | https://taxation-customs.ec.europa.eu/archives/taxable-persons/deductions_en | 2026-11-14 |
| Commission VAT returns. Read for opening taxpayer/transaction scope, reverse-charge customers and import/special-return distinctions; no country deadline supplied as a universal rule | https://taxation-customs.ec.europa.eu/taxation/vat/vat-directive/vat-returns_en | 2026-11-14 |
| Commission place of taxation. Read for goods/services general factors and material property/transport/event/digital exceptions; no automatic VAT result from client country or invoice description | https://taxation-customs.ec.europa.eu/taxation/vat/vat-directive/place-taxation_en | 2026-11-14 |
| HMRC VAT rates. Read for current standard/reduced/zero examples; only the standard-rated UK worked-case assumption is used | https://www.gov.uk/vat-rates | 2026-11-14 |

Not yet confirmed: every actual country's 2026 rates, registered person/scheme, tax point, consideration, input deduction/blocking/partial-exemption/capital-goods and evidence exceptions, return boxes/rounding/FX/adjustments, digital-link/filing and related-return obligations; current German Kz mappings, applicable intra-Community goods exemption/reporting conditions and actual billing/VAT treatment of every named supplier/category; actual source invoices and business-use proportions for any real case; each runtime's actual file/calculation/question/attachment capabilities. Historical EUR 50 and ten-question/library/example-count settings are internal presentation/coverage controls, not tax law. Old supplier-pattern certainties, greater-tax defaults, universal exemption categories, Claude-only UI commands and one-box-per-bank-row requirements are not usable current instructions.
