---
name: br-inss
description: Use this skill whenever asked about Brazilian INSS social contributions for self-employed individuals (contribuinte individual). Trigger on phrases like "INSS autônomo", "contribuinte individual", "GPS pagamento", "INSS 20%", "INSS simplificado 11%", "teto INSS", "previdência autônomo", or any question about Brazilian social security obligations for self-employed persons. Covers the 20% normal plan, 11% simplified plan, 5% MEI plan, contribution ceiling (teto), GPS payment mechanics, and edge cases. ALWAYS read this skill before touching any Brazilian INSS work.
version: 2.0
jurisdiction: BR
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: A licensed accountant (name withheld at their request)
review_status: current
trust_label: Checked by a licensed accountant (name withheld at their request)
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# BR Inss

## Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by Ariane Marrocos on 2026-06-03.
Items flagged for further clarification are tracked separately and excluded here.
This block is generated from verified `skill_facts` — edit the facts, not the prose.

### INSS Autônomo

- **Salário mínimo** — R$ 1.630,00  _(Legislação federal do salário mínimo 2026)_
- **Teto INSS** — R$ 8.475,55  _(Portaria Interministerial MPS/MF nº 13/2026.)_
- **Plano Normal (20%)** — 20% da renda (mín. R$ 326,00 / máx. R$ 1.695,11) — GPS código 1007  _(Lei 8.212/1991 Art. 21)_
- **Plano Simplificado (11%)** — 11% do salário mínimo = R$ 179,30 (fixo) — GPS código 1163  _(Lei 8.212/1991 Art. 21)_
- **MEI (5%)** — 5% do salário mínimo = R$ 81,50 (fixo) — recolhido via DAS-MEI  _(Lei Complementar nº 123/2006 – Art. 18-A.)_
- **Contribuição mínima (20%)** — R$ 326,00  _(Lei 8.212/1991 Art. 21)_
- **Contribuição máxima (20%)** — R$ 1.695,11  _(Lei 8.212/1991 Art. 21)_
- **1007** — Contribuinte individual — Normal (20%)  _(Lei 8.212/1991)_
- **1163** — Contribuinte individual — Simplificado (11%)  _(Lei 8.212/1991)_
- **1104** — Contribuinte Individual – Prestador de serviços a pessoa jurídica (com retenção previdenciária). Observação: o percentual efetivamente retido pode variar conforme a situação e a legislação previdenciária aplicável.  _(Lei 8.212/1991)_
- **1295** — Complementação (de 11% para 20% retroativa)  _(Lei 8.212/1991)_
- **Vencimento GPS** — Dia 15 do mês seguinte  _(Lei 8.212/1991)_
- **Multa por atraso** — 0,33% ao dia (limitada a 20%) + SELIC acumulada e 1% no mês do pagamento  _(Lei 8.212/1991; Lei 9.430/1996)_
- **Cobrança retroativa** — Até 5 anos  _(CTN Arts. 173 e 174)_
- **Duplo vínculo CLT+autônomo** — Total limitado ao teto; se CLT atinge o teto, sem GPS adicional  _(Lei 8.212/1991)_
- **Mês sem renda** — Sem contribuição obrigatória; pode recolher como facultativo  _(Lei nº 8.212/1991 Lei nº 8.213/1991)_
- **Plano 11% → aposentadoria por tempo** — Não conta para benefícios que exijam contribuição integral, salvo complementação para 20%  _(Lei 8.212/1991)_

## Seção 1 — Referência rápida

**Referência rápida**

| Campo | Valor |
| --- | --- |
| País | Brasil (República Federativa do Brasil) |
| Autoridade | Receita Federal (arrecadação); INSS (benefícios) |
| Legislação principal | Lei 8.212/1991 (Custeio); Lei 8.213/1991 (Benefícios) |
| Legislação complementar | Decreto 3.048/1999; LC 123/2006 (MEI) |
| Alíquota do Plano Normal | 20% da renda (entre salário mínimo e teto) |
| Alíquota do Plano Simplificado | 11% do salário mínimo (fixo) |
| Alíquota MEI | 5% do salário mínimo (fixo) |
| Salário mínimo (2025) | R$ 1.518,00 |
| Teto INSS (2025) | R$ 8.157,41 |
| Contribuição mínima (20%) | R$ 303,60 |
| Contribuição máxima (20%) | R$ 1.631,48 |
| Simplificado (11%) | R$ 166,98 |
| MEI (5%) | R$ 75,90 |
| Vencimento da GPS | Dia 15 do mês seguinte |
| Moeda | Apenas BRL |
| Contribuidor | Open Accountants |
| Validado por | Verificado por Ariane Marrocos (SP 312052/O-1) em 2026-06-03 |
| Data de validação | Verificado por Ariane Marrocos (SP 312052/O-1) em 2026-06-03 |

