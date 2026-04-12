---
name: brazil-vat
description: Use this skill whenever asked about Brazilian indirect taxes, VAT, consumption taxes, PIS, COFINS, ICMS, ISS, IPI, CBS, IBS, Imposto Seletivo, NF-e (Nota Fiscal Eletronica), Simples Nacional, CNPJ registration, tax reform (EC 132/2023), or any request involving Brazilian goods and services taxation, filing, compliance, or classification. Trigger on phrases like "Brazil tax", "Brazilian VAT", "PIS/COFINS", "ICMS", "ISS", "IPI", "CBS", "IBS", "NF-e", "nota fiscal", "Simples Nacional", "CNPJ", "tax reform Brazil", or any request involving Brazilian indirect tax compliance. This skill contains the complete Brazilian indirect tax framework covering both the current multi-tax system (PIS/COFINS/ICMS/ISS/IPI) and the new unified system (CBS/IBS/IS) under Constitutional Amendment 132/2023. ALWAYS read this skill before touching any Brazilian indirect tax work.
version: 2.0
---

# Brazil Indirect Tax / VAT Skill v2.0

## Section 1 -- Quick reference

**Read this whole section before classifying anything. Brazil does NOT have a single unified VAT. It has five indirect taxes at three levels of government, currently undergoing reform into a dual VAT (CBS+IBS).**

| Field | Value |
|---|---|
| Country | Federative Republic of Brazil (Republica Federativa do Brasil) |
| Tax system (current) | Five principal indirect taxes: PIS, COFINS, ICMS, ISS, IPI |
| Tax system (new, transitioning) | CBS + IBS + Imposto Seletivo (IS) under EC 132/2023 and LC 214/2025 |
| Transition period | 2026 through 2032; full new system from 1 January 2033 |
| PIS rate (non-cumulative / Lucro Real) | 1.65% on gross revenue |
| PIS rate (cumulative / Lucro Presumido) | 0.65% on gross revenue |
| COFINS rate (non-cumulative / Lucro Real) | 7.60% on gross revenue |
| COFINS rate (cumulative / Lucro Presumido) | 3.00% on gross revenue |
| Combined PIS+COFINS (non-cumulative) | 9.25% (with input credits) |
| Combined PIS+COFINS (cumulative) | 3.65% (no input credits, tax cascades) |
| ICMS general rate | 17-23% by state (internal); 4%, 7%, or 12% (interstate) |
| ISS rate | 2-5% (set by each municipality) |
| IPI rate | 0-300%+ (product-specific via TIPI table by NCM code) |
| CBS rate (2026 transition) | 0.9% (test rate alongside existing PIS/COFINS) |
| IBS rate (2026 transition) | 0.1% (test rate alongside existing ICMS/ISS) |
| Estimated combined CBS+IBS (full implementation) | ~26.5% (not final, subject to regulatory adjustment) |
| E-invoice | NF-e (Model 55, goods); NFS-e (services); NFC-e (Model 65, consumer retail); CT-e (Model 57, transport) |
| Filing portal (federal) | https://www.gov.br/receitafederal (Receita Federal) |
| Filing portal (state) | Each state's SEFAZ portal |
| Currency | BRL (Brazilian Real) |
| Identifier | CNPJ (XX.XXX.XXX/YYYY-ZZ format) |
| Primary legislation | Constituicao Federal Art. 153-156; LC 87/1996 (ICMS); Lei 10.637/2002 (PIS); Lei 10.833/2003 (COFINS); LC 116/2003 (ISS); Decreto 7.212/2010 (IPI); EC 132/2023; LC 214/2025 |
| Contributor | Open Accounting Skills Registry |
| Validated by | Deep research verification, April 2026 |
| Validation date | April 2026 |
| Skill version | 2.0 |

**Key current-system rates at a glance:**

| Tax | Level | Rate | Input credits? |
|---|---|---|---|
| PIS (non-cumulative) | Federal | 1.65% | Yes |
| COFINS (non-cumulative) | Federal | 7.60% | Yes |
| PIS (cumulative) | Federal | 0.65% | No |
| COFINS (cumulative) | Federal | 3.00% | No |
| ICMS (internal, general) | State | 17-23% by state | Yes (debit/credit) |
| ICMS (interstate, S/SE to N/NE/CW) | State | 7% | Yes |
| ICMS (interstate, other) | State | 12% | Yes |
| ICMS (imported goods >40% content) | State | 4% | Yes |
| ISS | Municipal | 2-5% | No (cascading) |
| IPI | Federal | NCM-specific (TIPI table) | Yes (manufacturing) |

**IBS+CBS reform context:**

EC 132/2023 replaces PIS+COFINS with CBS (federal) and ICMS+ISS with IBS (state+municipal). The transition runs 2026-2032. In 2026, CBS at 0.9% and IBS at 0.1% are test rates applied alongside the existing taxes. From 2027, CBS replaces PIS/COFINS entirely. From 2029, IBS begins replacing ICMS/ISS at increasing rates. By 2033, only CBS+IBS+IS remain. All reform-related rules are flagged as reviewer-judgement-required because regulations are still being published.

**Simples Nacional thresholds:**

| Revenue band (BRL, trailing 12 months) | Eligibility |
|---|---|
| Up to BRL 4,800,000 | Eligible for Simples Nacional (unified DAS payment) |
| Up to BRL 81,000 | MEI (Microempreendedor Individual) -- simplified regime |
| Above BRL 4,800,000 | Must use Lucro Presumido or Lucro Real |

**Conservative defaults -- Brazil-specific:**

