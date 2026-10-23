---
name: pt-income-tax
description: "Utilizar esta skill sempre que for solicitada ajuda com o IRS (Imposto sobre o Rendimento das Pessoas Singulares) em Portugal para trabalhadores independentes. Acionar com expressões como \"quanto IRS pago\", \"IRS Portugal\", \"Modelo 3\", \"Anexo B\", \"Categoria B\", \"regime simplificado\", \"contabilidade organizada\", \"retenção na fonte\", \"trabalhador independente\", \"recibos verdes\", \"coeficientes regime simplificado\", \"IRS Jovem\", \"adicional de solidariedade\", ou qualquer questão sobre apresentação ou cálculo de IRS para um cliente independente em Portugal. Esta skill abrange a declaração anual Modelo 3 + Anexo B, rendimentos da Categoria B, regime simplificado vs contabilidade organizada, escalões progressivos do IRS, adicional de solidariedade, deduções específicas, retenção na fonte, IRS Jovem e prazos de entrega. LER SEMPRE esta skill antes de tocar em qualquer trabalho de IRS português. Para regime RNH/IFICI ver skill pt-nhr-ifici. Trigger also on: \"how much tax do I pay in Portugal\", \"IRS Portugal\", \"Modelo 3\", \"income tax return Portugal\", \"NIF\", \"freelancer Portugal tax\"."
version: 2.0
jurisdiction: PT
tax_year: 2026
last_updated: 2026-10-23
reviewed_by: A licensed accountant (name withheld at their request)
review_status: current
trust_label: Checked by a licensed accountant (name withheld at their request)
source_checked: 2026-10-16
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# PT Income Tax

## Portugal — IRS (Imposto sobre o Rendimento das Pessoas Singulares) — Skill v3.1

> **Nota de remissão:** Se o contribuinte está sob regime RNH (Residente Não Habitual) ou IFICI (Incentivo Fiscal à Investigação Científica e Inovação), **ver o skill `pt-nhr-ifici`** para o tratamento detalhado. Esta skill cobre apenas o regime geral progressivo.

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **Mário Jorge da costa Vale** on 2026-06-04.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.
> **2026 update (2026-10-23):** the IRS bands and the IRS Jovem cap below were moved to tax year 2026 from the AT pages listed under Sources. The 2026 figures were not part of the 2026-06-04 review. The coefficients, withholding rates, thresholds and deadlines did not change for 2026.

### IRS Independente

**IRS Independente — rates & thresholds, tax year 2026**  _([CIRS art. 68.º / Redação da Lei n.º 73-A/2025, de 30/12](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs68.aspx))_

- **0 – €8.342** — 0 – €8.342 ; 12,50%  _(CIRS art. 68.º / Redação da Lei n.º 73-A/2025, de 30/12)_
- **€8.342 – €12.587** — 8.342 – €12.587 ; 15,70%  _(CIRS art. 68.º / Redação da Lei n.º 73-A/2025, de 30/12)_
- **€12.587 – €17.838** — 12.587 – €17.838 ; 21,20%  _(CIRS art. 68.º / Redação da Lei n.º 73-A/2025, de 30/12)_
- **€17.838 – €23.089** — 17.838 – €23.089 ; 24,10%  _(CIRS art. 68.º / Redação da Lei n.º 73-A/2025, de 30/12)_
- **€23.089 – €29.397** — 23.089 – €29.397 ; 31,10%  _(CIRS art. 68.º / Redação da Lei n.º 73-A/2025, de 30/12)_
- **€29.397 – €43.090** — 29.397 – €43.090 ; 34,90%  _(CIRS art. 68.º / Redação da Lei n.º 73-A/2025, de 30/12)_
- **€43.090 – €46.566** — 43.090 – €46.566 ; 43,10%  _(CIRS art. 68.º / Redação da Lei n.º 73-A/2025, de 30/12)_
- **€46.566 – €86.634** — 46.566 – €86.634 ; 44,60%  _(CIRS art. 68.º / Redação da Lei n.º 73-A/2025, de 30/12)_
- **Acima de €86.634** — Acima de €86.634 ; 48,00%  _(CIRS art. 68.º / Redação da Lei n.º 73-A/2025, de 30/12)_
- **€80.000 – €250.000** — 2,5%  _(CIRS)_
- **Acima de €250.000** — 5%  _(CIRS)_
- **Vendas de bens** — 0,15 (15% do bruto tributável; inclui operações com criptoativos, exceto mineração)  _(CIRS Art. 31.º, nº 1, a))_
- **Prestação de serviços** — 0,75 (atividades profissionais da tabela do art. 151.º) ; 0,35 (restantes prestações de serviços)  _(CIRS Art. 31.º, nº 1, b) e c))_
- **Hotelaria/alojamento** — 0,15 (exceto alojamento local na modalidade de moradia ou apartamento)  _(CIRS Art. 31.º)_
- **Propriedade intelectual (autor)** — Isenção de 50% até máximo de 10.000 ; o restante é sujeito a coeficiente de 0,95  _(CIRS Art. 31.º)_
- **Outros rendimentos Cat. B** — 0,10  _(CIRS Art. 31.º)_
- **Limiar contabilidade organizada** — > €200.000 de receitas (em dois períodos de tributação consecutivos, ou num único em montante superior a 25 %)  _(CIRS)_
- **Trabalhador independente Cat. B** — * CIRS Art. 101.º, nº 1, a) 16,5% ; * CIRS Art. 101.º, nº 1, b) 23% ; * CIRS Art. 101.º, nº 1, c) 11,5%  _(CIRS Art. 101.º)_
- **Ano 1** — Ano 1 - 100%  _(CIRS, artº 12º-B, nº 5, a) ; (máx. 55 x IAS = €29.542,15 em 2026 ; IAS 2026 = 537,13, Portaria n.º 480-A/2025/1))_
- **Anos 2–4** — Ano 2-4 - 75%  _(CIRS, artº 12º-B, nº 5, b))_
- **Anos 5–7** — Ano 5-7 - 50%  _(CIRS, artº 12º-B, nº 5, c))_
- **Anos 8–10** — Ano 8-10 - 25%  _(CIRS, artº 12º-B, nº 5, d))_
- **Entrega Modelo 3** — 1 abril – 30 junho  _(CIRS)_
- **Pagamentos por conta** — Até dia 20 de Julho, setembro, dezembro (dispensado se prestação < €50)  _(CIRS Art. 102º, nº 1 e 3)_

## Secção 1 — Referência Rápida

### Escalões de IRS 2026 (regime geral — rendimentos de 2026)

**Escalões de IRS 2026 (regime geral — rendimentos de 2026)**  _([art. 68.º n.º 1 do CIRS na redação da Lei n.º 73-A/2025, de 30 de dezembro](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs68.aspx))_

