---
name: tr-corporate-income-tax
description: "Turkish corporate income tax (kurumlar vergisi) for tax year 2026 under the Corporate Tax Law no. 5520 (KVK), for Turkish companies and foreign companies with Turkish income. Covers full and limited liability, the 25% rate and the 30% financial-sector rate, the export (5 points) and manufacturing (1 point in 2026, 12.5% from 2027) reductions, the 10% domestic minimum corporate tax from 2025 and what it lets you deduct, the Pillar Two 15% domestic and global top-up taxes for groups over EUR 750 million, the taxable base, participation exemptions, five-year losses, thin capitalisation, the suspension of inflation accounting to 2027, quarterly provisional tax, the annual return in the fourth month, withholding on payments to non-residents, penalties and interest. Trigger on: kurumlar vergisi, Turkish corporate tax, yurt içi asgari kurumlar vergisi, geçici vergi, iştirak kazancı istisnası, Pillar Two Türkiye. Out of scope: transfer pricing documentation, individuals (turkey-pit), VAT (turkey-vat), payroll (tr-payroll-social), company formation (tr-company-formation)."
version: 0.1
jurisdiction: TR
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Türkiye: corporate income tax (kurumlar vergisi) (2026) v0.1

Turkish corporate income tax is charged under the Kurumlar Vergisi Kanunu no. 5520 (KVK) and collected by the Revenue Administration (GİB). The tax period is the accounting period, normally the calendar year (art. 16). Figures below come from the consolidated KVK on mevzuat.gov.tr, which includes the 2026 amending laws 7577, 7578, 7582 and 7590, and from GİB's current table of filing and payment dates.

## Who this applies to

- **Taxable entities** (art. 1): capital companies (joint-stock, limited and partnerships limited by shares), co-operatives, public economic enterprises, economic enterprises of associations and foundations, and joint ventures.
- **Full liability** (art. 3(1)): an entity whose legal seat or business seat is in Türkiye is taxed on its worldwide income.
- **Limited liability** (art. 3(2)-(3)): an entity with neither its legal seat nor its business seat in Türkiye is taxed only on Turkish income, mainly business profits made through a Turkish workplace or permanent representative, and listed Turkish-source income.
- **Global minimum tax** (ek art. 1): group entities of multinational groups whose ultimate parent's consolidated revenue exceeded EUR 750 million in at least two of the four previous accounting periods are also subject to the domestic and global top-up taxes.
- **Out of this skill:** transfer pricing rules and documentation (KVK art. 13); CFC rules in detail (art. 7); free-zone, technology-zone and investment-incentive regimes; individuals and partnerships taxed as individuals (see [turkey-pit](turkey-pit.md)).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Corporate tax rate | 25% | 2026 | KVK art. 32(1), https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5520.pdf |
| Banks, financial leasing, factoring and financing companies, payment and e-money institutions, authorised FX dealers, asset management companies, capital market institutions, insurance, reinsurance and pension companies, and build-operate-transfer and public-private partnership project companies | 30% | 2026 | KVK art. 32(1) |
| Profits made only from exports | 5 points lower (20%) | 2026 | KVK art. 32(7) |
| Profits made only from manufacturing by companies with an industry registry certificate | 1 point lower (24%) in 2026 | 2026 | KVK art. 32(8) before Law 7582, archived text https://web.archive.org/web/20241006151859/https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5520.pdf |
| Manufacturing and agricultural production profits, from 2027 periods | 12.5% | 2027 | KVK art. 32(8) as amended by Law 7582 art. 8; in force for 2027 and later periods |
| Companies first listed on Borsa İstanbul with at least 20% floated | 2 points lower for five periods | 2026 | KVK art. 32(6) |
| Domestic minimum corporate tax | Tax may not be less than 10% of profit before deductions and exemptions | 2026 | KVK art. 32/C(1) |
| New companies, minimum tax | Not applied for the first three accounting periods | 2026 | KVK art. 32/C(5) |
| Provisional tax rate | The corporate tax rate of the current period | 2026 | KVK art. 32(2) |
| Global minimum tax rate (Pillar Two) | 15% | 2026 | KVK ek art. 6(1) |
| Pillar Two revenue threshold | EUR 750 million consolidated revenue in 2 of the 4 previous periods | 2026 | KVK ek art. 1(1) |
| Pillar Two transitional safe harbour, effective tax rate test | 17% for the 2026 period | 2026 | KVK provisional art. 17(1)(e)(2) |
| Loss carry-forward | 5 years | 2026 | KVK art. 9(1)(a) |
| Thin capitalisation | Shareholder and related-party debt above 3 times equity | 2026 | KVK art. 12(1) |
| Withholding on dividends paid to non-residents | 15% | 2026 | KVK art. 30(3); Presidential Decision 9286 art. 3, https://www.resmigazete.gov.tr/eskiler/2024/12/20241222-15.pdf |
| Foreign participation exemption, minimum holding | 10% for at least one year, foreign tax burden at least 15% | 2026 | KVK art. 5(1)(b) |
| Late-payment surcharge | 3.7% a month | 2026 | Law 6183 art. 51, https://www.mevzuat.gov.tr/MevzuatMetin/1.5.6183.pdf |

