---
name: portugal-crypto-tax
description: "Utilize esta skill sempre que for solicitada informação sobre a tributação de criptomoedas ou ativos digitais em Portugal. Acione-a perante expressões como \"imposto cripto Portugal\", \"Bitcoin Portugal\", \"criptoativos IRS\", \"mais-valias cripto Portugal\", \"rendimentos cripto Portugal\", \"staking Portugal\", \"rendimentos de mineração Portugal\", \"imposto NFT Portugal\", \"Modelo 3 cripto\", \"Anexo G cripto\", \"Anexo G1 cripto\", \"365 dias cripto Portugal\", \"Autoridade Tributária cripto\", \"imposto Binance Portugal\", \"imposto Coinbase Portugal\", \"DeFi Portugal\", ou qualquer questão sobre IRS, mais-valias ou IVA aplicável a criptomoedas, tokens ou ativos digitais para residentes fiscais portugueses ou rendimentos cripto de fonte portuguesa. Abrange a exclusão dos 365 dias, taxa de 28% para curto prazo, Categoria B (mineração/trading profissional), exclusão de NFT, método FIFO e reporte DAC8. Trigger also on: \"crypto tax Portugal\", \"Bitcoin Portugal\", \"cryptocurrency gains Portugal\", \"crypto income Portugal\", \"staking Portugal\", \"mining income Portugal\", \"NFT tax Portugal\", \"Modelo 3 crypto\", \"Anexo G crypto\", \"Anexo G1 crypto\", \"365 days crypto Portugal\", \"Autoridade Tributária crypto\", \"Binance Portugal tax\", \"Coinbase Portugal tax\", \"DeFi tax Portugal\". LEIA SEMPRE esta skill antes de tratar qualquer questão de criptoativos em Portugal."
version: 1.0
jurisdiction: PT
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Mário Jorge da costa Vale
review_status: current
depends_on: - portugal-income-tax
category: crypto
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Portugal Crypto Tax

## Portugal — Tributação de Criptoativos — Skill v1.1

## Verified rates & thresholds (accountant-reviewed)

- **Verified block note** — Reviewed against the cited tax authorities by Mário Jorge da costa Vale on 2026-06-04. Items flagged for further clarification are tracked separately and excluded here. This block is generated from verified skill_facts — edit the facts, not the prose.

### Cripto

- **Detido < 365 dias** — 28% taxa autónoma (ou englobamento)  _(CIRS Art. 10.º)_
- **Detido ≥ 365 dias** — ISENTO de IRS  _(CIRS Art. 10.º n.º 17)_
- **Cripto-para-cripto (swap)** — NÃO é evento tributável  _(CIRS)_
- **Taxa autónoma padrão** — 28%  _(CIRS Art. 72.º)_
- **Jurisdição na lista negra** — 35%  _(Portaria 150/2004)_
- **Englobamento** — 12,5% a 48% (progressivo)  _(CIRS Art. 22.º e 68º)_
- **Recebidos em fiat** — 28% no ano de recebimento  _(CIRS Cat. E)_
- **Recebidos em cripto** — Não tributável até conversão em fiat  _(CIRS Cat. E)_
- **Mineração habitual** — Cat. B — taxas progressivas  _(CIRS Cat. B)_
- **Método obrigatório** — FIFO  _(CIRS Art. 44.º/48.º)_
- **Regime simplificado** — Coeficiente 0,95 (campo 422 Anexo B)  _(CIRS Art. 31.º)_

## Secção 1 — Referência Rápida

**Referência Rápida**

