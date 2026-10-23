---
name: pt-cross-border
description: "Portuguese cross-border tax for tax year 2026: tax residence under CIRS art. 16 (183 days, habitual home, split years from the first day of presence, leavers kept resident for the whole year, nationals moving to listed low-tax places); non-residents' Portuguese-source income (25% final withholding on salary, pensions and business income, 28% on capital income, 25% or 28% on rent); the art. 17-A and 72(15) options to use resident bands; the tax representative; company residence and the IRC exit tax in five yearly instalments (CIRC art. 83 and 84); outbound withholding (25%, 28%, 35%) and EU directive exemptions; forms 21-RFI to 24-RFI; the A1 certificate. Trigger on: non-resident Portugal tax, moving to Portugal mid-year, leaving Portugal, artigo 17-A, representante fiscal, exit tax IRC, Modelo 21-RFI. Out of scope: pt-foreign-source-treaties, pt-nhr-ifici, pt-irs-employees-investment, pt-income-tax, portugal-crypto-tax, pt-corporate-tax, pt-transfer-pricing."
jurisdiction: PT
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
verified_by: pending
---

# Portugal: cross-border tax, residence, non-residents, arriving and leaving (tax year 2026)

This skill answers four questions. Is the person or company resident in Portugal for 2026, and from which day? How does Portugal tax a non-resident's Portuguese income? What does a company pay when it moves its seat or assets out? What must a Portuguese payer withhold when it pays abroad, and how is treaty relief claimed?

Sibling skills, which this one links to and does not repeat:

- `pt-foreign-source-treaties`: foreign income of a Portuguese resident, the foreign tax credit (CIRS art. 81) and Anexo J. Tax year 2026.
- `pt-nhr-ifici`: the old NHR regime and IFICI (20% rate), the activity lists, the registration steps. This skill only runs the IFICI entry test for a new arrival.
- `pt-irs-employees-investment`: the 2026 IRS bands, the specific deductions and the resident computation. The band table below is copied from there and was re-read today.
- `pt-income-tax`: self-employed income (Category B). Tax year 2025.
- `portugal-crypto-tax`: crypto, including the deemed sale of crypto on loss of residence (CIRS art. 10(25), numbered art. 10(22) before Decreto-Lei 97/2026 renumbered it).
- `pt-corporate-tax`: IRC rates, the participation exemption on dividends paid to EU and treaty parents (CIRC art. 14(3)), payments on account.
- `pt-transfer-pricing`: related-party pricing, including the exit values of assets moved abroad.

The law is the IRS Code (CIRS), the IRC Code (CIRC), the General Tax Law (LGT) and the Tax Offences Regime (RGIT), read article by article on the Portal das Finanças on 2026-10-23.

## Who this applies to

**Individuals: the residence tests (CIRS art. 16(1) and (2)).** A person is resident for a year if, in that year, they:

- stayed in Portugal more than 183 days, consecutive or not, in any 12-month period starting or ending in that year; or
- stayed less, but had a home in Portugal on any day of that period, in conditions that suggest a present intention to keep and occupy it as their habitual residence; or
- on 31 December were crew of a ship or aircraft serving a Portuguese-resident entity; or
- held a public post abroad for the Portuguese State (including Members of the European Parliament, art. 16(13)).

A day of presence is any day, full or part, that includes a night spent in Portugal (art. 16(2)). Residence is tested for each spouse separately (art. 16(5)).

**Part-year residence (split year).** A person who meets the 183-day or home test becomes resident from the first day of their stay. The exception: if they were resident on any day of the previous year, they are resident from 1 January (art. 16(3)). Residence ends on the last day of presence (art. 16(4)). For each part of the year, residents are taxed on worldwide income and non-residents only on Portuguese income (art. 15(1) to (3)). A person with two residence statuses in one year files one return for each (art. 57(6)).

**Leavers who stay resident for the whole year.** Two rules override the split:

- A person who leaves is resident for the whole year if they spent more than 183 days in Portugal that year and, after leaving, earned income in the same year that would have been taxable in Portugal had they stayed resident (art. 16(14)). This does not apply if they show that income is taxed by a similar income tax in another EU or EEA state (EEA only with exchange of information), or in another state at a rate of at least 60% of the Portuguese rate (art. 16(15)).
- A person who becomes resident again in the year after the year they left is treated as resident for the whole of the year they left (art. 16(16)).

