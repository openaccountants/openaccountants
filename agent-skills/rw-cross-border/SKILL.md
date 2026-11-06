---
name: rw-cross-border
description: "Rwanda cross-border income tax for the 2026 tax period under Law 027/2022 establishing taxes on income (as amended by Laws 051/2023 and 014/2025), Ministerial Order 009/26/10/TC on permanent residence and effective place of management, and Law 020/2023 on tax procedures. Covers residence of individuals (183 days, 122-day average) and companies (incorporation or effective management, four tests), the permanent establishment rules including the 90-day services test and dependent agents, Rwanda-source income including services performed abroad for residents, 15% withholding on dividends, interest, royalties, service fees, performance payments, repatriated branch profits and reinsurance premiums, the 5% rate for listed securities and long treasury bonds, the 10% tax on direct and indirect share transfers, the pending 1.5% digital services tax, the foreign tax credit cap, treaty residence certificates and the anti-abuse rule. Trigger on: Rwanda withholding tax non-resident, Rwanda permanent"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/rw-cross-border"
  jurisdiction: "RW"
  tax_year: "2026"
  last_updated: "2026-11-02"
---

# Rwanda cross-border: residence, permanent establishment, withholding on non-residents and foreign tax credit (2026) v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Rwanda taxes residents on income from all sources and non-residents on Rwanda-source income, through a permanent establishment or by withholding at source. The rules are in Law 027/2022 of 20/10/2022 establishing taxes on income (the Income Tax Law, "ITL"), as amended by Law 051/2023 (28% corporate rate) and Law 014/2025 (10% capital gains, digital services). Ministerial Order 009/26/10/TC of 24/09/2026 sets the residence and effective-management tests. Law 020/2023 on tax procedures governs collection and fines. The Rwanda Revenue Authority (RRA) administers them. The tax period is the calendar year (ITL art 8); this skill covers 2026. Company rates and filing are owned by [rw-corporate-income-tax](rw-corporate-income-tax.md), individuals by [rwanda-income-tax](rwanda-income-tax.md), related-party pricing by [rw-transfer-pricing](rw-transfer-pricing.md).

## Who this applies to

- **Resident individuals (ITL art 4).** Resident if any one applies:
  - a permanent residence in Rwanda: the home, house, apartment, hotel or other quarters where the person usually stays (Order 009 art 1);
  - a habitual abode in Rwanda;
  - a Rwandan representing Rwanda abroad;
  - present in Rwanda for 183 days or more in aggregate in the tax period;
  - present in the tax period and present for an average of more than 122 days in each of the two preceding tax periods.
- **Resident companies and other entities (ITL art 4; Order 009 art 2).** Resident if established under Rwandan law, or with a place of effective management in Rwanda at any time in the tax period. Effective management is in Rwanda if any one of these applies:
  - day-to-day control and management is done here;
  - shareholders' meetings are held here;
  - the books of accounts are kept here;
  - the main shareholders or directors are resident here.
- **Non-residents.** A non-resident individual pays personal income tax only on Rwanda-source income (ITL art 12). A non-resident entity pays corporate income tax on the business profit of its permanent establishment, on the same basis as a resident (ITL arts 44(7), 47). Other Rwanda-source income of non-residents is reached through withholding by the Rwandan payer (ITL art 60).
- **Permanent establishment (ITL art 5).** A known fixed place of business through which the business is wholly or partly carried out. It includes:
  - a place of management, a branch, a factory or workshop;
  - a mine, quarry or other place of natural resource exploitation;
  - a construction site, or a place of supervision or assembly works;
  - a place where services, including consulting, are provided through employees or other personnel for more than 90 days in any 12 months, continuously or not.
  - **Dependent agent:** a person who negotiates or concludes contracts in the non-resident's name, or plays the principal role leading to them, creates a permanent establishment.
  - **Not a PE:** facilities or stock used only for storage, stock for processing by another, purchasing or information-gathering, and other preparatory or auxiliary activities. An independent broker, general commissionaire or other independent agent acting in its ordinary course is not a PE either, unless it works wholly or almost wholly for the non-resident on non-arm's length terms.
  - **Subsidiaries:** control of or by another company does not by itself create a PE.
  - **Insurers:** an insurer (except for reinsurance) has a PE if it collects premiums or insures risks in Rwanda through a person other than an independent broker or agent.

