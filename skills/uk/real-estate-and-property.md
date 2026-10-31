---
name: real-estate-and-property
description: "Use this skill when an individual or company buys, lets or sells residential property in the United Kingdom. It covers Stamp Duty Land Tax (England and Northern Ireland) in depth, with the slice method, the 5% higher rates for additional dwellings, the 2% non-resident surcharge, first-time buyer relief up to GBP 500,000, the 17% rate for companies and the 14-day return; the Scottish LBTT bands, 8% Additional Dwelling Supplement and Welsh LTT tables; the 2026/27 rules on letting income (property allowance, finance-cost restriction at 20%, property rates from 2027/28); and Capital Gains Tax on residential property at 18%/24% with the 60-day return. Figures are for transactions and tax year 2026/27 as at 30 October 2026. Trigger on SDLT, stamp duty, LBTT, ADS, LTT, buy-to-let, second home surcharge, Section 24, 60-day CGT return. Out of scope: full SA105 work (uk-rental-sa105), PRR and full CGT (uk-capital-gains-sa108), company landlords (uk-corporation-tax), ATED."
jurisdiction: GB
category: international
tax_year: 2026
last_updated: 2026-10-30
version: 1.1
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Real Estate and Property in the United Kingdom: buying, letting and selling

## Real Estate and Property in the United Kingdom: Stamp Duty Land Tax on purchase, and what follows

This skill covers the tax on buying residential property in England and Northern Ireland, Stamp Duty Land Tax (SDLT), in depth: the standard bands, the higher rates landlords need to plan around, and the reliefs that actually apply versus the ones that get assumed. It also gives the purchase tax tables for Scotland (Land and Buildings Transaction Tax, LBTT) and Wales (Land Transaction Tax, LTT), the headline rules for letting income in 2026/27, and Capital Gains Tax (CGT) when a residential property is sold, including the 60-day return.

SDLT figures are for transactions with an effective date (normally completion) on or after 1 April 2025. They were still the law on 30 October 2026. Income tax and CGT figures are for the tax year 6 April 2026 to 5 April 2027 (2026/27).

## Who this is for

Individual buyers, landlords and sellers of UK residential property, and their advisers. That includes landlords buying an additional property (buy-to-let), first-time buyers, non-UK residents, and companies buying dwellings.

- **Buying:** SDLT in England and Northern Ireland is covered step by step. LBTT (Scotland) and LTT (Wales) are separate taxes with their own bands; this skill gives their rate tables, the second-home charge and the return deadline.
- **Letting:** the finance-cost restriction and the 2026/27 and 2027/28 rates are here. The full SA105 computation, Rent-a-Room, the Non-resident Landlord Scheme and Making Tax Digital are in uk-rental-sa105.
- **Selling:** CGT rates and the 60-day return are here. Private Residence Relief, Letting Relief and the full CGT computation are in uk-capital-gains-sa108.

Not covered: non-residential and mixed-use property beyond the rate tables, the Annual Tax on Enveloped Dwellings, corporation tax for company landlords (see uk-corporation-tax), VAT on property, and Scottish income tax bands (see uk-scottish-income-tax).

## Before you start, ask the client

- Where is the property: England, Northern Ireland, Scotland or Wales? (It decides which purchase tax applies.)
- After completion, will this be the only residential property worth £40,000 or more they own anywhere in the world?
- Are they replacing a main residence they have already sold, or still own alongside this purchase? (Decides whether the higher rates apply or can later be reclaimed.)
- Is this their first property purchase, and is the price £500,000 or less? (Decides first-time buyer relief in England and Northern Ireland.)
- How many days were they in the UK in the 12 months before the purchase, and how many do they expect in the 12 months after? (Decides the 2% surcharge and any refund of it.)
- Is the buyer an individual, or a company or other non-natural person? (The 17% flat rate can apply to dwellings over £500,000 bought by certain companies.)
- If letting: the rent, the mortgage interest and other finance costs, and the client's other income.
- If selling: the completion date, the expected gain, and whether the client is UK resident.

## The method, step by step

