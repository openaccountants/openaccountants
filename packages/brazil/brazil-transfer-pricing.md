---
name: brazil-transfer-pricing
description: "EN: Use this skill whenever asked about Brazil transfer pricing rules, documentation requirements, or preços de transferência compliance. Trigger on phrases like \"transfer pricing Brazil\", \"Brazilian TP documentation\", \"preços de transferência\", \"master file Brazil\", \"local file Brazil\", \"CbCR Brazil\", \"APA Brazil\", \"Law 14.596/2023\", \"IN RFB 2161\", \"arm's length Brazil\", \"ECF\", or any question about intercompany pricing for Brazilian entities. PT-BR: Use esta skill sempre que for solicitada análise sobre as regras de preços de transferência no Brasil, requisitos de documentação ou conformidade em preços de transferência. Acione com expressões como \"preços de transferência Brasil\", \"documentação de TP brasileira\", \"preços de transferência\", \"master file Brasil\", \"local file Brasil\", \"CbCR Brasil\", \"APA Brasil\", \"Lei 14.596/2023\", \"IN RFB 2161\", \"arm's length Brasil\", \"ECF\", ou qualquer questão sobre precificação intercompany para entidades brasileiras."
version: 1.0
jurisdiction: BR
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Ariane Marrocos
review_status: current
depends_on: - transfer-pricing-workflow-base
category: transfer-pricing
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Brazil Transfer Pricing

## Brasil — Preços de Transferência (TP) — Skill v1.1

## Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by **Ariane Marrocos** on 2026-06-03.
Items flagged for further clarification are tracked separately and excluded here.
This block is generated from verified `skill_facts` — edit the facts, not the prose.

### Preços de Transferência

- **Legislação principal** — Lei 14.596/2023 + IN RFB 2.161/2023  _(Lei 14.596/2023)_
- **Vigência** — Obrigatório desde 1º de janeiro de 2024  _(Lei 14.596/2023)_
- **Regime anterior** — Regras das Leis 9.430/1996 e 9.959/2000 substituídas pela Lei 14.596/2023.  _(Lei 14.596/2023)_
- **Brasil na OECD** — Brasil em processo de adesão à OCDE; regime de Preços de Transferência alinhado às diretrizes da OCDE desde 2024.  _(Organisation for Economic Co-operation and Development Lei nº 14.596/2023)_
- **Master File** — Obrigatório para contribuintes no escopo; entrega 3 meses após ECF  _(IN RFB 2.161/2023)_
- **Local File** — Obrigatório; português; 3 meses após ECF  _(IN RFB 2.161/2023)_
- **CbCR** — Receita consolidada ≥ R$ 2,4 bilhões  _(IN RFB 2.161/2023)_
- **ECF (dados de TP)** — Julho do ano seguinte  _(Instrução Normativa RFB nº 2.004/2021)_
- **Prazo especial 2024** — 31 de dezembro de 2025  _(IN RFB 2.161/2023)_
- **PIC (CUP)** — Sim  _(Lei 14.596/2023 Art. 12)_
- **PRL (Resale Price)** — Sim  _(Lei 14.596/2023)_
- **MCL (Cost Plus)** — Sim  _(Lei 14.596/2023)_
- **MLT/TNMM** — Sim  _(Lei 14.596/2023)_
- **MDL (Profit Split)** — Sim  _(Lei 14.596/2023)_
- **Atraso Master/Local File** — Multas específicas por atraso, omissão ou incorreção; inclui multa de 0,2% por mês-calendário ou fração em determinadas hipóteses  _(Lei 14.596/2023)_
- **Documentação inexata** — 3% da receita; mín R$ 20.000; máx R$ 5.000.000  _(Lei 14.596/2023)_
- **Atraso ECF** — Multa de R$ 1.500 por mês-calendário ou fração (PJ).  _(Lei 8.218/1991; IN RFB 2.004/2021)_
- **Ajuste de TP pela RFB** — Tributo devido + SELIC + multa de 75% (ou 150% em caso de fraude).  _(Lei 14.596/2023; Lei 9.430/1996)_

## Seção 1 — Referência Rápida

**Referência Rápida**

| Campo | Valor |
| --- | --- |
| País | Brasil (República Federativa do Brasil) |
| Autoridade tributária | Receita Federal do Brasil (RFB) |
| Legislação principal de TP | Lei 14.596/2023 (novo regime alinhado à OECD); IN RFB 2.161/2023 (regulamentação) |
| Regime anterior | Leis 9.430/1996 e 9.959/2000 (sistema prescritivo de margens fixas — totalmente substituído) |
| Membro da OECD? | Sim (ingresso em janeiro de 2024) |
| Signatário do BEPS? | Sim |
| Data de vigência (novas regras) | Obrigatório a partir de 1º de janeiro de 2024 (adoção antecipada disponível para o ano-calendário de 2023) |
| Moeda | BRL |
| Idioma da documentação | Local File: português; Master File: aceitos em inglês ou espanhol (tradução mediante solicitação) |
| Versão da skill | 1.1 |