| Rendimento Coletável (EUR) | Taxa Normal (A) | Taxa Média (B) | Imposto cumulativo no limite superior |
| --- | --- | --- | --- |
| Até 8 342 | 12,50% | 12,500% | 1 042,75 |
| 8 342 – 12 587 | 15,70% | 13,579% | 1 709,19 |
| 12 587 – 17 838 | 21,20% | 15,823% | 2 822,51 |
| 17 838 – 23 089 | 24,10% | 17,705% | 4 087,91 |
| 23 089 – 29 397 | 31,10% | 20,579% | 6 049,61 |
| 29 397 – 43 090 | 34,90% | 25,130% | 10 828,52 |
| 43 090 – 46 566 | 43,10% | 26,472% | 12 326,95 |
| 46 566 – 86 634 | 44,60% | 34,856% | 30 197,15 |
| Acima de 86 634 | 48,00% | — | — |

- **Fórmula (usada nesta skill)** — Imposto = imposto cumulativo do escalão inferior + (rendimento − limite inferior do escalão) × taxa marginal.  _(art. 68.º n.º 1 e 2 do CIRS)_
- **Convenção de arredondamento** — O imposto cumulativo da tabela é o limite superior do escalão × taxa média (coluna B), arredondado ao cêntimo. É o método da liquidação oficial (art. 68.º n.º 2: parte até ao limite do maior escalão × coluna B + excedente × coluna A do escalão seguinte), por isso a fórmula acima dá o mesmo valor que a AT.  _(art. 68.º n.º 2 CIRS)_
- **Atenção ao ano** — Para rendimentos de 2025 aplica-se a tabela da Lei n.º 55-A/2025 (8 059 … 83 696; 2.º escalão 16,00%). Não usar a tabela de 2026 para 2025, nem a de 2025 para 2026. A tabela de 2026 baixou as taxas dos 2.º a 5.º escalões e subiu todos os limites (Lei n.º 73-A/2025, OE2026, em vigor desde 1 de janeiro de 2026).  _(Lei n.º 73-A/2025 (OE2026))_
- **Verificação prévia obrigatória** — Antes de aplicar as tabelas progressivas, verificar se o contribuinte está abrangido por RNH ou IFICI (ver skill `pt-nhr-ifici`).

### Adicional de Solidariedade (art. 68.º-A CIRS)

**Adicional de Solidariedade (art. 68.º-A CIRS)**  _(art. 68.º-A CIRS)_

| Rendimento Coletável (EUR) | Taxa |
| --- | --- |
| 80 000 – 250 000 | 2,5% sobre o excedente acima de EUR 80 000 |
| Acima de 250 000 | 2,5% sobre EUR 170 000 + 5% sobre o excedente acima de EUR 250 000 |

- **Tributação conjunta** — Em tributação conjunta, aplica-se a metade do rendimento coletável e multiplica-se a coleta por dois.  _(art. 68.º-A n.º 3 CIRS)_

### Regime Simplificado — Coeficientes 2026 (art. 31.º n.º 1 CIRS)

**Regime Simplificado — Coeficientes 2026 (art. 31.º n.º 1 CIRS, sem alterações em 2026)**  _([art. 31.º n.º 1 CIRS](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs31.aspx))_

| Tipo de Rendimento | Coeficiente | Base Tributável Efetiva |
| --- | --- | --- |
| Vendas de mercadorias e produtos; operações com criptoativos (exceto mineração); atividades de restauração/bebidas e hotelaria (exceto alojamento local na modalidade de moradia ou apartamento) | 0,15 | 15% do bruto |
| **Atividades profissionais da tabela do art. 151.º** (Portaria 1011/2001 — inclui, entre outros: arquitetos 1001, engenheiros 1003, consultores 1320, programadores informáticos 1332, tradutores 1334, designers 1336, e o código residual **1519 — outros prestadores de serviços**) | **0,75** | 75% do bruto |
| Prestações de serviços **não** previstas na tabela do art. 151.º nem noutras alíneas | 0,35 | 35% do bruto |
| Mineração de criptoativos; propriedade intelectual e industrial (exploração), rendimentos prediais, capitais e mais-valias imputados à atividade | 0,95 | 95% do bruto |
| Alojamento local (moradia/apartamento) em zona de contenção | 0,50 | 50% do bruto |
| Subsídios não destinados à exploração | 0,30 | 30% do bruto |
| Subsídios à exploração e restantes rendimentos da Categoria B | 0,10 | 10% do bruto |

- **Propriedade intelectual — benefício EBF art. 58.º** — Se o titular for o titular originário residente, apenas 50% do rendimento é englobado, com limite de EUR 10 000 de montante excluído (regime em vigor até 2026 — Lei 20/2023); o remanescente segue o coeficiente 0,95. Não existe coeficiente 0,50 para propriedade intelectual.  _(EBF art. 58.º; Lei 20/2023)_
- **Armadilha de classificação** — A maioria das profissões liberais exercidas pessoalmente cai na tabela do art. 151.º (coeficiente 0,75) — incluindo, pela posição da AT, o código residual 1519 (mas, para retenção na fonte, a AT aplica ao código 1519 a taxa de 11,5% da alínea c) do n.º 1 do artigo 101.º). O coeficiente 0,35 só se aplica a prestações de serviços fora da tabela. Verificar o código de atividade no registo do contribuinte antes de escolher o coeficiente.  _([art. 151.º CIRS](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/informacoes_vinculativas/rendimento/cirs/Documents/PIV_16493.pdf))_
- **Dedução de contribuições obrigatórias (art. 31.º n.º 2)** — Nos rendimentos das alíneas b) e c), as contribuições obrigatórias para regimes de proteção social são dedutíveis apenas na parte em que excedam 10% dos rendimentos brutos (e quando não deduzidas a outro título). Não deduzir a totalidade da SS à base coeficiente.  _(art. 31.º n.º 2 CIRS)_
- **Regra dos 15% (art. 31.º n.º 13)**: Nas alíneas b) e c), acresce ao rendimento tributável a diferença positiva entre 15% do bruto e a soma da dedução específica do art. 25.º n.º 1 a) (EUR 4 587,09 em 2026 = 8,54 × IAS) ou, se superior, das contribuições não deduzidas pelo n.º 2, com as despesas comunicadas na e-fatura (pessoal, rendas, 1,5% do VPT, outras despesas da atividade). Os exemplos abaixo assumem que as despesas comunicadas cobrem os 15%.  _([art. 31.º n.º 13 CIRS](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs31.aspx); art. 25.º n.º 1 a))_
- **Limiar de elegibilidade do regime simplificado** — EUR 200 000 EUR (Receitas brutas do ano anterior (ou estimadas no ano corrente para novos contribuintes) ≤ EUR 200 000)  _([CIRS art. 28.º n.º 2 e 10](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs28.aspx))_

