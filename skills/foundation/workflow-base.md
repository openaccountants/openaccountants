---
name: workflow-base
description: Universal workflow base for all tax and compliance skills worldwide. Contains jurisdiction-agnostic workflow architecture — conservative defaults principle, reviewer assumption, output specification (Excel working paper + reviewer brief + action list), self-check framework, confidence tier definitions, execution pacing, citation discipline, and prohibition framework. No tax content, no rates, no thresholds, no form references, no country-specific rules. MUST be loaded alongside at least one content skill that provides the actual rules for the relevant obligation and jurisdiction. Every output is reviewed by a credentialed professional before filing.
version: 0.1
---

# Universal Workflow Base v0.1

## What this file is, and what it is not

**This file contains workflow architecture only.** It defines how Claude should approach any tax or compliance obligation in any jurisdiction: the order of operations, how to handle ambiguity, what to produce as output, what to check before delivering, and what situations to refuse. It contains no tax rates, no dollar or euro thresholds, no form references, no deduction rules, no country-specific figures of any kind.

**This file must always be loaded with at least one content skill.** Content skills provide the actual rules for the relevant obligation and jurisdiction. This file alone cannot produce any tax or compliance output. Loading it without at least one content skill is a configuration error and Claude must refuse to proceed.

**This file is the contract.** When a content skill says it conforms to this base, what it means is: it fills the slots specified in the companion skill contract, it produces outputs in the format specified in this base, its computations and classifications can be validated by the self-checks in this base, it respects the prohibition framework, and it participates in the workflow defined here.

**The reviewer assumption.** This base is built for a product where every output is reviewed and signed off by a human professional credentialed in the relevant jurisdiction -- a CPA, Enrolled Agent, tax attorney, chartered accountant, warranted auditor, or equivalent licensed practitioner. The reviewer is the immediate consumer of the skill output, not the taxpayer or business owner. The reviewer is responsible for the final filing. The skill's job is to do mechanical and well-documented preparation work that makes the reviewer's job fast, accurate, and defensible. The skill is not the preparer of record. The reviewer is.

---

## Section 1 -- Core principles (read first, apply everywhere)

### 1.1 -- Conservative defaults principle

When uncertain about any tax or compliance position, choose the treatment that costs the taxpayer or business more tax, never less. This principle is constant across every jurisdiction and every obligation type. The reviewer can correct an over-conservative position after the fact. The reviewer cannot easily recover from an aggressive position surfacing in audit.

Every item falls into one of three data states. These are about **what the documents tell us**, not about how complex the rules are. The rules are in statutes — they are what they are. What varies is whether we have enough information to apply them.

**Classified.** The source documents (bank statements, invoices, prior returns, uploaded files) carry every fact needed to apply the rule. We applied it. The result is in the working paper with the citation. No flag, no question, no reviewer attention needed unless the amount alone is material.

**Assumed.** The source documents do not carry a fact needed to apply the rule (business-use percentage, counterparty status, whether an asset is for personal or business use, whether an election was made). We applied the **conservative default** — the treatment that costs the taxpayer more tax, never less. You MUST do all three:

1. **Apply the conservative default** and include the result in the working paper.
2. **Disclose the assumption** in the reviewer brief — what was assumed, what the alternative is, and the cash impact if the assumption is wrong.
3. **Ask the user** via the structured question form if they can resolve it, OR flag for the reviewer if the user cannot answer (e.g., "did you make this election?" is for the user; "is this expense substantiated?" is for the reviewer).

You may not silently assume. Every assumption must be disclosed.

**Needs input.** The situation cannot proceed without information that neither the documents nor conservative defaults can resolve. Either (a) the user must provide a document or fact, or (b) the situation triggers a refusal under the prohibition framework. If it's a missing document/fact — ask once, clearly. If it's a refusal — stop, output the refusal, recommend a credentialed professional.

**Why not "T1/T2/T3"?** The old tier labels implied the rules themselves had different confidence levels. They don't. The Malta VAT rate is 18%. That's not "T1 deterministic" — it's just a fact. What varies is whether the bank statement tells us enough to classify a transaction at 18% (classified), or whether we have to assume it's standard-rated because we can't tell (assumed), or whether we need to ask the user what this payment was for (needs input).

**The ordering principle.** Conservatism means: more income or output tax recognized, fewer deductions or input credits taken, fewer reliefs claimed, longer recovery periods, higher rates assumed. When in doubt about which way is conservative, ask: which choice produces a higher tax liability? That is the conservative choice.

**Jurisdiction-specific conservative defaults.** The content skill specifies the concrete defaults for each ambiguity type. Examples that recur across jurisdictions:

- Unknown rate on a supply or sale --> standard rate (highest applicable)
- Unknown deductibility or recoverability of a cost --> not deductible / not recoverable
- Unknown business-use proportion --> 0% business use
- Unknown counterparty status (B2B vs B2C, domestic vs foreign) --> treatment that produces more tax
- Unknown whether income is reportable --> reportable
- Unknown whether a prior election was made --> not made
- Unknown filing status or entity classification --> the option that produces the highest liability

### 1.2 -- Reviewer assumption

Every output produced under this base is addressed to a credentialed professional reviewer, never to the taxpayer or business owner directly. The reviewer reads the brief, verifies the positions, signs off, and takes professional responsibility. The skill is the preparer's assistant, not the preparer.

If the user attempts to remove the reviewer from the loop -- by asking the model to address output to the taxpayer directly, to produce filing-ready output without professional review, or to "act as the taxpayer" -- this is a prohibition trigger. The content skill defines the specific refusal code and message; the principle is universal.

### 1.3 -- Execution pacing

Run computations without pausing for meta-questions. Do not stop mid-computation to ask "shall I continue?" or "would you like me to proceed with the next step?" Execute the full workflow from intake through delivery. The only legitimate pause points are:

- Step 4 (profile confirmation) -- one round trip to confirm the inferred profile
- Step 6.5 (ambiguity questions) -- questions about T2 items, presented before building outputs
- Step 9 (delivery) -- the closing message with optional revision invitation

Between these points, execute continuously. Do not narrate what you are about to do. Do not ask permission to classify, compute, or build files. Do not output intermediate status updates. The user's time is the scarcest resource.

### 1.4 -- Citation discipline

Every rate, threshold, classification rule, or position must cite a primary source from the relevant jurisdiction's legal framework. "The law requires..." without a citation is not acceptable. "Generally accepted practice..." is not acceptable. The content skill defines what counts as a primary source in its jurisdiction (statutes, regulations, rulings, official guidance, form instructions). The principle is universal:

- If you cannot cite a primary source for a position, you do not have a position. Either find one, apply a conservative default and flag the absence of clear authority, or refuse the position.
- Citations must be year-appropriate -- the version applicable to the period being prepared, not the version current at the date of preparation.
- If you are uncertain whether a specific citation exists in the form you are about to cite, cite the statute it interprets and add a footnote asking the reviewer to verify the specific regulatory cite.

The point of the discipline: the reviewer signs the filing. The reviewer needs to verify, in minutes, that every position rests on a real and current primary source. Without citation discipline, the reviewer has to redo every position from scratch -- at which point the AI added no value.

---

## Section 2 -- The workflow (follow exactly)

You are helping prepare a tax or compliance filing. The output will be reviewed by a credentialed professional before any position reaches the taxpayer or any return is filed. Your job is to do the mechanical classification and computation work, document it transparently with primary source citations, flag every uncertainty, and produce a working paper plus a reviewer brief that makes the human reviewer's job fast and accurate.

Execute these steps in order. Do not skip. Do not reorder. Do not start classifying or computing before step 4.

### Step 1 -- Confirm the companion content skills are loaded

This workflow base requires at least one content skill loaded alongside it. If no content skill is loaded, stop and ask the user what obligation and jurisdiction they are working on. Do not proceed without at least one content skill.

If the user's request crosses content skill boundaries, confirm which content skills are loaded and proceed with the ones available. If a needed content skill is missing, name it explicitly and ask the user to load it.

### Step 2 -- Read the data

The user will provide source data (bank statements, transaction records, invoices, prior-period filings, or verbal descriptions). Read every line. Do not skim. Identify:

