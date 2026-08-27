---
name: pt-corporate-tax
description: "LER SEMPRE este skill antes de tratar fiscalidade de pessoas coletivas em Portugal. Utilizar sempre que seja pedida assistência com Imposto sobre o Rendimento das Pessoas Coletivas (IRC) para sociedades residentes em Portugal. Ativar com expressões como \"IRC Portugal\", \"Modelo 22\", \"derrama estadual\", \"derrama municipal\", \"tributação autónoma\", \"Imposto sobre o Rendimento das Pessoas Coletivas\", \"SIFIDE II\", \"RFAI\", \"Pilar Dois Portugal\", \"Madeira IBC\", \"SGPS\", \"prejuízos fiscais 12 anos\", \"pagamentos por conta\", \"pagamento especial por conta\", \"PEC\", \"CIRC\", \"AT Autoridade Tributária\", \"IES\", \"preços de transferência Portugal\", \"CFC Portugal\", \"participation exemption Portugal\". Ativar também em inglês: \"Portugal corporate tax\", \"Portugal IRC\", \"Portugal Modelo 22\", \"Portugal Pillar Two top-up\", \"Madeira IBC 5%\", \"Portugal R&D credit\", \"Portugal SGPS participation exemption\". Cobre a taxa nominal de 21% nos termos do art.º 87.º CIRC, a taxa reduzida de 17% para PMEs sobre os primeiros €50.000 de matéria coletável, o regime do Centro Internacional de Negócios da Madeira (CINM/IBC) a 5% até 31 dez 2027, a Derrama Estadual progressiva (1,5%/3%/5%/9%) nos termos do art.º 87.º-A, a Derrama Municipal (0-1,5%), a Tributação Autónoma do art.º 88.º (viaturas, despesas de representação, ajudas de custo, paraísos fiscais), o Modelo 22 e respetivos Anexos (A regime geral, B simplificado, C grupos, D incentivos, E preços de transferência), os Pagamentos por Conta do art.º 105.º CIRC (3 prestações: julho, setembro, dezembro) a 80% da coleta do ano anterior, o Pagamento Especial por Conta (PEC) eliminado para PMEs em 2018 mas mantido para grandes empresas, o reporte de prejuízos fiscais a 12 anos com limitação a 65% da matéria coletável (art.º 52.º CIRC), o crédito SIFIDE II (32,5% + 50% incremental, aprovação ANI), o RFAI (25% / 10% por região), o regime SGPS (participation exemption art.º 51.º e 51.º-C), o Pilar Dois (Lei 27/2024 transpondo a Diretiva UE 2022/2523, MNE > €750M), os preços de transferência (art.º 63.º CIRC, Master/Local File por Portaria 268/2021, CbCR), as CFC do art.º 66.º, as retenções na fonte e o cumprimento do IES até 15 julho. Fora de âmbito: regime simplificado de tributação para microentidades (separado), entidades sem fins lucrativos / IPSS, sector financeiro e segurador (regimes especiais), exploração de petróleo e gás, organismos de investimento coletivo (regime especial), fundos de capital de risco, instituições religiosas. Para IVA ver portugal-vat-return; para IRS dos sócios ver pt-income-tax; para contabilidade e SAF-T ver portugal-bookkeeping."
jurisdiction: PT
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# PT Corporate Tax

## Portugal — IRC (Imposto sobre o Rendimento das Pessoas Coletivas) — Skill v1.0