Not covered here, refer to a specialist: the rates and permanent establishment tests of individual treaties; VAT on imported services; mining and minerals tax.

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Withholding on payments by residents, including tax-exempt residents (and by Rwandan PEs of non-residents), to a person not registered with the RRA, or registered without a recent income tax declaration (ITL art 60, first paragraph): dividends (other than resident-to-resident dividends under art 47), interest, royalties, service fees (including management and technical, but not transport), performance payments to artists, players and similar, goods sold in Rwanda, after-tax profit or retained earnings converted into shares (except financial institutions below the BNR minimum capital), payments in cash or kind for a non-resident contractor on top of the fee, reinsurance premiums to non-resident insurers | 15% of the amount excluding VAT (ITL art 60, items 1 to 7, 9, 10) | 2026 | https://www.rra.gov.rw/fileadmin/user_upload/Income_Tax_law_of_2022.pdf |
| Profits repatriated from Rwanda (branch remittances) | 15% (ITL art 60, item 8; same first-paragraph condition) | 2026 | same |
| Interest outside the 15% | interest on deposits of at least 1 year; interest on loans from a foreign development financial institution exempt in its home country; interest paid by Rwandan banks or deposit-taking microfinance institutions to foreign banks or financial institutions (ITL art 60, item 2) | 2026 | same |
| Reinsurance premiums outside the 15% | premiums to insurers that have signed agreements with the Government of Rwanda (ITL art 60, item 10) | 2026 | same |
| Dividends and interest on securities listed on the capital market, beneficiary resident in Rwanda or the East African Community; interest on treasury bonds of 3 years or more | 5% (ITL art 60) | 2026 | same |
| Board member allowances | 30% withholding (ITL art 59) | 2026 | same |
| Permanent establishment, services test | more than 90 days in any 12-month period (ITL art 5) | 2026 | same |
| Capital gains on the direct or indirect sale or transfer of shares, in Rwanda or abroad | 10% of the gain (ITL art 35; art 36 as amended by Law 014/2025 art 1) | 2026 | https://www.minijust.gov.rw/index.php?eID=dumpFile&f=130496&t=f&token=4b9d4de9658212b7aaeeb5c8a42c823a7b879d7b |
| Digital services by a company with a substantial national presence | 1.5% of Rwanda-source gross revenue, once an Order of the Minister sets scope and modalities (ITL art 50 bis, inserted by Law 014/2025 art 5) | 2026 | same |
| Corporate income tax on a permanent establishment's profit | 28% (ITL art 48 as amended by Law 051/2023 art 2) | 2026 | https://www.rra.gov.rw/fileadmin/user_upload/Law_amending_Income_Tax_Ok.pdf |
| Foreign tax credit cap | foreign tax payable on foreign income, at most the Rwandan tax on that income (ITL art 7) | 2026 | https://www.rra.gov.rw/fileadmin/user_upload/Income_Tax_law_of_2022.pdf |
| Late-payment interest | 0.5% a month for up to 6 months, 1% from 6 to 12 months, 1.5% after 12 months; simple; capped at 100% of the tax (Law 020/2023 art 80) | 2026 | https://www.rra.gov.rw/fileadmin/user_upload/OG_n___Special_ter_of_31.03.2023_Uburyo_bw_isoresha_Tax_procedures_01.pdf |

## The base

