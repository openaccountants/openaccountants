# Independent review: eg-transfer-pricing (v0.2) and eg-cross-border (v0.1)

- **Reviewer:** independent AI review agent (Claude), no shared context with the writer. The writer's source notes were used only to locate pages.
- **Date:** 2026-11-02
- **Files reviewed:** `skills/egypt/eg-transfer-pricing.md` (rewrite, compared against `upstream/main`), `skills/egypt/eg-cross-border.md` (new).
- **Rule applied:** docs/skill-template.md lines 1, 3, 5, 9 and 12.

## Sources re-read

All from eta.gov.eg. Scanned pages were rendered and read as images; text layers were read where they exist.

| Source | URL | What was read |
|---|---|---|
| Law 91 of 2005, original Gazette text | https://eta.gov.eg/sites/default/files/2024-03/law_no.91-2005.pdf | Page images, Gazette pp. 7 to 8 (arts. 1 end, 2, 3, 4 start), 18 (art. 24), 30 (arts. 47 to 49), 33 (arts. 52 items 3 to 6, 53, 54), 34 (arts. 55, 56) |
| Law 30 of 2023 | https://eta.gov.eg/sites/default/files/2024-03/law_no.30-2023.pdf | Text layer: art. 1 (art. 1 related person, art. 3 (b) (j), art. 4, art. 50 item 10, art. 52 item 1, art. 56 third para., art. 56 bis, art. 58 second para.), art. 2 (art. 4 bis, art. 46 bis 3 fourth para.), arts. 4 to 12 |
| Law 151 of 2026 | https://eta.gov.eg/sites/default/files/2026-08/law.no_.151.of_.2026.pdf | Whole text layer (arts. 1 to 7) |
| Gazette erratum to Laws 149, 150, 151 of 2026 (Gazette 32 bis, 8 Aug 2026) | https://eta.gov.eg/sites/default/files/2026-08/law.no_.149.150.151.of_.2026.retractation.pdf | Both page images. Not cited by the writer |
| Law 150 of 2026 (amends Law 206) | https://eta.gov.eg/sites/default/files/2026-08/law.no_.150.of_.2026.pdf | Whole text: replaces art. 38 first para. only, adds art. 27 bis. Not cited by the writer |
| Laws 152, 153 of 2026; MoF decision 450/2026 | eta.gov.eg 2026-08 folder | Read to rule out effect: dispute settlement renewal, stamp duty on listed share sales, dispute settlement rules. No effect on these two skills |
| Law 206 of 2020 | https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf | Page images, Gazette pp. 9 to 10 (arts. 9 to 13), 18 to 19 (art. 31), 24 to 25 (arts. 38 to 42), 30 (arts. 52, 53), 40 to 43 (arts. 68 to 81) |
| Law 211 of 2020 | https://eta.gov.eg/sites/default/files/2026-05/law_no.211-2020.pdf | Whole text layer |
| Law 7 of 2025; Law 5 of 2025 | https://eta.gov.eg/sites/default/files/2025-02/law_no.7.of_.2025.pdf | Law 7 whole text; Law 5 first pages (settlement of unregistered taxpayers, not relevant) |
| MoF decree 286 of 2021 (ER of Law 206) | https://eta.gov.eg/sites/default/files/2024-03/law_no.286-2021.pdf | Text layer: related-person definition, arts. 13 to 21 |
| ETA TP Guidelines (2018 ed.) | https://www.eta.gov.eg/sites/default/files/2026-03/egyptian-transfer-pricing-en-guidelines-2019-view.pdf | pp. 11 to 13, 40 to 48, 61 to 67, 84, 91 to 98 |
| ETA circular 1 of 2026 | https://eta.gov.eg/sites/default/files/2026-03/Dawry.no_.1.of_.2026.pdf | Page image (also quotes Law 91 art. 110 and Law 206 art. 53) |
| ETA Services Guide, 2nd ed. | https://eta.gov.eg/sites/default/files/2025-08/guide.of_.the_.egyptian.tax_.authority.services.second%20edition.pdf | Services 5/1 to 5/4, pp. 97 to 108 |
| ETA bilateral treaties page and income tax laws page | https://www.eta.gov.eg/ar/content/atfaqyat-thnayyt ; https://www.eta.gov.eg/ar/content/qwanyn-aldrybt-ly-aldkhl | Treaty table parsed (64 entries); laws page list of PDFs (found Law 150, 152, 153 of 2026 and the erratum) |