### Regime de Contabilidade Organizada (Despesas Reais)

- **Regime de Contabilidade Organizada (Despesas Reais)** — Quando as receitas brutas > EUR 200 000 (obrigatório) ou por opção: rendimento tributável = receitas brutas − despesas dedutíveis reais (requer Contabilista Certificado / CC). Aqui as contribuições SS deduzem-se integralmente como gasto.  _(CIRS)_

### Retenção na Fonte (Retenção pelos Clientes) — art. 101.º n.º 1 CIRS (redação Lei 45-A/2024)

**Retenção na Fonte (Retenção pelos Clientes) — art. 101.º n.º 1 CIRS (redação Lei 45-A/2024)**  _(art. 101.º n.º 1 CIRS (redação Lei 45-A/2024))_

| Tipo de Rendimento / Beneficiário | Taxa |
| --- | --- |
| Atividades profissionais da tabela do art. 151.º (art. 101.º n.º 1 b)) | **23%** |
| Propriedade intelectual e incrementos patrimoniais (art. 101.º n.º 1 a)) | 16,5% |
| Outros rendimentos Categoria B (art. 101.º n.º 1 c)) | 11,5% |
| Não residente — Categoria B (art. 71.º n.º 4 a), taxa liberatória) | 25% |

- **Recomposição do bruto** — Clientes empresariais que pagam a um profissional da tabela do art. 151.º com NIF retêm 23% e entregam à AT. O montante retido é creditado contra a coleta final de IRS. Recomposição do bruto: recebido ÷ 0,77.  _(art. 101.º n.º 1 b) CIRS)_
- **Transição 2025** — A taxa da al. b) baixou de 25% para 23% com o OE2025 (Lei 45-A/2024); no início de 2025 alguns clientes ainda aplicaram 25%. Confirmar sempre a taxa efetivamente retida em cada recibo antes de recompor — não presumir.  _(Lei 45-A/2024 (OE2025))_
- **Dispensa de retenção na fonte (art. 101.º-B n.º 1 a))** — Dispensados os titulares que prevejam auferir na categoria um montante anual inferior ao limiar do art. 53.º n.º 1 do CIVA — EUR 15 000 em 2026 (mecanismo prospetivo, não rendimento do ano anterior; vedado se no ano anterior o limite já foi atingido — n.º 3).  _(art. 101.º-B n.º 1 a) CIRS; art. 53.º n.º 1 CIVA)_

### Segurança Social (Contribuições)

**Segurança Social (Contribuições)**  _(https://www.seg-social.pt/ptss/pssd/documento/cmdddzytm006agq2y1ci6tibc)_

| Esquema | Valor | Base |
| --- | --- | --- |
| Trabalhador independente SS | 21,4% (25,2% para empresários em nome individual) | 70% das receitas brutas trimestrais de prestação de serviços (20% nas vendas de bens e hotelaria/restauração) ÷ 3 (base mensal) |
| Limite máximo da base mensal | 12 × IAS = EUR 6 445,56 (2026; IAS 2026 = EUR 537,13) | Rendimento relevante mensal acima do teto não contribui |
| Novos trabalhadores independentes | Isenção nos primeiros 12 meses de atividade (primeira inscrição) | Confirmar data de início na SS |

- **Dedutibilidade das contribuições SS** — Contribuições SS: em contabilidade organizada deduzem-se integralmente como gasto; em regime simplificado deduzem-se apenas na parte que exceda 10% do bruto (art. 31.º n.º 2).  _(art. 31.º n.º 2 CIRS)_

### IRS Jovem (art. 12.º-B CIRS, redação Lei 45-A/2024 / OE2025)

Para contribuintes até 35 anos (não dependentes), nos primeiros 10 anos de obtenção de rendimentos das categorias A e B:

**Escala de isenção IRS Jovem**  _(art. 12.º-B CIRS, redação Lei 45-A/2024 / OE2025)_

| Ano de rendimentos | Isenção |
| --- | --- |
| Ano 1 | 100% |
| Anos 2–4 | 75% |
| Anos 5–7 | 50% |
| Anos 8–10 | 25% |

- **Limite anual da isenção** — 55 × IAS = EUR 29 542,15 em 2026 (IAS 2026 = EUR 537,13, Portaria n.º 480-A/2025/1). Para rendimentos de 2025 o limite era EUR 28 737,50 (IAS 2025 = EUR 522,50). O limite aplica-se ao rendimento isento de cada ano.  _([art. 12.º-B n.º 5 CIRS](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs12b.aspx))_
- **Englobamento para taxa** — O rendimento isento é englobado para determinação da taxa aplicável ao rendimento não isento (não se tributa o remanescente "a partir do zero" da tabela).  _(art. 12.º-B CIRS)_
- **Confirmação de elegibilidade** — Confirmar elegibilidade e o número do ano antes de aplicar. As contribuições para a SS continuam a aplicar-se.

### Defaults Conservadores

**Defaults Conservadores**

| Situação | Pressuposto por Defeito |
| --- | --- |
| Tipo de serviço ambíguo (tabela 151.º vs outros serviços) | Aplicar coeficiente **0,75** — base mais elevada; sinalizar ao cliente para confirmar o código de atividade |
| Regime simplificado vs. contabilidade organizada | Regime simplificado (default para < EUR 200 000 receitas) |
| Elegibilidade IRS Jovem ambígua | NÃO aplicar — sinalizar ao cliente para confirmar anos de elegibilidade |
| Estatuto RNH/IFICI ambíguo | NÃO aplicar taxas especiais — aplicar escalões padrão; remeter para skill `pt-nhr-ifici` |
| Contribuições SS não fornecidas | Estimar a 21,4% × 70% do bruto (com teto 12 × IAS mensal = EUR 6 445,56 em 2026); sinalizar como estimativa |
| Taxa de retenção efetiva desconhecida | NÃO presumir 23% nem 25% — exigir os recibos/declarações de retenção |
| Despesa em contabilidade organizada sem fatura/recibo | Rejeitar — não dedutível sem documento de suporte |

### Limiares de Alerta (Red Flags)

**Limiares de Alerta (Red Flags)**

| Alerta | Limiar |
| --- | --- |
| Receitas brutas > EUR 200 000 | Contabilidade organizada obrigatória — parar se ainda em simplificado |
| Cliente único > 80% das receitas | Risco de requalificação como relação laboral (falso recibo verde) |
| Sem retenções recebidas mas clientes são empresas | Verificar — para profissões da tabela 151.º a retenção legal é 23% (salvo dispensa do art. 101.º-B) |
| Contribuições SS aparentemente ausentes ou muito baixas | Verificar cálculo da base SS (e isenção de 1.º ano, se aplicável) |
| IRS Jovem reclamado após o 10.º ano de rendimentos | Inelegível — sinalizar imediatamente |
| Coeficiente 0,35 usado por profissional da tabela 151.º | Errado na maioria dos casos — verificar código de atividade (0,75) |

## Secção 2 — Inputs Obrigatórios + Catálogo de Recusas

### Inputs Obrigatórios

Antes de calcular o IRS português, recolher:

1. **Total das receitas brutas** (recibos verdes emitidos e recebidos) — Categoria B integral
2. **Código de atividade no registo da AT** (tabela art. 151.º vs CAE) — determina o coeficiente (0,75 vs 0,35) e a taxa de retenção
3. **Discriminação por cliente** — para identificar tipo de serviço e retenções
4. **Declarações de retenção na fonte** — de cada cliente, com a taxa efetivamente aplicada
5. **Pagamentos de contribuições para a SS** — recibos trimestrais/mensais
6. **Regime aplicável** — simplificado ou contabilidade organizada (se eleito)
7. **Estatuto IRS Jovem** — idade + número do ano de obtenção de rendimentos
8. **Extratos bancários** — 12 meses do ano fiscal
9. **Estatuto RNH ou IFICI** — se aplicável (caso em que se remete para skill `pt-nhr-ifici`)
10. **Outras categorias de rendimentos** — Categoria A, F, G
11. **Estado civil e dependentes** — para quociente conjugal e deduções por dependentes

### Catálogo de Recusas

- **R-PT-1** — Receitas brutas > EUR 200 000 mas cliente insiste no regime simplificado (Parar — contabilidade organizada obrigatória; necessário Contabilista Certificado (CC))
- **R-PT-2** — Estatuto RNH/IFICI alegado (Remeter para skill `pt-nhr-ifici` — não aplicar regras especiais nesta skill)
- **R-PT-3** — Sem declarações de retenção mas pagamentos efetuados por empresas portuguesas (Sinalizar — para profissões da tabela 151.º a retenção legal é de 23% (art. 101.º n.º 1 b)); recolher declarações antes de finalizar)
- **R-PT-4** — Risco de falso recibo verde (cliente único > 80% das receitas, regularidade laboral) (Sinalizar — a AT pode requalificar como Categoria A; aconselhar revisão jurídica)
- **R-PT-5** — Contabilidade organizada sem CC (Parar — exige legalmente a assinatura de CC; não prosseguir sem este)
- **R-PT-6** — Código de atividade não confirmado e o coeficiente muda o resultado (0,75 vs 0,35) (Parar — pedir o comprovativo de início/alteração de atividade da AT antes de finalizar)

