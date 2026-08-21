---
name: mexico-crypto-tax
description: Use this skill whenever asked about Mexico cryptocurrency or virtual asset taxation. Trigger on phrases like "crypto tax Mexico", "Bitcoin Mexico", "impuesto criptomonedas", "ISR crypto", "SAT crypto", "activos virtuales Mexico", "Bitso tax", "staking Mexico", "mining income Mexico", "NFT tax Mexico", "Ley Fintech crypto", "declaración anual crypto", "CFDI crypto", or any question about the income tax, ISR, or IVA treatment of cryptocurrency, tokens, or digital assets for Mexican tax residents or Mexico-source crypto income. Covers SAT treatment of virtual assets, ISR rates, cost basis, CARF reporting, and Ley Fintech classification. ALWAYS read this skill before touching any Mexico crypto work.
version: 1.0
jurisdiction: MX
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - mexico-income-tax
category: crypto
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Mexico Crypto Tax

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | United Mexican States (Estados Unidos Mexicanos) |
| Tax | Impuesto Sobre la Renta (ISR) on Virtual Assets |
| Currency | MXN (Mexican Peso) — all values must be in MXN at transaction date |
| Tax year | Calendar year (1 January -- 31 December) — "ejercicio fiscal" |
| Primary authority | Ley del Impuesto Sobre la Renta (LISR), Art. 126 (enajenación de bienes), Art. 142 (otros ingresos), Art. 152 (progressive rates) |
| Supporting legislation | Ley para Regular las Instituciones de Tecnología Financiera (Ley Fintech, 2018), Art. 30; Código Fiscal de la Federación (CFF), Art. 16-A; Circular 4/2019 Banco de México |
| Tax authority | Servicio de Administración Tributaria (SAT) |
| Filing portal | Portal SAT (sat.gob.mx) |
| Filing deadline | 30 April of the following year (Declaración Anual de Personas Físicas) |
| International reporting | CARF — Mexico adopted implementation effective 1 April 2026; exchanges report to SAT |
| Validated by | Pending — requires sign-off by a Mexican Contador Público (C.P.) or licensed tax professional |
| Skill version | 1.0 |

### Key Principles

- Mexico does NOT have a specific crypto tax law — crypto is taxed under general ISR rules
- Virtual assets are classified as "activos virtuales" (intangible movable property) under Ley Fintech Art. 30
- They are explicitly NOT legal tender, NOT foreign currency, and NOT denominated in any currency
- The SAT taxes realized gains; mere holding (HODL) does not trigger tax
- There is an annual exemption of approximately $60,000 MXN for non-habitual disposals of movable property

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown whether trading or occasional | Treat as habitual (actividad empresarial) — higher compliance burden |
| Unknown cost basis | STOP — cannot compute gain without documented acquisition cost |
| Unknown residency status | STOP — Mexican residents taxed on worldwide income; non-residents on Mexico-source only |
| Mining classification unclear | Treat as "otros ingresos" (Art. 142 LISR) unless clearly commercial-scale |
| CFDI required? | If in doubt, issue CFDI for business crypto transactions |
| RESICO eligibility unclear | Verify income does not exceed $3,500,000 MXN annually |

## Section 2 -- Classification Rules

### 2.1 Legal Classification

**Legal Classification**

| Term | Definition | Authority |
| --- | --- | --- |
| Activos virtuales | Digital representations of value that can be electronically transferred and used as means of payment, NOT legal tender | Ley Fintech Art. 30 |
| Bienes intangibles muebles | Intangible movable property — the SAT's fiscal classification for crypto | SAT criteria (oficios 2019–2025) |
| Enajenación de bienes | Disposal/alienation of property — the chapter under which crypto sales are taxed | LISR Art. 126 |

### 2.2 Taxable Events

**Taxable Events**

| Event | Tax Treatment | LISR Chapter |
| --- | --- | --- |
| Sale of crypto for MXN/fiat | Taxable — enajenación de bienes | Art. 126 (occasional) or Art. 100 (business) |
| Crypto-to-crypto exchange (swap) | Taxable — enajenación (disposal at FMV) | Art. 126 / Art. 100 |
| Payment for goods/services with crypto | Taxable — disposal at FMV in MXN on date of transaction | Art. 126 / Art. 100 |
| Mining rewards received | Taxable — income at FMV when received | Art. 142 (otros ingresos) or Art. 100 (business) |
| Staking rewards received | Taxable — income at FMV when received | Art. 142 (otros ingresos) |
| Crypto received as salary/payment | Taxable — employment or professional income at FMV | Art. 94 (salarios) or Art. 100 |
| Holding crypto (HODL) | NOT taxable — no enajenación has occurred | — |
| Transfer between own wallets | NOT taxable — no change in ownership | — |
| Receiving crypto as gift | Taxable to recipient if exceeds annual gift exemption | Art. 93(XXIII) LISR |

