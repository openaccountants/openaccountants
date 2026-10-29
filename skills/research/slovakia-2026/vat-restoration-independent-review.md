# Independent Slovakia VAT restoration review

Date: 27 October 2026. Result: **PASS for the 24 restored units, the corrected old/current coverage account and exact preservation checks described here.** Two finite findings were raised and corrected by the integrating author. No further finite finding remains in this restoration delta. This is an independent source review of a tier-2 draft, not a Slovak accountant's attestation or certification of a completed country pack.

Final Guide: `skills/international/slovakia/slovakia-vat-return.md` in the `europe-slovakia` worktree. Frozen SHA-256: **7509ed359239a39aa2e136e9c018a7cdc4b496094021222e21d1a41097198766**.

## Actual comparison and scope

I read the whole 716-line pre-rewrite Guide at `c9c520db^1`, the current return at `187064a83bc15251730448448f9ed8a57a388ba6`, the integrated return and the actual linked registration and EU VAT Guides. I verified the old/current snapshots against the actual Git objects, rather than relying on the writer's ledger. The old Guide has 6,484 words; the main rewrite has 3,872, a 40.2838% reduction. The final integrated Guide has 5,907 words. The historical shrink therefore required a substantive disposition ledger even though the integrated text is longer.

Original old SHA: `20fb3aabb198b7ebc98b559691d7cdc6fe1982a2bc00e8c80863b3b22d048c1a`.
Main baseline SHA: `cb21ae475f7bf28d1e02ad30419c41512e100b8a6c5b2b9038bc34af1eb04d80`.
Writer's first integrated SHA: `f0655378e1c04468ee77b35a674e60080c784329d38a7cf1a4fad98fd1d4f54c`.
After the price-reduction finding: `bb2cb03570ea6f277ce4a40b300be353a5f21414eb99ed7472a7bfc25acd6279`.
Final after export-evidence restoration: `7509ed359239a39aa2e136e9c018a7cdc4b496094021222e21d1a41097198766`.

The 23 writer units all appear in the integrated text. They restore/correct the ID format, underlying-supply classifier, exemption catalogue, going-concern treatment, international transport services, private/free supplies, gifts, capital-asset register, eligible import self-assessment, credit notes, property age/election, N1 and historical-car boundaries, groups, import representation, electronic returns, Intrastat, EC-list sanctions, repeat fines, amendments, refunds and original-rate corrections. `independent-item-check.json` records each independent conclusion and the actual authority read. A separate 24th unit was necessary because a claimed sibling mapping did not exist.

The full old section/test disposition account now distinguishes retained methods, actual sibling coverage, corrections of erroneous old law, duplicated examples and expressly unconfirmed methods. Direct-tax/Malta digressions and AI-engine instructions are not missing Slovak VAT taxpayer rules. Old incorrect rates, arbitrary box mappings, automatic deduction entitlements and unsupported refund guarantees were not reinstated merely to preserve words.

## Findings and exact closures

