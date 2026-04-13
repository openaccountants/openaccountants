---
name: br-indirect-tax
description: >
  Use this skill whenever asked about Brazilian indirect tax obligations (ICMS, ISS, IPI) for self-employed individuals or small businesses. Trigger on phrases like "ICMS", "ISS", "IPI", "Brazil VAT", "Brazilian indirect tax", "nota fiscal", "imposto sobre servicos", "imposto sobre circulacao de mercadorias", or any question about indirect tax computation or compliance in Brazil. Covers ISS (municipal, 2-5%), ICMS (state, variable), IPI (federal), interaction with Simples Nacional, and the upcoming IBS/CBS tax reform. ALWAYS read this skill before touching any Brazilian indirect tax work.
version: 2.0
jurisdiction: BR
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Brazil Indirect Tax (ICMS/ISS/IPI) -- Self-Employed Skill v2.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | Brazil (Republica Federativa do Brasil) |
| Tax | ISS (municipal, 2-5%), ICMS (state, 7-25%), IPI (federal, varies by product) |
| Currency | BRL only |
| Tax year | Calendar year |
| Primary legislation | LC 87/1996 (Lei Kandir -- ICMS); LC 116/2003 (ISS); Decreto 7.212/2010 (RIPI -- IPI) |
| Supporting legislation | CF/88 Art. 155-156; LC 123/2006 (Simples Nacional); EC 132/2023 (Tax Reform) |
| Tax authority | State SEFAZ (ICMS); Municipal prefeitura (ISS); Receita Federal (IPI) |
| Filing portal | State SEFAZ portals; municipal NFS-e portals; Receita Federal (e-CAC) |
| Filing deadline | Varies by state, municipality, and regime |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by a Brazilian contador (CRC-registered) |
| Skill version | 2.0 |

### ISS Rate Range

| Municipality | Common ISS Rate |
|---|---|
| Sao Paulo | 2% to 5% (IT services typically 2-3%) |
| Rio de Janeiro | 2% to 5% |
| Most municipalities | Default 5% unless reduced by specific municipal law |

### ICMS Internal Rates (Intrastate)

| State | Standard Rate |
|---|---|
| Sao Paulo | 18% |
| Rio de Janeiro | 20% (18% + FECP 2%) |
| Minas Gerais | 18% |
| Most states | 17-20% |

### Interstate ICMS Rates

| Route | Rate |
|---|---|
| South/Southeast to South/Southeast | 12% |
| South/Southeast to North/Northeast/Center-West/ES | 7% |
| North/Northeast/Center-West/ES to any state | 12% |
| Imported goods (any interstate) | 4% |

### Conservative Defaults

| Ambiguity | Default |
|---|---|
| Unknown tax regime | Outside Simples Nacional (apply normal rates) |
| Unknown ICMS rate | Highest applicable intrastate rate |
| Unknown ISS rate | 5% (municipal maximum) |
| Unknown CNAE classification | Services (ISS) |
| Unknown interstate route | 7% (most conservative for credit purposes) |

---

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- tax regime (Simples/Lucro Presumido/Lucro Real), activity type (services/goods/manufacturing), CNAE code(s), state and municipality of registration.

**Recommended** -- revenue breakdown by type, interstate sales detail, Simples Nacional DAS history, nota fiscal register.

**Ideal** -- complete accounting records, ICMS credit ledger, ISS retention records, NF-e/NFS-e XML files.

### Refusal Catalogue

**R-BR-1 -- Tax reform transition (IBS/CBS).** "The IBS/CBS tax reform is still being finalized. Transition rules are not yet complete. Escalate all tax reform questions."

**R-BR-2 -- ICMS-ST detailed computation.** "ICMS Substituicao Tributaria requires product-specific MVA lookup and state-specific protocols. Escalate to contador."

**R-BR-3 -- Guerra fiscal disputes.** "Interstate tax incentive disputes (guerra fiscal) require specialist analysis. Escalate."

**R-BR-4 -- IPI complex chains.** "IPI credit chains for multi-step manufacturing require specialist analysis. Escalate."

---

## Section 3 -- Transaction Pattern Library

### 3.1 Revenue Patterns

| Pattern | Tax Treatment | Notes |
|---|---|---|
| VENDA MERCADORIA, NF-E | ICMS on goods sale | Intrastate rate applies |
| PRESTACAO SERVICO, NFS-E | ISS on service | Municipal rate applies |
| VENDA INTERESTADUAL | ICMS at interstate rate | 7% or 12% depending on route |
| EXPORTACAO | Exempt/zero ICMS and ISS | Immune under CF/88 |
| VENDA CONSUMIDOR FINAL (interstate) | DIFAL applies | Seller collects differential |
| PLATAFORMA DIGITAL, MARKETPLACE | ISS or ICMS | Depends on goods vs services |

