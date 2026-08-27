---
name: br-simples-nacional
description: "[PT-BR] Use esta skill sempre que for solicitado tratar do Simples Nacional brasileiro ou do regime MEI. Acione com expressões como \"Simples Nacional\", \"MEI\", \"microempreendedor individual\", \"DAS\", \"DASN-SIMEI\", \"anexo Simples\", \"tabela do Simples\", \"Fator R\", ou qualquer dúvida sobre o regime unificado de tributação para micro e pequenas empresas no Brasil. Cobre o DAS mensal fixo do MEI, as tabelas progressivas do Simples Nacional (Anexos I-V), os limites de faturamento, o Fator R, as declarações anuais e a interação com a Reforma Tributária 2026 (CBS/IBS). SEMPRE leia esta skill antes de tocar em qualquer trabalho de Simples Nacional ou MEI no Brasil. — [EN] Use this skill whenever asked about the Brazilian Simples Nacional or MEI regime. Triggers include \"Simples Nacional\", \"MEI\", \"DAS\", \"DASN-SIMEI\", \"Anexo Simples\", \"Fator R\", and any question on the unified tax regime for Brazilian micro and small businesses. Covers MEI fixed monthly DAS, Simples Nacional progressive tables (Anexos I-V), revenue thresholds, Fator R, annual declarations, and the interaction with the 2026 CBS/IBS tax reform. ALWAYS read this skill before touching any Brazilian Simples Nacional or MEI work."
version: 2.0
jurisdiction: BR
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Ariane Marrocos
review_status: current
depends_on:
  - income-tax-workflow-base
category: international
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# BR Simples Nacional

## Brasil — Simples Nacional — Skill v2.1

## Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by **Ariane Marrocos** on 2026-06-03. Items flagged for further clarification are tracked separately and excluded here. This block is generated from verified `skill_facts` — edit the facts, not the prose.

### Simples Nacional

- **MEI** — R$ 81.000/ano (proposta de aumento pendente)  _(LC 123/2006 Art. 18-A)_
- **Microempresa (ME)** — Considera-se Microempresa (ME), para fins da LC nº 123/2006, a pessoa jurídica com receita bruta anual igual ou inferior a R$ 360.000,00.  _(Lei Complementar nº 123/2006 – art. 3º, inciso I.)_
- **EPP** — Considera-se Empresa de Pequeno Porte (EPP) a pessoa jurídica com receita bruta anual superior a R$ 360.000,00 e igual ou inferior a R$ 4.800.000,00, nos termos do art. 3º da LC nº 123/2006.  _(Lei Complementar nº 123/2006 – art. 3º, inciso II.)_
- **Sublimite ICMS/ISS** — O sublimite de receita bruta de R$ 3.600.000, previsto na LC nº 123/2006, pode determinar o recolhimento do ICMS e/ou ISS fora do Simples Nacional em determinados Estados, sem excluir a empresa do regime simplificado.  _(Principal Lei Complementar nº 123/2006 Art. 19. Informou Art. 13 e ele trata dos tributos abrangidos pelo Simples Nacional. O tema sublimite estadual de ICMS/ISS está principalmente relacionado ao: Art. 19 da LC 123/2006.)_
- **Comércio/Indústria** — R$ 81,50 (INSS) + R$ 1,00 (ICMS)  _(Lei Complementar nº 123/2006 – art. 18-A. Lei nº 8.212/1991.)_
- **Serviços** — R$ 86,50 (INSS R$ 81,50 + ISS R$ 5,00).  _(Lei Complementar nº 123/2006 – art. 18-A. Lei nº 8.212/1991.)_
- **Comércio + Serviços** — R$ 87,50 (INSS R$ 81,50 + ICMS R$ 1,00 + ISS R$ 5,00).  _(Lei Complementar nº 123/2006 – art. 18-A. Lei nº 8.212/1991.)_
- **Anexo I** — Comércio, varejo  _(Resolução CGSN nº 140/2018.)_
- **Anexo II** — Indústria, manufatura (inclui IPI)  _(Resolução CGSN nº 140/2018.)_
- **Anexo III** — Anexo III – Prestação de serviços em geral, incluindo diversas atividades de manutenção, reparação, saúde, educação e serviços administrativos, conforme o CNAE e as regras da LC nº 123/2006.  _(Resolução CGSN nº 140/2018.)_
- **Anexo IV** — Anexo IV – Serviços de limpeza, vigilância, segurança, construção civil e atividades correlatas, cuja Contribuição Patronal Previdenciária (CPP) não está incluída no DAS e deve ser recolhida separadamente.  _(Lei nº 8.212/1991.)_
- **Anexo V (ou III via Fator R)** — Anexo V – Atividades intelectuais e profissionais, incluindo consultoria em TI e diversos serviços técnicos especializados, sujeitas à regra do Fator R. Quando o Fator R for igual ou superior a 28%, a tributação poderá ocorrer pelo Anexo III.  _(Resolução CGSN nº 140/2018.)_
- **Fator R limiar** — Nas atividades sujeitas ao Fator R, quando a razão entre a folha de salários dos últimos 12 meses e a receita bruta dos últimos 12 meses for igual ou superior a 28%, a tributação ocorre pelo Anexo III; caso contrário, permanece no Anexo V.  _(Resolução CGSN nº 140/2018.)_
- **DAS mensal** — O DAS do Simples Nacional deve ser recolhido até o dia 20 do mês subsequente ao da apuração da receita, prorrogando-se o vencimento para o primeiro dia útil seguinte quando não houver expediente bancário.  _(Lei Complementar nº 123/2006 – art. 21. Resolução CGSN nº 140/2018.)_
- **DEFIS anual** — A DEFIS deve ser transmitida pelas empresas optantes pelo Simples Nacional até 31 de março do ano subsequente ao ano-calendário a que se refere a declaração.  _(Resolução CGSN nº 140/2018.)_
- **DASN-SIMEI** — O Microempreendedor Individual (MEI) deve apresentar a DASN-SIMEI até 31 de maio do ano subsequente ao ano-calendário a que se referem as informações.  _(Resolução CGSN nº 140/2018.)_
- **Regime híbrido art. 21-A** — O optante pelo Simples Nacional poderá optar pelo recolhimento da CBS e do IBS fora do DAS, nos termos do art. 21-A da LC nº 123/2006, permitindo ao adquirente o aproveitamento dos créditos desses tributos conforme o regime geral.  _(Lei Complementar nº 123/2006 – art. 21-A (incluído pela Reforma Tributária). Lei Complementar nº 214/2025. Emenda Constitucional nº 132/2023.)_

