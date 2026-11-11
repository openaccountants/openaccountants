---
name: ec-cross-border
description: "Ecuador cross-border tax for 2026: what happens in income tax and in the currency outflow tax (Impuesto a la Salida de Divisas, ISD) when money, income or people cross the border. Covers Ecuadorian-source income of non-residents (LRTI art. 8), the permanent establishment test (RLRTI art. 9), withholding on payments abroad at the 25% company rate and 37% to tax havens, lower-tax jurisdictions and preferential regimes (LRTI art. 39; Res. NAC-DGERCGC26-00000009), interest, reinsurance and payments abroad that are not withheld (LRTI arts. 13, 32), dividends to non-residents at 10% (12% or 14% in the listed cases), shows by non-residents, the tax-haven test, treaty relief and the residence certificate, the foreign tax credit, and ISD at 5% (Ley Reformatoria para la Equidad Tributaria arts. 155 to 162) with its 2026 differentiated rates for imports, exemptions, presumptions and credit. Trigger on: pagos al exterior, retención no residentes, impuesto a la salida de divisas, ISD 5%, paraíso fiscal 37%, dividendos al exterior, convenio doble imposición Ecuador, certificado de residencia fiscal, establecimiento permanente Ecuador, paying a foreign supplier from Ecuador. Out of scope: company rates and the dividend tax in detail (ec-corporate-income-tax), individuals' residence and return (ecuador-income-tax), IVA on imported services (ecuador-iva), transfer pricing (ec-transfer-pricing), treaty-by-treaty rates."
version: 0.1
jurisdiction: EC
tax_year: 2026
last_updated: 2026-11-11
depends_on:
  - income-tax-workflow-base
category: cross-border
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
type: situation-rules
---

# Ecuador: cross-border tax (2026) v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

This skill covers the income tax and ISD rules that apply when an Ecuadorian payer sends money abroad, when a non-resident earns income in Ecuador, and when a resident is taxed abroad. Detail lives in the sibling skills, which this skill links and does not repeat:

- [ec-corporate-income-tax](ec-corporate-income-tax.md): the 25% rate, the dividend single tax (12%, 10% to non-residents, 14%), the 10% tax on share sales and the indirect-sale thresholds.
- [ecuador-income-tax](ecuador-income-tax.md): residence of individuals (183 days, centre of interests, temporary tax residence) and non-resident individuals at 25%.
- [ecuador-iva](ecuador-iva.md): IVA on imported services and digital services (self-assessed, 100% withholding).
- [ec-transfer-pricing](ec-transfer-pricing.md): related-party payments abroad.
- [ecuador-payroll](ecuador-payroll.md): foreign workers on an Ecuadorian payroll.

**Quick reference (2026).** Payments abroad of Ecuadorian-source income with no specific rate: 25% withholding (the company rate). To a recipient in a tax haven, lower-tax jurisdiction or preferential regime: 37% (the top individual rate). Dividends to non-residents: 10%. ISD on money sent abroad: 5%; 0% or 2.5% on listed imports in 2026; dividends to non-residents are exempt from ISD unless an Ecuadorian resident sits in the ownership chain. Withholdings are declared and paid next month by the ninth digit of the RUC.

**Which texts.** The LRTI (SRI codification, last reform 1 April 2026), the RLRTI (last reform 18 November 2025), SRI Resolution NAC-DGERCGC26-00000009 (withholding rates, applicable from 1 March 2026), the Ley Reformatoria para la Equidad Tributaria en el Ecuador (RO Supl. 242 of 29 December 2007, SRI copy with last reform 25 March 2024; ISD is in arts. 155 to 163), Decreto Ejecutivo 272 of 30 December 2025 (ISD differentiated rates for 2026, in force from 1 January 2026) and the SRI ISD page.

## Who this applies to

