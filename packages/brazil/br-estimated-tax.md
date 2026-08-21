---
name: br-estimated-tax
description: "Use esta skill sempre que for solicitado a tratar de pagamentos mensais estimados de imposto de renda no Brasil (Carnê-Leão) para profissionais autônomos, freelancers ou profissionais que recebem rendimentos de pessoas físicas ou de fontes do exterior. Cobre o cronograma de pagamento mensal, a tabela progressiva, despesas dedutíveis (livro caixa), o procedimento de pagamento via DARF 0190, multas por atraso e a interação com a declaração anual (DIRPF). SEMPRE leia esta skill antes de qualquer trabalho de imposto estimado no Brasil. Trigger also on: \"Carne-Leao\", \"carne-leao\", \"estimated tax Brazil\", \"Brazilian monthly tax\", \"DARF 0190\", \"recolhimento mensal obrigatorio\", \"livro caixa\", \"autonomous income tax\", or any question about monthly advance income tax obligations under Brazilian tax law."
version: 2.0
jurisdiction: BR
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Ariane Marrocos
review_status: current
depends_on: - income-tax-workflow-base
category: international
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# BR Estimated Tax

## Brasil — Carnê-Leão e Estimativa Mensal — Skill v2.1

## Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by Ariane Marrocos on 2026-06-03. Items flagged for further clarification are tracked separately and excluded here. This block is generated from verified skill_facts — edit the facts, not the prose.

### Carnê-Leão

- **Até R$ 2.259,20** — 0% BRL (parcela R$ 0,00)  _(Lei nº 7.713/1988 Medida Provisória nº 1.171/2023 Decreto nº 9.580/2018.)_
- **R$ 2.259,21 – R$ 2.826,65** — 7,5% BRL (parcela R$ 169,44)  _(Lei nº 7.713/1988 Medida Provisória nº 1.171/2023 Decreto nº 9.580/2018.)_
- **R$ 2.826,66 – R$ 3.751,05** — 15% BRL (parcela R$ 381,44)  _(Lei nº 7.713/1988 Medida Provisória nº 1.171/2023 Decreto nº 9.580/2018.)_
- **R$ 3.751,06 – R$ 4.664,68** — 22,5% BRL (parcela R$ 662,77)  _(Lei nº 7.713/1988 Medida Provisória nº 1.171/2023 Decreto nº 9.580/2018.)_
- **Acima de R$ 4.664,68** — 27,5% BRL (parcela R$ 896,00)  _(Lei nº 7.713/1988 Medida Provisória nº 1.171/2023 Decreto nº 9.580/2018.)_
- **Por dependente** — Na apuração mensal do Carnê-Leão, é permitida a dedução de R$ 189,59 por dependente, conforme previsto na Lei nº 9.250/1995.  _(Lei nº 9.250/1995. Complementar com o Decreto nº 9.580/2018.)_
- **INSS contribuinte individual** — Na apuração do Carnê-Leão, é dedutível da base de cálculo do imposto o valor da contribuição previdenciária oficial efetivamente paga pelo contribuinte individual no período.  _(Complementar com as Lei nº 9.250/1995 e Decreto nº 9.580/2018.)_
- **Livro caixa** — No Carnê-Leão, podem ser deduzidas as despesas escrituradas em livro-caixa, necessárias à percepção da receita e à manutenção da atividade profissional, desde que devidamente comprovadas, não sendo permitida a apuração de base de cálculo negativa.  _(Lei nº 9.250/1995 – Art. 8º. O tema do livro-caixa está mais diretamente disciplinado em: Lei nº 8.134/1990 e Decreto nº 9.580/2018 Complementarmente na Lei nº 9.250/1995 Portanto, a indicada não é a mais específica para o tema.)_
- **Pensão alimentícia judicial** — Na apuração do Carnê-Leão, é dedutível o valor da pensão alimentícia efetivamente pago em cumprimento de decisão judicial, acordo homologado judicialmente ou escritura pública, conforme previsto na legislação do Imposto de Renda.  _(Decreto nº 9.580/2018 Lei nº 9.250/1995.)_
- **Desconto simplificado mensal** — BRL 564,80 (Na apuração mensal do IRPF/Carnê-Leão, o contribuinte pode optar pelo desconto simplificado mensal de R$ 564,80 em substituição às deduções legais, conforme a legislação vigente.)  _(Lei nº 14.663/2023.)_
- **Código DARF** — O imposto apurado no Carnê-Leão deve ser recolhido mediante DARF código 0190, conforme as regras da Receita Federal.  _(Decreto nº 9.580/2018)_
- **Vencimento** — O imposto apurado no Carnê-Leão deve ser recolhido até o último dia útil do mês subsequente ao do recebimento dos rendimentos sujeitos à tributação.  _(Embora a Lei nº 7.713/1988 seja uma das bases do IRPF, a mais utilizada para o vencimento do Carnê-Leão é: Decreto nº 9.580/2018.)_
- **Multa de mora** — O pagamento em atraso do DARF do Carnê-Leão sujeita o contribuinte à multa de mora de 0,33% por dia de atraso, limitada a 20% do imposto devido, além de juros calculados com base na taxa SELIC.  _(CTN – Art. 161 (juros de mora). A multa de mora de 0,33% por dia limitada a 20% decorre principalmente da Lei nº 9.430/1996 - Art. 61. Complementares Código Tributário Nacional – art. 161 e Decreto nº 9.580/2018.)_
- **Juros de mora** — O pagamento em atraso do DARF do Carnê-Leão sujeita o contribuinte à multa de mora de 0,33% por dia de atraso, limitada a 20% do imposto devido, além de juros calculados com base na taxa SELIC.  _(CTN Art. 161 estabelece a incidência de juros de mora, mas a regra específica de utilização da SELIC para tributos federais decorre principalmente de Lei nº 9.430/1996 Art. 61, §3º. Complementares Código Tributário Nacional – art. 161 e Decreto nº 9.580/2018.)_

