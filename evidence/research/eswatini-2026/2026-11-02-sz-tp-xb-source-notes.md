# Eswatini TP and XB: source notes

Working notes for the two missing SZ domains (TP, XB): `skills/eswatini/sz-transfer-pricing.md` and `skills/eswatini/sz-cross-border.md`. All sources read on 2026-11-02. Tax year 2026 = year of assessment 1 July 2025 to 30 June 2026.

## How each source was read

| Source | URL | How read |
|---|---|---|
| Income Tax (Amendment) Act 2023 (Act 20 of 2023), 38 pages, scanned (no text layer) | https://www.ers.org.sz/documents/IncomeTaxAmendmentAct2023.pdf | curl; pages rendered with `pdftoppm -r 75` and read by eye: pp. 1 to 30 (pp. 31 to 38, Sixth and Seventh Schedules, not read) |
| Income Tax Order 1975, ERS consolidated copy to the 2013 amendments, 170 pages | https://www.ers.org.sz/documents/IncomeTaxOrder1975.pdf | curl; `pdftotext -layout` |
| ERS, Income Tax Order changes 2024 (10 pages) | https://ers.org.sz/whatsnew-file/1726738466004-Income_Tax_Order_Changes__2024.pdf | curl; `pdftotext` (found via the ERS "what's new" feed, https://www.ers.org.sz/api/whateNew) |
| ERS, public notice, returns for tax year end 2026 (1 page) | https://ers.org.sz/whatsnew-file/1791462650754-1784270658474_Notice_for_Filing_Income_tax_Returns_Public_Notice_Final_Aligned.pdf | curl; `pdftotext` (two-column layout, read with care) |
| ERS, FAQ guide, income tax returns 2026 | https://ers.org.sz/whatsnew-file/1790327377834-FAQ_Guide___Income_Tax_Returns_2026.pdf | curl; `pdftotext` |
| ERS, Withholding Taxes page | https://www.ers.org.sz/IncomeTax/Withholding | curl; HTML stripped |
| ERS, Rates and Thresholds page | https://www.ers.org.sz/IncomeTax/RatesandThres | curl; HTML stripped |
| ERS, Tax Legislations page and Practice Notes and Guidelines page | https://www.ers.org.sz/LegalandPolicy/TaxLegislation and https://www.ers.org.sz/LegalandPolicy/Notes_Guidelines | curl; links listed (no TP regulations, no practice notes listed) |
| Eswatini and South Africa DTA (2004) with Protocol | https://www.ers.org.sz/documents/SouthAfrica.pdf | curl; `pdftotext` |
| 2026-27 Budget Speech (ERS copy) | https://ers.org.sz/whatsnew-file/1772201986460-2026_27_FY_Budget_Speech_2026.pdf | curl; `pdftotext`, searched for tax measures; paras 159 to 167 read |
| EswatiniLII search API | https://eswatinilii.org/search/api/documents/ | curl; searched "transfer pricing", "Tax Administration Act", "Income Tax (Amendment) Act": no TP regulations, no Tax Administration Act, no 2023 amendment found |

## Figures and rules, with section and source

### Commencement and status
- Act 20 of 2023, assented 14 July 2023; s1(2): in force on a date set by the Minister by Gazette notice. Act p. S1.
- ERS 2024 summary: amendments "will come into effect on July 1, 2024". ERS changes 2024, p. 1.
- Budget Speech 2026 para 165 lists the Income Tax (Amendment) Act 2023 among completed reforms; para 166: no tax increases in 2026-27 other than excise duties.
- 2026 returns notice para 5: company rate for 2026 declarations 25%, presumptive 1.75%.

