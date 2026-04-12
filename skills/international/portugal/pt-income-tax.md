---
name: pt-income-tax
description: >
  Use this skill whenever asked about Portuguese individual income tax (IRS) for self-employed individuals (trabalhadores independentes). Trigger on phrases like "how much tax do I pay in Portugal", "IRS", "Modelo 3", "Anexo B", "Categoria B", "regime simplificado", "contabilidade organizada", "retenção na fonte", "trabalhador independente", "recibos verdes", "income tax return Portugal", "NIF", "coeficientes", "IRS Jovem", or any question about filing or computing income tax for a self-employed or freelance client in Portugal. Covers Modelo 3 + Anexo B, Categoria B income, regime simplificado vs contabilidade organizada, progressive IRS brackets (13.25%–48%), adicional de solidariedade, withholding tax (retenção na fonte), IRS Jovem, and filing deadlines.
version: 2.0
---

# Portugal Income Tax — Self-Employed / Trabalhador Independente (IRS Categoria B)

## Section 1 — Quick Reference

### IRS Brackets (2025)
| Rendimento coletável (€) | Taxa marginal | Taxa média |
|---|---|---|
| 0 – 7,703 | 13.25% | 13.25% |
| 7,703 – 11,623 | 18% | — |
| 11,624 – 16,472 | 23% | — |
| 16,473 – 21,321 | 26% | — |
| 21,322 – 27,146 | 32.75% | — |
| 27,147 – 39,791 | 37% | — |
| 39,792 – 51,997 | 43.5% | — |
| 51,998 – 81,199 | 45% | — |
| Above 81,199 | 48% | — |

**Adicional de solidariedade:** 2.5% on income €80,000–€250,000; 5% on income above €250,000

**Taxa de retenção na fonte (withholding rate):**
- Standard for trabalhadores independentes: 25% (on most services paid by companies)
- Specific rates apply for certain activities (e.g., intellectual property: 16.5%)

### Regime Simplificado vs Contabilidade Organizada
| Feature | Regime Simplificado | Contabilidade Organizada |
|---|---|---|
| Revenue threshold | ≤ €200,000 gross | Any revenue (mandatory above €200,000) |
| Tax base | Revenue × coeficiente | Actual revenue − actual expenses |
| Accounting required | Simple receipts register | Full double-entry bookkeeping (TOC required) |
| Deductible expenses | None individually — fixed % | All documented professional expenses |
| Best choice | Low expenses (below coeficiente floor) | High expenses (above coeficiente floor) |

### Regime Simplificado — Coeficientes (2025)
| Activity Category | Coeficiente | Effective deduction |
|---|---|---|
| Vendas (product sales) | 0.15 | 85% deducted |
| Serviços (most services, Art. 151 list) | 0.35 | 65% deducted |
| Other services (not on Art. 151 list) | 0.75 | 25% deducted |
| Atividades hoteleiras / alojamento local | 0.35 | 65% deducted |
| Atividades agrícolas | 0.10 | 90% deducted |
| Propriedade intelectual (royalties) | 0.50 | 50% deducted |
| Subsidies / income from capital | 1.00 | 0% deducted |

**Note on 0.35 services:** This applies to professions listed in Art. 151 CIRS (e.g., consultants, engineers, lawyers, accountants, architects, doctors) — i.e., the professional activities for which IRS withholding rate is 25%. Confirm applicable coeficiente for client's specific CAE/CIRS code.

### Key Deductions (both regimes)
| Deduction | Amount (2025) |
|---|---|
| Mínimo de existência | €10,640 (increases if dependants) |
| Specific deduction (Categoria A — salary, if applicable) | €4,462 or 72% of IAS |
| Despesas de saúde | 15% of medical expenses |
| Despesas de educação | 30% of expenses, max €800 |
| Encargos com habitação | 15% of rent paid, max €600 (tenants) |
| Pensões de alimentos | 20% of maintenance paid |
| Exigência de fatura | 15% deduction credit for invoiced services (restaurants, accommodation, etc.) |
| Contribuições para a segurança social (Categoria B) | 10% of net Categoria B income (limited) |

