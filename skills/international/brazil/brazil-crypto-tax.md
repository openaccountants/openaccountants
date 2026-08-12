---
name: brazil-crypto-tax
description: Use this skill whenever asked about Brazil cryptocurrency or digital asset taxation / Use esta skill sempre que for solicitado sobre tributação de criptomoedas ou ativos digitais no Brasil. Trigger on phrases like "crypto tax Brazil", "imposto de renda cripto", "Bitcoin Brazil", "criptoativos Brasil", "cryptocurrency gains Brazil", "Receita Federal crypto", "DARF crypto", "GCAP crypto", "staking Brazil", "mining income Brazil", "NFT tax Brazil", "Binance Brazil", "Mercado Bitcoin", "IN 1888", "Instrução Normativa 1888", "IRPF crypto", "ganho de capital crypto", or any question about the income tax, capital gains, or reporting obligations for cryptocurrency, tokens, or digital assets for Brazilian tax residents / ou qualquer pergunta sobre imposto de renda, ganhos de capital ou obrigações acessórias relativas a criptomoedas, tokens ou ativos digitais para residentes fiscais no Brasil. Covers progressive capital gains rates, monthly R$35,000 de minimis threshold, IN RFB 1,888/2019 reporting, DARF payments, IRPF annual declaration, and Crypto Framework Law 14,478/2022 / Abrange alíquotas progressivas de ganho de capital, isenção mensal de R$ 35.000, obrigação acessória da IN RFB 1.888/2019, pagamento de DARF, declaração anual de IRPF e Lei 14.478/2022 (Marco Legal das Criptos). ALWAYS read this skill before touching any Brazil crypto work / SEMPRE leia esta skill antes de qualquer trabalho com criptoativos no Brasil.
version: 1.0
jurisdiction: BR
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Ariane Marrocos
review_status: current
depends_on: - brazil-income-tax
category: crypto
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Brazil Crypto Tax

## Brasil — Tributação de Criptoativos — Skill v1.1

## Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by **Ariane Marrocos** on 2026-06-03.
Items flagged for further clarification are tracked separately and excluded here.
This block is generated from verified `skill_facts` — edit the facts, not the prose.

### Cripto

- **Até R$ 5.000.000** — 15%  _(Lei 13.259/2016)_
- **R$ 5.000.001 – R$ 10.000.000** — 17,5%  _(Lei 13.259/2016)_
- **R$ 10.000.001 – R$ 30.000.000** — 20%  _(Lei 13.259/2016)_
- **Acima de R$ 30.000.000** — 22,5%  _(Lei 13.259/2016)_
- **Limite de alienações** — É isento do imposto de renda o ganho de capital decorrente da alienação de criptoativos quando o valor total das alienações realizadas no mês, consideradas conjuntamente as operações efetuadas em diferentes exchanges e carteiras, não ultrapassar R$ 35.000, observadas as regras do art. 22 da Lei nº 9.250/1995 e os entendimentos da Receita Federal.  _(A IN RFB nº 1.888/2019 não institui a isenção; ela trata da obrigação acessória de reporte de operações com criptoativos.; Lei nº 9.250/1995 – art. 22. Decreto nº 9.580/2018 Soluções de Consulta da Receita Federal sobre criptoativos.)_
- **Efeito** — É isento do imposto de renda o ganho de capital auferido na alienação de bens e direitos quando o valor total das alienações realizadas no mês não ultrapassar R$ 35.000, observadas as regras do art. 22 da Lei nº 9.250/1995.  _(Lei nº 9.250/1995 – art. 22. Lei nº 11.196/2005.)_
- **Se ultrapassado** — Se o valor total das alienações realizadas no mês ultrapassar R$ 35.000, a isenção para alienação de bens de pequeno valor deixa de ser aplicável, e o ganho de capital passa a ser tributado pelas regras normais, não apenas sobre a parcela excedente ao limite.  _(Lei nº 11.196/2005 – art. 38. Lei nº 9.250/1995. Entendimentos da Receita Federal sobre alienação de bens de pequeno valor e criptoativos.)_
- **Quem reporta** — PF em exchange estrangeira: se operações > R$ 30.000/mês  _(IN RFB 1.888/2019)_
- **Exchanges brasileiras** — Reportam automaticamente à RFB todas as operações  _(IN RFB 1.888/2019)_
- **Saldo ≥ R$ 5.000 por cripto em 31/12** — Obrigatório declarar em Bens e Direitos  _(Instrução Normativa RFB nº 2.180/2024)_
- **Código DARF** — O imposto sobre ganho de capital apurado por pessoa física deve ser recolhido por DARF código 4600, até o último dia útil do mês subsequente ao da alienação do bem ou direito.  _(Programa GCAP Decreto nº 9.580/2018)_
- **Vencimento** — O imposto sobre ganho de capital deve ser recolhido até o último dia útil do mês subsequente ao da alienação do bem ou direito, mediante DARF código 4600.  _(Programa GCAP Decreto nº 9.580/2018)_
- **Ferramenta** — GCAP – Programa utilizado para apuração de ganho de capital e importação para a DIRPF  _(N SRF nº 84/2001)_
- **Padrão obrigatório** — Custo médio ponderado por unidade  _(Programa GCAP Decreto nº 9.580/2018)_