## Items checked

TP = eg-transfer-pricing, XB = eg-cross-border.

| # | Item | File | Source location | Result |
|---|---|---|---|---|
| 1 | Art. 30 arm's length rule, domestic and cross-border, APA power | TP | Guidelines p. 11 (law text as printed) | matches |
| 2 | Related person definition, four deemed groups, 50% of voting/management/profit/capital rights, attribution and employee/client rules | TP | Law 30/2023 art. 1, Gazette pp. 3 to 4; ER 206 definitions | matches |
| 3 | Who documents, PEs included, transaction list | TP | Law 206 art. 12; ER 206 art. 14 | matches |
| 4 | Master file, local file, CbC report or notification required | TP | Law 206 art. 12 first para. | matches |
| 5 | EGP 8,000,000 exemption, Minister may raise | TP | Law 206 art. 12 fourth para. | matches |
| 6 | Exemption measured on gross income plus expenses | TP | ER 206 art. 14 last para. | matches |
| 7 | Exemption scope (items a and b only) | TP | Law 206 art. 12 fourth para. | fixed (scope added; restores old "below threshold" point) |
| 8 | Minister may exempt from CbC report | TP | Law 206 art. 12 second para. | fixed (added) |
| 9 | CbC EGP 3 billion, foreign subsidiary condition | TP | Guidelines s. 5.5 p. 61; s. 5.8 p. 67 | matches |
| 10 | CbC EUR 750 million, filed in parent's country | TP | Guidelines p. 62, p. 67 | matches |
| 11 | CbC report or notification duty on all legal persons, free zone companies, PEs | TP | ER 206 art. 14 second para. | matches |
| 12 | 1% non-disclosure | TP | Law 206 art. 13 last para. (Law 211/2020 art. 1) | matches |
| 13 | 1% due even if disclosed in files | TP | ER 206 art. 16 | matches |
| 14 | 3% local file | TP | Law 211/2020 | matches |
| 15 | 3% master file | TP | Law 211/2020 | matches |
| 16 | 2% CbC report or notification | TP | Law 211/2020 | matches |
| 17 | 3% cap where several failures | TP | Law 211/2020 | matches |
| 18 | Base: total RPT for 3/3/2; undisclosed for 1% | TP | ER 206 art. 18 | matches |
| 19 | Thin cap 3:1 for 2024 to 2027, 4:1 2023, 2:1 2028 | TP | Law 30/2023 art. 5, Gazette p. 20 | matches |
| 20 | Permanent 2x average equity, EAS statements, banks/insurers/finance cos excluded | TP | Law 151/2026 art. 1 (art. 52 item 1) | matches |
| 21 | Law 151 art. 6 repeals art. 7 (not art. 5) of Law 30/2023 | TP | Law 151 art. 6 and erratum | matches |
| 22 | Infrastructure 4x: PM decision, unrelated lenders, 25% | TP | Law 151 art. 1 (art. 52 item 1 second para.) | matches |
| 23 | Infrastructure 4x: end of benefit | TP | Erratum, Gazette 32 bis p. 8 | fixed (erratum: ends with the term of the loans for carrying out the main works) |
| 24 | Effective 29 Jul 2026 (published 28 Jul, next day) | TP, XB | Law 151 art. 7 | matches |
| 25 | Interest rate cap: twice CBE credit and discount rate at start of calendar year in which the period ends | TP | Law 91 art. 24 item 4, Gazette p. 18 | matches |
| 26 | CBE rate 20.50% on 1 Jan 2026, so 41% cap | TP | Circular 1/2026 | matches |
| 27 | Art. 24 item 5 interest to non-taxable/exempt individuals | TP | Law 91 Gazette p. 18 | matches |
| 28 | Art. 52 items 3 to 5 not deductible | TP | Law 91 Gazette p. 33 | matches |
| 29 | ER 91 arts. 38 to 40 (decree 221/2018), five methods, choice rule, CUP priority gone, Guidelines as ETA reference | TP | Guidelines pp. 12 to 13 and note 4 | matches |
| 30 | Financial transactions include share transfers, loans, guarantees | TP | Guidelines p. 12 note 5 | matches |
| 31 | Most appropriate method (ch. 4 p. 42), CUP for commodities (p. 44), RPM for distribution (p. 47) | TP | Guidelines | matches |
| 32 | Comparables Egypt, then MEA, then global; strategy disclosed; ETA database | TP | Guidelines s. 5.7.3.1 pp. 64 to 65, note 17 | matches |
| 33 | Statistical tools narrow range | TP | Guidelines p. 84 | matches |
| 34 | Master/local file content, entity-by-entity, three years ideal | TP | Guidelines pp. 61 to 66 | matches |
| 35 | Intangibles, services, CCAs to separate guidance | TP | Guidelines p. 11 | matches |
| 36 | Filing lacking guide sections not counted | TP | ER 206 art. 19 | matches |
| 37 | ETA sets pricing if not filed; burden on taxpayer | TP | Law 206 art. 12 third para.; ER 206 art. 14; Law 206 art. 40 | matches |
| 38 | Return before 1 May or within four months | TP, XB | Law 206 art. 31(c), Gazette p. 18 | matches |
| 39 | Local file two months after return | TP | Law 206 art. 13(b) | matches |
| 40 | Master file on parent's date; Egypt parent or no requirement: local file date | TP | Law 206 art. 13(a); ER 206 art. 15 | matches |
| 41 | CbC within one year; first for FY ending 31 Dec 2018 | TP | Law 206 art. 13(c); Guidelines s. 5.9 p. 67 | matches |
| 42 | Records five years | TP | Law 206 art. 38, Gazette p. 24 | fixed (noted Law 150/2026 replaced only the first para.) |
| 43 | Information within 15 days, extension | TP | Law 206 art. 41, Gazette p. 25 | fixed (extension is by the ETA head, for the same period) |
| 44 | Form 3 سداد | TP | ER 206 art. 17 | matches |
| 45 | APA: types, pre-filing six months, form 1, form 2 within two months, 3 to 6 months, renewable, revision/cancellation, PEs eligible | TP | Guidelines pp. 91 to 98 | matches |
| 46 | Payment of TP charge does not bar other fines | TP | ER 206 art. 20 | matches |
| 47 | Breach of arts. 12/13 as an offence | TP | Law 206 art. 69(d), Gazette p. 40 | fixed (added: fine EGP 3,000 to 50,000, tripled on repeat) |
| 48 | Delay charge CBE rate + 2% | TP, XB | Law 91 art. 110 as quoted in circular 1/2026 | matches |
| 49 | 100% cap on delay charge | TP, XB | Law 206 art. 45 bis (Law 7/2025) | matches |
| 50 | Assessment window five years, interruption | TP | Law 206 art. 44 as replaced by Law 211/2020 | matches |
| 51 | Offences arts. 69 to 72, settlement arts. 75, 75 bis | TP, XB | Law 206 Gazette pp. 40 to 41; Law 7/2025 | matches |
| 52 | Information exchange | TP, XB | Law 206 art. 78, Gazette p. 42 | matches |
| 53 | Inclusive Framework membership | TP | Guidelines p. 11 | fixed (moved out of "Not yet confirmed" into the body; restores old content) |
| 54 | APA document language | TP | Guidelines p. 97 | fixed (added; restores part of old language point) |
| 55 | Individual residence: home, >183 days in 12 months, Egyptian paid from Egyptian treasury | XB | Law 91 art. 2, Gazette p. 7 | matches |
| 56 | Legal person residence: Egyptian law, main or actual management, >50% state | XB | Law 91 art. 2 | matches |
| 57 | Art. 47 scope, art. 48 item 4 | XB | Law 91 Gazette p. 30 | matches |
| 58 | PE list and 90 days in 12 months | XB | Law 30/2023 art. 1 (art. 4), Gazette pp. 4 to 5 | matches |
| 59 | Deemed PE: resources, services, insurance, split contracts | XB | Law 30/2023 art. 4 second para. (a), (b), (c), (f) | matches |
| 60 | Dependent agent | XB | Law 30/2023 art. 4 (d), (e) | fixed (purchase-only exception and the three contract types restored) |
| 61 | Art. 4 bis exclusions, foreign subsidiary | XB | Law 30/2023 art. 2 (art. 4 bis) | matches |
| 62 | Anti-fragmentation | XB | Art. 4 bis | fixed (writer dropped the "not preparatory or auxiliary" limb and the same-or-other-place condition) |
| 63 | Closely related >50% | XB | Art. 4 bis last para. | matches |
| 64 | Source income items (a) to (k) | XB | Law 91 art. 3, Gazette p. 8; Law 30/2023 (b), (j) | matches |
| 65 | Art. 56 20%, gross, items 1 to 4 and carve-outs | XB | Law 91 Gazette p. 34 | matches |
| 66 | Art. 56 payer list | XB | Same | fixed ("resident sole proprietor": the text says owners of sole proprietorships, with no residence qualifier) |
| 67 | Government foreign loans exempt | XB | Law 30/2023 art. 56 third para. | matches |
| 68 | 3-year loan exemption repealed, grandfathered where interest paid before 16 Jun 2023 | XB | Law 30/2023 arts. 6, 12 | matches |
| 69 | Infrastructure interest exemption conditions | XB | Law 151 art. 2 (art. 56 fourth para.) | matches |
| 70 | Infrastructure interest exemption end | XB | Erratum | fixed |
| 71 | Dividend tax 10%/5%, bonus shares, civil companies, resident-to-resident exclusion | XB | Law 151 art. 1 (art. 56 bis) | matches |
| 72 | PE deemed distribution 60 days | XB | Same | matches |
| 73 | Dividend tax remittance five working days | XB | Same | matches |
| 74 | Participation exemption 25%, two years, no add-back | XB | Law 151 art. 1 (art. 50 item 10); Law 30/2023 (add-back) | matches |
| 75 | Listed gains exempt, losses not deductible, delisting exception | XB | Law 151 arts. 1, 2 (arts. 50 item 7, 31 item 7) | matches |
| 76 | Unlisted gains taxable, non-resident pays within 60 days, T-bills outside; gain computation | XB | Law 151 art. 1 (arts. 46 bis 3, 4) | matches |
| 77 | Forgiveness of unpaid listed gains tax | XB | Law 151 art. 5 | fixed (period runs to the start date, 29 Jul 2026, not 28 Jul) |
| 78 | T-bill yields 20%, remittance timing | XB | Law 30/2023 (art. 58 second para.) | fixed (the payer remits the day after deduction; it does not "withhold the next day") |
| 79 | Refund interest CBE + 2%, 45 days, 22.50% | XB | Law 206 art. 53, Gazette p. 30; circular 1/2026 | matches |
| 80 | Foreign tax credit, cap, foreign losses | XB | Law 91 art. 54, Gazette p. 33 | matches |
| 81 | Departing resident 60 days before, sudden departure | XB | Law 206 art. 31(d), Gazette p. 19 | matches |
| 82 | Settlement of art. 135 offence 12.5% plus amounts and delay charge | XB | Law 7/2025 (art. 75 bis 1) | matches |
| 83 | Refund service 5/1: form 1, simplified registration, documents, 45 days, 15 days (10 + 5), no fee | XB | Services Guide pp. 97 to 100 | matches |
| 84 | Art. 56 certificate form 8, form 11, 7 days | XB | Services Guide pp. 100 to 102 | matches |
| 85 | Residence certificate form 9, 7 days | XB | Services Guide pp. 102 to 104 | matches |
| 86 | Advance inquiry form 7 | XB | Services Guide pp. 104 to 108 | fixed (30 and 60 day answer times added; page range corrected to 97 to 108) |
| 87 | 64 treaty entries (63 states plus CAEU) | XB | ETA treaties page | matches |