### IRS Jovem (Young People Tax Exemption)
- Age ≤ 35, first 10 years of work after completing studies
- Partial exemption: Year 1: 100%; Year 2: 75%; Years 3–4: 50%; Years 5–10: 25%
- Applies only to Categoria A or Categoria B income; maximum income ceiling applies

### Conservative Defaults
| Item | Default |
|---|---|
| Regime | Regime simplificado if revenue ≤ €200,000 and no expense documentation |
| Coeficiente | 0.35 for professional services (Art. 151 list) |
| Home office % | Do not assume — ask for floor area |
| Vehicle | Do not assume — ask for km log |
| Phone/internet | 50% if mixed use |

### Red Flag Thresholds
| Situation | Flag |
|---|---|
| Revenue > €200,000 | Must use contabilidade organizada |
| Revenue approaching €200,000 | Warn — threshold exceeded triggers organizada for entire year |
| No recibos verdes issued | Non-compliant — all services require recibo verde |
| Expenses > 65% of revenue | Verify — unusual for most services under simplificado |

---

## Section 2 — Required Inputs & Refusal Catalogue

### Minimum Required Inputs
1. Total gross receipts (rendimentos brutos) for the year
2. Regime: simplificado or contabilidade organizada
3. Activity type / CAE code (to confirm coeficiente)
4. Withholding taxes (retenções na fonte) already deducted
5. Personal situation: dependants, marital status (individual or joint declaration)
6. Segurança Social contributions paid (for deduction)
7. Pagamentos por conta (advance tax payments) made during the year

### Refusal Catalogue
**R-PT-1 — Revenue above simplificado threshold**
If gross revenue > €200,000: cannot use regime simplificado. State: "Your revenue exceeds the €200,000 threshold for regime simplificado. You must use contabilidade organizada with a Técnico Oficial de Contas (TOC)."

**R-PT-2 — No expense documentation (organizada)**
Refuse undocumented expenses. State: "Without receipts and records, we cannot deduct expenses under contabilidade organizada. Only expenses properly documented and relating to business activity are deductible."

**R-PT-3 — Personal expenses as professional costs**
Refuse personal costs. State: "These are personal expenses and cannot be deducted as despesas profissionais under CIRS."

**R-PT-4 — IVA included in rendimentos**
If IVA-registered (NIF sujeito passivo de IVA): gross receipts for IRS must exclude IVA. State: "IVA received from clients is not your income. Rendimentos must be the amount excluding IVA."

**R-PT-5 — NHR regime without confirmation**
If client mentions NHR (Non-Habitual Resident) regime: apply different rules. State: "NHR status changes the tax calculation significantly. Confirm NHR registration before applying standard Categoria B rules."

---

## Section 3 — Transaction Pattern Library

### 3.1 Income Patterns
| Bank Description Pattern | Income Type | Tax Treatment | Notes |
|---|---|---|---|
| Transferência de cliente | Rendimentos Categoria B | Include gross (ex-IVA if registered) | |
| SEPA credit + client name | Professional receipts | Include | |
| Transferência internacional / SWIFT | Foreign client | Include — convert to EUR at receipt date | |
| Stripe pagamento / STRIPE | Platform receipts | Include + Stripe fees as expense | |
| PayPal transferência | Platform receipts | EUR equivalent | |
| Upwork / Fiverr payout | Freelance platform | Gross earnings | |
| Renda recebida | Rendas (Category F) | Separate — Categoria F (or Predial) | Not Categoria B |
| Juros bancários | Juros (Category E) | Separate — usually 28% liberatório | |
| Dividendos | Dividendos (Category E) | Separate — 28% liberatório | |
| Reembolso de despesas (pass-through) | Despesas reembolsadas | Include if in recibo verde; exclude if separate debit note for pass-through costs | |

