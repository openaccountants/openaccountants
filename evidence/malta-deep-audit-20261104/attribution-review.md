# Independent attribution/status review, 4 November 2026

Reviewer: non-author business-audit agent. Scope is the uncommitted attribution/status diff on branch codex/malta-audit-attribution-2026-11-04, against ab692cc2ef1c6306de9435b63448294d30fc4052. This review does not reattest underlying Malta tax rules or publish an accountant approval.

## Result

CONDITIONAL PASS pending four displayed-version corrections listed below. No substantive tax-rule change found. The existing source audit findings remain open.

## Preservation checks actually performed

- Read entire15Guide attribution diff plus country README.
- Programmatically removed only reviewed_by/reviewed_on/tier/version/last_updated, permitted attribution lines, and displayed-version labels from old/current comparison. All15Guide bodies then matched exactly. Thus no rule, rate, figure, formula, worked example, disclaimer, source URL or source-read date was altered by this change. Descriptive version numbers are the exception explicitly scoped above.
- All three Michael Spiteri Staines programme files (global residence, permanent residence, nomad) are byte-for-byte identical to base, including review metadata. Malta bookkeeping is also byte-for-byte identical.
- Current skills/malta corpus has Michael Cutajar only in bookkeeping contribution footer and README maintenance table/prose. No other current Guide contains his name. Git history is preserved.
- Each of the four original audit reports is byte-for-byte identical to its parent-directory original, including the business report's limits and unchanged-metadata snapshot. New evidence README explicitly distinguishes historic metadata from current attribution.
- attribution-changes.json lists exactly15modified Guides and exactly3maintenance scopes, records no new approval/no live mutation/no tax-rule changes, consistently with the diff.
- README covered_by mappings are populated for all7applicable jobs and all7are explicitly partial. No new comprehensive, accountant-verified or live-withdrawal claim is made. The three named maintenance assignments are explicitly not new sign-offs.
- README's workflow/TA24/PT/quarterly scheduling holds correspond to the preserved personal-audit P1-A/B/C. Corporate election/TP eligibility holds correspond to business-audit B3/B4. VAT routing/calendar holds correspond to VAT V-A/B/C. These are sourced audit-status summaries, not newly invented rates or legal rules. Individual facts remain in the cited audit reports.

## Required consistency corrections before publication

1. malta-tax-optimization frontmatter1.3 but bodyline15stillv1.2.
2. malta-transfer-pricing frontmatter1.2 but quick-reference line35still1.1.
3. mt-estimated-tax frontmatter2.2 but bodyline17stillv2.1.
4. mt-rental-income frontmatter1.2 but quick-reference line36still1.1.

These should change only those displayed version labels. Formation and moving H1 versions already match. last_updated2026-11-04 on body/byline edits accurately records edit date, with evidence explicitly denying law reverification. Metadata-only review removals preserve original last_updated/version, which is appropriate and does not introduce a fresh-law date.

## Limits and retained failures

The root identified a pre-existing format failure in moving-to-malta (missing required executable examples). This review does not waive it, claim it passed or invent tax examples to satisfy it. Root should record the precise check outcome. Normal native checks remain required. Tier2is repository metadata, not proof the live application's canonical verification_state or review_records have changed. Repository ingestion/live propagation remains unverified. No source ledger is invented for attribution-only changes; exactdiff inventory and this preservation comparison are the relevant evidence.
