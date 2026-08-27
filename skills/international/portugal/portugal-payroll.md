---
name: portugal-payroll
description: "Utilize esta skill sempre que for solicitado sobre processamento de salários em Portugal, cálculo de vencimentos, retenção na fonte de IRS, contribuições para a Segurança Social (TSU), cálculo do custo total para a entidade patronal, conversões de líquido para bruto ou bruto para líquido, estrutura do recibo de vencimento português, Declaração Mensal de Remunerações (DMR), ou qualquer questão relativa ao cálculo de vencimentos, descontos ou obrigações da entidade patronal em Portugal. Acione perante expressões como \"processamento de salários\", \"retenção na fonte IRS\", \"Segurança Social\", \"TSU\", \"salário líquido\", \"custo entidade patronal\", \"subsídio de férias\", \"subsídio de Natal\", \"salário mínimo\", \"DMR\", \"recibo de vencimento\", \"13.º mês\" ou \"14.º mês\". Trigger also on: \"Portuguese payroll\", \"IRS withholding\", \"retenção na fonte\", \"Segurança Social\", \"TSU\", \"salário líquido\", \"employer cost Portugal\", \"subsídio de férias\", \"subsídio de Natal\", \"13th month Portugal\", \"14th month Portugal\", \"minimum wage Portugal\", \"salário mínimo\", \"DMR filing\", \"recibo de vencimento\"."
version: 1.0
jurisdiction: PT
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Mário Jorge da costa Vale
review_status: current
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Portugal Payroll

## Portugal — Processamento de Salários — Skill v1.1

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **Mário Jorge da costa Vale** on 2026-06-04.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### Folha de Pagamento

- **Continente 2026** — €920/mês  _(DL 139/2025)_
- **Continente 2025** — €870/mês  _(DL anterior)_
- **Açores 2026** — €966/mês  _(DL regional)_
- **Madeira 2026** — €980,00  _(Decreto Legislativo Regional n.º 1/2026/M, de 3 de fevereiro de 2026)_
- **Empregado** — 11% do bruto  _(Código Contributivo)_
- **Empregador** — 23,75% do bruto  _(Código Contributivo)_
- **Total** — 34,75%
- **Teto** — Sem teto — aplica-se ao salário total  _(Código Contributivo)_
- **FCT (Fundo de Compensação)** — Suspenso de Maio de 2023  _(Lei 70/2013)_
- **FGCT (Fundo de Garantia)** — Suspenso de Maio de 2023  _(Lei 70/2013)_
- **Total (FCT/FGCT)** — Suspenso de Maio de 2023
- **Empregador (gerente sem proteção desemprego)** — 20,30%  _(Código Contributivo)_
- **Empregado (gerente)** — 9,30%  _(Código Contributivo)_
- **Em dinheiro** — €6,15/dia (2026)  _(Portaria n.º 51-B/2026/1)_
- **Cartão refeição** — €10,46/dia (2026)  _(Portaria n.º 51-B/2026/1 (OE anual))_
- **1.ª hora (dia útil)** — 25%  _(Código do Trabalho)_
- **Horas seguintes (dia útil)** — 37,5%  _(Código do Trabalho)_
- **Descanso/feriados** — 50%  _(Código do Trabalho)_
- **Trabalho noturno (22h-7h)** — 25% mínimo  _(Código do Trabalho)_
- **Subsídio de férias** — 1 mês de salário (antes do início das férias)  _(Código do Trabalho)_
- **Subsídio de Natal** — 1 mês de salário (até 15 de dezembro)  _(Código do Trabalho)_
- **Férias anuais** — 22 dias úteis mínimo  _(Código do Trabalho)_
- **Licença paternidade** — 28 dias consecutivos obrigatórios (SS)  _(Código do Trabalho)_
- **DMR (Declaração Mensal)** — Até dia 10 do mês seguinte  _(AT)_
- **Pagamento SS/IRS** — Até dia 20 do mês seguinte  _(AT/ISS)_
- **Relatório Único** — Até 15 de abril  _(GEP/MTSSS)_

## Secção 1 — Referência Rápida

