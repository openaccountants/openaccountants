---
name: portugal-crypto-tax
description: "Utilize esta skill sempre que for solicitada informação sobre a tributação de criptomoedas ou ativos digitais em Portugal. Acione-a perante expressões como \"imposto cripto Portugal\", \"Bitcoin Portugal\", \"criptoativos IRS\", \"mais-valias cripto Portugal\", \"rendimentos cripto Portugal\", \"staking Portugal\", \"rendimentos de mineração Portugal\", \"imposto NFT Portugal\", \"Modelo 3 cripto\", \"Anexo G cripto\", \"Anexo G1 cripto\", \"365 dias cripto Portugal\", \"Autoridade Tributária cripto\", \"imposto Binance Portugal\", \"imposto Coinbase Portugal\", \"DeFi Portugal\", ou qualquer questão sobre IRS, mais-valias ou IVA aplicável a criptomoedas, tokens ou ativos digitais para residentes fiscais portugueses ou rendimentos cripto de fonte portuguesa. Abrange a exclusão dos 365 dias, taxa de 28% para curto prazo, Categoria B (mineração/trading profissional), exclusão de NFT, método FIFO e reporte DAC8. Trigger also on: \"crypto tax Portugal\", \"Bitcoin Portugal\", \"cryptocurrency gains Portugal\", \"crypto income Portugal\", \"staking Portugal\", \"mining income Portugal\", \"NFT tax Portugal\", \"Modelo 3 crypto\", \"Anexo G crypto\", \"Anexo G1 crypto\", \"365 days crypto Portugal\", \"Autoridade Tributária crypto\", \"Binance Portugal tax\", \"Coinbase Portugal tax\", \"DeFi tax Portugal\". LEIA SEMPRE esta skill antes de tratar qualquer questão de criptoativos em Portugal."
version: 1.0
jurisdiction: PT
tax_year: 2026
last_updated: 2026-10-23
reviewed_by: A licensed accountant (name withheld at their request)
review_status: current
trust_label: Checked by a licensed accountant (name withheld at their request)
depends_on:
  - portugal-income-tax
category: crypto
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Portugal Crypto Tax

## Portugal — Tributação de Criptoativos — Skill v1.1

## Verified rates & thresholds (accountant-reviewed)

- **Verified block note** — Reviewed against the cited tax authorities by Mário Jorge da costa Vale on 2026-06-04. Items flagged for further clarification are tracked separately and excluded here. This block is generated from verified skill_facts — edit the facts, not the prose.
- **2026 update (2026-10-23)**: Article numbers and rates below were brought to tax year 2026 from the AT pages listed under Sources. Decreto-Lei n.º 97/2026, de 20 de maio, renumbered CIRS art. 10.º: the 365-day exclusion is now n.º 22 (was n.º 19), crypto-for-crypto deferral n.º 23 (was 20), the non-cooperative-jurisdiction carve-out n.º 24 (was 21) and the exit rule n.º 25 (was 22). The rules themselves did not change. These 2026 corrections were not part of the 2026-06-04 review.

### Cripto

- **Detido < 365 dias** — 28% taxa autónoma (ou englobamento)  _(CIRS Art. 10.º)_
- **Detido ≥ 365 dias** — Excluído de IRS (ganhos e perdas)  _(CIRS Art. 10.º n.º 22, na redação do DL 97/2026; antes n.º 19)_
- **Cripto-para-cripto (swap)** — NÃO é evento tributável; o valor de aquisição transita  _(CIRS Art. 10.º n.º 23)_
- **Taxa autónoma padrão** — 28%  _(CIRS Art. 72.º n.º 1 c))_
- **Contraparte fora da UE/EEE sem convenção ou troca de informações**: não se aplicam a exclusão dos 365 dias nem o diferimento das permutas; perdas com contraparte em regime fiscal privilegiado não relevam  _(CIRS Art. 10.º n.º 24; Art. 43.º n.º 7)_
- **Englobamento** — 12,5% a 48% (progressivo, tabela 2026) + adicional de solidariedade 2,5% / 5%  _(CIRS Art. 22.º, 68.º e 68.º-A)_
- **Recebidos em fiat** — 28% no ano de recebimento  _(CIRS Cat. E)_
- **Recebidos em cripto** — Tributados como mais-valia na alienação dos criptoativos recebidos  _(CIRS Art. 5.º n.º 11)_
- **Perda de residência**: equiparada a alienação onerosa, ao valor de mercado  _(CIRS Art. 10.º n.º 25; Art. 43.º n.º 12)_
- **Mineração habitual** — Cat. B — taxas progressivas  _(CIRS Cat. B)_
- **Método obrigatório** — FIFO  _(CIRS Art. 44.º/48.º)_
- **Regime simplificado** — Coeficiente 0,15 nas operações com criptoativos; 0,95 na mineração  _(CIRS Art. 31.º n.º 1 a) e d))_

