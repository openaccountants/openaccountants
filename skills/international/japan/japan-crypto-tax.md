---
name: japan-crypto-tax
description: Use this skill whenever asked about Japan cryptocurrency or digital asset taxation. Trigger on phrases like "crypto tax Japan", "Bitcoin Japan tax", "暗号資産 税金", "仮想通貨 税金", "cryptocurrency Japan", "crypto income Japan", "miscellaneous income crypto", "雑所得", "NTA crypto", "staking tax Japan", "mining tax Japan", "NFT tax Japan", "DeFi tax Japan", "確定申告 crypto", "kakutei shinkoku crypto", "bitFlyer tax", "Coincheck tax", "crypto-to-crypto Japan", "総平均法", "移動平均法", or any question about the income tax, reporting, or cost basis treatment of cryptocurrency, tokens, or digital assets for Japan tax residents. Covers NTA Crypto FAQ guidance, miscellaneous income classification, aggregate taxation, cost basis methods (total average / moving average), the ¥200,000 filing threshold, and Kakutei Shinkoku reporting. ALWAYS read this skill before touching any Japan crypto work.
version: 1.0
jurisdiction: JP
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - jp-income-tax
category: crypto
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Japan Crypto Tax

## Japan Crypto / Digital Assets Tax Skill v1.0

## Section 1 — Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Japan (日本) |
| Tax | Income Tax (所得税) — crypto classified as miscellaneous income (雑所得) |
| Currency | JPY (Japanese Yen) — all values must be converted to JPY at the transaction date |
| Tax year | Calendar year (1 January – 31 December) |
| Primary authority | National Tax Agency (NTA / 国税庁) FAQ on Crypto Assets (暗号資産に関する税務上の取扱いについて(FAQ)); Income Tax Act (所得税法); NTA Individual Return Notice No. 1600 |
| Tax authority | National Tax Agency (国税庁 / NTA) |
| Filing portal | e-Tax (国税電子申告・納税システム) or paper filing at tax office |
| Maximum combined rate | 55% (45% national income tax + 10% local inhabitant tax) |
| Reconstruction surtax | 2.1% on national income tax (through 2037) |
| De minimis filing threshold | ¥200,000 — salary earners with crypto miscellaneous income below this do not need to file a final return (but local inhabitant tax return is still required) |
| Cost basis method | Total average method (総平均法, default for individuals) or moving average method (移動平均法) — must notify NTA of choice |
| Reporting | Kakutei Shinkoku (確定申告) — final tax return |
| Filing deadline | 16 February – 15 March of the following year (for CY 2025: 16 Feb – 15 Mar 2026) |
| Loss carry-forward | NOT PERMITTED for miscellaneous income |
| Validated by | Pending — requires sign-off by a Japanese licensed tax accountant (税理士) |
| Skill version | 1.0 |

### Key Principle

Crypto in Japan is classified as **miscellaneous income (雑所得 / zatsu shotoku)** under aggregate taxation (総合課税 / sōgō kazei). It is **NOT** classified as capital gains (譲渡所得), which means:
- Progressive income tax rates apply (up to 45% + 10% local = 55%)
- Crypto does NOT benefit from the separate ~20% taxation (分離課税) that applies to stock/securities trading
- Losses cannot be carried forward

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown cost basis | Zero (maximises gain) — STOP if material |
| Unknown cost basis method | Total average method (総平均法) — the statutory default for individuals |
| Unknown whether business or miscellaneous income | Miscellaneous income (雑所得) — this is the NTA's default classification |
| Unknown FMV at receipt | Use Japanese exchange price (bitFlyer, Coincheck) at time of transaction |
| Multiple income sources besides salary | Aggregate all miscellaneous income; file if total > ¥200,000 |

### Income Classification for Crypto

**Income Classification for Crypto**

| Classification | When it applies | Tax Treatment |
| --- | --- | --- |
| Miscellaneous income (雑所得) | Default for individual crypto trading, staking, mining, DeFi | Aggregate taxation at progressive rates |
| Business income (事業所得) | Only if crypto activity constitutes a "business" (organized, continuous, substantial) | Aggregate taxation; blue return deduction possible; losses offset other income |
| Employment income (給与所得) | Salary paid in crypto | Subject to withholding; employer obligations |

- **NTA position (FAQ 2-2)** — Crypto gains are principally classified as miscellaneous income (other) unless the activity clearly constitutes a business under established criteria.  _(NTA FAQ 2-2)_