## Secção 3 — Biblioteca de Padrões Transacionais

[Secção inalterada, exceto I-07 e E-17:]

**Padrões de descritivo I-07 / E-17**

| # | Padrão de Descritivo | Linha Fiscal | Notas |
| --- | --- | --- | --- |
| I-07 | `RETENÇÃO NA FONTE` (linha separada ou anotação) | Crédito de retenção | Recomposição: recebido = líquido após retenção → bruto = recebido ÷ (1 − taxa). Profissões da tabela 151.º: ÷ 0,77 (23%); confirmar taxa efetiva no recibo (transição 2025 pode mostrar 25% → ÷ 0,75) |
| E-17 | `DESCONTO RECIBO VERDE` / `RETENÇÃO CLIENTE` | Retenção pelo cliente (23% — tabela 151.º) | Não é despesa — crédito contra IRS; verificar com declaração |

## Secção 4 — Exemplos Práticos

### Exemplo 1 — Millennium BCP (Lisboa, Consultora — Regime Simplificado)

**Cliente:** Ana Ferreira, consultora de gestão (código 1320 da tabela do art. 151.º), Lisboa, regime simplificado.

[Extrato inalterado.]

**Nota:** Os clientes retiveram **23%** à fonte (art. 101.º n.º 1 b); taxa confirmada nos recibos). Montantes brutos antes de retenção (÷ 0,77):
- EMPRESA ALPHA: EUR 3 750,00 ÷ 0,77 = **EUR 4 870,13**
- STARTUP BETA: EUR 2 500,00 ÷ 0,77 = **EUR 3 246,75**
- GAMMA CONSULTING: EUR 4 200,00 ÷ 0,77 = **EUR 5 454,55**
- DELTA SA: EUR 3 100,00 ÷ 0,77 = **EUR 4 025,97**

Stripe: EUR 1 920 líquido (sem retenção — pagador estrangeiro). Recompor para ~EUR 1 978 (bruto faturado antes de comissões).

**Passo 1 — Total de Receitas Brutas**

```
Recompostas de clientes com retenção:  4 870,13 + 3 246,75 + 5 454,55 + 4 025,97 = EUR 17 597,40
Stripe bruto (sem retenção):           EUR  1 978,00
Restantes meses (extrapolados):        admitir ano completo = EUR 52 000 bruto (exemplo)
Total bruto Categoria B:               EUR 52 000
Total efetivamente retido:             17 597,40 − 13 550,00 = EUR 4 047,40
```

**Passo 2 — Coeficiente do Regime Simplificado**

```
Consultora (código 1320 — tabela art. 151.º) → coeficiente 0,75
Base tributável: EUR 52 000 × 0,75 = EUR 39 000
Dedução SS (art. 31.º n.º 2): SS paga EUR 4 200; 10% do bruto = EUR 5 200
  → excesso = max(0; 4 200 − 5 200) = EUR 0 → sem dedução
Regra dos 15% (art. 31.º n.º 13): assume-se que as despesas comunicadas cobrem os 15%
Rendimento tributável para IRS: EUR 39 000
```

**Passo 3 — Cálculo do IRS (tabela 2026, Lei 73-A/2025)**

```
Até 29 397:                              EUR 6 049,61 (cumulativo = 29 397 × 20,579%)
(39 000 − 29 397) × 34,90% = 9 603 × 0,349 = EUR 3 351,45
IRS bruto: 6 049,61 + 3 351,45 =         EUR 9 401,06
Menos retenções na fonte (23% efetivo):  EUR 4 047,40
Saldo IRS:                               EUR 9 401,06 − 4 047,40 = **EUR 5 353,66 a pagar**
(mais pagamentos por conta já efetuados, se existirem; deduções à coleta não incluídas)
```

```oa-check
name: PT Categoria B consultora, regime simplificado, bruto EUR 52,000 (2026)
inputs:
  gross: 52000
  coefficient: 0.75
  ss_paid: 4200
  band6_floor: 29397
  band5_avg: 0.20579
  band6_rate: 0.349
  withheld: 4047.40
steps:
  - ss_deduction: max(0, ss_paid - gross * 0.10)
  - taxable: gross * coefficient - ss_deduction
  - tax: round(band6_floor * band5_avg + (taxable - band6_floor) * band6_rate, 2)
  - balance: tax - withheld
expected:
  ss_deduction: 0
  taxable: 39000
  tax: 9401.06
  balance: 5353.66
```