## Seção 1 -- Referência Rápida

**Referência Rápida**

| Campo | Valor |
| --- | --- |
| País | Brasil (República Federativa do Brasil) |
| Tributo | Imposto de Renda (IR) — Ganho de Capital sobre Criptoativos |
| Moeda | BRL (todos os valores devem estar em BRL na data da operação) |
| Ano fiscal | Ano-calendário (1º de janeiro a 31 de dezembro) |
| Legislação principal | Lei 7.713/1988 (Art. 3º §3º); Lei 8.981/1995 (Art. 21); Lei 13.259/2016 (alíquotas progressivas de GC) |
| Marco regulatório | Instrução Normativa RFB 1.888/2019 (obrigação acessória mensal); Lei 14.478/2022 (Marco Legal das Criptos) |
| Autoridade fiscal | Receita Federal do Brasil (RFB) |
| Portal de entrega | e-CAC (Centro Virtual de Atendimento ao Contribuinte) |
| Declaração anual | IRPF (Declaração de Ajuste Anual do Imposto de Renda da Pessoa Física) |
| Prazo de entrega anual | Último dia útil de maio do ano seguinte (ex.: 29 de maio de 2026 para o ano-base 2025) |
| Obrigação mensal | DARF (Documento de Arrecadação de Receitas Federais) — código 4600 |
| Prazo de pagamento mensal | Último dia útil do mês seguinte ao da alienação |
| Validado por | Pendente — requer assinatura de contador brasileiro registrado no CRC |
| Versão da skill | 1.1 |

### Resumo das Alíquotas (2025)

**Resumo das Alíquotas (2025)**

| Item | Alíquota / Limite |
| --- | --- |
| Ganho de capital (alíquotas progressivas) | 15% / 17,5% / 20% / 22,5% (vide Seção 3) |
| Isenção mensal (de minimis) | Alienações ≤ **R$ 35.000** no total em todas as exchanges no mês → ganhos **isentos** |
| Limite mensal de obrigação acessória (IN 1.888) | Operações > **R$ 30.000/mês** fora de exchanges brasileiras → obrigatório reportar à RFB |
| Limite para declaração anual | Saldos ≥ **R$ 5.000** por tipo de cripto em 31 de dezembro → obrigatório declarar no IRPF |

### Nota sobre a Reforma Tributária (CBS/IBS)

Operações de PF (ganhos de capital, IRPF mensal) seguem inalteradas pela Reforma Tributária 2026. Para **PJ que opera exchange ou intermediação de criptoativos**, os serviços passam a ser tributados por CBS (a partir de 2027) e IBS (gradualmente de 2029 a 2033), substituindo PIS/Cofins/ISS. Compra/venda direta de cripto entre pessoas físicas permanece fora do campo de incidência de CBS/IBS (não é serviço).

### Padrões Conservadores

**Padrões Conservadores**

| Ambiguidade | Padrão |
| --- | --- |
| Custo de aquisição desconhecido | PARAR — não é possível apurar ganho sem custo de aquisição |
| Residência fiscal desconhecida | PARAR — o Brasil tributa renda mundial apenas para residentes fiscais |
| Valor de alienação próximo do limite de R$ 35.000 | Calcular com precisão considerando TODAS as exchanges/carteiras combinadas |
| Dúvida sobre entrega da IN 1.888 | Entregar em caso de dúvida — as multas pela não entrega são severas |
| Classificação do token indefinida | Tratar como criptoativo (ativo financeiro) — sujeito a ganho de capital |