**Portuguese nationals moving to a listed low-tax place.** A Portuguese national who moves their tax residence to a country on the government's list of clearly more favourable regimes stays resident in the year of the move and the next four years, unless they prove a good reason, such as temporary work for a Portuguese employer (art. 16(6)). It stops once they become resident somewhere not on the list (art. 16(7)).

**Non-residents** are taxed only on income obtained in Portugal (art. 15(2)). Art. 18(1) lists it. The main items: work done in Portugal or paid by a Portuguese payer; directors' fees from Portuguese companies; royalties and technical assistance paid by Portuguese payers; business income of a Portuguese permanent establishment; services done or used in Portugal and paid by a Portuguese payer (not transport, telecoms or finance); income from and gains on Portuguese property; gains on shares of Portuguese companies, and on foreign shares deriving more than 50% of their value from Portuguese property in the previous 365 days; pensions paid by Portuguese payers.

**Companies.** A company is resident if its registered office (sede) or place of effective management (direção efetiva) is in Portugal (CIRC art. 2(3)). Residents pay IRC on worldwide income (CIRC art. 4(1)); non-residents only on Portuguese income, which is the income of a Portuguese permanent establishment plus the items in art. 4(3) (property, Portuguese shares, royalties, interest, directors' fees and services paid by Portuguese payers, subject to the services carve-out in art. 4(4)).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Non-resident, salary and all business and professional income from Portuguese sources | 25% final withholding | 2026 | CIRS art. 71(4)(a): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs71.aspx |
| Non-resident, pensions | 25% final withholding, on the pension less the art. 53 deduction | 2026 | CIRS art. 71(4)(c) and (8) |
| No withholding on monthly salary or services up to the minimum wage, single payer, written declaration | 25% only on the excess | 2026 | CIRS art. 71(5) and (6) |
| Non-resident, salary or pension not withheld | 25% autonomous rate | 2026 | CIRS art. 72(6)(b): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs72.aspx |
| Non-resident with a Portuguese permanent establishment | 25% autonomous rate on its income | 2026 | CIRS art. 72(6)(a) |
| Non-resident individual, dividends and interest from Portuguese payers | 28% final withholding | 2026 | CIRS art. 71(1)(a) |
| Non-resident individual, rent from residential leases | 25% autonomous rate | 2026 | CIRS art. 72(2) |
| Residential leases for permanent housing of 5 to under 10 years / 10 to under 20 years / 20 years or more | 25% less 10 / 15 / 20 points (the rule is not limited to residents) | 2026 | CIRS art. 72(3) to (5) |
| Non-resident individual, other rent (shops, offices) | 28% autonomous rate | 2026 | CIRS art. 72(1)(e) |
| Non-resident individual, other income not withheld | 28% autonomous rate | 2026 | CIRS art. 72(1)(b) |
| Non-resident individual, gain on Portuguese property (not through a permanent establishment) | 50% of the gain is included and aggregated; the art. 68 rate is set on all income, foreign included. The old 28% rate of art. 72(1)(a) is repealed | 2026 | CIRS art. 43(2)(b), art. 22(3)(a) and (10): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs22.aspx |
| Capital income paid to a holder in a listed low-tax place, or to an account for unidentified third parties | 35% | 2026 | CIRS art. 71(17); CIRC art. 87(4)(h) and (i): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87.aspx |
| Non-resident company without a permanent establishment, general IRC rate | 25% | 2026 | CIRC art. 87(4) |
| IRC withholding, general rate / directors' fees | 25% / 21.5% | 2026 | CIRC art. 94(4): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc94.aspx |
| IRS withholding on Category F rent paid by a payer with organised accounts | 25% | 2026 | CIRS art. 101(1)(e): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs101.aspx |
| Resident IRC rate (exit gains are taxed at this rate) | 19% for periods starting in 2026; 18% in 2027; 17% from 2028 | 2026 | CIRC art. 87(1) and Lei 64/2025 art. 3 (note on the AT page) |
| Art. 17-A option: Portuguese income as a share of worldwide income | At least 90% | 2026 | CIRS art. 17-A(1): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs17a.aspx |
| IRS bands used for the art. 17-A, art. 72(15) and art. 71(11) options | 12.50% to 48% (first band up to EUR 8,342; band 3 to 17,838 at 21.20%; band 6 to 43,090 at 34.90%) | 2026 | CIRS art. 68(1), wording of Lei 73-A/2025: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs68.aspx |
| Category A specific deduction | 8.54 x IAS = EUR 4,587.09, or compulsory social security if higher | 2026 | CIRS art. 25(1)(a) and (2); IAS EUR 537.13, Portaria 480-A/2025/1: https://files.diariodarepublica.pt/1s/2025/12/25001/0000200002.pdf |
| IFICI special rate on net Category A and B income from a qualifying activity | 20% for 10 consecutive years | 2026 | EBF art. 58-A(2): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/bf_rep/Pages/ebf58a.aspx |
| IFICI look-back | Not resident in any of the 5 previous years | 2026 | EBF art. 58-A(1) |
| Leaver kept resident for the whole year | More than 183 days in the year, plus Portuguese-taxable income after leaving | 2026 | CIRS art. 16(14): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs16.aspx |
| Leaver test: foreign tax at least this share of the Portuguese tax (non-EU/EEA) | 60% | 2026 | CIRS art. 16(15)(b) |
| National moving to a listed low-tax place | Resident in the year of the move and 4 more years | 2026 | CIRS art. 16(6) |
| IRC exit tax, EU/EEA move | Pay in full, or in 5 equal yearly instalments with interest at the late-payment rate | 2026 | CIRC art. 83(2)(c) and (3): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc83.aspx |
| Bank guarantee if AT fears non-collection | Tax plus 25% | 2026 | CIRC art. 83(4) |
| Parent-Subsidiary exemption on dividends to an EU, EEA or treaty parent | Holding at least 10%, held 1 year | 2026 | CIRC art. 14(3): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc14.aspx (detail in `pt-corporate-tax`) |
| Interest and Royalties Directive exemption | Direct holding of at least 25%, held 2 years without interruption | 2026 | CIRC art. 14(12) and (13)(b) |
| Treaty relief form (21-RFI) validity | At most 1 year from the certificate's issue, and it ends earlier on the last day of the tax period the certificate covers; the directive interest and royalties form (MOD. 01-DJR) lasts 2 years per contract | 2026 | CIRC art. 98(3): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc98.aspx; CIRS art. 101-C(4) for individuals; AT FAQ 4201, 4203, 5642 |
| A1 posting, EU rules | Up to 24 months; longer only by exception agreement | 2026 | Segurança Social, practical guide on postings from Portugal (Reg. 883/2004 art. 12): https://www.seg-social.pt/ptss/pssd/documento/cmc2117bg00thkl2y1r0iz21r |

## The taxable base

**Non-resident individuals: gross or net?** The 25% and 28% final withholding rates apply to gross income. Pensions are the exception: the art. 53 deduction comes off first (art. 71(8)). Rent is taxed on the net amount after the property costs allowed by art. 41 (see `pt-irs-employees-investment`). A non-resident gets none of the deductions from the tax (art. 78), unless they use art. 17-A.

**Option 1: art. 17-A (resident rules, 90% test).** A resident of another EU or EEA state (with exchange of information) whose Portuguese income is at least 90% of their worldwide income for the year may opt to be taxed as an unmarried resident (art. 17-A(1)). A married couple may opt for joint taxation if both live in the EU or EEA, the household's Portuguese income is at least 90% of its total, and both opt (art. 17-A(2)). How it works:

1. Compute taxable income under the normal rules, including the foreign income.
2. Find the art. 68 rate for that total.
3. Apply it to the Portuguese income that a resident would aggregate (art. 17-A(3)).
4. Take off the art. 78 deductions for the person's own expenses, if the state of residence does not already allow them (art. 17-A(4)).
5. Withholding at the non-resident rates still happens and counts as a payment on account (art. 17-A(5)).

The option is made in the Modelo 3, within the normal filing period, with proof of the conditions (art. 17-A(6)). AT may ask for documents, to be supplied within 30 days (art. 17-A(7)).

**Option 2: art. 72(15) and (16) (no 90% test).** An EU or EEA resident may opt to have the art. 72(1)(b) and (e) income and the art. 72(6) income taxed at the art. 68 rate that would apply to a resident, worked out on all their income, including foreign income. Art. 72(1)(e) is rent not covered by art. 72(2), that is non-residential rent. Art. 72(6) covers permanent establishment income and salary or pensions that were not withheld. Art. 72(15) does not list art. 72(2), so residential rent cannot use this option; it reaches the resident bands only through art. 17-A.

**Option 3: refund under art. 71(11) to (13).** An EU or EEA resident who suffered final withholding on salary, directors' fees, royalties, business income, services, pensions or performers' fees (art. 18(1)(a) to (d), (f), (m) and (o)) may ask for back the excess over the tax at the art. 68 bands on all their income. Costs directly tied to the Portuguese income, or the art. 25 deduction for salary, are deductible (art. 71(12)). The request goes to AT within two years counted from the end of the calendar year after the year the income arose. AT refunds by the end of the third month after the month the full proof is presented, or pays interest (art. 71(13)). AT informs the state of residence (art. 71(16)).

**Which to use.** The flat rate wins when the person's worldwide income puts them in the top bands. The resident rates win when Portuguese income is modest and foreign income is small. Example 1 runs the test.

**Arrivals: IFICI.** A person who becomes resident under art. 16(1) and (2), was not resident in any of the five previous years, and works in an activity in EBF art. 58-A(1) may be taxed at 20% on net Category A and B income from that activity for ten consecutive years, or may opt to aggregate (art. 58-A(2)). It is barred for anyone who has had NHR, chose the art. 12-A returning-resident regime, or used IFICI before (art. 58-A(10) and (12)). The activity list, the registration deadline (15 January of the year after arrival) and the review bodies are in `pt-nhr-ifici`.

**Companies leaving: the IRC exit tax (CIRC art. 83).** When a company with its seat or effective management in Portugal moves its residence abroad, the difference between the market value and the tax value of all its assets, whether or not shown in the accounts, is taxed in the period in which it ceases (art. 83(1)). Assets that stay in a Portuguese permanent establishment and keep contributing to its profit are left out (art. 83(10)). Earlier tax losses may then be used against that permanent establishment's profit (art. 83(12)). For a move to another EU state, or to an EEA state with a tax-recovery assistance agreement equivalent to Directive 2010/24/EU:

- the tax on the net gain may be paid in full with the return, or in five equal yearly instalments, starting in the period of the move (art. 83(2));
- instalments carry interest at the late-payment rate from the day after the normal payment deadline (art. 83(3));
- the option is made in the return for the period of cessation, with a form listing the assets; AT may ask for a bank guarantee of the tax plus 25% (art. 83(4));
- the first instalment is due by the return deadline, the others by the last day of May each year (art. 83(7)).

The instalments stop if the assets are sold, cease or leave the activity, or are moved outside the EU/EEA: the tax on those assets is due by the end of May of the next year (art. 83(16)(a) and (b), (17)(a)). If the company moves outside the EU/EEA, all remaining tax is due by the date of the move (art. 83(16)(c), (17)(b)). Insolvency or liquidation makes every instalment due (art. 83(16)(d), (19)). Gains on shareholdings may use the participation exemption of art. 51-C if its conditions are met at the date of cessation (art. 83(15)).

**Permanent establishments.** The same rules apply when a non-resident company's Portuguese permanent establishment stops trading, or when its assets are moved out of Portugal (CIRC art. 84(1)). The five-instalment option applies if the assets go to another EU or qualifying EEA state (art. 84(2)).

**Individuals leaving.** For individuals, the CIRS text read today has an exit charge only for crypto assets: loss of residence counts as a sale of crypto (CIRS art. 10(25), numbered art. 10(22) before Decreto-Lei 97/2026; the gain is market value at departure less cost, art. 43(12); see `portugal-crypto-tax`). Shares and other assets are not taxed on departure under the articles read for this skill.

## Deadlines and filing

| What | When | Source |
|---|---|---|
| Tell AT about a change of residence status (arriving or leaving) | Within 60 days of the change | LGT art. 19(5): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/lgt/Pages/lgt19.aspx |
| Modelo 3 for 2026 income (non-residents with Portuguese income not fully taxed by final withholding, art. 17-A elections, split-year returns) | 1 April to 30 June 2027 | CIRS art. 60(1): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs60.aspx |
| Split year | One return for each residence status | CIRS art. 57(6) |
| IFICI request for a 2026 arrival | By 15 January 2027 | Portaria 352/2024/1 art. 2(1), via `pt-nhr-ifici` |
| Withheld IRC paid to the State | By the 20th of the month after the deduction | CIRC art. 94(6) |
| Form 21-RFI (relief at source) in the payer's hands | By the deadline for paying over the tax that would have been withheld | CIRC art. 98(2) |
| Refund claim (forms 22-RFI to 24-RFI) where tax was withheld in full | Within 2 years from the end of the year the income arose; AT refunds within 1 year or pays interest | CIRC art. 98(7) and (9); CIRS art. 101-C(7) and (9) for individuals |
| Art. 71(11) refund of excess withholding (EU/EEA individuals) | Within 2 years from the end of the year after the income arose | CIRS art. 71(13) |
| IRC exit tax instalments | First with the return for the period of cessation; then by 31 May each year | CIRC art. 83(7) |

**The forms.** AT lists four treaty forms (FAQ 5635): **21-RFI** asks for full or partial relief from withholding at source; **22-RFI** asks for a refund of tax on share dividends and on interest from debt securities; **23-RFI** asks for a refund on royalties, and on dividends and interest not covered by 22-RFI; **24-RFI** asks for a refund on other income. The 21-RFI goes to the Portuguese payer. Forms 22-RFI to 24-RFI go to AT's international relations service (Direção de Serviços de Relações Internacionais) (FAQ 5637). Each needs a certificate of tax residence from the other state (CIRC art. 98(2)(a); for individuals CIRS art. 101-C(2)). A 21-RFI with its certificate is valid for at most one year from the certificate's issue and expires on the last day of the tax period the certificate covers (FAQ 4201, 4203). The Interest and Royalties Directive uses its own forms: MOD. 01-DJR for relief at source and MOD. 02-DJR for a refund (FAQ 5640). The Parent-Subsidiary exemption has no form: the payer needs, before paying, a declaration issued or authenticated by the parent's tax authority (CIRC art. 14(4); FAQ 5643). The payer must have the original paper, not an emailed copy (FAQ 5308). A payer who pays income to non-residents reports it on Modelo 30 (AT forms page).

**Tax representative and the NIF.** A non-resident with income subject to IRS, and a resident who leaves Portugal for more than six months, must appoint a representative living in Portugal (CIRS art. 130(1); LGT art. 19(6)). The appointment is made in the declaration that registers the tax number (NIF), or the start or change of activity, and the representative must sign to accept (CIRS art. 130(3)). It is optional for residents of the EU or EEA (art. 130(2); LGT art. 19(8)). Outside the EU and EEA it is also not needed if the person signs up for electronic notifications (the morada única digital, the Portal das Finanças notification service, or an electronic mailbox) (LGT art. 19(15)). Without a representative, AT does not send notices, and the person cannot exercise rights such as complaints and appeals (CIRS art. 130(4); LGT art. 19(7)). Non-resident companies with Portuguese income and no permanent establishment have the same rule (CIRC art. 126).

**Social security.** An employee posted from one EU state to another stays insured at home if the posting is expected to last up to 24 months. The employer asks the home institution for an A1 certificate before the posting starts (Reg. 883/2004 art. 12). Longer postings need an exception agreement between the two institutions. Someone working in two or more states needs an A1 under art. 13. Postings from Portugal are requested on Segurança Social Direta (Trabalho > Entrada, saída e destacamento de trabalhadores > Destacamento de trabalhadores). Contribution rates are in `pt-social-contributions` and `portugal-payroll`.

## Penalties and interest

- **Late or missing return:** fine of EUR 150 to EUR 3,750 (RGIT art. 116(1)). Source: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit116.aspx
- **Late tax-number update by an individual** (for example, not reporting a change of residence status and address): fine of EUR 75 to EUR 375 (RGIT art. 117(4)). Late start, change or cessation of activity declarations: EUR 300 to EUR 7,500 (art. 117(2)). Source: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit117.aspx
- **Payer withheld tax and did not pay it over:** fine from the amount due to twice that amount; if negligent, 15% to half the amount (RGIT art. 114(1) and (2)). The same fines apply to tax that should have been withheld and was not (art. 114(4)). Source: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit114.aspx
- **Payer applied treaty or directive relief without the proof on time:** the payer owes all the tax that should have been withheld (CIRC art. 98(5)). It can escape that liability, but not the fine, by later producing the proof (art. 98(6)).
- **Exit tax instalment missed:** all remaining instalments fall due at once and AT starts enforcement (CIRC art. 83(8)).
- **Interest:** compensatory interest (LGT art. 35) and late-payment interest (LGT art. 44), as set out in `pt-irs-employees-investment`. Exit tax instalments carry late-payment interest by law (CIRC art. 83(3)).

## Cross-border points

- **Treaties come first for withholding.** No Portuguese withholding, or a reduced rate, applies where a treaty gives Portugal no taxing right or a limited one, but only if the 21-RFI and the residence certificate reach the payer in time (CIRC art. 98(1) and (2); CIRS art. 101-C(1) to (3) for individuals). Relief at source can also come from domestic law, such as the CIRC art. 14 directive exemptions (art. 98(1)).
- **Dividends to companies.** Exempt under CIRC art. 14(3) for qualifying EU, EEA or treaty parents (10% for 1 year); otherwise 25% (art. 87(4)), or 35% to a listed low-tax place (art. 87(4)(i)). See `pt-corporate-tax` for the full conditions and the anti-abuse rule.
- **Interest and royalties to EU associated companies.** Exempt if the recipient is the beneficial owner, subject to tax without exemption, takes a listed legal form, and the 25% direct holding has been held for 2 years (CIRC art. 14(12) and (13)). Not available if third-country residents control the recipient, unless it is shown that tax reduction was not a main purpose (art. 14(15)(a)). An amount above arm's length does not get the exemption (art. 14(15)(b)). Swiss companies have the same relief (art. 14(16)). The directive form lasts 2 years per contract (art. 98(3)(a)).
- **Individuals moving out** stay liable in Portugal on Portuguese-source income after leaving (art. 15(2)). Check art. 16(14) before treating the year as split.
- **Residents' foreign income:** `pt-foreign-source-treaties`.
- **Transfer of assets between a head office and a permanent establishment** is valued at arm's length: `pt-transfer-pricing`.

## Worked examples

### Example 1: non-resident landlord, 25% flat rate or the art. 17-A option

Claire lives in France and is tax resident there. In 2026 she lets her Lisbon flat under a 3-year residential lease for EUR 14,400 gross. She pays EUR 1,400 of IMI and condominium charges, so net Category F income is EUR 13,000. Her tenant is a private individual, so nothing is withheld. Her only other income is a French pension of EUR 1,000.

1. **The 90% test.** Portuguese income is 14,400 / (14,400 + 1,000) = 93.5% of her total. That is at least 90%, so she can opt under art. 17-A. (The ratio is above 90% on net figures too.)
2. **Flat rate.** Residential rent of a non-resident: 25% x 13,000 = EUR 3,250.00 (art. 72(2)).
3. **Art. 17-A.** Under resident rules, residential rent is taxed at 25% unless the owner opts to aggregate it (art. 72(2) and (13)). The rate of art. 17-A(3) applies to income that a resident would aggregate, so Claire also ticks the aggregation option for her rent (see Not yet confirmed). Taxable income includes foreign income. Her pension of EUR 1,000 is below EUR 4,587.09, so the art. 53 deduction removes all of it. Taxable income is EUR 13,000, all Portuguese. Tax = 12,587 x 13.579% + (13,000 - 12,587) x 21.20% = 1,709.19 + 87.56 = EUR 1,796.74.
4. **Result.** The option saves EUR 1,453.26. She files a Modelo 3 between 1 April and 30 June 2027 with Anexo F, makes the election and attaches proof of French residence and of her worldwide income. If she has health or other expenses that France does not allow, she may also claim the art. 78 deductions (art. 17-A(4)). How France then treats the rent is outside this skill.

```oa-check
name: PT non-resident landlord, 25% flat vs art. 17-A resident bands, 2026
inputs:
  rent_gross: 14400
  rent_costs: 1400
  foreign_pension: 1000
  pension_deduction: 4587.09
  flat_rate: 0.25
  band2_top: 12587
  band2_avg: 0.13579
  band3_rate: 0.212
steps:
  - share_pt: rent_gross / (rent_gross + foreign_pension)
  - net_rent: rent_gross - rent_costs
  - flat_tax: net_rent * flat_rate
  - pension_taxable: max(foreign_pension - pension_deduction, 0)
  - taxable: net_rent + pension_taxable
  - tax_17a: round(band2_top * band2_avg + (taxable - band2_top) * band3_rate, 2)
  - saving: flat_tax - tax_17a
expected:
  share_pt: 0.9351
  net_rent: 13000
  flat_tax: 3250.00
  taxable: 13000
  tax_17a: 1796.74
  saving: 1453.26
tolerance: 0.01
```

### Example 2: arriving on 1 July 2026, split year and the IFICI test

Mark is British. He has never lived in Portugal. He arrives in Lisbon on 1 July 2026, signs a long lease on a flat that day, sleeps in Portugal every night to 31 December, and starts work as a software engineer for a Portuguese company on 1 July. The company's main business code is on the Portaria 352/2024/1 Annex II list and it exports more than 50% of its turnover. Mark holds a master's degree and has six years' experience. His Portuguese gross salary for July to December 2026, including the pro-rata holiday and Christmas subsidies, is EUR 42,000. His employee social security at 11% is EUR 4,620. His UK salary for January to June was EUR 40,000.

1. **Residence.** Days of presence in 2026 = 31 + 31 + 30 + 31 + 30 + 31 = 184, which is more than 183. He also has a habitual home from 1 July. He was not resident on any day of 2025, so he is resident from 1 July 2026, his first day of presence (art. 16(3)).
2. **Split year.** For 1 January to 30 June he is non-resident and has no Portuguese income, so the UK salary is outside Portuguese tax (art. 15(2) and (3)). From 1 July he is taxed on worldwide income. Art. 57(6) requires one return for each residence status, subject to the general filing exemptions. All his Portuguese-taxable 2026 income falls in the resident part.
3. **IFICI entry test.** He became resident under art. 16(1). He was not resident in 2021 to 2025. ICT specialists (CPP code 25) are an Annex I profession. He has a master's plus three or more years' experience. The employer meets letter (c)(ii). He has never had NHR or art. 12-A. So he qualifies under EBF art. 58-A(1)(c)(ii), reviewed by AT. He must register by 15 January 2027. If he registers late, IFICI starts only in the year he registers (art. 58-A(7)).
4. **Net Category A income.** Social security of EUR 4,620 is more than 8.54 x IAS (EUR 4,587.09), so the deduction is EUR 4,620 (art. 25(2)). Net income = 42,000 - 4,620 = EUR 37,380.
5. **IFICI tax:** 20% x 37,380 = EUR 7,476.00.
6. **General rates, for comparison:** 29,397 x 20.579% + (37,380 - 29,397) x 34.90% = 6,049.61 + 2,786.07 = EUR 8,835.68.
7. **Result.** IFICI saves EUR 1,359.68 for 2026, before the deductions from the tax, which this comparison leaves out. The minimum-existence deduction does not apply on either route: his gross income is above 2.2 x 14 x IAS = EUR 16,543.60 (art. 70(4)(a)). He must tell AT about the change of status within 60 days (LGT art. 19(5)).

```oa-check
name: PT arrival 1 July 2026, 183-day count and IFICI 20% vs 2026 bands
inputs:
  pt_salary: 42000
  ss_rate: 0.11
  ias: 537.13
  ifici_rate: 0.20
  band5_top: 29397
  band5_avg: 0.20579
  band6_rate: 0.349
steps:
  - days_present: 31 + 31 + 30 + 31 + 30 + 31
  - over_183: days_present - 183
  - ss: pt_salary * ss_rate
  - specific_deduction: max(round(8.54 * ias, 2), ss)
  - net_a: pt_salary - specific_deduction
  - ifici_tax: net_a * ifici_rate
  - general_tax: round(band5_top * band5_avg, 2) + round((net_a - band5_top) * band6_rate, 2)
  - saving: general_tax - ifici_tax
expected:
  days_present: 184
  over_183: 1
  specific_deduction: 4620.00
  net_a: 37380.00
  ifici_tax: 7476.00
  general_tax: 8835.68
  saving: 1359.68
```

## Ask the client first

1. For each year in question: the exact dates in and out of Portugal (nights spent), and whether you had a home available in Portugal. (Residence and the first or last day of residence.)
2. Were you resident in Portugal on any day of the previous year, or in any of the last five years? Have you ever had NHR, IFICI or the art. 12-A regime? (Art. 16(3), IFICI eligibility.)
3. Where are you tax resident now, and do you hold a residence certificate from that country? Is it in the EU or EEA? (Treaty relief, the art. 17-A and 72(15) options, the need for a representative.)
4. List all your income for the year by type and country, Portuguese and foreign. (The 90% test and the band rate on worldwide income.)
5. If you are leaving: will you have Portuguese-taxable income after the day you leave, and do you plan to come back next year? (Art. 16(14) and (16).)
6. For a company: is the seat or effective management moving, which assets stay in a Portuguese permanent establishment, and where is the company going? (Exit tax and the five-instalment option.)

## Sources

| Source | URL | Read on |
|---|---|---|
| CIRS art. 15, scope of IRS | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs15.aspx | 2026-10-23 |
| CIRS art. 16, residence | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs16.aspx | 2026-10-23 |
| CIRS art. 17-A, option for EU/EEA residents | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs17a.aspx | 2026-10-23 |
| CIRS art. 10, capital gains (crypto on loss of residence, n.º 25) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs10.aspx | 2026-10-23 |
| CIRS art. 18, income obtained in Portugal | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs18.aspx | 2026-10-23 |
| CIRS art. 22, aggregation (non-residents' property gains, n.º 3(a) and 10) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs22.aspx | 2026-10-23 |
| CIRS art. 25, Category A deduction | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs25.aspx | 2026-10-23 |
| CIRS art. 43, gains (50% inclusion; exit value of crypto) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs43.aspx | 2026-10-23 |
| CIRS art. 53, pension deduction | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs53.aspx | 2026-10-23 |
| CIRS art. 57, returns (two residence statuses) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs57.aspx | 2026-10-23 |
| CIRS art. 60, filing period | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs60.aspx | 2026-10-23 |
| CIRS art. 68, 2026 bands (Lei 73-A/2025) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs68.aspx | 2026-10-23 |
| CIRS art. 70, minimum existence | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs70.aspx | 2026-10-23 |
| CIRS art. 71, final withholding rates and refunds | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs71.aspx | 2026-10-23 |
| CIRS art. 72, special rates | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs72.aspx | 2026-10-23 |
| CIRS art. 101, withholding on other categories | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs101.aspx | 2026-10-23 |
| CIRS art. 101-C, treaty relief and refunds for non-resident individuals | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs101c.aspx | 2026-10-23 |
| CIRS art. 130, representatives | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs130.aspx | 2026-10-23 |
| CIRC art. 2, residence of entities | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc2.aspx | 2026-10-23 |
| CIRC art. 4, scope of IRC | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc4.aspx | 2026-10-23 |
| CIRC art. 14, directive exemptions | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc14.aspx | 2026-10-23 |
| CIRC art. 83, transfer of residence (exit tax) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc83.aspx | 2026-10-23 |
| CIRC art. 84, permanent establishment ceasing or moving assets | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc84.aspx | 2026-10-23 |
| CIRC art. 87, rates (and Lei 64/2025 transition) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87.aspx | 2026-10-23 |
| CIRC art. 94, IRC withholding | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc94.aspx | 2026-10-23 |
| CIRC art. 98, relief and refunds for non-residents | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc98.aspx | 2026-10-23 |
| CIRC art. 126, representation of non-resident entities | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc126.aspx | 2026-10-23 |
| EBF art. 58-A, IFICI | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/bf_rep/Pages/ebf58a.aspx | 2026-10-23 |
| LGT art. 19, tax domicile and representative | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/lgt/Pages/lgt19.aspx | 2026-10-23 |
| RGIT art. 114, 116 and 117, fines | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit114.aspx | 2026-10-23 |
| AT FAQ, IRC international relations, forms 21-RFI to 24-RFI | https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/questoes_frequentes/Pages/faqs-00457.aspx | 2026-10-23 |
| AT forms page, double taxation (Mod. 2-RFI, Modelo 30) | https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/modelos_formularios/convencoes_dupla_trib_internacional/Pages/dupla-tributacao-internacional.aspx | 2026-10-23 |
| Portaria 480-A/2025/1, IAS 2026 EUR 537.13 | https://files.diariodarepublica.pt/1s/2025/12/25001/0000200002.pdf | 2026-10-23 |
| Segurança Social, practical guide: postings from Portugal (A1, 24 months, Reg. 883/2004 art. 12 and 13), published 3 May 2023 | https://www.seg-social.pt/ptss/pssd/documento/cmc2117bg00thkl2y1r0iz21r | 2026-10-23 |
| Segurança Social, practical guide: postings to Portugal | https://www.seg-social.pt/ptss/pssd/documento/cmc21059n00tbkl2yjgp69iw9 | 2026-10-23 |

Not yet confirmed:

- Whether AT accepts the resident option to aggregate residential rent (art. 72(13)) inside an art. 17-A election. Art. 17-A(1) applies the rules for residents, which include that option, but no AT instruction or FAQ on the point was found. Example 1 assumes it does; without it, the rent stays at 25%.
- Whether the 90% test in art. 17-A(1) is measured on gross or net income. Example 1 passes on both.
- The text of Reg. 883/2004 itself. EUR-Lex did not load; the A1 rules above come from the Segurança Social guides.
- The list of low-tax jurisdictions (the portaria behind the 35% rates and art. 16(6)) was not read today.
- Whether a person with no Portuguese income in the non-resident part of a split year must still file the second return under art. 57(6), or is exempt under art. 58.
- The deadline for Modelo 30 and the late-payment interest rate for 2027 were not read today.
