---
name: forex-controls
description: "Foreign exchange controls and cross-border money movement rules by country. Use when the user asks about: forex controls, foreign exchange limits, FEMA, LRS, SAFE, 外汇管制, capital controls, money transfer limits, remittance limits, CRS reporting, TCS India, IOF Brazil, sending money abroad, receiving money from overseas, forex restrictions China, India remittance limit, Brazil forex, Taiwan outward remittance, Korea forex reporting, Japan foreign exchange, ODI filing China, cross-border transfer, 境外汇款, 购汇额度, 地下钱庄, forex quota, capital movement restrictions, repatriation of profits, sending money home, or any question about moving money across international borders as a founder or freelancer."
version: 1.0
jurisdiction: INTL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Forex Controls

## Foreign Exchange Controls — Cross-Border Money Movement by Country

> **Based on work by [Artin (@ar-gen-tin)](https://github.com/ar-gen-tin/panrise)**, licensed under MIT. Adapted for the OpenAccountants format.

> **Disclaimer:** This skill provides general information about foreign exchange regulations. Forex rules change frequently and enforcement varies. Violating forex controls can result in severe penalties including account freezes, fines, and criminal charges. Consult a qualified advisor in the relevant jurisdiction before structuring cross-border transactions.

## Why Forex Controls Matter

Forex (外汇) controls determine whether a person or business can freely move money in and out of a country. For founders earning from global customers, forex restrictions are often the single most important factor in choosing where to incorporate.

**Key principle:** If your home country has strict forex controls, incorporate in a country WITHOUT controls (HK, SG, US, UAE). This enables unrestricted global payment receipt and selective remittance of only living expenses to the home country.

## Decision Matrix

**Decision Matrix**

| Nationality | Forex Impact | Annual Limit | Recommended Structure |
| --- | --- | --- | --- |
| Chinese (大陆) | **CRITICAL** | $50,000/year individual | HK Ltd → HK bank → Stripe HK |
| Indian | **HIGH** | $250,000/year (LRS) + 20% TCS >₹10 lakh | US LLC or SG Pte. Ltd. via LRS |
| Brazilian | **HIGH** | Complex bank requirements + IOF tax | US LLC + Mercury |
| Taiwanese | **MODERATE** | Declaration required >TWD 5,000,000 (~$150K USD) | HK Ltd or SG Pte. Ltd. |
| Korean | **MODERATE** | Report >$50,000 transactions | US LLC or SG Pte. Ltd. |
| Japanese | **LOW** | Report >¥30,000,000 (~$200K USD); no hard limits | Any structure works |
| US / EU / HK / SG / UAE | **NONE** | Free capital movement | Choose based on tax/customers |

## Country-by-Country Rules

### China — STRICT (外汇管制)

#### Individual Limits

- **China individual forex purchase quota (购汇额度)** — $50,000 USD/year USD (per person; applies to converting RMB to foreign currency)
- **Declaration of purpose required** — Each transaction requires declaring purpose (travel, education, living expenses — NOT investment)
- **Business use of individual quota prohibited** — Cannot legally use individual quota for business purposes

Banks may reject or flag repeated near-limit transfers

#### Business (Company) Forex

- **Legitimate trade payments** — Relatively smooth (with invoices + contracts)
- **Capital account transactions** — Requires SAFE (国家外汇管理局) approval
- **Profit repatriation from overseas subsidiary** — Allowed with documentation
- **ODI (境外直接投资) approval threshold** — >$5M USD USD (Requires NDRC + MOFCOM + SAFE approval; smaller amounts vary by province)

#### Practical Strategies for Chinese Founders

1. **Hong Kong company** — No forex controls in HK; receive USD/EUR freely
2. **Keep money offshore** — Only remit living expenses to mainland
3. **Personal remittance** — Within $50K/year limit via bank transfer
4. **Salary from HK company** — Subject to HK salaries tax if work performed in HK
5. **Service fees** — HK company pays mainland 个体户 for services (needs contract + 发票)

#### CRS Impact

- **China CRS participation** — China participates in CRS (Common Reporting Standard); foreign bank accounts are automatically reported to Chinese tax authorities
- **CRS applies to** — HK, Singapore, most EU countries, many offshore centers
- **US CRS exception** — Notable exception: US does not participate in CRS (but has FATCA)
- **2025 CRS enforcement expansion** — 2025 marks CRS enforcement expansion to mid-tier wealth brackets (<$1M assets)

#### Penalties

**China forex control penalties**

| Violation | Consequence |
| --- | --- |
| Using individual quota for business | Accounts frozen, blacklisted from forex purchase for 2 years |
| Undeclared overseas income | Back taxes + penalties (50–500% of unpaid amount) |
| Illegal forex channels (地下钱庄) | Criminal offense — 5–10 years imprisonment for amounts >RMB 1,000,000 |
| Structuring transfers (蚂蚁搬家) | 30% fine on violation amount; 2-year forex purchase ban |

#### Mainland Bank Inbound Wire Risk Controls

Inbound wires to mainland bank accounts may trigger compliance review:

**Inbound wire risk triggers**

| Trigger | Detail |
| --- | --- |
| Single transfer >$5,000 USD (frequent) | Human review likely |
| Single transfer >$50,000 USD | Mandatory human review |
| Multiple rapid transfers | Flagged as abnormal pattern |
| Mismatched declaration category | Automatic flag; may result in return of funds |

**Declaration categories for inbound wires:**

**Declaration categories for inbound wires**

| Payment Nature | Declaration Category | Required Documents |
| --- | --- | --- |
| Salary from HK company | 职工报酬 | Employment contract + payslip |
| Dividends from HK company | 利润汇回 | Shareholder resolution + articles |
| Service fees (个体户) | 服务贸易收入 | Service contract + VAT invoice |
| Personal living expenses | 经常转移 | Proof of family relationship |

### India — STRICT (FEMA / RBI)

#### Individual Limits (LRS — Liberalised Remittance Scheme)

- **LRS annual limit** — $250,000 USD/year USD (per person for permissible capital and current account transactions)
- **LRS coverage** — Covers: investment abroad, gifts, maintenance, travel, education
- **LRS can fund overseas company** — Can be used to fund an overseas company (investment under LRS)
- **LRS documentation requirements** — Requires: PAN card, A2 form through authorized dealer bank

#### Tax Collected at Source (TCS)

- **TCS on remittances** — 20% percent (on remittances >₹10 lakh/year (effective April 2025; was ₹7 lakh))
- **TCS refundability** — TCS is refundable against income tax liability — it is not a final tax
- **Budget 2026 TCS reduction** — 2% percent (Budget 2026 reduces education/medical TCS to 2%)

#### Business Forex

- **Current account trade payments** — Generally free with documentation
- **Capital account (ODI)** — RBI approval needed; automatic route available for most cases
- **Round-tripping prohibition** — Sending money abroad and bringing it back is strictly monitored

#### Practical Strategies for Indian Founders

1. **Wyoming LLC + Mercury** — Fund via LRS ($250K limit usually sufficient for solo operations)
2. **Singapore Pte. Ltd.** — Popular for Asia-focused Indian founders (strong DTAA with India)
3. **Keep offshore revenue offshore** — Repatriate only what is needed
4. **Separate Indian entity** for domestic clients (Indian subsidiary for domestic revenue)

#### Indian Tax on Foreign Income

- **Worldwide income taxation** — India taxes worldwide income for residents
- **Declaration requirements** — Must declare: salary/fees from foreign company, dividends from owned foreign company, capital gains on foreign assets
- **DTAA relief** — India has DTAs with US, Singapore, UK, UAE — avoid double taxation
- **Form 67** — Required to claim foreign tax credit in India

### Brazil — STRICT

Central Bank controls all forex transactions

- **Individual daily limit without documentation** — up to $10,000 USD per day USD (without documentation)
- **Company forex transactions** — All transactions need exchange contract through authorized bank
- **IOF (Imposto sobre Operações Financeiras)** — 0.38–6.38% percent (on forex transactions)

Brazilian founders commonly use US LLC + Mercury to avoid domestic forex complexity

### Taiwan — MODERATE

#### Individual Limits

- **Taiwan individual outward remittance without declaration** — TWD 5,000,000 (~$150,000 USD)/year TWD (for individual outward remittance without declaration)
- **Declaration above threshold** — Above TWD 5,000,000: must file declaration with Central Bank
- **Nature of threshold** — This is a declaration threshold, NOT a hard cap (unlike China's strict quota)

#### Business Forex

- **Trade transactions** — Generally free for trade transactions with documentation
- **Investment abroad reporting** — >TWD 5,000,000 TWD (Investment abroad: report to Investment Commission (MOEA))
- **OBU (Offshore Banking Unit)** — Tax-exempt interest income in OBU accounts

#### Practical Strategy

- **Hong Kong company** — Cultural proximity, cheaper than Singapore
- **OBU account** — For offshore income separation
- **Singapore** — If avoiding CFC triggers (SG 17% tax > Taiwan's 14% CFC threshold)

#### CFC Rules (2023+)

- **CFC trigger and exemption** — Holding >50% of a low-tax company (<14% effective rate) triggers deemed distribution for Taiwan tax. Exemption: real substance OR overseas income <NT$7,000,000.

### South Korea — MODERATE

#### Individual Limits

- **Korea individual transaction threshold without documentation** — $50,000 USD per transaction USD (without documentation)
- **Annual cumulative reporting** — Annual cumulative >$50K: must report to designated foreign exchange bank
- **Investment abroad reporting** — >$1,000,000 USD (Investment abroad: report to Bank of Korea)

#### Business Forex

- **Trade payments** — Generally free with invoice/contract
- **ODI notification threshold** — >$10,000,000 USD (ODI: report to designated bank; amounts need Bank of Korea notification)

### Japan — LIGHT

#### Individual Limits

- **No individual remittance limits** — No individual remittance limits
- **Reporting threshold to Ministry of Finance** — >¥30,000,000 (~$200,000 USD) JPY (must report to Ministry of Finance (after the fact))
- **Sensitive sector restriction** — Foreign Exchange and Foreign Trade Act restricts investment in sensitive sectors only

#### Business Forex

- **Japan business forex policy** — Generally free; Japan has very liberal forex policies
- **Large transaction reporting** — Large transactions reported post-facto

### Hong Kong — NONE ✓

- **Zero forex controls**
- Free movement of capital in and out
- No limits on foreign currency holding or conversion
- HKD is pegged to USD (7.75–7.85)
- Primary reason HK is the #1 choice for Chinese and Taiwanese founders

### Singapore — NONE ✓

- **Zero forex controls**
- Free capital movement
- MAS (Monetary Authority of Singapore) does not restrict currency transactions
- No reporting requirements for most transfers

### United States — LIGHT (Reporting Only)

- **No limits on moving money in/out**
- Reporting requirements:

**US reporting requirements**

| Requirement | Threshold | Consequence of Non-Compliance |
| --- | --- | --- |
| FBAR (FinCEN 114) | Foreign accounts aggregate >$10,000 at any time during year | $10,000 penalty per unreported account per year |
| FATCA (Form 8938) | Foreign financial assets >$50,000–$200,000 (varies by filing status) | $10,000 penalty + additional $10,000 per 30 days of non-compliance |
| CTR | Banks auto-report cash transactions >$10,000 | Structuring to avoid is a federal crime |

### UAE / Dubai — NONE ✓

- **Zero forex controls**
- No limits on repatriation of capital or profits
- Free movement of funds in any currency
- Note: UAE introduced 5% personal income tax effective January 2026; forex controls remain zero

### EU (General) — LIGHT

- Free movement of capital within EU (Treaty of Lisbon)
- Cross-border transfers within EU: same as domestic (SEPA)
- Transfers >€10,000 in cash: must declare at customs
- No limits on electronic transfers
- Individual countries may have reporting requirements (e.g., France requires reporting of foreign accounts)

## China-Specific: Mainland Income Reporting for Offshore Earners

### Annual Filing Window (汇算清缴)

- **Annual filing deadline** — March 1 – June 30 of following year date range (e.g., 2025 income reported by June 30, 2026)
- **Filing path** — 个税APP → 综合所得年度汇算 → 其他收入 → 境外所得（附表三）

### Foreign Tax Credit Calculation

- **Credit limit formula** — Credit limit (per country) = China total tax × (income from that country / total worldwide income)
- **Credit application when paid ≤ limit** — If foreign tax paid ≤ credit limit → full credit; China collects the difference
- **Credit application when paid > limit** — If foreign tax paid > credit limit → excess carries forward for 5 tax years (no refund)

### Penalties for Non-Reporting

**Penalties for non-reporting of overseas income**

| Scenario | Consequence |
| --- | --- |
| Discovered by tax authority | Back taxes + late payment surcharge (0.05%/day) + fine (50–500% of tax owed) |
| Voluntary self-correction | Late payment surcharge applies; fine typically reduced (<50%) |
| Tax evasion >RMB 100,000 AND >10% of tax due | Criminal liability (Article 201, Criminal Law) |

## CRS Response Protocol

When receiving a CRS inquiry letter from Chinese tax authorities:

**CRS inquiry letter response protocol**

| Letter Type | Urgency | Action |
| --- | --- | --- |
| Compliance reminder (合规提示函) | Low | Self-audit, voluntary supplemental filing |
| Risk notice / interview summons (风险提示函/约谈通知) | Medium — respond within 30 days | Prepare HK company documents, bank statements, tax records |
| Formal audit notice (税务稽查通知书) | **High — engage tax attorney immediately** | Do not destroy any documents; attorney-led response |

## Official Sources & Further Reading

- **China SAFE (国家外汇管理局):** https://www.safe.gov.cn
- **India RBI — LRS FAQ:** https://www.rbi.org.in/Scripts/FAQView.aspx?Id=115
- **India FEMA:** https://www.rbi.org.in/scripts/Fema.aspx
- **Taiwan Central Bank:** https://www.cbc.gov.tw
- **US FBAR (FinCEN):** https://www.fincen.gov/report-foreign-bank-and-financial-accounts
- **Hong Kong Monetary Authority:** https://www.hkma.gov.hk

## Footer notes

*Data reflects 2024–2026 rules. Forex regulations are enforced with increasing rigor worldwide. Verify current limits and procedures with your bank and a qualified advisor before large cross-border transfers.*
*Original content: [Artin (@ar-gen-tin)](https://github.com/ar-gen-tin/panrise) — MIT License.*
*OpenAccountants — open-source accounting skills for AI — info@openaaccountants.com*

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
