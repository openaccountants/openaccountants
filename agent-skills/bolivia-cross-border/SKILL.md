---
name: bolivia-cross-border
description: "Bolivia cross-border tax for 2026: what a Bolivian payer withholds when it pays, credits or remits Bolivian-source income abroad, and which treaty or Andean Community rule changes it. Covers the IUE-BE (Impuesto sobre las Utilidades de las Empresas, Beneficiarios del Exterior) of 25% on a presumed 50% profit, so 12.5% of the gross, final, under Ley 843 art. 51 and DS 24051 art. 34; what counts as Bolivian source (services from abroad, royalties, interest, rents, directors' fees); branch profits presumed remitted; deadlines by NIT digit and Forms 530 and 591; whether IVA and IT reach services bought from abroad; the Andean Community Decision 578 for Colombia, Ecuador and Peru; and the six bilateral treaties the SIN publishes (Argentina, Germany, Spain, France, Sweden, United Kingdom). Trigger on: IUE-BE, beneficiarios del exterior, remesas al exterior, Formulario 530, Formulario 591, pago al exterior Bolivia, Decisión 578, convenio doble tributación Bolivia, withholding tax Bolivia, pay"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/bolivia-cross-border"
  jurisdiction: "BO"
  tax_year: "2026"
  last_updated: "2026-11-11"
---

# Bolivia cross-border tax: IUE-BE on payments abroad, Decision 578 and treaties (2026) v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

The law is Ley N° 843 (Texto Ordenado), Título III (IUE), art. 51, with its regulation DS 24051 arts. 4 and 34, read in the SIN's consolidated edition "Ley N° 843 y Decretos Reglamentarios, Texto Ordenado, actualizado al 30/09/2026". The Código Tributario is Ley N° 2492, in the SIN consolidated edition to the same date. The Andean Community rule is Decision 578 of 4 May 2004. The bilateral treaties are those the Servicio de Impuestos Nacionales (SIN) lists on its "Convenios de doble tributación" page. All amounts are in bolivianos (Bs). Tax year 2026 (calendar year for withholdings, which are monthly).

This skill owns the cross-border withholding and the treaty and Decision 578 rules. It links to the sibling skills for figures they own: the IUE rate and the reinvestment rates ([bolivia-corporate-income-tax](bolivia-corporate-income-tax.md)), IVA and IT ([bolivia-iva](bolivia-iva.md)), individuals including non-domiciled workers ([bolivia-income-tax](bolivia-income-tax.md)) and related-party pricing ([bolivia-transfer-pricing](bolivia-transfer-pricing.md)).

## Who this applies to

- **Anyone in Bolivia who pays, credits or remits Bolivian-source income to a beneficiary abroad** (Ley 843 art. 51; DS 24051 art. 34): companies, branches, sole-owner businesses, the State and individuals. The payer is the withholding agent (agente de retención, Ley 2492 art. 25). It must withhold even if the foreign party will not accept a deduction; if it does not withhold, it answers for the tax jointly with the beneficiary.
- **What is Bolivian source** (Ley 843 arts. 42 and 44; DS 24051 art. 4):
  - income from goods located or economically used in Bolivia, from acts or activities carried out in Bolivia, or from events inside Bolivia, whatever the nationality or residence of the parties and wherever the contract was signed (art. 42);
  - pay of directors and board members for work done abroad for companies domiciled in Bolivia (art. 44 a);
  - fees for services of any kind performed from or in a foreign country, when linked to earning Bolivian-source profit (art. 44 b), and in particular consultancy, advice of every kind, technical assistance, research, professional services and expert reports done from or in a foreign country (DS 24051 art. 4 e);
  - rents from real estate in Bolivia, interest on deposits in Bolivia, interest on public securities, rentals of movables used in Bolivia, royalties from things or rights used economically in Bolivia (DS 24051 art. 4 a and b).
- **Branches of foreign companies.** Their profits are presumed distributed to the head office on the due date for filing their financial statements, net of earlier losses, whatever the date funds actually leave (DS 24051 art. 34). IUE-BE is due then.
- **Out of scope here:** the branch's or subsidiary's own IUE ([bolivia-corporate-income-tax](bolivia-corporate-income-tax.md)); pay for employees and individuals who are not domiciled in Bolivia but work in Bolivia ([bolivia-income-tax](bolivia-income-tax.md), the 13% RC-IVA rule for non-domiciled individuals); customs duties on imported goods.

