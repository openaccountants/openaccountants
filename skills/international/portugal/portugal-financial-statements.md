---
name: portugal-financial-statements
description: "Utilize esta skill na preparação, revisão ou aconselhamento sobre demonstrações financeiras anuais de uma sociedade portuguesa. Acione com expressões como \"demonstrações financeiras\", \"IES\", \"Informação Empresarial Simplificada\", \"SNC\", \"NCRF\", \"NC-PE\", \"NC-ME\", \"balanço\", \"demonstração de resultados\", \"demonstração de fluxos de caixa\", \"anexo\", \"Portal das Finanças\", \"depósito de contas\", \"ROC\", \"revisão legal de contas\" ou qualquer questão sobre preparação e depósito de contas estatutárias ao abrigo da lei portuguesa. Abrange o referencial SNC, limiares dimensionais, demonstrações obrigatórias, formatos, anexo, submissão da IES e requisitos de auditoria. Trigger also on: \"Portuguese financial statements\", \"SNC accounts\", \"IES filing Portugal\", \"NCRF\", \"NC-ME microentities\", \"NC-PE small entities\", \"balanço\", \"demonstração de resultados\", \"Portal das Finanças deposit of accounts\", \"ROC statutory audit Portugal\"."
version: 1.0
jurisdiction: PT
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Mário Jorge da costa Vale
review_status: current
depends_on:
  - financial-statements-workflow-base
category: financial-statements
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Portugal Financial Statements

## Portugal — Demonstrações Financeiras (SNC) — Skill v1.1

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **Mário Jorge da costa Vale** on 2026-06-04.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### Demonstrações Financeiras

- **Micro — balanço** — ≤ €350.000  _(DL 158/2009)_
- **Micro — volume negócios** — ≤ €700.000  _(DL 158/2009)_
- **Micro — empregados** — ≤ 10  _(DL 158/2009)_
- **Pequena — balanço** — ≤ €4.000.000  _(DL 98/2015)_
- **Pequena — volume negócios** — ≤ €8.000.000  _(DL 98/2015)_
- **Pequena — empregados** — ≤ 50  _(DL 98/2015)_
- **Micro — balanço** — ≤ €450.000  _(DL 126-B/2025)_
- **Micro — volume negócios** — ≤ €900.000  _(DL 126-B/2025)_
- **Pequena — balanço** — ≤ €5.000.000  _(DL 126-B/2025)_
- **Pequena — volume negócios** — ≤ €10.000.000  _(DL 126-B/2025)_
- **Média — balanço** — ≤ €25.000.000  _(DL 126-B/2025)_
- **Média — volume negócios** — ≤ €50.000.000  _(DL 126-B/2025)_
- **Teste** — 2 de 3 critérios no ano corrente + anterior  _(DL 158/2009)_
- **IES — prazo** — 15.º dia do 7.º mês após encerramento (15 julho)  _(Código IRC)_
- **Taxa de registo** — €80  _(IRN)_
- **Multa atraso** — €150–€3.750  _(RGIT)_
- **Balanço** — > €1.500.000  _(CSC)_
- **Volume de negócios** — > €3.000.000  _(CSC)_
- **Empregados** — > 50  _(CSC)_
- **Teste** — 2 de 3 por dois anos consecutivos  _(CSC)_
- **SA (Sociedade Anónima)** — Sempre obrigatória  _(CSC)_

## Secção 1 — Referência Rápida

**Referência Rápida**

| Campo | Valor |
| --- | --- |
| País | Portugal (República Portuguesa) |
| Moeda | EUR |
| Entidade competente | Portal das Finanças (AT — Autoridade Tributária e Aduaneira) + Conservatória do Registo Comercial |
| Legislação principal | Decreto-Lei n.º 158/2009 (SNC); Decreto-Lei n.º 98/2015 (revisão do SNC) |
| Legislação complementar | Código das Sociedades Comerciais (CSC); Código do Registo Comercial |
| Normativo contabilístico | SNC — Sistema de Normalização Contabilística (NCRF, NC-PE, NC-ME) |
| Exercício económico | Em regra, ano civil (janeiro a dezembro) |
| Prazo de entrega | 15.º dia do 7.º mês após o fim do exercício (i.e., 15 de julho para exercícios de ano civil) |
| Taxa de depósito | EUR 80 (registo da prestação de contas) |
| Submissão eletrónica | Via Portal das Finanças (submissão da IES) |