| Ambiguity | Default |
|---|---|
| Unknown tax regime | Lucro Presumido (cumulative PIS/COFINS, no input credits) |
| Unknown ICMS rate | Apply highest plausible internal rate for the state (conservative) |
| Unknown ISS rate | 5% (maximum) |
| Unknown whether Simples Nacional | Not Simples Nacional (apply full tax rates) |
| Unknown PIS/COFINS input credit eligibility | Not creditable |
| Unknown ICMS-ST applicability | Assume not subject to ST (flag for reviewer) |
| Unknown interstate vs internal | Internal (apply internal rate) |
| Unknown whether service or goods | Goods (ICMS applies, higher rate) |
| Unknown NCM code for IPI | 0% IPI (conservative for buyer; flag for reviewer) |
| Unknown business-use proportion | 0% recovery |
| Unknown whether transaction is in scope | In scope |

**Red flag thresholds:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | BRL 50,000 |
| HIGH tax-delta on a single conservative default | BRL 5,000 |
| MEDIUM counterparty concentration | >40% of output OR input |
| MEDIUM conservative-default count | >4 across the return |
| LOW absolute net tax position | BRL 100,000 |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- bank statement (extrato bancario) for the month in PDF, CSV, OFX, or pasted text. Must cover the full period. Acceptable from any Brazilian bank: Banco do Brasil, Itau Unibanco, Bradesco, Santander Brasil, Caixa Economica Federal, Nubank, Inter, BTG Pactual, Sicoob, or any other. NF-e XMLs are strongly preferred for ICMS and PIS/COFINS credit verification.

**Recommended** -- NF-e XML files for all sales and purchases (or the monthly SPED fiscal file), CNPJ and inscricao estadual/municipal, prior month's DARF/DAS payment receipts, constancia de optante Simples Nacional (if applicable).

**Ideal** -- complete NF-e download from the state SEFAZ portal, SPED fiscal file, EFD-Contribuicoes (PIS/COFINS), DCTF, prior period returns, CNPJ card showing all registrations.

**Refusal policy if minimum is missing -- SOFT WARN.** If no bank statement and no NF-e files at all, hard stop. If bank statement only without NF-e: proceed but record in the reviewer brief: "This return was produced from bank statement alone. The reviewer must verify that all PIS/COFINS credits are supported by valid NF-e/NFS-e, that ICMS credits match the SPED fiscal, and that state-specific rules have been correctly applied."

### Brazil-specific refusal catalogue

**R-BR-1 -- ICMS-ST complex margin calculations.** *Trigger:* product is subject to ICMS Substituicao Tributaria and the MVA (Margem de Valor Agregado) or adjusted MVA calculation is required. *Message:* "ICMS-ST margin calculations require product-specific CONFAZ protocol lookup and MVA adjustment formulas. This is outside the scope of automated classification. Escalate to a Contador CRC with ICMS-ST experience for the specific product and state pair."

**R-BR-2 -- Zona Franca de Manaus (ZFM) incentives.** *Trigger:* client operates in or ships to the Zona Franca de Manaus. *Message:* "ZFM incentives (IPI exemption, ICMS reduction, SUFRAMA credits) require PPB verification and specific SUFRAMA procedures. Escalate to a specialist."

**R-BR-3 -- State-specific ICMS incentive litigation (guerra fiscal).** *Trigger:* client benefits from a state ICMS incentive that may not be recognized by CONFAZ. *Message:* "Unrecognized state ICMS incentives carry glosa (disallowance) risk in destination states. Escalate to a tax attorney."

**R-BR-4 -- Transfer pricing interaction.** *Trigger:* intercompany transactions with related foreign parties affecting the indirect tax base. *Message:* "Transfer pricing adjustments affecting the indirect tax base require specialist analysis. Escalate."

**R-BR-5 -- Audit defence or penalty abatement.** *Trigger:* client is under audit or seeking penalty reduction. *Message:* "Audit defence and penalty abatement are outside this skill's scope. Engage a tax attorney."

**R-BR-6 -- Income tax return instead of indirect tax.** *Trigger:* user asks about IRPJ/CSLL corporate income tax or IRPF individual income tax. *Message:* "This skill only handles indirect taxes (PIS, COFINS, ICMS, ISS, IPI, CBS, IBS). For income tax, use the appropriate income tax skill."

---

## Section 3 -- Supplier pattern library (the lookup table)

This is the deterministic pre-classifier. When a transaction's counterparty matches a pattern in this table, apply the treatment directly. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name as it appears in the bank statement (extrato). If multiple patterns match, use the most specific.

### 3.1 Brazilian banks (fees -- financial service, exempt from PIS/COFINS)

| Pattern | Treatment | Notes |
|---|---|---|
| BANCO DO BRASIL, BB | EXCLUDE for bank charges/tarifas | Financial service, exempt. No PIS/COFINS, no ICMS, no ISS. |
| ITAU, ITAU UNIBANCO | EXCLUDE for bank charges/tarifas | Same |
| BRADESCO | EXCLUDE for bank charges/tarifas | Same |
| SANTANDER BRASIL, SANTANDER BR | EXCLUDE for bank charges/tarifas | Same |
| CAIXA, CAIXA ECONOMICA FEDERAL, CEF | EXCLUDE for bank charges/tarifas | Same |
| NUBANK, NU PAGAMENTOS | EXCLUDE for bank charges/tarifas | Same |
| BANCO INTER, INTER | EXCLUDE for bank charges/tarifas | Same |
| BTG PACTUAL | EXCLUDE for bank charges/tarifas | Same |
| SICOOB, SICREDI, BANCOOB | EXCLUDE for bank charges/tarifas | Cooperative bank fees, same treatment |
| BANCO SAFRA, BANCO VOTORANTIM | EXCLUDE for bank charges/tarifas | Same |
| JUROS, RENDIMENTO, IOF | EXCLUDE | Interest, yield, IOF -- financial, out of indirect tax scope |
| EMPRESTIMO, FINANCIAMENTO | EXCLUDE | Loan principal movement, out of scope |
| TARIFA BANCARIA, TAXA DE MANUTENCAO | EXCLUDE | Bank maintenance fee, exempt financial service |
| TED, DOC (fee lines) | EXCLUDE | Transfer fees, exempt financial service |