## Seção 1A — Contexto CBS/IBS (Reforma Tributária)

TP no Brasil aplica-se a IRPJ/CSLL sobre lucro. A Reforma Tributária 2026 afeta tributos sobre consumo (CBS/IBS), mas **serviços importados** entram no campo de CBS (sujeitos a recolhimento pelo tomador a partir de 2027). Atenção em operações intercompany de serviços com partes relacionadas no exterior — pode haver dupla incidência: TP (IRPJ) e CBS (consumo).

## Seção 2 — Requisitos de Documentação

### 2.1 Master File (Arquivo Global)

**Master File (Arquivo Global)**

| Item | Detalhe |
| --- | --- |
| Obrigatório? | Sim, para contribuintes no escopo (transações controladas com partes relacionadas no exterior) |
| Formato | Estrutura de três níveis alinhada à OECD, conforme IN RFB 2.161/2023 |
| Idioma | Inglês ou espanhol aceitos; tradução para o português mediante solicitação da RFB |
| Prazo de entrega | 3 meses após o prazo de entrega da ECF (outubro para contribuintes com ano-calendário padrão) |

### 2.2 Local File (Arquivo Local)

**Local File (Arquivo Local)**

| Item | Detalhe |
| --- | --- |
| Obrigatório? | Sim, para contribuintes com transações controladas |
| Níveis de conteúdo | Simplificado para contribuintes menores; completo para contribuintes maiores |
| Conteúdo do Local File completo | Descrição do negócio, concorrentes, transações controladas, aplicação de método, dados contábeis |
| Idioma | Português |
| Prazo de entrega | 3 meses após o prazo de entrega da ECF |

### 2.3 Classificação por Nível

**Classificação por Nível**

| Categoria | Critérios | Nível de Documentação |
| --- | --- | --- |
| Categoria 1 | Abaixo dos limites | Local File simplificado |
| Categoria 2 | Volumes intercompany intermediários | Local File padrão |
| Categoria 3 | Grandes volumes intercompany | Local File completo + Master File |

### 2.4 Declaração País-a-País (CbCR)

**Declaração País-a-País (CbCR)**

| Item | Detalhe |
| --- | --- |
| Limite | Receita consolidada do grupo ≥ BRL 2,4 bilhões (aprox. EUR 750 milhões) |
| Prazo de entrega | Incluído no ciclo de entrega da ECF |
| Conteúdo | Conforme Anexo III da OECD |

### 2.5 Declaração Corporativa (ECF)

**Declaração Corporativa (ECF)**

| Item | Detalhe |
| --- | --- |
| Informações de TP | Dados de preços de transferência incluídos na ECF (Escrituração Contábil Fiscal) |
| Prazo de entrega da ECF | Julho do ano seguinte (contribuintes com ano-calendário padrão) |

## Seção 3 — Princípio Arm's Length

### 3.1 Definição

- **Princípio arm's length** — As transações controladas devem ser precificadas de forma consistente com as condições que seriam estabelecidas entre partes não relacionadas em transações comparáveis sob circunstâncias comparáveis (princípio arm's length).  _(Artigo 2º, Lei 14.596/2023)_

### 3.2 Contexto Histórico

O regime anterior do Brasil (1996-2023) utilizava métodos prescritivos de margens fixas (PIC, PRL, CPL, PVEx, PVA, PVV, CAP) com margens estatutárias. O novo regime (a partir de 2024) adota plenamente o padrão arm's length da OECD.

### 3.3 Métodos Aceitos (Novo Regime)

**Métodos Aceitos (Novo Regime)**

| Método | Aceito |
| --- | --- |
| Preço Independente Comparável (PIC / CUP) | Sim |
| Preço de Revenda menos Lucro (PRL) | Sim |
| Custo mais Lucro (MCL / Cost Plus) | Sim |
| Margem Líquida da Transação (MLT / MMT / TNMM) | Sim |
| Divisão do Lucro (MDL / Profit Split) | Sim |

Observação: outros métodos da legislação anterior — PCI, PCEx, MMA, MMR, MTM, CAP, CPL — permanecem como referência histórica e podem aparecer em documentação de períodos transitórios.

### 3.4 Método Mais Apropriado

- **Método Mais Apropriado** — O método mais apropriado deve ser selecionado com base na natureza da transação, na comparabilidade e na disponibilidade de dados. Não há hierarquia estatutária.  _(Artigo 12, Lei 14.596/2023)_

### 3.5 Diretrizes da OECD como Fonte Subsidiária

- **Diretrizes da OECD como Fonte Subsidiária** — As Diretrizes de Preços de Transferência da OECD (edição de 2022 e atualizações aprovadas) servem como fonte subsidiária de interpretação, salvo quando contrárias à legislação brasileira ou a atos normativos da RFB.  _(IN RFB 2.161/2023, Art. 1º, §4º)_

## Seção 4 — Obrigações Acessórias

**Obrigações Acessórias**

