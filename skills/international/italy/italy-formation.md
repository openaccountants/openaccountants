---
name: italy-formation
description: Use this skill whenever asked about forming, incorporating, or registering a company in Italy. Trigger on phrases like "set up a company in Italy", "SRL formation", "SRLS", "Camera di Commercio", "Italian company formation", "register a business Italy", "società a responsabilità limitata", "Registro delle Imprese", "partita IVA", "Italian notary", or any question about starting a business entity in Italy. Covers entity types (SRL, SRLS, SPA, SNC, SAS), registration process, capital requirements, costs, post-formation compliance, and bank account opening. ALWAYS read this skill before advising on Italian company formation.
version: 1.0
jurisdiction: IT
tax_year: 2026
last_updated: 2026-09-22
review_status: pending_review
drafted_by: OpenAccountants
approved_by: pending
depends_on:
  - company-formation-workflow-base
category: formation
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Starting a business in Italy (ditta individuale, partnerships, S.r.l. and S.p.A.)

How to set up a business in Italy: which legal form to pick, the steps from the deed to the Registro delle Imprese, the capital that must be paid in, the VAT number (partita IVA), the ATECO activity code, the INPS and INAIL registrations, and the duties that start once the business exists. Figures are for tax year 2026. Italy's tax year is the calendar year. The Civil Code articles were read on Normattiva in their text in force on 22 September 2026. The annual government concession tax on company books comes from an Agenzia delle Entrate page that does not show a year; the amounts are fixed by statute and apply to 2026. The IRAP rate comes from the Agenzia's instructions to the IRAP return filed in 2026, which covers tax year 2025.

## Italy Company Formation Guide v1.0

Tax detail lives in other Guides: income tax for individuals and partners in `it-income-tax`, IRAP in `it-irap`, VAT returns in `italy-vat-return`, e-invoicing in `italy-einvoice`, and INPS contributions in `it-inps-contributions`. Where no official page prints a number, this Guide says so and gives none.

## Section 1: Quick Reference

| Field | Value |
| --- | --- |
| Country | Italy (Italian Republic) |
| Currency | Euro |
| Company registrar | Registro delle Imprese, kept by the local Camera di Commercio |
| Key legislation | Civil Code (Codice civile): arts. 2291 and following (S.n.c.), 2313 and following (S.a.s.), 2325 and following (S.p.A.), 2462 to 2483 (S.r.l.), 2463-bis (S.r.l. semplificata); D.L. 1/2012 art. 3 (S.r.l. semplificata costs); D.P.R. 633/1972 art. 35 (VAT registration) |
| Typical formation time | Legacy estimate: 1 to 3 weeks. No official page states a duration. The notary must file a company deed within ten days (art. 2330) |
| Taxes on an S.r.l. or S.p.A. | IRES and IRAP. The table below gives each rate. No official page prints one combined rate, so this Guide does not state one |
| Tax authority | Agenzia delle Entrate (codice fiscale, partita IVA, tax returns) |

**Company taxes (for detail see `it-irap` and `it-income-tax`)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art77!vig= |
| IRES, corporate income tax on the company's net income (TUIR art. 77) | 24% | "con l'aliquota del 24 per cento" |

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.agenziaentrate.gov.it/portale/documents/20143/9765340/IRAP_2026_istruzioni.pdf/6cd3bc0e-e7bd-f449-c86b-03cc142c1b74?t=1772192055414 |
| IRAP, regional tax, ordinary rate on the net value of production. Regions may vary it, and some sectors pay a surcharge in 2026 (see `it-irap`) | 3.9% | "l'aliquota del 3,9 per cento" |

IRAP is also due from S.n.c. and S.a.s., under art. 3(1)(b) of D.Lgs. 446/1997 (https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-15;446~art3!vig=2026-06-30). Individuals, including a ditta individuale, have not paid IRAP since 2022 (L. 234/2021 art. 1 comma 8, quoted in note 70 on the same Normattiva page; see `it-irap`).

## Section 2: Entity Types Comparison

The capital amounts are in the linked tables of Section 4.