1. **Decide which tax applies.** England or Northern Ireland: SDLT. Scotland: LBTT. Wales: LTT. Then confirm the transaction is residential, not non-residential or mixed-use. The bands and thresholds are entirely different, and in England and Northern Ireland non-residential or mixed-use property starts at £150,000.
2. **Compute standard SDLT on a slice basis.** Each portion of the price is taxed at its own band's rate, not the whole price at one rate. This is the step most often done wrong by hand. Always work band by band. The bands are 0% up to £125,000, 2% to £250,000, 5% to £925,000, 10% to £1,500,000 and 12% above (Finance Act 2003 s.55, Table A).
3. **Check the higher rates for additional dwellings.** They apply at £40,000 or more where all of these hold: after the purchase it will not be the buyer's only residential property worth £40,000 or more anywhere in the world; the buyer has not sold or given away their previous main home; and no one else has a lease on it with more than 21 years left. The rules apply to each buyer and their spouse. Where the higher rates apply, use the higher rates table: 5%, 7%, 10%, 15% and 17% on the same bands (FA 2003 Sch 4ZA para 1). That is 5 percentage points on every band.
4. **Replacing a main residence.** If the old main home has not been sold on the day the new purchase completes, the higher rates apply at completion, because the buyer owns two properties. If the previous main home is then sold within 3 years of buying the new one, the higher-rate part can be refunded. Claim within 12 months of the later of the sale and the filing date of the new return. Flag this window to the client straight away; it gets missed once the purchase is behind them.
5. **First-time buyer relief.** Only if every buyer is a first-time buyer and the price is not more than £500,000: 0% up to £300,000, 5% on the portion from £300,001 to £500,000 (FA 2003 Sch 6ZA). Above £500,000 there is no relief at all. Standard rates apply to the whole price, not a partial version of the relief.
6. **Non-UK resident surcharge.** An individual who is not present in the UK for at least 183 days in the 12 months before the purchase is "not a UK resident" for SDLT. They pay 2% on top of every rate that applies, including the zero bands, the first-time buyer rates and the higher rates (FA 2003 s.75ZA and Sch 9A). If they are then present in the UK for at least 183 days in any continuous 365-day period within the window that ends 365 days after the purchase, they can claim the 2% back by amending the return within 2 years of the effective date.
7. **Companies.** A company pays the higher rates on any residential property it buys for £40,000 or more (unless it is subject to a lease with more than 21 years left), even if it owns no other dwelling. If a dwelling costs more than £500,000, check whether the 17% flat rate for certain non-natural persons applies instead (FA 2003 Sch 4A). That is one rate on the whole price, not a banded calculation. Relief from the 17% rate is available for some uses, such as a property rental business or a property developer or trader; each has its own conditions.
8. **File and pay within 14 days.** The SDLT return must reach HMRC within 14 days of the effective date (FA 2003 s.76), and the tax is paid by then. In practice the solicitor files and pays on completion. The accountant should confirm it has been done, not assume it.
9. **Scotland and Wales.** Apply the LBTT or LTT tables below on the same slice basis. The Scottish Additional Dwelling Supplement (ADS) is 8% of the whole price, not a banded addition. The Welsh higher residential rates are a separate table, not the main table plus a fixed addition. Both returns are due within 30 days.
10. **If the property is let.** Residential mortgage interest is not deducted from rental profit. For 2026/27 it gives a tax reduction at 20% of the lower of the finance costs (with any brought forward) and the property profits, capped by the client's adjusted total income. The unused part carries forward. The full computation is in uk-rental-sa105.
11. **When the property is sold.** Work out the gain and the CGT at 18% or 24%. If CGT is due on a UK residential property, report and pay within 60 days of completion. A non-resident reports every disposal of UK property or land within 60 days, even with no tax to pay. Reliefs and the full computation are in uk-capital-gains-sa108.

## The traps