### 3.2 Brazilian government, tax authorities, and statutory bodies (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| RECEITA FEDERAL, RFB, DARF | EXCLUDE | Federal tax payment (IRPJ, CSLL, PIS, COFINS, IPI) |
| SEFAZ, SECRETARIA DA FAZENDA | EXCLUDE | State tax payment (ICMS) |
| PREFEITURA, SECRETARIA DE FINANCAS | EXCLUDE | Municipal tax/ISS payment |
| SIMPLES NACIONAL, DAS | EXCLUDE | Simples Nacional unified tax payment |
| INSS, PREVIDENCIA | EXCLUDE | Social security contribution |
| FGTS | EXCLUDE | Severance fund deposit |
| CRC, CONSELHO REGIONAL DE CONTABILIDADE | EXCLUDE | Professional body fee, not subject to indirect tax |
| JUNTA COMERCIAL | EXCLUDE | Commercial registry fee, sovereign act |
| DETRAN, IPVA | EXCLUDE | Vehicle registration/tax, not indirect tax |
| IPTU | EXCLUDE | Property tax, municipal, not indirect tax |

### 3.3 Brazilian utilities

| Pattern | Treatment | Taxes | Notes |
|---|---|---|---|
| CPFL, CPFL ENERGIA | ICMS applies (state rate) | ICMS + PIS/COFINS | Electricity -- ICMS varies by state; PIS/COFINS on electricity bills. NF-e issued. |
| CEMIG | ICMS applies | ICMS + PIS/COFINS | Same -- Minas Gerais electricity |
| LIGHT, LIGHT SA | ICMS applies | ICMS + PIS/COFINS | Rio de Janeiro electricity |
| ENEL, ENEL DISTRIBUICAO | ICMS applies | ICMS + PIS/COFINS | SP, RJ, CE, GO electricity |
| ENERGISA | ICMS applies | ICMS + PIS/COFINS | Multiple states |
| SABESP | ISS or exempt | ISS (municipality-dependent) | Water/sewer -- Sao Paulo. Treatment varies; some water services are exempt. |
| COPASA | ISS or exempt | ISS | Water -- Minas Gerais |
| CLARO, CLARO BRASIL | ICMS applies | ICMS + PIS/COFINS | Telecoms (ICMS, not ISS -- transport/communication) |
| VIVO, TELEFONICA BRASIL | ICMS applies | ICMS + PIS/COFINS | Same -- telecoms |
| TIM, TIM BRASIL | ICMS applies | ICMS + PIS/COFINS | Same |
| OI, OI SA | ICMS applies | ICMS + PIS/COFINS | Same |
| NET, NET SERVICOS | ICMS applies | ICMS + PIS/COFINS | Cable/internet -- telecoms subject to ICMS |

### 3.4 Insurance (exempt -- exclude from indirect tax)

| Pattern | Treatment | Notes |
|---|---|---|
| PORTO SEGURO | EXCLUDE | Insurance premium -- exempt from ICMS/ISS; subject to IOF (separate) |
| BRADESCO SEGUROS, BRADESCO AUTO | EXCLUDE | Same |
| SULAMERICA, SUL AMERICA | EXCLUDE | Same |
| ITAU SEGUROS | EXCLUDE | Same |
| ZURICH, ALLIANZ, MAPFRE BRASIL | EXCLUDE | Same |
| SEGURO, APOLICE, SINISTRO | EXCLUDE | All insurance transactions -- exempt indirect tax |

### 3.5 Transport and logistics

| Pattern | Treatment | Taxes | Notes |
|---|---|---|---|
| CORREIOS, ECT | ICMS (postal service is ICMS, not ISS) | ICMS + PIS/COFINS | Postal/courier -- CT-e issued for transport |
| JADLOG, TOTAL EXPRESS | ICMS | ICMS + PIS/COFINS | Express freight |
| AZUL CARGO, LATAM CARGO | ICMS | ICMS + PIS/COFINS | Air freight |
| 99, 99 TECNOLOGIA, 99POP | ISS | ISS + PIS/COFINS | Ride-hailing -- service subject to ISS (municipality rate) |
| UBER, UBER BRASIL | ISS | ISS + PIS/COFINS | Same -- ride-hailing is a service |
| IFOOD, IFOOD AGENCIA | ISS | ISS + PIS/COFINS | Food delivery platform -- ISS on service fee. Food items may have different treatment. |
| RAPPI | ISS | ISS + PIS/COFINS | Same as iFood |
| GOL, LATAM, AZUL (airline) | ICMS exempt or zero | | Domestic flights -- interstate passenger transport has specific ICMS treatment (generally non-taxable for ICMS; ISS does not apply to transport) |

### 3.6 Major Brazilian retailers and e-commerce