## Seção 1 — Referência rápida

**Referência rápida**

| Campo | Valor |
| --- | --- |
| País | Brasil |
| Tributo | Tributo unificado do Simples Nacional (DAS) que engloba IRPJ, CSLL, PIS, COFINS, CPP, ICMS, ISS, IPI |
| Moeda | Apenas BRL |
| Ano-base | Ano-calendário |
| Legislação principal | Lei Complementar 123/2006 (Estatuto Nacional da Microempresa) |
| Legislação complementar | Resoluções CGSN; LC 155/2016; EC 132/2023; LC 214/2025; LC 227/2026 |
| Autoridade fiscal | Receita Federal do Brasil (RFB); Comitê Gestor do Simples Nacional (CGSN) |
| Portal de entrega | Portal do Simples Nacional (www8.receita.fazenda.gov.br/SimplesNacional) |
| Prazo de entrega | DAS até o dia 20 do mês seguinte; DEFIS até 31 de março; DASN-SIMEI até 31 de maio |
| Colaborador | Open Accountants Community |
| Validação | Verificado por Ariane Marrocos (SP 312052/O-1) em 2026-06-03 |
| Versão da skill | 2.1 |

### Limites de faturamento

**Limites de faturamento**

| Categoria | Faturamento anual máximo |
| --- | --- |
| MEI | R$ 81.000 (TBC — há propostas para elevar a R$ 144.913,41 ainda não promulgadas) |
| Microempresa (ME) | R$ 360.000 |
| Empresa de Pequeno Porte (EPP) | R$ 4.800.000 |
| Sublimite ICMS/ISS | R$ 3.600.000 |

### DAS-MEI mensal (2025)

**DAS-MEI mensal (2025)**