- Applying the whole purchase price to a single band instead of computing tax on a slice basis. This overstates the liability.
- Forgetting that the higher rates start at £40,000, not some higher round-number threshold. A modest second property purchase is still caught.
- Using the old £625,000 first-time buyer ceiling. For transactions from 1 April 2025 the law says £500,000 (FA 2003 Sch 6ZA para 3(3)). HMRC's non-resident guidance still has a worked example dated 1 April 2025 that tests against £625,000; follow the statute.
- Missing the 3-year refund window when a client paid the higher rates on a genuine main-residence replacement because the old home had not sold at completion.
- Treating the 2% non-resident surcharge and the 5% higher rates as alternatives. They stack when both conditions are met: 7%, 9%, 12%, 17% and 19% on the bands.
- Missing that Multiple Dwellings Relief was abolished for SDLT transactions completing on or after 1 June 2024. Contracts exchanged on or before 6 March 2024 keep it, if not varied after that date. Portfolio landlords can no longer average the price across several dwellings in one SDLT transaction.
- Applying the Scottish ADS by band. It is 8% of the whole price.
- Deducting residential mortgage interest as an expense on a let property. Since 2020/21 no deduction is allowed for income tax; relief is only the 20% tax reduction (ITTOIA 2005 s.272A(4)).
- Assuming the 20% finance-cost credit continues. From 2027/28 it is given at the property basic rate of 22%, and property income is taxed at 22%, 42% and 47% (Finance Act 2026 s.7 and Sch 1 para 40).
- Waiting for the Self Assessment return to report a residential property gain. The 60-day return and payment come first.

## Rates, thresholds and deadlines

### Stamp Duty Land Tax: England and Northern Ireland (effective date on or after 1 April 2025)

| What | Value | Source |
| --- | --- | --- |
| Standard residential bands | 0% up to £125,000; 2% £125,001 to £250,000; 5% £250,001 to £925,000; 10% £925,001 to £1,500,000; 12% over £1,500,000 | FA 2003 s.55 Table A: https://www.legislation.gov.uk/ukpga/2003/14/section/55 ; https://www.gov.uk/stamp-duty-land-tax/residential-property-rates |
| Higher rates for additional dwellings | 5% up to £125,000; 7% to £250,000; 10% to £925,000; 15% to £1,500,000; 17% above (5 points on every band). Applies at £40,000 or more | FA 2003 Sch 4ZA para 1: https://www.legislation.gov.uk/ukpga/2003/14/schedule/4ZA/paragraph/1 ; https://www.gov.uk/guidance/stamp-duty-land-tax-buying-an-additional-residential-property |
| Refund of higher rates on replacing a main home | Previous main home sold within 3 years of buying the new one; claim within 12 months of the later of the sale and the new return's filing date | https://www.gov.uk/guidance/stamp-duty-land-tax-buying-an-additional-residential-property |
| First-time buyer relief | 0% up to £300,000; 5% £300,001 to £500,000; no relief if the price is over £500,000 | FA 2003 Sch 6ZA: https://www.legislation.gov.uk/ukpga/2003/14/schedule/6ZA ; https://www.gov.uk/stamp-duty-land-tax/residential-property-rates |
| Non-UK resident surcharge | 2% added to each rate, including zero bands, first-time buyer rates and higher rates | FA 2003 s.75ZA: https://www.legislation.gov.uk/ukpga/2003/14/section/75ZA ; https://www.gov.uk/guidance/rates-of-stamp-duty-land-tax-for-non-uk-residents |
| Non-UK resident test and refund | UK resident only if present at least 183 days in a continuous 365-day period within the relevant period; refund if met within the window ending 365 days after the effective date, claimed within 2 years | FA 2003 Sch 9A para 4: https://www.legislation.gov.uk/ukpga/2003/14/schedule/9A ; https://www.gov.uk/guidance/rates-of-stamp-duty-land-tax-for-non-uk-residents |
| Companies buying dwellings | Higher rates on any dwelling of £40,000 or more; 17% flat rate on a dwelling costing more than £500,000 bought by certain non-natural persons | FA 2003 Sch 4A para 1: https://www.legislation.gov.uk/ukpga/2003/14/schedule/4A/paragraph/1 ; https://www.gov.uk/guidance/stamp-duty-land-tax-corporate-bodies |
| New residential lease: rent | 1% on the net present value of the rent above £125,000 | https://www.gov.uk/stamp-duty-land-tax/residential-property-rates |
| Non-residential and mixed-use | 0% up to £150,000; 2% £150,001 to £250,000; 5% above £250,000 | FA 2003 s.55 Table B: https://www.legislation.gov.uk/ukpga/2003/14/section/55 ; https://www.gov.uk/stamp-duty-land-tax/nonresidential-and-mixed-rates |
| Return and payment | Within 14 days of the effective date (normally completion) | FA 2003 s.76(1): https://www.legislation.gov.uk/ukpga/2003/14/section/76 ; https://www.gov.uk/stamp-duty-land-tax |
| Multiple Dwellings Relief | Abolished for transactions completing on or after 1 June 2024; contracts exchanged on or before 6 March 2024 keep it if not varied | HMRC SDLTM29901: https://www.gov.uk/hmrc-internal-manuals/stamp-duty-land-tax-manual/sdltm29901 |

