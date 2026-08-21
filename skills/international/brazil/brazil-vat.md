---
name: brazil-vat
description: Use this skill whenever asked about Brazilian indirect taxes, VAT, consumption taxes, PIS, COFINS, ICMS, ISS, IPI, CBS, IBS, Imposto Seletivo, NF-e (Nota Fiscal Eletronica), Simples Nacional, CNPJ registration, tax reform (EC 132/2023), or any request involving Brazilian goods and services taxation, filing, compliance, or classification. Trigger on phrases like "Brazil tax", "Brazilian VAT", "PIS/COFINS", "ICMS", "ISS", "IPI", "CBS", "IBS", "NF-e", "nota fiscal", "Simples Nacional", "CNPJ", "tax reform Brazil", or any request involving Brazilian indirect tax compliance. This skill contains the complete Brazilian indirect tax framework covering both the current multi-tax system (PIS/COFINS/ICMS/ISS/IPI) and the new unified system (CBS/IBS/IS) under Constitutional Amendment 132/2023. ALWAYS read this skill before touching any Brazilian indirect tax work.
version: 2.0
jurisdiction: BR
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Ariane Marrocos
review_status: current
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Brazil VAT

## Brasil — Tributos Indiretos (Sistema Antigo PIS/Cofins/ICMS/IPI/ISS + Sistema Novo CBS/IBS) — Skill v3.0

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **Ariane Marrocos** on 2026-06-03.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### Tributos Indiretos (PIS-Cofins-

- **PIS não cumulativo (Lucro Real)** — 1,65% sobre o total das receitas auferidas pela pessoa jurídica, com créditos previstos no art. 3º da Lei nº 10.637/2002; aplicável predominantemente a Lucro Real percent  _(Lei 10.637/2002)_
- **Cofins não cumulativo** — 7,60% incidente sobre o total das receitas auferidas pela pessoa jurídica, admitindo créditos previstos no art. 3º da Lei nº 10.833/2003 percent  _(Lei 10.833/2003)_
- **PIS+Cofins não cumulativo combinado** — 9,25% (com créditos de entrada) percent  _(Leis 10.637/10.833)_
- **PIS cumulativo (Lucro Presumido)** — 0,65% sobre receita bruta, sem direito a créditos, aplicável em regra às pessoas jurídicas tributadas pelo Lucro Presumido percent  _(Lei nº 10.637/2002 instituiu a sistemática não cumulativa do PIS. Principal fundamento: Lei nº 9.718/1998)_
- **Cofins cumulativo** — 3,00% sobre receita bruta, sem direito a créditos, aplicável em regra às pessoas jurídicas tributadas pelo Lucro Presumido percent  _(Lei nº 10.833/2003 (Art. 1º base de cálculo; Art. 2º alíquota 7,6%; Art. 3º créditos); Principal fundamento: Lei nº 9.718/1998)_
- **PIS+Cofins cumulativo combinado** — 3,65% (sem créditos) percent  _(Lei nº 10.637/2002; Lei nº 10.833/2003; Lei nº 9.718/1998; Lei nº 9.715/1998)_
- **Sao Paulo** — 18%
- **Rio de Janeiro (RJ)** — A alíquota interna geral do ICMS no Estado do Rio de Janeiro é de 20%, acrescida em regra do adicional de 2% destinado ao FECP, resultando em carga tributária geral de 22%. percent  _(Lei Estadual nº 2.657/1996 Art. 14; Lei Estadual nº 10.253/2023; LC Estadual nº 210/2023)_
- **Minas Gerais** — 18%
- **Bahia (BA)** — A alíquota interna geral do ICMS no Estado da Bahia é de 20,5%, conforme a Lei nº 14.629/2023, aplicável quando não houver previsão de alíquota específica percent  _(Lei nº 7.014/1996; Lei nº 14.629/2023)_
- **Paraná (PR)** — A alíquota interna geral do ICMS no Estado do Paraná é de 19,5%, aplicável quando não houver previsão específica, conforme o art. 17, inciso V, do RICMS/PR percent  _(RICMS/PR Art. 17, inciso V; Lei nº 11.580/1996)_
- **Rio Grande do Sul (RS)** — 17%
- **Santa Catarina (SC)** — 17%
- **Sul/Sudeste → Sul/Sudeste (exceto ES)** — 12% percent  _(CF Art. 155; Resolução SF 22/89)_
- **South/Southeast to North/Northeast/Center-West/ES** — 7%
- **N/NE/CO/ES → qualquer estado** — Nas operações interestaduais originadas nos estados das regiões Norte, Nordeste, Centro-Oeste e no Espírito Santo, aplica-se, como regra geral, a alíquota interestadual de 12% percent  _(Constituição Federal de 1988; Resolução do Senado Federal nº 22/1989; CF Art. 155)_
- **Mercadorias importadas (interestadual)** — Aplica-se a alíquota interestadual de 4% às operações com bens e mercadorias importados do exterior ou com conteúdo de importação superior a 40%, observadas as exceções previstas na Resolução do Senado Federal nº 13/2012 percent  _(Resolução do Senado Federal nº 13/2012; Lei Complementar nº 87/1996)_
- **Alíquota ISS** — 2% a 5% (definida por município, mínimo 2%) percent  _(LC 116/2003; LC 157/2016)_
- **Alíquota IPI** — 0% a 300%+ (por NCM via tabela TIPI). As alíquotas do IPI são definidas por NCM na TIPI, variando conforme o produto, observadas as regras do RIPI percent  _(Decreto nº 7.212/2010 (RIPI); TIPI - Tabela de Incidência do IPI)_
- **CBS alíquota-teste 2026** — 0,9% percent  _(EC 132/2023; LC 214/2025)_
- **IBS alíquota-teste 2026** — 0,1% percent  _(EC 132/2023; LC 214/2025)_
- **CBS+IBS estimada (plena)** — ~26,5% (sujeita a ajuste), podendo sofrer ajustes conforme os mecanismos de revisão previstos na Reforma Tributária e na LC nº 214/2025 percent  _(Emenda Constitucional nº 132/2023; Lei Complementar nº 214/2025)_
- **CBS plena (extinção PIS/Cofins)** — A partir de 2027, a CBS passa a substituir o PIS/Pasep e a COFINS, que serão extintos, conforme as regras de transição estabelecidas pela EC nº 132/2023 e regulamentadas pela LC nº 214/2025  _(Emenda Constitucional nº 132/2023; Lei Complementar nº 214/2025)_
- **ICMS/ISS totalmente extintos** — O ICMS e o ISS serão gradualmente substituídos pelo IBS durante o período de transição da Reforma Tributária, sendo totalmente extintos em 2033  _(Emenda Constitucional nº 132/2023; Lei Complementar nº 214/2025)_
- **MEI** — Até R$ 81.000/ano BRL  _(LC 123/2006)_
- **Sublimite ICMS/ISS** — O sublimite para recolhimento de ICMS e ISS no âmbito do Simples Nacional é de R$ 3.600.000,00 BRL  _(Lei Complementar nº 123/2006 Arts. 19 e 20)_
- **Limite EPP** — R$ 4.800.000 BRL  _(LC 123/2006 Art. 3)_

## Seção 1 — Referência rápida

**Leia esta seção inteira antes de classificar qualquer transação. O Brasil NÃO possui um IVA unificado. Possui cinco tributos indiretos em três níveis de governo, atualmente em processo de reforma para um IVA dual (CBS+IBS) com adição de um Imposto Seletivo (IS).**

**Tabela de referência rápida**

| Campo | Valor |
| --- | --- |
| País | República Federativa do Brasil |
| Sistema tributário (atual) | Cinco tributos indiretos principais: PIS, Cofins, ICMS, ISS, IPI |
| Sistema tributário (novo, em transição) | CBS + IBS + Imposto Seletivo (IS), sob EC 132/2023, LC 214/2025 e LC 227/2026 |
| Período de transição | 2026 a 2032; sistema novo plenamente vigente em 1º de janeiro de 2033 |
| Alíquota PIS (não cumulativo / Lucro Real) | 1,65% sobre a receita bruta |
| Alíquota PIS (cumulativo / Lucro Presumido) | 0,65% sobre a receita bruta |
| Alíquota Cofins (não cumulativo / Lucro Real) | 7,60% sobre a receita bruta |
| Alíquota Cofins (cumulativo / Lucro Presumido) | 3,00% sobre a receita bruta |
| PIS+Cofins combinados (não cumulativo) | 9,25% (com créditos de entrada) |
| PIS+Cofins combinados (cumulativo) | 3,65% (sem créditos, tributo em cascata) |
| Alíquota geral ICMS | 17% a 23% por estado (interno); 4%, 7% ou 12% (interestadual) |
| Alíquota ISS | 2% a 5% (definida por cada município, mínimo 2% — LC 157/2016) |
| Alíquota IPI | 0% a 300%+ (específica por produto via tabela TIPI, por NCM) |
| Alíquota CBS (transição 2026) | 0,9% (alíquota-teste em paralelo a PIS/Cofins) |
| Alíquota IBS (transição 2026) | 0,1% (alíquota-teste em paralelo a ICMS/ISS) |
| Alíquota CBS+IBS estimada (plena implementação) | ~26,5% (não definitiva, sujeita a ajuste regulamentar) |
| Nota fiscal eletrônica | NF-e (Modelo 55, mercadorias); NFS-e (serviços); NFC-e (Modelo 65, varejo ao consumidor); CT-e (Modelo 57, transporte) |
| Portal de envio (federal) | https://www.gov.br/receitafederal (Receita Federal) |
| Portal de envio (estadual) | Portal da SEFAZ de cada estado |
| Portal de envio (municipal) | Portal de NFS-e de cada município |
| Moeda | BRL (Real brasileiro) |
| Identificador | CNPJ (formato XX.XXX.XXX/YYYY-ZZ) |
| Legislação primária | Constituição Federal Arts. 153-156; LC 87/1996 (ICMS — Lei Kandir); Lei 10.637/2002 (PIS); Lei 10.833/2003 (Cofins); LC 116/2003 (ISS); LC 157/2016 (alíquota mínima ISS); Decreto 7.212/2010 (RIPI); LC 123/2006 (Simples Nacional); EC 132/2023; LC 214/2025; LC 227/2026 |
| Contribuidor | Open Accounting Skills Registry |
| Validado por | Pendente — requer assinatura de contador brasileiro registrado no CRC |
| Versão da skill | 3.0 |