## The taxable base

**Starting point.** Corporate tax is charged on net corporate income for the period, computed under the GVK rules for business income (art. 6). In practice that is the commercial profit adjusted for non-deductible expenses, exemptions, deductions and losses.

**Not deductible** (art. 11, main items): interest on equity; interest, exchange losses and similar costs on thin capital; profit distributed in disguise through transfer pricing; reserves of any kind; corporate tax itself, fines, tax penalties, late-payment surcharges and late interest; 50% of advertising for alcohol and tobacco; and part of the financing costs of companies whose borrowings exceed their equity, at a share set by the President of up to 10% (art. 11(1)(a)-(ı)).

**Thin capitalisation** (art. 12). Debt from shareholders or persons related to them that exceeds three times equity at any time in the period is thin capital. Borrowings from a related bank or similar credit institution acting in its main business count at 50%. Interest and exchange losses on thin capital are not deductible (art. 11(1)(b)) and are treated as a distributed dividend (or, for a branch, a remittance to head office) on the last day of the period (art. 12).

**Exemptions.** Dividends from another fully liable Turkish company are exempt (art. 5(1)(a)). Dividends from a foreign joint-stock or limited company are exempt if the Turkish company holds at least 10% of its paid-in capital for at least a year, the subsidiary bears a total tax of at least 15% (at least the Turkish rate for finance, insurance and securities businesses), and the dividend is brought to Türkiye by the return deadline (art. 5(1)(b)).

**Losses** (art. 9). Tax losses from earlier years are deducted for up to five years, each year shown separately on the return. Losses taken over in a merger or full demerger are deductible only up to the equity taken over, and only if the last five years' returns were filed on time and the business carries on for at least five years. Foreign losses need an audited report from the foreign country.

**Inflation accounting.** Financial statements are not inflation-adjusted for the 2025, 2026 and 2027 accounting periods, including provisional tax periods, whatever the inflation test shows (VUK provisional art. 37, Law 7571). The President may extend this by up to three periods.

**Domestic minimum corporate tax** (art. 32/C). The tax computed under art. 32 and 32/A may not be less than 10% of profit before deductions and exemptions. That profit is the commercial balance-sheet profit plus non-deductible expenses (art. 32/C(6)). Only these may be taken off it: the exemptions in art. 5(1)(a), (ç), (i), (j) and (k), and those in (d) other than gains on owned property; the deductions in art. 10(1)(g), (h), (i) and (j); shipping-register and free-zone exemptions; technology development zone exemptions and R&D and design deductions; and, from 2026, the deduction under Law 7412 art. 6(1)(a). Tax given up through the IPO, export and manufacturing rate cuts, and investment contributions under incentive certificates issued before the article came in, is then deducted from the minimum tax (art. 32/C(3)). Loss carry-forwards are not on the list, so they do not reduce the minimum base. The rule also applies to provisional tax (art. 32/C(4)), and not for the first three periods of a new company (art. 32/C(5)).

**Global minimum tax** (ek art. 1 to 13). In-scope group entities in Türkiye compute a domestic top-up tax and, for parents, a global top-up tax so that the group's effective rate in each country reaches 15%. The under-taxed payments rule (UTPR) applies from 2025 periods (provisional art. 17(1)(d)). Until the end of the 2026 period, the top-up tax for a country is treated as nil if the country-by-country report shows revenue under EUR 10 million and pre-tax profit under EUR 1 million, or an effective rate of at least 17% (2026), or profit no higher than the substance-based carve-out (provisional art. 17(1)(e)).