**Secção 1 — Referência Rápida**

| Campo | Valor |
| --- | --- |
| País | Portugal (República Portuguesa) |
| Moeda | EUR |
| Periodicidade do processamento | Mensal (14 pagamentos/ano: 12 + subsídio de férias + subsídio de Natal) |
| Ano fiscal | Ano civil (1 de janeiro — 31 de dezembro) |
| Legislação principal | Código do IRS (CIRS); Código Contributivo (Lei n.º 110/2009); Código do Trabalho |
| Autoridade tributária | Autoridade Tributária e Aduaneira (AT) |
| Autoridade da Segurança Social | Instituto da Segurança Social (ISS) / Direção-Geral da Segurança Social (DGSS) |
| Taxa Contributiva Social (TSC) — trabalhador | 11% do vencimento bruto |
| Taxa contributiva — entidade patronal | 23,75% do vencimento bruto |
| Retenção na fonte | IRS — tabelas mensais publicadas pela AT (CIRS art.º 99.º) |
| Retribuição Mínima Mensal Garantida (RMMG) | 920 EUR/mês (2026, Continente) |
| Pagamentos | 14 por ano (12 meses + subsídio de férias + subsídio de Natal) |
| Entrega da DMR | Mensal, até ao dia 10 do mês seguinte |
| Pagamento da Segurança Social / IRS | Mensal, até ao dia 20 do mês seguinte |
| Versão da skill | 1.1 |

## Secção 2 — Retenção na Fonte de IRS

### Escalões de IRS (2026 — Rendimento Coletável Anual)

**Escalões de IRS (2026 — Rendimento Coletável Anual)**

| Escalão | Rendimento Coletável Anual (EUR) | Taxa Marginal |
| --- | --- | --- |
| 1.º | Até 7 703 | 13,25% |
| 2.º | 7 703 — 11 623 | 16,50% |
| 3.º | 11 623 — 17 838 | 22,00% |
| 4.º | 17 838 — 22 052 | 24,10% |
| 5.º | 22 052 — 28 227 | 31,40% |
| 6.º | 28 227 — 41 674 | 37,00% |
| 7.º | 41 674 — 55 696 | 43,50% |
| 8.º | 55 696 — 78 834 | 45,00% |
| 9.º | Acima de 78 834 | 48,00% |

### Mecanismo de Retenção na Fonte

- **Mecanismo de retenção** — A retenção mensal de IRS utiliza tabelas específicas publicadas anualmente por Despacho (tabelas do Anexo III), nos termos do art.º 99.º do CIRS. Desde 2023, Portugal aplica uma fórmula progressiva marginal na retenção (e não uma taxa fixa por escalão).  _(CIRS art.º 99.º)_

**Tabelas de Retenção**

| Tabela | Aplicável a |
| --- | --- |
| Tabela I | Casado, único titular |
| Tabela II | Casado, dois titulares |
| Tabela III | Não casado |
| Tabelas IV-VII | Pensionistas |
| Tabelas VIII-XI | Trabalhadores com deficiência |

### Regras-Chave de Retenção (2026)

**Regras-Chave de Retenção (2026)**

| Regra | Detalhe |
| --- | --- |
| Limiar de não retenção | Até 920 EUR/mês (salário mínimo) = 0% de IRS |
| Mínimo de existência | 12 880 EUR anuais (14 × 920) — totalmente isento |
| Dedução por dependente | 42,86 EUR/mês (casado único titular); 21,43 EUR (dois titulares); 34,29 EUR (não casado) |
| Dedução específica | 4 104 EUR/ano (ou contribuições efetivas para a Segurança Social, se superiores) |
| 3 ou mais dependentes | Redução de 1 ponto percentual na taxa marginal mais elevada aplicável |

### Retenção sobre Subsídio de Férias / Subsídio de Natal

- **Retenção sobre subsídios** — Os subsídios de férias e de Natal estão sujeitos a retenção na fonte de IRS à MESMA taxa do vencimento mensal normal, calculada de forma autónoma. A contribuição para a Segurança Social também se aplica à taxa normal de 11%.