**Rwanda-source income (ITL art 6).** Taxable income covers activities performed in Rwanda by any person and activities performed abroad by a resident. They include:
- services and employment;
- crafts, artistic, singing, sports, cultural and leisure activities;
- activities of a non-resident through a Rwandan PE;
- use, sale, lease or free transfer of business movable or immovable assets;
- agriculture, fishing and forestry;
- investments in shares;
- direct or indirect sale or transfer of shares or debentures;
- distribution of profits;
- lending and deposits;
- transfer, sale and lease of intellectual property;
- digital services, gaming, and any other income-generating activity.

**Services bought from abroad.** All payments by a Rwandan resident for services performed abroad are taxable income, except services consumed abroad (art 6, last paragraph). So a foreign provider's fee for services used in Rwanda falls within the 15% withholding even when the work is done outside Rwanda.

**Withholding (ITL arts 60, 64, 65, 66).**
- **Who withholds:** resident payers withhold 15% on the listed payments, including tax-exempt payers. The same applies to a non-resident's Rwandan PE for its payments.
- **The trigger:** the payee is not registered with the RRA, or is registered but has no recent income tax declaration. This condition is in the first paragraph of art 60 itself (art 63 repeats it for public tenders). A foreign payee without a Rwandan registration therefore suffers the 15%.
- **Non-resident without a PE:** a non-resident entity is liable to corporate income tax only through a Rwandan PE (ITL arts 44 item 7, 47), so for a foreign company without a PE the 15% is in practice the only Rwandan income tax on the payment. The Law does not call it a final tax.
- **Accrued liabilities:** an amount booked as a liability to a creditor that reduces taxable income counts as paid once it is more than 6 months past the end of the tax period.
- **Credit for registered payees:** for a registered payee who did not previously declare, the tax withheld is deducted from its income tax when it declares (art 60). A PE credits tax withheld on its income against its annual tax (art 10).
- **Exempt payees (art 65):** no withholding under art 60 applies to a payee whose profits are exempt, one holding an RRA tax clearance certificate, or one newly registered in the tax period.
- **Payer liability:** a payer who fails to withhold is personally liable for the tax, fines and interest (art 66).

**Repatriated profits.** A non-resident's PE pays 28% on its profit and a further 15% on profits repatriated from Rwanda (art 60, item 8, which art 60 applies to PEs' payments; the first-paragraph condition on the payee's registration is not adapted for a remittance to head office). The Law does not give a formula for the repatriated amount.

**Share transfers (ITL arts 35 to 38 as amended).**
- **Charge:** capital gains tax at 10% applies to the direct or indirect sale or transfer of shares, in Rwanda or abroad. The gain is the selling or transfer price less the acquisition value.
- **Who withholds:** the resident company whose shareholding structure changed. For licences, debt instruments, options, guarantees and similar assets, the seller or buyer withholds (art 37 as amended).
- **Indirect transfers:** a sale of a foreign holding company that changes a Rwandan company's ownership is caught.
- **Exempt:** gains on shares and securities listed on a Rwandan securities exchange, and on units of collective investment schemes (art 38).

**Employment.**
- **Exempt:** pay from a non-resident employer to a non-resident individual for services in Rwanda, unless the services relate to the employer's Rwandan PE (art 16).
- **Self-declaration:** where a treaty removes the employer's withholding duty, the employee declares and pays within 15 days after each month (art 58).
- **KIFC experts:** a newly resident expert working for a Kigali International Financial Centre licensed entity, not resident in the prior 5 years, is exempt on foreign income for 5 years (art 12).

**Digital services (art 50 bis).** A company supplying digital services in Rwanda with a substantial national presence is subject to 1.5% of its Rwanda-source gross revenue. The scope, the presence test and registration depend on an Order of the Minister.

**Residents' foreign income (ITL arts 7, 25).**
- **The credit:** a resident's tax on income from activities abroad is reduced by the foreign tax payable on that income. It is evidenced by a foreign declaration, a withholding certificate or a similar document, and capped at the Rwandan tax on that foreign income.
- **No deduction:** income tax paid abroad on business profit is not deductible (art 25), so relief is by credit only.
- **Filing:** the credit is entered in the Foreign Tax Credit field of the declaration (RRA Handbook).
- **Proof for foreign claims:** a taxpayer can request an RRA Foreign Tax Credit certificate, from RRA offices, case by case, to prove tax paid in Rwanda (RRA Handbook).