## Secção 1 — Referência Rápida

**Referência Rápida**

| Campo | Valor |
| --- | --- |
| País | Portugal (República Portuguesa) |
| Imposto | IRS — Imposto sobre o Rendimento das Pessoas Singulares |
| Moeda | EUR (todos os valores devem ser expressos em EUR à data da operação) |
| Ano fiscal | Ano civil (1 de janeiro – 31 de dezembro); esta skill está no ano fiscal 2026 |
| Autoridade primária | Código do IRS (CIRS), artigos 5.º, 10.º, 31.º, 43.º, 72.º; Lei n.º 24-D/2022 (Orçamento do Estado 2023) — disposições sobre criptoativos; Decreto-Lei n.º 97/2026, de 20 de maio — renumerou o art. 10.º (365 dias passa a n.º 22; saída passa a n.º 25) |
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

Base legal: CIRS art. 10.º n.º 22 (ganhos e perdas excluídos), na numeração do Decreto-Lei n.º 97/2026. Não se aplica quando o sujeito passivo ou a contraparte não seja residente na UE/EEE nem em Estado com convenção ou acordo de troca de informações (art. 10.º n.º 24).

Esta exclusão aplica-se a criptoativos que NÃO sejam qualificados como valores mobiliários. Não se aplica a traders profissionais (Categoria B).

### Classificação de Criptoativos em sede de IRS

**Classificação de Criptoativos em sede de IRS**

| Atividade | Categoria de IRS | Tratamento Fiscal |
| --- | --- | --- |
| Mais-valias em cripto detido < 365 dias | Categoria G (Mais-valias) | 28% autónoma ou taxas progressivas (englobamento) |
| Mais-valias em cripto detido ≥ 365 dias | Categoria G — isento | 0% (mas declaração obrigatória no Anexo G1) |
| Recompensas de staking / lending / yield farming pagas em fiat | Categoria E (Rendimentos de capitais, art. 5.º n.º 2 u)) | 28% autónoma ou taxas progressivas (englobamento) |
| Recompensas de staking / lending / yield farming recebidas em cripto | Mais-valia na alienação da cripto recebida (art. 5.º n.º 11) | 28% autónoma ou englobamento, se detida < 365 dias |
| Mineração / emissão de criptoativos | Categoria B (Rendimentos empresariais e profissionais) | Taxas progressivas 12,5%–48% (2026) + adicional de solidariedade |
| Trading habitual/profissional de cripto | Categoria B | Taxas progressivas 12,5%–48% (2026) + adicional de solidariedade |
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
| Taxa autónoma | **28%** | Por defeito — vantajosa quando o ganho ficaria a uma taxa marginal acima de 28% |
| Englobamento (agregação com taxas progressivas, opção do art. 72.º n.º 13) | **12,5%–48%** (+ adicional de solidariedade 2,5% acima de €80.000 e 5% acima de €250.000) | Vantajoso quando o rendimento coletável total, incluindo o ganho, não passa de €23.089 (taxa marginal até 24,10%) |

Não existe taxa de 35% para mais-valias de criptoativos: o art. 72.º n.º 18 não abrange a alínea k) do art. 10.º n.º 1. Com contraparte em regime fiscal privilegiado, as perdas não relevam (art. 43.º n.º 7) e, fora da UE/EEE sem convenção ou troca de informações, não há exclusão dos 365 dias nem diferimento das permutas (art. 10.º n.º 24).