| Atividade | INSS (5% do salário mínimo) | ICMS | ISS | Total |
| --- | --- | --- | --- | --- |
| Comércio/Indústria | R$ 75,90 | R$ 1,00 | -- | R$ 76,90 |
| Serviços | R$ 75,90 | -- | R$ 5,00 | R$ 80,90 |
| Comércio + Serviços | R$ 75,90 | R$ 1,00 | R$ 5,00 | R$ 81,90 |

Baseado no salário mínimo de R$ 1.518,00 vigente em 2025.

### Fórmula da alíquota efetiva

- **Alíquota Efetiva** — Alíquota Efetiva = (RBT12 x Alíquota Nominal - Parcela a Deduzir) / RBT12

### Defaults conservadores

**Defaults conservadores**

| Ambiguidade | Default |
| --- | --- |
| Tipo de entidade desconhecido | ME (não MEI — mais conservador) |
| CNAE desconhecido | Anexo V (alíquotas mais altas) |
| Folha desconhecida para Fator R | Fator R < 28% (permanece no Anexo V) |
| Faixa de faturamento desconhecida | Faixa mais alta aplicável |

## Seção 2 — Insumos obrigatórios e catálogo de recusas

### Insumos obrigatórios

**Mínimo viável** — tipo de entidade (MEI/ME/EPP), receita bruta dos últimos 12 meses (RBT12), tipo de atividade (CNAE), receita do mês corrente.

**Recomendado** — folha de salários (para o Fator R), unidade da federação de registro, histórico de pagamentos do DAS.

**Ideal** — dados completos do PGDAS-D, receita segregada por atividade, confirmação da classificação por Anexo, DEFIS do exercício anterior.

### Catálogo de recusas

- **R-BR-S1 — Transição por exclusão** — Receita superior a R$ 4.800.000. O cliente está excluído do Simples Nacional. Deve migrar para Lucro Presumido ou Lucro Real. Escalar para contador qualificado.
- **R-BR-S2 — Lucro Presumido / Lucro Real** — Esta skill cobre apenas o Simples Nacional e o MEI. Os demais regimes possuem métodos de apuração distintos.
- **R-BR-S3 — Regras estaduais específicas de ICMS** — Regras estaduais detalhadas de ICMS para empresas acima do sublimite exigem conhecimento estadual específico. Escalar.
- **R-BR-S4 — Regime híbrido CBS/IBS com creditamento** — A opção pelo regime híbrido do art. 21-A da LC 123/06 (introduzido pela LC 214/2025) exige análise da composição da clientela B2B versus B2C e simulação de impacto. Escalar para contador para decisão definitiva.

## Seção 3 — Biblioteca de padrões de transações

### 3.1 Padrões de receita

**Padrões de receita**

| Padrão | Tratamento | Notas |
| --- | --- | --- |
| VENDA, RECEITA, PIX RECEBIDO | Incluir no RBT12 | Receita bruta para definição de faixa |
| NF-E EMITIDA, NFS-E EMITIDA | Incluir no RBT12 | Receita por emissão de nota fiscal |
| MERCADO LIVRE, MARKETPLACE | Incluir no RBT12 | Vendas em plataformas |
| EXPORTAÇÃO | Incluir no RBT12 | O teste de limite inclui exportações |
| DEVOLUÇÃO, CANCELAMENTO | Deduzir da receita | Reduz a receita bruta |
| TRANSFERÊNCIA PRÓPRIA | EXCLUIR | Movimentação interna |

### 3.2 Padrões de pagamento de tributos

**Padrões de pagamento de tributos**

| Padrão | Tratamento | Notas |
| --- | --- | --- |
| DAS, SIMPLES NACIONAL | Pagamento unificado | Engloba todos os tributos |
| DAS-MEI, DASN | Pagamento fixo do MEI | Valor fixo mensal |
| ICMS FORA SIMPLES | ICMS apartado | Acima do sublimite ou ICMS-ST |
| ISS FORA SIMPLES | ISS apartado | Acima do sublimite |
| INSS PATRONAL | INSS patronal apartado | Apenas Anexo IV |
| CBS/IBS APARTADO (2026+) | Recolhimento separado fora do DAS | Apenas no regime híbrido do art. 21-A LC 123/06 |

### 3.3 Padrões de definição de Anexo

**Padrões de definição de Anexo**

