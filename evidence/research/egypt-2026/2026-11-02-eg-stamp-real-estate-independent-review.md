# Independent review: eg-stamp-duty and eg-real-estate-tax (tax year 2026)

Reviewer: independent AI review agent (Claude), no shared context with the writer. Review date: 2026-11-02. Rule: `docs/skill-template.md` line 12 (second reader) and line 5 (no lost rule; both files shrank more than 25%, so old was compared against new item by item).

Files reviewed (uncommitted, branch `pack/eg`): `skills/egypt/eg-stamp-duty.md` (v0.2; old 522 lines, new 193 after review) and `skills/egypt/eg-real-estate-tax.md` (v0.2; old 329 lines, new 211 after review). Old versions: `upstream/main`. The writer's notes (`2026-11-02-eg-stamp-real-estate-source-notes.md`) were used only to find pages.

## Sources re-read by the reviewer

Scanned files were rendered with `pdftoppm -r 110` and read as page images; text-layer files were read with `pdftotext`. Some PDFs were reused from the writer's download folder; the reviewer re-rendered and re-read every page cited, and re-downloaded Law 30/2023 to confirm the cached copy is byte-identical to the URL. Web pages were fetched fresh on 2026-11-02. No CAPTCHA or bot check was met. The RTA "Building laws" page again returned "Request Rejected" (site firewall) on 2026-11-02; it was not retried by other means.

| Source | URL | What the reviewer read |
|---|---|---|
| Law 153/2026, Gazette 30 bis (a), 28 Jul 2026 | https://eta.gov.eg/sites/default/files/2026-08/law.no_.153.of_.2026.pdf | Whole text (arts. 1 to 3) |
| Law 199/2020, Gazette 39 bis (z), 30 Sep 2020 | https://eta.gov.eg/sites/default/files/2024-03/law_no.199-2020.pdf | Arts. 1, 4, 5, 8, 9 |
| Law 76/2017, Gazette 24 bis (b), 19 Jun 2017 | https://eta.gov.eg/sites/default/files/2024-03/law_no.76-2017.pdf | PDF pp. 2 to 4 (art. 3 adding arts. 83 bis and 83 bis (1); arts. 4, 5) |
| Law 3/2022, Gazette 3 bis (h), 26 Jan 2022 | https://eta.gov.eg/sites/default/files/2024-03/vat-law_no.3-2022.pdf | PDF p. 11 (arts. 4 to 7) |
| Law 30/2023 | https://eta.gov.eg/sites/default/files/2024-03/law_no.30-2023.pdf | Title, art. list; text searched for stamp tax (none); arts. 3 to 10 |
| Investment Law 72/2017 | https://eta.gov.eg/sites/default/files/2024-10/law-72-2017.pdf | PDF p. 11 (arts. 9, 10) |
| Law 206/2020 | https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf | PDF p. 1 (issuing arts. 1 to 3) |
| Stamp Tax Law 111/1980 | https://eta.gov.eg/sites/default/files/2026-05/law.no_.111.of_.1981.pdf | PDF p. 1 (issuing arts. 1 to 4, Gazette 22 bis (a), 31 May 1980) |
| ETA circular 1/2026 | https://eta.gov.eg/sites/default/files/2026-03/Dawry.no_.1.of_.2026.pdf | Whole page |
| ETA Services Guide, 2nd ed. | https://eta.gov.eg/sites/default/files/2025-08/guide.of_.the_.egyptian.tax_.authority.services.second%20edition.pdf | Service 1/2 (p. 36, 37), service 2/11 (p. 164, 165), Law 6/2025 service (p. 246) |
| ETA news 13 Mar 2022 (advertising) | https://www.eta.gov.eg/ar/news/afa-alalanat-mn-drybt-aldmght-albalght-20-alty-kant-tkhd-lha-sabqana-wakhdaha-llsr-alam-ldrybt | Whole article |
| ETA news 26 Jul 2026 (Laws 151 to 153) | https://eta.gov.eg/ar/news/tdylat-jwhryt-ly-qanwn-aldrybt-ly-aldkhl-wqanwn-aldrybt-ly-aldmght-llqda-ly-alazdwaj-aldryby | Whole article |
| ETA stamp forms page and the four templates | https://www.eta.gov.eg/ar/content/nmadhj-aldmght | Link list; column headers of forms 9, 10, 21 (kh) tables 3 and 4 |
| ETA workspace portal | https://workspace.eta.gov.eg/workspace/dashboard | HTTP 200 and linked from ETA pages; not read |
| Law 196/2008, ETA text copy | https://eta.gov.eg/sites/default/files/2024-10/law-196-2008.pdf | PDF pp. 1 to 12 (issuing arts. 1 to 9, law arts. 1 to 35) |
| Law 196/2008, Gazette scan | https://eta.gov.eg/sites/default/files/2026-03/law.no_.196.of_.2008.pdf | PDF p. 1 (Gazette 25 bis (c), 23 Jun 2008) |
| Law 103/2012 | https://eta.gov.eg/sites/default/files/2024-10/law-103-2012.pdf | PDF pp. 1 to 6 (arts. 1 to 6, table 1) |
| Law 151/2026 | https://eta.gov.eg/sites/default/files/2026-08/law.no_.151.of_.2026.pdf | Art. 1 list, art. 43/42 text, art. 46 bis 3, arts. 6, 7 |
| Correction notice, Gazette 32 bis, 8 Aug 2026 | https://eta.gov.eg/sites/default/files/2026-08/law.no_.149.150.151.of_.2026.retractation.pdf | PDF p. 2 |
| Income Tax Law 91/2005 | https://eta.gov.eg/sites/default/files/2024-03/law_no.91-2005.pdf | Gazette pp. 17, 18 (arts. 21 to 24) |
| RTA notice 10 Mar 2026 | https://www.rta.gov.eg/news/amendments-and-facilities-real-estate-taxes | Whole notice |
| RTA notice 11 Oct 2026 | https://www.rta.gov.eg/news/extending-period-submitting-real-estate-tax-declarations-until-end-december-2026 | Whole notice |
| RTA home page | https://www.rta.gov.eg/ | Links (declaration service, English form for foreigners) |
| MoF explainer, 6 Oct 2026 | https://mof.gov.eg/ar/media/learn-more/news-2 | Whole Q&A (10 questions) |