## Seção 1 — Referência rápida

**Referência rápida**

| Campo | Valor |
| --- | --- |
| País | Brasil |
| Tributo | Antecipação mensal obrigatória do imposto de renda (Carnê-Leão / IRPF mensal) |
| Legislação principal | RIR/2018 (Decreto 9.580/2018), Arts. 118-122; Lei 7.713/1988, Art. 6 |
| Legislação complementar | IN RFB 1.500/2014; Lei 9.250/1995 Art. 8 (livro caixa); CTN Art. 161 |
| Autoridade | Receita Federal do Brasil (RFB) |
| Portal | carne-leao.receita.fazenda.gov.br / Meu Imposto de Renda |
| Moeda | Somente BRL |
| Cronograma de pagamento | Mensal — até o último dia útil do mês seguinte ao mês do rendimento |
| Código DARF | 0190 |
| Cálculo | Tabela progressiva aplicada sobre a renda mensal tributável após deduções |
| Escopo | Rendimentos de pessoas físicas e de fontes do exterior APENAS |
| Contribuinte | Open Accountants Community |
| Validado por | Pendente — requer aprovação de contador brasileiro |
| Data de validação | Verificado por Ariane Marrocos (SP 312052/O-1) em 2026-06-03 |

A reforma do consumo introduzida pela EC 132/2023, LC 214/2025 e LC 227/2026 afeta apenas tributos sobre o consumo (CBS, IBS, Imposto Seletivo e os antigos ICMS/ISS/PIS/COFINS/IPI). Ela NÃO altera o Carnê-Leão (IRPF mensal) nem a estimativa mensal de PJ (IRPJ). A estrutura do imposto de renda permanece inalterada.

**Tabela progressiva (2025 — confirmar quando publicada)**

| Renda mensal tributável (BRL) | Alíquota | Parcela a deduzir (BRL) |
| --- | --- | --- |
| Até 2.259,20 | 0% | 0,00 |
| 2.259,21 — 2.826,65 | 7,5% | 169,44 |
| 2.826,66 — 3.751,05 | 15% | 381,44 |
| 3.751,06 — 4.664,68 | 22,5% | 662,77 |
| Acima de 4.664,68 | 27,5% | 896,00 |

**Defaults conservadores**

| Ambiguidade | Default |
| --- | --- |
| Origem do rendimento incerta (pessoa física vs jurídica) | Confirmar — apenas rendimentos de pessoas físicas/exterior geram Carnê-Leão |
| Legitimidade de despesa de livro caixa incerta | Excluir despesas incertas (não pode gerar renda tributável negativa) |
| Taxa de câmbio incerta | Usar PTAX conforme IN RFB 1.500/2014 |
| Desconto simplificado vs itemizado | Escolher o que for mais vantajoso para o cliente |
| Sem rendimento no mês | Sem obrigação para esse mês |

## Seção 2 — Insumos exigidos e catálogo de recusas

### Insumos exigidos

Mínimo viável — renda bruta mensal de pessoas físicas e/ou fontes do exterior, contribuições ao INSS pagas, número de dependentes.

Recomendado — despesas de livro caixa com documentação, pensão alimentícia (judicial), DARFs pagos em meses anteriores.