**Treaties and anti-abuse.**
- **Residence certificate:** a payer applying a treaty must hold the payee's tax residence certificate from the treaty partner's competent authority, and submits it with the withholding declaration (Law 020/2023 art 22).
- **Treaty over Income Tax Law:** the Constitution (2003, revised 2015, art 95) ranks international treaties and agreements ratified by Rwanda above ordinary laws, and a law may not contradict a higher one; the Income Tax Law is an ordinary law, so a ratified treaty prevails over it.
- **Rates:** the RRA Handbook notes treaty-reduced withholding rates, but rates must be read from each treaty. The RRA lists the Presidential Order ratifying the Rwanda and DRC convention among its laws.
- **Information exchange:** Rwanda joined the Global Forum in 2017 and acceded to the amended Convention on Mutual Administrative Assistance on 11 August 2021 (RRA Handbook). The RRA may disclose information to enforce ratified treaties (Law 020/2023 arts 96, 97).
- **Anti-abuse (ITL art 68):** an arrangement whose principal purpose is a tax benefit, that lacks commercial substance, creates non-arm's length rights, or abuses the tax laws may be disregarded, recharacterised or reallocated, and persons may be deemed related.
- **Low-tax places:** transactions with persons in beneficial tax regimes (tax of 15% or less) are deemed controlled (Order 003/26/10/TC art 3; see rw-transfer-pricing).

## Deadlines and filing

| Obligation | When | Source |
|---|---|---|
| Withholding (arts 59, 60, 61, 63): declare and pay | within 15 days after the month in which tax was withheld; declared in E-Tax (Declare withholding tax page) | ITL art 64 |
| Capital gains tax on a share transfer | the resident company (or seller or buyer) declares and pays within 15 days after the month of the sale or transfer | ITL art 37 as amended by Law 014/2025 art 2 |
| Recipient where the payer had no duty to withhold | the recipient declares and pays within 15 days after the month of payment | Law 020/2023 art 74 |
| Employee where a treaty removes the employer's withholding duty | within 15 days after each month | ITL art 58 |
| Tax residence certificate for a treaty rate | submitted with the related withholding declaration | Law 020/2023 art 22 |
| Annual declaration of a PE or a resident claiming a foreign tax credit | 31 March 2027 for 2026 (see rw-corporate-income-tax) | ITL arts 9, 10 |
| Records of payments and tax withheld | kept 10 years after the tax period | ITL art 67 |

## Penalties and interest

- **Failure to withhold:** the payer is personally liable for the tax not withheld, with fines and interest (ITL art 66). Failing to withhold, and failing to file a withholding declaration on time, are also fixed-fine faults (Law 020/2023 art 81).
- **Late declaration and payment (art 82):** 20%, 40% or 60% of the tax by lateness. If declared on time but paid late: 5%, 10% or 30%. Bands: rw-corporate-income-tax.
- **Interest (art 80):** 0.5%, 1% or 1.5% a month by length of delay, simple, every started month counted, capped at 100% of the tax, payable even under appeal.
- **Treaty claims without a residence certificate:** the condition in Law 020/2023 art 22 is not met, so the domestic 15% applies.
- **Abusive arrangements:** reassessment under ITL art 68, with understatement fines of 10% (doubled above 20%) under Law 020/2023 art 83.

## Cross-border points

This whole skill is about cross-border points. In short:
- residence follows ITL art 4 and Order 009;
- a non-resident with a PE (including services over 90 days in 12 months) pays 28% on the PE's profit plus 15% on repatriated profits;
- other Rwanda-source payments, including services performed abroad but used in Rwanda, bear 15% withholding, or 5% on listed securities and long treasury bonds;
- share transfers, direct or indirect, bear 10%;
- residents relieve foreign tax by a capped credit;
- treaty rates need the payee's residence certificate.

