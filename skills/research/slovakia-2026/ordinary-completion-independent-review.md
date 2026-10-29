# Independent review of the ordinary PIT/CIT additions

**PASS for F09, F10, F13, F14 and F19 on the exact final bytes below.** The initial corporate freeze had one ordinary negative-EBITDA boundary omission. It was reported, corrected by root, and the narrow correction was rechecked against the Financial Administration's actual FAQ 5. No other actionable defect was found in the assigned additions. This is a bounded independent review of another writer's additions, not a fresh review of the earlier root-authored repairs or a whole-country PASS. Independent AI review is not accountant attestation.

| Source Guide | Version | Final reviewed SHA256 |
|---|---|---|
| slovakia-pit.md | 1.3 | e6ac260e6292250752edbdf87384ca37da4cd0d5a845c257fd41a08092d1abbf |
| sk-corporate-income-tax.md | 0.3 | e20a2c9d720fe0c8802e778eaebd764868c36f9f9dcd08ea14ee6331a750b84a |

The comparison baseline is commit `265f91ff`. The initial writer-frozen CIT hash was `dde78468e9a3cdd71b5b96a29c8ab17bd19b897f96edd0196a6e770f4d42741d`; that complete initial file is retained separately. VAT files were excluded from this review, including root's concurrent form edits. The reviewer edited no Guides or Git state.

Both current Guides were read in full. The actual raw primary bodies were rehashed independently, and the assigned provisions reread directly: Income Act2(w),9(1)(r),15,17(38),17k,21a,22(6),26–27,30,33,33a,43(3)(v),51ea and the relevant transition provisions. The actual final 2023 mortgage text and 2026 Annex1 were read. Fresh live primary opens corroborated the current law, historical mortgage law, December31 text and both pages of FS21/DZPaU/2025/I. The new thin-capitalisation authority page was fetched as an actual200 HTML body and read. Raw-source hashes, fresh receipts and provision extracts are adjacent.

## The one finding and its closure