### Land and Buildings Transaction Tax: Scotland

| What | Value | Source |
| --- | --- | --- |
| Residential bands (since 1 April 2021) | 0% up to £145,000; 2% £145,001 to £250,000; 5% £250,001 to £325,000; 10% £325,001 to £750,000; 12% over £750,000 | https://revenue.scot/taxes/land-buildings-transaction-tax/residential-property |
| First-time buyer relief | Nil rate band raised to £175,000 (saves up to £600) | https://revenue.scot/taxes/land-buildings-transaction-tax/residential-property |
| Additional Dwelling Supplement | 8% of the whole price where the contract was entered into on or after 5 December 2024 (6% for earlier contracts); applies at £40,000 or more; companies pay it on every dwelling | SSI 2024/367 art. 2: https://www.legislation.gov.uk/ssi/2024/367/article/2/made ; https://revenue.scot/taxes/land-buildings-transaction-tax/additional-dwelling-supplement-ads |
| ADS and replacing a main home | Not due if the previous main residence was sold in the 36 months before; repayment if it is sold within 36 months after | https://revenue.scot/taxes/land-buildings-transaction-tax/additional-dwelling-supplement-ads |
| Non-residential bands | 0% up to £150,000; 1% £150,001 to £250,000; 5% above £250,000 | https://revenue.scot/taxes/land-buildings-transaction-tax/non-residential-property |
| Return | Within 30 days beginning with the day after the effective date | LBTT (Scotland) Act 2013 s.29(3): https://www.legislation.gov.uk/asp/2013/11/section/29 |

### Land Transaction Tax: Wales

| What | Value | Source |
| --- | --- | --- |
| Main residential rates (since 10 October 2022) | 0% up to £225,000; 6% £225,001 to £400,000; 7.5% £400,001 to £750,000; 10% £750,001 to £1,500,000; 12% over £1,500,000 | https://www.gov.wales/land-transaction-tax-rates-and-bands |
| Higher residential rates (since 11 December 2024) | 5% up to £180,000; 8.5% £180,001 to £250,000; 10% £250,001 to £400,000; 12.5% £400,001 to £750,000; 15% £750,001 to £1,500,000; 17% over £1,500,000 | https://www.gov.wales/land-transaction-tax-rates-and-bands ; WSI 2024/1311: https://www.legislation.gov.uk/wsi/2024/1311/contents/made |
| Non-residential rates (since 22 December 2020) | 0% up to £225,000; 1% £225,001 to £250,000; 5% £250,001 to £1,000,000; 6% over £1,000,000 | https://www.gov.wales/land-transaction-tax-rates-and-bands |
| Return | Within 30 days beginning with the day after the effective date | Land Transaction Tax and Anti-avoidance of Devolved Taxes (Wales) Act 2017 s.44: https://www.legislation.gov.uk/anaw/2017/1/section/44 |

### Letting income: 2026/27, with the 2027/28 change (England and Northern Ireland rates)

| What | Value | Source |
| --- | --- | --- |
| Property allowance | £1,000 a year of gross property income; above that, use it instead of expenses, never both | https://www.gov.uk/guidance/tax-free-allowances-on-property-and-trading-income |
| Residential finance costs | No deduction from 2020/21 onwards (individuals, for income tax) | ITTOIA 2005 s.272A(4): https://www.legislation.gov.uk/ukpga/2005/5/section/272A |
| Finance cost tax reduction, 2026/27 | Basic rate (20%) on the lower of the finance costs (with any brought forward) and the adjusted property profits, capped by adjusted total income; the unused part carries forward | ITTOIA 2005 s.274AA: https://www.legislation.gov.uk/ukpga/2005/5/section/274AA ; Finance Act 2026 s.2: https://www.legislation.gov.uk/ukpga/2026/11/section/2 |
| Income tax rates, 2026/27 | Basic 20%, higher 40%, additional 45% | Finance Act 2026 s.2: https://www.legislation.gov.uk/ukpga/2026/11/section/2 |
| Property rates from 2027/28 | Property basic 22%, property higher 42%, property additional 47%; the finance cost reduction moves to the property basic rate | Finance Act 2026 s.7: https://www.legislation.gov.uk/ukpga/2026/11/section/7 ; ITTOIA 2005 s.274AA(5) as amended by FA 2026 Sch 1 para 40 |

