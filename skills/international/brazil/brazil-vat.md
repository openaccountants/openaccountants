---
name: brazil-vat
description: Use this skill whenever asked about Brazilian indirect taxes, VAT, consumption taxes, PIS, COFINS, ICMS, ISS, IPI, CBS, IBS, Imposto Seletivo, NF-e (Nota Fiscal Eletronica), Simples Nacional, CNPJ registration, tax reform (EC 132/2023), ICMS substituicao tributaria, Manaus Free Trade Zone (ZFM), interstate operations, guerra fiscal, or any request involving Brazilian goods and services taxation, filing, compliance, or classification. Trigger on phrases like "Brazil tax", "Brazilian VAT", "PIS/COFINS", "ICMS", "ISS", "IPI", "CBS", "IBS", "Imposto Seletivo", "NF-e", "nota fiscal", "Simples Nacional", "CNPJ", "tax reform Brazil", "EC 132", "substituicao tributaria", "ICMS-ST", "ZFM", "Manaus", "guerra fiscal", or any request involving Brazilian indirect tax compliance, rates, filing, or classification. This skill contains the complete Brazilian indirect tax framework covering both the current multi-tax system (PIS/COFINS/ICMS/ISS/IPI) and the new unified system (CBS/IBS/IS) under Constitutional Amendment 132/2023, including transition timeline 2026-2033, NF-e e-invoicing, Simples Nacional, interstate ICMS matrix, registration, filing obligations, edge cases, and comparison with EU VAT. ALWAYS read this skill before touching any Brazilian indirect tax work.
---

# Brazil Indirect Tax / VAT Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Federative Republic of Brazil (Republica Federativa do Brasil) |
| Jurisdiction Code | BR |
| Tax Type | Indirect / Consumption Taxes (multi-layer: federal, state, municipal) |
| Primary Legal Framework (Current) | Constituicao Federal Art. 153-156; Lei Complementar 87/1996 (ICMS); Lei 10.637/2002 (PIS); Lei 10.833/2003 (COFINS); Decreto 7.212/2010 (IPI); Lei Complementar 116/2003 (ISS) |
| Primary Legal Framework (New) | Emenda Constitucional 132/2023 (EC 132/2023); Lei Complementar 214/2025 (CBS/IBS/IS regulation) |
| Governing Bodies | Receita Federal do Brasil (RFB) -- federal taxes; State Secretarias de Fazenda (SEFAZ) -- ICMS; Municipal Secretarias de Financas -- ISS; Comite Gestor do IBS (new) |
| Currency | Brazilian Real (BRL) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Deep research verification, April 2026 |
| Validation Date | 2026-04-10 |
| Skill Version | 2.0 |
| Confidence Coverage | Tier 1: current system rate lookups, PIS/COFINS regimes, ICMS interstate matrix, NF-e basics, CNPJ format, Simples Nacional thresholds. Tier 2: new CBS/IBS/IS system (reform ongoing), transition timeline rates, ICMS-ST calculations, ZFM incentives, digital services classification. Tier 3: audit defence, transfer pricing interaction, state-specific ICMS incentives litigation, complex ICMS-ST margins, penalty abatement. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed Brazilian accountant (Contador CRC) or tax attorney must confirm before filing. Rules related to the new CBS/IBS/IS system are tagged [T2] because the reform is still being implemented and regulations are evolving.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to a licensed Brazilian tax professional and document the gap.

---

## Step 0: Client Onboarding Questions

Before performing ANY Brazilian indirect tax work, collect the following information. Do not proceed until all mandatory fields are answered.

### Mandatory Questions [T1]

1. **Corporate income tax regime:** Is the company taxed under Lucro Real, Lucro Presumido, or Simples Nacional? (Determines PIS/COFINS regime and filing obligations.)
2. **CNPJ and branch structure:** What is the company's CNPJ? Does it have branches (filiais) in other states?
3. **State(s) of operation:** In which states does the company have Inscricao Estadual (IE)?
4. **Municipality of headquarters:** Where is the company's sede (for ISS purposes)?
5. **Primary activity:** Goods (ICMS), services (ISS), manufacturing (IPI), or mixed?
6. **NCM codes (if goods):** What are the primary NCM codes of products sold? (Required for ICMS rate, IPI rate, and ICMS-ST determination.)
7. **Annual gross revenue (trailing 12 months):** Required to determine Simples Nacional eligibility and rate band.
8. **Transaction direction:** Internal (within one state), interstate, import, export, or combination?
9. **Customer type:** B2B (taxpayer) or B2C (final consumer)? (Affects DIFAL calculation.)
10. **Period under review:** Which tax year/month? (Critical for transition period -- 2025 current system only; 2026+ dual system.)

### Conditional Questions [T1]

11. **If Simples Nacional:** Has the company opted to pay CBS/IBS outside the DAS? (Affects customer credit entitlement from 2026.)
12. **If manufacturing:** Does the company operate in the Zona Franca de Manaus (ZFM)? If yes, does the product have valid PPB (Processo Produtivo Basico)?
13. **If interstate goods:** Does the product have imported content exceeding 40%? (4% interstate ICMS rule.)
14. **If ICMS-ST applicable:** What are the applicable CONFAZ protocols and current MVA percentages for the product/state pair?
15. **If importing services:** From which country? (Determines IRRF rate -- 15% standard or 25% tax haven.)
16. **If 2026-2028 period:** Is the company's NF-e/NFS-e system updated to include CBS/IBS fields?

---

## Step 1: Transaction Classification Rules

### 1.1 Brazil's Multi-Layer Indirect Tax System [T1]

Brazil does **not** have a single unified VAT like the EU. It has a **fragmented system** of five major indirect taxes levied at three levels of government. Key facts:

- **Three levels of government** impose consumption taxes: federal, state (26 states + Distrito Federal), and municipal (~5,570 municipalities). [T1]
- **Five principal indirect taxes** exist in the current system (operational until full transition by 2033). [T1]
- Brazil is undergoing a **historic tax reform** via Constitutional Amendment 132/2023 (EC 132/2023), replacing the five taxes with a dual VAT (CBS + IBS) plus a selective excise tax (IS). [T2]
- The transition runs from **2026 through 2032**, with full phase-out of old taxes by 1 January 2033. [T2]

**Source:** Constituicao Federal, Art. 153 (IPI, PIS, COFINS), Art. 155 (ICMS), Art. 156 (ISS); EC 132/2023.

### 1.2 Classification Decision Tree [T1]

```
START
  |
  +-- Is the supply GOODS or SERVICES?
  |     |
  |     +-- GOODS:
  |     |     +-- Is it manufactured/imported by the seller? --> IPI applies (check TIPI table)
  |     |     +-- Is it sold domestically? --> ICMS applies (check state rate + interstate rules)
  |     |     +-- Is it exported? --> ICMS exempt, IPI exempt, PIS/COFINS zero-rated
  |     |     +-- PIS + COFINS always apply (check cumulative vs. non-cumulative regime)
  |     |     +-- Is ICMS-ST applicable? --> Check CONFAZ protocols for product + state pair
  |     |
  |     +-- SERVICES:
  |           +-- Is the service on the LC 116/2003 list? --> ISS applies (2-5%)
  |           +-- Is it transport/communication? --> ICMS applies (not ISS)
  |           +-- Is it exported (result occurs abroad)? --> ISS exempt
  |           +-- PIS + COFINS always apply (check regime)
  |
  +-- Is the supply IMPORTED?
  |     +-- Goods: II + IPI + PIS-Import + COFINS-Import + ICMS-Import
  |     +-- Services: PIS-Import + COFINS-Import + ISS-Import + IRRF + IOF + possibly CIDE
  |
  +-- Is this 2026 or later?
        +-- YES: Add CBS (0.9% in 2026) + IBS (0.1% in 2026) on invoice [T2]
        +-- 2027: CBS replaces PIS/COFINS; ICMS/ISS still full rate [T2]
        +-- 2029+: IBS begins replacing ICMS/ISS at increasing rates [T2]
```

### 1.3 The Five Current Indirect Taxes [T1]