**Taxas Progressivas de IRS 2026 (para englobamento)**

| Rendimento Coletável | Taxa normal | Taxa média |
| --- | --- | --- |
| Até €8.342 | 12,50% | 12,500% |
| €8.342 – €12.587 | 15,70% | 13,579% |
| €12.587 – €17.838 | 21,20% | 15,823% |
| €17.838 – €23.089 | 24,10% | 17,705% |
| €23.089 – €29.397 | 31,10% | 20,579% |
| €29.397 – €43.090 | 34,90% | 25,130% |
| €43.090 – €46.566 | 43,10% | 26,472% |
| €46.566 – €86.634 | 44,60% | 34,856% |
| Superior a €86.634 | 48,00% | — |

Adicional de solidariedade: 2,5% sobre o rendimento coletável entre €80.000 e €250.000 e 5% acima de €250.000 (art. 68.º-A). A tabela de 2026 é a da Lei n.º 73-A/2025; não usar a de 2025.

- **Citação** — Código do IRS, artigo 72.º, n.º 1, alínea c) (taxa de 28% sobre o saldo das mais-valias da alínea k) do art. 10.º n.º 1); artigo 72.º n.º 13 (opção de englobamento); artigo 68.º (taxas progressivas, redação da Lei n.º 73-A/2025).  _(Código do IRS, artigo 72.º, n.º 1, alínea c) e n.º 13; artigo 68.º)_

### 3.2 Categoria E — Rendimentos de Capitais (Staking, Lending)

**Categoria E — Cenários e Taxas**

| Cenário | Taxa |
| --- | --- |
| Recompensas de staking / lending pagas em fiat | 28% (taxa autónoma do art. 72.º n.º 1 d); estes rendimentos estão dispensados de retenção na fonte, art. 101.º-B n.º 5) |
| Recompensas de staking / lending recebidas em cripto | **Não tributadas na receção**; tributadas como mais-valia quando a cripto recebida for alienada (art. 5.º n.º 11), com a regra dos 365 dias |
| Rendimento em fiat devido por entidade em jurisdição de tributação privilegiada | 35% (art. 72.º n.º 18 a)) |
| Opção pelo englobamento | Disponível — as taxas progressivas podem ser mais favoráveis |

- **Nuance crítica** — Quando as recompensas de staking são recebidas em cripto (ex.: staking de SOL com recompensas em SOL), não há tributação na receção. O art. 5.º n.º 11 manda tributá-las como mais-valia no momento da alienação da cripto recebida. Trocar essa cripto por outra cripto também não é tributado (art. 10.º n.º 23 inclui expressamente a cripto recebida nos termos do art. 5.º n.º 11).
- **Citação** — CIRS artigo 5.º n.º 2 u) e n.º 11; artigo 72.º, n.º 1, alínea d) (taxa autónoma 28%); artigo 101.º-B n.º 5 (dispensa de retenção).  _(CIRS artigo 5.º; artigo 72.º; artigo 101.º-B)_

### 3.3 Categoria B — Rendimentos Empresariais (Mineração, Trading Profissional)

**Categoria B — Regimes**

| Regime | Base Tributável | Taxa |
| --- | --- | --- |
| Regime simplificado (rendimentos da categoria ≤ €200.000 no ano anterior) | Operações com criptoativos: coeficiente 0,15 (art. 31.º n.º 1 a)) | Taxas progressivas sobre o rendimento presumido |
| Regime simplificado — mineração | Coeficiente 0,95 (art. 31.º n.º 1 d)); campo 422 do Quadro 4-A do Anexo B | Taxas progressivas |
| Contabilidade organizada | Lucro real = receita − despesas documentadas | Taxas progressivas 12,5%–48% (2026) + adicional de solidariedade |