## Two worked examples that recompute

### Example 1: decision, does a foreign consultant's project create a permanent establishment?

Nairobi Advisory Ltd (Kenya, not registered in Rwanda) contracts with a Kigali bank for a fee of FRW 40,000,000 excluding VAT. Its staff will be on site either 80 days or 120 days in 12 months. Assume no treaty reduction.

- **80 days (no PE, ITL art 5):** the bank withholds 15% x 40,000,000 = **FRW 6,000,000** and pays FRW 34,000,000. Nothing more is filed in Rwanda unless the consultant registers.
- **120 days (PE, more than 90 days):** the PE registers and pays 28% on its profit. With costs of FRW 25,000,000, profit is FRW 15,000,000 and tax is **FRW 4,200,000**.
  - If it is newly registered in the period, the fee is outside art 60 withholding (art 65).
  - If the bank still withholds FRW 6,000,000, it is credited (art 10). The excess FRW 1,800,000 is applied to other tax or refunded on request within 30 days.
  - Any profit sent home then bears 15% (art 60, item 8).

```oa-check
name: Rwanda foreign consultant, PE or not, fee FRW 40m (2026)
inputs:
  fee: 40000000
  costs: 25000000
  wht_rate: 0.15
  cit_rate: 0.28
steps:
  - wht_no_pe: fee * wht_rate
  - net_received_no_pe: fee - wht_no_pe
  - pe_profit: fee - costs
  - cit_pe: pe_profit * cit_rate
  - excess_credit_if_withheld: max(wht_no_pe - cit_pe, 0)
expected:
  wht_no_pe: 6000000.00
  net_received_no_pe: 34000000.00
  pe_profit: 15000000.00
  cit_pe: 4200000.00
  excess_credit_if_withheld: 1800000.00
```

### Example 2: resident company's foreign tax credit cap

Huye Engineering Ltd (Rwanda resident) has taxable business profit of FRW 1,000,000,000 for 2026. That includes FRW 200,000,000 from its Ugandan branch, which paid FRW 70,000,000 of Ugandan tax, evidenced by the Ugandan return.

- **Rwandan tax before credit:** 28% x 1,000,000,000 = FRW 280,000,000.
- **Cap (ITL art 7):** Rwandan tax on the foreign income, 28% x 200,000,000 = FRW 56,000,000.
- **Credit:** the lower of 70,000,000 and 56,000,000 = **FRW 56,000,000**. The other FRW 14,000,000 is not relieved, and it is not deductible (art 25).
- **Net Rwandan tax:** **FRW 224,000,000**, due by 31 March 2027.

```oa-check
name: Rwanda foreign tax credit cap, art 7 (2026)
inputs:
  taxable_profit: 1000000000
  foreign_income: 200000000
  foreign_tax_paid: 70000000
  rate: 0.28
steps:
  - rwanda_tax: taxable_profit * rate
  - credit_cap: foreign_income * rate
  - credit: min(foreign_tax_paid, credit_cap)
  - net_tax: rwanda_tax - credit
  - unrelieved: foreign_tax_paid - credit
expected:
  rwanda_tax: 280000000.00
  credit_cap: 56000000.00
  credit: 56000000.00
  net_tax: 224000000.00
  unrelieved: 14000000.00
```

## Ask the client first

1. For individuals: permanent residence or habitual abode in Rwanda, and days present in 2026 and in 2024 and 2025.
2. For entities: place of incorporation, and where day-to-day management, shareholder meetings, the books and the main shareholders or directors are.
3. What the non-resident does in Rwanda: offices, sites, staff days in any 12 months, and agents who conclude contracts.
4. Each payment to non-residents by type (dividend, interest, royalty, service fee, performance, reinsurance, repatriated profit), the amount excluding VAT, and the payee's RRA registration status.
5. Whether a treaty rate is claimed, and whether the payee's tax residence certificate is held.
6. For residents with foreign income: foreign tax paid and its evidence; any direct or indirect change in ownership of a Rwandan company.