### 3.2 Expense / Input Patterns

| Pattern | Tax Treatment | Notes |
|---|---|---|
| COMPRA MERCADORIA, NF-E ENTRADA | ICMS credit (if outside Simples) | Non-cumulative credit |
| MATERIA PRIMA, INSUMO | ICMS + IPI credit | Manufacturing inputs |
| SERVICO TOMADO, NFS-E | ISS may be retained at source | Check retention rules |
| ENERGIA ELETRICA | ICMS credit (partial) | Only for industrial use in some states |
| TELECOMUNICACOES | ICMS credit (partial) | Varies by state |
| ALUGUEL COMERCIAL | No ICMS/ISS credit | Rent is not subject to indirect tax |

### 3.3 Simples Nacional Patterns

| Pattern | Tax Treatment | Notes |
|---|---|---|
| DAS SIMPLES NACIONAL | Unified payment includes ICMS/ISS | Unless above sublimit |
| ICMS-ST SEPARADO | Paid outside Simples even in Simples | Substitute tributario products |
| ICMS IMPORTACAO | Paid separately at customs | Even in Simples |

---

## Section 4 -- Worked Examples

### Example 1 -- ISS Computation (Outside Simples)

**Input:** Consulting firm in Sao Paulo. Monthly service revenue R$ 50,000. ISS rate 5%.

**Computation:**
- ISS = R$ 50,000 x 5% = R$ 2,500

### Example 2 -- ICMS Computation (Outside Simples, Intrastate SP)

**Input:** Retailer in SP selling goods worth R$ 100,000. Internal rate 18%. Purchases R$ 60,000 with 18% ICMS.

**Computation:**
- ICMS on sales: R$ 100,000 x 18% = R$ 18,000
- ICMS credits on purchases: R$ 60,000 x 18% = R$ 10,800
- ICMS payable: R$ 18,000 - R$ 10,800 = R$ 7,200

### Example 3 -- Interstate Sale (SP to BA)

**Input:** SP company sells R$ 10,000 goods to BA company. Interstate rate 7%. BA internal rate 19%.

**Computation:**
- ICMS charged: R$ 10,000 x 7% = R$ 700 (seller pays to SP SEFAZ)
- If B2B (buyer is taxpayer): buyer pays DIFAL of 12% (19% - 7%) to BA
- If B2C: seller collects DIFAL of 12% and remits to BA

### Example 4 -- ISS Retention at Source

**Input:** Consulting invoice R$ 20,000 to large corporate client. ISS rate 5%. Subject to retention.

**Computation:**
- ISS = R$ 20,000 x 5% = R$ 1,000
- Client retains R$ 1,000 and remits to municipality
- Provider receives R$ 19,000
- Provider does not pay ISS separately on this invoice

---

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 ISS Structure

**Legislation:** LC 116/2003

Municipal tax on services. Rate range 2% to 5%. Base: gross price of the service. General rule: taxed where the service provider is established. Exceptions under Art. 3 for services taxed where performed.

### 5.2 ICMS Structure

**Legislation:** LC 87/1996

State tax on sale of goods, interstate/inter-municipal transport, telecommunications. Non-cumulative (credit for ICMS paid on inputs outside Simples). Rate varies by state and product.

### 5.3 IPI Structure

**Legislation:** Decreto 7.212/2010

Federal tax on industrialized products. Applies to manufacturers and importers. Rate varies by product per TIPI table (NCM code). Non-cumulative. Most self-employed service providers do NOT pay IPI.

### 5.4 Simples Nacional Interaction

**Legislation:** LC 123/2006, Art. 13, 18

ICMS and ISS are included in the DAS for Simples Nacional businesses below the R$ 3,600,000 sublimit. Above the sublimit, ICMS and ISS are paid outside Simples at normal rates.

### 5.5 Nota Fiscal Types

NF-e (goods/ICMS), NFS-e (services/ISS), NFC-e (retail consumer), CT-e (transport). NFS-e issued via municipal portal with provider CNPJ, client CNPJ/CPF, service code, value, ISS rate, ISS amount.

---

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 ISS Location of Taxation

Flag for reviewer when services are performed in a municipality different from the provider's registration. Certain services are taxed where performed under LC 116/2003, Art. 3.

### 6.2 DIFAL Computation

DIFAL applies when selling to a non-taxpayer consumer in another state. DIFAL = internal rate of destination state minus interstate rate. Flag for reviewer on all DIFAL calculations.

### 6.3 ICMS-ST (Substituicao Tributaria)

ICMS collected upfront by manufacturer/importer for the entire chain. Applies to specific product categories. Computation requires MVA (Margem de Valor Agregado). Always flag for reviewer.