**SK01, price-reduction exception.** The first restoration said later price decreases require a correction without stating the VAT Act §25(6) exception. The actual law permits no correction of the tax base/tax when a post-liability price reduction is made to another payer and both parties agree in writing. The final paragraph states that exception expressly and does not extend it to cancellations or increases generally. The restored correction timing, §53 input adjustment and original-rate instruction otherwise match the actual §§25/53 bodies. [Current VAT Act §25](https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html#paragraf-25).

**SK02 / R24, lost export evidence.** Old EC13 expressly required customs documentation. The writer's section map twice claimed that export evidence was in the linked EU Guide. I read that actual sibling: it contains no such export-evidence method. The current return merely named the §47 exemption. The final goods bullet now states §47(3)'s dispatch/transport evidence plus customs confirmation of EU exit, including its specified alternative-evidence route for oral/deemed export declarations. Both false sibling assertions were corrected in the map and R24 added to the ledger. The final single-bullet addition reverses to the exact previously reviewed `bb2cb035…` hash, so no other method or source changed in this final delta. [Current VAT Act §47](https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html#paragraf-47).

The historical writer proposal remains a 23-unit artifact. The current restored count is **24**, not 23. A sibling coverage mapping is evidence that a topic is present, not a new certification of that sibling's whole law. In particular, the shared EU Guide contains broad import wording; the explicit Slovak §84a method and the shared Guide's stated country-priority rule govern the national import exception.

## Primary bodies independently checked

Before reuse, I recomputed all four recorded raw-body hashes: the full 2026 VAT Act browser DOM body, the current 2026 Tax Procedure Code browser DOM body, the official EC-list methodology PDF and current EC-list HTML. I then read the actual relevant provisions and full substantive administrative passages. The PDF was independently extracted with `pdftotext`; its extraction was byte-identical to the text actually read. These were source bodies, not the writer's conclusions. Exact receipts are in `verified-source-receipts.json`; the relevant law extracts are beside this report.

The VAT reread covered §§4a–4b, 8–10, 24–25, 28–29, 31, 38–39, 41, 46–47, 49, 51, 52a, 53–54, 54a, 54d, 69(12)(c), 69a, 79, 84a, 85kp, 85l and 85n. The Tax Procedure Code reread covered §§14–16, 55, 69, 79, 154–155. These establish the actual restored thresholds, periods, taxpayer conditions, correction timing, refunds, sanctions and transitions. The full-body VAT receipt is SHA `acc5a74c44c5efe077cdcd84dfe42b53c26faf1e95ddb1861767b2f26ff699c6`; the Tax Code receipt is `2c8ed12052b2ca1c3b817a8a64f756398983b496eb62945c5b518d0e890fced4`.

I also opened fresh official bodies: the historical January 2024 VAT Act's §27, January 2026 Tax Code §§16/69/155, the Finnish tax authority's actual Slovak VAT-number row, the current Slovak filing/EC-list pages and the actual Intrastat instructions. The January/current Tax Code checks support the restored procedure and sanction figures throughout 2026. The historical VAT check supports 20%/10% examples while retaining the distinct 5% route. The 2018 EC-list PDF is used for sanction classification, not as authority for the 2026 monetary range. `fresh-web-receipts.json` records those reads honestly without inventing raw-response hashes.

## Independent verification and preservation

**87 source-receipt, arithmetic, boundary and preservation assertions passed, plus seven final export-delta checks.** These are transparent assertions in `check.py` and JSON records, not 94 independent legal opinions. Both existing `oa-check` examples were parsed and evaluated independently: restaurant output VAT 10,080/payable 5,480; consultancy output 7,360/input 4,485/payable 2,875. The March return's Saturday 25 April deadline moving to Monday 27 April 2026 was checked.

Additional controls include the inclusive €17 gift limit; strictly-more-than €1,700 movable-asset definition; first-use-inclusive five/twenty-year periods; the 40% property reset boundary; a six-year office without a resetting event; complete import base and €11,500 self-assessment/deduction; ordinary/centralised AEO eligibility differences; €46 N1 fuel and €23 mixed-car running-cost deduction; historical 20% correction rather than today's 23%; each condition of §25(6); greater-than-€5 cash-refund control and offsets; €100/€10,000 fine endpoints; equal-amount repeat fine; assessment-year origin, next-month discovery deadline; and Intrastat calendar/weekend rules.

The original protected metadata fields and entire CTA tail are byte-identical across old/main/integrated versions. Current description/category/year are preserved; the description has 125 words. Only the intentional version/date update changes those administrative fields. All nine content H2s and the existing CTA H2 remain exact. Both executable blocks, contribution line and final reservations remain unchanged. Reversing the individually identified added paragraphs, two sanction rows, question extension, seven source rows, import replacement, export-evidence addition and intentional date/version updates reproduces the **entire** main-baseline file exactly. This proves unrelated bytes were preserved; it does not independently revalidate every inherited baseline sentence.

## Remaining limits

The final Guide still expressly reserves 2026 return-row numbers/control-statement layout, date-specific ECB rate inputs, the first-breach rule's application to the separate control-statement sanction, and §50 coefficient detail. In particular, old provisional/final coefficient and rounding/de-minimis assertions have an explicit disposition as unconfirmed; this review does not establish that they are usable current methods. These ordinary matters remain ordinary unfinished work where required for the wider objective. They are not converted into specialist exclusions by this PASS.

No whole-country completion claim follows from this narrow restoration review. No Guide was edited, committed or pushed by this reviewer. No real taxpayer session, filing or licensed attestation was involved.
