---
name: br-income-tax
description: >
  Use this skill whenever asked about Brazilian individual income tax for self-employed individuals (autônomos / profissionais liberais). Trigger on phrases like "how much tax do I pay in Brazil", "DIRPF", "IRPF", "Carnê-Leão", "livro caixa", "imposto de renda", "CPF", "income tax return Brazil", "deductible expenses Brazil", "self-employed tax Brazil", "Simples Nacional", "MEI", or any question about filing or computing income tax for a self-employed or freelance client in Brazil. Covers DIRPF annual return, Carnê-Leão monthly IRPF, progressive brackets (7.5%–27.5%), livro caixa, Simples Nacional comparison, INSS contribuição individual, ISS municipio, and penalties.
version: 2.0
---

# Brazil Income Tax — Self-Employed / Autônomo (IRPF / DIRPF)

## Section 1 — Quick Reference

### IRPF Brackets (2025 — base cálculo mensal e anual)
**Monthly brackets (Carnê-Leão, applied to monthly net income):**
| Base de cálculo mensal (BRL) | Alíquota | Dedução |
|---|---|---|
| 0 – R$2,259.20 | Isento | — |
| R$2,259.21 – R$2,828.65 | 7.5% | R$169.44 |
| R$2,828.66 – R$3,751.05 | 15% | R$381.44 |
| R$3,751.06 – R$4,664.68 | 22.5% | R$662.77 |
| Above R$4,664.68 | 27.5% | R$896.00 |

**Annual brackets (DIRPF — base de cálculo anual):**
| Base de cálculo anual (BRL) | Alíquota | Dedução |
|---|---|---|
| 0 – R$27,110.40 | Isento | — |
| R$27,110.41 – R$33,919.80 | 7.5% | R$2,033.28 |
| R$33,919.81 – R$45,012.60 | 15% | R$4,577.27 |
| R$45,012.61 – R$55,976.16 | 22.5% | R$7,953.44 |
| Above R$55,976.16 | 27.5% | R$10,752.77 |

**Formula:** (Base × alíquota) − dedução = IRPF

### Key Deductions (Deduções Permitidas — DIRPF)
| Dedução | Valor / Regra |
|---|---|
| Dependentes | R$2,275.08 por dependente por ano |
| Despesas médicas e odontológicas | Ilimitadas — com comprovante |
| Contribuição ao INSS | 100% do valor pago (contribuição individual) |
| Previdência privada (PGBL) | Até 12% da renda tributável bruta |
| Pensão alimentícia judicial | 100% |
| Instrução (educação) | Até R$3,561.50 por ano por pessoa |
| Livro caixa (autônomo) | Despesas profissionais documentadas |
| Desconto simplificado | 20% da renda tributável bruta (max R$16,754.34) — em substituição às deduções reais |

### Regime de Tributação — Autônomo vs Simples Nacional
| Característica | Autônomo / IRPF | MEI | Simples Nacional (ME/EPP) |
|---|---|---|---|
| Faturamento máximo | Ilimitado (IRPF aplica-se) | R$81.000/ano | R$4.800.000/ano |
| Tributação | IRPF progressivo (7.5%–27.5%) | DASN fixo mensal (R$67–R$72/mês) | DAS unificado (4%–22,5% faixa) |
| ISS | Municipal + ISSQN | Incluso no MEI | Incluso no Simples |
| INSS | Contribuição individual 20% ou 11% | Incluso no MEI | Incluso no Simples |
| Livro caixa | Obrigatório | Não | Contabilidade separada |
| Melhor para | Profissional liberal com alto rendimento variável | Microempreendedor < R$81K | Empresa em crescimento |

### Carnê-Leão (Monthly Self-Assessment)
- Obrigatório para autônomos que recebem de **pessoas físicas** (individual clients) e/ou clientes do **exterior**
- **Prazo:** Até o último dia útil do mês seguinte (pagamento via DARF)
- Código DARF: 0190 (Carnê-Leão)
- **Quando não é obrigatório:** Se o pagador é pessoa jurídica (company) e já faz retenção na fonte (IRRF 1.5%–2.5%)