**When to refer.** Refer for: a claim that a treaty's business-profits article removes Bolivian tax on service fees (the SIN form for treaty relief names "dividends or other concepts"; its practice on service fees was not read); permanent-establishment questions; the most-favoured-nation clauses in the UK, French and Swedish treaties; interest on public debt and other special exemptions (Ley 1613 arts. 13 and 17, reproduced under Ley 843 art. 51); and any payment to a country on the SIN's low-tax list (see [bolivia-transfer-pricing](bolivia-transfer-pricing.md)).

## Rates, bands and thresholds

Quick answer: **withhold 12.5% of the gross amount paid abroad**, as a final tax. That is 25% (the IUE rate) on a profit the law presumes to be 50% of the gross. A treaty can lower it only where its cap is below 12.5%. IVA and IT do not apply to a service performed abroad.

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| IUE-BE: presumed net profit on Bolivian-source income paid or remitted abroad (Ley 843 art. 51), no proof to the contrary admitted | 50% of the total paid or remitted | 2026 | https://www.impuestos.gob.bo/wp-content/uploads/2026/10/1.-LEY-N%C2%B0-843-09-26-1.pdf |
| IUE-BE rate on that presumed profit, withheld as a single and final payment (art. 51) | 25%: so 12.5% of the gross | 2026 | same |
| IUE-BE on dividends or branch profits partly reinvested by capitalisation (Ley 1613 art. 10 kept by Ley 1705; DS 5563 art. 3 III) | Lower rates on the part not capitalised; the rates are in [bolivia-corporate-income-tax](bolivia-corporate-income-tax.md) | 2026 | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/281098 |
| Deadline to pay the IUE-BE withheld (DS 24051 art. 34; DS 5563 art. 3 V) | Month after the payment, credit or remittance: day 13 (NIT ending 0) to day 22 (NIT ending 9) | 2026 | https://www.impuestos.gob.bo/wp-content/uploads/2026/10/1.-LEY-N%C2%B0-843-09-26-1.pdf |
| IVA on services (Ley 843 art. 1 b) | Reaches only works and services performed in Bolivia; no reverse charge on services performed abroad was found in Título I or DS 21530 | 2026 | same |
| IT, 3% on gross income (Ley 843 art. 72) | Reaches only activity carried on in Bolivia; no IT on services bought from abroad was found in Título VI or DS 21532 | 2026 | same |
| Failure to withhold: omission of payment fine (Ley 2492 art. 165, text of Ley 1448) | 60% of the updated tax not withheld, plus the tax and interest | 2026 | https://www.impuestos.gob.bo/wp-content/uploads/2026/10/2.-LEY-N%C2%B0-2492-09-26-2.pdf |
| Andean Community, Decision 578 art. 11: dividends | Taxable only where the paying company is domiciled: Bolivia keeps its IUE-BE | 2026 | https://www.impuestos.gob.bo/wp-content/uploads/2025/09/decision-578.pdf |
| Decision 578 art. 10: interest | Taxable only where the payment is charged and recorded | 2026 | same |
| Decision 578 art. 9: royalties | Taxable only where the intangible is used | 2026 | same |
| Decision 578 art. 14: professional, technical, technical-assistance and consultancy services of enterprises | Taxable only where the benefit arises, presumed to be where the expense is charged and recorded | 2026 | same |
| Decision 578 art. 13: personal services of employees and professionals | Taxable only where the services are performed | 2026 | same |
| Spain treaty art. 10: dividends to a company (not a partnership) holding at least 25% directly | Cap 10% of the gross dividend | 2026 | https://www.hacienda.gob.es/sgt/normativadoctrina/tributaria/cdi/boe_bolivia.pdf |
| Spain treaty art. 10: other dividends; arts. 11 and 12: interest and royalties | Cap 15% | 2026 | same |
| United Kingdom treaty arts. 10, 11 and 12: dividends, interest and royalties | Cap 15%; the lower domestic rate applies where it is lower (exchange of notes, point 4 a) | 2026 | https://assets.publishing.service.gov.uk/media/5a817797e5274a2e87dbdc94/bolivia-dtc_-_in_force.pdf |
| Sweden treaty art. 10: dividends to a company holding at least 25% of the capital | Exempt in Bolivia | 2026 | https://www.impuestos.gob.bo/wp-content/uploads/2025/09/convenio-bolivia-suecia.pdf |
| Sweden treaty art. 10: other dividends; arts. 11 and 12: interest and royalties | Cap 15% | 2026 | same |
| Germany treaty art. 10 (1) b): dividends paid by a Bolivian company; arts. 11 and 12: interest and royalties | Cap 15%; the lower domestic rate applies where it is lower (protocol point 6) | 2026 | https://www.impuestos.gob.bo/wp-content/uploads/2025/09/convenio-bolivia-alemania.pdf |
| France treaty arts. 10, 11 and 12: dividends, interest and royalties | Cap 15% | 2026 | https://www.impuestos.gob.bo/wp-content/uploads/2025/09/convenio-bolivia-francia.pdf |
| Argentina treaty arts. 10 and 11: interest and dividends | Taxable only in the State where the credit is used or the paying company is domiciled: Bolivia keeps its IUE-BE | 2026 | https://www.impuestos.gob.bo/wp-content/uploads/2025/09/convenio-bolivia-argentina.pdf |