| Tax | Full Name | Level | Base | Typical Rate |
|-----|-----------|-------|------|-------------|
| PIS | Programa de Integracao Social | Federal | Revenue/imports | 1.65% (non-cumulative) / 0.65% (cumulative) |
| COFINS | Contribuicao para o Financiamento da Seguridade Social | Federal | Revenue/imports | 7.6% (non-cumulative) / 3% (cumulative) |
| ICMS | Imposto sobre Circulacao de Mercadorias e Servicos | State | Goods + interstate/intercity transport + communications | 17-23% (internal); 4%, 7% or 12% (interstate) |
| ISS | Imposto sobre Servicos de Qualquer Natureza | Municipal | Services | 2-5% |
| IPI | Imposto sobre Produtos Industrializados | Federal | Manufactured/imported goods | 0-300%+ (product-specific via TIPI table) |

### 1.4 PIS/COFINS Regime Classification [T1]

**Cumulative Regime** (Lei 9.718/1998): [T1]
- Applies to companies taxed under **Lucro Presumido** (presumed profit).
- PIS: **0.65%** on gross revenue.
- COFINS: **3%** on gross revenue.
- Combined: **3.65%**.
- **No input credits allowed.** Tax cascades through the supply chain.
- Base = gross revenue, with limited exclusions (ICMS excluded per STF RE 574.706).

**Non-Cumulative Regime** (Lei 10.637/2002 for PIS; Lei 10.833/2003 for COFINS): [T1]
- Applies to companies taxed under **Lucro Real** (actual profit).
- PIS: **1.65%** on gross revenue.
- COFINS: **7.6%** on gross revenue.
- Combined: **9.25%**.
- **Input credits allowed** on purchases of goods for resale, inputs to manufacturing, electricity, rent, depreciation of fixed assets, and other specified items.
- Effectively a **subtraction-method VAT** (credit/debit mechanism).

**Source:** Lei 10.637/2002, Art. 1-3 (PIS non-cumulative); Lei 10.833/2003, Art. 1-3 (COFINS non-cumulative).

### 1.5 PIS/COFINS on Imports [T1]

- PIS-Importacao: **2.1%** on the customs value + ICMS + PIS/COFINS themselves (grossed-up base).
- COFINS-Importacao: **9.65%** (general) or **10.65%** for certain goods (additional 1% surcharge per Lei 12.844/2013).
- Import PIS/COFINS generates input credits under the non-cumulative regime.

### 1.6 Key PIS/COFINS Exemptions and Reduced Rates [T1]

- Basic food basket items (cesta basica): reduced to zero rate in many cases.
- Exports: zero-rated (PIS/COFINS rate of 0% with credit maintenance).
- Revenue from equity method investments: excluded from the base.
- Certain inputs for agriculture and agroindustry: suspended or zero-rated.

### 1.7 ISS (Municipal Services Tax) [T1]

ISS is a municipal tax on services listed in **Lei Complementar 116/2003** (~200 service items across 40 sub-items).

**Key rules:** [T1]
- Rate: **minimum 2%, maximum 5%**, set by each municipality.
- ISS and ICMS are **mutually exclusive** -- a transaction is subject to one or the other, never both (except for mixed supply scenarios where the goods component bears ICMS and the services component bears ISS).
- ISS is generally due at the **location of the service provider** (sede do prestador), except for ~20 specific service categories where ISS is due at the location of the service provision (e.g., construction, security, cleaning).
- Exports of services are **exempt** from ISS (the result of the service must occur abroad, per LC 116/2003, Art. 2, I).

### 1.8 ISS on Digital Services [T2]

- Software licensing: STF ruled in ADIs 1.945 and 5.659 that software (whether customised or standardised) is subject to **ISS**, not ICMS.
- SaaS, cloud services, and digital platforms are subject to ISS under item 1.05 (licensing/sublicensing of software) or other applicable items.
- Municipal variation in ISS rates for technology services creates planning opportunities but also compliance complexity. [T2]

### 1.9 IPI (Federal Excise) [T1]

IPI is a federal excise tax on manufactured and imported products operating on a credit/debit basis.

**Key rules:** [T1]
- Rates are set per product in the **TIPI table** based on NCM codes.
- Rates range from **0% to over 300%** (cigarettes at the high end).
- IPI is charged **outside the price** (por fora) -- added on top of the sale price, unlike ICMS.
- IPI generates credits on inputs used in manufacturing.
- Exports are **exempt** with credit maintenance.
- IPI is **not charged** on resale by commercial establishments (only on industrialisation or import).

### 1.10 IPI and the Manaus Free Trade Zone (ZFM) [T1]

- Products manufactured in the Zona Franca de Manaus (ZFM) benefit from **IPI exemption** on domestic sales and exports.
- The ZFM incentives are constitutionally guaranteed until **2073** (ADCT Art. 40, extended by EC 83/2014).
- These incentives are **preserved** under the new CBS/IBS system per EC 132/2023. [T2]

---

## Step 2: Box/Line Assignment -- Deterministic Lookup Tables

### 2.1 ICMS Internal Rates by State (General Merchandise Rate) [T1]

| State | Code | General Rate |
|-------|------|-------------|
| Acre | AC | 19% |
| Alagoas | AL | 19% |
| Amapa | AP | 18% |
| Amazonas | AM | 20% |
| Bahia | BA | 20.5% |
| Ceara | CE | 20% |
| Distrito Federal | DF | 20% |
| Espirito Santo | ES | 17% |
| Goias | GO | 19% |
| Maranhao | MA | 23% |
| Mato Grosso | MT | 17% |
| Mato Grosso do Sul | MS | 17% |
| Minas Gerais | MG | 18% |
| Para | PA | 19% |
| Paraiba | PB | 20% |
| Parana | PR | 19.5% |
| Pernambuco | PE | 20.5% |
| Piaui | PI | 22.5% |
| Rio de Janeiro | RJ | 20% |
| Rio Grande do Norte | RN | 18% |
| Rio Grande do Sul | RS | 17% |
| Rondonia | RO | 19.5% |
| Roraima | RR | 20% |
| Santa Catarina | SC | 17% |
| Sao Paulo | SP | 18% |
| Sergipe | SE | 19% |
| Tocantins | TO | 20% |

**Note:** Many states apply higher rates to specific categories (fuel, telecommunications, electricity, alcoholic beverages) and lower rates to essentials. The above are general merchandise rates as of 2025-2026. Maranhao increased from 22% to 23% and Piaui increased from 21% to 22.5% effective 2025. [T1]

### 2.2 Interstate ICMS Rates Matrix [T1]

| Origin \ Destination | South + Southeast (MG, PR, RJ, RS, SC, SP, ES) | North + Northeast + Centre-West + DF |
|----------------------|------------------------------------------------|---------------------------------------|
| South + Southeast (except ES) | **12%** | **7%** |
| Espirito Santo | **12%** | **7%** |
| North + Northeast + Centre-West + DF | **12%** | **12%** |

**Imported goods rule:** For goods with imported content exceeding 40%, the interstate rate is **4%** regardless of origin/destination (Resolucao do Senado Federal 13/2012). [T1]

### 2.3 DIFAL (Diferencial de Aliquota) [T1]

When goods are sold interstate to a non-taxpayer (final consumer), the destination state collects the difference between its internal rate and the applicable interstate rate. Regulated by EC 87/2015 and Lei Complementar 190/2022. [T1]

### 2.4 ICMS Nature: Por Dentro Calculation [T1]

ICMS is applied **inside the price** (por dentro) -- the ICMS rate is applied to a base that includes the ICMS itself. A nominal 18% rate effectively means ~21.95% on the tax-exclusive price. [T1]

**Source:** Constituicao Federal Art. 155, II; Lei Complementar 87/1996 (Lei Kandir).

### 2.5 PIS/COFINS Rate Lookup Table [T1]

| Regime | PIS Rate | COFINS Rate | Combined | Input Credits? |
|--------|----------|-------------|----------|----------------|
| Cumulative (Lucro Presumido) | 0.65% | 3.00% | 3.65% | No |
| Non-Cumulative (Lucro Real) | 1.65% | 7.60% | 9.25% | Yes |
| Import (Goods) | 2.10% | 9.65% | 11.75% | Yes (non-cumulative) |
| Import (Goods, surcharge items) | 2.10% | 10.65% | 12.75% | Yes (non-cumulative) |
| Import (Services) | 1.65% | 7.60% | 9.25% | Yes (non-cumulative) |
| Export | 0% | 0% | 0% | Credits maintained |

### 2.6 ISS Rate Range [T1]