A Reforma Tributária 2026 (EC 132/2023, LC 214/2025) reforma apenas tributos sobre consumo (PIS, Cofins, ICMS, ISS, IPI → CBS+IBS). O INSS não é afetado — alíquotas e regras permanecem.

## Seção 2 — Insumos obrigatórios e catálogo de recusas

### Insumos obrigatórios

- **Insumos obrigatórios antes de calcular** — 1. Classificação do trabalhador — contribuinte individual, MEI ou facultativo? 2. Renda bruta mensal do trabalho autônomo 3. Emprego concorrente (CLT)? — regras de duplo vínculo 4. Plano desejado — Plano Normal (20%) ou Simplificado (11%) 5. O cliente deseja aposentadoria por tempo de contribuição? — somente com o plano de 20% 6. O cliente é MEI? — regime separado de 5% Se a classificação for desconhecida, PARE.

### Catálogo de recusas

- **R-BR-INSS-1 — Acordo bilateral** — Gatilho: trabalhador estrangeiro com acordo bilateral de previdência social. Mensagem: "Acordos bilaterais podem isentar do INSS. Escalar para revisão jurídica."
- **R-BR-INSS-2 — Cálculo de juros da complementação** — Gatilho: cálculo retroativo de complementação (código 1295) com juros. Mensagem: "O cálculo de juros pela SELIC exige dados de taxa atualizados. Escalar para contador."

### Proibições

- **Proibições** — NUNCA permitir que cliente do plano de 11% acredite que tem direito à aposentadoria por tempo — não tem NUNCA calcular abaixo do piso do salário mínimo NUNCA calcular acima do teto (plano de 20%) NUNCA ignorar retenções de PJ ao apurar a diferença da GPS NUNCA dizer a cliente com renda zero que ele deve pagar — é facultativo nos meses sem renda NUNCA confundir códigos de contribuinte individual (1007/1163) com códigos de facultativo (1406/1473) NUNCA apresentar a alíquota de 5% do MEI como disponível para não-MEI NUNCA calcular juros de complementação sem a SELIC vigente

## Seção 3 — Planos de contribuição

**Planos de contribuição**  _(Lei 8.212/1991 Art. 21)_

| Plano | Alíquota | Base | Código GPS | Benefícios |
| --- | --- | --- | --- | --- |
| Plano Normal | 20% | Renda (mínimo–teto) | 1007 | Completos: idade, tempo, invalidez, pensão, auxílio |
| Plano Simplificado | 11% | Salário mínimo (fixo) | 1163 | Limitados: apenas idade |
| MEI | 5% | Salário mínimo (fixo) | DAS-MEI | Limitados: apenas idade |

## Seção 4 — Regras de cálculo

### Plano Normal (20%)

- **Fórmula Plano Normal** — contribution = min(monthly_income, teto_INSS) x 20% contribution = clamp(R$ 303.60, contribution, R$ 1,631.48)

### Plano Simplificado (11%)

- **Fórmula Plano Simplificado** — contribution = R$ 1,518.00 x 11% = R$ 166.98 (fixed)
- **Base fixa** — Sempre baseado no salário mínimo, independentemente da renda efetiva.

### Retenção de PJ (serviços prestados a empresas)

- **Regra de retenção de PJ** — A empresa retém 11% do pagamento (até o teto). Se o cliente estiver no plano de 20%, pagar a diferença de 9% via GPS código 1007. Se o total de retenções de várias PJs atingir o teto, não há pagamento adicional necessário.

## Seção 5 — Pagamento da GPS e cadastro

### GPS (Guia da Previdência Social)

**GPS (Guia da Previdência Social)**

| Item | Detalhe |
| --- | --- |
| Gerada via | Gov.br, Meu INSS ou Carnê manual |
| Vencimento | Dia 15 do mês seguinte |
| Canais de pagamento | Banco, internet banking, lotéricas |

### Códigos da GPS

**Códigos da GPS**

| Código | Descrição |
| --- | --- |
| 1007 | Contribuinte individual — Normal (20%) |
| 1163 | Contribuinte individual — Simplificado (11%) |
| 1104 | Contribuinte individual — serviço para PJ (empresa retém 11%) |
| 1295 | Complementação (de 11% para 20% retroativa) |

### Cadastro

- **Cadastro** — CPF obrigatório. Deve possuir NIT/PIS/PASEP.

## Seção 6 — Dedutibilidade fiscal e penalidades

### Dedutibilidade fiscal

**Dedutibilidade fiscal**

| Pergunta | Resposta |
| --- | --- |
| Dedutível? | SIM — da renda bruta para fins de IRPF |
| Onde? | Declaração anual do IRPF |
| Carnê-leão | INSS deduzido antes de apurar a estimativa mensal |

### Penalidades

**Penalidades**

| Penalidade | Detalhe |
| --- | --- |
| Pagamento em atraso | SELIC diária + 0,33%/dia (limitada a 20%) |
| Não pagamento | Períodos não contam para aposentadoria |
| Cobrança retroativa | Até 5 anos |