> **Produzido pela OpenAccountants (openaccountants.com)**
>
> Este skill destina-se exclusivamente a fins informativos e não constitui aconselhamento fiscal, jurídico ou financeiro. Todos os outputs devem ser revistos e validados por um Contabilista Certificado inscrito na Ordem dos Contabilistas Certificados (OCC) ou por um Revisor Oficial de Contas (ROC) inscrito na OROC antes de qualquer submissão à Autoridade Tributária e Aduaneira (AT). A versão verificada mais recente é mantida em [openaccountants.com](https://openaccountants.com).

## Secção 1 — Referência rápida

**Referência rápida**

| Campo | Valor |
| --- | --- |
| País | Portugal (República Portuguesa) |
| Imposto | Imposto sobre o Rendimento das Pessoas Coletivas (IRC) |
| Moeda | EUR (Euros, €) |
| Período de tributação | Em regra, coincide com o ano civil (1 jan – 31 dez); art.º 8.º CIRC permite período diferente mediante comunicação à AT |
| Legislação primária | **Código do IRC (CIRC)** aprovado pelo DL 442-B/88, de 30 de novembro, e alterações subsequentes; **Lei do Orçamento do Estado para 2025** (Lei 45-A/2024) |
| Legislação complementar | Estatuto dos Benefícios Fiscais (EBF); Código Fiscal do Investimento (CFI, DL 162/2014); Lei 27/2024 (Pilar Dois); Portaria 268/2021 (preços de transferência); Portaria 220/2008 (Modelo 22) |
| **Taxa IRC standard** | **21%** sobre a matéria coletável (art.º 87.º n.º 1 CIRC) |
| **Taxa reduzida PMEs** | **17%** sobre os primeiros **€50.000** de matéria coletável; 21% sobre o remanescente (art.º 87.º n.º 2 CIRC, redação OE 2025) |
| **Madeira IBC (CINM)** | **5%** para entidades licenciadas no Centro Internacional de Negócios da Madeira até **31 dez 2027** (DL 165/86, alterado; aprovação UE Decisão SA.21259) |
| **Derrama Estadual** | Escalões progressivos sobre lucro tributável: 1,5% (€1,5M – €7,5M), 3% (€7,5M – €35M), 5% (€35M – €200M), 9% (> €200M) — art.º 87.º-A CIRC |
| **Derrama Municipal** | 0% a **1,5%** sobre lucro tributável, fixada por cada município (Lei 73/2013 – Lei das Finanças Locais). Lisboa e Porto: 1,5%; vários municípios do interior: 0% |
| **Tributação Autónoma (TA)** | Art.º 88.º CIRC — taxas variáveis sobre viaturas, despesas representação, ajudas de custo, paraísos fiscais; **+10 p.p. se exercício de prejuízo fiscal** |
| Declaração anual | **Modelo 22** + Anexos — submissão eletrónica via Portal das Finanças |
| Prazo Modelo 22 | Até ao **último dia útil de maio** do ano seguinte (TY 2024: 31 maio 2025; TY 2025: 31 maio 2026 — confirmar dia útil) |
| **IES** (Informação Empresarial Simplificada) | Até **15 julho** do ano seguinte |
| **Pagamentos por Conta (PPC)** | 3 prestações: **julho, setembro, dezembro** — total = 80% da coleta IRC do ano anterior (75% se VN ≤ €500.000) — art.º 105.º CIRC |
| **Pagamento Especial por Conta (PEC)** | Eliminado para PMEs (OE 2018); mantém-se para grandes empresas — art.º 106.º CIRC |
| Prejuízos fiscais | Reporte por **12 períodos de tributação**; limitação de dedução a **65% da matéria coletável** (art.º 52.º CIRC) |
| **SIFIDE II** | Crédito de **32,5%** das despesas de I&D + **50%** sobre parte incremental (acima da média dos 2 anos anteriores); reporte 8 anos; aprovação ANI |
| **RFAI** | Crédito de **25%** sobre investimento elegível até €15M; **10%** acima; condicionado à região (Norte/Centro/Alentejo/Madeira/Açores; menor em Algarve/Lisboa) |
| **Pilar Dois** | Lei 27/2024 transpõe Diretiva UE 2022/2523; aplica-se a MNEs com EBM > €750M; taxa efetiva mínima 15% (IIR + UTPR + QDMTT) |
| Retenções na fonte | Dividendos 28% (residentes) / 25% (não residentes); juros 28%/25%; royalties 25% — reduções por CDT |
| Portal | **Portal das Finanças** (portaldasfinancas.gov.pt) |
| Autoridade fiscal | **Autoridade Tributária e Aduaneira (AT)** |
| Conservação de documentos | 10 anos (art.º 123.º CIRC) |
| Validado por | Pendente — sign-off por Contabilista Certificado (OCC) ou ROC (OROC) |
| Versão do skill | 1.0 |

### 1.1 Defaults conservadores

**Defaults conservadores**

| Ambiguidade | Default |
| --- | --- |
| Estatuto PME desconhecido | Aplicar 21% (não PME) até confirmação dos critérios da Recomendação UE 2003/361/CE |
| Município desconhecido | Aplicar **1,5%** de derrama municipal (taxa máxima) até confirmação |
| Madeira IBC sem licença confirmada | Aplicar 21% standard; flag para verificação da licença CINM |
| Tributação autónoma — viatura sem valor de aquisição claro | Assumir escalão mais alto (35%) |
| Exercício de prejuízo fiscal | Adicionar **+10 p.p.** a todas as TA (art.º 88.º n.º 14) |
| SIFIDE — incremental vs base | Confirmar média dos 2 anos anteriores; se incerto, aplicar só 32,5% (sem componente incremental) |
| RFAI — região elegível | Confirmar NUTS II; se cliente em Lisboa/Algarve aplicar taxa reduzida ou recusar |
| Reporte prejuízos pré-2014 | Aplicar regras transitórias específicas; sinalizar para revisor |
| SGPS — participation exemption | Confirmar participação ≥10% e ≥1 ano detenção antes de aplicar isenção |
| Pilar Dois aplicabilidade | Confirmar EBM > €750M em 2 dos 4 anos anteriores; se incerto, sinalizar |
| Preços de transferência — limiar | Se VN ≥ €3M ou operações com partes relacionadas, exigir Master/Local File |

## Secção 2 — Entradas obrigatórias e catálogo de recusas

### 2.1 Entradas obrigatórias

- **Mínimo viável** — Demonstrações financeiras anuais aprovadas (balanço, demonstração de resultados); IES do exercício anterior; Modelo 22 do ano anterior; SAF-T (PT) Contabilidade; confirmação de (i) estatuto PME, (ii) município da sede, (iii) eventual licenciamento Madeira IBC, (iv) eventual qualificação como SGPS, (v) opção pelo Regime Especial de Tributação dos Grupos de Sociedades (RETGS), se aplicável.
- **Recomendado** — Razão geral e balancetes; mapa de amortizações e depreciações; mapa de provisões e imparidades; mapa de reporte de prejuízos fiscais por ano de origem; comprovativos de retenção na fonte sofrida; recibos dos pagamentos por conta efetuados; quadro de partes relacionadas e respetivos saldos/transações; mapa de viaturas (matrícula, data de aquisição, valor, utilizador).
- **Ideal** — Demonstrações financeiras com Certificação Legal de Contas (CLC) emitida por ROC; dossier de preços de transferência completo (Master File + Local File por Portaria 268/2021); certificado SIFIDE II emitido pela ANI; declaração RFAI com identificação dos investimentos elegíveis; mapa Pilar Dois GloBE Information Return (se aplicável); atas que documentem opções fiscais (RETGS, regime especial, etc.).
- **HARD STOP** — HARD STOP se faltar o mínimo. Sem DFs aprovadas e Modelo 22 do ano anterior não pode ser produzida computação de IRC.

### 2.2 Catálogo de recusas

- **R-PT-IRC-1** — Setores financeiro e segurador. Bancos, sociedades financeiras, instituições de pagamento, seguradoras e resseguradoras seguem regimes específicos (Decreto Regulamentar 25/2009 + regras de Banco de Portugal / ASF; contribuição extraordinária sobre o setor bancário). Fora de âmbito — escalar para fiscalista especializado.  _(Decreto Regulamentar 25/2009)_
- **R-PT-IRC-2** — Petróleo, gás e indústrias extrativas. Regime especial; tributação adicional sectorial. Fora de âmbito.
- **R-PT-IRC-3** — Organismos de investimento coletivo (OIC) e fundos. Fundos de investimento mobiliário e imobiliário, FCR, FIA, FIIAH têm regime fiscal próprio (DL 7/2015 e EBF). Fora de âmbito.  _(DL 7/2015; EBF)_
- **R-PT-IRC-4** — Entidades sem fins lucrativos / IPSS / sector cooperativo. IPSS, associações, fundações, cooperativas (com algumas exceções) — regime do art.º 9.º e 10.º CIRC, EBF, e Estatuto da Cooperação. Fora de âmbito.  _(art.º 9.º e 10.º CIRC)_
- **R-PT-IRC-5** — Não residentes sem estabelecimento estável. Tributação cedular (taxas liberatórias ou retenções definitivas). Para estabelecimentos estáveis (EE) de não residentes, aplicam-se regras de imputação dos arts. 4.º-3, 50.º e 55.º CIRC — escalar a fiscalista.  _(arts. 4.º-3, 50.º e 55.º CIRC)_
- **R-PT-IRC-6** — RETGS (Regime Especial de Tributação dos Grupos de Sociedades). Art.º 69.º a 71.º CIRC. A opção exige sociedade dominante com participação ≥75%, residência fiscal em Portugal e cumprimento de requisitos formais. Recusa por defeito — apenas Tier 2 com sign-off do revisor; computações em base consolidada não são produzidas neste skill.  _(art.º 69.º a 71.º CIRC)_
- **R-PT-IRC-7** — Procedimentos de inspeção, contraordenacionais ou contenciosos pendentes. Se a sociedade estiver em inspeção tributária ativa (Lei Geral Tributária art.º 63.º), processo de execução fiscal, impugnação judicial, reclamação graciosa ou MAP — escalar. Não produzir números que prejudiquem a posição em litígio.  _(Lei Geral Tributária art.º 63.º)_
- **R-PT-IRC-8** — Reorganizações empresariais (fusões, cisões, entradas de ativos, permutas). Regime de neutralidade fiscal dos arts. 73.º a 78.º CIRC requer análise específica. Fora de âmbito.  _(arts. 73.º a 78.º CIRC)_
- **R-PT-IRC-9** — Operações com paraísos fiscais (Portaria 150/2004 e Portaria 309-A/2020). Pagamentos a entidades em jurisdições da lista nacional de regimes fiscais claramente mais favoráveis exigem inversão do ónus da prova (art.º 23.º-A n.º 1 r CIRC) e tributação autónoma agravada (35%/55%). Tier 2; reviewer sign-off obrigatório.  _(Portaria 150/2004; Portaria 309-A/2020; art.º 23.º-A n.º 1 r CIRC)_
- **R-PT-IRC-10** — Âmbito cross-skill. IVA → `portugal-vat-return`; IRS dos sócios → `pt-income-tax`; Segurança Social → `pt-social-contributions`; contabilidade e SAF-T → `portugal-bookkeeping`; demonstrações financeiras e relatório de gestão → `portugal-financial-statements`; constituição de sociedade → `portugal-formation`.

## Secção 3 — Tier 1 — Taxa nominal IRC, regime PMEs e Madeira IBC

### 3.1 Taxa nominal — 21%

- **Taxa de IRC geral** — 21% (taxa geral)
- **Fórmula IRC standard** — IRC = 21% × Matéria Coletável  _(art.º 87.º n.º 1 CIRC)_

### 3.2 Taxa reduzida para PMEs — 17%

- **Taxa reduzida PMEs** — 17% percent (sobre os primeiros €50.000 de matéria coletável; excedente a 21%)  _(art.º 87.º n.º 2 CIRC (redação dada pela Lei do OE 2025))_
- **Fórmula PME** — Se matéria coletável ≤ €50.000: IRC = 17% × MC Se matéria coletável > €50.000: IRC = (17% × €50.000) + (21% × (MC − €50.000)) = €8.500 + 21% × (MC − €50.000)  _(art.º 87.º n.º 2 CIRC)_

O limite do escalão PME foi aumentado para €50.000 (vs €25.000 em anos anteriores). Verificar o texto da LOE 2025 publicada antes de aplicar.

**Definição de PME (Recomendação UE 2003/361/CE)**  _(Recomendação UE 2003/361/CE; DL 372/2007)_

| Categoria | Trabalhadores | E (VN anual ≤) OU (Balanço total ≤) |
| --- | --- | --- |
| Micro | < 10 | €2M / €2M |
| Pequena | < 50 | €10M / €10M |
| Média | < 250 | €50M / €43M |

- **Base de apreciação de limites** — Os limites são apreciados em base consolidada quando há empresas associadas ou parceiras.  _(art.º 3.º do anexo ao DL 372/2007)_

### 3.3 Madeira IBC (Centro Internacional de Negócios da Madeira) — 5%

- **Taxa Madeira IBC** — 5% percent (sobre rendimentos de atividades licenciadas pelo CINM, até 31 dezembro 2027)  _(DL 165/86, de 26 de junho; Decisão da Comissão Europeia SA.21259)_

**Requisitos Madeira IBC**  _(DL 165/86)_

| Requisito | Conteúdo |
| --- | --- |
| Licenciamento | Licença CINM emitida pela SDM (Sociedade de Desenvolvimento da Madeira) |
| Criação de postos de trabalho | Mínimo de 1 posto de trabalho nos primeiros 6 meses, com limite máximo de matéria coletável beneficiada conforme tabela (1 trabalhador → MC máxima beneficiada €2,73M; escalões crescentes até > 100 trabalhadores) |
| Investimento mínimo | Alternativa ao requisito de postos: €75.000 em ativos fixos tangíveis ou intangíveis nos primeiros 2 anos |
| Atividades elegíveis | Serviços internacionais conforme lista CINM (excluindo certas atividades financeiras e de consultoria não internacionais) |
| Plafonds | Tetos sobre matéria coletável beneficiada por nível de emprego |

- **Tributação acima dos plafonds** — Acima dos plafonds aplicáveis, a matéria coletável é tributada à taxa standard (Açores: 14,7%; Madeira fora do CINM: 14,7% para PMEs e 18,9% para outras — verificar Decreto Legislativo Regional aplicável).
- **Default conservador Madeira IBC** — Aplicar 21% standard até validação da licença CINM válida para o exercício e cumprimento dos requisitos de emprego/investimento.

### 3.4 Regiões Autónomas — taxas regionais

**Regiões Autónomas — taxas regionais**

| Região | Taxa standard | Taxa PMEs (primeiros €50.000) |
| --- | --- | --- |
| Continente | 21% | 17% |
| **Açores** (DLR específico) | 14,7% | 11,9% (verificar valor exato em DLR vigente) |
| **Madeira** (fora CINM) | 14,7% | 11,9% (verificar valor exato em DLR vigente) |
| **Madeira CINM/IBC** | 5% (até 31 dez 2027, com plafonds) | — |

(Reviewer: confirmar percentagens regionais contra o Decreto Legislativo Regional em vigor para 2025 — as RA podem adotar reduções dentro das margens permitidas pela Lei das Finanças Regionais.)

## Secção 4 — Derrama Estadual + Derrama Municipal

### 4.1 Derrama Estadual — art.º 87.º-A CIRC

- **Incidência** — A Derrama Estadual incide sobre a parte do lucro tributável (não da matéria coletável) superior a €1.500.000, em escalões progressivos.  _(art.º 87.º-A CIRC)_

**Derrama Estadual — escalões**  _(art.º 87.º-A CIRC)_

| Lucro tributável | Taxa |
| --- | --- |
| Até €1.500.000 | 0% |
| €1.500.000 — €7.500.000 | **1,5%** |
| €7.500.000 — €35.000.000 | **3%** |
| €35.000.000 — €200.000.000 | **5%** |
| Acima de €200.000.000 | **9%** |

- **Fórmula Derrama Estadual** — Derrama Estadual = Σ (taxa do escalão × lucro tributável dentro do escalão)  _(art.º 87.º-A CIRC)_
- **Acréscimo e não creditação** — A Derrama Estadual acresce ao IRC, à Derrama Municipal e à Tributação Autónoma. Não é creditável e não dá origem a reporte.  _(art.º 87.º-A CIRC)_

### 4.2 Derrama Municipal — Lei 73/2013 (Lei das Finanças Locais)

- **Fixação municipal** — Cada município pode fixar anualmente uma derrama até 1,5% sobre o lucro tributável do exercício. A taxa pode também ser zero ou diferenciada para PMEs (regime de incentivos municipais).  _(art.º 18.º da Lei 73/2013)_

**Taxas comuns para 2025 (verificar deliberação municipal específica)**  _(Lei 73/2013)_

| Município | Derrama Municipal |
| --- | --- |
| Lisboa | 1,5% |
| Porto | 1,5% |
| Cascais | 1,5% |
| Sintra | 1,5% |
| Várias do interior (ex: Mértola, Idanha-a-Nova) | 0% |
| Algumas com taxa reduzida para PMEs | 1,25% / 1,0% |

- **Fórmula Derrama Municipal** — Derrama Municipal = Taxa do município × Lucro Tributável  _(art.º 18.º da Lei 73/2013)_
- **Repartição multi-município** — Se a empresa tiver atividade em mais que um município, a derrama é repartida pela massa salarial em cada município (art.º 18.º n.º 2 da Lei 73/2013), salvo se o VN anual não exceder €50.000 (todos os rendimentos imputados ao município da sede).  _(art.º 18.º n.º 2 da Lei 73/2013)_
- **Default conservador Derrama Municipal** — Aplicar 1,5% até confirmação da deliberação municipal específica para o exercício.

## Secção 5 — Tributação Autónoma (art.º 88.º CIRC)

- **Natureza da TA** — A Tributação Autónoma (TA) é um imposto adicional sobre certas despesas, independentemente de se apurar matéria coletável positiva. Incide sobre o sujeito passivo (não sobre o beneficiário) e acresce ao IRC.  _(art.º 88.º CIRC)_
- **Agravamento por prejuízo fiscal** — Se o sujeito passivo apresentar prejuízo fiscal no exercício, as taxas de TA são agravadas em 10 p.p. (com exceção das taxas de 35%/55% sobre paraísos fiscais que já são as máximas).  _(art.º 88.º n.º 14 CIRC)_

### 5.1 Viaturas ligeiras de passageiros e mistas

**Viaturas ligeiras de passageiros e mistas**  _(art.º 88.º CIRC)_

| Custo de aquisição | Taxa TA (regra) | Taxa TA (com prejuízo) |
| --- | --- | --- |
| < €27.500 | 10% | 20% |
| €27.500 — €35.000 | 27,5% | 37,5% |
| > €35.000 | 35% | 45% |

- **Aplica-se sobre** — Depreciações, encargos com manutenção, combustíveis, seguros, rendas de locação, impostos (IUC).  _(art.º 88.º CIRC)_
- **Exclusões** — Veículos exclusivamente elétricos com custo até €62.500 (taxa 0%); híbridos plug-in com taxas reduzidas (5%/10%/17,5%); GPL/GNV (taxas reduzidas — verificar art.º 88.º n.º 18 atual).  _(art.º 88.º n.º 18 CIRC)_

### 5.2 Outras categorias

**Outras categorias de TA**  _(art.º 88.º CIRC; Portaria 150/2004)_

| Despesa | Taxa TA |
| --- | --- |
| Despesas de representação | 10% (+10 p.p. se prejuízo = 20%) |
| Ajudas de custo e km próprio (não faturados a cliente, sem mapa) | 5% (+10 p.p. = 15%) |
| Pagamentos a entidades em paraísos fiscais (Portaria 150/2004) — não documentados ou não justificados | **35%** (sujeitos passivos com contabilidade organizada) / **55%** (entidades isentas ou parcialmente isentas) |
| Encargos não documentados | 50% (+10 p.p. = 60%); 70% para entidades total ou parcialmente isentas |
| Bónus e remunerações variáveis pagas a gestores/administradores que representem mais de 25% da remuneração anual e excedam €27.500, salvo se diferidos > 3 anos com componente variável dependente de desempenho positivo | 35% |
| Lucros distribuídos a entidades isentas total ou parcialmente | 23% (sobre dividendos, em certos casos) — verificar redação atual do art.º 88.º n.º 11 |

- **Fórmula TA total** — TA Total = Σ (taxa aplicável × despesa em causa)  _(art.º 88.º CIRC)_
- **Liquidação da TA** — A TA é liquidada no Modelo 22 (campo próprio do Quadro 10) e paga com o saldo do IRC.

## Secção 6 — Modelo 22 + Anexos

### 6.1 Modelo 22 — declaração de rendimentos

- **Modelo 22** — A declaração periódica de rendimentos Modelo 22 de IRC é o instrumento de autoliquidação. Submetida obrigatoriamente por via eletrónica no Portal das Finanças.

**Quadros principais**

| Quadro | Conteúdo |
| --- | --- |
| Q01 | Identificação e tipo de declaração |
| Q03 | Resultado líquido do período (RLP) |
| Q07 | Correções para apuramento do lucro tributável (acréscimos e deduções) |
| Q09 | Apuramento da matéria coletável (deduções de benefícios fiscais; prejuízos fiscais reportáveis) |
| Q10 | Cálculo do imposto: IRC, derramas, tributação autónoma, retenções, PPC, PEC, créditos |
| Q11 | Outras informações |
| Q13 | Apuramento do PEC |

### 6.2 Anexos

**Anexos Modelo 22**

| Anexo | Quando obrigatório |
| --- | --- |
| **Anexo A** | Regime geral — Derrama Municipal repartida por município (sempre que aplicável) |
| **Anexo B** | Regime simplificado de determinação da matéria coletável (microentidades elegíveis com VN ≤ €200.000 e ativo ≤ €500.000, sem participações > 20%, etc.) |
| **Anexo C** | Regime Especial de Tributação dos Grupos de Sociedades (RETGS) — sociedade dominante |
| **Anexo D** | Benefícios fiscais (SIFIDE, RFAI, CFEI, DLRR, RFI/DLRR, etc.) |
| **Anexo E** | Regime das Operações entre Entidades Relacionadas — preços de transferência (sempre que VN ≥ €3M ou operações com partes relacionadas) |
| **Anexo F** | Entidades isentas ou parcialmente isentas |
| **Anexo G** | Atividade hoteleira e similares (informação setorial) |
| **Anexo H** | Imputação de rendimentos (CFC, art.º 66.º) |

### 6.3 IES (Informação Empresarial Simplificada)

- **IES** — Declaração anual conjunta cumprindo obrigações perante AT, IRN (Registo Comercial), Banco de Portugal e INE. Submetida no Portal das Finanças até 15 de julho do ano seguinte.

**Anexos IES relevantes para IRC**

| Anexo IES | Conteúdo |
| --- | --- |
| Anexo A | Balanço, demonstração de resultados, anexo |
| Anexo D | Operações com partes relacionadas |
| Anexo R | RETGS |
| Anexo Q | SGPS |

## Secção 7 — Pagamentos por Conta (art.º 105.º CIRC)

**Prestações de PPC**  _(art.º 105.º CIRC)_

| Prestação | Vencimento |
| --- | --- |
| 1ª | Julho (até último dia útil) |
| 2ª | Setembro (até último dia útil) |
| 3ª | 15 de dezembro |

- **Cálculo PPC** — Total PPC = 80% × Coleta IRC do ano N−1 (líquida de retenções) Se VN do ano N−1 ≤ €500.000: Total PPC = 75% × Coleta do ano N−1 PPC por prestação = Total PPC / 3 (arredondado por excesso)  _(art.º 105.º CIRC)_
- **Dispensa da 3ª prestação** — Quando o sujeito passivo verifique que o montante dos PPC já pagos é igual ou superior ao imposto que será devido com base na matéria coletável do exercício, pode deixar de efetuar a 3ª prestação. Esta dispensa deve ser comunicada e, se a estimativa for incorreta com erro superior a 20%, há juros compensatórios.  _(art.º 105.º n.º 5 e n.º 6 CIRC)_

## Secção 8 — Pagamento Especial por Conta (PEC) — art.º 106.º CIRC

- **Eliminação para PMEs** — A Lei do OE 2018 (Lei 114/2017) eliminou o PEC para sujeitos passivos que cumpram as obrigações declarativas (Modelo 22 e IES) nos prazos legais. Para PMEs em situação regularizada, o PEC deixou de ser exigido.  _(Lei 114/2017; art.º 106.º CIRC)_
- **Permanência para não dispensadas** — Mantém-se para grandes empresas e em casos de incumprimento das obrigações declarativas.  _(art.º 106.º CIRC)_
- **Cálculo PEC** — PEC = 1% do VN do exercício anterior, com mínimo €850 e máximo €70.000 + 20% sobre a parte que exceder €50.000 Pago em 2 prestações: - 1ª prestação: março - 2ª prestação: outubro Dedutível à coleta de IRC nos 6 períodos seguintes; reembolsável nos termos do art.º 93.º se não absorvido.  _(art.º 106.º CIRC; art.º 93.º CIRC)_
- **Default conservador PEC** — Confirmar se a entidade está dispensada (cumprimento declarativo em dia + ser PME). Em dúvida, calcular o PEC.

## Secção 9 — Prejuízos fiscais (art.º 52.º CIRC)

**Prejuízos fiscais — regras**  _(art.º 52.º CIRC (redação dada pela Lei 24-D/2022 e alterações posteriores))_

| Item | Regra |
| --- | --- |
| Período de reporte | **12 períodos de tributação** seguintes (regra atual; alterada de 5 → 12 em 2023) |
| Limitação anual de dedução | A dedução em cada período não pode exceder **65% da matéria coletável** apurada (art.º 52.º n.º 2) |
| Ordem de dedução | Por ordem cronológica (prejuízos mais antigos primeiro) |
| Carry-back | **Não permitido** em Portugal |
| Aquisição de controlo | Perda do direito à dedução se alteração da titularidade de mais de 50% do capital social ou da maioria dos direitos de voto, salvo autorização da AT (art.º 52.º n.º 8 e 9) |
| Período pré-2014 | Aplicam-se regras transitórias — prejuízos gerados em 2014-2016 com reporte de 12 anos; 2017-2022 com reporte de 5 anos (verificar regime de transição) |

- **Cálculo da dedução de prejuízos** — Dedução máxima do ano = min ( Prejuízos disponíveis , 65% × Matéria Coletável antes da dedução )  _(art.º 52.º CIRC)_

Exemplo: Matéria coletável antes de dedução = €100.000; prejuízos reportáveis disponíveis = €80.000.
- Limite 65% = €65.000.
- Dedução do ano = €65.000.
- Matéria coletável após dedução = €35.000.
- Prejuízos por reportar = €15.000 (continuam disponíveis nos exercícios seguintes até esgotar os 12 anos).

## Secção 10 — SIFIDE II (Sistema de Incentivos Fiscais à I&D Empresarial)

**SIFIDE II — componentes**  _(Código Fiscal do Investimento (DL 162/2014), arts. 35.º a 42.º)_

| Componente | Taxa |
| --- | --- |
| Taxa base | **32,5%** das despesas de I&D elegíveis incorridas no exercício |
| Taxa incremental | **+50%** sobre o aumento de despesas em relação à média dos **2 exercícios anteriores** (com tecto de €1.500.000 sobre a componente incremental) |

- **Reporte SIFIDE** — 8 períodos de tributação seguintes (créditos não utilizados).  _(DL 162/2014)_
- **Despesas elegíveis (não exaustivo)** — Aquisição de ativos fixos tangíveis e intangíveis afetos a I&D (exclui terrenos e edifícios fora de certas condições), despesas com pessoal afeto a I&D, despesas com participação em ensaios, despesas com auditorias externas, contratos com instituições do sistema científico, registo de patentes.  _(DL 162/2014)_
- **Procedimento** — 1. Submissão à ANI (Agência Nacional de Inovação) de candidatura/declaração com o dossier de despesas. 2. ANI emite declaração SIFIDE atestando o montante de crédito apurado. 3. Crédito deduzido à coleta de IRC no Modelo 22 (Quadro 10, campo 355) com base na declaração ANI.
- **Default conservador SIFIDE** — Não aplicar SIFIDE sem certificado ANI emitido. Se o certificado ainda não foi emitido, aplicar 0 e flag para revisor.

## Secção 11 — RFAI (Regime Fiscal de Apoio ao Investimento)

**RFAI por região**  _(Código Fiscal do Investimento (DL 162/2014), arts. 22.º a 26.º)_

| Região (NUTS II) | Taxa RFAI sobre investimento elegível |
| --- | --- |
| Norte, Centro, Alentejo, RA Madeira, RA Açores | **25%** sobre os primeiros €15.000.000 de investimento elegível; **10%** sobre o excedente |
| Algarve | **10%** (com algumas variações; verificar mapa de auxílios regionais 2022-2027) |
| Área Metropolitana de Lisboa | Geralmente **não elegível** (com exceções pontuais previstas no mapa de auxílios) |

- **Requisitos RFAI** — Investimento em ativos fixos tangíveis afetos à exploração (com exclusões: terrenos, edifícios — salvo em certos casos —, viaturas ligeiras, equipamento administrativo). Atividade em sectores elegíveis (indústria, turismo, alguns serviços — não inclui sectores excluídos do RGIC como pesca, agricultura primária, setor financeiro). Criação de postos de trabalho e manutenção por 3 anos (PME) ou 5 anos (não PME). Manutenção do investimento pelo mesmo período.  _(DL 162/2014)_
- **Reporte RFAI** — 10 períodos de tributação seguintes.  _(DL 162/2014)_
- **Limite de dedução à coleta** — 50% da coleta de IRC (com exceção para PMEs nos 2 primeiros anos — 100%).  _(DL 162/2014)_

## Secção 12 — Regime SGPS (Sociedade Gestora de Participações Sociais)

### 12.1 Participation exemption (art.º 51.º CIRC) — Dividendos

- **Isenção de lucros e reservas distribuídos** — Os lucros e reservas distribuídos a sujeitos passivos de IRC residentes em Portugal estão isentos de IRC, desde que cumulativamente cumpridos os requisitos.  _(art.º 51.º CIRC)_

**Requisitos participation exemption**  _(art.º 51.º CIRC)_

| Requisito | Conteúdo |
| --- | --- |
| **Participação mínima** | Detenção, direta ou indireta, de **≥10%** do capital social ou dos direitos de voto |
| **Período de detenção** | **≥1 ano** ininterrupto (a contar até à data da distribuição) ou compromisso de manter pelo período mínimo |
| **Sujeição da participada a imposto** | A participada está sujeita a IRC, IRS-PE ou imposto análogo a taxa nominal ≥ **60% da taxa IRC portuguesa** (ou seja, ≥12,6% face à taxa 21%); ou outras condições alternativas (art.º 51.º n.º 1 e n.º 6) |
| **Não residência em paraíso fiscal** | A participada não pode residir em jurisdição da lista de regimes fiscais claramente mais favoráveis (Portaria 150/2004 e 309-A/2020) |

### 12.2 Participation exemption (art.º 51.º-C CIRC) — Mais-valias

- **Isenção mais-valias e menos-valias** — As mais-valias e menos-valias realizadas com a transmissão onerosa de partes sociais que cumpram os mesmos requisitos do art.º 51.º estão isentas (no caso das mais-valias) ou não dedutíveis (no caso das menos-valias) — regime simétrico.  _(art.º 51.º-C CIRC)_

### 12.3 Regime SGPS específico

- **Regras específicas SGPS** — As SGPS (DL 495/88) podem ainda beneficiar de regras específicas sobre: Encargos financeiros suportados com a aquisição de participações (regime de subcapitalização e limitação dos encargos financeiros — art.º 67.º CIRC, "regra dos juros excessivos" / EBITDA fiscal). Prazos de imobilização das participações.  _(DL 495/88; art.º 67.º CIRC)_
- **Default conservador SGPS** — Confirmar (i) participação ≥10%, (ii) detenção ≥1 ano, (iii) sujeição da participada a IRC ou análogo, (iv) participada não residente em paraíso fiscal. Em qualquer dúvida, tributar normalmente.

## Secção 13 — Pilar Dois (Imposto Complementar) — Lei 27/2024

- **Legislação e âmbito** — Lei 27/2024, de 15 de julho — transpõe a Diretiva (UE) 2022/2523 do Conselho relativa a um nível mínimo mundial de tributação para os grupos de empresas multinacionais e grupos nacionais de grande dimensão na União. Aplica-se a grupos de empresas multinacionais (EMN) ou nacionais com rendimento total consolidado anual ≥ €750.000.000 em pelo menos 2 dos 4 períodos de tributação anteriores.  _(Lei 27/2024; Diretiva (UE) 2022/2523)_

**Componentes Pilar Dois**  _(Lei 27/2024)_

| Mecanismo | Conteúdo |
| --- | --- |
| **IIR** (Income Inclusion Rule / Regra de Inclusão dos Rendimentos) | A empresa-mãe final ou intermédia em Portugal deve incluir e tributar os rendimentos das suas filiais com taxa efetiva < 15% até ao mínimo de 15% |
| **UTPR** (Undertaxed Profits Rule / Regra dos Lucros Subtributados) | Mecanismo de "backstop" — se IIR não foi aplicada no topo, as entidades em Portugal pagam top-up |
| **QDMTT** (Qualified Domestic Minimum Top-up Tax / Imposto Complementar Nacional Qualificado) | Portugal aplica o top-up sobre os lucros gerados em Portugal por entidades do grupo até atingir 15% efetivo localmente |

- **Taxa efetiva mínima** — 15% percent (por jurisdição (GloBE Income / Taxes Covered, com ajustamentos GloBE))  _(Lei 27/2024)_
- **Obrigações declarativas** — GloBE Information Return (GIR) — submetido até 15 meses após o fim do exercício (18 meses no primeiro ano de aplicação). Declaração separada de liquidação do imposto complementar em Portugal.  _(Lei 27/2024)_
- **Entrada em vigor em Portugal** — IIR e QDMTT aplicáveis a períodos de tributação iniciados em ou após 1 de janeiro de 2024; UTPR a partir de 1 de janeiro de 2025.  _(Lei 27/2024)_
- **Default conservador Pilar Dois** — Se o grupo tem EBM consolidada > €750M em algum dos últimos 4 anos, escalar a equipa fiscal especializada em Pilar Dois. Este skill identifica a aplicabilidade mas não produz a computação GloBE.

## Secção 14 — Preços de Transferência (art.º 63.º CIRC)

- **Princípio arm's length** — As operações entre entidades relacionadas devem ser contratadas em condições equivalentes às que seriam acordadas entre entidades independentes ("arm's length principle" / princípio da plena concorrência).  _(art.º 63.º CIRC; Portaria 268/2021, de 26 de novembro)_

### 14.1 Obrigações documentais

**Obrigações documentais preços de transferência**  _(Portaria 268/2021)_

| Obrigação | Quando aplicável |
| --- | --- |
| **Dossier de preços de transferência** (Master File + Local File) | Sujeitos passivos com **volume de negócios ≥ €3.000.000** ou operações com partes relacionadas relevantes |
| **CbCR** (Country-by-Country Report) | Grupos multinacionais com receitas consolidadas ≥ **€750.000.000** |
| **Anexo E do Modelo 22** | Quando há operações com partes relacionadas (independentemente do limiar do dossier) |
| **Notificação CbCR** | Empresas residentes que pertençam a grupo MNE com obrigação CbCR — informar AT sobre a entidade declarante |

- **Métodos aceites** — CUP, Resale Price, Cost Plus, TNMM, Profit Split (alinhados com Diretrizes OCDE 2022).  _(Diretrizes OCDE 2022)_
- **Prazo do dossier** — Disponível na sociedade até 15 julho do ano seguinte (mesma data da IES).

## Secção 15 — CFC (Sociedades Estrangeiras Controladas) — art.º 66.º CIRC

**Requisitos CFC**  _(art.º 66.º CIRC)_

| Requisito | Conteúdo |
| --- | --- |
| Controlo | Participação ≥ **25%** (ou ≥10% se outros residentes portugueses controlam, no total, ≥50%) |
| Residência da CFC | Em jurisdição com regime fiscal claramente mais favorável (Portaria 150/2004) OU sujeição a imposto efetivo inferior a **50% do IRC português** |
| Tipo de rendimentos | Rendimentos passivos, royalties, juros, etc., conforme art.º 66.º n.º 2 |

- **Imputação e crédito** — O lucro imputado é tributado na sociedade portuguesa às taxas normais (com crédito por imposto pago no estrangeiro).  _(art.º 66.º CIRC)_
- **Anexo H obrigatório** — Anexo H ao Modelo 22 — preenchimento obrigatório quando há imputação CFC.

## Secção 16 — Retenções na fonte efetuadas pela sociedade

- **Obrigação de retenção** — A sociedade portuguesa, enquanto entidade pagadora, é obrigada a reter na fonte e entregar à AT (via Guia DMR/Modelo 30/Modelo 39 conforme tipo de beneficiário).

**Taxas de retenção na fonte**

| Rendimento | Taxa retenção — residente | Taxa retenção — não residente |
| --- | --- | --- |
| Dividendos (lucros e reservas distribuídos) | 28% (IRS) / dispensável se beneficiário sujeito IRC | 25% (com possibilidade de redução por CDT) |
| Juros | 28% (IRS) / 25% (IRC) | 25% (com redução por CDT) |
| Royalties | 25% | 25% (com redução por CDT; isenção Diretiva Juros e Royalties UE se aplicável) |
| Comissões e rendimentos de capitais diversos | 25% | 25% |
| Rendimentos prediais pagos a não residentes | 25% | 25% |

- **Diretiva Mães-Filhas** — Dispensa de retenção sobre dividendos pagos a sociedade-mãe na UE/EEE com participação ≥10% por ≥1 ano (transposta no art.º 14.º n.º 3 CIRC e art.º 97.º).  _(Diretiva 2011/96/UE; art.º 14.º n.º 3 CIRC; art.º 97.º CIRC)_
- **Diretiva Juros e Royalties** — Dispensa para juros/royalties entre sociedades associadas UE com participação ≥25% por ≥2 anos.  _(Diretiva 2003/49/CE)_

## Secção 17 — Madeira IBC (CINM)

### 17.1 Taxa e prazo

- **Taxa Madeira IBC e prazo** — 5% de IRC sobre rendimentos provenientes de atividades licenciadas pelo CINM. Regime válido até 31 de dezembro de 2027 (sob a aprovação atual da Comissão Europeia como auxílio de Estado compatível). Entidades licenciadas até 31 dez 2024 mantêm o regime até 31 dez 2027 (verificar regime transitório aplicável). percent  _(DL 165/86, de 26 de junho; Decisão da Comissão Europeia SA.21259)_

### 17.2 Requisitos (tabela simplificada)

**Requisitos Madeira IBC (tabela simplificada)**

| Postos de trabalho criados | Matéria coletável máxima beneficiada |
| --- | --- |
| 1 a 2 (com investimento mínimo €75.000) | €2.730.000 |
| 3 a 5 | €3.550.000 |
| 6 a 30 | €21.870.000 |
| 31 a 50 | €35.540.000 |
| 51 a 100 | €54.680.000 |
| > 100 | €205.500.000 |

*(Valores indicativos — verificar o regime atualizado em DL 165/86 e diplomas conexos para o exercício 2025.)*

### 17.3 Atividades elegíveis

- **Atividades elegíveis CINM** — Serviços internacionais (consultoria internacional, prestação de serviços a entidades não residentes em Portugal, e-commerce, propriedade intelectual com gestão na Madeira). Indústria (Zona Franca Industrial — separada). Registo Internacional de Navios da Madeira (MAR) — para atividade de transporte marítimo.
- **Não elegíveis** — Atividades financeiras puras (com restrições pós-reformas 2014), atividades de seguros, atividades concorrenciais no mercado nacional fora do CINM.

### 17.4 Outros benefícios CINM

- **Outros benefícios CINM** — Isenção de retenção sobre pagamento de dividendos a sócios não residentes (com condições). Isenção sobre prestações suplementares dos sócios. Imposto do Selo reduzido em certas operações.
- **Default conservador Madeira IBC final** — Sem licença CINM válida confirmada, aplicar regime geral (IRC 14,7% Madeira ou 21% Continente, conforme sede). Pedir cópia da licença CINM e relatório de cumprimento de requisitos de emprego/investimento.

## Secção 18 — Casos práticos

### 18.1 Lda restauração em Lisboa — não PME

**Factos:** Restaurante das Janelas, Lda. Período coincide com ano civil. Exercício 2025.
- Volume de negócios: €1.500.000.
- 25 trabalhadores. Critério PME cumprido (micro/pequena).
- Resultado líquido contabilístico: €120.000.
- Acréscimos fiscais (TA de viaturas extra, multas, donativos não enquadráveis): +€15.000.
- Deduções (provisões fiscalmente aceites revertidas): −€5.000.
- Sem prejuízos fiscais reportáveis.
- Sede em Lisboa (Derrama Municipal 1,5%).
- Viaturas: 1 ligeira a €40.000 (sem alternativos elétricos) e 1 ligeira a €25.000.
- Despesas de representação: €8.000.

#### 18.1.1 Apuramento do lucro tributável.

- **Apuramento do lucro tributável** — Resultado líquido contabilístico            €120.000 + Acréscimos (Q07)                          €15.000 − Deduções (Q07)                            (€5.000) ───────────── Lucro tributável                            €130.000 − Prejuízos reportáveis                          €0 ───────────── Matéria coletável                           €130.000

#### 18.1.2 IRC.

- **IRC** — Pequena empresa — taxa reduzida nos primeiros €50.000. IRC sobre €50.000 a 17%   = €8.500 IRC sobre €80.000 a 21%   = €16.800 ───────────── IRC                       = €25.300

#### 18.1.3 Derrama Estadual.

- **Derrama Estadual** — Lucro tributável (€130.000) < €1.500.000 → **€0**.

#### 18.1.4 Derrama Municipal Lisboa.

- **Derrama Municipal Lisboa** — Derrama Municipal = 1,5% × €130.000 = €1.950

#### 18.1.5 Tributação Autónoma.

- **Tributação Autónoma** — Viatura €40.000 a 35%                = €40.000 × 35% × 1 (depreciação/encargos anuais ~ €10.000) TA = €10.000 × 35%                  = €3.500 Viatura €25.000 a 10% (encargos €6.000) TA = €6.000 × 10%                   = €600 Despesas representação €8.000 a 10%   = €800 ───────────── TA total                              = €4.900 *(Notas: TA aplica-se aos encargos do exercício, não ao custo total de aquisição. Exemplo simplificado.)*

#### 18.1.6 Coleta total a pagar.

- **Coleta total a pagar** — IRC                  €25.300 Derrama Estadual          €0 Derrama Municipal     €1.950 TA                    €4.900 ───────────── Total                €32.150

#### 18.1.7 Acerto:

- **Acerto** — Coleta total                       €32.150 − Retenções na fonte sofridas        (€800) − PPC efetuados (julho/set/dez)   (€20.000) ───────────── A pagar com Modelo 22              €11.350 Modelo 22 a submeter até **31 maio 2026** (verificar dia útil). IES até **15 julho 2026**.

### 18.2 SGPS holding com dividendos de filial UE

**Factos:** Holding Atlântico, SGPS, S.A. Detém 100% da Atlântico Operações, Lda (PT) e 30% da SkyTech BV (Países Baixos) há 5 anos. Exercício 2025.
- Dividendos recebidos da Atlântico Ops: €500.000.
- Dividendos recebidos da SkyTech BV: €200.000.
- Outras receitas operacionais (serviços de gestão): €120.000.
- Custos operacionais (RH, escritório): €80.000.
- Encargos financeiros (empréstimo para aquisição de SkyTech BV): €50.000.

#### 18.2.1 Aplicação do art.º 51.º (participation exemption).

- **Aplicação do art.º 51.º** — **Dividendos Atlântico Ops:** 100% > 10%; ≥1 ano; participada residente PT e sujeita a IRC. **Isentos.** **Dividendos SkyTech BV:** 30% > 10%; ≥1 ano; Países Baixos sujeitos a IRC nacional > 12,6%; não paraíso fiscal. **Isentos.**  _(art.º 51.º)_

#### 18.2.2 Lucro tributável.

- **Lucro tributável** — Resultado líquido contabilístico         €690.000 (= 500 + 200 + 120 − 80 − 50) − Dividendos isentos art.º 51.º         (€700.000) + Encargos financeiros não aceites (regra art.º 67.º — EBITDA fiscal)      verificar limitação ───────────── Lucro tributável                          €40.000 (ilustrativo, após art.º 67.º) *(Reviewer: aplicar regra do art.º 67.º — limitação dos gastos de financiamento ao maior de €1M ou 30% do EBITDA fiscal — antes de finalizar números.)*  _(art.º 51.º; art.º 67.º)_

#### 18.2.3 IRC.

- **IRC** — Holding Atlântico cumpre critérios PME (assumido). Matéria coletável €40.000 < €50.000: IRC = 17% × €40.000 = €6.800

#### 18.2.4 Derrama Estadual / Municipal.

- **Derrama Estadual / Municipal** — Lucro tributável €40.000 → DE = €0. DM sede (assumir Porto 1,5%) = €600.

#### 18.2.5 Total:

- **Total** — IRC                  €6.800 DM                     €600 Total                €7.400

### 18.3 PME tech no Porto — SIFIDE

**Factos:** CodePorto, Lda. Desenvolvimento de software. Exercício 2025.
- Volume de negócios: €1.200.000.
- 18 trabalhadores. PME (pequena empresa).
- Lucro tributável: €200.000.
- Despesas de I&D elegíveis incorridas em 2025: €150.000.
- Média I&D 2023-2024: €80.000.
- Sem prejuízos reportáveis.
- Sede no Porto (DM 1,5%).
- ANI emitiu declaração SIFIDE confirmando o crédito.

#### 18.3.1 IRC sobre matéria coletável.

- **IRC sobre matéria coletável** — Matéria coletável = Lucro tributável (sem dedução de prejuízos)   €200.000 IRC sobre primeiros €50.000 a 17%                                  €8.500 IRC sobre €150.000 a 21%                                          €31.500 ───────────── IRC bruto                                                         €40.000

#### 18.3.2 Crédito SIFIDE.

- **Crédito SIFIDE** — Componente base: 32,5% × €150.000                                 €48.750 Componente incremental: 50% × (€150.000 − €80.000) = 50% × €70.000  €35.000 ───────────── Crédito SIFIDE                                                    €83.750

#### 18.3.3 Dedução à coleta.

- **Dedução à coleta** — IRC bruto                                                         €40.000 − Crédito SIFIDE deduzido no exercício (limitado à coleta)      (€40.000) ───────────── IRC líquido                                                            €0 Crédito SIFIDE a reportar (8 anos)                                €43.750

#### 18.3.4 Derrama Estadual:

- **Derrama Estadual** — Lucro tributável €200.000 → **€0**.

#### 18.3.5 Derrama Municipal Porto:

- **Derrama Municipal Porto** — DM = 1,5% × €200.000 = €3.000 *(Nota: a derrama municipal incide sobre o lucro tributável independentemente do SIFIDE.)*

#### 18.3.6 Total a pagar:

- **Total a pagar** — IRC líquido                €0 DM                       €3.000 TA (a calcular)            ... Total                    €3.000+ CodePorto deve preencher **Anexo D do Modelo 22** com identificação do crédito SIFIDE e juntar cópia da declaração ANI ao dossier fiscal.

## Secção 19 — Defaults conservadores (resumo)

**Defaults conservadores (resumo)**

| Item | Default |
| --- | --- |
| Estatuto PME | Não PME (21%) até confirmação da Recomendação UE 2003/361/CE em base consolidada |
| Sede / Município | DM 1,5% (taxa máxima) até confirmação |
| Madeira IBC | Não aplicável (21% standard) até prova de licença CINM válida |
| TA em exercício de prejuízo | Adicionar +10 p.p. (art.º 88.º n.º 14) |
| Viaturas — escalão | Quando dúvida, escalão mais alto (35%) |
| Prejuízos reportáveis | Aplicar limite 65% MC; respeitar ordem cronológica; verificar alterações de controlo |
| SIFIDE | Não aplicar sem declaração ANI emitida; sem componente incremental se média 2 anos anteriores incerta |
| RFAI | Verificar região NUTS II e mapa de auxílios; PMEs com manutenção 3 anos / não PMEs 5 anos |
| SGPS — participation exemption | Confirmar ≥10%, ≥1 ano, não paraíso fiscal, participada tributada |
| Pilar Dois | Se EBM consolidada > €750M em 2 dos 4 anos anteriores, escalar a especialista |
| Preços de transferência | Se VN ≥ €3M ou partes relacionadas, exigir Master/Local File |
| Pagamentos por Conta | 80% da coleta ano anterior; 75% se VN ≤ €500.000 |
| PEC | PMEs com cumprimento declarativo: dispensa; grandes empresas: aplicar |
| Retenções na fonte | Aplicar Diretivas UE (Mães-Filhas; Juros e Royalties) apenas com cumprimento dos requisitos formais e materiais |
| Conservação documental | 10 anos (art.º 123.º CIRC) |
| Submissão | Modelo 22 até último dia útil de maio; IES até 15 julho; via Portal das Finanças |
| OE 2025 não confirmado | Marcar **TBC** e sinalizar para verificação no texto publicado da Lei do OE 2025 |

## Secção 20 — Fontes

### Legislação primária

- **Legislação primária** — **Código do IRC (CIRC)** — aprovado pelo DL 442-B/88, de 30 de novembro, e alterações posteriores. - Art.º 8.º — período de tributação. - Art.º 14.º — isenções (Diretiva Mães-Filhas). - Art.º 23.º-A — encargos não dedutíveis (incl. pagamentos a paraísos fiscais). - Art.º 52.º — dedução de prejuízos fiscais (12 anos, limite 65%). - Art.º 51.º e 51.º-C — participation exemption (dividendos e mais-valias). - Art.º 63.º — preços de transferência. - Art.º 66.º — imputação de rendimentos (CFC). - Art.º 67.º — limitação dos gastos de financiamento. - Art.º 69.º a 71.º — RETGS. - Art.º 73.º a 78.º — reorganizações empresariais (neutralidade fiscal). - Art.º 87.º — taxas de IRC (21% / 17%). - Art.º 87.º-A — Derrama Estadual. - Art.º 88.º — Tributação Autónoma. - Art.º 97.º — dispensa de retenção (Diretiva Mães-Filhas). - Art.º 105.º — Pagamentos por Conta. - Art.º 106.º — Pagamento Especial por Conta. - Art.º 117.º — obrigações declarativas. - Art.º 120.º — declaração periódica de rendimentos (Modelo 22). - Art.º 121.º — IES. - Art.º 123.º — obrigações de escrituração (10 anos). **Lei do Orçamento do Estado para 2025** (Lei 45-A/2024) — atualização da taxa PME e limites. **DL 442-B/88** — aprovação do CIRC. **DL 372/2007** — definição de PME (transpõe Recomendação UE 2003/361/CE). **DL 165/86** — Centro Internacional de Negócios da Madeira (CINM/IBC). **Lei 73/2013** — Regime Financeiro das Autarquias Locais (Derrama Municipal).  _(CIRC; Lei 45-A/2024; DL 442-B/88; DL 372/2007; DL 165/86; Lei 73/2013)_

### Legislação complementar

- **Legislação complementar** — **Estatuto dos Benefícios Fiscais (EBF)** — aprovado pelo DL 215/89. **Código Fiscal do Investimento (CFI)** — DL 162/2014: - Arts. 22.º-26.º — RFAI. - Arts. 35.º-42.º — SIFIDE II. **Lei 27/2024, de 15 de julho** — transposição da Diretiva (UE) 2022/2523 (Pilar Dois — Imposto Complementar). **Diretiva (UE) 2022/2523** do Conselho — nível mínimo mundial de tributação (Pilar Dois). **Diretiva 2011/96/UE** — regime comum aplicável às sociedades-mãe e sociedades afiliadas de Estados-membros (Mães-Filhas). **Diretiva 2003/49/CE** — Juros e Royalties.  _(DL 215/89; DL 162/2014; Lei 27/2024; Diretiva (UE) 2022/2523; Diretiva 2011/96/UE; Diretiva 2003/49/CE)_

### Portarias e Decretos Regulamentares

- **Portarias e Decretos Regulamentares** — **Portaria 268/2021, de 26 de novembro** — dossier de preços de transferência. **Portaria 150/2004** — lista de regimes fiscais claramente mais favoráveis (paraísos fiscais), alterada pela Portaria 309-A/2020. **Portaria 220/2008** — declaração Modelo 22. **Decisão da Comissão Europeia SA.21259** — aprovação do regime CINM/Madeira IBC até 31 dez 2027.  _(Portaria 268/2021; Portaria 150/2004; Portaria 309-A/2020; Portaria 220/2008; Decisão SA.21259)_

### Plataformas e entidades

**Portal das Finanças** (portaldasfinancas.gov.pt) — submissão de Modelo 22, IES, pagamentos, consulta de situação fiscal.
**Autoridade Tributária e Aduaneira (AT)** — administração fiscal.
**ANI — Agência Nacional de Inovação** (ani.pt) — emissão de declarações SIFIDE.
**SDM — Sociedade de Desenvolvimento da Madeira** (ibc-madeira.com) — licenciamento CINM.
**OCC — Ordem dos Contabilistas Certificados** (occ.pt).
**OROC — Ordem dos Revisores Oficiais de Contas** (oroc.pt).

## PROIBIÇÕES

- **Não aplicar taxa reduzida PME sem confirmação** — NUNCA aplicar a taxa reduzida PME (17%) sem confirmar cumulativamente os critérios da Recomendação UE 2003/361/CE em base consolidada (empresas associadas e parceiras).  _(Recomendação UE 2003/361/CE)_
- **Não aplicar taxa Madeira IBC sem licença CINM** — NUNCA aplicar a taxa Madeira IBC de 5% sem licença CINM válida emitida pela SDM e sem verificação do cumprimento dos requisitos de emprego/investimento e dos plafonds de matéria coletável.
- **Não omitir Derrama Estadual** — NUNCA omitir a Derrama Estadual quando o lucro tributável excede €1.500.000.
- **Não presumir DM a 0%** — NUNCA presumir Derrama Municipal a 0% sem confirmar a deliberação da Assembleia Municipal para o exercício — usar 1,5% como default conservador.
- **Agravamento TA em exercício de prejuízo** — NUNCA esquecer o agravamento de +10 p.p. sobre todas as Tributações Autónomas em exercício de prejuízo fiscal (art.º 88.º n.º 14).  _(art.º 88.º n.º 14)_
- **Limite dedução prejuízos fiscais 65%** — NUNCA deduzir prejuízos fiscais acima de 65% da matéria coletável do exercício (art.º 52.º n.º 2).  _(art.º 52.º n.º 2)_
- **Limite temporal dedução prejuízos** — NUNCA deduzir prejuízos fiscais com mais de 12 períodos de tributação de antiguidade (ou as regras transitórias para exercícios pré-2023, conforme caso).
- **SIFIDE requer declaração ANI** — NUNCA aplicar o crédito SIFIDE sem a declaração emitida pela ANI; a candidatura submetida não basta.
- **Participation exemption limites** — NUNCA aplicar a participation exemption do art.º 51.º se a participada residir em jurisdição da Portaria 150/2004 ou estiver sujeita a tributação efetiva inferior aos limiares estatutários.  _(art.º 51.º; Portaria 150/2004)_
- **Anexo E partes relacionadas** — NUNCA omitir o Anexo E quando há operações com partes relacionadas, mesmo que o volume de negócios seja inferior a €3M.
- **Pilar Dois escalar especialista** — NUNCA tratar grupos com EBM consolidada > €750M sem analisar o Pilar Dois (Lei 27/2024) — escalar a especialista.  _(Lei 27/2024)_
- **RETGS fora de escopo** — NUNCA produzir computações RETGS (consolidação fiscal) neste skill (R-PT-IRC-6) — exige sign-off específico.  _(R-PT-IRC-6)_
- **Setores excluídos** — NUNCA tratar setor financeiro, segurador, OICs, IPSS, cooperativas ou indústrias extrativas neste skill (R-PT-IRC-1 a R-PT-IRC-4).  _(R-PT-IRC-1 a R-PT-IRC-4)_
- **Não aconselhar pagamento fora de prazo** — NUNCA aconselhar pagamento fora de prazo de IRC, PPC ou PEC — juros compensatórios e de mora aplicam-se nos termos da LGT (taxa de juro compensatório atual: confirmar Portaria em vigor).  _(LGT)_
- **Anexo H CFC** — NUNCA esquecer o Anexo H quando há imputação CFC (art.º 66.º).  _(art.º 66.º)_
- **Isenção retenção Diretiva Mães-Filhas requisitos** — NUNCA aplicar isenção de retenção pela Diretiva Mães-Filhas sem (i) participação ≥10%, (ii) detenção ≥1 ano (ou compromisso), (iii) participada residente UE/EEE sujeita a imposto, (iv) declaração formal da participada.  _(Diretiva Mães-Filhas)_
- **Outputs como estimativas pendentes de revisão** — NUNCA apresentar números como definitivos — todos os outputs devem ser explicitamente identificados como estimativas pendentes de revisão e sign-off por Contabilista Certificado (OCC) ou ROC (OROC).

## Disclaimer

Este skill e os seus outputs destinam-se exclusivamente a fins informativos e computacionais e **não constituem aconselhamento fiscal, jurídico ou financeiro**. Todos os outputs devem ser revistos e validados por um Contabilista Certificado inscrito na Ordem dos Contabilistas Certificados (OCC) ou por um Revisor Oficial de Contas inscrito na Ordem dos Revisores Oficiais de Contas (OROC) antes de qualquer submissão à Autoridade Tributária e Aduaneira (AT) ou ação com base nos números apurados. Especificações da Lei do Orçamento do Estado para 2025 sinalizadas como **TBC** devem ser verificadas contra o texto publicado em Diário da República antes de qualquer aplicação. A versão verificada mais recente é mantida em [openaccountants.com](https://openaccountants.com).

---

*OpenAccountants — skills de contabilidade open-source para IA*

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