## Seção 2 -- Regras de Classificação

### 2.1 Classificação pela Receita Federal

- **Classificação de criptoativos** — A Receita Federal classifica criptoativos como "ativos financeiros" / "bens e direitos". Não são moeda de curso legal, mas estão sujeitos ao imposto de renda sobre ganhos e devem ser declarados no IRPF anual.

**IRPF Bens e Direitos — Grupo 08 (Criptoativos)**

| Código | Tipo | Exemplos |
| --- | --- | --- |
| 01 | Bitcoin (BTC) | BTC |
| 02 | Outras criptomoedas (altcoins) | ETH, SOL, ADA, XRP, LTC, BNB |
| 03 | Stablecoins | USDT, USDC, DAI, BRZ, BUSD |
| 10 | NFTs (Tokens Não Fungíveis) | Arte digital, colecionáveis, itens de jogos |
| 99 | Outros criptoativos | Utility tokens, governance tokens, tokens DeFi, security tokens |

### 2.2 Fatos Geradores

**Fatos Geradores**

| Evento | Tributável? | Observações |
| --- | --- | --- |
| Cripto → BRL (venda em exchange) | Sim | Ganho = valor de alienação − custo de aquisição |
| Cripto → cripto (swap) | Sim | Cada permuta é uma alienação tributável; ganho/perda a valor de mercado |
| Cripto → bens/serviços | Sim | Alienação ao valor de mercado dos bens/serviços recebidos |
| Recebimento de cripto como pagamento | Sim | Rendimento ao valor de mercado na data do recebimento |
| Transferência entre carteiras próprias | Não | Não há mudança de titularidade beneficiária |
| Doação de cripto | Possivelmente | Pode incidir ITCMD (tributo estadual); não é IR federal |
| Herança de cripto | Possivelmente | ITCMD em nível estadual; custo de aquisição = valor de mercado na data do óbito ou valor declarado |

## Seção 3 -- Tabelas de Alíquotas e Apuração

### 3.1 Imposto sobre Ganho de Capital — Alíquotas Progressivas

**Alíquotas Progressivas**  _(Lei 13.259/2016, Art. 1º; Lei 8.981/1995, Art. 21.)_

| Faixa de lucro (BRL) | Alíquota |
| --- | --- |
| Até R$ 5.000.000 | **15%** |
| De R$ 5.000.001 a R$ 10.000.000 | **17,5%** |
| De R$ 10.000.001 a R$ 30.000.000 | **20%** |
| Acima de R$ 30.000.000 | **22,5%** |

- **Natureza das alíquotas** — São alíquotas marginais — cada faixa aplica-se apenas à parcela do ganho compreendida em seu intervalo.  _(Lei 13.259/2016, Art. 1º; Lei 8.981/1995, Art. 21.)_

### 3.2 Isenção Mensal (De Minimis)

**Isenção Mensal (De Minimis)**

| Parâmetro | Valor |
| --- | --- |
| Limite | Total de alienações ≤ **R$ 35.000** no mês-calendário |
| Abrangência | Soma de TODAS as alienações de cripto em TODAS as exchanges e carteiras no mês |
| Efeito | Se o total alienado ≤ R$ 35.000 → ganhos **isentos** de imposto |
| Se ultrapassado | O imposto incide sobre o **ganho total** (não apenas sobre o excedente a R$ 35.000) |

- **Atenção** — O limite de R$ 35.000 baseia-se no valor total alienado (e não no ganho), apurado considerando todas as plataformas combinadas — e não por exchange.

### 3.3 Pagamento Mensal por DARF

**Pagamento Mensal por DARF**

| Parâmetro | Valor |
| --- | --- |
| Código de DARF | **4600** (IRPF — Ganho de Capital — Alienação de Criptoativo) |
| Vencimento | Último dia útil do mês seguinte ao da alienação |
| Ferramenta de apuração | GCAP (Programa de Apuração dos Ganhos de Capital) — software da Receita Federal |
| Multa por atraso no pagamento | 0,33% ao dia (limitada a 20%) + juros pela taxa Selic |
| Emissão | Pelo GCAP ou pelo Sicalc Web (receita.fazenda.gov.br) |