> **Nota — Regime IFICI / antigo RNH:** trabalhadores qualificados ao abrigo do regime de Incentivo Fiscal à Investigação Científica e Inovação (IFICI) ou ainda abrangidos por direitos adquiridos do antigo Regime dos Residentes Não Habituais (RNH) estão sujeitos a uma taxa especial de retenção de 20% sobre rendimentos do trabalho dependente elegíveis (Categoria A). Para o mecanismo detalhado de retenção e elegibilidade, consultar a skill **pt-nhr-ifici**.

## Secção 3 — Segurança Social: Descontos do Trabalhador

**Secção 3 — Segurança Social: Descontos do Trabalhador**

| Contribuição | Taxa | Base | Limite máximo |
| --- | --- | --- | --- |
| Segurança Social (trabalhador) — TSC | 11% | Remuneração bruta | Sem limite (aplica-se ao vencimento total) |

### O Que Está Sujeito a Contribuições para a Segurança Social

- Vencimento base
- Diuturnidades
- Subsídios regulares (subsídio de alimentação acima do limite de isenção, subsídios de turno)
- Subsídios de férias e de Natal
- Trabalho suplementar
- Comissões

### O Que Está Isento de Contribuições para a Segurança Social

- Subsídio de refeição até 6,00 EUR/dia (numerário) ou 10,20 EUR/dia (cartão refeição) — valores de 2026
- Ajudas de custo e despesas de deslocação (dentro dos limites legais)
- Distribuição de participação nos lucros
- Compensações por cessação do contrato (dentro dos limites legais)

### Regras-Chave

- A contribuição do trabalhador de 11% é deduzida na fonte mensalmente
- Aplica-se a cada um dos 14 pagamentos (incluindo subsídios de férias e de Natal)
- Não existe limite máximo — aplica-se à totalidade do vencimento
- As contribuições para a Segurança Social são dedutíveis para efeitos de IRS (consideradas na dedução específica)

## Secção 4 — Segurança Social: Contribuições da Entidade Patronal

**Secção 4 — Segurança Social: Contribuições da Entidade Patronal**

| Contribuição | Taxa | Base |
| --- | --- | --- |
| Segurança Social (entidade patronal) | 23,75% | Remuneração bruta |
| **Taxa total combinada (TSU)** | **34,75%** | Trabalhador 11% + Entidade patronal 23,75% |

### Taxas Especiais para a Entidade Patronal

**Taxas Especiais para a Entidade Patronal**

| Situação | Taxa |
| --- | --- |
| Membros de órgãos estatutários (gerentes/administradores) com proteção no desemprego | 23,75% (trabalhador 11%) |
| Membros de órgãos estatutários sem proteção no desemprego | 20,30% (trabalhador 9,30%) |
| Trabalhadores do serviço doméstico | 18,90% (trabalhador 9,40%) |
| Incentivo ao primeiro emprego (3 anos) | Redução de 50% na taxa da entidade patronal |
| Desempregados de longa duração (3 anos) | Redução de 50% na taxa da entidade patronal |

### Fundo de Compensação do Trabalho (FCT)

**Fundo de Compensação do Trabalho (FCT)**

| Fundo | Taxa | Finalidade |
| --- | --- | --- |
| FCT (Fundo de Compensação do Trabalho) | 0,925% | Garantia de compensação por cessação do contrato |
| FGCT (Fundo de Garantia de Compensação do Trabalho) | 0,075% | Fundo de garantia mútua |
| **Total** | **1,00%** | Pago pela entidade patronal sobre a remuneração bruta |

- Aplica-se a contratos iniciados após 1 de outubro de 2013
- Pago mensalmente, até ao dia 20 do mês seguinte
- Isentos: trabalhadores do serviço doméstico, setor público

## Secção 5 — Salário Mínimo e Trabalho Suplementar

### Retribuição Mínima Mensal Garantida (RMMG)

**Retribuição Mínima Mensal Garantida (RMMG)**

| Região | 2026 — Mensal (EUR) |
| --- | --- |
| Continente | 920,00 |
| Açores | 966,00 |
| Madeira | 968,00 |