## Items checked

Result key: M = matches; F = fixed; N = moved to or kept on "Not yet confirmed"; R = restored from the old version. SD = eg-stamp-duty, RE = eg-real-estate-tax.

| # | Item | File | Source location | Result |
|---|---|---|---|---|
| 1 | Law 153/2026: tax on total sales of EGX-listed securities, listed fund units out, no costs deducted | SD | Law 153 art. 1 (art. 83 bis para. 1) | M |
| 2 | 0.5 per thousand buyer and 0.5 per thousand seller, resident or non-resident | SD | Same | M |
| 3 | 0.25 per thousand each side, same-day purchase and sale | SD | Same | M |
| 4 | Approved market makers under Law 95/1992 out | SD | Same, para. 3 | M |
| 5 | Settlement body withholds, remits within five days of start of next month, on form, jointly liable for tax and delay charge | SD | Same, last para. | M |
| 6 | Law 199/2020 art. 5 repealed | SD | Law 153 art. 2 | M |
| 7 | In force day after publication: 29 Jul 2026 (published 28 Jul 2026) | SD | Law 153 art. 3; Gazette 30 bis (a) | M |
| 8 | Old art. 83 bis: all securities, Egyptian or foreign, listed or not; 1.25 per thousand non-resident each side; 0.5 per thousand resident each side; same-day out | SD | Law 199 art. 1 | M |
| 9 | Resident exemption starts day after art. 4 deferral ends; deferral to end 2021 | SD | Law 199 arts. 4, 5 | F: start date on the text (1 Jan 2022) and "listed and unlisted alike" added; extension question kept N |
| 10 | 33% rule, 3 per thousand each side, two-year aggregation, tax already paid deducted, not deductible for income tax | SD | Law 76 art. 3 (art. 83 bis (1)) | F: item 2 needs a takeover "by another resident company in exchange for shares in the acquiring company"; aggregation covers purchases or sales, buyer pays on the acquisition line, seller on the exit line |
| 11 | Misr for Clearing or other settlement body withholds and remits per Minister's decision, jointly liable | SD | Same | M |
| 12 | Law 76 art. 3 added art. 83 bis (1); in force day after publication | SD | Law 76 arts. 3, 5 | M |
| 13 | Advertising: VAT 14%, Stamp Tax Law arts. 60 and 64 repealed, from 27 Jan 2022 | SD | Law 3/2022 arts. 5, 7 | M |
| 14 | Former advertising stamp rate 20% | SD | ETA news 13 Mar 2022 | R: rate now stated in the row |
| 15 | Public, awareness and election advertisements now VAT-exempt | SD | ETA news 13 Mar 2022 | R: old stamp exemption restored as its current VAT form |
| 16 | Investment Law: stamp, notarisation and registration exemption for incorporation, credit facility and mortgage contracts, five years from commercial register; land registration contracts; free zones out | SD | Law 72/2017 arts. 9, 10 | M |
| 17 | Law 206 applies to stamp tax where no special rule | SD | Law 206 issuing art. 1 | M |
| 18 | Unlisted securities out of stamp tax, into income tax; market makers exempt | SD | ETA news 26 Jul 2026; Law 153 art. 1 | M |
| 19 | Scope list of stamp tax | SD | Services Guide service 2/11 | F: cited as "service 11/2"; the guide numbers it 2/11 (service 2 of activity 11) |
| 20 | Stamp returns uploaded to the e-system with other returns; payment claim | SD | Services Guide service 1/2 | F: cited as "service 2/1", which in the guide is simplified registration; correct number 1/2 |
| 21 | Free written research service, no fee | SD | Services Guide service 2/11 | M |
| 22 | Forms 9, 10, 21 (kh) tables 3 and 4 | SD | ETA forms page and templates | F: the file left their content unconfirmed; table 3 is pay (art. 79 tax), table 4 sums paid out (art. 80 ordinary and additional tax), forms 9 and 10 are 2021 advertising templates; filing step 2 corrected; removed from Not yet confirmed |
| 23 | Pay stamp tax is art. 79 | SD | Form 21 (kh) table 3 header "ORD_TAX_M79" | M |
| 24 | Law 6/2025 enterprises exempt from stamp tax (linked to `eg-sme-tax`) | SD | Services Guide p. 246 | M |
| 25 | Delay charge: Central Bank rate on 1 January plus 2%, part months and pounds dropped; 20.50% on 1 Jan 2026 | SD, RE | Circular 1/2026; Law 206 art. 53 as quoted | M |
| 26 | Portal workspace.eta.gov.eg | SD | Linked from ETA pages; HTTP 200 | M (link only) |
| 27 | Law 30/2023 contains no stamp tax provision (old version tied insurance rates to it) | SD | Law 30/2023 title and text | M |
| 28 | Stamp Tax Law 111/1980, Gazette 22 bis (a), 31 May 1980, issuing arts. 1 to 4 | SD | PDF p. 1 | M |
| 29 | Non-resident gains on unlisted shares, 60-day payment | SD | Law 151 art. 46 bis 3 | M |
| 30 | RTA collects; taxpayer is owner or holder of right of use or exploitation, unregistered deed included; representatives | RE | Law 196 art. 1; art. 2 as replaced by Law 103 | M |
| 31 | What is taxed: any material or use, permanent or not, land or water, let or not | RE | Law 196 art. 8 | F: art. 8 lists three states (complete and occupied, complete and unoccupied, occupied though incomplete); "occupied or empty, used or not" replaced |
| 32 | Deemed built property | RE | Art. 9 | M |
| 33 | Built property on agricultural land; land tax lifted | RE | Art. 10 | M |
| 34 | Outside the tax: state public-purpose property, private state property from month after disposal, worship, expropriated | RE | Art. 11 | M |
| 35 | 10% after 30% residential, 32% non-residential, all expenses incl. maintenance | RE | Art. 12 as replaced by Law 103 | M |
| 36 | EGP 24,000, one unit per owner; deduction method (table 1: 2,000,000 market, 1,200 base, tax 120) | RE | Law 103 art. 3 (art. 18 (d)); table 1 | M |
| 37 | Original 2008 residential exemption EGP 6,000 | RE | Law 196 art. 18 (d) original | R: old version had it (misattributed to Law 117/2014) |
| 38 | Reassessment cap 30% residential, 45% non-residential over previous tax | RE | Art. 5 as replaced by Law 103 | M |
| 39 | Committees by building standard, location, services; five-year assessment, reassessment work 1 to 3 years before | RE | Arts. 4, 13 | M |
| 40 | Exempt list; Law 103 repealed other-law exemptions except issuing art. 4 and deleted art. 18 (c) | RE | Art. 18; Law 103 arts. 3, 5 | M |
| 41 | End of exemption: notify within 60 days, tax from 1 Jan next year | RE | Arts. 18, 22 | M |
| 42 | Relief grounds | RE | Art. 19; RTA notice | M |
| 43 | Relief start date | RE | Art. 20; RTA notice | F: file said "from the month after the request"; art. 20 says from the first day of the month the request is filed, and the RTA says the 2026 amendment counts from the date of the event |
| 44 | Relief: last instalment paid, EGP 50 deposit | RE | Art. 20 | M (refund on acceptance added) |
| 45 | 2026 write-off committees for uncollectable debts | RE | RTA notice | F: added (was omitted) |
| 46 | Rent taxed on actual rent less 50%; real estate tax credited up to that tax; 50% rule not for business assets | RE | Law 196 issuing art. 3 (Law 91 arts. 39, 45, 46) | M |
| 47 | Annual tax deductible for a business as a tax other than income tax | RE | Law 91 art. 23 item 3 (2005 text) | F: the file held this on Not yet confirmed; the 2005 text settles it against the old version's "not deductible"; later amendments to art. 23: N |
| 48 | Five-yearly and annual declarations, end December | RE | Art. 14 (a), (b) | M |
| 49 | Assessment published and notified; appeal 60 days from notification, EGP 50 deposit, committee 30 days, final | RE | Arts. 15 to 17; Law 103 art. 4 | M |
| 50 | Due 1 January; two equal instalments end June, end December, or in full with the first | RE | Arts. 3, 23; MoF Q9 | M |
| 51 | Payment place | RE | Art. 6; MoF Q9 | R: RTA directorates and offices, and electronic payment, restored from the old version's payment-location row; banks and post offices: N |
| 52 | Tenants jointly liable up to rent after registered letter | RE | Art. 24 | M |
| 53 | Delay charge from 1 January after the year due | RE | Art. 27 | F: rate is the 1 January preceding the date the charge starts, not "before the due date"; added that an appeal does not stop it |
| 54 | Fines EGP 200 to 2,000, doubled on repeat within three years | RE | Art. 30 | M |
| 55 | Evasion fines EGP 1,000 to 5,000 plus compensation equal to tax | RE | Art. 31 | M |
| 56 | Minister's written request; settlement | RE | Arts. 32, 33 | M |
| 57 | EGP 100,000 private residence exemption, spouse and minor children, about EGP 8 million per unit | RE | RTA notice; MoF Q2, Q7 | M (law text not found: N kept) |
| 58 | EGP 1,200 non-residential deduction | RE | MoF Q7 | M (origin in law: N kept) |
| 59 | Capital value 60% of market, rental value 3% of capital value | RE | MoF Q7; Law 103 table 1 | M |
| 60 | Filing discounts 25% and 10%, continuing; extra 5% for advance payment; 30% and 15% total; deducted from 2027 tax, refundable if exempt | RE | MoF Q6; RTA notice | M |
| 61 | Delay charge cap at principal; waiver for payers before law or within six months; extended to 2 Apr 2027 | RE | RTA notices 10 Mar and 11 Oct 2026 | M |
| 62 | 70% dispute settlement with delay charge waived; extended to 2 Apr 2027 | RE | RTA notices; MoF Q10 | F: original deadline 2 Oct 2026 and the second route (dispute ending where reduction over 30% claimed, to 31 Dec 2026) added |
| 63 | Single declaration to any office; gradual e-declaration; unregistered units taxed from filing date | RE | RTA notice 10 Mar 2026; MoF Q4, Q6 | M |
| 64 | RTA appeal right removed; online appeals | RE | RTA notice | M |
| 65 | Exempt units must still be declared, tenants do not file | RE | MoF Q3 | M |
| 66 | 2026 declarations to end December 2026 | RE | RTA notice 11 Oct 2026; MoF Q5 | M |
| 67 | Declaration service URL; English form for foreigners | RE | RTA home page | M (source row added) |
| 68 | Disposal tax 2.5% gross, no reduction, built property or building land outside villages, any number of disposals; heirs; trading only if ETA proves, then credited; contract value, ETA burden; in-kind contribution kept five years out; 60 days; art. 110 delay charge; disposal types; forced sales, expropriation, gifts to government out | RE | Law 151 art. 1 (art. 42, printed 43) | M; F: "or for improvement" added to the expropriation exclusion |
| 69 | Art. 42 not 43; "built" not "in kind" | RE | Correction notice, Gazette 32 bis, 8 Aug 2026 | M |
| 70 | Law 151 in force 29 Jul 2026 | RE | Law 151 art. 7 | M; pre-29 Jul text of art. 42: N added |
| 71 | Worked example arithmetic, both files | SD, RE | See below | M |