**Alíquotas-chave do sistema atual em um relance**

| Tributo | Esfera | Alíquota | Gera crédito? |
| --- | --- | --- | --- |
| PIS (não cumulativo) | Federal | 1,65% | Sim |
| Cofins (não cumulativo) | Federal | 7,60% | Sim |
| PIS (cumulativo) | Federal | 0,65% | Não |
| Cofins (cumulativo) | Federal | 3,00% | Não |
| ICMS (interno, geral) | Estadual | 17% a 23% por estado | Sim (débito/crédito) |
| ICMS (interestadual, S/SE para N/NE/CO) | Estadual | 7% | Sim |
| ICMS (interestadual, demais) | Estadual | 12% | Sim |
| ICMS (mercadorias importadas com >40% conteúdo estrangeiro) | Estadual | 4% (Resolução SF 13/2012) | Sim |
| ISS | Municipal | 2% a 5% | Não (cumulativo, em cascata) |
| IPI | Federal | Específica por NCM (TIPI) | Sim (na cadeia industrial) |

**Faixa de alíquotas internas de ICMS por estado (amostra principal)**

| Estado | Alíquota interna padrão |
| --- | --- |
| São Paulo (SP) | 18% |
| Rio de Janeiro (RJ) | 20% (18% + FECP 2%) |
| Minas Gerais (MG) | 18% |
| Bahia (BA) | 19% |
| Paraná (PR) | 19% |
| Rio Grande do Sul (RS) | 17% |
| Santa Catarina (SC) | 17% |
| Demais estados | 17% a 20% (média) |
| Estados com adicional FECP/FECOEP | Acrescentar 1% a 4% conforme estado e produto |

**Matriz de alíquotas interestaduais de ICMS**

| Rota | Alíquota |
| --- | --- |
| Sul/Sudeste para Sul/Sudeste (exceto ES) | 12% |
| Sul/Sudeste (exceto ES) para Norte/Nordeste/Centro-Oeste/ES | 7% |
| Norte/Nordeste/Centro-Oeste/ES para qualquer estado | 12% |
| Mercadorias importadas (qualquer interestadual) | 4% |

A EC 132/2023 substitui PIS+Cofins pela CBS (federal), e ICMS+ISS pelo IBS (estadual + municipal compartilhado). A LC 214/2025 regulamenta a primeira fase. A LC 227/2026 (segunda fase, janeiro de 2026) detalha o Comitê Gestor do IBS e regras de partilha. O Imposto Seletivo (IS) tributa bens e serviços específicos prejudiciais à saúde ou ao meio ambiente.

**Cronograma detalhado da transição**

| Ano | Evento |
| --- | --- |
| 2026 | Fase de teste. As notas fiscais devem trazer CBS (0,9%) + IBS (0,1%) = 1% simbólico. O pagamento fica suspenso por 3 meses sem multa após a publicação dos regulamentos. |
| 2027 | CBS plenamente vigente. PIS e Cofins extintos. IPI extinto (com exceções limitadas para a Zona Franca de Manaus). |
| 2028 | CBS plena; IPI residual apenas para ZFM. |
| 2029 | IBS começa cobrança gradual, com redução proporcional de ICMS/ISS. |
| 2030 a 2032 | Aumento progressivo do IBS e redução do ICMS/ISS, em escala anual. |
| 2033 | Transição completa. ICMS, ISS, PIS, Cofins, IPI todos eliminados. Sistema Dual VAT pleno: CBS (federal) + IBS (subnacional) + IS (seletivo). |

- **MEI (Microempreendedor Individual):** continua isento de IBS/CBS.
- **Simples Nacional:** permanece com opção de regime híbrido (art. 21-A da LC 123/2006, incluído pela LC 214/2025) — permitindo recolher CBS/IBS separadamente para transferir créditos aos clientes adquirentes que estejam fora do Simples.
- **Zona Franca de Manaus (ZFM):** mantém regime diferenciado de IPI residual e fundo de compensação previsto na EC 132/2023.

Todas as regras relativas à reforma estão marcadas como de julgamento exigido do revisor, pois os regulamentos ainda estão sendo publicados pelo Comitê Gestor do IBS, pela Receita Federal e pelo CONFAZ.

**Limites do Simples Nacional**

| Faixa de receita (BRL, últimos 12 meses) | Elegibilidade |
| --- | --- |
| Até BRL 81.000 | MEI (Microempreendedor Individual) — regime simplificado |
| Até BRL 3.600.000 | Sublimite estadual/municipal — ICMS e ISS dentro do DAS |
| Acima de BRL 3.600.000 até BRL 4.800.000 | Permanece no Simples para tributos federais; ICMS e ISS recolhidos fora do DAS conforme regras estaduais e municipais (LC 123/2006, Art. 13, §1º, e Art. 18) |
| Acima de BRL 4.800.000 | Deve utilizar Lucro Presumido ou Lucro Real |

**Defaults conservadores — específicos do Brasil**

| Ambiguidade | Default |
| --- | --- |
| Regime tributário desconhecido | Lucro Presumido (PIS/Cofins cumulativos, sem créditos) |
| Alíquota de ICMS desconhecida | Maior alíquota interna plausível para o estado (conservador) |
| Alíquota de ISS desconhecida | 5% (máximo legal) |
| Não se sabe se é Simples Nacional | Não é Simples Nacional (aplicar alíquotas plenas) |
| Elegibilidade de crédito de PIS/Cofins desconhecida | Não creditável |
| ICMS-ST aplicável desconhecido | Presumir que não está sujeito a ST (sinalizar para revisor) |
| Interestadual ou interno desconhecido | Interno (aplicar alíquota interna) |
| Operação com serviço ou mercadoria desconhecida | Mercadoria (ICMS, alíquota maior) |
| Código NCM desconhecido para IPI | 0% IPI (conservador para o comprador; sinalizar para revisor) |
| Proporção de uso empresarial desconhecida | 0% de recuperação |
| Não se sabe se a transação está no escopo | Dentro do escopo |
| Classificação CNAE desconhecida | Serviços (ISS) |
| Rota interestadual desconhecida | 7% (mais conservador para fins de crédito) |

**Limiares de alerta (red flag)**

| Limiar | Valor |
| --- | --- |
| ALTO — valor de transação individual | BRL 50.000 |
| ALTO — delta tributário de um default conservador | BRL 5.000 |
| MÉDIO — concentração de contraparte | >40% do output OU input |
| MÉDIO — número de defaults conservadores | >4 ao longo da apuração |
| BAIXO — posição líquida absoluta de tributo | BRL 100.000 |

## Seção 2 — Entradas obrigatórias e catálogo de recusas

### Entradas obrigatórias

**Mínimo viável** — extrato bancário do mês em PDF, CSV, OFX ou texto colado. Deve cobrir o período integralmente. Aceitável de qualquer banco brasileiro: Banco do Brasil, Itaú Unibanco, Bradesco, Santander Brasil, Caixa Econômica Federal, Nubank, Inter, BTG Pactual, Sicoob, ou qualquer outro. Os XMLs de NF-e são fortemente preferíveis para verificação de créditos de ICMS e PIS/Cofins.

**Recomendado** — arquivos XML de NF-e para todas as vendas e compras (ou o arquivo SPED Fiscal do mês), CNPJ e inscrição estadual/municipal, comprovantes de pagamento de DARF/DAS do mês anterior, declaração de opção pelo Simples Nacional (se aplicável), regime tributário confirmado (Simples / Lucro Presumido / Lucro Real), tipo de atividade (serviços / mercadorias / industrialização) e códigos CNAE.

**Ideal** — download completo de NF-e via portal da SEFAZ, arquivo SPED Fiscal, EFD-Contribuições (PIS/Cofins), DCTF, apurações de períodos anteriores, cartão CNPJ com todas as inscrições, ledger de créditos de ICMS, registros de retenção de ISS, XMLs de NF-e/NFS-e.

**Política de recusa em caso de falta do mínimo — SOFT WARN.** Se não houver nem extrato bancário nem XMLs de NF-e, parada absoluta. Se houver apenas extrato bancário sem NF-e: prosseguir, mas registrar no informe ao revisor: "Esta apuração foi produzida a partir apenas do extrato bancário. O revisor deve verificar que todos os créditos de PIS/Cofins estão respaldados por NF-e/NFS-e válida, que os créditos de ICMS conferem com o SPED Fiscal, e que as regras específicas do estado foram corretamente aplicadas."

### Catálogo de recusas específicas do Brasil

