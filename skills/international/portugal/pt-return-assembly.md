---
name: pt-return-assembly
description: "Utilizar esta skill sempre que for solicitada a montagem, finalização ou consolidação de um pacote fiscal anual português — IRS (pessoas singulares) e/ou IRC (sociedades). Acionar com expressões como \"preparar declaração IRS final\", \"preparar Modelo 22 final\", \"pacote contabilista certificado\", \"working paper Portugal\", \"submissão Portal das Finanças\", \"consolidação fiscal Portugal\", \"fechar a declaração\", \"montar dossier fiscal\", \"review final antes de submeter no Portal das Finanças\", \"pacote OCC para revisão\", \"encerramento do ano fiscal português\", \"preparar IES\", \"preparar SAF-T anual\", \"consolidar Modelo 3 e Anexos\", \"consolidar Modelo 22 e Anexos\", ou pedidos equivalentes em inglês: \"Portugal return assembly\", \"Portugal final tax package\", \"Portugal working paper\", \"Portugal IRS/IRC submission package\", \"Portuguese tax return capstone\". Esta é a skill capstone orquestradora que consolida os outputs de pt-income-tax, pt-nhr-ifici, pt-foreign-source-treaties, pt-corporate-tax, portugal-vat-return, pt-social-contributions, portugal-payroll, portugal-bookkeeping, portugal-financial-statements e portugal-crypto-tax num único working paper unificado, com reconciliações cross-skill, instruções de pagamento via Portal das Finanças (Multibanco / MBWay / IBAN), instruções de submissão (Modelo 3 / Modelo 22 / IES / SAF-T) e lista final de ações do contribuinte. Não recalcula nada — apenas reconcilia, monta e empacota para o revisor. LER SEMPRE este skill em ÚLTIMO LUGAR — é o capstone que consolida todos os outputs upstream."
jurisdiction: PT
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# pt-return-assembly

## Portugal — Montagem Final da Declaração (Capstone) — Skill v1.0

## DIRETIVA DE EXECUÇÃO CRÍTICA — LER PRIMEIRO

**Quando esta skill é invocada, o contribuinte já passou pelo intake e pelas skills de conteúdo relevantes. Pretende o working paper final pronto para revisão pelo Contabilista Certificado (OCC). Executar todos os passos sem parar para pedir autorização.**

Em concreto:

- **Não perguntar "quer que monte o pacote completo?".** O utilizador pediu a montagem. Produzir.
- **Não voltar a interrogar sobre NIF, residência fiscal, NIPC, CAE, ou estrutura do negócio** — o intake já capturou estes dados; confiar nos packages upstream.
- **Não pausar entre passos de reconciliação para confirmar.** Executar todas as verificações cruzadas em sequência; sinalizar falhas no brief do revisor e continuar.
- **As auto-verificações são alvos, não bloqueadores.** Se uma verificação falhar, registar em "Sinalizações para o Revisor" e continuar.
- **Não submeter nada no Portal das Finanças, no e-fatura, no portal da Segurança Social, ou em qualquer outro portal.** Esta skill produz um working paper e instruções de submissão. Um **Contabilista Certificado** (membro da OCC — Ordem dos Contabilistas Certificados) tem de rever e assinar, e o contribuinte (ou o CC, no seu portal) submete via Portal das Finanças.

**Se sentir necessidade de perguntar "como devo proceder?", escolha o caminho mais defensável, prossiga, e sinalize a decisão para o revisor.**

## O que este ficheiro é

A skill capstone final para a campanha fiscal portuguesa. Consome os outputs de todas as outras skills Portugal e monta um único working paper unificado que cobre, conforme aplicável:

- **Modelo 3 do IRS** — declaração anual de rendimentos das pessoas singulares (incluindo trabalhadores independentes / Categoria B, sócios-gerentes que recebam pró-labore, sujeitos passivos com rendimentos prediais ou de mais-valias), submetida no **Portal das Finanças** ao abrigo do Código do IRS (CIRS), com os respetivos Anexos A, B, C, D, E, F, G, H, J, L.
- **Modelo 22 do IRC** — declaração periódica de rendimentos das sociedades (sociedades comerciais, sociedades por quotas, sociedades anónimas, ENI equiparados, sociedades unipessoais), submetida no **Portal das Finanças** ao abrigo do Código do IRC (CIRC), com os respetivos Anexos A (Derrama Municipal), B (Regime simplificado), C (regiões autónomas), D (benefícios fiscais), E (regime simplificado).
- **IES — Informação Empresarial Simplificada** — declaração anual conjunta (AT + Banco de Portugal + INE + Conservatória do Registo Comercial) com Anexos contabilísticos.
- **SAF-T (PT)** — ficheiro normalizado de auditoria fiscal-tributária (Portaria 321-A/2007 e Portaria 302/2016, com atualizações), submissão mensal e anual conforme aplicável.
- **Declaração Periódica IVA — Modelo C** — mensal (volume de negócios > €650.000) ou trimestral, ao abrigo do Código do IVA (CIVA).
- **DMR — Declaração Mensal de Remunerações** — obrigação dos empregadores ao abrigo do CIRS Art.º 119º.
- **DRI — Declaração de Rendimentos Independentes (Segurança Social)** — declaração trimestral de rendimentos para trabalhadores independentes ao abrigo do Código Contributivo.

O output é um pacote pronto para o revisor: working paper linha-a-linha, tabela de reconciliação cross-skill, instruções de pagamento (referência Multibanco, IBAN AT, MBWay), instruções de submissão para Portal das Finanças e portal da Segurança Social, checklist do revisor, e lista final de ações do contribuinte.

## Secção 1 — Referência Rápida

**Referência Rápida**