| Pattern | Treatment | Taxes | Notes |
|---|---|---|---|
| MAGAZINE LUIZA, MAGALU | ICMS + PIS/COFINS | Full chain | General merchandise -- NF-e issued. Check NCM for IPI if manufactured. |
| CASAS BAHIA, PONTO (VIA) | ICMS + PIS/COFINS | Full chain | Same |
| AMERICANAS, B2W | ICMS + PIS/COFINS | Full chain | Same |
| MERCADO LIVRE, MERCADO PAGO | ICMS + PIS/COFINS (goods); ISS (marketplace fee) | Mixed | Marketplace: goods purchases have ICMS; platform service fees have ISS. Separate lines. |
| AMAZON BR, AMAZON BRASIL | ICMS + PIS/COFINS | Full chain | Check if seller is Amazon directly or third-party marketplace |
| SHOPEE BRASIL | ICMS + PIS/COFINS | Full chain | Same marketplace consideration |
| CARREFOUR, ATACADAO | ICMS + PIS/COFINS | Full chain | Supermarket/wholesale -- food items may have reduced/zero PIS/COFINS (cesta basica) |
| PAO DE ACUCAR, EXTRA, GPA | ICMS + PIS/COFINS | Full chain | Same |
| KALUNGA | ICMS + PIS/COFINS | Full chain | Office supplies |

### 3.7 SaaS and digital services -- foreign suppliers

| Pattern | Treatment | Notes |
|---|---|---|
| GOOGLE (Ads, Workspace, Cloud) | ISS on import + PIS/COFINS-Import + IRRF + IOF | Foreign digital service. Brazilian buyer must withhold/self-assess. ISS rate per municipality (2-5%). PIS-Import 1.65%, COFINS-Import 7.60%, IRRF 15% (or 25% if tax haven), IOF 0.38%. |
| MICROSOFT (365, Azure) | Same as Google | Check if billed by Microsoft Brasil (domestic) or Microsoft Corp (import) |
| ADOBE | Same | Check billing entity |
| META, FACEBOOK ADS | Same | |
| AWS, AMAZON WEB SERVICES | Same | Check if AWS Brasil or AWS Inc |
| SLACK, NOTION, FIGMA, CANVA | ISS-Import + PIS/COFINS-Import + IRRF + IOF | US entities -- full import service taxation |
| ANTHROPIC, OPENAI, CHATGPT | Same | US entities |
| SPOTIFY, NETFLIX, APPLE (B2C) | These platforms may collect taxes in Brazil directly for B2C | For B2B: check invoice and withholding obligations |

### 3.8 Payment processors

| Pattern | Treatment | Notes |
|---|---|---|
| PAGSEGURO, PAGBANK | EXCLUDE (financial service) or ISS | Payment processing fees -- may be exempt financial service or ISS-taxable depending on characterization |
| STONE, STONE PAGAMENTOS | Same | |
| CIELO | Same | |
| REDE, GETNET | Same | |
| MERCADO PAGO (transaction fees) | EXCLUDE (financial) | Transaction processing commission |
| PAYPAL BRASIL | EXCLUDE (financial) | Payment processing |
| STRIPE (if Brazilian entity) | ISS | If Stripe Brasil: ISS on service fee. If foreign: import service treatment. |

### 3.9 Professional services

| Pattern | Treatment | Taxes | Notes |
|---|---|---|---|
| CONTADOR, CONTABILIDADE, ESCRITORIO CONTABIL | ISS | ISS + PIS/COFINS | Accounting services -- ISS at municipal rate. NFS-e issued. |
| ADVOGADO, ADVOCACIA, ESCRITORIO DE ADVOCACIA | ISS | ISS + PIS/COFINS | Legal services |
| CONSULTORIA | ISS | ISS + PIS/COFINS | Consulting services |
| CARTORIO, TABELIONATO | ISS | ISS | Notarial services |

### 3.10 Payroll and labor (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| FOLHA, SALARIO, HOLERITE | EXCLUDE | Wages -- outside indirect tax scope |
| INSS, PREVIDENCIA | EXCLUDE | Social security |
| FGTS, FUNDO DE GARANTIA | EXCLUDE | Severance fund |
| VALE TRANSPORTE, VT | EXCLUDE | Transport voucher |
| VALE REFEICAO, VR, VALE ALIMENTACAO, VA | EXCLUDE | Meal/food voucher |
| FERIAS, 13o SALARIO, RESCISAO | EXCLUDE | Vacation pay, 13th salary, termination -- labor, not indirect tax |

### 3.11 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| TRANSFERENCIA PROPRIA, MESMA TITULARIDADE | EXCLUDE | Internal account movement |
| TED PROPRIA, PIX PROPRIO | EXCLUDE | Same-owner transfer via PIX or TED |
| APLICACAO, RESGATE, CDB, LCI, LCA | EXCLUDE | Investment application/redemption -- financial, out of scope |
| DIVIDENDO, LUCRO DISTRIBUIDO | EXCLUDE | Profit distribution, out of scope |
| EMPRESTIMO, MUTUO | EXCLUDE | Loan, out of scope |
| SAQUE, SAQUE ATM | Ask | Cash withdrawal -- ask purpose |

---

## Section 4 -- Worked examples

These are six fully worked classifications drawn from a hypothetical bank statement of a Sao Paulo-based self-employed software consultant (pessoa juridica, Lucro Presumido, CNPJ registered).

### Example 1 -- Standard domestic service sale with NFS-e

**Input line:**
`05.04.2026 ; EMPRESA ALFA LTDA ; CREDIT ; NFS-e 2026/041 Consultoria TI abril ; BRL 10,000.00`

