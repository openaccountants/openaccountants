# Independent F22 disposition review

**PASS for the amended F22 disposition and the single VAT-return qualification.** All specified historical units are accounted for. No further Guide method or `Not yet confirmed:` addition is required solely to settle F22. The annual zero-denominator method, special KV first-breach question, fixed-gross crossing circularity and other whole-pack findings remain open. This is not a whole-country PASS or accountant attestation.

| Frozen item | SHA256 |
|---|---|
| Complete original VAT archive, 37,813 bytes |20fb3aabb198b7ebc98b559691d7cdc6fe1982a2bc00e8c80863b3b22d048c1a|
| Amended VAT Guide v2.4, 49,828 bytes |49bfe203ced8cde44bf3e768fb395edd4bdf28d0e1f16eb05d384f8430e7f432|
| Amended F22 disposition proposal |adb5f684a6191a53eca44c221faa837b7f5169510c003a0fe0656140f12fe6c9|

The proposal was written by root. The reviewer read the actual complete old archive, complete current VAT-return Guide, complete current registration Guide, current Rule 11 and root's proposal. The initial current VAT file was commit `fce370c5`; the reviewed v2.4 adds the correction described below. Guide files and Git were not edited by the reviewer.

## Finding, correction and recheck

The initial Test 12 mapping said “registration 7a/69(3)” for a person already registered under 7. The return Guide also said the non-payer must first register under 7a without the existing-registration exception. Actual [VAT7a(1)/(2)](https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html#paragraf-7a) expressly dispenses with a duplicate application for an existing 7 registrant. Root amended only the return sentence and proposed Test 12 disposition. That precise delta passes: retain the 7 registration, self-assess500×23%=115, no input deduction, no duplicate 7a application.

The reviewer initially also alleged that the registration sibling had lost this exception. That allegation was wrong: its Cross-border section already states it at line 133. After rereading the entire current sibling, the reviewer withdrew that part. The registration file remains unchanged. No duplicate sibling edit is required.

The proposal manifest initially retained the old 49,557-byte length after the return correction. Root corrected it to 49,828; the independent controls verify the actual hash and byte length. These two matters are recorded in `findings.json`, including their closure and the withdrawn sibling allegation.

**Lost content restored: 1 distinct verified qualification** in the VAT-return treatment of the Test 12 population. The registration sibling already retained that rule. The permissible removal of unsupported comparison/workflow material is not counted as restored current coverage.

## Every specified unit has a disposition

`unit-ledger.json` enumerates 50 review units: 16 comparison rows, 2 literal templates, 3 confidence labels, 12 named tests, 12 reference-only topic bullets and 5 historical trust/publication claims. This is an explicit inventory of the assigned F22 groups, not a heuristic count of all tax rules in the country.

| Group | Independent disposition |
|---|---|
| All 16 Malta-comparison rows | Each original Slovak and Maltese cell is retained verbatim in the archive and enumerated independently. Current Slovak methods cover rates, forms, control statement, frequency, deadlines/payment, registration, capital adjustments, entertainment/cars, import/domestic reverse charge, currency and authority. Maltese cells are removed as unsupported operative comparison content under Rule 11. Historical allusions to articles/schedules do not establish a fetched, period-valid Maltese source body. No Maltese-law correctness claim is made. |
| Two literal templates | `REVIEWER FLAG` and `ESCALATION REQUIRED` are removable output boilerplate. Required fact gathering, source gaps, payer status and professional-review safeguards survive. Removing their literal formatting loses no tax entitlement or computation. |
| T1/T2/T3 labels | Removable confidence/workflow taxonomy. T1 methods survive in the actual rules/form matrix. T2 coefficient, vehicle and import populations survive, with the actual annual-denominator gap still disclosed. Old T3 complex-group/nonstandard/triangulation/SOPARFI-like names were exclusions, not supplied computations. A form row for triangulation does not certify its full legal regime. |
| Twelve named tests | Every economic population is mapped to the current legal method and actual period-valid form. Deleting duplicate named fixtures is allowed; wrong aliases are corrected. Full recovery still depends on actual payer/use/document conditions, not merely a registration number or a foreign invoice with no VAT. |
| Twelve direct-tax/reference bullets | CIT/small-company/PIT/dividend/social/health/minimum/withholding topics route to their current sibling methods. Motor-vehicle tax, municipal property tax and the three named banking/insurance/regulated-sector levy references had no computation or verified primary support in that old reference-only block; their removal is explicitly recorded. They are not newly covered 2026 taxes. Their being outside the seven domains is context, not by itself the Rule 11 justification for deleting a verified method. |
| OSS/MOSS pointer | Current return still names the OSS route and links to the shared EU Guide. No historical special-scheme schedule is reinstated. The old distance-selling threshold also remains routed through that shared Guide. This review does not certify that Guide's 2025 metadata or the complete 2026 OSS implementation. No ordinary domestic return computation is relabelled as specialist to close F22. |
| Five historical trust/publication claims | The old “deep research verification”, validation date/status, practitioner-validation and publication-sign-off assertions are retained as history and removed from operative claims. Actual current Rule 9/10 distinguishes source-cited tier 2 material from licensed-accountant sign-off. Protected frontmatter and CTA remain unchanged; no historical AI confidence claim is promoted to attestation. |

Rule 11 permits removal of boilerplate, duplicates and content with no official source. Its exception is applied to the actual historical material here. Merely storing an archive, or declaring an ordinary unsupported method “out of scope”, would not meet the rule. The supported Slovak methods are retained or corrected; the three already-disclosed VAT research gaps are not closed by this disposition.

## Current form and law recheck

The actual DPHv25 pages 2–3 were read again, including visual inspection of both rendered pages, and the actual KVDPHv25 body was reread. Raw body/image hashes are in `primary-source-manifest.json`. Fresh live primary opens corroborated the VAT Act, DPHv25 and KVDPHv25; the primary7a exception was also located live. The statutory bases were read directly from the retained complete current law, including 7a,11,15,24,43,47,49/51,69,77/78 and 84a. This recheck reuses the earlier independently reviewed F11 form bodies without treating that earlier result as a substitute for reading them.

| Old test | Correct current placement/result |
|---|---|
|1 domestic 23% purchase |46 deductible when eligible; total input 19, domestic subset 21.|
|2 EU consulting |230 self-assessed,09b/10b; eligible input 19.|
|3 entertainment |No input deduction. At a hypothetical 23% rate,500 gross would contain93.50 VAT, not the old94;406×23%=93.38. No restaurant rate is inferred from that inconsistent historical invoice.|
|4 qualifying IC goods sale |5,000 exempt base in 13 and its 14 subset;43 evidence and sales-list conditions apply.|
|5 nonEU B2B software |4.60 tax in 09b/10b; eligible input 19.|
|6 eligible 5% bread/milk |5 input in 18a and domestic 20a subset. Product qualification matters.|
|7 eligible84a import |11,500 tax in 11e/12e; input 19 and 23c subset when entitled.50,000 must be the complete24 import base, not automatically the old customs value alone;84a is conditional mandatory self-assessment, not a universal opt-in.|
|8 mixed M1 car |4,600×50%=2,300 input in 19/21; the other2,300 is not thereby proved to be an income-tax expense.|
|9 domestic construction |3,450 tax in 09b/10b and eligible input 19; actual sectionF and both-payer conditions.|
|10 qualifying export |8,000 exempt base in 13/15 with47 evidence.|
|11 IC acquisition |690 tax in 07/08 and eligible input 19; acquisition source/liability dates and documents apply. An acquisition is not itself an outgoing EC-sales-list supply.|
|12 existing 7 nonpayer service |115 self-assessed/payable, no input deduction or duplicate 7a application.|

Input subsets are not extra deductions on top of totals. The current output-rate map, input-rate subsets, summary 32–35 and KVDPH sections/codes match the actual forms. All 12 conditional arithmetic controls pass; the historical entertainment inconsistency is separately flagged as invalid arithmetic. The current Guide's two executable examples also pass.

Sources: [actual DPHv25](https://pfseform.financnasprava.sk/Formulare/VzoryTlaciv/DPHv25.pdf), [actual KVDPHv25](https://pfseform.financnasprava.sk/Formulare/eFormVzor/DP/form.607.html), [current VAT Act](https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html). Preservation controls also prove unchanged original slug, jurisdiction, review status, trust label, tier, licence and exact complete platform CTA.

## Closure boundary

No specified F22 unit remains unaccounted for and no additional `Not yet confirmed:` line is required for those permitted removals. The final disposition and this ledger preserve the exact distinction between archived unsupported history, migrated current methods, duplicate workflow text and unprovided specialist computations. F22 can close on these bytes. The whole-country review and the named ordinary VAT gaps remain open.
