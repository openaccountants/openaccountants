---
name: portugal-vat-return
description: Use this skill whenever asked to prepare, review, or create a Portuguese VAT return (Declaracao Periodica de IVA) for any client. Trigger on phrases like "prepare VAT return", "do the Portuguese VAT", "declaracao periodica", "IVA Portugal", "preencher declaracao de IVA", or any request involving Portuguese VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, SAF-T extracts, or other source data. This skill contains the complete Portuguese VAT classification rules, Declaracao Periodica campo mappings, deductibility rules, reverse charge treatment, regional rate tables (Continental, Madeira, Azores), SAF-T requirements, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any VAT-related work for Portugal.
status: deep-research-verified
version: 1.1
---

# Portugal VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Portugal (Continental, Madeira, Azores) |
| Jurisdiction Code | PT |
| Primary Legislation | Codigo do IVA (CIVA) -- Decreto-Lei 394-B/84, de 26 de dezembro |
| Supporting Legislation | RITI -- Regime do IVA nas Transacoes Intracomunitarias (DL 290/92); CIVA Art. 21 (blocked deductions); CIVA Art. 53 (regime de isencao); DL 198/2012 (SAF-T reporting); Portaria 302/2016 (SAF-T file structure) |
| Tax Authority | Autoridade Tributaria e Aduaneira (AT) |
| Filing Portal | Portal das Financas (https://www.portaldasfinancas.gov.pt) |
| Return Name | Declaracao Periodica de IVA (DPIVA) |
| Contributor | Deep research verified -- April 2026 |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.1 |
| Confidence Coverage | Tier 1: campo assignment, reverse charge, deductibility blocks, derived calculations. Tier 2: pro-rata, sector-specific deductions, Azores/Madeira rates. Tier 3: complex group structures, VAT groups (from July 2026), special regimes. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude assigns, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A Contabilista Certificado must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to Contabilista Certificado and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and NIF (Numero de Identificacao Fiscal)** [T1] -- 9 digits; VAT ID format is PT + 9 digits (e.g., PT123456789). CIVA Art. 2.
2. **VAT regime** [T1] -- Regime normal (CIVA Art. 1), regime de isencao (CIVA Art. 53), regime dos pequenos retalhistas (CIVA Art. 60-68), or regime forfetario dos produtores agricolas (CIVA Art. 59-A-59-D). CIVA Art. 29.
3. **Filing frequency** [T1] -- Monthly (turnover >= EUR 650,000 in prior year per CIVA Art. 41(1)(a)) or quarterly (turnover < EUR 650,000 per CIVA Art. 41(1)(b)).
4. **Region** [T1] -- Continental Portugal, Regiao Autonoma da Madeira, or Regiao Autonoma dos Acores. Determines applicable rate table. CIVA Art. 18.
5. **Industry/sector** [T2] -- Impacts partial deduction and sector-specific exemptions (e.g., banking, insurance, medical). CIVA Art. 9.
6. **Does the business make exempt supplies (CIVA Art. 9)?** [T2] -- If yes, pro-rata (percentagem de deducao) required under CIVA Art. 23.
7. **IVA credit carried forward** [T1] -- Campo 61 (excesso do periodo anterior). CIVA Art. 22(4).
8. **Is the client in regime de isencao (CIVA Art. 53)?** [T1] -- Small business exemption; confirm turnover below EUR 15,000 threshold.
9. **SAF-T (PT) compliance** [T1] -- Is the entity using certified invoicing software and submitting SAF-T files monthly? DL 198/2012.
10. **Does the client have intra-Community operations?** [T1] -- If yes, must file Declaracao Recapitulativa (CIVA Art. 23 RITI).

For CIVA Art. 53 exempt clients [T1]: confirm turnover was below EUR 15,000 (threshold since DL 35/2025, effective 1 July 2025; previously EUR 14,500). Tolerance margin: 25% above threshold (EUR 18,750). If turnover exceeds EUR 15,000 but stays below EUR 18,750 in a calendar year, exemption lapses from 1 January of the following year. If EUR 18,750 is exceeded during the year, IVA must be charged from the invoice that causes the breach. CIVA Art. 53(1).

**If any of items 1-3 are unknown, STOP. Do not classify any transactions until regime and period are confirmed.**

---

## Step 1: VAT Return Form Structure -- Declaracao Periodica de IVA (DPIVA)

**Filed electronically via Portal das Financas (AT). Certificado digital or Chave Movel Digital required.** [T1]
**Legislation:** CIVA Art. 41; Portaria 375/2003 (form structure).

The DPIVA is organised into Quadros (sections). Below is the complete campo (field) listing.

### Quadro 01-05: Identification and Period

| Campo | Portuguese Name | English Translation | Notes |
|-------|----------------|---------------------|-------|
| Q01 | Periodo de tributacao | Tax period | Month (MM) or quarter (QT) |
| Q02 | Ano | Year | Calendar year |
| Q03 | NIF do sujeito passivo | Taxpayer NIF | 9 digits |
| Q04 | Servico de financas competente | Competent tax office | Code number |
| Q04A | Declaracao dentro do prazo | Declaration within deadline | Yes/No |
| Q05 | Tipo de declaracao | Declaration type | 1st submission or replacement |

### Quadro 06: Apuramento do Imposto (Tax Calculation)

#### Quadro 06A -- Transmissoes de Bens e Prestacoes de Servicos (Output -- Sales/Supplies)

| Campo | Portuguese Name | English Translation | Type | Rate Region |
|-------|----------------|---------------------|------|-------------|
| Campo 1 | Base tributavel -- taxa reduzida | Taxable base -- reduced rate | Base | Continental 6% |
| Campo 2 | Imposto a favor do Estado -- taxa reduzida | Tax due to State -- reduced rate | Tax | Continental 6% |
| Campo 5 | Base tributavel -- taxa intermedia | Taxable base -- intermediate rate | Base | Continental 13% |
| Campo 6 | Imposto a favor do Estado -- taxa intermedia | Tax due to State -- intermediate rate | Tax | Continental 13% |
| Campo 3 | Base tributavel -- taxa normal | Taxable base -- standard rate | Base | Continental 23% |
| Campo 4 | Imposto a favor do Estado -- taxa normal | Tax due to State -- standard rate | Tax | Continental 23% |
| Campo 1A | Base tributavel -- taxa reduzida (Acores) | Taxable base -- reduced rate (Azores) | Base | Azores 4% |
| Campo 2A | Imposto -- taxa reduzida (Acores) | Tax -- reduced rate (Azores) | Tax | Azores 4% |
| Campo 5A | Base tributavel -- taxa intermedia (Acores) | Taxable base -- intermediate rate (Azores) | Base | Azores 9% |
| Campo 6A | Imposto -- taxa intermedia (Acores) | Tax -- intermediate rate (Azores) | Tax | Azores 9% |
| Campo 3A | Base tributavel -- taxa normal (Acores) | Taxable base -- standard rate (Azores) | Base | Azores 16% |
| Campo 4A | Imposto -- taxa normal (Acores) | Tax -- standard rate (Azores) | Tax | Azores 16% |
| Campo 1B | Base tributavel -- taxa reduzida (Madeira) | Taxable base -- reduced rate (Madeira) | Base | Madeira 4% |
| Campo 2B | Imposto -- taxa reduzida (Madeira) | Tax -- reduced rate (Madeira) | Tax | Madeira 4% |
| Campo 5B | Base tributavel -- taxa intermedia (Madeira) | Taxable base -- intermediate rate (Madeira) | Base | Madeira 12% |
| Campo 6B | Imposto -- taxa intermedia (Madeira) | Tax -- intermediate rate (Madeira) | Tax | Madeira 12% |
| Campo 3B | Base tributavel -- taxa normal (Madeira) | Taxable base -- standard rate (Madeira) | Base | Madeira 22% |
| Campo 4B | Imposto -- taxa normal (Madeira) | Tax -- standard rate (Madeira) | Tax | Madeira 22% |

#### Quadro 06A -- Operacoes Isentas e Outras (Exempt and Other Operations)

| Campo | Portuguese Name | English Translation | Notes |
|-------|----------------|---------------------|-------|
| Campo 7 | Transmissoes intracomunitarias de bens | Intra-Community supplies of goods | Exempt with right of deduction. CIVA Art. 14 RITI. |
| Campo 8 | Exportacoes | Exports (non-EU) | Exempt with right of deduction. CIVA Art. 14(1)(a). |
| Campo 9 | Operacoes isentas sem direito a deducao | Exempt operations without right of deduction | CIVA Art. 9 exemptions. |
| Campo 9A | Operacoes isentas com direito a deducao (outras) | Exempt operations with right of deduction (other) | Other Art. 14 exemptions. |

#### Quadro 06A -- Aquisicoes Intracomunitarias (IC Acquisitions -- Self-Assessment)

| Campo | Portuguese Name | English Translation | Type | Rate |
|-------|----------------|---------------------|------|------|
| Campo 10 | Base -- aquisicoes IC taxa reduzida | IC acquisitions base -- reduced rate | Base | 6%/4%/4% |
| Campo 11 | Imposto -- aquisicoes IC taxa reduzida | IC acquisitions tax -- reduced rate | Tax | 6%/4%/4% |
| Campo 13 | Base -- aquisicoes IC taxa intermedia | IC acquisitions base -- intermediate rate | Base | 13%/9%/12% |
| Campo 14 | Imposto -- aquisicoes IC taxa intermedia | IC acquisitions tax -- intermediate rate | Tax | 13%/9%/12% |
| Campo 12 | Base -- aquisicoes IC taxa normal | IC acquisitions base -- standard rate | Base | 23%/16%/22% |
| Campo 15 | Imposto -- aquisicoes IC taxa normal | IC acquisitions tax -- standard rate | Tax | 23%/16%/22% |

#### Quadro 06A -- Servicos de Outros Estados-Membros (Services from Other EU Member States)

| Campo | Portuguese Name | English Translation | Type |
|-------|----------------|---------------------|------|
| Campo 16 | Base -- servicos do Art. 6(6) CIVA | Services received from EU -- base | Base |
| Campo 17 | Imposto -- servicos do Art. 6(6) CIVA | Services received from EU -- tax | Tax |

#### Quadro 06B -- IVA Dedutivel (Input VAT -- Deductible)

| Campo | Portuguese Name | English Translation | Category |
|-------|----------------|---------------------|----------|
| Campo 20 | Imobilizado -- base tributavel | Fixed assets -- taxable base | Capital assets |
| Campo 21 | Imobilizado -- imposto dedutivel | Fixed assets -- deductible tax | Capital assets |
| Campo 22 | Existencias -- base tributavel | Inventory/stock -- taxable base | Resale goods |
| Campo 23 | Existencias -- imposto dedutivel | Inventory/stock -- deductible tax | Resale goods |
| Campo 24 | Outros bens e servicos -- base tributavel | Other goods and services -- taxable base | Overheads |
| Campo 25 | Outros bens e servicos -- imposto dedutivel | Other goods and services -- deductible tax | Overheads |

#### Quadro 06C -- Regularizacoes (Adjustments)

| Campo | Portuguese Name | English Translation | Direction |
|-------|----------------|---------------------|-----------|
| Campo 40 | Regularizacoes a favor do sujeito passivo | Adjustments in favour of taxpayer | Reduces tax payable |
| Campo 41 | Regularizacoes a favor do Estado | Adjustments in favour of the State | Increases tax payable |

#### Quadro 06D -- Apuramento (Summary Calculation)

| Campo | Portuguese Name | English Translation | Calculation |
|-------|----------------|---------------------|-------------|
| Campo 90 | Total do imposto a favor do Estado | Total output VAT | Sum of all output tax campos |
| Campo 91 | Total do imposto dedutivel | Total deductible input VAT | Sum of all input tax campos |
| Campo 92 | Imposto a entregar ao Estado | VAT payable to State | Campo 90 - Campo 91 (if positive) |
| Campo 93 | Excesso a reportar ao periodo seguinte | Excess to carry forward | Campo 91 - Campo 90 (if positive) |
| Campo 61 | Excesso do periodo anterior | Excess from prior period | Credit brought forward |
| Campo 94 | Total a pagar | Net amount payable | Campo 92 - Campo 61 (if applicable) |
| Campo 95 | Pedido de reembolso | Refund request | Optional; conditions under CIVA Art. 22(5) |
| Campo 96 | Credito de imposto | Tax credit after refund request | Remaining credit |

#### Quadro 06E -- Operacoes em Territorios com Taxas Diferentes

| Campo | Portuguese Name | English Translation | Notes |
|-------|----------------|---------------------|-------|
| Campo 97 | Operacoes onde o imposto e devido noutro EM | Operations where tax is due in another MS | CIVA Art. 6 place of supply |

### Quadro 07: Informacao Complementar (Supplementary Information)

| Campo | Portuguese Name | English Translation | Notes |
|-------|----------------|---------------------|-------|
| Campo 98 | Transmissoes intracomunitarias de bens (detalhe) | IC supplies detail | Also on Declaracao Recapitulativa |
| Campo 99 | Aquisicoes intracomunitarias de bens (detalhe) | IC acquisitions detail | Cross-check with Campo 10-15 |
| Campo 100 | Operacoes triangulares | Triangular operations | RITI Art. 8-10 |
| Campo 101 | Prestacoes de servicos a sujeitos passivos de outros EM | Services supplied to taxable persons in other MS | Art. 6(6)(a) CIVA |
| Campo 102 | Servicos recebidos de sujeitos passivos de outros EM | Services received from taxable persons in other MS | Art. 6(6)(a) CIVA |
| Campo 103 | Transmissoes de bens de que resulta instalacao/montagem noutro EM | Goods with installation/assembly in other MS | RITI Art. 7(2) |

---

## Step 2: Transaction Classification Matrix

### 2a. Determine Transaction Type [T1]

- **Sale** (IVA liquidado / output IVA) or **Purchase** (IVA dedutivel / input IVA). CIVA Art. 1-4.
- Salaries (salarios), social security (TSU), income tax (IRS/IRC), loan repayments (amortizacoes de emprestimo), dividends, bank charges = **OUT OF SCOPE**. Never on DPIVA.
- **Legislation:** CIVA Art. 1 (incidencia objetiva); CIVA Art. 2 (sujeitos passivos).

### 2b. Determine Counterparty Location [T1]

| Location | Classification | Notes |
|----------|---------------|-------|
| Portugal Continental | Domestic -- continental rates | CIVA Art. 18(1) |
| Regiao Autonoma dos Acores | Domestic -- Azores rates | DL Regional 18/2022/A |
| Regiao Autonoma da Madeira | Domestic -- Madeira rates | DL Regional 21/2024/M |
| EU Member State (AT, BE, BG, HR, CY, CZ, DK, EE, FI, FR, DE, GR, HU, IE, IT, LV, LT, LU, NL, PL, RO, SK, SI, ES, SE) | EU | RITI Art. 1 |
| Non-EU (US, UK, BR, CH, AU, etc.) | Third country | UK is non-EU post-Brexit. |

### 2c. Sales Classification Lookup Table [T1]

**Legislation:** CIVA Art. 18, Art. 14, Art. 14 RITI.

| Transaction Type | Counterparty | Rate | Campo (Base) | Campo (Tax) | Legal Basis |
|-----------------|--------------|------|-------------|-------------|-------------|
| Domestic sale -- standard goods/services | PT Continental | 23% | Campo 3 | Campo 4 | CIVA Art. 18(1)(c) |
| Domestic sale -- intermediate goods | PT Continental | 13% | Campo 5 | Campo 6 | CIVA Art. 18(1)(b), Lista II |
| Domestic sale -- reduced goods | PT Continental | 6% | Campo 1 | Campo 2 | CIVA Art. 18(1)(a), Lista I |
| Domestic sale -- standard goods/services | PT Azores | 16% | Campo 3A | Campo 4A | DL Regional 18/2022/A |
| Domestic sale -- intermediate goods | PT Azores | 9% | Campo 5A | Campo 6A | DL Regional 18/2022/A |
| Domestic sale -- reduced goods | PT Azores | 4% | Campo 1A | Campo 2A | DL Regional 18/2022/A |
| Domestic sale -- standard goods/services | PT Madeira | 22% | Campo 3B | Campo 4B | DL Regional 21/2024/M |
| Domestic sale -- intermediate goods | PT Madeira | 12% | Campo 5B | Campo 6B | DL Regional 21/2024/M |
| Domestic sale -- reduced goods | PT Madeira | 4% | Campo 1B | Campo 2B | DL Regional 21/2024/M |
| Intra-Community supply of goods (B2B) | EU | 0% | Campo 7 | -- | CIVA Art. 14 RITI |
| Export of goods | Non-EU | 0% | Campo 8 | -- | CIVA Art. 14(1)(a) |
| Exempt domestic supply | PT | 0% | Campo 9 | -- | CIVA Art. 9 |
| B2B services to EU customer | EU | 0% | Campo 101 (info) | -- | CIVA Art. 6(6)(a) |

### 2d. Purchases Classification Lookup Table [T1]

**Legislation:** CIVA Art. 19-25.

| Transaction Type | Supplier Location | Category | Campo (Base) | Campo (Tax) | Legal Basis |
|-----------------|-------------------|----------|-------------|-------------|-------------|
| Domestic purchase -- fixed assets | PT | Imobilizado | Campo 20 | Campo 21 | CIVA Art. 19(1)(a) |
| Domestic purchase -- resale goods | PT | Existencias | Campo 22 | Campo 23 | CIVA Art. 19(1)(a) |
| Domestic purchase -- overheads | PT | Outros bens e servicos | Campo 24 | Campo 25 | CIVA Art. 19(1)(a) |
| IC acquisition of goods -- reduced rate | EU | Per category | Campo 10 (base) | Campo 11 (tax) | RITI Art. 22 |
| IC acquisition of goods -- intermediate rate | EU | Per category | Campo 13 (base) | Campo 14 (tax) | RITI Art. 22 |
| IC acquisition of goods -- standard rate | EU | Per category | Campo 12 (base) | Campo 15 (tax) | RITI Art. 22 |
| Services received from EU (B2B) | EU | Per category | Campo 16 (base) | Campo 17 (tax) | CIVA Art. 6(6)(a) |
| Services/goods from non-EU | Non-EU | Per category | Campo 16/applicable | Campo 17/applicable | CIVA Art. 6(6)(a) |
| Local consumption abroad (hotel, restaurant) | EU/Non-EU | N/A | No entry | No entry | Foreign VAT irrecoverable |

### 2e. Expense Category Rules [T1]

| Category (Portuguese) | Category (English) | Campo Pair | Rule | Legal Basis |
|-----------------------|--------------------|-----------:|------|-------------|
| Imobilizado | Fixed/capital assets | 20/21 | Tangible and intangible assets capitalised on the balance sheet | CIVA Art. 19(1)(a); SNC/NCRF standards |
| Existencias | Inventory/stock for resale | 22/23 | Goods purchased to be resold without transformation, or raw materials | CIVA Art. 19(1)(a) |
| Outros bens e servicos | Other goods and services / overheads | 24/25 | All other deductible purchases: rent, utilities, professional services, office supplies, etc. | CIVA Art. 19(1)(a) |

---

## Step 3: VAT Rate Tables

### 3a. Continental Portugal Rate Table [T1]

**Legislation:** CIVA Art. 18(1).

| Rate | Name (Portuguese) | Name (English) | Applicable Supplies (Examples) | Legal Basis |
|------|-------------------|-----------------|-------------------------------|-------------|
| 23% | Taxa normal | Standard rate | Most goods and services not listed in Lista I or Lista II. Professional services, electronics, clothing, furniture, alcohol. | CIVA Art. 18(1)(c) |
| 13% | Taxa intermedia | Intermediate rate | Restaurant meals and takeaway (excluding alcoholic beverages); wine; agricultural tools and inputs; musical instruments; horticultural products; some food preparations; diesel used in agriculture. | CIVA Art. 18(1)(b); Lista II annexed to CIVA |
| 6% | Taxa reduzida | Reduced rate | Essential foodstuffs (bread, milk, fruit, vegetables, cereals, meat, fish); pharmaceutical products; medical equipment; books and periodicals; newspapers; passenger transport; hotel accommodation; water supply; electricity (contracted power <= 6.90 kVA); renewable energy equipment; cultural events; social housing construction. | CIVA Art. 18(1)(a); Lista I annexed to CIVA |
| 0% | Isencao com direito a deducao | Zero rate (exemption with deduction right) | Exports (CIVA Art. 14(1)(a)); intra-Community supplies (Art. 14 RITI). | CIVA Art. 14 |

### 3b. Azores (Acores) Rate Table [T2]

**Legislation:** Decreto Legislativo Regional 18/2022/A; CIVA Art. 18(3).

| Rate | Equivalent Continental | Applicable Supplies | Legal Basis |
|------|----------------------|---------------------|-------------|
| 16% | 23% standard | Same scope as continental standard rate | DL Regional 18/2022/A |
| 9% | 13% intermediate | Same scope as continental intermediate rate | DL Regional 18/2022/A |
| 4% | 6% reduced | Same scope as continental reduced rate | DL Regional 18/2022/A |

### 3c. Madeira Rate Table [T2]

**Legislation:** Decreto Legislativo Regional 21/2024/M; CIVA Art. 18(3).

| Rate | Equivalent Continental | Applicable Supplies | Legal Basis |
|------|----------------------|---------------------|-------------|
| 22% | 23% standard | Same scope as continental standard rate | DL Regional 21/2024/M |
| 12% | 13% intermediate | Same scope as continental intermediate rate | DL Regional 21/2024/M |
| 4% | 6% reduced | Same scope as continental reduced rate (effective from 1 October 2024) | DL Regional 21/2024/M |

### 3d. Rate Determination by Region -- Quick Reference [T1]

| Region | Reduced | Intermediate | Standard | Legislation |
|--------|---------|-------------|----------|-------------|
| Continental | 6% | 13% | 23% | CIVA Art. 18(1) |
| Azores | 4% | 9% | 16% | DL Regional 18/2022/A |
| Madeira | 4% | 12% | 22% | DL Regional 21/2024/M |

### 3e. Which Rate Applies -- Place of Taxation [T1]

| Scenario | Rate to Apply | Legal Basis |
|----------|--------------|-------------|
| Seller and buyer both in Continental | Continental rates | CIVA Art. 18(1) |
| Seller in Continental, goods shipped TO Azores | Azores rates | CIVA Art. 18(3) |
| Seller in Continental, goods shipped TO Madeira | Madeira rates | CIVA Art. 18(3) |
| Seller in Azores, goods shipped to Continental | Continental rates | CIVA Art. 18(3) |
| Seller in Azores, buyer in Azores | Azores rates | CIVA Art. 18(3) |
| Seller in Madeira, buyer in Madeira | Madeira rates | CIVA Art. 18(3) |
| Services -- B2B general rule | Rate of place of recipient | CIVA Art. 6(6)(a) |
| Services -- B2C general rule | Rate of place of supplier | CIVA Art. 6(6)(b) |

**Key rule:** For goods, the rate of the destination region applies. For B2B services, the rate of the recipient's region applies. [T1] CIVA Art. 18(3).

---

## Step 4: Blocked Input Tax (Non-Deductible IVA)

### 4a. Fully Blocked Categories [T1]

**Legislation:** CIVA Art. 21.

| Category | Portuguese Term | Rule | Legal Basis |
|----------|----------------|------|-------------|
| Passenger vehicles (purchase, lease, repair, maintenance) | Viaturas de turismo | 0% deductible. IVA fully blocked on acquisition, leasing, rental, repair, and maintenance of viaturas de turismo (passenger cars). | CIVA Art. 21(1)(a) |
| Entertainment expenses | Despesas de representacao | 0% deductible. Includes client entertainment, gifts, hospitality. | CIVA Art. 21(1)(c) |
| Accommodation and meals (general) | Alojamento e alimentacao | 0% deductible. Exception: staff on business travel where > 50% business purpose. | CIVA Art. 21(1)(d) |
| Tobacco | Tabaco | 0% deductible. | CIVA Art. 21(1)(e) |
| Recreational and luxury items | Despesas de divertimento e luxo | 0% deductible. Includes yachts, pleasure boats, hunting, leisure activities. | CIVA Art. 21(1)(f) |
| Personal use | Uso pessoal | 0% deductible. General principle -- IVA only deductible on business-related expenditure. | CIVA Art. 20(1) |

### 4b. Fuel Deductibility Table [T1]

**Legislation:** CIVA Art. 21(1)(b).

| Fuel Type | Vehicle Type | Deductible % | Legal Basis |
|-----------|-------------|-------------|-------------|
| Gasoleo (diesel) | Viatura de turismo (passenger car) | 50% | CIVA Art. 21(1)(b) |
| Gasoleo (diesel) | Viatura comercial (commercial vehicle) | 100% | CIVA Art. 21(1)(b) -- exclusion from restriction |
| Gasolina (petrol) | Viatura de turismo (passenger car) | 50% | CIVA Art. 21(1)(b) |
| Gasolina (petrol) | Viatura comercial (commercial vehicle) | 100% | CIVA Art. 21(1)(b) -- exclusion from restriction |
| GPL (LPG) | Any vehicle | 100% | CIVA Art. 21(1)(b) |
| GNV (natural gas) | Any vehicle | 100% | CIVA Art. 21(1)(b) |
| Eletricidade (electric charging) | Any vehicle (including turismo) | 100% | CIVA Art. 21(1)(b) |
| Biocombustiveis (biofuels) | Viatura de turismo | 50% | CIVA Art. 21(1)(b) |
| Biocombustiveis (biofuels) | Viatura comercial | 100% | CIVA Art. 21(1)(b) |

### 4c. Vehicle Exceptions -- When IVA IS Deductible [T2]

**Legislation:** CIVA Art. 21(2).

IVA on passenger vehicles (viaturas de turismo) IS deductible when the vehicle is used **exclusively** for:

| Exception | Portuguese Term | Deductible? | Legal Basis |
|-----------|----------------|-------------|-------------|
| Goods transport | Transporte de mercadorias | Yes -- 100% | CIVA Art. 21(2)(a) |
| Taxi / hire car services | Servicos de taxi / aluguer | Yes -- 100% | CIVA Art. 21(2)(b) |
| Driving instruction | Ensino de conducao | Yes -- 100% | CIVA Art. 21(2)(c) |
| Vehicle rental as business activity | Locacao (atividade do sujeito passivo) | Yes -- 100% | CIVA Art. 21(2)(d) |
| Emergency / ambulance | Ambulancias | Yes -- 100% | CIVA Art. 21(2) |

**[T2] Reviewer must confirm exclusive business use before allowing deduction.**

### 4d. Accommodation and Meals Exception [T2]

**Legislation:** CIVA Art. 21(1)(d).

| Situation | Deductible? | Condition | Legal Basis |
|-----------|-------------|-----------|-------------|
| Staff on business travel | Yes -- up to 100% | Business travel constitutes > 50% of trip purpose. Must have supporting documentation (travel order, boarding passes, etc.) | CIVA Art. 21(1)(d) |
| Client entertainment meal | No -- 0% | Classified as despesas de representacao | CIVA Art. 21(1)(c) |
| Daily meals for owner/employees at workplace | No -- 0% | Not business travel | CIVA Art. 21(1)(d) |

### 4e. Registration-Based Recovery [T1]

| Regime | IVA Charged on Sales? | Input IVA Recovery? | Legal Basis |
|--------|----------------------|---------------------|-------------|
| Regime normal | Yes | Yes (subject to category rules) | CIVA Art. 19-25 |
| Regime de isencao (CIVA Art. 53) | No | No | CIVA Art. 53(2) |
| Regime dos pequenos retalhistas | Simplified settlement (25% of IVA on purchases) | No standard recovery | CIVA Art. 60-68 |
| Regime forfetario (agricultural) | Flat-rate compensation | No standard recovery | CIVA Art. 59-A to 59-D |

### 4f. Pro-Rata / Partial Deduction (Percentagem de Deducao) [T2]

**Legislation:** CIVA Art. 23.

If business makes both taxable and exempt supplies (CIVA Art. 9):

```
% deducao = (Transmissoes tributaveis + Exportacoes + Transmissoes IC isentas com direito a deducao)
             / (Total do volume de negocios)
             * 100
```

Rounded **up** to the nearest whole integer. CIVA Art. 23(4).

**Annual regularisation required in the December DPIVA or last period DPIVA. Flag for reviewer.**

---

## Step 5: Registration and NIF

### 5a. NIF Format [T1]

| Item | Value | Legal Basis |
|------|-------|-------------|
| NIF structure | 9 digits | DL 14/2013, Art. 4 |
| VAT ID format (VIES) | PT + 9 digits (e.g., PT123456789) | CIVA Art. 2; RITI Art. 18 |
| Check digit | 9th digit -- mod 11 validation | DL 14/2013 |
| First digit meaning | 1-3 = individual; 5 = empresa; 6 = entidade publica; 7 = heranca indivisa; 8 = empresario em nome individual; 9 = irregular/temp | Administrative practice |

### 5b. Regime de Isencao -- CIVA Art. 53 [T1]

| Item | Detail | Legal Basis |
|------|--------|-------------|
| Threshold | EUR 15,000 annual turnover (since DL 35/2025, effective 1 July 2025; previously EUR 14,500) | CIVA Art. 53(1) |
| Tolerance margin | 25% above threshold (EUR 18,750). If exceeded mid-year, IVA must be charged from the invoice causing the breach. If turnover exceeds EUR 15,000 but not EUR 18,750, exemption lapses from 1 January of the following year. | CIVA Art. 53(1) as amended |
| Who qualifies | Sujeitos passivos (taxable persons) who did not exceed EUR 15,000 in the prior calendar year AND do not have organised accounting (contabilidade organizada) AND are not required to have it | CIVA Art. 53(1) |
| Obligations | Invoice must state: "IVA -- regime de isencao, artigo 53.o do CIVA" | CIVA Art. 57 |
| Filing | NO Declaracao Periodica required | CIVA Art. 53 |
| Input IVA | NO recovery | CIVA Art. 53(2) |
| Threshold breach | Must register for regime normal within 30 days. CIVA Art. 58. | CIVA Art. 58 |
| Reverse charge | Art. 53 entities ARE subject to reverse charge on services from abroad (CIVA Art. 2(1)(e)). Must self-assess and pay IVA with NO right to deduct. | CIVA Art. 2(1)(e) |
| Voluntary opt-in | Can voluntarily register for regime normal (renunciation of exemption). Once registered, must remain for minimum 5 years. | CIVA Art. 55 |

### 5c. Registration Process [T1]

| Step | Action | Legal Basis |
|------|--------|-------------|
| 1 | Obtain NIF from AT (Servico de Financas or online) | DL 14/2013 |
| 2 | Submit Declaracao de Inicio de Atividade (start of activity) | CIVA Art. 31 |
| 3 | Select VAT regime | CIVA Art. 29 |
| 4 | Obtain access to Portal das Financas (certificado digital or CMD) | Portaria 375/2003 |
| 5 | Set up certified invoicing software (SAF-T compliant) | DL 198/2012 |

---

## Step 6: Filing Deadlines and Penalties

### 6a. DPIVA Filing Deadlines [T1]

**Legislation:** CIVA Art. 41.

| Filing Frequency | Condition | DPIVA Deadline | Payment Deadline | Legal Basis |
|-----------------|-----------|----------------|------------------|-------------|
| Monthly | Turnover >= EUR 650,000 in prior year | 10th of the 2nd month following the tax period (e.g., January DPIVA due by 10 March) | 15th of the 2nd month following the tax period (e.g., January IVA due by 15 March) | CIVA Art. 41(1)(a) |
| Quarterly | Turnover < EUR 650,000 in prior year | 15th of the 2nd month following the quarter end (e.g., Q1 Jan-Mar DPIVA due by 15 May) | 20th of the 2nd month following the quarter end (e.g., Q1 IVA due by 20 May) | CIVA Art. 41(1)(b) |

### 6b. Quarterly Calendar [T1]

| Quarter | Period | DPIVA Due | Payment Due |
|---------|--------|-----------|-------------|
| Q1 | January -- March | 15 May | 20 May |
| Q2 | April -- June | 15 August | 20 August |
| Q3 | July -- September | 15 November | 20 November |
| Q4 | October -- December | 15 February (following year) | 20 February (following year) |

### 6c. Monthly Calendar Example (2026) [T1]

| Month | DPIVA Due | Payment Due |
|-------|-----------|-------------|
| January 2026 | 10 March 2026 | 15 March 2026 |
| February 2026 | 10 April 2026 | 15 April 2026 |
| March 2026 | 10 May 2026 | 15 May 2026 |
| April 2026 | 10 June 2026 | 15 June 2026 |
| May 2026 | 10 July 2026 | 15 July 2026 |
| June 2026 | 10 August 2026 | 15 August 2026 |

### 6d. Other Filing Obligations [T1]

| Return | Period | Deadline | Legal Basis |
|--------|--------|----------|-------------|
| Declaracao Recapitulativa (IC sales/services list) | Monthly or quarterly (aligns with DPIVA) | Same as DPIVA | RITI Art. 23; Portaria 986/2009 |
| Declaracao Anual / IES (Informacao Empresarial Simplificada) | Annual | 15 July of the following year | DL 8/2007; CIVA Art. 29(1)(g) |
| SAF-T (PT) monthly submission | Monthly | By the 5th of the following month | DL 198/2012; Portaria 302/2016 |
| Comunicacao de inventarios (inventory report) | Annual | 31 January of the following year | DL 198/2012, Art. 3-A |

### 6e. Penalties (Coimas) [T1]

**Legislation:** Regime Geral das Infracoes Tributarias (RGIT) -- Lei 15/2001.

| Infraction | Penalty Range | Legal Basis |
|------------|--------------|-------------|
| Late filing of DPIVA | EUR 150 to EUR 3,750 (negligence); EUR 300 to EUR 7,500 (intent) | RGIT Art. 116 |
| Non-filing of DPIVA | EUR 300 to EUR 7,500 | RGIT Art. 116 |
| Late payment of IVA | Juros compensatorios (compensatory interest) at 4% per annum (rate set annually by Portaria) applied from the day after deadline until payment. | LGT Art. 35; CIVA Art. 27(5) |
| Failure to submit SAF-T | EUR 200 to EUR 10,000 | RGIT Art. 117 |
| Failure to issue compliant invoices | EUR 150 to EUR 3,750 per infraction | RGIT Art. 123 |
| IVA fraud (simulacao / faturacao falsa) | Criminal liability -- up to 5 years imprisonment | RGIT Art. 103-104 |

### 6f. Juros Compensatorios (Compensatory Interest) [T1]

**Legislation:** Lei Geral Tributaria (LGT) Art. 35.

| Item | Detail |
|------|--------|
| Rate | 4% per annum (verify annually; set by Portaria) |
| Calculation | Applied daily from the day after the payment deadline until the date of actual payment |
| Formula | `Juros = IVA em divida * (taxa anual / 365) * numero de dias em atraso` |
| Example | EUR 10,000 IVA late by 30 days = EUR 10,000 * (0.04 / 365) * 30 = EUR 32.88 |

---

## Step 7: Reverse Charge (Autoliquidacao)

### 7a. Cross-Border Reverse Charge [T1]

**Legislation:** CIVA Art. 2(1)(e); CIVA Art. 6(6)(a); RITI Art. 21-23.

| Situation | Legal Basis | Treatment |
|-----------|-------------|-----------|
| B2B services received from EU supplier | CIVA Art. 2(1)(e); Art. 6(6)(a) | Self-assess IVA at Portuguese rate. Report base in Campo 16, tax in Campo 17 (output). Claim input per category (Campos 20-25). |
| B2B services received from non-EU supplier | CIVA Art. 2(1)(e); Art. 6(6)(a) | Same as EU -- self-assess at Portuguese rate. Report in Campo 16/17. |
| Intra-Community acquisition of goods | RITI Art. 22 | Self-assess output IVA. Report base in Campo 10/12/13, tax in Campo 11/14/15. Claim input per category (Campos 20-25). |
| Import of goods from non-EU (physical) | CIVA Art. 27(5); Codigo Aduaneiro | IVA collected by Customs (Alfandega) at border via DU (Documento Unico). Recoverable via Campo 20-25 using the DU as supporting document. NOT via reverse charge on DPIVA. |

### 7b. Domestic Reverse Charge [T1]

**Legislation:** CIVA Art. 2(1)(e-j).

| Situation | Legal Basis | Treatment |
|-----------|-------------|-----------|
| Construction services (subcontracting in sector da construcao civil) | CIVA Art. 2(1)(j) | Subcontractor invoices without IVA. Main contractor (adquirente) self-assesses. Invoice must reference Art. 2(1)(j). |
| Scrap metal and waste (sucata e residuos) | CIVA Art. 2(1)(i) | Seller of scrap invoices without IVA. Buyer self-assesses. Annex E of CIVA lists qualifying materials. |
| CO2 emission allowances (licencas de emissao de CO2) | CIVA Art. 2(1)(h) | Seller invoices without IVA. Buyer self-assesses. |
| Gold -- investment gold | CIVA Art. 2(1)(g) | Exempt under CIVA Art. 15 with option to tax. If option exercised, reverse charge applies. |
| Renewable energy certificates (garantias de origem) | CIVA Art. 2(1)(l) | Buyer self-assesses. |

### 7c. Reverse Charge Mechanics [T1]

For all reverse charge scenarios, the mechanics are:

1. Report the net amount in the relevant output/acquisition campo (e.g., Campo 12 for IC acquisition at standard rate).
2. Self-assess output IVA at the applicable Portuguese rate in the corresponding tax campo (e.g., Campo 15).
3. Claim input IVA deduction in the appropriate input campo (Campos 20-25) based on expense category.
4. **Net effect: zero for fully taxable businesses.** CIVA Art. 19(1)(c).
5. For partially exempt businesses, only the pro-rata portion is deductible as input. CIVA Art. 23.

### 7d. Reverse Charge Exceptions [T1]

| Situation | Treatment | Legal Basis |
|-----------|-----------|-------------|
| Out-of-scope items (wages, dividends, bank charges) | NEVER reverse charge | CIVA Art. 1 |
| Local consumption abroad (hotel, restaurant, taxi in foreign country) | NOT reverse charge. Foreign VAT paid at source. Irrecoverable. | CIVA Art. 6(6) -- place of supply exception |
| EU supplier already charged their local VAT | NOT reverse charge. Foreign VAT is embedded in cost. | RITI Art. 22 |
| Art. 53 exempt entity receiving foreign services | Reverse charge APPLIES. Must self-assess and PAY IVA with NO right to deduct. | CIVA Art. 2(1)(e) |

---

## Step 8: SAF-T (PT) Requirements

### 8a. SAF-T Obligation [T1]

**Legislation:** Decreto-Lei 198/2012; Portaria 302/2016 (SAF-T file structure).

| Item | Detail | Legal Basis |
|------|--------|-------------|
| Who must comply | All taxable persons with seat, permanent establishment, or domicile in Portugal who are required to have organised accounting or who voluntarily adopt it | DL 198/2012, Art. 2 |
| What is submitted | SAF-T (PT) file -- XML format containing all invoices, credit notes, and debit notes issued | Portaria 302/2016 |
| Monthly submission | By the 5th of the month following the month of issuance | DL 198/2012, Art. 3 |
| Certified software | Invoicing software must be certified by AT (Autoridade Tributaria). Certification number must appear on all invoices. | DL 28/2019 |
| ATCUD code | All invoices must include a unique ATCUD (Codigo Unico do Documento) code since January 2024 | DL 28/2019; Portaria 195/2020 |
| Retention period | 10 years (minimum retention for tax records in Portugal) | LGT Art. 63-C |

### 8b. SAF-T and DPIVA Cross-Check [T1]

AT performs automated cross-checks between SAF-T data and DPIVA submissions. Discrepancies trigger automatic alerts. Ensure:

- Total output IVA in SAF-T = Campos 2 + 4 + 6 (+ regional campos if applicable) on DPIVA.
- Total taxable base in SAF-T = Campos 1 + 3 + 5 (+ regional campos) on DPIVA.
- Number of documents in SAF-T aligns with reported activity.

---

## Step 9: Edge Case Registry

These are known ambiguous situations and their confirmed resolutions. Each is tagged with its confidence tier.

### EC1 -- EU hotel / restaurant abroad [T1]
**Situation:** Client pays for hotel in Spain. Invoice shows Spanish IVA at 10%.
**Resolution:** NOT reverse charge. Foreign IVA was charged and paid at source. No Portuguese IVA entry on DPIVA. Spanish IVA is an irrecoverable cost embedded in the expense. Expense recorded gross (including Spanish IVA) on P&L.
**Legislation:** CIVA Art. 6(7) -- place of supply for accommodation and restaurant services is where the immovable property is located or where the service is physically performed.

### EC2 -- SaaS subscription from US provider [T1]
**Situation:** US company (e.g., Google, AWS), EUR 100/month, no IVA on invoice.
**Resolution:** Reverse charge applies. Self-assess 23% IVA (EUR 23) as output in Campo 16/17. Claim as input in Campo 24/25 (if overhead) or 20/21 (if capital asset). Net effect = zero for fully taxable business.
**Legislation:** CIVA Art. 2(1)(e); CIVA Art. 6(6)(a).

### EC3 -- Intra-Community acquisition of goods [T1]
**Situation:** French supplier ships goods to Portugal, EUR 5,000, no IVA charged.
**Resolution:** Self-assess 23% output IVA (EUR 1,150). Report Campo 12 = EUR 5,000 (base), Campo 15 = EUR 1,150 (tax). Claim input IVA EUR 1,150 in Campo 22/23 (if stock) or Campo 24/25 (if overhead). Net = zero.
**Legislation:** RITI Art. 22; CIVA Art. 19(1)(c).

### EC4 -- Company car (viatura de turismo) purchase [T1]
**Situation:** Client purchases passenger car EUR 25,000 + EUR 5,750 IVA (23%). Not a taxi or rental company.
**Resolution:** IVA BLOCKED. EUR 5,750 is NOT deductible. No input IVA recovery. The EUR 5,750 becomes part of the cost of the asset.
**Legislation:** CIVA Art. 21(1)(a).

### EC5 -- Art. 53 client receives EU services [T1]
**Situation:** Art. 53 exempt client (regime de isencao) subscribes to German SaaS platform, EUR 50/month.
**Resolution:** Art. 53 entities ARE liable under reverse charge for services from abroad. Must self-assess IVA (23% = EUR 11.50/month) and PAY to AT. NO right to deduct (since Art. 53 does not permit input recovery). Must file a DPIVA for this purpose despite normally being exempt from filing.
**Legislation:** CIVA Art. 2(1)(e); CIVA Art. 53(2).

### EC6 -- Azores/Madeira rate determination [T2]
**Situation:** Client on Continental Portugal sells goods to a customer in the Azores. Goods are shipped to Azores.
**Resolution:** Azores rates apply (16%/9%/4%) because the place of supply for goods is where transport begins if both parties are in Portugal, BUT the rate of the destination region applies per CIVA Art. 18(3). Report in Campos 1A-6A (Azores campos). **Flag for reviewer: confirm destination and applicable rate.**
**Legislation:** CIVA Art. 18(3).

### EC7 -- Credit notes (nota de credito) [T1]
**Situation:** Client issues or receives a credit note relating to a prior sale or purchase.
**Resolution:** Reduce original campo entries accordingly. If issuing a credit note for a sale, reduce the relevant output campo. If receiving a credit note from a supplier, reduce the relevant input campo. Use Campo 40 (regularizacao a favor do sujeito passivo) or Campo 41 (regularizacao a favor do Estado) as appropriate per CIVA Art. 78.
**Legislation:** CIVA Art. 78 (regularizacoes).

### EC8 -- Domestic reverse charge in construction [T1]
**Situation:** Subcontractor provides construction services (e.g., plumbing, electrical work) to a main contractor in the construction sector.
**Resolution:** Subcontractor invoices WITHOUT IVA, citing Art. 2(1)(j) CIVA on the invoice. Main contractor self-assesses IVA at 23% and claims input deduction (net zero). Both parties must be in the construction sector. If the client is the final consumer (not in construction), reverse charge does NOT apply -- subcontractor charges IVA normally.
**Legislation:** CIVA Art. 2(1)(j).

### EC9 -- Export to non-EU country [T1]
**Situation:** Client sells goods to Brazil, EUR 10,000. Goods physically leave Portuguese territory.
**Resolution:** Exempt with right of deduction. Campo 8 = EUR 10,000 (base). No output IVA. All input IVA related to this export is fully deductible. Must retain proof of export (customs documents, DAU/DU).
**Legislation:** CIVA Art. 14(1)(a).

### EC10 -- Regime de isencao threshold boundary [T1]
**Situation:** Art. 53 client's cumulative turnover reaches EUR 14,800 in October. In November, a EUR 300 invoice would push total to EUR 15,100.
**Resolution:** Under the revised Art. 53 (DL 35/2025, effective 1 July 2025), the EUR 15,000 threshold has a 25% tolerance margin (EUR 18,750). If turnover exceeds EUR 15,000 but does NOT exceed EUR 18,750 during the calendar year, the exemption lapses from 1 January of the following year (the client must register for regime normal by then). If turnover exceeds EUR 18,750 during the year, IVA must be charged immediately from the invoice that causes the breach. In this example, EUR 15,100 is above EUR 15,000 but below EUR 18,750, so the client remains Art. 53 exempt for the remainder of the current year and must register for regime normal from 1 January of the following year.
**Legislation:** CIVA Art. 53(1) as amended by DL 35/2025; CIVA Art. 58.

### EC11 -- Tourist VAT refund (Tax Free shopping) [T2]
**Situation:** Non-EU tourist purchases goods in Portugal and requests IVA refund at departure.
**Resolution:** The retailer charges IVA normally. The tourist obtains a Tax Free form from the retailer. At departure from the EU, customs stamps the form. The tourist claims a refund from the refund operator (e.g., Global Blue, Planet). The retailer may subsequently issue a credit note and adjust output IVA via Campo 40 (regularizacao a favor do sujeito passivo). **Flag for reviewer: confirm documentation chain.**
**Legislation:** CIVA Art. 14(1)(b); DL 295/87.

### EC12 -- SAF-T discrepancy with DPIVA [T1]
**Situation:** AT flags a discrepancy between SAF-T monthly submission and DPIVA campo totals.
**Resolution:** Review invoicing system for (a) unsubmitted invoices, (b) timing differences (invoice issued in one month, DPIVA period covers another), (c) credit notes not reflected, (d) manual adjustments. Correct either the SAF-T resubmission or the DPIVA via a declaracao de substituicao (replacement declaration). Penalty risk per RGIT Art. 116-117.
**Legislation:** DL 198/2012; RGIT Art. 116.

### EC13 -- Mixed use asset -- partial deduction [T2]
**Situation:** Client purchases laptop EUR 1,500 + EUR 345 IVA (23%) used 60% for business and 40% personally.
**Resolution:** Only business-use portion is deductible. EUR 345 * 60% = EUR 207 deductible. Report EUR 1,500 in Campo 20, EUR 207 in Campo 21. **Flag for reviewer: confirm business-use percentage and documentation.**
**Legislation:** CIVA Art. 20(1); CIVA Art. 23.

### EC14 -- Diesel fuel for passenger vehicle [T1]
**Situation:** Client fills up diesel for a company passenger car (viatura de turismo). Invoice: EUR 80 net + EUR 18.40 IVA (23%).
**Resolution:** 50% of IVA is deductible. EUR 18.40 * 50% = EUR 9.20 deductible. Report in Campo 24 (base EUR 80), Campo 25 (tax EUR 9.20). The remaining EUR 9.20 is an irrecoverable cost.
**Legislation:** CIVA Art. 21(1)(b).

### EC15 -- Electric vehicle charging for turismo vehicle [T1]
**Situation:** Client charges an electric company car (classified as viatura de turismo). Invoice: EUR 30 net + EUR 6.90 IVA (23%).
**Resolution:** 100% of IVA on electricity for electric vehicles is deductible, even if the vehicle itself is a viatura de turismo. Report in Campo 24 = EUR 30, Campo 25 = EUR 6.90.
**Legislation:** CIVA Art. 21(1)(b) -- electric vehicles excepted from the 50% restriction.

### EC16 -- Triangular operations (operacoes triangulares) [T3]
**Situation:** Portuguese company A buys goods from French company B, instructs B to ship directly to Spanish company C.
**Resolution:** Triangular simplification under RITI Art. 8-10. A acts as intermediary. Report in Campo 100 (informacao complementar). **Escalate to Contabilista Certificado -- complex place of supply and reporting requirements.**
**Legislation:** RITI Art. 8-10.

---

## Step 10: Test Suite

### Test 1 -- Standard domestic purchase, 23% IVA [T1]
**Input:** Portuguese supplier, office supplies, gross EUR 246, IVA EUR 46, net EUR 200. Regime normal client. Continental Portugal.
**Expected output:** Campo 24 = EUR 200 (base), Campo 25 = EUR 46 (input IVA deductible).
**Legislation:** CIVA Art. 19(1)(a).

### Test 2 -- US software subscription, reverse charge [T1]
**Input:** US provider (AWS), EUR 100/month, no IVA on invoice. Regime normal client. Continental.
**Expected output:** Output: Campo 16 = EUR 100, Campo 17 = EUR 23. Input: Campo 24 = EUR 100, Campo 25 = EUR 23. Net IVA effect = zero.
**Legislation:** CIVA Art. 2(1)(e); CIVA Art. 6(6)(a).

### Test 3 -- Intra-Community goods acquisition [T1]
**Input:** German supplier ships goods to Portugal, EUR 5,000, no IVA. Goods are stock for resale. Continental.
**Expected output:** Output: Campo 12 = EUR 5,000, Campo 15 = EUR 1,150 (23%). Input: Campo 22 = EUR 5,000, Campo 23 = EUR 1,150. Net = zero.
**Legislation:** RITI Art. 22; CIVA Art. 19(1)(c).

### Test 4 -- EU B2B sale of goods [T1]
**Input:** Client sells goods to Spanish business EUR 3,000, ships PT to ES. Spanish customer VAT-registered.
**Expected output:** Campo 7 = EUR 3,000. No output IVA. File Declaracao Recapitulativa listing the supply.
**Legislation:** CIVA Art. 14 RITI.

### Test 5 -- Art. 53 client domestic purchase [T1]
**Input:** Art. 53 client (regime de isencao) buys supplies EUR 500 including IVA.
**Expected output:** No DPIVA entry. No IVA recovery. EUR 500 is a full cost on P&L.
**Legislation:** CIVA Art. 53(2).

### Test 6 -- Passenger vehicle purchase, blocked [T1]
**Input:** Client purchases passenger car EUR 25,000 + EUR 5,750 IVA (23%). Client is NOT a taxi/rental company.
**Expected output:** IVA BLOCKED. Campo 21 or 25 = EUR 0 for this item. EUR 5,750 capitalised as part of asset cost.
**Legislation:** CIVA Art. 21(1)(a).

### Test 7 -- EU hotel, local consumption [T1]
**Input:** Client pays hotel in France EUR 300 including French TVA EUR 30.
**Expected output:** No Portuguese IVA entry on DPIVA. French TVA is irrecoverable. Expense = EUR 300 gross.
**Legislation:** CIVA Art. 6(7).

### Test 8 -- Reverse charge services from EU, both sides [T1]
**Input:** Irish company provides legal services EUR 1,000, no IVA. Regime normal client. Continental.
**Expected output:** Output: Campo 16 = EUR 1,000, Campo 17 = EUR 230 (23%). Input: Campo 24 = EUR 1,000, Campo 25 = EUR 230. Net = zero.
**Legislation:** CIVA Art. 2(1)(e); CIVA Art. 6(6)(a).

### Test 9 -- Diesel fuel for passenger vehicle (50% deduction) [T1]
**Input:** Diesel purchase for company car (viatura de turismo). Net EUR 80, IVA EUR 18.40 (23%).
**Expected output:** Campo 24 = EUR 80, Campo 25 = EUR 9.20 (50% of EUR 18.40). Remaining EUR 9.20 is irrecoverable cost.
**Legislation:** CIVA Art. 21(1)(b).

### Test 10 -- Sale in Azores at reduced rate [T2]
**Input:** Seller in Continental Portugal ships goods (Lista I items -- basic foodstuffs) to customer in Azores. Net EUR 500.
**Expected output:** Campo 1A = EUR 500 (Azores reduced rate base), Campo 2A = EUR 20 (4% Azores reduced rate). NOT Campo 1/2 (continental).
**Legislation:** CIVA Art. 18(3); DL Regional 18/2022/A.

### Test 11 -- Export to Brazil [T1]
**Input:** Client exports manufactured goods to Brazil. Net EUR 10,000. Customs documents obtained.
**Expected output:** Campo 8 = EUR 10,000. No output IVA. All input IVA attributable to this export is fully deductible.
**Legislation:** CIVA Art. 14(1)(a).

### Test 12 -- Construction reverse charge (domestic) [T1]
**Input:** Subcontractor invoices main contractor for plumbing work EUR 2,000, no IVA. Both parties in construction sector.
**Expected output:** Main contractor self-assesses. Output IVA = EUR 460 (23%). Input IVA = EUR 460 (in Campo 24/25). Net = zero. Subcontractor's invoice cites Art. 2(1)(j) CIVA.
**Legislation:** CIVA Art. 2(1)(j).

### Test 13 -- Art. 53 client receiving EU services (reverse charge obligation) [T1]
**Input:** Art. 53 exempt client subscribes to German SaaS, EUR 50/month.
**Expected output:** Must file DPIVA. Output: Campo 16 = EUR 50, Campo 17 = EUR 11.50 (23%). Input: EUR 0 (no deduction right under Art. 53). Net IVA payable = EUR 11.50.
**Legislation:** CIVA Art. 2(1)(e); CIVA Art. 53(2).

### Test 14 -- Electric vehicle charging [T1]
**Input:** Electric charging for company turismo EV. Net EUR 30, IVA EUR 6.90 (23%).
**Expected output:** Campo 24 = EUR 30, Campo 25 = EUR 6.90 (100% deductible -- electric fuel exception).
**Legislation:** CIVA Art. 21(1)(b).

---

## Step 11: Comparison with Malta

| Feature | Portugal | Malta | Notes |
|---------|----------|-------|-------|
| **Return name** | Declaracao Periodica de IVA (DPIVA) | VAT3 Form | PT fields called "campos"; MT fields called "boxes" |
| **VAT ID format** | PT + 9 digits | MT + 8 digits | |
| **Standard rate** | 23% (Continental) / 22% (Madeira) / 16% (Azores) | 18% | PT has three regional rate sets; MT has one |
| **Intermediate rate** | 13% / 12% / 9% | 12% and 7% | MT has two intermediate rates; PT has one per region |
| **Reduced rate** | 6% / 4% / 4% | 5% | |
| **Small business exemption** | Regime de isencao -- EUR 15,000 (CIVA Art. 53) | Article 11 -- EUR 35,000 | MT threshold is 2.4x higher |
| **Small business filing** | No DPIVA (unless reverse charge triggered) | Annual 4-box declaration by 15 March | MT requires an annual summary; PT requires nothing (unless foreign services trigger reverse charge) |
| **Filing frequency** | Monthly (>= EUR 650,000) or Quarterly (< EUR 650,000) | Quarterly (Article 10); Monthly (Article 12) | |
| **Monthly DPIVA deadline** | 10th of 2nd month after period | N/A (quarterly: 21st of month after quarter) | PT monthly filers have ~40 days; MT quarterly filers have ~21 days |
| **Quarterly DPIVA deadline** | 15th of 2nd month after quarter | 21st of month after quarter | PT has ~45 days; MT has ~21 days |
| **Capital goods threshold** | No specific campo threshold (capitalisation follows SNC/NCRF) | EUR 1,160 gross (Article 24 VAT Act) | MT has a rigid threshold; PT follows accounting standards |
| **Blocked categories** | CIVA Art. 21: passenger vehicles, entertainment, accommodation/meals, tobacco, luxury/recreational, personal use | 10th Schedule: entertainment, motor vehicles, tobacco, alcohol, art/antiques, pleasure craft, personal use | Broadly similar; PT allows 50% fuel deduction for turismo vehicles; MT blocks fuel with blocked vehicles |
| **Fuel deduction (passenger car)** | 50% for diesel/petrol; 100% for GPL/GNV/electric (CIVA Art. 21(1)(b)) | Blocked if vehicle is blocked (10th Schedule) | Key difference: PT allows partial fuel recovery even on blocked vehicles |
| **Reverse charge -- domestic** | Construction (Art. 2(1)(j)), scrap (Art. 2(1)(i)), CO2 allowances (Art. 2(1)(h)), gold (Art. 2(1)(g)) | No domestic reverse charge (except gold under specific conditions) | PT has broader domestic reverse charge |
| **SAF-T requirement** | Mandatory monthly SAF-T submission + ATCUD on invoices | No SAF-T requirement | Major compliance difference |
| **Regional rate variation** | Three regions with different rates (Continental, Azores, Madeira) | Single rate nationwide | Unique to PT -- no MT equivalent |
| **Tax authority** | Autoridade Tributaria e Aduaneira (AT) | Commissioner for Revenue (CFR) | |
| **Filing portal** | Portal das Financas | CFR VAT Online | |
| **Penalty for late filing** | EUR 150 - EUR 3,750 (negligence) / EUR 300 - EUR 7,500 (intent) | Varies; generally EUR 50-500 per return | PT penalties significantly higher |
| **Interest on late payment** | Juros compensatorios at 4% p.a. | 0.33% per month (4% p.a.) | Similar effective rate |
| **VAT groups** | Available from July 2026 (new regime) | Available | PT regime is new |
| **Pro-rata** | CIVA Art. 23 -- rounded up to nearest integer | Article 22(4) -- standard formula | Similar methodology |

---

## Step 12: Reviewer Escalation Protocol

When Claude identifies a [T2] situation, output the following structured flag before proceeding:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment Claude considers most likely correct and why]
Action Required: Contabilista Certificado must confirm before filing.
```

When Claude identifies a [T3] situation, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to Contabilista Certificado. Document gap.
```