- **Nota** — No regime simplificado, apenas 15% das receitas de operações com cripto (exceto mineração) é considerada tributável. Esta regra aplica-se apenas a atividades genuinamente enquadráveis na Categoria B. Na mineração, o coeficiente é 0,95, ou seja, 95% é tributável. Os rendimentos de operações com cripto consideram-se obtidos na alienação onerosa (art. 31.º n.º 17), e a cessação de atividade e a perda da residência são equiparadas a alienação (art. 31.º n.º 18).
- **Citação** — CIRS artigo 31.º n.º 1 a) e d), n.º 17 e 18 (coeficientes e momento do rendimento); artigo 28.º n.º 2 (limite de €200.000).  _(CIRS artigo 31.º; artigo 28.º)_

## Secção 4 — Métodos de Custo de Aquisição

### 4.1 FIFO — Obrigatório

**Métodos de custo de aquisição — estatuto**

| Método | Estatuto |
| --- | --- |
| FIFO (First In, First Out) | **Obrigatório** — "os alienados são os adquiridos há mais tempo" (art. 43.º n.º 8 g) do CIRS), aplicado separadamente em cada prestador de serviços de criptoativos onde a cripto esteja depositada (art. 43.º n.º 9) |
| LIFO | Não permitido |
| Custo médio | Não permitido |
| Identificação específica | Não permitido |

### 4.2 Componentes do Valor de Aquisição

- **Valor de aquisição inclui** — Preço de compra em EUR (convertido à taxa de câmbio da data de aquisição); Comissões e encargos da exchange na aquisição; Taxas de rede/gas diretamente imputáveis à aquisição
- **Valor de realização inclui** — Receita de venda em EUR (ou valor de mercado se a alienação for por contrapartida não-fiat)  _(artigo 44.º do CIRS)_
- **Despesas dedutíveis** — Despesas e encargos necessários efetivamente suportados na aquisição e na alienação do criptoativo

### 4.3 Permutas Cripto-por-Cripto — NÃO Tributáveis

- **Permutas cripto-por-cripto** — Base legal: CIRS art. 10.º n.º 23 (antes n.º 20). Não se aplica fora da UE/EEE sem convenção ou troca de informações (art. 10.º n.º 24). Esta é uma diferença fundamental em relação à maioria das jurisdições da UE. Ao trocar uma cripto por outra (ex.: BTC → ETH): Não há facto tributário; O valor de aquisição do ativo original transita para o novo ativo; O período de detenção para efeitos da exclusão dos 365 dias reinicia-se na data da permuta (interpretação conservadora — a AT não emitiu orientação definitiva sobre a continuidade do período de detenção em permutas); O imposto só é desencadeado quando a cripto é definitivamente convertida para moeda fiat (EUR, USD, etc.) ou usada na aquisição de bens/serviços
- **Pressuposto conservador quanto ao período de detenção** — Tratar cada permuta como nova aquisição para efeitos dos 365 dias. Sinalizar para revisão profissional sempre que a continuidade do período de detenção seja determinante para o resultado fiscal.

## Secção 5 — DeFi, Staking, Mineração e Airdrops

### 5.1 Staking e Lending

**Staking e Lending — tipos e tratamento**

| Tipo | Categoria | Tratamento |
| --- | --- | --- |
| Recompensas de staking recebidas em cripto | Art. 5.º n.º 11 | **Não tributadas na receção**; mais-valia na alienação da cripto recebida (28% ou englobamento se < 365 dias) |
| Recompensas de staking recebidas em fiat | Categoria E | Tributáveis a 28% (ou taxas progressivas via englobamento) no ano de recebimento |
| Juros de lending recebidos em fiat | Categoria E | Tributáveis a 28% no ano de recebimento |
| Juros de lending recebidos em cripto | Art. 5.º n.º 11 | Não tributados na receção; mais-valia na alienação da cripto recebida |
| Staking/validação como atividade regular | Categoria B | Taxas progressivas (sobrepõe-se à Categoria E) |

### 5.2 Mineração

**Mineração — cenários e categoria**