### 3.2 Expense Patterns (Contabilidade Organizada Only)
| Bank Description Pattern | Expense Category | Deductible? | Notes |
|---|---|---|---|
| NOS / MEO / Vodafone PT | Telefone | Partial — business % | T2 |
| NOS / MEO / Vodafone internet | Internet | Business % | T2 |
| EDP / Endesa / Galp energia | Eletricidade | Home office % | T2 |
| Renda escritório / local profissional | Renda profissional | 100% | Must be professional premises |
| Adobe / Slack / Figma | Software/SaaS | 100% | |
| FNAC / Worten / Auchan | Equipamento | Amortização if >€250 | T2 |
| CP / comboios / metro | Viagens profissionais | 100% — purpose documented | |
| TAP / Ryanair / easyJet | Viagens profissionais | 100% — document | |
| Hotel / Airbnb (viagem profissional) | Alojamento | 100% — professional purpose | |
| Restaurante (jantar com cliente) | Representação | 50% (limite legal) | Document who attended |
| Formação profissional / cursos | Formação | 100% — business-related | |
| Livros / publicações profissionais | Documentação | 100% — professional | |
| Seguro de responsabilidade civil | Seguro profissional | 100% | |
| Contabilista / TOC | Honorários contabilidade | 100% | |
| Segurança Social (trabalhador independente) | Contrib. SS | Deductible — 10% of Categoria B income | See deduction rules |
| IRS pago / pagamentos por conta | Imposto | EXCLUDE — not deductible | |
| IVA entregue ao Estado | IVA | EXCLUDE — not income tax deductible | |

### 3.3 Retenção na Fonte (Withholding Tax Credits)
| Situation | Withholding Rate | Treatment |
|---|---|---|
| Services to corporate clients (Art. 151 list) | 25% | Credit against final IRS |
| Intellectual property / royalties | 16.5% | Credit against final IRS |
| Payments from public entities | 11.5% | Credit against final IRS |
| Foreign client (no Portuguese withholding) | 0% | Include gross income; no credit |

**Gross-up:** If client paid net (withheld 25%): gross = net ÷ 0.75. Always check recibo verde — the recibo verde shows the gross amount.

### 3.4 Foreign Currency & Platform Receipts
| Source | Currency | Treatment |
|---|---|---|
| USD from US clients | USD | Convert to EUR at Banco de Portugal / ECB rate on receipt date |
| GBP from UK | GBP | Convert at receipt date |
| Stripe USD | USD | Use Stripe statement EUR equivalent |
| PayPal multi-currency | Various | PayPal statement EUR equivalent |
| Upwork USD | USD | Convert; platform fee = despesa deducível |
| Google AdSense | USD/EUR | Monthly; convert if USD |

### 3.5 Internal Transfers
| Pattern | Treatment |
|---|---|
| Transferência para poupança | EXCLUDE — internal |
| Pagamento cartão crédito | EXCLUDE — individual expenses captured |
| Entre contas próprias | EXCLUDE |
| Recebimento de empréstimo | EXCLUDE — not income |

---

## Section 4 — Worked Examples

### Example 1 — Millennium BCP: Consultor IT, Regime Simplificado
**Scenario:** IT consultant (Art. 151 list), €75,000 gross receipts, regime simplificado (coeficiente 0.35), retenção na fonte €18,750 (25%)

**Bank statement extract (Millennium BCP):**
```
Data         | Descrição                                  | Débito (€)    | Crédito (€)   | Saldo (€)
15/04/2025   | TRANSF TECHCO CONSULTORIA LDA             |               | 11,250.00     | 52,000.00
20/04/2025   | TRANSF STARTUP LISBOA LDA                 |               |  7,500.00     | 59,500.00
25/04/2025   | DB ADOBE SYSTEMS                          | 65.00         |               | 59,435.00
28/04/2025   | DB NOS COMUNICAÇÕES                       | 45.00         |               | 59,390.00
30/04/2025   | COMISSÃO BANCÁRIA                         | 8.50          |               | 59,381.50
```

