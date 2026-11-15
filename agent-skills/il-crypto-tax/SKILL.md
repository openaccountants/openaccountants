---
name: il-crypto-tax
description: "Use this skill when advising on Israeli cryptocurrency tax reporting and capital gains calculations. Trigger on phrases like \"crypto tax Israel\", \"bitcoin tax Israel\", \"מס קריפטו\", \"FIFO Israel\", \"Form 1325 crypto\", \"Form 1322\", \"capital gains crypto Israel\", \"staking tax Israel\", \"airdrop tax Israel\", \"DeFi tax Israel\", \"voluntary disclosure crypto Israel\", \"gilui mirtzon\", \"גילוי מרצון\", or any Israeli cryptocurrency tax query. ALWAYS read this skill before advising on Israeli crypto taxation."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/il-crypto-tax"
  jurisdiction: "IL"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Israel: cryptocurrency tax working papers

> **Based on work by [Skills IL](https://github.com/skills-il/tax-and-finance)**, licensed under MIT. Adapted for the OpenAccountants format.

> **General reference only.** Reconstruct transactions and prepare a computation for an Israeli CPA. Do not file a return from a wallet balance or a vendor-generated tax total.

## Scope

Israel, 2026: investment disposals, business/mining classification, barter, gain/loss records and filing handoff. Circular 5/2018 distinguishes assets from currency, capital activity from business and mining, and requires a documentary audit trail. It does not settle every DeFi/token arrangement. Annual forms described here are explicitly the **2025-2026 filing cycle**, pending tax-year 2026 forms.

| Quick reference | Rate or threshold and condition | Official source |
|---|---|---|
| Individual capital treatment | Use the s.91 rules and acquisition-period conditions in [il-income-tax-returns](il-income-tax-returns.md); a material-shareholder security uplift is not a blanket crypto uplift | ITO s.91(b), https://www.btl.gov.il/Laws1/00_0103_000000.pdf |
| Business/mining | Ordinary income classification; use the personal/company computation appropriate to the actual taxpayer | ITO ss.2, 121, 126; https://www.btl.gov.il/Laws1/00_0103_000000.pdf |
| General disposal report and advance | Within 30 days; listed-security exceptions do not automatically apply to decentralised payment assets | ITO s.91(d), https://www.btl.gov.il/Laws1/00_0103_000000.pdf |
| Loss carryforward | File the loss-year return; capital-gain and foreign-source ordering conditions apply | ITO s.92, https://www.btl.gov.il/Laws1/00_0103_000000.pdf |

## Ask the client first

Obtain tax residence and arrival/departure dates; every exchange, wallet and chain; complete buy/sell/swap and fee records; fiat bank flows; transfers between owned wallets; opening lots and prior returns; acquisition/gift/inheritance evidence; mining/staking/lending/airdrop/NFT/ICO/IEO contracts; foreign taxes; missing keys or insolvency claims; and other income for surtax. Record timestamps, NIS values and valuation evidence. Frequency, scale, expertise, financing, time and the manner of operation require a business-status review; do not default to investment when uncertain.

## The method, step by step

### Classification before arithmetic

Circular 5/2018 ss.2.3 and 3.1 treats a decentralised payment instrument as an asset under s.88 rather than currency. A disposal is assessed under Part E; business activity is ordinary income and mining is business income. Payment in crypto is barter, with NIS value used for both the disposal and acquired asset. Under s.3.1.5.1, where the acquired goods/asset have a quoted price, that price is used for the crypto disposal; otherwise establish the crypto fair value in NIS. Preserve bank/exchange evidence and the ownership trail. Company income-tax computation is owned by [il-corporate-tax](il-corporate-tax.md); self-employed operations and social-contribution screening are owned by [il-freelancer-ops](il-freelancer-ops.md). Its VAT section distinguishes non-business investors, financial trading activity, mining and ordinary businesses accepting crypto; seek specialist classification rather than applying the standard VAT rate mechanically. [Official circular](https://www.gov.il/BlobFolder/policy/income-tax-professional-inst-5-2018/he/Policy_ProfessionalInstIncomeTax_hor_acc%2015.2.18.pdf).

Stablecoin names (USDT, USDC, DAI) do not prove currency status or absence of gain. Examine the actual token rights and transaction. Crypto-to-crypto swaps and spending assets need a disposal analysis even without a fiat withdrawal. Transfers between the taxpayer's own wallets must be identified so that the same ownership movement is not counted as a sale. Preserve an audit trail for bridging/wrapping instead of assuming every protocol label has the same result.

### Reconstruct cost and NIS consideration

For each disposal identify the asset, acquisition and sale dates, consideration, allowable cost and transaction costs, and real/inflationary components under ITO ss.88-91. Keep valuation methodology and evidence for every fiat and crypto leg. Do not claim that a Bank of Israel representative rate is mandatory for every crypto valuation, or assert a weekend fallback without the applicable currency rule. Those old claims remain unresolved below.

The old FIFO workflow is retained as a **conditional working-paper method**, not a verified Israeli legal mandate: queue purchases chronologically; match each disposal to the oldest eligible lots; allocate actual fees; reduce partial lots and reconcile remaining holdings. Record the taxpayer's documented/approved method before using it. Circular 5/2018 does not prescribe FIFO, and a monthly reporting grouping does not choose a cost-basis method.

### Losses, gifts and inheritance

Apply s.92 only where a corresponding gain would have been taxable. Real gains are offset first, then each NIS 1 of remaining loss offsets NIS 3.5 of taxable inflationary amount; foreign-asset losses first offset foreign gains, and carryforward requires the loss-year return. Securities-only interest/dividend offsets cannot automatically be applied to crypto. Do not assume spouse losses can be pooled merely because a return is joint. The old “no wash-sale rule, December sale/January rebuy always valid” is not a safe conclusion: obtain a substantive commercial/anti-avoidance review ([ITO ss.88, 92](https://www.btl.gov.il/Laws1/00_0103_000000.pdf)).

The s.97(a)(5) exemption concerns a gift to a statutory relative, or to another individual where the assessing officer is satisfied of good faith, and requires that the recipient is not a foreign resident. A qualifying tax-exempt gift may carry the prior owner's cost/acquisition history under s.88, but s.97(a)(5) itself concerns the gift exemption and excludes a foreign-resident recipient. Inheritance basis is addressed separately by s.88; deaths after 31 March 1981 use the statutory continuity rule, while older deaths have different treatment. Do not apply a universal zero basis, market-value step-up or donor carryover to every gift/inheritance ([ITO ss.88, 97(a)](https://www.btl.gov.il/Laws1/00_0103_000000.pdf)).

Insolvency (including FTX/Celsius patterns), theft and lost keys require evidence that a legally recognizable loss has crystallized; a police report or bankruptcy order alone is not a universal statutory test, and a frozen balance is not automatically a realized capital loss. Preserve recovery rights and distributions for specialist review.

### Surtax: load the annual-return computation

Use both s.121B bases in [il-income-tax-returns](il-income-tax-returns.md), after determining business versus capital character. The additional charge is not imposed on a whole crypto gain just because total income exceeds the general threshold. The statute defines capital-source taxable income by excluding business/employment and other personal-exertion income. The worked cases below demonstrate both coincident and mixed bases; the example rates/threshold are those owned by the annual-return skill ([ITO s.121B](https://www.btl.gov.il/Laws1/00_0103_000000.pdf)).

### Reporting form and transaction detail

For the 2025-2026 filing cycle, the rights guide's virtual-currency section uses Form 1399י, transaction symbol 77/code 71, with separate computations for each transaction; it permits same-month grouping with a weighted acquisition date and an attached calculation sheet. This does not authorize an unexamined annual net number or replace the general 30-day statutory report/advance rule. Forms 1322/1325 are securities schedules, not a universal crypto return. The annual surtaxes under s.121B are expressly excluded from the s.91(d) advance provisions by s.121B(b); do not include them automatically in the general 30-day gain advance. Reconcile all advance payments to the annual return and retain the submission acknowledgment ([rights guide, virtual-currency section](https://www.gov.il/BlobFolder/generalpage/income-tax-guide-knowyourright/he/Guides_IncomeTax_da-2025.pdf); [ITO s.91(d)](https://www.btl.gov.il/Laws1/00_0103_000000.pdf)).

Retain per-disposal asset description, acquisition/sale dates, original cost, proceeds, fees, gain/loss and lot remainder. The 2025-2026 filing-cycle guide requires wallet addresses on online transmission, up to 2 addresses; confirm tax-year 2026 fields and submission specifications when published. A salaried person with disposals must have filing obligations screened; do not assume salary withholding settles capital activity. Tax-year 2026 annual filing dates and any approved representative extension require the current notice.

## Boundary and exception table

| Activity or boundary | Treatment of the working paper |
|---|---|
| Investment buy/hold/sale or swap | Capital analysis, subject to actual business-status and asset-rights review |
| Mining | Business classification; do not vary to capital merely because scale is small |
| Staking rewards, liquidity mining/yield farming | Classification and recognition timing unresolved; do not assign a passive rate by default |
| Airdrops, hard forks | No automatic receipt-income or zero-basis rule established here |
| NFT creator vs collector | Different rights/activity may matter; label alone does not set a rate |
| CeFi/DeFi lending interest | Check contract and income category; no blanket passive rate |
| Gift/inheritance | Apply the correct s.88 acquisition-history rule and gift conditions |
| Loss, frozen wallet or insolvent exchange | Preserve recovery evidence; recognize no loss solely from inaccessibility |
| Foreign jurisdiction or new immigrant | Coordinate foreign obligations and load the immigrant skill before assuming exemption |

## Worked cases

### Simple investment disposal

Retain the old 0.5 BTC bought in January 2025 for NIS 80,000 and sold in August 2025 for NIS 120,000. Assume the CPA has confirmed investment character, the full NIS 40,000 as real gain, applicability of the 25% cap and sufficient ordinary-rate position to use it, with no losses/credits/surtax or additional costs. Tax is NIS 10,000. Use the actual 2025 filing record and late-reporting analysis, not an invented 2026 disposal date.

```oa-check
name: Historical simple BTC capital computation
inputs:
  proceeds: 120000
  cost: 80000
steps:
  - real_gain: proceeds-cost
  - tax: real_gain*0.25
expected:
  real_gain: 40000
  tax: 10000
```

### Swap lot reconciliation, conditional on approved FIFO

Retain 2 ETH bought in March 2024 at NIS 5,000 and 3 ETH bought in June 2024 at NIS 7,000, then in October 2024 3 ETH exchanged for 0.5 BTC when each ETH is worth NIS 9,000. Under the **assumed approved FIFO method**, allocated cost is NIS 17,000, consideration/new BTC cost is NIS 27,000 and gain is NIS 10,000; 2 ETH with cost NIS 14,000 remain. At the assumed applicable 25% cap, tax is NIS 2,500. This tests the lot arithmetic, not a claim that FIFO is mandatory.

```oa-check
name: Conditional FIFO swap and remaining lots
inputs:
  first_units: 2
  first_unit_cost: 5000
  second_units: 3
  second_unit_cost: 7000
  sold_units: 3
  unit_value: 9000
steps:
  - cost: first_units*first_unit_cost+(sold_units-first_units)*second_unit_cost
  - proceeds: sold_units*unit_value
  - gain: proceeds-cost
  - remaining_cost: (first_units+second_units-sold_units)*second_unit_cost
  - tax: gain*0.25
expected:
  cost: 17000
  proceeds: 27000
  gain: 10000
  remaining_cost: 14000
  tax: 2500
```

### Surtax decision: all capital income versus mixed income

Assume total taxable income is NIS 800,000. If it is all capital-source, general surtax is NIS 2,353.20 and the separate capital charge is NIS 1,568.80, totaling NIS 3,922. If the same total is NIS 500,000 employment and NIS 300,000 capital-source, only the general NIS 2,353.20 arises: the capital base does not exceed the statutory threshold. Do not apply 5% to the whole gain in the mixed case.

```oa-check
name: Separate surtax bases all-capital versus mixed
inputs:
  total: 800000
  all_capital: 800000
  mixed_capital: 300000
steps:
  - general: max(total-721560,0)*0.03
  - all_extra: max(all_capital-721560,0)*0.02
  - all_total: general+all_extra
  - mixed_extra: max(mixed_capital-721560,0)*0.02
  - mixed_total: general+mixed_extra
expected:
  general: 2353.20
  all_extra: 1568.80
  all_total: 3922
  mixed_extra: 0
  mixed_total: 2353.20
```

The old staking case (10 ETH staked, 0.5 ETH reward at NIS 8,000/ETH, NIS 4,000 value at receipt) remains a valuation scenario. It does not establish recognition timing, a NIS 1,000 tax charge, future basis or that depositing/locking the original ETH was not a disposal; protocol terms and law must be resolved before a tax result is used.

## When to refuse or refer

Refer business/investment uncertainty, missing transactions, unsupported basis or valuation, DeFi multi-chain/bridging/wrapping, NFT/ICO/IEO terms, cross-border taxation, loss realization, gifts/inheritance and disclosure. Retain the old 100-trade and NIS 500,000-gain escalation cues as **internal workflow alerts**, not legal thresholds or safe harbours. An absence of those alerts does not make a case simple.

The old voluntary-disclosure Green/Regular Track table is not current eligibility advice: it claimed NIS 500,000 annual income/NIS 1,500,000 assets at 31 December 2024 and 31 August 2026 deadlines, identifying applications and criminal immunity. No complete current official procedure has been read to confirm these claims, and the stated deadline is already past as of this review. Obtain specialist advice before any contact or submission; no immunity is promised.

## Filing and payment

Prepare the disposal schedules and applicable annual return for the actual year, review all current form/portal requirements, reconcile advances and withholding, and retain the accepted filing/payment receipts. General capital-disposal deadline is in the quick reference. The old 2025-return paper/online deadlines could not be reopened; no tax-year 2026 deadline is inferred.

## Completion checklist

Reconcile opening and closing holdings plus every owned wallet; classify disposals/transfers/rewards; verify NIS valuation and cost method; separately assess income tax, VAT and social contributions where relevant; apply eligible losses and both surtax bases; match forms to asset type; trace tax advances; preserve unresolved positions for CPA review.

## Sources

| Source | URL | Read on |
|---|---|---|
| ITA Circular 5/2018; Read for ss.2.3, 3.1.1-3.1.5 asset/business/mining/barter distinction and ss.3.2-3.3 VAT categories/documentary audit trail | https://www.gov.il/BlobFolder/policy/income-tax-professional-inst-5-2018/he/Policy_ProfessionalInstIncomeTax_hor_acc%2015.2.18.pdf | 2026-11-14 |
| Consolidated Income Tax Ordinance; Read for s.88 original-cost/gift/inheritance definitions, ss.91(b),(d), 92, 97(a)(5), 121B capital-source definition | https://www.btl.gov.il/Laws1/00_0103_000000.pdf | 2026-11-14 |
| ITA rights guide, tax year 2025, 2025-2026 filing cycle; Read for virtual-currency Form 1399 transaction identification and monthly grouping/attached working paper, distinct securities schedules | https://www.gov.il/BlobFolder/generalpage/income-tax-guide-knowyourright/he/Guides_IncomeTax_da-2025.pdf | 2026-11-14 |

Not yet confirmed: FIFO as a mandatory/accepted legal cost method in the taxpayer's circumstances; mandatory Bank of Israel rates and weekend fallback; DeFi/staking/airdrop/NFT/hard-fork/lending recognition, valuation and basis; spouse-loss pooling and any loss-harvest safe harbour; precise loss-realization treatment for insolvency/theft/lost keys; applicable current voluntary-disclosure tracks, deadlines, identifying information and immunity. The old voluntary-disclosure table's NIS 500,000/NIS 1,500,000/31 August 2026 claims are not instructions. No 30% material-shareholder uplift is asserted for ordinary decentralised crypto merely by analogy to a company security. Inflationary/real gain splitting and historic acquisition periods need their full s.88/s.91 computation, not the old blanket post-1 January 1994 rule. Current tax-year 2026 annual forms/deadlines, the older 29 May/30 June 2026 dates, and the old OECD CARF “Israel collection from 1 January 2026” statement remain unconfirmed. The older Form 1322/1325 crypto shortcut is corrected to the official asset-reporting route above.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `il-crypto-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/il-crypto-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