Totals: 71 items checked; 55 matched; 12 fixed (items 9, 10, 19, 20, 22, 31, 43, 45, 47, 53, 62, 68; related filing-step, source-row and Not-yet-confirmed edits are counted with them); 4 restored (items 14, 15, 37, 51). Items that match but keep a Not-yet-confirmed note are counted as matched. Newly added to "Not yet confirmed": 6 (old amending stamp laws list and e-invoice stamp claim; payment at banks and post offices; exemption-claim proof documents; resale-property CIT treatment; pre-29 Jul 2026 art. 42 text; post-2005 amendments to Law 91 art. 23). Removed from it: 2 (forms content; CIT deductibility of the annual tax, now stated from the law).

Validation after fixes: `python3 scripts/check-examples.py --require` on both files: 4 oa-check blocks, 0 failures, 0 missing. `scripts/skill_checks.py` (a) to (o): all pass on both files. `python3 scripts/validate-guides.py --no-index-check`: validation passed, no warning names either file.

## Content loss (line 5)

Both files shrank more than 25% (stamp 522 to 193 lines; real estate 329 to 211). Every old rule, rate, threshold, deadline, exemption, taxpayer group and edge case was compared against the new file.

Restored, checked against the law or an official page:
1. Stamp: resident securities exemption start date, 1 Jan 2022 on the text (old "suspended since 1 Jan 2022"), corrected to cover listed and unlisted alike.
2. Stamp: advertising stamp rate of 20% before the 2022 repeal.
3. Stamp: public-authority and election advertisement exemption, now in its VAT form.
4. Real estate: original 2008 residential exemption of EGP 6,000 (old version attributed the 6,000 to 24,000 rise to Law 117/2014; it was Law 103/2012).
5. Real estate: buildings under construction (old "not taxed until fully built") restored in its statutory form: an incomplete building is taxed once occupied.
6. Real estate: payment place (RTA directorates and offices, art. 6; electronic payment).