**Note on credits:** €11,250 received = €15,000 gross − 25% retenção €3,750. Always gross up from recibo verde.

**Regime Simplificado Computation:**
| Linha | Valor |
|---|---|
| Rendimentos brutos Categoria B | €75,000 |
| Rendimento tributável: €75,000 × 0.35 | €26,250 |
| Mínimo de existência (se aplicável) | (€10,640) |
| **Rendimento coletável** | **€15,610** |
| IRS: 13.25% × €7,703 + 18% × €7,907 | €1,021 + €1,423 = **€2,444** |
| Less: retenção na fonte crédito | (€18,750) |
| **IRS a pagar / reembolso** | **Reembolso de €16,306** |

### Example 2 — Caixa Geral de Depósitos (CGD): Designer, Contabilidade Organizada
**Scenario:** Designer, €55,000 receipts, contabilidade organizada, actual expenses €18,000, no withholding (mostly foreign clients)

**Bank statement extract (CGD):**
```
Data valor   | Descrição                                  | Débito (€)    | Crédito (€)   | Saldo (€)
10/03/2025   | TRANSF RECEBIDA LONDON STUDIO UK          |               | 12,000.00     | 38,500.00
15/03/2025   | TRANSF RECEBIDA STARTUP PORTO             |               |  4,250.00     | 42,750.00
20/03/2025   | DB FIGMA INTERNET SERVICES                | 45.00         |               | 42,705.00
22/03/2025   | DB TRANSPORTES URBANOS (MTS PORTO)        | 120.00        |               | 42,585.00
28/03/2025   | ENCARGO CGD CONTA                         | 7.00          |               | 42,578.00
```

**Contabilidade Organizada:**
| Linha | Valor |
|---|---|
| Rendimentos brutos | €55,000 |
| Despesas profissionais | (€18,000) |
| Rendimento líquido | €37,000 |
| Contribuições SS (10% limite aplicado) | (€3,700) |
| **Rendimento coletável** | **€33,300** |
| IRS progressive: ~€6,800 | |
| Retenção na fonte (foreign: €0) | €0 |
| **IRS a pagar** | **~€6,800** |

### Example 3 — Banco Santander Totta: Arquiteto com Retenção
**Scenario:** Arquiteto, €90,000 rendimentos (companies deducted 25% = €22,500 withheld), regime simplificado, married with 2 children

**Bank statement extract (Santander Totta):**
```
Data         | Descrição                                  | Débito (€)    | Crédito (€)   | Saldo (€)
08/05/2025   | TRF ENT URBANISMO CONSTRUTORA SA          |               | 22,500.00     | 98,000.00
12/05/2025   | TRF ENT PROJECTOS ARQUITECTURA LDA        |               | 15,000.00     | 113,000.00
15/05/2025   | DB SEGURANÇA SOCIAL (SS)                  | 1,200.00      |               | 111,800.00
20/05/2025   | DB EDP COMERCIAL                          | 185.00        |               | 111,615.00
25/05/2025   | COMISSÃO SANTANDER                        | 12.00         |               | 111,603.00
```

**Note:** €22,500 deposited = gross €30,000 − 25% withholding €7,500.

**Regime Simplificado:**
| Linha | Valor |
|---|---|
| Rendimentos brutos (Arquitetura — Art. 151 → coef. 0.35) | €90,000 |
| Rendimento tributável: €90,000 × 0.35 | €31,500 |
| **Rendimento coletável (casado 2 filhos — quotient aplicado)** | €31,500 |
| IRS (taxa aplicável ao conjunto, dividida por 2) | calculate on €15,750 per half |
| Tax per half: 13.25%×7,703 + 18%×8,047 | €1,021 + €1,448 = €2,469 |
| × 2 = | **€4,938** |
| Retenção creditada | (€22,500) |
| **Reembolso** | **€17,562** |