### Capital Gains Tax on residential property: 2026/27

| What | Value | Source |
| --- | --- | --- |
| Rates for individuals | 18% on gains within the unused basic rate band, 24% above | TCGA 1992 s.1H(3): https://www.legislation.gov.uk/ukpga/1992/12/section/1H ; https://www.gov.uk/capital-gains-tax/rates |
| Trustees and personal representatives | 24% | TCGA 1992 s.1H(6) and (8): https://www.legislation.gov.uk/ukpga/1992/12/section/1H |
| Annual exempt amount | £3,000 for 2026/27 | https://www.gov.uk/capital-gains-tax/rates |
| 60-day return | On or before the 60th day after completion; UK residents report and pay when CGT is due; non-residents report every disposal of UK property or land, even with no tax | FA 2019 Sch 2 para 3: https://www.legislation.gov.uk/ukpga/2019/1/schedule/2/paragraph/3 ; https://www.gov.uk/report-and-pay-your-capital-gains-tax/if-you-sold-a-property-in-the-uk-on-or-after-6-april-2020 |

### Penalties and interest

| What | Value | Source |
| --- | --- | --- |
| SDLT return late | £100 if delivered within 3 months after the filing date; £200 otherwise | FA 2003 Sch 10 para 3: https://www.legislation.gov.uk/ukpga/2003/14/schedule/10/part/1 |
| SDLT return more than 12 months late | An extra tax-related penalty of up to the full tax on the transaction | FA 2003 Sch 10 para 4: https://www.legislation.gov.uk/ukpga/2003/14/schedule/10/part/1 |
| SDLT records | Keep until the sixth anniversary of the effective date (or until an enquiry ends, if later); penalty up to £3,000 | FA 2003 Sch 10 paras 9 and 11: https://www.legislation.gov.uk/ukpga/2003/14/schedule/10/part/2 |
| SDLT paid late | Interest on the unpaid tax | FA 2003 s.87: https://www.legislation.gov.uk/ukpga/2003/14/section/87 ; https://www.gov.uk/guidance/penalties-and-interest-on-a-late-stamp-duty-land-tax-return |
| 60-day CGT return late | £100; after 6 months the greater of 5% of the tax and £300; a further penalty after 12 months | FA 2009 Sch 55 paras 3, 5 and 6 (table item 2A): https://www.legislation.gov.uk/ukpga/2009/10/schedule/55 |

## Worked examples

### Example 1: buy-to-let in England, buyer already owns a home

A UK-resident buyer completes on a residential buy-to-let in England for £500,000 in April 2026. They already own their main home, so after completion they own two dwellings worth £40,000 or more. The higher rates apply. They are not a first-time buyer, and they are UK resident, so there is no surcharge.

- 5% on the first £125,000 = £6,250
- 7% on the next £125,000 (£125,001 to £250,000) = £8,750
- 10% on the final £250,000 (£250,001 to £500,000) = £25,000
- Total SDLT = £40,000, against £15,000 at the standard rates.

The return and payment are due within 14 days of completion. Once the property is let, the mortgage interest is not deducted from rent; it gives a 20% tax reduction for 2026/27 (22% from 2027/28).

```oa-check
name: SDLT higher rates, England, GBP 500,000 additional dwelling (from 1 April 2025)
inputs:
  price: 500000
steps:
  - band_1: min(price, 125000) * 0.05
  - band_2: (min(price, 250000) - 125000) * 0.07
  - band_3: (min(price, 925000) - 250000) * 0.10
  - sdlt_higher: band_1 + band_2 + band_3
  - std_2: (min(price, 250000) - 125000) * 0.02
  - std_3: (min(price, 925000) - 250000) * 0.05
  - sdlt_standard: std_2 + std_3
  - extra_cost: sdlt_higher - sdlt_standard
expected:
  sdlt_higher: 40000.00
  sdlt_standard: 15000.00
  extra_cost: 25000.00
```