- **Payers in Ecuador** (companies, permanent establishments, individuals keeping accounts) who pay or credit amounts abroad that are taxable income in Ecuador for the recipient, directly, by set-off or through financial intermediaries. They are withholding agents (LRTI art. 48).
- **Non-residents** with Ecuadorian-source income not attributable to a permanent establishment. They are taxed by withholding on each payment (LRTI art. 39). Income attributable to a permanent establishment is taxed in the PE's own return (see ec-corporate-income-tax).
- **Residents** (individuals and companies) on foreign income: taxed in Ecuador on worldwide income with credit for foreign tax (LRTI arts. 2, 49; RLRTI art. 136).
- **Anyone who sends money abroad** for ISD: individuals, estates and private companies, Ecuadorian or foreign, that transfer, send or carry money abroad, or fall under the ISD presumptions (Ley Reformatoria para la Equidad Tributaria art. 158). Banks, the Banco Central and couriers withhold or collect it.
- **Not subject to ISD**: state bodies and public companies, international organisations and diplomatic missions with their accredited foreign officials, and public-debt service (article after art. 156).
- **Out of scope**: treaty-by-treaty rates, the Andean Community regime (CAN Decision 578), mining and hydrocarbon contracts, and IVA (ecuador-iva).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Payment abroad of Ecuadorian-source income with no specific withholding rate (services occasionally provided in Ecuador, royalties, fees, interest not covered below, other payments that are not dividends) | 25%, the general company rate, on the total paid or credited | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/12c884d5-c8d9-4171-becc-1513b990b87a/LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (LRTI arts. 37, 39); https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/272ca6a9-d679-4b4e-8da0-fb4671cf5f8f/NAC-DGERCGC26-00000009_Ret_IR.pdf (art. 4) |
| Same payment to a person resident, incorporated or located in a tax haven or lower-tax jurisdiction, or under a preferential regime | 37%, the top rate for individuals | 2026 | same (LRTI art. 39; Res. art. 4); top rate from https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar?id=bb7aac3c-251d-4243-9477-10a3ba8e7355&nombre=NAC-DGERCGC25-00000043.pdf |
| Dividends from an Ecuadorian company to a non-resident | 10%; 12% if the distributing company's beneficial owner is an Ecuadorian tax resident; 14% if a tax-haven resident sits at any level of the chain and the beneficial owner is Ecuadorian, or if the company failed to report its ownership | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/12c884d5-c8d9-4171-becc-1513b990b87a/LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (LRTI art. 39.2(4), (5)); detail in ec-corporate-income-tax |
| Interest on loans from foreign financial institutions, qualified specialised non-financial lenders, government-to-government or multilateral credit | not subject to income tax or withholding, and deductible, up to the maximum referential rate of the Junta de Política y Regulación Monetaria y Financiera at registration; the excess is withheld at 25% to be deductible | 2026 | same (LRTI art. 13(3)) |
| Other interest paid abroad | 25% withholding, whatever the lender's residence | 2026 | same (LRTI art. 13(3), second paragraph) |
| Imports of goods | deductible; no income tax and no withholding | 2026 | same (LRTI art. 13(1)) |
| Reinsurance premiums ceded to insurers with no PE or representation in Ecuador | withheld on a base of 25% of the premium (within the regulator's percentage) or 50% (above it); 100% if the reinsurer is in a tax haven | 2026 | same (LRTI arts. 13(6), 32) |
| Insurance placed abroad with insurers not authorised in Ecuador, where allowed | withheld and paid by the insured on one quarter of the premium; on the whole premium if the insurer is in a tax haven | 2026 | same (LRTI art. 32) |
| Shows with non-resident performers or foreign companies without a PE | company rate (25%) on the whole income; 37% to tax-haven recipients; 15% where the organiser is a registered tourism provider (25% if the recipient is in a tax haven) | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/ee775a90-0ba9-48fe-85cb-9a52673c4c61/REGLAMENTO_PARA_APLICACION_LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (RLRTI art. 13); LRTI art. 39.3 |
| Payment to a resident or non-resident for selling shares or similar rights not listed on an Ecuadorian stock exchange | 2% withholding on the consideration | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/272ca6a9-d679-4b4e-8da0-fb4671cf5f8f/NAC-DGERCGC26-00000009_Ret_IR.pdf (art. 2(4)(d)); the 10% single tax itself is in ec-corporate-income-tax |
| Gains of residents and non-residents on listed Ecuadorian shares | 10% withholding | 2026 | same (art. 2(7)(f)) |
| Tax haven, lower-tax jurisdiction or preferential regime | a jurisdiction or regime meeting at least two of: (1) effective income tax rate below 60% of Ecuador's, or unknown; (2) activities need not be carried on substantially there to get its tax benefits; (3) no effective exchange of information to international transparency standards. Applies even if not on the SRI list | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/12c884d5-c8d9-4171-becc-1513b990b87a/LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (LRTI, article on paraísos fiscales after art. 4); RLRTI article on paraísos fiscales |
| ISD, general rate | 5% of the amount transferred, sent or carried abroad | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/856c3226-b8bc-47c6-bc15-a870ddade2b6/LEY_REFORMATORIA_PARA_LA_EQUIDAD_TRIBUTARIA_REFORMA2024.pdf (art. 162, as replaced in RO Supl. 516 of 12 Mar 2024); https://www.sri.gob.ec/impuesto-a-la-salida-de-divisas-isd |
| ISD on imports, 2026: fuel | 0% | 2026 | https://www.sri.gob.ec/impuesto-a-la-salida-de-divisas-isd; https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/4f86d99e-dff2-4382-9359-dc86d05abb2f/Decreto_Ejecutivo_No_272.pdf (Decreto 272, a scanned image) |
| ISD on imports, 2026: tariff subheadings on the pharmaceutical-sector list | 0% | 2026 | same |
| ISD on imports, 2026: tariff subheadings on the productive-sectors list | 2.5%, within the annual fiscal space set by the Ministerio de Economía y Finanzas | 2026 | same |
| ISD exemption, cash carried by a traveller leaving Ecuador | up to 3 SBU (USD 1,446 for 2026), plus 1 SBU per accompanied minor | 2026 | https://www.sri.gob.ec/impuesto-a-la-salida-de-divisas-isd; Ley Reformatoria art. 159(1) |
| ISD exemption, transfers abroad other than by card | up to 3 SBU, with the periodicity set in the SRI's rules | 2026 | same (art. 159(2)) |
| ISD exemption, card spending or withdrawals abroad | USD 5,188.26 a year for 2025, 2026 and 2027 | 2026 | https://www.sri.gob.ec/impuesto-a-la-salida-de-divisas-isd |
| ISD exemption, dividends paid abroad after income tax to foreign companies or non-resident individuals | exempt, unless Ecuadorian-resident shareholders of the paying company hold rights in the foreign recipient's chain, or a beneficial owner resident in Ecuador sits in the chain | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/856c3226-b8bc-47c6-bc15-a870ddade2b6/LEY_REFORMATORIA_PARA_LA_EQUIDAD_TRIBUTARIA_REFORMA2024.pdf (art. 159(5)); https://www.sri.gob.ec/impuesto-a-la-salida-de-divisas-isd |
| ISD exemption, repayment of foreign loans of 180 days or more from foreign financial institutions or qualified non-financial lenders, for housing, microcredit, equity or productive investment in Ecuador | capital exempt; interest exempt up to the referential rate; not for related-party lenders in tax havens unless the borrower is a financial institution | 2026 | same (art. 159(3)) |

## The base

**Is the income Ecuadorian-source? (LRTI art. 8).** It is, among others, when it comes from: work, professional, commercial and other activities carried on in Ecuador; activities abroad paid by Ecuadorian-domiciled persons, companies or the public sector; gains on assets located in Ecuador and on direct or indirect sales of shares in Ecuadorian companies or PEs; royalties for copyright, industrial property and technology transfer; dividends of Ecuadorian companies; interest paid by Ecuadorian residents or companies; and Ecuadorian lotteries, inheritances and gifts. **Exception:** pay of non-resident individuals for occasional services in Ecuador (a stay of less than six months, consecutive or not, in a calendar year) is not Ecuadorian-source where a foreign company pays it as part of its own withheld or exempt income, or pays it abroad without charging an Ecuadorian company or PE.

**Is there a permanent establishment? (RLRTI art. 9).** A fixed place where the foreign company carries on all or part of its activity: a management centre, branch, agency or office acting for it, factories, workshops, real estate, mines and other extraction sites, a building, construction or assembly site lasting more than 6 months, warehouses for goods sold in the country, or an office for consultancy or for services to performers. A dependent person also creates a PE where they habitually conclude contracts in the company's name, are contracted to act for it, hold its goods for sale in Ecuador, or pay its rent and running costs. Not a PE: facilities used only to display goods, a place used only to collect information, and independent brokers, commission agents and distributors acting in their ordinary course.

**The method for a payment abroad, step by step.**

1. Is the payment Ecuadorian-source income for the recipient (art. 8)? If not, no income tax withholding. Imports of goods are never withheld (art. 13(1)).
2. Is it attributable to an Ecuadorian PE of the recipient? Then the PE is taxed in its own return, not by withholding.
3. Does a specific rule apply? Dividends (art. 39.2), share sales (Res. art. 2), interest (art. 13(3)), insurance and reinsurance (arts. 13(6), 32), shows (RLRTI art. 13). Use that rate and base.
4. Otherwise withhold 25% on the total paid or credited (art. 39; Res. art. 4).
5. Is the recipient in a tax haven, lower-tax jurisdiction or preferential regime (the two-of-three test, whether or not on the SRI list)? Then 37%.
6. Does a treaty in force reduce or remove the tax? Before applying it, confirm that the recipient is resident in the other state (Res. NAC-DGERCGC26-00000009 art. 9) with a current residence certificate for the period from its competent authority, translated into Spanish by a certified translator and legalised by an Ecuadorian consul or apostilled (RLRTI art. 134). The dividend rules give way to treaties in force (art. 39.2, last paragraph).
7. Withhold when paying or crediting, whichever comes first (LRTI art. 50; Res. art. 8). Issue the comprobante de retención within 5 days of receiving the sales document.
8. Deductibility: a necessary expense paid abroad is deductible only if the withholding was made where due, or a treaty removed it (art. 13, first paragraph).
9. ISD: if the money leaves through the financial system, the bank withholds 5% on the amount transferred unless an exemption applies; the exemption is claimed with the SRI's declaration of exempt transactions (Ley Reformatoria art. 161(a); SRI ISD page).

**ISD: what is taxed (Ley Reformatoria arts. 155, 156, 160).** The transfer or carrying of money abroad, in cash or by cheque, transfer, remittance, withdrawal or payment of any kind, except set-offs (compensaciones). The base is the amount transferred. Two presumptions:

- **Payments made from abroad** by persons or companies domiciled or resident in Ecuador are presumed made with funds that cause ISD in Ecuador, even if no money was sent from Ecuador. For imports paid from abroad the base is the customs value; for services and intangibles, the total paid without discounts or the amount booked, whichever is higher (SRI ISD page).
- **Export proceeds not brought back.** For exports of goods or services generated in Ecuador, ISD is presumed on proceeds that do not enter Ecuador within six months after the goods arrive at the destination port (or after shipment, if arrival cannot be identified). ISD paid on payments from abroad can be offset. This presumed ISD is paid once a year, in July (SRI ISD page; art. 156).

**ISD as a credit.** ISD paid on imports of raw materials, inputs and capital goods on the Comité de Política Tributaria list may be credited against income tax of that year or the next four. Unused amounts can be refunded on request after the income tax return for the year of payment is filed. No refund for ISD already deducted as an expense (articles after art. 162; SRI ISD page). Habitual exporters and listed service exporters can recover ISD on imports used to produce the exports within 90 days.

**Foreign tax credit for residents (LRTI art. 49; RLRTI art. 136).** Residents include foreign income in their worldwide income and credit the income tax actually and finally paid abroad on it, up to the Ecuadorian tax attributable to that income. Dividends received from abroad are taxed in the general base with this credit (art. 39.2(8)).

## Deadlines and filing

| Item | Deadline | Source URL |
|---|---|---|
| Withhold income tax on a payment abroad | when paid or credited, whichever is first | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/12c884d5-c8d9-4171-becc-1513b990b87a/LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (LRTI art. 50); Res. NAC-DGERCGC26-00000009 art. 8 |
| Issue the comprobante de retención | within 5 days of receiving the sales document | same (LRTI art. 50) |
| Declare and pay income tax withheld | next month by the ninth digit of the RUC: 1 = 10th, 2 = 12th, 3 = 14th, 4 = 16th, 5 = 18th, 6 = 20th, 7 = 22nd, 8 = 24th, 9 = 26th, 0 = 28th; Galápagos up to the 28th | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/ee775a90-0ba9-48fe-85cb-9a52673c4c61/REGLAMENTO_PARA_APLICACION_LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (RLRTI art. 102) |
| ISD withheld or collected by banks and couriers, and ISD on their own transfers | same dates as income tax withholding; special taxpayers by the 11th | https://www.sri.gob.ec/impuesto-a-la-salida-de-divisas-isd; Ley Reformatoria art. 161(a) |
| ISD on payments from abroad and on card spending above the annual exemption, self-declared by the cardholder | cumulative annual return in April of the following year by ninth digit | https://www.sri.gob.ec/impuesto-a-la-salida-de-divisas-isd |
| ISD presumed on export proceeds not brought back | once a year, in July | same |
| Shows with non-resident performers: SRI certificate before tickets are printed | apply at least 10 business days before the first event | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/ee775a90-0ba9-48fe-85cb-9a52673c4c61/REGLAMENTO_PARA_APLICACION_LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (RLRTI art. 13) |

**Filing, step by step.** The withholding agent records the payment and the withholding in its accounts and issues the electronic comprobante de retención. In SRI en línea it files the monthly income tax withholding return with the payments abroad and pays by the ninth-digit date. ISD on a bank transfer is withheld and paid over by the bank; the payer files the SRI declaration of exempt or non-taxed transactions online where it claims an exemption. ISD on payments from abroad and card spending above the exemption goes on the ISD form in SRI en línea. Where a payment needs proof of withholding for a foreign tax credit, the SRI issues a certificate once it confirms the withholding was paid (RLRTI art. 133).

## Penalties and interest

| Item | Rule | Source URL |
|---|---|---|
| Withholding not made, or made in part | fine equal to the tax that should have been withheld, plus interest; the agent remains jointly liable | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/12c884d5-c8d9-4171-becc-1513b990b87a/LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (LRTI art. 50(1)) |
| Withholding return filed late | LRTI art. 100 (3% of the tax a month, capped at 100%; detail in ecuador-income-tax) | same (art. 50(2)) |
| Comprobante de retención not issued | 5% of the amount withheld | same (art. 50(3)) |
| Expense paid abroad without the withholding due | not deductible | same (art. 13, first paragraph) |
| Traveller leaving with cash above the exemption without declaring and paying ISD | the ISD plus a fine of up to 50% of the undeclared base | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/856c3226-b8bc-47c6-bc15-a870ddade2b6/LEY_REFORMATORIA_PARA_LA_EQUIDAD_TRIBUTARIA_REFORMA2024.pdf (art. 161(b)) |
| Bank that withholds ISD and does not pass it on | treated as tax fraud by the institution | same (art. 161(a)) |
| Foreign loan repaid early (extraordinary payments of 50% or more of the balance within the first 180 days) | the ISD exemption is lost; ISD on the whole credit plus interest from the day after the first transfer | https://www.sri.gob.ec/impuesto-a-la-salida-de-divisas-isd |
| Interest on late tax | Código Tributario art. 21 (see ecuador-income-tax) | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/00682c30-727a-4268-b095-f485d226ce49/Codigo_Tributario_10082023.pdf |

## Cross-border points

- **Treaties.** Ecuador's treaties override the domestic rates where their conditions are met (LRTI art. 13 first paragraph, art. 39.2 last paragraph). This skill does not list the treaties or their rates: read the treaty itself and check it is in force for the payment date.
- **Moving to a tax haven.** A resident individual who claims residence in a tax haven stays resident in Ecuador for four more years unless they prove 183 days and their centre of interests there (LRTI art. 4.1(b)); see ecuador-income-tax.
- **Indirect sales** of Ecuadorian companies through a foreign parent, and the thresholds (300 or 1,000 fracciones básicas), are in ec-corporate-income-tax.
- **IVA** on services imported from abroad is self-assessed by the Ecuadorian buyer with 100% withholding: see ecuador-iva.
- **International transport companies** with Ecuadorian-source income are taxed on a base of 2% of gross income from their transport operations, and their Ecuadorian-source income is exempt to the extent agreed in reciprocity and double tax agreements (LRTI art. 31).

## Two worked examples that recompute

### Example 1: consulting fee paid to a foreign company, with and without a tax haven

Andes Tech S.A. (Quito) pays USD 50,000 for consulting services provided in Ecuador by a foreign company with no PE in Ecuador, which bears the tax. No treaty is claimed.

- Ecuadorian-source (services carried on in Ecuador, art. 8(1)); no specific rate, so 25%: withholding 50,000 × 25% = **USD 12,500**. Andes Tech transfers the net USD 37,500 through its bank.
- ISD at 5% on the amount transferred: 37,500 × 5% = **USD 1,875**, withheld by the bank. No ISD exemption covers a service fee.
- If the consultant were in a tax haven: withholding 50,000 × 37% = **USD 18,500**; net transfer USD 31,500; ISD 31,500 × 5% = **USD 1,575**.
- Andes Tech can deduct the fee only because it made the withholding (art. 13).

```oa-check
name: EC 2026, USD 50,000 fee abroad, 25% vs 37% withholding and 5% ISD
inputs:
  fee: 50000
  rate_general: 0.25
  rate_haven: 0.37
  isd_rate: 0.05
steps:
  - wht_general: fee * rate_general
  - net_general: fee - wht_general
  - isd_general: net_general * isd_rate
  - wht_haven: fee * rate_haven
  - net_haven: fee - wht_haven
  - isd_haven: net_haven * isd_rate
  - total_tax_general: wht_general + isd_general
  - total_tax_haven: wht_haven + isd_haven
expected:
  wht_general: 12500
  net_general: 37500
  isd_general: 1875
  wht_haven: 18500
  net_haven: 31500
  isd_haven: 1575
  total_tax_general: 14375
  total_tax_haven: 20075
```

### Example 2: dividend to a foreign parent, three ownership chains (a decision worked both ways)

Costa S.A. distributes USD 200,000 of 2025 profits, after income tax, to its only shareholder, a foreign company. The shareholders are deciding whether to keep an Ecuadorian-resident individual at the top of the chain.

- **Chain A: foreign parent, foreign beneficial owner, no tax haven.** Dividend tax 10% = **USD 20,000** (art. 39.2(4)). The net USD 180,000 is exempt from ISD (art. 159(5)). Total **USD 20,000**.
- **Chain B: same parent, but the beneficial owner is an Ecuadorian resident.** Dividend tax 12% = **USD 24,000**. The ISD exemption does not apply (a beneficial owner resident in Ecuador sits in the chain), so ISD 5% × 176,000 = **USD 8,800**. Total **USD 32,800**.
- **Chain C: Ecuadorian beneficial owner and a tax-haven company in the chain.** Dividend tax 14% = **USD 28,000**; ISD 5% × 172,000 = **USD 8,600**. Total **USD 36,600**.

What decides it is who the beneficial owner is and whether a tax haven sits in the chain: the figure that moves is the dividend rate (10%, 12%, 14%) and whether ISD applies at all. Treaty rates, if a treaty applies to the parent's state, are not covered here.

```oa-check
name: EC 2026, USD 200,000 dividend abroad, three ownership chains
inputs:
  dividend: 200000
  isd_rate: 0.05
steps:
  - tax_a: dividend * 0.10
  - isd_a: 0
  - total_a: tax_a + isd_a
  - tax_b: dividend * 0.12
  - isd_b: (dividend - tax_b) * isd_rate
  - total_b: tax_b + isd_b
  - tax_c: dividend * 0.14
  - isd_c: (dividend - tax_c) * isd_rate
  - total_c: tax_c + isd_c
expected:
  tax_a: 20000
  total_a: 20000
  tax_b: 24000
  isd_b: 8800
  total_b: 32800
  tax_c: 28000
  isd_c: 8600
  total_c: 36600
```

## Ask the client first

1. What exactly is being paid (goods, services, royalty, interest, dividend, insurance, share price), and is the service carried on in Ecuador or abroad?
2. Where is the recipient resident, does it have a PE in Ecuador, and is its jurisdiction a tax haven, lower-tax jurisdiction or preferential regime?
3. Is a treaty claimed, and is there a current residence certificate, translated and apostilled or legalised?
4. Who is the beneficial owner at the top of the chain, and is any holder in a tax haven (for dividends)?
5. For a loan: the lender, its term (180 days or more?), the interest rate against the referential maximum, and whether it is registered.
6. Is the money leaving through an Ecuadorian bank, paid from an account abroad, or carried in cash; and for goods, are they on the 2026 ISD import lists?

## Sources

| Source | URL | Read on |
|---|---|---|
| LRTI, SRI codification (last reform 1 Apr 2026): article on paraísos fiscales, arts. 4.1, 8, 13, 31, 32, 37, 39, 39.2, 39.3, 48, 49, 50 read | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/12c884d5-c8d9-4171-becc-1513b990b87a/LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf | 2026-11-11 |
| RLRTI, SRI codification (last reform 18 Nov 2025): article on paraísos fiscales, arts. 9, 13, 102, 133, 134, 136 read | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/ee775a90-0ba9-48fe-85cb-9a52673c4c61/REGLAMENTO_PARA_APLICACION_LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf | 2026-11-11 |
| SRI Resolution NAC-DGERCGC26-00000009 (27 Feb 2026, applicable from 1 Mar 2026): whole document read | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/272ca6a9-d679-4b4e-8da0-fb4671cf5f8f/NAC-DGERCGC26-00000009_Ret_IR.pdf | 2026-11-11 |
| SRI Resolution NAC-DGERCGC25-00000043: 2026 table, top rate 37% (art. 2) | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar?id=bb7aac3c-251d-4243-9477-10a3ba8e7355&nombre=NAC-DGERCGC25-00000043.pdf | 2026-11-11 |
| Ley Reformatoria para la Equidad Tributaria en el Ecuador, SRI copy (last reform 25 Mar 2024): arts. 155 to 163 (ISD) read | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/856c3226-b8bc-47c6-bc15-a870ddade2b6/LEY_REFORMATORIA_PARA_LA_EQUIDAD_TRIBUTARIA_REFORMA2024.pdf | 2026-11-11 |
| SRI, Impuesto a la Salida de Divisas page: who pays, exemptions, presumptions, rates by year to 2026, payment, credit | https://www.sri.gob.ec/impuesto-a-la-salida-de-divisas-isd | 2026-11-11 |
| Decreto Ejecutivo 272 (30 Dec 2025, in force 1 Jan 2026): ISD differentiated rates for 2026, read by OCR of the scanned SRI copy | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/4f86d99e-dff2-4382-9359-dc86d05abb2f/Decreto_Ejecutivo_No_272.pdf | 2026-11-11 |
| Código Tributario, SRI codification (10 Aug 2023): art. 21 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/00682c30-727a-4268-b095-f485d226ce49/Codigo_Tributario_10082023.pdf | 2026-11-11 |

Not yet confirmed: the list of double tax treaties in force and their rates, the SRI's rules on applying treaty benefits automatically up to an amount (Res. NAC-DGERCGC18-00000433 was not read); CAN Decision 578; the current SRI tax-haven list; the periodicity of the 3 SBU ISD exemption on transfers; the 2026 ISD import lists and the fiscal-space cap under Decreto 272; the ISD Reglamento (not read); the withholding base when the payer bears the non-resident's tax (gross-up); whether the maximum referential interest rate for 2026 has been published.
