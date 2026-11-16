---
name: bg-company-formation
description: "Company formation and entity choice in Bulgaria for 2026, in euro after the 1 January 2026 changeover. Covers the sole trader (ET), the limited liability company (OOD, and EOOD with one owner) and the joint-stock company (AD); minimum capital (EUR 1 for an OOD or EOOD, EUR 25,000 for an AD) and how much must be paid in before registration; registration in the Commercial Register at the Registry Agency, step by step, and how fast it decides; the state registration fees; the euro conversion of existing company capital; publication of annual financial statements by 30 September and the fine for missing it; and the first tax steps (corporate tax return, VAT registration threshold). Trigger phrases: register a company in Bulgaria, ООД, ЕООД, ЕТ, АД, Търговски регистър, minimum capital Bulgaria, Bulgarian company set-up. Out of scope: corporate tax computation (bg-corporate-income-tax), sole trader and dividend tax (bulgaria-income-tax), VAT (bulgaria-vat-return), cross-border (bg-cross-border)."
version: 0.3
jurisdiction: BG
category: international
tax_year: 2026
last_updated: 2026-11-16
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: formation
type: filing-howto
---

# Bulgaria Company Formation & Entity Choice v0.3

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Who this is for: an individual or a company setting up a business in Bulgaria in 2026 and choosing between a sole trader (ET), a limited liability company (OOD, or EOOD with one owner) and a joint-stock company (AD), then registering it in the Commercial Register. It covers the minimum capital, what must be paid in before registration, the registration steps and fees, the euro conversion of existing companies, the annual publication duty and its fine, and the first tax steps. Tax year: 2026.

Bulgaria adopted the euro on 1 January 2026. Lev amounts still printed in older acts and tariffs are read as euro at the fixed rate of BGN 1.95583 = EUR 1, rounded to the cent (Euro Introduction Act arts. 11(2), 12, 13). This applies to state fees and fines as well (Euro Introduction Act transitional § 5(1)). Each converted figure below shows the lev amount next to it.

The most common Bulgarian business vehicle is the limited liability company (OOD, or EOOD if single-member), governed by the Commercial Act and registered in the Commercial Register at the Registry Agency. The statutory minimum share capital is a token EUR 1. The company pays 10% corporate tax, and dividends it pays to a sole trader or a resident individual carry a 5% final tax (Personal Income Taxes Act arts. 38(1), 46(3)). A sole trader pays 15% on its profit and has unlimited liability. For dividends paid abroad see bg-cross-border.

Out of scope: corporate tax computation (bg-corporate-income-tax), sole trader and dividend tax (bulgaria-income-tax), VAT returns (bulgaria-vat-return), cross-border (bg-cross-border), partnerships (SD, KD), the partnership limited by shares (KDA), the variable-capital company, banks and insurers, and non-profit entities.

## Ask the client first

1. How many owners, and are they individuals or companies? (One owner: ET or EOOD; several: OOD or AD.)
2. Does the owner accept unlimited personal liability? (ET: yes; OOD, EOOD, AD: liability limited to the contribution.)
3. How much capital will the company have, and how much is paid in at the start?
4. Will the application be filed electronically or on paper? (The electronic fee is half.)
5. Does the activity need a licence or permit from a state body before registration?
6. For an existing company: when is its next Commercial Register filing that needs a copy of its articles or contract?

## The method, step by step

### Step 1. Choose the entity [Commercial Act, https://www.registryagency.bg/media/filer_public/2026/08/01/trgovski_zakon.pdf]