| Parameter | Value |
|-----------|-------|
| Minimum rate | 2% |
| Maximum rate | 5% |
| Set by | Each municipality individually |
| Legal basis | LC 116/2003 |

### 2.7 New System Tax Lookup (CBS/IBS/IS) [T2]

| Tax | Full Name | Level | Replaces | Estimated Rate |
|-----|-----------|-------|----------|----------------|
| CBS | Contribuicao sobre Bens e Servicos | Federal | PIS + COFINS | ~8.8% |
| IBS | Imposto sobre Bens e Servicos | State + Municipal | ICMS + ISS | ~17.7% |
| IS | Imposto Seletivo | Federal | Partially IPI (harmful goods only) | Varies by product |
| **Combined CBS+IBS** | | | | **~26.5% (estimated, not final)** |

### 2.8 Reduced Rate Categories (New System) [T2]

| Category | Reduction | Effective Rate (approx.) |
|----------|-----------|------------------------|
| Health services and medical devices | 60% | ~10.6% |
| Education services | 60% | ~10.6% |
| Urban, semi-urban, metropolitan public transport | 60% | ~10.6% |
| Agricultural and livestock inputs | 60% | ~10.6% |
| National security and sovereignty items | 60% | ~10.6% |
| Personal hygiene and cleaning products (cesta basica ampliada) | 60% | ~10.6% |
| Cultural and artistic activities | 60% | ~10.6% |
| Core basic food basket (cesta basica nacional) | 100% (exempt) | 0% |
| Medical devices for persons with disabilities | 100% (exempt) | 0% |
| PROUNI-eligible higher education institutions | 100% (exempt) | 0% |

### 2.9 Simples Nacional Rate Tables [T1]

**Anexo I -- Commerce (goods resale):**

| Revenue Band (BRL, trailing 12 months) | Nominal Rate | Deduction (BRL) |
|----------------------------------------|-------------|-----------------|
| Up to 180,000 | 4.00% | 0 |
| 180,000.01 to 360,000 | 7.30% | 5,940 |
| 360,000.01 to 720,000 | 9.50% | 13,860 |
| 720,000.01 to 1,800,000 | 10.70% | 22,500 |
| 1,800,000.01 to 3,600,000 | 14.30% | 87,300 |
| 3,600,000.01 to 4,800,000 | 19.00% | 378,000 |

Effective rate = ((Revenue x Nominal Rate) - Deduction) / Revenue

**Other Anexos:** [T1]
- Anexo II: Industry (manufacturing) -- rates from 4.5% to 30%.
- Anexo III: Services (general) -- rates from 6% to 33%.
- Anexo IV: Services (construction, surveillance) -- rates from 4.5% to 33% (no CPP included; employer must pay CPP separately).
- Anexo V: Services (intellectual/technical) -- rates from 15.5% to 30%, but companies with payroll ratio >= 28% may use Anexo III rates instead.

### 2.10 NF-e / E-Document Types [T1]

| Document | Code | Use |
|----------|------|-----|
| NF-e | Model 55 | Sale of goods (ICMS/IPI) |
| NFS-e | Municipal | Services (ISS) |
| CT-e | Model 57 | Transport services |
| NFC-e | Model 65 | Consumer retail (replaces cupom fiscal) |
| MDF-e | -- | Manifest of fiscal documents for transport |

### 2.11 CNPJ Format [T1]

**Format:** `XX.XXX.XXX/YYYY-ZZ`
- First 8 digits (`XX.XXX.XXX`): Company root number.
- 4 digits after `/` (`YYYY`): Branch number. `0001` = headquarters (matriz). `0002`, `0003`, etc. = branches (filiais).
- Last 2 digits (`ZZ`): Check digits (modulo 11).

**Example:** `12.345.678/0001-95`

### 2.12 Registration Requirements [T1]

| Registration | Required For | Issuing Authority | Required to Issue |
|-------------|-------------|-------------------|-------------------|
| CNPJ | All legal entities | Receita Federal | Any fiscal document |
| Inscricao Estadual (IE) | ICMS taxpayers | State SEFAZ | NF-e (model 55) |
| Inscricao Municipal (IM) | ISS taxpayers | Municipal Secretaria | NFS-e |

Under CBS/IBS, registration will be unified through the Comite Gestor do IBS. A single registration should suffice for IBS purposes across all states and municipalities. CNPJ remains the primary identifier. [T2]

---

## Step 3: Reverse Charge / Substituicao Tributaria

### 3.1 ICMS Substituicao Tributaria (ICMS-ST) [T2]

ICMS-ST is a mechanism where one taxpayer in the supply chain (typically the manufacturer or importer) collects ICMS on behalf of subsequent participants in the chain.

**How it works:**
1. The manufacturer calculates ICMS on its own sale (normal debit/credit).
2. The manufacturer **also** calculates and collects ICMS-ST for downstream operations, using a **Margem de Valor Agregado (MVA)** -- an estimated markup percentage set by state agreements (convenios/protocolos CONFAZ).
3. The downstream purchaser (distributor/retailer) does not collect ICMS on resale of that product; ICMS was already pre-paid.

**ICMS-ST base calculation:** [T2]
```
ICMS-ST Base = (Product price + IPI + freight + other charges) x (1 + MVA%)
ICMS-ST = (ICMS-ST Base x internal rate of destination state) - ICMS on own operation
```

**MVA Adjustment for Interstate Operations:** [T2]
When the interstate rate differs from the destination internal rate, states require an **MVA Ajustada** (adjusted MVA):
```
MVA Ajustada = [(1 + MVA original) x (1 - interstate rate) / (1 - internal rate)] - 1
```

**Product categories subject to ICMS-ST** include: fuels, beverages, cigarettes, pharmaceuticals, auto parts, tyres, construction materials, cleaning products, and others as defined in CONFAZ agreements. [T2]

**Risks:** MVA percentages change frequently. Using outdated MVAs is a common audit finding. [T2]

### 3.2 Imported Services -- Reverse Charge Equivalent [T1]

When a Brazilian company imports services, the following taxes apply on the remittance:

| Tax | Rate | Notes |
|-----|------|-------|
| PIS-Importacao | 1.65% | On service remittance value |
| COFINS-Importacao | 7.60% | On service remittance value |
| ISS-Importacao | 2-5% | Municipality-dependent |
| IRRF | 15% or 25% | 25% if remitting to a tax haven jurisdiction |
| IOF | 0.38% | On the FX transaction |
| CIDE | 10% | If technology transfer/royalty (conditional) [T2] |

Total effective tax on imported services can exceed **40%** of the remittance value. [T1]

**New system (CBS/IBS):** CBS and IBS will apply on imported services under the destination principle. The importer (Brazilian buyer) will self-assess CBS/IBS. IRRF and other withholdings remain separate from the indirect tax reform. [T2]

### 3.3 ICMS on Imports [T1]

- ICMS is charged on imports at the internal rate of the importing state.
- The base includes the customs value, import duty (II), IPI, PIS-Import, COFINS-Import, and the ICMS itself (calculated por dentro).
- Import ICMS generates credits under normal rules.

---

## Step 4: Deductibility Check (Credit Rules)

### 4.1 PIS/COFINS Input Credits [T1]

| Regime | Credits Allowed? | Creditable Items |
|--------|-----------------|------------------|
| Cumulative (Lucro Presumido) | **No** | None -- tax cascades |
| Non-Cumulative (Lucro Real) | **Yes** | Goods for resale, manufacturing inputs, electricity, rent, depreciation of fixed assets, and other specified items |
| Import (Non-Cumulative) | **Yes** | Import PIS/COFINS generates credits |

### 4.2 ICMS Input Credits [T1]

- ICMS operates on a **credit/debit basis** (proper VAT mechanism for goods). [T1]
- Credits are taken on purchases of goods for resale, inputs to manufacturing, and certain services (transport, communications). [T1]
- **Fixed assets (CIAP):** ICMS paid on acquisition of fixed assets (ativo permanente) is creditable at **1/48 per month** over four years, via the CIAP mechanism. The monthly credit is proportional to the ratio of taxable vs. exempt/non-taxable sales. If the asset is sold or transferred before 48 months, the remaining credits are forfeited. [T1]

### 4.3 IPI Input Credits [T1]

