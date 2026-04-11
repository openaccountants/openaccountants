---
name: br-indirect-tax
description: Use this skill whenever asked about Brazilian indirect tax obligations (ICMS, ISS, IPI) for self-employed individuals or small businesses. Trigger on phrases like "ICMS", "ISS", "IPI", "Brazil VAT", "Brazilian indirect tax", "nota fiscal", "imposto sobre servicos", "imposto sobre circulacao de mercadorias", or any question about indirect tax computation or compliance in Brazil. Covers ISS (municipal, 2-5%), ICMS (state, variable), IPI (federal), interaction with Simples Nacional, and the upcoming IBS/CBS tax reform. ALWAYS read this skill before touching any Brazilian indirect tax work.
---

# Brazil Indirect Tax (ICMS/ISS/IPI) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Brazil |
| Jurisdiction Code | BR |
| Primary Legislation | LC 87/1996 (Lei Kandir -- ICMS); LC 116/2003 (ISS); Decreto 7.212/2010 (RIPI -- IPI) |
| Supporting Legislation | CF/88 Art. 155-156; LC 123/2006 (Simples Nacional); EC 132/2023 (Tax Reform) |
| Tax Authority | State SEFAZ (ICMS); Municipal prefeitura (ISS); Receita Federal (IPI) |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by a Brazilian contador (CRC-registered) |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Tax Year | 2025 |
| Confidence Coverage | Tier 1: ISS rate range, ICMS structure, IPI basic rules, Simples interaction. Tier 2: ICMS ST, interstate rate differentials, ISS location of service rules. Tier 3: tax reform transition (IBS/CBS), tax wars (guerra fiscal), ICMS credits complex chains. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified professional must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before advising on indirect tax, you MUST know:

1. **Tax regime** [T1] -- Simples Nacional, Lucro Presumido, or Lucro Real
2. **Activity type** [T1] -- services (ISS), goods (ICMS), or manufacturing (IPI)
3. **CNAE code(s)** [T1] -- determines applicable tax and rates
4. **State and municipality of registration** [T1] -- ICMS rates vary by state; ISS rates by municipality
5. **Whether selling interstate** [T2] -- different ICMS rates for interstate operations
6. **Whether importing** [T2] -- ICMS on imports, IPI on imported goods
7. **Whether on Simples Nacional** [T1] -- indirect taxes are generally included in DAS

**If on Simples Nacional and below the R$ 3,600,000 sublimit, ICMS and ISS are included in the DAS. This skill's detailed computation applies primarily to businesses OUTSIDE Simples or those exceeding the sublimit.**

---

## Step 1: ISS (Imposto Sobre Servicos) [T1]

**Legislation:** LC 116/2003; municipal legislation

### Overview [T1]

| Feature | Detail |
|---------|--------|
| Level | Municipal |
| Applies to | Services (as listed in the LC 116/2003 service list) |
| Rate range | **2% to 5%** (set by each municipality) |
| Minimum rate | 2% (LC 157/2016) |
| Base | Gross price of the service |

### ISS Rate Examples [T1]

| Municipality | Common ISS Rate |
|-------------|----------------|
| Sao Paulo | 2% to 5% (varies by service type; IT services typically 2-3%) |
| Rio de Janeiro | 2% to 5% |
| Belo Horizonte | 2% to 5% |
| Most municipalities | Default 5% unless reduced by specific municipal law |

### Location of Taxation [T1/T2]

| Rule | Where ISS is Due |
|------|-----------------|
| General rule | Municipality where the service provider is established |
| Exceptions (LC 116/2003, Art. 3) | Certain services taxed where performed (construction, cleaning, security, events, etc.) |

[T2] Flag for reviewer when services are performed in a municipality different from the provider's registration.

### ISS Computation [T1]

ISS = Gross service revenue x Municipal ISS rate

---

## Step 2: ICMS (Imposto sobre Circulacao de Mercadorias e Servicos) [T1/T2]

**Legislation:** LC 87/1996 (Lei Kandir); state RICMS regulations

### Overview [T1]

| Feature | Detail |
|---------|--------|
| Level | State |
| Applies to | Sale of goods, interstate/inter-municipal transport, telecommunications |
| Non-cumulative | Credit for ICMS paid on inputs (outside Simples) |
| Rate | Varies by state and product |

### Internal ICMS Rates (Intrastate) [T1]

| State | Standard Rate |
|-------|--------------|
| Sao Paulo | 18% |
| Rio de Janeiro | 20% (increased from 18% + FECP 2%) |
| Minas Gerais | 18% |
| Parana | 19% |
| Rio Grande do Sul | 17% |
| Most states | 17-20% |

### Interstate ICMS Rates [T1]

