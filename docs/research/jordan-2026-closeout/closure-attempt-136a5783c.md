# Jordan repair closure attempt at 136a5783c

**JR01-JR06 are closed for the conditional source baseline. JR07 still needs three bounded evidence repairs.** Limited source-baseline publication is acceptable in principle with the retained holds, but this head is not yet cleared because its RATES evidence group contains unrelated secondary search material and two associations omit relevant quoted clauses.

Inspected frozen head: `136a5783c6dab634956fb39aaff94d48131f43ea`. Initial review: `2cec36c47e29f010fe0884693d40018c1313df7e`. Actual base: `46c01152da0fdd1b722f61190c88413d0a195d02`. Read date: 2026-11-01.

The entire Guide repair diff and all 18 substantive affected rows were checked. Timely declared-tax payment, partial imported-service triggers and their proportional limits, foreign-branch income, ordinary full SSC coverage, the 60-day interest condition, interest-WHT scope/exclusions, unsupported GST entitlement holds, national-contribution cessation and the advance-payment extension are now stated correctly within the identified baseline. No current filing clearance follows.

## Remaining evidence-only repairs

1. **GST C013:** retain `GSTBASE` and add `GST7`, in both `explicit_row_evidence_associations` and its ledger cell. The tied-supply sentences are quoted in GST7; GSTBASE quotes only the buyer-price fragment.
2. **Payroll C002:** retain `SSC3` and `IT12`, and add `SSC20` in both places. The employee names/data duty is in SSC20's article 21 excerpt; SSC3's excerpt covers coverage exceptions.
3. **Replace RATES' wrong transcript slice and add actual schedule-title provenance.** The current extract includes unrelated secondary search results and author commentary. Its lines match the cache, but they do not support the claimed list-title evidence. Use the cached primary blocks below. Add `SCHEDULES` as a source/evidence group for the opened schedule-list titles. Safe associations are GST `C008=[GST7,SCHEDULES]`, `C009=[RATES,SCHEDULES]`, `C049=[SCHEDULES]`, `C050=[RATES]`. Preserve the remaining source-baseline, classification and currentness holds.

Actual historical opened-list output is in sibling `sources/agent-a2a55474814cab15f.jsonl.source-extracts.txt`, **lines 1613-1639** (the longer duplicate runs through 1684). Full-cache SHA256: `7306da4a428260389fef9754073974ff1c736f84a869191feea68c4e42f84886`. It is the original author's retrieved official file-list output, reread now, not a fresh fetch and not the contents of the linked schedules. It states exactly:

```text
كشف السلع الخاضعة للضريبة بنسبة 10%
كشف السلع الخاضعة للضريبة بنسبة 5%
كشف السلع الخاضعة للضريبة بنسبة 4%
كشف السلع الخاضعة للضريبة بنسبة 2%
جدول رقم 3 الخاص بالسلع والخدمات المعفاة من الضريبة-  ثانيا الخدمات المعفاة
جدول رقم 3 الخاص بالسلع والخدمات المعفاة من الضريبة-  اولا  السلع المعفاة
```

The source URL is the [ISTD schedules list](https://www.istd.gov.jo/AR/List/%D8%AC%D8%AF%D8%A7%D9%88%D9%84_%D8%A7%D9%84%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9_%D8%A7%D9%84%D8%B9%D8%A7%D9%85%D8%A9_%D8%B9%D9%84%D9%89__%D8%A7%D9%84%D9%85%D8%A8%D9%8A%D8%B9%D8%A7%D8%AA). The actual rate-search first-page output is in the **same cache, lines 2324-2371**, corresponding to the [ISTD rates search](https://www.istd.gov.jo/AR/List/%D8%A7%D9%84%D9%86%D8%B3%D8%A8_%D8%A7%D9%84%D8%B6%D8%B1%D9%8A%D8%A8%D9%8A%D8%A9). These two read scopes should remain separate.

`independent-additional-search.json` also contains an official ISTD schedule-list **search result** beginning at character 11044 of the decoded JSON string. It corroborates the titles, but it must not be labelled as a separate opened-list read. The historical actual list output above is sufficient; no new source hunt is needed. The JSON receipt embeds the full exact primary excerpts and locators.

## Evidence and integrity

All 220 current ledger texts match the Guides and all 220 explicit association keys exist. The 218-row historical destination tables remain byte-identical to the initially reviewed versions. All nine initial review receipts match their recorded hashes. All 13 non-null source-manifest cache hashes match. All 931 nonblank new quoted lines were matched to the retained primary/transcript/Arabic-OCR cache; the wrong RATES selection demonstrates why textual identity alone is not proof of relevance.

Formation, all six full CTA suffixes and platform metadata remain preserved. The exact-head author validation receipt was read and matched: 75 shape checks, 10 examples, changed-guide validation, strict metadata and whole-base whitespace checks pass. This focused closure did not repeat those unchanged checks.

Four of the original 34 mapping rows remain affected by JR07 (`GST C008/C009/C013`, `payroll C002`), plus two related source-read rows (`GST C049/C050`). All 18 substantive wording rows are repaired; no new operative tax conclusion is required to finish these evidence fixes.

JO-IT-CURRENT, JO-GST-CURRENT, JO-SSC-CURRENT, JO-SSC-REDUCTION and named application holds remain open. No native GitHub approval, merge, Guide edit or commit was performed or asserted. The original review is preserved. A focused independent check of the bounded evidence repair can close JR07; it will not close operative-law currentness.