- **R-BR-1** — Gatilho: produto sujeito a ICMS Substituição Tributária com necessidade de MVA (Margem de Valor Agregado) ou MVA ajustada. Mensagem: "Os cálculos de margem de ICMS-ST exigem consulta a protocolos CONFAZ específicos do produto e fórmulas de ajuste da MVA. Isto está fora do escopo da classificação automatizada. Escalar para Contador inscrito no CRC com experiência em ICMS-ST para o par produto/estado em questão."
- **R-BR-2** — Gatilho: cliente opera ou despacha para a Zona Franca de Manaus. Mensagem: "Os incentivos da ZFM (isenção de IPI, redução de ICMS, créditos SUFRAMA) requerem verificação de PPB e procedimentos específicos da SUFRAMA. Escalar para especialista."
- **R-BR-3** — Gatilho: cliente se beneficia de incentivo estadual de ICMS que pode não ser reconhecido pelo CONFAZ. Mensagem: "Incentivos estaduais de ICMS não reconhecidos carregam risco de glosa no estado de destino. Escalar para advogado tributarista."
- **R-BR-4** — Gatilho: operações intercompany com partes vinculadas estrangeiras que afetem a base dos tributos indiretos. Mensagem: "Ajustes de preços de transferência que afetam a base de tributo indireto requerem análise especializada. Escalar."
- **R-BR-5** — Gatilho: cliente em fiscalização ou buscando redução de multa. Mensagem: "Defesa em fiscalização e redução de multa estão fora do escopo desta skill. Engajar advogado tributarista."
- **R-BR-6** — Gatilho: usuário pergunta sobre IRPJ/CSLL (pessoa jurídica) ou IRPF (pessoa física). Mensagem: "Esta skill cobre apenas tributos indiretos (PIS, Cofins, ICMS, ISS, IPI, CBS, IBS, IS). Para imposto de renda, utilizar a skill apropriada."
- **R-BR-7** — Gatilho: cadeias de crédito de IPI em industrialização em múltiplas etapas. Mensagem: "Cadeias de crédito de IPI em industrialização em múltiplas etapas exigem análise especializada. Escalar."
- **R-BR-8** — Gatilho: perguntas sobre questões controvertidas da transição CBS/IBS ainda pendentes de regulamento. Mensagem: "A reforma CBS/IBS ainda está sendo regulamentada (LC 214/2025 e LC 227/2026). Regras de transição não estão totalmente publicadas. Escalar todas as perguntas controversas de transição."

## Seção 3 — Biblioteca de padrões de fornecedores (tabela de consulta)

Este é o pré-classificador determinístico. Quando o contraparte de uma transação combinar com um padrão desta tabela, aplicar o tratamento diretamente. Se nenhum padrão combinar, descer para as regras Tier 1 da Seção 5.

**Como ler esta tabela.** Combinar por substring case-insensitive sobre o nome do contraparte como aparece no extrato bancário. Se múltiplos padrões combinarem, usar o mais específico.

### 3.1 Bancos brasileiros (tarifas — serviço financeiro, isentas de PIS/Cofins)

**Padrões de bancos brasileiros**

| Padrão | Tratamento | Notas |
| --- | --- | --- |
| BANCO DO BRASIL, BB | EXCLUIR para tarifas | Serviço financeiro, isento. Sem PIS/Cofins, sem ICMS, sem ISS. |
| ITAU, ITAU UNIBANCO | EXCLUIR para tarifas | Idem |
| BRADESCO | EXCLUIR para tarifas | Idem |
| SANTANDER BRASIL, SANTANDER BR | EXCLUIR para tarifas | Idem |
| CAIXA, CAIXA ECONOMICA FEDERAL, CEF | EXCLUIR para tarifas | Idem |
| NUBANK, NU PAGAMENTOS | EXCLUIR para tarifas | Idem |
| BANCO INTER, INTER | EXCLUIR para tarifas | Idem |
| BTG PACTUAL | EXCLUIR para tarifas | Idem |
| SICOOB, SICREDI, BANCOOB | EXCLUIR para tarifas | Tarifas de banco cooperativo, mesmo tratamento |
| BANCO SAFRA, BANCO VOTORANTIM | EXCLUIR para tarifas | Idem |
| JUROS, RENDIMENTO, IOF | EXCLUIR | Juros, rendimento, IOF — financeiro, fora do escopo de tributo indireto |
| EMPRESTIMO, FINANCIAMENTO | EXCLUIR | Movimento de principal de empréstimo, fora do escopo |
| TARIFA BANCARIA, TAXA DE MANUTENCAO | EXCLUIR | Tarifa de manutenção bancária, serviço financeiro isento |
| TED, DOC (linhas de tarifa) | EXCLUIR | Tarifas de transferência, serviço financeiro isento |

### 3.2 Governo brasileiro, autoridades fiscais e entidades estatutárias (excluir integralmente)

**Padrões governo brasileiro**

| Padrão | Tratamento | Notas |
| --- | --- | --- |
| RECEITA FEDERAL, RFB, DARF | EXCLUIR | Pagamento de tributo federal (IRPJ, CSLL, PIS, Cofins, IPI) |
| SEFAZ, SECRETARIA DA FAZENDA | EXCLUIR | Pagamento de tributo estadual (ICMS) |
| PREFEITURA, SECRETARIA DE FINANCAS | EXCLUIR | Pagamento de tributo municipal / ISS |
| SIMPLES NACIONAL, DAS | EXCLUIR | DAS unificado do Simples Nacional |
| INSS, PREVIDENCIA | EXCLUIR | Contribuição previdenciária |
| FGTS | EXCLUIR | Depósito do Fundo de Garantia |
| CRC, CONSELHO REGIONAL DE CONTABILIDADE | EXCLUIR | Anuidade de órgão de classe, não sujeita a tributo indireto |
| JUNTA COMERCIAL | EXCLUIR | Taxa do registro mercantil, ato soberano |
| DETRAN, IPVA | EXCLUIR | Licenciamento/tributo veicular, não é tributo indireto |
| IPTU | EXCLUIR | Tributo predial municipal, não é tributo indireto |

### 3.3 Serviços públicos brasileiros (concessionárias)

**Padrões serviços públicos**

| Padrão | Tratamento | Tributos | Notas |
| --- | --- | --- | --- |
| CPFL, CPFL ENERGIA | ICMS aplica (alíquota estadual) | ICMS + PIS/Cofins | Energia elétrica — ICMS varia por estado; PIS/Cofins sobre fatura. NF-e emitida. |
| CEMIG | ICMS aplica | ICMS + PIS/Cofins | Energia — Minas Gerais |
| LIGHT, LIGHT SA | ICMS aplica | ICMS + PIS/Cofins | Energia — Rio de Janeiro |
| ENEL, ENEL DISTRIBUICAO | ICMS aplica | ICMS + PIS/Cofins | Energia — SP, RJ, CE, GO |
| ENERGISA | ICMS aplica | ICMS + PIS/Cofins | Energia — múltiplos estados |
| SABESP | ISS ou isento | ISS (depende do município) | Água/esgoto — São Paulo. Tratamento varia; alguns serviços de água são isentos. |
| COPASA | ISS ou isento | ISS | Água — Minas Gerais |
| CLARO, CLARO BRASIL | ICMS aplica | ICMS + PIS/Cofins | Telecom (ICMS, não ISS — transporte/comunicação) |
| VIVO, TELEFONICA BRASIL | ICMS aplica | ICMS + PIS/Cofins | Idem — telecom |
| TIM, TIM BRASIL | ICMS aplica | ICMS + PIS/Cofins | Idem |
| OI, OI SA | ICMS aplica | ICMS + PIS/Cofins | Idem |
| NET, NET SERVICOS | ICMS aplica | ICMS + PIS/Cofins | TV a cabo/internet — telecom sujeito a ICMS |

### 3.4 Seguros (isento — excluir do tributo indireto)

**Padrões seguros**

| Padrão | Tratamento | Notas |
| --- | --- | --- |
| PORTO SEGURO | EXCLUIR | Prêmio de seguro — isento de ICMS/ISS; sujeito a IOF (separado) |
| BRADESCO SEGUROS, BRADESCO AUTO | EXCLUIR | Idem |
| SULAMERICA, SUL AMERICA | EXCLUIR | Idem |
| ITAU SEGUROS | EXCLUIR | Idem |
| ZURICH, ALLIANZ, MAPFRE BRASIL | EXCLUIR | Idem |
| SEGURO, APOLICE, SINISTRO | EXCLUIR | Todas as operações de seguro — isentas de tributo indireto |

### 3.5 Transporte e logística

**Padrões transporte e logística**

| Padrão | Tratamento | Tributos | Notas |
| --- | --- | --- | --- |
| CORREIOS, ECT | ICMS (serviço postal é ICMS, não ISS) | ICMS + PIS/Cofins | Postal/courier — CT-e emitido para transporte |
| JADLOG, TOTAL EXPRESS | ICMS | ICMS + PIS/Cofins | Frete expresso |
| AZUL CARGO, LATAM CARGO | ICMS | ICMS + PIS/Cofins | Frete aéreo |
| 99, 99 TECNOLOGIA, 99POP | ISS | ISS + PIS/Cofins | App de transporte — serviço sujeito a ISS (alíquota municipal) |
| UBER, UBER BRASIL | ISS | ISS + PIS/Cofins | Idem — app de transporte é serviço |
| IFOOD, IFOOD AGENCIA | ISS | ISS + PIS/Cofins | Plataforma de delivery — ISS sobre a comissão. Itens de comida podem ter tratamento próprio. |
| RAPPI | ISS | ISS + PIS/Cofins | Idem iFood |
| GOL, LATAM, AZUL (companhia aérea) | ICMS isento ou zero |  | Voos domésticos — transporte interestadual de passageiros possui tratamento específico de ICMS (geralmente não tributável de ICMS; ISS não se aplica a transporte) |