### Example 4 — BPI (Banco BPI): Freelancer com Home Office
**Scenario:** Copywriter, €32,000 rendimentos, contabilidade organizada (escolhida para maior controlo), home office (apartamento 65m², escritório 10m²)

**Bank statement extract (BPI):**
```
Data operação | Descrição                                 | Débito (€)    | Crédito (€)   | Saldo (€)
05/06/2025    | TRANSF. RECEBIDA EDITORA PRESENÇA        |               | 5,500.00      | 19,000.00
10/06/2025    | TRANSF. RECEBIDA AGÊNCIA PALAVRAS        |               | 3,200.00      | 22,200.00
15/06/2025    | DB RENDA HABITAÇÃO                       | 850.00        |               | 21,350.00
20/06/2025    | DB NOS FIBRA                             | 35.00         |               | 21,315.00
25/06/2025    | COMISSÃO MANUTENÇÃO CONTA BPI            | 6.00          |               | 21,309.00
```

**Home office (escritório a domicílio):**
- % profissional: 10/65 = 15.4%
- Renda anual €10,200 × 15.4% = €1,571
- Eletricidade €1,560 × 15.4% = €240
- Internet €420 × 15.4% = €65

**Contabilidade organizada:**
| Linha | Valor |
|---|---|
| Rendimentos brutos | €32,000 |
| Despesas diretas | (€3,200) |
| Home office (renda + eletricidade + internet) | (€1,876) |
| Rendimento líquido | €26,924 |
| Contribuições SS | (€2,692) |
| **Rendimento coletável** | **€24,232** |
| IRS: 13.25%×7,703 + 18%×3,920 + 23%×7,849 + 26%×4,760 | €1,021 + €706 + €1,805 + €1,238 = **€4,770** |

### Example 5 — ActivoBank: Programador, IRS Jovem
**Scenario:** Developer, age 27, 2nd year of professional activity after graduation, €48,000 rendimentos, IRS Jovem applies

**Bank statement extract (ActivoBank):**
```
Data         | Descrição                                  | Débito (€)    | Crédito (€)   | Saldo (€)
12/07/2025   | TRANSFERÊNCIA FINTECH STARTUP              |               | 12,000.00     | 38,000.00
18/07/2025   | TRANSFERÊNCIA AGÊNCIA TECH                |               |  8,000.00     | 46,000.00
22/07/2025   | DÉBITO GITHUB ENTERPRISE                  | 180.00        |               | 45,820.00
26/07/2025   | DÉBITO JETBRAINS                          | 120.00        |               | 45,700.00
30/07/2025   | DÉBITO ACTIVOBANK MENSALIDADE              | 5.00          |               | 45,695.00
```

**IRS Jovem — Year 2: 75% exemption**
- Rendimento bruto Categoria B: €48,000
- Rendimento tributável (coef. 0.35): €16,800
- IRS Jovem exemption Year 2: 75% exempt → only 25% taxable
- Rendimento tributável após IRS Jovem: €16,800 × 25% = **€4,200**
- IRS: €4,200 × 13.25% = **€556.50**

**Savings vs no IRS Jovem:** Without exemption: IRS ~€1,700. Saving: ~€1,143.

### Example 6 — Montepio: Consultora com Pagamentos por Conta
**Scenario:** Management consultant, €130,000 rendimentos, regime simplificado, pagamentos por conta €8,000 already paid

**Bank statement extract (Montepio):**
```
Data         | Descrição                                  | Débito (€)    | Crédito (€)   | Saldo (€)
03/08/2025   | TRANSFERÊNCIA GRUPO EMPRESARIAL SA        |               | 30,000.00     | 185,000.00
10/08/2025   | TRANSFERÊNCIA CONSULTORIA IBÉRICA LDA     |               | 15,000.00     | 200,000.00
15/08/2025   | PAGAMENTO POR CONTA IRS AT                | 4,000.00      |               | 196,000.00
20/08/2025   | DB VODAFONE NEGÓCIOS                      | 65.00         |               | 195,935.00
25/08/2025   | COMISSÃO MONTEPIO                         | 9.50          |               | 195,925.50
```

