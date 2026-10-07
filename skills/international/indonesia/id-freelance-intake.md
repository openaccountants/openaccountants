---
name: id-freelance-intake
description: ALWAYS USE THIS SKILL when a user asks for help preparing a 2025 Indonesian tax return AND mentions freelancing, self-employment, online seller, kontraktor, pekerjaan bebas, sole proprietor (Usaha Dagang), or a PT Perorangan in Indonesia. Trigger on phrases like "siapkan SPT Tahunan", "lapor pajak freelance Indonesia", "PPh Final UMKM 0,5%", "PP 55/2022", "PT Perorangan tax return", "online seller Indonesia tax", "kontraktor pajak", "pekerjaan bebas", "Usaha Dagang", "Coretax SPT", "NPWP 16 digit", or any similar phrasing where the user is an Indonesia-resident self-employed individual, sole proprietor, or micro-PT founder. This is the REQUIRED entry point for the Indonesian freelance/SME workflow — every downstream skill in the stack (id-pph-final-umkm, id-income-tax, id-corporate-tax, id-withholding, id-payroll-pph21, indonesia-vat, id-bookkeeping, id-einvoice-coretax, id-formation, id-tax-optimization, id-return-assembly) depends on this skill running first. Uses ask_user_input_v0-style structured questions. Indonesian residents only (full-year tax residents and foreigners with > 183 days permanent presence). ALWAYS read this skill first when starting an Indonesian freelance/SME tax workflow.
jurisdiction: ID
tax_year: 2026
last_updated: 2026-09-27
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Indonesia: intake for freelancers, sole traders and PT Perorangan founders

Tax year 2026 (calendar year), with a short section on the tax year 2025 return that was due on 31 March 2026. Figures and rules are stated as published by the Directorate General of Taxes (Direktorat Jenderal Pajak, DJP) on pajak.go.id and checked on 25 September 2026.

## Scope

This Guide is the first step for an Indonesian tax resident individual who earns money outside a job: a freelancer or professional (pekerjaan bebas), a trader or service business run in their own name (including a trade name, Usaha Dagang), an online seller, or the founder of a single-founder company (PT Perorangan). It decides:

- whether the person is in scope at all (residency, entity);
- which income tax method applies for 2026: the 0.5% final tax on turnover, the deemed-profit norm (NPPN) with simple records, or full bookkeeping with general rates;
- whether clients must withhold PPh 21 from the person's fees, and what to do with the withholding slips;
- whether VAT registration (PKP) is required;
- what the annual return (SPT Tahunan) needs, where and when it is filed, and what happens if it is late;
- which specialist topics to hand on to (payroll, withholding, VAT, bookkeeping, company tax).

Out of scope: non-residents and part-year residents, corporate groups, and anything needing audited accounts. Those are referred (see "When to refuse or refer").