Ideal — contabilidade mensal completa, todas as notas/recibos de clientes, comprovantes de INSS, livro caixa completo.

Política de recusa caso o mínimo esteja ausente — SOFT WARN. Sem os valores mensais de rendimento, a tabela progressiva não pode ser aplicada. Solicitar no mínimo o valor bruto recebido.

### Catálogo de recusas

- **R-BR-ET-1 — Rendimentos de pessoas jurídicas** — Gatilho: cliente pergunta sobre Carnê-Leão em rendimentos recebidos de empresas. Mensagem: "Rendimentos de pessoas jurídicas estão sujeitos a IRRF na fonte, não a Carnê-Leão. O Carnê-Leão aplica-se apenas a rendimentos de pessoas físicas e de fontes do exterior."
- **R-BR-ET-2 — Rendimentos com criptomoedas** — Gatilho: cliente pergunta sobre Carnê-Leão de cripto. Mensagem: "A tributação de rendimentos com criptomoedas possui regras específicas fora do escopo desta skill."
- **R-BR-ET-3 — Interações com não residentes** — Gatilho: cliente é não residente ou em transição de residência. Mensagem: "Obrigações tributárias de não residentes estão fora do escopo desta skill."

## Seção 3 — Biblioteca de padrões de pagamento

Este é o pré-classificador determinístico para transações de extrato bancário. Quando um débito casar com um padrão abaixo, classifique-o como pagamento de Carnê-Leão.

### 3.1 Débitos de DARF 0190

**Débitos de DARF 0190**

| Padrão | Tratamento | Observações |
| --- | --- | --- |
| DARF, DOCUMENTO DE ARRECADACAO | Pagamento de Carnê-Leão | Casar com código 0190 |
| RECEITA FEDERAL, RFB | Pagamento de Carnê-Leão | Casar com periodicidade mensal |
| CODIGO 0190 | Pagamento de Carnê-Leão | Código DARF explícito |
| CARNE LEAO, CARNE-LEAO | Pagamento de Carnê-Leão | Descrição explícita |
| IMPOSTO DE RENDA MENSAL | Pagamento de Carnê-Leão | Imposto de renda mensal |

### 3.2 Identificação por tempo

Os pagamentos mensais vencem no último dia útil do mês seguinte. Um débito de DARF 0190 em fevereiro normalmente cobre os rendimentos de janeiro.

**Identificação por tempo**

| Mês do débito | Mês do rendimento coberto |
| --- | --- |
| Fevereiro | Janeiro |
| Março | Fevereiro |
| ... | ... |
| Janeiro (ano seguinte) | Dezembro |

### 3.3 Relacionados, mas NÃO são Carnê-Leão

**Relacionados, mas NÃO são Carnê-Leão**

| Padrão | Tratamento | Observações |
| --- | --- | --- |
| DARF com código diferente de 0190 | EXCLUIR | Obrigação tributária distinta |
| INSS, CONTRIBUICAO PREVIDENCIARIA | EXCLUIR | Previdência social |
| ISS, IMPOSTO SOBRE SERVICOS | EXCLUIR | Imposto municipal sobre serviços |
| IRRF, RETENCAO NA FONTE | EXCLUIR | Retenção na fonte (de empresas) |
| IRPF QUOTA, DECLARACAO ANUAL | EXCLUIR | Pagamento de saldo da declaração anual |
| MULTA, JUROS DE MORA | EXCLUIR | Multa/juros por atraso |
| GPS, GUIA DA PREVIDENCIA | EXCLUIR | Contribuição previdenciária |

## Seção 4 — Exemplos resolvidos

### Exemplo 1 — Cálculo mensal padrão

Entrada: Renda mensal BRL 8.000 de clientes pessoas físicas. INSS = BRL 877,24. 1 dependente. Despesas de livro caixa = BRL 1.200.

**Cálculo mensal padrão**

| Item | Valor |
| --- | --- |
| Renda bruta | BRL 8.000,00 |
| (-) INSS | BRL 877,24 |
| (-) 1 dependente | BRL 189,59 |
| (-) Livro caixa | BRL 1.200,00 |
| Renda tributável | BRL 5.733,17 |
| Imposto (27,5%) | BRL 1.576,62 |
| (-) Parcela a deduzir | BRL 896,00 |
| **Carnê-Leão devido** | **BRL 680,62** |

### Exemplo 2 — Abaixo do limite de isenção

Entrada: Renda mensal BRL 2.000 após deduções.