- IPI generates credits on inputs used in manufacturing. [T1]
- Credits are taken on acquisition of raw materials, intermediate products, and packaging materials. [T1]
- No credits on goods acquired for resale (IPI does not apply on resale). [T1]

### 4.4 ISS -- No Credit Mechanism [T1]

- ISS is **cumulative** -- there is no input credit mechanism. Tax applies on the full service value. [T1]

### 4.5 CBS/IBS Input Credits (New System) [T2]

- **Full input credit** on all acquisitions for business use (like EU VAT). [T2]
- Non-cumulative by design -- eliminates cascading. [T2]
- IS (Imposto Seletivo) is **not creditable** against CBS/IBS. [T2]
- Credits from Simples Nacional suppliers: buyers receive no CBS/IBS credit unless the Simples company opts to pay CBS/IBS outside the DAS. [T2]

### 4.6 Export Credit Maintenance [T1]

Exports are fully relieved of indirect taxes with credit maintenance: [T1]
- **ICMS:** Exempt (LC 87/1996, Art. 3, II), credits maintained.
- **IPI:** Exempt, credits maintained.
- **PIS/COFINS:** Zero-rated (aliquota zero), credits maintained.
- **ISS:** Exempt if the result of the service is verified abroad.
- Under CBS/IBS, exports will be **zero-rated** with full credit maintenance. [T2]

**Note:** In practice, ICMS credit recovery from exports is slow, subject to state-level administrative procedures, and may require judicial action. [T2]

---

## Step 5: Derived Calculations

### 5.1 ICMS-ST Full Calculation Example [T2]

**Scenario:** Manufacturer in SP ships beverages to distributor in MG. Original MVA: 40%.

```
Manufacturer's price (without IPI): BRL 1,000
IPI (10%): BRL 100
ICMS on own operation (12% interstate): BRL 120 (on BRL 1,000)

Step 1 -- MVA Adjustment (interstate rate 12%, MG internal rate 18%):
MVA Ajustada = [(1 + 0.40) x (1 - 0.12) / (1 - 0.18)] - 1
            = [1.40 x 0.88 / 0.82] - 1
            = 50.24%

Step 2 -- ICMS-ST Base:
ICMS-ST Base = (BRL 1,000 + BRL 100) x (1 + 0.5024) = BRL 1,652.64

Step 3 -- ICMS-ST Amount:
ICMS-ST = (BRL 1,652.64 x 18%) - BRL 120 = BRL 297.48 - BRL 120 = BRL 177.48
```

### 5.2 Simples Nacional Effective Rate Calculation [T1]

```
Effective rate = ((Trailing 12-month Revenue x Nominal Rate) - Deduction) / Trailing 12-month Revenue
```

**Example:** Commerce company (Anexo I), BRL 1,200,000 trailing 12-month revenue:
```
Revenue band: BRL 720,000.01 to BRL 1,800,000
Nominal rate: 10.70%, Deduction: BRL 22,500

Effective rate = ((1,200,000 x 10.70%) - 22,500) / 1,200,000
               = (128,400 - 22,500) / 1,200,000
               = 105,900 / 1,200,000
               = 8.825%
```

### 5.3 ICMS Por Dentro Grossing-Up [T1]

To convert a nominal ICMS rate to the effective tax-exclusive rate:
```
Effective rate = Nominal rate / (1 - Nominal rate)

Example (18% nominal):
Effective rate = 0.18 / (1 - 0.18) = 0.18 / 0.82 = 21.95%
```

### 5.4 CBS/IBS Transition Period Calculation (2026) [T2]

During 2026-2028, CBS and IBS are charged **in addition to** existing taxes, but can be offset:
```
CBS (0.9%) can be offset against PIS/COFINS due
IBS (0.1%) can be offset against ICMS due

Net additional burden: Zero (if offset is properly applied)
Total taxes on invoice: PIS + COFINS + ICMS + IPI (if applicable) + CBS (0.9%) + IBS (0.1%)
```

---

## Step 6: Key Thresholds

### 6.1 Simples Nacional Eligibility [T1]

| Category | Annual Gross Revenue Limit |
|----------|--------------------------|
| MEI (Microempreendedor Individual) | BRL 81,000 |
| Microempresa (ME) | BRL 360,000 |
| Empresa de Pequeno Porte (EPP) | BRL 4,800,000 |

- Companies exceeding BRL 4.8 million in trailing 12-month gross revenue are **excluded** from Simples Nacional. [T1]
- Certain activities are **barred** regardless of revenue (e.g., financial institutions, factoring companies, holding companies). [T1]
- For ICMS and ISS purposes, the state/municipal sub-limit is **BRL 3,600,000** in some states. Companies between BRL 3.6M and BRL 4.8M must pay ICMS and ISS outside Simples Nacional (regular regime). [T1]

### 6.2 Imported Goods Interstate ICMS Threshold [T1]

- Imported content exceeding **40%**: interstate ICMS rate drops to **4%** (RSF 13/2012). [T1]

### 6.3 NF-e Cancellation Window [T1]

- NF-e can be cancelled within **24 hours** of authorization if goods have not departed. [T1]
- After 24 hours: correction letter (CC-e) for non-financial fields, or return NF-e required. [T1]

### 6.4 NF-e Retention Period [T1]

- NF-e XML files must be stored for **5 years** (general statute of limitations). [T1]

### 6.5 ICMS Fixed Asset Credit Period [T1]

- **1/48 per month** over 4 years via CIAP mechanism. [T1]

### 6.6 PIS/COFINS Credit Deadline After Extinction [T2]

- LC 214/2025 sets a maximum period of **5 years** after the end of PIS/COFINS (i.e., until end of 2031) to use accumulated PIS/COFINS credits. After that, unused credits are permanently lost. [T2]

---

## Step 7: Filing Deadlines

### 7.1 Current System Filing Calendar [T1]

| Obligation | Frequency | Deadline | Taxpayers |
|-----------|-----------|----------|-----------|
| ICMS return (GIA / SPED Fiscal EFD) | Monthly | Varies by state (typically day 15-20 of following month) | ICMS taxpayers |
| PIS/COFINS (EFD-Contribuicoes) | Monthly | 10th business day of 2nd month following | Lucro Real and Lucro Presumido |
| IPI (via SPED Fiscal EFD) | Monthly | Same as ICMS return | Manufacturers/importers |
| ISS (GIS / DES / NFS-e closing) | Monthly | Varies by municipality (typically day 10-15) | Service providers |
| Simples Nacional (DAS) | Monthly | 20th of following month | Simples Nacional companies |
| DCTF (Federal Tax Debits Declaration) | Monthly | 15th business day of 2nd month following | Lucro Real / Lucro Presumido |
| ICMS-ST (GNRE / GIA-ST) | Monthly | Varies by agreement | ICMS-ST substitutos |
| DIRF (Withholding info) | Annual | Last business day of February | All withholding agents |

### 7.2 SPED -- Public Digital Bookkeeping System [T1]

| SPED Module | Content | Who Must File |
|-------------|---------|---------------|
| EFD-ICMS/IPI (SPED Fiscal) | Monthly ICMS and IPI transactions | ICMS/IPI taxpayers |
| EFD-Contribuicoes | Monthly PIS and COFINS | Lucro Real and Lucro Presumido |
| EFD-Reinf | Withholding taxes and social contributions | Applicable taxpayers |
| ECD (SPED Contabil) | Digital accounting books | Lucro Real and Lucro Presumido |
| ECF | Corporate income tax digital return | All corporate taxpayers |

All businesses in Lucro Real or Lucro Presumido must file SPED obligations. Simples Nacional companies have reduced SPED requirements. [T1]

### 7.3 New System Filing [T2]

- CBS returns will be filed with the RFB, likely monthly, integrated into a new SPED module. [T2]
- IBS returns will be filed with the Comite Gestor do IBS. [T2]
- The split payment system may reduce or automate parts of the return process. [T2]
- During the transition (2026-2032), taxpayers must file obligations for **both** old and new systems concurrently. [T2]

---

## Step 8: Tax Reform Transition (CBS/IBS/IS)

### 8.1 Overview of the Reform [T2]

Constitutional Amendment 132/2023, promulgated on 20 December 2023, enacts the most significant reform of Brazilian taxation since the 1988 Constitution. It replaces the five fragmented indirect taxes with a **dual VAT** system plus a selective excise.