### Transfer pricing (Act 20 of 2023)
- s2 definitions (Act s2, pp. S1 to S2, S7): "arm's length principle" = the price payable between independent enterprises; "associate person" = a person who acts or is likely to act on the directions, requests, suggestions or wishes of the person, including (a) a relative, (b) a partner, a partner's associate or a partnership in which the person is a partner, (c) the trustee of a trust under which the person or an associate benefits or may benefit, (d) a company the person alone or with an associate controls directly or indirectly 50% or more of share capital or voting power, or which is accustomed or may reasonably be expected to act on their directions; "controlled transaction" = any transaction between associated persons; "uncontrolled transaction" = between independent persons; "financial indicator" per method (price, mark up, resale margin, net profit margin, division of operating profit or loss); "tested party" per s65sex; "transfer pricing methods" per s65quin(3).
- s65quat (Act s31, p. S22): (1)(a) person liable to tax in Eswatini dealing with an associated person; (b) persons not liable to tax dealing where the transaction relates to an Eswatini PE of one of them; taxable income consistent with the ALP; (2) adjustment where conditions not at arm's length reduce or postpone tax; (3) per s65quin; (4) no deduction for PE payments to head office (other than reimbursement of actual expenses) as royalties, fees or similar for patents or other rights, commission for specific services or management, or interest (except banking).
- s65quin (pp. S23 to S25): (1) most appropriate method; (2) four selection criteria; (3) five methods: CUP, resale price, cost plus, TNMM, transactional profit split (residual split proviso); (4) one method enough; (5), (6) other method only if none applies and result consistent, burden on the user; (7) ALP also applies to transactions with persons in a jurisdiction the Commissioner determines provides a beneficial tax regime, associated or not, including via an Eswatini PE of a non-resident; (8) beneficial regime = effective tax rate within limits the Minister sets by Gazette notice; (9), (10) commodity quoted-price rule (grains, oil seeds, other products of the land, hydrocarbons, derivatives), shipment date by bill of lading or airway bill; export proviso: agreed price if higher; (11) keep documentation required under s35bis and other documents the Commissioner may require "as per the Transfer Pricing Regulations"; (12) consideration for intangible rights with an associate (other than alienation) capped at a Gazette percentage of EBITDA from the activity; (13) section does not apply to controlled transactions between persons liable to tax in Eswatini where the total value is below a threshold set by Gazette notice, unless the Commissioner directs in writing before the year.
- s65sex (pp. S25 to S26): tested party for cost plus, resale price, TNMM; consistent with functional analysis; least complex functions; foreign tested party needs sufficient information; refers to "regulation 11"; (6) interpret ss65quat to 65sex per OECD TP Guidelines; (7) Order prevails over the Guidelines.
- s65sep (p. S26 to S27): interest cap 30% of tax EBITDA for group companies other than banking or insurance; carry forward three years. Owned by sz-corporate-income-tax, only linked.
- s32I(3) (Act s17, p. S14): cost base of an asset acquired in a non-arm's length transaction = market value at acquisition. s32J(2) (p. S15): disposal to an associate or non-arm's length = greater of cost base and FMV.
- s66bis (Act s32, p. S27): offence by a company deemed committed by the public officer unless without knowledge and with reasonable diligence.
- s68quin (Act s34, pp. S27 to S28): binding general rulings.
- s40(9) (Act s23, p. S19): no additional tax under s40(1)(b), (c) where the incorrect statement is the subject of a private ruling application filed before or at the time of the return.
- s35(9), (10) (Act s20, p. S18): failure to comply with s35(1), (2), (4) or (7): E25 per day, maximum E10,000.
- s33(1) proviso (Act s18, p. S17): extension of time for a return on written application with good cause; s33(16): withholding return with each payment of withheld tax; s33(17): penalty not exceeding E25 per day for a late withholding return.
- ERS 2024 summary, "Transfer Pricing": new definitions (arm's length determination, methods, tested party) for intra-group transactions; interest limited to 30% excluding financial institutions.

### Order 1975 (consolidated to 2013), provisions not changed by the 2023 Act pages read
- s11bis(6): trading stock acquired other than at arm's length taken at current market price in the Commissioner's opinion.
- s35bis(3): records kept in Eswatini, in English or siSwati, for at least five years after the year; (4) longer while an objection or appeal is pending; (5) deduction may be disallowed without records.
- s40(1): additional tax of twice the tax for a default in rendering a return (a), and twice the difference for an omission (b) or incorrect statement (c); (3) remission where no intent; (5) a non-permissible deduction counts as an omission.
- s40bis: 20% for failure to withhold; 10% / 15% / 20% / 25% for remittance under 30 days / 30 to under 90 / 90 to under 180 / 180 days or more late; borne personally.
- s57(2): interest 18% per annum on tax not paid by the due date; Minister may vary by Gazette notice.
- s66(1)(b), (h), (j): fine up to E10,000, imprisonment up to one year, or both (includes failing to produce documents, keep s35bis records, or comply with s59C). s66(2): failing to withhold, remit and account for withholding tax, or to comply with s32E: fine up to E50,000, imprisonment up to five years, or both.
- s68: DTAs have effect as if enacted, for immunity, exemption or relief, only while reciprocal relief has the effect of law in the other country. s68bis practice notes; s68ter private rulings.

### Cross-border
- s7: gross income from a source within or deemed within Swaziland (Eswatini).
- s11(1)(a) to (k): deemed-source list (sale contracts made in Eswatini; services in carrying on a trade in Eswatini; Government employment abroad; pensions for Eswatini service, apportioned; aircraft businesses; use or right of use in Eswatini of IP, films, broadcast material (g), plant, machinery, equipment, vehicles or movable property (gg); know-how for use in Eswatini (h); management charge paid by a resident or person carrying on business in Eswatini (j); interest secured on Eswatini property, paid by a resident borrower, or relating to an Eswatini business (k)).
- s11(7): foreign government stock interest untaxed abroad because of non-residence is deemed Eswatini-source for an ordinarily resident person.
- s11(9A): foreign interest of a person ordinarily resident or carrying on business in Eswatini deemed Eswatini-source unless effectively connected with a foreign branch; credit for foreign tax on it, limited to the Eswatini tax on that interest.
- PE definition (Act s2, pp. S4 to S5): fixed place list (i) to (xiii); (xiv) services through employees or other personnel for more than thirty (30) days in aggregate in any twelve (12) month period beginning or ending in the year of assessment; (b) dependent agent (habitually concludes contracts or plays the principal role; stock of goods); (c) independent agent excluded; (d) not independent if acting exclusively or almost exclusively for closely related persons; (e) control of or by a company not of itself a PE; (f) "closely related" = control or common control.
- "royalty" amended to "payment of any kind received as a consideration", adding industrial, commercial or scientific equipment (Act s2(d), p. S7).
- s21(2): NRST 15%; proviso (12.5% for Botswana, Lesotho, Namibia, SA companies not subsidiaries or branches of outside companies) deleted by Act s10 (p. S11). ERS 2024 summary confirms 15% (increase from 12.5%).
- s22(1): NRST payable on dividends to a non-company person not ordinarily resident or carrying on business; deceased estates; a company with place of effective management outside Eswatini; bearer scrip. s22(2) exemptions. s24 recovery from paying company or agent. s25 apportionment. s26(1): pay within 30 days of the date the dividend is payable, with a return.
- s12(1)(e): dividends to persons not ordinarily resident or carrying on business, and to any company, exempt from normal tax. s12(1)(u): royalty or management charge subject to s32B exempt from normal tax.
- s27: NR interest tax; "ten" replaced with "fifteen" (Act s11, p. S12). ERS 2024 summary: increased from 10% to 15%. ERS Withholding page still says ten per cent (stale). ERS Rates page shows "Outside SACU 15%".
- s28(a) address-outside presumption; s28(c) company debtor deemed ordinarily resident if registered, managed or controlled in Eswatini. s29 exemptions; s29(c) (E20 de minimis) deleted by Act s12. s31 debtor withholds. s32(1): payable within 14 days after accrual; s32(3) credit against normal tax.
- s32A: entertainers and sportspersons 15% of gross; remit within 15 days of payment; personal liability.
- s32B: royalties and management charges 15% of gross, final (s32B(3)); remit within 15 days of payment (s32B(4)(b)); exemption for public-character institutions (royalties); personal liability s32B(6).
- s32E: BPT 15% on deemed repatriated income A - B (A taxable income of branch, B Eswatini tax on it); treated as normal tax; 12.5% proviso and s32E(4) "neighbouring country" definition deleted by Act s14 (p. S13). ERS 2024 summary: fixed at 15% regardless of country.
- s32F, s32G remittance changed to the 15th of the next month (Act ss15, 16).
- s32H(4) to (7) (Act s17, p. S14): entry at market value; exit deemed disposal at market value; Commissioner may exempt by written notice where intending to re-acquire residence and security given.
- s59: non-resident (principal place of business outside Eswatini) construction contractors: 15% of payment not shown to be direct cost of materials; on account; remit within 15 days; annual return within 30 days after year end; personal liability.
- s59A: 15% of gross under an Eswatini-source services contract (not employment; goods incidental); excludes s32B and s59 payments; on account; remit within 15 days; annual return within 30 days after year end.
- s59C: notify the Commissioner within 30 days of an agreement with a non-resident for services in Eswatini.
- Third Schedule Part I (Act s39, pp. S29 to S30): para 1(a) company 25%; para 2 non-resident person other than company or trust: rate not to reduce tax below 10% of taxable income, 3% for the pension part.
- s69quin (Act s36, p. S28): where any inconsistency between the Order and any other law prescribing a rate of tax, the Order prevails.
- 2026 returns notice: every person ordinarily not resident to whom Eswatini-source gross income accrued must file; all non-individual entities 31 October 2026; individuals with employment income above E1,000,000, with employment and other income, HNWIs: 30 November 2026; other approved year ends within four months; TaxEase only; payment EFT, speed points, MoMo Pay, deposits, no cash.
- ERS Rates and Thresholds: all non-resident withholding due "on or before the 15th day of the following month"; additional tax scale as s40bis. (Differs from the statutory 14 or 15 days or 30 days for ss26, 32, 32A, 32B, 59, 59A.)
- ERS Withholding page: BPT formula A minus B; services withholding example (mechanic with tools and parts).
- SA DTA: Gazette notice under s68(2) dated 24 November 2004; Art. 9 associated enterprises with corresponding adjustment and competent authority consultation; Art. 10(2): 10% for a beneficial owner company holding at least 25% of capital, 15% otherwise; Protocol (23 January 2004): BPT on repatriated income of an SA company's PE not above 10%.
- ERS Tax Legislations page lists DTAs: Botswana, Lesotho, Mauritius, Republic of China (Taiwan), Seychelles, South Africa, United Kingdom (all PDFs answered HTTP 200; only South Africa read).

## Conflicts found
- `sz-corporate-income-tax.md` (rows: NRST 12.5% for BLNS companies; non-resident interest 10%; BPT 12.5%) and `sz-tax-overview.md` (12.5% NRST example; "interest 10%") conflict with Act 20 of 2023 ss10, 11, 14 and the ERS 2024 summary (15% for all three from 1 July 2024). Not edited here (separate PR).
- ERS Withholding page shows 10% on non-resident interest; superseded by the Act.

## Not found / not confirmed
- Transfer Pricing Regulations (s65quin(11), "regulation 11" in s65sex(4)): not on ERS, not on EswatiniLII.
- Gazette notices: s65quin(13) threshold, s65quin(12) intangibles percentage, s65quin(8) beneficial regime limits, Act 20 of 2023 commencement.
- Tax Administration Act: none on the ERS legislation page or EswatiniLII.
- CbCR, master/local file, APA procedures: none in the texts read.
- Amendment of the remittance periods in ss26, 32, 32A, 32B, 59, 59A to the 15th of the following month.

## Blocked sources
None. EswatiniLII answered without a human check; it simply does not hold the 2023 Act or any TP regulations.
