---
name: portugal-financial-statements
description: "Utilize esta skill na preparação, revisão ou aconselhamento sobre demonstrações financeiras anuais de uma sociedade portuguesa para exercícios de 2026. Acione com expressões como \"demonstrações financeiras\", \"IES\", \"Informação Empresarial Simplificada\", \"SNC\", \"NCRF\", \"NCRF-PE\", \"NC-ME\", \"balanço\", \"demonstração de resultados\", \"demonstração de fluxos de caixa\", \"anexo\", \"Portal das Finanças\", \"depósito de contas\", \"ROC\", \"revisão legal de contas\" ou qualquer questão sobre preparação e depósito de contas estatutárias ao abrigo da lei portuguesa. Abrange o referencial SNC, os novos limiares dimensionais do DL 126-B/2025 (micro EUR 450.000 / 900.000, pequenas EUR 5.000.000 / 10.000.000, médias EUR 25.000.000 / 50.000.000), as demonstrações obrigatórias por dimensão, formatos, anexo, prazo de aprovação, submissão da IES até 15 de julho e a revisão legal de contas (CSC art. 262.º: EUR 1.500.000 / 3.000.000 / 50). Fora do âmbito: IRC e impostos diferidos em detalhe (pt-corporate-tax), plano de contas e lançamentos (portugal-bookkeeping), declaração periódica de IVA (portugal-vat-return). Trigger also on: \"Portuguese financial statements\", \"SNC accounts\", \"IES filing Portugal\", \"NCRF\", \"NC-ME microentities\", \"NCRF-PE small entities\", \"Portugal size thresholds 2026\", \"Portal das Finanças deposit of accounts\", \"ROC statutory audit Portugal\"."
version: 1.3
jurisdiction: PT
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - financial-statements-workflow-base
category: financial-statements
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Portugal Financial Statements

## Portugal: Demonstrações Financeiras (SNC), Skill v1.2 (exercícios de 2026)

## Rates and thresholds

> Source-cited draft: not reviewed by an accountant.

Todos os valores foram lidos no Diário da República (texto consolidado ou original) ou no Portal das Finanças em 30 de outubro de 2026. As fontes estão na secção final. Para as taxas de IRC usadas nos impostos diferidos, a skill `pt-corporate-tax` manda se houver divergência.

### Demonstrações Financeiras

- **Micro: total do balanço**: ≤ €450.000 (exercícios com início em ou após 1 jan 2026) _(DL 158/2009, art. 9.º, n.º 1, na redação do DL 126-B/2025)_
- **Micro: volume de negócios líquido**: ≤ €900.000 _(idem)_
- **Micro: número médio de empregados**: ≤ 10 _(idem)_
- **Pequena: total do balanço**: ≤ €5.000.000 _(DL 158/2009, art. 9.º, n.º 2, na redação do DL 126-B/2025)_
- **Pequena: volume de negócios líquido**: ≤ €10.000.000 _(idem)_
- **Pequena: número médio de empregados**: ≤ 50 _(idem)_
- **Média: total do balanço**: ≤ €25.000.000 _(DL 158/2009, art. 9.º, n.º 3, na redação do DL 126-B/2025)_
- **Média: volume de negócios líquido**: ≤ €50.000.000 _(idem)_
- **Média: número médio de empregados**: ≤ 250 _(idem)_
- **Limites até 2025 (exercícios iniciados antes de 1 jan 2026)**: micro €350.000 / €700.000 / 10; pequena €4.000.000 / €8.000.000 / 50; média €20.000.000 / €40.000.000 / 250 _(DL 158/2009, art. 9.º, na redação do DL 98/2015)_
- **Pequenos grupos (base consolidada)**: ≤ €7.500.000 de balanço / ≤ €15.000.000 de volume de negócios / 50 empregados _(DL 158/2009, art. 9.º-B, n.º 1, na redação do DL 126-B/2025; o limite de 50 empregados vem do DL 98/2015 e não mudou)_
- **Grupos médios**: ≤ €25.000.000 / ≤ €50.000.000 / 250 empregados _(DL 158/2009, art. 9.º-B, n.º 2)_
- **Teste**: não ultrapassar 2 dos 3 limites; os limites reportam-se ao período anterior; muda-se de categoria a partir do 3.º período quando 2 dos 3 limites são ultrapassados em dois períodos consecutivos _(DL 158/2009, arts. 9.º e 9.º-A)_
- **Entidades de interesse público**: sempre grandes entidades _(DL 158/2009, art. 9.º, n.º 5)_
- **Aprovação das contas**: 3 meses após o fecho; 5 meses se houver contas consolidadas ou método da equivalência patrimonial _(CSC, art. 65.º, n.º 5)_
- **IES: prazo**: até 15 de julho (ano civil); 15.º dia do 7.º mês após o fecho (outros períodos), seja ou não dia útil _(CIRC, art. 121.º, n.os 2 e 3; DL 8/2007, art. 5.º, n.º 1)_
- **IES entregue fora de prazo: coima**: €150 a €3.750, elevada para o dobro para pessoas coletivas _(RGIT, arts. 117.º, n.º 1, e 26.º, n.º 4)_
- **Gerente que não submete as contas aos sócios: coima**: €50 a €1.500 _(CSC, art. 528.º, n.º 1)_
- **Revisão legal (Lda sem conselho fiscal): total do balanço**: > €1.500.000 _(CSC, art. 262.º, n.º 2)_
- **Revisão legal: vendas líquidas e outros proveitos**: > €3.000.000 _(CSC, art. 262.º, n.º 2)_
- **Revisão legal: número médio de trabalhadores**: > 50 _(CSC, art. 262.º, n.º 2)_
- **Revisão legal: teste**: 2 dos 3 limites ultrapassados durante dois anos consecutivos _(CSC, art. 262.º, n.º 2)_
- **SA (Sociedade Anónima)**: fiscalização sempre com ROC (fiscal único ROC, conselho fiscal com ROC, ou ROC autónomo) _(CSC, arts. 413.º, 414.º e 446.º)_
- **SA com conselho fiscal e ROC separados**: obrigatório para emitentes cotados e SA não totalmente dominadas que ultrapassem 2 de €20.000.000 / €40.000.000 / 250 em dois anos consecutivos _(CSC, art. 413.º, n.º 2)_
- **Mandato do ROC designado pela assembleia geral**: não superior a 4 anos _(CSC, art. 446.º, n.º 2)_