| Cenário | Categoria | Tratamento |
| --- | --- | --- |
| Mineração ocasional (hobby) | Sem regra própria no CIRS lido (ver Not yet confirmed) | Tratamento a confirmar; a mineração habitual é Categoria B |
| Mineração habitual (infraestrutura dedicada) | Categoria B | Taxas progressivas 12,5%–48% (2026) + adicional de solidariedade, declarada no Anexo B |
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
| Recompensas de yield farming em cripto | Não tributadas na receção; mais-valia na alienação da cripto recebida (art. 5.º n.º 11) |
| Impermanent loss | Não é facto tributário reconhecido (a perda só é reconhecida na efetiva alienação para fiat) |
| Recompensas em governance tokens | Valor de aquisição = €0 (gratuitos); tributados na alienação para fiat após análise do período de detenção |

### 5.5 Hard Forks

- **Hard Forks — tratamento conservador** — Sem orientação específica da AT. Tratamento conservador: Valor de aquisição da moeda original: inalterado; Valor de aquisição da moeda resultante do fork: €0; Período de detenção de 365 dias para a moeda resultante: inicia-se na data do fork; Tributação desencadeada na alienação para fiat

## Secção 6 — Tratamento de NFT

- **Exclusão de NFT** — Os NFT estão expressamente excluídos do regime de tributação de criptoativos em Portugal.

**Tratamento de NFT**

| Regra | Detalhe |
| --- | --- |
| Base legal | CIRS art. 10.º n.º 21 (antes n.º 18); Lei n.º 24-D/2022 (OE 2023) — os NFT ("tokens não fungíveis") são classificados como ativos digitais únicos e excluídos das regras fiscais dos criptoativos |
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
| **Anexo E** | Rendimentos de capitais da Categoria E (staking, lending) pagos em fiat | Quando recompensas de staking/lending foram pagas em fiat (as recebidas em cripto vão ao Anexo G quando alienadas) |
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

- **Limitação por jurisdição privilegiada** — Se a contraparte estiver sujeita a regime fiscal privilegiado (art. 63.º-D da LGT), as perdas não relevam no saldo (art. 43.º n.º 7). Não há taxa de 35% para mais-valias de cripto.  _(CIRS art. 43.º n.º 7; art. 72.º n.º 18)_

## Secção 9 — Normas Antiabuso

### 9.1 Cláusula Geral Antiabuso

- **Cláusula geral antiabuso** — O artigo 38.º, n.º 2, da Lei Geral Tributária (LGT) consagra uma cláusula geral antiabuso. A AT pode desconsiderar montagens que sejam: Total ou parcialmente artificiais; Estruturadas com a finalidade essencial de obter vantagem fiscal; Contrárias à finalidade da legislação  _(artigo 38.º, n.º 2, da LGT)_

### 9.2 Normas Antiabuso Específicas Para Cripto

**Normas Antiabuso Específicas Para Cripto**

| Medida | Detalhe |
| --- | --- |
| Tributação à saída | A perda da qualidade de residente é equiparada a alienação onerosa dos criptoativos (artigo 10.º, n.º 25, do CIRS, na numeração do DL 97/2026; antes n.º 22, em vigor desde 2023). O ganho é o valor de mercado à data da perda de residência menos o valor de aquisição e as despesas da aquisição (artigo 43.º, n.º 12). Cripto detida há 365 dias ou mais nessa data fica excluída (artigo 10.º, n.º 22); a restante paga 28% ou englobamento. Na Categoria B, a perda de residência também é equiparada a alienação (artigo 31.º, n.º 18 b)). Ver Exemplo 4 |
| Paraísos fiscais | Perdas apuradas com contraparte sujeita a regime fiscal privilegiado não relevam (artigo 43.º, n.º 7). Fora da UE/EEE sem convenção ou troca de informações não há exclusão dos 365 dias nem diferimento de permutas (artigo 10.º, n.º 24). A taxa de 35% do artigo 72.º, n.º 18 não se aplica às mais-valias de cripto; aplica-se a rendimentos de capitais em fiat devidos por entidades nessas jurisdições |
| Preços de transferência | Operações entre partes relacionadas valorizadas em condições de plena concorrência (artigo 43.º, n.º 11, do CIRS, por remissão para o artigo 63.º, n.º 4, do CIRC) |
| Reporte por exchanges | As plataformas portuguesas reportam dados de clientes à AT desde 2024; DAC8 a partir de 2026 |
| Coimas | Falta de declaração: coimas de €375 a €22.500 (consoante a intenção e o montante); fraude fiscal: responsabilidade criminal |