Nota didática: na versão anterior desta skill (coeficiente 0,35 + dedução integral da SS + taxas antigas) este caso aparecia como reembolso — estava errado em três pontos distintos.

### Exemplo 2 — Caixa Geral de Depósitos (Porto, Programador)

**Cliente:** Pedro Costa, programador informático (código 1332 — tabela art. 151.º), Porto, IRS Jovem ano 2 (75% isento).

```
Receitas brutas: EUR 45 000 → coeficiente 0,75 (tabela 151.º)
Base tributável: 45 000 × 0,75 = EUR 33 750
SS paga: 45 000 × 70% × 21,4% = EUR 6 741,00
Dedução SS (art. 31.º n.º 2): 6 741 − 10% × 45 000 = 6 741 − 4 500 = EUR 2 241
Rendimento tributável: 33 750 − 2 241 = EUR 31 509

IRS Jovem ano 2 → 75% isento; isenção = 31 509 × 75% = EUR 23 631,75
  (abaixo do limite anual de 55 × IAS = EUR 29 542,15 em 2026: OK)
Rendimento não isento: 31 509 × 25% = EUR 7 877,25

Englobamento para taxa (art. 12.º-B n.º 4): imposto sobre a totalidade (31 509):
  6 049,61 + (31 509 − 29 397) × 34,90% = 6 049,61 + 2 112 × 0,349
  = 6 049,61 + 737,09 = EUR 6 786,70
Imposto devido = proporção não isenta: 6 786,70 × 25% = **EUR 1 696,68**
```

```oa-check
name: PT Categoria B programador, IRS Jovem ano 2, bruto EUR 45,000 (2026)
inputs:
  gross: 45000
  coefficient: 0.75
  ss_relevant_share: 0.70
  ss_rate: 0.214
  ias: 537.13
  exempt_share: 0.75
steps:
  - ss_paid: gross * ss_relevant_share * ss_rate
  - ss_deduction: max(0, ss_paid - gross * 0.10)
  - taxable: gross * coefficient - ss_deduction
  - cap: 55 * ias
  - exempt: min(taxable * exempt_share, cap)
  - tax_on_all: round(29397 * 0.20579 + (taxable - 29397) * 0.349, 2)
  - tax_due: round(tax_on_all * (taxable - exempt) / taxable, 2)
expected:
  ss_paid: 6741
  taxable: 31509
  cap: 29542.15
  exempt: 23631.75
  tax_on_all: 6786.70
  tax_due: 1696.68
```

Alerta: o IRS Jovem requer confirmação do número do ano (opção exercida na Modelo 3). NÃO calcular o imposto aplicando o escalão mais baixo diretamente à parte não isenta — o rendimento isento conta para a taxa.

### Exemplo 3 — BPI (Algarve, Arquiteta — Contabilidade Organizada)

**Cliente:** Sofia Pinto, arquiteta, receitas brutas EUR 220 000 (contab. organizada obrigatória apenas se o limite tiver sido ultrapassado em dois períodos de tributação consecutivos ou em montante superior a 25 % num único exercício; caso contrário, por opção; CC exigido).

```
Receitas brutas: EUR 220 000
Despesas dedutíveis (reais):
- Renda do escritório:        EUR 12 000,00
- Utilidades:                 EUR  2 400,00
- Telefone/internet:          EUR  1 200,00
- Software:                   EUR  2 400,00
- Honorários CC:              EUR  4 800,00
- Seguro profissional:        EUR  1 500,00
- Deslocações:                EUR  3 000,00
- Contribuições SS:           EUR 16 552,20
Total de despesas:            EUR 43 852,20

SS — cálculo com teto: rendimento relevante mensal = 70% × 220 000 ÷ 12 = EUR 12 833,33
  > teto de 12 × IAS = EUR 6 445,56/mês (2026) → base mensal limitada a 6 445,56
  SS anual = 6 445,56 × 21,4% × 12 = 1 379,35 × 12 = EUR 16 552,20
  (sem teto seria 220 000 × 70% × 21,4% = 32 956,00 — não aplicável)

Resultado líquido: 220 000 − 43 852,20 = EUR 176 147,80

IRS (tabela 2026, Lei 73-A/2025), escalão acima de 86 634:
  30 197,15 + (176 147,80 − 86 634) × 48%
  = 30 197,15 + 89 513,80 × 0,48
  = 30 197,15 + 42 966,62 = EUR 73 163,77

Adicional de solidariedade (art. 68.º-A; rendimento coletável > 80 000):
  (176 147,80 − 80 000) × 2,5% = 96 147,80 × 0,025 = EUR 2 403,70

Total IRS: 73 163,77 + 2 403,70 = **EUR 75 567,47**
```

```oa-check
name: PT Categoria B arquiteta, contabilidade organizada, receitas EUR 220,000 (2026)
inputs:
  gross: 220000
  other_expenses: 27300
  ias: 537.13
  ss_rate: 0.214
steps:
  - ss_monthly: round(min(gross * 0.70 / 12, 12 * ias) * ss_rate, 2)
  - ss_annual: ss_monthly * 12
  - profit: gross - other_expenses - ss_annual
  - irs: round(86634 * 0.34856 + (profit - 86634) * 0.48, 2)
  - solidarity: round((min(profit, 250000) - 80000) * 0.025, 2)
  - total: irs + solidarity
expected:
  ss_annual: 16552.20
  profit: 176147.80
  irs: 73163.77
  solidarity: 2403.70
  total: 75567.47
```

Alerta: bruto > EUR 200 000 — CC obrigatório; adicional de solidariedade aplica-se; confirmar a base SS efetivamente fixada antes de fechar (em contabilidade organizada, o rendimento relevante corresponde ao lucro tributável do ano anterior, com o máximo de 12 vezes o IAS).

### Exemplo 4 — Santander Portugal (Lisboa, Designer, muitos MB Way)

**Cliente:** Margarida Santos, designer gráfica (código 1336 — tabela art. 151.º), Lisboa.

[Tratamento MB Way inalterado: pagadores particulares não retêm; empresas com NIF retêm — para profissões da tabela 151.º, a 23%.]