| Campo | Valor |
| --- | --- |
| País | Portugal (República Portuguesa) |
| Imposto | IRS — Imposto sobre o Rendimento das Pessoas Singulares |
| Moeda | EUR (todos os valores devem ser expressos em EUR à data da operação) |
| Ano fiscal | Ano civil (1 de janeiro – 31 de dezembro) |
| Autoridade primária | Código do IRS (CIRS), artigos 10.º, 12.º-A, 28.º, 31.º, 72.º; Lei n.º 24-D/2022 (Orçamento do Estado 2023) — disposições sobre criptoativos |
| Reforma central | A Lei 24-D/2022 (OE 2023) introduziu a tributação de criptoativos a partir de 1 de janeiro de 2023 — antes desta data, os ganhos cripto para pessoas singulares NÃO eram tributáveis |
| Autoridade fiscal | Autoridade Tributária e Aduaneira (AT) |
| Portal de submissão | Portal das Finanças (portaldasfinancas.gov.pt) |
| Prazo de entrega | 1 de abril – 30 de junho do ano seguinte |
| Reporte UE | DAC8 — plataformas cripto reportam a partir de 2026; plataformas registadas em Portugal já reportam desde 2024 (até 31 de janeiro anualmente) |
| Validado por | Verificado por Mário Jorge da costa Vale (CA - 85883) em 2026-06-04 |
| Versão da skill | 1.1 |

### A Exclusão dos 365 Dias — A Regra Central de Portugal

**A Exclusão dos 365 Dias**

| Período de Detenção | Tratamento Fiscal |
| --- | --- |
| **< 365 dias** | Tributado à **taxa autónoma de 28%** com opção de englobamento (taxas progressivas) |
| **≥ 365 dias** | **ISENTO de IRS** — mas tem de ser declarado no Anexo G1 |

Esta exclusão aplica-se a criptoativos que NÃO sejam qualificados como valores mobiliários. Não se aplica a traders profissionais (Categoria B).

### Classificação de Criptoativos em sede de IRS

**Classificação de Criptoativos em sede de IRS**

| Atividade | Categoria de IRS | Tratamento Fiscal |
| --- | --- | --- |
| Mais-valias em cripto detido < 365 dias | Categoria G (Mais-valias) | 28% autónoma ou taxas progressivas (englobamento) |
| Mais-valias em cripto detido ≥ 365 dias | Categoria G — isento | 0% (mas declaração obrigatória no Anexo G1) |
| Recompensas de staking / lending / yield farming | Categoria E (Rendimentos de capitais) | 28% autónoma ou taxas progressivas (englobamento) |
| Mineração / emissão de criptoativos | Categoria B (Rendimentos empresariais e profissionais) | Taxas progressivas 14,5%–53% |
| Trading habitual/profissional de cripto | Categoria B | Taxas progressivas 14,5%–53% |
| Permuta cripto-por-cripto | NÃO é facto tributário | O valor de aquisição transita para o novo ativo |
| Rendimentos de NFT | Excluídos do regime de criptoativos | Ver Secção 6 |

### Pressupostos Conservadores

**Pressupostos Conservadores**

| Ambiguidade | Pressuposto |
| --- | --- |
| Período de detenção desconhecido | Tratar como < 365 dias (tributável a 28%) |
| Desconhece-se se a atividade é ocasional ou habitual | Tratar como ocasional (Categoria G/E), salvo indicadores claros de atividade empresarial |
| Valor de aquisição desconhecido | PARAR — não é possível apurar mais-valia sem custo de aquisição |
| Estatuto de residência desconhecido | PARAR — afeta tributação mundial vs. fonte |
| Recompensa de staking: passiva ou empresarial? | Tratar como Categoria E (passivo — 28%) |
| Cripto recebida como contrapartida por trabalho | Categoria A (trabalho dependente) ou Categoria B (trabalho independente) — não Categoria G |

## Secção 2 — Inputs Necessários e Catálogo de Recusas

### Inputs Necessários

- **Mínimo viável** — histórico de operações da(s) exchange(s) ou carteira(s), confirmação da residência fiscal em Portugal, períodos de detenção para todas as alienações e indicação se a atividade é ocasional ou profissional.
- **Recomendado** — exportações CSV completas de todas as exchanges utilizadas (Binance, Coinbase, Kraken, Revolut, etc.), endereços de carteiras com histórico on-chain, datas e custos de aquisição de cada posição, registo de atividade de staking/lending/mineração, e estatuto RNH/IFICI quando aplicável.
- **Ideal** — exportação completa de tracker de portefólio (ex.: CoinTracking, Koinly), histórico de interações com protocolos DeFi com datas, documentação de todos os períodos de detenção (prova da data de aquisição) e registos de eventuais airdrops de tokens.