## Secção 2 — Referencial de Relato

**Referencial de Relato**

| Tipo de entidade | Normativo aplicável |
| --- | --- |
| Grandes e médias entidades | NCRF completas (28 normas, alinhadas com IFRS for SMEs) |
| Pequenas entidades | NC-PE (Norma Contabilística e de Relato Financeiro para Pequenas Entidades) |
| Microentidades | NC-ME (Norma Contabilística para Microentidades — muito simplificada) |
| Grupos cotados (contas consolidadas) | IFRS tal como adotadas pela UE (obrigatório, apenas para empresas cotadas na Euronext Lisbon) |
| Grupos não cotados (contas consolidadas) | NCRF ou IFRS (opção) |
| Bancos e seguradoras | IFRS (obrigatório) |

As entidades podem sempre optar por aplicar um normativo de nível superior (e.g., uma microentidade pode optar por aplicar a NC-PE ou as NCRF completas).

## Secção 3 — Limiares Dimensionais

Em vigor para os exercícios económicos até 31 de dezembro de 2025:

**Limiares Dimensionais (até 31 dez 2025)**

| Critério | Micro (NC-ME) | Pequena (NC-PE) | Média | Grande |
| --- | --- | --- | --- | --- |
| Total do balanço | ≤ EUR 350 000 | ≤ EUR 4 000 000 | ≤ EUR 20 000 000 | > EUR 20 000 000 |
| Volume de negócios líquido | ≤ EUR 700 000 | ≤ EUR 8 000 000 | ≤ EUR 40 000 000 | > EUR 40 000 000 |
| Número médio de empregados | ≤ 10 | ≤ 50 | ≤ 250 | > 250 |

**A partir dos exercícios económicos com início em 1 de janeiro de 2026** (DL 126-B/2025):

**Limiares Dimensionais (a partir de 1 jan 2026)**  _(DL 126-B/2025)_

| Critério | Micro | Pequena | Média | Grande |
| --- | --- | --- | --- | --- |
| Total do balanço | ≤ EUR 450 000 | ≤ EUR 5 000 000 | ≤ EUR 25 000 000 | > EUR 25 000 000 |
| Volume de negócios líquido | ≤ EUR 900 000 | ≤ EUR 10 000 000 | ≤ EUR 50 000 000 | > EUR 50 000 000 |
| Número médio de empregados | ≤ 10 | ≤ 50 | ≤ 250 | > 250 |

- **Teste de limiares** — Não pode ultrapassar 2 dos 3 limiares. Avaliação no primeiro exercício, ou durante dois exercícios consecutivos subsequentes.

## Secção 4 — Demonstrações Financeiras Obrigatórias

**Demonstrações Financeiras Obrigatórias**

| Documento | Micro (NC-ME) | Pequena (NC-PE) | Média/Grande (NCRF) |
| --- | --- | --- | --- |
| Balanço | Obrigatório (simplificado) | Obrigatório | Obrigatório |
| Demonstração de resultados por naturezas | Obrigatório (simplificado) | Obrigatório | Obrigatório |
| Demonstração de alterações no capital próprio | Não obrigatório | Não obrigatório | Obrigatório |
| Demonstração de fluxos de caixa | Não obrigatório | Não obrigatório | Obrigatório |
| Anexo | Obrigatório (mínimo) | Obrigatório (simplificado) | Obrigatório (completo) |
| Relatório de gestão | Obrigatório (todas as sociedades) | Obrigatório | Obrigatório |
| Certificação legal de contas | Se aplicável | Se aplicável | Obrigatória (se reunidos os limiares) |

## Secção 5 — Checklist de Ajustamentos de Fim de Exercício

**Checklist de Ajustamentos de Fim de Exercício**