### Business vs Miscellaneous Income — NTA Criteria

**Business vs Miscellaneous Income — NTA Criteria**

| Factor | Miscellaneous Income | Business Income |
| --- | --- | --- |
| Scale of activity | Personal, occasional | Organised, substantial |
| Continuity | Intermittent | Continuous, systematic |
| Infrastructure | Personal devices | Dedicated office, equipment |
| Livelihood dependency | Side income | Primary source of income |
| Number of transactions | Moderate | Very high volume |

- **Conservative default** — Unless the taxpayer can clearly demonstrate business-level activity, classify as miscellaneous income.

### National Income Tax Rates (2025)

**National Income Tax Rates (2025)**  _(Income Tax Act (所得税法) Art. 89; NTA 2025 Individual Income Tax Guide.)_

| Taxable Income | Rate | Deduction Amount |
| --- | --- | --- |
| ¥1 – ¥1,950,000 | 5% | ¥0 |
| ¥1,950,001 – ¥3,300,000 | 10% | ¥97,500 |
| ¥3,300,001 – ¥6,950,000 | 20% | ¥427,500 |
| ¥6,950,001 – ¥9,000,000 | 23% | ¥636,000 |
| ¥9,000,001 – ¥18,000,000 | 33% | ¥1,536,000 |
| ¥18,000,001 – ¥40,000,000 | 40% | ¥2,796,000 |
| Over ¥40,000,000 | 45% | ¥4,796,000 |

### Combined Rates (National + Local Inhabitant Tax)

**Combined Rates (National + Local Inhabitant Tax)**

| Taxable Income | National Rate | Local Rate | Combined |
| --- | --- | --- | --- |
| Up to ¥1,950,000 | 5% | 10% | 15% |
| ¥1,950,001 – ¥3,300,000 | 10% | 10% | 20% |
| ¥3,300,001 – ¥6,950,000 | 20% | 10% | 30% |
| ¥6,950,001 – ¥9,000,000 | 23% | 10% | 33% |
| ¥9,000,001 – ¥18,000,000 | 33% | 10% | 43% |
| ¥18,000,001 – ¥40,000,000 | 40% | 10% | 50% |
| Over ¥40,000,000 | 45% | 10% | 55% |

- **Reconstruction surtax (復興特別所得税)** — 2.1% of national income tax, applicable through 2037. This increases the effective national rates slightly (e.g., 45% becomes 45% × 1.021 = 45.945%).

### Basic Deduction (基礎控除)

**Basic Deduction (基礎控除)**

| Taxpayer's Total Income | Basic Deduction |
| --- | --- |
| Up to ¥24,000,000 | ¥480,000 |
| ¥24,000,001 – ¥24,500,000 | ¥320,000 |
| ¥24,500,001 – ¥25,000,000 | ¥160,000 |
| Over ¥25,000,000 | ¥0 |

### Permitted Methods (NTA FAQ 2-4, 2-5)

**Permitted Methods (NTA FAQ 2-4, 2-5)**  _(NTA FAQ 2-4, 2-5)_

| Method | Japanese Name | Description | Default? |
| --- | --- | --- | --- |
| Total average method | 総平均法 (sō heikin hō) | (Opening balance value + total year acquisitions) ÷ (opening quantity + total year acquisitions quantity) = unit cost for the year | YES — default for individuals |
| Moving average method | 移動平均法 (idō heikin hō) | Recalculate average unit cost each time tokens are acquired; use year-end average | Must notify NTA |

- **FIFO not available** — FIFO is NOT available for individuals in Japan (unlike many other jurisdictions).  _(NTA FAQ 2-4, 2-5)_

### Notification Requirement

- To use moving average method, the taxpayer must file a notification (届出書) with the tax office
- The notification must be filed by the filing deadline of the first return that includes crypto income
- Once elected, the method applies to all tokens of the same type
- Changing method requires another notification and approval

### Total Average Method — Formula

- **Total Average Method formula** — Year-end unit cost = (Opening balance value + Sum of all acquisition costs during the year) ÷ (Opening quantity + Total quantity acquired during the year) Transfer cost (譲渡原価) = Units sold during the year × Year-end unit cost  _(NTA FAQ 2-4, 2-5)_

### Moving Average Method — Formula

- **Moving Average Method formula** — At each acquisition: New average unit cost = (Existing holdings value + New acquisition cost) ÷ (Existing quantity + New quantity acquired) Year-end unit cost = Most recent average unit cost as of 31 December Transfer cost = Units sold during the year × Year-end unit cost  _(NTA FAQ 2-4, 2-5)_