### 9.3 Regimes RNH / IFICI e Cripto

- **RNH/IFICI e cripto** — Para tratamento RNH/IFICI dos rendimentos cripto estrangeiros ver skill pt-nhr-ifici.

## Secção 10 — Exemplos Práticos

### Exemplo 1 — Ganho de Curto Prazo (< 365 Dias)

**Input:** Residente fiscal em Portugal. Comprou 2 BTC a €30.000 cada em 1 de fevereiro de 2026. Vendeu 2 BTC a €50.000 cada em 1 de outubro de 2026 (8 meses de detenção — < 365 dias). Comissões de exchange: €200 totais na aquisição, €300 na alienação. Rendimento anual de trabalho dependente: €40.000 (segurança social 11% = €4.400). Sem outros rendimentos.

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

Opção B — Englobamento (tabela 2026):
  Salário: €40.000 − dedução específica €4.587,09 (8,54 × IAS; acima da SS de €4.400)
    = €35.412,91 coletável
  Imposto só sobre o salário: 29.397 × 20,579% + (35.412,91 − 29.397) × 34,90% = €8.149,16
  Com o ganho: €35.412,91 + €39.500 = €74.912,91 coletável
  Imposto: 46.566 × 26,472% + (74.912,91 − 46.566) × 44,60% = €24.969,67
  Imposto adicional por englobar: €24.969,67 − €8.149,16 = €16.820,51
  (sem adicional de solidariedade: €74.912,91 < €80.000)
  Englobamento é MAIS caro → Escolher taxa autónoma.

Imposto sobre o ganho: €11.060 (taxa autónoma preferida)
Declarado em: Anexo G, Quadro 18
```

```oa-check
name: PT crypto gain held under 365 days, 28% vs aggregation (2026)
inputs:
  proceeds: 100000
  sale_fees: 300
  cost: 60000
  buy_fees: 200
  salary: 40000
  ias: 537.13
steps:
  - gain: proceeds - sale_fees - (cost + buy_fees)
  - autonomous_tax: gain * 0.28
  - specific_deduction: round(max(8.54 * ias, salary * 0.11), 2)
  - cat_a: salary - specific_deduction
  - tax_salary_only: round(29397 * 0.20579 + (cat_a - 29397) * 0.349, 2)
  - aggregated: cat_a + gain
  - tax_aggregated: round(46566 * 0.26472 + (aggregated - 46566) * 0.446, 2)
  - extra_if_aggregated: tax_aggregated - tax_salary_only
expected:
  gain: 39500
  autonomous_tax: 11060
  cat_a: 35412.91
  tax_salary_only: 8149.16
  tax_aggregated: 24969.67
  extra_if_aggregated: 16820.51
```

### Exemplo 2 — Ganho de Longo Prazo (≥ 365 Dias) — Isento

**Input:** Residente fiscal em Portugal. Comprou 5 ETH a €1.500 cada em 15 de janeiro de 2025. Vendeu 5 ETH a €4.000 cada em 20 de fevereiro de 2026 (401 dias de detenção — ≥ 365 dias). Comissões de exchange: €100 totais. A exchange está na UE.

**Cálculo:**
```
Mais-valia:  (5 × €4.000) − (5 × €1.500) − €100 = €12.400

Período de detenção: 401 dias ≥ 365 → EXCLUÍDO (art. 10.º n.º 22)

Imposto: €0
Declarado em: Anexo G1, Quadro 7 (declaração obrigatória
  ainda que isento)
```

### Exemplo 3 — Recompensas de Staking (Categoria E)

**Input:** Residente fiscal em Portugal. Fez staking de SOL numa exchange da UE ao longo de 2026. Recebeu 50 SOL em recompensas de staking, pagas em SOL. 30 SOL foram vendidos por EUR a €150 cada (= €4.500) em 2026, menos de 365 dias depois de recebidos. 20 SOL permanecem na carteira (não vendidos).

**Cálculo:**
```
Receção das 50 SOL: não tributada (art. 5.º n.º 11)