`OC-01`, F10, initially open at CIT line109 and the thin-capitalisation variant: the unqualified positive-EBITDA subtraction can exceed the covered expense when EBITDA is negative. With covered costs 100,000 and EBITDA −100,000, subtracting 25% of EBITDA gives a 125,000 adjustment. The [Financial Administration's FAQ 5](https://podpora.financnasprava.sk/663968-Pravidl%C3%A1-n%C3%ADzkej-kapitaliz%C3%A1cie-) says the covered interest is disallowed in full. The correct adjustment is 100,000.

Root's final correction supplies `allowed = min(covered, max(0, 25% × accounting EBITDA))` and `disallowed = covered − allowed`, explicitly covers zero/negative EBITDA, adds the primary source and executable100,000 boundary variants, and preserves the original positive example's25,000 result. That precise delta was rechecked and passes. The original finding remains in `findings.json` with its initial and final hashes, source and closure evidence; it was not silently erased.

## Assigned legal results

| Finding | Independent result |
|---|---|
| F09 child credit | PASS. Birthday months are inclusive, birth/adoption and specified entry months count immediately, changing child counts split the cap, and other-parent base aggregation uses eligible start-month proportions. Both the percentage cap and high-base taper apply to the augmented base. Both people meet the statutory 90% test. The original Peter result is preserved. |
| F09 mortgage credit | PASS. Historical pre 2024 branch remains 50% of certified interest attributable to up to50,000 principal,400 full-year cap and 1.3 reference-income multiple. Current branch is 50%,1,200 cap,1.6 multiple and own permanent housing. Application-age and contract-income dates, co-borrowers, one-contract/overlap,60-month window, partial first/last caps, payout, non-resident and death rules are separated. No invented official reference wage is used. |
| F13 micro status | PASS. Exact60,000 revenue boundary plus controlled-transaction, insolvency and short-period exclusions, including the death exception. Full loss use turns on status in the deduction period. Five-period expiry is retained. |
| F14 government bonds | PASS. Ordinary foreign bank interest 19%, non-exempt qualifying government coupon gross base 13%, and qualifying non-business retail-bond yield/sale exemption are distinguished. The temporary 16% rate is confined to 2025 payments. Section 43(3)(v) is not presented as a universal individual-bond withholding rule. |
| F10 interest | PASS after OC-01 correction. Actual contract-date transition, non-related debt scope, exclusions, sum of statutory bases, capitalised-interest treatment, five-period blocked-cost carry, strict 3m activation, actual 17k-increase switch-off of21a, back-to-back lending and separate21a capitalisation/no-carry rules are supplied. |
| F19 assets | PASS for the supplied ordinary classifications and methods. CPA/KS codes control the group: computers, ordinary cars, certificate-qualified BEV/PHEV, furniture and building classes are differentiated. Hotel/sports20–40-year original-asset period is separate from the at-least 10% improvements/repairs asset with six-year life. The actual FS guidance confirms below-threshold treatment and application to a 2025 return filed after 2025. |

Sources: [current Income Act](https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html), [final 2023 mortgage text](https://static.slov-lex.sk/static/SK/ZZ/2003/595/20230801.html), [actual Annex1](https://static.slov-lex.sk/pdf/prilohy/SK/ZZ/2003/595/20260101_5740211-2.pdf), [FS hotel/sports guidance](https://www.financnasprava.sk/_img/pfsedit/Dokumenty_PFS/Zverejnovanie_dok/Dane/Novinky_leg/Priame_dane_uct/2025/2025.06.27_021_DZPaU_2025_I.pdf). Assigned sections and retail 9(1)(r) were independently compared unchanged in the December31 text. Its 52zzzm postpones the listed care-related changes to 2027 returns.

## Independent controls and preservation

Fifty independently constructed boundary/arithmetic controls pass. They include exact/one-cent-over micro limits and exclusions; child birthday/birth/count-change/parent aggregation and high-base taper; old/new/full/partial mortgage caps and low actual interest; asset first-year depreciation and the exact 10% boundary; statutory interest denominator,3m activation, carry capacity/expiry and positive/zero/negative 21a EBITDA. They were written independently of the writer's checker. `decimal-controls.json` preserves actual/expected values.

The repository example checker passes for the two files: four oa-check blocks, zero failures and zero missing. Targeted invocation of the repository Guide validator passes with zero errors/warnings. Its first direct import needed the scripts directory on Python's import path; the corrected targeted run succeeded with the existing Python dependencies. No package was installed. Whole-country validation was not rerun against the concurrently changing VAT files.

Preservation is compared to the actual commit 265f91ff files, not word counts:

| Baseline content | Disposition |
|---|---|
| All frontmatter except intended version/date | Identical, including slugs, descriptions, tax year, jurisdiction, review status, trust label, licence and dependency metadata. |
| All source URLs, historical PIT MIT/40-contributor credit, bylines and complete CTA suffixes | Retained. Source rows are expanded/reread, not deleted. |
| Jana/Peter/Alfa/Beta examples | Every original input, original expected output and original step remains. The negative-boundary correction changes only a newly added thin-cap variant step; the four baseline examples remain intact. |
| PIT prior residence, rates, separate tax bases, expenses, allowances, rental/securities/dividends, deadlines, advances, penalties and cross-border routes | Retained. Micro, capital and credit shorthand is replaced by qualified methods; no original population is discarded. The mortgage unread-source reservation is resolved, not merely removed. |
| CIT prior base/add-backs,85n VAT treatment, general depreciation periods, micro depreciation, losses, dividends, minimum tax, filing, advances, financial-transaction pointer, sanctions, cross-border and specialist exclusions | Retained. The generic asset/interest paragraphs become explicit methods; their old statutory topics survive. Annex1 unread-source reservation is resolved. |
| Earlier root fixes | Retained as baseline content. They are not counted as newly independent work in this review. |

`preservation-controls.json` and the complete diffs provide mechanical evidence for metadata, sources and examples. The table above records the substantive replacement/migration judgement; shape checks alone are not treated as completeness evidence.

## Scope remaining open

The whole-country review remains open for the other findings and populations in the whole-pack report. In particular, this PASS does not close VAT annual actual denominator 0, special KV first-breach treatment, exact fixed-gross crossing circularity, VAT form/content changes, remaining payroll calendar/posting work, XB source/type/treaty 35% wording, ordinary TP correction charges/rate-threshold analysis, or historical removed-unit dispositions. Current form/ECB reservations outside the assigned PIT/CIT methods remain for root's separate source reconciliation. Unusual asset codes, financial-sector borrowers, reorganisations, treaty-specific facts and other expressly excluded specialist populations are not newly certified by these additions.