### Conservative Defaults
| Item | Default |
|---|---|
| Home office | Não assumir — perguntar % área |
| Vehicle % | Não assumir — solicitar km logbook |
| Telefone/internet | 50% se uso misto |
| Desconto simplificado vs real | Calcular ambos — usar o maior |
| INSS modalidade | 20% contribuição individual (default); checar se optou por 11% (plano básico) |

### Red Flag Thresholds
| Situação | Flag |
|---|---|
| Faturamento > R$81.000/ano | MEI não aplicável |
| Faturamento > R$360.000/ano | Faixa Simples Nacional muda |
| Rendimentos sem retenção de PF | Carnê-Leão obrigatório |
| Rendimentos do exterior | Carnê-Leão obrigatório |
| Despesas > 70% da receita | Alto — verificar documentação |

---

## Section 2 — Required Inputs & Refusal Catalogue

### Minimum Required Inputs
1. Total gross income (rendimentos brutos) for the year — from all sources
2. Whether income received from individuals (PF) or companies (PJ) — determines Carnê-Leão obligation
3. IRRF (imposto retido na fonte) already withheld by payers
4. INSS contributions paid (contribuição individual)
5. Livro caixa expenses (if autônomo using real deductions)
6. Personal deductions: dependants, medical, education, private pension (PGBL)
7. Carnê-Leão payments already made during the year

### Refusal Catalogue
**R-BR-1 — No livro caixa documentation**
If client claims real deductions but has no records: refuse those deductions. State: "Without a properly maintained livro caixa with receipts, we cannot claim professional expenses as deductions. Consider the desconto simplificado (20%) instead."

**R-BR-2 — Medical expenses without receipts**
Medical deductions are unlimited but require receipts with CPF of healthcare provider. State: "Medical deductions require receipts (recibos) with the provider's CPF/CNPJ. Without these, we cannot include medical expenses."

**R-BR-3 — Personal expenses as professional costs**
Refuse personal costs in the livro caixa. State: "Only expenses directly related to earning your professional income can be included in the livro caixa. Personal expenses are not deductible."

**R-BR-4 — Carnê-Leão not paid**
If autônomo received income from PF clients and did not pay Carnê-Leão monthly: flag the outstanding obligation. State: "Carnê-Leão was due monthly on income from individual (PF) clients. Outstanding amounts must be calculated and paid via DARF with applicable late fees."

**R-BR-5 — Offshore income omitted**
If client has income from foreign clients not reported: flag. State: "Income from overseas clients (including USD, EUR) is subject to Carnê-Leão in Brazil. All foreign-source income must be reported in your DIRPF."

---

## Section 3 — Transaction Pattern Library

### 3.1 Income Patterns
| Bank Description Pattern | Income Type | Tax Treatment | Notes |
|---|---|---|---|
| TED / DOC de cliente PJ | Rendimentos de PJ | IRRF retido pelo pagador (1.5%–2.5%) | Comprovar com informe de rendimentos |
| PIX de cliente PJ | Rendimentos de PJ | Mesmo tratamento TED | |
| PIX / TED de pessoa física | Rendimentos de PF | Carnê-Leão mensal obrigatório | Não há retenção na fonte |
| Remessa internacional / SWIFT | Rendimentos exterior | Carnê-Leão mensal obrigatório | Converter para BRL na data do recebimento (PTAX) |
| Stripe / PayPal pagamento | Rendimentos exterior | Carnê-Leão | Usar extrato da plataforma |
| Upwork / Fiverr liquidação | Plataforma internacional | Carnê-Leão | Taxa plataforma = despesa no livro caixa |
| Aluguel recebido (pessoa física) | Rendimentos de aluguel | Carnê-Leão | Categoria separada — rendimento de aluguel |
| Juros / rendimentos poupança | Rendimentos de capital | Já tributados (IR na fonte / alíquota regressiva) | |
| Dividendos (2024+) | Dividendos | Tributados na fonte (10% proposta — verificar legislação vigente) | |
| Transferência própria | — | EXCLUIR | |

