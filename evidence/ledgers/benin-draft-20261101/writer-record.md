# Benin writer record, 1 November 2026

This is writer evidence for eight source-cited draft Guides, not independent pack review, accountant attestation, completed registration or completed tax filing. Pinned base: `a7888d0d6c1f7cb0fed13d8d3f6b7e05f1d12297`; branch `codex/benin-tax-2026`. Repository root, branch and status were inspected and `git fetch origin` completed before writing. The pinned base remains the comparison; no rebase or reference rewriting was performed.

## Actual scope

Six legacy jobs were refreshed: monthly salary ITS; ordinary IS/minimum/instalments; monthly VAT for confirmed VAT status; VPS; SARL/SA formation preparation; and the routing/general-sanctions overview. Two missing jobs were added: TP pricing/reporting/documentation screening and domestic cross-border withholding classification. The read CGI and June-law provisions support these bounded jobs. All seven tax-domain rows remain partial in the country README. CNSS, the VAT threshold instrument, individual treaties, special distribution/gain/rent computations and authenticated forms are expressly unresolved. No whole-country or whole-law reading claim is made.

The complete original-topic destination table contains 81 headings/bold topics, excluding unchanged CTA boilerplate. Six legacy CTA tails and the `review_status`, `trust_label` and `license` fields are byte-identical to the pinned base. No legacy Guide was deleted. Every replacement is longer than its old body. Eight ledgers contain 113 rule/example rows with short French excerpts, source URL/article and read date.

## Official source access and read scope

The obsolete `api.impots.bj` CGI URL failed DNS/502. The current public DGI site `https://www.impots.bj/` loads `/static/js/main.ba57ecb6.chunk.js`; its public axios base is `https://apisiteweb.impots.bj/api/`. Its documents listing `https://apisiteweb.impots.bj/api/documents?order[annee]=desc&page=1` supplied the observed current CGI/original-finance/rectifying-finance PDF paths. These were fetched without credentials; no authentication or access restriction was bypassed. The public list's `isDeleted` flags were not treated as proof of legal repeal or validity. The signed documents and their dates determine the legal source used. Only public-host provenance is recorded here; full HTML/JavaScript remains private and is not part of this contribution.

- [DGI CGI 2026](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf): cover/title and the article ranges listed in each Guide's Sources read in native extracted text with surrounding conditions. It explicitly consolidates law 2025-22 of 8 December 2025, not the June amendment. Selected PDF pages 1, 29, 48, 49, 62, 63, 89, 116, 117, 203 and 239 visually checked. The literal-quote check covers 90 CGI ledger excerpts after typography/whitespace normalisation; this is not a substitute for independent row-by-row review.
- [Signed original LF 2026](https://budgetbenin.bj/storage/2025/12/Loi-des-finances-2026.pdf): tax articles 1–17 read from French OCR, pages 2–5 visually checked. In particular, current gas/motorcycle relief, preserved separate levies, BTP fuel deduction and refund deadline were read. No reliance on the CGI's stale 2024 relief footnote.
- [Signed law 2026-10 of 24 June 2026](https://apisiteweb.impots.bj/media/6adcb8249c4ab_B%C3%A9nin-Loi%20de%20finances%20rectificative%202026.pdf): PDF pages 1–6 and 17 visually read, tax articles 1–19 and final 48–49, plus adjacent article 20 heading. Budget tables on other pages were not reviewed merely because all pages were OCR-captured. Article 1's income-period rule is explicitly retained; signature date alone is not used to determine an income period.
- [National SARL decree 2014-220](https://monentreprise.bj/Decret_N_2014_220_du_28_mars_2014_portant_modalites_de_creation_des_Societes_a_Responsabilite_Limitee_a73a58faf6.pdf): pages 1–4 visually read, arts. 1–11/signature. Actual signed date is 26 March 2014, despite the portal/filename saying 28 March. Annex model statutes were not fully reviewed.
- [Signed OHADA AUSCGIE](https://biblio.ohada.org/doc_num.php?explnum_id=2032): arts. 140, 309–311-1, 376, 387–389 and 694 with adjacent text; selected pages 36, 77, 93, 95 and 161 also visually read. No whole-240-page reading claim. Signed quarter-capital and two-of-three audit rules take precedence over conflicting portal summaries in these drafts.
- APIEx current public pages `/creer/societe`, `/informer/couts-delais`, `/informer/pieces-requises`, `/informer/processus` and `/informer/certificats`: packet, fees/exclusions, complete-file processing target, six public stages and certificate descriptions read. Authenticated upload, checkout, validation and receipts were not accessed.
- [CNSS contribution guidance](https://cnss.bj/procedure-de-recouvrement-des-cotisations/): HTTP 500 in direct and web retrieval; ordinary Brave browser displayed a WordPress critical-error page. No successful read date or current contribution percentage is claimed.

Complete source PDFs, HTML, native text, French OCR, renders and fetch-error receipts remain in the private sibling `../sources`, outside Git. `source-capture-manifest.json` records public URLs and byte hashes for sources used. Capturing an entire source is distinguished from the actual read scope above. Failed old URLs and merely downloaded but unread alternatives are not authority for a Guide rule.

## Validation

Reproduce with:

```sh
PYTHONPATH=/Users/michaelcutajar/Documents/ChatGPT/OA/output/finland-pack-2026-10-26/validation-deps python3 evidence/ledgers/benin-draft-20261101/writer-checks.py
```

`check-results.json` records actual argv, stdout, stderr and exit status for every final command. The pinned adapter changes only the validator's comparison functions in memory, without changing repository scripts or Git refs. It includes the staged/working candidate against the pinned base and skips generated index freshness under the repository's contributor mode.

All 15 scoped checks pass for all eight Guides. All 16 executable examples pass. Strict YAML/types, six baseline hashes, 81 topic destinations, CTA/platform preservation and both staged/unstaged whitespace checks pass. Pinned validator: zero errors, one warning group: its slug heuristic classifies the new cross-border-withholding job as payroll withholding as well, alongside the different VPS job. The warning is reported, not suppressed; the jobs and their ownership/routing are distinct. No generated index/bundle, package, ownership or unrelated country file is changed.

Writer QA found and fixed an initially vague formation read-scope phrase, two extra EOF blank lines, and article 1's PDF-page fragment. Those fixes were followed by the final passing run. Independent source/example/legacy review remains required before acceptance or any push.