Key law behind this Guide: the Income Tax Law (UU PPh) as amended by UU 7/2021 (HPP); PP 55/2022 on income tax adjustments, as amended by PP 20/2026 (in force 22 April 2026); PMK 164/2023 on the 0.5% regime and PKP reporting; PMK 168/2023 on PPh 21; PER-17/PJ/2015 on NPPN; PMK 81/2024 on Coretax; PMK 131/2024 on VAT from 2025 ([DJP on PMK 164/2023](https://www.pajak.go.id/en/node/104146); [DJP juklak PMK 168/2023](https://pajak.go.id/index.php/en/node/104821); [DJP on PMK 81/2024](https://www.pajak.go.id/en/node/112032); [DJP on PMK 131/2024](https://www.pajak.go.id/en/node/113455)).

## What changed in 2026 (read this first)

PP 20/2026 changed the 0.5% final tax regime from 22 April 2026. The rate and ceiling did not change; who may use it, and how turnover is counted, did ([DJP article, author's opinion](https://www.pajak.go.id/en/node/119950); [DJP slides on PP 20/2026](https://pajak.go.id/sites/default/files/2026-06/Peraturan%20Pemerintah%20nomor%2020%20Tahun%202026.pdf)).

- **No more 7-year limit for individuals.** Article 59 of PP 55/2022 is deleted for individuals and single-founder PT Perorangan. They may use the 0.5% rate for as long as they meet the criteria, or until they choose general rates ([DJP slides](https://pajak.go.id/sites/default/files/2026-06/Peraturan%20Pemerintah%20nomor%2020%20Tahun%202026.pdf)).
- **Transition for people whose period had ended.** An individual whose 7 years ended in 2024 may use 0.5% for tax years 2025 and 2026. An individual or PT Perorangan whose period ended in 2025 may use it for tax year 2026, in each case only if they meet the PP 55/2022 criteria ([DJP slides](https://pajak.go.id/sites/default/files/2026-06/Peraturan%20Pemerintah%20nomor%2020%20Tahun%202026.pdf)).
- **Fewer eligible entities.** Only individuals, single-founder PT Perorangan and cooperatives are subjects. A CV, firma, ordinary PT or village enterprise (BUMDes) newly registered cannot use 0.5%; those registered before PP 20/2026 keep it until their existing period ends ([DJP slides](https://pajak.go.id/sites/default/files/2026-06/Peraturan%20Pemerintah%20nomor%2020%20Tahun%202026.pdf)). A DJP staff article states that under PP 55/2022 that period was 3 years for a PT and 4 years for a CV, firma or BUMDes ([DJP article, author's opinion](https://www.pajak.go.id/en/node/119969)).
- **Turnover is counted wider.** The Rp4.8 billion test now adds all gross income from business and from pekerjaan bebas, whether taxed finally or not, including foreign turnover.
- **Household aggregation (check).** DJP staff articles explaining PP 20/2026 art. 58(2)-(3) say that husband, wife (even with separate property or separate filing), minor children and every PT Perorangan either spouse set up are added together, and that if the total exceeds Rp4.8 billion in one year none of them may use 0.5% in the next year ([DJP article, author's opinion](https://pajak.go.id/en/node/119991)). These are personal-opinion articles and DJP's official PP 20/2026 summary does not cover the household rule, so check the PP 20/2026 text or ask the tax office (KPP) before relying on it. The official summary does confirm that one or more PT Perorangan plus their individual owner are counted together ([DJP slides](https://pajak.go.id/sites/default/files/2026-06/Peraturan%20Pemerintah%20nomor%2020%20Tahun%202026.pdf)).
- **Pekerjaan bebas list made explicit.** Content creators (influencers, selebgram, bloggers, vloggers), painters, sculptors and "other artists" are named. A DJP staff article says this confirms, rather than changes, the old exclusion ([DJP article, author's opinion](https://pajak.go.id/en/node/120065)).
- **End of 2026 cut-off.** An individual or PT Perorangan that no longer meets the new criteria may keep using 0.5% until the end of 2026 ([DJP slides](https://pajak.go.id/sites/default/files/2026-06/Peraturan%20Pemerintah%20nomor%2020%20Tahun%202026.pdf)).

Tax year 2025 was the first annual return filed on Coretax DJP. The deadline stayed 31 March 2026, but DJP waived fines and interest for individuals who filed or paid by 30 April 2026 (KEP-55/PJ/2026) ([DJP article, author's opinion](https://pajak.go.id/en/node/119611)).

## Ask the client first

Ask these before reading any documents. Use plain words and add the Indonesian term in brackets the first time.

- **Residency in 2026.** Do you live in Indonesia, or were you here more than 183 days in any 12 months? ([UU PPh on DJP](https://www.pajak.go.id/en/node/35337)) Part-year or non-resident: refer.
- **What you do.** Describe the work. Is it a profession or a personal skill you sell (doctor, lawyer, accountant, consultant, architect, notary, translator, writer, researcher, trainer, speaker, artist, musician, presenter, content creator, insurance agent, broker or finder of customers)? Or is it trading, making goods or running a service business?
- **Entity.** Do you invoice in your own name, under a trade name, through a PT Perorangan, or through a CV, firma or PT?
- **Gross turnover.** Your total gross receipts for 2025 and your expected total for 2026, from all business and professional work, including income earned abroad.
- **Household.** Are you married? Do you file as one family unit, or separately (separate property, PH; or wife filing on her own, MT)? What are your spouse's and minor children's business or professional receipts, and does either of you own a PT Perorangan?
- **Your history with the 0.5% rate.** Have you ever paid the 0.5% (or earlier 1%) final tax? From which year? Did you ever notify DJP that you chose general rates? ([DJP on the earlier rates](https://pajak.go.id/en/node/120065))
- **NPPN notice.** Did you file a notice to use the deemed-profit norm (NPPN) for 2026 by 31 March 2026? Do you keep full books (pembukuan) or only simple records (pencatatan)?
- **Withholding slips.** Did clients withhold PPh 21 or PPh 23 from your fees? Do you have the slips (bukti potong, for example BP-21)? Did you give any client a UMKM certificate (surat keterangan) or a statement that your turnover is under Rp500 million (surat pernyataan)?
- **VAT.** Are you registered for VAT (PKP)? Did your turnover go above Rp4.8 billion in any book year?
- **Staff and payments you make.** Do you pay employees, pay other freelancers, rent premises, or pay suppliers abroad?
- **Coretax.** Is your Coretax DJP account active, and have you created your authorisation code or electronic certificate (kode otorisasi / sertifikat elektronik)?
- **Family status for PTKP.** Single or married, and how many dependants (at most three count)?

## The method, step by step

1. **Confirm residency.** An individual who lives in Indonesia, or is present more than 183 days in 12 months, is a resident taxpayer ([UU PPh on DJP](https://www.pajak.go.id/en/node/35337)). If the person arrived or left during 2026, or is unsure, stop and refer.
2. **Confirm registration.** For individuals the population number (NIK) serves as the taxpayer number (NPWP); a person who meets the subjective and objective conditions must be registered, but holding an NIK does not by itself mean tax is due ([DJP article, author's opinion](https://stats.pajak.go.id/en/node/71919)). Check that the business code (KLU) in the Coretax profile matches the real activity, because the NPPN percentage depends on it.
3. **Split the income into types.** Put every receipt into one of: employment; pekerjaan bebas (professional or personal-skill services); business (trade, production, other services); income already taxed finally under its own rule (for example construction services); passive income. Mixed earners keep separate records for each type.
4. **Test the Rp4.8 billion ceiling on the wide measure.** Add, for the previous tax year: all business turnover plus all pekerjaan bebas receipts, final and non-final, Indonesian and foreign. Add every PT Perorangan the person owns ([DJP slides](https://pajak.go.id/sites/default/files/2026-06/Peraturan%20Pemerintah%20nomor%2020%20Tahun%202026.pdf)). If married and filing separately (PH or MT), DJP staff articles also add the spouse's, the minor children's and every PT Perorangan either spouse founded; check this with the KPP or the PP 20/2026 text ([DJP article, author's opinion](https://pajak.go.id/en/node/119991)). If the total is above Rp4.8 billion, the 0.5% final tax is not available for the next year. Transition: for tax year 2026, an individual or PT Perorangan that fails only the new PP 20/2026 tests may still use 0.5% until 31 December 2026, so the wide test (and, if confirmed, the household test) first removes 0.5% from 2027 ([DJP slides](https://pajak.go.id/sites/default/files/2026-06/Peraturan%20Pemerintah%20nomor%2020%20Tahun%202026.pdf)).
5. **Choose the method for each income type.**
   - Pekerjaan bebas income: never the 0.5% rate. Use NPPN if gross is less than Rp4.8 billion and the notice was filed in time; otherwise full bookkeeping ([DJP article, author's opinion](https://pajak.go.id/en/node/120065)).
   - Business income of an eligible individual: 0.5% final on gross monthly turnover, unless the person has notified DJP that they chose general rates. For 2026, someone who fails only the new PP 20/2026 tests keeps 0.5% to 31 December 2026. If general rates apply, use NPPN (if notified and gross is less than Rp4.8 billion) or full bookkeeping.
   - PT Perorangan: 0.5% only if single-founder, not delivering pekerjaan-bebas-type services, and the combined turnover test is met; otherwise the corporate return at general rates (see the company tax Guide).
6. **Apply the 0.5% regime correctly (if used).** Tax is 0.5% of each month's gross turnover, paid by the 15th of the next month. An individual pays nothing on the first Rp500 million of turnover in the tax year, counted cumulatively from January ([DJP article, author's opinion](https://www.pajak.go.id/en/node/119950); [DJP on PMK 81/2024](https://www.pajak.go.id/en/node/112032)). Clients who are withholders deduct 0.5% final, instead of their normal withholding, only if shown the UMKM certificate (surat keterangan); an individual with turnover under Rp500 million gives a statement (surat pernyataan) so that nothing is withheld ([DJP](https://www.pajak.go.id/en/node/104146)).
7. **Apply NPPN correctly (if used).** Net income = NPPN percentage for the KLU and region x gross receipts. No expenses and no loss carry-forward are deducted on top ([DJP article, author's opinion](https://pajak.go.id/en/node/120065)). Then subtract PTKP and apply the Art. 17 rates.
8. **Collect the withholding credits.** Gather every BP-21 (PPh 21 on fees to a non-employee, Bukan Pegawai) and any other slips. Non-final withholding is a credit against the annual tax. 0.5% final tax withheld by a client is a payment of that final tax, not a credit against tax at general rates ([DJP](https://www.pajak.go.id/en/node/104146)). On Coretax, slips issued by withholders pre-fill the return ([DJP](https://www.pajak.go.id/en/node/112032)).
9. **Plan monthly instalments (PPh 25) for general-rate filers.** Under UU PPh art. 25(1) the monthly instalment is the tax due on last year's annual return, less PPh 21 and 23 withheld, PPh 22 collected and creditable foreign tax, divided by 12; instalments are credited in the annual return ([UU PPh on DJP](https://www.pajak.go.id/en/node/35337)). Special rules for shop-type traders and first-year businesses: check, and see the individual income tax Guide.
10. **Check VAT.** Above Rp4.8 billion of turnover a business must be registered as PKP; below that, registration is voluntary. For a taxpayer on the 0.5% regime whose turnover passes Rp4.8 billion, PMK 164/2023 allows the PKP report up to the end of that book year; the earlier general rule was the end of the following month. For anyone else (NPPN or bookkeeping), check the current deadline and see the VAT Guide ([DJP](https://www.pajak.go.id/en/node/104146)).
11. **Check duties as a payer.** Employees, rent, payments to other freelancers or to non-residents create withholding duties; route to the payroll and withholding Guides. Not covered here, check before relying: the registration deadline after starting a business or profession, the monthly PPh 21/26 return deadline, and the special PPh 25 rate for shop-type traders (OPPT); see the income tax and payroll Guides.
12. **Check Coretax readiness and file.** The annual return (SPT Tahunan PPh Orang Pribadi) for 2026 is due by 31 March 2027 on Coretax DJP; the balance due (PPh 29) is payable by the same date ([DJP article, author's opinion](https://pajak.go.id/en/node/119611)).
13. **Record open points and hand off.** Write down every assumption and every item that needs a Konsultan Pajak.

## Figures and dates, with the year they apply to

| Item | Figure | Applies to | Source |
| --- | --- | --- | --- |
| Final tax on gross turnover (eligible individual, PT Perorangan, cooperative) | 0.5% of monthly gross turnover | 2026 (unchanged by PP 20/2026) | [DJP article, author's opinion](https://www.pajak.go.id/en/node/119950) |
| Ceiling for the 0.5% regime | turnover not above Rp4.8 billion (Rp4.800.000.000) in one tax year | 2026 | [DJP slides on PP 20/2026](https://pajak.go.id/sites/default/files/2026-06/Peraturan%20Pemerintah%20nomor%2020%20Tahun%202026.pdf) |
| Turnover not taxed under the 0.5% regime | first Rp500 million a year, individuals only | 2026 | [DJP article, author's opinion](https://www.pajak.go.id/en/node/119950) |
| Payment of the 0.5% tax | by the 15th of the following month | from 2025 (PMK 81/2024) | [DJP on PMK 81/2024](https://www.pajak.go.id/en/node/112032) |
| Old time limits (PP 55/2022, now deleted for individuals and PT Perorangan) | 7 years individual; 4 years PT Perorangan, CV, firma, BUMDes, cooperative; 3 years PT | periods that began before 22 April 2026 | [DJP article, author's opinion](https://www.pajak.go.id/en/node/119969); [DJP slides on PP 20/2026](https://pajak.go.id/sites/default/files/2026-06/Peraturan%20Pemerintah%20nomor%2020%20Tahun%202026.pdf) |
| Cooperative time limit (kept) | 4 tax years from registration | 2026 | [DJP slides on PP 20/2026](https://pajak.go.id/sites/default/files/2026-06/Peraturan%20Pemerintah%20nomor%2020%20Tahun%202026.pdf) |
| NPPN available if gross is | less than Rp4.8 billion a year | 2026 | [DJP](https://pajak.go.id/en/node/35180) |
| NPPN notice deadline | within the first 3 months of the tax year (31 March 2026 for 2026; 31 March 2027 for 2027) | 2026 and 2027 | [DJP article, author's opinion](https://pajak.go.id/en/node/114299) |
| NPPN percentage, example: computer programming (KLU 62010), general practice (KLU 86201) | 50% in every region | PER-17/PJ/2015 table, still in use in 2026 | [PER-17/PJ/2015 Lampiran I](https://www.pajak.go.id/sites/default/files/2019-03/Lampiran%201_PER%20-%2017.PJ_.2015.pdf) |
| PPh 21 on fees to a non-employee (Bukan Pegawai) | 50% of gross x Art. 17 rates | from 1 January 2024 (PMK 168/2023) | [DJP juklak PMK 168/2023](https://pajak.go.id/index.php/en/node/104821) |
| PPh 26 on services by a non-resident individual | 20% final, or treaty rate | from 1 January 2024 | [DJP juklak PMK 168/2023](https://pajak.go.id/index.php/en/node/104821) |
| Art. 17 rates for individuals | 5% to Rp60 million; 15% over Rp60 million to Rp250 million; 25% over Rp250 million to Rp500 million; 30% over Rp500 million to Rp5 billion; 35% over Rp5 billion | from tax year 2022, unchanged in 2026 | [DJP article, author's opinion](https://pajak.go.id/en/node/71824) |
| PTKP (non-taxable allowance) | Rp54,000,000 self; plus Rp4,500,000 if married; plus Rp4,500,000 per dependant, at most 3 | 2026 | [DJP article, author's opinion](https://www.pajak.go.id/en/node/38279) |
| PKP (VAT) registration | turnover above Rp4.8 billion; 0.5%-regime taxpayers report by end of that book year (PMK 164/2023 relaxation); earlier general rule end of the following month, others check | 2026 | [DJP](https://www.pajak.go.id/en/node/104146) |
| VAT | 12% rate; for non-luxury goods, services and intangibles the base is 11/12 of price (effective 11%) | from 1 January 2025 (PMK 131/2024) | [DJP](https://www.pajak.go.id/en/node/113455) |
| Annual return deadline (individual) | 3 months after the tax year: 31 March 2027 for tax year 2026 | 2026 | [DJP article, author's opinion](https://pajak.go.id/en/node/118848) |
| Late annual return (individual) | fine of Rp100,000 | 2026 | [DJP article, author's opinion](https://pajak.go.id/en/node/66324) |
| Residency test | present more than 183 days in 12 months (or living in Indonesia) | 2026 | [UU PPh on DJP](https://www.pajak.go.id/en/node/35337) |

At-least or more-than matters here. The 0.5% regime is for turnover **not above** Rp4.8 billion; NPPN is for gross **less than** Rp4.8 billion; PKP registration is required when turnover is **above** Rp4.8 billion. A person with exactly Rp4.8 billion can use 0.5% but, on the printed wording, not NPPN.

## Boundaries and exceptions

| Situation | Treatment | Source |
| --- | --- | --- |
| Profession or personal-skill service (doctor, lawyer, accountant, consultant, architect, notary, PPAT, appraiser, actuary and similar experts; musicians, presenters, actors, models, painters, sculptors, content creators, other artists; athletes; advisers, teachers, trainers, speakers, moderators; writers, researchers, translators; advertising agents; project supervisors; brokers and finders of customers; street sales agents; insurance agents; multi-level marketing distributors) | Pekerjaan bebas. Never 0.5%; NPPN or bookkeeping; clients withhold PPh 21 as Bukan Pegawai | [DJP slides on PP 20/2026](https://pajak.go.id/sites/default/files/2026-06/Peraturan%20Pemerintah%20nomor%2020%20Tahun%202026.pdf); [DJP juklak PMK 168/2023](https://pajak.go.id/index.php/en/node/104821) |
| Trading, production, online selling, a service run as a business | Business income. 0.5% if eligible; otherwise NPPN or bookkeeping | [DJP article, author's opinion](https://www.pajak.go.id/en/node/119950) |
| Unclear whether profession or business (for example a freelance developer or designer) | Treat as pekerjaan bebas (the conservative reading, since "similar experts" and "other artists" are now named) and flag for a Konsultan Pajak | [DJP article, author's opinion](https://pajak.go.id/en/node/120065) |
| Both profession and business | Separate records. Business part may use 0.5%; profession part uses NPPN or books. Both count toward the Rp4.8 billion test | [DJP slides on PP 20/2026](https://pajak.go.id/sites/default/files/2026-06/Peraturan%20Pemerintah%20nomor%2020%20Tahun%202026.pdf) |
| Income already taxed finally under its own rule (for example construction services) | Stays under that rule, but its turnover still counts toward the Rp4.8 billion test | [DJP slides on PP 20/2026](https://pajak.go.id/sites/default/files/2026-06/Peraturan%20Pemerintah%20nomor%2020%20Tahun%202026.pdf) |
| Married, one family unit (joint number) | Spouses' income is combined under the general rules | [DJP article, author's opinion](https://pajak.go.id/en/node/119991) |
| Married, separate property (PH) or wife filing separately (MT) | Check: DJP staff articles say turnover is still combined with spouse, minor children and all PT Perorangan of either spouse for the Rp4.8 billion test, with tax still computed per taxpayer; not in the official summary, so confirm with the KPP | [DJP article, author's opinion](https://pajak.go.id/en/node/119991) |
| PT Perorangan set up to sell a pekerjaan-bebas-type service (for example a tax consultant's own PT) | Not eligible for 0.5% | [DJP slides on PP 20/2026](https://pajak.go.id/sites/default/files/2026-06/Peraturan%20Pemerintah%20nomor%2020%20Tahun%202026.pdf) |
| CV, firma, ordinary PT, BUMDes registered on or after 22 April 2026 | Not eligible for 0.5%; general corporate rules | [DJP slides on PP 20/2026](https://pajak.go.id/sites/default/files/2026-06/Peraturan%20Pemerintah%20nomor%2020%20Tahun%202026.pdf) |
| Entity registered before 22 April 2026 (other than PT Perorangan and cooperatives) | Keeps 0.5% until its PP 55/2022 period ends | [DJP slides on PP 20/2026](https://pajak.go.id/sites/default/files/2026-06/Peraturan%20Pemerintah%20nomor%2020%20Tahun%202026.pdf) |
| Individual who chose general rates | Notice by the end of a tax year; general rates apply from the next year. A new registrant may choose at registration | [DJP](https://www.pajak.go.id/en/node/104146) |
| Missed the NPPN notice | Treated as choosing bookkeeping for that year | [DJP](https://pajak.go.id/en/node/35180) |
| Once on bookkeeping | A DJP staff article says: stays on bookkeeping and cannot go back to simple records | [DJP article, author's opinion](https://pajak.go.id/en/node/118848) |
| Books or records not kept or not shown at audit | DJP computes net income using NPPN | [DJP](https://pajak.go.id/en/node/35180) |
| Turnover under Rp500 million on the 0.5% regime | No tax, but the annual return must still be filed | [DJP](https://www.pajak.go.id/en/node/104146) |
| Bribes and gratuities, including to foreign public officials | Never deductible (new art. 20A) | [DJP slides on PP 20/2026](https://pajak.go.id/sites/default/files/2026-06/Peraturan%20Pemerintah%20nomor%2020%20Tahun%202026.pdf) |

## Worked cases

**Case 1: online seller on the 0.5% regime, tax year 2026.** Individual, not married, sells goods online, no profession income, turnover Rp100 million every month (Rp1.2 billion for 2026), no spouse or PT Perorangan. Turnover is not above Rp4.8 billion, so 0.5% applies. January to May cumulative turnover is Rp500 million, which is not taxed. From June each month's Rp100 million is taxed: 0.5% x Rp100,000,000 = Rp500,000, paid by the 15th of the next month (June tax by 15 July 2026). Total for 2026: 0.5% x (Rp1,200,000,000 - Rp500,000,000) = Rp3,500,000. The annual return is still filed by 31 March 2027. ([DJP article, author's opinion](https://www.pajak.go.id/en/node/119950); [DJP on PMK 81/2024](https://www.pajak.go.id/en/node/112032))

**Case 2: general practitioner on NPPN, tax year 2026.** A GP (KLU 86201, pekerjaan bebas) with gross fees of Rp600 million in 2026, married with one child (PTKP K/1), filed the NPPN notice by 31 March 2026. Net income = 50% x Rp600,000,000 = Rp300,000,000. PTKP = Rp54,000,000 + Rp4,500,000 + Rp4,500,000 = Rp63,000,000. Taxable income = Rp237,000,000. Tax = 5% x Rp60,000,000 = Rp3,000,000, plus 15% x Rp177,000,000 = Rp26,550,000, total Rp29,550,000. Suppose the hospitals' BP-21 slips show Rp20,000,000 withheld (an assumed figure for illustration; use the real slips). Balance due (PPh 29) = Rp9,550,000, payable by 31 March 2027. Had the notice been missed, the GP would be treated as keeping books and must compute actual profit. ([PER-17/PJ/2015 Lampiran I](https://www.pajak.go.id/sites/default/files/2019-03/Lampiran%201_PER%20-%2017.PJ_.2015.pdf); [DJP article, author's opinion](https://pajak.go.id/en/node/71824); [DJP](https://pajak.go.id/en/node/35180))

**Case 3: PPh 21 on a one-off fee, 2026.** A company pays a freelance photographer an honorarium of Rp200 million. PPh 21 base = 50% x Rp200,000,000 = Rp100,000,000. Tax = 5% x Rp60,000,000 = Rp3,000,000 plus 15% x Rp40,000,000 = Rp6,000,000, total Rp9,000,000 withheld, with a BP-21 slip. The photographer credits Rp9,000,000 in the annual return. Since PMK 168/2023 the formula is a single, non-cumulative calculation per payment. ([DJP article, author's opinion](https://www.pajak.go.id/en/node/114896); [DJP juklak PMK 168/2023](https://pajak.go.id/index.php/en/node/104821))

**Case 4: household aggregation (check; based on a DJP staff article, not the official summary).** Husband is a notary with Rp3 billion of fees in 2026; wife runs a boutique with Rp2 billion turnover on the 0.5% regime; their minor child earns Rp500 million as a child singer. They file separately. Combined turnover = Rp5.5 billion, above Rp4.8 billion, so the wife cannot use 0.5% in 2027 even though her own turnover is unchanged. The husband and child were never eligible (pekerjaan bebas). ([DJP article, author's opinion](https://pajak.go.id/en/node/119991))

**Case 5: wide turnover test, 2026 turnover deciding 2027.** Trader with 2026 Rp2 billion trade turnover, Rp2.5 billion construction turnover (taxed under the construction final rule) and Rp1.5 billion as a paid speaker (general rates). Total Rp6 billion: from 2027 not eligible for 0.5% on the trade income, which is then taxed at general rates (for 2026 the transition keeps 0.5% to 31 December 2026 if only the new test is failed). With Rp1 billion construction instead, the total is Rp4.5 billion and the trade income can use 0.5%. ([DJP slides on PP 20/2026](https://pajak.go.id/sites/default/files/2026-06/Peraturan%20Pemerintah%20nomor%2020%20Tahun%202026.pdf))

**Case 6: freelancer registered for VAT.** A PKP consultant invoices a service of Rp12,000,000 in 2026. VAT = 12% x (11/12 x Rp12,000,000) = Rp1,320,000, the same as 11% of the price. ([DJP](https://www.pajak.go.id/en/node/113455))

**Case 7: 0.5% period ended in 2024.** An individual trader started on the 0.5% regime in 2018, so the 7-year period ended in 2024. Turnover is Rp2 billion a year and there are no household issues. The trader may use 0.5% for tax years 2025 and 2026 under the PP 20/2026 transition. For 2027, check: article 59 is deleted and DJP says individuals have no time limit while they meet the criteria, but the transition text names only 2025 and 2026, so confirm with the KPP before relying on it. ([DJP slides on PP 20/2026](https://pajak.go.id/sites/default/files/2026-06/Peraturan%20Pemerintah%20nomor%2020%20Tahun%202026.pdf); [DJP article, author's opinion](https://www.pajak.go.id/en/node/119950))

**Case 8: missed NPPN notice.** A freelance translator with gross fees of Rp400 million in 2026 did not file the NPPN notice by 31 March 2026. Translators are pekerjaan bebas, so 0.5% is not available. Without the notice the translator is treated as choosing bookkeeping for 2026 and must compute actual profit from books; DJP guidance says a taxpayer on bookkeeping cannot go back to simple records. ([DJP](https://pajak.go.id/en/node/35180); [DJP article, author's opinion](https://pajak.go.id/en/node/118848))

## When to refuse or refer

Stop, say why in one sentence, and refer to a Konsultan Pajak (or an Akuntan Publik where audited accounts are needed) when:

- the person was not resident for the whole of 2026, arrived or left during the year, or claims non-resident or treaty status;
- the person is a foreign national who may qualify for special treatment of foreign-source income, or has treaty questions;
- the business is part of a group, has related-party dealings across borders, or needs audited financial statements;
- the household or company turnover is at or near Rp4.8 billion and the person wants to rely on 0.5% or NPPN (the wide and household counting rules are new, and a DJP staff article tells such households to consult their KPP before filing: [DJP article, author's opinion](https://pajak.go.id/en/node/119991));
- the person's 0.5% period ended in 2024 and they want to stay on 0.5% for 2027 (check: the transition text names only 2025 and 2026, while the official summary says individuals now have no time limit; confirm with the KPP);
- the classification between profession and business is disputed and material to the result;
- the person has an open audit, objection or tax assessment (SKP) for the years involved;
- the person wants to use a CV, firma or ordinary PT to reach the 0.5% rate (not available to new registrations from 22 April 2026: [DJP slides on PP 20/2026](https://pajak.go.id/sites/default/files/2026-06/Peraturan%20Pemerintah%20nomor%2020%20Tahun%202026.pdf));
- the facts suggest splitting turnover across family members or companies to stay under the ceiling (the PP 20/2026 anti-avoidance rules target this).

Conservative defaults when the facts are unclear:

- profession or business unclear: treat as profession (no 0.5%);
- NPPN notice not shown: assume none was filed, so bookkeeping applies;
- household turnover unknown: do not rely on 0.5% for the next year until it is known;
- PTKP status unknown: use single, no dependants (TK/0);
- Coretax access unknown: assume not active and flag.

## Filing and payment

**During 2026**

- 0.5% regime: pay each month's tax by the 15th of the next month ([DJP on PMK 81/2024](https://www.pajak.go.id/en/node/112032)).
- General rates: pay PPh 25 instalments by the 15th of the next month ([DJP on PMK 81/2024](https://www.pajak.go.id/en/node/112032)).
- PKP: VAT returns and payments monthly (see the VAT Guide).
- Payers of wages or fees: PPh 21/26 withheld is paid by the 15th of the next month ([DJP on PMK 81/2024](https://www.pajak.go.id/en/node/112032)).

**The annual return for tax year 2026**

- File the individual annual return (SPT Tahunan PPh Orang Pribadi) on Coretax DJP by 31 March 2027. Coretax has one individual return form in place of the old 1770, 1770 S and 1770 SS; the filer answers yes/no questions in the main form and each "yes" opens an attachment ([DJP article, author's opinion](https://pajak.go.id/en/node/118848)).
- Before filing: activate Coretax and create the authorisation code or electronic certificate. Try the DJP simulator first if unsure.
- Pay any balance (PPh 29) before the filing deadline.
- The NPPN notice for the following year is also due by 31 March (for 2027, by 31 March 2027) through Coretax: Layanan Wajib Pajak, Layanan Administrasi, service AS.04-01 ([DJP article, author's opinion](https://pajak.go.id/en/node/114299)).
- Late filing: fine of Rp100,000 for an individual ([DJP article, author's opinion](https://pajak.go.id/en/node/66324)).

**Tax year 2025 (returns filed in 2026)**

- The 2025 return was due 31 March 2026 on Coretax. Under KEP-55/PJ/2026, individuals who filed and/or paid between 1 April and 30 April 2026 have no fine or interest; DJP does not issue a tax bill (STP) for them, and where one was already issued the regional office removes the sanction ([DJP article, author's opinion](https://pajak.go.id/en/node/119611)).
- A 2025 return filed after 30 April 2026 is late in the ordinary way.
- For 2025 the old PP 55/2022 rules applied, except that an individual whose 7 years ended in 2024 could use 0.5% for 2025 under the PP 20/2026 transition.

## Completion checklist

- [ ] Residency for the whole of 2026 confirmed, or the case referred.
- [ ] NIK/NPWP, registered tax office (KPP) and KLU code recorded; KLU matches the real activity.
- [ ] Entity recorded: individual, trade name, PT Perorangan, or other entity.
- [ ] Every receipt classified as employment, pekerjaan bebas, business, separately-final, or passive.
- [ ] Wide turnover test done for the previous year, including foreign receipts and pekerjaan bebas receipts.
- [ ] Household test done if married filing separately (spouse, minor children, all PT Perorangan of either spouse).
- [ ] 0.5% history recorded: start year, any notice choosing general rates, transition year if the old period ended in 2024 or 2025.
- [ ] Method chosen for each income type, with the reason: 0.5%, NPPN (notice date recorded) or bookkeeping.
- [ ] Monthly 0.5% payments reconciled to turnover, with the Rp500 million allowance applied cumulatively.
- [ ] UMKM certificate or statement given to withholders where relevant.
- [ ] All BP-21 and other slips collected; final and non-final withholding kept apart.
- [ ] PTKP status recorded (default TK/0 if unknown).
- [ ] PPh 25 instalments for next year computed if on general rates.
- [ ] PKP test done for each book year; registration or voluntary status recorded.
- [ ] Payer duties (employees, rent, other freelancers, non-resident suppliers) routed.
- [ ] Coretax account active and authorisation code or certificate created.
- [ ] Filing date 31 March 2027 diarised; NPPN notice for 2027 diarised for the same date if needed.
- [ ] Open points and conservative defaults written down for the reviewer.

## Intake summary to hand on

```
INTAKE SUMMARY: Indonesia, tax year 2026

Taxpayer: [name] | NIK/NPWP: [number] | KPP: [office]
Residency: resident all year (yes / refer)
Entity: individual | trade name | PT Perorangan | other
KLU: [code and activity] | PTKP: [TK/0 ... K/3]
Coretax: active with authorisation code | onboarding needed

Income types: pekerjaan bebas [yes/no] | business [yes/no] | mixed [yes/no]
Wide turnover (previous year): Rp [ ] | household total: Rp [ ]
0.5% history: first year [ ] | transition year [ ] | chose general rates [yes/no]
Method: 0.5% final | NPPN (notice filed [date]) | bookkeeping
Withholding credits: BP-21 total Rp [ ] | other slips Rp [ ]
PKP: registered | not required | registration overdue
Employees / payer duties: [ ]

Hand on to: bookkeeping | 0.5% final tax | individual income tax | company tax |
VAT and e-invoicing | payroll | withholding | entity choice | annual return assembly

Open points, refusals and conservative defaults: [list]
```

Related topics in this library: `id-pph-final-umkm` (0.5% final tax), `id-income-tax` (general rates and NPPN), `id-corporate-tax`, `id-withholding`, `id-payroll-pph21`, `indonesia-vat`, `id-einvoice-coretax`, `id-bookkeeping`, `id-formation`, `id-tax-optimization`, `id-return-assembly`.

This Guide is information, not tax advice. Rules change; check the current DJP text before filing, and have a qualified Indonesian tax professional (Konsultan Pajak) check the return before it is submitted on Coretax.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