Restored as "Not yet confirmed" items (could not be sourced): stamp amending laws 140/2006, 53/2014, 110/2018, 147/2019, 174/2019 and the claim that e-invoices carry a nominal stamp; real estate payment at banks and post offices; proof documents for an exemption claim; different CIT treatment of property held for resale.

Lost content restored: 10 (6 into the body from the law, 4 as Not yet confirmed items)

### Removed and why:

- Stamp: "Conservative defaults" table and "Red flag thresholds" (EGP 100,000, 25,000 a quarter, 500,000, GAFI cap trigger): workflow guidance with no official source.
- Stamp: Excel working paper layout, tab structure and formulas: boilerplate.
- Stamp: e-invoicing system description (mandatory since July 2023, UUIDs), e-signature Law 15/2004, ITIDA, Egypt Trust, digital.gov.eg, notarisation digitisation: not stamp tax rules and no official source read; the open question on e-stamp channels stays on Not yet confirmed.
- Stamp: legislative timeline rows for the 2021 insurance draft (not enacted) and Law 157/2025 (VAT): not stamp law or no source.
- Stamp: old 0.05% resident rate on unlisted shares and "listed only" suspension: contrary to Law 199/2020 art. 5 (residents not subject on any security); unlisted shares are now outside stamp tax entirely (Law 153/2026).
- Stamp: old same-day exemption as current law: replaced by the Law 153/2026 0.25 per thousand rate; the old exemption is kept for 1 Jan to 28 Jul 2026.
- Stamp: insurance rates attributed to Law 30/2023, bank, document, lease, court and certificate rates, GAFI fees, exempt document list, T-bills, insurer and bank remittance, understamping penalty: not dropped, all carried on Not yet confirmed (no official schedule text found).
- Stamp: refusal catalogue (complex securities, free zone, Islamic finance, double stamp, historical transitions): referral guidance, not rules; the substantive points (free zone, Islamic finance, transitions, treaty relief) are covered in the body or on Not yet confirmed.
- Stamp: duplicate quick-reference tables and the "Tier 1 rules (compressed)" section: duplicates of the rate tables.
- Real estate: self-check list, "What this file is", YMYL banner, secondary-source verification notes (PwC, Andersen): boilerplate or secondary sources.
- Real estate: worked examples on the pre-2026 EGP 24,000 regime and the below-threshold example: examples, not rules; the 24,000 and 6,000 figures remain in the rates table.
- Real estate: "20% non-residential rate in secondary sources" note: no official source; the 10% rate for all property is in the table.
- Real estate: transfer tax "due on registration", "administered by RETA under Law 196 art. 40", "family transactions and inheritance exempt under art. 41": contrary to Law 91 art. 42 as replaced by Law 151/2026 (ETA, 60 days, ascendants, spouses and descendants out); noted on Not yet confirmed.
- Real estate: "wealth tax on rental income 10% to 27.5% under Law 91 art. 47" and CIT add-back "Form 10": contrary to Law 91 arts. 39, 45 and art. 23 item 3; noted on Not yet confirmed.
- Real estate: property registration Law 114/1946 and transfer pricing scope lines: out-of-scope pointers, no rule.