Porção vendida:   30 SOL × €150 = €4.500 de valor de realização
  Tributada como mais-valia na alienação (art. 5.º n.º 11; art. 10.º n.º 1 k))
  Valor de aquisição das SOL recebidas: €0 (pressuposto conservador)
  Mais-valia: €4.500 − €0 = €4.500, detida < 365 dias
  Imposto: €4.500 × 28% = €1.260 (art. 72.º n.º 1 c)); sem retenção na fonte
  (art. 101.º-B n.º 5), pago na liquidação do IRS

Porção não vendida: 20 SOL, não tributável em 2026
  Período de detenção de 365 dias inicia-se na data de receção

Imposto total para 2026: €1.260
Declarado em: Anexo G (mais-valias de criptoativos)
```

```oa-check
name: PT staking rewards received in SOL and sold within 365 days (2026)
inputs:
  sol_sold: 30
  price: 150
  acquisition_value: 0
steps:
  - proceeds: sol_sold * price
  - gain: proceeds - acquisition_value
  - tax: gain * 0.28
expected:
  proceeds: 4500
  tax: 1260
```

### Exemplo 4: Saída de Portugal com cripto (art. 10.º n.º 25)

**Input:** Residente fiscal em Portugal até 30 de setembro de 2026, data em que deixa de ser residente. Nessa data detém: 1 BTC comprado em 1 de junho de 2026 por €60.000 mais €100 de comissão (121 dias de detenção), com valor de mercado de €70.000; e 10 ETH comprados em 1 de março de 2024 por €20.000 (mais de 365 dias), com valor de mercado de €30.000. Não vende nada. Exchange na UE.

**Cálculo:**
```
Perda de residência = alienação onerosa (art. 10.º n.º 25)
Ganho = valor de mercado à data da saída − valor de aquisição − despesas (art. 43.º n.º 12)

BTC (121 dias, < 365): €70.000 − €60.000 − €100 = €9.900
  Imposto: €9.900 × 28% = €2.772 (ou englobamento, se mais favorável)
ETH (> 365 dias): ganho €10.000 excluído (art. 10.º n.º 22)

Imposto à saída: €2.772, na declaração de 2026 (Anexo G)
```

```oa-check
name: PT crypto exit charge on loss of residence (2026)
inputs:
  btc_market_value: 70000
  btc_cost: 60000
  btc_fees: 100
  btc_days_held: 121
steps:
  - btc_gain: btc_market_value - btc_cost - btc_fees
  - btc_tax: btc_gain * 0.28
expected:
  btc_gain: 9900
  btc_tax: 2772