### What is included in acquisition cost

- Purchase price in JPY
- Exchange commissions and fees
- Transfer fees directly related to acquisition

Source: NTA FAQ 2-3 (暗号資産の必要経費).

### Deductible Expenses (必要経費)

**Deductible Expenses (必要経費)**

| Expense | Deductible? |
| --- | --- |
| Exchange trading fees on sale | Yes |
| Internet/smartphone costs (proportional) | Yes, if directly related to crypto activity |
| Computer/hardware (if > ¥100,000) | Depreciation over useful life |
| Books, research materials | Yes, if directly related |
| Tax software subscription | Yes |
| General living expenses | No |

### 5.1 Mining

**5.1 Mining**

| Aspect | Treatment |
| --- | --- |
| Receipt of mined tokens | Miscellaneous income at FMV (JPY) when mined |
| Cost basis of mined tokens | FMV at receipt (becomes acquisition cost) |
| Deductible expenses | Electricity, hardware depreciation, cooling, rent (proportional) |
| Subsequent sale | Gain/loss calculated under total/moving average from FMV cost basis |

### 5.2 Staking

**5.2 Staking**

| Aspect | Treatment |
| --- | --- |
| Staking rewards received | Miscellaneous income at FMV when received |
| Cost basis of reward tokens | FMV at receipt date |
| Subsequent sale | Gain computed under normal cost basis rules |

### 5.3 Airdrops

**5.3 Airdrops**

| Scenario | Treatment |
| --- | --- |
| Airdrop with FMV at receipt | Miscellaneous income at FMV |
| Airdrop with zero value at receipt | No income on receipt; cost basis = ¥0; full gain on disposal |
| Airdrop requiring action | Income at FMV when claimed |

### 5.4 DeFi Yield / Lending

**5.4 DeFi Yield / Lending**

| Activity | Treatment |
| --- | --- |
| Interest/yield from lending protocols | Miscellaneous income at FMV when received |
| Liquidity provision (deposit tokens) | May constitute a disposal — exchange of tokens for LP tokens at FMV |
| LP withdrawal | Disposal of LP tokens; gain/loss computed |
| Yield farming rewards | Miscellaneous income at FMV when received |

### 5.5 Hard Forks

**5.5 Hard Forks**

| Scenario | Treatment |
| --- | --- |
| New tokens from fork | Cost basis = ¥0 (if no acquisition cost); NTA FAQ indicates no income at time of fork if market value is not established |
| Sale of forked tokens | Full proceeds treated as income |

### 5.6 Crypto-to-Crypto Swaps — CRITICAL

**Every crypto-to-crypto swap is a taxable event in Japan.** This is one of the most impactful rules.

**Crypto-to-Crypto Swaps table**  _(NTA FAQ 1-2 (暗号資産で暗号資産を購入した場合))_

| Event | Treatment |
| --- | --- |
| Swap BTC for ETH | Disposal of BTC at FMV of ETH received; gain = FMV of ETH – cost basis of BTC disposed |
| Swap ETH for stablecoin | Same — disposal of ETH |
| Any token exchange | Both sides are taxable events |

## Section 6 — NFT Treatment

**NFT Treatment**

| Event | Treatment |
| --- | --- |
| Purchase of NFT with crypto | Disposal of crypto at FMV; acquisition of NFT at FMV |
| Purchase of NFT with fiat | Acquisition — record cost |
| Sale of NFT | Miscellaneous income (gain = proceeds – cost basis) |
| Creation and primary sale (artist) | Business income or miscellaneous income depending on scale |
| Royalty on secondary sale | Miscellaneous income |
| NFT-for-NFT swap | Disposal of both NFTs at FMV |
| NFT becomes worthless | Loss — cannot carry forward (miscellaneous income limitation) |

### 7.1 Kakutei Shinkoku (確定申告 — Final Tax Return)

**Kakutei Shinkoku table**

| Element | Detail |
| --- | --- |
| Form | Kakutei Shinkoku-sho (確定申告書) — B form |
| Crypto income section | 雑所得（その他） — Miscellaneous income (Other) |
| Computation sheet | NTA Crypto Calculation Sheet (暗号資産の計算書) — total average version available on NTA website |
| Filing method | e-Tax online or paper at tax office |
| Filing period | 16 February – 15 March of the following year |

