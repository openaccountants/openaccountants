---
name: uy-company-formation
description: "Company formation and entity choice in Uruguay for 2026, each rule tied to the law on IMPO. Covers the SAS (Ley 19.820: one or more founders, 10% of cash capital paid in at signing, full payment within 24 months, registration within 30 days, digital constitution), the SRL (Ley 16.060: up to 50 partners, 50% of cash contributions at signing, the rest within two years) and the SA (25% paid in and 50% subscribed at signing, capital in pesos, bank account for cash contributions), registration at the Registro Nacional de Comercio, BPS registration and the first-hire steps, the beneficial owner rules (Ley 19.484: 15% threshold, reporting to the Banco Central), approval and registration of annual accounts, and the yearly tax calendar. Trigger on: abrir empresa Uruguay, SAS Uruguay, SRL, sociedad anónima, constituir sociedad, beneficiario final, company formation Uruguay 2026. Out of scope: free-zone users, cooperatives, trusts, branches of foreign companies."
version: 0.2
jurisdiction: UY
tax_year: 2026
last_updated: 2026-11-14
category: formation
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: formation
type: filing-howto
---

# Uruguay: company formation and entity choice, 2026 v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

This skill sets out how to choose and form a company in Uruguay in 2026, in the order a founder meets the steps, and what the company must keep doing afterwards. Taxes are in the other Uruguay skills and are linked, not repeated:

- [uy-corporate-income-tax](uy-corporate-income-tax.md): IRAE, which every company here pays, and its returns and payments on account.
- [uruguay-iva](uruguay-iva.md): IVA registration and returns.
- [uruguay-payroll](uruguay-payroll.md) and [uruguay-social-contributions](uruguay-social-contributions.md): BPS, for staff and for working owners.
- [uy-cross-border](uy-cross-border.md): foreign shareholders, dividends and payments abroad.

**Which text of the law.** Ley 16.060 (Ley de Sociedades Comerciales), Ley 19.820 (SAS, Title II), Ley 19.484 (beneficial owners, arts. 22 to 26), as consolidated on IMPO; BPS for its own registration steps.

**Quick reference, 2026**

| Item | SAS | SRL | SA |
|---|---|---|---|
| Founders | One or more persons, individual or legal, but not an SA (Ley 19.820 art. 11) | Two or more (Ley 16.060 art. 1), at most 50 (art. 223) | Two or more (Ley 16.060 art. 1) |
| Cash capital paid in at signing | At least 10%; in-kind 100% (Ley 19.820 art. 15) | At least 50% of each partner's cash contribution; in-kind 100% (art. 228) | At least 25% paid in, 50% subscribed, for a single-act constitution (art. 280) |
| Balance | Within 24 months | Within two years | As the statute provides (not read) |
| Liability | Limited to contributions, including for labour and tax debts, unless the veil is lifted (Ley 19.820 art. 8) | Limited to paying in the quotas (art. 223) | Limited to shares (not read for this skill) |

## Who this applies to