### 3.6 Grandes varejistas e e-commerce brasileiros

**Padrões varejistas e e-commerce**

| Padrão | Tratamento | Tributos | Notas |
| --- | --- | --- | --- |
| MAGAZINE LUIZA, MAGALU | ICMS + PIS/Cofins | Cadeia completa | Mercadoria geral — NF-e emitida. Verificar NCM para IPI se industrializado. |
| CASAS BAHIA, PONTO (VIA) | ICMS + PIS/Cofins | Cadeia completa | Idem |
| AMERICANAS, B2W | ICMS + PIS/Cofins | Cadeia completa | Idem |
| MERCADO LIVRE, MERCADO PAGO | ICMS + PIS/Cofins (mercadorias); ISS (taxa de marketplace) | Misto | Marketplace: compras de mercadoria têm ICMS; taxas de plataforma têm ISS. Separar as linhas. |
| AMAZON BR, AMAZON BRASIL | ICMS + PIS/Cofins | Cadeia completa | Verificar se o vendedor é a Amazon diretamente ou marketplace de terceiros |
| SHOPEE BRASIL | ICMS + PIS/Cofins | Cadeia completa | Mesmo cuidado com marketplace |
| CARREFOUR, ATACADAO | ICMS + PIS/Cofins | Cadeia completa | Supermercado/atacado — alimentos podem ter PIS/Cofins reduzido/zero (cesta básica) |
| PAO DE ACUCAR, EXTRA, GPA | ICMS + PIS/Cofins | Cadeia completa | Idem |
| KALUNGA | ICMS + PIS/Cofins | Cadeia completa | Material de escritório |

### 3.7 SaaS e serviços digitais — fornecedores estrangeiros

**Padrões SaaS estrangeiros**

| Padrão | Tratamento | Notas |
| --- | --- | --- |
| GOOGLE (Ads, Workspace, Cloud) | ISS-Importação + PIS/Cofins-Importação + IRRF + IOF | Serviço digital estrangeiro. Adquirente brasileiro deve reter/auto-apurar. ISS por município (2-5%). PIS-Importação 1,65%, Cofins-Importação 7,60%, IRRF 15% (ou 25% se paraíso fiscal), IOF 0,38%. |
| MICROSOFT (365, Azure) | Igual ao Google | Verificar se faturado pela Microsoft Brasil (doméstico) ou Microsoft Corp (importação) |
| ADOBE | Idem | Verificar entidade emissora |
| META, FACEBOOK ADS | Idem |  |
| AWS, AMAZON WEB SERVICES | Idem | Verificar se AWS Brasil ou AWS Inc |
| SLACK, NOTION, FIGMA, CANVA | ISS-Importação + PIS/Cofins-Importação + IRRF + IOF | Entidades dos EUA — tributação plena de importação de serviço |
| ANTHROPIC, OPENAI, CHATGPT | Idem | Entidades dos EUA |
| SPOTIFY, NETFLIX, APPLE (B2C) | Estas plataformas podem recolher tributos diretamente para B2C | Para B2B: verificar nota e obrigações de retenção |

### 3.8 Processadores de pagamento

**Padrões processadores de pagamento**

| Padrão | Tratamento | Notas |
| --- | --- | --- |
| PAGSEGURO, PAGBANK | EXCLUIR (serviço financeiro) ou ISS | Comissão de processamento — pode ser serviço financeiro isento ou sujeita a ISS dependendo da caracterização |
| STONE, STONE PAGAMENTOS | Idem |  |
| CIELO | Idem |  |
| REDE, GETNET | Idem |  |
| MERCADO PAGO (taxas de transação) | EXCLUIR (financeiro) | Comissão de processamento de transação |
| PAYPAL BRASIL | EXCLUIR (financeiro) | Processamento de pagamento |
| STRIPE (se entidade brasileira) | ISS | Se Stripe Brasil: ISS sobre a comissão. Se estrangeiro: tratamento de importação de serviço. |

### 3.9 Serviços profissionais

**Padrões serviços profissionais**

| Padrão | Tratamento | Tributos | Notas |
| --- | --- | --- | --- |
| CONTADOR, CONTABILIDADE, ESCRITORIO CONTABIL | ISS | ISS + PIS/Cofins | Serviços contábeis — ISS à alíquota municipal. NFS-e emitida. |
| ADVOGADO, ADVOCACIA, ESCRITORIO DE ADVOCACIA | ISS | ISS + PIS/Cofins | Serviços jurídicos |
| CONSULTORIA | ISS | ISS + PIS/Cofins | Serviços de consultoria |
| CARTORIO, TABELIONATO | ISS | ISS | Serviços notariais |

### 3.10 Folha de pagamento e relações de trabalho (excluir integralmente)

**Padrões folha de pagamento**

| Padrão | Tratamento | Notas |
| --- | --- | --- |
| FOLHA, SALARIO, HOLERITE | EXCLUIR | Salários — fora do escopo de tributo indireto |
| INSS, PREVIDENCIA | EXCLUIR | Contribuição previdenciária |
| FGTS, FUNDO DE GARANTIA | EXCLUIR | Fundo de garantia |
| VALE TRANSPORTE, VT | EXCLUIR | Vale-transporte |
| VALE REFEICAO, VR, VALE ALIMENTACAO, VA | EXCLUIR | Vale-refeição/alimentação |
| FERIAS, 13o SALARIO, RESCISAO | EXCLUIR | Férias, 13º, rescisão — trabalhistas, não tributo indireto |

### 3.11 Transferências internas e exclusões

**Padrões transferências internas**

| Padrão | Tratamento | Notas |
| --- | --- | --- |
| TRANSFERENCIA PROPRIA, MESMA TITULARIDADE | EXCLUIR | Movimento interno entre contas |
| TED PROPRIA, PIX PROPRIO | EXCLUIR | Transferência de mesma titularidade via PIX ou TED |
| APLICACAO, RESGATE, CDB, LCI, LCA | EXCLUIR | Aplicação/resgate de investimento — financeiro, fora do escopo |
| DIVIDENDO, LUCRO DISTRIBUIDO | EXCLUIR | Distribuição de lucros, fora do escopo |
| EMPRESTIMO, MUTUO | EXCLUIR | Empréstimo, fora do escopo |
| SAQUE, SAQUE ATM | Perguntar | Saque em espécie — perguntar finalidade |

### 3.12 Padrões de receita (vendas e prestação)

**Padrões de receita**

| Padrão | Tratamento | Notas |
| --- | --- | --- |
| VENDA MERCADORIA, NF-E | ICMS sobre venda de mercadoria | Aplica alíquota interna |
| PRESTACAO SERVICO, NFS-E | ISS sobre o serviço | Aplica alíquota municipal |
| VENDA INTERESTADUAL | ICMS à alíquota interestadual | 7% ou 12% conforme rota |
| EXPORTACAO | Imune/zero ICMS e ISS | Imunidade constitucional (CF/88 Art. 155 §2º, X, "a") |
| VENDA CONSUMIDOR FINAL (interestadual) | DIFAL aplica | Vendedor recolhe o diferencial de alíquota |
| PLATAFORMA DIGITAL, MARKETPLACE | ISS ou ICMS | Depende de mercadoria vs serviço |

### 3.13 Padrões de entradas/insumos

**Padrões de entradas/insumos**

| Padrão | Tratamento | Notas |
| --- | --- | --- |
| COMPRA MERCADORIA, NF-E ENTRADA | Crédito de ICMS (se fora do Simples) | Crédito não cumulativo |
| MATERIA PRIMA, INSUMO | Crédito de ICMS + IPI | Insumos para industrialização |
| SERVICO TOMADO, NFS-E | ISS pode ser retido na fonte | Verificar regras de retenção |
| ENERGIA ELETRICA | Crédito de ICMS (parcial) | Apenas uso industrial em alguns estados |
| TELECOMUNICACOES | Crédito de ICMS (parcial) | Varia por estado |
| ALUGUEL COMERCIAL | Sem crédito de ICMS/ISS | Aluguel não é sujeito a tributo indireto |

### 3.14 Padrões do Simples Nacional

**Padrões Simples Nacional**

| Padrão | Tratamento | Notas |
| --- | --- | --- |
| DAS SIMPLES NACIONAL | Pagamento unificado, inclui ICMS/ISS | A menos que acima do sublimite (BRL 3.600.000) |
| ICMS-ST SEPARADO | Pago fora do Simples mesmo dentro do Simples | Produtos com substituição tributária |
| ICMS IMPORTACAO | Pago separadamente no desembaraço | Mesmo no Simples |

## Seção 4 — Exemplos resolvidos

Estes são exemplos integralmente resolvidos baseados em um extrato bancário hipotético de um consultor de software pessoa jurídica, sediado em São Paulo, Lucro Presumido, com CNPJ ativo, e em exemplos adicionais para cobrir cenários estaduais e municipais distintos.

### Exemplo 1 — Venda de serviço doméstico padrão com NFS-e

**Linha de entrada:**
`05.04.2026 ; EMPRESA ALFA LTDA ; CRÉDITO ; NFS-e 2026/041 Consultoria TI abril ; BRL 10.000,00`