**Reasoning:**
Software consulting service. Subject to ISS (not ICMS, because it is a service on LC 116/2003 list). Sao Paulo ISS rate for IT consulting: 2-5% (depends on municipality code). Also subject to PIS/COFINS: cumulative regime (Lucro Presumido) = 0.65% PIS + 3% COFINS = 3.65% on revenue. NFS-e was issued by the client.

**Output:**

| Date | Counterparty | Gross | ISS base | ISS rate | PIS | COFINS | Notes |
|---|---|---|---|---|---|---|---|
| 05.04.2026 | EMPRESA ALFA LTDA | +10,000 | 10,000 | 5% (SP default) | 65.00 | 300.00 | Confirm ISS rate for SP municipality |

### Example 2 -- Interstate goods sale

**Input line:**
`10.04.2026 ; DISTRIBUIDORA BETA SA (RJ) ; CREDIT ; NF-e 001-12345 venda mercadorias ; BRL 50,000.00`

**Reasoning:**
Sale of goods from SP to RJ. Interstate ICMS rate: SP (South/Southeast) to RJ (South/Southeast) = 12%. PIS/COFINS cumulative = 3.65% on gross. IPI: depends on NCM, assume 0% for resale (IPI only on manufactured/imported goods). DIFAL may apply if buyer is final consumer (not in this case -- buyer is a distributor with IE).

**Output:**

| Date | Counterparty | Gross | ICMS rate | ICMS | PIS/COFINS | IPI | Notes |
|---|---|---|---|---|---|---|---|
| 10.04.2026 | DISTRIBUIDORA BETA SA (RJ) | +50,000 | 12% (interstate SP>RJ) | Included in price (por dentro) | 3.65% | 0% (resale) | Verify NF-e and NCM |

### Example 3 -- Imported digital service (SaaS from US)

**Input line:**
`15.04.2026 ; NOTION LABS INC ; DEBIT ; Monthly subscription ; USD 15.00 ; BRL 85.00`

**Reasoning:**
Notion is a US entity. This is an importation of services. Brazilian buyer must self-assess: ISS-Import (SP rate, say 2.9% for IT services), PIS-Import (1.65%), COFINS-Import (7.60%), IRRF (15% withholding on remittance), IOF (0.38% on FX). Total effective tax on the remittance can exceed 25%. No NFS-e from the supplier; buyer's obligation to collect and remit.

**Output:**

| Date | Counterparty | Gross BRL | ISS-Import | PIS-Import | COFINS-Import | IRRF | IOF | Notes |
|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | NOTION LABS INC | -85.00 | ~2.47 | ~1.40 | ~6.46 | ~12.75 | ~0.32 | Imported service -- self-assess all taxes. Confirm ISS rate. |

### Example 4 -- Simples Nacional client sale

**Input line:**
`18.04.2026 ; CLIENTE VAREJO ; CREDIT ; NFC-e venda balcao ; BRL 5,000.00`

**Reasoning:**
If client is Simples Nacional (DAS payer), all taxes (ICMS, ISS, PIS, COFINS, IRPJ, CSLL, CPP) are paid through the unified DAS guia based on revenue band. Anexo I (commerce) or Anexo III/V (services). No separate PIS/COFINS/ICMS/ISS calculation needed -- the DAS covers everything. Effective rate depends on trailing 12-month revenue.

**Output:**

| Date | Counterparty | Gross | Treatment | Notes |
|---|---|---|---|---|
| 18.04.2026 | CLIENTE VAREJO | +5,000 | Simples Nacional -- included in DAS | Calculate DAS based on Anexo and revenue band. No separate ICMS/PIS/COFINS line items. |

### Example 5 -- Entertainment / personal expense

**Input line:**
`22.04.2026 ; RESTAURANTE FOGO DE CHAO ; DEBIT ; Jantar ; BRL 800.00`

**Reasoning:**
Restaurant meal. For PIS/COFINS non-cumulative regime, input credits are available only on items that are inputs to production, goods for resale, electricity, rent, depreciation, and other specified categories. Restaurant meals are not creditable inputs. For ICMS: not applicable (restaurant is a service). For Lucro Presumido (cumulative PIS/COFINS): no input credits at all regardless. Default: no credit recovery.

**Output:**

| Date | Counterparty | Gross | Credit recovery | Notes |
|---|---|---|---|---|
| 22.04.2026 | RESTAURANTE FOGO DE CHAO | -800.00 | None | Entertainment -- no PIS/COFINS credit. Not an ICMS-creditable purchase. |

### Example 6 -- Electricity bill with ICMS

**Input line:**
`28.04.2026 ; ENEL DISTRIBUICAO SP ; DEBIT ; Fatura energia eletrica ; BRL 1,500.00`

**Reasoning:**
Electricity bill. Subject to ICMS at the SP internal rate (18% general, but electricity may have a specific ICMS rate -- often 25% for commercial consumers in SP). PIS/COFINS are also charged on electricity. Under the non-cumulative regime, PIS/COFINS on electricity IS creditable (Lei 10.637/2002, Art. 3, III). Under cumulative regime: no credit. ICMS on electricity generates credit under normal debit/credit rules if the business is an ICMS taxpayer.

**Output:**

| Date | Counterparty | Gross | ICMS credit | PIS/COFINS credit | Notes |
|---|---|---|---|---|---|
| 28.04.2026 | ENEL DISTRIBUICAO SP | -1,500.00 | Yes (if ICMS taxpayer) | Yes (if Lucro Real) / No (if Lucro Presumido) | Check NF-e for exact ICMS and PIS/COFINS amounts |