### Catálogo de Recusas

- **R-PTC-1 — Residência desconhecida** — Os residentes fiscais em Portugal são tributados em IRS sobre o rendimento mundial. Os não residentes apenas são tributados sobre rendimento de fonte portuguesa. Não é possível avançar sem confirmar o estatuto de residência fiscal.
- **R-PTC-2 — Sem registos de operações ou prova de período de detenção** — A exclusão dos 365 dias é o benefício mais valioso da tributação cripto em Portugal. Sem prova das datas de aquisição, a AT pode recusar a exclusão. Não é possível avançar sem registos completos.
- **R-PTC-3 — Detenção de criptoativos por pessoa coletiva** — As sociedades que detêm criptoativos estão sujeitas a IRC (Imposto sobre o Rendimento das Pessoas Coletivas) com regras distintas. Esta skill cobre apenas pessoas singulares (IRS). Escalar para contabilista certificado.
- **R-PTC-4 — Disputas sobre classificação na Categoria B** — Saber se a atividade cripto constitui atividade profissional/empresarial (Categoria B) depende da regularidade, volume e intenção. A Categoria B sobrepõe-se às Categorias G e E. Escalar para profissional qualificado.
- **R-PTC-5 — Tokens valores mobiliários** — Criptoativos qualificáveis como valores mobiliários têm tratamento fiscal distinto e não beneficiam da exclusão dos 365 dias. Escalar para classificação.

## Secção 3 — Tabelas de Taxas

### 3.1 Categoria G — Mais-valias (Curto Prazo, < 365 Dias)

**Opções de taxa Categoria G**

| Opção | Taxa | Quando é Vantajosa |
| --- | --- | --- |
| Taxa autónoma | **28%** | Por defeito — vantajosa quando o rendimento total ficaria num escalão marginal > 28% |
| Taxa autónoma (jurisdição constante da lista) | **35%** | Se a contraparte estiver em jurisdição de tributação privilegiada (Portaria 150/2004) |
| Englobamento (agregação com taxas progressivas) | **14,5%–53%** | Vantajoso quando o rendimento total anual (incluindo mais-valias cripto) < ~€23.000 |

**Taxas Progressivas de IRS 2025 (para englobamento)**

| Rendimento Coletável | Taxa |
| --- | --- |
| Até €7.703 | 14,5% |
| €7.704 – €11.623 | 21% |
| €11.624 – €16.472 | 26,5% |
| €16.473 – €21.321 | 28,5% |
| €21.322 – €27.146 | 35% |
| €27.147 – €39.791 | 37% |
| €39.792 – €51.997 | 43,5% |
| €51.998 – €81.199 | 45% |
| Superior a €81.199 | 48% (+ sobretaxa de solidariedade de 2,5% > €80.000 e 5% > €250.000 = efetiva até 53%) |

- **Citação** — Código do IRS, artigo 72.º, n.º 1, alínea d) (taxa de 28%); artigo 68.º (taxas progressivas); Lei n.º 24-D/2022 (disposições do OE 2023 sobre cripto).  _(Código do IRS, artigo 72.º, n.º 1, alínea d); artigo 68.º; Lei n.º 24-D/2022)_

### 3.2 Categoria E — Rendimentos de Capitais (Staking, Lending)

**Categoria E — Cenários e Taxas**

| Cenário | Taxa |
| --- | --- |
| Recompensas de staking / lending (pagas em fiat ou convertidas para fiat) | 28% (taxa liberatória ou taxa especial) |
| Recompensas de staking / lending (recebidas em cripto, ainda não convertidas) | **Não imediatamente tributáveis** — tributadas a 28% no momento da conversão para fiat |
| Rendimento proveniente de jurisdição de tributação privilegiada | 35% |
| Opção pelo englobamento | Disponível — as taxas progressivas podem ser mais favoráveis |