## Secção 1: Referência Rápida

**Referência Rápida**

| Campo | Valor |
| --- | --- |
| País | Portugal (República Portuguesa) |
| Moeda | EUR |
| Entidade competente | Autoridade Tributária e Aduaneira (AT), através do Portal das Finanças (IES), que serve também o registo comercial, o INE e o Banco de Portugal |
| Legislação principal | Decreto-Lei n.º 158/2009 (SNC), alterado pelo DL 98/2015 e pelo DL 126-B/2025 (novos limiares a partir de 2026) |
| Legislação complementar | Código das Sociedades Comerciais (CSC); Código do Registo Comercial; Decreto-Lei n.º 8/2007 (IES); Código do IRC, art. 121.º |
| Normativo contabilístico | SNC: NCRF (completas), NCRF-PE (pequenas entidades), NC-ME (microentidades) |
| Exercício económico | Em regra, ano civil (janeiro a dezembro); a sociedade pode adotar outro período |
| Aprovação das contas | No prazo de 3 meses após o fecho do exercício (5 meses com contas consolidadas ou método da equivalência patrimonial) (CSC, art. 65.º, n.º 5) |
| Prazo de entrega da IES | 15 de julho para exercícios de ano civil; 15.º dia do 7.º mês após o fecho nos restantes casos, seja ou não dia útil (CIRC, art. 121.º; DL 8/2007, art. 5.º) |
| Taxa de registo | Ver "Not yet confirmed" (não confirmada hoje) |
| Submissão eletrónica | IES por transmissão eletrónica no Portal das Finanças |

## Secção 2: Referencial de Relato

**Referencial de Relato**

| Tipo de entidade | Normativo aplicável | Base |
| --- | --- | --- |
| Grandes e médias entidades | NCRF completas | DL 158/2009 (SNC) |
| Pequenas entidades | NCRF-PE (só pode ser adotada pelas entidades do art. 9.º, n.º 2) | DL 158/2009, art. 9.º-C |
| Microentidades | NC-ME obrigatória, salvo opção pelas NCRF ou pela NCRF-PE, identificada na declaração do art. 117.º, n.º 1, al. b) do CIRC | DL 158/2009, art. 9.º-D |
| Entidades com valores mobiliários admitidos em mercado regulamentado (contas consolidadas) | IFRS adotadas pela UE (obrigatório) | DL 158/2009, art. 4.º, n.º 1 |
| Outros grupos (contas consolidadas) | NCRF, ou IFRS por opção desde que as contas sejam objeto de certificação legal | DL 158/2009, art. 4.º, n.º 2 |
| Filiais incluídas na consolidação de uma entidade cotada (contas individuais) | Podem usar IFRS, ficando sujeitas a certificação legal | DL 158/2009, art. 4.º, n.º 3 |
| Bancos e seguradoras | IFRS (regras dos supervisores) | Ver "Not yet confirmed" |