**Key design principles:** [T2]
- **Destination principle:** Tax revenue accrues to the jurisdiction of consumption, not production. Eliminates guerra fiscal.
- **Full input credit:** Broad-based credit for all taxes paid on inputs (like EU VAT). Non-cumulative by design.
- **Single rate per tax:** One CBS rate nationally; one IBS rate per state + municipal combination.
- **Invoice-credit method:** Proper EU-style VAT, with tax explicitly stated on invoices and full credit chain.
- **Cash-back for low-income:** CBS/IBS paid on essential goods can be refunded to low-income families registered in CadUnico.
- **Split payment:** Tax may be collected at the payment moment (electronic split payment system).

**Source:** EC 132/2023, new Art. 156-A (IBS), Art. 195, V (CBS); Lei Complementar 214/2025.

### 8.2 Year-by-Year Transition Rates [T2]

| Year | CBS | IBS | PIS/COFINS | ICMS | ISS | Notes |
|------|-----|-----|-----------|------|-----|-------|
| 2025 | -- | -- | Full | Full | Full | Current system only |
| 2026 | **0.9%** | **0.1%** | Full | Full | Full | Test year; invoices must show CBS/IBS; payment waived if ancillary obligations met; 4-month penalty waiver for CBS/IBS invoice errors |
| 2027 | **Full reference rate** | **0.1%** | **Extinguished** | Full | Full | CBS replaces PIS/COFINS; CBS collection begins 1 Jan 2027; IS collection also begins |
| 2028 | Full | TBD | -- | Full | Full | Continued testing of IBS |
| 2029 | Full | Full reference rate | -- | 90% of current rate | 90% of current rate | IBS full rate begins; ICMS/ISS phase-out starts |
| 2030 | Full | Full | -- | 80% of current rate | 80% of current rate | Continued phase-out |
| 2031 | Full | Full | -- | 70% of current rate | 70% of current rate | Continued phase-out |
| 2032 | Full | Full | -- | 60% of current rate | 60% of current rate | Last year of dual system |
| 2033 | Full | Full | -- | **Extinguished** | **Extinguished** | New system fully operational |

### 8.3 Key Transition Rules [T2]

- During 2026, CBS at 0.9% and IBS at 0.1% appear on invoices but **payment is waived** provided the taxpayer complies with ancillary (reporting) obligations. A **four-month penalty-free adaptation period** applies from the date CBS/IBS regulations are published. [T2]
- From 2027, CBS is collected at the full reference rate and PIS/COFINS are **extinguished**. Companies have until end of 2031 (5 years) to use accumulated PIS/COFINS credits. [T2]
- ICMS credits accumulated before the transition can be used during the phase-out period and, if unused, can be compensated via a specific federal fund through 2032. [T2]
- Existing ICMS state incentives (beneficios fiscais) are validated until 2032 and can be maintained until their original expiry or 2032, whichever is earlier, subject to CONFAZ registration requirements. [T2]
- Long-term contracts signed before EC 132/2023 may have specific transition rules. [T2]
- The Simples Nacional regime is **preserved** but adapted for the new taxes. [T2]

### 8.4 IS -- Imposto Seletivo (Selective Excise) [T2]

- Extra-fiscal tax on goods and services **harmful to health or the environment**.
- Applied on top of CBS/IBS (not a replacement but an addition).
- Target categories: tobacco, alcoholic beverages, sugar-sweetened beverages, mineral extraction, fossil fuels, and potentially others.
- Rates to be set by ordinary law. IS is **not creditable** against CBS/IBS.
- IS does **not** apply to exports, electricity, or telecommunications.
- IS does **not** apply to goods/services produced in the ZFM.
- IS collection begins in **2027**. [T2]

### 8.5 Simples Nacional under the New System [T2]

- Simples Nacional is **preserved** under EC 132/2023.
- CBS and IBS will be included within the Simples Nacional single payment (DAS).
- Companies in Simples Nacional may **opt** to pay CBS and IBS outside the simplified regime (under the regular credit/debit system) to allow their customers to claim full input credits. This is an important commercial consideration -- large corporate buyers may pressure Simples suppliers to opt out so they can recover CBS/IBS credits. [T2]
- Opt-in applies per calendar year and is irrevocable for that year. [T2]

### 8.6 Non-Resident Digital Platform Obligations [T2]

- Non-resident digital service providers supplying B2C in Brazil must **register** for CBS/IBS and collect/remit the tax. This follows the OECD model and is similar to EU VAT MOSS/OSS. [T2]

### 8.7 NF-e Updates for 2026 [T2]

- From 1 January 2026, NF-e and NFS-e must include CBS and IBS fields. [T2]
- A four-month penalty waiver applies from the date regulations are published. [T2]
- If regulations are published in January 2026, mandatory correct recording begins approximately May 2026. [T2]
- NFS-e Nacional (national standardized service invoice) is being implemented using the ABRASF data model. Under CBS/IBS, a unified e-invoicing standard covering both goods and services is expected. [T2]

### 8.8 NF-e Structure and Requirements [T1]

- **XML format:** Every NF-e is an XML document digitally signed by the issuer.
- **SEFAZ authorization:** Before the goods can ship, the NF-e XML must be transmitted to the state SEFAZ and receive an **authorization protocol**.
- **Access key:** Each NF-e has a unique 44-digit access key (chave de acesso) encoding: UF code, date, CNPJ, model, series, number, emission type, numeric code, and check digit.
- **DANFE:** The Documento Auxiliar da NF-e is a printed representation (PDF/barcode) that accompanies physical goods. It is **not** the invoice itself -- the XML is the legally valid document.
- **Cancellation:** Within **24 hours** of authorization if goods have not departed. After 24 hours, CC-e (correction letter) or return NF-e required.
- **Retention:** 5 years.

### 8.9 Comparison with EU VAT [T1]

| Feature | Brazil (Current) | Brazil (New CBS/IBS) | EU VAT |
|---------|-------------------|---------------------|--------|
| Number of taxes | 5 (PIS, COFINS, ICMS, ISS, IPI) | 3 (CBS, IBS, IS) | 1 (VAT) |
| Tax levels | Federal, state, municipal | Federal + subnational | National (EU-harmonised) |
| Mechanism | Mixed (credit/debit + cumulative) | Invoice-credit (VAT-type) | Invoice-credit |
| Cascading | Yes (cumulative PIS/COFINS) | No (full input credit) | No (full input credit) |
| Principle | Origin (ICMS) + provider location (ISS) | Destination | Destination |
| Standard rate | ~34-40% effective combined | ~26.5% combined | 15-27% (varies by Member State) |
| Reduced rates | Complex, product/state-specific | Limited categories (60% reduction) | 0-2 reduced rates per MS |
| E-invoicing | Mandatory (NF-e since 2008) | Mandatory (enhanced) | Partial (ViDA directive from 2028+) |
| Threshold for registration | Simples Nacional up to BRL 4.8M | Simples Nacional preserved | EUR 85,000 from 2025 (SME scheme) |
| Cross-border B2B | Reverse charge (imports) | Reverse charge (imports) | Reverse charge (IC acquisitions) |
| Cross-border B2C digital | Inconsistent enforcement | Platform registration required | OSS / IOSS |
| Refund mechanism | Slow, bureaucratic (especially ICMS) | Split payment / automated | Cash refund or offset |
| Real-time reporting | SPED (monthly) | Real-time split payment planned | Varies (DRR from 2028+) |

---

## PROHIBITIONS

The following actions are **strictly prohibited** when applying this skill:

1. **NEVER** calculate ICMS without confirming the specific state, the direction of the transaction (internal vs. interstate), and the NCM code of the product. Different states, products, and directions yield entirely different rates. [T1]

2. **NEVER** assume a single PIS/COFINS rate without first confirming whether the taxpayer is in the **cumulative** (Lucro Presumido) or **non-cumulative** (Lucro Real) regime. The rates are fundamentally different (3.65% vs. 9.25%). [T1]

3. **NEVER** apply CBS/IBS rates as if they are final law without flagging as [T2]. The reform is in transition. Rates, rules, and timelines may be adjusted by subsequent legislation. Always caveat CBS/IBS advice as subject to change. [T2]

4. **NEVER** advise a client to claim ICMS credits on goods purchased from a supplier benefiting from a unilateral (non-CONFAZ-approved) state incentive without flagging the **glosa** risk. The destination state may disallow the credit. [T2]

