# Finland direct statutory reconciliation

23 October 2026. Continues the local country batch at `4a3d34ea`; no content push. The previous turn made concrete progress with the 2026 core rewrites, controls and source audit. This pass addresses selected legal gaps across the existing country pack.

## Retrieval and limits

The browser reader returned navigation shells for several Finlex consolidated pages. Direct HTTPS retrieval returned official HTML containing the Finnish statutory body in public server-rendered records. Extracted that body, retaining structural section headings, numeric child values and table cells. Checked every 2026 scale row against Vero's table. A first formatting assertion failed because table paragraphs introduce newlines; the subsequent whitespace-normalised comparison matched all numeric cells. No incorrect table was written into a Guide.

`2026-10-23-finland-direct-statute-retrieval.json` records eight statute URLs, raw/extracted SHA-256 values, selected sections and their hashes. Full source text remains in local research snapshots under `/private/tmp/oa-finlex-*`; the repository does not carry copied statute bodies. Retrieval is wider than substantive review: only the listed sections and relevant visible commencement notes were read. This is not independent review or a full amendment audit.

The attempted consolidated route for Act 1143/2025 returned 404. The actual amending Act was found in the official Statute Book PDF and read in full, including its transition. The working PDF is cited in the property Guide. No claim is made that the guessed route resolved.

## Findings applied

| Topic | Source work and resulting change |
|---|---|
| Individual core | Income Tax Act sections 30a, 38, 41, 96 and 124 and 2026 Scale Act sections 1–2. Added the start-up net-worth timing, election deadline, no-double-pension-deduction basis and Åland boundary. |
| Corporate | Income Tax Act sections 9, 119, 122 and 124. Confirmed selected current rate/loss rules and flagged listed-company/permit conditions. Section 9's displayed new PE-attribution reference starts in 2027 and was not used as 2026 law. |
| Residence | Income Tax Act sections 9 and 11. Connected ordinary home/presence, citizenship departure and part-year treatment to the law; retained special-service/treaty application as open. |
| TP | Assessment Procedure Act sections 14a–14c, 31, 32 and 32a, plus Vero documentation sections 6.6–6.7. Added control/actual-transaction analysis, method-selection principles, a gross cost-plus arithmetic control and scoped documentation sanctions. No benchmark was chosen. |
| CbCR | Assessment Procedure Act sections 14d–14e, 32 and 32a. Added statutory notification/report deadlines, secondary/surrogate gates, parent-refusal handling and scoped penalties. Live exchange relationships and current transmission specifications remain open. |
| Property transfer | Transfer Tax Act sections 4, 6–7, 15 and 20–21; Act 1143/2025 PDF. Added the contingent-consideration payment route and its contract-date transition from 1 January 2026, without moving the original payment deadline. |
| Payroll | Prepayment Act sections 9, 11 and 13. Added wage classification and the statutory cash withholding limit, with a conditional example that does not determine insurance recovery or a separate tax debt. |
| VAT | VAT Act sections 3, 84–85a, 102 and 114. Connected selected registration/rate/deduction principles to current wording and distinguished visible historical rates. Specialist supply and procedure rules remain open. |
| YEL | Sections 4, 89, 109, 112–112a, 114–115, 122 and 143, plus displayed review-transition provisions. Added consent above the review cap, the pre-2029 first-review condition for 2023–2025 starts, the disability-pension retrospective exception and scoped enforcement rules. Base-year monetary amounts are not 2026 indexed figures. |

Business Income Tax Act sections 7, 8 and 16 were also read. Their deduction framework and the visible 2026 membership-fee amendments require a later transaction-specific deduction pass; no blanket deduction catalogue is introduced here. The displayed 2027 PE-expense amendment was not treated as 2026 law.

## Verification and next action

31 executable controls across ten Finland source Guides pass, including the four added in this pass. Nine edited source Guides pass strict metadata audit against `4a3d34ea` with zero errors/warnings/notices, and whitespace checks pass. Every substantive source edit advances its version.

Next: refresh the expanded source-link snapshot, run the relevant repository checks, preserve a local reviewed-source checkpoint and obtain independent full-pack review before a single country content push. Named Finnish accountant review remains a separate open requirement. All seven domains stay partial; specialist gaps and legacy formation work remain in the README. No live filing, country completion or professional approval is claimed.

Final local verification for this pass: all 92 source URLs have HTTP 200 evidence without redirects. Six new statutory URLs were fetched, while the preceding 86 results retain their original check timestamps. The full repository suite passed 129 tests with `TMPDIR=/private/tmp`. No generated trees were changed and no Finland content was pushed.
