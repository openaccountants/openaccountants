---
name: sz-cross-border
description: "Eswatini cross-border income tax for the year of assessment 1 July 2025 to 30 June 2026 (tax year 2026) under the Income Tax Order 1975 as amended by the Income Tax (Amendment) Act 2023 (in force from 1 July 2024). Covers the source basis and the deemed-source rules, ordinary residence, the permanent establishment definition (fixed place, 30-day services test, dependent agents), non-resident shareholders tax at 15% (the 12.5% rate for Botswana, Lesotho, Namibia and South Africa companies is repealed), non-residents tax on interest at 15%, 15% final withholding on royalties and management charges, 15% on non-resident entertainers, contractors and service providers, branch profits tax at 15% (10% cap under the South Africa treaty protocol), the 10% minimum for non-resident individuals, exit taxation, the foreign tax credit on foreign interest, treaties, deadlines and penalties. Trigger on: Eswatini non-resident tax, Swaziland withholding tax non-resident, branch profits tax Eswatini, per"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/sz-cross-border"
  jurisdiction: "SZ"
  tax_year: "2026"
  last_updated: "2026-11-02"
---

# Eswatini cross-border: source, permanent establishment, non-resident taxes, branch profits tax and treaties (year to 30 June 2026) v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Eswatini taxes income from a source within or deemed to be within Eswatini (Income Tax Order 1975, s7). Non-residents are also taxed through the separate non-resident taxes in Part III and the withholding rules in ss59 to 59C. The Income Tax (Amendment) Act 2023 (Act 20 of 2023) changed several of these from 1 July 2024, the date the Eswatini Revenue Service (ERS) gives:
- it repealed the 12.5% rates for southern African companies (non-resident shareholders tax: Botswana, Lesotho, Namibia and South Africa; branch profits tax: those four and Mozambique);
- it raised non-residents tax on interest from 10% to 15%;
- it added a permanent establishment definition and exit rules.

The year of assessment runs from 1 July to 30 June; this skill covers the year 1 July 2025 to 30 June 2026.

## Who this applies to

- **Source basis (s7).** Gross income is income from a source within or deemed within Eswatini. Residence mainly decides which withholding regime applies, not whether foreign income is taxed. The Order has no general foreign-income charge; the exceptions are below.
- **Deemed Eswatini source (s11(1)).** Amounts are Eswatini-source, wherever paid, if they arise from:
  - a contract for the sale of goods made in Eswatini;
  - services or work done in carrying on a trade in Eswatini;
  - services under a Government employment contract, even if performed abroad;
  - a pension for services in Eswatini (apportioned for mixed service);
  - aircraft businesses of residents and Eswatini-managed companies;
  - the use, or right of use, in Eswatini of patents, designs, trade marks, copyright, films, broadcast material, or plant, machinery, equipment, vehicles or other movable property;
  - imparting scientific, technical, industrial or commercial knowledge for use in Eswatini, and related assistance;
  - a management charge paid by a person ordinarily resident or carrying on business in Eswatini;
  - interest where the debt is secured on property in Eswatini, the borrower is ordinarily resident in Eswatini, or the borrowing relates to a business carried on in Eswatini.
- **Residents' foreign income caught anyway:**
  - foreign interest received by a person ordinarily resident or carrying on business in Eswatini is deemed Eswatini-source, unless it is effectively connected with a foreign branch (s11(9A));
  - interest on foreign government stock not taxed abroad because the holder is not resident there is deemed Eswatini-source (s11(7)).
- **Residence.** The Order uses "ordinarily resident" without a general statutory definition. For particular taxes:
  - a company is non-resident for non-resident shareholders tax if its place of effective management is outside Eswatini (s22(1)(c));
  - a company debtor is deemed ordinarily resident for interest if registered, managed or controlled in Eswatini (s28(c));
  - non-residents tax on interest applies to a company not registered in Eswatini (s27(c)).