- Fixada pelo Decreto-Lei n.º 139/2025 (em vigor a 1 de janeiro de 2026)
- Ano anterior (2025): 870,00 EUR
- Custo anual para a entidade patronal por trabalhador ao salário mínimo: ~14 094 EUR (incluindo subsídios + TSU)
- Trabalhadores ao salário mínimo pagam 0% de IRS (proteção do mínimo de existência)
- Vencimento líquido mínimo (após 11% Segurança Social): 818,80 EUR/mês

### Período Normal de Trabalho e Trabalho Suplementar

**Período Normal de Trabalho e Trabalho Suplementar**

| Parâmetro | Padrão |
| --- | --- |
| Período normal de trabalho semanal | 40 horas |
| Limite diário | 8 horas (extensível a 10 por instrumento de regulamentação coletiva) |
| Limite anual de trabalho suplementar | 150 horas/ano (200 por convenção coletiva) |
| Acréscimo da 1.ª hora (dia útil) | 25% |
| Acréscimo das horas seguintes (dia útil) | 37,5% |
| Acréscimo em dia de descanso/feriado | 50% |
| Subsídio de trabalho noturno (22h-7h) | Mínimo de 25% |

## Secção 6 — Benefícios Obrigatórios

**Secção 6 — Benefícios Obrigatórios**

| Benefício | Detalhe |
| --- | --- |
| Férias anuais | 22 dias úteis (mínimo) |
| Subsídio de férias | Equivalente a um mês de vencimento (pago antes do início das férias ou em junho) |
| Subsídio de Natal | Equivalente a um mês de vencimento (pago até 15 de dezembro) |
| Subsídio de refeição (subsídio de alimentação) | Não obrigatório por lei mas largamente generalizado; isento até 6,00 EUR/dia (numerário) ou 10,20 EUR/dia (cartão) |
| Baixa por doença | Paga pela Segurança Social a partir do 4.º dia (55%-75% do vencimento, conforme duração) |
| Licença de parentalidade (mãe) | 120 dias a 100% ou 150 dias a 80% (pago pela Segurança Social) |
| Licença de parentalidade (pai) | 28 dias consecutivos obrigatórios (pago pela Segurança Social) |
| Faltas por falecimento de familiar | 2 a 5 dias, conforme o grau de parentesco |
| Licença por casamento | 15 dias consecutivos |
| Seguro de acidentes de trabalho | Obrigatório (a entidade patronal deve contratar seguradora) |

### 13.º e 14.º Meses (Subsídios)

**13.º e 14.º Meses (Subsídios)**

| Subsídio | Valor | Prazo | Segurança Social / IRS |
| --- | --- | --- | --- |
| Subsídio de Natal | 1 mês de vencimento | Até 15 de dezembro (ou em duodécimos ao longo dos 12 meses) | Sujeito a 11% Segurança Social + IRS |
| Subsídio de férias | 1 mês de vencimento | Antes do início das férias ou até 30 de junho | Sujeito a 11% Segurança Social + IRS |

O trabalhador pode optar (ou a entidade patronal pode determinar) pelo pagamento em duodécimos (1/12 por mês). Ambos os subsídios são proporcionais ao tempo de trabalho efetivo se o trabalhador iniciar ou cessar funções a meio do ano.

## Secção 7 — Requisitos do Recibo de Vencimento

- **Obrigação de emissão** — A entidade patronal portuguesa DEVE emitir um recibo de vencimento por cada pagamento de salário.

**Elementos obrigatórios do recibo de vencimento**

| Elemento | Obrigatório |
| --- | --- |
| Identificação da entidade patronal (nome, NIPC, n.º Segurança Social) | Sim |
| Identificação do trabalhador (nome, NIF, NISS) | Sim |
| Período a que respeita (mês/ano) | Sim |
| Categoria profissional e antiguidade | Sim |
| Retribuição base (vencimento base) | Sim |
| Subsídios e suplementos regulares | Sim |
| Discriminação do trabalho suplementar | Sim |
| Remuneração bruta total | Sim |
| Contribuição do trabalhador para a Segurança Social (11%) | Sim |
| Valor da retenção na fonte de IRS | Sim |
| Outros descontos (quotizações sindicais, adiantamentos, etc.) | Sim |
| Subsídio de refeição (dias × valor unitário) | Sim (se aplicável) |
| Vencimento líquido a pagar | Sim |
| Data e meio de pagamento | Sim |
| Subsídio de férias / Natal (quando pago) | Sim |