- **Nuance crítica** — Quando as recompensas de staking são recebidas na mesma cripto (ex.: staking de SOL com recompensas em SOL), não há tributação imediata. A tributação ocorre apenas quando as recompensas são convertidas para moeda fiat ou utilizadas em compras. Esta leitura é confirmada pela interpretação da Belim Tax Law Office das disposições do CIRS e pela orientação da AT.
- **Citação** — CIRS artigo 5.º (rendimentos de capitais); artigo 71.º, n.º 1 (taxa liberatória 28%); artigo 72.º, n.º 1, alínea d) (taxa especial 28%).  _(CIRS artigo 5.º; artigo 71.º, n.º 1; artigo 72.º, n.º 1, alínea d))_

### 3.3 Categoria B — Rendimentos Empresariais (Mineração, Trading Profissional)

**Categoria B — Regimes**

| Regime | Base Tributável | Taxa |
| --- | --- | --- |
| Regime simplificado (volume de negócios < €200.000) | 15% da receita bruta cripto é tratada como rendimento tributável (coeficiente 0,15 para vendas; 0,95 para serviços) | Taxas progressivas sobre o rendimento presumido |
| Regime simplificado — mineração em específico | Campo 422 do Quadro 4-A do Anexo B | Taxas progressivas |
| Contabilidade organizada | Lucro real = receita − despesas documentadas | Taxas progressivas 14,5%–53% |

- **Nota** — No regime simplificado, apenas 15% das receitas de vendas de cripto é considerada tributável (dedução automática de 85%), o que resulta numa taxa efetiva muito baixa. Esta regra aplica-se, contudo, apenas a atividades genuinamente enquadráveis na Categoria B. Especificamente para mineração, o coeficiente é de 0,95 (campo 422), ou seja, 95% é tributável.
- **Citação** — CIRS artigo 31.º (coeficientes do regime simplificado); artigo 28.º (âmbito da Categoria B).  _(CIRS artigo 31.º; artigo 28.º)_

## Secção 4 — Métodos de Custo de Aquisição

### 4.1 FIFO — Obrigatório

**Métodos de custo de aquisição — estatuto**

| Método | Estatuto |
| --- | --- |
| FIFO (First In, First Out) | **Obrigatório** — exigido pelos artigos 44.º e 48.º do CIRS para apuramento do valor de aquisição |
| LIFO | Não permitido |
| Custo médio | Não permitido |
| Identificação específica | Não permitido |

### 4.2 Componentes do Valor de Aquisição

- **Valor de aquisição inclui** — Preço de compra em EUR (convertido à taxa de câmbio da data de aquisição); Comissões e encargos da exchange na aquisição; Taxas de rede/gas diretamente imputáveis à aquisição
- **Valor de realização inclui** — Receita de venda em EUR (ou valor de mercado se a alienação for por contrapartida não-fiat)  _(artigo 44.º do CIRS)_
- **Despesas dedutíveis** — Despesas e encargos necessários efetivamente suportados na aquisição e na alienação do criptoativo

### 4.3 Permutas Cripto-por-Cripto — NÃO Tributáveis

- **Permutas cripto-por-cripto** — Esta é uma diferença fundamental em relação à maioria das jurisdições da UE. Ao trocar uma cripto por outra (ex.: BTC → ETH): Não há facto tributário; O valor de aquisição do ativo original transita para o novo ativo; O período de detenção para efeitos da exclusão dos 365 dias reinicia-se na data da permuta (interpretação conservadora — a AT não emitiu orientação definitiva sobre a continuidade do período de detenção em permutas); O imposto só é desencadeado quando a cripto é definitivamente convertida para moeda fiat (EUR, USD, etc.) ou usada na aquisição de bens/serviços
- **Pressuposto conservador quanto ao período de detenção** — Tratar cada permuta como nova aquisição para efeitos dos 365 dias. Sinalizar para revisão profissional sempre que a continuidade do período de detenção seja determinante para o resultado fiscal.

## Secção 5 — DeFi, Staking, Mineração e Airdrops

### 5.1 Staking e Lending

**Staking e Lending — tipos e tratamento**