```

## Auto-verificações

Antes de entregar qualquer cálculo de imposto cripto em Portugal, confirmar:

- [ ] Residência confirmada — residente fiscal em Portugal (mundial) ou não residente?
- [ ] Período de detenção calculado para cada alienação — é ≥ ou < 365 dias?
- [ ] FIFO aplicado por tipo de moeda, separadamente em cada prestador onde a cripto está depositada (art. 43.º n.º 8 g) e n.º 9)
- [ ] Saída de Portugal no ano? Perda de residência = alienação ao valor de mercado (art. 10.º n.º 25; art. 43.º n.º 12)
- [ ] Permutas cripto-por-cripto tratadas como não tributáveis (valor de aquisição transita)
- [ ] NFT corretamente excluídos do regime de criptoativos
- [ ] Recompensas de staking em cripto: não tributadas na receção; mais-valia na alienação (art. 5.º n.º 11)
- [ ] Indicadores de Categoria B avaliados — atividade ocasional ou profissional?
- [ ] Comparação englobamento vs. taxa autónoma efetuada
- [ ] Mais-valias isentas (≥ 365 dias) ainda assim declaradas no Anexo G1
- [ ] Estatuto RNH/IFICI verificado — habitualmente irrelevante para cripto (ver skill pt-nhr-ifici)
- [ ] Contraparte fora da UE/EEE sem convenção ou troca de informações (art. 10.º n.º 24) ou em regime fiscal privilegiado (perdas não relevam, art. 43.º n.º 7)?
- [ ] Output marcado como estimativa — sinalizado para revisão profissional

## PROIBIÇÕES

- NUNCA assumir que Portugal continua a ser um paraíso fiscal cripto — os ganhos são tributáveis desde 1 de janeiro de 2023
- NUNCA aplicar imposto a cripto detida há ≥ 365 dias (salvo trading profissional ou tokens valores mobiliários)
- NUNCA tratar permutas cripto-por-cripto como facto tributário — NÃO são tributáveis em Portugal
- NUNCA esquecer de declarar ganhos isentos no Anexo G1 — a omissão pode gerar coimas
- NUNCA assumir que recompensas de staking em cripto são tributáveis na receção: são tributadas como mais-valia na alienação da cripto recebida (art. 5.º n.º 11)
- NUNCA classificar rendimentos de NFT no regime de criptoativos — os NFT estão expressamente excluídos
- NUNCA ignorar a questão do reinício do período de detenção em permutas cripto-por-cripto — usar o pressuposto conservador
- NUNCA apresentar posições fiscais cripto como definitivas — etiquetar sempre como estimativa e sinalizar para revisão profissional
- NUNCA ignorar a tributação à saída para pessoas singulares que percam a residência fiscal portuguesa (art. 10.º n.º 25)
- NUNCA calcular mais-valias sem datas de aquisição verificadas — a exclusão dos 365 dias depende de período de detenção comprovável

## Sources

| Source | URL | Read on |
|---|---|---|
| CIRS art. 10, crypto gains, 365-day exclusion (n.º 22), swaps (n.º 23), carve-out (n.º 24), exit (n.º 25), wording of Decreto-Lei 97/2026 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs10.aspx | 2026-10-23 |
| CIRS art. 5, crypto remuneration (n.º 2 u) and n.º 11) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs5.aspx | 2026-10-23 |
| CIRS art. 31, coefficients 0.15 and 0.95 for crypto, n.º 17 and 18 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs31.aspx | 2026-10-23 |
| CIRS art. 43, FIFO (n.º 8 g), 9), losses with privileged regimes (n.º 7), exit value (n.º 12) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs43.aspx | 2026-10-23 |
| CIRS art. 43, wording until May 2026 (exit rule then cited as art. 10 n.º 22) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/ra/Pages/irs43ra_202605.aspx | 2026-10-23 |
| CIRS art. 55, loss carry-forward (5 years if aggregated; Category B 12 years) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs55.aspx | 2026-10-23 |
| CIRS art. 68, IRS bands 2026 (wording of Lei 73-A/2025) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs68.aspx | 2026-10-23 |
| CIRS art. 72, 28% rate (n.º 1 c) and d)), aggregation option (n.º 13), 35% list (n.º 18) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs72.aspx | 2026-10-23 |
| CIRS art. 101-B, no withholding on crypto remuneration (n.º 5) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs101b.aspx | 2026-10-23 |

Not yet confirmed: the treatment of occasional (hobby) mining outside Category B; the acquisition value of crypto received as a staking reward (this skill assumes EUR 0); whether a crypto-for-crypto swap restarts the 365-day period (no AT guidance read); the Anexo G, G1 and B box numbers; the EUR 375 to EUR 22,500 fine range; DAC8 reporting dates. Art. 10 n.º 24 still refers to "n.os 19 e 20" after the renumbering; this skill reads it as the 365-day and swap rules now in n.º 22 and 23, which is not confirmed by AT guidance.

## Aviso Legal

Esta skill e os seus outputs são disponibilizados apenas para fins informativos e de cálculo, não constituindo aconselhamento fiscal, jurídico ou financeiro. A Open Accountants e os seus contribuidores declinam qualquer responsabilidade por erros, omissões ou consequências decorrentes do uso desta skill. Todos os outputs devem ser revistos e validados por profissional qualificado (contabilista certificado, advogado tributarista ou revisor oficial de contas em Portugal) antes da submissão ou de qualquer atuação com base nos mesmos.

A versão mais atualizada e verificada desta skill é mantida em [openaccountants.com](https://openaccountants.com). Inicie sessão para aceder à versão mais recente, solicitar revisão profissional por contabilista licenciado e acompanhar atualizações à medida que a legislação fiscal evolui.

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