### Example 2: non-UK resident first-time buyer in England

A buyer living abroad completes on their first home in England for £450,000. They spent 77 days in the UK in the 12 months before completion, so they are not UK resident for SDLT. The price is not more than £500,000, so first-time buyer relief applies, and the 2% surcharge is added to each first-time buyer rate.

- (0% + 2%) on the first £300,000 = £6,000
- (5% + 2%) on the final £150,000 = £10,500
- Total SDLT = £16,500. Without the surcharge it would be £7,500.

If the buyer is then in the UK for at least 183 days in a continuous 365-day period that ends within 365 days after completion, the £9,000 surcharge can be reclaimed by amending the return within 2 years of completion.

```oa-check
name: SDLT first-time buyer with non-resident surcharge, GBP 450,000 (from 1 April 2025)
inputs:
  price: 450000
steps:
  - band_1: min(price, 300000) * 0.02
  - band_2: (min(price, 500000) - 300000) * 0.07
  - sdlt_with_surcharge: band_1 + band_2
  - sdlt_ftb_only: (min(price, 500000) - 300000) * 0.05
  - surcharge: sdlt_with_surcharge - sdlt_ftb_only
expected:
  sdlt_with_surcharge: 16500.00
  sdlt_ftb_only: 7500.00
  surcharge: 9000.00
```

*Working paper aid only. Confirm every figure against the law and the gov.uk, Revenue Scotland or Welsh Government page cited before filing, and have it reviewed by a chartered accountant or licensed tax adviser before acting on it.*

## Sources