### 7.2 The ¥200,000 Threshold

**¥200,000 Threshold table**

| Taxpayer Type | Filing Required? |
| --- | --- |
| Salary earner (年末調整 done by employer) with misc. income ≤ ¥200,000 | NO national income tax return required |
| Salary earner with misc. income > ¥200,000 | YES — must file Kakutei Shinkoku |
| Self-employed / business owner | Always required if crypto income exists |
| Salary > ¥20,000,000 | Always required regardless |

- **Critical note** — Even if the ¥200,000 threshold exempts you from national filing, you must still file a local inhabitant tax return (住民税の申告) with your municipality. The ¥200,000 exemption applies ONLY to national income tax.

### 7.3 NTA Crypto Calculation Tool

The NTA provides a downloadable Excel spreadsheet (暗号資産の計算書（総平均法用）) that automates the total average method calculation:
- Available at: nta.go.jp (Publication → Pamphlets → Individual → Crypto)
- Input: transaction history from each exchange
- Output: total income from crypto for the year
- Japanese exchanges (bitFlyer, Coincheck, GMO Coin) provide annual transaction reports (年間取引報告書) that can be directly input

### 7.4 Key Deadlines

**Key Deadlines table**

| Deadline | Date (CY 2025 income) |
| --- | --- |
| Tax year end | 31 December 2025 |
| Filing period opens | 16 February 2026 |
| Filing deadline | 15 March 2026 (16 March if 15th falls on weekend/holiday) |
| Payment deadline | 15 March 2026 (or extension via bank transfer — 振替納税 in late April) |
| Local inhabitant tax | Assessed and notified June 2026; paid in 4 installments |

### 7.5 Exchange Reporting

Japanese licensed crypto exchanges (暗号資産交換業者) registered with the Financial Services Agency (FSA / 金融庁) are required to:
- Submit annual transaction reports to the NTA
- Issue annual transaction summaries (年間取引報告書) to users
- Report suspicious transactions

### The miscellaneous income limitation

**Loss offset table**

| Rule | Detail | Authority |
| --- | --- | --- |
| Loss offset within miscellaneous income | Losses within "other miscellaneous income" (その他の雑所得) CAN offset gains within the same sub-category in the same year | Income Tax Act |
| Loss offset against other income categories | **NOT PERMITTED** — miscellaneous income losses cannot offset salary, business, or other income | Income Tax Act Art. 69 |
| Loss carry-forward | **NOT PERMITTED** for miscellaneous income | Income Tax Act Art. 70 |
| Loss carry-back | **NOT PERMITTED** | — |

### Important nuance

Unlike India's regime, Japan **does allow** offsetting losses within the same miscellaneous income (other) sub-category within the same year. So if you lose ¥1,000,000 on BTC and gain ¥1,500,000 on ETH, your net miscellaneous income is ¥500,000. But if your net miscellaneous income for the year is a loss, that loss **cannot** offset salary or other income, and **cannot** be carried forward.

### Business income exception

- **Business income exception** — If crypto activity is classified as business income (事業所得), losses CAN: offset other income in the same year (損益通算); be carried forward for 3 years (with blue return / 青色申告). This is why the business vs miscellaneous income classification matters, but NTA's default is miscellaneous income.

### 9.1 No Wash Sale Rule

- **No Wash Sale Rule** — Japan has no specific wash sale rule for crypto. You can sell to crystallise a loss within miscellaneous income and immediately rebuy. However, the limited utility of losses (no carry-forward, no cross-category offset) reduces the incentive.

### 9.2 Low-Value / Gratuitous Transfer Rule

**Low-Value / Gratuitous Transfer Rule table**

| Provision | Effect |
| --- | --- |
| Transfer at below market value | NTA may deem the transfer at FMV; difference may be treated as gift (贈与税) |
| Gift tax (贈与税) | Gift of crypto valued > ¥1,100,000 (after basic deduction) attracts gift tax at 10%–55% |
| Inheritance | Crypto included in estate at FMV; inheritance tax applies |

### 9.3 NTA Enforcement

- Japanese exchanges report all user transaction data to the NTA
- The NTA has a dedicated crypto audit team
- Non-filing or underreporting of crypto income carries penalties: 15%–20% additional tax (過少申告加算税) plus interest (延滞税)

### Example 1 — BTC Trading, Total Average Method