The Swedish, German, French and Argentine texts on the SIN site are scanned images; their rows were read from the scans.

## The base

**Step 1: is the payment Bolivian-source?** Use the source rules under "Who this applies to". The test is where the goods are used, where the activity happens, or (for services from abroad) whether the service is linked to earning Bolivian-source profit. A Bolivian company buying a foreign consultant's report for its own business is paying Bolivian-source income, even though the work was done abroad (art. 44 b; DS 24051 art. 4 e). Foreign-source income is outside the IUE (art. 42), so nothing is withheld.

**Step 2: the base is the gross amount paid, credited or remitted.** No deduction of the foreign party's costs is allowed: the 50% profit is presumed "sin admitir prueba en contrario" (art. 51). The tax is 25% of 50%, so 12.5% of the gross. If the contract says the foreign party receives a fixed net sum and the Bolivian payer bears the tax, the gross is the net divided by 0.875, and the tax is 12.5% of that gross.

**Step 3: what the withholding does.** The withholding is the foreign beneficiary's final Bolivian tax ("pago único y definitivo", art. 51). The payer owes it to the SIN from the moment of payment, credit or remittance (DS 24051 art. 34), not only when cash leaves Bolivia. The SIAT Form 530 consolidates every remittance of the month (box 13 amounts remitted for interest and services; box 26 = box 13 x 50%; box 909 tax determined).

**Step 4: the payer's own deduction.** Fees for advice, management or services from abroad are deductible for the payer's IUE only if backed by an invoice or proof that the tax due was withheld when the income is Bolivian-source (DS 24051 art. 12 f, text of DS 4850). Without the IUE-BE withholding the expense is at risk. Bolivian IVA credit needs a Bolivian invoice, which a foreign supplier does not issue.

**Step 5: IVA and IT.** The IVA reaches sales of movables in Bolivia, works and services performed in Bolivia, and definitive imports (Ley 843 art. 1). Goods imported pay IVA at customs (art. 4 d; see [bolivia-iva](bolivia-iva.md)). For services performed abroad, no rule in Título I or DS 21530 (consolidated to 30 September 2026) makes the Bolivian buyer self-assess IVA, and the IT reaches only activity carried on in Bolivia (art. 72). So the cross-border cost of a service bought from abroad is the IUE-BE alone. This is a reading of the consolidated texts; a later rule outside them would change it (see "Not yet confirmed").

**Step 6: dividends and branch profits.** A dividend paid by a Bolivian company to a foreign shareholder, and a branch's profit (presumed remitted on the due date of its financial statements), bear IUE-BE at 12.5% of the amount. Capitalised reinvestment lowers the rate on the part not capitalised; the rates and the reserve conditions are in [bolivia-corporate-income-tax](bolivia-corporate-income-tax.md). If the reserve is later distributed or not reinvested, the tax becomes omitted tax with interest under Ley 2492 art. 47 (DS 5563 art. 3 IV).