## Example recomputations (by hand)

SD case 1: 2,000,000 x 0.0005 = 1,000 (seller); 1,000 (buyer); total 2,000; old non-resident seller 2,000,000 x 0.00125 = 2,500. Matches.

SD case 2: same day 1,000,000 x 0.00025 = 250; 1,050,000 x 0.00025 = 262.50; total 512.50. Next day 500 + 525 = 1,025. Saving 512.50. Matches; the decision is worked both ways.

RE case 1: 180,000 x 0.70 = 126,000; less 100,000 = 26,000; x 10% = 2,600; x 0.75 = 1,950. Matches.

RE case 2: 200,000 x 0.68 = 136,000; less 1,200 = 134,800; x 10% = 13,480; on time x 0.90 = 12,132; on time and prepaid x 0.85 = 11,458; saving 13,480 - 11,458 = 2,022. Matches (MoF Q6: 10% plus 5% for non-residential).

Market-value check: 100,000 / 0.70 / 0.03 / 0.60 = 7,936,508, about EGP 7.94 million. Disposal: 3,000,000 x 2.5% = 75,000. Matches.

## Still open

The 2026 law amending Law 196 (number, Gazette date, text) was not found on an official host, so every 2026 real estate figure rests on RTA and MoF pages; the current stamp schedule outside securities (Law 143/2006 and later not on eta.gov.eg); whether the 33% rule still reaches unlisted shares; whether the Law 199/2020 art. 4 deferral was extended; the general stamp return's frequency and due date; the pre-29 Jul 2026 text of Law 91 art. 42.