- **Fórmula de apuração** — Ganho mensal = Σ(valor de alienação − custo de aquisição) de todas as alienações de cripto no mês Se total alienado > R$ 35.000: Imposto = aplicar alíquotas progressivas sobre o ganho total Senão: Imposto = R$ 0 (isento)

## Seção 4 -- Métodos de Custo de Aquisição

### 4.1 Método Aceito

**Método Aceito**

| Método | Status | Observações |
| --- | --- | --- |
| **Custo médio ponderado por unidade** | **Padrão / default** | A Receita Federal exige o custo médio ponderado |
| Identificação específica | Não padrão | Não é o método default segundo orientação da RFB |
| FIFO / LIFO | Não padrão | Não previstos pela Receita Federal para pessoa física |

- **Cálculo do custo médio ponderado** — Novo custo médio = (custo total anterior + custo da nova aquisição) / quantidade total mantida  _(O método padrão para pessoas físicas brasileiras é o custo médio ponderado por unidade)_

### 4.2 Componentes do Custo de Aquisição

- Preço de compra em BRL (converter moeda estrangeira pela PTAX da data da aquisição)
- Taxas de exchange e corretagem
- Taxas de rede/gas diretamente atribuíveis à aquisição
- Taxas de transferência

### 4.3 Declaração do Custo de Aquisição no IRPF

- Utilizar sempre o **custo de aquisição**, nunca o valor de mercado
- Informar em "Bens e Direitos" → Grupo 08 → código apropriado
- "Situação em 31/12/2024" = custo de aquisição ao final do exercício anterior
- "Situação em 31/12/2025" = custo de aquisição atualizado ao final do exercício corrente
- Em caso de venda integral no exercício, informar R$ 0,00 no saldo final do ano

## Seção 5 -- DeFi, Staking, Mineração e Airdrops

**DeFi, Staking, Mineração e Airdrops**

| Atividade | Tratamento Tributário | Momento | Observações |
| --- | --- | --- | --- |
| Mineração (pessoa física, eventual) | Rendimento a valor de mercado quando os tokens forem vendidos | Na alienação | Custo de aquisição = despesas incorridas (energia etc.), se documentadas; caso contrário, zero |
| Mineração (negócio/profissional) | Receita empresarial (PJ ou MEI) | No recebimento ou na alienação, conforme a contabilidade | Sujeita a tributos corporativos (Simples, Lucro Presumido ou Lucro Real) |
| Recompensas de staking | Rendimento a valor de mercado no recebimento → fixa o custo de aquisição | No recebimento (para custo); ganho na alienação | Tratar como "rendimentos" — deve constar no IRPF; sujeito a GC na alienação |
| Juros de empréstimo DeFi | Rendimento a valor de mercado no recebimento | No recebimento | Análogo a rendimento financeiro; pode ser classificado como "rendimentos de aplicação financeira" |
| Provisão de liquidez | Adicionar ao pool = potencial alienação (swap); tokens LP = nova aquisição | A cada evento | Cada lado da entrada/saída de liquidez é fato gerador se o total no mês > R$ 35 mil |
| Yield farming | Rendimento a valor de mercado no recebimento | No recebimento | Cada recebimento de token estabelece um novo custo de aquisição |
| Airdrops (gratuitos) | Custo de aquisição = R$ 0; tributável na alienação se alienações mensais > R$ 35.000 | Na alienação | Devem ser declarados em "Bens e Direitos" do IRPF se o valor ≥ R$ 5.000 |
| Airdrops (vinculados a serviço) | Rendimento a valor de mercado no recebimento | No recebimento | Incluir em "Rendimentos Tributáveis Recebidos de PF/Exterior" |
| Hard forks | Novas moedas: custo de aquisição = R$ 0 | Na alienação | Declarar no IRPF; custo da moeda original permanece inalterado |

## Seção 6 -- Tratamento de NFTs

**Tratamento de NFTs**