- **Permanent establishment (s2, added by Act 20 of 2023 s2).**
  - **Fixed place:** a fixed place of business through which an enterprise's business is wholly or partly carried on. It includes a place of management, a branch, an office, a factory, a workshop, a mine, an oil or gas well, a quarry, a farm or plantation, an installation used in exploring for natural resources, a place where substantial equipment or machinery is used or installed, and a building, construction, assembly or installation project or related supervision. No minimum duration is stated for these.
  - **Services:** services, including consultancy, furnished by a non-resident through employees or other personnel, where the activities continue in Eswatini for more than 30 days in aggregate in any 12-month period beginning or ending in the year of assessment.
  - **Dependent agent:** a person acting in Eswatini for a non-resident creates a permanent establishment if they habitually conclude contracts, or habitually play the principal role leading to contracts that are routinely concluded without material change, in the non-resident's name, for the transfer or use of its property, or for its services. Habitually holding a stock of goods from which they regularly deliver also counts.
  - **Exclusions:** an independent agent acting in the ordinary course of business is excluded, but not one acting exclusively or almost exclusively for closely related persons. Control of, or by, a company does not by itself create a permanent establishment.

Not covered here, refer to a specialist: treaty rate tables and treaty permanent establishment tests, transfer pricing (see [Transfer pricing](sz-transfer-pricing.md)), the interest cap (see [Corporate income tax](sz-corporate-income-tax.md)), VAT on imported services (see [VAT](sz-vat-gst.md)).

## Rates, bands and thresholds

| Item | Amount and conditions | Tax year | Official URL |
|---|---|---|---|
| Non-resident shareholders tax on dividends (s21(2)) | 15% of the dividend. The 12.5% proviso for Botswana, Lesotho, Namibia and South Africa companies was deleted by Act 20 of 2023 s10, from 1 July 2024 | 2026 | https://www.ers.org.sz/documents/IncomeTaxAmendmentAct2023.pdf |
| same, ERS confirmation | ERS: "shall be at 15%" (increase from 12.5%), effective 1 July 2024 | 2026 | https://ers.org.sz/whatsnew-file/1726738466004-Income_Tax_Order_Changes__2024.pdf |
| Non-residents tax on interest (s27) | 15% of the interest ("ten" replaced by "fifteen", Act 20 of 2023 s11). The de minimis exemption for interest of E20 or less a year (s29(c)) was deleted (s12) | 2026 | https://www.ers.org.sz/documents/IncomeTaxAmendmentAct2023.pdf |
| Royalties and management charges to a person not ordinarily resident or carrying on business in Eswatini (s32B) | 15% of the gross amount, final tax | 2026 | https://www.ers.org.sz/documents/IncomeTaxOrder1975.pdf |
| Non-resident public entertainers and sportspersons, and foreign groups (s32A) | 15% of gross remuneration or receipts | 2026 | same |
| Non-resident contractors, construction operations (s59) | 15% of each payment, excluding the shown direct cost of materials; on account of the contractor's tax | 2026 | same |
| Non-resident services under an Eswatini-source services contract (s59A) | 15% of the gross payment; on account of the non-resident's tax; royalties, management charges and s59 payments excluded | 2026 | same |
| Branch profits tax (s32E) | 15% of deemed repatriated income (taxable income less Eswatini tax on it). The 12.5% neighbouring-country proviso and s32E(4) were deleted by Act 20 of 2023 s14 | 2026 | https://www.ers.org.sz/documents/IncomeTaxAmendmentAct2023.pdf |
| Branch profits tax, South African company | Not above 10% of repatriated income (South Africa treaty, Protocol on Article 23) | 2026 | https://www.ers.org.sz/documents/SouthAfrica.pdf |
| Company income tax rate (branch taxable income) | 25% (Third Schedule Part I para 1(a)) | 2026 | https://www.ers.org.sz/documents/IncomeTaxAmendmentAct2023.pdf |
| Non-resident natural person, minimum | Rate cannot reduce total tax below 10% of taxable income, or 3% of the part that is pension (Third Schedule Part I para 2) | 2026 | same |
| Permanent establishment, services test | More than 30 days in aggregate in any 12-month period (s2) | 2026 | same |
| Failure to withhold | Payer personally liable plus additional tax of 20% of the tax not withheld (s40bis(1)) | 2026 | https://www.ers.org.sz/documents/IncomeTaxOrder1975.pdf |
| Withheld but remitted late | 10% under 30 days late; 15% from 30 days; 20% from 90 days; 25% from 180 days (s40bis(2)) | 2026 | same |
| Interest on tax paid late | 18% a year (s57(2)) | 2026 | same |
| Late withholding tax return | Up to E25 a day until received (s33(17), added by Act 20 of 2023 s18) | 2026 | https://www.ers.org.sz/documents/IncomeTaxAmendmentAct2023.pdf |

