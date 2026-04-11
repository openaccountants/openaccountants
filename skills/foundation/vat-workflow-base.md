---
name: vat-workflow-base
description: Tier 1 workflow base for VAT return preparation skills. Contains the universal workflow runbook, two-tier classification rule, conservative defaults principle, structured question form, output specification, and 14 self-checks. This skill provides workflow architecture only — it contains no legal content, no jurisdiction-specific facts, no rates, no return form details. It MUST be loaded alongside (a) a regional/directive layer that provides the legal framework for the relevant tax system (e.g., eu-vat-directive for EU member states) and (b) a country-specific skill that provides rates, return form structure, supplier patterns, and refusals (e.g., germany-vat-return). This skill is the foundation that every country VAT skill loads on top of.
version: 0.2.0
---

# VAT Workflow Base Skill v0.1

## What this file is, and what it is not

**This file contains workflow architecture only.** It defines how Claude should approach a VAT return classification task: the order of operations, how to handle ambiguity, what to produce as output, what to check before delivering. It contains no legal content, no tax rates, no return form structures, no refusal triggers tied to any particular jurisdiction, no supplier patterns.

**This file must always be loaded with two other files:** a regional or directive layer that provides the legal framework (e.g., `eu-vat-directive` for EU member states), and a country-specific layer that provides the national implementation (e.g., `germany-vat-return`, `malta-vat-return`). This file alone cannot produce a VAT return. Loading it without companion files is a configuration error and Claude must refuse to proceed.

**This file is the contract.** When a country skill or a regional skill says it conforms to v0.1 of this base, what they mean is: they fill the country slots specified in Section 7, they produce outputs in the format specified in Section 3, their classifications can be validated by the self-checks in Section 5, and they participate in the workflow in Section 1.

---

## Section 1 — The workflow (read this first, follow exactly)

You are helping a small business owner prepare a VAT return. The output will be reviewed by a warranted accountant before filing. Your job is to do the mechanical classification work and produce a working paper plus a reviewer brief that makes the human reviewer's job fast and accurate.

Execute these nine steps in order. Do not skip. Do not reorder. Do not start classifying transactions before step 4. Do not build any output files before step 7.

**The fundamental ordering principle:** ask the user about ambiguities BEFORE building the workbook, not after. The workbook is built once, with the user's answers already incorporated. There is no v1 conservative-default workbook that gets thrown away — the only workbook the user ever sees is the final one. This is different from earlier versions of this workflow base (v0.1.x) where the workbook was built first and questions came at the end. The new ordering eliminates the wasted work of building a workbook the user is going to invalidate by answering questions, and it makes the question form a real interactive step instead of an afterthought stapled onto the chat response.

### Step 1 — Confirm the companion skills are loaded

This workflow base requires two companion files:
1. **A regional or directive layer** providing the legal framework (e.g., `eu-vat-directive` for EU member states)
2. **A country-specific skill** providing the national implementation (e.g., `germany-vat-return`)

If either is missing, stop and tell the user: "I need a regional VAT layer and a country-specific skill loaded alongside this workflow base. Which jurisdiction is this return for?" Do not proceed without both.

### Step 2 — Read the data

The user will provide a bank statement (CSV, PDF, or pasted text). Read every line. Do not skim. Identify:

- The period covered (first transaction date to last)
- The currency (must match the country's currency or be flagged as a currency conversion case)
- The number of transactions
- Any obvious format problems (missing columns, truncated data, unreadable encoding)

If the data is unreadable, in the wrong currency without conversion documentation, or covers a different country than the loaded skills, stop and tell the user.

### Step 3 — Infer the client profile from the data

Before asking the user any onboarding questions, attempt to infer the client profile from the bank statement alone. Look for:

- **Entity type signals.** Owner withdrawals, drawings, private transfers → sole proprietor / self-employed individual. Salary payments to multiple non-owner names → company with employees. Single recurring director-salary payment → single-director company.
- **Location signals.** Bank name, tax authority name in payment descriptions, recurring local supplier addresses, fuel station locations, the country code on counterparty IBANs.
- **Tax identifiers.** VAT number / tax registration number leaked in invoice descriptions (commonly visible on advertising platform billing, cloud service billing, marketplace fee descriptions). Tax authority reference numbers in payment descriptions.
- **Period and frequency.** First and last transaction dates. Filename if helpful.
- **Business activity.** Customer mix (recurring B2B invoices vs. one-off vs. consumer-looking), software stack (consulting toolkit vs. e-commerce toolkit vs. retail point-of-sale), travel patterns, presence of a fixed office cost or just flexible workspace memberships.
- **Employees.** Wage outgoing patterns, social-security or payroll-tax contributions to known statutory bodies (specific names provided by the country skill).
- **Property.** Recurring rent payments, mortgage payments, utility patterns suggesting a fixed premises. Absence of these suggests no fixed location (home office, coworking).
- **Cross-border activity.** Foreign IBANs on incoming payments, foreign currency lines, foreign supplier names.
- **Maturity signals.** Recurring monthly invoices from the same customers and a stable software stack suggest an established business. Sparse activity, ramp-up patterns, or many one-off transactions suggest a new or seasonal business. This affects how to interpret round-number transfers, owner injections, and unexplained gaps.
- **Description-level classification signals.** The transaction description (Buchungstext, Verwendungszweck, or equivalent) frequently contains the answer to category questions. Words like "Consulting", "Beratung", "Logo Design", "Workshop", "Renovierung Büro", "Bewirtung", "Geschäftsessen", "Mobilfunk Rechnung Büro", "shipped to [country]" are themselves classification signals. **If a description contains a keyword that maps to a category in the country skill's Tier 1 rules or supplier pattern library, treat the description as answering the question. Do not escalate to the user.** For example: a sale to a UK or US counterparty with "Consulting" in the description is unambiguously a §3a(2) service to a non-EU B2B customer — classify silently as Kz 45 and do not ask whether it was services or goods. A purchase from a marketplace platform with "Logo Design" in the description is unambiguously a marketing/branding service for a business with a consulting profile — apply the deductible default and do not ask whether it was business purpose.

Produce a one-paragraph inferred profile. State it as a hypothesis, not a fact.

### Step 4 — Confirm the inferred profile (one round trip)

Output the inferred profile to the user in this exact form:

> "Based on the bank statement, here is what I believe about your situation:
> 
> [One paragraph: entity type, location, tax IDs if found, period, business activity, employee status, property status, cross-border footprint.]
> 
> Is this correct? If anything is wrong, tell me and I will adjust before I start classifying. If it is correct, reply 'confirmed' and I will proceed."

Wait for confirmation. If the user corrects anything, update the profile and re-confirm in one sentence ("Updated: [change]. Proceeding."). Do not ask the full onboarding questionnaire from the country skill at this stage — only ask follow-ups for items the data could not infer at all.

### Step 5 — Run refusal checks

Before classifying any transaction, check the confirmed client profile against the refusal catalogues from both companion skills (the regional layer's catalogue and the country layer's catalogue). If any refusal trigger fires, stop immediately, output the refusal message verbatim, and end the conversation. Do not attempt partial classification.

### Step 6 — Classify deterministically against the country skill

For every transaction in the bank statement, in order:

1. **First, exclusion check.** Apply the country skill's exclusion patterns (transfers to own accounts, drawings, payroll, tax payments, bank fees, statutory contributions). If the line matches an exclusion, mark it excluded with the reason and move on.
2. **Second, supplier pattern lookup.** Check the counterparty against the country skill's supplier pattern library (a literal lookup table). If the counterparty matches a pattern, apply the deterministic treatment from the table. Do not second-guess the table.
3. **Third, deterministic Tier 1 rules.** If no supplier pattern matched, check the country skill's Tier 1 classification rules together with the regional layer's harmonized rules. If a rule applies unambiguously from the data alone, apply it.
4. **Fourth, Tier 2 ambiguity.** If neither supplier pattern nor Tier 1 rule resolves the line, mark it as Tier 2 ambiguous and apply the conservative default from the country skill in your working memory. **Do not write the workbook yet.** Tier 2 lines are queued for Step 6.5, where the user will be asked about them via the `ask_user_input_v0` tool. The user's answer in Step 6.5 either confirms the conservative default or replaces it with a different treatment, and Step 7 then writes the workbook with the final treatment for every line.

Every transaction MUST end up in exactly one of these states: excluded with reason, classified deterministically, or marked as Tier 2 with a default applied and queued for Step 6.5. No transaction may be silently dropped. At the end of Step 6 you have a list of all classifications in working memory and a list of Tier 2 rows that need user input. The workbook does not exist yet. Do not build it until Step 7.

### Step 6.5 — Ask the user about Tier 2 ambiguities via the question tool

Before building any output files, you MUST present the Tier 2 ambiguities to the user and get their answers. The questions are presented as tappable UI via the `ask_user_input_v0` tool, NOT as a free-text question form in the chat response. Tappable questions have substantially lower friction than typed answers, which is why the v0.1.x design (free-text form at the end of the chat response) is replaced by this step.

**The targeting principle.** Step 6.5 is built for `claude.ai` and the official Claude apps (web, desktop, mobile), where the `ask_user_input_v0` tool renders as interactive buttons. If the tool is not available in the runtime, do not fall back to a free-text form — instead, halt and tell the user: "This skill requires an interactive UI for the question form, which is available in claude.ai and the Claude apps. Please run this skill from one of those surfaces." Trying to support both surfaces in the same skill produces complexity that pays no benefit.

**The filtering rule.** Not every Tier 2 row becomes a question. Apply the rules from Section 4 (the question form rules) to filter the Tier 2 list:

1. **Below the cash floor.** If the Tier 2 row's cash impact is below the country skill's question threshold (a country slot — defaults to €50 of input/output VAT for eurozone member states if the country skill does not specify), do not ask. Apply the conservative default and disclose in the brief.
2. **No-effect rule.** If the row's outcome is the same regardless of how the user answers (e.g., a German B2C vs B2B sale where both go to Kz 81 at 19%), do not ask. Apply the conservative default and disclose in the brief.
3. **Description-answered rule.** If Step 3's description-level inference should have classified this row silently, the row should never have been Tier 2 in the first place. Re-read the description and reclassify silently.

After filtering, group Tier 2 rows that share the same question. Multiple Telekom mobile lines all asking "what's the business use percentage" become one question covering all the lines, not three separate questions.

**The grouping by cash impact.** Order the surviving questions by cash impact, descending. The highest-impact question is the first one presented. The user sees the most consequential decision first.

**The tool format constraint.** The `ask_user_input_v0` tool takes 1-3 questions per call, each with 2-4 mutually exclusive options. This is a hard constraint and it is also a design forcing function. If you cannot reduce a question to 4 options, the question is too vague and you need to either split it into two questions or collapse some options.

The tool format for each question:

```
question: "[Plain language question naming the line(s) and the cash impact]"
options:
  - "[Most likely answer — the conservative default, labelled with what it means]"
  - "[Second most likely answer — the cash impact of choosing this]"
  - "[Third option if applicable]"
  - "[\"Don't know\" / \"Apply default\" — the safety option]"
type: "single_select"
```

A "don't know" or "apply default" option MUST be present on every question. The user is allowed to skip any question by selecting the safety option, in which case the conservative default stands. This is the equivalent of skipping a free-text question, but it is an explicit click rather than a silent omission.

**Worked example (German Q1 hypothetical, illustrative only — NOT drawn from any test fixture):**

Tier 2 row: a single intra-Community supply of goods to a French customer, €15,000, with the description suggesting goods shipped but the five §6a UStG conditions unverified.

```
question: "An intra-Community supply of goods to a French customer for €15,000 (the largest single line on your return) — what's the status of the §6a zero-rating conditions?"
options:
  - "All five conditions met (VIES verified, transport proof, invoice format correct, customer in another EU member state, dispatch documented) — keep at Kz 41 zero-rated"
  - "Some conditions uncertain — keep at Kz 41 with a reviewer flag, the reviewer will verify before filing"
  - "One or more conditions failed — flip to Kz 81 19% (€2,394.96 additional output VAT)"
  - "Don't know — apply conservative default (Kz 41 with reviewer flag)"
type: "single_select"
```

The user taps once. Their answer becomes part of the answer set that Step 7 uses to build the workbook. If they tap option 3, the workbook is built with the line at Kz 81 19% from the start — no v1 workbook with the wrong treatment, no regeneration, no waste.

**Tool call sequencing.** If you have 1-3 questions, fire one tool call. If you have 4-6 questions, fire two tool calls (3+3 or 3+2 or 2+2 — group by cash impact). If you have 7+ questions, that is a signal that either your filtering is too lax or you should consider firing the excessive-ambiguity refusal (R-EU-12). The hard ceiling is still 10 questions across all tool calls in the conversation. Above 10, fire R-EU-12.

**Wait for answers.** After firing the tool, wait for the user's response. The user's answers come back as their next message — each answer corresponds to a question by index. Capture the answer set and proceed to Step 7.

**Output of Step 6.5.** A complete answer set covering every Tier 2 row that survived filtering. Rows below the cash floor or excluded by the no-effect rule have their conservative defaults locked in without being asked. Rows the user answered "don't know" on also have their conservative defaults locked in. Rows the user answered substantively have the user's answer locked in. The answer set is now the input to Step 7.



### Step 7 — Build the outputs

By the time you reach Step 7, you have a complete classification for every row in working memory: deterministic for Tier 1 rows, user-answered for Tier 2 rows that were asked in Step 6.5, conservative-default for Tier 2 rows that were filtered out or where the user selected "don't know." The workbook is built once, with the final treatment for every row already locked in. There is no v1/v2 distinction — there is one workbook and it is the deliverable.

Produce two artefacts in this order. Step 7 has internal sub-steps that MUST all be completed before Step 7.5 begins.

**Artefact 1 — The Excel working paper.** Follow the output specification in Section 3. Use the country skill's template for sheet structure. Use live formulas, not hardcoded values. This artefact has THREE sub-steps and Step 7 is not complete until all three have executed:

  - **7.1.a — Write the workbook.** Use openpyxl (or equivalent) via `bash_tool` to create the file at `/mnt/user-data/outputs/<country>-vat-<period>-working-paper.xlsx`. The file MUST be a real `.xlsx` file on disk. Do not substitute markdown tables in the chat response for the Excel file. If you cannot create the file because the runtime does not provide `bash_tool` or `create_file`, stop immediately and tell the user: "This skill requires file creation tools to be enabled. Please enable Code Execution in your Claude settings, then try again." Do not proceed to a degraded markdown-only output.

  - **7.1.b — Run the recalc script.** Immediately after writing the workbook, run `python /mnt/skills/public/xlsx/scripts/recalc.py /mnt/user-data/outputs/<country>-vat-<period>-working-paper.xlsx` via `bash_tool`. This is NOT optional. The script computes every formula in the workbook and caches the results so that downstream tools (and the model's own self-checks) can read the actual numeric values rather than the formula text. Skipping this step produces a workbook where the cached values are all `None` and the self-check in Section 5 (Check 3) cannot pass. The recalc command is part of the build, not a follow-up note — the workbook is not "built" until recalc has been run on it.

  - **7.1.c — Verify zero formula errors.** Read the JSON output from recalc.py. It MUST contain `"status": "success"` and `"total_errors": 0`. If the JSON shows any errors, the formulas have bugs — fix them in the workbook, re-run recalc, and verify again. Loop until zero errors. Do not proceed to Artefact 2 until 7.1.c reports success. The bottom-line figure on the Return Form sheet is not knowable until recalc has run successfully.

**Artefact 2 — The reviewer brief as markdown.** Follow the template in Section 3. Save to `/mnt/user-data/outputs/<country>-vat-<period>-reviewer-brief.md`. The brief MUST cite the bottom-line Kz 83 figure read from the recalculated workbook (i.e., from the cached value on the Return Form sheet after step 7.1.c), not from the model's own arithmetic. If the brief and the workbook disagree on the bottom line, the workbook wins and the brief is wrong — fix the brief.

The brief MUST also document, for every Tier 2 row, the source of its final treatment. Each row falls into one of four buckets:
  - **User-answered (substantive).** The user picked a non-default option in Step 6.5. Record the question, the user's answer, and the resulting treatment.
  - **User-answered (don't-know / apply-default).** The user explicitly selected the safety option. Record the question, the fact that the user selected don't-know, and the conservative default that was applied.
  - **Filtered out — below cash floor.** The Tier 2 row was below the country skill's question threshold. Record the row, the conservative default, and the cash impact (which by definition is below the threshold).
  - **Filtered out — no-effect rule.** Both possible answers led to the same Kz at the same rate, so the question would not have changed the return. Record the row and the conservative default.

This is the disclosure-in-the-brief side of the disclose-vs-ask distinction from Section 2 of this base. Step 6.5 is where user-facing ambiguities get resolved; the brief is where every Tier 2 default — regardless of whether it was asked — is recorded for the human reviewer.

The complete Step 7 sequence is: 7.1.a write → 7.1.b recalc → 7.1.c verify → Artefact 2 (write brief). Four tool calls minimum: bash openpyxl (or create_file) for the workbook, bash recalc, bash verification read, create_file for the brief. If any of these is missing, Step 7 is incomplete and Step 7.5 cannot start. Note that present_files does NOT happen in Step 7 — it happens in Step 9 after the self-checks are complete, so that the user is only ever shown a workbook that has passed both the line-by-line review and the structural self-check pass.

### Step 7.5 — Line-by-line review pass (in-conversation audit)

Before running the structural self-checks in Step 8, you MUST walk every row of the Transactions sheet of the workbook you just built and apply an explicit review check to each row. This step exists because the most common error mode in VAT classification is *attention failure*, not knowledge failure: high-cash-impact lines (the €15k intra-Community supply, the €1,899 capital asset) draw attention away from medium-cash-impact lines, and the medium-cash-impact lines carry small but real errors (a €35 hallucinated input VAT on a chamber dues line, a €62 hallucinated input VAT on an international flight). These errors hide in long lists of substantively correct lines and they survive both spot-check review and the structural self-checks in Step 8 unless you walk every line individually.

This step is NOT a separate auditor file. It is a self-check pass run by you, in the same conversation, immediately after Step 7 completes. The shift in your role from preparer to reviewer is achieved by the change in instructions, not by a change in conversation. For the duration of Step 7.5, you are reviewing your own work with adversarial intent — you are looking for what's wrong, not confirming what's right.

**The review protocol — apply to every row in order, no exceptions, no sampling:**

1. **Read the row.** Date, counterparty, description, gross amount, the Kz you assigned, the treatment text, the default flag.

2. **Ask: "Would the actual invoice from this supplier carry VAT at the rate I claimed?"** This is the single most important question in the review pass. If you claimed input VAT recovery on this line, the underlying invoice must actually contain VAT charged at that rate. If the supplier is in a category that does not charge VAT — statutory contributions to public-law bodies (chamber dues, professional licensing fees, statutory pension contributions), exempt-without-credit supplies under Articles 132/135 (insurance, financial services, healthcare, education, residential rent, postage stamps, gambling), international passenger transport zero-rated under national implementations of Article 148, government fees and licensing, donations and grants, statutory health insurance — then the invoice does not contain VAT and your input VAT claim is hallucinated. Flag the row for correction. The country skill's supplier pattern library and refusal catalogue list the country-specific zero-VAT categories; the directive layer lists the EU-wide ones. Read both with this question in mind for every row.

3. **Ask: "Did the description carry information I should have used but didn't?"** Re-read the Buchungstext / Verwendungszweck / equivalent. If a word in the description (Consulting, Beratung, Workshop, Logo Design, Bewirtung, Geschäftsessen, Renovierung Büro, shipped to [country], Kontoführungsgebühr, Mitgliedsbeitrag, Versicherung, Beitrag) maps to a treatment in the country skill, did your classification reflect it? If you classified a line as "B2B vs B2C unknown — defaulted to B2C" but the description says "Workshop Teilnahme" (which is a generic term that doesn't disambiguate) you may have done the right thing. If you classified a line as "services or goods unknown" but the description literally says "Consulting Jan 2026," you didn't read the description and the line should be reclassified silently. Flag for correction.

4. **Ask: "Is the Kz / box assignment what the country skill's supplier pattern library says it should be?"** If the supplier is in the library, your treatment must match the library's entry. If you departed from the library, you need a documented reason in the treatment text — and the reason must be that the data shows something the library couldn't anticipate, not that you forgot to look. If the supplier is not in the library, what general rule did you apply? Is it the right rule? Country skills' supplier pattern libraries exist to encode the answers to exactly these questions; the most common reason for an error in this category is that you applied a general rule instead of looking up the specific supplier.

5. **Ask: "Is the cross-border treatment correct?"** If the counterparty name suggests a non-domestic entity (foreign country in name, foreign address in description, foreign currency, foreign VAT prefix on the invoice), did you apply the right place-of-supply rule? Services to non-EU B2B customers go to the local "non-taxable supply outside scope" box (Kz 45 for Germany, equivalent for other countries), not to a domestic sales box and not to an intra-Community services box. Goods shipped to another EU member state go to the intra-Community supply box only if all five Article 138 conditions are met; if any condition is unverified, the conservative default is domestic sales at the standard rate. EU SaaS suppliers (Google IE, Microsoft IE, Adobe IE, Slack IE, etc.) bill from Ireland or Luxembourg with reverse charge; you self-account at the customer member state's rate, not at the supplier's rate.

6. **Ask: "Did I apply the right conservative default, and did I disclose it?"** Every row with the Default flag set to Y must have a disclosure in the reviewer brief listing the alternative treatment and the cash delta. If the Default flag is set but the brief doesn't have an entry for this row, the disclosure is missing and the row needs to be added to the brief. If the disclosure is present but the alternative treatment is wrong (e.g., the disclosure says "alternative is 19% recovery" but the conservative default already gives 19% recovery), the disclosure is meaningless and the row needs revisiting.

7. **For the highest-cash-impact rows (top 10 by absolute gross amount), do all six checks above plus an additional check:** read the country skill's worked example most relevant to this row's category, and verify your treatment matches the worked example's pattern. If the row is an intra-Community supply, read the country skill's intra-Community supply worked example. If the row is an AWS branch-billing case, read the AWS exception worked example. If the row is a high-value capital asset, read the capital goods scheme worked example. The worked examples exist for exactly this verification step.

**Output of Step 7.5:** an in-memory list of rows that failed any of the six checks, with one line each describing what failed and what the correction is. If the list is non-empty, you MUST update the workbook (re-run Step 7's sub-steps 7.1.a through 7.1.c with the corrections applied), update the brief, and re-run Step 7.5. You may not proceed to Step 8 until Step 7.5 produces an empty failure list.

**Time budget:** for a 73-line bank statement, Step 7.5 should take roughly the same number of attention units as Step 6 (the original classification pass), because you are walking every row a second time. This is intentional. Step 7.5 is not a quick check; it is a full re-pass with adversarial intent. If you find yourself rushing, you are doing it wrong — slow down and apply the six checks rigorously.

**What Step 7.5 does NOT do:** it does not re-derive the law from primary sources (that's a future enhancement, not in scope for v0.1.3). It does not call external tools for verification. It is a same-model, same-data, same-conversation review pass whose value comes entirely from forcing equal attention on every row regardless of cash impact. It catches attention failures well; it catches knowledge failures only when the model's training data correctly contains the relevant fact. The honest scope of Step 7.5 is the IHK / Lufthansa / Amazon-LU class of error — errors where the classifier *knew* the rule but didn't apply it to the specific row because attention was elsewhere.

### Step 8 — Self-check before delivering

Run the 14 self-checks in Section 5 of this base against the workbook produced in Step 7 and the brief produced in Step 7. If any check fails, fix the output and re-run Step 7.5 followed by Step 8 again. Only proceed to Step 9 when all 14 checks pass. Step 8 is a structural gate, not a quality bar — it catches things like missing rows, broken formulas, missing brief sections, and arithmetic mismatches. The substantive review happened in Step 7.5; Step 8 is the structural backstop.

### Step 9 — Present the files and write the closing chat response

Only after Steps 6, 6.5, 7, 7.5, and 8 have all completed cleanly do you present the workbook and brief to the user.

**9.1 — Call `present_files`** with both file paths in this order:
1. The Excel working paper at `/mnt/user-data/outputs/<country>-vat-<period>-working-paper.xlsx`
2. The reviewer brief at `/mnt/user-data/outputs/<country>-vat-<period>-reviewer-brief.md`

The workbook is listed first because it is the primary deliverable. The user cannot see the files until `present_files` has been called on them. Saving them to `/mnt/user-data/outputs/` is necessary but not sufficient.

**9.2 — Write a short closing chat response.** The chat response is brief by design — three to five sentences total — because the deliverables are the files, not the chat. The chat response covers:

- The bottom-line figure (Kz 83 for Germany, equivalent box for other countries), read from the cached value in the workbook, not computed in the chat. State it as "X payable" or "X refundable" with the currency.
- A one-sentence summary of what's in each file.
- A one-sentence flag for the highest-priority item in the reviewer brief — typically the largest single Tier 2 default that the user took from Step 6.5 (or the largest cash-impact line that was filtered out below the cash floor).
- An optional one-line invitation to revise: "If you need to change any of your earlier answers, tell me which question and I'll regenerate the workbook with the updated treatment."

**Do NOT include the question form in Step 9.** The questions already happened in Step 6.5. Re-asking them in Step 9 would be a regression to the v0.1.x design. The chat response in Step 9 is purely a delivery message, not an interactive prompt.

**9.3 — Optional: handle a revision request.** If the user responds to your closing chat message with "actually, on Q3 the answer should have been X," treat that as a revision request and re-run Steps 7, 7.5, 8, and 9 with the updated answer set. This is the only place the workbook is regenerated, and it is gated on the user actually wanting a revision rather than running on every conversation. Most users will not request a revision, and the cost of the second workbook generation in the rare case where they do is acceptable because it's motivated by new information.

---

## Section 2 — Two-tier rule and conservative defaults

Every transaction you classify falls into one of two tiers. There is no third tier.

**Tier 1 — you know.** The country skill's rules and the regional layer's rules clearly apply, the data carries every fact you need, and a careful reader of the same sources would reach the same conclusion. Classify silently. Do not narrate the rule. Do not add a question to the form.

**Tier 2 — you do not know.** Either (a) the law is clear but the data does not carry the fact you need (counterparty type, business-use percentage, customer VAT verification, etc.), or (b) the public sources themselves are unclear or silent on this case. You MUST do all three of the following, in order, with no exceptions:

1. **State the ambiguity** in one sentence in the reviewer brief.
2. **Apply the conservative default** from the country skill — the option that costs the user more tax, never less.
3. **Decide whether to add a question to the structured form (Section 4) or only disclose in the reviewer brief.** Not every Tier 2 ambiguity requires a user-facing question. Add the question to the form ONLY if both of the following are true:
   - **(a) The cash impact is at or above the country skill's question threshold** (a country slot — defaults to €50 of input/output VAT for eurozone member states if the country skill does not specify). Below this threshold, apply the default and disclose in the brief without asking.
   - **(b) The user has information the data does not contain.** If the answer is something only the user can know (vehicle business-use percentage, restaurant attendees and purpose, whether an Apple ID is personal or business), include it on the form. If the answer is in the description and you simply did not look (Step 3 of the workflow exists to prevent this), do not ask — re-read the description and classify silently.

If either (a) or (b) fails, the ambiguity goes to the reviewer brief only — not to the user form. Ask yourself before adding any question to the form: "Would a careful human reviewer reading the description reach the same default conclusion I did, or do they need information from the user that isn't on the bank line?" If the reviewer would reach the same conclusion, the question is for the brief, not the form.

You may not silently apply a default *without* disclosing it. You may not ask a question *without* applying a default. The disclosure-in-the-brief is mandatory for every Tier 2 default; the question on the user form is conditional on cash impact and on whether the user genuinely has the answer.

**Conservative defaults — universal principle.** When uncertain, choose the treatment that costs the user more tax. The country skill specifies the concrete defaults for each ambiguity type. The principle behind them is constant:

- Unknown rate on a sale → standard rate
- Unknown VAT status of a purchase → not deductible
- Unknown counterparty country → domestic
- Unknown customer status (B2B vs B2C) → B2C and charge VAT
- Unknown business-use proportion → 0% recovery
- Unknown blocked-input status → blocked
- Unknown whether a transaction is in scope → in scope

The reviewer can correct an over-payment after the fact. The reviewer cannot easily recover from an unreported liability surfacing in audit.

---

## Section 3 — Output specification

Three outputs per VAT return. All three are mandatory. Never produce one without the others.

### Output 1 — Excel working paper

The country skill provides a sheet structure template. The base requires the following minimum:

**Sheet "Transactions"** — one row per bank statement line, columns:

| Column | Content | Color convention |
|---|---|---|
| A | Date | Black |
| B | Counterparty | Black |
| C | Description | Black |
| D | Gross amount | Blue (hardcoded input from bank) |
| E | Net amount | Black (formula or input) |
| F | VAT amount | Black (formula or input) |
| G | Rate applied | Black |
| H | Box code / line code | Black |
| I | Treatment label | Black |
| J | Default applied? (Y/N) | Black, yellow background if Y |
| K | Question reference (linked to brief) | Black |
| L | Excluded? Reason if yes | Black |

Every transaction in the bank statement appears as one row. Excluded transactions have a reason in column L and zero in columns E, F, H. Tier 2 transactions have "Y" in column J and a question reference in column K.

**Sheet "Box Summary"** — one row per box code on the country's return form, with the total computed via `=SUMIFS()` formula referencing Sheet "Transactions" column H. The country skill provides the list of valid box codes for that country. Formulas, not hardcoded values. Use the xlsx skill's color conventions: black text for formula cells.

**Sheet "Return Form"** — the final return-ready figures, structured to match the country's actual return form layout. Cross-sheet references to the Box Summary sheet, in green text per xlsx convention. The bottom-line payable/refundable figure is a single labelled cell.

**Color conventions** (from the xlsx skill):
- Blue text: hardcoded inputs from the bank statement
- Black text: formulas
- Green text: cross-sheet references
- Yellow background: cells requiring reviewer attention (any row where a default was applied)

**After building the workbook**, run `python /mnt/skills/public/xlsx/scripts/recalc.py <filename>` to recalculate all formulas and check for errors. If the output JSON shows `errors_found`, fix the errors and re-run until `status` is `success`. Only then present the file via `present_files`.

**File location.** Save to `/mnt/user-data/outputs/<country>-vat-<period>-working-paper.xlsx` and present via the `present_files` tool.

### Output 2 — Reviewer brief (markdown)

A short narrative document that gives the human reviewer the context they need to verify the working paper efficiently. Follow this exact template:

```markdown
# [Country] VAT Return — Reviewer Brief
**Period:** [period]  
**Generated:** [date]  
**Source data:** [bank statement file name]  
**Underlying invoices seen:** [yes / no / partial]

## Bottom line
- **[Box code for final figure]**: [amount] [currency] [payable / refundable]
- Total output VAT: [amount]
- Total input VAT: [amount]
- Total transactions classified: [count]
- Of which Tier 2 with default applied: [count]
- Of which excluded: [count]

## High flags (review first)
[Numbered list of items with cash impact > country skill's HIGH threshold, or Tier 2 defaults with potential swing > country skill's HIGH tax-delta threshold. Each item: one sentence what, one sentence why it matters, one sentence what the reviewer should do.]

## Medium flags
[Numbered list of secondary items: counterparty concentration above threshold, more than 5 conservative defaults, items at category boundaries.]

## Low / informational flags
[Period total approaching review threshold, related filings triggered (e.g., EC Sales List equivalent), unusual but not high-impact patterns.]

## Conservative defaults applied
[For each Tier 2 default: one line. Format: "[transaction date] [counterparty] [amount] — defaulted to [treatment] because [reason]; alternative if user confirms otherwise: [alternative treatment]."]

## Invoices the reviewer should pull
[List of specific invoices the reviewer needs to verify before signing off. Not generic "verify invoices" — specific items.]

## Refusal triggers checked and cleared
[Confirmation that no refusal triggers fired, listing every R-code from both the regional layer and the country layer, with a one-sentence note on why each was cleared.]
```

**File location.** Save to `/mnt/user-data/outputs/<country>-vat-<period>-reviewer-brief.md` and present via `present_files`.

### Output 3 — Chat response

The chat response is short and serves three purposes:

1. **Bottom-line summary.** Two or three sentences. The figure (read from the workbook, not computed in the chat), the period, the most important caveat.
2. **Pointers to the two files**, presented via the `present_files` tool, with one sentence each on what they contain.
3. **Optional one-line revision invitation.** "If you need to change any of your earlier answers, tell me which question and I'll regenerate the workbook." This is the safety valve for the user-changes-their-mind case described in Step 9.3.

Do not include the question form in the chat response. The questions happen earlier in the workflow, in Step 6.5, via the `ask_user_input_v0` tool. By the time Output 3 is being written, the user has already answered. The chat response is a delivery message, not an interactive prompt.

Do not repeat the working paper contents in chat. Do not duplicate the reviewer brief. The chat response is a navigation aid, not a third copy of the output.

---

## Section 4 — The question form (tool-based, runs in Step 6.5)

Tier 2 ambiguities are presented to the user as tappable UI via the `ask_user_input_v0` tool, NOT as a free-text form embedded in a chat response. This is a v0.2.0 design change from the v0.1.x free-text form. The tappable UI has dramatically lower user friction than typed answers, which means the user is far more likely to answer every question rather than skipping the form. It also forces the questions to be sharper, because each option must be a discrete choice rather than an open prompt.

This section defines the rules for filtering Tier 2 rows into questions, the format for each tool call, and the constraints the tool format imposes on question design.

**Where this section runs in the workflow.** Step 6.5 of the workflow in Section 1. The questions are presented BEFORE Step 7 builds the workbook, so the workbook is built once with the user's answers already incorporated. There is no v1/v2 workbook split.

**Targeting.** This skill targets `claude.ai` and the official Claude apps where `ask_user_input_v0` renders as interactive buttons. If the tool is unavailable, halt and tell the user that this skill requires claude.ai or a Claude app to run. Do not fall back to a free-text form.

### Filtering rules — which Tier 2 rows become questions

Not every Tier 2 row becomes a question. Apply these rules in order to filter the Tier 2 list before generating tool calls:

1. **Description-answered rule.** If Step 3's description-level inference should have classified this row silently, the row should never have been Tier 2 in the first place. Re-read the description and reclassify silently before falling through to the question form. This is a regression check on the Step 3 inference, not a real filter.

2. **Cash floor.** If the row's cash impact is below the country skill's question threshold (a country slot — defaults to €50 of input/output VAT for eurozone member states if the country skill does not specify), do not ask. Apply the conservative default and disclose in the brief.

3. **No-effect rule.** If both possible answers to the question lead to the same box code at the same rate (e.g., a German B2C vs B2B sale where both go to Kz 81 at 19%), do not ask. The question is for the user's records, not the return.

4. **Grouping.** Multiple Tier 2 rows that share the same question (e.g., three Telekom mobile lines all asking "what's the business use percentage") become one question covering all the lines, not three separate questions.

5. **Hard ceiling — 10 questions total across all tool calls.** If the surviving question count exceeds 10, fire R-EU-12 (excessive ambiguity) instead of asking. The 10-question ceiling exists because beyond 10 questions, the user's situation is too complex for this skill to handle reliably and the return should be escalated to a human practitioner.

### Tool call format

The `ask_user_input_v0` tool takes 1-3 questions per call, each with 2-4 mutually exclusive options. This is a hard constraint of the tool and it is also a design forcing function: if a question cannot be reduced to 4 options, it is too vague to ask.

**Format for each question:**

```yaml
question: "[Plain language question naming the line(s) by date/counterparty/amount, plus the cash impact of the most consequential answer]"
options:
  - "[Most likely answer — typically the conservative default, labelled with what it means]"
  - "[Second most likely answer — the cash impact of choosing this]"
  - "[Third option, if applicable]"
  - "[Don't know / apply default — the safety option]"
type: "single_select"
```

**Mandatory features of every question:**

- **Name the line(s) explicitly.** Never ask "what about that fuel transaction" — always "the four Aral fuel lines totalling €196.90 from January-March." The user needs to know which line is being asked about without scrolling through anything.
- **Quantify the cash swing.** Every question must state the cash impact of the most consequential alternative. "Cash swing if 100% business: €43" or "Cash swing if Kz 41 fails: €2,395 additional VAT." Without the cash impact, the user cannot prioritize their attention.
- **A "don't know" or "apply default" option must be present.** The user is allowed to skip any question by selecting the safety option, in which case the conservative default stands. This is the equivalent of skipping a free-text question, but it is an explicit click rather than a silent omission. Skipping is a valid answer and the brief records it as such.
- **Options are mutually exclusive.** No "select all that apply" questions. If a row needs more than one decision, split it into two questions.

**Worked example (illustrative — NOT drawn from any test fixture):**

Suppose a hypothetical client has three mobile phone lines that need a business-use percentage decision.

```yaml
question: "Three mobile phone lines totalling €269.70 — what's the business use percentage?"
options:
  - "100% business with a contemporaneous mileage / call log — recover full input VAT (~€43)"
  - "Mixed-use with declared business percentage (you'll tell me the %)"
  - "Personal phone with occasional business calls — keep blocked at 0%"
  - "Don't know — apply conservative default (block at 0%)"
type: "single_select"
```

If the user picks option 2, the model needs to ask a follow-up question to get the percentage. That follow-up is its own tool call with a different question structure (could be free-text or could be ranges like "25%/50%/75%/other"). Do not try to cram the percentage into the first question's options.

### Tool call sequencing

- **1-3 questions.** One tool call. All questions in a single `ask_user_input_v0` call.
- **4-6 questions.** Two tool calls, sequenced. Group by cash impact: highest-impact questions in the first call, lower-impact in the second. The user answers the first call before the second call is fired.
- **7-10 questions.** Three or four tool calls, sequenced. Same grouping principle. This is the maximum the skill should ever produce; beyond 10 questions, fire R-EU-12.
- **Above 10.** Do not ask. Fire R-EU-12 (excessive ambiguity refusal). The conversation ends with the refusal message; no workbook is built.

### What the rules NO LONGER apply

The v0.1.x rule "one form per conversation, not three batches" is replaced by the tool sequencing above. Multiple tool calls are fine — each call is a tappable UI moment, not a batch in the v0.1.x sense. The user experience is: answer 3 questions, then 3 more, then 2 more — not "answer one big form at the end."

The v0.1.x rule "form is presented in the chat response in Step 7" is gone. The questions happen in Step 6.5, before Step 7. The chat response in Step 9 is purely a delivery message and contains no question form.

The v0.1.x "Group A / Group B / Group C" labelling is gone. The tool format does not have group headers; questions are simply ordered by cash impact within each tool call.

The "Invoices the reviewer will need" list is no longer part of the question form (it never belonged there in the first place — it was a list of things the user could not answer). It moves to the reviewer brief as a dedicated section.

---

## Section 5 — Self-check before output

Run these fourteen checks against your draft output before sending the chat response. If any fails, fix the output and re-run. Do not deliver a return that fails any check. These checks are deterministic — they catch errors of execution and integrity, not errors of conceptual understanding. They are necessary but not sufficient. They are the cheapest reliability gain in the workflow and they must all pass.

### Structural integrity checks (always run first)

**Check 1 — Completeness.** Every transaction in the input bank statement appears exactly once in the Excel working paper, either classified or excluded with a reason. Count the rows in the input CSV; count the rows in Sheet "Transactions" of the workbook; they must match. If the CSV has 73 lines, Sheet "Transactions" must have 73 data rows. No silent drops.

**Check 2 — Arithmetic integrity.** The bottom-line figure on the Return Form sheet equals (sum of output VAT) − (sum of input VAT). The Excel formulas must compute this — do not assert it from your own arithmetic. If the recalc script returned errors, this check fails by definition.

**Check 3 — Recalc ran successfully.** You ran `python /mnt/skills/public/xlsx/scripts/recalc.py <filename>` against the working paper and the JSON output shows `status: success` with `total_errors: 0`. If recalc was skipped or returned errors, the working paper is not deliverable. Re-run and verify.

**Check 4 — Exclusion consistency.** Every transaction with a value in column L (excluded with reason) has zero in columns E (net), F (VAT), and H (box code). A transaction cannot be both excluded and classified. If a row has both an exclusion reason and a box code, one of them is wrong.

**Check 5 — No double-counting.** No transaction appears in two box codes. Each row in Sheet "Transactions" has exactly one value in column H (or is excluded). Verify by counting: the sum of (rows with a code in H) plus (rows with a value in L) equals the total row count.

### Cross-document consistency checks

**Check 6 — Default disclosure matches working paper.** Every transaction with "Y" in column J of Sheet "Transactions" has a corresponding line in the "Conservative defaults applied" section of the reviewer brief. Count them on both sides. They must match exactly. If the working paper has 9 defaults flagged and the brief lists 8, there is one default missing from disclosure.

**Check 7 — Question coverage.** Every Tier 2 ambiguity that drove a default has a corresponding question in the structured form, OR is in the "Invoices the reviewer will need" list, OR is grouped with other transactions of the same category under one question. No Tier 2 item is silently absent from all three.

**Check 8 — Tier 2 default values match the country skill.** For every transaction with "Y" in column J, the treatment in column I matches one of the conservative defaults documented in the country skill's quick reference table. The model cannot invent its own defaults. If the country skill says "unknown rate → standard rate" and the working paper applied a reduced rate as a default, that is a check failure.

### Country-skill compliance checks

**Check 9 — Supplier pattern compliance.** For every transaction whose counterparty matches an entry in the country skill's supplier pattern library, the treatment in column I and the box code in column H match the table's specified treatment for that pattern. Re-read the lookup table. Compare row by row. This check is the single most valuable one — it catches drift on cases the country skill explicitly wanted to be deterministic. If the lookup table says supplier X is "domestic standard rate" and the working paper has supplier X as reverse charge, this check fails.

**Check 10 — Reverse charge zero-net check.** For every transaction classified as reverse charge (the country skill specifies which box codes apply), the self-assessed output VAT equals the corresponding input VAT on the same line, *unless* the input recovery is partially blocked with an explicit reason in column I. €100 of output reverse-charge VAT with €0 of input recovery is either a missing input side or an undocumented block. Either fix it or document it.

**Check 11 — Related filings triggered.** For every transaction in a box that requires a related filing (for example, certain cross-border B2B transactions trigger an additional informational return separate from the main VAT return), the reviewer brief contains a note that the related filing is required for the period. The country skill specifies which box codes trigger which related filings. If Sheet "Transactions" has any line in such a box and the brief is silent on the related filing, this check fails.

**Check 12 — Period boundary.** Every transaction date in column A falls within the declared filing period. A Q1 return contains only dates between the period start and end inclusive. If any row has a date outside the period, either the period is wrong or the row should not be on this return.

**Check 13 — Currency consistency.** Every transaction is in the country's currency. If any line in the input had a different currency in the original CSV, it must either be excluded with a reason in column L or converted with the conversion rate documented in the brief. Silent assumption that everything is in the local currency is a check failure.

### Refusal trace

**Check 14 — Refusal sweep with named codes.** The reviewer brief contains an explicit refusal trace listing every refusal R-code from both the regional layer's catalogue and the country skill's catalogue, with a one-sentence note on why each was cleared for this client. Example: "R-XX-1 [refusal name]: cleared, user confirmed [relevant fact] in step 4. R-XX-2 [refusal name]: cleared, no [relevant signal] in the bank statement..." The trace is verbose but it makes the refusal handling auditable rather than asserted. Without it, the reviewer has to take the model's word that the checks were done.

### Failure handling

If any check fails, fix the output and re-run all fourteen. Do not deliver until all fourteen pass. If a check fails twice in a row on the same item, stop and report the failure to the user explicitly rather than attempting to silently work around it — repeated failure on the same check usually indicates a deeper bug in the classification that the model cannot fix on its own.

---

## Section 6 — How this workflow base interacts with companion skills

This base is one of three files that must be loaded together. The division of responsibility:

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

- **If the country skill says X and a regional layer says Y about the same fact:** prefer the country skill. National implementation governs.
- **If the country skill is silent on something the regional layer specifies:** apply the regional layer.
- **If the country skill is silent on something this workflow base specifies:** apply this workflow base.
- **If the workflow base specifies a workflow step that the country skill describes differently:** follow this base's workflow order, but use the country skill's content within that step.
- **If the user's situation triggers both a regional refusal and a country-specific refusal:** fire the country-specific refusal (it is more precise).

The country skill should not redefine the workflow, the output specification, the structured question form, or the self-checks. Those are owned by this base. If a country skill redefines them, treat the country skill as buggy and fall back to the base versions.

---

## Section 7 — Country slot contract

Every country skill loaded alongside this workflow base MUST provide the following. The country skill is incomplete without all of these. This base is incomplete without a country skill.

### Mandatory slots

1. **Standard VAT rate(s)** as a single number or list.
2. **Reduced VAT rate(s)** with a brief description of what they apply to.
3. **Return form name and field structure** — the exact box codes and what each one represents.
4. **Filing portal name** (the digital filing system the country uses).
5. **Filing deadlines** — the rules for monthly, quarterly, annual filings.
6. **Supplier pattern library** — a literal lookup table mapping common counterparty name patterns to their VAT treatment. Coverage must be comprehensive for the country's typical small-business counterparties. **Minimum 25 entries** for any country skill, with countries that have dense SaaS ecosystems or frequent edge cases expected to exceed 30. Mandatory categories: telecoms, utilities, banks, post and logistics, transport, food retail, fuel, restaurants, hotels, office supplies, coworking, government fees, insurance, major SaaS providers (Google, Microsoft, Adobe, Meta, AWS, Apple, Slack, Dropbox, Zoom, LinkedIn, Atlassian, Anthropic, OpenAI). The table is the authoritative pre-classifier — it overrides Tier 1 rules in case of conflict.
7. **Country-specific exclusion patterns** — the local-language patterns that mark a line as excluded (owner draws, wages, tax authority payments, statutory contributions).
8. **Country-specific refusal catalogue** — refusals on top of the regional layer's catalogue. Numbered as R-XX-1, R-XX-2, ... where XX is the country code.
9. **Tier 2 question catalogue** — for each ambiguity type, the question text, the conservative default, and how the answer changes classification. Used to populate the structured question form.
10. **Conservative default values** — the country-specific concrete defaults for each ambiguity type listed in Section 2 of this base.
11. **Worked examples** — minimum 6 fully worked transaction classifications drawn from realistic bank statement lines, each showing input → reasoning → output. These are pattern anchors for the model. **Worked examples must be drawn from a hypothetical client, not from any real test bank statement that will be used to validate the skill** — this prevents eval contamination.
12. **Excel template specification** — the country-specific column structure for Sheet "Transactions" (which box codes are valid in column H), the box list for Sheet "Box Summary", and the layout of Sheet "Return Form".
13. **Red flag thresholds** — country slot values that feed the reviewer brief: HIGH single-transaction threshold, HIGH tax-delta threshold for a single default, MEDIUM counterparty concentration threshold, LOW absolute-position threshold.
14. **Required inputs manifest** — minimum / recommended / ideal inputs and the refusal policy if the minimum is not met (HARD STOP or SOFT WARN).

### Optional slots

15. **Country-specific bank statement reading guide** — local CSV format conventions, common bank export quirks, language-specific field names.
16. **Sectoral notes** — patterns specific to common business types in that country.

If any mandatory slot is missing from the country skill, refuse to proceed and tell the user the country skill is incomplete.

---

## Section 8 — Reference material

### Validation status

This file is v0.1 of `vat-workflow-base`, drafted as part of the Accora skill architecture redesign in April 2026. It was extracted from `eu-vat-base` v0.3 by separating the workflow content (which is jurisdiction-agnostic and lives here) from the EU directive content (which is jurisdiction-specific to the EU and now lives in `eu-vat-directive`). No substantive workflow content was changed in the extraction — the file is a structural refactor, not a content revision.

### Origin

This file inherits its content from `eu-vat-base` v0.3 Sections 1, 2, 3, 4, 5, 7, and 8. The country slot contract in Section 7 of this file is the same 14 mandatory + 2 optional slots specified in the v0.3 base. The 14 self-checks in Section 5 of this file are the same 14 self-checks added to the v0.3 base. The workflow runbook in Section 1 of this file is the same 8-step runbook from the v0.3 base.

The only deletions from the v0.3 base content are: references to EU-specific concepts (which moved to `eu-vat-directive`), the 12 EU-wide refusals (which moved to `eu-vat-directive`), and EU-specific source citations.

### Known gaps

1. The 14 self-checks are deterministic but not exhaustive. They catch errors of execution and integrity, not errors of conceptual understanding. They are the foundation of the eval loop, not its only component.
2. The cautious confirmation step (Step 4 of the workflow) costs one round trip. If MVP testing shows users dropping off at this step, consider an opt-out for clearly unambiguous profiles.
3. The structured question form's 10-question maximum is a heuristic, not a measured optimum.
4. The Excel template structure has not yet been validated against real practitioner feedback for legibility.
5. The supplier pattern library minimum (25 entries) is a starting threshold and may need to be raised once we see how it performs across countries.

### Change log

- **v0.2.0 (April 2026):** Major architectural restructure — questions now happen BEFORE the workbook is built, not after. This is a workflow reorder, not a patch. The previous v0.1.x sequence was Step 6 (classify) → Step 7 (build workbook with conservative defaults) → chat response containing free-text question form → user answers nowhere because the workflow ends. This produced a workbook that was structurally already obsolete by the time the user finished reading the questions, plus a free-text form that users were likely to skim or skip because it required typing in chat. The v0.2.0 sequence is Step 6 (classify) → Step 6.5 (ask questions via `ask_user_input_v0` tool, tappable buttons) → Step 7 (build workbook ONCE with the user's answers already incorporated) → Step 7.5 (line-by-line review) → Step 8 (structural self-check) → Step 9 (present files + brief delivery message). The changes: Step 6.5 is new and is the entire question-form mechanism, restructured around the tappable tool; Step 7 produces only two artefacts (workbook and brief), not three (the chat response moves to Step 9); Step 9 is new and handles file presentation plus the closing message; Section 4 is rewritten end-to-end to describe the tool format, the filtering rules, and the tool sequencing rather than the free-text form template; Output 3 in Section 3 is updated to drop the question form reference. The targeting is `claude.ai` and the official Claude apps only; the skill halts if `ask_user_input_v0` is unavailable rather than falling back to the v0.1.x free-text form. The architectural justification: the v0.1.x ordering produced double work (build workbook with defaults, then either throw it away when the user answers or leave the user holding a stale file) AND high user friction (typed answers in chat are skippable in a way tappable buttons are not). The v0.2.0 ordering builds once, asks via UI, and the user gets the final workbook directly. No previous patch in v0.1.x is invalidated — Step 3's nine inference categories, Step 7's recalc gate, Step 7.5's line-by-line review pass, Section 4's filtering rules (cash floor, no-effect rule, description-answered rule), and the 14 self-checks all carry over unchanged. What changed is *when* the question form runs and *how* it presents itself to the user.
- **v0.1.3 (April 2026):** Added Step 7.5 — line-by-line review pass — between Step 7 (build outputs) and Step 8 (structural self-check). Step 7.5 is a same-conversation, same-model, in-workflow review pass that walks every row of the Transactions sheet with adversarial intent and applies six explicit checks per row (would the invoice carry VAT, did the description carry information, does the Kz match the supplier pattern library, is cross-border treatment correct, was the conservative default applied and disclosed, and for top-10 cash impact rows, does the treatment match the relevant worked example). Step 7.5 must produce an empty failure list before Step 8 can begin. This patch is the response to the diagnosis that the IHK and Lufthansa errors in earlier reruns were *attention failures* not *knowledge failures* — the model knew the rules, it just didn't apply them to the specific medium-cash-impact rows because attention was on the high-cash-impact rows. Step 7.5 forces equal attention on every row regardless of cash impact, which is what catches that error class. Step 7.5 explicitly does NOT call external tools and does NOT verify against primary sources — those are future enhancements outside v0.1.3 scope. The honest scope of Step 7.5 is attention failures only; knowledge failures (where the model lacks the relevant fact entirely) require a different mechanism that isn't in this patch. This patch replaces the previously planned separate `vat-audit-base` skill, which was dropped because (a) Claude as auditor has the same training-data blind spots as Claude as classifier, so a separate auditor catches knowledge failures no better than an in-workflow review pass would, and (b) the separate auditor pattern encouraged checklist-writing which led directly to the eval contamination problem identified in the v0.1 auditor draft.
- **v0.1.2 (April 2026):** Step 7 hardened against the recalc-skip failure mode. The first rerun of v0.1.1 produced a structurally correct .xlsx file with 112 live formulas but skipped the recalc.py step, leaving the cached values empty. The file worked when opened in Excel (which auto-recalculates) but failed Check 3 of the self-check suite (which depends on cached values being present) and was technically "uncomputed" until a human opened it. This patch rewrites Step 7 as three explicit sub-steps (7.1.a write, 7.1.b recalc, 7.1.c verify) with each one a hard gate before the next. The recalc command is now part of the build sequence rather than a follow-up note. Step 7 is not complete until all three sub-steps have executed and recalc reports `total_errors: 0`. Also added a runtime check at 7.1.a: if `bash_tool` or `create_file` is unavailable, the model stops with a clear message rather than degrading to a markdown-only output. No structural changes to the workflow architecture, the question form rules, the conservative defaults principle, or the country slot contract.
- **v0.1.1 (April 2026):** Three targeted patches in response to first rerun feedback. (1) Section 1 Step 3 added a ninth inference category — "description-level classification signals" — making it explicit that words like "Consulting", "Logo Design", "Bewirtung", "shipped to [country]" in the transaction description are themselves classification signals and that the model should classify silently rather than asking when the description carries the answer. (2) Section 2's two-tier rule was rewritten to distinguish disclosure-in-the-brief (mandatory for every Tier 2 default) from question-on-the-form (conditional on cash impact and on whether the user genuinely has information the data does not contain). (3) Section 4 added two new rules to the question form: a minimum cash-impact floor (questions below the country skill's threshold, defaulting to €50, must not appear on the form) and an explicit prohibition on questions whose outcome does not affect the return. The first rerun produced a 10-question form where 3-5 questions failed at least one of these rules; the patches close those loopholes. No structural changes to the workflow, output specification, country slot contract, or self-checks.
- **v0.1 (April 2026):** Initial draft as part of the three-tier architecture split. Extracted from `eu-vat-base` v0.3. No substantive changes from v0.3 — this is a structural refactor that separates workflow architecture from regional legal content.

### Self-check (v0.1 of this document, not the runtime self-check in Section 5)

1. Workflow at top of file: yes (Section 1, before metadata).
2. Imperatives not descriptions: yes.
3. Output specification mandates Excel + markdown + chat: yes (Section 3).
4. Structured question form is a literal template: yes (Section 4).
5. Self-check before output: yes (Section 5, fourteen checks).
6. No legal content, no jurisdiction-specific facts: yes (verified — no references to specific tax authorities, no specific rates, no specific box codes, no references to specific countries, no legal citations).
7. Country slots tightened: yes (Section 7, 14 mandatory + 2 optional).
8. Inferred-profile-first ordering: yes (Step 3 before Step 4 confirmation, no onboarding questionnaire upfront).
9. Loading model explicit: yes (Section 6).
10. Refusal handling delegated to companion skills: yes (this file contains no refusal catalogue — refusals are owned by the regional and country layers).
11. Reference material at bottom: yes (Section 8).

## End of VAT Workflow Base Skill v0.1

This base is incomplete without two companion files: a regional/directive layer (e.g., `eu-vat-directive`) and a country-specific skill (e.g., `germany-vat-return`). If you are reading this without both companions loaded, ask the user which jurisdiction and refuse to proceed until both are loaded.


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