**Raciocínio:**
Serviço de consultoria em software. Sujeito a ISS (não a ICMS, pois consta da lista da LC 116/2003). Alíquota de ISS em São Paulo para consultoria em TI: 2-5% (varia conforme código municipal). Também sujeito a PIS/Cofins: regime cumulativo (Lucro Presumido) = 0,65% PIS + 3% Cofins = 3,65% sobre a receita. NFS-e emitida pelo prestador.

**Saída Exemplo 1**

| Data | Contraparte | Bruto | Base ISS | Alíquota ISS | PIS | Cofins | Notas |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 05.04.2026 | EMPRESA ALFA LTDA | +10.000 | 10.000 | 5% (padrão SP) | 65,00 | 300,00 | Confirmar alíquota de ISS para o município de SP |

### Exemplo 2 — Venda interestadual de mercadoria

**Linha de entrada:**
`10.04.2026 ; DISTRIBUIDORA BETA SA (RJ) ; CRÉDITO ; NF-e 001-12345 venda mercadorias ; BRL 50.000,00`

**Raciocínio:**
Venda de mercadoria de SP para RJ. Alíquota interestadual de ICMS: SP (Sul/Sudeste) para RJ (Sul/Sudeste) = 12%. PIS/Cofins cumulativo = 3,65% sobre o bruto. IPI: depende do NCM; presumir 0% para revenda (IPI incide apenas em mercadorias industrializadas/importadas). DIFAL pode aplicar se comprador for consumidor final (não é o caso — comprador é distribuidor com IE).

**Saída Exemplo 2**

| Data | Contraparte | Bruto | Alíquota ICMS | ICMS | PIS/Cofins | IPI | Notas |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 10.04.2026 | DISTRIBUIDORA BETA SA (RJ) | +50.000 | 12% (interestadual SP>RJ) | Incluso no preço (por dentro) | 3,65% | 0% (revenda) | Verificar NF-e e NCM |

### Exemplo 3 — Importação de serviço digital (SaaS dos EUA)

**Linha de entrada:**
`15.04.2026 ; NOTION LABS INC ; DÉBITO ; Monthly subscription ; USD 15,00 ; BRL 85,00`

**Raciocínio:**
Notion é entidade dos EUA. Importação de serviço. Adquirente brasileiro deve auto-apurar: ISS-Importação (alíquota SP, ex. 2,9% para serviços de TI), PIS-Importação (1,65%), Cofins-Importação (7,60%), IRRF (15% de retenção sobre a remessa), IOF (0,38% sobre o câmbio). Tributação efetiva total na remessa pode ultrapassar 25%. Sem NFS-e do fornecedor; obrigação do adquirente recolher e remeter.

**Saída Exemplo 3**

| Data | Contraparte | Bruto BRL | ISS-Imp | PIS-Imp | Cofins-Imp | IRRF | IOF | Notas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 15.04.2026 | NOTION LABS INC | -85,00 | ~2,47 | ~1,40 | ~6,46 | ~12,75 | ~0,32 | Serviço importado — auto-apurar todos os tributos. Confirmar alíquota ISS. |

### Exemplo 4 — Venda a cliente do Simples Nacional

**Linha de entrada:**
`18.04.2026 ; CLIENTE VAREJO ; CRÉDITO ; NFC-e venda balcão ; BRL 5.000,00`

**Raciocínio:**
Se o cliente é Simples Nacional (pagador de DAS), todos os tributos (ICMS, ISS, PIS, Cofins, IRPJ, CSLL, CPP) são pagos pelo DAS unificado, conforme a faixa de receita. Anexo I (comércio) ou Anexo III/V (serviços). Não há cálculo separado de PIS/Cofins/ICMS/ISS — o DAS cobre tudo. A alíquota efetiva depende da receita dos últimos 12 meses (RBT12).

**Saída Exemplo 4**

| Data | Contraparte | Bruto | Tratamento | Notas |
| --- | --- | --- | --- | --- |
| 18.04.2026 | CLIENTE VAREJO | +5.000 | Simples Nacional — incluído no DAS | Calcular DAS com base no Anexo e na faixa de RBT12. Sem linhas separadas de ICMS/PIS/Cofins. |

### Exemplo 5 — Despesa com entretenimento / pessoal

**Linha de entrada:**
`22.04.2026 ; RESTAURANTE FOGO DE CHAO ; DÉBITO ; Jantar ; BRL 800,00`

**Raciocínio:**
Refeição em restaurante. Para PIS/Cofins não cumulativo, créditos de entrada estão disponíveis apenas em insumos de produção, mercadorias para revenda, energia, aluguel, depreciação e outras categorias específicas. Refeições em restaurante não geram crédito. Para ICMS: não se aplica (restaurante é serviço). Para Lucro Presumido (PIS/Cofins cumulativos): sem créditos em nenhum caso. Default: sem recuperação de crédito.

**Saída Exemplo 5**

| Data | Contraparte | Bruto | Recuperação de crédito | Notas |
| --- | --- | --- | --- | --- |
| 22.04.2026 | RESTAURANTE FOGO DE CHAO | -800,00 | Nenhuma | Entretenimento — sem crédito de PIS/Cofins. Não é compra creditável de ICMS. |

### Exemplo 6 — Fatura de energia elétrica com ICMS

**Linha de entrada:**
`28.04.2026 ; ENEL DISTRIBUICAO SP ; DÉBITO ; Fatura energia elétrica ; BRL 1.500,00`

**Raciocínio:**
Fatura de energia. Sujeita a ICMS na alíquota interna de SP (18% geral, mas a energia pode ter alíquota específica de ICMS — frequentemente 25% para consumidor comercial em SP). PIS/Cofins também incidem na fatura. No regime não cumulativo, PIS/Cofins sobre energia gera crédito (Lei 10.637/2002, Art. 3º, III). No regime cumulativo: sem crédito. ICMS sobre energia gera crédito pelo regime normal de débito/crédito se o adquirente for contribuinte do ICMS.

**Saída Exemplo 6**

| Data | Contraparte | Bruto | Crédito de ICMS | Crédito PIS/Cofins | Notas |
| --- | --- | --- | --- | --- | --- |
| 28.04.2026 | ENEL DISTRIBUICAO SP | -1.500,00 | Sim (se contribuinte ICMS) | Sim (Lucro Real) / Não (Lucro Presumido) | Conferir NF-e quanto a valores exatos de ICMS e PIS/Cofins |

### Exemplo 7 — Apuração de ICMS intra-SP (Lucro Real, comércio)

**Entrada:** Varejista em SP, vendas de mercadoria R$ 100.000. Alíquota interna 18%. Compras R$ 60.000 com 18% de ICMS.

**Cômputo:**
- ICMS sobre vendas: R$ 100.000 × 18% = R$ 18.000
- Créditos de ICMS sobre compras: R$ 60.000 × 18% = R$ 10.800
- ICMS a recolher: R$ 18.000 − R$ 10.800 = R$ 7.200

### Exemplo 8 — Venda interestadual SP → BA com DIFAL

**Entrada:** Empresa de SP vende R$ 10.000 em mercadorias para empresa BA. Alíquota interestadual 7%. Alíquota interna BA 19%.

**Cômputo:**
- ICMS destacado na NF-e: R$ 10.000 × 7% = R$ 700 (vendedor recolhe à SEFAZ-SP)
- Se B2B (comprador é contribuinte): comprador recolhe DIFAL de 12% (19% − 7%) à BA
- Se B2C (consumidor final não contribuinte): vendedor coleta o DIFAL de 12% e remete à BA (partilha estadual conforme EC 87/2015, atualmente integralmente devida ao estado de destino)

### Exemplo 9 — Retenção de ISS na fonte

**Entrada:** Fatura de consultoria de R$ 20.000 emitida a grande cliente corporativo. Alíquota ISS 5%. Sujeita a retenção.

**Cômputo:**
- ISS: R$ 20.000 × 5% = R$ 1.000
- O cliente retém R$ 1.000 e remete diretamente ao município
- O prestador recebe R$ 19.000 líquidos
- O prestador NÃO recolhe o ISS separadamente sobre essa fatura
- O prestador escritura a fatura com indicação de "ISS retido na fonte"

## Seção 5 — Regras Tier 1 (comprimidas)

### 5.1 Árvore de decisão de classificação

- **Árvore de decisão** — Mercadoria = ICMS + IPI (se manufaturada/importada) + PIS/Cofins. Serviço = ISS + PIS/Cofins. Transporte/comunicação = ICMS (não ISS) + PIS/Cofins. ICMS e ISS são mutuamente excludentes (exceto em fornecimento misto, hipótese específica de aplicação).

### 5.2 Determinação do regime de PIS/Cofins

- **Determinação do regime** — Lucro Real = não cumulativo (1,65% + 7,60% = 9,25%, com créditos de entrada). Lucro Presumido = cumulativo (0,65% + 3,00% = 3,65%, sem créditos de entrada). Simples Nacional = incluído no DAS (sem apuração separada de PIS/Cofins). Determinar o regime PRIMEIRO — ele muda toda a apuração.

### 5.3 Alíquotas internas de ICMS

- **Alíquotas internas de ICMS** — Variam por estado, de 17% a 23%. Aplicar a alíquota interna do estado em que ocorre a operação. Para operações interestaduais, usar 7% (S/SE → N/NE/CO) ou 12% (demais combinações). Mercadorias importadas com >40% de conteúdo de importação: 4% interestadual (Resolução SF 13/2012). Atenção a adicionais FECP/FECOEP em estados específicos.  _(Resolução SF 13/2012)_

### 5.4 Cálculo "por dentro" do ICMS