| Tipo | Categoria | Tratamento |
| --- | --- | --- |
| Recompensas de staking recebidas na mesma cripto | Categoria E | **Não imediatamente tributáveis** — tributadas a 28% apenas na conversão para fiat |
| Recompensas de staking recebidas em fiat | Categoria E | Tributáveis a 28% (ou taxas progressivas via englobamento) no ano de recebimento |
| Juros de lending recebidos em fiat | Categoria E | Tributáveis a 28% no ano de recebimento |
| Juros de lending recebidos em cripto | Categoria E | Não imediatamente tributáveis — tributados na conversão para fiat |
| Staking/validação como atividade regular | Categoria B | Taxas progressivas (sobrepõe-se à Categoria E) |

### 5.2 Mineração

**Mineração — cenários e categoria**

| Cenário | Categoria | Tratamento |
| --- | --- | --- |
| Mineração ocasional (hobby) | Provável Categoria E | 28% na conversão para fiat |
| Mineração habitual (infraestrutura dedicada) | Categoria B | Taxas progressivas 14,5%–53%, declarada no Anexo B |
| Mineração especificamente | Categoria B, campo 422 | Coeficiente 0,95 no regime simplificado |

- **Sobreposição de categorias** — A Categoria B sobrepõe-se à Categoria E quando a atividade é habitual. Nos termos do CIRS, havendo padrão profissional/empresarial estabelecido, este prevalece.

### 5.3 Airdrops

**Airdrops — tipos e tratamento**

| Tipo | Tratamento |
| --- | --- |
| Airdrop gratuito (sem ação exigida) | Não imediatamente tributável; valor de aquisição = €0; tributado na alienação |
| Airdrop em contrapartida de serviço prestado | Categoria B ou Categoria E consoante o contexto |
| Airdrop recebido por operador empresarial | Rendimento de Categoria B |

### 5.4 Protocolos DeFi

**Protocolos DeFi — atividades e tratamento**

| Atividade | Tratamento |
| --- | --- |
| Fornecer liquidez a pools DEX | Adicionar cripto ao pool — não é facto tributário (lógica cripto-por-cripto); o LP token recebido herda o valor de aquisição dos ativos depositados |
| Recompensas de yield farming em cripto | Categoria E — não imediatamente tributáveis até conversão para fiat |
| Impermanent loss | Não é facto tributário reconhecido (a perda só é reconhecida na efetiva alienação para fiat) |
| Recompensas em governance tokens | Valor de aquisição = €0 (gratuitos); tributados na alienação para fiat após análise do período de detenção |

### 5.5 Hard Forks

- **Hard Forks — tratamento conservador** — Sem orientação específica da AT. Tratamento conservador: Valor de aquisição da moeda original: inalterado; Valor de aquisição da moeda resultante do fork: €0; Período de detenção de 365 dias para a moeda resultante: inicia-se na data do fork; Tributação desencadeada na alienação para fiat

## Secção 6 — Tratamento de NFT

- **Exclusão de NFT** — Os NFT estão expressamente excluídos do regime de tributação de criptoativos em Portugal.

**Tratamento de NFT**

| Regra | Detalhe |
| --- | --- |
| Base legal | Lei n.º 24-D/2022 (OE 2023) — os NFT ("tokens não fungíveis") são classificados como ativos digitais únicos e excluídos das regras fiscais dos criptoativos |
| Mais-valias na venda de NFT | Atualmente NÃO tributáveis para pessoas singulares (inexistência de norma específica) |
| Criação e venda de NFT | Pode constituir rendimento empresarial de Categoria B se for habitual (atividade criativa/artística) |
| Royalties de NFT | Potencialmente Categoria B ou Categoria E consoante a regularidade |
| NFT como valores mobiliários | Se o NFT representar um valor mobiliário (instrumento financeiro), cai no regime dos valores mobiliários e não no regime dos criptoativos |

A exclusão dos NFT é um dos aspetos mais favoráveis da tributação cripto em Portugal. Contudo, a AT ou futura legislação podem alterar este tratamento. Monitorizar anualmente as atualizações do OE (Orçamento do Estado).

## Secção 7 — Obrigações Declarativas

### 7.1 Modelo 3 — Declaração Anual de IRS

**Modelo 3 — Anexos**