### 3.2 Expense Patterns (Livro Caixa — Autônomo)
| Bank Description Pattern | Categoria | Dedutível? | Observação |
|---|---|---|---|
| Vivo / Claro / Tim / Oi / TIM | Telefone | Parcial — % profissional | T2 |
| NET / Claro internet / Tim Fibra | Internet | % profissional | T2 |
| Cemig / Enel / Copel / Light | Energia elétrica | % escritório | T2 |
| SABESP / Cedae / Copasa | Água | % escritório | T2 |
| Aluguel escritório (CNPJ locadora) | Aluguel profissional | 100% | Precisa de recibo/nota |
| Amazon.com.br / Mercado Livre | Material de escritório | Sim — uso profissional | Guardar NF/comprovante |
| Adobe / Slack / Notion / GitHub | Software / SaaS | Sim — 100% | |
| Latam / Gol / Azul (viagem profissional) | Passagens aéreas | Sim — propósito profissional | Documentar |
| Hotel / Airbnb (viagem profissional) | Hospedagem | Sim | |
| Restaurante (reunião profissional) | Refeições profissionais | Sim — com cliente | Documentar |
| Livros / cursos profissionais | Formação | Sim — relacionados à atividade | |
| Seguro profissional (responsabilidade civil) | Seguro | Sim | |
| Contador / advogado | Honorários profissionais | Sim | |
| INSS contribuição individual | Previdência | Deduível na DIRPF (não no livro caixa) | Quadro separado na DIRPF |
| PGBL / previdência privada | Previdência privada | Até 12% da renda tributável na DIRPF | Não no livro caixa |
| IRPF / DARF pagamentos | Imposto | EXCLUIR — não dedutível | |
| ISS municipal (DARF / guia) | ISS | Dedutível no livro caixa | ISS sobre serviços prestados |
| IOF | IOF | Depende — IOF em câmbio pode ser custo do câmbio | |
| Cartão de crédito (débito) | — | EXCLUIR — despesas individuais já capturadas | |

### 3.3 Retenção na Fonte (IRRF) — Créditos
| Situação | Alíquota IRRF | Tratamento |
|---|---|---|
| Serviços para pessoa jurídica (PJ) | 1.5% ou 2.5% (depende do serviço) | Crédito no DIRPF — informe de rendimentos do pagador |
| Serviços de assessoria | 1.5% | Crédito |
| Serviços técnicos / IT / engenharia | 1.5% | Crédito |
| Comissões | 2.5% | Crédito |
| Rendimentos sem retenção (PF cliente) | 0% | Carnê-Leão due |
| Exterior (wire) | 0% retido no Brasil | Carnê-Leão obrigatório |

### 3.4 Câmbio e Plataformas Internacionais
| Fonte | Moeda | Tratamento |
|---|---|---|
| USD de clientes EUA | USD | Converter pela PTAX do Banco Central na data do recebimento |
| EUR de clientes europeus | EUR | PTAX na data de recebimento |
| Stripe USD | USD | Usar saldo em BRL do extrato Stripe ou converter PTAX |
| PayPal | USD/multi | Usar conversão do PayPal ou PTAX |
| Upwork / Fiverr | USD | Gross USD; converter; taxa plataforma = despesa |
| Google AdSense | USD | Mensal — converter PTAX |

### 3.5 Transferências Internas
| Padrão | Tratamento |
|---|---|
| TED / PIX para conta poupança própria | EXCLUIR |
| Retirada para uso pessoal (pro-labore informal) | EXCLUIR — não é despesa |
| Pagamento fatura cartão | EXCLUIR — despesas já capturadas individualmente |
| Aporte de sócio / empréstimo pessoal | EXCLUIR — não é receita |

---

## Section 4 — Worked Examples

### Example 1 — Itaú Unibanco: Consultor de TI, Rendimentos PJ + Carnê-Leão PF
**Scenario:** IT consultant, R$180,000 PJ income (1.5% IRRF = R$2,700 retido), R$36,000 PF client income (Carnê-Leão required), INSS R$14,016, livro caixa R$25,000