**Step 7: does a treaty or Decision 578 lower it?** Treaties approved by the legislature rank above the Código Tributario and the laws (Ley 2492 art. 5 I). The Andean Community decision applies to people domiciled in Colombia, Ecuador and Peru (see "Cross-border points"). Compare the treaty cap with 12.5%:

- **Cap below 12.5%:** Spain, a company holding at least 25% (10% on dividends); Sweden, a company holding at least 25% (dividends exempt). Use Form 591; the SIAT computes both and keeps the lower (box 26 = 25% x 50% x box 13; box 39 = box 13 x treaty %; box 909 the lower).
- **Cap of 15% or more:** the domestic 12.5% is already lower. The UK exchange of notes (point 4 a) and the German protocol (point 6) say so expressly. Withhold 12.5% on Form 530.
- **Allocation to the source State only** (Decision 578 and the 1976 Argentina treaty for dividends and interest): Bolivia keeps its full IUE-BE; relief, if any, is given by the other State.

## Deadlines and filing

**Steps, in the order the filer meets them** (SIN, SIAT form pages for Forms 530 and 591):

1. Before paying, decide whether the payment is Bolivian-source and whether a treaty or Decision 578 applies. Keep proof of the beneficiary's residence and, for a treaty claim, that it is the beneficial owner.
2. Register each remittance individually in the SIAT **Módulo de Pagos Anticipados**. Each registered remittance can be paid on its own, so the payment can be shown abroad.
3. File **Form 530** (IUE-BE) in the SIAT online, consolidating the month's remittances: box 13 amounts remitted for interest and services; box 26 presumed net profit (box 13 x 50%); for dividends, box 484 the dividend, box 481 the amount reinvested, box 482 the amount actually remitted and box 483 the presumed profit on it; box 909 tax determined; boxes 622 and 640 payments on account; box 996 balance due.
4. Where a ratified treaty caps the tax below the IUE-BE, file **Form 591** instead for those remittances: box 13 amount remitted; box 26 the domestic tax; box 39 the treaty tax; box 909 the lower; box 996 balance due.
5. Pay by the NIT-digit day of the month after the payment, credit or remittance: NIT ending 0, day 13; 1, day 14; 2, day 15; 3, day 16; 4, day 17; 5, day 18; 6, day 19; 7, day 20; 8, day 21; 9, day 22 (DS 24051 art. 34).
6. For a branch, the remittance is presumed on the due date of the financial statements, 120 days after the year-end (see [bolivia-corporate-income-tax](bolivia-corporate-income-tax.md)); file and pay Form 530 in the following month.
7. Keep Form 530 or 591 and the payment as support for the payer's IUE deduction (DS 24051 art. 12 f).

## Penalties and interest

- **Not withholding** is omission of payment: a fine of 60% of the updated tax not withheld (Ley 2492 art. 165), and the payer answers for the tax jointly with the beneficiary (art. 25 point 4). Paying early in the procedure reduces or extinguishes the fine (arts. 156 and 157); the reductions are in [bolivia-corporate-income-tax](bolivia-corporate-income-tax.md).
- **Late payment** of tax withheld: the debt is fixed in UFV at the due date and carries interest under Ley 2492 art. 47 (rates in [bolivia-corporate-income-tax](bolivia-corporate-income-tax.md)).
- **Late or missing Form 530 or 591** is a breach of a formal duty under art. 162 (50 to 5,000 UFV, the amount set by SIN regulation).

## Cross-border points

**Andean Community, Decision 578.** It applies to persons domiciled in a member country, for income and wealth taxes; for Bolivia it names the "Impuesto a la renta" (art. 1), which covers the IUE and the IUE-BE. The text names Bolivia, Colombia, Ecuador, Peru and Venezuela as member countries (art. 2 a). The general rule is that income is taxed only in the member country where its source is, and the others must treat it as exempt (art. 3). What it means for a Bolivian payer:

| Income paid by a Bolivian payer to a resident of Colombia, Ecuador or Peru | Who taxes (Decision 578) | Bolivian IUE-BE |
|---|---|---|
| Dividends (art. 11) | Only Bolivia, where the paying company is domiciled; the other country may not tax the receiving company | 12.5% (reinvestment rates may apply) |
| Interest (art. 10) | Only where the payment is charged and recorded: Bolivia when the Bolivian payer books it | 12.5% |
| Royalties (art. 9) | Only where the intangible is used: Bolivia when used in Bolivia | 12.5% |
| Technical, professional, technical-assistance or consultancy services of an enterprise (art. 14) | Only where the benefit arises, presumed to be where the expense is charged and recorded: Bolivia when the Bolivian payer books the expense | 12.5% |
| Personal services of an employee or professional (art. 13) | Only where the services are performed: if performed wholly outside Bolivia, Bolivia may not tax them | Refer: the treaty rule and Bolivian source rule (art. 44 b) point different ways |
| Business profits (art. 6) | Only where the activity is carried out (an office, branch, works, agent and the other places listed) | Not a withholding case; the branch files IUE |
| Transport enterprises (art. 8) | Only where the enterprise is domiciled | Refer |

Decision 578 also obliges the tax administrations to exchange information and assist each other in collection (arts. 19 and 21) and allows each country to apply its own anti-avoidance law (art. 20).

**Bilateral treaties.** The SIN publishes six: Argentina, Germany, Spain, France, Sweden and the United Kingdom. The caps for dividends, interest and royalties are in the rates table. Three points:

- **Domestic law is often lower.** With IUE-BE at 12.5% of the gross, a 15% cap gives no relief. The treaties matter where the cap is lower (Spain and Sweden for 25% corporate holdings) and where a treaty article takes the income out of Bolivian tax altogether (for example business profits without a permanent establishment). Refer for the second.
- **Most-favoured-nation clauses.** The UK exchange of notes (point 4 b), the French protocol and the Swedish protocol (interest and royalties) say that if Bolivia agrees a lower rate with another OECD member, that lower rate applies to them. Spain and Sweden are OECD members with lower dividend rates. Refer before applying a rate through these clauses.
- **No treaty with the United States, Brazil, Chile or most other trading partners** appears on the SIN list: payments to them bear the full 12.5%.

**Residents' foreign income.** The IUE taxes only Bolivian-source profit (art. 42), so a Bolivian company's foreign-source income is outside the base ([bolivia-corporate-income-tax](bolivia-corporate-income-tax.md)). There is therefore little double taxation for Bolivia to relieve, and the treaties' relief articles mostly bind the other State.

**Transfer pricing.** Payments to a related party abroad must also be at arm's length ([bolivia-transfer-pricing](bolivia-transfer-pricing.md)). The IUE-BE applies whatever the price.

## Two worked examples that recompute

### Example 1: SRL pays a US software consultant, with and without gross-up

Andes Logística SRL (NIT ending 4) pays a US consulting firm Bs 70,000 in March 2026 for a system design done entirely in the US for its Bolivian operations. There is no treaty with the US.

- Source: consultancy done from abroad and linked to Bolivian-source profit is Bolivian-source (Ley 843 art. 44 b; DS 24051 art. 4 e).
- IUE-BE: 70,000 x 50% x 25% = Bs 8,750. The SRL pays Bs 61,250 to the consultant and Bs 8,750 to the SIN on Form 530 by 17 April 2026.
- No IVA and no IT on the service (performed abroad).
- The edge, gross-up: if the contract promises the consultant Bs 70,000 net, the gross is 70,000 / 0.875 = Bs 80,000 and the IUE-BE is Bs 10,000. The SRL's cost and IUE deduction are Bs 80,000.

```oa-check
name: Andes Logistica SRL, Bs 70,000 consultancy from the US, net and grossed-up (2026)
inputs:
  paid: 70000
steps:
  - presumed_profit: paid * 0.50
  - iue_be: presumed_profit * 0.25
  - net_to_consultant: paid - iue_be
  - effective_rate: iue_be / paid
  - grossed_up: paid / (1 - 0.125)
  - iue_be_grossed: grossed_up * 0.125
expected:
  presumed_profit: 35000
  iue_be: 8750
  net_to_consultant: 61250
  effective_rate: 0.125
  grossed_up: 80000
  iue_be_grossed: 10000
```