| Cenário | Tratamento |
| --- | --- |
| Compra de NFT | Aquisição pelo custo — custo de aquisição (Grupo 08, Código 10 no IRPF) |
| Venda de NFT com lucro | Ganho de capital; sujeito ao de minimis de R$ 35.000/mês e às alíquotas progressivas |
| Criação e venda (artista/criador) | Se habitual → receita empresarial (MEI, Simples ou Lucro Presumido); se eventual → rendimentos diversos via GCAP |
| Permuta NFT → NFT | Fato gerador — cada lado avaliado a valor de mercado |
| Royalties de NFT (smart contract) | Rendimento a valor de mercado no recebimento; declarar como rendimento |
| Declaração obrigatória no IRPF | Sim, se o custo de aquisição ≥ R$ 5.000 em 31 de dezembro |

## Seção 7 -- Obrigações Acessórias

### 7.1 Obrigação Mensal — IN RFB 1.888/2019

**Obrigação Mensal — IN RFB 1.888/2019**  _(Instrução Normativa RFB 1.888 (3 de maio de 2019), alterada pela IN RFB 2.065/2022.)_

| Quem deve reportar | Quando | Como |
| --- | --- | --- |
| **Exchanges brasileiras** (ex.: Mercado Bitcoin, Foxbit, NovaDAX) | Mensalmente, todas as operações independentemente do valor | Automático — a exchange reporta à RFB |
| **Pessoas físicas** que operam em exchanges estrangeiras (Binance, Coinbase, Kraken etc.) ou P2P | Mensalmente, se o total de operações > **R$ 30.000** no mês | Via e-CAC, sistema "Coleta Nacional" |
| **Pessoas jurídicas** que operam em exchanges estrangeiras | Mensalmente, se o total de operações > **R$ 30.000** no mês | Via e-CAC |

- **Prazo** — Último dia útil do mês seguinte ao das operações.  _(Instrução Normativa RFB 1.888 (3 de maio de 2019), alterada pela IN RFB 2.065/2022.)_
- **Penalidades pelo descumprimento** — Pessoas físicas: até 1,5% do valor da operação não declarada; Pessoas jurídicas: até 3% do valor da operação não declarada; Entrega em atraso: a partir de R$ 100 por mês de atraso; Código de DARF para multas: 5720  _(Art. 10, IN 1.888)_

### 7.2 Apuração Mensal no GCAP e Pagamento de DARF

**Apuração Mensal no GCAP e Pagamento de DARF**

| Etapa | Detalhe |
| --- | --- |
| 1. Apurar os ganhos | Utilizar o GCAP para cada mês com alienações > R$ 35.000 |
| 2. Emitir DARF | Código 4600; período = mês/ano da alienação |
| 3. Pagar DARF | Até o último dia útil do mês seguinte |
| 4. Importar para o IRPF | No encerramento do exercício, importar dados do GCAP para a declaração anual |

### 7.3 Declaração Anual do IRPF

**Declaração Anual do IRPF**

| Seção | Finalidade | Quem deve declarar |
| --- | --- | --- |
| **Bens e Direitos, Grupo 08** | Declarar todos os criptoativos pelo custo de aquisição | Quem detiver ≥ R$ 5.000 em qualquer tipo de cripto em 31 de dezembro |
| **Rendimentos Isentos e Não Tributáveis** | Informar ganhos isentos (meses com alienações ≤ R$ 35.000) | Quem teve ganhos isentos com cripto |
| **Rendimentos Sujeitos à Tributação Exclusiva** | Informar ganhos já tributados por DARF | Quem pagou DARF sobre ganhos com cripto |
| **Dívidas e Ônus Reais** | Informar dívidas/empréstimos relacionados a cripto | Quando aplicável |

- **Campo Discriminação** — O campo "Discriminação" deve incluir: quantidade detida, nome/símbolo do token, exchange ou forma de custódia (exchange brasileira, exchange estrangeira ou carteira de autocustódia) e data de aquisição.
- **IRPF 2025 — localização** — A partir do IRPF 2025: o contribuinte deve indicar se o criptoativo está no Brasil (localização 105) ou no exterior (localização 106).

### 7.4 Lei 14.478/2022 — Marco Legal das Criptos