**Bank statement extract (Itaú Personnalité):**
```
Data          | Histórico                                  | Débito (R$)   | Crédito (R$)  | Saldo (R$)
15/04/2025    | TED REC TECHCORP BRASIL LTDA              |               | 13,250.00     | 84,500.00
20/04/2025    | PIX REC DR JOAO SILVA                    |               |  3,000.00     | 87,500.00
25/04/2025    | DARF CARNE LEAO 0190                     | 375.00        |               | 87,125.00
28/04/2025    | DEBITO DAS INSS CONTRIB IND              | 1,168.00      |               | 85,957.00
30/04/2025    | TARIFA SERVICOS ITAU                     | 35.00         |               | 85,922.00
```

**Nota:** TED de R$13,250 = R$15,000 bruto − 1.5% IRRF R$225. PJ sempre retém.

**DIRPF Computation:**
| Linha | Valor |
|---|---|
| Rendimentos de PJ (bruto) | R$180,000 |
| Rendimentos de PF (bruto) | R$36,000 |
| **Total rendimentos tributáveis** | **R$216,000** |
| Livro caixa (despesas profissionais) | (R$25,000) |
| INSS contribuição individual | (R$14,016) |
| Dependente (1 filho) | (R$2,275) |
| **Base de cálculo** | **R$174,709** |
| IRPF: 27.5% × R$174,709 − R$10,752.77 | R$48,045 − R$10,753 = **R$37,292** |
| Créditos: IRRF PJ (R$2,700) + Carnê-Leão pago (R$5,400 est.) | (R$8,100) |
| **IRPF a pagar** | **~R$29,192** |

### Example 2 — Bradesco: Designer, Desconto Simplificado vs Real
**Scenario:** Designer freelancer, R$72,000 rendimentos (tudo PF clientes), R$12,000 despesas documentadas, single

**Bank statement extract (Bradesco Prime):**
```
Data          | Histórico                                  | Débito (R$)   | Crédito (R$)  | Saldo (R$)
10/03/2025    | PIX RECEBIDO AGENCIA CRIATIVA             |               | 8,500.00      | 32,100.00
15/03/2025    | PIX RECEBIDO STUDIO DESIGN               |               | 4,200.00      | 36,300.00
20/03/2025    | DEB ADOBE CREATIVE CLOUD                  | 145.00        |               | 36,155.00
22/03/2025    | DEB FIGMA INC                            | 45.00         |               | 36,110.00
28/03/2025    | TARIFAS BRADESCO                          | 20.00         |               | 36,090.00
```

**Comparação:**
| | Desconto Simplificado | Deduções Reais |
|---|---|---|
| Rendimentos | R$72,000 | R$72,000 |
| Dedução | 20% = R$14,400 | Livro caixa R$12,000 |
| INSS (ambos) | (R$7,920) | (R$7,920) |
| Base de cálculo | R$49,680 | R$52,080 |
| IRPF (27.5% − dedução) | ~R$5,913 | ~R$6,548 |
| **Vencedor** | **Desconto Simplificado** | — |

**Regra:** Se despesas reais < 20% dos rendimentos → desconto simplificado é melhor.

### Example 3 — Banco do Brasil: Médico, Livro Caixa Completo
**Scenario:** Médico autônomo, R$400,000 rendimentos (mix PJ + PF), R$80,000 despesas consultório, INSS R$14,016 (teto), médicas R$15,000 (dependentes), PGBL R$20,000

**Bank statement extract (BB Empresas):**
```
Data          | Histórico                                  | Débito (R$)   | Crédito (R$)  | Saldo (R$)
08/05/2025    | TED HOSPITAL SAO LUIZ LTDA                |               | 35,250.00     | 380,000.00
12/05/2025    | PIX PACIENTE CONSULTA                    |               |  1,200.00     | 381,200.00
15/05/2025    | DEB ALUGUEL SALA CLINICA LTDA             | 5,000.00      |               | 376,200.00
20/05/2025    | DEB INSS CONTRIB INDIVIDUAL              | 1,168.00      |               | 375,032.00
25/05/2025    | DARF IRRF CARNE LEAO                     | 8,500.00      |               | 366,532.00
```