Uma entidade pode sempre aplicar um normativo de nível superior: a microentidade pode optar pela NCRF-PE ou pelas NCRF (art. 9.º-D, n.º 2); a pequena entidade pode aplicar as NCRF completas, porque a NCRF-PE é uma alternativa (art. 9.º-C).

## Secção 3: Limiares Dimensionais

**Limiares Dimensionais (exercícios iniciados antes de 1 jan 2026)** _(DL 158/2009, art. 9.º, na redação do DL 98/2015)_

| Critério | Micro (NC-ME) | Pequena (NCRF-PE) | Média | Grande |
| --- | --- | --- | --- | --- |
| Total do balanço | ≤ EUR 350 000 | ≤ EUR 4 000 000 | ≤ EUR 20 000 000 | > EUR 20 000 000 |
| Volume de negócios líquido | ≤ EUR 700 000 | ≤ EUR 8 000 000 | ≤ EUR 40 000 000 | > EUR 40 000 000 |
| Número médio de empregados | ≤ 10 | ≤ 50 | ≤ 250 | > 250 |

**Limiares Dimensionais (exercícios com início em ou após 1 jan 2026)** _(DL 158/2009, art. 9.º, na redação do DL 126-B/2025, art. 2.º; aplicação nos termos do art. 3.º)_

| Critério | Micro | Pequena | Média | Grande |
| --- | --- | --- | --- | --- |
| Total do balanço | ≤ EUR 450 000 | ≤ EUR 5 000 000 | ≤ EUR 25 000 000 | > EUR 25 000 000 |
| Volume de negócios líquido | ≤ EUR 900 000 | ≤ EUR 10 000 000 | ≤ EUR 50 000 000 | > EUR 50 000 000 |
| Número médio de empregados | ≤ 10 | ≤ 50 | ≤ 250 | > 250 |

O número de empregados não mudou. Os limites de grupos (art. 9.º-B) passaram a: pequenos grupos ≤ EUR 7 500 000 de balanço, ≤ EUR 15 000 000 de volume de negócios e 50 empregados; grupos médios ≤ EUR 25 000 000, ≤ EUR 50 000 000 e 250 empregados, em base consolidada.

- **Como se aplica o teste** (art. 9.º-A): os limites reportam-se ao período imediatamente anterior. A entidade só deixa a sua categoria a partir do 3.º período, quando em dois períodos consecutivos imediatamente anteriores ultrapassa 2 dos 3 limites. Volta à categoria quando deixa de ultrapassar 2 dos 3 limites nos dois períodos consecutivos imediatamente anteriores.
- **Exercícios de 2026**: o DL 126-B/2025 aplica-se às demonstrações financeiras de exercícios com início em, ou após, 1 de janeiro de 2026 (art. 3.º). Para as contas de 2026, os novos limites são comparados com os valores dos períodos anteriores, nos termos do art. 9.º-A.
- **Entidades de interesse público**: são sempre grandes entidades, seja qual for a dimensão (art. 9.º, n.º 5).
- **Atenção**: os limiares da revisão legal de contas do CSC (Secção 10) são outra regra e não mudaram com o DL 126-B/2025.

## Secção 4: Demonstrações Financeiras Obrigatórias

**Demonstrações Financeiras Obrigatórias** _(DL 158/2009, art. 11.º; método direto: NCRF 2, § 14; relatório de gestão: CSC, arts. 65.º e 66.º)_