| Origin / Destination | Rate |
|---------------------|------|
| South/Southeast to South/Southeast | 12% |
| South/Southeast to North/Northeast/Center-West/ES | 7% |
| North/Northeast/Center-West/ES to any state | 12% |
| Imported goods (any interstate) | 4% (Resolucao SF 13/2012) |

### DIFAL (Diferencial de Aliquota) [T2]

When selling to a non-taxpayer consumer in another state, DIFAL applies:
- DIFAL = Internal rate of destination state - Interstate rate
- Seller collects and remits DIFAL to destination state
- [T2] Flag for reviewer on DIFAL calculations

### ICMS-ST (Substituicao Tributaria) [T2]

| Rule | Detail |
|------|--------|
| What | ICMS collected upfront by the manufacturer/importer for the entire chain |
| When | Specific product categories (beverages, fuels, auto parts, electronics, etc.) |
| How | MVA (Margem de Valor Agregado) applied to calculate presumed final price |

[T2] Always flag ICMS-ST situations for reviewer -- computation is complex and product-specific.

---

## Step 3: IPI (Imposto sobre Produtos Industrializados) [T1]

**Legislation:** Decreto 7.212/2010 (RIPI); TIPI (Tabela de Incidencia do IPI)

### Overview [T1]

| Feature | Detail |
|---------|--------|
| Level | Federal |
| Applies to | Industrialized products (manufacturing, transformation, assembly) |
| Non-cumulative | Credit for IPI on inputs |
| Rate | Varies by product (TIPI table, based on NCM code) -- 0% to 30%+ |
| Exemptions | Products listed in TIPI with rate 0% or NT (non-taxable) |

### Who Pays [T1]

| Situation | IPI Obligation |
|-----------|---------------|
| Manufacturer | Yes -- on sale of manufactured goods |
| Importer | Yes -- on customs clearance |
| Service provider | No -- IPI does not apply to services |
| Retailer | Generally no (unless performing industrialization) |

### IPI for Self-Employed [T1]

Most self-employed service providers do NOT pay IPI. IPI applies only if the self-employed person manufactures or transforms products. If on Simples Nacional, IPI is included in the DAS (Anexo II for industry).

---

## Step 4: Simples Nacional Interaction [T1]

**Legislation:** LC 123/2006, Art. 13, 18

| Tax | Treatment in Simples |
|-----|---------------------|
| ISS | Included in DAS (Anexos III, IV, V) |
| ICMS | Included in DAS (Anexos I, II) |
| IPI | Included in DAS (Anexo II) |
| Exception | If revenue > R$ 3,600,000 sublimit, ICMS and ISS are paid OUTSIDE Simples at normal rates |

### When Indirect Tax Applies Separately (Even in Simples) [T1]

| Situation | Tax Treatment |
|-----------|--------------|
| Revenue exceeds R$ 3,600,000 sublimit | ICMS/ISS paid at normal state/municipal rates |
| ICMS-ST products | ICMS-ST is paid separately even in Simples |
| ICMS on imports | Paid separately at customs |
| DIFAL on interstate B2C | May apply depending on state agreement |

---

## Step 5: Nota Fiscal (Tax Invoice) [T1]

### Types [T1]

| Type | Use |
|------|-----|
| NF-e (Nota Fiscal Eletronica) | Sale of goods (ICMS) |
| NFS-e (Nota Fiscal de Servicos Eletronica) | Services (ISS) |
| NFC-e (Nota Fiscal de Consumidor Eletronica) | Retail to final consumer |
| CT-e | Transport services |

### NFS-e for Service Providers [T1]

| Requirement | Detail |
|-------------|--------|
| Issuance | Via municipal portal (each city has its own system) |
| Mandatory fields | Provider CNPJ, client CNPJ/CPF, service code, value, ISS rate, ISS amount |
| Retention | ISS may be retained by the client (ISS retido na fonte) for certain services |

---

## Step 6: Tax Reform -- IBS and CBS [T3]

**Legislation:** Emenda Constitucional 132/2023; LC pending (2025-2026)

| Detail | Value |
|--------|-------|
| What | Brazil is replacing ICMS, ISS, IPI, PIS, and COFINS with two new taxes: IBS (state/municipal) and CBS (federal) |
| Timeline | Transition period 2026-2032; full implementation by 2033 |
| Combined rate | Expected ~26.5% (among highest globally) |
| Current status | Implementation laws being debated/enacted through 2025-2026 |

[T3] ESCALATE all tax reform transition questions. The rules are not yet finalized for full implementation.

---

## Step 7: Edge Case Registry