| Campo | Valor |
| --- | --- |
| País | República Portuguesa |
| Autoridade tributária | Autoridade Tributária e Aduaneira (AT) |
| Portal de submissão (fiscal) | Portal das Finanças (https://www.portaldasfinancas.gov.pt) |
| Portal de e-faturação | Portal e-fatura (https://faturas.portaldasfinancas.gov.pt) |
| Portal de Segurança Social | Segurança Social Direta (https://www.seg-social.pt) |
| Plataforma de pagamento | Multibanco (referência MB), MBWay, débito direto SEPA, IBAN AT, Pay@Portuguese banks |
| Moeda | EUR (€) |
| Ano fiscal — pessoas singulares | Ano civil (1 janeiro – 31 dezembro) |
| Ano fiscal — sociedades | Geralmente coincide com o ano civil; pode ser não-coincidente mediante autorização (CIRC Art.º 8º nº 2) |
| Ano fiscal atual | 2025 (campanha de submissão decorre em 2026) |
| Declaração singular | **Modelo 3** (IRS), submissão no Portal das Finanças |
| Declaração sociedades | **Modelo 22** (IRC), submissão no Portal das Finanças |
| Declaração empresarial conjunta | **IES** (Informação Empresarial Simplificada) |
| Auditoria fiscal eletrónica | **SAF-T (PT)** — submissão mensal de faturação e anual de contabilidade |
| Declaração de IVA | Modelo C (mensal ou trimestral) |
| Declaração mensal de remunerações | **DMR** (até dia 10 do mês seguinte) |
| Prazo Modelo 3 IRS 2025 | **30 junho 2026** (último dia útil de junho do ano n+1; CIRS Art.º 60º) |
| Prazo Modelo 22 IRC 2025 (período coincidente com ano civil) | **31 maio 2026** (último dia útil de maio do ano n+1; CIRC Art.º 120º) |
| Prazo IES 2025 | **15 julho 2026** (CIRC Art.º 121º) |
| Prazo SAF-T faturação mensal | Até **dia 5** do mês seguinte (Portaria 195/2020) |
| Prazo Declaração Periódica IVA mensal | Até **dia 20** (regime mensal) ou **dia 22** (regime trimestral) do 2.º mês seguinte |
| Prazo DMR | Até **dia 10** do mês seguinte (CIRS Art.º 119º) |
| Prazo DRI Segurança Social | Até **dia 31** do mês seguinte ao final do trimestre |
| Recibo / comprovativo | Comprovativo de entrega gerado automaticamente pelo Portal das Finanças (PDF) |
| Legislação fundamental | Código do IRS (Decreto-Lei nº 442-A/88), Código do IRC (Decreto-Lei nº 442-B/88), Código do IVA (Decreto-Lei nº 394-B/84), Lei Geral Tributária (LGT, Decreto-Lei nº 398/98), Regime Geral das Infrações Tributárias (RGIT, Lei nº 15/2001), Código Contributivo (Lei nº 110/2009), Estatuto dos Benefícios Fiscais (EBF, Decreto-Lei nº 215/89), Orçamento do Estado 2025 (Lei nº 45-A/2024) e Orçamento do Estado 2026 (em discussão) |
| Versão da skill | 1.0 |
| Validada por | Pendente — requer assinatura por **Contabilista Certificado** membro da OCC (Ordem dos Contabilistas Certificados); para opiniões de planeamento fiscal específico, também **Consultor Fiscal** inscrito |

## Secção 2 — Entradas Obrigatórias dos Skills Upstream

A skill de montagem **não recalcula nada**. Espera outputs estruturados das skills upstream abaixo. Se uma skill upstream não tiver corrido, a montagem sinaliza a lacuna e continua com os dados disponíveis.

### 2.1 Declaração singular (Modelo 3) — inputs

**Inputs Modelo 3**

| Skill upstream | Output consumido | Onde aparece no Modelo 3 |
| --- | --- | --- |
| `pt-income-tax` | Rendimento global, deduções específicas, deduções à coleta, taxas progressivas, adicional de solidariedade, retenções na fonte (IRS), regime simplificado vs contabilidade organizada, IRS Jovem | Modelo 3 — Rosto, Anexo A (trabalho dependente), Anexo B (trabalho independente), Anexo C (contabilidade organizada), Anexo H (deduções à coleta) |
| `pt-nhr-ifici` | Regime de Residente Não Habitual (legacy 2024–2034 cohort) ou IFICI (Incentivo Fiscal à Investigação Científica e Inovação); rendimentos de fonte estrangeira com tributação reduzida; rendimentos de "atividades de elevado valor acrescentado" | Modelo 3 — Anexo L (rendimentos obtidos no estrangeiro — RNH/IFICI) |
| `pt-foreign-source-treaties` | Rendimentos de fonte estrangeira, crédito de imposto por dupla tributação internacional (CIRS Art.º 81º), aplicação de Convenções para Evitar a Dupla Tributação (CDT) | Modelo 3 — Anexo J (rendimentos obtidos no estrangeiro) |
| `pt-corporate-tax` | (Apenas se o sujeito passivo for sócio de uma sociedade com transparência fiscal CIRC Art.º 6º) Lucro tributável imputado ao sócio | Modelo 3 — Anexo D (imputação de rendimentos) |
| `portugal-vat-return` | Para trabalhadores independentes Categoria B com IVA: posição anual de IVA; reconciliação de volume de negócios apenas | Verificação cruzada; não aparece diretamente no Modelo 3 |
| `pt-social-contributions` | Contribuições para a Segurança Social pagas como trabalhador independente; DRI trimestrais | Modelo 3 — Anexo B / C (dedução específica) |
| `portugal-bookkeeping` | Para contabilidade organizada: demonstração de resultados, conciliação fiscal-contabilística | Modelo 3 — Anexo C (campos de apuramento) |
| `portugal-crypto-tax` | Mais-valias e rendimentos de criptoativos (CIRS Art.º 10º-A, introduzido em 2023); detenção < 365 dias (categoria G) ou ≥ 365 dias (exclusão) | Modelo 3 — Anexo G (mais-valias) ou Anexo E (rendimentos de capitais) consoante natureza |
| `portugal-payroll` | Trabalhador independente que também recebe rendimentos de trabalho dependente: salários, retenções de IRS, contribuições para a Segurança Social, descontos sindicais, subsídios | Modelo 3 — Anexo A |

### 2.2 Declaração de sociedades (Modelo 22) — inputs

**Inputs Modelo 22**

| Skill upstream | Output consumido | Onde aparece no Modelo 22 |
| --- | --- | --- |
| `pt-corporate-tax` | Lucro tributável, derrama estadual (CIRC Art.º 87º-A), derrama municipal (Lei das Finanças Locais), tributações autónomas (CIRC Art.º 88º), prejuízos fiscais reportáveis (CIRC Art.º 52º), regime simplificado de IRC (CIRC Art.º 86º-A e seguintes), benefícios fiscais ao investimento (CFI, RFAI, SIFIDE) | Modelo 22 — Quadros 07, 09, 10, 11, 13; Anexos A, B, D |
| `portugal-bookkeeping` | Balancete final pós-encerramento, demonstração de resultados, balanço, mapas de depreciações e amortizações (Modelo 32) | Suporta Modelo 22 + IES |
| `portugal-financial-statements` | Demonstrações financeiras (SNC ou NCM): Balanço, Demonstração de Resultados por Naturezas, Demonstração das Alterações no Capital Próprio, Demonstração dos Fluxos de Caixa, Anexo | Submetidas via IES; suportam Modelo 22 |
| `portugal-vat-return` | Posição anual de IVA da sociedade; declarações periódicas; pro-rata se aplicável; regularizações | Verificação cruzada; não aparece no Modelo 22 mas fundamental para a IES (Anexo L) |
| `portugal-payroll` | Custos com pessoal, retenções na fonte de IRS dos colaboradores (Categoria A), contribuições TSU (Taxa Social Única) | Modelo 22 — Quadro 07 (gastos com pessoal); DMR cross-check |
| `pt-social-contributions` | TSU (23,75% entidade empregadora + 11% colaborador); contribuições sócios-gerentes; isenções e taxas reduzidas (jovens, +55 anos, primeiro emprego) | DMR + Modelo 22 verificação cruzada |
| `pt-foreign-source-treaties` | Rendimentos de fonte estrangeira da sociedade; crédito por dupla tributação internacional (CIRC Art.º 91º); regime de participation exemption (CIRC Art.º 51º) | Modelo 22 — Quadro 09 (deduções), campos específicos de CDT |
| `portugal-crypto-tax` | Ganhos e perdas em criptoativos detidos pela sociedade — tratados como ativos financeiros / inventários consoante natureza | Modelo 22 — Quadro 07 (correções fiscais ao resultado contabilístico) |

### 2.3 Identificadores exigidos pelo intake

**Identificadores**

| Identificador | Obrigatório para |
| --- | --- |
| **NIF** (Número de Identificação Fiscal) — 9 dígitos, atribuído pela AT a pessoas singulares e coletivas | Todas as declarações |
| **NISS** (Número de Identificação de Segurança Social) — 11 dígitos | Declarações Segurança Social, DMR, DRI |
| **NIPC** (Número de Identificação de Pessoa Coletiva) — coincide com NIF para sociedades | Modelo 22, IES |
| **CAE** (Classificação das Atividades Económicas) — código principal e códigos secundários | Modelo 22, IES, Anexo B do Modelo 3 |
| **Código de Acesso ao Portal das Finanças** (senha pessoal) | Submissão pelo próprio (ou pelo CC, com mandato) |
| **Senha do CC** (Contabilista Certificado) — credenciais OCC | Submissão obrigatória pelo CC quando aplicável |
| **Regime de IVA** — normal mensal, normal trimestral, isenção Art.º 53º (pequenos sujeitos passivos), regime forfetário Art.º 60º | Declaração periódica de IVA |
| **Domicílio fiscal** — concelho (define derrama municipal) | Modelo 22 — Quadro 10 |
| **Período de tributação** (sociedades com período não coincidente com ano civil) | Modelo 22 |
| **Estado civil + dependentes + agregado familiar** | Modelo 3 — Rosto |
| **Residência fiscal** (residente, não-residente, RNH, IFICI, status fiscal de Madeira/Açores) | Modelo 3 |
| **IBAN PT** + comprovativo de morada | Reembolsos e pagamentos |

- **Identificador em falta** — Se qualquer identificador estiver em falta, a skill de montagem sinaliza-o como "Necessita Input" e produz o working paper com placeholders em vez de parar.  _(unsure - no explicit legal citation provided)_

### 2.4 Coordenação AT + Segurança Social + e-fatura

Portugal tem múltiplas obrigações declarativas em portais distintos, mas a AT consolida no Portal das Finanças:

- **AT (Portal das Finanças):** Modelo 3, Modelo 22, IES, declarações periódicas de IVA, SAF-T, DMR (para parte fiscal), retenções na fonte, IMI, IMT, IUC.
- **Segurança Social (Segurança Social Direta):** TSU, contribuições trabalhadores independentes, DRI, DMR (para parte contributiva — DMR é declaração conjunta AT + SS).
- **e-fatura (faturas.portaldasfinancas.gov.pt):** comunicação de faturas emitidas e recebidas, e SAF-T faturação mensal.

A capstone produz **um pacote único integrado** com as três vertentes reconciliadas. Um sócio-gerente de uma sociedade unipessoal por quotas, por exemplo, terá obrigações como contribuinte singular (Modelo 3), como sociedade (Modelo 22), e como sujeito passivo de Segurança Social (TSU + DRI). A montagem cruza as três.

## Secção 3 — Workflow de Montagem — Reconciliações Cross-Skill

- **Regra geral de tolerância** — A skill de montagem verifica que os números das skills upstream são mutuamente consistentes. Se uma verificação cruzada falhar por mais de €1,00, a discrepância é levantada no brief do revisor — nunca arredondada silenciosamente.  _(unsure - no explicit legal citation provided)_

### 3.1 Verificação cruzada 1 — Reconciliação de volume de negócios

**Reconciliação volume de negócios**

| Origem | Valor | Regra |
| --- | --- | --- |
| `portugal-bookkeeping` / balancete — volume de negócios líquido | Total dos rendimentos operacionais | Valor âncora |
| `portugal-vat-return` — soma das bases tributáveis anuais de IVA (Campo 1 + Campo 5 + Campo 7 do Modelo C, ajustado para operações isentas/não sujeitas) | Soma do output das 12 declarações mensais (ou 4 trimestrais) | Deve reconciliar com a contabilidade ± diferenças temporais admissíveis e operações fora do campo do IVA |
| `pt-corporate-tax` (sociedades) / `pt-income-tax` (singulares) — total dos rendimentos brutos | Topo do quadro de apuramento fiscal | Tem de igualar a contabilidade ± correções fiscais ao resultado contabilístico (Quadro 07 do Modelo 22) |
| SAF-T faturação anual — total dos documentos emitidos | Soma de TotalGross dos InvoiceType FT/FR/FS no ano | Deve reconciliar com volume de negócios ± notas de crédito e ajustamentos |

**Se houver divergência:** causas prováveis são (i) operações isentas Art.º 9º CIVA não capturadas pela skill de IVA, (ii) diferenças temporais entre regime de caixa e regime de acréscimo (CIRC Art.º 18º), (iii) operações intracomunitárias intracomunitárias com inversão do sujeito passivo, (iv) rendimentos não sujeitos a IVA mas sujeitos a IRC/IRS, (v) ajustamentos de períodos anteriores.

### 3.2 Verificação cruzada 2 — Créditos de imposto e retenções

**Créditos e retenções — pessoas singulares (Modelo 3)**

| Linha | Skill de origem | Descrição |
| --- | --- | --- |
| Retenções na fonte sobre rendimentos do trabalho dependente | pt-income-tax + portugal-payroll | Crédito; campo do Anexo A |
| Retenções na fonte sobre rendimentos da Categoria B (independentes) — 25% / 11,5% / 16,5% | pt-income-tax | Crédito; campo do Anexo B |
| Retenções na fonte sobre rendimentos prediais (Categoria F) — 25% | pt-income-tax | Crédito; campo do Anexo F |
| Retenções na fonte sobre rendimentos de capitais (Categoria E) — 28% (geral) ou 35% (paraísos fiscais) | pt-income-tax | Crédito ou tributação liberatória |
| Crédito de imposto por dupla tributação internacional (CIRS Art.º 81º) | pt-foreign-source-treaties | Crédito; limitado ao menor entre imposto pago no estrangeiro e fração do IRS correspondente |
| Pagamentos por conta de IRS efetuados durante 2025 (CIRS Art.º 102º) | pt-income-tax | Crédito |

**Créditos e retenções — sociedades (Modelo 22)**

| Linha | Skill de origem | Descrição |
| --- | --- | --- |
| Retenções na fonte suportadas pela sociedade (rendas, juros, dividendos, prestações de serviços) | pt-corporate-tax | Crédito; campo 359 do Modelo 22 |
| Pagamentos por conta de IRC (CIRC Art.º 105º) — três prestações em julho, setembro, dezembro | pt-corporate-tax | Crédito; campo 360 |
| Pagamento adicional por conta (CIRC Art.º 105º-A) — se aplicável | pt-corporate-tax | Crédito; campo 361 |
| Pagamento especial por conta (CIRC Art.º 106º — revogado mas com remanescentes em uso) | pt-corporate-tax | Crédito; campo 362 (apenas se remanescente) |
| Crédito de imposto por dupla tributação internacional (CIRC Art.º 91º) | pt-foreign-source-treaties | Crédito; campo 353 |
| Benefícios fiscais com natureza de crédito (RFAI, SIFIDE, CFEI II) | pt-corporate-tax | Crédito; Anexo D |

- **Regra de créditos** — O total dos créditos não pode exceder a coleta para efeitos de reembolso a não ser que esteja expressamente previsto na lei (e.g., excesso de crédito SIFIDE pode ser reportado 8 anos). Cada retenção tem de ser suportada por declaração de retenção / Modelo 39 (rendimentos de capitais) ou Modelo 10 (rendimentos do trabalho e Categoria B) emitido pelo substituto tributário.  _(unsure - no explicit legal citation provided for the SIFIDE 8-year carryover)_

### 3.3 Verificação cruzada 3 — DMR mensal vs Modelo 10 anual

**DMR vs Modelo 10**

| Item | Origem | Regra |
| --- | --- | --- |
| Soma das 12 DMR (janeiro-dezembro 2025) — total de rendimentos pagos e retenções de IRS | portugal-payroll | Tem de igualar o Modelo 10 / Anexo J do Modelo 22 |
| Modelo 10 (declaração anual de rendimentos pagos e retenções) — prazo 10 fevereiro 2026 | portugal-payroll | Suporta o Anexo A do Modelo 3 dos colaboradores |
| Coima por atraso DMR | RGIT Art.º 117º | €100 a €2.500 por declaração em atraso |

**Se houver divergência:** verificar bonus / 14º mês / subsídio de Natal não capturados em DMR mensal; benefícios em espécie reconhecidos apenas em fecho; correções salariais retroativas.

### 3.4 Verificação cruzada 4 — Contribuições Segurança Social — empregadores e independentes

**Contribuições SS**

| Item | Origem | Regra |
| --- | --- | --- |
| TSU empregador 23,75% + colaborador 11% sobre remunerações sujeitas | pt-social-contributions + portugal-payroll | DMR mensal cruzar com folhas de salário |
| Contribuições trabalhador independente — 21,4% sobre 70% do rendimento relevante (regime geral) ou 25,2% sobre 70% (sócios-gerentes / membros estatutários) | pt-social-contributions | DRI trimestral; reconciliar com Modelo 3 Anexo B |
| Isenção do primeiro ano de atividade para trabalhadores independentes | pt-social-contributions | Confirmar elegibilidade |
| Taxa reduzida 18,4% para trabalhadores independentes que sejam pensionistas | pt-social-contributions | Confirmar status |
| Coima por atraso na entrega de DMR para Segurança Social | RGIT + Código Contributivo | €100 a €2.500 |

- **Reembolso TSU primeiro emprego** — Para o reembolso TSU "primeiro emprego" (jovens até 30 anos): verificar elegibilidade ao abrigo do regime de incentivo à contratação de jovens (Decreto-Lei nº 72/2017 com alterações) — pode haver isenção parcial até 7 anos.  _(Decreto-Lei nº 72/2017)_

### 3.5 Verificação cruzada 5 — IVA suportado e dedutível, pro-rata

**IVA suportado e dedutível**

| Item | Origem | Regra |
| --- | --- | --- |
| IVA liquidado (output) — Campo 4 do Modelo C | portugal-vat-return | Sobre operações tributáveis em PT |
| IVA dedutível (input) — Campo 22 do Modelo C | portugal-vat-return | Apenas sobre bens/serviços afetos a operações tributáveis |
| Pro-rata definitivo do ano (se sujeito passivo misto) — CIVA Art.º 23º | portugal-vat-return | Calcular pro-rata anual; regularizar diferença vs pro-rata provisório nas declarações mensais |
| Regularizações de IVA — Anexo R | portugal-vat-return | Campo 40 (a favor sujeito passivo) e Campo 41 (a favor Estado) |
| Anexo recapitulativo de operações intracomunitárias (Modelo IRC — declaração recapitulativa) | portugal-vat-return | Mensal/trimestral; reconciliar com VIES |
| SAF-T faturação anual — IVA liquidado por taxa | portugal-bookkeeping + e-fatura | Tem de reconciliar com soma das declarações periódicas |

**Se houver divergência > €1:** muito provavelmente correção pro-rata em falta, faturas emitidas em e-fatura sem reflexo nas declarações periódicas, ou notas de crédito não regularizadas.

### 3.6 Verificação cruzada 6 — Tributações autónomas (Modelo 22 — Quadro 13)

Para sociedades — as tributações autónomas são adicionadas à coleta e calculadas sobre encargos específicos, mesmo em situação de prejuízo:

**Tributações autónomas**

| Encargo | Taxa base | Acréscimo se prejuízo |
| --- | --- | --- |
| Despesas não documentadas | 50% | +10 pp = 60% |
| Despesas com viaturas ligeiras de passageiros < €27.500 (custo) | 10% | +10 pp |
| Viaturas €27.500 a €35.000 | 27,5% | +10 pp |
| Viaturas > €35.000 | 35% | +10 pp |
| Viaturas híbridas plug-in (limites diferenciados) | Taxas reduzidas | +10 pp se prejuízo |
| Viaturas elétricas puras (BEV) | 0% (com limites) | n/a |
| Despesas de representação | 10% | +10 pp |
| Ajudas de custo / quilómetros não faturados a clientes | 5% | +10 pp |
| Bónus a gestores que excedam 25% da remuneração total e € do valor mínimo | 35% | +10 pp |
| Indemnizações de cessação de funções de gestor | 35% | +10 pp |
| Lucros distribuídos a entidades total ou parcialmente isentas | 23% | n/a |

- **Confirmação TA** — A skill de montagem confirma que pt-corporate-tax calculou todas as TA aplicáveis e que a TA total foi adicionada à coleta no Quadro 10. Tolerância: €1.  _(unsure - no explicit legal citation provided)_

### 3.7 Verificação cruzada 7 — Derramas (municipal + estadual)

**Derramas**

| Derrama | Base | Taxa | Quem |
| --- | --- | --- | --- |
| **Derrama Municipal** (Lei das Finanças Locais — Lei nº 73/2013) | Lucro tributável da sociedade | Até 1,5% — definida por cada município anualmente; muitos municípios cobram 1,5%, outros 0% para PME | Sociedades, exceto as do regime simplificado em alguns municípios |
| **Derrama Estadual** (CIRC Art.º 87º-A) | Lucro tributável > €1.500.000 | 3% (€1,5M-€7,5M) + 5% (€7,5M-€35M) + 9% (>€35M) | Sociedades com lucro tributável superior a €1,5M |
| **Derrama Regional** Madeira/Açores | Equivalente em regimes regionais autónomos | Taxas regionais | Sociedades sediadas nas regiões autónomas |

- **Total da Coleta** — Coleta IRC + Derrama Municipal + Derrama Estadual + Tributações Autónomas = Total da Coleta (Campo 351 do Modelo 22)  _(Modelo 22 Campo 351)_

### 3.8 Verificação cruzada 8 — Adicional de solidariedade (IRS)

**Adicional de solidariedade**

| Escalão | Taxa adicional |
| --- | --- |
| €80.000 a €250.000 | 2,5% |
| > €250.000 | 5% |

- **Regra do adicional de solidariedade** — O adicional incide apenas sobre a parte do rendimento que excede o limiar. A skill de montagem cruza com pt-income-tax para confirmar que foi corretamente aplicado, em particular para sujeitos passivos casados com tributação separada (em que o limiar se aplica individualmente). Aplicável para pessoas singulares com rendimento coletável agregado > €80.000.  _(unsure - no explicit legal citation provided)_

### 3.9 Verificação cruzada 9 — Disciplina de tolerância

- **Disciplina de tolerância** — Para cada verificação cruzada acima, o limiar é €1,00. Se uma diferença estiver entre €1 e €100, documentar a variação e prosseguir com sinalização ao revisor. Acima de €100, levantar como "Necessita Input" — o revisor deve resolver antes da assinatura.  _(unsure - no explicit legal citation provided)_

## Secção 4 — Estrutura do Working Paper para o Contabilista Certificado (OCC)

O revisor é um **Contabilista Certificado** membro da **OCC — Ordem dos Contabilistas Certificados** (regulamento próprio publicado em Diário da República), com Cédula Profissional ativa e seguro de responsabilidade civil profissional em vigor. Para opiniões em matéria de planeamento fiscal e auditoria fiscal específica, pode também ser **Consultor Fiscal** inscrito pela OCC. O brief é um único ficheiro markdown que o CC lê antes de assinar.

```markdown
# Pacote de Declaração Anual — [Nome do contribuinte] — Período 2025

## Sumário Executivo
- Entidade declarante: [Singular / ENI / Sociedade por Quotas / SA / Unipessoal / Outro]
- NIF: [9 dígitos]
- NIPC (se aplicável): [9 dígitos]
- NISS (se aplicável): [11 dígitos]
- CAE principal: [_____]
- Regime fiscal IRS / IRC:
  - [Modelo 3 — IRS Categoria B regime simplificado / contabilidade organizada]
  - [Modelo 22 — IRC regime geral / regime simplificado (CIRC Art.º 86º-A) / regime PME]
  - [RNH legacy 2024-2034 / IFICI / regime geral]
- Regime de IVA: [Mensal / Trimestral / Isenção Art.º 53º / Forfetário Art.º 60º / Outro]
- Declarações a submeter:
  - [ ] Modelo 3 IRS — Portal das Finanças — prazo 30 junho 2026
  - [ ] Modelo 22 IRC — Portal das Finanças — prazo 31 maio 2026
  - [ ] IES — Portal das Finanças — prazo 15 julho 2026
  - [ ] Declaração periódica de IVA dezembro 2025 (regime mensal) — prazo 10 fevereiro 2026
  - [ ] Declaração periódica de IVA 4º trimestre 2025 (regime trimestral) — prazo 20 fevereiro 2026
  - [ ] DMR dezembro 2025 — prazo 10 janeiro 2026
  - [ ] Modelo 10 — prazo 10 fevereiro 2026
  - [ ] DRI 4º trimestre 2025 — prazo 31 janeiro 2026
  - [ ] SAF-T faturação dezembro 2025 — prazo 5 janeiro 2026
  - [ ] SAF-T contabilístico anual (com IES) — prazo 15 julho 2026
- Total da coleta IRS / IRC: €X
- Total das retenções e pagamentos por conta: €X
- Saldo a pagar / reembolsar: €X / (€X)

## Apuramento de IRC (sociedades)
[De pt-corporate-tax]
- Resultado contabilístico antes de impostos
- Correções fiscais ao resultado (Quadro 07)
- Lucro tributável
- Prejuízos fiscais reportáveis (CIRC Art.º 52º — 5 anos / 12 anos PME até 2023 / 5 anos a partir de 2024)
- Matéria coletável
- Coleta IRC (21% taxa geral; 17% sobre primeiros €50.000 PME — CIRC Art.º 87º)
- Derrama municipal (até 1,5% conforme município)
- Derrama estadual (escalões 3%/5%/9% acima €1,5M)
- Tributações autónomas (Quadro 13)
- Total da coleta

## Apuramento de IRS (singulares)
[De pt-income-tax, pt-nhr-ifici, pt-foreign-source-treaties]
- Rendimentos por categoria (A, B, E, F, G, H)
- Deduções específicas
- Rendimento líquido
- Englobamento ou opção pelas taxas liberatórias (CIRS Art.º 22º)
- Quociente conjugal (se aplicável)
- Coleta a taxas progressivas (CIRS Art.º 68º)
- Deduções à coleta (CIRS Art.º 78º) — saúde, educação, lares, dependentes
- Coleta líquida
- Adicional de solidariedade (>€80.000)
- Imposto a pagar / reembolso

## IVA Anual
[De portugal-vat-return]
- Resumo das 12 (ou 4) declarações periódicas
- IVA liquidado, IVA dedutível, IVA entregue
- Pro-rata definitivo (se aplicável)
- Regularizações
- Verificação cruzada com volume de negócios da contabilidade

## Segurança Social
[De pt-social-contributions]
- TSU empregador + colaboradores (sociedades)
- Contribuições do sujeito passivo como trabalhador independente (singulares)
- DRI trimestrais
- DMR (parte SS)

## Folha de Pagamentos
[De portugal-payroll]
- Resumo anual de remunerações
- Retenções na fonte IRS Categoria A
- TSU
- Modelo 10 / DMR cross-check

## Contabilidade e Demonstrações Financeiras
[De portugal-bookkeeping, portugal-financial-statements]
- Balancete final pós-encerramento
- Balanço, DR, DACP, DFC, Anexo
- Mapas de depreciações e amortizações (Modelo 32)
- SAF-T contabilístico anual

## Criptoativos
[De portugal-crypto-tax]
- Mais-valias Categoria G (detenção < 365 dias) — taxa 28% ou englobamento
- Detenção ≥ 365 dias — exclusão CIRS Art.º 10º-A nº 2
- Operações de staking, mining, validation — Categoria B ou E conforme natureza
- Rendimentos de criptoativos para sociedades — tratamento contabilístico-fiscal

## Reconciliações Cross-Skill
- Volume de negócios contabilidade vs IVA vs Modelo 22/Modelo 3: [pass/fail]
- Retenções na fonte declaradas vs créditos reclamados: [pass/fail]
- DMR mensal vs Modelo 10 anual: [pass/fail]
- TSU empregador + colaboradores vs registos SS: [pass/fail]
- SAF-T faturação anual vs contabilidade: [pass/fail]
- Tributações autónomas — taxas aplicadas: [pass/fail]
- Derramas (municipal + estadual) — corretamente computadas: [pass/fail]
- Adicional de solidariedade — escalão correto: [pass/fail]

## Sinalizações para o Revisor
- Itens que requerem confirmação adicional pelo CC / Consultor Fiscal
- Despesas borderline (representação, donativos fora EBF)
- Benefícios fiscais reclamados (RFAI, SIFIDE, CFEI, DLRR) — documentação
- Operações com partes relacionadas (CIRC Art.º 63º — Preços de Transferência)
- Operações com paraísos fiscais (CIRC Art.º 23º-A — limitação à dedutibilidade)
- Prejuízos fiscais reportáveis — verificação de regra dos 70% (CIRC Art.º 52º)
- Pagamento Especial por Conta — remanescentes em uso (revogado mas dedutível ainda 6 anos)
- Endividamento excessivo — barrier rules (CIRC Art.º 67º)
- Provisões e ajustamentos (CIRC Art.º 28º a 39º-A)
- Mais-valias e menos-valias fiscais com regimes específicos
- Operações de fusão / cisão com regime de neutralidade (CIRC Art.º 73º)
- Pro-rata IVA — sujeito passivo misto
- Faturação simplificada vs fatura completa — limites
- e-fatura — desfasamento entre faturas comunicadas e contabilidade

## Posições Adotadas
[Lista com referências legais]
- e.g., "Coeficiente regime simplificado de 0,75 aplicado à atividade [____] — CIRS Art.º 31º nº 1 al. b)"
- e.g., "Taxa reduzida IRC 17% sobre primeiros €50.000 — sociedade qualifica-se como PME (Decreto-Lei nº 372/2007); CIRC Art.º 87º nº 2"
- e.g., "RFAI reclamado de €X — investimento elegível na região do Norte; deduzido até 25% do investimento até concorrência de 50% da coleta"
- e.g., "Operações com [paraíso fiscal] sujeitas a CIRC Art.º 23º-A — comprovativo de substância económica anexo"
- e.g., "Crédito por dupla tributação internacional — Convenção PT-[país]; limitado nos termos do CIRS Art.º 81º / CIRC Art.º 91º"

## Notas de Planeamento para 2026
[Ver Secção 9]
```

## Secção 5 — Resumo da Liquidação Fiscal (Bloco Headline)

Este bloco é o cabeçalho que o revisor e o contribuinte leem primeiro.

### 5.1 Bloco Headline — IRS (singulares)

```markdown
# IRS 2025 — Liquidação Headline (€)

Rendimento bruto (todas as categorias):    X
Deduções específicas:                      (X)
Rendimento líquido:                        X
Quociente familiar (se conjugal):          /
Coleta a taxas progressivas:               X
Adicional de solidariedade (>€80K):        X
Deduções à coleta (saúde, educação, etc.): (X)
Coleta líquida:                            X

Menos: Retenções na fonte:                 (X)
Menos: Pagamentos por conta:               (X)
Menos: Crédito dupla tributação:           (X)
= Imposto a pagar / (a reembolsar):        X / (X)

Submissão: Modelo 3 + Anexos aplicáveis
Prazo: 30 junho 2026
Portal: Portal das Finanças
Pagamento: Multibanco / MBWay / IBAN AT
```

### 5.2 Bloco Headline — IRC (sociedades)

```markdown
# IRC 2025 — Liquidação Headline (€)

Volume de negócios:                        X
Resultado antes de impostos (RAI):         X
Correções fiscais Quadro 07:               +X / -X
Lucro tributável:                          X
Prejuízos fiscais utilizados (CIRC 52º):   (X) [máx 70% do LT]
Matéria coletável:                         X

Coleta IRC:
  - 17% sobre primeiros €50.000 (PME):     X
  - 21% sobre excedente:                   X
Derrama municipal (até 1,5%):              X
Derrama estadual (escalões 3/5/9%):        X
Tributações autónomas (Quadro 13):         X
= Total da coleta (Campo 351):             X

Menos: Retenções na fonte suportadas:      (X)
Menos: Pagamentos por conta (PPC):         (X)
Menos: Pagamento adicional (PAPC):         (X)
Menos: Crédito dupla tributação:           (X)
Menos: Benefícios fiscais (RFAI/SIFIDE):   (X)
= Imposto a pagar / (a reembolsar):        X / (X)

Submissão: Modelo 22 + Anexos + IES
Prazo Modelo 22: 31 maio 2026
Prazo IES: 15 julho 2026
Portal: Portal das Finanças
Pagamento: Multibanco / IBAN AT
```

## Secção 6 — Instruções de Pagamento — Portal das Finanças

Os pagamentos de IRS, IRC, IVA e outros tributos são processados através do Portal das Finanças, que gera uma referência de pagamento (entidade + referência Multibanco + valor) após a submissão da declaração ou da nota de liquidação. O contribuinte paga via:

- **Multibanco** (caixa automática ou home banking) — usando a referência gerada (entidade 5 dígitos + referência 9 dígitos + montante)
- **MBWay** — funcionalidade disponível para alguns tributos via aplicação móvel
- **Débito direto SEPA** — autorização prévia no Portal das Finanças
- **Transferência bancária para IBAN da AT** — IBAN PT50 0781 0112 0112 0120 0083 8 (verificar no Portal das Finanças a cada pagamento, pois o IBAN pode variar consoante o tipo de tributo)
- **Pay@ ou serviços bancários** das principais instituições portuguesas com integração ao Portal das Finanças

### 6.1 Tipos de tributo e canais

**Tipos de tributo e canais**

| Tributo | Autoridade | Portal | Canal de pagamento |
| --- | --- | --- | --- |
| IRS | AT | Portal das Finanças | Multibanco / MBWay / IBAN AT / débito direto |
| IRC | AT | Portal das Finanças | Idem |
| IVA | AT | Portal das Finanças | Idem |
| Pagamentos por conta IRC (julho/setembro/dezembro) | AT | Portal das Finanças | Idem |
| Pagamentos por conta IRS (julho/setembro/dezembro) | AT | Portal das Finanças | Idem |
| Tributações autónomas | AT | Liquidadas com Modelo 22 | Idem |
| Derrama municipal e estadual | AT (cobra para municípios) | Liquidadas com Modelo 22 | Idem |
| Retenções na fonte (substitutos tributários) | AT | Guia de pagamento mensal | Multibanco até dia 20 do mês seguinte |
| TSU (entidades empregadoras + colaboradores) | Segurança Social | Segurança Social Direta | Multibanco até dia 20 do mês seguinte |
| Contribuições trabalhador independente | Segurança Social | Segurança Social Direta | Multibanco até dia 20 do mês seguinte |
| IMI (Imposto Municipal sobre Imóveis) | AT | Portal das Finanças | 1 prestação (≤€100) maio; 2 prestações (€100-€500) maio + novembro; 3 prestações (>€500) maio + agosto + novembro |
| IUC (Imposto Único de Circulação) | AT | Portal das Finanças | Anual, no mês do aniversário do veículo |

### 6.2 Fluxo Portal das Finanças → Multibanco

1. Aceder ao Portal das Finanças (https://www.portaldasfinancas.gov.pt) com NIF + senha (ou Chave Móvel Digital / Cartão de Cidadão)
2. Submeter a declaração (Modelo 3, Modelo 22, declaração periódica IVA)
3. Após validação, o sistema processa e emite a nota de liquidação (geralmente em horas para IVA; até final do ano civil seguinte para IRS/IRC)
4. A nota de liquidação contém a referência de pagamento Multibanco (Entidade + Referência + Montante)
5. Pagar até à data-limite indicada:
   - Caixa Multibanco (com cartão débito)
   - Home banking (todos os bancos portugueses oferecem "Pagamentos ao Estado")
   - MBWay (limites por tributo)
   - Transferência IBAN AT (atenção: identificar o IBAN correto no Portal das Finanças)
6. Após o pagamento, a AT atualiza o estado no Portal das Finanças e emite comprovativo de pagamento (PDF descarregável)

### 6.3 Pagamentos por conta de IRC (CIRC Art.º 105º)

**Pagamentos por conta IRC**  _(CIRC Art.º 105º)_

| PPC | Prazo | Base de cálculo |
| --- | --- | --- |
| 1ª prestação | Até **31 julho** | 80% (ou 95% se VN>€500.000) da coleta do ano anterior dividida por 3 |
| 2ª prestação | Até **30 setembro** | Idem |
| 3ª prestação | Até **15 dezembro** | Idem |

- **Limitação à dispensa** — Pode dispensar-se da 3ª prestação se o sujeito passivo entender que a soma das duas primeiras já cobre o IRC final, mas suporta juros compensatórios se errar por mais de 20%.  _(CIRC Art.º 107º)_

### 6.4 Pagamentos por conta de IRS (CIRS Art.º 102º)

**Pagamentos por conta IRS**  _(CIRS Art.º 102º)_

| PPC | Prazo | Base de cálculo |
| --- | --- | --- |
| 1ª prestação | Até **20 julho** | 76,5% × IRS do penúltimo ano × coeficiente |
| 2ª prestação | Até **20 setembro** | Idem |
| 3ª prestação | Até **20 dezembro** | Idem |

### 6.5 Comprovativos de pagamento a conservar

**Comprovativos a conservar**

| Documento | Emitido por | Conservar por |
| --- | --- | --- |
| Comprovativo de submissão (Modelo 3 / 22 / IES / IVA) | Portal das Finanças | Indefinidamente |
| Nota de liquidação | AT | Indefinidamente |
| Comprovativo Multibanco (talão) ou print home banking | Banco | Pelo menos 4 anos (caducidade tributária — LGT Art.º 45º) |
| Comprovativo de pagamento no Portal das Finanças | AT | Indefinidamente |
| Certidões de não-dívida (à AT e à Segurança Social) | AT / SS | 3 meses validade; renovar conforme necessário |

### 7.1 Submissões no Portal das Finanças

**Canais de submissão**

| Canal | Descrição | Adequado para |
| --- | --- | --- |
| **Portal das Finanças — preenchimento direto** | Formulário online no Portal | Contribuintes singulares sem CC; PME simples |
| **Portal das Finanças — ficheiro de submissão** | Upload de ficheiros XML / ZIP gerados por software de contabilidade certificado | CC profissionais; sociedades com volume |
| **Software certificado de contabilidade / faturação** | Integração API via webservices da AT | Sociedades com ERP; grandes contribuintes |

### 7.2 Submissão do Modelo 3 (IRS)

1. Aceder ao Portal das Finanças com NIF + senha (ou Chave Móvel Digital / Cartão de Cidadão / autenticação.gov)
2. Menu: "Cidadãos" → "Serviços" → "IRS" → "Entregar Declaração — Modelo 3"
3. Selecionar ano de tributação 2025
4. O sistema apresenta uma declaração pré-preenchida com dados já comunicados à AT (rendimentos do trabalho, retenções, despesas dedutíveis via e-fatura, contribuições SS, faturas com NIF, etc.)
5. Validar e corrigir os anexos pré-preenchidos; acrescentar Anexos manualmente:
   - Anexo A (trabalho dependente — geralmente pré-preenchido)
   - Anexo B (independentes regime simplificado)
   - Anexo C (independentes contabilidade organizada)
   - Anexo D (transparência fiscal)
   - Anexo E (rendimentos de capitais)
   - Anexo F (rendimentos prediais)
   - Anexo G (mais-valias)
   - Anexo H (deduções à coleta)
   - Anexo J (rendimentos obtidos no estrangeiro)
   - Anexo L (RNH / IFICI)
6. Validar — Portal das Finanças executa verificações lógicas e aritméticas; resolver erros (a vermelho) e analisar avisos (a amarelo)
7. Submeter → sistema emite comprovativo de entrega (PDF)
8. Aguardar nota de liquidação — geralmente emitida ao longo de julho/agosto para declarações entregues a tempo

**Atenção:** uma declaração entregue com IBAN PT válido permite reembolso por transferência. Sem IBAN, o reembolso é por cheque (mais demorado e em desuso).

### 7.3 Submissão do Modelo 22 (IRC)

A submissão do Modelo 22 obriga à intervenção de Contabilista Certificado (CIRC Art.º 117º; Estatuto da OCC). O CC submete pelo seu acesso pessoal ao Portal das Finanças com a sua senha de CC.

1. CC acede ao Portal das Finanças com NIF do CC + senha CC
2. Menu: "Empresas" → "Serviços" → "IRC" → "Entregar Declaração — Modelo 22"
3. Selecionar período de tributação 2025
4. Preencher Quadros 01 a 13:
   - Quadro 01: Identificação
   - Quadro 02: Características da declaração
   - Quadro 03: Identificação do sujeito passivo e do TOC/CC
   - Quadro 04: Tipo de declaração
   - Quadro 05: Período de tributação
   - Quadro 06: Identificação dos representantes (se aplicável)
   - Quadro 07: Apuramento do lucro tributável (correções fiscais)
   - Quadro 08: Regime fiscal especial (transparência, holding, ZFM Madeira)
   - Quadro 09: Apuramento da matéria coletável
   - Quadro 10: Cálculo do imposto
   - Quadro 11: Outras informações
   - Quadro 12: Retenções na fonte
   - Quadro 13: Tributações autónomas
5. Submeter Anexos aplicáveis:
   - Anexo A (Derrama Municipal) — obrigatório se sociedade
   - Anexo B (regime simplificado IRC)
   - Anexo C (operações nas regiões autónomas)
   - Anexo D (benefícios fiscais — RFAI, SIFIDE, CFEI, DLRR)
   - Anexo E (regime simplificado)
6. Validar e submeter — Portal emite comprovativo
7. Aguardar nota de liquidação e referência de pagamento Multibanco

### 7.4 Submissão da IES (Informação Empresarial Simplificada)

A IES é declaração conjunta para AT + Banco de Portugal + INE + Conservatória do Registo Comercial. Substitui múltiplas declarações antigas (declaração anual contabilística, prestação de contas, etc.). Submetida pelo CC.

1. CC acede ao Portal das Finanças
2. Menu: "Empresas" → "Serviços" → "IES — Declaração Anual"
3. Preencher Anexos:
   - Anexo A: Informação contabilística (SNC ou NCM ou NCM-ME conforme dimensão)
   - Anexo L: Operações com partes relacionadas (Preços de Transferência) — se VN > €3M
   - Anexo R: Operações intracomunitárias
   - Anexo Q: Operações com territórios offshore
   - Outros anexos consoante natureza
4. Anexar SAF-T contabilístico (.xml) gerado pelo software certificado
5. Validar e submeter — Portal emite comprovativo único que serve as 4 entidades destinatárias

### 7.5 Submissão da Declaração Periódica de IVA (Modelo C)

1. CC ou sujeito passivo acede ao Portal das Finanças
2. Menu: "Empresas" / "Cidadãos" → "Serviços" → "IVA" → "Declaração Periódica"
3. Selecionar período (mês ou trimestre)
4. Preencher Quadros 01 a 06 + Anexo R (regularizações)
5. Submeter → comprovativo + nota de liquidação
6. Pagar até prazo (dia 20 ou 22 do 2º mês seguinte)

### 7.6 Submissão de SAF-T (PT)

**Tipos de SAF-T**

| Tipo SAF-T | Submissão | Prazo |
| --- | --- | --- |
| **SAF-T Faturação** | Comunicação mensal de documentos (faturas, notas de crédito, recibos) | Até **dia 5** do mês seguinte (Portaria 195/2020) — via webservice ou e-fatura |
| **SAF-T Contabilístico** | Anual, junto com IES | **15 julho 2026** para 2025 |
| **SAF-T Auditoria fiscal** | Sob solicitação da AT em inspeções | Variável |

### 7.7 Submissões na Segurança Social Direta

**Submissões Segurança Social Direta**

| Declaração | Prazo |
| --- | --- |
| **DMR** (declaração mensal de remunerações — parte SS) | Até **dia 10** do mês seguinte |
| **DRI** (declaração de rendimentos independentes) | Até **dia 31** do mês seguinte ao fim do trimestre (jan, abr, jul, out) |
| **Folha de Férias / Mapa de Encargos** | Anualmente em janeiro |
| **Declarações de Início / Cessação / Suspensão de atividade** | 15 dias após o facto |

### 7.8 Resumo de prazos (período 2025)

**Resumo de prazos**

| Tipo de declarante | Declaração | Autoridade | Prazo |
| --- | --- | --- | --- |
| Singular (residente) | Modelo 3 IRS + Anexos | AT | **30 junho 2026** |
| Sociedade (período = ano civil) | Modelo 22 IRC + Anexos | AT | **31 maio 2026** |
| Sociedade | IES + SAF-T contabilístico anual | AT (+ BdP + INE + ConservRegCom) | **15 julho 2026** |
| Sujeito passivo IVA mensal | Modelo C — dezembro 2025 | AT | **10 fevereiro 2026** |
| Sujeito passivo IVA trimestral | Modelo C — 4º trimestre 2025 | AT | **20 fevereiro 2026** |
| Empregador / substituto tributário | DMR — dezembro 2025 | AT + SS | **10 janeiro 2026** |
| Empregador / substituto tributário | Modelo 10 (anual de rendimentos pagos) | AT | **10 fevereiro 2026** |
| Empregador / sujeito passivo retenção rend. capitais | Modelo 39 | AT | **31 janeiro 2026** |
| Trabalhador independente | DRI — 4º trimestre 2025 | SS | **31 janeiro 2026** |
| Todos | SAF-T Faturação dezembro 2025 | AT (e-fatura) | **5 janeiro 2026** |
| Sociedades sujeitas a CbCR | Country-by-Country Report | AT | 12 meses após fim do período de relato |

### 7.9 Coimas por atraso

**Coimas por atraso**

| Infração | Coima | Base legal |
| --- | --- | --- |
| Falta ou atraso na entrega de declaração obrigatória (Modelo 3, Modelo 22, IVA, IES) | €150 a €3.750 | RGIT Art.º 116º |
| Falta ou atraso na entrega de DMR | €100 a €2.500 | RGIT Art.º 117º |
| Falta de comunicação de elementos no e-fatura | €150 a €3.750 | RGIT Art.º 117º |
| Falta de envio do SAF-T faturação | €150 a €3.750 | RGIT Art.º 117º |
| Falta de pagamento (não falta de declaração) — juros compensatórios | Taxa juros compensatórios + coima | LGT Art.º 35º + RGIT Art.º 114º |
| Falta de retenção na fonte | Coima + retenção em singelo + juros | RGIT Art.º 114º |

- **Atenuante** — Entrega voluntária antes de qualquer ato inspetivo reduz a coima ao mínimo legal.  _(RGIT Art.º 29º)_

### 7.10 Substituição de declaração

- **Substituição de declaração** — Se uma declaração já submetida contiver erros, deve apresentar-se declaração de substituição ao abrigo do CIRS Art.º 59º / CIRC Art.º 122º. Pode ser: (i) Dentro do prazo legal: sem coima; (ii) Fora do prazo legal: com coima reduzida (RGIT Art.º 29º — atenuação para regularização espontânea); (iii) Em consequência de inspeção: sem atenuação; pode haver crime fiscal se houver ocultação.  _(CIRS Art.º 59º / CIRC Art.º 122º / RGIT Art.º 29º)_

## Secção 8 — Lista Final de Ações do Contribuinte (Calendar)

```markdown
# Lista de Ações — [Nome do contribuinte] — Período 2025

## Janeiro 2026

| Data | Ação | Responsável |
|---|---|---|
| 5 jan | SAF-T Faturação dezembro 2025 — comunicação via webservice ou portal e-fatura | CC / software |
| 10 jan | DMR dezembro 2025 (parte SS + parte AT — Modelo 10 mensal embutido) | CC / empregador |
| 20 jan | Retenções na fonte de dezembro 2025 (rendimentos pagos a terceiros) | Sociedade / sujeito passivo |
| 20 jan | TSU dezembro 2025 (entidade empregadora + colaboradores) | Sociedade |
| 20 jan | Contribuições SS dezembro 2025 do trabalhador independente | Singular |
| 31 jan | DRI 4º trimestre 2025 — declaração de rendimentos relevantes para SS | Trabalhador independente |
| 31 jan | Modelo 39 (rendimentos de capitais — anual) | Substituto tributário |

## Fevereiro 2026

| Data | Ação | Responsável |
|---|---|---|
| 5 fev | SAF-T Faturação janeiro 2026 | CC / software |
| 10 fev | DMR janeiro 2026 | CC / empregador |
| 10 fev | **Declaração Periódica de IVA dezembro 2025 (regime mensal)** | CC |
| 10 fev | **Modelo 10 — anual de rendimentos pagos e retenções** | Substituto tributário |
| 20 fev | **Declaração Periódica de IVA 4º trimestre 2025 (regime trimestral)** | CC |

## Março 2026

| Data | Ação | Responsável |
|---|---|---|
| 5 mar | SAF-T Faturação fevereiro 2026 | CC / software |
| 10 mar | DMR fevereiro 2026 | CC / empregador |
| 20 mar | IVA janeiro 2026 (mensal) | CC |
| 31 mar | Modelo 30 — rendimentos pagos a não-residentes | Substituto tributário |

## Maio 2026

| Data | Ação | Responsável |
|---|---|---|
| **31 mai** | **MODELO 22 IRC + Anexos — submissão e pagamento** | CC obrigatoriamente |

## Junho 2026

| Data | Ação | Responsável |
|---|---|---|
| **30 jun** | **MODELO 3 IRS + Anexos — submissão e pagamento** | Singular (ou CC com mandato) |

## Julho 2026

| Data | Ação | Responsável |
|---|---|---|
| **15 jul** | **IES — Informação Empresarial Simplificada + SAF-T contabilístico anual** | CC obrigatoriamente |
| 20 jul | 1ª prestação Pagamentos por Conta IRS 2026 (Categoria B sem retenção) | Singular |
| 31 jul | 1ª prestação Pagamentos por Conta IRC 2026 | Sociedade |

## Setembro 2026

| Data | Ação | Responsável |
|---|---|---|
| 20 set | 2ª prestação PPC IRS 2026 | Singular |
| 30 set | 2ª prestação PPC IRC 2026 | Sociedade |

## Dezembro 2026

| Data | Ação | Responsável |
|---|---|---|
| 15 dez | 3ª prestação PPC IRC 2026 | Sociedade |
| 20 dez | 3ª prestação PPC IRS 2026 | Singular |

## Obrigações contínuas durante 2026

| Item | Autoridade | Periodicidade |
|---|---|---|
| SAF-T Faturação | AT (e-fatura) | Mensal (dia 5) |
| DMR | AT + SS | Mensal (dia 10) |
| Retenções na fonte | AT | Mensal (dia 20) |
| TSU empregador + colaboradores | SS | Mensal (dia 20) |
| Declaração Periódica IVA mensal | AT | Mensal (dia 20 ou 22) |
| Comunicação de inventários (sociedades com volume) | AT | Anual em janeiro |
| IMI | AT | Maio (1 prestação) ou maio/agosto/novembro |
| IUC (por veículo) | AT | Anual no mês do aniversário |

## Conservação de documentos

Por força da LGT Art.º 123º + Decreto-Lei nº 36/2017 + Código Comercial Art.º 40º, os livros, registos contabilísticos e respetivos documentos de suporte devem ser conservados por 10 anos. Para efeitos exclusivamente fiscais, o prazo é de 4 anos (LGT Art.º 45º — caducidade do direito à liquidação), mas estende-se a 12 anos se houver direito ao reporte de prejuízos.

Conservar pelo menos:
- Demonstrações financeiras + Anexo (sociedades)
- Balancetes mensais e final
- Diários e razão (geral + auxiliares)
- Faturas emitidas e recebidas + documentos de transporte (guias)
- SAF-T mensais e anual
- Comunicação de inventários
- Comprovativos de submissão (Modelo 3, 22, IVA, IES, DMR, DRI)
- Notas de liquidação e comprovativos de pagamento
- Comprovativos de pagamentos por conta
- Certidões de não-dívida (AT e SS)
- Mapas de depreciações e amortizações
- Contratos relevantes (laborais, locação financeira, mútuos, prestação de serviços com partes relacionadas)
- Atas de assembleias-gerais e órgãos de administração (sociedades)
```

## Secção 2 — Entradas Obrigatórias dos Skills Upstream

0. **Invocar pt-income-tax** — Consumir output para Modelo 3 rendimento, deduções, taxas, retenções
0. **Invocar pt-nhr-ifici** — Consumir output RNH/IFICI para Anexo L
0. **Invocar pt-foreign-source-treaties** — Consumir crédito de dupla tributação para Anexo J
0. **Invocar pt-corporate-tax** — Consumir lucro tributável, derramas, tributações autónomas para Modelo 22
0. **Invocar portugal-vat-return** — Consumir posição anual de IVA para reconciliação
0. **Invocar pt-social-contributions** — Consumir TSU e contribuições independentes
0. **Invocar portugal-payroll** — Consumir custos com pessoal, retenções Categoria A, DMR
0. **Invocar portugal-bookkeeping** — Consumir balancete, demonstração de resultados, mapas de depreciação
0. **Invocar portugal-financial-statements** — Consumir demonstrações financeiras SNC/NCM para IES
0. **Invocar portugal-crypto-tax** — Consumir mais-valias e rendimentos de criptoativos

## Secção 3 — Workflow de Montagem — Reconciliações Cross-Skill

0. **Executar verificações cruzadas 1-9** — Reconciliar volume de negócios, créditos e retenções, DMR vs Modelo 10, contribuições SS, IVA e pro-rata, tributações autónomas, derramas, adicional de solidariedade, e aplicar disciplina de tolerância

## Secção 4 — Estrutura do Working Paper para o Contabilista Certificado (OCC)

0. **Montar working paper** — Consolidar todos os outputs upstream no template markdown do working paper para o CC

## Secção 5 — Resumo da Liquidação Fiscal (Bloco Headline)

0. **Gerar bloco headline** — Produzir bloco headline IRS e/ou IRC conforme aplicável

## Secção 6 — Instruções de Pagamento — Portal das Finanças

0. **Gerar instruções de pagamento** — Produzir instruções de pagamento via Portal das Finanças / Multibanco / MBWay

## Secção 7 — Instruções de Submissão

0. **Gerar instruções de submissão** — Produzir instruções de submissão para Portal das Finanças, SAF-T e Segurança Social Direta

## Secção 8 — Lista Final de Ações do Contribuinte (Calendar)

0. **Gerar lista final de ações** — Produzir calendário de ações mensal do contribuinte para 2026

## Secção 9 — Notas para o Exercício de 2026 (Planeamento)

A capstone produz uma secção prospetiva para que o contribuinte chegue à próxima campanha consciente das alterações estruturais previstas.

### 9.1 Orçamento do Estado 2026 — pontos de atenção

À data desta versão da skill, o Orçamento do Estado 2026 (OE 2026) está em discussão parlamentar. Pontos estruturais a monitorizar:

**OE 2026 — pontos de atenção**  _(OE 2025/2026)_

**OE 2026 — tabela de pontos de atenção**  _(OE 2025 / OE 2026 (projetado))_

| Área | OE 2025 (atual) | OE 2026 (projetado / em discussão) | Ação |
| --- | --- | --- | --- |
| Taxa geral IRC | 21% (CIRC Art.º 87º) | Possível redução adicional para 19% (PSD/governo propõe trajetória de descida) | Reforecast pós-OE 2026 |
| Taxa reduzida IRC PME (primeiros €50.000) | 17% | Possível redução para 15% | Reforecast |
| Adicional de solidariedade IRS — limiar | €80.000 | Manutenção esperada | Sem alteração |
| Escalões IRS | Atualização mínima esperada (~2-3%) | Atualização anual com inflação | Aplicar a partir de 1 jan 2026 |
| Dedução específica Categoria A | €4.350,24 (4,1× IAS) | Atualização anual | Atualizar payroll |
| IAS (Indexante dos Apoios Sociais) 2026 | €522,50 em 2025 | Subir conforme atualização anual | Atualizar contribuições e benefícios |
| Tributação autónoma — viaturas | Tabela 2025 | Possíveis revisões para incentivar viaturas elétricas | Verificar tabelas 2026 |
| Benefícios fiscais — RFAI / SIFIDE | Em vigor | Possível prorrogação / revisão das percentagens | Monitorizar |

### 9.2 Fim do regime RNH legacy e IFICI

O regime de Residente Não Habitual (RNH) foi formalmente **revogado** pelo OE 2024 (Lei nº 82/2023), mantendo-se as inscrições anteriores até ao final do respetivo período de 10 anos. O contribuinte com inscrição RNH ativa em 2023 mantém o regime até **2034** no máximo. Não há novas adesões.

Em substituição, foi criado o **IFICI — Incentivo Fiscal à Investigação Científica e Inovação** (EBF Art.º 58º-A, com regulamentação em portaria), aplicável a:
- Investigadores em entidades certificadas
- Docentes do ensino superior
- Investidores em empresas certificadas
- Profissionais qualificados em "atividades de elevado valor acrescentado" certificadas

**Para 2026:** confirmar elegibilidade IFICI dos contribuintes singulares; reportar Anexo L do Modelo 3.

### 9.3 Pilar Dois (Global Minimum Tax) — MNEs

A Diretiva (UE) 2022/2523 foi transposta para o ordenamento português pela **Lei nº 41/2024** (Imposto Mínimo Complementar). Aplica-se a:
- Grupos multinacionais e grupos nacionais de grande dimensão com **volume de negócios consolidado ≥ €750 milhões** em 2 dos 4 anos anteriores
- Imposto mínimo efetivo de **15%** por jurisdição
- Componentes: IIR (Income Inclusion Rule), UTPR (Under-Taxed Profits Rule), QDMTT (Qualified Domestic Minimum Top-up Tax)

**Para 2026:** se o cliente fizer parte de grupo MNE em escala Pillar Two, exige análise específica e potencial declaração GIR (GloBE Information Return). **Skill `pt-corporate-tax` deve cobrir os detalhes; a montagem apenas sinaliza.**

### 9.4 Cripto — evolução do regime

O regime atual (CIRS Art.º 10º-A, introduzido em 2023):
- Detenção < 365 dias: Categoria G, taxa 28% (ou englobamento)
- Detenção ≥ 365 dias: exclusão (salvo emitente de paraíso fiscal)
- Staking, mining, validation: Categoria B ou E conforme natureza

**Para 2026:** monitorizar a aplicação do **Regulamento MiCA (UE)** e os requisitos de reporte da diretiva DAC8 (transposta para PT), que exigem reporte automático de transações em criptoativos pelas plataformas a partir de 2026. Os contribuintes receberão automaticamente informação no Portal das Finanças.

### 9.5 SAF-T contabilístico — submissão direta (não apenas com IES)

Está em curso a transição para submissão **mensal direta** do SAF-T contabilístico (não apenas anual com a IES). Inicialmente prevista para 2025, sucessivamente adiada. **Monitorizar Portaria atualizada** para confirmar data de entrada em vigor.

### 9.6 Pagamentos por conta para 2026

Calcular PPC IRS / IRC para 2026 com base na coleta 2025 já apurada. Lembrar que:
- PPC IRC: 80% da coleta ano anterior, dividido em 3 prestações (julho/setembro/dezembro)
- PPC IRS Categoria B: 76,5% × IRS penúltimo ano × coeficiente

### 9.7 Preços de transferência (CIRC Art.º 63º + Portaria 268/2021)

Para sociedades com operações com partes relacionadas:
- **Dossier de preços de transferência** obrigatório se volume de negócios > €3M ou operações com partes relacionadas > €100.000
- **Master file e local file** para entidades de grupos MNE
- **Anexo L da IES** — operações com partes relacionadas

### 9.8 Continuidade no e-fatura e SAF-T

Confirmar que a contabilidade e a faturação estão a alimentar o e-fatura em tempo real:
- Faturas emitidas com NIF do cliente — comunicadas em tempo real ou até dia 5 do mês seguinte
- Faturas recebidas com NIF do sujeito passivo — pré-preenchimento automático do Modelo 3
- Para Categoria B: faturas emitidas via Portal das Finanças (recibos eletrónicos) ou software certificado

## Secção 10 — Bloco de Atestação do Revisor (OCC Sign-off)

O working paper final inclui um bloco de atestação que o **Contabilista Certificado** assina antes de qualquer submissão.

```markdown
# Atestação do Revisor — Período 2025

Eu, [Nome], Contabilista Certificado membro da Ordem dos Contabilistas
Certificados (OCC) com Cédula Profissional nº [____], a atuar em
representação de [Nome do contribuinte, NIF ________], titular de seguro de
responsabilidade civil profissional válido, declaro que revi o working paper
preparado por [preparador / OpenAccountants AI], verifiquei as
reconciliações cross-skill com o cuidado profissional exigido pelo Estatuto
da OCC, e confirmo que:

  [ ] As demonstrações financeiras (sociedades) ou os elementos da
       contabilidade da Categoria B (singulares contabilidade organizada)
       em que se baseia esta declaração estão devidamente encerrados e
       assinados, e o SAF-T contabilístico foi gerado
  [ ] As correções fiscais ao resultado contabilístico (Quadro 07 do Modelo
       22 / Categoria B Modelo 3 Anexo C) estão devidamente justificadas e
       documentadas
  [ ] As tributações autónomas (Quadro 13 do Modelo 22) foram aplicadas a
       todos os encargos relevantes, com as taxas corretas e com os
       acréscimos por prejuízo onde aplicáveis
  [ ] As derramas municipal e estadual foram corretamente calculadas com
       base no município do domicílio fiscal e no escalão de lucro
       tributável
  [ ] As retenções na fonte declaradas estão suportadas por declarações dos
       substitutos tributários (Modelo 10, Modelo 39)
  [ ] As contribuições para a Segurança Social foram pagas dentro do prazo
       (ou estão devidamente regularizadas com plano)
  [ ] Os benefícios fiscais reclamados (RFAI, SIFIDE, CFEI, DLRR) estão
       documentados, com elegibilidade comprovada
  [ ] Os prejuízos fiscais reportáveis utilizados respeitam o limite de 70%
       da matéria coletável (CIRC Art.º 52º) e os prazos de reporte
  [ ] As operações com partes relacionadas estão documentadas conforme
       Portaria 268/2021 (Preços de Transferência)
  [ ] As operações com territórios offshore / paraísos fiscais estão
       sinalizadas no Anexo Q da IES
  [ ] A IES + SAF-T contabilístico anual estão preparados para submissão até
       15 julho 2026
  [ ] O pacote de comunicação ao contribuinte inclui instruções claras de
       pagamento via Multibanco / IBAN AT e prazos
  [ ] Não foi back-aplicada qualquer regra prospetiva do OE 2026 ao período
       de 2025

Assinatura: ____________________  Data: ____________________
            [Nome do CC]
Cédula Profissional OCC nº: ____________________
Sociedade de Contabilidade / Firma: ____________________
Seguro de Responsabilidade Civil — Apólice: ____________________ / Validade: __________
```

**Sem esta atestação assinada, não há submissão.**

Para o **Modelo 22 (IRC)**, a intervenção do CC é **obrigatória por lei** (CIRC Art.º 117º). Para o **Modelo 3 (IRS)** com Categoria B em contabilidade organizada, a intervenção do CC é igualmente obrigatória. Para o IRS Categoria B em regime simplificado e para o IRS sem rendimentos profissionais, o contribuinte pode submeter diretamente.

## Secção 11 — Defaults Conservadores

Quando os inputs das skills upstream forem ambíguos ou estiverem em falta, aplicar os seguintes defaults e sinalizar para o revisor:

**Tabela de defaults conservadores**

| Situação | Default conservador |
| --- | --- |
| Reconciliação cross-skill difere > €1 | Sinalizar como "Necessita Input"; não arredondar silenciosamente |
| Coeficiente regime simplificado Categoria B ambíguo (entre dois CAE) | Aplicar o **coeficiente mais alto** (menos favorável ao contribuinte); sinalizar |
| Classificação PME / não-PME para taxa reduzida IRC 17% borderline | Aplicar taxa geral 21% sobre TODO o lucro; sinalizar para revisão de elegibilidade PME (DL 372/2007) |
| Município de domicílio fiscal incerto (mudança a meio do ano) | Aplicar a derrama municipal mais alta possível; sinalizar para o revisor |
| Despesa de representação ou ajuda de custo sem documentação adequada | Tratar como TA aplicável; sinalizar |
| Operação com paraíso fiscal sem comprovativo de substância | Aplicar limitação CIRC Art.º 23º-A (não dedutível); sinalizar |
| Crédito por dupla tributação sem comprovativo de imposto pago no estrangeiro | Excluir o crédito; sinalizar para obtenção de comprovativo |
| Prejuízo fiscal reportável sem prova de origem (sociedades) | Excluir; sinalizar para reconstituição |
| RNH / IFICI sem inscrição confirmada no Portal das Finanças | Tratar como regime geral; sinalizar para regularização |
| RFAI / SIFIDE sem documentação técnica e financeira | Excluir o benefício; sinalizar para preparação do dossier |
| Operações intracomunitárias sem VIES check | Sinalizar; pode haver inversão do sujeito passivo aplicável ou IVA português |
| Mais-valia em cripto sem registo de data de aquisição | Tratar como detenção < 365 dias (Categoria G, 28%); sinalizar |
| IBAN do contribuinte em falta (reembolso) | Sinalizar para obtenção; sem IBAN, reembolso atrasa |
| Cessação de atividade declarada no ano sem regularização do IVA | Sinalizar para regularização das existências (IVA Art.º 24º) |
| Pagamentos por conta efetuados mas sem comprovativo | Excluir do crédito; sinalizar para reconciliação com extrato AT |
| Dúvida entre englobamento e taxa liberatória (CIRS Art.º 22º) | Apresentar simulação dos dois cenários no brief; deixar decisão ao revisor |
| Regime de transparência fiscal aplicável incerto | Aplicar o regime que produz tributação superior (conservador); sinalizar |
| OE 2026 aplicado ao ano 2025 | Rejeitar; 2025 usa regras OE 2025; OE 2026 aplica-se desde 1 jan 2026 |

- **Regra de tolerância (reforço)** — Tolerância de €1. Qualquer discrepância superior é escalada, não absorvida.

## Secção 12 — Catálogo de Recusas

- **R-PT-ASM-1** — Skill upstream não correu. Nomear a skill em falta. Continuar com os dados disponíveis; sinalizar a lacuna; não fabricar a computação em falta.
- **R-PT-ASM-2** — Auto-verificação upstream falhou. Registar a verificação específica; continuar mas sinalizar.
- **R-PT-ASM-3** — Reconciliação cross-skill > €1. Levantar como "Necessita Input"; não arredondar silenciosamente.
- **R-PT-ASM-4** — Declaração já submetida no Portal das Finanças e o pedido é submeter declaração nova "em cima". Recusar e explicar o procedimento de declaração de substituição (CIRS Art.º 59º / CIRC Art.º 122º). Produzir o working paper da substituição se solicitado, com indicação clara de que se trata de substituição.  _(CIRS Art.º 59º / CIRC Art.º 122º)_
- **R-PT-ASM-5** — Falta de Contabilista Certificado quando obrigatório. Para Modelo 22 IRC (todas as sociedades) e para IRS Categoria B em contabilidade organizada, a intervenção do CC é obrigatória por lei (CIRC Art.º 117º; CIRS regulamentação). Sinalizar como bloqueador; não submeter sem CC. Idem para sociedades com volume de negócios > €200.000 que não tenham CC vinculado.  _(CIRC Art.º 117º)_
- **R-PT-ASM-6** — Inconsistências entre Modelo 3 e Modelo 22 do mesmo contribuinte. Sócio-gerente que receba pró-labore deve aparecer simultaneamente no Modelo 22 da sociedade (gasto com pessoal) e no Modelo 3 do próprio (Categoria A). Se houver inconsistência > €1, levantar para reconciliação antes de submeter qualquer das duas declarações.
- **R-PT-ASM-7** — Fora do âmbito: regime fiscal de Zona Franca da Madeira (ZFM) Centro Internacional de Negócios, isenções IRC específicas para entidades com determinados estatutos especiais (cooperativas em certos regimes, IPSS), companhias de seguros e instituições de crédito (regimes especiais CIRC), atividades petrolíferas, jogos e apostas (regime especial), tributação de fundos de investimento e SGPS (regimes específicos). Encaminhar para especialista; não tentar.
- **R-PT-ASM-8** — Fora do âmbito: não-residentes fiscais sem estabelecimento estável em PT, residentes que mudaram durante o ano, expatriados com obrigações em múltiplas jurisdições, Permanent Establishment determinação ao abrigo de CDT. Encaminhar para especialista internacional; esta skill assume residência fiscal portuguesa anual completa.
- **R-PT-ASM-9** — Fora do âmbito: contencioso tributário, reclamações graciosas, impugnações judiciais, recursos hierárquicos, ações junto do CAAD (Centro de Arbitragem Administrativa), defesa em inspeção tributária. Encaminhar para advogado fiscalista / consultor fiscal com prática contenciosa.
- **R-PT-ASM-10** — Intake incompleto. Nomear o campo de intake em falta (NIF, NIPC, NISS, CAE, residência fiscal, regime de IVA, etc.). Não é possível finalizar a declaração até ser fornecido.
- **R-PT-ASM-11** — Pedido para submeter diretamente no Portal das Finanças. Esta skill produz um working paper. A submissão é ação do contribuinte ou do CC (no portal do CC), após revisão e atestação. Recusar educadamente; fornecer as instruções de submissão.
- **R-PT-ASM-12** — Aplicação retroativa de regras OE 2026 ao ano 2025. As datas de entrada em vigor governam; não retro-aplicar taxas / limiares 2026 a declarações 2025. Recusar educadamente; explicar regras transitórias.
- **R-PT-ASM-13** — Fora do âmbito: regimes setoriais especiais (banca, seguros, exploração de jogos, atividades extrativas, agricultura e silvicultura com regime especial), regime das SIIMI / OIC, regime das SGPS, fusões/cisões com regime de neutralidade fiscal complexa, reorganizações empresariais transfronteiriças, fiscalidade verde (carbono, plástico). Encaminhar para especialista.
- **R-PT-ASM-14** — Pedido envolve criptografia / NFTs / DeFi com perfil ambíguo. Sinalizar para análise especializada (skill `portugal-crypto-tax` deve cobrir os casos standard; perfis complexos exigem opinião escrita).

## Secção 13 — Auto-verificações

- **Verificação PT-ASM-1** — Todas as skills upstream exigidas para o tipo de declaração escolhido produziram output, ou a lacuna está sinalizada.
- **Verificação PT-ASM-2** — O volume de negócios reconcilia entre `portugal-bookkeeping`, `portugal-vat-return`, e a skill de imposto sobre rendimento aplicável (`pt-income-tax` / `pt-corporate-tax`) dentro de €1.
- **Verificação PT-ASM-3** — As retenções na fonte declaradas (Anexo A / Anexo B / Modelo 22 campo 359) estão suportadas por Modelo 10 / Modelo 39 dos substitutos tributários; cada retenção tem comprovativo.
- **Verificação PT-ASM-4** — A soma das 12 DMR mensais (parte fiscal) reconcilia com o Modelo 10 anual; o Anexo A do Modelo 3 dos colaboradores é coerente.
- **Verificação PT-ASM-5** — TSU empregador + colaboradores pagas até dia 20 do mês seguinte; nenhuma em mora; certidão de não-dívida da Segurança Social verificada.
- **Verificação PT-ASM-6** — Pro-rata IVA definitivo (se aplicável) calculado e Anexo R do Modelo C com regularizações apresentado.
- **Verificação PT-ASM-7** — SAF-T faturação anual reconcilia com a contabilidade (volume de negócios e IVA liquidado).
- **Verificação PT-ASM-8** — Tributações autónomas (Quadro 13 do Modelo 22) calculadas com as taxas corretas, com acréscimo de 10 pp em caso de prejuízo, e adicionadas à coleta no Campo 365.
- **Verificação PT-ASM-9** — Derrama municipal aplicada com taxa do município do domicílio fiscal; Anexo A do Modelo 22 preenchido. Derrama estadual aplicada por escalões se lucro tributável > €1.500.000.
- **Verificação PT-ASM-10** — Adicional de solidariedade IRS aplicado por escalão se rendimento coletável > €80.000.
- **Verificação PT-ASM-11** — Coeficientes do regime simplificado Categoria B aplicados corretamente conforme CAE (CIRS Art.º 31º — 0,15 / 0,75 / 0,35 / 0,95 / 0,30 / 1,00 consoante atividade).  _(CIRS Art.º 31º)_
- **Verificação PT-ASM-12** — Prejuízos fiscais reportáveis (CIRC Art.º 52º) utilizados dentro do limite de 70% da matéria coletável e dentro dos prazos de reporte (5 anos / 12 anos PME até 2023 / 5 anos a partir de 2024).  _(CIRC Art.º 52º)_
- **Verificação PT-ASM-13** — Benefícios fiscais (RFAI, SIFIDE, CFEI, DLRR) declarados no Anexo D do Modelo 22, com limites respeitados (RFAI: até 25% do investimento + 50% da coleta; SIFIDE: dedução até concorrência da coleta + reporte 8 anos).
- **Verificação PT-ASM-14** — Prazos explícitos na lista de ações: 5 jan (SAF-T), 10 jan (DMR), 31 jan (DRI/Modelo 39), 10 fev (Modelo 10 / IVA mensal), 20 fev (IVA trimestral), 31 mai (Modelo 22), 30 jun (Modelo 3), 15 jul (IES).
- **Verificação PT-ASM-15** — Fluxo Portal das Finanças descrito: submissão → nota de liquidação → referência Multibanco → pagamento → comprovativo.
- **Verificação PT-ASM-16** — Período de conservação de documentos (10 anos LGT + Código Comercial; 4 anos caducidade tributária) declarado.
- **Verificação PT-ASM-17** — Brief do revisor contém referências legais para cada posição adotada (CIRS, CIRC, CIVA, LGT, EBF, Portarias).
- **Verificação PT-ASM-18** — Para sociedades: CC obrigatório identificado, com Cédula Profissional ativa e seguro RC. Para Categoria B contabilidade organizada: CC identificado.
- **Verificação PT-ASM-19** — Notas de planeamento 2026 (OE 2026, fim RNH legacy, IFICI, Pilar Dois, DAC8 cripto, evolução SAF-T) incluídas no brief; regras prospetivas NÃO back-aplicadas.
- **Verificação PT-ASM-20** — IBAN PT do contribuinte registado no Portal das Finanças para reembolso (se aplicável); confirmado coincidir com a titularidade do NIF.

## Secção 14 — Output Files (PDF / Excel package)

O output final é um conjunto de três ficheiros, colocados em `/mnt/user-data/outputs/`:

1. `[slug_contribuinte]_2025_pt_master.xlsx` — Master workbook. Folhas:
   - Cover (identificação)
   - Identidade & regime fiscal
   - Modelo 3 (se aplicável) — todos os Anexos preenchidos linha a linha
   - Modelo 22 (se aplicável) — Quadros 01 a 13 + Anexos A/B/C/D/E
   - IES — Anexos A/L/Q/R principais
   - Apuramento de IRC / IRS (memória de cálculo)
   - Mapa de depreciações (Modelo 32)
   - Reconciliação SAF-T ↔ contabilidade ↔ IVA
   - Reconciliação DMR ↔ Modelo 10 ↔ folha salarial
   - Reconciliação cross-skill (síntese das 9 verificações)
   - Calendário 2026 — pagamentos por conta + obrigações declarativas
   - Tracker de comprovativos de pagamento (Multibanco / IBAN)
   - Sinalizações para o revisor
   Usar fórmulas vivas onde possível; verificar ausência de `#REF!`.

2. `reviewer_brief.md` — Ficheiro markdown com todo o conteúdo da Secção 4 (estrutura do working paper para o CC), com os blocos headline da Secção 5 e o bloco de atestação da Secção 10.

3. `taxpayer_action_list.md` — Ficheiro markdown com a lista de ações da Secção 8, mais o bloco de instruções de pagamento da Secção 6 e o bloco de instruções de submissão da Secção 7.

Os três ficheiros são apresentados ao utilizador no final.

Se a execução esgotar o contexto a meio da construção, completar primeiro o trabalho de cálculo / reconciliação e produzir os outputs formatados que forem possíveis, indicando claramente quais os deliverables que ficaram parciais.

## Secção 15 — Limitações Conhecidas + Change Log

### 15.1 Limitações conhecidas

1. O preenchimento direto dos PDFs oficiais da AT não é automatizado; o CC ou o contribuinte introduz os valores no Portal das Finanças usando o working paper como guia.
2. O Portal das Finanças aceita ficheiros XML normalizados gerados por software de contabilidade certificado pela AT; esta skill não gera o XML — gera os valores que alimentam o XML.
3. Demonstrações financeiras (SNC, NCM, NCM-ME) são geradas pelas skills `portugal-financial-statements` e `portugal-bookkeeping`; a montagem apenas confirma a sua existência e consistência.
4. Dossier completo de Preços de Transferência (Master File + Local File ao abrigo da Portaria 268/2021) não é assembled aqui; carece skill própria para volumes complexos.
5. Regimes setoriais especiais (banca, seguros, jogos, ZFM Madeira CINM, OIC, SGPS, agricultura) estão fora do âmbito.
6. Pilar Dois (Lei nº 41/2024) — apenas sinalização para entidades em grupos MNE ≥ €750M; a declaração GIR carece skill própria.
7. Country-by-Country Report (Anexo H da IES + reporte específico) está fora do âmbito de assemblagem aqui.
8. As regras prospetivas do OE 2026 poderão sofrer alterações até promulgação final; toda regra prospetiva neste skill deve ser re-verificada contra a Lei do OE 2026 quando publicada em Diário da República.
9. Submissão automática no Portal das Finanças via webservice não é executada pela skill — fica a cargo do CC / contribuinte.
10. Comunicações de e-fatura mensais ocorrem em paralelo durante o ano, não no momento da montagem; a skill apenas confirma que o e-fatura está em dia.
11. Cripto DeFi avançado (LP tokens, yield farming, NFTs, DAOs) pode exceder o enquadramento padrão do CIRS Art.º 10º-A; a skill `portugal-crypto-tax` cobre casos standard.
12. A skill assume um único CC vinculado; se houver mudança de CC durante o exercício, há obrigações de comunicação ao Portal das Finanças que ficam fora do âmbito desta capstone.

### 15.2 Change log

- v1.0 (2026-05): Versão inicial. Modelada sobre `ng-return-assembly`, `id-return-assembly`, `mt-return-assembly` e `us-ca-return-assembly`. Adaptada para Modelo 3 IRS + Anexos, Modelo 22 IRC + Anexos, IES, SAF-T (PT), DMR/DRI, declaração periódica de IVA, submissão via Portal das Finanças, pagamento Multibanco/IBAN AT, e impacto prospetivo do OE 2026. Coordena 11 skills upstream Portugal (foundation, pt-income-tax, pt-nhr-ifici, pt-foreign-source-treaties, pt-corporate-tax, portugal-vat-return, pt-social-contributions, portugal-payroll, portugal-bookkeeping, portugal-financial-statements, portugal-crypto-tax). Atestação requer Contabilista Certificado membro da OCC.

## Secção 16 — Fontes

**Tabela de fontes**

| Fonte | Referência |
| --- | --- |
| Código do IRS (CIRS) — Decreto-Lei nº 442-A/88, de 30 novembro, com sucessivas alterações | Tributação singular; Art.º 22º (englobamento), 31º (regime simplificado), 59º (substituição), 60º (prazo Modelo 3), 68º (taxas gerais), 78º (deduções à coleta), 81º (CDT), 102º (PPC), 119º (DMR) |
| Código do IRC (CIRC) — Decreto-Lei nº 442-B/88, de 30 novembro, com sucessivas alterações | Tributação societária; Art.º 6º (transparência fiscal), 8º (período de tributação), 18º (regime de acréscimo), 23º-A (despesas não dedutíveis / paraísos fiscais), 28º a 39º-A (provisões e ajustamentos), 51º (participation exemption), 52º (prejuízos fiscais), 63º (preços de transferência), 67º (limitação dedução de juros), 73º (neutralidade fusões), 86º-A e seguintes (regime simplificado IRC), 87º (taxa geral 21%, taxa PME 17%), 87º-A (derrama estadual), 88º (tributações autónomas), 91º (CDT), 105º (PPC), 117º (intervenção do CC), 120º (prazo Modelo 22), 121º (IES), 122º (substituição) |
| Código do IVA (CIVA) — Decreto-Lei nº 394-B/84, de 26 dezembro, com sucessivas alterações | IVA; Art.º 9º (isenções), 23º (pro-rata), 24º (regularização ativos fixos), 53º (regime de isenção pequenos sujeitos passivos), 60º (regime forfetário), 41º a 44º (declarações periódicas) |
| Lei Geral Tributária (LGT) — Decreto-Lei nº 398/98, de 17 dezembro | Caducidade (Art.º 45º — 4 anos / 12 anos prejuízos), prescrição, juros compensatórios (Art.º 35º), conservação de documentos (Art.º 123º) |
| Regime Geral das Infrações Tributárias (RGIT) — Lei nº 15/2001 | Coimas: Art.º 114º (falta de pagamento), 116º (falta declaração), 117º (atraso DMR / SAF-T), 29º (atenuação por regularização espontânea) |
| Código Contributivo — Lei nº 110/2009, de 16 setembro | TSU, contribuições independentes, isenções, DRI, taxas reduzidas |
| Estatuto dos Benefícios Fiscais (EBF) — Decreto-Lei nº 215/89 | RFAI, SIFIDE, DLRR, CFEI II, IFICI (Art.º 58º-A), benefícios setoriais |
| Lei das Finanças Locais — Lei nº 73/2013 | Derrama municipal (até 1,5%) |
| Código Comercial Art.º 40º + Decreto-Lei nº 36/2017 | Conservação de livros 10 anos |
| Lei nº 82/2023 (OE 2024) | Revogação do regime RNH (com manutenção dos inscritos até 2034) |
| Lei nº 45-A/2024 (OE 2025) | Atualizações 2025 |
| Lei nº 41/2024 | Imposto Mínimo Complementar — Pilar Dois (Diretiva (UE) 2022/2523) |
| Portaria nº 321-A/2007 e Portaria nº 302/2016 (SAF-T) | Estrutura SAF-T (PT) |
| Portaria nº 195/2020 (e-fatura) | Comunicação mensal de faturação |
| Portaria nº 268/2021 (Preços de Transferência) | Dossier obrigatório, Master File, Local File |
| Decreto-Lei nº 372/2007 | Definição de PME |
| Decreto-Lei nº 72/2017 (com alterações) | Incentivo à contratação de jovens (TSU reduzida) |
| Portal das Finanças — Autoridade Tributária e Aduaneira | https://www.portaldasfinancas.gov.pt |
| Portal e-fatura | https://faturas.portaldasfinancas.gov.pt |
| Segurança Social Direta | https://www.seg-social.pt |
| Ordem dos Contabilistas Certificados (OCC) | https://www.occ.pt |
| Diário da República Eletrónico | https://dre.pt |
| Versão da skill | 1.0 |

## Disclaimer final

OpenAccountants — skills de contabilidade open-source para IA
Isto não constitui aconselhamento fiscal. Todos os outputs devem ser revistos e assinados por um Contabilista Certificado (membro da OCC — Ordem dos Contabilistas Certificados) com Cédula Profissional ativa e seguro de responsabilidade civil profissional, antes de submissão no Portal das Finanças, no portal da Segurança Social Direta, ou em qualquer outra plataforma oficial.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your jurisdiction — no liability on either side until you and the accountant sign a formal engagement letter — book a free 30-minute call:

→ [Book a call](https://calendly.com/openaccountants-info/30min)

We'll route you to the named verifier covering your country or state. You can also see the full list of verified accountants at [openaccountants.com/network](https://openaccountants.com/network).