- **Cálculo por dentro do ICMS** — O ICMS é calculado por dentro do preço. Uma alíquota nominal de 18% sobre um preço bruto de R$ 100 significa que R$ 18 de ICMS já está incluído (R$ 100 × 18% = R$ 18). A base tributo-excluída é R$ 82; a alíquota efetiva sobre a base tributo-excluída é ~21,95%.

### 5.5 Classificação do ISS

- **Classificação do ISS** — Serviços previstos na lista da LC 116/2003 (cerca de 200 itens em ~40 subitens). Alíquota definida pelo município (2% a 5%, com piso de 2% por força da LC 157/2016). ISS devido no local do estabelecimento do prestador, exceto em ~20 categorias específicas (construção civil, segurança, limpeza, etc.) em que o ISS é devido no local da prestação (LC 116/2003, Art. 3º, incisos).  _(LC 116/2003; LC 157/2016)_

### 5.6 Classificação do IPI

- **Classificação do IPI** — Aplica-se apenas a produtos industrializados e importados. Alíquota por NCM, conforme tabela TIPI. Cobrado por fora (acrescido ao preço). Gera créditos sobre insumos da industrialização. Não incide sobre revenda por estabelecimento meramente comercial.

### 5.7 Tratamento de exportações

- **Tratamento de exportações** — Exportações são isentas/imunes em todos os tributos indiretos: ICMS imune (Lei Kandir, LC 87/1996, Art. 3º; imunidade constitucional CF/88 Art. 155 §2º, X, "a"), IPI imune, PIS/Cofins alíquota zero com manutenção dos créditos, ISS isento (se o resultado ocorrer no exterior — LC 116/2003, Art. 2º, I). Preservação integral dos créditos de entrada.  _(LC 87/1996 Art. 3º; CF/88 Art. 155 §2º, X, "a"; LC 116/2003 Art. 2º, I)_

### 5.8 Tratamento de importações

- **Tratamento de importações** — Importação de mercadorias: II (imposto de importação) + IPI + ICMS + PIS-Importação (2,1%) + Cofins-Importação (9,65% ou 10,65%). Importação de serviços: ISS-Importação + PIS-Importação (1,65%) + Cofins-Importação (7,60%) + IRRF (15%/25%) + IOF (0,38%) + eventualmente CIDE (10% para transferência de tecnologia). A tributação efetiva sobre serviços importados pode ultrapassar 40%.

### 5.9 Requisitos de NF-e para créditos de ICMS / PIS / Cofins

- **Requisitos de NF-e para créditos** — Créditos exigem NF-e válida (Modelo 55 para mercadorias) ou NFS-e (para ISS em serviços, onde relevante). Crédito de ICMS = ICMS destacado na NF-e. Crédito de PIS/Cofins (apenas não cumulativo) = valores na NF-e ou calculados a partir dos itens creditáveis previstos na Lei 10.637/2002 Art. 3º e Lei 10.833/2003 Art. 3º.  _(Lei 10.637/2002 Art. 3º; Lei 10.833/2003 Art. 3º)_

### 5.10 Créditos de entrada de PIS/Cofins (apenas não cumulativo)

- **Créditos de entrada PIS/Cofins** — Itens creditáveis: mercadorias para revenda, insumos para industrialização/produção, energia consumida na produção, aluguel de imóveis/máquinas usados no negócio, depreciação de bens do ativo, frete sobre compras. NÃO creditáveis: entretenimento, despesas pessoais, itens não diretamente vinculados à atividade geradora de receita.

### 5.11 Tratamento no Simples Nacional

- **Tratamento no Simples Nacional** — Todos os tributos (ICMS, ISS, PIS, Cofins, IRPJ, CSLL, CPP) recolhidos pela guia DAS. Alíquota efetiva determinada pelo Anexo (I-V) e pela faixa de receita dos últimos 12 meses (RBT12). Sem apuração separada de ICMS/ISS/PIS/Cofins, exceto: - **Sublimite estadual/municipal de BRL 3.600.000** (LC 123/2006, Art. 13, §1º, e Art. 18): acima desse sublimite, ICMS e ISS são recolhidos fora do DAS, pelas regras normais do estado/município. - **ICMS-ST**, **ICMS na importação** e **DIFAL** são pagos separadamente, mesmo no Simples. Comprador que recebe nota de fornecedor do Simples: crédito de ICMS limitado (percentual destacado na NF-e) e crédito de PIS/Cofins limitado.  _(LC 123/2006, Art. 13, §1º, e Art. 18)_

### 5.12 Regras de transição (CBS/IBS, 2026+)

- **Regras de transição** — **2026**: CBS 0,9% + IBS 0,1% aplicam-se como alíquotas-teste, em paralelo aos tributos existentes. São creditáveis contra PIS/Cofins e ICMS/ISS, respectivamente. Pagamento suspenso por 3 meses, sem multa, após a publicação dos regulamentos. **2027**: CBS substitui PIS/Cofins integralmente (tributos antigos extintos); IPI extinto, com exceções para a Zona Franca de Manaus. **2029-2032**: IBS substitui gradualmente ICMS/ISS. **2033**: restam apenas CBS + IBS + IS. Todas as regras de transição são marcadas como julgamento exigido do revisor.

### 5.13 DIFAL (Diferencial de Alíquota)

- **DIFAL** — DIFAL aplica-se quando há venda interestadual a não contribuinte (consumidor final). DIFAL = alíquota interna do estado de destino menos a alíquota interestadual. Recolhido ao estado de destino por força da EC 87/2015 (atualmente partilha de 100% para destino, conforme LC 190/2022). Sinalizar para revisor todos os cálculos de DIFAL.  _(EC 87/2015; LC 190/2022)_

### 5.14 Classificação de software

- **Classificação de software** — SaaS / serviços em nuvem são, em geral, ISS (STF ADIs 1.945 e 5.659). Software empacotado era historicamente ICMS, mas modernamente é predominantemente ISS por força das mesmas ADIs. Sinalizar para revisor — exigir verificação da legislação estadual e municipal aplicável.  _(STF ADIs 1.945 e 5.659)_

### 5.15 Tipos de nota fiscal eletrônica

- **Tipos de nota fiscal eletrônica** — NF-e (mercadorias / ICMS), NFS-e (serviços / ISS), NFC-e (venda ao consumidor no varejo), CT-e (transporte). NFS-e é emitida pelo portal municipal, contendo CNPJ do prestador, CNPJ/CPF do tomador, código de serviço, valor, alíquota de ISS e valor do ISS.

## Seção 6 — Catálogo Tier 2 (comprimido)

### 6.1 Determinação de regime tributário

- **Determinação de regime tributário** — *Padrão:* cliente não sabe se está em Lucro Real, Lucro Presumido ou Simples Nacional. *Default:* Lucro Presumido (cumulativo, sem créditos). *Pergunta:* "Qual seu regime tributário? Verifique o cartão CNPJ ou consulte seu Contador."

### 6.2 Aplicabilidade de ICMS-ST

- **Aplicabilidade de ICMS-ST** — *Padrão:* o produto pode estar sujeito a ICMS Substituição Tributária. *Default:* presumir que não está sujeito a ST (sinalizar para revisor). *Pergunta:* "Este produto está sujeito a ICMS-ST no seu estado? Qual é a MVA aplicável segundo o protocolo CONFAZ?"

### 6.3 Operação interestadual ou interna

- **Operação interestadual ou interna** — *Padrão:* venda ou compra em que origem/destino não é claro. *Default:* interna (aplicar alíquota interna). *Pergunta:* "Em qual estado está o comprador/vendedor?"

### 6.4 Alíquota de ISS por município

- **Alíquota de ISS por município** — *Padrão:* serviço em que a alíquota municipal exata não é conhecida. *Default:* 5% (máximo, com piso de 2% por LC 157/2016). *Pergunta:* "Qual município é competente para o ISS dessa prestação? Qual é a alíquota aplicável?"  _(LC 157/2016)_

### 6.5 Tratamento de transição CBS/IBS

- **Tratamento de transição CBS/IBS** — *Padrão:* transação em 2026 em que as alíquotas-teste CBS/IBS possam aplicar. *Default:* aplicar apenas o sistema atual (não adicionar CBS/IBS sem confirmação). *Pergunta:* "Seu sistema de NF-e/NFS-e está atualizado para incluir os campos de CBS/IBS? Seu Contador confirmou o tratamento de transição?"

### 6.6 Retenção sobre serviço importado

- **Retenção sobre serviço importado** — *Padrão:* pagamento a prestador estrangeiro. *Default:* aplicar tributação plena de importação (ISS, PIS/Cofins-Importação, IRRF 15%, IOF). *Pergunta:* "O prestador é de país com tratado tributário? É jurisdição de paraíso fiscal (IRRF 25%)?"

### 6.7 Fornecimento misto (mercadoria + serviço)

- **Fornecimento misto** — *Padrão:* transação que inclui mercadoria e serviço. *Default:* tratar como mercadoria (ICMS, alíquota maior). *Pergunta:* "Pode separar os componentes de mercadoria e serviço? A parte de mercadoria sujeita-se a ICMS e a de serviço a ISS."

### 6.8 Veículos e combustível

- **Veículos e combustível** — *Padrão:* compra de combustível, manutenção de veículo. *Default:* sem crédito (sinalizar para revisor). *Pergunta:* "Esse veículo é de uso exclusivo do negócio? O combustível é para veículo da empresa?"

### 6.9 Transferências de entrada com valores redondos

- **Transferências com valores redondos** — *Padrão:* grande crédito de valor redondo proveniente de contraparte com nome do sócio. *Default:* excluir como aporte de sócio. *Pergunta:* "Esse valor é pagamento de cliente, aporte de capital ou empréstimo?"