### EC1 -- ISS retained at source [T1]
**Situation:** IT consulting firm invoices a large company. Client retains ISS.
**Resolution:** Certain services are subject to ISS retention at source (ISS retido). The client deducts ISS from payment and remits to the municipality. The service provider shows ISS retido on the NFS-e and does not pay ISS separately on that invoice.

### EC2 -- Simples Nacional exceeding sublimit [T2]
**Situation:** EPP with R$ 4,000,000 revenue (above R$ 3,600,000 sublimit).
**Resolution:** Federal taxes remain in Simples DAS. ICMS and ISS are calculated and paid OUTSIDE Simples at normal state/municipal rates. [T2] Significant complexity increase -- flag for contador.

### EC3 -- Interstate sale from Simples Nacional [T1]
**Situation:** Simples Nacional company in SP sells goods to customer in BA.
**Resolution:** ICMS is included in Simples DAS at the Simples rate. The buyer in BA may not be able to take full ICMS credit (limited to the ICMS portion within the Simples rate). DIFAL may apply if selling to non-taxpayer consumer.

### EC4 -- Service provider also sells goods [T2]
**Situation:** IT company provides consulting (ISS) and sells software licenses (ICMS or ISS depending on classification).
**Resolution:** Software classification is contentious. SaaS/cloud services are generally ISS. Packaged software was historically ICMS but increasingly ISS. [T2] Flag for reviewer -- must check state and municipal legislation.

### EC5 -- IPI on artisanal manufacturing [T1]
**Situation:** Self-employed person makes and sells handmade goods.
**Resolution:** If registered as industry (CNAE indicates manufacturing), IPI applies. If on Simples Nacional (Anexo II), IPI is included in DAS. If outside Simples, must register as industrial establishment and file IPI returns (DCTF).

---

## Step 8: Test Suite

### Test 1 -- ISS computation (outside Simples)
**Input:** Consulting firm in Sao Paulo. Monthly service revenue R$ 50,000. ISS rate 5%.
**Expected output:**
- ISS = R$ 50,000 x 5% = R$ 2,500

### Test 2 -- ICMS computation (outside Simples, intrastate SP)
**Input:** Retailer in SP selling goods worth R$ 100,000 (before ICMS). Internal rate 18%.
**Expected output:**
- ICMS on sales: R$ 100,000 x 18% = R$ 18,000
- Less: ICMS credits on purchases (e.g., R$ 60,000 purchases x 18% = R$ 10,800)
- ICMS payable: R$ 18,000 - R$ 10,800 = R$ 7,200

### Test 3 -- Simples Nacional with ISS included
**Input:** IT services company on Simples, Anexo III, RBT12 = R$ 300,000, monthly revenue R$ 28,000.
**Expected output:**
- Band 2: effective rate = (300,000 x 11.20% - 9,360) / 300,000 = 8.08%
- DAS = 28,000 x 8.08% = R$ 2,262.40 (includes ISS, IRPJ, CSLL, PIS, COFINS, CPP)

### Test 4 -- Interstate sale (SP to BA)
**Input:** SP company sells R$ 10,000 goods to BA company. Interstate rate 7%. BA internal rate 19%.
**Expected output:**
- ICMS charged: R$ 10,000 x 7% = R$ 700 (seller pays to SP SEFAZ)
- DIFAL (if B2B, buyer is taxpayer): buyer pays DIFAL of 12% (19% - 7%) to BA
- If B2C: seller collects DIFAL of 12% and remits to BA

### Test 5 -- ISS retention at source
**Input:** Consulting invoice R$ 20,000 to large corporate client. ISS rate 5%. Subject to retention.
**Expected output:**
- ISS = R$ 20,000 x 5% = R$ 1,000
- Client retains R$ 1,000 and remits to municipality
- Provider receives R$ 19,000
- Provider does not pay ISS separately on this invoice

---

## PROHIBITIONS

- NEVER apply ICMS to pure services -- services are subject to ISS (except telecom and interstate transport)
- NEVER apply ISS to sale of physical goods -- goods are subject to ICMS
- NEVER ignore the R$ 3,600,000 sublimit for Simples Nacional ICMS/ISS
- NEVER assume ICMS rates are uniform across states -- they vary from 7% to 25%+ depending on state and product
- NEVER assume ISS rates are the same in all municipalities -- they range from 2% to 5%
- NEVER compute IPI for pure service providers -- IPI applies only to industrialized products
- NEVER ignore ICMS-ST obligations -- they apply even to Simples Nacional companies for listed products
- NEVER advise on the IBS/CBS tax reform as if it is fully enacted -- transition rules are still being finalized [T3]
- NEVER present calculations as definitive -- always label as estimated and direct client to a CRC-registered contador

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CRC-registered contador or equivalent licensed practitioner in Brazil) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