**Input:** Japanese tax resident, salary earner (salary ¥6,000,000). CY 2025 crypto activity:
- 1 January: Holds 0.5 BTC (opening balance), cost ¥2,000,000
- 15 March: Buys 1 BTC at ¥8,000,000
- 20 June: Buys 0.5 BTC at ¥9,000,000
- 10 October: Sells 1 BTC at ¥12,000,000
- Exchange fees: ¥30,000 (on sales)

**Computation (Total Average Method / 総平均法):**
```
Opening: 0.5 BTC, value ¥2,000,000
Acquired in year: 1.5 BTC, value ¥17,000,000 (¥8,000,000 + ¥9,000,000)

Total: 2 BTC, total cost ¥19,000,000
Year-end unit cost = ¥19,000,000 ÷ 2 = ¥9,500,000 per BTC

Transfer cost for 1 BTC sold = 1 × ¥9,500,000 = ¥9,500,000

Income calculation:
  Proceeds:         ¥12,000,000
  Transfer cost:    ¥9,500,000
  Exchange fees:    ¥30,000
  Net income:       ¥2,470,000

Remaining: 1 BTC, value ¥9,500,000 (carries to next year)

Tax:
  Salary: ¥6,000,000
  Crypto misc. income: ¥2,470,000
  Total income: ¥8,470,000
  (deductions applied, then progressive rates)
  Crypto pushes income into higher bracket.
  Exceeds ¥200,000 threshold → must file Kakutei Shinkoku.
```

### Example 2 — Crypto-to-Crypto Swap

**Input:** Japanese tax resident. Swaps 2 ETH (cost basis ¥600,000 total via total average) for 0.1 BTC when:
- FMV of 0.1 BTC = ¥1,000,000
- FMV of 2 ETH = ¥1,000,000

**Computation:**
```
Disposal of 2 ETH:
  Proceeds (FMV of BTC received):  ¥1,000,000
  Cost basis of 2 ETH:             ¥600,000
  Gain:                             ¥400,000

  This ¥400,000 is miscellaneous income.

Acquisition of 0.1 BTC:
  Cost basis = ¥1,000,000 (FMV at time of swap)
  Added to BTC total average pool.
```

### Example 3 — Mining Income with Expenses

**Input:** Japanese tax resident. Mined 0.05 BTC over CY 2025. FMV at various receipt dates totals ¥500,000. Electricity costs attributable to mining: ¥80,000. Hardware (¥300,000 PC, 30% crypto use, 4-year depreciation).

**Computation:**
```
Mining income (miscellaneous): ¥500,000

Deductible expenses:
  Electricity:                      ¥80,000
  Depreciation: ¥300,000 ÷ 4 × 30% = ¥22,500
  Total expenses:                   ¥102,500

Net mining miscellaneous income:    ¥397,500

Cost basis of mined BTC: ¥500,000 (FMV at receipt)
  For future disposal calculations.
```

## Self-Checks

- [ ] Is crypto income classified as miscellaneous income (雑所得) unless business criteria are clearly met?
- [ ] Has the correct cost basis method been applied (total average unless moving average notified)?
- [ ] Have ALL crypto-to-crypto swaps been identified as taxable events?
- [ ] Has the ¥200,000 threshold been checked for salary earners (and local tax filing noted even if below)?
- [ ] Are progressive national + 10% local inhabitant tax rates applied (not flat capital gains rates)?
- [ ] Is the reconstruction surtax (2.1%) applied on national income tax?
- [ ] Have mining/staking expenses been properly identified and prorated?
- [ ] Have losses within miscellaneous income been correctly netted within the same sub-category?
- [ ] Is the Kakutei Shinkoku filed by 15 March of the following year?
- [ ] Are all values converted to JPY at the transaction-date exchange rate?

## PROHIBITIONS

- NEVER classify crypto as capital gains (譲渡所得) — it is miscellaneous income (雑所得) for individuals
- NEVER apply the ~20% separate taxation rate for stocks — crypto is under aggregate taxation
- NEVER use FIFO for crypto cost basis — only total average (総平均法) or moving average (移動平均法)
- NEVER ignore crypto-to-crypto swaps — EVERY swap is a taxable event in Japan
- NEVER carry forward miscellaneous income losses to future years
- NEVER offset miscellaneous income losses against salary or other income categories
- NEVER assume the ¥200,000 threshold exempts from local inhabitant tax filing
- NEVER ignore the NTA notification requirement for moving average method election
- NEVER treat transfers between own wallets as disposals
- NEVER present crypto tax positions as definitive — always label as estimated and flag for professional review

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

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