- **Lei 14.478/2022 — Marco Legal das Criptos** — Essa lei (sancionada em 21 de dezembro de 2022, com vigência a partir de 20 de junho de 2023) estabelece o marco regulatório das prestadoras de serviços de ativos virtuais (VASPs) no Brasil. Embora seja predominantemente regulatória (e não tributária), impacta o compliance fiscal porque: - Exige o credenciamento das VASPs junto ao Banco Central do Brasil (BCB) - Impõe compliance de PLD/KYC para as exchanges em operação no Brasil - Viabiliza melhor troca de informações entre as exchanges e a Receita Federal - O BCB foi designado regulador principal (Decreto 11.563/2023)  _(Lei 14.478/2022; Decreto 11.563/2023)_

### 7.5 Decripto — Sucessor da IN 1.888

A Receita Federal vem desenvolvendo o "Decripto" para substituir o regime de reporte da IN 1.888. O sistema trará formatos de dados mais padronizados, maior capacidade de cruzamento e menor margem para inconsistências. Os contribuintes devem acompanhar os comunicados da RFB quanto aos prazos de implementação.

## Seção 8 -- Compensação e Transporte de Prejuízos

**Compensação e Transporte de Prejuízos**

| Regra | Detalhe |
| --- | --- |
| Compensação dentro do mês | Perdas com cripto podem compensar ganhos com cripto **no mesmo mês** |
| Compensação entre meses | Perdas de um mês **não podem** ser transportadas para compensar ganhos em meses futuros |
| Compensação entre classes de ativos | Perdas com cripto **não podem** compensar ganhos de outras classes (ex.: ações, imóveis) |
| Transporte para frente | **Não permitido** para fins de ganho de capital de pessoa física |
| Transporte para trás | **Não permitido** |
| Implicação estratégica | Os contribuintes devem temporizar as alienações para compensar ganhos e perdas dentro do mesmo mês-calendário |

Diferença crucial em relação a outras jurisdições: o Brasil não permite o transporte de perdas de capital com cripto. As perdas expiram ao final do mês em que ocorrem.

## Seção 9 -- Regras Antielisivas

**Regras Antielisivas**

| Regra | Descrição |
| --- | --- |
| Norma geral antielisão (CTN, Art. 116, parágrafo único) | A autoridade fiscal pode desconsiderar atos sem substância econômica |
| Preços de transferência | Aplicáveis a operações transfronteiriças com partes vinculadas (Lei 14.596/2023, alinhada à OCDE) |
| Beneficiário final | A Receita Federal pode desconsiderar interpostas pessoas ou trusts |
| Estruturação / fracionamento | Fracionar deliberadamente alienações entre meses para permanecer abaixo de R$ 35.000 é monitorado; se identificado como artificial, a RFB pode agregar |
| Declaração de capitais no exterior | CBE (Capitais Brasileiros no Exterior) — declaração anual ao BCB para ativos no exterior > US$ 1 milhão (trimestral se > US$ 100 milhões) |
| Regras de CFC | Residentes brasileiros com participações em entidades estrangeiras em jurisdições de baixa tributação: a renda pode ser atribuída anualmente (Lei 14.754/2023) |

## Seção 10 -- Exemplos Resolvidos

### Exemplo 1 -- Alienação Mensal Abaixo de R$ 35.000 (Isenta)

**Dados:** Residente fiscal no Brasil. Em março de 2025, vendeu 0,5 BTC por R$ 30.000 no Mercado Bitcoin. Custo de aquisição (custo médio): R$ 20.000.

**Apuração:**
```
Valor de alienação:        R$ 30.000
Custo de aquisição:        R$ 20.000
Ganho:                     R$ 10.000

Total alienado em março:   R$ 30.000 (≤ limite de R$ 35.000)

Imposto devido:            R$ 0 (isento — total alienado ≤ R$ 35.000)
```

**Declaração:** Informar o ganho em "Rendimentos Isentos e Não Tributáveis" no IRPF anual. Não há DARF a recolher. Não há obrigação de IN 1.888 (operação em exchange brasileira — reporta automaticamente).

### Exemplo 2 -- Alienação Mensal Acima de R$ 35.000 (Tributável)

**Dados:** Residente fiscal no Brasil. Em julho de 2025:
- Vendeu 1 BTC por R$ 50.000 na Binance (exchange estrangeira). Custo de aquisição: R$ 30.000.
- Vendeu 2 ETH por R$ 15.000 na Coinbase (exchange estrangeira). Custo de aquisição: R$ 8.000.