- **Founders** setting up a new commercial company in Uruguay: individuals or companies, resident or not, choosing between the SAS, the SRL and the SA.
- **Not every activity may use an SAS.** It is barred for companies offering shares to the public, companies with direct or indirect State shareholders, activities for which the law requires a specific type, and SAs formed before Ley 19.820 that later change type (Ley 19.820 art. 8).
- **Out of scope.** Sole proprietorships (unipersonales: see [uruguay-social-contributions](uruguay-social-contributions.md) for their BPS minimum), sociedades de hecho, cooperatives, trusts, free-zone users, and branches of foreign companies.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| SAS: capital paid in at signing, cash contributions | At least 10% | 2026 | https://www.impo.com.uy/bases/leyes/19820-2019 (art. 15) |
| SAS: capital paid in at signing, contributions in kind | 100% | 2026 | same |
| SAS: longest term for full payment of the shares | 24 months | 2026 | same |
| SAS: registration of the constitutive act at the Registro de Personas Jurídicas, Sección Registro Nacional de Comercio | Within 30 days of signing; digital filings are reviewed within 24 hours from the next working day | 2026 | same (art. 11) |
| SAS: State oversight (as for a closed SA) once annual income exceeds UI 37,500,000 at year end | Applies automatically 180 days later | 2026 | same (art. 10) |
| SAS: State control of non-cash contributions where income exceeds UI 4,000,000 or Uruguayan assets exceed UI 2,500,000 | In the form the regulation sets | 2026 | same (art. 34) |
| SRL: maximum number of partners | 50; above that, become an SA within two years or dissolve | 2026 | https://www.impo.com.uy/bases/leyes/16060-1989 (art. 223) |
| SRL: cash contribution paid in at signing | At least 50%, the rest within two years; in-kind contributions in full | 2026 | same (art. 228) |
| SRL: partners' guarantee of contributions to third parties | Joint, for two years from each contribution | 2026 | same (art. 229) |
| SRL: registration and publication | Contract registered at the Registro Público de Comercio, then an extract published within 60 days | 2026 | same (art. 227) |
| SA: single-act constitution | At least 25% of capital paid in and 50% subscribed | 2026 | same (art. 280) |
| SA: currency of capital | Uruguayan pesos; foreign currency may be allowed where the main object is investing in assets abroad | 2026 | same (art. 279) |
| SA: cash contributions | Deposited in a bank account in the name of the company in formation, "Cuenta integración de capital" | 2026 | same (art. 281) |
| Annual accounts: approval by partners or shareholders | Within 180 days of the year end (120 days for open companies); taken as approved if not challenged within 30 days of communication, except where shareholder meetings apply | 2026 | same (art. 97) |
| Annual accounts: registration with the State control body (AIN) | Within the terms of the regulation, above the asset or income levels the Executive sets; fines from UI 1,000, up to UI 3,000 on repeat; no profit distribution before the last accounts are registered | 2026 | same (art. 97 bis) |
| Beneficial owner: individual holding directly or indirectly at least this share of capital or votes, or otherwise in final control | 15% | 2026 | https://www.impo.com.uy/bases/leyes/19484-2017 (art. 22) |
| Holders of nominative shares or quotas reported to the Banco Central: changes after the first report | Within 45 days (90 days where the holders are non-residents) | 2026 | same (art. 25) |
| BPS: register each new employee (alta) | From 10 days before the start date up to the start date itself | 2026 | https://www.bps.gub.uy/bps/file/10291/13/guia---industria-y-comercio.pdf |

## The base

**Choosing the type.** The practical differences, all from the articles cited:

| Question | SAS | SRL | SA |
|---|---|---|---|
| Can one person form it? | Yes | No | No |
| Who may not form it? | An SA | Anyone may, within 50 partners | Anyone may |
| How are owners' stakes held? | Shares; the statute may cap how much one holder may control (Ley 19.820 art. 15) | Quotas of equal value, not represented by negotiable titles (Ley 16.060 art. 223) | Shares |
| Internal audit body | Not compulsory (Ley 19.820 art. 32) | As the contract provides (art. 226) | Not read for this skill |
| Signing formality | Private or public document; fully online with an advanced electronic signature (Ley 19.820 art. 11) | Contract with the content of arts. 6 and 226 | Statute; constitution by single act or public subscription (art. 280) |
| Accounts | Prepared under adequate accounting standards and registered where required (Ley 19.820 art. 33) | Approved within 180 days; registered where required (arts. 97 and 97 bis) | Same |

**Name.** An SAS's name must differ from existing companies and be followed by "sociedad por acciones simplificada" or "S.A.S." (Ley 19.820 art. 12). An SRL's name must show its type, or partners and signers become jointly and individually liable (Ley 16.060 art. 225).