| Feature | Ditta Individuale (Sole Trader) | S.r.l. (Standard) | S.r.l.s. (Simplified) | S.n.c. / S.a.s. (Partnerships) | S.p.A. (Joint-stock Company) |
| --- | --- | --- | --- | --- | --- |
| Legal personality | No | Yes, from registration (art. 2331, applied to the S.r.l. by art. 2463) | Yes, as for the S.r.l. | No. The code gives legal personality on registration only to the companies (società di capitali) | Yes, from registration (art. 2331) |
| Liability | Unlimited | Limited | Limited | S.n.c.: unlimited for all partners. S.a.s.: unlimited for the accomandatari, limited for the accomandanti | Limited |
| Min. founders | 1 | 1 | 1, natural persons only (art. 2463-bis) | 2 | 1 |
| Min. share capital | None | Standard minimum (diecimila euro); a reduced capital of at least one euro is allowed (art. 2463) | At least one euro and below the standard S.r.l. minimum | None | cinquantamila euro (art. 2327) |
| Paid in at the deed | None | At least a quarter of cash contributions, paid to the directors; the whole amount if there is a single founder or a reduced capital | Everything, in cash, to the directors | None | At least a quarter of cash contributions, into a bank; the whole amount if there is a single founder |
| Governance flexibility | Not applicable | High (customisable statuto) | Low: the standard-model clauses cannot be changed | Low | Medium |
| Tax treatment | IRPEF on the owner (`it-income-tax`); forfettario possible (Section 3, Step 6) | IRES and IRAP | IRES and IRAP | Income taxed on the partners (IRPEF); IRAP on the partnership | IRES and IRAP |
| Notary required | No | Yes (public deed) | Yes, but no notary fees are due (D.L. 1/2012 art. 3) | Yes in practice: the deed must be a public deed or carry signatures authenticated by a notary (art. 2296) | Yes |
| Admin burden | Low | High | Medium | Low to medium | Very high |

**Recommended default:** standard S.r.l. for most commercial purposes. S.r.l.s. for small businesses owned by individuals who accept the fixed model statuto. A single individual starting small often begins as a ditta individuale.

## Section 3: Registration Process

The steps below are for an S.r.l. A ditta individuale skips Steps 2 to 5: it registers with one Comunicazione Unica (Step 6).

### Step 1: Choose Company Name (Denominazione Sociale)

- **Company name requirements.** The name must contain the words "società a responsabilità limitata" (art. 2463). An S.r.l.s. must contain "società a responsabilità limitata semplificata" (art. 2463-bis). Check with the Camera di Commercio that the name is free.

### Step 2: Draft Atto Costitutivo and Statuto

- **Atto costitutivo and statuto requirements.** The atto costitutivo (deed of incorporation) must be a public deed and state, among other things, the capital subscribed and paid in (art. 2463). An S.r.l.s. must use the standard model set by decree of the Ministry of Justice, and its clauses cannot be changed (art. 2463-bis). A standard S.r.l. can customise its statuto.

### Step 3: Notary Appointment

- **Notary appointment requirements.** Both S.r.l. and S.r.l.s. need a notary. For an S.r.l.s. the deed and registration are exempt from stamp duty and registry fees (diritti di segreteria), and no notary fees are due (D.L. 1/2012 art. 3(3)). The notary checks identity, capacity and that the capital has been paid.

### Step 4: Deposit Share Capital

- **Deposit share capital requirements.** S.r.l.: at least a quarter of the cash contributions ("almeno il venticinque per cento") and any share premium are paid to the directors named in the deed, not into a bank. A single founder pays the whole amount (art. 2464). A policy or bank guarantee can replace the cash payment. Reduced-capital S.r.l. and S.r.l.s.: cash only, paid in full to the directors. S.p.A.: at least a quarter of cash contributions is paid into a bank, the whole amount for a single founder (art. 2342). The amounts are in Section 4.

### Step 5: Register with Registro delle Imprese