## The base

**Non-resident shareholders tax (ss21 to 26).**
- **Charged on:** dividends to:
  - a person (other than a company) not ordinarily resident or carrying on business in Eswatini;
  - the estate of a deceased non-resident whose dividend is exempt from normal tax under s12(1)(e)(ii);
  - a company with its place of effective management outside Eswatini;
  - holders of bearer scrip.
- **Who pays:** the paying company (or an Eswatini agent receiving the dividend) pays the tax and may recover it from the shareholder (s24).
- **Exemptions:** dividends from registered agricultural co-operatives in Botswana, Lesotho, Namibia, Eswatini or South Africa; dividends to public-character ecclesiastical, charitable or educational institutions; and dividends Government has exempted in writing (s22(2)).
- **Apportionment:** where the company also has foreign profits, the tax is charged on the Eswatini share of its net profits (s25).
- **Interaction with normal tax:** dividends to non-residents are exempt from normal tax (s12(1)(e)), so this tax is the only Eswatini tax on them.

**Non-residents tax on interest (ss27 to 32).**
- **Charged on:** interest accruing to:
  - a non-company person not ordinarily resident in Eswatini;
  - a non-resident deceased estate;
  - a company not registered in Eswatini.
  
  The debtor must be ordinarily resident or carry on business in Eswatini. Interest paid to an address outside Eswatini is presumed to fall in this charge until the contrary is shown (s28(a)).
- **Who withholds:** the debtor, or an agent receiving the interest (s31).
- **Exemptions (s29):** co-operative interest; public-character institutions; interest on bills or notes financing imports through a recognised bank; loans Government has exempted in writing.
- **Credit against normal tax:** where the interest is also in a person's taxable income (for example, of an Eswatini branch), the tax is credited against normal tax on it (s32(3)).

**Royalties and management charges (s32B).**
- **Rate and finality:** 15% of the gross amount. The tax is final, and the income is exempt from normal tax (s12(1)(u)).
- **Royalty** includes payment of any kind for the use of, or right to use, industrial, commercial or scientific equipment (s2 as amended by Act 20 of 2023 s2(d)).
- **Exemption:** royalties to public-character ecclesiastical, charitable or educational institutions.

**Entertainers (s32A).** 15% of the gross amount, deducted by the local agent, promoter or payer. Without a local intermediary, the group's members are jointly and severally liable.

**Contractors and services (ss59, 59A).**
- **Construction (s59):** "non-resident person" means a person whose principal place of business is outside Eswatini (s59(1)). Payers withhold 15% on construction payments, net of the shown direct cost of materials.
- **Services (s59A):** 15% on the gross amount of an Eswatini-source services contract. Incidental goods are included: ERS's example is a visiting mechanic's labour and parts.
- **Not final:** both are on account. The non-resident still files a return (s59(6), s59A(8a)), and the 2026 ERS return notice requires a return from every person not ordinarily resident who received Eswatini-source gross income.

**Branch profits tax (s32E).** A non-resident company carrying on business in Eswatini through a branch pays 15% on deemed repatriated income on top of normal tax:
- deemed repatriated income = A - B;
- A is the branch's taxable income for the year;
- B is the Eswatini tax payable on that taxable income.

It is treated as normal tax (s32E(3)). It is charged whether or not profits are actually remitted.

**Non-resident individuals.** They are taxed on Eswatini-source income at the individual rates (see [Income tax](sz-income-tax.md)), subject to the 10% minimum above.

**Exit and entry (s32H(4) to (7), added by Act 20 of 2023 s17).**
- **Exit:** a resident who becomes non-resident is deemed to dispose of all business assets (other than taxable assets) at market value at that time.
- **Deferral:** the Commissioner may exempt the person in writing if they intend to resume residence and give security for the tax.
- **Entry:** a non-resident who becomes resident is deemed to acquire their business assets at market value.