**DIRPF — Deduções Reais:**
| Linha | Valor |
|---|---|
| Rendimentos tributáveis | R$400,000 |
| Livro caixa (despesas consultório) | (R$80,000) |
| INSS (teto) | (R$14,016) |
| PGBL (12% do rendimento bruto) | (R$20,000) |
| Dependentes 2× | (R$4,550) |
| Despesas médicas dependentes | (R$15,000) |
| **Base de cálculo** | **R$266,434** |
| IRPF: 27.5% × R$266,434 − R$10,752.77 | R$73,269 − R$10,753 = **R$62,516** |
| IRRF PJ retido | (R$6,000 est.) |
| Carnê-Leão pago | (R$18,500 est.) |
| **IRPF a pagar** | **~R$38,016** |

### Example 4 — Caixa Econômica Federal: Desenvolvedor com Renda Exterior
**Scenario:** Developer, R$60,000 domestic PJ clients + USD $30,000 (R$150,000) from US clients via Stripe, Carnê-Leão required on foreign income

**Bank statement extract (Caixa Econômica):**
```
Data          | Histórico                                  | Débito (R$)   | Crédito (R$)  | Saldo (R$)
10/06/2025    | TED STARTUP BRASIL LTDA                  |               | 14,750.00     | 95,000.00
15/06/2025    | TRANSFERENCIA STRIPE INC USD              |               | 25,000.00     | 120,000.00
20/06/2025    | DARF CARNE LEAO REND EXT 0190             | 5,500.00      |               | 114,500.00
25/06/2025    | DEB IOF CAMBIO                            | 150.00        |               | 114,350.00
30/06/2025    | TARIFA CONTA PJ CAIXA                    | 30.00         |               | 114,320.00
```

**IOF:** IOF on foreign exchange conversion = custo do câmbio → pode ser despesa no livro caixa.

**DIRPF:**
| Linha | Valor |
|---|---|
| Rendimentos PJ (R$60,000 bruto) | R$60,000 |
| Rendimentos exterior (USD $30K × PTAX) | R$150,000 |
| Total rendimentos tributáveis | R$210,000 |
| Livro caixa | (R$20,000) |
| INSS | (R$14,016) |
| **Base de cálculo** | **R$175,984** |
| IRPF: 27.5% × R$175,984 − R$10,752.77 | **R$37,642** |
| IRRF PJ (R$900) + Carnê-Leão pago (R$28,000) | (R$28,900) |
| **Saldo** | **R$8,742** |

### Example 5 — Nubank: Autônomo Jovem, MEI vs IRPF Comparison
**Scenario:** Young professional, R$75,000 faturamento, deciding between MEI and IRPF autônomo treatment

**Bank statement extract (Nubank PJ):**
```
Data          | Descrição                                  | Saída (R$)    | Entrada (R$)  | Saldo (R$)
12/07/2025    | Pix recebido CLIENTE TECH                |               | 12,000.00     | 45,000.00
18/07/2025    | Pix recebido AGENCIA DIGITAL             |               |  6,500.00     | 51,500.00
22/07/2025    | Débito GITHUB ENTERPRISE                  | 180.00        |               | 51,320.00
26/07/2025    | DAS MEI PAGAMENTO                        | 72.85         |               | 51,247.15
30/07/2025    | Tarifa Nubank Conta PJ                   | 0.00          |               | 51,247.15
```

**MEI vs Autônomo:**
| | MEI | Autônomo (IRPF) |
|---|---|---|
| DAS/IRPF mensal | R$72.85/mês = R$874/ano | Carnê-Leão ~R$5,000+/ano |
| Limite faturamento | R$81.000 | Ilimitado |
| INSS | Incluso no DAS | 20% sobre salário contribuição ou 11% (plano básico) |
| Nota fiscal | Pode emitir | Pode emitir (autônomo) |
| Complexidade | Simples | Maior |
| **Veredito para R$75K** | **MEI muito mais vantajoso** | |

### Example 6 — Santander Brasil: Arquiteta, Parcelamento IRPF
**Scenario:** Architect, R$120,000 annual income, IRPF due R$15,000, requesting parcelamento (instalments)