| Atividade CNAE | Anexo típico | Notas |
| --- | --- | --- |
| Comércio, varejo | Anexo I | Venda de mercadorias |
| Indústria, manufatura | Anexo II | Inclui IPI |
| Serviços gerais, manutenção | Anexo III | Verificar Fator R para atividades do V |
| Limpeza, segurança, construção | Anexo IV | Sem CPP no DAS |
| Consultoria em TI, serviços profissionais | Anexo V (ou III se Fator R >= 28%) | Fator R é crítico |

## Seção 4 — Exemplos resolvidos

### Exemplo 1 — DAS mensal do MEI (Serviços)

**Entrada:** MEI prestando serviços de TI. Salário mínimo R$ 1.518.

**Cálculo:**
- INSS: 5% x 1.518 = R$ 75,90
- ISS: R$ 5,00
- Total DAS: R$ 80,90/mês

### Exemplo 2 — Simples Nacional, Anexo I Comércio

**Entrada:** RBT12 = R$ 500.000. Receita do mês = R$ 45.000.

**Cálculo:**
- Faixa 3 (360.001 a 720.000)
- Alíquota efetiva = (500.000 x 9,50% - 13.860) / 500.000 = 6,728%
- DAS = 45.000 x 6,728% = R$ 3.027,60

### Exemplo 3 — Anexo V com Fator R >= 28%

**Entrada:** Empresa de consultoria, RBT12 = R$ 400.000. Folha dos últimos 12 meses = R$ 130.000.

**Cálculo:**
- Fator R = 130.000 / 400.000 = 32,5% (>= 28%)
- Aplica-se Anexo III em vez do V
- Faixa 3: alíquota efetiva = (400.000 x 13,50% - 17.640) / 400.000 = 9,09%

### Exemplo 4 — Excesso de receita no MEI (dentro de 20%)

**Entrada:** MEI com receita anual de R$ 90.000 (11,1% acima do limite).

**Classificação:**
- Excesso = R$ 9.000
- DAS complementar sobre o excesso pelas alíquotas do Simples ME
- Migração para ME a partir de janeiro do ano seguinte

## Seção 5 — Regras de Tier 1 (quando os dados são claros)

### 5.1 Elegibilidade do MEI

- **Elegibilidade do MEI** — Receita anual máxima R$ 81.000. Máximo de 1 empregado. Vedado a profissões regulamentadas. Vedado a sócio de outra empresa. Vedado ter filiais.  _(LC 123/2006, Arts. 18-A a 18-E)_

### 5.2 Anexos do Simples Nacional

- **Anexos do Simples Nacional** — Anexo I: Comércio (4,00% -- 19,00%). Anexo II: Indústria (4,50% -- 30,00%). Anexo III: Serviços I (6,00% -- 33,00%). Anexo IV: Serviços II — limpeza/segurança/construção (4,50% -- 33,00%, sem CPP no DAS). Anexo V: Serviços profissionais (15,50% -- 30,50%).  _(LC 123/2006, Anexos I-V (com redação dada pela LC 155/2016))_

### 5.3 Regra do Fator R

- **Regra do Fator R** — Para atividades do Anexo V, se o Fator R (razão folha/receita dos últimos 12 meses) >= 28%, a atividade passa a ser tributada pelo Anexo III.  _(LC 123/2006, Art. 18, § 5º-J)_

### 5.4 Sublimite de ICMS/ISS

- **Sublimite de ICMS/ISS** — Se a receita ultrapassar R$ 3.600.000 mas permanecer abaixo de R$ 4.800.000: os tributos federais continuam no DAS do Simples, mas ICMS e ISS são recolhidos FORA do Simples às alíquotas normais estaduais/municipais.

### 5.5 Regra especial do Anexo IV

- **Regra especial do Anexo IV** — O Anexo IV NÃO inclui a CPP (INSS patronal) no DAS. O INSS patronal deve ser recolhido em separado (20% sobre a folha).

## Seção 6 — Catálogo Tier 2 (exige julgamento do revisor)

### 6.1 Cálculo do Fator R

- **Cálculo do Fator R** — Exige dados precisos de folha, incluindo pró-labore, salários, FGTS, INSS e 13º salário. Sinalizar para o revisor.

### 6.2 Atividades em múltiplos Anexos