```
Receitas brutas MB Way (particulares, sem retenção): EUR 18 000
TRANSF de empresas (brutos; retenção 23% confirmada): EUR 24 000
Total bruto: EUR 42 000

Coeficiente 0,75 (tabela 151.º): 42 000 × 0,75 = EUR 31 500
SS paga: 42 000 × 70% × 21,4% = EUR 6 291,60
Dedução SS: 6 291,60 − 10% × 42 000 = 6 291,60 − 4 200 = EUR 2 091,60
Tributável: 31 500 − 2 091,60 = EUR 29 408,40

IRS (tabela 2026): 6 049,61 + (29 408,40 − 29 397) × 34,90%
   = 6 049,61 + 11,40 × 0,349 = 6 049,61 + 3,98 = EUR 6 053,59
Menos retenções: 24 000 × 23% = EUR 5 520,00
Saldo IRS: 6 053,59 − 5 520,00 = **EUR 533,59 a pagar**
```

```oa-check
name: PT Categoria B designer, bruto EUR 42,000, saldo após retenções (2026)
inputs:
  gross: 42000
  withheld_base: 24000
steps:
  - ss_paid: gross * 0.70 * 0.214
  - taxable: gross * 0.75 - max(0, ss_paid - gross * 0.10)
  - tax: round(29397 * 0.20579 + (taxable - 29397) * 0.349, 2)
  - balance: tax - withheld_base * 0.23
expected:
  taxable: 29408.40
  tax: 6053.59
  balance: 533.59
```

### Exemplo 5 — Cliente sob RNH / IFICI

**Cliente alegando RNH ou IFICI:** STOP nesta skill.

Aplicar a recusa **R-PT-2** e remeter o trabalho para a skill `pt-nhr-ifici`, que trata em detalhe:
- Taxa fixa de 20% sobre AEVA (Atividades de Elevado Valor Acrescentado)
- Isenções de rendimentos de fonte estrangeira
- Processo de candidatura à AT
- Lista de profissões qualificadas

Não aplicar taxas progressivas nem 20% flat **sem confirmação documental** do estatuto. A presente skill assume regime geral.

### Exemplo 6 — ActivoBank / Moey (Coimbra, Tradutora)

**Cliente:** Rita Alves, tradutora (código 1334 — tabela art. 151.º), Coimbra, primeiro ano como trabalhadora independente.

Considerações para o primeiro ano:
- Coeficientes das alíneas b), c) e f) reduzidos em 50 % no período de início de atividade e em 25 % no seguinte, se não auferir rendimentos das categorias A ou H (art. 31.º n.º 10)
- Regime simplificado aplica-se (novo contribuinte, rendimento estimado < EUR 200 000)
- Dispensa de retenção (art. 101.º-B): só se **previr auferir** menos de EUR 15 000 anuais (limiar do art. 53.º n.º 1 CIVA, igual em 2026). Com EUR 22 000 estimados, **não** há dispensa — os clientes empresariais retêm 23%.
- IRS Jovem: se a Rita tiver até 35 anos, ano 1 → isenção 100% (limite 55 × IAS = EUR 29 542,15 em 2026)
- SS: isenção nos primeiros 12 meses de atividade (primeira inscrição) — confirmar data de registo

```
Receitas brutas (ano completo): EUR 22 000
Coeficiente (tradutora — código 1334, tabela 151.º): 0,75, reduzido em 50% no ano de início
  (art. 31.º n.º 10; a Rita não tem rendimentos A ou H) → 0,375
Base tributável: 22 000 × 0,375 = EUR 8 250
Dedução SS: EUR 0 pagos no ano 1 (isenção) → sem dedução
Rendimento tributável: EUR 8 250

IRS Jovem ano 1 (100% isento; 8 250 ≤ 29 542,15): isenção total
**IRS: EUR 0** (retenções de 23% eventualmente sofridas são reembolsadas na liquidação)
```

Nota: o rendimento isento é declarado na Modelo 3 (a opção IRS Jovem exerce-se na declaração).

## Secção 5 — Regras de Tier 1 (Aplicar Diretamente)

- **T1-PT-1 — Regime simplificado: coeficiente, não despesas reais** — Em regime simplificado, rendimento tributável = receitas brutas × coeficiente. Despesas individuais NÃO são dedutíveis (estão implicitamente cobertas pelo coeficiente), mas nas alíneas b) e c) acresce ao rendimento tributável a diferença positiva entre 15 % dos rendimentos brutos e as despesas e encargos comunicados (art. 31.º n.º 13). Apenas as contribuições para a SS pagas são deduzidas separadamente da base tributável. Aplicar mecanicamente — não somar despesas em regime simplificado. — e o coeficiente das profissões da tabela do art. 151.º é 0,75 (art. 31.º n.º 1 b)); 0,35 apenas para serviços fora da tabela.  _([art. 31.º n.º 1 b) CIRS](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs31.aspx))_
- **T1-PT-2 — Retenção na fonte é um adiantamento, não uma redução de rendimento** — A retenção pelos clientes (23% para profissões da tabela 151.º; 16,5% propriedade intelectual; 11,5% outros B) é um adiantamento creditado contra a coleta final. Não reduz as receitas brutas. Recompor sempre: bruto = líquido ÷ (1 − taxa efetiva) — ÷ 0,77 no caso típico de 23%. Confirmar a taxa em cada recibo (transição 25% → 23% em 2025).
- **T1-PT-3 — Contribuições SS: dedução limitada em regime simplificado** — Contabilidade organizada: dedutíveis integralmente como gasto. Regime simplificado (alíneas b) e c) do art. 31.º n.º 1): dedutíveis apenas na parte em que excedam 10% dos rendimentos brutos e quando não deduzidas a outro título (art. 31.º n.º 2). Nunca deduzir a totalidade por defeito.  _(art. 31.º n.º 2 CIRS)_
- **T1-PT-4 — IRS Jovem: confirmar número do ano antes de aplicar** — Nunca presumir. Contribuinte até 35 anos, primeiros 10 anos de obtenção de rendimentos; escala 100% (ano 1), 75% (anos 2–4), 50% (anos 5–7), 25% (anos 8–10); limite anual 55 × IAS; rendimento isento englobado para efeitos de taxa. Pedir sempre confirmação.
- **T1-PT-5 — Contabilidade organizada obrigatória a partir de EUR 200 000** — Receitas brutas acima de EUR 200 000 obrigam à contabilidade organizada a partir do período seguinte apenas quando o limite seja ultrapassado em dois períodos de tributação consecutivos ou, num único exercício, em montante superior a 25 % (art. 28.º n.º 6). Aplicar regime simplificado apenas quando confirmado bruto ≤ EUR 200 000 no ano anterior (ou ano corrente para novos contribuintes).  _(https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs28.aspx)_
- **T1-PT-6 — Pagamentos de IRS e IVA não são despesas de IRS** — Pagamentos à AT (pagamento por conta, saldo de IRS) e entregas de IVA são pagamentos de imposto, não despesas de Categoria B. Excluir todos os descritivos de pagamentos à AT do cálculo do rendimento.
- **T1-PT-7 — RNH / IFICI: encaminhar para skill dedicada** — Se houver qualquer indício de estatuto RNH ou IFICI (datas de registo, ano de início, indicação do cliente), parar e remeter para a skill `pt-nhr-ifici`. Não tentar aplicar a taxa de 20% AEVA, nem isenções de rendimento estrangeiro, nesta skill.
- **T1-PT-8 — Verificar o código de atividade antes do coeficiente** — O coeficiente depende do enquadramento do art. 151.º, não da descrição informal da atividade. Pedir o comprovativo de atividade da AT; na dúvida aplicar 0,75 e sinalizar (default conservador).  _(art. 151.º CIRS)_