| Entity | Rule and conditions | Law | Source |
|---|---|---|---|
| ET (ЕТ), sole trader | Any individual with legal capacity and a permanent address in Bulgaria may register. Liability is unlimited: the trader is the individual, and all of a debtor's property secures its creditors. Business income is taxed at 15% on its corporate-tax profit (see bulgaria-income-tax). | Commercial Act art. 56; Obligations and Contracts Act art. 133; Personal Income Taxes Act art. 48(2) | https://www.registryagency.bg/media/filer_public/2026/08/01/trgovski_zakon.pdf https://www.registryagency.bg/media/filer_public/2026/08/01/zakon_za_zadlzheniiata_i_dogovorite.pdf https://nra.bg/wps/wcm/connect/nra.bg25863/e0daae38-32b9-40b7-8c21-ff7feed98935/%D0%97%D0%94%D0%94%D0%A4%D0%9B+%D1%81%D0%B5%D0%BF%D1%82%D0%B5%D0%BC%D0%B2%D1%80%D0%B8+2026.docx?MOD=AJPERES |
| OOD (ООД), limited liability company | Formed by one or more persons, each liable for the company's debts only up to their contribution to capital. The company contract is in writing. | Commercial Act arts. 113, 114(1) | https://www.registryagency.bg/media/filer_public/2026/08/01/trgovski_zakon.pdf |
| EOOD (ЕООД), single-member limited liability company | An OOD with one owner. A founding act replaces the company contract. The sole owner manages the company personally or through an appointed manager, and takes the decisions of the general meeting. | Commercial Act arts. 114(3), 147(1), (2) | same |
| AD (АД), joint-stock company | Used for larger or capital-raising businesses. Capital and share values are set in euro and euro cents. | Commercial Act art. 161(1) | same |

### Step 2. Set and pay in the capital [Commercial Act, https://www.registryagency.bg/media/filer_public/2026/08/01/trgovski_zakon.pdf]

| Item | Amount and conditions | Law | Source |
|---|---|---|---|
| Minimum share capital, OOD and EOOD | EUR 1; each share at least one euro cent. Before 2026 the minimum was BGN 2. | Commercial Act art. 117(1) | https://www.registryagency.bg/media/filer_public/2026/08/01/trgovski_zakon.pdf |
| Capital paid in before registration, OOD and EOOD | The legal minimum must be paid in. Where the capital is set above the minimum, at least 70% must be paid in. The contract sets the terms for the rest, and the full capital must be paid within two years of registration. | Commercial Act arts. 119(1)(4), (5), 115 item 4 | same |
| Minimum share capital, AD | EUR 25,000. A separate law can set a different minimum for certain companies. The whole capital must be subscribed. | Commercial Act art. 161(2), (3), (4) | same |
| Capital paid in before registration, AD | At least 25% of the nominal or issue value of each share | Commercial Act art. 174(1)(3) | same |

The Registry Agency lists a bank note confirming the paid-in capital, from a bank of the founder's choice, among the documents for an OOD or EOOD (https://www.registryagency.bg/bg/registri/targovski-registar/kak-da-registriram-firma/). That page still mentions the old BGN 2 minimum; the Commercial Act as amended from 1 January 2026 (EUR 1) wins.

### Step 3. Prepare the documents

1. The company contract (OOD) or founding act (EOOD), in writing, stating the name, seat and address, objects and term, the partners, the capital and the terms for paying in any unpaid part, the shares, the management and representation (Commercial Act arts. 114, 115).
2. The manager's consent and specimen signature, notarised (Registry Agency, How to register a company).
3. For an EOOD, the sole owner's decision appointing the manager; for an OOD, the minutes of the founders' meeting (same page).
4. The manager's declarations under Commercial Act arts. 141(8) and 142 (eligibility and the non-compete rule), as listed by the Registry Agency (same page).
5. The bank note for the paid-in capital (Step 2).
6. Any licence or permit the activity needs (Commercial Act art. 119(3); Registry Agency, same page).

### Step 4. File the application with the Commercial Register [Commercial Register Act, https://www.registryagency.bg/media/filer_public/2026/08/01/zakont_za_trgovskiia_registr_i_registra_na_iuridicheskite_litsa_s_nestopanska_tsel.pdf]