**Apuração:**
```
Total alienado em julho: R$ 50.000 + R$ 15.000 = R$ 65.000 (> R$ 35.000)

Ganho BTC:  R$ 50.000 - R$ 30.000 = R$ 20.000
Ganho ETH:  R$ 15.000 - R$ 8.000  = R$ 7.000
Ganho total: R$ 27.000

Imposto (alíquotas progressivas):
  R$ 27.000 está integralmente na primeira faixa (≤ R$ 5 mi)
  Imposto = R$ 27.000 × 15% = R$ 4.050

Código de DARF: 4600
Vencimento:     último dia útil de agosto de 2025
```

**Declaração:**
1. Pagar DARF (R$ 4.050) até o final de agosto de 2025
2. Entregar a IN 1.888 via e-CAC (operações em exchange estrangeira > R$ 30.000 no mês)
3. Importar dados do GCAP no IRPF anual (entrega até maio de 2026)

### Exemplo 3 -- Rendimentos de Staking e Posterior Alienação

**Dados:** Residente fiscal no Brasil. Em 2025:
- Recebeu 1 ETH em recompensas de staking ao longo do ano. O valor de mercado em cada data de recebimento totaliza R$ 10.000.
- Em dezembro, vendeu o 1 ETH staked por R$ 12.000 no Mercado Bitcoin.

**Apuração:**
```
Rendimentos de staking:
  Custo de aquisição do ETH recebido = R$ 10.000 (VM nas datas de recebimento)
  Declarar como rendimento no momento do recebimento

Alienação em dezembro:
  Total alienado em dezembro: R$ 12.000 (≤ R$ 35.000)
  Ganho: R$ 12.000 - R$ 10.000 = R$ 2.000
  Imposto: R$ 0 (isento — total alienado ≤ R$ 35.000)
```

**Declaração:** Informar o rendimento de staking no IRPF. Declarar a posição de ETH em Bens e Direitos (Grupo 08, Código 02). Ganho isento em "Rendimentos Isentos".

## Autoverificações

Antes de finalizar qualquer apuração de tributos sobre criptoativos no Brasil:

- [ ] Confirmado que o contribuinte é residente fiscal no Brasil (domicílio fiscal no Brasil)
- [ ] Total mensal de alienações calculado em TODAS as exchanges e carteiras combinadas
- [ ] Limite de minimis de R$ 35.000 aplicado corretamente (com base no valor total alienado, não no ganho)
- [ ] DARF emitida e paga em todos os meses em que as alienações ultrapassaram R$ 35.000
- [ ] IN 1.888 entregue mensalmente para operações em exchanges estrangeiras > R$ 30.000
- [ ] Custo de aquisição apurado pelo método do custo médio ponderado
- [ ] Todos os saldos de cripto ≥ R$ 5.000 por tipo declarados no IRPF Bens e Direitos (Grupo 08)
- [ ] Ganhos isentos informados em "Rendimentos Isentos e Não Tributáveis"
- [ ] Ganhos tributados importados do GCAP para o IRPF
- [ ] Rendimentos de staking/mineração/airdrop incluídos e custo de aquisição estabelecido
- [ ] Sem transporte de prejuízos entre meses (vedado no Brasil)
- [ ] Ativos em exchanges estrangeiras informados em CBE quando aplicável (> US$ 1 milhão no exterior)

## Aviso Legal

Esta skill e seus resultados são fornecidos exclusivamente para fins informativos e de apoio à apuração e não constituem aconselhamento tributário, jurídico ou financeiro. A Open Accountants e seus colaboradores não se responsabilizam por erros, omissões ou consequências decorrentes do uso desta skill. Todos os resultados devem ser revisados e assinados por um profissional habilitado (como contador registrado no CRC, advogado tributarista ou profissional licenciado equivalente no Brasil) antes da entrega ou de qualquer providência.

A versão mais atualizada e verificada desta skill é mantida em [openaccountants.com](https://openaccountants.com). Faça login para acessar a versão mais recente, solicitar revisão por contador habilitado e acompanhar atualizações conforme a legislação for alterada.

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