## Secção 6 — Catálogo Tier 2

**Catálogo Tier 2**

| Código | Situação | Motivo de Escalonamento | Tratamento Sugerido |
| --- | --- | --- | --- |
| T2-PT-1 | Regime RNH / IFICI | Isenções de rendimento estrangeiro e taxa de 20% — complexidade | Remeter para skill `pt-nhr-ifici` |
| T2-PT-2 | Múltiplas categorias (A + B, ou B + F) | Regras de englobamento vs. tributação autónoma para certas categorias | Sinalizar — contribuinte pode optar pelo englobamento ou não |
| T2-PT-3 | Casais — tributação conjunta | Tributação conjunta vs. separada produz resultados distintos (quociente conjugal) | Apresentar ambas as opções; não escolher por defeito |
| T2-PT-4 | Falso recibo verde (cliente único > 80%) | A AT pode requalificar como Categoria A; tratamento diferente | Sinalizar para revisão jurídica; não requalificar unilateralmente |
| T2-PT-5 | Deduções à coleta para saúde, educação, habitação (Anexo H) | Deduções pessoais fora da Categoria B — sujeitas a matching com e-fatura | Confirmar que as faturas na e-fatura estão atribuídas ao NIF; sinalizar deduções não reclamadas |
| T2-PT-6 | Residência parcial ou não residente | Taxas e regras de convenções diferentes para não residentes | Sinalizar — não aplicar taxas de residente a não residentes |

## Secção 7 — Modelo 3 e Anexos: Mapeamento

[Tabela de anexos inalterada.]

**Prazo de entrega (art. 60.º n.º 1 CIRS):** de 1 de abril a 30 de junho do ano seguinte, independentemente de o dia 30 de junho ser útil ou não útil (ex.: IRS 2026 a entregar de 1 de abril a 30 de junho de 2027). Não usar "último dia útil de junho".

## Secção 8 — Folha de Trabalho (Excel)

```
PAPEL DE TRABALHO IRS PORTUGAL (CATEGORIA B — REGIME SIMPLIFICADO)
Contribuinte: _______________  NIF: _______________  Ano: 2026

SECÇÃO A — RECEITAS BRUTAS (Categoria B)
                                        EUR
Total faturado (recibos verdes bruto)   ___________
Recomposição de montantes retidos (÷ 0,77 a 23%) ___________
Plataformas online (recompostas)        ___________
Outras receitas Categoria B             ___________
TOTAL RECEITAS BRUTAS                   ___________

SECÇÃO B — COEFICIENTE REGIME SIMPLIFICADO
Código de atividade (tabela 151.º?):    _______________
Coeficiente aplicado (0,75 / 0,35 / 0,15 / 0,95): ___________
Base tributável (bruto × coeficiente)   ___________
Dedução SS = max(0; SS paga − 10% × receitas brutas)  (___________)
RENDIMENTO TRIBUTÁVEL IRS               ___________

SECÇÃO C — CÁLCULO DO IRS (TABELA 2026, LEI 73-A/2025)
Imposto pelos escalões                  ___________
Isenção IRS Jovem (englobar isento p/ taxa; limite 55 × IAS) (___________)
IRS antes de créditos                   ___________
Menos: retenções na fonte (taxa efetiva por recibo) (___________)
Menos: pagamentos por conta IRS (20 jul/set/dez)    (___________)
SALDO IRS A PAGAR / (REEMBOLSAR)        ___________

SECÇÃO D — ADICIONAL DE SOLIDARIEDADE (art. 68.º-A)
(Apenas se rendimento coletável > EUR 80 000) ___________

SECÇÃO E — SEGURANÇA SOCIAL
Base mensal: 70% × bruto trimestral ÷ 3 (teto 12 × IAS = 6 445,56 em 2026) ___________
SS anual devida: base mensal × 21,4% × 12  ___________
Menos: SS já paga                          (___________)
Saldo SS a pagar                           ___________

SECÇÃO F — ALERTAS DO REVISOR
[ ] Regime simplificado confirmado (bruto ≤ EUR 200 000 ano anterior)?
[ ] Código de atividade confirmado (tabela 151.º → 0,75)?
[ ] Taxa de retenção efetiva confirmada em cada recibo (23% vs 25%)?
[ ] Dedução SS limitada ao excesso sobre 10% do bruto?
[ ] Pagamentos SS conferidos contra recibos (e teto 12 × IAS)
[ ] IRS Jovem — número do ano confirmado? Isento englobado para taxa?
[ ] Estatuto RNH/IFICI verificado (se aplicável, ver skill pt-nhr-ifici)?
[ ] Risco de falso recibo verde avaliado (cliente único > 80%)?
[ ] Deduções pessoais e-fatura verificadas (Anexo H)?
```

## Secção 9 — Guia de Leitura de Extratos Bancários

[Inalterada.]

## Secção 10 — Onboarding e Recolha de Informação em Falta

> "Para calcular o IRS com rigor, preciso das declarações de retenção na fonte de cada cliente, com a taxa efetivamente aplicada (em regra 23% para profissões da tabela do art. 151.º desde 2025; alguns clientes podem ter aplicado 25% na transição). Pode pedi-las aos clientes em janeiro/fevereiro — as empresas têm obrigação legal de emiti-las. Em alternativa, consulte o Portal das Finanças → 'Consultar' → 'Retenções na Fonte'."

**Tipo de serviço ambíguo:**
> "Para aplicar o coeficiente correto do regime simplificado, preciso do seu código de atividade na AT. Se a atividade consta da tabela do artigo 151.º do CIRS (consultores, programadores, tradutores, designers, arquitetos, engenheiros, etc., incluindo o código residual 1519), o coeficiente é 0,75. Vendas de mercadorias e hotelaria/restauração: 0,15. Outras prestações de serviços fora da tabela: 0,35. Confirme o código que consta do seu comprovativo de início de atividade."

**IRS Jovem:**
> "Com base na sua idade, poderá ter direito ao IRS Jovem. Este isenta 100% no 1.º ano, 75% nos anos 2–4, 50% nos anos 5–7 e 25% nos anos 8–10 de obtenção de rendimentos, com o limite anual de 55 × IAS (EUR 29 542,15 em 2026). Para o aplicar, preciso de confirmar: (1) que tem 35 anos ou menos, e (2) o número do ano da sua carreira de obtenção de rendimentos em Portugal."