1. The Commercial Register and Register of Non-Profit Legal Entities is kept by the Registry Agency (Агенция по вписванията) under the Minister of Justice (Commercial Register Act art. 3(1)).
2. File the application on the official form (form A4 for a new company, per the Registry Agency page) (art. 13(1)), with a declaration that the stated facts are true (art. 13(4)), and attach the documents (art. 13(6)). A paper application may be filed at any Registry Agency office at the seat of a district court (art. 13(7)).
3. Pay the state fee (table below). An electronic application costs at most 50% of the paper fee (art. 12(2)).

| Entity | Paper application | Electronic application | Tariff | Source |
|---|---|---|---|---|
| ET, sole trader | BGN 30 = EUR 15.34 | BGN 15 = EUR 7.67 | Tariff art. 16а(1)(1), (2)(1) | https://www.registryagency.bg/media/filer_public/2025/12/30/izvlechenietarifatrriulnts.docx |
| OOD or EOOD | BGN 110 = EUR 56.24 | BGN 55 = EUR 28.12 | Tariff art. 16а(1)(3), (2)(3) | same |
| AD or single-member AD | BGN 360 = EUR 184.07 | BGN 180 = EUR 92.03 | Tariff art. 16а(1)(4), (2)(4) | same |
| Branch of a foreign trader | BGN 340 = EUR 173.84 | BGN 170 = EUR 86.92 | Tariff art. 16а(1)(8), (2)(8) | same |

The fees are set by the Registry Agency tariff. The tariff itself still prints leva; the Registry Agency's euro extract of it, published on 30 December 2025, gives each fee in leva and euro, converted at BGN 1.95583 and rounded to the cent under the Euro Introduction Act.

### Step 5. What happens after filing [Commercial Register Act, https://www.registryagency.bg/media/filer_public/2026/08/01/zakont_za_trgovskiia_registr_i_registra_na_iuridicheskite_litsa_s_nestopanska_tsel.pdf]

1. The registration officer examines an application for first registration of a trader by the end of the next working day after it reaches the register, and decides straight away (art. 19(3)). Other applications are decided after three working days (art. 19(2)).
2. If documents or the fee are missing, the officer instead issues instructions to put the defect right, published no later than the next working day; the applicant may comply with a further application, and the officer refuses if the instructions are not met by the end of the art. 19(2) period (art. 22(5)).
3. Time to prepare documents and open the capital account comes on top.

### Step 6. Existing companies and the euro [Euro Introduction Act, https://dv.parliament.bg/DVWeb/showMaterialDV.jsp?idMat=224950]