Resultado: Renda tributável BRL 2.000 < BRL 2.259,20. Alíquota 0%. Sem imposto devido.

### Exemplo 3 — Fontes de renda mistas

Entrada: BRL 5.000 de pessoas físicas + BRL 10.000 de uma empresa.

Resultado: Carnê-Leão somente sobre os BRL 5.000. Os BRL 10.000 da empresa estão sujeitos a IRRF na fonte.

### Exemplo 4 — Rendimentos do exterior

Entrada: Residente brasileiro recebe USD 3.000 de cliente nos EUA. Taxa PTAX = BRL 5,20.

Cálculo: Equivalente em BRL = 3.000 x 5,20 = BRL 15.600. Sujeito ao Carnê-Leão pela tabela progressiva. Sinalizar ao contador para confirmar a metodologia da taxa de câmbio.

### Exemplo 5 — Classificação de extrato bancário

Linha de entrada: `28.02.2025 ; DARF COD 0190 PERIODO 01/2025 ; DEBITO ; -680.62 ; BRL`

Classificação: Pagamento de Carnê-Leão referente aos rendimentos de janeiro de 2025. Pagamento de imposto — não é despesa dedutível da atividade.

## Seção 5 — Regras de cálculo

### 5.1 Fórmula de cálculo mensal

- **Fórmula de cálculo mensal** — gross_income = income from individuals + foreign income for the month deductions = dependents + INSS + livro_caixa + alimony taxable_income = gross_income - deductions tax_due = (taxable_income x applicable_rate) - table_deduction carne_leao = max(0, tax_due)

### 5.2 Deduções permitidas

**Deduções permitidas**

| Dedução | Valor (2025) |
| --- | --- |
| Por dependente | BRL 189,59/mês |
| INSS (contribuinte individual) | Valor efetivamente pago |
| Despesas de livro caixa | Despesas efetivas documentadas |
| Pensão alimentícia judicial | Valor efetivamente pago |
| Desconto simplificado mensal | BRL 564,80 (alternativa ao itemizado) |

### 5.3 Regras do livro caixa

- **Regras do livro caixa** — Permitidas: aluguel de escritório, contas do espaço profissional, materiais profissionais, custos com empregados, desenvolvimento profissional, viagens diretamente relacionadas aos serviços. Não permitidas: despesas pessoais, depreciação de veículo (uso pessoal), home office integral (apenas a área proporcional). As deduções do livro caixa NÃO podem gerar renda tributável negativa da atividade. O piso é BRL 0.

### 5.4 Interação com a DIRPF anual

- **Interação com a DIRPF anual** — annual_tax = tax on total annual income credits = total_carne_leao + total_IRRF balance = annual_tax - credits if balance > 0: pay (or split into up to 8 instalments) if balance < 0: refund

## Seção 6 — Multas e juros

### 6.1 Encargos por pagamento em atraso

**Encargos por pagamento em atraso**

| Elemento | Regra |
| --- | --- |
| Multa de mora | 0,33% ao dia, limitada a 20% |
| Juros de mora | SELIC acumulada a partir do mês seguinte ao vencimento + 1% no mês do pagamento |

### 6.2 Cálculo

- **Cálculo de multa/juros** — penalty = min(tax x 0.33% x days_late, tax x 20%) interest = tax x (accumulated_SELIC + 1%) total = tax + penalty + interest

### 6.3 A inadimplência não elimina a obrigação

- **Inadimplência não elimina obrigação** — Deixar de pagar o Carnê-Leão durante o ano NÃO elimina a obrigação. A DIRPF anual evidenciará o imposto devido acrescido das multas e juros acumulados.

## Seção 7 — Procedimento de pagamento via DARF

### 7.1 Geração do DARF

- **Geração do DARF** — 1. Acessar o módulo Carnê-Leão em carne-leao.receita.fazenda.gov.br ou no Meu Imposto de Renda 2. Informar renda mensal, deduções e dependentes 3. O sistema calcula o imposto e gera o DARF com código 0190 4. Pagar via internet banking, caixa eletrônico ou agência bancária 5. Guardar o comprovante do DARF para a declaração anual

### 7.2 Campos do DARF

**Campos do DARF**

| Campo | Valor |
| --- | --- |
| Código da Receita | 0190 |
| Período de Apuração | Último dia do mês do rendimento |
| CPF | CPF do cliente |
| Valor Principal | Valor do imposto devido |

## Seção 8 — Casos extremos

EC1 — Renda mista de pessoas físicas e jurídicas. O Carnê-Leão aplica-se somente à parcela recebida de pessoas físicas. A renda de pessoas jurídicas é sujeita a IRRF na fonte.