### 6.10 Saques em espécie

- **Saques em espécie** — *Padrão:* "saque", "saque ATM", "saque caixa". *Default:* excluir. *Pergunta:* "Para que foi usado o caixa?"

### 6.11 Local de tributação do ISS

- **Local de tributação do ISS** — *Padrão:* o serviço é prestado em município diferente do município de registro do prestador. *Default:* tributar no município do prestador. *Pergunta:* "O serviço se enquadra em alguma das hipóteses do Art. 3º da LC 116/2003 (construção, segurança, limpeza etc.), em que o ISS é devido no local da prestação?"  _(LC 116/2003 Art. 3º)_

### 6.12 Computação do DIFAL

- **Computação do DIFAL** — *Padrão:* venda interestadual a consumidor final. *Default:* aplicar DIFAL (alíquota interna do estado de destino menos alíquota interestadual). *Pergunta:* "O comprador é contribuinte (com IE) ou consumidor final? Em qual estado?"

### 6.13 Classificação de software (SaaS vs licenciado)

- **Classificação de software (SaaS vs licenciado)** — *Padrão:* fornecimento de software. *Default:* ISS (conforme STF ADIs 1.945 e 5.659). *Pergunta:* "É SaaS, software de prateleira (entrega física), ou licença por download? Sinalizar para revisor."  _(STF ADIs 1.945 e 5.659)_

## Seção 7 — Modelo de papel de trabalho em Excel (específico para Brasil)

### Aba "Transactions"

Colunas: A (Data), B (Contraparte/CNPJ), C (nº NF-e/NFS-e), D (Bruto BRL), E (Valor ICMS), F (Valor PIS), G (Valor Cofins), H (Valor ISS), I (Valor IPI), J (Tipo: ICMS/ISS/Misto), K (Direção: Interna/Interestadual/Importação/Exportação), L (Default S/N), M (Pergunta), N (Notas).

### Aba "Tax Summary"

Seções separadas para cada tributo:

```
PIS/COFINS:
| Receita (PIS/Cofins output) | =SUMIFS sobre entradas de crédito |
| PIS devido | =Receita * alíquota PIS |
| Cofins devida | =Receita * alíquota Cofins |
| Créditos PIS (se não cumulativo) | =SUMIFS sobre entradas de débito com crédito PIS |
| Créditos Cofins (se não cumulativo) | =SUMIFS sobre entradas de débito com crédito Cofins |
| PIS líquido | =PIS devido - créditos PIS |
| Cofins líquida | =Cofins devida - créditos Cofins |

ICMS (se aplicável):
| ICMS output | =SUMIFS sobre vendas ICMS |
| Créditos ICMS (entrada) | =SUMIFS sobre créditos ICMS de compras |
| ICMS líquido | =Output - Input |

ISS (se aplicável):
| ISS sobre serviços prestados | =SUMIFS sobre receita de serviço * alíquota ISS |
```

### Modelo simplificado (uma página)

```
BRASIL — TRIBUTOS INDIRETOS — Papel de trabalho
Período: [Mês / Trimestre]

A. ISS
  A1. Receita total de serviço                     ___________
  A2. Alíquota ISS                                 ___________
  A3. ISS devido                                   ___________
  A4. ISS retido na fonte                          ___________
  A5. ISS a recolher (A3 - A4)                     ___________

B. ICMS
  B1. Receita total de mercadoria (interna)        ___________
  B2. Alíquota ICMS (interna)                      ___________
  B3. ICMS output                                  ___________
  B4. Créditos de ICMS                             ___________
  B5. ICMS a recolher (B3 - B4)                    ___________
  B6. Vendas interestaduais                        ___________
  B7. DIFAL (se B2C interestadual)                 ___________

C. SIMPLES NACIONAL — VERIFICAÇÃO
  C1. Receita últimos 12 meses (RBT12)             ___________
  C2. Acima do sublimite BRL 3.600.000? (S/N)      ___________
  C3. Se sim: ICMS/ISS recolhidos fora do Simples  ___________

FLAGS DE REVISOR:
  [ ] Regime tributário confirmado?
  [ ] Códigos CNAE verificados?
  [ ] Operações interestaduais sinalizadas?
  [ ] Produtos ICMS-ST identificados?
  [ ] Verificação do sublimite efetuada?
```

### Convenções de cor e formatação

Azul para valores travados do extrato/NF-e. Preto para fórmulas. Verde para referências entre abas. Fundo amarelo em qualquer linha em que Default = "S". Fundo vermelho em linhas que exigem verificação de alíquota específica do estado.

## Seção 8 — Guia de leitura de extrato bancário brasileiro

**Convenções de formato.** Bancos brasileiros exportam extratos em PDF (mais comum), OFX, CSV ou via internet banking. Formato de data: DD/MM/AAAA. Colunas comuns: Data, Histórico ou Descrição, Valor (negativo para débitos), Saldo. Alguns bancos exibem Documento (número de documento) e Agência/Conta.

**Formatos de extrato por banco**

| Banco | Formatos | Campos-chave |
| --- | --- | --- |
| Banco do Brasil, Caixa, Itaú | CSV, PDF, OFX | Data, Histórico, Valor, Saldo |
| Bradesco, Santander | CSV, PDF | Data, Descrição, Débito, Crédito |
| Nubank, Inter, C6 | CSV | Data, Descrição, Valor |

**Termos bancários-chave (pistas de classificação)**

| Termo | Pista de classificação |
| --- | --- |
| TED, DOC, PIX | Transferência — checar direção |
| BOLETO | Pagamento de boleto — provável despesa |
| DAS, SIMPLES | Pagamento de Simples Nacional |
| SEFAZ, ICMS | Pagamento de tributo estadual |
| PREFEITURA, ISS | Pagamento de tributo municipal |
| NF-E, NOTA FISCAL | Vinculado a nota fiscal |

**Transferências via PIX.** PIX é o meio dominante (24/7 instantâneo). Lançamentos como "PIX RECEBIDO" ou "PIX ENVIADO" com nome do contraparte ou CNPJ/CPF. Conferir contraparte contra Seção 3.

**TED e DOC.** Métodos mais antigos. TED com nome do contraparte e banco. DOC está em descontinuação. Ambos com referência de transferência.

**Boletos.** Lançamentos como "PAGAMENTO BOLETO" ou "LIQUIDACAO BOLETO" com referência de código de barras. O nome do beneficiário pode não aparecer na descrição — cruzar com as faturas.

**Débito automático.** Débitos automáticos para concessionárias e pagamentos recorrentes. Exibem o nome do prestador: CPFL, VIVO, CLARO etc.

**Transferências internas e exclusões.** Entre contas do próprio cliente. Rotuladas "TRANSFERENCIA MESMA TITULARIDADE", "TED PROPRIA", "PIX PROPRIO". Sempre excluir.

**Retiradas do sócio (pró-labore).** Sócio ou autônomo retirando pró-labore ou dividendos. Rotuladas "PRO-LABORE", "DISTRIBUICAO LUCROS", "RETIRADA SOCIO". Excluir — trabalhista/distribuição, não tributo indireto.

**Estornos e devoluções.** Identificados por "ESTORNO", "DEVOLUCAO", "CREDITO ESTORNO". Lançar como valor negativo no mesmo tratamento da transação original.

**Operações em moeda estrangeira.** Converter para BRL pela taxa PTAX (Banco Central) na data. IOF (0,38% no câmbio) sobre a conversão.

**Lançamentos de investimento.** "APLICACAO CDB", "RESGATE LCI", "RENDIMENTO POUPANCA". Tudo financeiro — excluir do tributo indireto.

**Pagamentos de DAS / DARF.** "PAGAMENTO DAS" (Simples Nacional), "PAGAMENTO DARF" (federal). Excluir — pagamento de tributo, não fornecimento.

## Seção 9 — Fallback de onboarding (apenas quando a inferência falhar)

### 9.1 CNPJ e tipo de entidade jurídica

- **9.1 CNPJ e tipo de entidade jurídica** — Regra de inferência: o formato CNPJ (XX.XXX.XXX/YYYY-ZZ) pode aparecer em descrições de transferência. Filial 0001 = matriz. Pergunta fallback: "Qual seu CNPJ?"

### 9.2 Regime tributário

- **9.2 Regime tributário** — Regra de inferência: pagamentos de DAS sugerem Simples Nacional. DARF código 5952 sugere PIS não cumulativo (Lucro Real). DARF código 8109 sugere PIS cumulativo (Lucro Presumido). Pergunta fallback: "Você é Lucro Real, Lucro Presumido ou Simples Nacional?"

### 9.3 Estado(s) de atuação

- **9.3 Estado(s) de atuação** — Regra de inferência: localização da agência bancária, concessionárias de utilities (CPFL = SP, CEMIG = MG, LIGHT = RJ). Pergunta fallback: "Em quais estados você possui inscrição estadual?"

### 9.4 Período de apuração

- **9.4 Período de apuração** — Regra de inferência: primeira e última data de transação. Apuração mensal é padrão. Pergunta fallback: "A qual mês refere-se este extrato?"

### 9.5 Setor e atividade principal

- **9.5 Setor e atividade principal** — Regra de inferência: mix de contrapartes, descrições de NF-e, código CNAE no cartão CNPJ. Pergunta fallback: "Qual sua atividade principal — mercadoria, serviço, indústria ou misto?"

### 9.6 Status de Simples Nacional