- **Atividades em múltiplos Anexos** — A receita deve ser segregada por atividade. A receita de cada atividade é tributada pelo respectivo Anexo, mas o RBT12 para definição de faixa é a receita TOTAL. Sinalizar para o revisor.

### 6.3 Sublimite ultrapassado

- **Sublimite ultrapassado** — Receita acima de R$ 3.600.000: aumento significativo de complexidade. Sinalizar para contador.

### 6.4 MEI próximo do teto

- **MEI próximo do teto** — Receita próxima de R$ 81.000: se ultrapassar em mais de 20%, o MEI é convertido retroativamente em ME a partir de janeiro. Deve contratar contador.

### 6.5 Decisão entre Simples cheio e regime híbrido CBS/IBS (a partir de 2026)

- **Decisão híbrido vs Simples cheio** — Sinalizar para o revisor sempre que o cliente tiver clientela predominantemente B2B com interesse no creditamento de CBS/IBS. A opção pelo art. 21-A da LC 123/06 implica recolhimento apartado de CBS+IBS e exige simulação comparativa.

## Seção — Simples Nacional e a Reforma Tributária 2026

### Marco legal

- **EC 132/2023** — Emenda Constitucional que institui o IVA dual brasileiro (CBS federal + IBS subnacional) e extingue gradualmente PIS, COFINS, ICMS e ISS.  _(EC 132/2023)_
- **LC 214/2025** — Lei Complementar que regulamenta a CBS e o IBS, define fato gerador, base de cálculo, não cumulatividade plena, regimes específicos e a opção do art. 21-A da LC 123/06 para optantes do Simples Nacional.  _(LC 214/2025)_
- **LC 227/2026** — Segunda fase da regulamentação, em vigor a partir de janeiro de 2026, com início efetivo da cobrança simbólica.  _(LC 227/2026)_

### MEI permanece isento

- **MEI permanece isento** — O MEI permanece isento de IBS/CBS. Continua recolhendo seus tributos via DAS-MEI, que unifica INSS + ISS/ICMS no valor fixo mensal. Não há qualquer alteração estrutural para o MEI em 2026 e não há repasse de créditos de IBS/CBS aos seus clientes.

### Simples Nacional (ME/EPP) — duas opções a partir de 2026

- **Duas opções a partir de 2026** — O Simples Nacional para ME e EPP continua existindo. Em 2026, o optante pode escolher entre dois caminhos: **(a) Permanecer integralmente no Simples (caminho padrão).** O DAS continua a ser o recolhimento único. IBS e CBS já estão embutidos no DAS, sem créditos transferíveis aos clientes. É a opção mais simples administrativamente e adequada a clientelas predominantemente B2C ou compostas por outros optantes do Simples. **(b) Regime híbrido (opção do art. 21-A da LC 123/06, introduzido pela LC 214/2025).** O contribuinte recolhe CBS e IBS separadamente, fora do DAS, pelas regras gerais do IVA dual, permitindo a transferência de créditos aos adquirentes. Os demais tributos do Simples (IRPJ, CSLL, PIS/COFINS residuais, CPP, ICMS/ISS quando aplicáveis) continuam no DAS. É vantajoso para EPP que vende a empresas B2B do Lucro Real/Presumido interessadas em apropriar créditos integrais.

### Período de teste em 2026

- **Período de teste em 2026** — 2026 é ano de teste com alíquotas simbólicas: CBS 0,9% + IBS 0,1% nas notas fiscais. As multas estão suspensas pelos 3 primeiros meses após a regulamentação, permitindo adaptação operacional sem penalização imediata por erros formais.

### Decisão híbrido vs Simples cheio

**Decisão híbrido vs Simples cheio**

| Perfil do cliente | Recomendação inicial |
| --- | --- |
| Predominantemente B2C ou Simples/MEI | Permanecer no Simples cheio |
| Predominantemente B2B (Lucro Real/Presumido) que exige créditos | Avaliar regime híbrido do art. 21-A |
| Misto | Simulação comparativa obrigatória |

- **Sinalização revisor R-BR-S4** — Sinalizar para revisor (R-BR-S4) toda decisão pelo regime híbrido. A escolha é anual e tem impacto direto sobre a precificação, a competitividade B2B e a carga administrativa.  _(R-BR-S4)_

## Seção 7 — Modelo de papel de trabalho em Excel