EC2 — Rendimentos do exterior. Sujeitos ao Carnê-Leão. Converter pela taxa PTAX conforme IN RFB 1.500/2014. Sinalizar ao contador.

EC3 — Sem renda no mês. Sem obrigação de Carnê-Leão. Sem DARF.

EC4 — Renda abaixo do limite de isenção. Renda tributável após deduções abaixo de BRL 2.259,20: alíquota 0%, sem imposto devido.

EC5 — Livro caixa supera a renda. Deduções não podem gerar renda tributável negativa. O piso é BRL 0.

EC6 — Desconto simplificado vs itemizado. O cliente pode optar pela alternativa que resulte em menor renda tributável: simplificado BRL 564,80 ou deduções itemizadas.

## Seção 9 — Self-checks

Antes de entregar o resultado, verificar:

- [ ] Origem da renda confirmada (pessoas físicas/exterior vs pessoas jurídicas)
- [ ] Alíquotas da tabela progressiva atualizadas para 2025
- [ ] Deduções de livro caixa documentadas e legítimas
- [ ] Livro caixa não gera renda tributável negativa
- [ ] Código DARF 0190 utilizado
- [ ] Prazo de pagamento no último dia útil do mês seguinte
- [ ] Taxa de juros baseada na SELIC atualizada para cálculo de multas
- [ ] Valor da dedução por dependente atualizado
- [ ] Contribuição ao INSS corretamente deduzida
- [ ] Resultado rotulado como estimado até confirmação do contador

## Seção 10 — Suíte de testes

### Teste 1 — Cálculo mensal padrão

Entrada: Renda BRL 8.000. INSS BRL 877,24. 1 dependente. Livro caixa BRL 1.200.
Esperado: Tributável = BRL 5.733,17. Imposto = BRL 680,62.

### Teste 2 — Abaixo do limite de isenção

Entrada: Renda tributável BRL 2.000.
Esperado: Alíquota 0%. Sem imposto devido.

### Teste 3 — Fontes mistas

Entrada: BRL 5.000 de pessoas físicas. BRL 10.000 de empresa.
Esperado: Carnê-Leão apenas sobre BRL 5.000.

### Teste 4 — Sem renda

Entrada: Sem rendimentos qualificados em março.
Esperado: Sem obrigação.

### Teste 5 — Pagamento em atraso

Entrada: BRL 680,62 com vencimento em 28/fev. Pago com 45 dias de atraso. SELIC acumulada = 0,92%.
Esperado: Multa = BRL 680,62 x 0,33% x 45 = BRL 101,07 (teto de 20% = BRL 136,12, portanto aplica-se BRL 101,07). Juros = BRL 680,62 x (0,92% + 1%) = BRL 13,07.

### Teste 6 — Renda do exterior

Entrada: USD 3.000. PTAX = 5,20.
Esperado: BRL 15.600 sujeitos ao Carnê-Leão pela tabela progressiva.

## Proibições

- NUNCA aplicar o Carnê-Leão a rendimentos de pessoas jurídicas (sujeitos a IRRF na fonte)
- NUNCA permitir que as deduções do livro caixa gerem renda tributável negativa
- NUNCA esquecer os juros baseados na SELIC ao calcular encargos por atraso
- NUNCA usar o código DARF errado — sempre 0190 para Carnê-Leão
- NUNCA ignorar a natureza mensal da obrigação — NÃO é trimestral
- NUNCA apresentar valores como definitivos — orientar confirmação com contador

## Disclaimer

Esta skill e seus resultados são fornecidos apenas para fins informativos e de cálculo, não constituindo aconselhamento tributário, jurídico ou financeiro. A Open Accountants e seus colaboradores não se responsabilizam por quaisquer erros, omissões ou consequências decorrentes do uso desta skill. Todos os resultados devem ser revisados e aprovados por profissional qualificado (como um contador ou profissional licenciado equivalente em sua jurisdição) antes de qualquer transmissão ou ação.

A versão mais atualizada e verificada desta skill é mantida em [openaccountants.com](https://openaccountants.com). Faça login para acessar a versão mais recente, solicitar revisão profissional de um contador licenciado e acompanhar atualizações conforme a legislação tributária mudar.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your jurisdiction — no liability on either side until you and the accountant sign a formal engagement letter — book a free 30-minute call:

→ [Book a call](https://calendly.com/openaccountants-info/30min)

We'll route you to the named verifier covering your country or state. You can also see the full list of verified accountants at [openaccountants.com/network](https://openaccountants.com/network).

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