### 2.3 Occasional vs Business Activity

The SAT distinguishes between occasional disposals and habitual business activity:

**Occasional vs Business Activity**

| Factor | Occasional (Enajenación de bienes) | Business (Actividad empresarial) |
| --- | --- | --- |
| Frequency | Infrequent, sporadic sales | Regular, systematic trading |
| Intent | Not primary economic activity | Profit-seeking as primary activity |
| Tax treatment | Annual declaration; $60,000 MXN exemption may apply | Monthly provisional payments; full ISR + 16% IVA potential |
| Reporting | In Declaración Anual under "enajenación" | Monthly declarations + annual |
| Cost basis adjustment | INPC inflation adjustment allowed | Full deductions per business rules |

## Section 3 -- Rate Tables

### 3.1 ISR Progressive Rates — Personas Físicas (2025)

**ISR Progressive Rates — Personas Físicas (2025)**  _(LISR Art. 152; Resolución Miscelánea Fiscal 2025.)_

| Lower Limit (MXN) | Upper Limit (MXN) | Fixed Quota (MXN) | Marginal Rate |
| --- | --- | --- | --- |
| $0.01 | $8,952.49 | $0.00 | 1.92% |
| $8,952.50 | $75,984.55 | $171.88 | 6.40% |
| $75,984.56 | $133,536.07 | $4,461.94 | 10.88% |
| $133,536.08 | $155,229.80 | $10,723.55 | 16.00% |
| $155,229.81 | $185,852.57 | $14,194.54 | 17.92% |
| $185,852.58 | $374,837.88 | $19,682.13 | 21.36% |
| $374,837.89 | $590,795.99 | $60,049.40 | 23.52% |
| $590,796.00 | $1,127,926.84 | $110,842.74 | 30.00% |
| $1,127,926.85 | $1,503,902.46 | $271,981.99 | 32.00% |
| $1,503,902.47 | $4,511,707.37 | $392,294.17 | 34.00% |
| $4,511,707.38 | En adelante | $1,417,491.57 | 35.00% |

- **Combining crypto gains with other income** — Crypto gains are added to ALL other income for the year to determine the applicable bracket.  _(LISR Art. 152; Resolución Miscelánea Fiscal 2025.)_

### 3.2 Corporate ISR Rate

**Corporate ISR Rate**  _(LISR Art. 9.)_

| Entity Type | Rate |
| --- | --- |
| Personas morales (corporations) | 30% flat on net gain |

### 3.3 RESICO Rates (Régimen Simplificado de Confianza)

If the taxpayer qualifies for RESICO (total annual income ≤ $3,500,000 MXN):

**RESICO Rates (Régimen Simplificado de Confianza)**

| Annual Income (MXN) | Rate |
| --- | --- |
| Up to $300,000 | 1.00% |
| $300,001 – $600,000 | 1.10% |
| $600,001 – $1,000,000 | 1.50% |
| $1,000,001 – $2,500,000 | 2.00% |
| $2,500,001 – $3,500,000 | 2.50% |

**Warning:** RESICO applicability to crypto traders is uncertain. Conservative default: use the general progressive regime unless a tax professional confirms RESICO eligibility.

### 3.4 The 20% Alternative Rate

- **20% alternative rate on gross proceeds** — If a taxpayer cannot prove their cost basis for a crypto disposal, the SAT may apply a 20% rate on gross proceeds instead. This is not an elective option — it is a fallback when documentation is insufficient.  _(LISR Art. 126, third paragraph.)_

### 3.5 Annual Exemption

**Annual Exemption**

| Exemption | Amount | Condition |
| --- | --- | --- |
| Enajenación de bienes muebles | ~$60,000 MXN per year (3× UMA anualizada, approx. $124,000 MXN for 2025 per some sources) | Non-habitual disposals only; habitual traders do NOT qualify |

The exact threshold is tied to the UMA (Unidad de Medida y Actualización) and updated annually.

## Section 4 -- Cost Basis Methods

### 4.1 Accepted Methods

**Accepted Methods**

| Method | Status |
| --- | --- |
| Specific identification | Primary method — match each sale to a specific acquisition lot |
| FIFO (First In, First Out) | Accepted when specific identification impractical |
| INPC-adjusted cost | Cost basis may be adjusted for inflation using INPC (Índice Nacional de Precios al Consumidor) from acquisition month to disposal month |
| Average cost | Less common; may be accepted with documentation |
| LIFO | Not standard practice |