```
BRASIL SIMPLES NACIONAL -- Papel de Trabalho
Período: [Mês]

A. RECEITA
  A1. RBT12 (receita bruta, últimos 12 meses)       ___________
  A2. Receita do mês corrente                        ___________
  A3. Tipo de atividade / CNAE                       ___________
  A4. Anexo aplicável                                ___________

B. APURAÇÃO DA ALÍQUOTA
  B1. Faixa de receita                               ___________
  B2. Alíquota nominal                               ___________
  B3. Parcela a deduzir                              ___________
  B4. Alíquota efetiva = (A1 x B2 - B3) / A1         ___________

C. APURAÇÃO DO DAS
  C1. DAS = A2 x B4                                  ___________

D. FATOR R (se atividade do Anexo V)
  D1. Folha total (últimos 12 meses)                 ___________
  D2. Fator R = D1 / A1                              ___________
  D3. >= 28%? Se sim, aplicar Anexo III              ___________

E. CBS/IBS 2026 (se aplicável)
  E1. Opção pelo art. 21-A LC 123/06? (S/N)          ___________
  E2. CBS apartada (0,9% em 2026)                    ___________
  E3. IBS apartado (0,1% em 2026)                    ___________

SINALIZAÇÕES AO REVISOR:
  [ ] Tipo de entidade confirmado (MEI/ME/EPP)?
  [ ] CNAE verificado para seleção do Anexo?
  [ ] Fator R calculado (se Anexo V)?
  [ ] Verificação de sublimite (R$ 3.600.000)?
  [ ] Verificação de exclusão (R$ 4.800.000)?
  [ ] Decisão híbrido vs Simples cheio (2026+)?
```

## Seção 8 — Guia de leitura de extratos bancários

### Formatos de extratos bancários brasileiros

**Formatos de extratos bancários brasileiros**

| Banco | Formato | Campos-chave |
| --- | --- | --- |
| Banco do Brasil, Caixa, Itaú | CSV, PDF, OFX | Data, Histórico, Valor, Saldo |
| Bradesco, Santander | CSV, PDF | Data, Descrição, Débito, Crédito |
| Nubank, Inter, C6 | CSV | Data, Descrição, Valor |

### Termos-chave

**Termos-chave**

| Termo | Indicação |
| --- | --- |
| PIX RECEBIDO | Receita — incluir no faturamento |
| DAS, SIMPLES | Pagamento de tributo |
| PGDAS-D | Sistema de apuração do Simples |
| DASN-SIMEI | Declaração anual do MEI |
| DEFIS | Declaração anual do Simples |
| CBS, IBS | Tributos do IVA dual (a partir de 2026) |

## Seção 9 — Roteiro de onboarding (fallback)

```
PERGUNTAS DE ONBOARDING -- BRASIL SIMPLES NACIONAL
1. Tipo de entidade: MEI, ME ou EPP?
2. Receita bruta nos últimos 12 meses (RBT12)?
3. Código(s) CNAE?
4. Folha de salários — últimos 12 meses?
5. Estado de registro?
6. Se MEI: próximo do teto de R$ 81.000?
7. Possui atividades em múltiplos Anexos?
8. DEFIS ou DASN-SIMEI do ano anterior disponível?
9. Há produtos com ICMS-ST?
10. Possui empregados?
11. (2026+) Composição da clientela: B2B ou B2C?
12. (2026+) Pretende optar pelo regime híbrido do art. 21-A LC 123/06?
```

## Seção 10 — Material de referência

### Tabelas dos Anexos (completas)

**Anexo I — Comércio**

| Faixa | Alíquota | Faixa de Receita | Dedução |
| --- | --- | --- | --- |
| Faixa 1 | 4,00% | até 180K | -- |
| Faixa 2 | 7,30% | 180-360K | 5.940 |
| Faixa 3 | 9,50% | 360-720K | 13.860 |
| Faixa 4 | 10,70% | 720K-1,8M | 22.500 |
| Faixa 5 | 14,30% | 1,8-3,6M | 87.300 |
| Faixa 6 | 19,00% | 3,6-4,8M | 378.000 |

**Anexo II — Indústria**