## Totals

- Items checked: 87
- Matched: 70
- Fixed: 17 (items 7, 8, 23, 42, 43, 47, 53, 54, 60, 62, 66, 70, 77, 78, 86, plus the Sources table additions for the erratum (both files) and Law 150/2026 (TP))
- Moved to "Not yet confirmed": 0 (nothing in the bodies failed to confirm; the writer's existing "Not yet confirmed" lines stand, less the Inclusive Framework point, now confirmed)

Lost content restored: 3 (TP: the exemption covers only the master and local files, so the arm's length rule and disclosure still apply below the threshold; Egypt's Inclusive Framework membership and OECD alignment; APA documentation language). Other old-version items (revised return and local file deadline, CbC notification deadline, surrogate CbC filing, documentation language, safe harbours, APA roll-back and fees, secret comparables, 3 to 5 year APA term) are on the writer's "Not yet confirmed" line or replaced by sourced text; the "first Middle East country", EGP 1m practical benchmark and Big-4 references had no official source and were rightly dropped.

## Example recomputations (by hand)

**TP Case 1.** 1% x 10,000,000 = 100,000. 3% x 50,000,000 = 1,500,000. Sum 1,600,000; cap 3% x 50,000,000 = 1,500,000; charge = min = 1,500,000. Matches.

**TP Case 2.** Interest A = 45,000,000 x 10% = 4,500,000. 2026 limit 3 x 10,000,000 = 30,000,000; deductible 4,500,000 x 30/45 = 3,000,000; disallowed 1,500,000. B: 30,000,000 x 10% = 3,000,000; limit 75,000,000, so all 3,000,000 deductible. 2028 at 2:1: 4,500,000 x 20/45 = 2,000,000. 10% is under the 41% rate cap. Matches. It is a decision case (loan against equity).

**XB Case 1.** 1,000,000 + 500,000 + 300,000 = 1,800,000; 20% = 360,000; net 1,440,000. The 2025 five-year loan is outside both the grandfathered 3-year exemption (interest not paid before 16 Jun 2023) and the infrastructure exemption. Matches.

**XB Case 2.** Branch: 10% x 10,000,000 = 1,000,000. Subsidiary: 10% x 4,000,000 = 400,000. Deferred 600,000. Matches. It is a decision case (branch against subsidiary).

## Contradictions with eg-corporate-tax and eg-withholding-tax (not edited)

- No figure contradictions: thin cap (2x permanent, 3:1 for 2026, 4x infrastructure), art. 56 at 20%, dividends 10%/5%, PE deemed distribution at 60 days, delay charge CBE + 2% (22.50% in 2026) with the 100% cap all agree.
- Both sibling files carry the uncorrected Law 151 wording that the infrastructure benefit "ends with the loans and the main works" (eg-corporate-tax thin cap infrastructure row; eg-withholding-tax infrastructure loans row). The Gazette erratum of 8 Aug 2026 corrects art. 52 item 1 and art. 56 fourth para.; the other reviewer should align them and cite the erratum.
- Neither sibling cites Law 150/2026 (art. 38 first para. of Law 206 now refers to Law 6/2025 and drops the EGP 500,000 bookkeeping threshold); relevant to eg-corporate-tax if it states the bookkeeping duty.

## Still open

The writer's "Not yet confirmed" items stand: the 2026 documentation threshold after any MoF decision (laws page lists none), the Guidelines' decree number, Instructions 78/2023, CbC notification deadline, the 2:1 versus 3:1 question for a period straddling 29 Jul 2026, whether art. 56 first para. or art. 54 were amended after 2005, the non-resident rate on unlisted share gains, and whether the branch deemed distribution is measured after corporate tax.