### Conservação de Registos

- **Prazo de conservação** — A entidade patronal deve conservar os registos de processamento de salários por um período mínimo de 5 anos (legislação laboral geral) e 10 anos para efeitos fiscais.

## Secção 8 — Obrigações Declarativas

**Secção 8 — Obrigações Declarativas**

| Obrigação | Periodicidade | Prazo | Entidade |
| --- | --- | --- | --- |
| Declaração Mensal de Remunerações (DMR) | Mensal | Até ao dia 10 do mês seguinte | AT + Segurança Social |
| Pagamento das contribuições para a Segurança Social | Mensal | Entre os dias 10 e 20 do mês seguinte | Segurança Social (DGSS) |
| Pagamento da retenção na fonte de IRS | Mensal | Até ao dia 20 do mês seguinte | AT |
| Pagamento FCT/FGCT | Mensal | Até ao dia 20 do mês seguinte | Fundos de Compensação |
| Relatório Único | Anual | Até 15 de abril (via portal) | GEP / MTSSS |
| Declaração anual de IRS (Modelo 3) | Anual | 1 de abril — 30 de junho (entregue pelo trabalhador) | AT |
| Modelo 10 (rendimentos pagos a não residentes) | Anual | Até 28 de fevereiro | AT |

### DMR — Detalhes

**DMR — Detalhes**

| Parâmetro | Detalhe |
| --- | --- |
| Conteúdo | Por trabalhador: vencimento bruto, contribuições para a Segurança Social, retenção na fonte de IRS |
| Submissão | Eletrónica através do Portal das Finanças |
| Validação | Tem de ser validada pelo sistema da Segurança Social para se considerar entregue |
| Penalidades | Atraso na entrega: coimas de 150 EUR a 3 750 EUR; atraso no pagamento: agravamento de 10% + juros |

### Calendário Anual

**Calendário Anual**

| Mês | Obrigação |
| --- | --- |
| Janeiro | DMR de dezembro; pagamento Segurança Social / IRS de dezembro |
| Fevereiro | Prazo do Modelo 10 (não residentes) |
| Março | Acerto anual da Segurança Social |
| Abril | Relatório Único; DMR de março |
| Junho | Pagamento do subsídio de férias; abertura da entrega de IRS |
| Novembro | Primeira tranche do subsídio de Natal (se em duodécimos) |
| Dezembro | Subsídio de Natal até dia 15; fecho anual do processamento de salários |

## Secção 9 — Padrões Comuns de Processamento

### Padrão 1: Vencimento Mensal Padrão (Não Casado, Sem Dependentes, Continente)

```
Vencimento base:                      EUR 1 800,00
Subsídio de refeição (22 dias × 7,63): +EUR   167,86 (cartão, isento de SS / IRS)
Bruto para efeitos de SS / IRS:        EUR 1 800,00
- Segurança Social trabalhador (11%):  -EUR   198,00
= Base tributável para IRS:            EUR 1 602,00
- Retenção na fonte IRS (~14,5%):      -EUR   ~232,00
= Vencimento líquido:                  EUR 1 370,00
+ Subsídio de refeição:               +EUR   167,86
= Total recebido:                      EUR ~1 538,00

Custo para a entidade patronal:
  Vencimento base:                     EUR 1 800,00
+ Segurança Social patronal (23,75%): +EUR   427,50
+ FCT (1%):                           +EUR    18,00
+ Subsídio de refeição:               +EUR   167,86
= Custo mensal entidade patronal:      EUR ~2 413,36
```

### Padrão 2: Trabalhador ao Salário Mínimo (2026)