**Regime Simplificado:**
| Linha | Valor |
|---|---|
| Rendimentos brutos (€130,000 × 0.35) | €45,500 |
| Contribuições SS approx. | (€4,550) |
| Rendimento coletável | ~€40,950 |
| IRS (progressive): approx. | €10,200 |
| Retenção na fonte creditada | (€32,500) |
| Pagamentos por conta creditados | (€8,000) |
| **Reembolso** | **~€30,300** |

---

## Section 5 — Tier 1 Rules (Compressed Reference)

### Residência Fiscal
- **Residente em Portugal:** Permanência > 183 dias no ano, OU habitação permanente em Portugal em 31 de dezembro → rendimentos mundiais tributados em Portugal
- **Não residente:** Apenas rendimentos de fonte portuguesa; taxas especiais; formulários diferentes (Modelo 3 – Anexo J)

### Recibos Verdes (Green Receipts)
- Todos os trabalhadores independentes devem emitir recibo verde por cada prestação de serviços
- Emissão obrigatória via portal das Finanças (e-fatura)
- O recibo verde documenta: montante bruto, retenção na fonte, valor líquido
- Empresas clientes retêm 25% e entregam à AT

### Segurança Social — Trabalhador Independente
- Contribuição de 21.4% de rendimentos relevantes (base = 70% dos rendimentos tributáveis do trimestre anterior)
- Isenção nos primeiros 12 meses de atividade (em regra)
- Contribuições SS → parcialmente deductíveis no IRS (10% limite)

### Pagamentos por Conta (Advance Tax)
- Obrigatórios se coleta IRS do ano anterior > €1,000
- 3 pagamentos: julho, setembro, dezembro
- Cada um = 1/3 de (coleta anterior × 75%) ajustado pelo coeficiente de variação de rendimentos

### Mínimo de Existência
- Rendimento líquido total < €10,640: zero IRS applies
- Proteção básica garantida pela legislação fiscal

### Scadenze (Filing Deadlines)
| Evento | Prazo |
|---|---|
| Entrega Modelo 3 IRS | Abril 1 – junho 30 (ano seguinte) |
| Pagamento IRS ou reembolso | Agosto (após apuramento AT) |
| Pagamentos por conta | Julho 31 / Setembro 30 / Dezembro 15 |
| Alteração de atividade / CAE | Em caso de mudança — informar AT |

### Penalidades
| Situação | Penalidade |
|---|---|
| Entrega tardia Modelo 3 | €200 – €2,500 |
| Falta de entrega | €375 – €22,500 |
| Declaração incorreta | 15%–60% do imposto em falta |
| Atraso no pagamento | Juros compensatórios 4% + juros de mora |

---

## Section 6 — Tier 2 Catalogue

### T2-PT-1: Escritório em Casa (Home Office)
**Porquê T2:** A proporção de uso profissional depende de dados que só o cliente conhece.

**Método:** m² escritório ÷ m² total × renda/eletricidade/internet
**Exigências:** m² total da habitação, m² do escritório dedicado, confirmação de uso exclusivamente profissional.
**Aviso:** A AT pode questionar se o escritório é partilhado com o espaço pessoal. Documentar adequadamente.

### T2-PT-2: Viatura (Uso Profissional)
**Porquê T2:** A proporção km profissional/total é um dado que só o cliente detém.

**Opções:**
1. **Tabela ANSR / baremo de km:** Registar km profissionais; custo por km segundo tabela
2. **Custos reais × % profissional:** Documentar km totais e profissionais
3. **Viatura afeta ao estabelecimento:** Custo integral com amortização; bijtelling-equivalent para uso pessoal