**Bank statement extract (Santander Select):**
```
Data          | Histórico                                  | Débito (R$)   | Crédito (R$)  | Saldo (R$)
03/08/2025    | TED REC CONSTRUTORA ABC LTDA              |               | 22,500.00     | 148,000.00
10/08/2025    | TED REC PROJETO ARQ DESIGN               |               | 12,000.00     | 160,000.00
15/08/2025    | DARF IRPF QUOTA 1/8                      | 1,875.00      |               | 158,125.00
20/08/2025    | DEB AUTODESK BRASIL LTDA                  | 350.00        |               | 157,775.00
25/08/2025    | TARIFA SANTANDER PRIME                   | 42.00         |               | 157,733.00
```

**IRPF parcelamento:** IRPF due > R$100: may be paid in up to 8 instalments. First instalment = 1/8; remaining 7 by last business day of each subsequent month. Interest (Selic) applies from 2nd instalment.

---

## Section 5 — Tier 1 Rules (Compressed Reference)

### Residência Fiscal
- **Residente:** Domicílio no Brasil OU permanência > 183 dias em 12 meses consecutivos → rendimentos mundiais tributáveis
- **Não-residente:** Apenas rendimentos de fonte brasileira; taxas de IRRF diferentes

### Carnê-Leão — Quando Obrigatório
| Situação | Carnê-Leão? |
|---|---|
| Recebimento de pessoa física (PF) | Obrigatório |
| Recebimento do exterior (qualquer valor) | Obrigatório |
| Recebimento de pessoa jurídica (PJ) com IRRF | NÃO — PJ já retém |
| Aluguéis recebidos de PF | Obrigatório |
| Pensão judicial recebida | Obrigatório |

**DARF Carnê-Leão:** Código 0190 | Prazo: último dia útil do mês seguinte | App: e-CAC ou Receitanet

### INSS — Contribuição do Autônomo
- **Contribuinte individual:** Alíquota 20% sobre salário de contribuição (piso: salário mínimo; teto: R$8,157.41/mês em 2025)
- **Plano Simplificado:** 11% sobre um salário mínimo — apenas para trabalhadores que não precisam de aposentadoria por tempo de contribuição
- Contribuição INSS = 100% dedutível na DIRPF

### ISS — Imposto Sobre Serviços
- Municipal — cada município define sua alíquota (2%–5%)
- Autônomos podem ser obrigados a recolher ISS mensalmente ou ter ISS retido pelo tomador PJ
- ISS dedutível no livro caixa como despesa profissional

### Obrigatoriedade de Declaração (DIRPF)
| Critério | Obrigado a declarar |
|---|---|
| Rendimentos tributáveis > R$33,888 | Sim |
| Rendimentos isentos > R$200,000 | Sim |
| Operações em bolsa | Sim |
| Bens e direitos > R$800,000 | Sim |
| Obteve ganho de capital | Sim |

### Prazo DIRPF
| Evento | Prazo |
|---|---|
| DIRPF entrega | Março 15 – Maio 31 (ano seguinte) |
| Carnê-Leão mensal | Último dia útil do mês seguinte |
| Imposto a pagar (quota única ou 1ª quota) | Maio 31 |
| Demais quotas (até 8) | Último dia útil mês a mês |

### Multas e Juros
| Situação | Penalidade |
|---|---|
| Declaração em atraso | 1% ao mês sobre IR devido (mínimo R$165.74, máximo 20%) |
| Omissão de rendimentos | 75% do IR não declarado + juros Selic |
| Fraude fiscal | 150%–225% do imposto |
| Atraso no DARF Carnê-Leão | 0.33% ao dia (máximo 20%) + Selic |

---

## Section 6 — Tier 2 Catalogue

### T2-BR-1: Escritório em Casa (Home Office)
**Por que T2:** A proporção profissional/residencial depende de dados que só o cliente conhece.

**Método:** m² escritório ÷ m² total × aluguel/energia/água/internet
**Exige do cliente:** Área total do imóvel (m²), área exclusiva de escritório (m²), confirmação de uso exclusivamente profissional.

### T2-BR-2: Veículo (Uso Profissional)
**Por que T2:** A proporção km profissional/pessoal é um dado que só o cliente tem.