| Documento | Micro (NC-ME) | Pequena (NCRF-PE) | Média/Grande (NCRF) |
| --- | --- | --- | --- |
| Balanço | Obrigatório (pode ser modelo reduzido) | Obrigatório (pode ser modelo reduzido) | Obrigatório |
| Demonstração dos resultados por naturezas | Obrigatória (pode ser modelo reduzido) | Obrigatória (pode ser modelo reduzido) | Obrigatória (a demonstração por funções é facultativa e adicional) |
| Demonstração das alterações no capital próprio | Dispensada | Dispensada | Obrigatória |
| Demonstração dos fluxos de caixa | Dispensada | Dispensada | Obrigatória; os fluxos das atividades operacionais pelo método direto (NCRF 2, § 14) |
| Anexo | Dispensado se as divulgações do art. 11.º, n.º 4 forem feitas no final do balanço | Obrigatório | Obrigatório |
| Relatório de gestão | Dispensado se divulgar no final do balanço a informação sobre quotas ou ações próprias do art. 66.º, n.º 5, al. d) do CSC (CSC, art. 66.º, n.º 6) | Obrigatório (CSC, art. 65.º) | Obrigatório (CSC, art. 65.º) |
| Certificação legal de contas | Se aplicável (Secção 10) | Se aplicável (Secção 10) | Se aplicável (Secção 10) |

Divulgações no final do balanço de uma microentidade que não apresente anexo (art. 11.º, n.º 4): (a) compromissos financeiros, garantias e ativos e passivos contingentes fora do balanço, incluindo pensões e compromissos com empresas coligadas ou associadas; (b) adiantamentos e créditos concedidos a membros dos órgãos de administração, direção ou supervisão; (c) as informações da alínea d) do n.º 5 do art. 66.º do CSC, quando aplicável.

## Secção 5: Checklist de Ajustamentos de Fim de Exercício

**Checklist de Ajustamentos de Fim de Exercício**

| # | Ajustamento | Notas específicas de Portugal |
| --- | --- | --- |
| 1 | Depreciações e amortizações | NCRF 7; método sistemático; as taxas do Decreto Regulamentar 25/2009 são o máximo aceite fiscalmente (ver `portugal-tax-optimization` e `pt-corporate-tax`) |
| 2 | Provisões | NCRF 21; obrigação presente, saída provável de recursos, estimativa fiável |
| 3 | Acréscimos e diferimentos | Regime do acréscimo (periodização económica) |
| 4 | Imparidade de dívidas a receber | NCRF 27; avaliação individual e por carteira |
| 5 | Inventários | NCRF 18; menor entre custo (FIFO/custo médio ponderado) e valor realizável líquido |
| 6 | Impostos diferidos | NCRF 25; diferenças temporárias; usar a taxa de IRC do período em que a diferença reverte: 19% em 2026, 18% em 2027, 17% a partir de 2028 (CIRC, art. 87.º, n.º 1, e Lei 64/2025, art. 3.º; ver `pt-corporate-tax`) mais derramas |
| 7 | Operações em moeda estrangeira | NCRF 23; itens monetários à taxa de fecho |
| 8 | Locações | NCRF 9; locação financeira ou operacional |
| 9 | Benefícios dos empregados | NCRF 28; férias, subsídio de férias e subsídio de Natal vencidos e não pagos |
| 10 | Subsídios do governo | NCRF 22; rendimento diferido reconhecido em resultados |
| 11 | Ativos intangíveis | NCRF 6; capitalização de despesas de desenvolvimento se cumpridos os critérios |
| 12 | Estimativa de IRC | Imposto corrente, tributações autónomas e derramas (ver `pt-corporate-tax`) |

A numeração das NCRF segue o SNC; o conteúdo de cada norma não foi relido hoje (ver "Not yet confirmed").

## Secção 6: Demonstração de Resultados por Naturezas

Modelo SNC por naturezas (estrutura de referência; os modelos oficiais constam de portaria, ver "Not yet confirmed"):

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
  --- Resultado antes de depreciações, gastos de financiamento e impostos ---

Gastos/reversões de depreciação e de amortização
Imparidade de investimentos depreciáveis/amortizáveis (perdas/reversões)
  --- Resultado operacional (antes de gastos de financiamento e impostos) ---

Juros e rendimentos similares obtidos
Juros e gastos similares suportados
  --- Resultado antes de impostos ---

Imposto sobre o rendimento do período
  --- Resultado líquido do período ---
