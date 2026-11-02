# Independent review: Chad listed-goods import eligibility

Decision: **changes required**, one blocking source-completeness defect. This review concerns only the new import-eligibility working paper at frozen commit `0a85c3bd65f4dc30edf9319cf52d04c395a1d305`. It is not acceptance of a completed customs filing, certification of current wider Chad law, or accountant attestation.

Independent reviewer: separate Codex review agent, 2026-11-01. Read `CLAUDE.md`, the complete `docs/skill-template.md`, candidate Guide, 12-row ledger, old-topic destination map and both initial draft receipts. No candidate content or initial receipts changed. Full source files, text and renders remain outside Git. The reviewer did not commit, push, open a PR, post comments or attest.

## Blocking defect

**P1: origin is missing from the wheat exemption decision.** Candidate Guide line 31 lists wheat with an exemption statement, line 40 marks goods supported by identity/use alone, and the intake has no country-of-origin question. This agrees with the September order's literal product list but fails to account for a specific finance-law rule identified during the parent review.

The actual [2026 finance law, article 65, PDF page 78](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=78) establishes a 5% customs duty from 1 January 2026 for three years on listed products of CEMAC origin. The list includes HS 10 01 wheat. Short original-language excerpts: `produits du cru originaires de la zone CEMAC`; `Froment (blé)`; `5%`. The reviewer independently downloaded this official PDF and read page 78 visually, including neighbouring articles 64 and66 and the complete article 65 table. Articles64 and66 concern different products and do not resolve the wheat interaction. No whole-law reading is claimed.

The September order article 2 names wheat, and article 3 repeals contrary earlier provisions. These texts alone do not establish how that ministerial order interacts with the finance-law charge or establish any enabling authority to remove it. This review does **not** conclude that 5% is finally payable. The unresolved question is whether the September exemption displaces the article 65 duty for CEMAC-origin wheat.

Required correction before narrow acceptance: hold CEMAC-origin wheat and wheat with unresolved origin for legal/customs reconciliation, with origin asked and recorded before the supported decision; alternatively exclude wheat from this job. Carry the conflict and official source into the Guide, ledger and relevant case/intake gates. Do not expand the article 65 finding to maize, rice or all foods: its wheat tariff row is specific. Parent owns all corrections.

## Twelve ledger rows checked