| Obrigação | Detalhe |
| --- | --- |
| ECF (informações de TP) | Entrega eletrônica anual (julho) |
| Master File | Entregue 3 meses após o prazo da ECF |
| Local File | Entregue 3 meses após o prazo da ECF |
| CbCR | Conforme ciclo de entrega da ECF |
| Responsabilidade técnica | Especialista/consultor externo que preparou o estudo econômico assume a responsabilidade técnica |

## Seção 5 — Prazos

**Prazos**

| Item | Prazo |
| --- | --- |
| Entrega da ECF (incluindo dados de TP) | Julho do ano seguinte (ano-calendário padrão) |
| Master File e Local File | 3 meses após o prazo da ECF (outubro no padrão; dezembro de 2025 para a transição do ano-calendário de 2024) |
| Prazo especial para o ano-calendário de 2024 (primeiro ano) | 31 de dezembro de 2025 |
| CbCR | Dentro do ciclo de entrega da ECF |

## Seção 6 — Penalidades

**Penalidades**

| Infração | Penalidade |
| --- | --- |
| Entrega em atraso do Master/Local File | 0,2% por mês (ou fração) sobre a receita bruta do contribuinte |
| Entrega sem atender aos requisitos (inexata/incompleta) | 3% da receita bruta; mínimo BRL 20.000; máximo BRL 5.000.000 |
| Entrega em atraso da ECF | BRL 1.500/mês para pessoas jurídicas (regra geral) |
| Informações inexatas no CbCR | 0,2% da receita consolidada do grupo multinacional do ano anterior |
| Ajuste de TP pela RFB | Tributo adicional + juros SELIC + multa de 75% (padrão) ou 150% (fraude/sonegação) |

## Seção 7 — Acordos Prévios de Preços (APA)

**Acordos Prévios de Preços (APA)**

| Item | Detalhe |
| --- | --- |
| Disponibilidade | Sim (introduzido pela Lei 14.596/2023; "Processo de Consulta Específico") |
| Tipos | Unilateral (inicialmente); bilateral/multilateral previstos |
| Regulamentação | Em desenvolvimento — RFB abriu consulta pública em agosto de 2024 |
| Vigência | Regulamentação em vigor a partir de 1º de janeiro de 2025 |
| Duração | A definir (expectativa de 3-5 anos) |
| Taxas | A definir |
| Status | Novo mecanismo; experiência prática ainda limitada |

## Seção 8 — Safe Harbours

**Safe Harbours**

| Área | Detalhe |
| --- | --- |
| Geral | Não há safe harbour estatutário amplo no novo regime |
| Serviços intragrupo de baixo valor agregado | Conforme Art. 23 da Lei 14.596/2023; regras específicas para serviços intragrupo |
| Operações financeiras | Disposições específicas em instruções normativas em elaboração |
| Commodities | Regras separadas em desenvolvimento |
| Regime histórico | Métodos antigos de margens fixas (PRL 20%, CPL 20%, etc.) não se aplicam mais |

## Seção 9 — Desenvolvimentos Recentes

**Desenvolvimentos Recentes**

| Data | Desenvolvimento |
| --- | --- |
| Janeiro de 2024 | Novo regime de TP alinhado à OECD passa a ser obrigatório (Lei 14.596/2023) |
| Setembro de 2023 | Publicação da IN RFB 2.161/2023 (regulamentação) |
| Agosto de 2024 | Consulta pública sobre regras de serviços intragrupo e APA |
| Janeiro de 2025 | Regulamentação de APA em vigor |
| Janeiro de 2024 | Brasil torna-se membro da OECD |
| Dezembro de 2025 | Primeiras entregas de Master/Local File (referentes ao ano-calendário de 2024) |
| Contínuo | Instruções normativas adicionais esperadas para: commodities, intangíveis, operações financeiras, reestruturações |
| Contínuo | Implementação do Pilar Dois em discussão |

## Seção 10 — Interação com Outras Skills

**Interação com Outras Skills**

| Skill relacionada | Interação |
| --- | --- |
| brazil-corporate-tax (IRPJ/CSLL) | Ajustes de TP afetam a base do IRPJ e da CSLL |
| brazil-bookkeeping | Documentação de TP baseia-se em registros contábeis brasileiros (alinhados ao IFRS) |
| Entrega da ECF | Dados de preços de transferência são parte integrante da ECF |
| Subcapitalização | Regras separadas nos Arts. 24-25 da Lei 12.249/2010 interagem com TP em empréstimos intercompany |
| CbCR | Utilizado pela RFB para avaliação de risco |
| Valoração aduaneira | Ajustes de TP podem impactar tributos aduaneiros sobre importações |
| brazil-indirect-tax (CBS/IBS) | Serviços importados intercompany podem gerar dupla incidência: TP (IRPJ/CSLL) e CBS (consumo, a partir de 2027) |

## Aviso Legal

Esta skill e seus resultados são fornecidos apenas para fins informativos e computacionais e não constituem aconselhamento tributário, jurídico ou financeiro. A Open Accountants e seus colaboradores não assumem qualquer responsabilidade por erros, omissões ou consequências decorrentes do uso desta skill. Todos os resultados devem ser revisados e validados por profissional qualificado antes da entrega ou utilização.

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