```

## Secção 7: Formato do Balanço

Modelo SNC (estrutura de referência):

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

-------------------------------------

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

## Secção 8: Anexo às Demonstrações Financeiras

**Anexo às Demonstrações Financeiras**

| # | Divulgação | Micro | Pequena (NCRF-PE) | Média/Grande |
| --- | --- | --- | --- | --- |
| 1 | Políticas contabilísticas | Só se apresentar anexo | Obrigatório | Obrigatório (completo) |
| 2 | Movimentos de ativos fixos tangíveis | Só se apresentar anexo | Obrigatório | Obrigatório |
| 3 | Locações | Não exigido | Se material | Obrigatório |
| 4 | Partes relacionadas | Adiantamentos e créditos a administradores, no final do balanço (art. 11.º, n.º 4, al. b)) | Pessoal-chave de gestão | Obrigatório (completo) |
| 5 | Instrumentos financeiros | Não exigido | Simplificado | Obrigatório |
| 6 | Pessoal | Número médio de empregados | Número médio e gastos | Detalhado |
| 7 | Remunerações dos órgãos sociais | Não exigido | Não exigido | Obrigatório |
| 8 | Compromissos, garantias e contingências fora do balanço | Obrigatório no final do balanço (art. 11.º, n.º 4, al. a)) | Obrigatório | Obrigatório |
| 9 | Impostos sobre o rendimento | Não exigido | Simplificado | Obrigatório (reconciliação) |
| 10 | Capital próprio (detalhe) | Só se apresentar anexo | Obrigatório | Obrigatório |
| 11 | Subsídios do governo | Se aplicável | Obrigatório | Obrigatório |
| 12 | Acontecimentos após a data do balanço | Só se apresentar anexo | Obrigatório | Obrigatório |

As linhas 4 e 8 da coluna "Micro" vêm do art. 11.º, n.º 4 do DL 158/2009. O detalhe das restantes divulgações por norma (NC-ME, NCRF-PE, NCRF) não foi relido hoje (ver "Not yet confirmed").

## Secção 9: Requisitos de Submissão

**Requisitos de Submissão**

| Item | Detalhe |
| --- | --- |
| Forma de submissão | IES (Informação Empresarial Simplificada), por transmissão eletrónica no Portal das Finanças |
| O que a IES cumpre de uma só vez | Declaração anual de informação contabilística e fiscal (CIRC, art. 117.º, n.º 1, al. c)); registo da prestação de contas; informação estatística ao INE; dados contabilísticos ao Banco de Portugal; informação estatística à DGAE; confirmação do beneficiário efetivo (DL 8/2007, art. 2.º, n.º 1) |
| Prazo de entrega | 15 de julho para períodos de ano civil (CIRC, art. 121.º, n.º 2); 15.º dia do 7.º mês após o fecho para outros períodos (art. 121.º, n.º 3), seja ou não dia útil |
| Cessação de atividade | Prazo do art. 120.º, n.º 3 do CIRC (art. 121.º, n.º 4) |
| Concordância | Os valores da declaração têm de concordar com a contabilidade (CIRC, art. 121.º, n.º 5) |
| Aprovação prévia | As contas devem ser aprovadas pelos sócios no prazo de 3 meses (5 com consolidação ou equivalência patrimonial) (CSC, art. 65.º, n.º 5); só as contas aprovadas vão a registo (CSC, art. 70.º, n.º 1) |
| Publicidade | Relatório de gestão, certificação legal e parecer do órgão de fiscalização disponíveis na sede e no sítio da Internet, quando exista (CSC, art. 70.º, n.º 2) |
| Anexos da IES | Anexo A (contas individuais) e outros conforme aplicável (ver "Not yet confirmed") |
| Idioma | Português |
| Coima por entrega fora de prazo | EUR 150 a EUR 3 750 (RGIT, art. 117.º, n.º 1), com limites elevados para o dobro para pessoas coletivas (RGIT, art. 26.º, n.º 4): EUR 300 a EUR 7 500 |
| Gerente que não submete as contas aos sócios | Coima de EUR 50 a EUR 1 500 (CSC, art. 528.º, n.º 1) |
| Taxa de registo, submissão por Contabilista Certificado, consequências da falta de depósito | Ver "Not yet confirmed" |

## Secção 10: Requisitos de Auditoria

### Sociedades por quotas (Lda) sem conselho fiscal

- **Condição de nomeação** (CSC, art. 262.º, n.º 2): a Lda sem conselho fiscal tem de designar um revisor oficial de contas (ROC) para a revisão legal quando, durante dois anos consecutivos, ultrapassa 2 dos 3 limites seguintes.

**Limiares de nomeação de ROC** _(CSC, art. 262.º, n.º 2; texto consolidado com última alteração em 2026-08-26)_

| Critério | Limiar |
| --- | --- |
| Total do balanço | EUR 1 500 000 |
| Total das vendas líquidas e outros proveitos | EUR 3 000 000 |
| Número de trabalhadores empregados em média durante o exercício | 50 |

- **Quando deixa de ser necessário** (art. 262.º, n.º 3): se a sociedade passar a ter conselho fiscal, ou se 2 dos 3 limites não forem ultrapassados durante dois anos consecutivos.
- **Quem designa** (art. 262.º, n.º 4): os sócios; na falta de designação aplicam-se os arts. 416.º a 418.º.
- **Conselho fiscal facultativo** (art. 262.º, n.º 1): o contrato de sociedade pode prever um conselho fiscal, com as regras das sociedades anónimas.
- Estes limites não foram alterados pelo DL 126-B/2025 e podem ser mudados por portaria (art. 262.º, n.º 7).

### Sociedades anónimas (SA): sempre com ROC

- **Modelo clássico** (CSC, art. 413.º, n.º 1): fiscal único, que tem de ser ROC ou SROC, ou conselho fiscal; ou conselho fiscal e ROC separado. O conselho fiscal tem de incluir um ROC, salvo se houver ROC separado (art. 414.º, n.os 1 e 2).
- **Conselho fiscal e ROC separados obrigatórios** (art. 413.º, n.º 2, al. a)): emitentes de valores mobiliários admitidos em mercado regulamentado, e SA não totalmente dominadas que, durante dois anos consecutivos, ultrapassem 2 de: balanço EUR 20 000 000, volume de negócios líquido EUR 40 000 000, 250 empregados.
- **Outros modelos** (art. 446.º, n.º 1): nos modelos com comissão de auditoria ou conselho geral e de supervisão, a assembleia geral designa um ROC ou SROC.

### Outras entidades com certificação legal

- Grupos não cotados que optem por IFRS nas contas consolidadas (DL 158/2009, art. 4.º, n.º 2).
- Filiais de grupos cotados que usem IFRS nas contas individuais (DL 158/2009, art. 4.º, n.º 3).
- Entidades de interesse público e entidades que preparam contas consolidadas em geral: ver "Not yet confirmed".

### Qualificação do auditor

- **Qualificação do auditor**: Revisor Oficial de Contas (ROC) ou Sociedade de Revisores Oficiais de Contas (SROC) (CSC, arts. 262.º, 413.º, 414.º e 446.º), inscritos na Ordem dos Revisores Oficiais de Contas.

### Mandato do auditor

- **Duração**: o ROC designado pela assembleia geral ao abrigo do art. 446.º é designado por tempo não superior a quatro anos (art. 446.º, n.º 2). As regras de rotação para entidades de interesse público não foram relidas hoje.

## Secção 11: Exemplos

**Exemplo 1: pequena entidade que passa a microentidade em 2026.** Uma Lda tem, em 2024 e 2025, balanço de EUR 480 000, volume de negócios de EUR 850 000 e 8 empregados. Com os limites até 2025, ultrapassava 2 dos 3 limites de microentidade (EUR 480 000 > 350 000 e EUR 850 000 > 700 000) e era pequena entidade. Para as contas de 2026, aplicam-se os novos limites: só o balanço ultrapassa o limite (EUR 480 000 > 450 000); o volume de negócios (EUR 850 000 ≤ 900 000) e os empregados (8 ≤ 10) não. Ultrapassa 1 dos 3, logo pode ser microentidade: deve aplicar a NC-ME, salvo opção pela NCRF-PE ou NCRF (art. 9.º-D), e fica dispensada da demonstração das alterações no capital próprio e da demonstração dos fluxos de caixa (art. 11.º, n.º 3). A revisão legal de contas não se aplica: não ultrapassa nenhum dos limites do CSC.

**Exemplo 2: Lda que passa a precisar de ROC.** Uma Lda sem conselho fiscal tem, em 2024 e em 2025, balanço de EUR 1 600 000, vendas líquidas e outros proveitos de EUR 2 800 000 e 55 trabalhadores em média. Em cada um dos dois anos ultrapassa 2 dos 3 limites do art. 262.º, n.º 2 (balanço EUR 1 600 000 > 1 500 000 e trabalhadores 55 > 50; as vendas ficam abaixo de EUR 3 000 000). Tem de designar um ROC para a revisão legal. Para efeitos do SNC continua pequena entidade (EUR 1 600 000 ≤ 5 000 000, EUR 2 800 000 ≤ 10 000 000, 55 > 50: ultrapassa só 1 dos 3), o que mostra que os dois testes são independentes.

## Sources

| Source | URL | Read on |
|---|---|---|
| Decreto-Lei 158/2009 (SNC), consolidated text: arts. 4.º, 9.º, 9.º-A, 9.º-C, 9.º-D, 11.º | https://diariodarepublica.pt/dr/legislacao-consolidada/decreto-lei/2009-34517175 | 2026-10-30 |
| Decreto-Lei 126-B/2025, arts. 2.º (new arts. 9.º and 9.º-B limits) and 3.º (applies to periods starting on or after 1 January 2026) | https://files.diariodarepublica.pt/1s/2025/12/23501/0000400005.pdf | 2026-10-30 |
| Decreto-Lei 98/2015, art. 2.º (art. 9.º limits in force until 2025, art. 9.º-B small-group 50 employees, art. 11.º(1)(d) without "método direto") and art. 5.º (CSC art. 66.º(6), micro entities exempt from the management report) | https://files.diariodarepublica.pt/1s/2015/06/10600/0347003493.pdf | 2026-10-30 |
| Aviso 8256/2015 (NCRF, DR 2.ª série n.º 146, 29 Jul 2015; copy published by the Comissão de Normalização Contabilística), NCRF 2 § 14: operating cash flows by the direct method | https://www.cnc.min-financas.pt/pdf/SNC/2016/Aviso_8256_2015_29Jul_NCRF_RG.pdf | 2026-10-30 |
| Código das Sociedades Comerciais, art. 262.º (consolidated, last change 2026-08-26) | https://diariodarepublica.pt/dr/legislacao-consolidada/decreto-lei/1986-34443975-66858136 | 2026-10-30 |
| Código das Sociedades Comerciais, arts. 65.º, 70.º, 413.º, 414.º, 446.º, 528.º (consolidated) | https://diariodarepublica.pt/dr/legislacao-consolidada/decreto-lei/1986-34443975 | 2026-10-30 |
| Decreto-Lei 8/2007 (IES), consolidated: arts. 2.º and 5.º | https://diariodarepublica.pt/dr/legislacao-consolidada/decreto-lei/2007-34526275 | 2026-10-30 |
| CIRC art. 121.º, annual accounting and tax declaration (IES) deadline | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc121.aspx | 2026-10-30 |
| CIRC art. 87.º with Lei 64/2025 art. 3.º (IRC 19% in 2026, 18% in 2027, 17% from 2028) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87.aspx | 2026-10-30 |
| RGIT art. 117.º, late or missing declarations | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit117.aspx | 2026-10-30 |
| RGIT art. 26.º, fines doubled for companies | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit26.aspx | 2026-10-30 |
| Regulamento Emolumentar dos Registos e Notariado (consolidated, searched for the accounts-filing fee) | https://diariodarepublica.pt/dr/legislacao-consolidada/decreto-lei/2001-34475775 | 2026-10-30 |

Not yet confirmed: the registration fee for the accounts filing (the old version said EUR 80; the RERN text read today does not state it, and a 2007 portaria set EUR 85, so the current amount is open); that the IES must be submitted by a Contabilista Certificado; the consequences of not depositing accounts (no certificates, administrative dissolution); that banks and insurers must use IFRS in their individual accounts (Banco de Portugal and ASF rules not read); that entities preparing consolidated accounts under NCRF and public-interest entities always need a statutory audit; audit-firm rotation rules for public-interest entities; the line-by-line content of the official statement models (Portaria 220/2015) and the NCRF, NCRF-PE and NC-ME disclosure detail in Sections 5, 6, 7 and 8; the list of IES annexes (Anexo A, A1 and others) and the file format (old version: XML, with PDF annexes for consolidated accounts); whether the 2027 State Budget changes any of these figures.

## Aviso Legal

Esta skill e os respetivos resultados são disponibilizados apenas para fins informativos e de cálculo e não constituem aconselhamento fiscal, jurídico ou financeiro. A Open Accountants e os seus contribuidores não assumem qualquer responsabilidade por erros, omissões ou consequências decorrentes da utilização desta skill. Todos os resultados devem ser revistos e validados por um profissional qualificado antes de serem submetidos ou utilizados como base de decisão.

> Contributed by Michael Cutajar.

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