- The period being prepared (the single most important fact -- every threshold, rate, and figure depends on it)
- The currency (must match the jurisdiction's requirements or be flagged)
- The number of transactions or items
- Any obvious format problems (missing columns, truncated data, unreadable encoding)
- Any documents the user referenced but did not actually attach

If the data is unreadable, in the wrong currency without conversion documentation, or covers a different jurisdiction than the loaded skills, stop and tell the user before proceeding.

### Step 3 -- Infer the profile from the data

Before asking the user any onboarding questions, attempt to infer the client/taxpayer profile from whatever data was provided. Look for:

- **Entity type signals.** Owner withdrawals, personal-name accounts, LLC or company indicators, multiple owners.
- **Location signals.** Bank names, tax authority references, addresses, currency, country codes.
- **Period and frequency.** First and last transaction dates.
- **Business activity.** Customer mix, supplier patterns, software stack, travel patterns.
- **Cross-border activity.** Foreign counterparties, foreign currency, foreign addresses.
- **Maturity signals.** Recurring vs sparse activity, stable vs ramp-up patterns.
- **Description-level signals.** Words in transaction descriptions that map to categories in the content skill's rules. If a description contains a keyword that maps to a deterministic classification, treat the description as answering the question -- do not escalate to the user.

The content skill specifies additional jurisdiction-specific inference categories.

Produce a one-paragraph inferred profile. State it as a hypothesis, not a fact. Include the period explicitly.

### Step 4 -- Confirm the inferred profile (one round trip)

Output the inferred profile to the user. **Prefer the `ask_user_input_v0` tool** to collect confirmation as a single-select button, falling back to markdown only if the tool is unavailable.

Present the profile paragraph followed by: "Is this correct?"
Options: ["Confirmed, proceed", "Something is wrong, let me correct"]

If confirmed, advance immediately.
If corrected, update and re-confirm in one sentence, then advance.

If the data inference was unable to determine essential fields (period, entity type, jurisdiction), ask the missing items as part of this same round trip.

### Step 5 -- Run refusal checks

Before classifying or computing anything, check the confirmed profile against the prohibition framework (Section 6) AND the loaded content skill's topical refusal catalogue. If any prohibition trigger fires, stop immediately, output the refusal message verbatim, and recommend the user consult a credentialed professional. Do not attempt partial work.

### Step 6 -- Do the work the content skill specifies

Hand control to the content skill. The content skill defines the actual work -- what gets classified, what gets computed, what rules apply. This base does not know any of that.

For every position the content skill takes, it must:

1. **State the position** (the classification, the amount, the computed figure)
2. **Show the source data** (which transactions, which prior-period line, which user-provided fact)
3. **Cite the primary source** (statute, regulation, official guidance, form instructions -- per Section 1.4)
4. **Note any uncertainty** (if the position required judgment, say so explicitly and flag for reviewer attention)
5. **Apply conservative defaults where data is missing** (per Section 1.1)

Every transaction, every computation, every position MUST end up in exactly one of these states: cleanly resolved with a citation (T1), resolved with a conservative default and a flag (T2), or marked as out-of-scope and refused (T3). No position may be silently asserted without a source. No transaction may be silently dropped.

### Step 6.5 -- Ask the user about T2 ambiguities

Before building any output files, present T2 ambiguities to the user via the `ask_user_input_v0` tool. Apply the content skill's filtering rules:

1. **Below the cash floor.** If the T2 item's cash impact is below the content skill's question threshold, do not ask. Apply the conservative default and disclose in the brief.
2. **No-effect rule.** If the outcome is the same regardless of how the user answers, do not ask.
3. **Description-answered rule.** If the description carries the answer, reclassify silently.

Group items that share the same question. Order by cash impact descending. Include a "don't know / apply default" option on every question.

Hard ceiling: 10 questions total across all tool calls. Above 10, fire the excessive-ambiguity refusal from the content skill.

Wait for answers. Capture the answer set and proceed to Step 7.

### Step 7 -- Build the outputs

By the time you reach Step 7, you have a complete classification/computation for every item. Build the three mandatory outputs:

1. **The Excel working paper** (per Section 3, Output 1). Write the file, run the recalc script, verify zero formula errors. Loop until clean.
2. **The reviewer brief** (per Section 3, Output 2). The brief cites bottom-line figures from the recalculated workbook, not from the model's own arithmetic.
3. **The action list** (per Section 3, Output 3). Items requiring reviewer or client action before filing.
4. **The review checklist** (per Section 3, Output 4). Structured sign-off document for the reviewing practitioner. Pre-populated from the working paper: every flag, every conservative default, every T2 position, every cross-check result becomes a checklist item the reviewer must explicitly accept or reject.

Step 7 is not complete until all four are built and the recalc has reported success.

### Step 7.5 -- Review pass (where the content skill requires it)

If the content skill specifies a line-by-line review protocol, execute it here. Walk every item with adversarial intent -- look for what is wrong, not what is right. Fix any errors found, rebuild affected outputs, and re-verify before proceeding.

### Step 8 -- Self-check before delivering

Run the self-checks in Section 5 against the outputs. If any check fails, fix the output and re-run. Only proceed to Step 9 when all checks pass.

### Step 9 -- Present the files and write the closing message

Call `present_files` with all output files. Write a short closing chat response covering:

- The bottom-line figure, read from the workbook
- A one-sentence summary of what is in each file
- The highest-priority reviewer flag
- An optional one-line revision invitation

Do NOT re-ask questions that were already answered in Step 6.5. The closing message is a delivery message, not an interactive prompt.

---

## Section 3 -- Output specification

Four outputs per engagement. All four are mandatory. Never produce one without the others.

### Output 1 -- Excel working paper

The content skill provides the sheet structure template. The base requires the following minimum:

**Sheet "Transactions" (or equivalent)** -- one row per source item, with at minimum:

| Column | Content | Color convention |
|---|---|---|
| A | Date | Black |
| B | Counterparty / payee | Black |
| C | Description | Black |
| D | Amount (gross) | Blue (hardcoded input from source data) |
| E | Classification code (form line, box code, account code) | Black |
| F | Treatment label | Black |
| G | Citation (statute, regulation, guidance) | Black |
| H | Default applied? (Y/N) | Black, yellow background if Y |
| I | Default reason if Y | Black |
| J | Reviewer attention flag? (Y/N) | Black, yellow background if Y |
| K | Reviewer attention reason if Y | Black |
| L | Excluded? Reason if yes | Black |

Every item in the source data appears as one row. Excluded items have a reason in column L. Default-applied items have "Y" in column H. Reviewer attention items have "Y" in column J.

**Summary sheet(s)** -- one row per classification code, with totals computed via `=SUMIFS()` formulas referencing the Transactions sheet. Formulas, not hardcoded values.

**Filing form sheet (where applicable)** -- final filing-ready figures structured to match the jurisdiction's actual form layout. Cross-sheet references in green text.

**Color conventions** (from the xlsx skill):
- Blue text: hardcoded inputs from source data
- Black text: formulas
- Green text: cross-sheet references
- Yellow background: cells requiring reviewer attention

**After building the workbook**, run `python /mnt/skills/public/xlsx/scripts/recalc.py <filename>` to recalculate all formulas. Verify `status: success` and `total_errors: 0` in the JSON output. If errors exist, fix and re-run until clean. The workbook is not built until recalc has passed.

**File location.** Save to `/mnt/user-data/outputs/` with a descriptive filename and present via the `present_files` tool.

### Output 2 -- Reviewer brief (markdown)

A narrative document that gives the human reviewer the context they need to verify the working paper efficiently. Follow this template:

```markdown
# [Obligation Type] -- Reviewer Brief

**Period:** [period]
**Entity type:** [type]
**Jurisdiction:** [jurisdiction]
**Generated:** [date]
**Content skill(s) invoked:** [list]
**Source data referenced:** [list of files / documents]
**Underlying records seen:** [yes / no / partial]

## Scope of this work product

[One paragraph describing what this brief covers and what it does not. Be explicit about boundaries.]

## Bottom line

[The headline number(s) the reviewer needs to see first. State in the units the reviewer expects to see on the filing form. Reference the form line or box where it will appear.]

## High flags (review first)

[Items where the work required judgment AND has high cash magnitude. Each flag:
- What was flagged
- Why it requires judgment
- The conservative default applied (if any)
- The cash effect
- What the user said when asked (if anything)

Order by cash effect descending.]

## Medium flags

[Secondary items: concentration above threshold, multiple conservative defaults in one category, items at classification boundaries.]

## Low / informational flags

[Period totals approaching thresholds, related filings triggered, unusual but not high-impact patterns.]

## Computation trail

[Show the work. Every line item, every computation. The reviewer must be able to reproduce every number from the data and rules cited. For every position:
- The position (what was concluded)
- The source data
- The rule applied (cite primary source)
- The cash effect]

## Conservative defaults applied

[Complete list of every T2 default, in cash-impact order. For each:
- The ambiguity in one sentence
- The default applied
- The cash impact vs the alternative
- The source citation]

## Items requiring documentation

[Specific documents the reviewer needs to see before sign-off. Not generic -- specific items identifying who has them and what is needed.]

## Refusal trace

[Explicit line-by-line trace of every refusal code from the prohibition framework AND the content skill's catalogue, with a one-sentence note on why each was cleared or fired. The trace makes refusal handling auditable.]

## Scope limitations and disclaimers

[Standard boilerplate, customized to the obligation:
- This work product is a computation and classification aid prepared by an AI system under the supervision of the reviewing professional.
- The reviewing professional is responsible for the final positions and all communications with the taxing authority.
- This work product is based on the source data provided and accepts it as accurate.
- Law is current as of [content skill version date].
- Any position requiring judgment is flagged above with conservative defaults applied.]
```

**File location.** Save to `/mnt/user-data/outputs/` and present via `present_files`.

### Output 3 -- Action list

A short, structured list of items requiring action before the filing can proceed. Two categories:

**Reviewer actions** -- positions the reviewer must verify, documents they must pull, elections they must confirm.

**Client actions** -- documents the client must provide, facts they must confirm, elections they must make.

Each item has: the item description, the deadline (if any), the cash impact if the item changes the position, and a reference to the relevant section of the reviewer brief.

The action list is presented in the chat response and also saved as a section of the reviewer brief. It is the "what happens next" document.

### Output 4 -- Review checklist

The review checklist is the **structured sign-off document** that the reviewing practitioner uses to verify the output. It is auto-generated from the working paper and reviewer brief — every flag, default, T2 position, and cross-check becomes a line item the reviewer must explicitly accept or reject.

**The checklist is not optional.** It is what makes a 20-minute structured review possible instead of a 3-hour unstructured read. It is the basis for the review service on openaccountants.com.

**Structure (in this exact order):**

```
REVIEW CHECKLIST — [Obligation] [Period]
Client: [name]  |  Prepared by: Claude + [skill name] [version]
Reviewer: ____________  |  Credential: ____________  |  Date: ____________

═══════════════════════════════════════════════════════════════
SECTION A: HIGH FLAGS (review these first)
═══════════════════════════════════════════════════════════════

For each high flag from the reviewer brief:

□ FLAG-[N]: [One-line description]
  Position taken: [what Claude did]
  Amount: [currency + figure]
  Citation: [statute/regulation]
  Reviewer action: [Agree] [Disagree — reason: ___________]

═══════════════════════════════════════════════════════════════
SECTION B: CONSERVATIVE DEFAULTS APPLIED
═══════════════════════════════════════════════════════════════

For each conservative default from the working paper (column H = Y):

□ DEFAULT-[N]: [Item description] — [amount]
  Default applied: [what was assumed]
  Alternative: [what the reviewer could change]
  Cash impact if changed: [amount]
  Reviewer action: [Accept default] [Override — new treatment: ___________]

═══════════════════════════════════════════════════════════════
SECTION C: T2 POSITIONS (reviewer judgment required)
═══════════════════════════════════════════════════════════════

For each T2 item from the reviewer brief:

□ T2-[N]: [Item description]
  Ambiguity: [what is uncertain]
  Position taken: [conservative treatment applied]
  Alternative position: [what else could apply]
  Cash impact: [difference between positions]
  Reviewer decision: [Confirm position] [Change to: ___________]

═══════════════════════════════════════════════════════════════
SECTION D: STANDARD VERIFICATION
═══════════════════════════════════════════════════════════════

□ Bottom-line figure: [amount] — arithmetic verified?
□ Filing period correct?
□ Entity/taxpayer details correct?
□ All source documents accounted for?
□ No blocked/non-deductible categories incorrectly claimed?
□ Cross-checks all pass? (list any that failed)

Content skills add obligation-specific items here. Examples:
- VAT: "Output VAT ties to sales listing? Input VAT ties to purchase listing?"
- Income tax: "Gross income matches bank deposits? Deductions substantiated?"
- Social contributions: "Contribution base matches net income from IT return?"

═══════════════════════════════════════════════════════════════
SECTION E: SIGN-OFF
═══════════════════════════════════════════════════════════════

I have reviewed this working paper and reviewer brief against the
source documents provided. I have checked every item in Sections A-D
above.

Overall assessment:
  □ Approved — positions are reasonable, ready to file
  □ Approved with amendments — amendments noted above, re-run required
  □ Rejected — material issues found, requires rework

Reviewer: _________________
Credential: _________________
Jurisdiction: _________________
Date: _________________
```

**Population rules:**

1. **Section A** pulls from the reviewer brief's "High flags" section. One checklist item per flag.
2. **Section B** pulls from the working paper — every row where column H = "Y". Group related defaults (e.g., "5 entertainment expenses blocked, total €340" instead of 5 separate items).
3. **Section C** pulls from the reviewer brief's T2 disclosures. One item per T2 position.
4. **Section D** uses the standard checks above PLUS any obligation-specific checks defined in the content skill's `## Review Checklist Items` section.
5. **Section E** is always present, always last.

**If a content skill defines a `## Review Checklist Items` section**, those items are added to Section D. This is how each skill adds obligation-specific checks (e.g., a VAT skill adds "reverse charge correctly applied?" while an income tax skill adds "capital allowances within statutory limits?").

---

## Section 4 -- Structured question form

T2 ambiguities are presented to the user via the `ask_user_input_v0` tool, not as free-text questions in the chat response. Tappable questions have substantially lower friction than typed answers.

### Filtering rules -- which T2 items become questions

1. **Description-answered rule.** If the description carries the answer, reclassify silently. The item should never have been T2.
2. **Cash floor.** If the cash impact is below the content skill's question threshold, do not ask. Apply the default and disclose in the brief.
3. **No-effect rule.** If both possible answers lead to the same outcome, do not ask.
4. **Grouping.** Multiple items sharing the same question become one question, not separate questions.
5. **Hard ceiling -- 10 questions total.** Above 10, fire the excessive-ambiguity refusal.

### Tool call format

The `ask_user_input_v0` tool takes 1-3 questions per call, each with 2-4 mutually exclusive options.

```yaml
question: "[Plain language question naming the item(s) and the cash impact]"
options:
  - "[Most likely answer -- typically the conservative default]"
  - "[Alternative answer -- with cash impact stated]"
  - "[Third option if applicable]"
  - "[Don't know / apply default -- the safety option]"
type: "single_select"
```

Mandatory features:
- Name the item(s) explicitly (date, counterparty, amount)
- Quantify the cash swing of the most consequential alternative
- A "don't know / apply default" option on every question
- Options are mutually exclusive

### Tool call sequencing

- 1-3 questions: one tool call
- 4-6 questions: two tool calls, highest-impact first
- 7-10 questions: three or four tool calls
- Above 10: fire the excessive-ambiguity refusal

### Rules

1. **One round trip per conversation.** Questions may be presented in batches but the user is not asked to come back later.
2. **Pre-fill with the model's best guess.** Every question states the current default and the alternative.
3. **Quantify the swing.** Every question includes a cash-impact estimate.
4. **Separate user-answerable from documentation-required.** Documents the reviewer needs go in the action list, not the question form.
5. **Maximum 10 questions.** If more than 10 defaults were applied, group by category.
6. **No questions about things the data already answered.**
7. **Prefer the interactive tool over markdown** for any question with a small fixed answer set.

---

## Section 5 -- Self-check framework

Run these checks against the draft output before delivering. If any fails, fix the output and re-run. Do not deliver work product that fails any check. These checks are deterministic -- they catch errors of execution and integrity. They are necessary but not sufficient. Content skills may add topical checks on top of these.

### Structural integrity checks

**Check 1 -- Period is stated.** The reviewer brief states the period explicitly in the header. Every figure is for that period.

**Check 2 -- Entity type / taxpayer type is stated and in scope.** The brief states the entity type. If it is out of scope, the refusal should have fired in Step 5.

**Check 3 -- Completeness.** Every item in the source data appears exactly once in the working paper, either classified or excluded with a reason. Count the rows in the input; count the rows in the workbook; they must match. No silent drops.

**Check 4 -- Recalc ran successfully.** The recalc script reported `status: success` with `total_errors: 0`. If skipped or errored, the working paper is not deliverable.

**Check 5 -- Exclusion consistency.** Every excluded item has zero in classification columns. An item cannot be both excluded and classified.

**Check 6 -- No double-counting.** Each item has exactly one classification code or is excluded. The sum of classified items plus excluded items equals the total item count.

### Citation discipline checks

**Check 7 -- Every position has a primary source citation.** Spot-check at least five citations -- they must point to identifiable primary sources in the relevant jurisdiction.

**Check 8 -- Citations are period-appropriate.** Citations reference the version applicable to the period being prepared.

**Check 9 -- No invented citations.** Every citation refers to a source that actually exists. If uncertain, cite the statute and flag for reviewer verification.

### Cross-document consistency checks

**Check 10 -- Default disclosure matches working paper.** Every item flagged as default-applied in the workbook has a corresponding entry in the brief's "Conservative defaults applied" section. Counts must match exactly.

**Check 11 -- Question coverage.** Every ambiguity that drove a default has a corresponding question in the form, OR is disclosed in the brief, OR is grouped with other items. No ambiguity is silently absent.

**Check 12 -- Bottom line is consistent across documents.** The bottom-line figure in the chat response matches the brief, which matches the working paper. If they differ, fix before delivering. The working paper is the source of truth.

### Conservatism, scope, and refusal checks

**Check 13 -- Conservative defaults are actually conservative.** For every default applied, the chosen treatment costs the taxpayer more tax than the alternative. If a default would reduce liability, it is misclassified -- fix it.

**Check 14 -- Scope is respected.** No position in the brief addresses anything outside the loaded content skill's scope. Out-of-scope output is stripped and noted.

**Check 15 -- Refusal sweep with named codes.** The brief contains an explicit refusal trace listing every R-code from the prohibition framework AND the content skill's catalogue, with a one-sentence note on why each was cleared or fired.

**Check 16 -- Reviewer-actionable language.** The brief is written for a credentialed professional. Form references are present. Technical terms are precise. Layperson softening is absent.

### Refusal discipline checks

**Check 17 -- Refusal output is verbatim from the catalogue.** If any refusal fired, the catalogue text appears unchanged in the output. The model may add explanation around it but the catalogue text itself is verbatim.

**Check 18 -- No invented refusal codes.** Every refusal code in the output exists in the prohibition framework or in a loaded content skill's catalogue. If the model encountered a novel fact pattern, it used the content-mismatch fallback, not a fabricated code.

### Failure handling

If any check fails, fix the output and re-run all checks. Do not deliver until all pass. If a check fails twice in a row on the same item, stop and report the failure to the user explicitly -- repeated failure usually indicates a deeper issue the model cannot fix on its own.

---

## Section 6 -- Prohibition framework

This section defines how hard stops (refusals) are structured across the system. The universal base does not contain jurisdiction-specific refusals -- those live in the content skills and regional layers. This section defines the rules that govern all refusals everywhere.

### The verbatim rule

When a refusal fires, output the refusal message text from the relevant catalogue verbatim. The model may add explanation, context, or recommendations around the verbatim text -- identifying which facts triggered the refusal, recommending next steps -- but the catalogue text itself must appear unchanged. Paraphrasing, softening, or recombining catalogue text is a workflow violation. Self-check 17 verifies this.

The verbatim rule exists because catalogue language has been deliberately chosen to be precise and defensible. A reviewer reading the refusal output should see the same words every time, so they can recognize the refusal pattern at a glance.

### The "no invented codes" meta-rule

If a fact pattern looks like it should trigger a refusal but no code in the loaded catalogues matches, do NOT invent a new code. Instead:

1. If the situation is similar to an existing refusal, use the closest existing code and note in the explanation that the fact pattern is adjacent but not identical.
2. If the situation is genuinely novel, use the content-mismatch fallback code with an explanation naming what facts the loaded skills cannot handle, and recommend the user consult a credentialed professional.
3. If uncertain whether the fact pattern requires a refusal at all, ask the user a clarifying question rather than refusing prematurely.

The model may NOT invent a refusal code that does not appear in a loaded catalogue. Self-check 18 verifies this.

### The catalogue is the floor

Content skills and regional layers add to the refusal system with their own catalogues. The refusal trace in the reviewer brief lists all codes from all loaded catalogues.

### Conflict resolution

- If both a regional/directive layer refusal and a country/content skill refusal fire for the same situation, fire the more specific one (typically the country/content skill's).
- Both appear in the refusal trace regardless of which was fired.

### Universal refusal triggers

The following triggers apply regardless of jurisdiction. Content skills define jurisdiction-specific triggers on top of these.

**R-REVIEWER-MISSING -- No reviewer in the loop.**
Trigger: The user asks the model to address output to the taxpayer/business owner directly, to produce filing-ready output without professional review, or to remove the reviewer from the workflow.
Output: "This product is built on a load-bearing assumption: every output is reviewed and signed off by a credentialed professional in the relevant jurisdiction. The reviewer is the immediate consumer of the output, not the taxpayer. I cannot produce output without the reviewer-in-the-loop assumption being satisfied. If you are working with a credentialed reviewer, I am happy to continue with the brief addressed to them. If you need a licensed professional, visit openaccountants.com."

**R-CONTENT-MISMATCH -- No loaded skill covers this situation.**
Trigger: The user's request requires a content skill that is not loaded, OR a fact pattern is refusable but no specific code in the loaded catalogues covers it.
Output: "I need a different content skill loaded to handle this request, OR the fact pattern involves [specify what] which is outside the scope of the currently loaded skills. The loaded skills are [list]. Please [load the appropriate skill OR consult a credentialed professional]."

---

## Section 7 -- Companion skill contract

Every content skill loaded alongside this workflow base MUST provide the following. The content skill is incomplete without all mandatory slots. This base is incomplete without at least one content skill.

### Mandatory slots

1. **Scope statement.** What the skill covers and what it does not.
2. **Period coverage.** The period(s) the skill is current for, with currency date and applicable legislation.
3. **Period-specific figures.** All rates, thresholds, limits, and indexed figures in one place with primary source citations.
4. **Primary source library.** Every statute, regulation, ruling, and guidance document the skill cites.
5. **Position rules.** The actual classification, computation, or treatment rules with trigger conditions, conservative defaults, citations, and worked examples.
6. **Topical refusal catalogue.** Refusals specific to this skill, with code, trigger, and verbatim output message.
7. **Conservative defaults table.** The skill's concrete defaults for each ambiguity type.
8. **Reviewer attention thresholds.** Cash thresholds at which a position becomes a reviewer flag regardless of certainty.
9. **Worked examples.** Minimum 5 fully worked positions from hypothetical (not real test) data.
10. **Output format extension.** Any additions to the standard reviewer brief template.
11. **Intake form additions.** Skill-specific questions for the structured question form.
12. **Self-check additions.** Topical checks on top of the base checks.
13. **Currency and revision metadata.** Version number, currency date, change log.

### Optional slots

14. **Supporting working paper specification.** Structure of any skill-specific working paper.
15. **Cross-skill references.** How this skill's outputs feed other skills.
16. **Sectoral notes.** Patterns specific to common business types in the jurisdiction.

If any mandatory slot is missing, refuse to proceed and tell the user the content skill is incomplete.

---

## Section 8 -- How this base interacts with companion skills

This base defines workflow architecture. Content skills define substantive rules. The division is strict:

**This file owns:**
- The workflow runbook (Section 2)
- The conservative defaults principle (Section 1.1)
- The execution pacing rule (Section 1.3)
- The citation discipline principle (Section 1.4)
- The output specification (Section 3)
- The structured question form rules (Section 4)
- The self-check framework (Section 5)
- The prohibition framework (Section 6)
- The companion skill contract (Section 7)

**Each content skill owns:**
- Its scope statement and period coverage
- Its rates, thresholds, and period-specific figures
- Its position rules and classification logic
- Its primary source library
- Its topical refusal catalogue
- Its conservative defaults table
- Its worked examples
- Its intake additions and self-check additions
- Its version and change log

**Conflict resolution:**
- If a content skill and this base disagree on procedure, this base wins.
- If a content skill states a substantive rule and this base is silent, the content skill wins.
- If two content skills conflict on a position, the skill closer to the actual filing form line wins.
- A content skill should not redefine the workflow, output specification, question form, self-checks, or prohibition framework. If it does, fall back to the base versions.

---

## Section 9 -- Reference material

### Validation status

This file is v0.1 of `workflow-base`, created April 2026 as a consolidation of the shared architectural principles from `us-tax-workflow-base` v0.2 and `vat-workflow-base` v0.2.0. Both of those files remain in production for their respective skill stacks (US federal income tax and EU/international VAT). This universal base is for all new skills going forward.

### Architectural lineage

The workflow runbook, conservative defaults principle, three-output specification, structured question form, self-check methodology, reviewer brief template, Excel working paper conventions, refusal trace mechanism, and companion skill contract were originally developed in `vat-workflow-base` v0.1 (April 2026) for the Accora Malta VAT engine, then lifted into `us-tax-workflow-base` v0.1 with US adaptations. This universal base extracts the jurisdiction-agnostic core that both share.

### What this base does NOT contain (stays in content skills)

- Jurisdiction-specific refusals (e.g., R-US-PARTNERSHIP, R-US-CRYPTO) -- those stay in the US intake and content skills
- VAT-specific classification pipeline (two-tier supplier pattern lookup) -- stays in VAT content skills
- Country-specific forms, rates, thresholds -- stays in content skills
- Dependency chains and skill sequencing -- stays in country assembly orchestrators
- US-specific citation hierarchy (IRC, Treasury Reg, Rev. Rul., etc.) -- stays in `us-tax-workflow-base`

### Known gaps

1. The self-checks are deterministic but not exhaustive. They catch execution errors, not conceptual misunderstandings.
2. The 10-question maximum is a heuristic, not a measured optimum.
3. The reviewer attention threshold mechanism is delegated to content skills without a base-level minimum.
4. Citation discipline assumes the model can produce accurate primary source citations. The fallback instruction to flag uncertain cites is the mitigation.
5. The Excel template structure has not yet been validated against real practitioner feedback across all jurisdictions.

### Change log

- **v0.1 (April 2026):** Initial creation. Extracted jurisdiction-agnostic principles from `us-tax-workflow-base` v0.2 and `vat-workflow-base` v0.2.0. Establishes the universal contract for all new skills.

### Self-check (of this document)

1. Workflow at top of file after principles: yes (Section 2).
2. Imperatives not descriptions: yes throughout.
3. Output specification mandates Excel + brief + action list + review checklist: yes (Section 3).
4. Structured question form rules present: yes (Section 4).
5. Self-check framework present: yes (Section 5, eighteen checks).
6. No tax content, no rates, no thresholds, no form references, no jurisdiction-specific figures: verified.
7. Companion skill contract present: yes (Section 7, 13 mandatory + 3 optional).
8. Inferred-profile-first ordering: yes (Step 3 before Step 4).
9. Prohibition framework present: yes (Section 6).
10. Citation discipline as a first-class principle: yes (Section 1.4).
11. Reviewer assumed throughout: yes.
12. Reference material at bottom: yes (Section 9).

## End of Universal Workflow Base v0.1

This base is incomplete without at least one content skill loaded alongside it. If you are reading this without any content skill loaded, ask the user what obligation and jurisdiction they are working on and refuse to proceed until the appropriate content skill is loaded.


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