All twelve rows were compared with the complete signed two-page [Arrêté 135](https://ecofinances.gouv.td/wp-content/uploads/2026/09/Arrete-N135-Exoneration-des-droits-et-taxes-sur-les-produits09092026164852.pdf). Both pages were rendered from an independent download and visually read, including the preamble, neighbouring clauses, full operative text, signature and stamped `09 SEP 2026` date. Hashes and candidate identity are in `check-results.json`.

| ID | Result | Review evidence |
|---|---|---|
| 1 | Pass within order | Article3 takes effect from signature; stamped date is 9 September 2026. Restricting this Guide to post-signature imports is consistent with its defined job. No retrospective relief asserted. |
| 2 | Pass within order | Article1 names forage seeds, fodder, feed and other products exclusively intended for livestock feeding. The use gate is preserved. |
| 3 | Pass within order | Article1 names equipment/materials intended for drilling, pumping and water supply. No restriction to a particular type of taxpayer invented. |
| 4 | Pass within order | Article1 ties agricultural equipment, machinery, materials and inputs to forage-crop production. General farm machinery is not automatically accepted. |
| 5 | Pass within order | Article1 states exemption from duties and taxes on importation for its listed goods. No numerical zero rate or domestic-sale exemption inferred. |
| 6 | **Blocked** | Product list and cereal-flour exclusion match article 2, but the blanket wheat decision lacks the article 65 origin conflict gate described above. Literal source fidelity is insufficient for acceptance. |
| 7 | Pass within order | Article3 assigns implementation to the Director General of Customs and Indirect Duties. |
| 8 | Pass within order | Article3 repeals contrary earlier provisions. This was checked as the order's wording, not accepted as proof it overrides a statutory charge. |
| 9 | Pass within order | Entire three-article text has no application form, application deadline, HS table or turnover threshold. Negative statement is limited to this order. Ledger's short heading excerpt is not the sole basis for this absence check. |
| 10 | Pass within order | Entire order supplies no penalty, interest figure or appeal timetable. Wider customs rules expressly remain outside this job. |
| 11 | Pass within order | Import wording does not itself establish domestic-sale, input-credit, treaty or origin treatment. The external article 65 rule nevertheless must gate wheat. |
| 12 | Pass within order | Operative articles contain no fixed expiry date. Candidate disclaims any blanket absence-of-amendment certification. |

Figures/rule rows checked: 12; 11 confirmed within the cited order, one blocked by the additional official source. Fixes made by reviewer: 0. Lost content restored: 0; this adds a distinct job and does not rewrite/delete a legacy Guide. No additional research was pursued beyond the specific official source needed to test the failed wheat condition.

## Cases, boundaries and preservation

Both examples independently recompute: 3,000,000+1,000,000=4,000,000 supported and 0 held; 2,000,000+4,000,000=6,000,000 supported plus 6,000,000 held=12,000,000 shipment total. They reconcile hypothetical invoice values, not customs value or a tariff liability. Case 2 correctly decides to hold a general-use tractor with unresolved forage-production use. Neither case uses wheat, so neither arithmetic result changes because of the blocking defect.

The candidate distinguishes supported product wording from release approval and tax liability. Missing classification/codes/procedures, valuation, independently chargeable fees, dispute deadlines and live amendments are explicitly unresolved. The README states all seven domains partial and the six retained Guides unrefreshed. No false complete-country, broad-current-law, completed-filing or accountant-review claim found.

All six legacy Guide hashes match the original capture, the frozen parent and fetched origin/main. All82 legacy heading/bold-bullet/table topics have matching same-file destination entries: formation 14, corporate 17, income 16, payroll 11, overview 12, VAT 12. Full-byte equality also preserves prose and CTA text beyond those topic entries. Their 2025 law/secondary-source claims are not recertified. All four candidate manifest entries match; both draft receipts also match the frozen commit. See exact hashes in `check-results.json`.

## Commands and results

Reproducible mechanical/preservation checks: `python3 evidence/ledgers/chad-review-20261101/review-checks.py`. The script records full argv, stdout, stderr and exit codes in `check-results.json`, using the supplied private PYTHONPATH dependency directory.

- `python3 scripts/skill_checks.py skills/chad/td-import-exemption-eligibility.md`:15/15 pass.
- `python3 scripts/check-examples.py --require skills/chad/td-import-exemption-eligibility.md`:1 file, 2 blocks, 0 failures, 0 missing.
- `python3 scripts/validate-guides.py --changed-only --no-index-check`:1 Guide checked, 0 errors, 0 warning groups. README is the second changed guide-path file and is not treated as a Guide by the validator.
- `git fetch origin`: initially failed under the restricted network with `Could not resolve host: github.com`; approved ordinary retry succeeded and advanced origin/main from db5bf4ff7 to 9c691b5e9. HEAD remained frozen and is ahead 1/behind 16. Review does not claim the branch is rebased.
- Web-reader opens of both official PDFs returned internal access errors. Direct `curl --fail --location --max-time45 --output <private-file> --write-out '%{http_code} %{size_download} %{url_effective}' <official-URL>` downloads succeeded: order HTTP 200 / 668632 bytes; finance law HTTP 200 / 15295926 bytes. No CAPTCHA, disguise or archive used.
- `pdftoppm -r140 -png <private-order.pdf> <private-prefix>` and `pdftotext -layout <private-order.pdf> <private-order.txt>` succeeded. Both page renders visually inspected.
- `pdftoppm -f78 -l78 -r145 -png <private-finance-law.pdf> <private-prefix>` succeeded. Relevant page 78 visually inspected, including full article 65 and neighbouring 64/66. This is selective reading only.

Still unconfirmed: the exact legal/customs reconciliation of article 65 with the September order; the previously listed live filing, classification and wider-law matters. **Do not promote this frozen candidate as independently accepted until the wheat gate is corrected and the changed evidence is reviewed.**