### Example 2: dividend to a Spanish parent: treaty rate or reinvestment? Worked both ways

Altiplano Foods SA declares a dividend of Bs 1,000,000 from its 2025 profit. 30% of its shares are held directly by Ibérica Alimentos SA, a Spanish company (not a partnership). Its share is Bs 300,000. The rest is held in Bolivia.

- **Option A, remit it all.** Domestic IUE-BE 12.5% = Bs 37,500. The Spain treaty caps dividends to a company holding at least 25% at 10% (art. 10 a) = Bs 30,000, which is lower, so file Form 591: tax Bs 30,000, cash to Spain Bs 270,000.
- **Option B, capitalise 75% and remit 25%.** Ibérica capitalises Bs 225,000 into a reserve for fixed assets, inventories or investment in the same business by the end of the next IUE year (DS 5563 art. 3 I). The Bs 75,000 not capitalised bears 3.125% (rate in [bolivia-corporate-income-tax](bolivia-corporate-income-tax.md)): Bs 2,343.75. The treaty cap on Bs 75,000 is Bs 7,500, higher, so the domestic rate applies on Form 530. Cash to Spain Bs 72,656.25.
- **What decides it** is whether the parent needs the cash now. Option B costs Bs 27,656.25 less tax, but Bs 225,000 stays in Bolivia and is taxed as omitted tax with interest if the reserve is later paid out or not reinvested.
- The edge: had Ibérica held 20%, the 10% rate would not apply; the treaty cap would be 15%, above 12.5%, so Option A would cost 12.5%.

```oa-check
name: Altiplano Foods SA, dividend to a 30% Spanish parent, Spain treaty vs 75% reinvestment (2026)
inputs:
  dividend_total: 1000000
  share: 0.30
steps:
  - to_spain: dividend_total * share
  - domestic_a: to_spain * 0.125
  - treaty_a: to_spain * 0.10
  - tax_a: min(domestic_a, treaty_a)
  - cash_a: to_spain - tax_a
  - capitalised: to_spain * 0.75
  - remitted_b: to_spain - capitalised
  - domestic_b: remitted_b * 0.03125
  - treaty_b: remitted_b * 0.10
  - tax_b: min(domestic_b, treaty_b)
  - cash_b: remitted_b - tax_b
  - tax_saving_b: tax_a - tax_b
expected:
  to_spain: 300000
  domestic_a: 37500
  treaty_a: 30000
  tax_a: 30000
  cash_a: 270000
  capitalised: 225000
  remitted_b: 75000
  domestic_b: 2343.75
  treaty_b: 7500
  tax_b: 2343.75
  cash_b: 72656.25
  tax_saving_b: 27656.25
```

## Ask the client first

1. What is paid, to whom, and where the work or the asset is: a service done abroad, a royalty, interest, rent, a dividend, a branch profit, directors' fees. This decides whether it is Bolivian-source.
2. The beneficiary's country of residence and, for a company receiving dividends, its percentage holding and legal form (company or partnership). This decides Decision 578 or a treaty and the treaty rate.
3. Whether the contract price is gross or net of Bolivian tax (gross-up).
4. For dividends and branch profits: how much will be capitalised and into what assets, and the year-end.
5. The payer's NIT last digit (payment day) and the month of each payment, credit or remittance.
6. Whether the beneficiary is a related party or in a low-tax country on the SIN list (transfer pricing).

## Sources