**Exige do cliente:** Marca/modelo/cilindrada, km totais, km profissionais, custos (combustível, seguro, manutenção).

### T2-PT-3: Telefone e Internet
**Porquê T2:** Divisão pessoal/profissional é específica do cliente.

**Orientação:** Linha profissional dedicada: 100%. Uso misto: % profissional estimada (50% default).

### T2-PT-4: Representação (Refeições com Clientes)
**Porquê T2:** A identidade dos clientes presentes e o objetivo profissional devem ser fornecidos pelo cliente.

**Regra:** 50% do custo de refeições de representação é dedutível (com fatura em nome da empresa/NIF profissional).
**Exige do cliente:** Para cada despesa — lista de pessoas presentes, objetivo profissional, valor.

### T2-PT-5: Escolha de Regime (Simplificado vs Organizado)
**Porquê T2:** A escolha ótima depende das despesas reais do cliente — dados que devem ser verificados.

**Processo de comparação:**
1. Calcular rendimento tributável regime simplificado: rendimentos × coeficiente
2. Calcular rendimento tributável organizado: rendimentos − despesas reais
3. Comparar: se despesas reais > (1 − coeficiente) × rendimentos → organizado vence
4. Para serviços 0.35: despesas reais > 65% → organizado vence

---

## Section 7 — Excel Working Paper

### Folha 1: Rendimentos
| Coluna | Conteúdo |
|---|---|
| A | Data recebimento |
| B | Cliente |
| C | N.º Recibo Verde |
| D | Valor bruto (€) |
| E | Retenção na fonte (€) |
| F | Valor líquido recebido |
| G | Categoria (Categoria B / Outro / Excluir) |

**Total rendimentos brutos:** `=SUMIF(G:G,"Categoria B",D:D)`
**Total retenções:** `=SUMIF(G:G,"Categoria B",E:E)`

### Folha 2: Despesas (Contabilidade Organizada)
| Coluna | Conteúdo |
|---|---|
| A | Data |
| B | Fornecedor |
| C | Valor (€) |
| D | Categoria de despesa |
| E | % profissional |
| F | Valor dedutível (=C×E) |
| G | Referência do documento |

### Folha 3: Apuramento IRS
| Linha | Valor |
|---|---|
| Rendimentos brutos Categoria B | |
| Rendimento tributável (× coeficiente OU − despesas reais) | |
| Contribuições SS (10% limite) | |
| Rendimento coletável | |
| IRS bruto (tabela progressiva) | |
| Deduções à coleta (saúde, educação, etc.) | |
| IRS líquido | |
| Retenções na fonte | |
| Pagamentos por conta | |
| **IRS a pagar / reembolso** | |

---

## Section 8 — Bank Statement Reading Guide

### Millennium BCP
- Format: `Data | Descrição | Débito (€) | Crédito (€) | Saldo (€)`
- Date: DD/MM/YYYY
- Income = Crédito column
- "TRANSF" = transferência (wire received)

### Caixa Geral de Depósitos (CGD)
- Format: `Data valor | Descrição | Débito (€) | Crédito (€) | Saldo (€)`
- Date: DD/MM/YYYY
- Income = Crédito; "TRANSF RECEBIDA" = incoming transfer

### Santander Totta
- Format: `Data | Descrição | Débito (€) | Crédito (€) | Saldo (€)`
- Date: DD/MM/YYYY
- "TRF ENT" = transferência entrada (incoming)

### BPI (Banco BPI)
- Format: `Data operação | Descrição | Débito (€) | Crédito (€) | Saldo (€)`
- Date: DD/MM/YYYY
- "TRANSF. RECEBIDA" = incoming

### ActivoBank
- Format: `Data | Descrição | Débito (€) | Crédito (€) | Saldo (€)`
- Date: DD/MM/YYYY