5. **NEVER** issue or advise on NF-e without the correct CFOP (Codigo Fiscal de Operacoes e Prestacoes). Incorrect CFOPs are a leading cause of fiscal infractions. [T1]

6. **NEVER** assume that ISS applies to a transaction without checking the **LC 116/2003 services list**. If the service is not on the list, ISS does not apply (and ICMS may apply instead, or no indirect tax at all). [T1]

7. **NEVER** apply ICMS-ST without verifying the current MVA percentage from the applicable CONFAZ protocol. MVAs change frequently and vary by product and by origin/destination state pair. [T2]

8. **NEVER** tell a taxpayer that accumulated ICMS credits from exports can be easily monetised. In practice, ICMS credit recovery is slow, subject to state-level administrative procedures, and may require judicial action. [T2]

9. **NEVER** advise a foreign company that it has no Brazilian indirect tax obligations on B2C digital supplies to Brazil. Both the current system and the new CBS/IBS system impose obligations on cross-border digital services. [T2]

10. **NEVER** calculate IPI on a resale operation. IPI applies only on **industrialisation** (manufacturing, transformation, assembly) and **import**, not on commercial resale. [T1]

11. **NEVER** advise on ZFM tax incentives without confirming the specific product's PPB (Processo Produtivo Basico) compliance. ZFM benefits are conditional on meeting local content and manufacturing process requirements set by SUFRAMA. [T2]

12. **NEVER** assume the CBS/IBS combined rate is exactly 26.5%. This is the government's reference estimate; the actual rate will be defined by law and may differ. Always present it as an approximation. [T2]

13. **NEVER** state that PIS/COFINS continue past 2026 under the new system. PIS/COFINS are **extinguished** from 1 January 2027, replaced by CBS at the full reference rate. Only accumulated credits may be used until end of 2031. [T2]

---

## Edge Case Registry

### Edge Case 1: Transition Period -- Dual System Compliance (2026) [T2]

**Scenario:** A Lucro Real company selling goods interstate in 2026 must calculate PIS (1.65%), COFINS (7.6%), ICMS (12% interstate), IPI (if applicable), **plus** CBS (0.9%) and IBS (0.1%) on the same transaction.

**Rule:** CBS at 0.9% and IBS at 0.1% must appear on the invoice but payment is waived provided ancillary obligations are met. The CBS can be offset against PIS/COFINS due. IBS at 0.1% can be offset against ICMS due. Systems must be updated to handle both tax stacks. A four-month penalty-free period applies from publication of CBS/IBS regulations. [T2]

### Edge Case 2: Simples Nacional Company Selling to Large Corporation [T2]

**Scenario:** A Simples Nacional supplier sells BRL 100,000 in goods to a Lucro Real buyer. Under the current system, the buyer gets limited PIS/COFINS credits on Simples Nacional purchases. Under the new system, if the Simples company does **not** opt for separate CBS/IBS taxation, the buyer receives no CBS/IBS input credit.

**Rule:** The Simples Nacional company may opt to pay CBS and IBS outside the DAS (separately) so that the buyer can claim full credits. This opt-in applies per calendar year and is irrevocable for that year. Advise Simples Nacional suppliers selling primarily to Lucro Real companies to evaluate opting out. [T2]

### Edge Case 3: Manaus Free Trade Zone (ZFM) Preservation [T2]

**Scenario:** A manufacturer in the ZFM sells goods to Sao Paulo. Under the current system, the product is IPI-exempt and has ICMS incentives. Under the new system, will these incentives survive?

**Rule:** EC 132/2023 explicitly preserves ZFM incentives. CBS and IBS will apply at reduced rates or with credits/exemptions to maintain the ZFM's competitive advantage. The exact mechanism is defined in LC 214/2025 and involves a credit presumido (presumed credit) for IBS purposes on goods produced in the ZFM. IPI continues at zero or reduced rate for ZFM products (IPI is being converted to a zero-rate tax for all products except those subject to IS, but ZFM products retain their advantage). [T2]

### Edge Case 4: ICMS-ST with MVA Adjustment for Interstate Operations [T2]

**Scenario:** A manufacturer in SP (ICMS-ST substituto) ships beverages to a distributor in MG. SP internal rate is 18%; MG internal rate is 18%. The CONFAZ protocol sets the MVA for this product at 40%.

**Calculation:** [T2]
```
Manufacturer's price (without IPI): BRL 1,000
IPI (if applicable, e.g., 10%): BRL 100
ICMS on own operation (12% interstate): BRL 120 (on BRL 1,000)
ICMS-ST base = (BRL 1,000 + BRL 100) x (1 + 0.40) = BRL 1,540
ICMS-ST = (BRL 1,540 x 18%) - BRL 120 = BRL 277.20 - BRL 120 = BRL 157.20
```

**MVA Adjustment:** When the interstate rate (12%) differs from the destination internal rate (18%):
```
MVA Ajustada = [(1 + MVA original) x (1 - interstate rate) / (1 - internal rate)] - 1
MVA Ajustada = [(1 + 0.40) x (1 - 0.12) / (1 - 0.18)] - 1 = [1.40 x 0.88 / 0.82] - 1 = 50.24%
```
The adjusted MVA (50.24%) replaces the original MVA (40%) for interstate ICMS-ST calculations. This is a common audit point. [T2]

### Edge Case 5: Digital Services -- ISS vs. ICMS Conflict Resolution [T2]

**Scenario:** A SaaS company in Sao Paulo provides cloud software to a client in Rio de Janeiro.

**Rule:** Following STF precedent (ADIs 1.945 and 5.659, decided in 2021), software operations (including SaaS) are subject to **ISS**, not ICMS. ISS is due at the municipality of the service provider (Sao Paulo) unless the service falls under one of the ~20 ISS exceptions. SaaS is generally taxed at the provider's location.