## Deadlines and filing

- **Annual return.** KVK art. 14(3) says the return is filed from the 1st to the 25th of the fourth month after the period ends. GİB's current table says from the first to the last day of that month, 23:59. For a calendar year, that is April 2027 for 2026. The tax is paid by the end of the month the return is filed (art. 21; GİB table).
- **Provisional tax.** Paid quarterly at the corporate tax rate on cumulative quarterly profit, under the GVK rules (art. 32(2); GVK mükerrer art. 120). GİB's table gives the 17th of the second month after each quarter for filing and payment: 17 May, 17 August, 17 November and 17 February. The minimum tax applies to provisional periods too.
- **Domestic top-up tax return.** By the last day of the twelfth month after the period ends, paid in the same period (KVK ek art. 10; GİB table).
- **Global top-up tax return and GloBE information return.** By the last day of the fifteenth month after the period ends; for the 2024 period, the eighteenth month (KVK ek art. 8, provisional art. 17(1)(b); GİB table).
- **Leaving Türkiye.** Where the taxpayer leaves the country, the return is filed within the 15 days before it leaves (GİB table).

## Penalties and interest

- **Late return.** A first-degree irregularity: TRY 35,000 for capital companies in 2026 (VUK art. 352, table 1, Communiqué 588).
- **Tax loss.** One times the tax lost; three times with fake or misleading documents; halved for a late return filed before an audit; increased by 50% for unregistered business (VUK art. 344).
- **Provisional tax under-declared** by more than 10% is assessed with late interest and penalty, even after the provisional tax can no longer be offset (GVK mükerrer art. 120).
- **Late payment.** 3.7% a month, daily for part months (Law 6183 art. 51).

## Cross-border points

- **Withholding on non-residents** (art. 30). Payers withhold corporate tax on Turkish construction profits spread over more than one year, professional fees, rental income, investment income other than dividends, and listed digital marketplace payments. The law rate is 15%; the President sets the actual rates by type of payment. Royalties and payments for the sale of intangible rights are also withheld. Dividends paid to non-resident companies are withheld at 15% (Decision 9286). Payments to companies in countries the President lists as harmful tax regimes are withheld at 30%.
- **Branch remittances.** A non-resident's Turkish branch withholds 15% on profit after tax transferred to head office (art. 30(6)).
- **Foreign tax credit** (art. 33). Foreign corporate tax on foreign profits is credited up to the Turkish tax on those profits; unused credit can be carried for three periods. A Turkish company holding at least 25% of a foreign subsidiary can also credit the underlying foreign tax on dividends. Documents must be certified by the Turkish consulate.
- **Treaties.** A tax treaty can lower Turkish withholding; treaty rates are not covered here.

## Worked examples

### Example 1: Trading company, standard rate, 2026

A Turkish limited company has a commercial profit of TRY 10,000,000 for 2026 and TRY 500,000 of non-deductible expenses. It has no exemptions or losses. Its taxable base is TRY 10,500,000 and corporate tax at 25% is TRY 2,625,000. The minimum tax is 10% of TRY 10,500,000, TRY 1,050,000, so the normal tax applies. It paid TRY 2,000,000 of provisional tax during the year, so TRY 625,000 is due with the return in April 2027.

```oa-check
name: Limited company, base TRY 10.5 million at 25% (2026)
inputs:
  commercial_profit: 10000000
  non_deductible: 500000
  provisional_paid: 2000000
steps:
  - base: commercial_profit + non_deductible
  - normal_tax: base * 0.25
  - minimum_tax: (commercial_profit + non_deductible) * 0.10
  - tax: max(normal_tax, minimum_tax)
  - due: tax - provisional_paid
expected:
  normal_tax: 2625000
  minimum_tax: 1050000
  tax: 2625000
  due: 625000
```

### Example 2: Old losses, where the minimum tax bites

A company that has traded for many years has a 2026 commercial profit of TRY 20,000,000, which includes TRY 2,000,000 of exempt dividends from a Turkish subsidiary, plus TRY 1,000,000 of non-deductible expenses. It has TRY 15,000,000 of losses from the last five years. The normal base is TRY 21,000,000 less TRY 2,000,000 of exempt dividends and TRY 15,000,000 of losses: TRY 4,000,000, so TRY 1,000,000 of tax at 25%. For the minimum tax, the dividend exemption may be deducted (art. 5(1)(a) is on the list) but the losses may not: the minimum base is TRY 19,000,000 and the minimum tax is TRY 1,900,000. The company pays TRY 1,900,000.