| Source | URL | Read on |
|---|---|---|
| SIN, Ley N° 843 y Decretos Reglamentarios, Texto Ordenado, actualizado al 30/09/2026: read Título I arts. 1 to 4 (IVA object and taxable event), Título III arts. 42, 44 and 51 with the related Ley 1613 notes, DS 24051 arts. 4, 12 and 34, Título VI art. 72, and searched DS 21530 and DS 21532 for any rule on services from abroad (none found) | https://www.impuestos.gob.bo/wp-content/uploads/2026/10/1.-LEY-N%C2%B0-843-09-26-1.pdf | 2026-11-11 |
| SIN, Ley N° 2492 Código Tributario Boliviano, Texto Ordenado, actualizado al 30/09/2026: read arts. 5, 25 and 165 | https://www.impuestos.gob.bo/wp-content/uploads/2026/10/2.-LEY-N%C2%B0-2492-09-26-2.pdf | 2026-11-11 |
| Gaceta Oficial, Decreto Supremo N° 5563 of 2 March 2026 (HTML text): read arts. 2 and 3 | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/281098 | 2026-11-11 |
| SIN, Convenios de doble tributación: the page listing the six treaties and Decision 578 | https://www.impuestos.gob.bo/index.php/convenios-de-doble-tributacion/ | 2026-11-11 |
| SIN copy of Andean Community Decision 578 (text PDF): read arts. 1 to 22 | https://www.impuestos.gob.bo/wp-content/uploads/2025/09/decision-578.pdf | 2026-11-11 |
| Spain, Ministerio de Hacienda, Spain-Bolivia convention of 30 June 1997 as published in the BOE of 10 December 1998: read arts. 10, 11 and 12 | https://www.hacienda.gob.es/sgt/normativadoctrina/tributaria/cdi/boe_bolivia.pdf | 2026-11-11 |
| GOV.UK, UK-Bolivia double taxation convention signed 3 November 1994 and exchange of notes: read arts. 7, 10, 11, 12 and 28 and the notes, point 4 | https://assets.publishing.service.gov.uk/media/5a817797e5274a2e87dbdc94/bolivia-dtc_-_in_force.pdf | 2026-11-11 |
| SIN copy (scanned) of the Bolivia-Sweden convention: read art. 10 and the protocol, by OCR of the scan | https://www.impuestos.gob.bo/wp-content/uploads/2025/09/convenio-bolivia-suecia.pdf | 2026-11-11 |
| SIN copy (scanned) of the Bolivia-Germany convention: read arts. 10, 11 and 12 and protocol point 6, by OCR of the scan | https://www.impuestos.gob.bo/wp-content/uploads/2025/09/convenio-bolivia-alemania.pdf | 2026-11-11 |
| SIN copy (scanned) of the Bolivia-France convention: read arts. 10, 11 and 12 and the protocol, by OCR of the scan | https://www.impuestos.gob.bo/wp-content/uploads/2025/09/convenio-bolivia-francia.pdf | 2026-11-11 |
| SIN copy (scanned) of the Bolivia-Argentina convention: read arts. 9 to 12, by OCR of the scan | https://www.impuestos.gob.bo/wp-content/uploads/2025/09/convenio-bolivia-argentina.pdf | 2026-11-11 |
| SIN SIAT, Form 530 IUE-BE: box names, codes and formulas (13, 26, 481 to 484, 909, 622, 640) and the Módulo de Pagos Anticipados | https://siatinfo.impuestos.gob.bo/index.php/declaraciones-juradas-en-formato-electronico/impuesto-a-las-utilidades-de-las-empresas/530-iue-beneficiarios-del-exterior | 2026-11-11 |
| SIN SIAT, Form 591 IUE remittances under international conventions: purpose and boxes 13, 26, 39, 909, 996 | https://siatinfo.impuestos.gob.bo/index.php/declaraciones-juradas-en-formato-electronico/impuesto-a-las-utilidades-de-las-empresas/591-iue-remesas-al-exterior-segun-convenios-internacionales | 2026-11-11 |

Not yet confirmed: any rule outside the consolidated Ley 843 text (to 30 September 2026) that taxes services or digital services bought from abroad with IVA or IT; the SIN's documentary requirements for a treaty claim on Form 591 (residence certificate, beneficial ownership) and its practice on service fees under treaty business-profits articles; the entry-into-force dates and current status of the Argentina, Germany, France and Sweden conventions (read from scans that were partly illegible); the French protocol's point 5 on technical services and royalties, which the scan shows only in part; whether Decision 578 still binds Venezuela, which the decision names as a member; how the most-favoured-nation clauses in the UK, French and Swedish treaties interact with the Spanish 10% and Swedish 0% dividend rates; the UFV value in bolivianos on any date (Banco Central de Bolivia, not read).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-11. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `bolivia-cross-border` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/bolivia-cross-border. If neither is available, confirm every figure against the official source pages cited above before relying on it.