---

## Section 5 -- Tier 1 classification rules (compressed)

### 5.1 Classification decision tree

Goods = ICMS + IPI (if manufactured/imported) + PIS/COFINS. Services = ISS + PIS/COFINS. Transport/communications = ICMS (not ISS) + PIS/COFINS. ICMS and ISS are mutually exclusive (except mixed supply).

### 5.2 PIS/COFINS regime determination

Lucro Real = non-cumulative (1.65%+7.60% = 9.25%, with input credits). Lucro Presumido = cumulative (0.65%+3.00% = 3.65%, no input credits). Simples Nacional = included in DAS (no separate PIS/COFINS filing). Determine regime FIRST -- it changes the entire calculation.

### 5.3 ICMS internal rates

Rates vary by state from 17% to 23%. Apply the internal rate of the state where the supply occurs. For interstate supplies, use 7% (S/SE to N/NE/CW) or 12% (all other combinations). Imported goods with >40% import content: 4% interstate.

### 5.4 ICMS por dentro calculation

ICMS is calculated inside the price. A nominal 18% rate on a BRL 100 gross price means BRL 18 ICMS is already included (BRL 100 x 18% = BRL 18). The tax-exclusive base is BRL 82; effective rate on tax-exclusive base is ~21.95%.

### 5.5 ISS classification

Services on the LC 116/2003 list (approximately 200 items across 40 sub-items). Rate set by municipality (2-5%). ISS is due at the provider's location except for ~20 specific categories (construction, security, cleaning) where ISS is due at the location of provision.

### 5.6 IPI classification

Applies only to manufactured and imported goods. Rate per NCM code from the TIPI table. Charged outside the price (por fora). Generates credits on manufacturing inputs. Not charged on resale by commercial establishments.

### 5.7 Export treatment

Exports are exempt/zero-rated across all indirect taxes: ICMS exempt (Lei Kandir, LC 87/1996), IPI exempt, PIS/COFINS zero-rated with credit maintenance, ISS exempt (if result occurs abroad). Full input credit preservation.

### 5.8 Import treatment

Goods imports: II (import duty) + IPI + ICMS + PIS-Import (2.1%) + COFINS-Import (9.65% or 10.65%). Service imports: ISS-Import + PIS-Import (1.65%) + COFINS-Import (7.60%) + IRRF (15%/25%) + IOF (0.38%) + possibly CIDE (10% for technology transfer). Total effective tax on imported services can exceed 40%.

### 5.9 NF-e requirements for ICMS/PIS/COFINS credits

Credits require valid NF-e (Model 55 for goods) or NFS-e (for ISS on services where relevant). ICMS credit = ICMS highlighted on the NF-e. PIS/COFINS credit (non-cumulative only) = amounts on NF-e or calculated from creditable items per Lei 10.637/2002 Art. 3 and Lei 10.833/2003 Art. 3.

### 5.10 PIS/COFINS input credits (non-cumulative only)

Creditable items: goods for resale, inputs to manufacturing/production, electricity consumed in production, rent of buildings/machinery used in business, depreciation of fixed assets, freight on purchases. NOT creditable: entertainment, personal expenses, items not directly related to revenue-generating activities.

### 5.11 Simples Nacional treatment

All taxes (ICMS, ISS, PIS, COFINS, IRPJ, CSLL, CPP) paid through DAS guia. Effective rate determined by Anexo (I-V) and trailing 12-month revenue band. No separate ICMS/ISS/PIS/COFINS calculation. Buyer receiving from Simples supplier: limited ICMS credit (percentage shown on NF-e) and limited PIS/COFINS credit.

### 5.12 Transition rules (CBS/IBS, 2026+)

2026: CBS 0.9% + IBS 0.1% apply as test rates alongside existing taxes. These are creditable against existing PIS/COFINS and ICMS/ISS respectively. 2027: CBS replaces PIS/COFINS entirely (old taxes extinguished). 2029-2032: IBS gradually replaces ICMS/ISS. 2033: only CBS+IBS+IS remain. All transition rules are reviewer-judgement-required.

---

## Section 6 -- Tier 2 catalogue (compressed)

### 6.1 Tax regime determination

*Pattern:* client does not know if Lucro Real, Lucro Presumido, or Simples Nacional. *Default:* Lucro Presumido (cumulative, no credits). *Question:* "What is your tax regime? Check your CNPJ card or consult your Contador."

### 6.2 ICMS-ST applicability

*Pattern:* product may be subject to ICMS Substituicao Tributaria. *Default:* assume not subject to ST (flag for reviewer). *Question:* "Is this product subject to ICMS-ST in your state? What is the applicable MVA from the CONFAZ protocol?"

### 6.3 Interstate vs internal supply

*Pattern:* sale or purchase where origin/destination state is unclear. *Default:* internal (apply internal rate). *Question:* "Which state is the buyer/seller located in?"

### 6.4 ISS rate by municipality

*Pattern:* service where the exact municipal ISS rate is unknown. *Default:* 5% (maximum). *Question:* "What municipality governs this service for ISS purposes? What is the applicable ISS rate?"

### 6.5 CBS/IBS transition treatment

*Pattern:* transaction in 2026 where CBS/IBS test rates may apply. *Default:* apply current system only (do not add CBS/IBS without confirmation). *Question:* "Is your NF-e/NFS-e system updated to include CBS/IBS fields? Has your Contador confirmed the transition treatment?"