**Método:** km profissional ÷ km total × despesas com o veículo (combustível, manutenção, seguro, amortização)
**Exige do cliente:** km totais anuais, km profissionais (logbook), valor do veículo, despesas anuais com o veículo.

### T2-BR-3: Telefone e Internet
**Por que T2:** Divisão pessoal/profissional é subjetiva.

**Orientação:** Linha exclusivamente profissional: 100%. Uso misto: % estimado (padrão 50%–70%). Documentar critério utilizado.

### T2-BR-4: Desconto Simplificado vs Deduções Reais
**Por que T2:** A escolha ótima depende das despesas reais do cliente — calcular ambas.

**Quando usar desconto simplificado:** Despesas documentadas < 20% dos rendimentos tributáveis brutos.
**Quando usar deduções reais:** Despesas documentadas > 20% (sobretudo médicos, alto PGBL, dependentes múltiplos).
**Nota:** A escolha é feita na DIRPF — não pode ser alterada após o prazo de entrega.

### T2-BR-5: PGBL vs VGBL (Previdência Privada)
**Por que T2:** O tipo de plano determinam a dedutibilidade — o cliente precisa confirmar.

- **PGBL:** Contribuições dedutíveis até 12% da renda tributável na DIRPF; resgate tributado na saída
- **VGBL:** Não dedutível na DIRPF; resgate tributado apenas sobre o rendimento
- **Recomendação:** PGBL apenas para quem faz declaração completa (deduções reais) — verificar com o cliente

---

## Section 7 — Excel Working Paper

### Aba 1: Rendimentos
| Coluna | Conteúdo |
|---|---|
| A | Data |
| B | Fonte (pagador) |
| C | CNPJ/CPF pagador |
| D | Valor bruto (R$) |
| E | IRRF retido (R$) |
| F | Valor líquido |
| G | Tipo: PJ com IRRF / PF / Exterior |
| H | Carnê-Leão devem | (se PF ou Exterior) |

**Total rendimentos tributáveis:** `=SUMIF(G:G,"PJ com IRRF",D:D)+SUMIF(G:G,"PF",D:D)+SUMIF(G:G,"Exterior",D:D)`

### Aba 2: Livro Caixa
| Coluna | Conteúdo |
|---|---|
| A | Data |
| B | Fornecedor/descrição |
| C | CNPJ/CPF |
| D | Valor (R$) |
| E | Categoria (aluguel/telecom/material/viagem etc.) |
| F | % profissional |
| G | Dedutível (=D×F) |
| H | Nota Fiscal / comprovante |

### Aba 3: DIRPF — Apuração
| Linha | Valor |
|---|---|
| Rendimentos tributáveis totais | |
| Livro caixa OU desconto simplificado (o maior) | |
| INSS contribuição individual | |
| PGBL | |
| Dependentes | |
| Pensão alimentícia | |
| **Base de cálculo** | |
| IRPF (tabela progressiva anual) | |
| Créditos: IRRF + Carnê-Leão + médicas | |
| **IRPF a pagar / restituir** | |

---

## Section 8 — Bank Statement Reading Guide

### Itaú Unibanco
- Format: `Data | Histórico | Débito (R$) | Crédito (R$) | Saldo (R$)`
- Date: DD/MM/YYYY
- Income = Crédito column
- "TED REC" = TED recebido; "PIX REC" = PIX recebido

### Bradesco
- Format: `Data | Histórico | Débito (R$) | Crédito (R$) | Saldo (R$)`
- Date: DD/MM/YYYY
- "PIX RECEBIDO" = income; "DEB" = debit/expense

### Banco do Brasil
- Format: `Data | Histórico | Débito (R$) | Crédito (R$) | Saldo (R$)`
- Date: DD/MM/YYYY
- "TED HOSPITAL..." = incoming corporate payment

### Caixa Econômica Federal
- Format: `Data | Histórico | Débito (R$) | Crédito (R$) | Saldo (R$)`
- Date: DD/MM/YYYY
- "TRANSFERENCIA...USD" = foreign wire (check PTAX rate for conversion)

### Nubank PJ
- Format: `Data | Descrição | Saída (R$) | Entrada (R$) | Saldo (R$)`
- Date: DD/MM/YYYY
- Income = Entrada column; "Pix recebido" = incoming PIX