```
Vencimento base (RMMG):                EUR   920,00
- Segurança Social trabalhador (11%):  -EUR   101,20
- Retenção na fonte IRS:               -EUR     0,00 (isento — mínimo de existência)
= Vencimento líquido:                  EUR   818,80

Custo anual:
  14 meses × 920 × 1,2375 (com SS patronal) = EUR 15 939,00
  + FCT 1% sobre 14 meses = EUR 128,80
  Custo anual total para a entidade patronal ≈ EUR 16 068
```

### Padrão 3: Mês do Subsídio de Férias (junho)

Em junho, o trabalhador recebe duplo pagamento:
- Vencimento normal de junho (sujeito a Segurança Social + IRS à taxa normal)
- Subsídio de férias = 1 mês de vencimento base (sujeito a Segurança Social + IRS de forma autónoma)

Cada pagamento tem o IRS calculado independentemente utilizando a mesma taxa de retenção.

### Padrão 4: Acerto de Contas na Cessação do Contrato

**Padrão 4: Acerto de Contas na Cessação do Contrato**

| Componente | Cálculo |
| --- | --- |
| Vencimento em dívida | Dias trabalhados no mês final / 30 × vencimento |
| Subsídio de férias proporcional | Meses trabalhados / 12 × vencimento mensal |
| Subsídio de Natal proporcional | Meses trabalhados / 12 × vencimento mensal |
| Férias não gozadas (ano corrente) | Proporcional aos 22 dias |
| Férias não gozadas (transitadas) | Dias completos × valor diário |
| Compensação por cessação (se aplicável) | Nos termos do Código do Trabalho |

## Secção 10 — Interação com Outras Skills

**Secção 10 — Interação com Outras Skills**

| Skill | Interação |
| --- | --- |
| portugal-bookkeeping | Lançamentos contabilísticos do processamento (conta 63x); provisões para subsídios de férias e de Natal |
| portugal-einvoice | Sem interação direta (faturação eletrónica é B2B; recibos de vencimento são autónomos) |
| pt-nhr-ifici | Mecânica de retenção na fonte à taxa especial de 20% para trabalhadores qualificados no regime IFICI / direitos adquiridos do antigo RNH |
| payroll-workflow-base | Fluxo geral de processamento; especificidades portuguesas definidas nesta skill |

### Especificidades do Processamento em Portugal

- **14 pagamentos**: Portugal impõe 14 pagamentos de vencimento por ano. Considerar este facto na conversão de vencimento anual em custo mensal.
- **Duodécimos**: O trabalhador pode requerer o pagamento dos subsídios de férias e de Natal em 12 prestações mensais iguais (1/12 por mês). A entidade patronal também pode optar por este método.
- **Regiões autónomas**: Os Açores e a Madeira têm valores de salário mínimo ligeiramente superiores e podem ter tabelas de retenção de IRS diferentes.
- **Tabelas de retenção de IRS**: Atualizadas anualmente por Despacho da AT (nos termos do art.º 99.º do CIRS). Utilizar sempre as tabelas do ano em curso. As tabelas de 2026 aplicam-se retroativamente a partir de 1 de janeiro de 2026.
- **Subsídio de refeição**: Benefício amplamente generalizado. A parcela isenta (6,00 EUR em numerário / 10,20 EUR em cartão) NÃO está sujeita a Segurança Social nem a IRS. O excesso ESTÁ sujeito.
- **Trabalho suplementar**: Sujeito a contribuições para a Segurança Social e a retenção na fonte de IRS à taxa normal.
- **Regime IFICI / RNH**: Para trabalhadores abrangidos, a retenção na fonte de IRS é efetuada à taxa especial de 20% — consultar a skill **pt-nhr-ifici**.

## Aviso Legal

Esta skill e os respetivos resultados são disponibilizados apenas para fins informativos e de cálculo, não constituindo aconselhamento fiscal, jurídico ou financeiro. A Open Accountants e os seus contribuidores não aceitam qualquer responsabilidade por erros, omissões ou consequências decorrentes da utilização desta skill. Todos os resultados devem ser revistos e validados por profissional qualificado antes da entrega ou de qualquer atuação com base nos mesmos.

A versão mais atualizada e verificada desta skill é mantida em [openaccountants.com](https://openaccountants.com).

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