| # | Ajustamento | Notas específicas de Portugal |
| --- | --- | --- |
| 1 | Depreciações e amortizações | NCRF 7; método sistemático; taxas fiscais (Decreto Regulamentar 25/2009) como máximo |
| 2 | Provisões | NCRF 21; obrigação presente, saída provável de recursos, estimativa fiável |
| 3 | Acréscimos e diferimentos | Princípio rigoroso da periodização económica (especialização dos exercícios) |
| 4 | Imparidade de dívidas a receber | NCRF 27; avaliação individual e por carteira |
| 5 | Inventários | NCRF 18; menor entre custo (FIFO/CMP) e valor realizável líquido (VRL) |
| 6 | Impostos diferidos | NCRF 25; diferenças temporárias; taxa de IRC de 21% + derrama |
| 7 | Operações em moeda estrangeira | NCRF 23; itens monetários à taxa de fecho |
| 8 | Locações | NCRF 9; classificação como locação financeira ou operacional |
| 9 | Benefícios dos empregados | NCRF 28; provisão para férias, subsídio de férias e subsídio de Natal |
| 10 | Subsídios do governo | NCRF 22; rendimento diferido reconhecido em resultados |
| 11 | Ativos intangíveis | NCRF 6; capitalização de despesas de desenvolvimento se cumpridos os critérios |
| 12 | Estimativa de IRC | Imposto corrente + tributações autónomas + derrama municipal |

## Secção 6 — Demonstração de Resultados por Naturezas

Modelo SNC — por naturezas:

```
Vendas e serviços prestados
Subsídios à exploração
Ganhos/perdas imputados de subsidiárias, associadas e empreendimentos conjuntos
Variação nos inventários da produção
Trabalhos para a própria entidade
Custo das mercadorias vendidas e das matérias consumidas
Fornecimentos e serviços externos
Gastos com o pessoal
Imparidade de inventários (perdas/reversões)
Imparidade de dívidas a receber (perdas/reversões)
Provisões (aumentos/reduções)
Imparidade de investimentos não depreciáveis/amortizáveis (perdas/reversões)
Aumentos/reduções de justo valor
Outros rendimentos e ganhos
Outros gastos e perdas
  ─── Resultado antes de depreciações, gastos de financiamento e impostos (EBITDA) ───

Gastos/reversões de depreciação e de amortização
Imparidade de investimentos depreciáveis/amortizáveis (perdas/reversões)
  ─── Resultado operacional (antes de gastos de financiamento e impostos) ───

Juros e rendimentos similares obtidos
Juros e gastos similares suportados
  ─── Resultado antes de impostos ───

Imposto sobre o rendimento do período
  ─── Resultado líquido do período ───
```

## Secção 7 — Formato do Balanço

Modelo SNC:

```
ATIVO

Ativo não corrente
  Ativos fixos tangíveis
  Propriedades de investimento
  Goodwill
  Ativos intangíveis
  Participações financeiras
  Outros ativos financeiros
  Ativos por impostos diferidos

Ativo corrente
  Inventários
  Clientes
  Estado e outros entes públicos
  Outras contas a receber
  Diferimentos
  Ativos financeiros detidos para negociação
  Caixa e depósitos bancários

TOTAL DO ATIVO

─────────────────────────────────────

CAPITAL PRÓPRIO E PASSIVO

Capital próprio
  Capital realizado
  Ações (quotas) próprias
  Outros instrumentos de capital próprio
  Prémios de emissão
  Reservas legais
  Outras reservas
  Resultados transitados
  Excedentes de revalorização
  Resultado líquido do período

TOTAL DO CAPITAL PRÓPRIO

Passivo não corrente
  Provisões
  Financiamentos obtidos
  Outras contas a pagar
  Passivos por impostos diferidos

Passivo corrente
  Fornecedores
  Estado e outros entes públicos
  Financiamentos obtidos
  Outras contas a pagar
  Diferimentos

TOTAL DO PASSIVO

TOTAL DO CAPITAL PRÓPRIO E PASSIVO
```

## Secção 8 — Anexo às Demonstrações Financeiras

**Anexo às Demonstrações Financeiras**