### 4.2 Cost Basis Components

**Cost Basis Components**

| Component | Included? |
| --- | --- |
| Purchase price in MXN (at exchange rate on acquisition date) | Yes |
| Exchange fees and commissions on acquisition | Yes |
| Network/gas fees on acquisition | Yes |
| Exchange fees and commissions on disposal | Yes — deductible from proceeds |
| INPC inflation adjustment | Yes — for enajenación de bienes calculation |

### 4.3 INPC Adjustment

- **INPC adjustment formula** — Adjusted cost = Original cost × (INPC disposal month / INPC acquisition month)  _(LISR Art. 124.)_

For occasional disposals under the enajenación de bienes chapter, the cost basis can be adjusted for inflation:

This can meaningfully reduce the taxable gain for long-held assets in a high-inflation environment.

### 4.4 Unverifiable Cost Basis

- **Unverifiable cost basis consequence** — If the taxpayer cannot document their acquisition cost, the SAT may apply a 20% tax on gross sale proceeds. This is punitive — it effectively assumes zero cost basis and then applies 20% to the full amount.

## Section 5 -- DeFi / Staking / Mining / Airdrop Treatment

### 5.1 Mining

**Mining**

| Aspect | Treatment |
| --- | --- |
| Occasional mining (hobby) | "Otros ingresos" (Art. 142 LISR) — taxable at progressive rates |
| Commercial mining operation | Actividad empresarial — ISR at progressive rates + 16% IVA on services |
| Valuation | FMV in MXN at date of receipt |
| Cost basis of mined coins | FMV at receipt (for future disposal) |
| Deductible expenses (commercial) | Electricity, equipment depreciation, internet, facility costs |
| CFDI requirement | Business miners must issue CFDI for self-billed income |

### 5.2 Staking

**Staking**

| Aspect | Treatment |
| --- | --- |
| Staking rewards | Taxable as "otros ingresos" at FMV when received |
| Cost basis of staking rewards | FMV at receipt date (for future disposal) |
| Staking-as-a-service | If providing service: actividad empresarial + IVA |
| Loss from slashing | Likely not deductible absent specific SAT guidance |

### 5.3 Airdrops

**Airdrops**

| Aspect | Treatment |
| --- | --- |
| Promotional airdrop | Taxable as "otros ingresos" at FMV when received |
| Fork-based distribution | Cost basis of ₩0; taxable on disposal |
| Airdrop in exchange for a service | Income at FMV — may be actividad empresarial |

### 5.4 DeFi

**DeFi**

| Activity | Treatment |
| --- | --- |
| DeFi lending interest | Income at FMV — "otros ingresos" or business income |
| Liquidity provision (AMM) | Depositing tokens to pool = potential disposal; LP tokens have new cost basis |
| Yield farming rewards | Income at FMV when received |
| Impermanent loss | Not specifically addressed by SAT; likely not deductible |
| Crypto-to-crypto swaps in DeFi | Each swap is a taxable enajenación |
| Wrapping (e.g., ETH → WETH) | Arguable — conservative: treat as disposal |

## Section 6 -- NFT Treatment

**NFT Treatment**

| Aspect | Treatment |
| --- | --- |
| Purchase of NFT | Acquisition cost for future disposal |
| Sale of NFT at profit | Taxable — enajenación de bienes at progressive ISR rates |
| Creation and sale (artist/creator) | Business income (actividad empresarial) — ISR + 16% IVA |
| NFT royalties | Income — "otros ingresos" or business income depending on regularity |
| NFT-to-NFT swap | Disposal of both — compute gain/loss on each |
| IVA on NFT sales | If business activity: 16% IVA applies to NFT sales (digital service) |
| CFDI for NFT sales | Required for business transactions |

## Section 7 -- Reporting Requirements

### 7.1 Individual Filing

**Individual Filing**

| Requirement | Detail |
| --- | --- |
| Return type | Declaración Anual de Personas Físicas |
| Filing deadline | 30 April of the following year |
| Filing portal | Portal SAT (sat.gob.mx) |
| Crypto section | No dedicated crypto form — report under "Enajenación de bienes" (occasional) or "Actividad empresarial" (business) |
| Payment deadline | 30 April (or installments if arranged) |

### 7.2 Monthly Provisional Payments

**Monthly Provisional Payments**

| Who | Obligation |
| --- | --- |
| Habitual traders (actividad empresarial) | Must make monthly ISR provisional payments (pagos provisionales) by the 17th of the following month |
| Occasional sellers (enajenación) | No monthly obligation — annual declaration only |