## Seção 7 — Duplo vínculo e mudança de plano

### Empregado CLT + autônomo

- **Regra de duplo vínculo** — Total do INSS limitado ao teto. Se as contribuições do emprego atingirem o teto, não há INSS adicional como autônomo.

### Mês sem renda

- **Mês sem renda** — Sem contribuição obrigatória. O mês não conta. Pode-se pagar como facultativo opcionalmente.

### Mudança de Simplificado para Normal

- **Mudança de plano** — Cliente no plano de 11% pode mudar para 20% a partir daquela data. Para períodos anteriores, pagar complementação (diferença de 9%) via GPS código 1295 com juros pela SELIC.

### MEI que ultrapassa o limite de receita

- **MEI ultrapassa limite** — Deve ser desenquadrado. Passa a contribuinte individual. Períodos anteriores como MEI (5%) valem apenas para aposentadoria por idade. Sinalizar para revisor.

## Seção 8 — Registro de casos excepcionais

### EC1 — Plano Simplificado deseja aposentadoria por tempo

Situação: Cliente no plano de 11% precisa de aposentadoria por tempo de contribuição.
Resolução: Mudar para 20% ou pagar complementação (código 1295) referente aos períodos anteriores.

### EC2 — Duplo vínculo, emprego no teto

Situação: Salário CLT de R$ 8.157,41, com renda adicional como autônomo.
Resolução: O vínculo empregatício já atinge o teto. Nenhuma GPS adicional.

### EC3 — Retenção de PJ + plano de 20%

Situação: R$ 6.000 de PJ, retidos 11% = R$ 660. Cliente no plano de 20%.
Resolução: Devido R$ 1.200. Retido R$ 660. GPS de R$ 540.

### EC4 — Renda abaixo do mínimo

Situação: Renda de R$ 800.
Resolução: Base mínima de R$ 1.518. Contribuição de R$ 303,60 (20%) ou R$ 166,98 (11%).

### EC5 — Várias PJs, retenção excedente

Situação: R$ 5.000 da PJ-A + R$ 5.000 da PJ-B. Ambas retêm 11%.
Resolução: Total de R$ 10.000, mas teto de R$ 8.157,41. Retenção máxima = R$ 897,32. Pode ter havido pagamento a maior. Solicitar restituição.

### EC6 — Mês sem renda

Situação: Sem renda em março/2025.
Resolução: Sem contribuição obrigatória. Pode-se pagar como facultativo.

## Seção 9 — Protocolo de escalonamento ao revisor

Quando uma situação exigir julgamento do revisor:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Qualified contador must confirm before advising client.
```

Quando a situação estiver fora do escopo da skill:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified contador. Document gap.
```

## Seção 10 — Bateria de testes

### Teste 1 — 20% padrão, faixa intermediária

Entrada: Renda de R$ 4.000. Normal (20%). Sem retenção de PJ.
Saída esperada: R$ 800,00. GPS 1007.

### Teste 2 — Excede o teto

Entrada: Renda de R$ 12.000. Normal (20%).
Saída esperada: Base limitada a R$ 8.157,41. Contribuição de R$ 1.631,48.

### Teste 3 — Simplificado

Entrada: Renda de R$ 5.000. Simplificado (11%).
Saída esperada: R$ 166,98 (fixo sobre o mínimo). GPS 1163.

### Teste 4 — Retenção de PJ + diferença de 20%

Entrada: R$ 6.000 de PJ. Retido R$ 660. Plano de 20%.
Saída esperada: Devido R$ 1.200. GPS de R$ 540.

### Teste 5 — Duplo vínculo, no teto

Entrada: CLT R$ 8.157,41 + autônomo R$ 3.000.
Saída esperada: Nenhuma GPS adicional.

### Teste 6 — Sem renda

Entrada: Sem renda em março/2025.
Saída esperada: Sem contribuição obrigatória.

### Teste 7 — Renda mínima

Entrada: Renda de R$ 800. Normal (20%).
Saída esperada: Base de R$ 1.518. Contribuição de R$ 303,60.

## Aviso legal

Esta skill e seus resultados são fornecidos apenas para fins informativos e de cálculo e não constituem aconselhamento tributário, jurídico ou financeiro. A Open Accountants e seus contribuidores não se responsabilizam por quaisquer erros, omissões ou consequências decorrentes do uso desta skill. Todos os resultados devem ser revisados e aprovados por um profissional qualificado (como contador, EA, advogado tributarista ou profissional licenciado equivalente em sua jurisdição) antes do envio ou de qualquer ação.

A versão mais atualizada e verificada desta skill é mantida em [openaccountants.com](https://openaccountants.com). Faça login para acessar a versão mais recente, solicitar revisão profissional por um contador licenciado e acompanhar atualizações conforme a legislação tributária mudar.

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