Under CBS/IBS, this distinction becomes irrelevant -- CBS/IBS applies to both goods and services, taxed at the **destination** (consumer's location). [T2]

### Edge Case 6: Imported Services -- Full Tax Stack [T1]

**Scenario:** A Brazilian company imports consulting services from a US firm, paying BRL 100,000.

**Calculation:** [T1]
```
PIS-Importacao: 1.65% = BRL 1,650
COFINS-Importacao: 7.6% = BRL 7,600
ISS-Importacao: 2-5% (municipality-dependent), e.g., 5% = BRL 5,000
IRRF: 15% = BRL 15,000 (or 25% if tax haven)
IOF: 0.38% = BRL 380
CIDE: 10% if technology transfer/royalty = BRL 10,000 (if applicable) [T2]

Estimated total: BRL 29,630 to BRL 39,630+
```

### Edge Case 7: Interstate Transfer of Goods Between Branches [T2]

**Scenario:** Company transfers goods from its SP warehouse (CNPJ/0001) to its MG branch (CNPJ/0002). No sale occurs.

**Current rule:** The STF ruled in ADC 49 (2021) that ICMS **does not** apply to interstate transfers between establishments of the same taxpayer (no change of ownership). States have resisted implementing this ruling. LC 204/2023 partially regulated the matter, allowing credit transfer. This remains contentious. [T2]

**New system:** Under CBS/IBS, inter-branch transfers will likely not trigger tax, as there is no supply to a third party. [T2]

### Edge Case 8: ICMS Credits on Fixed Assets (CIAP) [T1]

**Scenario:** A company purchases a BRL 500,000 machine for its factory in Sao Paulo.

**Rule:** ICMS paid on fixed assets is creditable at **1/48 per month** over four years via CIAP. Monthly credit is proportional to the ratio of taxable vs. exempt sales. If the asset is sold before 48 months, remaining credits are forfeited. [T1]

### Edge Case 9: Export of Goods -- Full Tax Relief [T1]

**Scenario:** A Brazilian exporter sells manufactured goods to a buyer in Germany.

**Rule:** Exports are fully relieved: [T1]
- ICMS: Exempt with credit maintenance (Lei Kandir, LC 87/1996, Art. 3, II).
- IPI: Exempt with credit maintenance.
- PIS/COFINS: Zero-rated with credit maintenance.
- ISS: Exempt if the result of the service is verified abroad.
- Accumulated ICMS credits can be transferred to third parties (subject to state rules) or monetised, though in practice this is slow and bureaucratic.

### Edge Case 10: Guerra Fiscal -- State ICMS Incentive Invalidation [T2]

**Scenario:** A company benefiting from an ICMS incentive granted by Goias (without CONFAZ unanimity approval) sells goods to a buyer in Sao Paulo. SP disallows (glosa) the buyer's ICMS credits.

**Rule:** ICMS incentives granted without unanimous CONFAZ approval are technically unconstitutional (CF Art. 155, sec. 2, XII, g). However, LC 160/2017 and CONFAZ Convenio 190/2017 validated many existing incentives. States may still challenge credits on goods benefiting from non-validated incentives. This is a major litigation risk. [T2]

**New system:** IBS uses the destination principle, eliminating the incentive for origin-based tax breaks. Existing incentives preserved only until 2032. [T2]

### Edge Case 11: Split Payment and Cash-Back Mechanism [T2]

**Scenario:** Under CBS/IBS, a low-income consumer (registered in CadUnico) purchases basic food items.

**Rule:** The split payment system will automatically segregate the CBS/IBS component at the point of payment. For CadUnico-registered consumers, the CBS/IBS portion on defined essential goods will be **refunded** directly. Implementation details are in LC 214/2025 and forthcoming regulations. [T2]

### Edge Case 12: Non-Resident Digital Platform Obligations [T2]

**Scenario:** A foreign digital platform supplies digital services to Brazilian consumers.

**Current rule:** PIS/COFINS-Import and ISS-Import apply. Enforcement has been inconsistent.

**New rule (CBS/IBS):** Non-resident digital service providers supplying B2C in Brazil must **register** for CBS/IBS and collect/remit the tax. The platform bears the compliance obligation. [T2]

---

## Test Suite

### Test 1: PIS/COFINS Regime Identification [T1]

**Input:** "Our company is taxed under Lucro Presumido. What PIS/COFINS rates apply?"

**Expected Output:** Cumulative regime. PIS: 0.65%, COFINS: 3.00%. Combined: 3.65%. No input credits available. Source: Lei 9.718/1998.

**Grading:** PASS if rates are exactly 0.65% / 3.00% and regime is identified as cumulative with no credits. FAIL if non-cumulative rates (1.65% / 7.6%) are cited.

---

### Test 2: Interstate ICMS Rate Lookup [T1]

**Input:** "What ICMS rate applies to a sale of goods from Sao Paulo to Bahia?"

**Expected Output:** 7%. SP is in the South/Southeast region; BA is in the Northeast. Interstate rate from South/Southeast to North/Northeast/Centre-West is 7%. Source: CF Art. 155, sec. 2, VII; Resolucao do Senado 22/1989.

**Grading:** PASS if rate is 7% with correct reasoning. FAIL if 12% (intra-South/Southeast rate) is cited.

---

### Test 3: ICMS-ST MVA Adjustment Calculation [T2]

**Input:** "Calculate the adjusted MVA for an interstate ICMS-ST operation. Original MVA: 50%. Interstate rate: 12%. Destination internal rate: 18%."

**Expected Output:**
```
MVA Ajustada = [(1 + 0.50) x (1 - 0.12) / (1 - 0.18)] - 1
            = [1.50 x 0.88 / 0.82] - 1
            = [1.6098] - 1
            = 60.98%
```
Adjusted MVA: 60.98%.

**Grading:** PASS if formula is correct and result is approximately 60.98%. FAIL if original MVA (50%) is used without adjustment.

---

### Test 4: Simples Nacional Effective Rate Calculation [T1]

**Input:** "Our commerce company (Anexo I) had BRL 1,200,000 in trailing 12-month gross revenue. What is our effective Simples Nacional rate?"

**Expected Output:**
Revenue band: BRL 720,000.01 to BRL 1,800,000. Nominal rate: 10.70%. Deduction: BRL 22,500.
```
Effective rate = ((1,200,000 x 10.70%) - 22,500) / 1,200,000
               = (128,400 - 22,500) / 1,200,000
               = 105,900 / 1,200,000
               = 8.825%
```
Effective rate: 8.825%.

**Grading:** PASS if effective rate is 8.825%. FAIL if nominal rate (10.70%) is presented as the effective rate.

---

### Test 5: CBS/IBS Transition Year Rate (2026) [T2]

**Input:** "What CBS and IBS rates apply in 2026?"

**Expected Output:** CBS: 0.9%. IBS: 0.1%. These are testing-phase rates that must appear on invoices but payment is waived provided ancillary obligations are met. A four-month penalty-free adaptation period applies from publication of CBS/IBS regulations. Existing PIS/COFINS/ICMS/ISS continue at full rates. Source: EC 132/2023 transition provisions; LC 214/2025.

**Grading:** PASS if both rates are correct, the no-payment/waiver nature is explained, and the dual-system nature is noted. FAIL if full reference rates are cited for 2026.

---

### Test 6: Export Tax Treatment [T1]

**Input:** "A Brazilian manufacturer exports machinery to Argentina. What indirect taxes apply?"

**Expected Output:** All indirect taxes are relieved on export:
- ICMS: Exempt (LC 87/1996, Art. 3, II), credits maintained.
- IPI: Exempt, credits maintained.
- PIS: Zero-rated, credits maintained.
- COFINS: Zero-rated, credits maintained.
- ISS: N/A (goods, not services).
Total indirect tax on export: 0%. Exporter retains all input credits.

**Grading:** PASS if all five taxes are addressed with zero/exempt status and credit maintenance noted. FAIL if any tax is applied to the export.

---

### Test 7: CNPJ Validation [T1]

**Input:** "Is this a valid CNPJ format: 12.345.678/0001-95?"

**Expected Output:** The format is valid: `XX.XXX.XXX/YYYY-ZZ`. 8-digit root (12.345.678), branch 0001 (headquarters), check digits 95. Actual validity of the check digits requires modulo 11 calculation. The format structure is correct.

**Grading:** PASS if format is correctly identified with root/branch/check digit explanation. FAIL if format is rejected.

---

### Test 8: ISS vs. ICMS Classification for SaaS [T2]

**Input:** "Our company provides SaaS to clients across Brazil. Is this subject to ISS or ICMS?"

**Expected Output:** ISS. Following STF rulings in ADIs 1.945 and 5.659, software operations (including SaaS) are subject to ISS, not ICMS. ISS is due at the municipality of the service provider. Rate: 2-5% depending on the municipality. Service item: LC 116/2003, item 1.05.

Under the new CBS/IBS system (from 2026+), this distinction is eliminated -- CBS/IBS applies to all goods and services uniformly. [T2]

**Grading:** PASS if ISS is identified with STF precedent cited. FAIL if ICMS is applied.

---

### Test 9: Imported Services Tax Stack [T1]

**Input:** "Our Brazilian company will pay BRL 100,000 to a US consulting firm. What taxes apply on the remittance?"

**Expected Output:** Multiple taxes apply:
- PIS-Importacao: 1.65% = BRL 1,650
- COFINS-Importacao: 7.6% = BRL 7,600
- ISS-Importacao: 2-5% (municipality-dependent), e.g., 5% = BRL 5,000
- IRRF: 15% = BRL 15,000 (or 25% if remitting to a tax haven jurisdiction)
- IOF: 0.38% = BRL 380
- CIDE: 10% if technology transfer/royalty = BRL 10,000 (if applicable)

Estimated total taxes: BRL 29,630 to BRL 39,630+ depending on ISS rate, CIDE applicability, and jurisdiction classification. Flag as [T2] for CIDE applicability.

**Grading:** PASS if at least PIS-Import, COFINS-Import, ISS-Import, IRRF, and IOF are identified. FAIL if only one or two taxes are mentioned.

---

### Test 10: ZFM Product IPI Treatment [T1]

**Input:** "A factory in the Zona Franca de Manaus produces electronics with a valid PPB. What IPI applies on domestic sale to Rio de Janeiro?"

**Expected Output:** IPI is **exempt** for goods manufactured in the ZFM with valid PPB. ICMS incentives also apply (typically reduced rate or credit presumido). ZFM benefits are constitutionally guaranteed until 2073 (ADCT Art. 40). Under CBS/IBS, equivalent benefits will be maintained via presumed credits. [T2]

**Grading:** PASS if IPI exemption is identified with PPB requirement and ZFM constitutional guarantee. FAIL if IPI is charged at standard rates.

---

### Test 11: ICMS Internal Rate Lookup [T1]

**Input:** "What is the general ICMS rate for internal sales in Minas Gerais?"

**Expected Output:** 18%. Source: MG state legislation (RICMS/MG).

**Grading:** PASS if 18% is cited. FAIL if a different rate is given.

---

### Test 12: Interstate ICMS on Imported Goods [T1]

**Input:** "We import goods via the port of Santos (SP) and resell them interstate to Parana. The goods have over 40% imported content. What interstate ICMS rate applies?"

**Expected Output:** 4%. Under Resolucao do Senado Federal 13/2012, goods with imported content exceeding 40% are subject to a 4% interstate ICMS rate, regardless of origin/destination state combination.

**Grading:** PASS if 4% is cited with RSF 13/2012 reference. FAIL if 7% or 12% is applied.

---

### Test 13: PIS/COFINS Extinction Year [T2]

**Input:** "When are PIS and COFINS extinguished under the tax reform?"

**Expected Output:** PIS and COFINS are extinguished from **1 January 2027**, replaced by CBS at the full reference rate (~8.8%). Accumulated PIS/COFINS credits can be used until end of 2031 (5-year window per LC 214/2025). Source: EC 132/2023; LC 214/2025.

**Grading:** PASS if 2027 is stated with credit deadline. FAIL if 2029 or any other year is cited.

---

### Test 14: Transition Period -- ICMS Phase-Out (2029) [T2]

**Input:** "In 2029, what happens to ICMS rates?"

**Expected Output:** In 2029, ICMS is reduced to **90% of the current rate** in each state. For example, if SP's internal rate is 18%, the 2029 rate would be 16.2% (18% x 90%). Simultaneously, IBS applies at its full reference rate. PIS/COFINS are already extinguished (since 2027). Source: EC 132/2023 transition schedule.

**Grading:** PASS if 90% reduction is stated with correct example calculation. FAIL if full ICMS rate is cited for 2029.

---

## Reviewer Escalation Protocol

### When to Escalate [T1]

Escalate to a licensed Brazilian accountant (Contador CRC) or tax attorney in the following situations:

1. **Any [T3] question:** The skill does not cover this topic. Do not guess.
2. **ICMS-ST calculations:** Always have a reviewer verify the applicable CONFAZ protocol, MVA percentage, and adjusted MVA formula before filing. [T2]
3. **State-specific ICMS incentive claims:** Risk of glosa (credit disallowance) requires legal review. [T2]
4. **CBS/IBS transition calculations:** The reform is still being implemented. All CBS/IBS advice must be flagged as subject to regulatory change. [T2]
5. **ZFM PPB compliance:** Requires verification by SUFRAMA. [T2]
6. **Transfer pricing interaction with indirect taxes:** [T3]
7. **Audit defence and penalty abatement:** [T3]
8. **Complex ICMS-ST margins with multiple downstream participants:** [T3]
9. **Guerra fiscal litigation strategy:** [T3]
10. **Cross-border restructuring for indirect tax efficiency:** [T3]

### Escalation Format [T1]

When escalating, provide:
- **Issue summary:** What question or calculation could not be confidently resolved.
- **Confidence tier:** [T2] or [T3].
- **Data collected:** All relevant facts gathered during onboarding (Step 0).
- **Preliminary analysis:** What the skill suggests, clearly caveated as unreviewed.
- **Recommended specialist:** Contador CRC, tax attorney (advogado tributarista), or both.

---

## Contribution Notes

### Key Legal References

| Reference | Subject |
|-----------|---------|
| Constituicao Federal, Art. 153, IV | IPI (federal competence) |
| Constituicao Federal, Art. 155, II | ICMS (state competence) |
| Constituicao Federal, Art. 156, III | ISS (municipal competence) |
| Constituicao Federal, Art. 195, I, b | PIS/COFINS (social contributions) |
| Lei Complementar 87/1996 (Lei Kandir) | ICMS general rules, interstate, exports |
| Lei Complementar 116/2003 | ISS services list and general rules |
| Lei 10.637/2002 | PIS non-cumulative regime |
| Lei 10.833/2003 | COFINS non-cumulative regime |
| Lei 9.718/1998 | PIS/COFINS cumulative regime |
| Decreto 7.212/2010 (RIPI) | IPI regulations |
| Lei Complementar 123/2006 | Simples Nacional |
| Emenda Constitucional 132/2023 | Tax reform (CBS, IBS, IS) |
| Lei Complementar 214/2025 | CBS/IBS/IS regulation |
| Resolucao do Senado Federal 13/2012 | 4% interstate rate for imported goods |
| Emenda Constitucional 87/2015 | DIFAL on interstate B2C sales |
| Lei Complementar 190/2022 | DIFAL regulation |
| Lei Complementar 204/2023 | ICMS on interstate transfers (ADC 49 regulation) |
| Lei Complementar 160/2017 | Validation of state ICMS incentives |
| CONFAZ Convenio 190/2017 | Registration of validated ICMS incentives |
| STF RE 574.706 | Exclusion of ICMS from PIS/COFINS base |
| STF ADIs 1.945 and 5.659 | Software subject to ISS, not ICMS |
| STF ADC 49 | ICMS not applicable on inter-branch transfers |
| ADCT Art. 40 (as amended by EC 83/2014) | ZFM incentives guaranteed until 2073 |

### Glossary

| Term | Definition |
|------|-----------|
| Aliquota | Tax rate |
| Base de calculo | Tax base / taxable amount |
| CFOP | Codigo Fiscal de Operacoes e Prestacoes -- operation code on NF-e |
| CNPJ | Cadastro Nacional da Pessoa Juridica -- company tax ID |
| CONFAZ | Conselho Nacional de Politica Fazendaria -- council of state finance secretaries |
| CPF | Cadastro de Pessoas Fisicas -- individual tax ID |
| Credito presumido | Presumed (deemed) credit |
| Cumulative (cumulativo) | Tax regime without input credit deductions |
| DANFE | Documento Auxiliar da NF-e -- printed auxiliary document |
| DAS | Documento de Arrecadacao do Simples Nacional -- Simples payment slip |
| DIFAL | Diferencial de Aliquota -- rate differential on interstate B2C sales |
| EFD | Escrituracao Fiscal Digital -- digital fiscal bookkeeping (SPED) |
| Glosa | Disallowance of tax credits by the tax authority |
| Guerra fiscal | Tax wars between states using ICMS incentives |
| ICMS-ST | ICMS Substituicao Tributaria -- tax substitution mechanism |
| Lucro Presumido | Presumed profit corporate income tax regime |
| Lucro Real | Actual profit corporate income tax regime |
| MVA | Margem de Valor Agregado -- value-added margin for ICMS-ST |
| NCM | Nomenclatura Comum do Mercosul -- product classification code |
| NF-e | Nota Fiscal Eletronica -- electronic invoice for goods |
| NFS-e | Nota Fiscal de Servicos Eletronica -- electronic invoice for services |
| Non-cumulative (nao cumulativo) | Tax regime with input credit deductions |
| Por dentro | Tax included within its own base (ICMS method) |
| Por fora | Tax applied on top of the base (IPI method) |
| PPB | Processo Produtivo Basico -- basic manufacturing process requirement for ZFM |
| SEFAZ | Secretaria de Estado de Fazenda -- state finance department |
| SPED | Sistema Publico de Escrituracao Digital -- public digital bookkeeping system |
| SUFRAMA | Superintendencia da Zona Franca de Manaus -- ZFM regulatory authority |
| TIPI | Tabela de Incidencia do IPI -- IPI rate table by NCM |
| ZFM | Zona Franca de Manaus -- Manaus Free Trade Zone |

### Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-04-06 | Initial release covering current system (PIS/COFINS/ICMS/ISS/IPI) and new system (CBS/IBS/IS) under EC 132/2023. Transition timeline 2026-2032 included. |
| 2.0 | 2026-04-10 | Restructured to Step format (Q1). Updated transition timeline: PIS/COFINS extinguished 2027 (not 2029) per LC 214/2025. Updated ICMS rates: Maranhao 23%, Piaui 22.5%. Added 2026 penalty waiver details. Added Step 0 onboarding questions. Added classification decision tree. Added PIS/COFINS credit deadline (end 2031). Added Prohibition 13. Added Test 13-14. Deep research verification completed April 2026. |

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