### 6.6 Imported service withholding

*Pattern:* payment to foreign service provider. *Default:* apply full import taxation (ISS, PIS/COFINS-Import, IRRF at 15%, IOF). *Question:* "Is the foreign provider from a country with a tax treaty? Is this a tax haven jurisdiction (IRRF 25%)?"

### 6.7 Mixed supply (goods + services)

*Pattern:* transaction that includes both goods and services components. *Default:* treat as goods (ICMS, higher rate). *Question:* "Can you separate the goods and services components? The goods portion is subject to ICMS and the services portion to ISS."

### 6.8 Vehicle and fuel

*Pattern:* fuel purchase, vehicle maintenance. *Default:* no credit (flag for reviewer). *Question:* "Is this vehicle used exclusively for the business? Is the fuel for a company vehicle?"

### 6.9 Round-number incoming transfers

*Pattern:* large round credit from owner-named counterparty. *Default:* exclude as capital injection (aporte de socio). *Question:* "Is this a customer payment, capital injection, or loan?"

### 6.10 Cash withdrawals

*Pattern:* saque, saque ATM, saque caixa. *Default:* exclude. *Question:* "What was the cash used for?"

---

## Section 7 -- Excel working paper template (Brazil-specific)

### Sheet "Transactions"

Columns: A (Date), B (Counterparty/CNPJ), C (NF-e/NFS-e number), D (Gross BRL), E (ICMS amount), F (PIS amount), G (COFINS amount), H (ISS amount), I (IPI amount), J (Tax type: ICMS/ISS/Mixed), K (Supply direction: Internal/Interstate/Import/Export), L (Default Y/N), M (Question), N (Notes).

### Sheet "Tax Summary"

Separate sections for each tax:

```
PIS/COFINS:
| Revenue (output PIS/COFINS) | =SUMIFS for credit entries |
| PIS due | =Revenue * PIS rate |
| COFINS due | =Revenue * COFINS rate |
| PIS credits (if non-cumulative) | =SUMIFS for debit entries with PIS credit |
| COFINS credits (if non-cumulative) | =SUMIFS for debit entries with COFINS credit |
| Net PIS | =PIS due - PIS credits |
| Net COFINS | =COFINS due - COFINS credits |

ICMS (if applicable):
| Output ICMS | =SUMIFS for sales ICMS |
| Input ICMS credits | =SUMIFS for purchase ICMS credits |
| Net ICMS | =Output - Input |

ISS (if applicable):
| ISS on services rendered | =SUMIFS for service revenue * ISS rate |
```

### Color and formatting conventions

Blue for hardcoded values from bank statement/NF-e. Black for formulas. Green for cross-sheet references. Yellow background for any row where Default = "Y". Red background for rows requiring state-specific rate verification.

---

## Section 8 -- Brazilian bank statement reading guide (extrato bancario)

**Extrato bancario format conventions.** Brazilian banks export statements in PDF (most common), OFX, CSV, or via internet banking screen. Date format: DD/MM/YYYY. Common columns: Data (date), Historico or Descricao (description), Valor (amount, negative for debits), Saldo (balance). Some banks show Documento (document number) and Agencia/Conta (branch/account).

**PIX transfers.** PIX is the dominant payment method in Brazil (instant 24/7 transfers). PIX entries appear as "PIX RECEBIDO" (received) or "PIX ENVIADO" (sent) with the counterparty name or CNPJ/CPF. Match the counterparty name against Section 3.

**TED and DOC transfers.** Older bank transfer methods. TED entries show the counterparty name and bank. DOC is being phased out. Both appear with a transfer reference number.

**Boleto payments.** Boleto bancario is a common payment instrument. Entries appear as "PAGAMENTO BOLETO" or "LIQUIDACAO BOLETO" with a bar code reference. The payee name may not be visible in the description -- cross-reference with invoices.

**Debito automatico.** Automatic debits (direct debits) for utilities and recurring payments. Show the service provider name: CPFL, VIVO, CLARO, etc.

**Internal transfers and exclusions.** Transfers between the client's own accounts. Labelled "TRANSFERENCIA MESMA TITULARIDADE", "TED PROPRIA", "PIX PROPRIO". Always exclude.

**Owner draws (retirada pro-labore).** Self-employed or company owner withdrawing pro-labore or dividends. Labelled "PRO-LABORE", "DISTRIBUICAO LUCROS", "RETIRADA SOCIO". Exclude -- labor/dividend, not indirect tax.

**Refunds and reversals.** Identified by "ESTORNO", "DEVOLUCAO", "CREDITO ESTORNO". Book as a negative in the same tax treatment as the original transaction.

**Foreign currency transactions.** Convert to BRL at the PTAX rate (Banco Central do Brasil) for the transaction date. IOF (0.38% on FX) applies on the currency conversion.

**Investment entries.** "APLICACAO CDB", "RESGATE LCI", "RENDIMENTO POUPANCA". All financial/investment -- exclude from indirect tax.

**DAS / DARF payments.** "PAGAMENTO DAS" (Simples Nacional), "PAGAMENTO DARF" (federal taxes). Exclude -- these are tax payments, not supplies.

---

## Section 9 -- Onboarding fallback (only when inference fails)

### 9.1 CNPJ and legal entity type
*Inference rule:* CNPJ format (XX.XXX.XXX/YYYY-ZZ) may appear in transfer descriptions. Branch 0001 = headquarters. *Fallback question:* "What is your CNPJ?"