**What the SAS statute must contain** (Ley 19.820 art. 12): founders' names and identity or tax numbers; name; registered address; duration (no legal cap); object, or "any lawful activity"; subscribed and paid-in capital in pesos, with class, number and value of shares and payment terms; management and at least one legal representative.

**Until registration.** An SAS not yet registered follows the rules for companies in formation; a single founder answers personally and jointly for the company's debts until the process ends (Ley 19.820 art. 13).

**Beneficial owners.** From 1 January 2017 every resident entity must identify its beneficial owners with supporting documents (Ley 19.484 art. 23); non-resident entities with a permanent establishment or effective management in Uruguay have the same duty (art. 24). Companies issuing nominative shares or quotas also report the holders and their percentages to the Banco Central del Uruguay (art. 25). Supporting papers are kept like the statutory books, including the ownership chain (art. 26).

## Deadlines and filing

The steps in the order a founder meets them:

1. **Choose the type and draft the statute or contract** with the contents above.
2. **Sign.** SAS: private or public document, or online with an advanced electronic signature (Ley 19.820 art. 11). SA: pay in at least 25% of the capital into a "Cuenta integración de capital" in a bank and subscribe 50% (Ley 16.060 arts. 280 and 281). SRL: pay in at least 50% of each cash contribution (art. 228).
3. **Register.** SAS: at the Registro de Personas Jurídicas, Sección Registro Nacional de Comercio, within 30 days; the SAS exists from registration (Ley 19.820 art. 11). SRL: once the contract is registered, publish within 60 days an extract with name, partners, capital and quotas, object, term, address and registration details (Ley 16.060 art. 227).
4. **Identify and report the beneficial owners** and, for nominative shares or quotas, the holders, to the Banco Central; report later changes within 45 days, or 90 days for non-resident holders (Ley 19.484 arts. 23 to 25).
5. **Register with DGI and BPS** before starting activity; get a personal BPS user for the owners or representatives and, if needed, delegate permissions ([BPS guide](https://www.bps.gub.uy/bps/file/10291/13/guia---industria-y-comercio.pdf)).
6. **First employee.** Declare the company's wage-council group (Consejos de Salarios), then register the worker in GAFI from 10 days before the start date up to that date; send the monthly nómina and pay the month after ([uruguay-payroll](uruguay-payroll.md)).
7. **Every year.** Prepare the accounts, have them approved within 180 days of year end, and register them with the control body where the thresholds apply (Ley 16.060 arts. 97 and 97 bis); file IRAE ([uy-corporate-income-tax](uy-corporate-income-tax.md)), IVA ([uruguay-iva](uruguay-iva.md)) and pay BPS monthly. No dividend can be paid before the last accounts are registered where registration is required.

## Penalties and interest

- **Accounts not registered**: fines from UI 1,000, up to UI 3,000 on repeat, and no profit distribution until registered (Ley 16.060 art. 97 bis).
- **SRL above 50 partners**: transform into an SA within two years or dissolve (Ley 16.060 art. 223).
- **SRL name without its type**: partners, managers and signers become jointly and individually liable for the act (Ley 16.060 art. 225).
- **Unregistered single-founder SAS**: the founder is personally and jointly liable (Ley 19.820 art. 13).
- **BPS registration and nómina fines**: see [uruguay-payroll](uruguay-payroll.md).

## Cross-border points

- **Foreign founders** may form any of the three types; an SAS may also be formed by a foreign legal person other than an SA, giving its foreign tax number in place of a RUT (Ley 19.820 arts. 11 and 12).
- **Non-resident entities with effective management or a permanent establishment in Uruguay** must identify their beneficial owners like resident entities (Ley 19.484 art. 24).
- **Dividends to foreign shareholders** are taxed in IRNR; see [uy-cross-border](uy-cross-border.md).

## Two worked examples that recompute

### Example 1: which type needs the least cash at signing for UYU 400,000 of capital

Ana and Bruno want a company with UYU 400,000 of capital, all in cash. How much must they pay in when they sign?

- **SAS:** at least 10% = UYU 40,000; the remaining UYU 360,000 within 24 months.
- **SA (single act):** at least 25% paid in = UYU 100,000, with at least 50% (UYU 200,000) subscribed.
- **SRL:** each partner pays at least 50% of their cash contribution = UYU 200,000 in total; the rest within two years.

The decision: the SAS needs the least cash on day one (UYU 40,000), and Ana could even form it alone. The SRL needs five times as much up front and at least two partners. If the founders want quotas that cannot be traded and expect fewer than 50 partners, the SRL still works, but it ties up UYU 160,000 more at signing than the SAS.

```oa-check
name: Cash at signing for UYU 400,000 of cash capital, SAS, SA and SRL
inputs:
  capital: 400000
steps:
  - sas_at_signing: capital * 0.10
  - sas_balance: capital - sas_at_signing
  - sa_at_signing: capital * 0.25
  - sa_subscribed_min: capital * 0.50
  - srl_at_signing: capital * 0.50
  - srl_minus_sas: srl_at_signing - sas_at_signing
expected:
  sas_at_signing: 40000.00
  sas_balance: 360000.00
  sa_at_signing: 100000.00
  sa_subscribed_min: 200000.00
  srl_at_signing: 200000.00
  srl_minus_sas: 160000.00
```

## Ask the client first

1. How many founders, who they are (individuals, companies, an SA?), and whether any is non-resident.
2. The activity, and whether a law requires a specific company type or bars the SAS (public offer, State shareholder).
3. Capital: amount, cash or in kind, and how fast the founders can pay it in.
4. Who will be the beneficial owners (15% test) and whether shares or quotas will be nominative.
5. Expected income and assets in the first years (SAS oversight at UI 37,500,000 of income; control of non-cash contributions at UI 4,000,000 of income or UI 2,500,000 of Uruguayan assets).
6. Will there be employees from the start, and in which wage-council group?

## Sources

| Source | URL | Read on |
|---|---|---|
| Ley 19.820, IMPO consolidated text: Title II arts. 8 to 15 and 32 to 34 read (SAS concept, limits, oversight, constitution, statute contents, capital, controls) | https://www.impo.com.uy/bases/leyes/19820-2019 | 2026-11-11 |
| Ley 16.060, IMPO consolidated text: arts. 1, 97, 97 bis, 223 to 231, 279 to 281 read (definition, accounts, SRL, SA capital) | https://www.impo.com.uy/bases/leyes/16060-1989 | 2026-11-11 |
| Ley 19.484, IMPO consolidated text: arts. 22 to 26 read (beneficial owners, reporting to the Banco Central) | https://www.impo.com.uy/bases/leyes/19484-2017 | 2026-11-11 |
| BPS, Guía de obligaciones Industria y Comercio (January 2025 edition, page updated 21 May 2026), all pages read: personal BPS user, alta deadline, nómina, payment | https://www.bps.gub.uy/bps/file/10291/13/guia---industria-y-comercio.pdf | 2026-11-11 |

Not yet confirmed: whether an SA or SRL can be formed online like an SAS; registry, publication and notary costs and typical timings (the old file's "days" for an SAS and "around 30 days" for an SA or SRL had no official source); the DGI registration (RUT) procedure and forms; the asset and income levels and terms for registering accounts with the AIN (set by regulation, not read); the SA shareholder liability and balance-payment rules, and whether an SA may continue with a single shareholder; whether the bearer share rules of Ley 18.930 still apply; the 2026 UI value for converting the SAS thresholds; whether the company must file the annual Impuesto al Patrimonio (net wealth tax) return (carried from the old file, Texto Ordenado 1996, not read); the publication channels (Diario Oficial and a newspaper) for an SA or SRL extract (carried from the old file, not read).

> Contributed by OpenAccountants.