```oa-check
name: Minimum corporate tax with loss carry-forward (2026)
inputs:
  commercial_profit: 20000000
  non_deductible: 1000000
  exempt_dividends: 2000000
  losses_brought_forward: 15000000
steps:
  - normal_base: commercial_profit + non_deductible - exempt_dividends - losses_brought_forward
  - normal_tax: normal_base * 0.25
  - minimum_base: commercial_profit + non_deductible - exempt_dividends
  - minimum_tax: minimum_base * 0.10
  - tax: max(normal_tax, minimum_tax)
expected:
  normal_tax: 1000000
  minimum_tax: 1900000
  tax: 1900000
```

## Ask the client first

1. What is the company's legal form, where are its legal seat and its management, and what is its accounting period?
2. When did it start trading (the minimum tax does not apply for the first three periods)?
3. Is it a bank, insurer, leasing, factoring or other company on the 30% list, or does it export or manufacture with an industry registry certificate?
4. What losses does it carry forward, from which years, and what exemptions or R&D deductions does it claim?
5. How much does it borrow from shareholders or related parties, against what equity?
6. Is it part of a group with consolidated revenue of EUR 750 million or more, and does it pay dividends, royalties or fees abroad?

## Sources

| Source | URL | Read on |
|---|---|---|
| Kurumlar Vergisi Kanunu no. 5520, consolidated (to Law 7590): arts. 1, 3, 5, 6, 9, 11, 12, 14, 16, 21, 30, 32, 32/C, 33, ek 1, ek 6, ek 8, ek 10, provisional art. 17, amendment table | https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5520.pdf | 2026-10-31 |
| KVK, archived consolidated text of 6 October 2024 (art. 32(8) before Law 7582) | https://web.archive.org/web/20241006151859/https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5520.pdf | 2026-10-31 |
| Vergi Usul Kanunu no. 213, consolidated: provisional art. 37 (inflation accounting), arts. 344, 352, table 1 | https://www.mevzuat.gov.tr/MevzuatMetin/1.5.213.pdf | 2026-10-31 |
| Gelir Vergisi Kanunu no. 193, mükerrer art. 120 (provisional tax) | https://www.mevzuat.gov.tr/MevzuatMetin/1.5.193.pdf | 2026-10-31 |
| Law 6183, art. 51 | https://www.mevzuat.gov.tr/MevzuatMetin/1.5.6183.pdf | 2026-10-31 |
| Presidential Decision 9286 (dividend withholding 10% to 15%), Official Gazette 22 December 2024 no. 32760 | https://www.resmigazete.gov.tr/eskiler/2024/12/20241222-15.pdf | 2026-10-31 |
| GİB, Beyanname verme ve ödeme süreleri | https://cdn.gib.gov.tr/api/gibportal-file/file/getFileResources?objectKey=arsiv%2Fyardim-kaynaklar%2Fyararli-bilgiler%2FBeyannameVermeveOdemeSureleri.pdf | 2026-10-31 |
| Yerel ve Küresel Asgari Tamamlayıcı Kurumlar Vergisi Uygulama Genel Tebliği, Official Gazette 26 December 2025 no. 33119 (scope and definitions only) | https://www.resmigazete.gov.tr/eskiler/2025/12/20251226-9.pdf | 2026-10-31 |

Not yet confirmed: withholding rates set by Decision 2009/14593 for interest, royalties, fees and rent paid to non-residents (the old version gave 10% interest and 20% royalties from a Big Four site); the list of harmful-tax countries under art. 30(7); withholding on payments to residents under art. 15 and Decision 2009/14594 (other than dividends); the share of financing costs disallowed under art. 11(1)(i) (set by Presidential decision, not read) and art. 11(1)(j); the reduced rate for investment incentive certificates (art. 32/A) and contribution rates; the property and share sale exemption (art. 5(1)(e)); the art. 10 deductions (R&D, venture capital, cash capital increase); the CFC rule (art. 7) in detail; transfer pricing (art. 13), a separate domain; Pillar Two computation detail from the 26 December 2025 communiqué; whether the 30% rate list changed for 2026 beyond Law 7524; the Law 7412 deduction referred to in art. 32/C(2)(d).
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