**Foreign tax credit (s11(9A)(b), (c)).** The only credit in the Order is for foreign tax on foreign interest deemed Eswatini-source under s11(9A)(a). It is capped at the Eswatini tax on that interest. Otherwise, relief depends on a treaty.

**Treaties (s68).**
- **Status:** an agreement published by Gazette notice has effect as if enacted in the Order, for the immunity, exemption or relief it gives. This holds only while the other country gives the matching relief the effect of law (s68(2)).
- **Treaties published by ERS:** Botswana, Lesotho, Mauritius, Seychelles, South Africa, Taiwan and the United Kingdom.
- **South Africa treaty (2004):**
  - dividends are capped at 10% for a beneficial owner company holding at least 25% of the capital, 15% otherwise (Article 10(2));
  - branch profits tax on the repatriated income of a South African company's permanent establishment is not discrimination under Article 23 provided it does not exceed 10% (Protocol, 23 January 2004), which in practice caps it at 10%.
- **Supremacy:** section 69quin (Act 20 of 2023 s36) says the Order prevails over any other law prescribing a rate of tax.

## Deadlines and filing

| Obligation | When | Source |
|---|---|---|
| Non-resident shareholders tax | company pays within 30 days of the date the dividend is payable, with a return of payees (s26(1)); the ERS rates page shows the 15th of the following month | Order s26; ERS Rates and Thresholds |
| Non-residents tax on interest | within 14 days after the interest accrues, with a return of payees (s32(1), (2)); the ERS rates page shows the 15th of the following month | Order s32; ERS Rates and Thresholds |
| Entertainers, royalties and management charges, contractors, services | within 15 days from the date of payment (ss32A(3), 32B(4)(b), 59(5)(b), 59A(5)); the ERS rates page shows the 15th of the following month | Order; ERS Rates and Thresholds |
| Withholding tax return | with each payment of withheld tax (s33(16), added by Act 20 of 2023) | Act 20 of 2023 s18 |
| Annual return of payments to non-resident contractors and service providers | within 30 days after the end of the year of assessment (ss59(8), 59A(8)) | Order |
| Notify ERS of an agreement with a non-resident for services in Eswatini | within 30 days of entering into it, giving its nature, start, duration, estimated value and the non-resident's address (s59C) | Order |
| Annual return, non-individual entities including branches, year ended 30 June 2026 | 31 October 2026, on TaxEase; other approved year ends within four months | ERS notice, returns for tax year end 2026 |
| Annual return, non-resident individuals with Eswatini-source income | the notice requires a return from every person not ordinarily resident with Eswatini-source gross income; the date follows the taxpayer segment: 30 November 2026 for individuals (employment income above E1,000,000, employment and other income, assets above E3 million), 31 October 2026 for VAT and non-VAT registered businesses | same |

Payment is by EFT, bank deposit, speed point at ERS service centres or MoMo Pay; cash is not accepted (2026 notice, para 7).

## Penalties and interest

- **Failure to withhold:** the payer is personally liable for the tax and pays additional tax of 20% of it (s40bis(1); ss32A(4), 32B(6), 59(9), 59A(9)). The additional tax cannot be recovered from the payee (s40bis(3)).
- **Late remittance of tax withheld:** 10%, 15%, 20% or 25% of the tax by lateness band (s40bis(2)).
- **Interest:** 18% a year on tax not paid when due (s57(2)).
- **Late withholding return:** up to E25 a day until the return is received (s33(17)).
- **Offences:**
  - failing to withhold, remit and account for withholding tax, or to comply with s32E (branch profits tax): a fine up to E50,000, imprisonment up to five years, or both (s66(2));
  - failing to notify a non-resident agreement under s59C: a fine up to E10,000, imprisonment up to one year, or both (s66(1)(j)).
- **Understatement:** additional tax of twice the tax understated (s40(1)(b), (c)), which the Commissioner may waive or remit in part or full where there was no intent to evade (s40(3)).

## Cross-border points