| # | Divulgação | Micro | Pequena (NC-PE) | Média/Grande |
| --- | --- | --- | --- | --- |
| 1 | Políticas contabilísticas | Simplificadas | Obrigatório | Obrigatório (completo) |
| 2 | Movimentos de ativos fixos tangíveis | Resumo | Obrigatório | Obrigatório |
| 3 | Locações | Não obrigatório | Se material | Obrigatório |
| 4 | Partes relacionadas | Não obrigatório | Pessoal-chave de gestão | Obrigatório (completo) |
| 5 | Instrumentos financeiros | Não obrigatório | Simplificado | Obrigatório |
| 6 | Pessoal (informação sobre empregados) | Número médio de empregados | Número médio + gastos | Detalhado |
| 7 | Órgãos sociais (remunerações da gestão) | Não obrigatório | Não obrigatório | Obrigatório |
| 8 | Compromissos e contingências | Obrigatório (básico) | Obrigatório | Obrigatório |
| 9 | Impostos sobre o rendimento | Não obrigatório | Simplificado | Obrigatório (reconciliação) |
| 10 | Capital próprio (detalhe) | Obrigatório (básico) | Obrigatório | Obrigatório |
| 11 | Subsídios do governo | Se aplicável | Obrigatório | Obrigatório |
| 12 | Acontecimentos após a data do balanço | Obrigatório | Obrigatório | Obrigatório |

## Secção 9 — Requisitos de Submissão

**Requisitos de Submissão**

| Item | Detalhe |
| --- | --- |
| Forma de submissão | IES (Informação Empresarial Simplificada) — eletrónica via Portal das Finanças |
| Cobertura da submissão única | Declaração fiscal (IRC), depósito no registo comercial, estatísticas (INE) e dados para o Banco de Portugal |
| Prazo de entrega | 15.º dia do 7.º mês após o fim do exercício (15 de julho para sociedades de ano civil) |
| Taxa de depósito | EUR 80 (componente do registo da prestação de contas) |
| Formato | XML eletrónico via Portal das Finanças; anexos em PDF para contas consolidadas |
| Anexos da IES | Anexo A (contas individuais), Anexo A1 (consolidadas), outros conforme aplicável |
| Idioma | Português |
| Contabilista Certificado | A submissão tem de ser efetuada por um Contabilista Certificado (CC) |
| Coima por entrega fora de prazo | EUR 150 a EUR 3 750 (coimas — sanções contraordenacionais) |
| Consequências da não entrega | Impossibilidade de obtenção de certidões comerciais; eventual processo de dissolução |

## Secção 10 — Requisitos de Auditoria

### Nomeação obrigatória de ROC (Revisor Oficial de Contas)

- **Condição de nomeação** — As sociedades têm de nomear um auditor estatutário (certificação legal de contas) se ultrapassarem 2 dos 3 limiares durante dois exercícios consecutivos.

**Limiares de nomeação de ROC**

| Critério | Limiar |
| --- | --- |
| Total do balanço | EUR 1 500 000 |
| Volume de negócios líquido | EUR 3 000 000 |
| Número médio de empregados | 50 |

### Sempre sujeitas a revisão legal de contas

- **Entidades sempre sujeitas a ROC** — Sociedades Anónimas (SA): exigem sempre ROC (conselho fiscal ou conselho de auditoria); Entidades emitentes de valores mobiliários admitidos à negociação em mercado regulamentado; Entidades que preparam contas consolidadas; Entidades de interesse público.

### Qualificação do auditor

- **Qualificação do auditor** — Revisor Oficial de Contas (ROC) ou Sociedade de Revisores Oficiais de Contas (SROC), inscritos na Ordem dos Revisores Oficiais de Contas (OROC).

### Mandato do auditor

- **Duração e rotação do mandato** — Duração: 3 a 4 anos (consoante o modelo de governo societário); Mandato máximo: aplicam-se regras de rotação para entidades de interesse público.

## Aviso Legal

Esta skill e os respetivos resultados são disponibilizados apenas para fins informativos e de cálculo e não constituem aconselhamento fiscal, jurídico ou financeiro. A Open Accountants e os seus contribuidores não assumem qualquer responsabilidade por erros, omissões ou consequências decorrentes da utilização desta skill. Todos os resultados devem ser revistos e validados por um profissional qualificado antes de serem submetidos ou utilizados como base de decisão.

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
