---
name: pt-social-contributions
description: Use this skill whenever asked about Portuguese self-employed social contributions (contribuições para a Segurança Social). Trigger on phrases like "Segurança Social trabalhador independente", "Portuguese social contributions", "declaração trimestral SS", "contribuições independente Portugal", or any question about social contribution obligations for a self-employed client in Portugal. Covers the 21.4% rate on 70% of relevant income, quarterly declaration, and first-year exemption. ALWAYS read this skill before touching any Portugal social contributions work.
version: 2.0
jurisdiction: PT
tax_year: 2026
last_updated: 2026-10-23
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# PT Social Contributions

## Portugal Social Contributions -- Self-Employed Skill v2.0

## Rates and thresholds

Source-cited draft: not reviewed by an accountant.

### Segurança Social

- **Trabalhador independente** — 21,4%  _(Código Contributivo Art. 163)_
- **Empresário em nome individual** — 25,2%  _(Código Contributivo)_
- **Rendimento relevante — serviços** — 70% do bruto  _(Código Contributivo Art. 162)_
- **Rendimento relevante — bens** — 20% do bruto  _(Código Contributivo Art. 162)_
- **Base mínima mensal (IAS)** — €20,00 por mês (valor mínimo a pagar quando não há rendimentos ou as contribuições apuradas são inferiores a 20,00€; não existe base mínima igual ao IAS)  _([Portaria n.º 6-B/2025/1, de 6 de janeiro](https://www.seg-social.pt/ptss/pssd/documento/cmc1xyfxz00dekl2ynxz676sw))_
- **Base máxima mensal (12×IAS)** — €6 445,56 (12 x IAS, 2026)  _([Código Contributivo Art.º 163º, nº 5](https://www.seg-social.pt/ptss/pssd/documento/cmc1xyfxz00dekl2ynxz676sw))_
- **Primeiros 12 meses** — Isento de contribuições  _(Código Contributivo)_
- **Emprego concorrente (< 4×IAS)** — Isento se rendimento relevante < 4 x IAS/mês (em 2026 4 x 537,13 = €2 148,52)  _([Código Contributivo Art.º 157º, nº 1, a)](https://www.seg-social.pt/ptss/pssd/documento/cmc1xyfxz00dekl2ynxz676sw))_
- **Declaração trimestral** — Janeiro (out-dez), abril (jan-mar), julho (abr-jun), outubro (jul-set)  _(Código Contributivo)_
- **Pagamento mensal** — Entre 10 e 20 do mês  _(Código Contributivo)_
- **Dedutibilidade fiscal** — SIM — dedutíveis do IRS  _(CIRS)_

## Section 1 -- Quick reference

**Quick reference**  _(https://www.seg-social.pt/ptss/pssd/documento/cmc1xyfxz00dekl2ynxz676sw)_

| Field | Value |
| --- | --- |
| Country | Portugal (Portuguese Republic) |
| Authority | ISS (Instituto da Segurança Social) for contributions; AT (Autoridade Tributária) for tax |
| Primary legislation | Código Contributivo (Lei n.o 110/2009, art. 139-170) |
| Supporting legislation | Decreto Regulamentar 1-A/2011; annual updates via Portaria |
| Self-employed rate | 21.4% |
| Empresário em nome individual rate | 25.2% |
| Relevant income -- services | 70% of gross |
| Relevant income -- goods | 20% of gross |
| Minimum monthly contribution | EUR 20 |
| Maximum monthly base (12x IAS) | EUR 6 445,56 (2026) |
| First 12 months | Exempt from contributions |
| Declaration frequency | Quarterly |
| Payment frequency | Monthly (between 10th and 20th) |
| Currency | EUR only |
| Contributor | Open Accountants |
| Validated by | Not reviewed by an accountant |
| Validation date | Not reviewed by an accountant |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

- **Required inputs before computing** — Before computing, you MUST obtain: 1. Activity type -- trabalhador independente, empresário em nome individual, or profissional liberal? 2. Gross quarterly income (rendimento relevante) -- from the quarterly declaration 3. Year of activity -- first 12 months exempt from contributions 4. Any concurrent employment? -- reduced rate may apply 5. Category of services -- services (prestação de serviços) vs sales of goods (venda de bens)? 6. Does the client have an accountant (contabilidade organizada)? -- affects relevant income calculation. If income type (services vs goods) is unknown, STOP. The relevant income percentage differs.

### Refusal catalogue

- **R-PT-SOC-1 -- Cross-border EU worker** — Trigger: client is a Portuguese resident providing services in another EU state. Message: "Cross-border social insurance requires A1 certificate analysis under EU Regulation 883/2004. Escalate to qualified adviser."
- **R-PT-SOC-2 -- Pensioner reduced rates** — Trigger: self-employed pensioner asks about reduced contribution rate. Message: "Pensioner contribution rates require confirmation with ISS. Flag for reviewer."

### Prohibitions

- **Prohibitions list** — NEVER apply 21.4% to gross income directly -- the relevant income percentage (70% for services, 20% for goods) must be applied first. NEVER forget the first 12 months exemption for new self-employed. NEVER ignore the minimum monthly contribution of EUR 20 -- with zero income, or contributions below EUR 20, this minimum applies after the exemption period. NEVER confuse the self-employed rate (21.4%) with the empresário rate (25.2%). NEVER present quarterly declaration income as the contribution base -- it must be converted to monthly. NEVER forget to clamp at the maximum of 12 x IAS (EUR 6 445,56 in 2026). NEVER state that contributions are NOT tax-deductible -- they ARE deductible from IRS income. NEVER advise on concurrent employment exemption without verifying the 4 x IAS threshold.  _(https://www.seg-social.pt/ptss/pssd/documento/cmc1xyfxz00dekl2ynxz676sw)_

## Section 3 -- Relevant income calculation

Legislation: Código Contributivo, art. 162

### Without organized accounting (sem contabilidade organizada)

**Relevant income percentages without organized accounting**

| Income type | Relevant income % |
| --- | --- |
| Prestação de serviços (services) | 70% of gross |
| Produção e venda de bens (goods) | 20% of gross |
| Mixed (services + goods) | Apply each % to respective category |

### With organized accounting (com contabilidade organizada)

- **Relevant income with organized accounting** — Relevant income = actual net profit from accounting records.

### Quarterly to monthly conversion

- **Quarterly to monthly conversion formula** — quarterly_relevant_income = sum of relevant_income for the 3 months in the quarter monthly_relevant_income = quarterly_relevant_income / 3

## Section 4 -- Rates, base, and bounds (2026)

Legislation: Código Contributivo, art. 163, 168

### Contribution rates

**Contribution rates**  _(https://www.seg-social.pt/ptss/pssd/documento/cmc1xyfxz00dekl2ynxz676sw)_

| Category | Rate |
| --- | --- |
| Trabalhador independente | 21.4% |
| Empresário em nome individual (commercial/industrial income) and EIRL holder | 25.2% |

### Base bounds

**Base bounds**  _(https://www.seg-social.pt/ptss/pssd/documento/cmc1xyfxz00dekl2ynxz676sw)_

| Bound | Amount |
| --- | --- |
| Minimum monthly contribution (no IAS minimum base) | EUR 20 |
| Maximum monthly base (12x IAS, 2026) | EUR 6 445,56 |

- **Monthly base clamp formula** — monthly_base = min(monthly_relevant_income, 6 445,56); if the resulting contribution is below EUR 20, pay EUR 20  _(https://www.seg-social.pt/ptss/pssd/documento/cmc1xyfxz00dekl2ynxz676sw)_

## Section 5 -- Computation steps

### Step 5.1 -- Quarterly declaration

**Quarterly declaration schedule**

| Declaration period | Income period covered | Filing deadline |
| --- | --- | --- |
| January | Oct--Dec (prior year) | End of January |
| April | Jan--Mar | End of April |
| July | Apr--Jun | End of July |
| October | Jul--Sep | End of October |

### Step 5.2 -- Calculate monthly relevant income

- **Monthly relevant income calculation** — IF services_only (sem contabilidade): relevant_income = quarterly_gross x 70% / 3 ELIF goods_only: relevant_income = quarterly_gross x 20% / 3 ELIF mixed: relevant_income = (services_gross x 70% + goods_gross x 20%) / 3 ELIF contabilidade_organizada: relevant_income = prior-year lucro tributável / 12 (minimum 805,70 = 1,5 x IAS; fixed in October for the following year)  _(https://www.seg-social.pt/ptss/pssd/documento/cmc1xyfxz00dekl2ynxz676sw)_

### Step 5.3 -- Apply bounds and calculate

- **Apply bounds and calculate contribution** — monthly_base = min(relevant_income, 6 445,56) monthly_contribution = max(20, monthly_base x 21.4%)  _(https://www.seg-social.pt/ptss/pssd/documento/cmc1xyfxz00dekl2ynxz676sw)_

### Step 5.4 -- Contributions apply for the next quarter

- **Contributions apply for next quarter** — The quarterly declaration determines contributions for the month of the declaration and the 2 following months.  _(https://www.seg-social.pt/ptss/pssd/documento/cmc1xyfxz00dekl2ynxz676sw)_

## Section 6 -- Payment schedule, exemptions, and tax deductibility

### Payment schedule

**Payment schedule**

| Obligation | Due date |
| --- | --- |
| Monthly contribution payment | Between 10th and 20th of each month |
| Payment method | Direct debit, ATM, or Segurança Social Direta portal |

- **Late payment** — Late payment: interest at legal rate + potential loss of benefits.

### Exemptions

- **First 12 months** — new self-employed workers are exempt from contributions for the first 12 months of activity.
- **Concurrent employment exemption** — if the self-employed person also has employment where the employer pays at least the minimum contribution base: If employment income >= IAS: self-employed contributions may be reduced or exempt. If average monthly relevant income >= 4 x IAS (EUR 2 148,52 in 2026): exemption does NOT apply, and contributions are due on the amount above that limit  _(https://www.seg-social.pt/ptss/pssd/documento/cmc1xyfxz00dekl2ynxz676sw)_

### Tax deductibility

**Tax deductibility**

| Question | Answer |
| --- | --- |
| Are Segurança Social contributions deductible? | YES -- from gross income for IRS purposes |
| Classification | Category B deductions |
| When deductible? | In the year they are paid |

## Section 7 -- Organized accounting and recibos verdes

### Self-employed with organized accounting

- **Organized accounting net profit rule** — Relevant income = prior-year taxable profit (lucro tributável, Anexo SS of Modelo 3) / 12, with a minimum monthly base of EUR 805,70 (1,5 x IAS), fixed in October for the following year. Confirm profit calculation methodology with contabilista. Flag for reviewer.  _(https://www.seg-social.pt/ptss/pssd/documento/cmc1xyfxz00dekl2ynxz676sw)_

### Recibos verdes (green receipts) income

- **Recibos verdes income treatment** — This IS self-employed income. Standard 70% relevant income rule applies. All recibos verdes amounts are reported in the quarterly declaration.

## Section 8 -- Edge case registry

### EC1 -- First year of activity

Situation: Client opened activity in March 2025. Resolution: Exempt from contributions until February 2026 (12 months). First quarterly declaration due in April 2026. Contributions begin from the month following the first declaration.

### EC2 -- Services income below minimum

Situation: Client provides services with quarterly gross EUR 1,000. Resolution: Relevant income = EUR 1,000 x 70% / 3 = EUR 233.33/month. Monthly contribution = EUR 233.33 x 21.4% = EUR 49.93 (above the EUR 20 minimum, so no floor applies).

### EC3 -- Very high income

Situation: Client earns EUR 30,000/quarter from services. Resolution: Relevant income = EUR 7,000/month. Capped at EUR 6,445.56 (12 x IAS, 2026). Monthly contribution = EUR 6,445.56 x 21.4% = EUR 1,379.35.

### EC4 -- Mixed services and goods

Situation: Client earns EUR 6,000 from services and EUR 15,000 from goods in the quarter. Resolution: Relevant income = (EUR 6,000 x 70% + EUR 15,000 x 20%) / 3 = EUR 2,400/month. Contribution = EUR 2,400 x 21.4% = EUR 513.60.

### EC5 -- Concurrent employment, exemption applies

Situation: Client employed at EUR 1,200/month, self-employed quarterly services EUR 2,000. Resolution: Self-employed relevant income = EUR 466.67/month (below 4 x IAS). Employment exemption applies. Contributions = EUR 0.

## Section 9 -- Reviewer escalation protocol

When a situation requires reviewer judgement:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Qualified contabilista certificado must confirm before advising client.
```

When a situation is outside skill scope:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified contabilista. Document gap.
```

## Section 10 -- Test suite

### Test 1 -- Standard services, mid-range

Input: Quarterly gross services EUR 9,000, no employment, established. Expected output: Relevant income = EUR 2,100/month. Contribution = EUR 449.40/month. Annual: EUR 5,392.80.

### Test 2 -- Minimum base applies

Input: Quarterly gross services EUR 1,500. Expected output: Relevant income = EUR 350/month. Base = EUR 350 (no minimum base). Contribution = EUR 74.90/month (above the EUR 20 minimum).

### Test 3 -- Maximum base applies

Input: Quarterly gross services EUR 30,000. Expected output: Relevant income = EUR 7,000/month. Capped at EUR 6,445.56 (12 x IAS, 2026). Contribution = EUR 1,379.35/month.

### Test 4 -- First year exempt

Input: Activity opened 4 months ago, quarterly gross EUR 12,000. Expected output: Exempt (within first 12 months). Contributions = EUR 0.

### Test 5 -- Goods-only income

Input: Quarterly gross goods sales EUR 20,000, no employment. Expected output: Relevant income = EUR 1,333.33/month. Contribution = EUR 285.33/month.

### Test 6 -- Concurrent employment, exemption applies

Input: Employment salary EUR 1,500/month, self-employed quarterly services EUR 2,000. Expected output: Self-employed relevant income = EUR 466.67/month (below 4 x IAS). Exemption applies. Contributions = EUR 0.

### Test 7 -- Empresário em nome individual

Input: Sole proprietor with employees, quarterly services EUR 15,000. Expected output: Rate = 25.2%. Relevant income = EUR 3,500/month. Contribution = EUR 882.00/month.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

> Contributed by Ryan Duguid.

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