This whole skill is about cross-border points. In short:
- Eswatini taxes Eswatini-source and deemed-source income;
- a non-resident is taxed through a permanent establishment at 25% plus 15% branch profits tax (10% for a South African company), or by 15% non-resident taxes on dividends, interest, royalties, management charges, entertainers, contractors and services;
- royalties and management charges are final, while contractor and service withholding is on account;
- residents get a credit only for foreign tax on foreign interest;
- treaties apply under s68 subject to reciprocity.

## Two worked examples that recompute

### Example 1: branch profits tax on a non-resident's Eswatini branch

Highveld Engineering BV (Netherlands) runs a branch in Manzini. For the year to 30 June 2026 its taxable income is E4,000,000. The Netherlands has no treaty with Eswatini on the ERS list.

- **Normal tax at 25%:** E1,000,000.
- **Deemed repatriated income:** 4,000,000 - 1,000,000 = E3,000,000.
- **Branch profits tax at 15%:** E450,000.
- **Total Eswatini tax:** E1,450,000, an effective 36.25% of taxable income.

```oa-check
name: Eswatini branch profits tax, taxable income E4m (year to 30 June 2026)
inputs:
  taxable_income: 4000000
  cit_rate: 0.25
  bpt_rate: 0.15
steps:
  - normal_tax: taxable_income * cit_rate
  - repatriated: taxable_income - normal_tax
  - branch_profits_tax: repatriated * bpt_rate
  - total_tax: normal_tax + branch_profits_tax
  - effective_rate: total_tax / taxable_income
expected:
  normal_tax: 1000000.00
  repatriated: 3000000.00
  branch_profits_tax: 450000.00
  total_tax: 1450000.00
  effective_rate: 0.3625
```

### Example 2: decision, branch or subsidiary for a South African group

A South African company will earn E4,000,000 of taxable profit a year in Eswatini. It plans to pay home E1,000,000 a year and reinvest the rest. Should it operate through a branch or a 100% subsidiary?

- **Both:** normal tax at 25% = E1,000,000.
- **Branch:** branch profits tax applies to deemed repatriated income whether or not cash is sent. The South Africa treaty Protocol caps it at 10%: 10% x 3,000,000 = E300,000.
- **Subsidiary:** non-resident shareholders tax applies only to dividends paid. The treaty rate for a company holding at least 25% is 10%: 10% x 1,000,000 = E100,000.
- **The figure that decides it:** the subsidiary costs E200,000 a year less while profits are retained. If all E3,000,000 were paid out each year, both would cost E300,000. Without the treaty (a non-South African parent), both rates would be 15%.
- **Conditions:** the parent must be a South African resident and the beneficial owner of the dividends; the treaty relief applies through s68(2) only while South Africa gives matching relief the effect of law, and the s69quin question on the "Not yet confirmed" line is open.

```oa-check
name: Eswatini branch vs subsidiary, SA parent, profit E4m, E1m paid out (year to 30 June 2026)
inputs:
  taxable_income: 4000000
  cit_rate: 0.25
  treaty_bpt_cap: 0.10
  treaty_dividend_rate: 0.10
  dividend_paid: 1000000
steps:
  - normal_tax: taxable_income * cit_rate
  - after_tax_profit: taxable_income - normal_tax
  - branch_extra: after_tax_profit * treaty_bpt_cap
  - subsidiary_extra: dividend_paid * treaty_dividend_rate
  - annual_saving_subsidiary: branch_extra - subsidiary_extra
  - subsidiary_extra_full_payout: after_tax_profit * treaty_dividend_rate
expected:
  normal_tax: 1000000.00
  after_tax_profit: 3000000.00
  branch_extra: 300000.00
  subsidiary_extra: 100000.00
  annual_saving_subsidiary: 200000.00
  subsidiary_extra_full_payout: 300000.00
```

## Ask the client first