- **9.6 Status de Simples Nacional** — Regra de inferência: pagamentos de DAS no extrato. Pergunta fallback: "Você é optante do Simples Nacional? Em caso afirmativo, qual Anexo se aplica?"

### 9.7 Operações interestaduais

- **9.7 Operações interestaduais** — Regra de inferência: contrapartes com agências bancárias ou endereços fora do estado. Pergunta fallback: "Você vende para ou compra de outros estados? Quais?"

### 9.8 Atividades de exportação

- **9.8 Atividades de exportação** — Regra de inferência: créditos em moeda estrangeira, contrapartes com nomes estrangeiros. Pergunta fallback: "Você exporta mercadorias ou serviços?"

### 9.9 Créditos de períodos anteriores

- **9.9 Créditos de períodos anteriores** — Regra de inferência: não inferível de um único período. Sempre perguntar. Pergunta: "Você possui créditos de PIS/Cofins ou ICMS transportados de meses anteriores?"

### 9.10 Disponibilidade de NF-e

- **9.10 Disponibilidade de NF-e** — Regra de inferência: se o cliente fornecer XMLs de NF-e ou arquivo SPED, está respondido. Pergunta fallback: "Pode fornecer os XMLs de NF-e ou o arquivo SPED Fiscal deste período?"

### 9.11 Códigos CNAE

- **9.11 Códigos CNAE** — Regra de inferência: não inferível do extrato isolado; confirmar no cartão CNPJ. Pergunta fallback: "Quais são seus códigos CNAE? Algum deles altera o tratamento de ISS ou anexo do Simples?"

### 9.12 Retenção de ISS na fonte

- **9.12 Retenção de ISS na fonte** — Regra de inferência: faturas a entes públicos ou grandes corporativos podem implicar retenção. Pergunta fallback: "Você teve faturas com ISS retido na fonte no período?"

### 9.13 RBT12 (se Simples)

- **9.13 RBT12 (se Simples)** — Regra de inferência: não inferível de um único mês. Pergunta fallback: "Qual é seu RBT12 (receita dos últimos 12 meses) atual?"

### 9.14 ICMS-ST

- **9.14 ICMS-ST** — Regra de inferência: observar NF-e de entrada com indicação de ST. Pergunta fallback: "Algum de seus produtos está sujeito a ICMS Substituição Tributária?"

## Seção 10 — Material de referência

### Fontes

**Legislação primária (sistema atual):**
1. Constituição Federal — Arts. 153 (IPI, PIS, Cofins), 155 (ICMS), 156 (ISS), 156-A (IBS)
2. Lei Complementar 87/1996 (Lei Kandir) — ICMS
3. Lei 10.637/2002 — PIS não cumulativo
4. Lei 10.833/2003 — Cofins não cumulativo
5. Lei 9.718/1998 — PIS/Cofins cumulativo
6. Lei Complementar 116/2003 — ISS
7. Lei Complementar 157/2016 — Alíquota mínima de ISS (2%)
8. Resolução do Senado Federal 13/2012 — alíquota interestadual de 4% para mercadorias importadas
9. Decreto 7.212/2010 (RIPI) — regulamentação do IPI
10. Lei Complementar 123/2006 — Simples Nacional (e art. 21-A, incluído pela LC 214/2025)
11. Lei Complementar 190/2022 — DIFAL após a EC 87/2015

**Legislação da reforma (sistema novo):**
12. Emenda Constitucional 132/2023 — base constitucional de CBS/IBS/IS
13. Lei Complementar 214/2025 — regulamentação de CBS/IBS/IS (primeira fase)
14. Lei Complementar 227/2026 — segunda fase, regras de Comitê Gestor do IBS e partilha

**Precedentes judiciais:**
15. STF RE 574.706 — exclusão do ICMS da base de PIS/Cofins
16. STF ADIs 1.945 e 5.659 — software sujeito a ISS, não a ICMS

**Outros:**
17. Receita Federal — https://www.gov.br/receitafederal
18. CONFAZ — https://www.confaz.fazenda.gov.br (convênios e protocolos de ICMS)
19. Taxa PTAX — Banco Central do Brasil

### Lacunas conhecidas

1. A biblioteca de fornecedores cobre marcas nacionais comuns, mas não negócios regionais ou concessionárias específicas de estado.
2. Percentuais de MVA em ICMS-ST são por produto e estado; esta skill não contém a base completa de protocolos CONFAZ.
3. Programas estaduais de incentivo de ICMS (guerra fiscal) não são cobertos.
4. A transição CBS/IBS está em curso — alíquotas e regras podem mudar conforme regulamentação do Comitê Gestor.
5. Os exemplos resolvidos usam um consultor de SP. Outras combinações estado/município podem produzir resultados distintos.
6. Alíquotas municipais de ISS não estão exaustivamente listadas — há mais de 5.500 municípios.

### Change log

- **v3.0 (Maio 2026):** Reescrita completa em PT-BR. Consolida o conteúdo de br-indirect-tax.md em brazil-vat.md. Acrescenta cronograma detalhado de transição CBS/IBS (LC 214/2025, LC 227/2026), regime híbrido do Simples (art. 21-A), matriz ampliada de alíquotas ICMS estaduais, retenção de ISS na fonte, DIFAL, classificação de software (STF ADIs 1.945 e 5.659), sublimite do Simples de BRL 3.600.000 (LC 123/2006), Resolução SF 13/2012, LC 157/2016, LC 190/2022, R-BR-7 (cadeias IPI), R-BR-8 (litígio CBS/IBS) e prohibitions.
- **v2.0 (Abril 2026):** Reescrita completa na estrutura Malta v2.0. Quick reference (Seção 1), supplier pattern library (Seção 3), exemplos resolvidos (Seção 4), Tier 1 (Seção 5), Tier 2 (Seção 6), modelo Excel (Seção 7), guia de extrato bancário (Seção 8), onboarding fallback (Seção 9).
- **v1.0 (Abril 2026):** Versão monolítica anterior cobrindo os cinco tributos indiretos e contexto da reforma.

### Self-check (v3.0)

1. Quick reference no topo, com os cinco tributos atuais e contexto da reforma CBS/IBS/IS: sim (Seção 1).
2. Defaults conservadores com tratamento específico por regime: sim (Seção 1).
3. Biblioteca de fornecedores como tabelas literais com fornecedores brasileiros: sim (Seção 3, 14 sub-tabelas).
4. Exemplos resolvidos do consultor SP + exemplos adicionais (interestadual, DIFAL, retenção ISS): sim (Seção 4, 9 exemplos).
5. Tier 1 comprimido: sim (Seção 5, 15 regras).
6. Tier 2 comprimido: sim (Seção 6, 13 itens).
7. Modelo Excel: sim (Seção 7).
8. Guia de leitura de extrato bancário: sim (Seção 8).
9. Onboarding como fallback com regras de inferência: sim (Seção 9, 14 itens).
10. Distinção PIS/Cofins cumulativo vs não cumulativo explícita: sim (Seções 1 e 5.2).
11. Cálculo por dentro do ICMS explícito: sim (Seção 5.4).
12. Tributação de importação de serviço (~40% efetivo) explícita: sim (Seções 5.8 e Exemplo 3).
13. Tratamento de Simples Nacional via DAS explícito: sim (Seções 5.11 e Exemplo 4).
14. Sublimite Simples BRL 3.600.000 explícito: sim (Seções 1 e 5.11).
15. Imunidade de exportação em todos os tributos explícita: sim (Seção 5.7).
16. Catálogo de recusas presente: sim (Seção 2, R-BR-1 a R-BR-8).
17. Cronograma detalhado CBS/IBS: sim (Seção 1).
18. Regime híbrido do Simples (art. 21-A LC 123/06 via LC 214/2025): sim (Seção 1).

## Fim da Skill Brasil — Tributos Indiretos v3.0

## PROIBIÇÕES

- NUNCA aplicar ICMS a serviços puros — serviços sujeitam-se a ISS (exceto telecomunicações e transporte interestadual).
- NUNCA aplicar ISS a venda de mercadoria física — mercadoria sujeita-se a ICMS.
- NUNCA ignorar o sublimite de BRL 3.600.000 do Simples Nacional para ICMS/ISS.
- NUNCA presumir que as alíquotas de ICMS são uniformes entre estados — variam de 7% a 25%+.
- NUNCA presumir que as alíquotas de ISS são iguais em todos os municípios — variam de 2% a 5%.
- NUNCA computar IPI para prestadores de serviço puro — IPI incide apenas em produtos industrializados.
- NUNCA ignorar obrigações de ICMS-ST — aplicam-se inclusive a empresas do Simples Nacional.
- NUNCA opinar sobre a reforma IBS/CBS como se já estivesse plenamente em vigor.
- NUNCA apresentar cálculos como definitivos — sempre rotular como estimativos e direcionar o cliente a um contador registrado no CRC.

## Disclaimer

Esta skill e seus produtos são fornecidos exclusivamente para fins informativos e de cálculo e não constituem aconselhamento tributário, jurídico ou financeiro. Open Accountants e seus contribuintes não assumem qualquer responsabilidade por erros, omissões ou consequências decorrentes do uso desta skill. Todos os resultados devem ser revisados e assinados por profissional qualificado (contador registrado no CRC, advogado tributarista ou profissional licenciado equivalente) antes do envio ou da tomada de decisão.

A versão mais atualizada e verificada desta skill é mantida em [openaccountants.com](https://openaccountants.com). Faça login para acessar a versão mais recente, solicitar revisão profissional de contador licenciado e acompanhar atualizações conforme a legislação tributária evolui.

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