## Sources

| Source | URL | Read on |
|---|---|---|
| Law 027/2022 establishing taxes on income, OG Special of 28/10/2022 (read for arts 3, 4 to 7, 10, 12, 16, 25, 35 to 41, 44, 47, 58 to 68) | https://www.rra.gov.rw/fileadmin/user_upload/Income_Tax_law_of_2022.pdf | 2026-11-02 |
| Law 051/2023 amending the income tax law (read for arts 1 and 2: declarations and the 28% rate) | https://www.rra.gov.rw/fileadmin/user_upload/Law_amending_Income_Tax_Ok.pdf | 2026-11-02 |
| Official Gazette Special of 29/05/2025, Law 014/2025 amending the income tax law (read whole: arts 1 to 8, capital gains rate and withholding, exempt persons, gaming, digital services) | https://www.minijust.gov.rw/index.php?eID=dumpFile&f=130496&t=f&token=4b9d4de9658212b7aaeeb5c8a42c823a7b879d7b | 2026-11-02 |
| Ministerial Order 009/26/10/TC of 24/09/2026, OG Special of 25/09/2026 (read whole: arts 1 to 5, permanent residence and effective place of management) | https://www.rra.gov.rw/fileadmin/user_upload/Ministerial_orders-Financial_statements.pdf | 2026-11-02 |
| Ministerial Order 003/26/10/TC of 29/04/2026 (read for arts 2(a) and 3: beneficial tax regimes and deemed controlled transactions) | https://www.rra.gov.rw/fileadmin/Folder_for_2025/Ministerial_Order_on_Simplified_Accounting_Method_April_2026.pdf | 2026-11-02 |
| Law 020/2023 on tax procedures (read for arts 22, 74, 80 to 83, 96, 97) | https://www.rra.gov.rw/fileadmin/user_upload/OG_n___Special_ter_of_31.03.2023_Uburyo_bw_isoresha_Tax_procedures_01.pdf | 2026-11-02 |
| RRA Tax Handbook 2025 (read for exchange of information, withholding tax chapters and summary, foreign tax credit certificate and declaration field) | https://www.rra.gov.rw/fileadmin/Folder_for_2025/RRA_Tax_Handbook_2025_Final.pdf | 2026-11-02 |
| RRA, Laws, policies and rulings page (read for the list of laws and orders in force and the DRC treaty ratification order) | https://www.rra.gov.rw/en/laws-policies-and-rulings | 2026-11-02 |
| Constitution of the Republic of Rwanda of 2003 revised in 2015, OG Special of 24/12/2015 (read for art 95, hierarchy of laws; RwandaLII copy of the Gazette text) | https://rwandalii.org/akn/rw/act/law/2003/nn/eng@2015-12-24/source.pdf | 2026-11-02 |

Not yet confirmed: whether the 15% withholding is a final tax for a non-resident individual without a permanent establishment (the Law does not say so; a non-resident entity without a PE is outside corporate income tax under arts 44 and 47); how "profits repatriated" is measured for a branch, and how the art 60 condition on the payee's registration applies to a remittance to head office; whether any constitutional revision after 2015 changed art 95, and how ITL art 68 interacts with treaties; the list of treaties in force and their rates (the Handbook's generic 10%, 5%, 12% figures are not tied to named treaties, so they are not used); whether the Order under art 50 bis has been issued, so the 1.5% digital services tax is not treated as live; the treatment of a non-resident seller in an indirect transfer where no resident company can withhold; Law 021/2023 on automatic exchange of information and the 2024 Common Reporting Standard Order (not read); whether Law 020/2023 sets a fixed fine amount for failure to withhold separate from the art 81 bands.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-02. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `rw-cross-border` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/rw-cross-border. If neither is available, confirm every figure against the official source pages cited above before relying on it.