| Anexo | Conteúdo | Quando Usar |
| --- | --- | --- |
| **Anexo G** (Quadro 18) | Mais-valias tributáveis — cripto detido < 365 dias | Quando alienou cripto detido < 365 dias com ganho (ou perda) |
| **Anexo G** (Quadro 18A) | Mais-valias em que a contraparte se situa em jurisdição extra-UE/EEE sem convenção fiscal | Situações específicas de contraparte estrangeira |
| **Anexo G1** (Quadro 7) | Mais-valias isentas — cripto detido ≥ 365 dias | **Obrigatório ainda que isento** — tem de ser declarado para efeitos de controlo pela AT |
| **Anexo E** | Rendimentos de capitais da Categoria E (staking, lending) | Quando recompensas de staking/lending foram recebidas ou convertidas para fiat |
| **Anexo B** (Quadro 4-A) | Rendimentos empresariais da Categoria B (mineração, trading profissional) | Campo 419: trading/serviços cripto; campo 422: mineração |
| **Anexo B** (Quadro 13G) | Informação suplementar sobre atividade cripto | Obrigatório quando se entrega Anexo B para atividade cripto |

### 7.2 Detalhes de Submissão

**Detalhes de Submissão**

| Item | Detalhe |
| --- | --- |
| Prazo de entrega | 1 de abril – 30 de junho do ano seguinte |
| Prazo de pagamento | 31 de agosto do ano seguinte |
| Plataforma | Portal das Finanças (portaldasfinancas.gov.pt) |
| Declaração obrigatória | Mesmo que os ganhos sejam isentos (≥ 365 dias), devem ser declarados no Anexo G1 |

### 7.3 Reporte por Exchanges

- **Reporte por Exchanges** — Os prestadores de serviços de criptoativos registados em Portugal estão obrigados a reportar à AT todas as operações dos clientes até 31 de janeiro do ano seguinte. A DAC8 alargará este reporte a plataformas em toda a UE a partir de 2026.

### 7.4 Conservação de Registos

**Conservação de Registos**

| Exigência | Detalhe |
| --- | --- |
| Período de conservação | 4 anos a contar do final do ano fiscal relevante (artigo 128.º do CIRS) — alargado para 12 anos se a AT abrir investigação |
| Registos a manter | Logs de operações com datas (crítico para prova dos 365 dias), registos do valor de aquisição, livro FIFO, logs de staking/mineração, endereços de carteiras |
| Prova do período de detenção | **Essencial** — a documentação da data de aquisição é o registo mais importante para invocar a exclusão dos 365 dias |
| Formato | Exportações CSV das exchanges, registos de blockchain explorers, dados de trackers de portefólio |

## Secção 8 — Compensação de Perdas e Reporte

### 8.1 Perdas da Categoria G (Curto Prazo)

**Perdas Categoria G**

| Regra | Detalhe |
| --- | --- |
| Compensação no mesmo ano | Menos-valias cripto (< 365 dias) podem compensar mais-valias cripto (< 365 dias) dentro da Categoria G |
| Compensação entre categorias | As perdas da Categoria G NÃO podem compensar rendimentos das Categorias E ou B |
| Reporte para anos seguintes | As menos-valias da Categoria G podem ser reportadas durante **5 anos** (artigo 55.º do CIRS) |
| Exigência de englobamento | Para reportar perdas é OBRIGATÓRIO optar pelo englobamento no ano da perda e nos anos subsequentes |

### 8.2 Perdas da Categoria E

- **Perdas Categoria E** — Os rendimentos da Categoria E (staking/lending) não geram perdas no sentido tradicional — são tributados no momento do recebimento. Não existe reporte de perdas.

### 8.3 Perdas da Categoria B

**Perdas Categoria B**

| Regra | Detalhe |
| --- | --- |
| Compensação no mesmo ano | As perdas da Categoria B podem compensar rendimentos da Categoria B |
| Reporte para anos seguintes | **12 anos** nos termos do artigo 55.º, n.º 1, alínea a), do CIRS |
| Compensação entre categorias | Não podem compensar outras categorias |

### 8.4 Limitação por Jurisdições de Tributação Privilegiada

- **Limitação por jurisdição privilegiada** — Se a contraparte se situar em jurisdição de tributação privilegiada (Portaria 150/2004), a taxa é de 35% e as regras de compensação de perdas podem ser restringidas.  _(Portaria 150/2004)_