| Faixa | Alíquota | Dedução |
| --- | --- | --- |
| Faixa 1 | 4,50% | -- |
| Faixa 2 | 7,80% | 5.940 |
| Faixa 3 | 10,00% | 13.860 |
| Faixa 4 | 11,20% | 22.500 |
| Faixa 5 | 14,70% | 85.500 |
| Faixa 6 | 30,00% | 720.000 |

**Anexo III — Serviços I**

| Faixa | Alíquota | Dedução |
| --- | --- | --- |
| Faixa 1 | 6,00% | -- |
| Faixa 2 | 11,20% | 9.360 |
| Faixa 3 | 13,50% | 17.640 |
| Faixa 4 | 16,00% | 35.640 |
| Faixa 5 | 21,00% | 125.640 |
| Faixa 6 | 33,00% | 648.000 |

**Anexo IV — Serviços II**

| Faixa | Alíquota | Dedução |
| --- | --- | --- |
| Faixa 1 | 4,50% | -- |
| Faixa 2 | 9,00% | 8.100 |
| Faixa 3 | 10,20% | 12.420 |
| Faixa 4 | 14,00% | 39.780 |
| Faixa 5 | 22,00% | 183.780 |
| Faixa 6 | 33,00% | 828.000 |

**Anexo V — Serviços III**

| Faixa | Alíquota | Dedução |
| --- | --- | --- |
| Faixa 1 | 15,50% | -- |
| Faixa 2 | 18,00% | 4.500 |
| Faixa 3 | 19,50% | 9.900 |
| Faixa 4 | 20,50% | 17.100 |
| Faixa 5 | 23,00% | 62.100 |
| Faixa 6 | 30,50% | 540.000 |

### Principais referências legais

**Principais referências legais**

| Tema | Referência |
| --- | --- |
| Estatuto do Simples Nacional | LC 123/2006 |
| Tabelas dos Anexos | LC 123/2006, Anexos I-V (alterados pela LC 155/2016) |
| MEI | LC 123/2006, Arts. 18-A a 18-E |
| Fator R | LC 123/2006, Art. 18, § 5º-J |
| Limites de faturamento | LC 123/2006, Art. 3º |
| Sublimite ICMS/ISS | LC 123/2006, Arts. 13 e 18 |
| Reforma Tributária — IVA dual | EC 132/2023 |
| Regulamentação CBS/IBS | LC 214/2025 |
| Segunda fase / vigência 2026 | LC 227/2026 |
| Opção híbrida do Simples | LC 123/2006, Art. 21-A (incluído pela LC 214/2025) |

## PROIBIÇÕES

- NUNCA aplicar as alíquotas do Simples Nacional a empresas acima de R$ 4.800.000
- NUNCA permitir que profissionais regulamentados se inscrevam como MEI
- NUNCA ignorar o Fator R no cálculo de atividades do Anexo V
- NUNCA usar somente a receita da atividade corrente para definir a faixa — usar o RBT12 de TODAS as atividades
- NUNCA esquecer que o Anexo IV NÃO inclui o INSS patronal no DAS
- NUNCA tratar os valores do DAS-MEI como fixos entre anos — variam com o salário mínimo
- NUNCA omitir a verificação do sublimite de ICMS/ISS para empresas acima de R$ 3.600.000
- NUNCA apresentar cálculos como definitivos — sempre rotular como estimativa e direcionar o cliente a um contador registrado no CRC
- NUNCA recomendar a opção pelo regime híbrido do art. 21-A da LC 123/06 sem simulação comparativa e revisão por contador
- NUNCA tratar o MEI como sujeito a CBS/IBS — o MEI permanece isento e continua recolhendo apenas pelo DAS-MEI

## Aviso legal

Esta skill e seus resultados são fornecidos exclusivamente para fins informativos e de cálculo e não constituem aconselhamento tributário, jurídico ou financeiro. A Open Accountants e seus colaboradores não assumem qualquer responsabilidade por erros, omissões ou consequências decorrentes do uso desta skill. Todos os resultados devem ser revisados e assinados por profissional qualificado (como contador registrado no CRC ou profissional licenciado equivalente no Brasil) antes de qualquer entrega ou tomada de decisão.

A versão mais atualizada e verificada desta skill é mantida em [openaccountants.com](https://openaccountants.com). Faça login para acessar a versão mais recente, solicitar revisão profissional por contador licenciado e acompanhar atualizações conforme a legislação evoluir.

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