- **Registration with Registro delle Imprese.** The notary files the deed with the Registro delle Imprese within ten days ("entro dieci giorni", art. 2330, applied to the S.r.l. by art. 2463). The company exists as a legal person from registration (art. 2331). For an S.n.c. or S.a.s. the directors file the deed within thirty days (art. 2296). A fixed registration tax (imposta di registro) is due on the deed. The consolidated tariff on Normattiva still prints the original lire amount, and no allowed page prints the current euro amount, so this Guide gives none. Camera di Commercio fees and stamp duty are set on sites outside the allowed list; ask the notary.

### Step 6: Obtain PEC and Codice Fiscale / Partita IVA

- **PEC and Codice Fiscale / Partita IVA.** Anyone starting a business, trade or profession must declare it to the Agenzia delle Entrate within thirty days, and receives a partita IVA that does not change until the activity ends (D.P.R. 633/1972 art. 35). Companies use form AA7/10; individuals use form AA9/12. Anyone who must be entered in the Registro delle Imprese or the REA (companies, partnerships, a ditta individuale in trade or crafts) files through the Comunicazione Unica (ComUnica), which reaches the Registro delle Imprese, the Agenzia delle Entrate, INPS and INAIL in one filing. A professional who need not be in the Registro delle Imprese files form AA9/12 directly with the Agenzia.
- **ATECO code.** The filing states the activity by its ATECO code. The 2025 classification replaced the 2007 one and has been used in filings with the Agenzia since 1 April 2025 (Agenzia resolution 24/E of 8 April 2025). The code matters later: for a forfettario it sets the profitability coefficient, and some sectors pay an IRAP surcharge.
- **Forfettario for a ditta individuale.** An individual can choose the flat-rate regime in form AA9/12 or in ComUnica. Entry conditions and rates are in the table below; the full rules are in `it-income-tax`.
- **PEC.** Every company needs a certified e-mail address (PEC), recorded in the Registro delle Imprese. The statute was not read for this refresh (see "When to refuse or refer").

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.agenziaentrate.gov.it/portale/regime-forfetario-le-regole-2020-/infogen-regime-forfetario-le-regole-2020- |
| Forfettario: previous-year revenue or fees, annualised, must not be above | EUR 85,000 | "non superiori a 85.000 euro" |
| Forfettario substitute tax, in place of IRPEF and its surcharges | 15% | "nella misura del 15%" |
| Forfettario start-up rate, first five years, if the conditions are met | 5% | "L'imposta sostitutiva è ridotta al 5% per i primi cinque anni di attività" |

### Step 7: INPS and INAIL Registration

- **INPS and INAIL Registration.** ComUnica also carries the INPS and INAIL registrations. A trader or craftsman (ditta individuale, or a partner who works in the business) is enrolled with the INPS artigiani or commercianti fund; a professional without a professional fund pays into the gestione separata; company directors paid a fee also fall in the gestione separata. INAIL insures employees and, in some trades, working owners. Rates and minimums are in `it-inps-contributions`.

### Step 8: Tassa di Concessione Governativa

- **Tassa di Concessione Governativa.** S.p.A., S.r.l. and S.a.p.a. pay a yearly government concession tax for the numbering and stamping of their books. It depends on the capital on 1 January of the year paid. The first year is paid by postal slip (c/c 6007) before the VAT start-of-activity declaration; later years by F24 with tax code 7085 by 16 March. Partnerships and individuals do not pay it.

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.agenziaentrate.gov.it/portale/schede/pagamenti/f24verstassareg/f24-tassa-ccgg |
| Yearly tax if capital is not above EUR 516,456.90 | EUR 309.87 | "309,87 euro, se l’ammontare del capitale o del fondo di dotazione non supera" |
| Capital limit | EUR 516,456.90 | "516.456,90 euro" |
| Yearly tax if capital is above the limit | EUR 516.46 | "516,46 euro, se il capitale sociale o il fondo di dotazione supera tale importo" |


## Section 4: Capital Requirements

The standard S.r.l. minimum is printed in words in art. 2463 ("diecimila euro") and in digits in art. 2463-bis, which is why the table uses that article.