1. For a company: where it is registered and where effective management and control is exercised; for an individual, whether they are ordinarily resident and how many days they spend in Eswatini.
2. What the non-resident does in Eswatini: an office or site, equipment, a project, staff providing services (days in each 12-month period), or an agent concluding contracts or holding stock.
3. Each payment to a non-resident by type (dividend, interest, royalty, management charge, services, construction, entertainment), with amounts, dates paid and tax withheld.
4. The payee's country of residence, whether a treaty is claimed, and whether a South African parent holds at least 25% of the capital.
5. For a branch: taxable income and the Eswatini tax on it for the year.
6. For residents: foreign interest and the foreign tax paid on it, and any plan to leave Eswatini.

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax (Amendment) Act 2023 (Act 20 of 2023), scanned, pages rendered and read by eye: read for s1, s2 (permanent establishment, associate person, royalty), ss10 to 16 (ss21, 27, 29, 32C, 32E, 32F, 32G), s17 (s32H exit rules), s18 (s33), s23 (s40), s36 (s69quin) and s39 (Third Schedule Part I) | https://www.ers.org.sz/documents/IncomeTaxAmendmentAct2023.pdf | 2026-11-02 |
| Income Tax Order 1975, ERS consolidated copy to the 2013 amendments: read for s7, s11, s12(1)(e), (h), (u), ss21 to 32B, s32E, ss33, 40, 40bis, 57, ss59 to 59C, s66 and s68 | https://www.ers.org.sz/documents/IncomeTaxOrder1975.pdf | 2026-11-02 |
| ERS, Income Tax Order changes 2024 (read for the 1 July 2024 effective date and the changes to ss21, 27 and 32E) | https://ers.org.sz/whatsnew-file/1726738466004-Income_Tax_Order_Changes__2024.pdf | 2026-11-02 |
| ERS, Withholding Taxes (whole page read; it still shows 10% on non-resident interest, superseded by the Act) | https://www.ers.org.sz/IncomeTax/Withholding | 2026-11-02 |
| ERS, Rates and Thresholds (whole page read; withholding due dates and additional tax scale) | https://www.ers.org.sz/IncomeTax/RatesandThres | 2026-11-02 |
| ERS, public notice, annual income tax returns for tax year end 2026 (read for who files, including non-residents, deadlines and payment methods) | https://ers.org.sz/whatsnew-file/1791462650754-1784270658474_Notice_for_Filing_Income_tax_Returns_Public_Notice_Final_Aligned.pdf | 2026-11-02 |
| Eswatini and South Africa double taxation agreement and Protocol (read for the Gazette notice, Article 9, Article 10 and the Protocol on branch profits tax) | https://www.ers.org.sz/documents/SouthAfrica.pdf | 2026-11-02 |
| ERS, Tax Legislations page (read for the list of treaties published: Botswana, Lesotho, Mauritius, Seychelles, South Africa, Taiwan, United Kingdom) | https://www.ers.org.sz/LegalandPolicy/TaxLegislation | 2026-11-02 |
| 2026-27 Budget Speech, ERS copy (read for paras 159 to 167; no new income tax measures announced) | https://ers.org.sz/whatsnew-file/1772201986460-2026_27_FY_Budget_Speech_2026.pdf | 2026-11-02 |

Not yet confirmed:
- The Gazette commencement notice for Act 20 of 2023; 1 July 2024 rests on the ERS 2024 summary.
- Whether the remittance periods in ss26, 32, 32A, 32B, 59 and 59A have been aligned by law with the "15th of the following month" on the ERS rates page; only ss32C, 32F and 32G were seen amended.
- Whether s69quin (Order prevails over other laws prescribing a rate) limits treaty rates given effect under s68; no ERS guidance found.
- Treaty rates and permanent establishment articles in the Botswana, Lesotho, Mauritius, Seychelles, Taiwan and United Kingdom treaties (not read), and any treaties in force but not on the ERS list.
- Whether non-resident shareholders tax is formally a final tax: the Order exempts the dividend from normal tax (s12(1)(e)) but does not use the word "final".
- Any Tax Administration Act replacing the Order's administrative and penalty provisions: none found on the ERS legislation page.
- The sibling skills sz-corporate-income-tax and sz-tax-overview still show 12.5% non-resident shareholders tax, 12.5% branch profits tax and 10% non-resident interest; Act 20 of 2023 and the ERS 2024 summary give 15% for all three.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-02. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `sz-cross-border` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/sz-cross-border. If neither is available, confirm every figure against the official source pages cited above before relying on it.
