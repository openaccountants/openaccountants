# Guinea bounded source and preservation checkpoint, 1 November 2026

Baseline: a7888d0d6c1f7cb0fed13d8d3f6b7e05f1d12297. Worktree: codex/guinea-tax-2026. Writer checkpoint only; independent review pending, no accountant attestation.

## Actual source scope

The [DGB 2026 law page](https://dgb.gov.gn/2026-lf/) links the [enacted LFI bundle](https://dgb.gov.gn/wp-content/uploads/2026/04/Loi-de-Finances-Initiale-2026.pdf). The writer downloaded the actual 10,628,785-byte PDF, read law pages 19–24 and promulgation pages 27–28 through French OCR, and visually checked pages 20,21,27. The source includes signed decree D/2026/0103/PRG/SGG dated 31 March 2026, expressly promulgating L/2026/010/CNT. The earlier `/2026/02/loi-de-finances-en-vigueur-1.pdf` download has identical bytes to the canonical April link. PDF SHA-256: `676d0032a8c1eb447081af70a91700bd4ec484070e3e458f2305d4307298f33b`.

Only complete replacements of CGI265 (LFI art.14) and CGI383 VI (LFI art.13) are drafted. Scope, valuations, exemptions and procedures outside those replacements are not inferred from an unavailable consolidated CGI. The official [DGB projects list](https://dgb.gov.gn/projets-de-lois-de-finances/) lists a rectifying project; the [Assembly's 29 October account](https://assembleenationale.gov.gn/plfr-2026-intercom/) describes examination, and the [Guinea embassy's 1 November report](https://sn.ambaguinee.org/?p=119469) describes adoption of the receipts portion on 31 October. None establishes the final promulgated amendment text. Its status and effect remain a source gap, rather than a bill treated as law.

The [Ministry code library](https://mbudget.gov.gn/codes/) returned 403 through direct fetch and an ordinary Brave browser visit. The [DGI 2021 document](https://dgi.gov.gn/wp-content/uploads/2021/12/Code-G%C3%A9n%C3%A9ral-des-Imp%C3%B4ts-2021.pdf) is search-indexed as a project, not relied on as enacted law. The APIP code page opened but exposed no operative text/download. No claim is made that these attempts establish current corporate/PAYE/VAT/CNSS rates.

## Preservation and validation

Six legacy files remain byte-identical to the baseline, including their platform fields and complete CTA suffixes. The complete destination map records 65 legacy topics/context items, all retained as historical and unverified for 2026. Two new Guides have 25 legal ledger rows and four recomputing cases. All seven country domains remain partial; TP/XB remain missing.

Each new Guide passes all fifteen `skill_checks.py` checks. Four executable examples pass. Scoped validator, strict metadata integrity against the pinned baseline and full baseline diff whitespace check are required at freeze. Private full captures, OCR and page images are in the sibling `sources/` directory outside this Git worktree.