### 7.3 CFDI Requirements

**CFDI Requirements**

| Scenario | CFDI Required? |
| --- | --- |
| Business-to-business crypto transactions | Yes — must issue CFDI |
| Business receiving crypto as payment | Yes — CFDI for the underlying supply |
| Individual occasional sale | No CFDI required for personal transactions |
| Mining as business | Yes — self-billed CFDI for mining income |

### 7.4 CARF and Exchange Reporting

**CARF and Exchange Reporting**

| Requirement | Detail |
| --- | --- |
| CARF adoption | Mexico implemented CARF effective 1 April 2026 |
| Exchange obligations | Crypto intermediaries (exchanges, brokers, platforms) report user transaction data directly to SAT |
| What is reported | User identification, transaction amounts, gains/losses |
| Impact | SAT can cross-reference declared income against exchange reports |

### 7.5 Record-Keeping

**Record-Keeping**

| Requirement | Detail |
| --- | --- |
| Retention period | 5 years from filing deadline (CFF Art. 30) |
| Records to maintain | Full transaction logs, exchange CSVs, cost basis records, CFDI documentation, INPC adjustment workpapers |
| Format | Digital records acceptable; XML for CFDI |
| Burden of proof | On the taxpayer — SAT can audit and request all documentation |

## Section 8 -- Loss Offset and Carry-Forward

### 8.1 Loss Offset Rules

**Loss Offset Rules**

| Rule | Detail |
| --- | --- |
| Loss offset within same category | Losses from enajenación de bienes muebles can offset gains from enajenación de bienes muebles within the same year |
| Cross-category offset | Losses from crypto generally CANNOT offset employment income, interest, or other income categories |
| Actividad empresarial losses | Business losses can offset business income; carry-forward for up to 10 years |
| Enajenación losses | Limited offset — only against gains from same type of asset disposal |

### 8.2 Business Loss Carry-Forward

**Business Loss Carry-Forward**

| Rule | Detail |
| --- | --- |
| Available to | Taxpayers under actividad empresarial regime |
| Duration | Up to 10 years |
| Adjustment | Must adjust for inflation using INPC |
| Condition | Must be properly documented and declared in the year incurred |

### 8.3 Key Limitation

Occasional sellers (enajenación de bienes) have significantly more limited loss utilization than business traders. If crypto trading generates recurring losses, consult a tax professional about whether actividad empresarial classification is more appropriate.

## Section 9 -- Anti-Avoidance Rules

### 9.1 SAT Enforcement Powers

**SAT Enforcement Powers**

| Measure | Detail |
| --- | --- |
| Exchange data access | SAT receives transaction data from Mexican exchanges (Bitso, etc.) and through CARF from foreign platforms (from April 2026) |
| Bank account monitoring | SAT monitors bank deposits; large unexplained deposits trigger audits |
| Discrepancia fiscal | If spending exceeds declared income, SAT can assess tax on the difference |
| Informant reporting | Third-party reporting obligations exist |

### 9.2 Penalties

**Penalties**

| Violation | Penalty |
| --- | --- |
| Failure to file | 55%–75% surcharge on unpaid tax |
| Late filing | Inflation-adjusted surcharges (recargos) + fines |
| Underdeclared income | 55%–75% of unpaid tax + surcharges |
| Tax fraud (defraudación fiscal) | Criminal penalties — imprisonment and fines |
| Failure to issue CFDI | Fines per missing CFDI |

### 9.3 Transfer Pricing

- **Transfer pricing for related-party crypto transactions** — For related-party crypto transactions (e.g., between a taxpayer and a controlled entity), arm's length principles apply. The SAT can recharacterize transactions at fair market value.

### 9.4 Crypto as Payment for Invoiced Services

- **Crypto as payment for invoiced services obligations** — If crypto is used to pay for services that should be invoiced, both parties have obligations: the service provider must issue a CFDI in MXN at the transaction-date exchange rate, and the payer must recognize a disposal of the crypto at FMV.

## Section 10 -- Worked Examples

### Example 1 -- Occasional Sale, INPC Adjustment

**Input:** Mexican tax resident, salaried employee. Bought 0.5 BTC on Bitso in January 2024 for $250,000 MXN. Sold 0.5 BTC in November 2025 for $500,000 MXN. Exchange fees: $3,000 MXN total. INPC Jan 2024: 133.24; INPC Nov 2025: 142.50 (hypothetical). No other disposals in the year. Salary income: $600,000 MXN.