**RNH / IFICI:**
> "Se está abrangido pelo regime de Residente Não Habitual (RNH) ou pelo IFICI, o tratamento de IRS é diferente — taxa fixa de 20% sobre Atividades de Elevado Valor Acrescentado, com possíveis isenções de rendimentos de fonte estrangeira. Confirma o seu estatuto e, em caso afirmativo, o trabalho será encaminhado para a skill especializada (`pt-nhr-ifici`)?"

**Contribuições SS desconhecidas:**
> "As contribuições para a Segurança Social podem reduzir o IRS, mas em regime simplificado só a parte que exceda 10% das suas receitas brutas é dedutível. Tem os recibos de pagamento à SS? Caso não, posso estimar: base contributiva = 70% das receitas brutas trimestrais ÷ 3 (com teto mensal de 12 × IAS), à taxa de 21,4%."

## Secção 11 — Remissão para RNH / IFICI

[Inalterada.]

## Secção 12 — Referências

### Legislação-Chave

- **Legislação-Chave** — - **CIRS (Código do IRS)** — Decreto-Lei n.º 442-A/88, de 30 de novembro, com as alterações em vigor; art. 28.º (Categoria B), art. 31.º (coeficientes; n.º 2 dedução SS), art. 60.º (prazo de entrega), art. 68.º (taxas), art. 68.º-A (adicional de solidariedade), art. 71.º (não residentes), art. 101.º/101.º-B (retenção e dispensa), art. 102.º (pagamentos por conta), art. 12.º-B (IRS Jovem) - **Lei n.º 73-A/2025, de 30 de dezembro (OE2026)** — tabela de taxas do art. 68.º aplicável aos rendimentos de 2026 - **Lei n.º 55-A/2025, de 22 de julho** — tabela de taxas do art. 68.º aplicável aos rendimentos de 2025 - **Lei n.º 45-A/2024, de 31 de dezembro (OE2025)** — IRS Jovem atual (art. 12.º-B) e retenção 23% (art. 101.º n.º 1 b)) - **Portaria n.º 1011/2001, de 21 de agosto** — tabela de atividades do art. 151.º do CIRS (determina coeficiente 0,75 e retenção 23%). *Nota: não confundir com a lista de atividades de elevado valor acrescentado do RNH/IFICI (Portaria n.º 230/2019 e sucessoras) — instrumento distinto, ver skill `pt-nhr-ifici`.* - **Portaria n.º 480-A/2025/1** — IAS 2026 = EUR 537,13 - **Portaria n.º 6-B/2025/1** — IAS 2025 = EUR 522,50 - **EBF art. 58.º** — propriedade intelectual: englobamento de 50%, exclusão máxima EUR 10 000 (vigente até 2026) - **Decreto Regulamentar n.º 25/2009** — depreciações e amortizações (contabilidade organizada)  _(CIRS; Lei n.º 73-A/2025; Lei n.º 55-A/2025; Lei n.º 45-A/2024; Portaria n.º 1011/2001; Portaria n.º 6-B/2025/1; EBF art. 58.º; Decreto Regulamentar n.º 25/2009)_

### Prazos (rendimentos de 2026)

**Prazos (rendimentos de 2026)**  _(art. 60.º n.º 1 CIRS; art. 102.º n.º 1 e 3 CIRS)_

| Prazo | Evento |
| --- | --- |
| 1 abr – 30 jun 2026 | Entrega da Modelo 3 de IRS 2025 (prazo fixo — art. 60.º n.º 1) |
| até 20 de julho de 2026 | Pagamento por conta 2026 — 1.ª prestação (art. 102.º n.º 1) |
| até 20 de setembro de 2026 | Pagamento por conta 2026 — 2.ª prestação |
| até 20 de dezembro de 2026 | Pagamento por conta 2026 — 3.ª prestação (não exigível se < EUR 50 — art. 102.º n.º 3) |
| 1 abr – 30 jun 2027 | Entrega da Modelo 3 de IRS 2026 (prazo fixo) |

### Referências Úteis

[Inalterada.]

## Sources

| Source | URL | Read on |
|---|---|---|
| CIRS art. 68, IRS bands 2026 (wording of Lei 73-A/2025) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs68.aspx | 2026-10-23 |
| CIRS art. 31, simplified regime coefficients, 10% SS rule, 15% rule, crypto | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs31.aspx | 2026-10-23 |
| CIRS art. 28, EUR 200,000 threshold and exit from the simplified regime | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs28.aspx | 2026-10-23 |
| CIRS art. 12-B, IRS Jovem (55 x IAS cap) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs12b.aspx | 2026-10-23 |
| CIRS art. 101, withholding rates (23%, 16.5%, 11.5%) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs101.aspx | 2026-10-23 |
| CIRS art. 101-B, withholding waiver | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs101b.aspx | 2026-10-23 |
| CIRS art. 102, payments on account | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs102.aspx | 2026-10-23 |
| CIVA art. 53(1), EUR 15,000 threshold | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/artigo-53-o-do-civa.aspx | 2026-10-23 |
| Portaria 480-A/2025/1, IAS 2026 = EUR 537.13 | https://diariodarepublica.pt/dr/detalhe/portaria/480-a-2025-993056222 | 2026-10-23 |
| Segurança Social, Guia Prático, Novo Regime dos Trabalhadores Independentes (21.4%, 25.2%, 70%/20%, ceiling EUR 6,445.56) | https://www.seg-social.pt/ptss/pssd/documento/cmc1xyfxz00dekl2ynxz676sw | 2026-10-23 |

Not yet confirmed: the EBF art. 58 intellectual property rule (50% up to EUR 10,000) was not re-read for 2026; the accountant review of 2026-06-04 covered the 2025 figures, not the 2026 ones; the Social Security guide's own worked example prints the ceiling as EUR 6,445.66, while 12 x EUR 537.13 = EUR 6,445.56, which its text also states.

## Disclaimer

Esta skill e os seus outputs são fornecidos exclusivamente para fins informativos e de cálculo e não constituem aconselhamento fiscal, jurídico ou financeiro. A Open Accountants e os seus contribuidores não aceitam qualquer responsabilidade por erros, omissões ou consequências decorrentes da utilização desta skill. Todos os outputs devem ser revistos e validados por um profissional qualificado (Contabilista Certificado, advogado fiscalista ou equivalente licenciado na jurisdição aplicável) antes de qualquer entrega ou actuação.

A versão mais actualizada e verificada desta skill é mantida em [openaccountants.com](https://openaccountants.com). Faça login para aceder à versão mais recente, solicitar revisão profissional por um contabilista licenciado e acompanhar actualizações à medida que a lei fiscal evolui.

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