### 9.2 Tax regime
*Inference rule:* DAS payments suggest Simples Nacional. DARF code 5952 suggests PIS non-cumulative (Lucro Real). DARF code 8109 suggests PIS cumulative (Lucro Presumido). *Fallback question:* "Are you Lucro Real, Lucro Presumido, or Simples Nacional?"

### 9.3 State(s) of operation
*Inference rule:* bank branch location, utility providers (CPFL = SP, CEMIG = MG, LIGHT = RJ). *Fallback question:* "In which state(s) do you have inscricao estadual?"

### 9.4 Filing period
*Inference rule:* first and last transaction dates. Monthly filing is standard. *Fallback question:* "Which month does this cover?"

### 9.5 Industry and primary activity
*Inference rule:* counterparty mix, NF-e descriptions, CNAE code on CNPJ card. *Fallback question:* "What is your primary business activity -- goods, services, manufacturing, or mixed?"

### 9.6 Simples Nacional status
*Inference rule:* DAS payments in the statement. *Fallback question:* "Are you registered under Simples Nacional? If so, which Anexo applies?"

### 9.7 Interstate operations
*Inference rule:* counterparties with out-of-state bank branches or addresses. *Fallback question:* "Do you sell to or purchase from other states? Which ones?"

### 9.8 Export activities
*Inference rule:* foreign currency credits, foreign-named counterparties. *Fallback question:* "Do you export goods or services?"

### 9.9 Prior period credits
*Inference rule:* not inferable from single period. Always ask. *Question:* "Do you have PIS/COFINS or ICMS credits carried forward from the prior month?"

### 9.10 NF-e availability
*Inference rule:* if client provides NF-e XMLs or SPED file, answered. *Fallback question:* "Can you provide your NF-e XMLs or SPED fiscal file for this period?"

---

## Section 10 -- Reference material

### Sources

**Primary legislation (current system):**
1. Constituicao Federal -- Articles 153 (IPI, PIS, COFINS), 155 (ICMS), 156 (ISS)
2. Lei Complementar 87/1996 (Lei Kandir) -- ICMS
3. Lei 10.637/2002 -- PIS non-cumulative
4. Lei 10.833/2003 -- COFINS non-cumulative
5. Lei 9.718/1998 -- PIS/COFINS cumulative
6. Lei Complementar 116/2003 -- ISS
7. Decreto 7.212/2010 (RIPI) -- IPI regulation
8. Lei Complementar 123/2006 -- Simples Nacional

**Reform legislation (new system):**
9. Emenda Constitucional 132/2023 -- CBS/IBS/IS constitutional basis
10. Lei Complementar 214/2025 -- CBS/IBS/IS regulation

**Judicial precedents:**
11. STF RE 574.706 -- ICMS exclusion from PIS/COFINS base
12. STF ADIs 1.945 and 5.659 -- Software subject to ISS, not ICMS

**Other:**
13. Receita Federal -- https://www.gov.br/receitafederal
14. CONFAZ -- https://www.confaz.fazenda.gov.br (ICMS agreements)
15. PTAX exchange rate -- Banco Central do Brasil

### Known gaps

1. The supplier pattern library covers common national brands but not regional businesses or state-specific utilities.
2. ICMS-ST MVA percentages are product- and state-specific; this skill does not contain the full CONFAZ protocol database.
3. State-specific ICMS incentive programs (guerra fiscal) are not covered.
4. The CBS/IBS transition is ongoing -- rates and rules may change as regulations are published.
5. The worked examples use a Sao Paulo-based consultant. Other state/municipality combinations may produce different results.
6. Municipal ISS rates are not exhaustively listed -- there are over 5,500 municipalities.

### Change log

- **v2.0 (April 2026):** Full rewrite to Malta v2.0 structure. Quick reference at top (Section 1) with IBS+CBS reform context, current rates, and conservative defaults. Supplier pattern library restructured as literal lookup tables (Section 3) with Brazilian vendors. Six worked examples added (Section 4). Tier 1 rules compressed (Section 5). Tier 2 catalogue added (Section 6). Excel template specification added (Section 7). Brazilian bank statement reading guide (extrato bancario) added (Section 8). Onboarding fallback with inference rules (Section 9).
- **v1.0 (April 2026):** Previous version with full monolithic structure covering all five indirect taxes and reform context.

### Self-check (v2.0)

1. Quick reference at top with all five current taxes and CBS/IBS reform context: yes (Section 1).
2. Conservative defaults with regime-specific treatment: yes (Section 1).
3. Supplier library as literal lookup tables with Brazilian vendors: yes (Section 3, 11 sub-tables).
4. Worked examples from hypothetical SP consultant: yes (Section 4, 6 examples).
5. Tier 1 rules compressed: yes (Section 5, 12 rules).
6. Tier 2 catalogue compressed: yes (Section 6, 10 items).
7. Excel template specification: yes (Section 7).
8. Brazilian bank statement reading guide (extrato bancario): yes (Section 8).
9. Onboarding as fallback with inference rules: yes (Section 9, 10 items).
10. PIS/COFINS cumulative vs non-cumulative distinction explicit: yes (Section 1, 5.2).
11. ICMS por dentro calculation explicit: yes (Section 5.4).
12. Import service taxation (~40% effective) explicit: yes (Section 5.8, Example 3).
13. Simples Nacional DAS treatment explicit: yes (Section 5.11, Example 4).
14. Export zero-rating across all taxes explicit: yes (Section 5.7).
15. Refusal catalogue present: yes (Section 2, R-BR-1 through R-BR-6).

## End of Brazil Indirect Tax Skill v2.0


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