### Santander Brasil
- Format: `Data | Histórico | Débito (R$) | Crédito (R$) | Saldo (R$)`
- Date: DD/MM/YYYY
- "TED REC" = TED recebido

### Exclusion Patterns (all Brazilian banks)
| Padrão | Ação |
|---|---|
| TED / PIX para conta própria | EXCLUIR — transferência interna |
| Pagamento fatura cartão | EXCLUIR — despesas capturadas individualmente |
| DARF pagamento | EXCLUIR — crédito fiscal (não despesa) |
| DAS MEI | EXCLUIR — imposto |
| Transferência para poupança | EXCLUIR — aplicação pessoal |
| Crédito de empréstimo / financiamento | EXCLUIR — não é receita |

---

## Section 9 — Onboarding Fallback

**Prioridade 1 (bloqueante):**
1. "Qual foi o total dos seus rendimentos brutos no ano? Separar: de PJ (empresas) e de PF (pessoas físicas) e do exterior."
2. "Você pagou Carnê-Leão mensalmente sobre os rendimentos de PF e exterior?"
3. "Tem comprovante de IRRF retido na fonte pelos pagadores PJ (informe de rendimentos)?"

**Prioridade 2 (para cálculo):**
4. "Tem livro caixa com despesas documentadas? Total do ano?"
5. "Pagou INSS como contribuinte individual? Valor total anual?"
6. "Tem dependentes (filhos, cônjuge)? Tem despesas médicas para deduzir (com recibo e CPF do prestador)?"
7. "Tem previdência privada PGBL? Valor das contribuições no ano?"

**Prioridade 3 (outros):**
8. "Tem rendimentos isentos (dividendos recebidos até 2023, indenizações)? Valores?"
9. "Realizou operações em bolsa de valores?"
10. "Fez parcelamento do IRPF do ano passado? Quantas quotas e valores pagos?"

---

## Section 10 — Reference Material

### Formulários DIRPF Principais
| Ficha / Programa | Finalidade |
|---|---|
| Programa IRPF (Receita Federal) | Declaração anual DIRPF |
| Ficha Rendimentos Tributáveis (titular) | Rendimentos PJ + PF + exterior |
| Ficha Pagamentos e Doações Efetuados | INSS, PGBL, pensão alimentícia, médicos |
| Ficha Bens e Direitos | Imóveis, veículos, aplicações |
| Carnê-Leão online (e-CAC) | Apuração e DARF mensal |

### Plataformas
- **e-CAC (Centro Virtual de Atendimento):** cav.receita.fazenda.gov.br
- **Programa IRPF:** Baixar em receita.economia.gov.br (liberado em março cada ano)
- **Receita Federal:** gov.br/receitafederal

### Referências Legais
- RIR/2018 (Decreto 9.580/2018): Regulamento do Imposto de Renda
- IN RFB 1.500/2014: Obrigações acessórias IRPF
- Lei 9.250/1995: Cálculo IRPF

---

## Prohibitions
- Não fornecer orientação sobre PIS/COFINS ou CSLL — apuram-se na empresa, não no IRPF pessoa física
- Não fornecer orientação sobre IRPJ (Imposto de Renda Pessoa Jurídica) — esta skill é para PF autônomo
- Não fornecer orientação sobre Simples Nacional ou Lucro Presumido de empresas — cobrem-se em skills separadas
- Não calcular ganho de capital em alienação de bens imóveis ou ações — sujeito a regras específicas (GCAP)
- Não calcular contribuição INSS patronal — aplicável a empregadores, não a autônomos

## Disclaimer
Este skill oferece orientação geral para fins informativos e de planejamento. Não constitui consultoria tributária. A legislação tributária brasileira é administrada pela Secretaria Especial da Receita Federal do Brasil. Os clientes devem consultar um contador ou advogado tributarista registrado no CRC (Conselho Regional de Contabilidade) para orientação específica à sua situação. Alíquotas, deduções e tabelas são atualizadas anualmente — verificar sempre as regras vigentes em gov.br/receitafederal.
