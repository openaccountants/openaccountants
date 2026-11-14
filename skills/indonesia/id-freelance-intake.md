---
name: id-freelance-intake
description: >
  Entry point for Indonesian calendar-2026 resident freelancer, sole-trader and
  single-founder-company tax work. Collect entity, residence, actual activity,
  owner/household turnover, elections, NPPN notice, withholding, VAT and filing
  facts, then route to the correct Indonesian method. Trigger on freelance tax,
  pekerjaan bebas, UMKM, PT Perorangan, SPT Tahunan and Indonesian tax intake.
  Never route Indonesia income tax to the similarly named US Idaho skill.
jurisdiction: ID
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
version: "2.0"
category: international
type: filing-howto
---
# Indonesia: freelancer and small-business intake v2.0

Tax year 2026 (calendar year), with a short section on the tax year 2025 return that was due on 31 March 2026. Operative official Indonesian sources were read on 14 November 2026; exact unresolved items are named below. Residence, business eligibility and annual filing are separate tests.

## Scope

This skill is the first step for an Indonesian tax resident individual who earns money outside a job: a freelancer or professional (pekerjaan bebas), a trader or service business run in their own name (including a trade name, Usaha Dagang), an online seller, or the founder of a single-founder company (PT Perorangan). It decides:

- whether the person is in scope at all (residency, entity);
- which income tax method applies for 2026: the 0.5% final tax on turnover, the deemed-profit norm (NPPN) with simple records, or full bookkeeping with general rates;
- whether clients must withhold PPh 21 from the person's fees, and what to do with the withholding slips;
- whether VAT registration (PKP) is required;
- what the annual return (SPT Tahunan) needs, where and when it is filed, and what happens if it is late;
- which specialist topics to hand on to (payroll, withholding, VAT, bookkeeping, company tax).

Out of scope: non-residents and part-year residents, corporate groups, and anything needing audited accounts. Those are referred (see "When to refuse or refer").