### 6.4 Software Classification

SaaS/cloud services are generally ISS. Packaged software was historically ICMS but increasingly ISS. Flag for reviewer -- must check state and municipal legislation.

---

## Section 7 -- Excel Working Paper Template

```
BRAZIL INDIRECT TAX -- Working Paper
Period: [Month / Quarter]

A. ISS
  A1. Total service revenue                        ___________
  A2. ISS rate                                     ___________
  A3. ISS due                                      ___________
  A4. ISS retained at source                       ___________
  A5. ISS payable (A3 - A4)                        ___________

B. ICMS
  B1. Total goods revenue (intrastate)             ___________
  B2. ICMS rate (intrastate)                       ___________
  B3. Output ICMS                                  ___________
  B4. Input ICMS credits                           ___________
  B5. ICMS payable (B3 - B4)                       ___________
  B6. Interstate sales                             ___________
  B7. DIFAL (if B2C interstate)                    ___________

C. SIMPLES NACIONAL CHECK
  C1. Revenue in last 12 months (RBT12)            ___________
  C2. Above R$ 3,600,000 sublimit? (Y/N)           ___________
  C3. If yes: ICMS/ISS paid outside Simples        ___________

REVIEWER FLAGS:
  [ ] Tax regime confirmed?
  [ ] CNAE codes verified?
  [ ] Interstate operations flagged?
  [ ] ICMS-ST products identified?
  [ ] Sublimit check performed?
```

---

## Section 8 -- Bank Statement Reading Guide

### Brazilian Bank Statement Formats

| Bank | Format | Key Fields |
|---|---|---|
| Banco do Brasil, Caixa, Itau | CSV, PDF, OFX | Data, Historico, Valor, Saldo |
| Bradesco, Santander | CSV, PDF | Data, Descricao, Debito, Credito |
| Nubank, Inter, C6 | CSV | Data, Descricao, Valor |

### Key Brazilian Banking Terms

| Term | Classification Hint |
|---|---|
| TED, DOC, PIX | Transfer -- check direction |
| BOLETO | Bill payment -- likely expense |
| DAS, SIMPLES | Simples Nacional tax payment |
| SEFAZ, ICMS | State tax payment |
| PREFEITURA, ISS | Municipal tax payment |
| NF-E, NOTA FISCAL | Invoice-related |

---

## Section 9 -- Onboarding Fallback

```
ONBOARDING QUESTIONS -- BRAZIL INDIRECT TAX
1. What is your tax regime? (Simples Nacional / Lucro Presumido / Lucro Real)
2. What are your CNAE codes?
3. Activity type: services, goods, or manufacturing?
4. State and municipality of registration?
5. Do you sell interstate? To which states?
6. Do you import goods?
7. If on Simples: what is your RBT12 (last 12 months revenue)?
8. Are any of your products subject to ICMS-ST?
9. Do you issue NFS-e, NF-e, or both?
10. Any ISS retention at source situations?
```

---

## Section 10 -- Reference Material

### Key Legislation

| Topic | Reference |
|---|---|
| ISS rates and rules | LC 116/2003 |
| ISS minimum rate | LC 157/2016 |
| ICMS (Lei Kandir) | LC 87/1996 |
| Interstate rates | Resolucao SF 13/2012 (imported goods 4%) |
| IPI | Decreto 7.212/2010 |
| Simples Nacional | LC 123/2006 |
| Tax reform | EC 132/2023 |
| Nota fiscal | CONFAZ agreements |

### Tax Reform (IBS/CBS) -- Status

Brazil is replacing ICMS, ISS, IPI, PIS, and COFINS with IBS (state/municipal) and CBS (federal). Transition period 2026-2032; full implementation by 2033. Combined rate expected ~26.5%. Implementation laws being debated/enacted through 2025-2026. ESCALATE all tax reform transition questions.

---

## PROHIBITIONS

- NEVER apply ICMS to pure services -- services are subject to ISS (except telecom and interstate transport)
- NEVER apply ISS to sale of physical goods -- goods are subject to ICMS
- NEVER ignore the R$ 3,600,000 sublimit for Simples Nacional ICMS/ISS
- NEVER assume ICMS rates are uniform across states -- they vary from 7% to 25%+
- NEVER assume ISS rates are the same in all municipalities -- they range from 2% to 5%
- NEVER compute IPI for pure service providers -- IPI applies only to industrialized products
- NEVER ignore ICMS-ST obligations -- they apply even to Simples Nacional companies
- NEVER advise on the IBS/CBS tax reform as if it is fully enacted
- NEVER present calculations as definitive -- always label as estimated and direct client to a CRC-registered contador

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CRC-registered contador or equivalent licensed practitioner in Brazil) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