---

## Step 13: Out of Scope -- Direct Tax [T3]

This skill does not compute income tax. The following is reference information only. Do not execute any of these rules. Escalate to Contabilista Certificado.

- **IRS (Imposto sobre o Rendimento das Pessoas Singulares):** Progressive rates 14.5% to 48% + taxa adicional de solidariedade (2.5% on income > EUR 80,000; 5% on income > EUR 250,000). Codigo do IRS -- DL 442-A/88.
- **IRC (Imposto sobre o Rendimento das Pessoas Coletivas):** 21% standard rate; 17% on first EUR 50,000 for PMEs (small/medium enterprises). Codigo do IRC -- DL 442-B/88.
- **Seguranca Social (TSU):** Separate obligation. Employer: 23.75%. Employee: 11%. Self-employed: 21.4% (regime simplificado). Codigo dos Regimes Contributivos do Sistema Previdencial -- Lei 110/2009.
- **Derrama municipal:** Municipal surcharge up to 1.5% on IRC taxable income. Lei 73/2013.
- **Derrama estadual:** State surcharge: 3% (EUR 1.5M-7.5M), 5% (EUR 7.5M-35M), 9% (> EUR 35M). CIRC Art. 87-A.

---

## PROHIBITIONS [T1]

- NEVER let AI guess campos -- they are 100% deterministic from the facts (region, rate, category). CIVA Art. 41.
- NEVER apply Art. 53 exemption if turnover threshold was exceeded in the prior year. CIVA Art. 53(1).
- NEVER allow Art. 53 clients to recover input IVA. CIVA Art. 53(2).
- NEVER apply reverse charge to out-of-scope categories (salaries, loan repayments, dividends, bank charges). CIVA Art. 1.
- NEVER apply reverse charge to local consumption abroad (hotel, restaurant, taxi consumed in another country). CIVA Art. 6(7).
- NEVER recover IVA on passenger vehicles (viaturas de turismo) unless exclusive business use is proven and falls within CIVA Art. 21(2) exceptions. CIVA Art. 21(1)(a).
- NEVER recover IVA on entertainment expenses (despesas de representacao). CIVA Art. 21(1)(c).
- NEVER apply continental rates to Azores/Madeira transactions -- always verify the destination region and use the correct rate table. CIVA Art. 18(3).
- NEVER apply Azores rates to Madeira transactions or vice versa. CIVA Art. 18(3).
- NEVER apply more than 50% deduction on diesel/petrol for viaturas de turismo. CIVA Art. 21(1)(b).
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude.
- NEVER file a DPIVA without ensuring SAF-T monthly submission is up to date. DL 198/2012.
- NEVER confuse exempt with right of deduction (Campo 7, 8, 9A) with exempt without right of deduction (Campo 9). CIVA Art. 14 vs. Art. 9.
- NEVER ignore the ATCUD requirement on invoices since January 2024. DL 28/2019.
- NEVER allow domestic construction reverse charge when the customer is a final consumer (not in the construction sector). CIVA Art. 2(1)(j).
- NEVER process imports of physical goods from non-EU via reverse charge on DPIVA -- these are handled by Customs (Alfandega) via the DU document. CIVA Art. 27(5).

---

## Contribution Notes

All legislation references, campo numbers, thresholds, rate tables, and blocked categories are specific to Portugal (Continental, Madeira, and Azores). Regional rates (Azores and Madeira) are based on the latest Decretos Legislativos Regionais and have been cross-referenced with PWC Tax Summaries (Portugal -- Other Taxes) as of 2025.

**A skill may not be published without sign-off from a Contabilista Certificado in Portugal.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