| Entity Type | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2463bis!vig= |
| S.r.l. standard minimum capital (art. 2463, secondo comma, numero 4, as referred to in art. 2463-bis) | EUR 10,000 | "inferiore all'importo di 10.000 euro previsto all'articolo 2463" |
| S.r.l.s. minimum capital; it must also be below EUR 10,000, subscribed and paid in full at formation, in cash, to the directors | EUR 1 | "pari almeno ad 1 euro" |

| Entity Type | Min. Share Capital | Min. Paid-Up | Payment Timing | In-Kind Contributions |
| --- | --- | --- | --- | --- |
| S.r.l. (several founders) | diecimila euro (art. 2463) | A quarter of cash contributions plus the whole share premium, to the directors (art. 2464) | At the deed | Permitted, if the deed allows; those quotas are paid in full at subscription (art. 2464) |
| S.r.l. (single founder) | diecimila euro | The whole cash contribution (art. 2464) | At the deed | Permitted |
| S.r.l. with reduced capital | At least one euro, below diecimila euro (art. 2463) | All of it, in cash, to the directors | At the deed | Not permitted: cash only |
| S.r.l.s. | At least one euro, below diecimila euro (art. 2463-bis) | All of it, in cash, to the directors | At the deed | Not permitted: cash only |
| S.p.A. | cinquantamila euro (art. 2327) | A quarter of cash contributions into a bank; the whole amount for a single founder (art. 2342) | At the deed | Permitted; those shares are paid in full at subscription; services cannot be contributed (art. 2342) |

A reduced-capital S.r.l. must set aside at least one fifth of each year's net profit as a legal reserve until reserve and capital together reach diecimila euro (art. 2463). If an S.r.l. or S.p.A. comes to have a single member, amounts still unpaid must be paid within ninety days (arts. 2464 and 2342).


## Section 5: Costs Breakdown

No allowed page prints notary fees, Camera di Commercio registration fees, stamp duty on the filing, the registration tax in euro, or PEC prices. The legacy cost table gave amounts for all of these; they are removed. What official pages do settle:

- S.r.l.s.: no notary fees, and no stamp duty or registry fees on the deed and registration (D.L. 1/2012 art. 3(3): https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2012-01-24;1~art3!vig=). The exemption does not name the registration tax (imposta di registro), which Step 5 says is due on the deed.
- S.r.l. and S.p.A.: the yearly concession tax in the table in Section 3, Step 8.
- Ask the notary for a written quote covering fees, registration tax, stamp duty and chamber fees.

### Annual Maintenance

| Item | Cost |
| --- | --- |
| Diritto annuale (Camera di Commercio) | Set by the chamber system; not on an allowed page |
| Tassa concessione governativa (S.r.l., S.p.A.) | See the table in Section 3, Step 8 |
| Commercialista (accountant) fees | Market price; no official figure |
| Bilancio deposit (annual accounts filing) | Chamber fees; not on an allowed page |

## Section 6: Post-Formation Compliance

| Obligation | Deadline | Authority |
| --- | --- | --- |
| Bilancio (annual accounts) | Approved by the shareholders within 120 days of the year end, or up to 180 days where the statuto allows it for the reasons in art. 2364; filed within 30 days of approval (art. 2435) | Registro delle Imprese |
| IRES and IRAP return (Modello Redditi SC, IRAP) | By the last day of the tenth month after the end of the tax year (D.P.R. 322/1998 art. 2(2)). For a calendar year that is 31 October. The IRAP return follows the same deadline (art. 2(3)) | Agenzia delle Entrate |
| IVA settlements and annual return | Monthly or quarterly (see `italy-vat-return`) | Agenzia delle Entrate |
| E-invoices | Every invoice through the SdI (see `italy-einvoice`) | Agenzia delle Entrate |
| Diritto annuale | Legacy: paid with the first income tax instalment. Not checked on an allowed page | Camera di Commercio |
| Titolare effettivo (beneficial owner register) | Legacy: within 30 days of any change. Not checked on an allowed page | Camera di Commercio |
| Libro soci updates | On any share transfer | Internal (notarised) |
| Concession tax on books | 16 March each year (Section 3, Step 8) | Agenzia delle Entrate |


## Section 7: Bank Account Opening