### Montepio
- Format: `Data | Descrição | Débito (€) | Crédito (€) | Saldo (€)`
- Date: DD/MM/YYYY

### Exclusion Patterns (all Portuguese banks)
| Padrão | Ação |
|---|---|
| Transferência para poupança | EXCLUIR |
| Pagamento cartão crédito | EXCLUIR — despesas capturadas individualmente |
| IVA entregue (DB AT/IVA) | EXCLUIR — IVA não é imposto sobre o rendimento |
| PGTO IRS AT / pagamento por conta | EXCLUIR de despesas — crédito na declaração |
| Transferência entre contas próprias | EXCLUIR |
| Levantamento ATM | EXCLUIR |

---

## Section 9 — Onboarding Fallback

**Prioridade 1 (bloqueante):**
1. "Qual foi o total dos seus rendimentos brutos (Categoria B) no ano fiscal?"
2. "Qual o seu regime: simplificado ou contabilidade organizada?"
3. "Qual é a sua atividade profissional / código CAE ou Art. 151 CIRS?"

**Prioridade 2 (para cálculo exato):**
4. "Tem faturas/recibos para todas as despesas profissionais?"
5. "As empresas clientes retiveram 25% na fonte? Tem os comprovativos de retenção?"
6. "Qual o seu estado civil? Tem dependentes (filhos, etc.)?"
7. "Contribuiu para a Segurança Social como trabalhador independente? Quanto pagou?"

**Prioridade 3 (deduções adicionais):**
8. "Efectuou pagamentos por conta ao longo do ano? Valores e datas?"
9. "Tem despesas de saúde, educação, habitação significativas para deduções à coleta?"
10. "Tem idade ≤ 35 anos e está nos primeiros 10 anos de atividade profissional após conclusão de estudos? (IRS Jovem)"

**Abordagem conservadora:**
- Usar regime simplificado se receitas ≤ €200,000 e sem documentação de despesas
- Não incluir despesas não documentadas
- Excluir home office se não confirmados dados de área

---

## Section 10 — Reference Material

### Formulários Principais
| Formulário | Finalidade |
|---|---|
| Modelo 3 | Declaração de rendimentos IRS anual |
| Anexo B | Rendimentos Categoria B (trabalhadores independentes) |
| Anexo H | Benefícios fiscais e deduções |
| Anexo J | Rendimentos obtidos no estrangeiro |
| Modelo 3 (Categoria F) | Rendas (propriedade) |

### Portal das Finanças
- **e-Fatura:** Portal para emissão de recibos verdes e faturas
- **IRS Automático:** Sistema pre-filled para contribuintes com rendimentos simples
- **Autenticação:** NIF + senha, ou Chave Móvel Digital

### Referências Legislativas
- CIRS Art. 31: Coeficientes regime simplificado
- CIRS Art. 151: Lista de atividades profissionais (tabela de retenção 25%)
- CIRS Art. 33: Despesas dedutíveis (contabilidade organizada)
- AT (Autoridade Tributária): portaldasfinancas.gov.pt

---

## Prohibitions
- Do not advise on IVA (imposto sobre o valor acrescentado) registration, rates, or filing — separate Portugal IVA skill required
- Do not advise on IRC (imposto sobre o rendimento das pessoas coletivas / corporate tax) — this skill covers individual taxpayers only
- Do not advise on IMI (property tax), IMT (transfer tax), or IS (stamp duty)
- Do not advise on NHR regime (Non-Habitual Resident) — complex separate regime requiring dedicated analysis
- Do not guarantee AT acceptance of any position — every situation is subject to audit

## Disclaimer
This skill provides general guidance for informational and planning purposes. It does not constitute tax advice. Portuguese tax law is administered by the Autoridade Tributária e Aduaneira (AT). Clients should consult a Contabilista Certificado (CC) or tax advisor for advice specific to their circumstances. IRS brackets, coeficientes, and deductions change annually — verify current rules at portaldasfinancas.gov.pt.