## Secção 9 — Normas Antiabuso

### 9.1 Cláusula Geral Antiabuso

- **Cláusula geral antiabuso** — O artigo 38.º, n.º 2, da Lei Geral Tributária (LGT) consagra uma cláusula geral antiabuso. A AT pode desconsiderar montagens que sejam: Total ou parcialmente artificiais; Estruturadas com a finalidade essencial de obter vantagem fiscal; Contrárias à finalidade da legislação  _(artigo 38.º, n.º 2, da LGT)_

### 9.2 Normas Antiabuso Específicas Para Cripto

**Normas Antiabuso Específicas Para Cripto**

| Medida | Detalhe |
| --- | --- |
| Tributação à saída | Quando se perde a residência fiscal portuguesa, os ganhos cripto não realizados consideram-se alienados ao valor de mercado à data da saída — potencialmente tributáveis (artigo 10.º, n.º 22, do CIRS) |
| Agravamento por paraísos fiscais | Rendimentos provenientes de / transações com entidades em jurisdições de tributação privilegiada: taxa de 35% (artigo 72.º, n.º 17, do CIRS) |
| Preços de transferência | Operações entre partes relacionadas valorizadas em condições de plena concorrência (artigo 43.º, n.º 9, do CIRS, por remissão para o artigo 63.º, n.º 4, do CIRC) |
| Reporte por exchanges | As plataformas portuguesas reportam dados de clientes à AT desde 2024; DAC8 a partir de 2026 |
| Coimas | Falta de declaração: coimas de €375 a €22.500 (consoante a intenção e o montante); fraude fiscal: responsabilidade criminal |

### 9.3 Regimes RNH / IFICI e Cripto

- **RNH/IFICI e cripto** — Para tratamento RNH/IFICI dos rendimentos cripto estrangeiros ver skill pt-nhr-ifici.

## Secção 10 — Exemplos Práticos

### Exemplo 1 — Ganho de Curto Prazo (< 365 Dias)

**Input:** Residente fiscal em Portugal. Comprou 2 BTC a €30.000 cada em 1 de março de 2025. Vendeu 2 BTC a €50.000 cada em 1 de novembro de 2025 (8 meses de detenção — < 365 dias). Comissões de exchange: €200 totais na aquisição, €300 na alienação. Rendimento anual de trabalho dependente: €40.000.

**Cálculo:**
```
Valor de realização:   2 × €50.000 = €100.000
Menos comissões:                    −€300
Realização líquida:                  €99.700

Custo de aquisição:    2 × €30.000 = €60.000
Mais comissões aq.:                 +€200
Custo total:                         €60.200

Mais-valia:            €99.700 − €60.200 = €39.500

Opção A — Taxa autónoma de 28%:
  €39.500 × 28% = €11.060

Opção B — Englobamento:
  Rendimento total: €40.000 (salário) + €39.500 (cripto) = €79.500
  Taxa marginal a €79.500 ≈ 45%
  Englobamento é MAIS caro → Escolher taxa autónoma.

Imposto: €11.060 (taxa autónoma preferida)
Declarado em: Anexo G, Quadro 18
```

### Exemplo 2 — Ganho de Longo Prazo (≥ 365 Dias) — Isento

**Input:** Residente fiscal em Portugal. Comprou 5 ETH a €1.500 cada em 15 de janeiro de 2024. Vendeu 5 ETH a €4.000 cada em 20 de fevereiro de 2025 (401 dias de detenção — ≥ 365 dias). Comissões de exchange: €100 totais.

**Cálculo:**
```
Mais-valia:  (5 × €4.000) − (5 × €1.500) − €100 = €12.400

Período de detenção: 401 dias ≥ 365 → ISENTO

Imposto: €0
Declarado em: Anexo G1, Quadro 7 (declaração obrigatória
  ainda que isento)
```

### Exemplo 3 — Recompensas de Staking (Categoria E)

**Input:** Residente fiscal em Portugal. Fez staking de SOL numa exchange registada em Portugal ao longo de 2025. Recebeu 50 SOL em recompensas de staking. 30 SOL foram convertidos para EUR a €150 cada (= €4.500). 20 SOL permanecem na carteira de staking (não convertidos).

