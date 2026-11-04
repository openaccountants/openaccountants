# Malta audit and attribution closeout, 4 November 2026

Audited public revision: `ab692cc2ef1c6306de9435b63448294d30fc4052` in `openaccountants/openaccountants`.

## Result

All 34 Guides were read: 32 in `skills/malta` and two in `skills/orchestrator`. The initial count of 33 country Guides included the country README; it was not an additional Guide. The four reports record actual checked provisions and remaining scopes. This is a findings audit, not a certificate of zero mistakes, comprehensive coverage or accountant approval.

- [Personal tax, payroll and old workflows](personal-audit.md): wrong form and invented filing workflow, wrong PT benchmark/scheduling, remittance eligibility, operative 2026 extension and crypto recognition errors; a real statute/MTCA table discrepancy remains unresolved.
- [Business and companies](business-audit.md): size-threshold commencement, final-tax election conditions and dates, routing and conditional eligibility defects; advanced trust, duty and portal scopes remain unverified.
- [Property, succession and residence](property-residence-audit.md): rental election, historical rate, garage VAT, valuation formula and securities description errors; programme-law checks do not verify unread immigration material.
- [VAT and whole-pack inventory](vat-audit.md): goods/services date distinction, foreign-purchase classification, shifted calendar dates, scope and boundary errors; duplicate VAT return material.

## Evidence and interpretation

[inventory.json](inventory.json) pins every source Guide hash and original attribution. [mechanical-audit.json](mechanical-audit.json) records format/evidence gaps separately from substantive findings. At the initial audit, all 18 existing executable calculation blocks passed, while five tax Guides lacked required examples. The correction batch now has 62 executable blocks passing with no missing required examples; legal premises are independently checked only within the recorded correction scopes. There is no Malta-specific support in the repository contradiction detector, so no clean contradiction-detector result is claimed. Cross-Guide comparisons were manual.

## Authorised attribution change

Michael asked to retain only two or three Guides under his name, remove his name from the others, and welcome other Maltese accountants. The country README assigns exactly three maintenance jobs: individual income tax, VAT returns and bookkeeping. These are not new sign-offs. Ten pre-existing Michael review claims are withdrawn in repository frontmatter; five other contribution footers and two current corridor bylines are replaced by team/unassigned wording. The initial attribution-only phase preserved Michael Spiteri Staines's three programme review entries. The later GRP quotation correction resets that Guide's prior approval; the untouched Nomad and MPRP Guides and their existing review entries remain byte-identical to the audited base. Git and this pinned inventory preserve historical contribution/review metadata.

The first commit, `63d81783`, changes attribution and country routing/status without changing tax figures, rules or examples. Michael then explicitly asked to fix what was not updated. The subsequent correction batch changes 31 Guide bodies, supplies per-Guide ledgers and old-topic destinations, and obtains non-author review of the changed claims. The original read-only reports describe the pre-correction findings; see the correction closeout and independent reviews for the current result. No professional approval or live website approval/authorship mutation is asserted. Repository ingestion must be verified before claiming a live-site change.

## Reduction plan

1. Retire the two unsafe orchestrators from filing use. Preserve neutral intake material and require a genuine official return/field map before any replacement is published.
2. Merge the duplicated VAT3 return into malta-vat-return with a slug alias and explicit moved/not-moved inventory. Distinguish goods acquisitions from services.
3. Merge rental method and canonical rental rules after fixing the short-stay and garage conditions. Merge property-transfer tables into the capital-gains/property core after resolving the historical-rate and valuation errors.
4. Turn the moving/family-office/planning hubs into short navigation-only routes rather than competing tax authorities. Leave advanced trusts, succession, participation, immigration and cross-border scopes open for other Maltese accountants.
5. Keep useful specialist material as unclaimed research with its actual limits. Do not delete research or count an empty slot as coverage. No technical slug retirement is executed by this attribution PR because repository removal alone does not retract a live platform Guide.

The substantive corrections in this batch carry changed-claim ledgers, old-topic destination maps and independent review. Future substantive corrections or technical retirements require the same evidence. The original read-only reports are preserved verbatim; references to unchanged metadata in them describe the pinned pre-change revision, not this PR's current state.


## Current correction evidence

- Personal corrections are recorded in the nine `personal-*` [ledgers](ledgers/) and [validation](personal-validation.json).
- [Business corrections](business-corrections.md), [required checks](business-pr-blockers.json) and [independent review](business-independent-review.md).
- [Property validation](property-residence-validation.json) and [independent review](property-independent-review.md).
- [VAT independent review](vat-independent-review.md) and [correction manifest](vat-correction-manifest.json).
- [Per-Guide ledgers](ledgers/) and complete original [personal workflow archives](personal-archive/).

The personal independent review records findings and their closure, including correction of an accidental licence edit, cohort ordering, residual TA24 metadata, student/retirement assumptions and crypto classification. Neither automated arithmetic nor non-author source checking is a licensed accountant's attestation.

See [CLOSEOUT.md](CLOSEOUT.md) for the final correction/test result, preserved preflight failures and remaining limits, and [personal independent review](personal-independent-review.md) for the final accepted personal batch.