1. On 1 January 2026 the registered capital of every OOD, EOOD and AD was replaced with its euro value automatically, by the Registry Agency (Euro Introduction Act art. 33(1), (2)).
2. OOD capital is converted by dividing by 1.95583 and rounding to the cent (art. 31(4)).
3. The duty to file the updated contract or statute arises with the next filing only where the Commercial Act needs a copy of it to be filed, and no state fee is charged for it (art. 32(4), as amended by State Gazette 92/2026, https://www.parliament.bg/bg/laws/ID/167535).
4. Companies must bring their articles and contracts into line within the period in art. 32(1). The period current in 2026 is held under Not yet confirmed (see Sources); do not quote a deadline to a client until it is confirmed.

### Step 7. Annual duties after registration

| Duty | Deadline, amount and conditions | Law | Source |
|---|---|---|---|
| Publish the annual financial statements | Every trader under the Commercial Act, companies included, applies to the Commercial Register by 30 September of the following year. A sole trader not subject to audit is outside this duty. | Accountancy Act art. 38(1)(1), (9)(1) | https://www.registryagency.bg/media/filer_public/2026/08/01/zakon_za_schetovodstvoto.pdf |
| Dormant company | A company that did no business in the year files a one-off declaration instead, by 30 June of the following year, free of the state fee | Accountancy Act art. 38(9)(2), (11) | same |
| Automatic publication from 2026 | Annual statements and declarations filed through the statistics system are published automatically on the trader's record, except for joint-stock companies and companies whose statements must be audited | Commercial Register Act arts. 13(10), 19(8) | https://www.registryagency.bg/media/filer_public/2026/08/01/zakont_za_trgovskiia_registr_i_registra_na_iuridicheskite_litsa_s_nestopanska_tsel.pdf |
| Fine for not publishing, person responsible | BGN 200 to 3,000, which is EUR 102.26 to EUR 1,533.88 (computed: divided by 1.95583, rounded to the cent) | Accountancy Act art. 74(1) | https://www.registryagency.bg/media/filer_public/2026/08/01/zakon_za_schetovodstvoto.pdf |
| Property sanction for not publishing, company | 0.1% to 0.5% of net sales for the year concerned, at least BGN 200 (EUR 102.26, computed as above); a repeat breach doubles the fine or sanction | Accountancy Act art. 74(1), (2) | same |
| Corporate income tax | 10%. Annual return filed from 1 March to 30 June of the following year; the tax, less advances, paid by 30 June. See bg-corporate-income-tax. | Corporate Income Tax Act arts. 20, 92(2), 93(1) | https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/%D0%97%D0%9A%D0%9F%D0%9E+%D1%81%D0%B5%D0%BF%D1%82%D0%B5%D0%BC%D0%B2%D1%80%D0%B8+2026.docx?MOD=AJPERES |
| VAT registration | A business established in Bulgaria must register when its annual turnover in Bulgaria for the calendar year exceeds the national threshold of EUR 51,130. It may register voluntarily below that. This replaced the old BGN 100,000 rolling 12-month test from 1 January 2026 (art. 96 as amended by State Gazette 115/2025). See bulgaria-vat-return. | VAT Act arts. 96(1), 100(1) | https://nra.bg/wps/wcm/connect/nra.bg25863/d8cef699-d86e-42b3-a6a8-26bf10a2e86e/%D0%97%D0%94%D0%94%D0%A1_2026.docx?MOD=AJPERES |

## Boundary and exception table

| Situation | Treatment | Law |
|---|---|---|
| OOD capital set above EUR 1 | At least 70% paid in before registration; the rest within two years | Commercial Act arts. 119(1)(5), 115 item 4 |
| Activity needs a state licence or permit | The licence or permit is filed for the entry | Commercial Act arts. 119(3), 174(3) |
| Application missing documents or the fee | Instructions, then refusal if not cured in time | Commercial Register Act art. 22(5) |
| A separate law sets another AD minimum (for example banks) | That law's minimum applies | Commercial Act art. 161(3) |
| Company with no activity in the year | One-off declaration by 30 June instead of statements | Accountancy Act art. 38(9)(2) |
| Sole trader not subject to audit | No publication duty | Accountancy Act art. 38(9)(1) |

## Worked cases

### Case 1. EOOD with EUR 5,000 capital, filed electronically

A single founder sets up an EOOD with capital of EUR 5,000 and files online. The capital is above the EUR 1 minimum, so at least 70% must be paid in before registration: EUR 3,500 (Commercial Act art. 119(1)(5)). The remaining EUR 1,500 is due within two years of registration (art. 115 item 4). The electronic fee is EUR 28.12 against EUR 56.24 on paper (Tariff art. 16а(1)(3), (2)(3)), a saving of EUR 28.12. The officer decides by the end of the next working day after filing (Commercial Register Act art. 19(3)).

```oa-check
name: Bulgaria EOOD, capital EUR 5,000, electronic filing, 2026
inputs:
  capital: 5000
  paper_fee_bgn: 110
  electronic_fee_bgn: 55
  rate: 1.95583
steps:
  - paid_in_before_registration: capital * 0.70
  - paid_later: capital - paid_in_before_registration
  - paper_fee_eur: round(paper_fee_bgn / rate, 2)
  - electronic_fee_eur: round(electronic_fee_bgn / rate, 2)
  - saving: paper_fee_eur - electronic_fee_eur
expected:
  paid_in_before_registration: 3500.00
  paid_later: 1500.00
  paper_fee_eur: 56.24
  electronic_fee_eur: 28.12
  saving: 28.12
```

### Case 2. Statements not published, net sales EUR 400,000, second breach

An OOD with net sales of EUR 400,000 for 2025 did not apply to publish its 2025 statements by 30 September 2026, and it had already been sanctioned once for the same breach. The company's property sanction is 0.1% to 0.5% of net sales, EUR 400 to EUR 2,000, above the EUR 102.26 floor; a repeat breach doubles it to EUR 800 to EUR 4,000 (Accountancy Act art. 74(1), (2)). The person responsible faces a fine of EUR 102.26 to EUR 1,533.88, doubled to EUR 204.52 to EUR 3,067.76.

```oa-check
name: Bulgaria OOD, statements not published, net sales EUR 400,000, repeat breach, 2026
inputs:
  net_sales: 400000
  rate: 1.95583
steps:
  - floor_eur: round(200 / rate, 2)
  - sanction_low: max(net_sales * 0.001, floor_eur)
  - sanction_high: max(net_sales * 0.005, floor_eur)
  - repeat_low: sanction_low * 2
  - repeat_high: sanction_high * 2
  - fine_low: round(200 / rate, 2) * 2
  - fine_high: round(3000 / rate, 2) * 2
expected:
  floor_eur: 102.26
  sanction_low: 400.00
  sanction_high: 2000.00
  repeat_low: 800.00
  repeat_high: 4000.00
  fine_low: 204.52
  fine_high: 3067.76
```

## When to refuse or refer

- Refuse to quote the euro-conversion deadline for updating articles (Step 6, item 4) until it is confirmed.
- Refer banks, insurers, investment firms and other licensed activities: a separate law may set the capital and the licence comes first.
- Refer notary fees and bank charges for the capital account: they are not in the Registry Agency tariff and are not confirmed here.
- Refer the tax choice between sole trader, freelancer and company to bulgaria-tax-optimization, and the computations to bulgaria-income-tax and bg-corporate-income-tax.

## Filing and payment

- Commercial Register application: online through the Registry Agency, or on paper at a Registry Agency office at the seat of a district court (Commercial Register Act art. 13(7)); state fee as in Step 4.
- Annual statements: by 30 September of the following year (Accountancy Act art. 38(1)(1)).
- Corporate tax return: 1 March to 30 June of the following year, to the NRA territorial directorate where the company is registered (Corporate Income Tax Act art. 92(2)).

## Completion checklist

- Entity chosen and the liability consequence explained.
- Capital set and the amount paid in before registration checked (70% rule, or 25% per share for an AD).
- Documents prepared, notarised consent and declarations included.
- Fee paid at the electronic or paper rate.
- Decision received, or instructions answered before the art. 19(2) period ends.
- Annual publication, corporate tax and VAT threshold diarised.

## Sources

| Source | URL | Read on |
|---|---|---|
| Commercial Act (Търговски закон), Registry Agency copy consolidated to State Gazette 69/2026, arts. 56, 113, 114, 115, 117, 119, 147, 161, 174 | https://www.registryagency.bg/media/filer_public/2026/08/01/trgovski_zakon.pdf | 2026-11-16 |
| Commercial Register and Register of Non-Profit Legal Entities Act, Registry Agency copy consolidated to State Gazette 25/2026, arts. 3, 12, 13, 19, 22 | https://www.registryagency.bg/media/filer_public/2026/08/01/zakont_za_trgovskiia_registr_i_registra_na_iuridicheskite_litsa_s_nestopanska_tsel.pdf | 2026-11-16 |
| Act supplementing the Commercial Register Act, State Gazette 92/2026, Parliament text, including § 3 amending Euro Introduction Act art. 32(4) | https://www.parliament.bg/bg/laws/ID/167535 | 2026-11-16 |
| Registry Agency, extract of the Tariff of State Fees for the Commercial Register, in leva and euro (Извлечение тарифа ТРРЮЛНЦ, uploaded 30 December 2025), art. 16а | https://www.registryagency.bg/media/filer_public/2025/12/30/izvlechenietarifatrriulnts.docx | 2026-11-16 |
| Tariff of State Fees Collected by the Registry Agency, art. 16а (text as at 5 January 2026, in leva) | https://www.registryagency.bg/media/filer_public/2026/01/07/tarifa_za_drzhavnite_taksi_sbirani_ot_agentsiiata_po_vpisvaniiata.pdf | 2026-10-30 |
| Registry Agency, State fees (fees expressed in euro from 2026) | https://www.registryagency.bg/bg/prestsentar/novini/drzhavni-taksi/ | 2026-10-30 |
| Registry Agency, How to register a company (documents list; still shows the old BGN 2 minimum) | https://www.registryagency.bg/bg/registri/targovski-registar/kak-da-registriram-firma/ | 2026-11-16 |
| Accountancy Act (Закон за счетоводството), Registry Agency copy consolidated to State Gazette 67/2026, arts. 38, 74 | https://www.registryagency.bg/media/filer_public/2026/08/01/zakon_za_schetovodstvoto.pdf | 2026-11-16 |
| Euro Introduction Act, State Gazette 70/2024 as published: arts. 11, 12, 13, 31, 32, 33 and transitional § 5 | https://dv.parliament.bg/DVWeb/showMaterialDV.jsp?idMat=224950 | 2026-11-16 |
| Bulgarian National Bank, National Euro Changeover Plan (rate BGN 1.95583) | https://www.bnb.bg/bnbweb/groups/public/documents/bnb_download/eurochangeoverplan_en.pdf | 2026-11-16 |
| Corporate Income Tax Act, NRA consolidated text to State Gazette 55/2026, arts. 20, 92, 93 | https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/%D0%97%D0%9A%D0%9F%D0%9E+%D1%81%D0%B5%D0%BF%D1%82%D0%B5%D0%BC%D0%B2%D1%80%D0%B8+2026.docx?MOD=AJPERES | 2026-11-16 |
| Personal Income Taxes Act, NRA consolidated text to State Gazette 85/2026, arts. 38(1), 46(3), 48(2) | https://nra.bg/wps/wcm/connect/nra.bg25863/e0daae38-32b9-40b7-8c21-ff7feed98935/%D0%97%D0%94%D0%94%D0%A4%D0%9B+%D1%81%D0%B5%D0%BF%D1%82%D0%B5%D0%BC%D0%B2%D1%80%D0%B8+2026.docx?MOD=AJPERES | 2026-11-16 |
| Value Added Tax Act, NRA consolidated text to State Gazette 115/2025, arts. 96(1), 100(1) | https://nra.bg/wps/wcm/connect/nra.bg25863/d8cef699-d86e-42b3-a6a8-26bf10a2e86e/%D0%97%D0%94%D0%94%D0%A1_2026.docx?MOD=AJPERES | 2026-11-16 |
| Obligations and Contracts Act (Закон за задълженията и договорите), Registry Agency copy, art. 133 | https://www.registryagency.bg/media/filer_public/2026/08/01/zakon_za_zadlzheniiata_i_dogovorite.pdf | 2026-11-16 |

Not yet confirmed: the period in Euro Introduction Act art. 32(1) for bringing articles and contracts into line (12 months in the Act as published in State Gazette 70/2024; the Act was amended by State Gazette 25, 49, 63, 65, 99, 100 and 115 of 2025 and 55 and 82 of 2026, which were not read; the previous version of this skill said 36 months, from a private law database); notary fees for the manager's consent and specimen signature (not in the Registry Agency tariff); the bank's charges and practice for the capital account; Commercial Act arts. 141(8) and 142 were not read (the declarations are listed from the Registry Agency page).