### Documents Typically Required

- **Documents required for bank account.** Visura camerale (Chamber of Commerce extract); atto costitutivo and statuto; ID and codice fiscale of all directors and shareholders; PEC address; description of the business.

### Typical Timeline

- **Bank account opening timeline.** Legacy estimate: 1 to 3 weeks (Italian banks are thorough with KYC). An S.p.A. needs the bank before the deed, because its capital is paid into a bank. An S.r.l. pays its capital to the directors, so the account can follow registration.

### Common Banks

- **Common banks.** Intesa Sanpaolo, UniCredit, BNL (BNP Paribas) (traditional); Banca Sella, Qonto, Finom (digital).

## Section 8: Foreign Founder Considerations

| Question | Answer |
| --- | --- |
| Non-resident directors allowed? | Yes. A codice fiscale is required |
| Physical presence required? | For the notary deed, yes, or a power of attorney that is itself notarised and apostilled |
| Apostille requirements | Foreign documents need an apostille and a sworn Italian translation |
| Foreign ownership restrictions | None for a standard S.r.l.; regulated sectors may need authorisations |
| Codice fiscale for foreigners | From an Italian consulate abroad or the Agenzia delle Entrate |

These answers are legacy practice notes.

## Section 9: Common Mistakes and Refusals

- **R-IT-F1: Choosing S.r.l.s. for a growing business.** The S.r.l.s. has a fixed model statuto whose clauses cannot be changed, and its capital must stay below the standard minimum (Section 4). It cannot hold investor-friendly provisions. Advise a standard S.r.l. for a business expecting growth or outside investment. A standard S.r.l. can also have a reduced capital of at least one euro.  _(R-IT-F1)_
- **R-IT-F2: Failing to set up PEC.** A company needs an active PEC address in the Registro delle Imprese; without it the company misses official notices.  _(R-IT-F2)_
- **R-IT-F3: Ignoring tassa concessione governativa.** The yearly concession tax on company books (Section 3, Step 8) is often missed. It is due regardless of turnover.  _(R-IT-F3)_
- **R-IT-F4: Single-shareholder S.r.l. with only a quarter paid up.** With one founder, art. 2464 requires the whole cash contribution at formation. The quarter minimum applies only when there are several founders.  _(R-IT-F4)_
- **R-IT-F5: In-kind contributions in S.r.l.s.** The S.r.l.s. (and the reduced-capital S.r.l.) take cash only. Use a standard S.r.l. with full capital if non-cash contributions are needed.  _(R-IT-F5)_
- **R-IT-F6: Paying S.r.l. capital into a bank and waiting for release.** Since 2013 S.r.l. capital is paid to the directors named in the deed (art. 2464). The bank deposit rule now applies to the S.p.A. (art. 2342).  _(R-IT-F6)_

## Section 10: Timeline

Durations are legacy estimates, except the notary's ten-day filing limit (art. 2330: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2330!vig=) and the thirty-day VAT declaration limit (art. 35).

| Step | Duration | Cumulative |
| --- | --- | --- |
| Name check and document preparation | 2 to 5 days | Day 2 to 5 |
| Capital paid (to the directors for an S.r.l.; to a bank for an S.p.A.) | At the deed | Day 3 to 10 |
| Notary appointment and deed | 1 to 5 days | Day 3 to 10 |
| Notary files with Registro delle Imprese | Within ten days of the deed (law) | Day 5 to 20 |
| Registration complete | 3 to 7 days | Day 8 to 27 |
| Partita IVA and codice fiscale (via ComUnica) | 1 to 3 days; declaration due within thirty days of starting | Day 9 to 30 |
| INPS and INAIL registration | With ComUnica | Day 9 to 30 |
| Bank account fully operational | 1 to 3 weeks | Day 16 to 50 |
| **Ready to trade** |  | **About 2 to 5 weeks** |

## The method, step by step