**Cálculo:**
```
Porção convertida:   30 SOL × €150 = €4.500
  Imposto: €4.500 × 28% = €1.260 (taxa liberatória,
  retida pela exchange portuguesa)

Porção não convertida: 20 SOL — NÃO imediatamente tributável
  (recompensas recebidas na mesma cripto, ainda não convertidas para fiat)
  Valor de aquisição destes 20 SOL = €0 para futura alienação
  Período de detenção de 365 dias inicia-se na data de receção

Imposto total para 2025: €1.260
Declarado em: Anexo E (para a porção convertida)
```

## Auto-verificações

Antes de entregar qualquer cálculo de imposto cripto em Portugal, confirmar:

- [ ] Residência confirmada — residente fiscal em Portugal (mundial) ou não residente?
- [ ] Período de detenção calculado para cada alienação — é ≥ ou < 365 dias?
- [ ] FIFO aplicado por tipo de moeda em todas as exchanges e carteiras
- [ ] Permutas cripto-por-cripto tratadas como não tributáveis (valor de aquisição transita)
- [ ] NFT corretamente excluídos do regime de criptoativos
- [ ] Recompensas de staking em cripto: não imediatamente tributáveis (apenas na conversão para fiat)
- [ ] Indicadores de Categoria B avaliados — atividade ocasional ou profissional?
- [ ] Comparação englobamento vs. taxa autónoma efetuada
- [ ] Mais-valias isentas (≥ 365 dias) ainda assim declaradas no Anexo G1
- [ ] Estatuto RNH/IFICI verificado — habitualmente irrelevante para cripto (ver skill pt-nhr-ifici)
- [ ] Risco de contraparte em jurisdição de tributação privilegiada avaliado (taxa de 35%)
- [ ] Output marcado como estimativa — sinalizado para revisão profissional

## PROIBIÇÕES

- NUNCA assumir que Portugal continua a ser um paraíso fiscal cripto — os ganhos são tributáveis desde 1 de janeiro de 2023
- NUNCA aplicar imposto a cripto detida há ≥ 365 dias (salvo trading profissional ou tokens valores mobiliários)
- NUNCA tratar permutas cripto-por-cripto como facto tributário — NÃO são tributáveis em Portugal
- NUNCA esquecer de declarar ganhos isentos no Anexo G1 — a omissão pode gerar coimas
- NUNCA assumir que recompensas de staking em cripto são imediatamente tributáveis — só são tributadas na conversão para fiat
- NUNCA classificar rendimentos de NFT no regime de criptoativos — os NFT estão expressamente excluídos
- NUNCA ignorar a questão do reinício do período de detenção em permutas cripto-por-cripto — usar o pressuposto conservador
- NUNCA apresentar posições fiscais cripto como definitivas — etiquetar sempre como estimativa e sinalizar para revisão profissional
- NUNCA ignorar o risco de tributação à saída para pessoas singulares que percam a residência fiscal portuguesa
- NUNCA calcular mais-valias sem datas de aquisição verificadas — a exclusão dos 365 dias depende de período de detenção comprovável

## Aviso Legal

Esta skill e os seus outputs são disponibilizados apenas para fins informativos e de cálculo, não constituindo aconselhamento fiscal, jurídico ou financeiro. A Open Accountants e os seus contribuidores declinam qualquer responsabilidade por erros, omissões ou consequências decorrentes do uso desta skill. Todos os outputs devem ser revistos e validados por profissional qualificado (contabilista certificado, advogado tributarista ou revisor oficial de contas em Portugal) antes da submissão ou de qualquer atuação com base nos mesmos.

A versão mais atualizada e verificada desta skill é mantida em [openaccountants.com](https://openaccountants.com). Inicie sessão para aceder à versão mais recente, solicitar revisão profissional por contabilista licenciado e acompanhar atualizações à medida que a legislação fiscal evolui.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — no liability on either side until you and the accountant sign
a formal engagement letter — book a free 30-minute call:

→ [Book a call](https://calendly.com/openaccountants-info/30min)

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
