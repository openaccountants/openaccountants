# Independent staged-delta review, 31 October 2026

Verdict: **changes required** on candidate commit `1cb2c0f59aa4fd2e31975cf307614acd86617c48`. This review covers the two new levy Guides, their ledgers and the README delta. It does not establish full-country coverage, filing readiness or accountant attestation. Exact candidate hashes are in `initial-candidate-manifest.json`.

The reviewer did not write the candidate. Read CLAUDE.md, docs/skill-template.md and docs/OWNERS.md. Checked **47 ledger rows** (18 environmental and 29 coal) against complete relevant source context and recomputed **four examples**. Every supplied quotation agrees with its full source. The row-by-row interpretation record is `row-checks.json`. One supplied rule is missing from the Guide, as described below.

## Required fixes

| ID | Priority | Location | Finding and repair |
|---|---|---|---|
| F1 | P2 | coal Guide, The base; ledger R005 | Act section 2 fourth paragraph allows shipment security to be required. The ledger accurately supplies it, but the Guide has no security instruction or reservation. Add the sourced rule and require the actual security demand/rules. Do not invent a percentage. |
| F2 | P3 | both new descriptions | The environmental description has 55 words and coal has 53. The frontmatter specification requires 80 to 150. Expand grounded scope and routing descriptions. The automated shape checker does not catch this. |

F1 source: https://lovdata.no/dokument/NL/lov/1925-07-17-2, section 2 fourth paragraph. No other incorrect tax figure or supplied legal interpretation was found in this staged delta. Recheck the repaired exact bytes and regenerated ledgers before approving the additions.

## Interpretation checks

Coal: read sections 1 to 11 and the entire 2026 charging decision. The seasonal achieved average FOB method, CIF paid freight/insurance adjustment, actual charter cost versus discretionary own-vessel freight, actual exporter bunker use, corresponding producer joint liability, 31 December book/account duty, office assessment, registered dispatch/office-availability clocks, appeal receipt deadline, appeal extension, payment despite appeal, NOK 100 interest condition, and supplementary-assessment clocks agree with the sources. Summed all ten progressively increasing band widths independently: cumulative bounds are 100,000; 300,000; 600,000; 1,000,000; 1,500,000; 2,100,000; 2,800,000; 3,600,000; 4,500,000; 5,500,000 tonnes. The text does not extrapolate a rate thereafter or apply coal rates to all minerals.

Environmental levy: read regulation sections 1 to 8, Environmental Protection Act sections 3(i), 78 and 96 context, the full resident refund page and the relevant Governor pages. Valid population-register status, personal-versus-employer payer route, completed outward-travel evidence, three years from actual travel, ticket collection and private-boat payment are supported. The authority procedure describes practical ticket collection followed by refunds; the Guide correctly keeps the statutory resident prohibition/exemption distinct. No aviation exemption is invented. Its unverified incorporated-tariff exception scope remains explicit.

Independently followed the Fund's displayed form link in a normal browser. The initial screen confirms the title and three separately displayed access labels. Privacy acceptance was unchecked. No acceptance, login, without-login opening, data entry or submission occurred. `refund-form-browser.txt` preserves the observation. No private fields or completion receipt were verified.

Arithmetic: visitor 12 x NOK 150 = NOK 1,800; resident private claim 3 x NOK 150 = NOK 450 and separately routed employer amount 2 x NOK 150 = NOK 300; coal first band NOK 500,000; adjusted coal FOB NOK 147 million / 150,000 = NOK 980, duty NOK 980,000 + NOK 441,000 = NOK 1,421,000 and flat-rate overstatement NOK 49,000. Fictional inputs are visibly assumptions. All four `oa-check` blocks pass the standard script. Both Guides pass all ten automated shape checks. Commands and outputs are in `checks.json`.

## Preservation and README

Compared all six earlier Guides to commit `e0ac02e13c68a2bf6a36b3e3f70fa3b618d2a3ec` at `skills/international/svalbard/`. All six are byte-identical after relocation. Verified every byte-exact destination entry in the preservation table, including all 693 prior Guide nonblank lines and 46 unchanged README lines. Reviewed the two changed README narration rows: count expands from six to eight and actual 24/31 October read dates remain separated. Lost content restored: **0**; no old Guide content was removed. The 24 October independent review is unchanged. See `preservation-checks.json`.

The README keeps three domain gaps and further ordinary job/operational gaps explicit, keeps issue #424 open, distinguishes SJ metadata from Jan Mayen research, and does not represent the additions as full-country coverage or attestation. Its statement that the two new Guides await review was accurate at the reviewed candidate. Document-transfer exclusion was independently checked against Kartverket's Svalbard subsection (updated 1 January 2026): https://www.kartverket.no/eiendom/dokumentavgift-og-gebyr/fritak-for-dokumentavgift. Registration fees remain separate. Customs territory exclusion was checked in Customs Duty Act section 1-1(2), https://lovdata.no/dokument/NL/lov/2022-03-11-8, and customs controls remain distinguished in https://www.toll.no/no/bedrift/import/tolletaten-pa-svalbard/ (updated 27 November 2025). These are applicability checks, not a positive audit of every remaining charge.

## Evidence and limits

All seven supplied raw HTML and reader-text receipt hashes match. Every candidate-manifest hash matches. Reviewer direct shell fetches failed DNS resolution; web fetching Lovdata returned 405. The normal browser then opened and displayed all seven cited official source pages successfully, including complete operative Lovdata contexts. Browser source captures and their hashes are in `sources/` and `source-checks.json`. No CAPTCHA, access disguise or archive fallback was used. No authority was contacted.

The declared gaps are unresolved: current incorporated aviation exceptions, carrier remittance/settlement, refund fields/receipt beyond access, departmental coal book format/evidence/transmission, current coal interest rate, and exports beyond the final listed coal band. These gaps prevent a filing-ready or country-complete verdict. The reviewer did not run repository-wide CI or attest the older six Guides afresh; preservation and the staged tax delta are the bounded review.