1. Pick the legal form with the client's answers below, using the comparison in Section 2 and the capital rules of Civil Code arts. 2463, 2463-bis, 2464, 2327 and 2342 (https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2463bis!vig=).
2. For a company or partnership, have the notary draw up the deed. Pay the capital as art. 2464 (S.r.l.) or art. 2342 (S.p.A.) requires, and check the notary files it within ten days under art. 2330 (https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2330!vig=). For an S.n.c. or S.a.s., file within thirty days under art. 2296 (https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2296!vig=).
3. File the start-of-activity declaration within thirty days under D.P.R. 633/1972 art. 35 (https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art35!vig=): through ComUnica if the business goes in the Registro delle Imprese, with form AA7/10 for entities (https://www.agenziaentrate.gov.it/portale/web/guest/schede/istanze/aa7_10/schedainfo-aa7_10) or AA9/12 for individuals (https://www.agenziaentrate.gov.it/portale/schede/istanze/aa9_11-apertura-variazione-chiusura-pf/scheda-informativa-aa9_11). State the 2025 ATECO code (https://www.agenziaentrate.gov.it/portale/documents/20143/8410900/RISOLUZIONE+ATECO+2025/05fdbeda-c727-bf26-ecab-a2e6c1080753) and, for an individual, whether the forfettario is chosen.
4. For an S.r.l. or S.p.A., pay the first-year concession tax on the books before the VAT declaration, then by 16 March each year (https://www.agenziaentrate.gov.it/portale/schede/pagamenti/f24verstassareg/comequando).
5. Confirm the INPS fund for each owner or director and hand over to `it-inps-contributions`, `it-income-tax`, `it-irap`, `italy-vat-return` and `italy-einvoice`.

## Ask the client first

- Will you run the business alone, with partners, or with investors, and do you need limited liability?
- How much capital can you put in, and in cash or in assets?
- Are all founders natural persons? (An S.r.l.s. allows only natural persons.)
- What will the business do? (This sets the ATECO code, whether the Registro delle Imprese is needed, and the INPS fund.)
- For an individual: what were last year's revenue and employment income? (This decides the forfettario.)
- Are you resident in Italy, and do you already have a codice fiscale?

## When to refuse or refer

- Regulated activities (banking, insurance, investment services, professions with their own registers and funds): refer to a specialist.
- Contributions in kind, valuations and reports on assets contributed: refer to the notary and a commercialista; this Guide does not cover the valuation rules.
- Any cost quote (notary, registration tax, stamp duty, chamber fees, diritto annuale): refer to the notary. No allowed page prints them.
- PEC duties for companies and directors, and the beneficial owner register: this Guide did not read those statutes; refer to a commercialista.
- A foreign parent setting up a branch or subsidiary, or a founder moving to Italy: refer for tax residence and permanent establishment advice.

## Sources

- Civil Code arts. 2296, 2327, 2330, 2331, 2342, 2364, 2435, 2463, 2463-bis, 2464: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2463!vig=
- D.L. 1/2012 art. 3: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2012-01-24;1~art3!vig=
- D.P.R. 633/1972 art. 35: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art35!vig=
- D.P.R. 322/1998 art. 2: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1998-07-22;322~art2!vig=2026-06-30
- TUIR art. 77: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art77!vig=
- D.Lgs. 446/1997 art. 3: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-15;446~art3!vig=2026-06-30
- Agenzia delle Entrate, IRAP 2026 instructions: https://www.agenziaentrate.gov.it/portale/documents/20143/9765340/IRAP_2026_istruzioni.pdf/6cd3bc0e-e7bd-f449-c86b-03cc142c1b74?t=1772192055414
- Agenzia delle Entrate, concession tax on company books: https://www.agenziaentrate.gov.it/portale/schede/pagamenti/f24verstassareg/f24-tassa-ccgg
- Agenzia delle Entrate, forfettario rules: https://www.agenziaentrate.gov.it/portale/regime-forfetario-le-regole-2020-/infogen-regime-forfetario-le-regole-2020-
- Agenzia delle Entrate, forms AA7/10 and AA9/12 and resolution 24/E of 2025 on ATECO: links in "The method, step by step"

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute legal, tax, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional before acting upon.

The most up-to-date version of this Guide is maintained at openaccountants.com.

> Contributed by OpenAccountants.

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