Key law behind this skill: the Income Tax Law (UU PPh) as amended by UU 7/2021 (HPP); PP 55/2022 on income tax adjustments, as amended by PP 20/2026 (in force 22 April 2026); PMK 164/2023 on the 0.5% regime and PKP reporting; PMK 168/2023 on PPh 21; PER-17/PJ/2015 on NPPN; PMK 81/2024 on Coretax; PMK 131/2024 on VAT from 2025 ([DJP on PMK 164/2023](https://www.pajak.go.id/id/peraturan/tata-cara-pengenaan-pajak-penghasilan-atas-penghasilan-dari-usaha-yang-diterima-atau); [DJP juklak PMK 168/2023](https://www.pajak.go.id/id/peraturan/petunjuk-pelaksanaan-pemotongan-pajak-atas-penghasilan-sehubungan-dengan-pekerjaan-jasa-1); [DJP on PMK 81/2024](https://pajak.go.id/en/node/113110); [DJP on PMK 131/2024](https://jdih.kemenkeu.go.id/api/download/f128868e-3cf6-4596-8407-c34eeca0e7be/2024pmkeuangan131.pdf)).

## What changed in 2026 (read this first)

PP 20/2026 changed the 0.5% final tax regime from 22 April 2026. The rate and ceiling did not change; who may use it, and how turnover is counted, did ([Official operative rule](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0); [PP 20/2026](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0)).

- **No more 7-year limit for individuals.** Article 59 of PP 55/2022 is deleted for individuals and single-founder PT Perorangan. They may use the 0.5% rate for as long as they meet the criteria, or until they choose general rates ([PP 20/2026](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0)).
- **Transition for people whose period had ended.** An individual whose 7 years ended in 2024 may use 0.5% for tax years 2025 and 2026. An individual or PT Perorangan whose period ended in 2025 may use it for tax year 2026, in each case only if they meet the PP 55/2022 criteria ([PP 20/2026](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0)).
- **Fewer eligible entities.** Only individuals, single-founder PT Perorangan and cooperatives are subjects. A CV, firma, ordinary PT or village enterprise (BUMDes) newly registered cannot use 0.5%; those registered before PP 20/2026 keep it until their existing period ends ([PP 20/2026](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0)). A DJP staff article states that under PP 55/2022 that period was 3 years for a PT and 4 years for a CV, firma or BUMDes ([Official operative rule](https://www.pajak.go.id/peraturan/penyesuaian-pengaturan-di-bidang-pajak-penghasilan)).
- **Turnover is counted wider.** The Rp4.8 billion test now adds all gross income from business and from pekerjaan bebas, whether taxed finally or not, including foreign turnover.
- **Household aggregation:** The actual amended arts. 57-58 and explanation confirm owner/company aggregation and PH/MT spouse/company aggregation for the ceiling; the explanation includes the minor child. It is no longer left to an unverified opinion article. Record all relevant preceding-year business/professional turnover and distinguish individual calculations from the eligibility aggregation. An aggregated-ceiling exit or general-rate election can prevent later return under amended art. 57(4). [PP 20/2026 amended arts. 57-58 and explanation](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0).
- **Pekerjaan bebas list made explicit.** Content creators (influencers, selebgram, bloggers, vloggers), painters, sculptors and "other artists" are named. A DJP staff article says this confirms, rather than changes, the old exclusion ([Official operative rule](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0)).
- **Specified end-of-2026 transition:** Art. II(1)(f) applies only to previously qualifying taxpayers newly excluded by the professional-company or owner/company-aggregation provisions identified there. It is not a blanket concession for every person who fails any criterion. Preserve the exact earlier eligibility and transition entitlement. [PP 20/2026 art. II](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0).

Tax year 2025 was the first annual return filed on Coretax DJP. The deadline stayed 31 March 2026, but DJP waived fines and interest for individuals who filed or paid by 30 April 2026 (KEP-55/PJ/2026) ([Official operative rule](https://www.pajak.go.id/en/node/119459)).

## Ask the client first

Read the existing case, intake and documents first; ask only for facts not already established. Use plain words and add the Indonesian term in brackets the first time.

- **Residency in 2026:** Establish whether the person lives in Indonesia, is present more than 183 days in any twelve months, or is present during the tax year with an intention to reside. These are alternatives, not a citizenship test. Record dates, residence evidence and any treaty/part-year issue; this intake's ordinary full-year route is not sufficient for disputed or split residence. [Income Tax Law art. 2(3)(a)](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf).
- **What you do.** Describe the work. Is it a profession or a personal skill you sell (doctor, lawyer, accountant, consultant, architect, notary, translator, writer, researcher, trainer, speaker, artist, musician, presenter, content creator, insurance agent, broker or finder of customers)? Or is it trading, making goods or running a service business?
- **Entity.** Do you invoice in your own name, under a trade name, through a PT Perorangan, or through a CV, firma or PT?
- **Gross turnover.** Your total gross receipts for 2025 and your expected total for 2026, from all business and professional work, including income earned abroad.
- **Household.** Are you married? Do you file as one family unit, or separately (separate property, PH; or wife filing on her own, MT)? What are your spouse's and minor children's business or professional receipts, and does either of you own a PT Perorangan?
- **Your history with the 0.5% rate.** Have you ever paid the 0.5% (or earlier 1%) final tax? From which year? Did you ever notify DJP that you chose general rates? ([DJP on the earlier rates](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0))
- **NPPN notice.** Did you file a notice to use the deemed-profit norm (NPPN) for 2026 by 31 March 2026? Do you keep full books (pembukuan) or only simple records (pencatatan)?
- **Withholding slips.** Did clients withhold PPh 21 or PPh 23 from your fees? Do you have the slips (bukti potong, for example BP-21)? Did you give any client a UMKM certificate (surat keterangan) or a statement that your turnover is under Rp500 million (surat pernyataan)?
- **VAT.** Are you registered for VAT (PKP)? Did your turnover go above Rp4.8 billion in any book year?
- **Staff and payments you make.** Do you pay employees, pay other freelancers, rent premises, or pay suppliers abroad?
- **Coretax.** Is your Coretax DJP account active, and have you created your authorisation code or electronic certificate (kode otorisasi / sertifikat elektronik)?
- **Family status for PTKP.** Single or married, and how many dependants (at most three count)?

## The method, step by step

1. **Confirm residence and subjective period.** Apply all art. 2(3)(a) alternatives and the actual start/end facts. Arrival during a year is not resolved by counting only calendar-year days or calling every foreign national non-resident. This full-year workflow refers treaty and part-year cases. [Income Tax Law arts. 2-2A](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf).
2. **Confirm registration.** Resident individuals use mapped NIK as NPWP; non-resident individuals, entities and government institutions also have sixteen-digit NPWP formats. A national identifier alone does not establish tax liability or successful registration. Obtain current tax profile, NITKU and actual KLU activity without inventing a code. [DJP identifier launch](https://www.pajak.go.id/index.php/id/siaran-pers/peluncuran-layanan-perpajakan-berbasis-nik-sebagai-npwp-npwp-16-digit-dan-nitku).
3. **Split the income into types.** Put every receipt into one of: employment; pekerjaan bebas (professional or personal-skill services); business (trade, production, other services); income already taxed finally under its own rule (for example construction services); passive income. Mixed earners keep separate records for each type.
4. **Test the wide ceiling and connected taxpayers.** For the preceding tax year, aggregate business and professional turnover, final/non-final and domestic/foreign, before discounts; apply owner/all-founded-company and PH/MT spouse/company rules plus the minor-child explanation. Income excluded from the monthly tax base can still count toward eligibility. Apply current-year crossing and exact art. II transitions separately; a universal mid-year switch or universal grace year is wrong. Check the permanent-exit provisions, not just next year's own turnover. [PP 20/2026 amended arts. 56-58 and art. II](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0); [PP 55/2022 art. 61](https://www.pajak.go.id/peraturan/penyesuaian-pengaturan-di-bidang-pajak-penghasilan).
5. **Choose the method for each income type.**
   - Pekerjaan bebas income: never the 0.5% rate. Use NPPN if gross is less than Rp4.8 billion and the notice was filed in time; otherwise full bookkeeping ([Official operative rule](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0)).
   - Business income of an eligible individual: 0.5% final on gross monthly turnover, unless the person has notified DJP that they chose general rates. For 2026, continue an earlier entitlement only under the precise applicable art. II transition; professional-company/owner-aggregation transition is not a blanket waiver. If general rates apply, use NPPN (if notified and gross is less than Rp4.8 billion) or full bookkeeping.
   - PT Perorangan: 0.5% only if single-founder, not delivering pekerjaan-bebas-type services, and the combined turnover test is met; otherwise the corporate return at general rates (see the company tax Guide).
6. **Apply the 0.5% regime correctly (if used).** Tax is 0.5% of the applicable monthly gross received or accrued before discounts, settled by permitted self-payment or collection, with ordinary self-payment due on the following month's fifteenth. An individual pays nothing on the first Rp500 million of turnover in the tax year, counted cumulatively from January ([Official operative rule](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0); [DJP on PMK 81/2024](https://pajak.go.id/en/node/113110)). Where PMK 164 arts. 7-8 actually apply, withholding/collection is reconciled with self-payment using the certificate and transaction exceptions; an individual with turnover under Rp500 million gives a statement (surat pernyataan) so that nothing is withheld ([DJP](https://www.pajak.go.id/id/peraturan/tata-cara-pengenaan-pajak-penghasilan-atas-penghasilan-dari-usaha-yang-diterima-atau)).
7. **Apply NPPN correctly (if used).** Net income = NPPN percentage for the KLU and region x gross receipts. No expenses and no loss carry-forward are deducted on top ([Official operative rule](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0)). Then subtract PTKP and apply the Art. 17 rates.
8. **Collect the withholding credits.** Gather every BP-21 (PPh 21 on fees to a non-employee, Bukan Pegawai) and any other slips. Non-final withholding is a credit against the annual tax. 0.5% final tax withheld by a client is a payment of that final tax, not a credit against tax at general rates ([DJP](https://www.pajak.go.id/id/peraturan/tata-cara-pengenaan-pajak-penghasilan-atas-penghasilan-dari-usaha-yang-diterima-atau)). On Coretax, slips issued by withholders pre-fill the return ([DJP](https://pajak.go.id/en/node/113110)).
9. **Plan ordinary-rate instalments.** Under art. 25, prior-year tax less eligible PPh 21/22/23 and permitted foreign tax, divided by the relevant year/part-year months, supplies the ordinary base. Do not subtract prior instalments again. OPPT has a distinct 0.75%-of-prescribed-monthly-turnover rule; ordinary new-taxpayer nil instalments and reorganisations have their own rules. PMK 164 art. 16 also addresses first ordinary-rate periods after final tax. Obtain the actual category and history before computing. [Income Tax Law art. 25](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf); [PMK 81 arts. 226-237](https://pajak.go.id/en/node/113110); [PMK 164 art. 16](https://www.pajak.go.id/id/peraturan/tata-cara-pengenaan-pajak-penghasilan-atas-penghasilan-dari-usaha-yang-diterima-atau).
10. **Check VAT separately.** Above the statutory small-business turnover limit, PMK 164 art. 17 requires reporting for PKP by book-year end, with ordinary duties from the first period of the following book year under art. 18; earlier election and late-registration treatment are separate. These PKP reporting provisions are not limited to taxpayers paying final turnover tax. Below the limit, voluntary registration is possible. Obtain the actual effective status and supply category. [PMK 164 arts. 17-19](https://www.pajak.go.id/id/peraturan/tata-cara-pengenaan-pajak-penghasilan-atas-penghasilan-dari-usaha-yang-diterima-atau).
11. **Check duties as a payer.** Establish whether the actual payer/category and transaction impose withholding: private household payments are not automatically business-agent obligations. Route employment/non-employee fees through `id-payroll-pph21`; analyse other supplier/rental/non-resident payments separately. Protected `id-withholding` remains unchanged and some older deadlines/VAT assumptions conflict with the laws read here, so do not copy its figures blindly. [PMK 168 art. 2](https://www.pajak.go.id/id/peraturan/petunjuk-pelaksanaan-pemotongan-pajak-atas-penghasilan-sehubungan-dengan-pekerjaan-jasa-1); [PMK 81 art. 94](https://pajak.go.id/en/node/113110). Not yet confirmed: the registration deadline specific to this taxpayer's commencement/status and any transaction-specific withholding outside this method.
12. **Prepare annual filing.** For calendar 2026, the ordinary individual annual deadline is 31 March 2027. Pay any annual balance BEFORE submitting and not beyond the applicable deadline; valid extension and specific relief need their own evidence. Confirm the actual return and supported channel under PER-3/PJ/2026. This method never creates a live account, certificate, payment or filing. [KUP art. 3](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf); [PMK 81 art. 95](https://pajak.go.id/en/node/113110); [PER-3/PJ/2026 arts. 2-8](https://www.pajak.go.id/id/peraturan/tata-cara-penyampaian-penerimaan-dan-pengolahan-surat-pemberitahuan-0).
13. **Record open points and hand off.** Write down every assumption and every item that needs a Konsultan Pajak.

## Rates, bands and thresholds

| Item | Figure | Applies to | Source |
| --- | --- | --- | --- |
| Final tax on gross turnover (eligible individual, PT Perorangan, cooperative) | 0.5% of monthly gross turnover | 2026 (unchanged by PP 20/2026) | [Official operative rule](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0) |
| Ceiling for the 0.5% regime | turnover not above Rp4.8 billion (Rp4.800.000.000) in one tax year | 2026 | [PP 20/2026](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0) |
| Turnover not taxed under the 0.5% regime | first Rp500 million a year, individuals only | 2026 | [Official operative rule](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0) |
| Payment of the 0.5% tax | by the 15th of the following month | from 2025 (PMK 81/2024) | [DJP on PMK 81/2024](https://pajak.go.id/en/node/113110) |
| Old time limits (PP 55/2022, now deleted for individuals and PT Perorangan) | 7 years individual; 4 years PT Perorangan, CV, firma, BUMDes, cooperative; 3 years PT | periods that began before 22 April 2026 | [Official operative rule](https://www.pajak.go.id/peraturan/penyesuaian-pengaturan-di-bidang-pajak-penghasilan); [PP 20/2026](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0) |
| Cooperative time limit (kept) | 4 tax years from registration | 2026 | [PP 20/2026](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0) |
| NPPN available if gross is | less than Rp4.8 billion a year | 2026 | [DJP](https://www.pajak.go.id/index.php/id/peraturan/norma-penghitungan-penghasilan-neto) |
| NPPN notice deadline | within the first 3 months of the tax year (31 March 2026 for 2026; 31 March 2027 for 2027) | 2026 and 2027 | [Official operative rule](https://www.pajak.go.id/index.php/id/peraturan/norma-penghitungan-penghasilan-neto) |
| NPPN percentage, example: computer programming (KLU 62010), general practice (KLU 86201) | 50% in every region | PER-17/PJ/2015 table, still in use in 2026 | [PER-17/PJ/2015 Lampiran I](https://www.pajak.go.id/sites/default/files/2019-03/Lampiran%201_PER%20-%2017.PJ_.2015.pdf) |
| PPh 21 on fees to a non-employee (Bukan Pegawai) | 50% of gross x Art. 17 rates | from 1 January 2024 (PMK 168/2023) | [DJP juklak PMK 168/2023](https://www.pajak.go.id/id/peraturan/petunjuk-pelaksanaan-pemotongan-pajak-atas-penghasilan-sehubungan-dengan-pekerjaan-jasa-1) |
| PPh 26 on services by a non-resident individual | 20% final, or treaty rate | from 1 January 2024 | [DJP juklak PMK 168/2023](https://www.pajak.go.id/id/peraturan/petunjuk-pelaksanaan-pemotongan-pajak-atas-penghasilan-sehubungan-dengan-pekerjaan-jasa-1) |
| Art. 17 rates for individuals | 5% to Rp60 million; 15% over Rp60 million to Rp250 million; 25% over Rp250 million to Rp500 million; 30% over Rp500 million to Rp5 billion; 35% over Rp5 billion | from tax year 2022, unchanged in 2026 | [Official operative rule](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| PTKP (non-taxable allowance) | Rp54,000,000 self; plus Rp4,500,000 if married; plus Rp4,500,000 per dependant, at most 3 | 2026 | [Official operative rule](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| PKP (VAT) registration | Turnover above Rp4.8 billion; report by book-year end, ordinary obligations from the following book-year first period, subject to early/late routes | 2026, independent of final-income-tax choice | [PMK 164 arts. 17-19](https://www.pajak.go.id/id/peraturan/tata-cara-pengenaan-pajak-penghasilan-atas-penghasilan-dari-usaha-yang-diterima-atau) |
| VAT | Nominal 12%; ordinary non-luxury mechanism uses 11/12 of price, computed effective 11%. Separately regulated bases/rates and exemptions are not overridden | Calendar 2026 with actual supply/category established | [PMK 131/2024 arts. 2-4](https://jdih.kemenkeu.go.id/api/download/f128868e-3cf6-4596-8407-c34eeca0e7be/2024pmkeuangan131.pdf) |
| Annual return deadline (individual) | 3 months after the tax year: 31 March 2027 for tax year 2026 | 2026 | [Official operative rule](https://www.pajak.go.id/id/peraturan/tata-cara-penyampaian-penerimaan-dan-pengolahan-surat-pemberitahuan-0) |
| Late annual return (individual) | fine of Rp100,000 | 2026 | [Official operative rule](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Residency test | present more than 183 days in 12 months (or living in Indonesia) | 2026 | [UU PPh on DJP](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |

At-least or more-than matters here. The 0.5% regime is for turnover **not above** Rp4.8 billion; NPPN is for gross **less than** Rp4.8 billion; PKP registration is required when turnover is **above** Rp4.8 billion. A person with exactly Rp4.8 billion can use 0.5% but, on the printed wording, not NPPN.

## Boundary and exception table

| Situation | Treatment | Source |
| --- | --- | --- |
| Profession or personal-skill service (doctor, lawyer, accountant, consultant, architect, notary, PPAT, appraiser, actuary and similar experts; musicians, presenters, actors, models, painters, sculptors, content creators, other artists; athletes; advisers, teachers, trainers, speakers, moderators; writers, researchers, translators; advertising agents; project supervisors; brokers and finders of customers; street sales agents; insurance agents; multi-level marketing distributors) | Pekerjaan bebas. Never 0.5%; NPPN or bookkeeping; clients withhold PPh 21 as Bukan Pegawai | [PP 20/2026](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0); [DJP juklak PMK 168/2023](https://www.pajak.go.id/id/peraturan/petunjuk-pelaksanaan-pemotongan-pajak-atas-penghasilan-sehubungan-dengan-pekerjaan-jasa-1) |
| Trading, production, online selling, a service run as a business | Business income. 0.5% if eligible; otherwise NPPN or bookkeeping | [Official operative rule](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0) |
| Unclear whether profession or business, including a developer/designer | Keep actual activity and organisation unresolved; show conditional methods but no taxpayer-specific final-regime conclusion | [PP 20/2026 amended art. 56 and explanations](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0) |
| Both profession and business | Separate records. Business part may use 0.5%; profession part uses NPPN or books. Both count toward the Rp4.8 billion test | [PP 20/2026](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0) |
| Income already taxed finally under its own rule (for example construction services) | Stays under that rule, but its turnover still counts toward the Rp4.8 billion test | [PP 20/2026](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0) |
| Married, one family unit (joint number) | Spouses' income is combined under the general rules | [Official operative rule](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0) |
| Married, PH or MT | The amended turnover aggregation and minor-child explanation apply to eligibility; separate taxpayer calculations and allowance rules still require their own analysis | [PP 20/2026 amended arts. 57-58 and explanations](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0); [PMK 164 art. 6](https://www.pajak.go.id/id/peraturan/tata-cara-pengenaan-pajak-penghasilan-atas-penghasilan-dari-usaha-yang-diterima-atau) |
| PT Perorangan set up to sell a pekerjaan-bebas-type service (for example a tax consultant's own PT) | Not eligible for 0.5% | [PP 20/2026](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0) |
| CV, firma, ordinary PT, BUMDes registered on or after 22 April 2026 | Not eligible for 0.5%; general corporate rules | [PP 20/2026](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0) |
| Entity registered before 22 April 2026 (other than PT Perorangan and cooperatives) | Keeps 0.5% until its PP 55/2022 period ends | [PP 20/2026](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0) |
| Individual who chose general rates | Notice by the end of a tax year; general rates apply from the next year. A new registrant may choose at registration | [DJP](https://www.pajak.go.id/id/peraturan/tata-cara-pengenaan-pajak-penghasilan-atas-penghasilan-dari-usaha-yang-diterima-atau) |
| Missed the NPPN notice | Treated as choosing bookkeeping for that year | [DJP](https://www.pajak.go.id/index.php/id/peraturan/norma-penghitungan-penghasilan-neto) |
| Once using books or missed notice | Keep actual notice/election history and apply consistency/change-approval rules; a software assumption or missing paper copy does not establish that a notice was never filed | [Income Tax Law art. 14; KUP art. 28](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf); [PER-17 arts. 1-2](https://www.pajak.go.id/index.php/id/peraturan/norma-penghitungan-penghasilan-neto) |
| Books or records not kept or not shown at audit | DJP computes net income using NPPN | [DJP](https://www.pajak.go.id/index.php/id/peraturan/norma-penghitungan-penghasilan-neto) |
| Turnover under Rp500 million on the 0.5% regime | No tax, but the annual return must still be filed | [DJP](https://www.pajak.go.id/id/peraturan/tata-cara-pengenaan-pajak-penghasilan-atas-penghasilan-dari-usaha-yang-diterima-atau) |
| Bribes and gratuities, including to foreign public officials | Never deductible (new art. 20A) | [PP 20/2026](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0) |

## Worked cases

**Case 1: online seller on the 0.5% regime, tax year 2026.** Individual, not married, sells goods online, no profession income, turnover Rp100 million every month (Rp1.2 billion for 2026), no spouse or PT Perorangan. Turnover is not above Rp4.8 billion, so 0.5% applies only with all earlier election/activity/aggregation criteria established. January to May cumulative turnover is Rp500 million, which is not taxed. From June each month's Rp100 million is taxed: 0.5% x Rp100,000,000 = Rp500,000, paid by the 15th of the next month (June tax by 15 July 2026). Total for 2026: 0.5% x (Rp1,200,000,000 - Rp500,000,000) = Rp3,500,000. The annual return is still filed by 31 March 2027. ([Official operative rule](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0); [DJP on PMK 81/2024](https://pajak.go.id/en/node/113110))

**Case 2: general practitioner on NPPN, tax year 2026.** A GP (KLU 86201, pekerjaan bebas) with gross fees of Rp600 million in 2026, married with one child (PTKP K/1), filed the NPPN notice by 31 March 2026. Net income = 50% x Rp600,000,000 = Rp300,000,000. PTKP = Rp54,000,000 + Rp4,500,000 + Rp4,500,000 = Rp63,000,000. Taxable income = Rp237,000,000. Tax = 5% x Rp60,000,000 = Rp3,000,000, plus 15% x Rp177,000,000 = Rp26,550,000, total Rp29,550,000. Suppose the hospitals' BP-21 slips show Rp20,000,000 withheld (an assumed figure for illustration; use the real slips). Balance due (PPh 29) = Rp9,550,000, payable by 31 March 2027. Had the notice been missed, the GP would be treated as keeping books and must compute actual profit. ([PER-17/PJ/2015 Lampiran I](https://www.pajak.go.id/sites/default/files/2019-03/Lampiran%201_PER%20-%2017.PJ_.2015.pdf); [Official operative rule](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf); [DJP](https://www.pajak.go.id/index.php/id/peraturan/norma-penghitungan-penghasilan-neto))

**Case 3: PPh 21 on a one-off fee, 2026.** A company pays a freelance photographer an honorarium of Rp200 million. PPh 21 base = 50% x Rp200,000,000 = Rp100,000,000. Tax = 5% x Rp60,000,000 = Rp3,000,000 plus 15% x Rp40,000,000 = Rp6,000,000, total Rp9,000,000 withheld, with a BP-21 slip. The photographer credits Rp9,000,000 in the annual return. Since PMK 168/2023 the formula is a single, non-cumulative calculation per payment. ([Official operative rule](https://www.pajak.go.id/id/peraturan/petunjuk-pelaksanaan-pemotongan-pajak-atas-penghasilan-sehubungan-dengan-pekerjaan-jasa-1); [DJP juklak PMK 168/2023](https://www.pajak.go.id/id/peraturan/petunjuk-pelaksanaan-pemotongan-pajak-atas-penghasilan-sehubungan-dengan-pekerjaan-jasa-1))

**Case 4: household aggregation confirmed from the operative law and explanation.** Husband is a notary with Rp3 billion of fees in 2026; wife runs a boutique with Rp2 billion turnover on the 0.5% regime; their minor child earns Rp500 million as a child singer. They file separately. Combined turnover = Rp5.5 billion, above Rp4.8 billion, so the wife cannot use 0.5% in 2027 even though her own turnover is unchanged; also test amended art. 57(4)'s continuing exclusion. The husband and child's professional receipts do not enter the final business-tax base (pekerjaan bebas). ([Official operative rule](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0))

**Case 5: wide turnover test, 2026 turnover deciding 2027.** Trader with 2026 Rp2 billion trade turnover, Rp2.5 billion construction turnover (taxed under the construction final rule) and Rp1.5 billion as a paid speaker (general rates). Total Rp6 billion: from 2027 not eligible for 0.5% on the trade income, which is then taxed at general rates (any 2026 transitional entitlement must separately satisfy its exact art. II limb, rather than a universal grace-year assumption). With Rp1 billion construction instead, the total is Rp4.5 billion and the turnover ceiling alone is not breached, but eligibility still depends on elections, history and any permanent exclusion. ([PP 20/2026](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0))

**Case 6: freelancer registered for VAT.** Assume an ordinary taxable consulting supply with no exemption or separately prescribed basis/rate. A PKP consultant invoices a service of Rp12,000,000 in 2026. VAT = 12% x (11/12 x Rp12,000,000) = Rp1,320,000, the same as 11% of the price. ([DJP](https://jdih.kemenkeu.go.id/api/download/f128868e-3cf6-4596-8407-c34eeca0e7be/2024pmkeuangan131.pdf))

**Case 7: old period ended in 2024.** Retain the individual trader who started the earlier final-tax clock in 2018, with the former seven-year period ending in 2024, annual turnover Rp2 billion and no connected-taxpayer disqualification. Art. II expressly provides the stated 2025/2026 continuation subject to earlier criteria. Article 59 is now deleted, while amended art. 57 retains substantive eligibility and permanent-exit rules. Do not derive a universal 2027 right or refusal from the old seven-year clock alone: establish the actual amended entitlement, earlier general-rate election and transition facts. [PP 55 former arts. 59,69](https://www.pajak.go.id/peraturan/penyesuaian-pengaturan-di-bidang-pajak-penghasilan); [PP 20/2026 amended art. 57 and art. II](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0).

**Case 8: missed NPPN notice.** A freelance translator with gross fees of Rp400 million in 2026 did not file the NPPN notice by 31 March 2026. Translators are pekerjaan bebas, so 0.5% is not available. Without the notice the translator is treated as choosing bookkeeping for 2026 and must compute actual profit from books; Apply the actual books/records history and consistency/change rules rather than assume an unfiled notice from a missing copy. ([DJP](https://www.pajak.go.id/index.php/id/peraturan/norma-penghitungan-penghasilan-neto); [Official operative rule](https://www.pajak.go.id/id/peraturan/tata-cara-penyampaian-penerimaan-dan-pengolahan-surat-pemberitahuan-0))


### Recomputing the original seller and doctor cases

The seller case assumes eligibility, no earlier opt-out and all monthly receipts qualifying. The doctor's final annual credit is the explicitly supplied documented-slip input, not a fee-withholding calculation. Annual settlement is paid before submission. Sources: [PP 55 art. 60](https://www.pajak.go.id/peraturan/penyesuaian-pengaturan-di-bidang-pajak-penghasilan); [PMK 164 arts. 6-9](https://www.pajak.go.id/id/peraturan/tata-cara-pengenaan-pajak-penghasilan-atas-penghasilan-dari-usaha-yang-diterima-atau); [PER-17 annex I, KLU 86201](https://www.pajak.go.id/sites/default/files/2019-03/Lampiran%201_PER%20-%2017.PJ_.2015.pdf); [Income Tax Law art. 17](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf); [DJP PTKP table](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf).

```oa-check
name: Intake online seller monthly-to-annual check
inputs:
  turnover: 1200000000
  allowance: 500000000
  monthly_turnover: 100000000
  rate: 0.005
steps:
  - annual_base: max(turnover - allowance, 0)
  - annual_tax: annual_base * rate
  - monthly_tax_after_crossing: monthly_turnover * rate
  - seven_months: monthly_tax_after_crossing * 7
expected:
  annual_base: 700000000
  annual_tax: 3500000
  monthly_tax_after_crossing: 500000
  seven_months: 3500000
```

```oa-check
name: Intake GP NPPN and documented annual credits
inputs:
  fees: 600000000
  norm: 0.5
  self_allowance: 54000000
  married_addition: 4500000
  one_child: 4500000
  actual_credits: 20000000
steps:
  - norm_income: fees * norm
  - ptkp: self_allowance + married_addition + one_child
  - taxable: max(norm_income - ptkp, 0)
  - tax: min(taxable, 60000000) * 0.05 + max(taxable - 60000000, 0) * 0.15
  - balance: tax - actual_credits
expected:
  norm_income: 300000000
  ptkp: 63000000
  taxable: 237000000
  tax: 29550000
  balance: 9550000
```

## When to refuse or refer

Stop, say why in one sentence, and refer to a Konsultan Pajak (or an Akuntan Publik where audited accounts are needed) when:

- the person was not resident for the whole of 2026, arrived or left during the year, or claims non-resident or treaty status;
- the person is a foreign national who may qualify for special treatment of foreign-source income, or has treaty questions;
- the business is part of a group, has related-party dealings across borders, or needs audited financial statements;
- the household or company turnover is at or near Rp4.8 billion and the person wants to rely on 0.5% or NPPN (establish the exact preceding/current-year aggregate, legal boundary, history and transition before a taxpayer-specific conclusion: [Official operative rule](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0));
- the earlier final-tax clock and 2027 entitlement are disputed; analyse the amended eligibility/permanent-exit rules and exact transition, referring unresolved facts with the actual law;
- the classification between profession and business is disputed and material to the result;
- the person has an open audit, objection or tax assessment (SKP) for the years involved;
- the person wants to use a CV, firma or ordinary PT to reach the 0.5% rate (not available to new registrations from 22 April 2026: [PP 20/2026](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0));
- the facts suggest splitting turnover across family members or companies to stay under the ceiling (the PP 20/2026 anti-avoidance rules target this).

Conservative defaults when the facts are unclear:

- profession or business unclear: retain both classifications and request actual contracts/activity evidence; no affirmative final-regime conclusion;
- NPPN notice not shown: request the actual receipt/history; no NPPN conclusion until the notice and prior books status are established;
- household turnover unknown: do not rely on 0.5% for the next year until it is known;
- PTKP status unknown: obtain the actual family/status evidence; do not invent TK/0;
- Coretax access unknown: record readiness as unconfirmed, without creating or altering access.

## Filing and payment

**During 2026**

- 0.5% regime: pay each month's tax by the 15th of the next month ([DJP on PMK 81/2024](https://pajak.go.id/en/node/113110)).
- General rates: pay PPh 25 instalments by the 15th of the next month ([DJP on PMK 81/2024](https://pajak.go.id/en/node/113110)).
- PKP: VAT returns and payments monthly (see the VAT Guide).
- Payers of wages or fees: PPh 21/26 withheld is paid by the 15th of the next month ([DJP on PMK 81/2024](https://pajak.go.id/en/node/113110)).

**The annual return for tax year 2026**

- File the individual annual return (SPT Tahunan PPh Orang Pribadi) on Coretax DJP by 31 March 2027. Match the current individual return and its applicable attachments; old 1770/1770S/1770SS names are historical search terms, not certified 2026 field mappings ([Official operative rule](https://www.pajak.go.id/id/peraturan/tata-cara-penyampaian-penerimaan-dan-pengolahan-surat-pemberitahuan-0)).
- Before filing: activate Coretax and create the authorisation code or electronic certificate. Try the DJP simulator first if unsure.
- Pay any annual balance before submission and not beyond the applicable deadline; record payment and accepted-return evidence separately.
- The NPPN notice for the following year is also due by 31 March (for 2027, by 31 March 2027) through the applicable current DJP notification channel; the precise current screen/service identifier has not been confirmed ([Official operative rule](https://www.pajak.go.id/index.php/id/peraturan/norma-penghitungan-penghasilan-neto)).
- Late filing: fine of Rp100,000 for an individual ([Official operative rule](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf)).

**Tax year 2025 (returns filed in 2026)**

- The 2025 return was due 31 March 2026 on Coretax. Under KEP-55/PJ/2026, individuals who filed and/or paid between 1 April and 30 April 2026 have no fine or interest; DJP does not issue a tax bill (STP) for them, and where one was already issued the regional office removes the sanction ([Official operative rule](https://www.pajak.go.id/en/node/119459)).
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
- [ ] PTKP status evidenced; unresolved status explicitly flagged, not defaulted to TK/0.
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

Related topics in this library: `id-pph-final-umkm` (0.5% final tax), `id-bookkeeping` (NPPN/books evidence; the missing ordinary individual tax computation must be separately supplied), `id-corporate-tax`, `id-withholding`, `id-payroll-pph21`, `indonesia-vat`, `id-einvoice-coretax`, `id-bookkeeping`, `id-formation`, `id-tax-optimization`, `id-return-assembly`.

This skill is information, not tax advice. Rules change; check the current DJP text before filing, and have a qualified Indonesian tax professional (Konsultan Pajak) check the return before it is submitted on Coretax.


Routing correction: the old `id-income-tax` slug resolves to Idaho in the United States. Never load it for an Indonesian return. `id-bookkeeping` supports Indonesian records/NPPN; `id-payroll-pph21` supports employment withholding; neither replaces an independently documented full ordinary individual return computation where needed. `id-tax-optimization` remains held in another open PR and is not rewritten or certified by this intake.

## Sources

| Official source | Read for and date |
|---|---|
| [DJP consolidated Income Tax/KUP laws](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) | Income Tax arts. 2-2A,14,17,21,25 and KUP arts. 3,7,28: residence alternatives, method boundaries, brackets, instalments, filing and records. Read 2026-11-14. |
| [PP 20/2026](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0) | Amended arts. 56-58, deleted art. 59, art. 20A and art. II with explanations: professional activity, aggregation and precise transition, not opinion articles. Read 2026-11-14. |
| [PP 55/2022](https://www.pajak.go.id/peraturan/penyesuaian-pengaturan-di-bidang-pajak-penghasilan) | Arts. 59-63 and historical art. 69: earlier clocks, monthly turnover, individual allowance, crossing-year treatment and settlement. Read 2026-11-14. |
| [PMK 164/2023](https://www.pajak.go.id/id/peraturan/tata-cara-pengenaan-pajak-penghasilan-atas-penghasilan-dari-usaha-yang-diterima-atau) | Arts. 5-9,16-19: permanent election, payments/certificates, annual evidence and PKP reporting independently of final-tax choice. Read 2026-11-14. |
| [PER-17/PJ/2015](https://www.pajak.go.id/index.php/id/peraturan/norma-penghitungan-penghasilan-neto) | Arts. 1-9, strict NPPN threshold, timely notice, books/records and assessment norms. Read 2026-11-14. |
| [PER-17 annex I](https://www.pajak.go.id/sites/default/files/2019-03/Lampiran%201_PER%20-%2017.PJ_.2015.pdf) | Actual KLU 62010 and 86201 rows and adjacent descriptions, all three regional norm columns. Read 2026-11-14. |
| [PMK 168/2023](https://www.pajak.go.id/id/peraturan/petunjuk-pelaksanaan-pemotongan-pajak-atas-penghasilan-sehubungan-dengan-pekerjaan-jasa-1) | Arts. 2-3,12-16,20-22: payer/recipient classifications, non-employee gross/base, resident/treaty boundary and evidence. Read 2026-11-14. |
| [DJP withholding book](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) | PTKP and statutory/TER tables, printed pages 39-42,46-48. Read 2026-11-14. |
| [PMK 81/2024](https://pajak.go.id/en/node/113110) | Arts. 94-95,100,226-237: deposits, annual pre-submission payment, holiday adjustment and ordinary/special instalments. Read 2026-11-14. |
| [PMK 131/2024](https://jdih.kemenkeu.go.id/api/download/f128868e-3cf6-4596-8407-c34eeca0e7be/2024pmkeuangan131.pdf) | Arts. 2-6: nominal VAT, ordinary non-luxury base and separately regulated scheme exclusion. Read 2026-11-14. |
| [PER-3/PJ/2026](https://www.pajak.go.id/id/peraturan/tata-cara-penyampaian-penerimaan-dan-pengolahan-surat-pemberitahuan-0) | Arts. 2-8: annual return periods, deadlines, extension and supported filing/receipt routes. Read 2026-11-14. |
| [DJP identifier launch](https://www.pajak.go.id/index.php/id/siaran-pers/peluncuran-layanan-perpajakan-berbasis-nik-sebagai-npwp-npwp-16-digit-dan-nitku) | Resident-individual NIK and other sixteen-digit NPWP/NITKU formats. Read 2026-11-14. |
| [Official KEP-55/2026 implementation notice](https://www.pajak.go.id/en/node/119459) | Historical individual tax-year-2025 payment/filing sanction relief through 30 April 2026, not a tax-year-2026 extension. Read 2026-11-14. |

Not yet confirmed: taxpayer-specific commencement registration deadline; actual current annual-return fields and notification service identifiers; disputed residence/activity/connected-party facts; ordinary individual computation where the old missing route was relied upon; special withholding/incentive/foreign-credit cases beyond this intake. A pending portal detail does not justify substituting another country's skill, a personal-opinion rule or invented taxpayer facts.