| Source | URL | Read on |
|---|---|---|
| Finance Act 2003 s.55 (SDLT Tables A and B) | https://www.legislation.gov.uk/ukpga/2003/14/section/55 | 2026-10-30 |
| Finance Act 2003 Sch 4ZA para 1 (higher rates) | https://www.legislation.gov.uk/ukpga/2003/14/schedule/4ZA/paragraph/1 | 2026-10-30 |
| Finance Act 2003 Sch 6ZA (first-time buyer relief) | https://www.legislation.gov.uk/ukpga/2003/14/schedule/6ZA | 2026-10-30 |
| Finance Act 2003 s.75ZA (2% surcharge) | https://www.legislation.gov.uk/ukpga/2003/14/section/75ZA | 2026-10-30 |
| Finance Act 2003 Sch 9A (non-resident test) | https://www.legislation.gov.uk/ukpga/2003/14/schedule/9A | 2026-10-30 |
| Finance Act 2003 Sch 4A para 1 (17% rate) | https://www.legislation.gov.uk/ukpga/2003/14/schedule/4A/paragraph/1 | 2026-10-30 |
| Finance Act 2003 s.76 (return within 14 days) | https://www.legislation.gov.uk/ukpga/2003/14/section/76 | 2026-10-30 |
| Finance Act 2003 s.87 (interest) | https://www.legislation.gov.uk/ukpga/2003/14/section/87 | 2026-10-30 |
| Finance Act 2003 Sch 10 Part 1 (late return penalties) | https://www.legislation.gov.uk/ukpga/2003/14/schedule/10/part/1 | 2026-10-30 |
| Finance Act 2003 Sch 10 Part 2 (records) | https://www.legislation.gov.uk/ukpga/2003/14/schedule/10/part/2 | 2026-10-30 |
| GOV.UK, SDLT: residential property rates | https://www.gov.uk/stamp-duty-land-tax/residential-property-rates | 2026-10-30 |
| GOV.UK, SDLT: non-residential and mixed rates | https://www.gov.uk/stamp-duty-land-tax/nonresidential-and-mixed-rates | 2026-10-30 |
| GOV.UK, SDLT: buying an additional residential property | https://www.gov.uk/guidance/stamp-duty-land-tax-buying-an-additional-residential-property | 2026-10-30 |
| GOV.UK, Rates of SDLT for non-UK residents | https://www.gov.uk/guidance/rates-of-stamp-duty-land-tax-for-non-uk-residents | 2026-10-30 |
| GOV.UK, SDLT: corporate bodies | https://www.gov.uk/guidance/stamp-duty-land-tax-corporate-bodies | 2026-10-30 |
| GOV.UK, Stamp Duty Land Tax overview | https://www.gov.uk/stamp-duty-land-tax | 2026-10-30 |
| GOV.UK, Penalties and interest on a late SDLT return | https://www.gov.uk/guidance/penalties-and-interest-on-a-late-stamp-duty-land-tax-return | 2026-10-30 |
| HMRC SDLT Manual SDLTM29901 (abolition of MDR) | https://www.gov.uk/hmrc-internal-manuals/stamp-duty-land-tax-manual/sdltm29901 | 2026-10-30 |
| Revenue Scotland, LBTT residential property | https://revenue.scot/taxes/land-buildings-transaction-tax/residential-property | 2026-10-30 |
| Revenue Scotland, Additional Dwelling Supplement | https://revenue.scot/taxes/land-buildings-transaction-tax/additional-dwelling-supplement-ads | 2026-10-30 |
| Revenue Scotland, LBTT non-residential property | https://revenue.scot/taxes/land-buildings-transaction-tax/non-residential-property | 2026-10-30 |
| SSI 2024/367 art. 2 (ADS 8%) | https://www.legislation.gov.uk/ssi/2024/367/article/2/made | 2026-10-30 |
| LBTT (Scotland) Act 2013 s.29 | https://www.legislation.gov.uk/asp/2013/11/section/29 | 2026-10-30 |
| Welsh Government, LTT rates and bands | https://www.gov.wales/land-transaction-tax-rates-and-bands | 2026-10-30 |
| WSI 2024/1311 (LTT higher rates) | https://www.legislation.gov.uk/wsi/2024/1311/contents/made | 2026-10-30 |
| LTT and Anti-avoidance of Devolved Taxes (Wales) Act 2017 s.44 | https://www.legislation.gov.uk/anaw/2017/1/section/44 | 2026-10-30 |
| ITTOIA 2005 s.272A (finance cost restriction) | https://www.legislation.gov.uk/ukpga/2005/5/section/272A | 2026-10-30 |
| ITTOIA 2005 s.274AA (tax reduction) | https://www.legislation.gov.uk/ukpga/2005/5/section/274AA | 2026-10-30 |
| Finance Act 2026 s.2 (2026/27 rates) | https://www.legislation.gov.uk/ukpga/2026/11/section/2 | 2026-10-30 |
| Finance Act 2026 s.7 (2027/28 property rates) | https://www.legislation.gov.uk/ukpga/2026/11/section/7 | 2026-10-30 |
| GOV.UK, Tax-free allowances on property and trading income | https://www.gov.uk/guidance/tax-free-allowances-on-property-and-trading-income | 2026-10-30 |
| TCGA 1992 s.1H (CGT rates) | https://www.legislation.gov.uk/ukpga/1992/12/section/1H | 2026-10-30 |
| GOV.UK, Capital Gains Tax rates | https://www.gov.uk/capital-gains-tax/rates | 2026-10-30 |
| Finance Act 2019 Sch 2 para 3 (60-day return) | https://www.legislation.gov.uk/ukpga/2019/1/schedule/2/paragraph/3 | 2026-10-30 |
| GOV.UK, Report and pay CGT on UK property | https://www.gov.uk/report-and-pay-your-capital-gains-tax/if-you-sold-a-property-in-the-uk-on-or-after-6-april-2020 | 2026-10-30 |
| Finance Act 2009 Sch 55 (late return penalties) | https://www.legislation.gov.uk/ukpga/2009/10/schedule/55 | 2026-10-30 |

Not yet confirmed: the day SDLT late-payment interest starts (FA 2003 s.87(1) says 30 days after the relevant date, while HMRC's penalties page says the day after the 14-day deadline, so the skill says only that interest is charged); HMRC's late payment interest rate in force on 30 October 2026; whether Wales has any first-time buyer relief, and how Wales now treats multiple dwellings (WSI 2025/119 modifies its relief; not read); LBTT and LTT penalties and interest.

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