**Computation:**
```
Disposal proceeds:          $500,000
Less exchange fees:          -$3,000
Net proceeds:               $497,000

Cost basis:                 $250,000
INPC adjustment:            $250,000 × (142.50 / 133.24) = $267,380
Adjusted cost basis:        $267,380

Gain:                       $497,000 - $267,380 = $229,620

Exemption check:            Single disposal, non-habitual — $60,000 exemption does NOT apply
                            if total disposals exceed the threshold (verify UMA for year).
                            Conservative: treat as fully taxable.

Combined income:            $600,000 salary + $229,620 crypto = $829,620 total

ISR on $829,620:
  Art. 152 tariff:          $110,842.74 + ($829,620 - $590,796) × 30%
                          = $110,842.74 + $71,647.20
                          = $182,489.94

Less ISR already withheld on salary (employer PAYE), the crypto gain adds
approximately $68,886 in additional ISR ($229,620 × ~30% effective marginal rate).
```

Filed in Declaración Anual by 30 April 2026.

### Example 2 -- Habitual Trader with Monthly Provisionals

**Input:** Mexican tax resident. Trades crypto full-time on Bitso and Binance. Total 2025 trading income: $1,200,000 MXN in net gains. Operating expenses (internet, equipment): $80,000 MXN. Registered under actividad empresarial.

**Computation:**
```
Gross income:               $1,200,000
Deductible expenses:         -$80,000
Net taxable income:         $1,120,000

ISR on $1,120,000:
  Art. 152 tariff:          $110,842.74 + ($1,120,000 - $590,796) × 30%
                          = $110,842.74 + $158,761.20
                          = $269,603.94

Monthly provisionals:       ~$22,467/month (subject to adjustment based on actual monthly income)
Annual reconciliation:      File Declaración Anual, credit provisional payments against annual ISR
```

Monthly provisional payments due by the 17th of the following month.

### Example 3 -- Mining Income

**Input:** Mexican tax resident operates a small mining rig at home. Mined 0.02 BTC over 2025 with total FMV of $20,000 MXN at various receipt dates. Electricity cost: $8,000 MXN.

**Computation:**
```
Mining income (otros ingresos):   $20,000 (FMV at receipt dates)
Cost basis for mined BTC:         $20,000 (for future disposal calculation)

If classified as otros ingresos (occasional):
  Added to other income for progressive rate computation
  Deductions: limited under otros ingresos chapter

If classified as actividad empresarial:
  Electricity deduction:   $8,000
  Net income:              $12,000
  ISR: at progressive rates, added to other income
  IVA: 16% may apply on mining services
```

Conservative: declare as otros ingresos unless professional confirms business classification.

## Self-Checks

Before finalising any Mexico crypto tax computation, verify:

- [ ] Has the taxpayer confirmed Mexican tax residency?
- [ ] Are all transaction values converted to MXN at the transaction-date exchange rate?
- [ ] Is the taxpayer classified as occasional (enajenación) or habitual (actividad empresarial)?
- [ ] Has the INPC adjustment been applied for enajenación de bienes?
- [ ] Is the annual exemption for movable property applicable (non-habitual only)?
- [ ] Has the 20% gross proceeds fallback been avoided by documenting cost basis?
- [ ] For business traders: are monthly provisional payments being made?
- [ ] Have all crypto-to-crypto swaps been treated as disposals?
- [ ] CFDI requirements: are business transactions properly invoiced?
- [ ] Have loss offset rules been applied correctly (same category only)?
- [ ] CARF: does the taxpayer know exchanges now report to SAT?
- [ ] Flag for reviewer: confirm UMA-based exemption threshold for the relevant year

## PROHIBITIONS

- NEVER state that crypto is tax-free in Mexico — realized gains are taxable under ISR
- NEVER ignore crypto-to-crypto swaps — each is a taxable enajenación
- NEVER apply the 20% gross proceeds rate by choice — it is a punitive fallback for missing cost basis
- NEVER forget INPC adjustment for occasional disposals — it can meaningfully reduce tax
- NEVER mix enajenación and actividad empresarial rules — they have different compliance obligations
- NEVER ignore monthly provisional payment obligations for business traders
- NEVER assume RESICO eligibility without verification of income limits and regime requirements
- NEVER compute gains in USD or other currencies — SAT requires MXN
- NEVER treat wallet-to-wallet transfers as taxable disposals
- NEVER ignore CARF reporting — SAT receives exchange data from April 2026
- NEVER present crypto tax positions as definitive — always label as estimated and flag for professional review

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Mexican Contador Público, licensed tax advisor, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
