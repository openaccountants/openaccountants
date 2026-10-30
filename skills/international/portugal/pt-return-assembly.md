---
name: pt-return-assembly
description: "Utilizar esta skill sempre que for solicitada a montagem, finalização ou consolidação de um pacote fiscal anual português do período de tributação de 2026 (campanha de entrega em 2027): IRS (pessoas singulares, Modelo 3 e anexos, entregue de 1 de abril a 30 de junho de 2027) e/ou IRC (sociedades, Modelo 22 até 31 de maio de 2027, IES até 15 de julho de 2027). Acionar com expressões como \"preparar declaração IRS final\", \"preparar Modelo 22 final\", \"pacote contabilista certificado\", \"working paper Portugal\", \"submissão Portal das Finanças\", \"consolidação fiscal Portugal\", \"fechar a declaração\", \"montar dossier fiscal\", \"review final antes de submeter no Portal das Finanças\", \"pacote OCC para revisão\", \"encerramento do ano fiscal português\", \"preparar IES\", \"preparar SAF-T anual\", \"consolidar Modelo 3 e Anexos\", \"consolidar Modelo 22 e Anexos\", ou pedidos equivalentes em inglês: \"Portugal return assembly\", \"Portugal final tax package\", \"Portugal working paper\", \"Portugal IRS/IRC submission package\", \"Portuguese tax return capstone\". Esta é a skill capstone orquestradora que consolida os outputs de pt-income-tax, pt-irs-employees-investment, pt-nhr-ifici, pt-foreign-source-treaties, pt-corporate-tax, portugal-vat-return, pt-social-contributions, portugal-payroll, portugal-bookkeeping, portugal-financial-statements e portugal-crypto-tax num único working paper unificado, com reconciliações cross-skill, instruções de pagamento via Portal das Finanças, instruções de submissão (Modelo 3 / Modelo 22 / IES / SAF-T) e lista final de ações do contribuinte. Não recalcula nada: apenas reconcilia, monta e empacota para o revisor. Fora do âmbito: não-residentes (pt-cross-border), preços de transferência em detalhe (pt-transfer-pricing). LER SEMPRE este skill em ÚLTIMO LUGAR: é o capstone que consolida todos os outputs upstream."
version: 1.1
jurisdiction: PT
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# PT Return Assembly

## Portugal: Montagem Final da Declaração (Capstone), Skill v1.1 (período de tributação 2026)

## DIRETIVA DE EXECUÇÃO CRÍTICA: LER PRIMEIRO

**Quando esta skill é invocada, o contribuinte já passou pelo intake e pelas skills de conteúdo relevantes. Pretende o working paper final pronto para revisão pelo Contabilista Certificado (OCC). Executar todos os passos sem parar para pedir autorização.**

Em concreto:

- **Não perguntar "quer que monte o pacote completo?".** O utilizador pediu a montagem. Produzir.
- **Não voltar a interrogar sobre NIF, residência fiscal, NIPC, CAE, ou estrutura do negócio.** O intake já capturou estes dados; confiar nos packages upstream.
- **Não pausar entre passos de reconciliação para confirmar.** Executar todas as verificações cruzadas em sequência; sinalizar falhas no brief do revisor e continuar.
- **As auto-verificações são alvos, não bloqueadores.** Se uma verificação falhar, registar em "Sinalizações para o Revisor" e continuar.
- **Não submeter nada no Portal das Finanças, no e-fatura, no portal da Segurança Social, ou em qualquer outro portal.** Esta skill produz um working paper e instruções de submissão. Um **Contabilista Certificado** (membro da OCC, Ordem dos Contabilistas Certificados) tem de rever e assinar quando a declaração assenta em contabilidade organizada, e o contribuinte (ou o CC, no seu acesso) submete via Portal das Finanças.

**Se sentir necessidade de perguntar "como devo proceder?", escolha o caminho mais defensável, prossiga, e sinalize a decisão para o revisor.**

## O que este ficheiro é

A skill capstone final para a campanha fiscal portuguesa do **período de tributação de 2026**, cujas declarações anuais são entregues em 2027. Consome os outputs de todas as outras skills Portugal e monta um único working paper unificado que cobre, conforme aplicável:

- **Modelo 3 do IRS**: declaração anual de rendimentos das pessoas singulares (trabalhadores por conta de outrem, pensionistas, trabalhadores independentes / Categoria B, sócios-gerentes que recebam remuneração, sujeitos passivos com rendimentos prediais ou de mais-valias), entregue por transmissão eletrónica no **Portal das Finanças** de 1 de abril a 30 de junho de 2027 (CIRS art. 60.º, n.º 1), com o rosto e os anexos A, B, C, D, E, F, G, G1, H, I, J e L (Portaria n.º 104/2026/1, art. 1.º) e o Anexo SS quando aplicável.
- **Modelo 22 do IRC**: declaração periódica de rendimentos das sociedades e outras entidades sujeitas a IRC, enviada até ao último dia de maio de 2027 (CIRC art. 120.º, n.º 1), com os anexos aplicáveis (Despacho n.º 320/2026): A (derrama municipal), C (regiões autónomas), D (benefícios fiscais), E (regime simplificado), F (organismos de investimento coletivo), G (regime especial do transporte marítimo) e AIMI. O Anexo B só se usa para períodos anteriores a 2011.
- **IES (Informação Empresarial Simplificada)**: declaração anual de informação contabilística e fiscal (CIRC art. 117.º, n.º 1, al. c), e art. 121.º), enviada até 15 de julho de 2027.
- **SAF-T (PT)**: ficheiro normalizado criado pela Portaria n.º 321-A/2007; a comunicação das faturas à AT é feita até ao dia 5 do mês seguinte ao da emissão (Decreto-Lei n.º 198/2012, art. 3.º, n.º 2).
- **Declaração periódica de IVA**: mensal (volume de negócios do ano anterior igual ou superior a €650.000) ou trimestral, até ao dia 20 do 2.º mês seguinte (CIVA art. 41.º, n.º 1).
- **DMR (Declaração Mensal de Remunerações)**: obrigação dos empregadores, até ao dia 10 do mês seguinte ao do pagamento (CIRS art. 119.º, n.º 1, al. c), subal. i)).
- **Declaração trimestral da Segurança Social** dos trabalhadores independentes: até ao último dia de janeiro, abril, julho e outubro (ISS, Guia Prático dos Trabalhadores Independentes).

O output é um pacote pronto para o revisor: working paper linha-a-linha, tabela de reconciliação cross-skill, instruções de pagamento (referência para pagamento gerada pelo Portal das Finanças), instruções de submissão para Portal das Finanças e Segurança Social Direta, checklist do revisor, e lista final de ações do contribuinte.

## Secção 1: Referência Rápida

**Referência Rápida**

| Campo | Valor |
| --- | --- |
| País | República Portuguesa |
| Autoridade tributária | Autoridade Tributária e Aduaneira (AT) |
| Portal de submissão (fiscal) | Portal das Finanças (https://www.portaldasfinancas.gov.pt) |
| Portal de e-faturação | Portal e-fatura (https://faturas.portaldasfinancas.gov.pt) |
| Portal de Segurança Social | Segurança Social Direta (https://www.seg-social.pt) |
| Plataforma de pagamento | Referência para pagamento gerada pelo Portal das Finanças (Multibanco / home banking); outros canais conforme indicado no documento de cobrança |
| Moeda | EUR (€) |
| Ano fiscal: pessoas singulares | Ano civil (1 janeiro a 31 dezembro) |
| Ano fiscal: sociedades | Ano civil, salvo período diferente adotado nos termos do CIRC art. 8.º, n.os 2 e 3 |
| Período de tributação desta versão | **2026** (campanha de entrega em 2027) |
| Declaração singular | **Modelo 3** (IRS), transmissão eletrónica obrigatória (Portaria n.º 104/2026/1, art. 2.º, n.º 1) |
| Declaração sociedades | **Modelo 22** (IRC), por transmissão eletrónica de dados (CIRC art. 120.º, n.º 1) |
| Declaração anual de informação contabilística e fiscal | **IES** (CIRC art. 121.º) |
| Comunicação de faturas | e-fatura / SAF-T (PT), até ao dia 5 do mês seguinte (DL 198/2012, art. 3.º, n.º 2) |
| Declaração de IVA | Declaração periódica (mensal ou trimestral, CIVA art. 41.º) |
| Declaração mensal de remunerações | **DMR** (até dia 10 do mês seguinte; CIRS art. 119.º, n.º 1, al. c), i)) |
| Prazo Modelo 3 IRS 2026 | **1 abril a 30 junho 2027**, "independentemente de este dia ser útil ou não útil" (CIRS art. 60.º, n.º 1) |
| Prazo Modelo 22 IRC 2026 (período = ano civil) | **31 maio 2027** (último dia de maio, útil ou não; CIRC art. 120.º, n.º 1). Período diferente: último dia do 5.º mês seguinte ao termo (art. 120.º, n.º 2) |
| Prazo IES 2026 | **15 julho 2027** (CIRC art. 121.º, n.º 2). Período diferente: 15.º dia do 7.º mês posterior ao termo (art. 121.º, n.º 3) |
| Prazo comunicação de faturas | Até **dia 5** do mês seguinte ao da emissão (DL 198/2012, art. 3.º, n.º 2) |
| Prazo declaração periódica de IVA | Até **dia 20 do 2.º mês seguinte** ao mês (mensal) ou ao trimestre (trimestral) (CIVA art. 41.º, n.º 1); pagamento até **dia 25 do 2.º mês seguinte** (CIVA art. 27.º, n.º 1) |
| Prazo DMR | Até **dia 10** do mês seguinte ao do pagamento (CIRS art. 119.º, n.º 1, al. c), i)) |
| Prazo declaração trimestral SS (independentes) | Até ao **último dia de janeiro, abril, julho e outubro** (ISS, Guia Prático) |
| Recibo / comprovativo | Comprovativo de entrega emitido pelo Portal das Finanças |
| Legislação fundamental | Código do IRS (Decreto-Lei n.º 442-A/88), Código do IRC (Decreto-Lei n.º 442-B/88), Código do IVA (Decreto-Lei n.º 394-B/84), Lei Geral Tributária (LGT, Decreto-Lei n.º 398/98), Regime Geral das Infrações Tributárias (RGIT, Lei n.º 15/2001), Código Contributivo (Lei n.º 110/2009), Estatuto dos Benefícios Fiscais (EBF, Decreto-Lei n.º 215/89), Lei n.º 64/2025 (taxas de IRC 2026 e 2027), Orçamento do Estado para 2026 (Lei n.º 73-A/2025), Estatuto da OCC |
| Versão da skill | 1.1 |
| Validada por | Pendente: requer assinatura por **Contabilista Certificado** membro da OCC quando a declaração assenta em contabilidade organizada (Estatuto da OCC, art. 10.º, n.º 1, al. b)) |

**Prazos em dia não útil.** Os prazos do Modelo 3, do Modelo 22 e da IES correm "independentemente de esse dia ser útil ou não útil". Para os prazos de IVA, a regra de transição para o dia útil seguinte e as datas concretas de 2027 estão em `portugal-vat-return`.

## Secção 2: Entradas Obrigatórias dos Skills Upstream

A skill de montagem **não recalcula nada**. Espera outputs estruturados das skills upstream abaixo. Se uma skill upstream não tiver corrido, a montagem sinaliza a lacuna e continua com os dados disponíveis.

### 2.1 Declaração singular (Modelo 3): inputs

**Inputs Modelo 3**

| Skill upstream | Output consumido | Onde aparece no Modelo 3 |
| --- | --- | --- |
| `pt-income-tax` | Rendimentos da Categoria B (trabalho independente): regime simplificado vs contabilidade organizada, coeficientes do art. 31.º, retenções na fonte, pagamentos por conta, IRS Jovem, taxas progressivas de 2026 e adicional de solidariedade | Anexo B (regime simplificado ou atos isolados), Anexo C (contabilidade organizada) |
| `pt-irs-employees-investment` | Trabalho dependente e pensões (Categoria A e H), rendimentos de capitais (E), prediais (F), mais-valias (G), deduções à coleta | Anexo A, Anexo E, Anexo F, Anexo G, Anexo G1, Anexo H |
| `pt-nhr-ifici` | Regime de Residente Não Habitual (regime transitório) ou IFICI (EBF art. 58.º-A); rendimentos de fonte estrangeira com tratamento próprio | Anexo L |
| `pt-foreign-source-treaties` | Rendimentos de fonte estrangeira, crédito de imposto por dupla tributação internacional (CIRS art. 81.º), aplicação de Convenções para Evitar a Dupla Tributação (CDT) | Anexo J (rendimentos obtidos no estrangeiro) |
| `pt-corporate-tax` | (Apenas se o sujeito passivo for sócio de uma sociedade em transparência fiscal, CIRC art. 6.º) Lucro tributável imputado ao sócio | Anexo D (imputação de rendimentos) |
| `portugal-vat-return` | Para trabalhadores independentes Categoria B com IVA: posição anual de IVA; reconciliação de volume de negócios apenas | Verificação cruzada; não aparece diretamente no Modelo 3 |
| `pt-social-contributions` | Contribuições para a Segurança Social pagas como trabalhador independente; declarações trimestrais | Anexo B / C (contribuições); Anexo SS ao Modelo 3 |
| `portugal-bookkeeping` | Para contabilidade organizada: demonstração de resultados, conciliação fiscal-contabilística | Anexo C (campos de apuramento) |
| `portugal-crypto-tax` | Ganhos com criptoativos (CIRS art. 10.º, n.º 1, al. k)); detenção inferior a 365 dias (tributada) ou igual ou superior a 365 dias (excluída, art. 10.º, n.º 22); mineração e outras operações da Categoria B | Anexo G / Anexo G1 ou Anexo B / C consoante natureza |
| `portugal-payroll` | Trabalhador independente que também recebe rendimentos de trabalho dependente: salários, retenções de IRS, contribuições para a Segurança Social, quotizações sindicais | Anexo A |

**Anexos do Modelo 3 em vigor** (Portaria n.º 104/2026/1, art. 1.º, produz efeitos a 1 de janeiro de 2026): aprovados de novo os anexos A (trabalho dependente e pensões), B (rendimentos empresariais e profissionais, regime simplificado ou atos isolados), C (contabilidade organizada), D (imputação de rendimentos), H (benefícios fiscais e deduções) e J (rendimentos obtidos no estrangeiro); mantidos com novas instruções os anexos E (rendimentos de capitais) e G (mais-valias e outros incrementos patrimoniais); mantidos o rosto e os anexos F (rendimentos prediais), G1 (mais-valias não tributadas) e L (residente não habitual / incentivo fiscal à investigação científica e inovação), aprovados pela Portaria n.º 72-B/2025/1, e o Anexo I (rendimentos de herança indivisa), aprovado pela Portaria n.º 39-B/2024. Os modelos "destinam-se a declarar os rendimentos dos anos de 2015 e seguintes" (art. 1.º, n.º 4), pelo que servem para os rendimentos de 2026 até serem substituídos. As instruções do Anexo H foram depois alteradas pela Portaria n.º 136-C/2026/1.

### 2.2 Declaração de sociedades (Modelo 22): inputs

**Inputs Modelo 22**

| Skill upstream | Output consumido | Onde aparece no Modelo 22 |
| --- | --- | --- |
| `pt-corporate-tax` | Lucro tributável, taxa de IRC (19% para períodos iniciados em 2026; 15% sobre os primeiros €50.000 para PME e Small Mid Cap; 12,5% startups), derrama estadual (CIRC art. 87.º-A), derrama municipal, tributações autónomas (CIRC art. 88.º), prejuízos fiscais (CIRC art. 52.º), benefícios fiscais ao investimento (RFAI, SIFIDE II) | Modelo 22 (apuramento do lucro tributável, matéria coletável e cálculo do imposto); Anexos A, C, D, E |
| `portugal-bookkeeping` | Balancete final pós-encerramento, demonstração de resultados, balanço, mapas de depreciações e amortizações (Modelo 32) | Suporta Modelo 22 + IES |
| `portugal-financial-statements` | Demonstrações financeiras (SNC, NCM ou NCM-ME): Balanço, Demonstração de Resultados por Naturezas, Demonstração das Alterações no Capital Próprio, Demonstração dos Fluxos de Caixa, Anexo | Submetidas via IES; suportam Modelo 22 |
| `portugal-vat-return` | Posição anual de IVA da sociedade; declarações periódicas; pro-rata se aplicável; regularizações | Verificação cruzada; reflete-se na IES |
| `portugal-payroll` | Custos com pessoal, retenções na fonte de IRS dos colaboradores (Categoria A), contribuições para a Segurança Social | Modelo 22 (gastos com pessoal); cruzamento com DMR |
| `pt-social-contributions` | Contribuições da entidade empregadora e dos trabalhadores; membros de órgãos estatutários (MOE); entidades contratantes | DMR + Modelo 22 verificação cruzada |
| `pt-foreign-source-treaties` | Rendimentos de fonte estrangeira da sociedade; crédito por dupla tributação internacional (CIRC art. 91.º); participation exemption (CIRC art. 51.º) | Modelo 22, deduções à coleta e correções ao resultado |
| `pt-transfer-pricing` | Operações com entidades relacionadas (CIRC art. 63.º; Portaria n.º 268/2021) | Correções no Modelo 22; informação na IES |
| `portugal-crypto-tax` | Ganhos e perdas em criptoativos detidos pela sociedade, tratados consoante natureza contabilística | Modelo 22 (correções fiscais ao resultado contabilístico) |

**Impresso a usar para o período de 2026.** O Modelo 22 e os anexos são aprovados por despacho (CIRC art. 117.º, n.º 2). O impresso em vigor a 30 de outubro de 2026 é o do Despacho n.º 320/2026, feito para as alterações legislativas de 2025: o seu campo 347-B ainda multiplica por 20% e o 347-A por 16% (PME) ou 12,5% (startups), as taxas dos períodos de 2025. A declaração do período de 2026 (enviada até 31 de maio de 2027) usa o impresso que estiver aprovado para essa campanha; confirmar o novo despacho antes de preencher.

**Anexos do Modelo 22 em vigor em 2026** (Despacho n.º 320/2026, de 9 de janeiro): aprovados de novo a declaração Modelo 22 e os anexos C, D e F; mantidos os anexos A (períodos de 2015 e seguintes), B (apenas períodos anteriores a 2011), E, G e AIMI, aprovados pelo Despacho n.º 422/2025. Títulos dos formulários da AT: A "Derrama municipal", C "Regiões Autónomas", D "Benefícios fiscais", E "Regime simplificado", F "Organismos de investimento coletivo", G "Regime especial de determinação da matéria coletável" (atividades de transporte marítimo).

**Quadro 10 (Cálculo do imposto) do impresso do Despacho n.º 320/2026.** Campos usados nas reconciliações desta skill; confirmar no impresso aprovado para a campanha de 2027:

| Campo | Conteúdo (fórmula impressa no quadro) |
| --- | --- |
| 347-A / 347-B | Imposto à taxa reduzida (primeiros €50.000) / à taxa normal |
| 351 | Coleta (347-A + 347-B + 349 + 350 + 370): IRC apenas, sem derramas nem tributações autónomas |
| 373 | Derrama estadual (art. 87.º-A) |
| 378 | Coleta total (351 + 373) |
| 353 | Dupla tributação jurídica internacional (art. 91.º) |
| 355 | Benefícios fiscais |
| 356 | Pagamento especial por conta (art. 93.º) |
| 357 / 358 | Total das deduções / total do IRC liquidado (378 - 357) |
| 359 | Retenções na fonte |
| 360 | Pagamentos por conta (art. 105.º) |
| 374 | Pagamentos adicionais por conta (art. 105.º-A) |
| 361 / 362 | IRC a pagar / IRC a recuperar (358 + 371 - 359 - 360 - 374) |
| 364 | Derrama municipal (o Anexo A transporta para este campo) |
| 365 | Tributações autónomas |
| 366 / 369 | Juros compensatórios / juros de mora |
| 367 / 368 | Total a pagar / total a recuperar |

### 2.3 Identificadores exigidos pelo intake

**Identificadores**

| Identificador | Obrigatório para |
| --- | --- |
| **NIF** (Número de Identificação Fiscal), atribuído pela AT a pessoas singulares e coletivas | Todas as declarações |
| **NISS** (Número de Identificação de Segurança Social) | Declarações Segurança Social, DMR, declaração trimestral |
| **NIPC** (Número de Identificação de Pessoa Coletiva), coincide com o NIF da sociedade | Modelo 22, IES |
| **CAE** (Classificação das Atividades Económicas), código principal e códigos secundários | Modelo 22, IES, Anexo B do Modelo 3 (art. 151.º do CIRS e coeficientes) |
| **Senha de acesso ao Portal das Finanças** | Submissão pelo próprio |
| **Senha do Contabilista Certificado** | Nos casos em que a declaração deva por este ser assinada, o CC é identificado por senha atribuída pela AT (Portaria n.º 104/2026/1, art. 2.º, n.º 2) |
| **Regime de IVA**: normal mensal, normal trimestral, isenção do art. 53.º (volume de negócios até €15.000), outros regimes especiais | Declaração periódica de IVA |
| **Domicílio fiscal e estabelecimentos**: concelho (define derrama municipal e o Anexo A) | Modelo 22, Anexo A |
| **Período de tributação** (sociedades com período não coincidente com ano civil) | Modelo 22, IES |
| **Estado civil + dependentes + agregado familiar**; opção por tributação conjunta | Modelo 3, rosto |
| **Residência fiscal** (residente, não residente, RNH, IFICI, Madeira/Açores) | Modelo 3 |
| **IBAN** + comprovativo de titularidade | Reembolsos e pagamentos |

- **Identificador em falta**: se qualquer identificador estiver em falta, a skill de montagem sinaliza-o como "Necessita Input" e produz o working paper com placeholders em vez de parar. Regra interna de trabalho desta skill, não uma regra legal.

### 2.4 Coordenação AT + Segurança Social + e-fatura

Portugal tem obrigações declarativas em portais distintos:

- **AT (Portal das Finanças):** Modelo 3, Modelo 22, IES, declarações periódicas de IVA, comunicação de faturas, DMR, declarações de retenções (Modelo 10, Modelo 39, Modelo 30), IMI, IMT, IUC.
- **Segurança Social (Segurança Social Direta):** contribuições de trabalhadores por conta de outrem e da entidade empregadora, declaração trimestral e contribuições dos trabalhadores independentes, entidades contratantes. A declaração anual dos independentes em contabilidade organizada faz-se através do Anexo SS ao Modelo 3, "enviada aos serviços da Segurança Social pela entidade tributária competente" (ISS, Guia Prático).
- **e-fatura (faturas.portaldasfinancas.gov.pt):** comunicação das faturas emitidas, em tempo real, por ficheiro SAF-T (PT) ou por inserção direta no Portal, até ao dia 5 do mês seguinte (DL 198/2012, art. 3.º, n.os 1 e 2).

A capstone produz **um pacote único integrado** com as três vertentes reconciliadas. Um sócio-gerente de uma sociedade unipessoal por quotas, por exemplo, terá obrigações como contribuinte singular (Modelo 3), como sociedade (Modelo 22 e IES), e perante a Segurança Social (como membro de órgão estatutário). A montagem cruza as três.

## Secção 3: Workflow de Montagem, Reconciliações Cross-Skill

- **Regra geral de tolerância**: a skill de montagem verifica que os números das skills upstream são mutuamente consistentes. Se uma verificação cruzada falhar por mais de €1,00, a discrepância é levantada no brief do revisor, nunca arredondada silenciosamente. Regra interna de trabalho desta skill, não uma regra legal.

### 3.1 Verificação cruzada 1: Reconciliação de volume de negócios

**Reconciliação volume de negócios**

| Origem | Valor | Regra |
| --- | --- | --- |
| `portugal-bookkeeping` / balancete: volume de negócios líquido | Total dos rendimentos operacionais | Valor âncora |
| `portugal-vat-return`: soma das bases tributáveis anuais de IVA das declarações periódicas, ajustada para operações isentas e não sujeitas | Soma das 12 declarações mensais (ou 4 trimestrais) | Deve reconciliar com a contabilidade, com diferenças temporais admissíveis e operações fora do campo do IVA identificadas |
| `pt-corporate-tax` (sociedades) / `pt-income-tax` (singulares): total dos rendimentos brutos | Topo do quadro de apuramento fiscal | Tem de igualar a contabilidade, mais ou menos as correções fiscais ao resultado contabilístico no Modelo 22 |
| Faturas comunicadas à AT (e-fatura / SAF-T faturação) no ano | Soma dos documentos emitidos | Deve reconciliar com volume de negócios, mais ou menos notas de crédito e ajustamentos |

**Se houver divergência:** causas habituais são (i) operações isentas do art. 9.º do CIVA não capturadas pela skill de IVA, (ii) diferenças temporais entre o momento do IVA e a periodização contabilística (CIRC art. 18.º), (iii) operações intracomunitárias com autoliquidação pelo adquirente, (iv) rendimentos não sujeitos a IVA mas sujeitos a IRC/IRS, (v) ajustamentos de períodos anteriores.

Os elementos das declarações de IRC e da IES "devem, sempre que for caso disso, concordar exactamente com os obtidos na contabilidade" (CIRC art. 120.º, n.º 10, e art. 121.º, n.º 5).

### 3.2 Verificação cruzada 2: Créditos de imposto e retenções

**Créditos e retenções: pessoas singulares (Modelo 3)**

| Linha | Skill de origem | Descrição |
| --- | --- | --- |
| Retenções na fonte sobre rendimentos do trabalho dependente e pensões | pt-irs-employees-investment + portugal-payroll | Crédito; Anexo A |
| Retenções na fonte sobre rendimentos da Categoria B pagos por entidades com contabilidade organizada: 23% (atividades da tabela do art. 151.º), 16,5% (rendimentos da al. c) do n.º 1 do art. 3.º), 11,5% (outros rendimentos da Categoria B), 20% (IFICI, EBF art. 58.º-A) | pt-income-tax | Crédito; Anexo B ou C (CIRS art. 101.º, n.º 1, als. a) a d)) |
| Retenções na fonte sobre rendimentos prediais (Categoria F): 25%; 10% para os rendimentos abrangidos pelo EBF art. 45.º-C, n.º 1 | pt-irs-employees-investment | Crédito; Anexo F (CIRS art. 101.º, n.º 1, als. e) e f)) |
| Retenções na fonte sobre rendimentos de capitais (Categoria E): taxa liberatória de 28%; 35% nos casos do art. 71.º, n.º 17 | pt-irs-employees-investment | Tributação liberatória, ou crédito se o titular optar pelo englobamento (CIRS art. 71.º) |
| Crédito de imposto por dupla tributação internacional (CIRS art. 81.º) | pt-foreign-source-treaties | Crédito; limitado ao menor entre o imposto pago no estrangeiro e a fração do IRS correspondente |
| Pagamentos por conta de IRS efetuados durante 2026 (CIRS art. 102.º) | pt-income-tax | Crédito |

**Créditos e retenções: sociedades (Modelo 22)**

| Linha | Skill de origem | Descrição |
| --- | --- | --- |
| Retenções na fonte suportadas pela sociedade (rendas, juros, dividendos, prestações de serviços) | pt-corporate-tax | Dedução ao imposto apurado |
| Pagamentos por conta de IRC (CIRC art. 104.º e 105.º): três pagamentos, com vencimento em julho, setembro e 15 de dezembro de 2026 | pt-corporate-tax | Dedução ao imposto apurado |
| Pagamentos adicionais por conta (CIRC art. 104.º-A e 105.º-A), quando houve derrama estadual no período anterior | pt-corporate-tax | Dedução à derrama estadual |
| Pagamento especial por conta (CIRC art. 106.º): revogado pela Lei n.º 12/2022 para os períodos iniciados em ou após 1 de janeiro de 2022 | pt-corporate-tax | Nenhum PEC é devido em 2026 |
| Crédito de imposto por dupla tributação internacional (CIRC art. 91.º) | pt-foreign-source-treaties | Dedução à coleta |
| Benefícios fiscais com natureza de crédito (RFAI, SIFIDE II) | pt-corporate-tax | Dedução à coleta; Anexo D |

- **Regra de créditos**: o total dos créditos não gera reembolso para além do que a lei preveja. O IRC é reembolsado quando o valor apurado, líquido das deduções, for negativo ou inferior aos pagamentos por conta (CIRC art. 104.º, n.º 2); não há pagamento nem reembolso inferior a €25 (art. 104.º, n.º 7). Cada retenção tem de estar suportada pelo documento comprovativo que a entidade devedora entrega ao titular até 20 de janeiro (CIRS art. 119.º, n.º 1, al. b)) e pelas declarações do substituto tributário (Modelo 10, Modelo 39).

### 3.3 Verificação cruzada 3: DMR mensal vs declaração anual

**DMR vs Modelo 10**

| Item | Origem | Regra |
| --- | --- | --- |
| Soma das 12 DMR (janeiro a dezembro de 2026): rendimentos do trabalho dependente pagos, retenções de IRS, contribuições obrigatórias e quotizações sindicais | portugal-payroll | A DMR é entregue até ao dia 10 do mês seguinte ao do pagamento (CIRS art. 119.º, n.º 1, al. c), i)); tem de reconciliar com a folha salarial anual e com o Anexo A dos colaboradores |
| Modelo 10 (restantes rendimentos do ano anterior: Categoria B, prediais, outros) | portugal-payroll / pt-income-tax | Até ao **final de fevereiro de 2027** para os rendimentos de 2026 (CIRS art. 119.º, n.º 1, al. c), ii), redação do DL 49/2025) |
| Declaração de substituição da DMR / Modelo 10 | portugal-payroll | Nos 30 dias imediatos ao facto que altere os rendimentos declarados (CIRS art. 119.º, n.º 1, al. d)) |
| Coima por falta ou atraso | RGIT art. 117.º, n.º 1 | €150 a €3.750 (limites elevados para o dobro para pessoas coletivas, RGIT art. 26.º, n.º 4) |

**Se houver divergência:** verificar subsídios de férias e de Natal ou duodécimos não capturados na DMR mensal; benefícios em espécie reconhecidos apenas em fecho; correções salariais retroativas.

### 3.4 Verificação cruzada 4: Contribuições Segurança Social, empregadores e independentes

**Contribuições SS**

| Item | Origem | Regra |
| --- | --- | --- |
| Contribuições da entidade empregadora e dos trabalhadores sobre remunerações: regime geral 34,75%, cabendo 23,75% à entidade empregadora e 11% ao trabalhador (Código Contributivo art. 53.º); membros de órgãos estatutários com funções de gerência ou administração, também 34,75% (23,75% + 11%, art. 69.º, n.º 2); taxas especiais em `pt-social-contributions` | pt-social-contributions + portugal-payroll | Cruzar a declaração de remunerações à Segurança Social com as folhas de salário e a DMR |
| Prazos da entidade empregadora | pt-social-contributions + portugal-payroll | Confirmar ou corrigir a declaração de remunerações até ao dia 20 do mês seguinte (art. 40.º, n.º 8); pagar entre o dia 1 e o dia 25 do mês seguinte (art. 43.º, redação do DL 127/2025, em vigor desde 1 de janeiro de 2026) |
| Contribuições do trabalhador independente: 21,4% (25,2% para empresários em nome individual e titulares de EIRL) sobre o rendimento relevante, que é 70% do valor das prestações de serviços e 20% dos rendimentos da produção e venda de bens | pt-social-contributions | Declaração trimestral; reconciliar com Modelo 3, Anexo B |
| Início de enquadramento dos independentes: produz efeitos no 1.º dia do 12.º mês após o início de atividade | pt-social-contributions | Confirmar data de início e se houve reinício |
| Contribuição mínima: €20,00 por mês quando não há rendimento ou o valor calculado seria inferior (ISS, Guia Prático; detalhe em `pt-social-contributions`) | pt-social-contributions | Confirmar meses com contribuição mínima |
| Coimas da Segurança Social (falta de declaração ou de pagamento) | pt-social-contributions | Escalões e montantes em `pt-social-contributions` |
| Isenções (acumulação com trabalho por conta de outrem com rendimento relevante médio inferior a 4 × IAS = €2.148,52; pensionistas) | pt-social-contributions | Confirmar status |
| IAS de 2026 | pt-social-contributions | €537,13 |

- **Incentivos à contratação**: reduções ou isenções contributivas de incentivo ao emprego (por exemplo, contratação de jovens) são verificadas em `pt-social-contributions`; a montagem apenas confirma que o upstream aplicou o regime com documentação de suporte.

### 3.5 Verificação cruzada 5: IVA suportado e dedutível, pro-rata

**IVA suportado e dedutível**

| Item | Origem | Regra |
| --- | --- | --- |
| IVA liquidado nas operações tributáveis em Portugal | portugal-vat-return | Somar os campos de imposto liquidado das declarações periódicas do ano |
| IVA dedutível | portugal-vat-return | Apenas sobre bens/serviços afetos a operações que conferem direito à dedução |
| Pro-rata definitivo do ano (se sujeito passivo misto), CIVA art. 23.º | portugal-vat-return | Calcular pro-rata anual; regularizar a diferença face ao pro-rata provisório na última declaração do ano |
| Regularizações de IVA | portugal-vat-return | Incluídas nas declarações periódicas: campos 40 e 41, cada um com o seu anexo; as regularizações a favor do sujeito passivo vão para o campo 40 (AT, Ofício-Circulado n.º 25119/2026) |
| Declaração recapitulativa de operações intracomunitárias | portugal-vat-return | Mensal ou trimestral; reconciliar com VIES (CIVA art. 29.º, n.º 1, al. i)) |
| IVA liquidado nas faturas comunicadas (e-fatura / SAF-T), por taxa | portugal-bookkeeping + e-fatura | Tem de reconciliar com a soma das declarações periódicas |

**Se houver divergência superior a €1:** as causas mais comuns são correção pro-rata em falta, faturas comunicadas no e-fatura sem reflexo nas declarações periódicas, ou notas de crédito não regularizadas.

### 3.6 Verificação cruzada 6: Tributações autónomas (Modelo 22)

Para sociedades, as tributações autónomas (CIRC art. 88.º) são calculadas sobre encargos específicos e acrescem ao imposto, mesmo em situação de prejuízo. Taxas de 2026:

**Tributações autónomas**

| Encargo | Taxa base | Em período com prejuízo fiscal |
| --- | --- | --- |
| Despesas não documentadas (art. 88.º, n.º 1) | 50% (70% para entidades isentas ou que não exerçam atividade comercial, industrial ou agrícola, n.º 2) | +10 pp |
| Encargos com viaturas ligeiras de passageiros com custo de aquisição inferior a €37.500 (art. 88.º, n.º 3, al. a)) | 8% | +10 pp |
| Viaturas com custo igual ou superior a €37.500 e inferior a €45.000 (al. b)) | 25% | +10 pp |
| Viaturas com custo igual ou superior a €45.000 (al. c)) | 32% | +10 pp |
| Viaturas híbridas plug-in elegíveis e viaturas a gás natural veicular, mesmos escalões (art. 88.º, n.º 18) | 2,5% / 7,5% / 15% | +10 pp |
| Viaturas exclusivamente elétricas (art. 88.º, n.º 20) | 10%, só se o custo exceder o valor da portaria do art. 34.º, n.º 1, al. e) | +10 pp |
| Despesas de representação (art. 88.º, n.º 7) | 10% | +10 pp |
| Pagamentos a entidades em regime fiscal claramente mais favorável, sem prova de operação efetiva e normal (art. 88.º, n.º 8) | 35% (55% nos casos do n.º 2) | +10 pp |
| Ajudas de custo e compensação por deslocação em viatura própria não faturadas a clientes (art. 88.º, n.º 9) | 5% | +10 pp |
| Bónus e remunerações variáveis a gestores superiores a 25% da remuneração anual e de valor superior a €27.500, salvo diferimento (art. 88.º, n.º 13, al. b)) | 35% | +10 pp |
| Indemnizações e compensações por cessação de funções de gestores (art. 88.º, n.º 13, al. a)) | 35% | +10 pp |
| Lucros distribuídos a sujeitos passivos com isenção total ou parcial, com participação detida há menos de um ano (art. 88.º, n.º 11) | 23% | +10 pp |

O agravamento de "10 pontos percentuais" aplica-se aos sujeitos passivos que apresentem prejuízo fiscal no período (art. 88.º, n.º 14). Fonte da tabela e detalhe das condições: `pt-corporate-tax`.

- **Confirmação TA**: a skill de montagem confirma que pt-corporate-tax calculou todas as TA aplicáveis e que a TA total foi acrescida ao imposto no Modelo 22. Tolerância: €1 (regra interna).

### 3.7 Verificação cruzada 7: Derramas (municipal + estadual)

**Derramas**

| Derrama | Base | Taxa | Quem |
| --- | --- | --- | --- |
| **Derrama Municipal** (Lei n.º 73/2013, art. 18.º) | Lucro tributável sujeito e não isento de IRC | Até 1,5%, fixada anualmente por cada município; taxa reduzida ou isenção possíveis para sujeitos passivos com volume de negócios do ano anterior até €150.000 | Sociedades residentes e estabelecimentos estáveis; Anexo A do Modelo 22 quando há estabelecimentos em mais de um município |
| **Derrama Estadual** (CIRC art. 87.º-A) | Parte do lucro tributável superior a €1.500.000 | 3% (de €1.500.000 até €7.500.000) + 5% (de €7.500.000 até €35.000.000) + 9% (acima de €35.000.000), cada taxa só sobre a sua parcela | Sociedades com lucro tributável superior a €1,5M |
| **Derrama Regional** Madeira/Açores | Regimes regionais | Taxas regionais | Não coberta por esta pack; ver `pt-corporate-tax` |

- **Total**: IRC + derrama municipal + derrama estadual + tributações autónomas formam o total a pagar no Modelo 22, deduzido dos pagamentos por conta e retenções. As derramas incidem sobre o **lucro tributável** (antes da dedução de prejuízos), não sobre a matéria coletável (ver `pt-corporate-tax`).

### 3.8 Verificação cruzada 8: Adicional de solidariedade (IRS)

**Adicional de solidariedade** (CIRS art. 68.º-A)

| Rendimento coletável | Taxa adicional |
| --- | --- |
| De mais de €80.000 até €250.000 | 2,5% |
| Superior a €250.000 | 5% |

- **Regra do adicional de solidariedade**: o adicional incide apenas sobre a parte do rendimento coletável que excede cada limiar. Em tributação conjunta, aplica-se ao rendimento dividido por dois e o resultado é multiplicado por dois (ver `pt-income-tax`). A skill de montagem cruza com pt-income-tax para confirmar que foi corretamente aplicado.

### 3.9 Verificação cruzada 9: Disciplina de tolerância

- **Disciplina de tolerância**: para cada verificação cruzada acima, o limiar é €1,00. Se uma diferença estiver entre €1 e €100, documentar a variação e prosseguir com sinalização ao revisor. Acima de €100, levantar como "Necessita Input": o revisor deve resolver antes da assinatura. Regra interna de trabalho desta skill, não uma regra legal.

## Secção 4: Estrutura do Working Paper para o Contabilista Certificado (OCC)

O revisor é um **Contabilista Certificado** inscrito na **OCC (Ordem dos Contabilistas Certificados)**. A inscrição na Ordem permite, em exclusivo, "a assinatura das demonstrações financeiras e das declarações fiscais que tenham por base informação contabilística" das entidades que possuam ou devam possuir contabilidade organizada (Estatuto da OCC, art. 10.º, n.º 1, al. b)). O brief é um único ficheiro markdown que o CC lê antes de assinar.

```markdown
# Pacote de Declaração Anual: [Nome do contribuinte], Período 2026

## Sumário Executivo
- Entidade declarante: [Singular / ENI / Sociedade por Quotas / SA / Unipessoal / Outro]
- NIF: [_____]
- NIPC (se aplicável): [_____]
- NISS (se aplicável): [_____]
- CAE principal: [_____]
- Regime fiscal IRS / IRC:
  - [Modelo 3: IRS Categoria B regime simplificado / contabilidade organizada]
  - [Modelo 22: IRC regime geral / regime simplificado (Anexo E) / taxa PME]
  - [RNH (regime transitório) / IFICI / regime geral]
- Regime de IVA: [Mensal / Trimestral / Isenção art. 53.º / Outro]
- Declarações a submeter:
  - [ ] Modelo 3 IRS: Portal das Finanças, de 1 abril a 30 junho 2027
  - [ ] Modelo 22 IRC: Portal das Finanças, até 31 maio 2027
  - [ ] IES: Portal das Finanças, até 15 julho 2027
  - [ ] Declaração periódica de IVA de dezembro 2026 (regime mensal): até 22 fevereiro 2027 (20 fevereiro é sábado); pagamento até 25 fevereiro 2027
  - [ ] Declaração periódica de IVA do 4.º trimestre 2026 (regime trimestral): até 22 fevereiro 2027 (20 fevereiro é sábado); pagamento até 25 fevereiro 2027
  - [ ] DMR de dezembro 2026: até 10 janeiro 2027
  - [ ] Modelo 10 (restantes rendimentos 2026): até final de fevereiro 2027
  - [ ] Modelo 39 (rendimentos sujeitos a retenção liberatória 2026): até final de fevereiro 2027
  - [ ] Declaração trimestral SS (outubro a dezembro 2026): até 31 janeiro 2027
  - [ ] Comunicação das faturas de dezembro 2026: até 5 janeiro 2027
  - [ ] Comunicação do inventário a 31 dezembro 2026 (se aplicável): até 31 janeiro 2027
- Total da coleta IRS / IRC: €X
- Total das retenções e pagamentos por conta: €X
- Saldo a pagar / reembolsar: €X / (€X)

## Apuramento de IRC (sociedades)
[De pt-corporate-tax]
- Resultado contabilístico antes de impostos
- Correções fiscais ao resultado
- Lucro tributável
- Prejuízos fiscais dedutíveis (CIRC art. 52.º: sem limite temporal; dedução anual até 65% do lucro tributável, 75% quando a parte acima resulta de prejuízos de 2020 e 2021)
- Matéria coletável
- Coleta IRC (19% para períodos iniciados em 2026; 15% sobre os primeiros €50.000 para PME e Small Mid Cap; 12,5% para startups que cumpram a Lei n.º 21/2023; CIRC art. 87.º e Lei n.º 64/2025, art. 3.º)
- Derrama municipal (até 1,5% conforme município)
- Derrama estadual (3% / 5% / 9% sobre as parcelas acima de €1,5M)
- Tributações autónomas
- Total a pagar

## Apuramento de IRS (singulares)
[De pt-income-tax, pt-irs-employees-investment, pt-nhr-ifici, pt-foreign-source-treaties]
- Rendimentos por categoria (A, B, E, F, G, H)
- Deduções específicas (Categoria A: 8,54 × IAS = €4.587,09, CIRS art. 25.º, n.º 1, al. a))
- Rendimento líquido
- Englobamento ou opção pelas taxas liberatórias e especiais (CIRS arts. 71.º, 72.º e 22.º)
- Tributação conjunta (se aplicável, CIRS art. 69.º)
- Coleta a taxas progressivas de 2026 (CIRS art. 68.º, redação da Lei n.º 73-A/2025)
- Deduções à coleta (CIRS art. 78.º e seguintes): dependentes, despesas gerais familiares, saúde, educação, habitação, lares
- Coleta líquida
- Adicional de solidariedade (acima de €80.000)
- IRS Jovem (CIRS art. 12.º-B), se optado
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
- Contribuições da entidade empregadora e dos trabalhadores (sociedades)
- Contribuições do sujeito passivo como trabalhador independente (singulares)
- Declarações trimestrais
- Membros de órgãos estatutários
- Entidades contratantes

## Folha de Pagamentos
[De portugal-payroll]
- Resumo anual de remunerações
- Retenções na fonte IRS Categoria A
- Contribuições para a Segurança Social
- DMR / folha salarial cross-check

## Contabilidade e Demonstrações Financeiras
[De portugal-bookkeeping, portugal-financial-statements]
- Balancete final pós-encerramento
- Balanço, DR, DACP, DFC, Anexo
- Mapas de depreciações e amortizações (Modelo 32)
- SAF-T (PT) da contabilidade (exportação, CIRC art. 123.º, n.º 8)

## Criptoativos
[De portugal-crypto-tax]
- Ganhos de criptoativos detidos menos de 365 dias: tributação autónoma de 28% ou englobamento (CIRS art. 72.º, n.º 1, al. c))
- Detenção igual ou superior a 365 dias: ganhos e perdas excluídos (CIRS art. 10.º, n.º 22)
- Mineração e outras operações empresariais: Categoria B (coeficientes 0,95 e 0,15 do art. 31.º)
- Criptoativos detidos por sociedades: tratamento contabilístico-fiscal

## Reconciliações Cross-Skill
- Volume de negócios contabilidade vs IVA vs Modelo 22/Modelo 3: [pass/fail]
- Retenções na fonte declaradas vs créditos reclamados: [pass/fail]
- DMR mensal vs folha salarial anual: [pass/fail]
- Contribuições SS vs registos SS: [pass/fail]
- Faturas comunicadas (e-fatura / SAF-T) vs contabilidade: [pass/fail]
- Tributações autónomas: taxas aplicadas: [pass/fail]
- Derramas (municipal + estadual): corretamente computadas: [pass/fail]
- Adicional de solidariedade: escalão correto: [pass/fail]

## Sinalizações para o Revisor
- Itens que requerem confirmação adicional pelo CC
- Despesas borderline (representação, donativos fora do EBF)
- Benefícios fiscais reclamados (RFAI, SIFIDE II, outros): documentação
- Operações com entidades relacionadas (CIRC art. 63.º, Preços de Transferência; ver pt-transfer-pricing)
- Operações com entidades em regime fiscal claramente mais favorável (CIRC art. 23.º-A e TA de 35% do art. 88.º, n.º 8)
- Prejuízos fiscais dedutíveis: limite de 65% (CIRC art. 52.º, n.º 2) e perda por alteração de titularidade de mais de 50% do capital (art. 52.º, n.os 8 e 9)
- Pagamento especial por conta: revogado desde 2022; confirmar com o revisor o tratamento de remanescentes antigos
- Limitação à dedutibilidade de gastos de financiamento (CIRC art. 67.º)
- Perdas por imparidade e provisões (CIRC art. 28.º e seguintes)
- Mais-valias e menos-valias fiscais com regimes específicos (reinvestimento, CIRC art. 48.º)
- Operações de fusão / cisão com regime de neutralidade (CIRC art. 73.º e seguintes)
- Pro-rata IVA: sujeito passivo misto
- Fatura simplificada vs fatura completa: limites
- e-fatura: desfasamento entre faturas comunicadas e contabilidade

## Posições Adotadas
[Lista com referências legais]
- e.g., "Coeficiente 0,75 do regime simplificado aplicado à atividade [____] da tabela do art. 151.º: CIRS art. 31.º, n.º 1, al. b)"
- e.g., "Taxa de IRC de 15% sobre os primeiros €50.000: a sociedade qualifica-se como PME (anexo ao Decreto-Lei n.º 372/2007); CIRC art. 87.º, n.º 2"
- e.g., "RFAI reclamado de €X: investimento elegível; limites em pt-corporate-tax (CFI art. 23.º)"
- e.g., "Pagamentos a [jurisdição] abrangidos pelo CIRC art. 23.º-A: prova de operação efetiva e normal anexa"
- e.g., "Crédito por dupla tributação internacional: Convenção PT-[país]; limitado nos termos do CIRS art. 81.º / CIRC art. 91.º"

## Notas de Planeamento para 2027
[Ver Secção 9]
```

## Secção 5: Resumo da Liquidação Fiscal (Bloco Headline)

Este bloco é o cabeçalho que o revisor e o contribuinte leem primeiro.

### 5.1 Bloco Headline: IRS (singulares)

```markdown
# IRS 2026: Liquidação Headline (€)

Rendimento bruto (todas as categorias):    X
Deduções específicas:                      (X)
Rendimento líquido:                        X
Quociente conjugal (se conjunta):          /2
Coleta a taxas progressivas:               X
Adicional de solidariedade (>€80.000):     X
Deduções à coleta (saúde, educação, etc.): (X)
Coleta líquida:                            X

Menos: Retenções na fonte:                 (X)
Menos: Pagamentos por conta:               (X)
Menos: Crédito dupla tributação:           (X)
= Imposto a pagar / (a reembolsar):        X / (X)

Submissão: Modelo 3 + Anexos aplicáveis
Prazo: 1 abril a 30 junho 2027
Portal: Portal das Finanças
Pagamento: referência indicada na nota de liquidação
```

### 5.2 Bloco Headline: IRC (sociedades)

```markdown
# IRC 2026: Liquidação Headline (€)

Volume de negócios:                        X
Resultado antes de impostos (RAI):         X
Correções fiscais:                         +X / -X
Lucro tributável:                          X
Prejuízos fiscais deduzidos (CIRC 52.º):   (X) [máx. 65% do LT; 75% com prejuízos de 2020/2021]
Matéria coletável:                         X

Coleta IRC:
  - 15% sobre primeiros €50.000 (PME):     X
  - 19% sobre excedente:                   X
  = Coleta (campo 351):                     X
Derrama estadual (parcelas 3/5/9%; c. 373): X
Derrama municipal (até 1,5%; c. 364):      X
Tributações autónomas (c. 365):            X
= Total:                                   X

Menos: Retenções na fonte suportadas (c. 359): (X)
Menos: Pagamentos por conta (c. 360):      (X)
Menos: Pagamentos adicionais por conta (c. 374): (X)
Menos: Crédito dupla tributação (c. 353):  (X)
Menos: Benefícios fiscais (RFAI/SIFIDE):   (X)
= Imposto a pagar / (a reembolsar):        X / (X)

Submissão: Modelo 22 + Anexos + IES
Prazo Modelo 22: 31 maio 2027
Prazo IES: 15 julho 2027
Portal: Portal das Finanças
Pagamento: até 31 maio 2027 (CIRC art. 104.º, n.º 1, al. b))
```

## Secção 6: Instruções de Pagamento, Portal das Finanças

Os pagamentos de IRS, IRC, IVA e outros tributos fazem-se com a referência para pagamento que a AT emite (no documento de cobrança, na nota de liquidação ou após a submissão da declaração de autoliquidação). O contribuinte paga:

- **Multibanco** (caixa automática ou home banking), usando a entidade, a referência e o montante indicados no documento de cobrança
- **Home banking**, na opção de pagamentos ao Estado
- **Outros canais** (débito direto, transferência) apenas conforme indicado no próprio documento de cobrança ou no Portal das Finanças. Não usar IBAN da AT copiado de documentos antigos: confirmar sempre no documento de cobrança do pagamento em causa.

### 6.1 Tipos de tributo e prazos de pagamento

**Tipos de tributo e prazos**

| Tributo | Autoridade | Portal | Prazo de pagamento |
| --- | --- | --- | --- |
| IRS (saldo da liquidação) | AT | Portal das Finanças | Na data-limite indicada na nota de liquidação |
| IRC (autoliquidação) | AT | Portal das Finanças | Até ao último dia do prazo do Modelo 22 (CIRC art. 104.º, n.º 1, al. b)): 31 maio 2027 para 2026 |
| IVA | AT | Portal das Finanças | Até dia 25 do 2.º mês seguinte ao mês ou trimestre (CIVA art. 27.º, n.º 1) |
| Pagamentos por conta IRC | AT | Portal das Finanças | Julho, setembro e 15 de dezembro (CIRC art. 104.º, n.º 1, al. a)) |
| Pagamentos por conta IRS (Categoria B) | AT | Portal das Finanças | Até dia 20 de julho, setembro e dezembro (CIRS art. 102.º, n.º 1) |
| Tributações autónomas | AT | Liquidadas com o Modelo 22 | Idem IRC |
| Derrama municipal e estadual | AT (cobra para municípios e Estado) | Liquidadas com o Modelo 22 | Idem IRC |
| Retenções na fonte de IRS (substitutos tributários) | AT | Guia de pagamento | Até ao dia 20 do mês seguinte àquele em que foram deduzidas (CIRS art. 98.º, n.º 3) |
| Contribuições SS da entidade empregadora e trabalhadores | Segurança Social | Segurança Social Direta | Entre o dia 1 e o dia 25 do mês seguinte (Código Contributivo art. 43.º) |
| Contribuições do trabalhador independente | Segurança Social | Segurança Social Direta | Entre o dia 10 e o dia 20 do mês seguinte (ISS, Guia Prático) |
| IMI (Imposto Municipal sobre Imóveis) | AT | Portal das Finanças | Uma prestação em maio (até €100); duas prestações em maio e novembro (mais de €100 até €500); três prestações em maio, agosto e novembro (mais de €500) (CIMI art. 120.º, n.º 1) |
| IUC (Imposto Único de Circulação) | AT | Portal das Finanças | Anual, por veículo (prazo a confirmar no Portal das Finanças) |

### 6.2 Fluxo Portal das Finanças: pagamento

1. Aceder ao Portal das Finanças com NIF e senha (ou Chave Móvel Digital / Cartão de Cidadão)
2. Submeter a declaração (Modelo 3, Modelo 22, declaração periódica de IVA)
3. A declaração considera-se apresentada na data da submissão, sob condição de correção de erros no prazo de 30 dias; findo esse prazo sem correção, fica sem efeito (Portaria n.º 104/2026/1, art. 3.º, n.os 2 e 3, para o Modelo 3)
4. No IRC e no IVA o imposto é autoliquidado e pago até ao prazo legal; no IRS a AT emite a nota de liquidação com o valor e a data-limite
5. Pagar com a referência indicada: Multibanco, home banking, ou outro canal indicado no documento
6. Após o pagamento, descarregar o comprovativo de pagamento no Portal das Finanças

### 6.3 Pagamentos por conta de IRC (CIRC arts. 104.º, 105.º e 107.º)

**Pagamentos por conta IRC**  _(CIRC art. 104.º, n.º 1, al. a), e art. 105.º)_

| PPC | Vencimento | Base de cálculo |
| --- | --- | --- |
| 1.ª prestação | **Julho** (7.º mês, se período diferente do ano civil) | 80% do imposto do período anterior (95% se o volume de negócios do período anterior for superior a €500.000), líquido das retenções, repartido por três montantes iguais arredondados por excesso para euros |
| 2.ª prestação | **Setembro** (9.º mês) | Idem |
| 3.ª prestação | **15 de dezembro** (dia 15 do 12.º mês) | Idem |

- **Dispensa**: não há pagamentos por conta quando o imposto do período de referência for inferior a €200 (CIRC art. 104.º, n.º 4).
- **Limitação do 3.º pagamento**: o sujeito passivo pode deixar de efetuar ou limitar o terceiro pagamento se os pagamentos já feitos cobrirem o imposto do período; se, por isso, deixar de ser paga importância superior a 20% da que seria entregue em condições normais, há juros compensatórios (CIRC art. 107.º).
- **Atraso**: se um pagamento por conta não for feito no prazo, "começam a correr imediatamente juros compensatórios" (CIRC art. 104.º, n.º 5).
- **Pagamentos adicionais por conta** (derrama estadual): nos mesmos prazos, se houve derrama estadual no período anterior (CIRC arts. 104.º-A e 105.º-A; taxas em pt-corporate-tax).

### 6.4 Pagamentos por conta de IRS (CIRS art. 102.º)

**Pagamentos por conta IRS**  _(CIRS art. 102.º)_

| PPC | Prazo | Base de cálculo |
| --- | --- | --- |
| 1.ª prestação | Até **20 julho** | Total = 65% do montante da fórmula do art. 102.º, n.º 2, que usa a coleta, as retenções e os rendimentos da Categoria B do **penúltimo ano**; cada prestação é um terço, arredondado por excesso para euros |
| 2.ª prestação | Até **20 setembro** | Idem |
| 3.ª prestação | Até **20 dezembro** | Idem |

- Só os titulares de rendimentos da Categoria B estão obrigados (art. 102.º, n.º 1). Os pagamentos de 2026 resultam da liquidação de 2024; os de 2027 resultam da liquidação de 2025.
- Cessam quando as retenções e os pagamentos já feitos igualarem ou excederem o imposto do ano, ou quando deixam de ser auferidos rendimentos da Categoria B (art. 102.º, n.º 4). Podem ser reduzidos (n.º 5); se a redução deixar por pagar mais de 20% do normal, há juros compensatórios (n.º 6).

### 6.5 Comprovativos de pagamento a conservar

**Comprovativos a conservar**

| Documento | Emitido por | Conservar por |
| --- | --- | --- |
| Comprovativo de submissão (Modelo 3 / 22 / IES / IVA) | Portal das Finanças | Durante o prazo de conservação de registos (10 anos civis subsequentes, CIVA art. 52.º, n.º 1) |
| Nota de liquidação | AT | Idem |
| Comprovativo de pagamento (talão Multibanco ou home banking) | Banco | Pelo menos durante o prazo de caducidade (4 anos, LGT art. 45.º, n.º 1), e durante o prazo de conservação se for documento de suporte contabilístico |
| Comprovativo de pagamento no Portal das Finanças | AT | Idem |
| Certidões de situação tributária e contributiva regularizada (AT e SS) | AT / SS | Renovar conforme a validade indicada na própria certidão |

## Secção 7: Instruções de Submissão

### 7.1 Submissões no Portal das Finanças

**Canais de submissão**

| Canal | Descrição | Adequado para |
| --- | --- | --- |
| **Portal das Finanças: preenchimento direto** | Formulário online no Portal | Contribuintes singulares; PME simples |
| **Portal das Finanças: envio de ficheiro** | Upload de ficheiros gerados por software de contabilidade | CC profissionais; sociedades com volume |
| **Software certificado de faturação / contabilidade** | Comunicação de faturas em tempo real ou por ficheiro SAF-T (PT) (DL 198/2012, art. 3.º, n.º 1) | Sociedades com ERP; grandes contribuintes |

### 7.2 Submissão do Modelo 3 (IRS)

1. Aceder ao Portal das Finanças com NIF + senha (ou Chave Móvel Digital / Cartão de Cidadão)
2. Menu de IRS: "Entregar Declaração" (Modelo 3)
3. Selecionar ano dos rendimentos 2026
4. Se disponível, o sistema apresenta uma declaração pré-preenchida com dados já comunicados à AT (rendimentos do trabalho, retenções, despesas dedutíveis com base nas faturas comunicadas até ao final de fevereiro de 2027, CIRS art. 78.º-B, n.º 5)
5. Validar e corrigir os anexos pré-preenchidos; acrescentar os anexos aplicáveis (Portaria n.º 104/2026/1):
   - Anexo A (rendimentos do trabalho dependente e pensões)
   - Anexo B (rendimentos empresariais e profissionais: regime simplificado ou atos isolados)
   - Anexo C (rendimentos empresariais e profissionais: contabilidade organizada)
   - Anexo D (imputação de rendimentos)
   - Anexo E (rendimentos de capitais)
   - Anexo F (rendimentos prediais)
   - Anexo G (mais-valias e outros incrementos patrimoniais)
   - Anexo G1 (mais-valias não tributadas)
   - Anexo H (benefícios fiscais e deduções)
   - Anexo I (rendimentos de herança indivisa)
   - Anexo J (rendimentos obtidos no estrangeiro)
   - Anexo L (residentes não habituais / IFICI)
   - Anexo SS (Segurança Social, trabalhadores independentes)
6. Validar: o Portal executa verificações lógicas e aritméticas; resolver erros e analisar avisos
7. Submeter: o sistema emite comprovativo de entrega. A declaração considera-se apresentada na data da submissão, sob condição de correção de erros em 30 dias (Portaria n.º 104/2026/1, art. 3.º, n.º 2)
8. Aguardar nota de liquidação

**Rendimentos de fonte estrangeira com crédito de imposto ainda não determinado no Estado da fonte:** o prazo do n.º 1 é prorrogado até 31 de dezembro desse ano, desde que o contribuinte comunique à AT, dentro do prazo normal, que cumpre as condições (CIRS art. 60.º, n.os 3 e 4).

**Contabilista Certificado:** quando a Categoria B é tributada com base em contabilidade organizada (Anexo C), a declaração é assinada pelo CC, identificado por senha atribuída pela AT (Portaria n.º 104/2026/1, art. 2.º, n.º 2; Estatuto da OCC, art. 10.º, n.º 1, al. b)).

**Atenção:** declarar o IBAN de que o contribuinte é titular no Portal das Finanças, para o reembolso ser pago por transferência.

### 7.3 Submissão do Modelo 22 (IRC)

As sociedades comerciais e as demais entidades do CIRC art. 123.º, n.º 1, são obrigadas a dispor de contabilidade organizada. As declarações fiscais que assentam nessa contabilidade são assinadas pelo Contabilista Certificado (Estatuto da OCC, art. 10.º, n.º 1, al. b)), que submete com a sua senha.

1. CC acede ao Portal das Finanças com as suas credenciais
2. Menu de IRC: "Entregar Declaração" (Modelo 22), no impresso aprovado para a campanha de 2027 (ver Secção 2.2: o impresso do Despacho n.º 320/2026 ainda traz as taxas dos períodos de 2025)
3. Selecionar período de tributação 2026
4. Preencher os quadros do rosto do Modelo 22: identificação do sujeito passivo e do CC, tipo de declaração, período de tributação, regime de tributação, apuramento do lucro tributável (correções ao resultado contabilístico), apuramento da matéria coletável, cálculo do imposto, tributações autónomas, retenções e pagamentos por conta, outras informações
5. Juntar os anexos aplicáveis (Despacho n.º 320/2026):
   - Anexo A (derrama municipal): quando a sociedade tem estabelecimentos em mais de um município e matéria coletável superior a €50.000 (repartição pela massa salarial; ver pt-corporate-tax)
   - Anexo C (Regiões Autónomas)
   - Anexo D (benefícios fiscais: RFAI, SIFIDE II e outros)
   - Anexo E (regime simplificado de IRC)
   - Anexo F (organismos de investimento coletivo)
   - Anexo G (regime especial do transporte marítimo)
   - Anexo AIMI (prédios afetos a uso pessoal dos sócios e gerentes, para efeitos do adicional ao IMI)
6. Validar e submeter: o Portal emite comprovativo
7. Pagar o imposto autoliquidado até 31 maio 2027 (CIRC art. 104.º, n.º 1, al. b)); o reembolso, quando a declaração é enviada no prazo e sem erros, é feito até ao fim do 3.º mês seguinte ao envio (art. 104.º, n.º 3)

**Grupos (RETGS):** a sociedade dominante envia a declaração do grupo e cada sociedade do grupo envia a sua (CIRC art. 120.º, n.º 6).

**Cessação de atividade:** a declaração do período da cessação é enviada até ao último dia do 3.º mês seguinte (CIRC art. 120.º, n.º 3).

### 7.4 Submissão da IES (Informação Empresarial Simplificada)

A IES é a declaração anual de informação contabilística e fiscal do CIRC art. 117.º, n.º 1, al. c), "enviada nos termos e com os anexos que para o efeito sejam mencionados no respectivo modelo" (art. 121.º, n.º 1). Submetida pelo CC.

1. CC acede ao Portal das Finanças
2. Menu: "IES / Declaração Anual"
3. Preencher o rosto e os anexos aplicáveis do modelo da IES em vigor (informação contabilística SNC, NCM ou NCM-ME; informação de IVA; operações com entidades relacionadas, CIRC art. 63.º; outros consoante a atividade)
4. Validar e submeter até **15 julho 2027** (CIRC art. 121.º, n.º 2): o Portal emite comprovativo
5. O dossier de preços de transferência, quando exigido, é constituído até ao mesmo prazo (ver `pt-transfer-pricing`; isenção para rendimentos totais inferiores a €10.000.000, Portaria n.º 268/2021)

### 7.5 Submissão da Declaração Periódica de IVA

1. CC ou sujeito passivo acede ao Portal das Finanças
2. Menu de IVA: "Declaração Periódica"
3. Selecionar período (mês ou trimestre)
4. Preencher os quadros da declaração e, se houver regularizações, os anexos dos campos 40 e 41; no Quadro 06 apura-se o imposto a entregar ao Estado (campo 93) ou o crédito a recuperar (campos 94, 95 e 96) (AT, Ofício-Circulado n.º 25119/2026). Os restantes números de campo estão em `portugal-vat-return`. A Portaria n.º 298/2026/1 aprovou um novo modelo que só se aplica às declarações de períodos iniciados a partir de 1 de julho de 2027; desde 1 de julho de 2026 já vale a quadrícula «Regime Grupos IVA» no Quadro 01 para as entidades de um grupo de IVA (Lei n.º 62/2025), cujo apuramento global é feito na declaração do grupo (mesmo ofício-circulado)
5. Submeter até dia 20 do 2.º mês seguinte (CIVA art. 41.º, n.º 1) e pagar até dia 25 do 2.º mês seguinte (CIVA art. 27.º, n.º 1). A declaração de junho e do 2.º trimestre segue o calendário especial descrito em `portugal-vat-return`
6. A declaração é devida mesmo em período sem operações tributáveis (ver `portugal-vat-return`)

### 7.6 Comunicação de faturas e SAF-T (PT)

**Comunicação de faturas e SAF-T**

| Obrigação | Como | Prazo |
| --- | --- | --- |
| **Comunicação de faturas à AT** | Em tempo real, por ficheiro SAF-T (PT), ou por inserção direta no Portal das Finanças (DL 198/2012, art. 3.º, n.º 1) | Até **dia 5** do mês seguinte ao da emissão (art. 3.º, n.º 2) |
| **Comunicação do inventário** (entidades com contabilidade organizada obrigadas a inventário) | Ficheiro por transmissão eletrónica | Até **31 de janeiro**, inventário a 31 de dezembro do ano anterior (DL 198/2012, art. 3.º-A, n.º 1) |
| **SAF-T (PT) da contabilidade** | Capacidade de exportação obrigatória (CIRC art. 123.º, n.º 8) | A pedido da AT, nomeadamente em inspeção |
| **SAF-T Auditoria fiscal** | Sob solicitação da AT em inspeções | Prazo fixado na notificação |

### 7.7 Submissões na Segurança Social Direta

**Submissões Segurança Social Direta**

| Declaração | Prazo |
| --- | --- |
| **Declaração de remunerações** (entidade empregadora) | Confirmação ou correção dos valores apurados pelo sistema até ao dia 20 do mês seguinte; o silêncio vale como aceitação (Código Contributivo art. 40.º, n.º 8) |
| **Declaração trimestral** dos trabalhadores independentes | Até ao **último dia de janeiro, abril, julho e outubro**, relativa aos três meses anteriores (ISS, Guia Prático) |
| **Anexo SS ao Modelo 3** (independentes em contabilidade organizada e declaração anual) | Com o Modelo 3, enviado à Segurança Social pela AT (ISS, Guia Prático) |
| **Início / fim de atividade** de empresários em nome individual e titulares de EIRL só com atividade industrial ou comercial | Online, "no mês em que a alteração acontecer" (ISS, Guia Prático) |

### 7.8 Resumo de prazos (período 2026)

**Resumo de prazos**

| Tipo de declarante | Declaração | Autoridade | Prazo |
| --- | --- | --- | --- |
| Singular (residente) | Modelo 3 IRS + Anexos | AT | **1 abril a 30 junho 2027** (CIRS art. 60.º, n.º 1) |
| Sociedade (período = ano civil) | Modelo 22 IRC + Anexos, e pagamento | AT | **31 maio 2027** (CIRC art. 120.º, n.º 1; art. 104.º, n.º 1, al. b)) |
| Sociedade | IES | AT | **15 julho 2027** (CIRC art. 121.º, n.º 2) |
| Sujeito passivo IVA mensal | Declaração periódica de dezembro 2026 | AT | **22 fevereiro 2027** (20 fevereiro é sábado; regra em `portugal-vat-return`); pagamento até **25 fevereiro 2027** |
| Sujeito passivo IVA trimestral | Declaração periódica do 4.º trimestre 2026 | AT | **22 fevereiro 2027** (20 fevereiro é sábado); pagamento até **25 fevereiro 2027** |
| Empregador | DMR de dezembro 2026 | AT | **10 janeiro 2027** (CIRS art. 119.º, n.º 1, al. c), i)) |
| Entidade devedora de rendimentos | Documento comprovativo dos rendimentos e retenções de 2026 ao titular | Contribuinte | **20 janeiro 2027** (CIRS art. 119.º, n.º 1, al. b)) |
| Substituto tributário | Modelo 10 (restantes rendimentos de 2026) | AT | **Final de fevereiro 2027** (CIRS art. 119.º, n.º 1, al. c), ii)) |
| Entidade que paga rendimentos sujeitos a retenção liberatória | Modelo 39 (rendimentos de 2026) | AT | **Final de fevereiro 2027** (CIRS art. 119.º, n.º 12, al. b)) |
| Entidade que paga rendimentos com isenção, dispensa ou redução de taxa (art. 71.º) | Declaração própria | AT | **Final de julho 2027** (CIRS art. 119.º, n.º 2, al. a)) |
| Entidade que paga rendimentos a não residentes | Modelo 30 | AT | **Até ao fim do 2.º mês seguinte** ao pagamento (CIRS art. 119.º, n.º 7, al. a)) |
| Trabalhador independente | Declaração trimestral SS (outubro a dezembro 2026) | SS | **31 janeiro 2027** |
| Todos os emitentes de faturas | Comunicação das faturas de dezembro 2026 | AT (e-fatura) | **5 janeiro 2027** |
| Entidades com inventário | Comunicação do inventário a 31 dezembro 2026 | AT | **31 janeiro 2027** |
| Grupos multinacionais com rendimentos consolidados de €750.000.000 ou mais no período anterior | Declaração financeira e fiscal por país (CIRC art. 117.º, n.º 1, al. d), e art. 121.º-A, n.º 1) | AT | **12 meses** após o fim do período de relato (art. 121.º-A, n.º 3); cada entidade do grupo comunica quem declara até ao prazo do Modelo 22 (art. 121.º-A, n.º 4) |

### 7.9 Coimas por atraso

**Coimas por atraso**

| Infração | Coima | Base legal |
| --- | --- | --- |
| Falta ou atraso na entrega de declaração que permita à AT determinar a matéria coletável (Modelo 3, Modelo 22, IVA, IES) | €150 a €3.750 | RGIT art. 116.º, n.º 1 |
| Falta ou atraso na apresentação de declarações, documentos, comunicações (DMR, Modelo 10, comunicação de faturas, SAF-T) | €150 a €3.750 | RGIT art. 117.º, n.º 1 |
| Falta ou atraso nas declarações de início, alteração ou cessação de atividade | €300 a €7.500 | RGIT art. 117.º, n.º 2 |
| Pessoas coletivas | Limites mínimo e máximo elevados para o dobro; máximo de €165.000 em caso de dolo | RGIT art. 26.º, n.os 1 e 4 |
| Falta de entrega da prestação tributária (imposto, retenções, pagamentos por conta): negligência | 15% a metade do imposto em falta | RGIT art. 114.º, n.º 2 |
| Falta de entrega da prestação tributária: dolo, sem crime | Valor da prestação em falta até ao dobro | RGIT art. 114.º, n.º 1 |
| Juros compensatórios: liquidação retardada por facto do sujeito passivo, declaração fora de prazo | Contam-se dia a dia | LGT art. 35.º, n.os 1, 3 e 6 |
| Juros de mora: imposto não pago no prazo legal | 7,221% ao ano desde 1 de janeiro de 2026, a taxa das dívidas ao Estado | LGT art. 44.º, n.º 3; Aviso n.º 18/2026/2 (IGCP) |

- **Dispensa de coima**: não é aplicada coima quando, nos cinco anos anteriores, o agente não foi condenado nem beneficiou de dispensa ou redução, a infração não causou prejuízo efetivo à receita e a falta está regularizada; a falta de entrega de imposto conta sempre como prejuízo (RGIT art. 29.º, n.os 1 a 3).

### 7.10 Substituição de declaração

- **IRC**: quando tenha sido liquidado imposto inferior ao devido ou declarado prejuízo superior ao efetivo, a declaração de substituição pode ser apresentada "ainda que fora do prazo", pagando o imposto em falta (CIRC art. 122.º, n.º 1). Quando a autoliquidação resultou em imposto superior ao devido, a substituição faz-se no prazo de um ano a contar do termo do prazo legal (art. 122.º, n.º 2). O pagamento da diferença é feito até ao dia do envio da declaração de substituição (art. 104.º, n.º 1, al. c)).
- **IRS**: a declaração é ainda apresentada nos 30 dias imediatos a qualquer facto que altere os rendimentos já declarados (CIRS art. 60.º, n.º 2). Uma declaração submetida com erros pode ser corrigida no prazo de 30 dias (Portaria n.º 104/2026/1, art. 3.º, n.º 2).
- **Coimas**: regularização espontânea pode beneficiar da dispensa do RGIT art. 29.º, se reunidos os requisitos; em consequência de inspeção não há essa atenuação, e pode haver crime fiscal se houver ocultação.

## Secção 8: Lista Final de Ações do Contribuinte (Calendar)

```markdown
# Lista de Ações: [Nome do contribuinte], Período 2026

Nota: datas legais. Os prazos de IVA e outros que terminem em dia não útil seguem a regra descrita em portugal-vat-return. O Modelo 3, o Modelo 22 e a IES não transitam ("independentemente de esse dia ser útil").

## Janeiro 2027

| Data | Ação | Responsável |
|---|---|---|
| 5 jan | Comunicação das faturas de dezembro 2026 (e-fatura / SAF-T) | CC / software |
| 10 jan | DMR de dezembro 2026 | CC / empregador |
| 10 a 20 jan | Contribuições SS de dezembro 2026 do trabalhador independente | Singular |
| 20 jan | Entrega das retenções na fonte de IRS de dezembro 2026 | Sociedade / substituto tributário |
| 20 jan | Documento comprovativo dos rendimentos e retenções de 2026 aos titulares | Entidade devedora |
| 20 jan | Confirmação da declaração de remunerações SS de dezembro 2026 | Sociedade |
| 1 a 25 jan | Pagamento das contribuições SS de dezembro 2026 (entidade empregadora e trabalhadores) | Sociedade |
| 31 jan | Declaração trimestral SS (outubro a dezembro 2026) | Trabalhador independente |
| 31 jan | Comunicação do inventário a 31 dezembro 2026 | Sociedade com inventário |

## Fevereiro 2027

| Data | Ação | Responsável |
|---|---|---|
| 5 fev | Comunicação das faturas de janeiro 2027 | CC / software |
| 10 fev | DMR de janeiro 2027 | CC / empregador |
| 20 fev (22 fev) | **Declaração periódica de IVA de dezembro 2026 (mensal) e do 4.º trimestre 2026 (trimestral)** | CC |
| 25 fev | **Pagamento do IVA de dezembro 2026 / 4.º trimestre 2026** | CC / sujeito passivo |
| final fev | **Modelo 10: restantes rendimentos de 2026** | Substituto tributário |
| final fev | **Modelo 39: rendimentos de 2026 sujeitos a retenção liberatória** | Entidade pagadora |
| final fev | Faturas de 2026 comunicadas contam para as deduções à coleta; Categoria B indica no Portal as faturas afetas à atividade (CIRS art. 78.º-B, n.º 5; art. 31.º, n.º 15, al. a)) | Singular |

## Março 2027

| Data | Ação | Responsável |
|---|---|---|
| 5 mar | Comunicação das faturas de fevereiro 2027 | CC / software |
| 10 mar | DMR de fevereiro 2027 | CC / empregador |
| 15 mar | AT disponibiliza o montante das deduções à coleta de 2026 (CIRS art. 78.º-B, n.º 6) | AT |
| 20 mar | Declaração periódica de IVA de janeiro 2027 (mensal) | CC |
| 31 mar | Prazo para reclamar das deduções à coleta apuradas (CIRS art. 78.º-B, n.º 7) | Singular |

## Abril 2027

| Data | Ação | Responsável |
|---|---|---|
| 1 abr | Início da entrega do Modelo 3 dos rendimentos de 2026 | Singular |
| 30 abr | Declaração trimestral SS (janeiro a março 2027) | Trabalhador independente |

## Maio 2027

| Data | Ação | Responsável |
|---|---|---|
| maio | IMI: prestação única (até €100) ou 1.ª prestação | Proprietário |
| **31 mai** | **MODELO 22 IRC + Anexos: envio e pagamento** | CC |

## Junho 2027

| Data | Ação | Responsável |
|---|---|---|
| **30 jun** | **MODELO 3 IRS + Anexos: último dia de entrega** | Singular (CC se contabilidade organizada) |

## Julho 2027

| Data | Ação | Responsável |
|---|---|---|
| **15 jul** | **IES: declaração anual de informação contabilística e fiscal; dossier de preços de transferência constituído (se exigido)** | CC |
| 20 jul | 1.º pagamento por conta de IRS de 2027 (Categoria B) | Singular |
| julho | 1.º pagamento por conta de IRC de 2027 (e adicional, se aplicável) | Sociedade |
| 31 jul | Declaração trimestral SS (abril a junho 2027) | Trabalhador independente |

## Agosto 2027

| Data | Ação | Responsável |
|---|---|---|
| agosto | IMI: 2.ª prestação (só quando o imposto é superior a €500) | Proprietário |

## Setembro 2027

| Data | Ação | Responsável |
|---|---|---|
| 20 set | 2.º pagamento por conta de IRS de 2027 | Singular |
| setembro | 2.º pagamento por conta de IRC de 2027 | Sociedade |

## Novembro 2027

| Data | Ação | Responsável |
|---|---|---|
| novembro | IMI: última prestação (imposto superior a €100) | Proprietário |

## Dezembro 2027

| Data | Ação | Responsável |
|---|---|---|
| 15 dez | 3.º pagamento por conta de IRC de 2027 | Sociedade |
| 20 dez | 3.º pagamento por conta de IRS de 2027 | Singular |

## Obrigações contínuas durante 2027

| Item | Autoridade | Periodicidade |
|---|---|---|
| Comunicação de faturas | AT (e-fatura) | Mensal (dia 5) |
| DMR | AT | Mensal (dia 10) |
| Entrega de retenções na fonte | AT | Mensal (dia 20) |
| Contribuições SS (empregador e trabalhadores) | SS | Mensal (declaração confirmada até dia 20; pagamento entre dia 1 e dia 25) |
| Contribuições SS do independente | SS | Mensal (dia 10 a dia 20) |
| Declaração periódica de IVA | AT | Mensal ou trimestral (dia 20 do 2.º mês seguinte; pagamento dia 25) |
| Modelo 30 (rendimentos de não residentes) | AT | Até ao fim do 2.º mês seguinte ao pagamento |
| Comunicação de inventários | AT | Anual (31 janeiro) |
| IMI | AT | Maio; maio e novembro; ou maio, agosto e novembro |
| IUC (por veículo) | AT | Anual |

## Conservação de documentos

Os sujeitos passivos são obrigados a arquivar e conservar "durante os 10 anos civis subsequentes todos os registos e respetivos documentos de suporte" (CIVA art. 52.º, n.º 1). Para efeitos de liquidação, o direito da AT caduca em 4 anos, quando a lei não fixar outro prazo (LGT art. 45.º, n.º 1); quando houve dedução ou crédito de imposto, o prazo é o do exercício desse direito (art. 45.º, n.º 3). Os prejuízos fiscais de IRC não têm limite temporal de dedução (CIRC art. 52.º, n.º 1), pelo que a prova da sua origem deve ser conservada enquanto forem deduzidos.

Conservar pelo menos:
- Demonstrações financeiras + Anexo (sociedades)
- Balancetes mensais e final
- Diários e razão (geral + auxiliares)
- Faturas emitidas e recebidas + documentos de transporte
- Ficheiros SAF-T (PT)
- Comunicação de inventários
- Comprovativos de submissão (Modelo 3, 22, IVA, IES, DMR, declarações trimestrais SS)
- Notas de liquidação e comprovativos de pagamento
- Comprovativos de pagamentos por conta
- Certidões de situação regularizada (AT e SS)
- Mapas de depreciações e amortizações
- Contratos relevantes (laborais, locação financeira, mútuos, prestação de serviços com entidades relacionadas)
- Atas de assembleias-gerais e órgãos de administração (sociedades)
```

## Secção 2: Entradas Obrigatórias dos Skills Upstream

0. **Invocar pt-income-tax**: consumir output da Categoria B para Modelo 3 (Anexo B / C), retenções, pagamentos por conta, IRS Jovem
0. **Invocar pt-irs-employees-investment**: consumir Categorias A, H, E, F, G e deduções à coleta (Anexos A, E, F, G, G1, H)
0. **Invocar pt-nhr-ifici**: consumir output RNH/IFICI para Anexo L
0. **Invocar pt-foreign-source-treaties**: consumir crédito de dupla tributação para Anexo J
0. **Invocar pt-corporate-tax**: consumir lucro tributável, derramas, tributações autónomas para Modelo 22
0. **Invocar portugal-vat-return**: consumir posição anual de IVA para reconciliação
0. **Invocar pt-social-contributions**: consumir contribuições de empregador, trabalhadores e independentes
0. **Invocar portugal-payroll**: consumir custos com pessoal, retenções Categoria A, DMR
0. **Invocar portugal-bookkeeping**: consumir balancete, demonstração de resultados, mapas de depreciação
0. **Invocar portugal-financial-statements**: consumir demonstrações financeiras SNC/NCM para IES
0. **Invocar portugal-crypto-tax**: consumir ganhos e rendimentos de criptoativos
0. **Invocar pt-transfer-pricing** (sociedades com entidades relacionadas): consumir ajustamentos e o estado do dossier

## Secção 3: Workflow de Montagem, Reconciliações Cross-Skill

0. **Executar verificações cruzadas 1-9**: reconciliar volume de negócios, créditos e retenções, DMR vs declarações anuais, contribuições SS, IVA e pro-rata, tributações autónomas, derramas, adicional de solidariedade, e aplicar disciplina de tolerância

## Secção 4: Estrutura do Working Paper para o Contabilista Certificado (OCC)

0. **Montar working paper**: consolidar todos os outputs upstream no template markdown do working paper para o CC

## Secção 5: Resumo da Liquidação Fiscal (Bloco Headline)

0. **Gerar bloco headline**: produzir bloco headline IRS e/ou IRC conforme aplicável

## Secção 6: Instruções de Pagamento, Portal das Finanças

0. **Gerar instruções de pagamento**: produzir instruções de pagamento com a referência do Portal das Finanças

## Secção 7: Instruções de Submissão

0. **Gerar instruções de submissão**: produzir instruções de submissão para Portal das Finanças, e-fatura / SAF-T e Segurança Social Direta

## Secção 8: Lista Final de Ações do Contribuinte (Calendar)

0. **Gerar lista final de ações**: produzir calendário de ações mensal do contribuinte para 2027

## Secção 9: Notas para o Exercício de 2027 (Planeamento)

A capstone produz uma secção prospetiva para que o contribuinte chegue à próxima campanha consciente das alterações já legisladas e das que estão por legislar.

### 9.1 O que mudou em 2026 e o que já está legislado para 2027

**Alterações em vigor no período de 2026 e já legisladas para 2027**  _(Lei n.º 64/2025; Lei n.º 73-A/2025; CIRS e CIRC)_

| Área | 2026 (este pacote) | 2027 e seguintes | Ação |
| --- | --- | --- | --- |
| Taxa geral IRC (CIRC art. 87.º, n.º 1) | 19% para períodos iniciados em 2026 (Lei n.º 64/2025, art. 3.º, n.º 2) | 18% para períodos iniciados em 2027 (art. 3.º, n.º 3); 17% a partir de 2028 (art. 87.º, n.º 1) | Recalcular pagamentos por conta e impostos diferidos |
| Taxa IRC PME / Small Mid Cap (primeiros €50.000) | 15% (CIRC art. 87.º, n.º 2; Lei n.º 64/2025, art. 3.º, n.º 4) | 15% enquanto a lei não mudar | Confirmar qualificação PME (anexo ao DL 372/2007) |
| Adicional de solidariedade IRS | 2,5% de €80.000 a €250.000; 5% acima (CIRS art. 68.º-A) | Sem alteração legislada conhecida | Nenhuma |
| Escalões IRS | Tabela de 2026 (CIRS art. 68.º, redação da Lei n.º 73-A/2025; primeiro escalão até €8.342) | A tabela de 2027 depende do Orçamento do Estado para 2027 | Reforecast quando a lei for publicada |
| Dedução específica Categoria A | 8,54 × IAS = €4.587,09 (CIRS art. 25.º, n.º 1, al. a)) | Acompanha o IAS de 2027 | Atualizar payroll |
| IAS (Indexante dos Apoios Sociais) | €537,13 em 2026 | IAS de 2027 por portaria | Atualizar contribuições e limiares |
| Tributação autónoma: viaturas | 8% / 25% / 32% com limiares €37.500 e €45.000 (CIRC art. 88.º, n.º 3) | Sem alteração legislada conhecida | Verificar o Orçamento do Estado para 2027 |
| Benefícios fiscais: RFAI / SIFIDE II | Em vigor (detalhe em pt-corporate-tax) | Monitorizar prorrogações e revisões | Monitorizar |

### 9.2 Regime RNH (transitório) e IFICI

O regime de Residente Não Habitual (RNH) foi revogado pela Lei n.º 82/2023 (Orçamento do Estado para 2024), com regime transitório para quem já estava inscrito ou reunia as condições de transição. A duração e as condições exatas do regime transitório estão em `pt-nhr-ifici`. Não há novas adesões ao RNH.

Em substituição, existe o **IFICI** (EBF art. 58.º-A), aplicável a atividades qualificadas como de investigação científica e inovação e outras atividades certificadas (ver `pt-nhr-ifici`). A tributação dos rendimentos dos beneficiários está em `pt-nhr-ifici`; na retenção na fonte, os rendimentos da Categoria B dos sujeitos passivos abrangidos pelo EBF art. 58.º-A são retidos a 20% (CIRS art. 101.º, n.º 1, al. d)). Quem beneficiou de RNH ou IFICI não pode usar o IRS Jovem (CIRS art. 12.º-B, n.º 9).

**Para 2027:** confirmar inscrição e elegibilidade IFICI dos contribuintes singulares; reportar no Anexo L do Modelo 3.

### 9.3 Pilar Dois (imposto mínimo global): grupos multinacionais

Portugal transpôs a Diretiva (UE) 2022/2523 (imposto mínimo global). Aplica-se a grupos multinacionais e grupos nacionais de grande dimensão, com uma taxa efetiva mínima por jurisdição e as regras IIR, UTPR e imposto complementar nacional.

**Para 2027:** se o cliente fizer parte de grupo abrangido, exige análise específica e potencial declaração GloBE. **A skill `pt-corporate-tax` deve cobrir os detalhes; a montagem apenas sinaliza.** Os limiares, a taxa mínima e o diploma de transposição estão na linha "Not yet confirmed" das fontes.

### 9.4 Cripto: regime em vigor

O regime em vigor (CIRS art. 10.º, n.º 1, al. k); numeração do n.º 22 dada pelo DL 97/2026):
- Ganhos com criptoativos detidos menos de 365 dias: Categoria G, taxa autónoma de 28% (CIRS art. 72.º, n.º 1, al. c)) ou englobamento
- Detenção igual ou superior a 365 dias: ganhos e perdas excluídos (art. 10.º, n.º 22), com as exceções do próprio artigo (ver `portugal-crypto-tax`)
- Mineração: Categoria B, coeficiente 0,95 (CIRS art. 31.º, n.º 1, al. d)); outras operações com criptoativos na Categoria B: coeficiente 0,15 (al. a))

**Para 2027:** monitorizar a aplicação do **Regulamento MiCA (UE)** e da troca automática de informação sobre criptoativos (DAC8), que alimentará a informação disponível à AT. Detalhe e datas em `portugal-crypto-tax`.

### 9.5 SAF-T da contabilidade: entrega à AT

Está prevista a entrega do ficheiro SAF-T (PT) da contabilidade à AT, sucessivamente adiada. A obrigação atual em vigor é a de dispor de capacidade de exportação do ficheiro (CIRC art. 123.º, n.º 8). **Monitorizar** o diploma que fixe a data de entrada em vigor da entrega.

### 9.6 Pagamentos por conta para 2027

Calcular os pagamentos por conta de 2027 com base nas regras da Secção 6:
- PPC IRC: 80% (ou 95% se o volume de negócios de 2026 for superior a €500.000) do imposto de 2026, líquido de retenções, em três prestações (julho / setembro / 15 de dezembro de 2027); dispensa abaixo de €200
- PPC IRS Categoria B: 65% da fórmula do art. 102.º, n.º 2, com base no penúltimo ano (2025), até 20 julho, 20 setembro e 20 dezembro de 2027

### 9.7 Preços de transferência (CIRC art. 63.º + Portaria n.º 268/2021)

Para sociedades com operações com entidades relacionadas:
- **Dossier de preços de transferência**: dispensado para sujeitos passivos com rendimentos totais no período inferiores a €10.000.000 (Portaria n.º 268/2021); acima disso, dispensa para operações de valor não superior a €100.000 por contraparte e €500.000 no total. Detalhe em `pt-transfer-pricing`
- **Dossier principal e dossier específico** para entidades de grupos multinacionais
- **IES**: informação sobre operações com entidades relacionadas (CIRC art. 63.º)

### 9.8 Continuidade no e-fatura e SAF-T

Confirmar que a contabilidade e a faturação estão a alimentar o e-fatura:
- Faturas emitidas comunicadas em tempo real, por SAF-T ou no Portal, até dia 5 do mês seguinte (DL 198/2012, art. 3.º, n.º 2)
- Faturas recebidas com NIF do adquirente comunicadas até ao final de fevereiro do ano seguinte contam para as deduções à coleta do Modelo 3 (CIRS art. 78.º-B, n.º 5)
- Para Categoria B: faturas-recibo emitidas no Portal das Finanças ou por software certificado; indicar até ao final de fevereiro as faturas afetas à atividade (CIRS art. 31.º, n.º 15)

## Secção 10: Bloco de Atestação do Revisor (OCC Sign-off)

O working paper final inclui um bloco de atestação que o **Contabilista Certificado** assina antes de qualquer submissão.

```markdown
# Atestação do Revisor: Período 2026

Eu, [Nome], Contabilista Certificado inscrito na Ordem dos Contabilistas
Certificados (OCC) com o n.º [____], a atuar em representação de
[Nome do contribuinte, NIF ________], declaro que revi o working paper
preparado por [preparador / OpenAccountants AI], verifiquei as
reconciliações cross-skill com o cuidado profissional exigido pelo Estatuto
da OCC e pelo Código Deontológico, e confirmo que:

  [ ] As demonstrações financeiras (sociedades) ou os elementos da
       contabilidade da Categoria B (singulares com contabilidade organizada)
       em que se baseia esta declaração estão devidamente encerrados, e o
       ficheiro SAF-T (PT) da contabilidade pode ser exportado
  [ ] As correções fiscais ao resultado contabilístico (Modelo 22 /
       Anexo C do Modelo 3) estão devidamente justificadas e documentadas
  [ ] As tributações autónomas foram aplicadas a todos os encargos
       relevantes, com as taxas de 2026 e com o agravamento de 10 pontos
       percentuais em período com prejuízo fiscal
  [ ] As derramas municipal e estadual foram corretamente calculadas com
       base no município (taxa de 2026) e nas parcelas do lucro tributável
  [ ] As retenções na fonte declaradas estão suportadas pelos documentos
       comprovativos e declarações dos substitutos tributários (Modelo 10,
       Modelo 39)
  [ ] As contribuições para a Segurança Social foram pagas dentro do prazo
       (ou estão devidamente regularizadas com plano)
  [ ] Os benefícios fiscais reclamados (RFAI, SIFIDE II, outros) estão
       documentados, com elegibilidade comprovada (Anexo D)
  [ ] Os prejuízos fiscais deduzidos respeitam o limite de 65% do lucro
       tributável (75% na parte de prejuízos de 2020 e 2021) e não se
       perderam por alteração de titularidade (CIRC art. 52.º)
  [ ] As operações com entidades relacionadas estão documentadas conforme
       a Portaria n.º 268/2021 (Preços de Transferência), quando exigido
  [ ] As operações com entidades em regime fiscal claramente mais favorável
       estão identificadas e tributadas (CIRC arts. 23.º-A e 88.º, n.º 8)
  [ ] A IES está preparada para envio até 15 julho 2027
  [ ] O pacote de comunicação ao contribuinte inclui instruções claras de
       pagamento com a referência do Portal das Finanças e prazos
  [ ] Não foi aplicada ao período de 2026 qualquer taxa ou regra de 2027
       (por exemplo, a taxa de IRC de 18%)

Assinatura: ____________________  Data: ____________________
            [Nome do CC]
N.º de inscrição na OCC: ____________________
Sociedade de Contabilidade / Firma: ____________________
Seguro de Responsabilidade Civil, Apólice: ____________________ / Validade: __________
```

**Sem esta atestação assinada, não há submissão.**

Para o **Modelo 22 (IRC)** e para a **IES**, a declaração assenta em contabilidade organizada (CIRC art. 123.º, n.º 1) e é assinada pelo CC (Estatuto da OCC, art. 10.º, n.º 1, al. b)). Para o **Modelo 3 (IRS)** com Categoria B em contabilidade organizada, a declaração é igualmente assinada pelo CC (Portaria n.º 104/2026/1, art. 2.º, n.º 2). Para o IRS Categoria B em regime simplificado e para o IRS sem rendimentos empresariais e profissionais, o contribuinte pode submeter diretamente.

## Secção 11: Defaults Conservadores

Quando os inputs das skills upstream forem ambíguos ou estiverem em falta, aplicar os seguintes defaults e sinalizar para o revisor:

**Tabela de defaults conservadores**

| Situação | Default conservador |
| --- | --- |
| Reconciliação cross-skill difere mais de €1 | Sinalizar como "Necessita Input"; não arredondar silenciosamente |
| Coeficiente do regime simplificado da Categoria B ambíguo (entre dois CAE) | Aplicar o **coeficiente mais alto** (menos favorável ao contribuinte); sinalizar |
| Classificação PME / não-PME para a taxa de 15% borderline | Aplicar a taxa geral de 19% sobre TODO o lucro; sinalizar para revisão de elegibilidade PME (anexo ao DL 372/2007) |
| Município de domicílio fiscal incerto (mudança a meio do ano) ou taxa municipal de 2026 não confirmada | Aplicar 1,5% (máximo); sinalizar para o revisor |
| Despesa de representação ou ajuda de custo sem documentação adequada | Tratar como sujeita a TA; sinalizar |
| Pagamento a entidade em regime fiscal claramente mais favorável sem prova de operação efetiva e normal | Aplicar CIRC art. 23.º-A (não dedutível) e TA de 35%; sinalizar |
| Crédito por dupla tributação sem comprovativo de imposto pago no estrangeiro | Excluir o crédito; sinalizar para obtenção de comprovativo (ou usar a prorrogação do CIRS art. 60.º, n.º 3, se aplicável) |
| Prejuízo fiscal sem prova de origem (sociedades) | Excluir; sinalizar para reconstituição |
| RNH / IFICI sem inscrição confirmada no Portal das Finanças | Tratar como regime geral; sinalizar para regularização |
| RFAI / SIFIDE II sem documentação técnica e financeira | Excluir o benefício; sinalizar para preparação do dossier |
| Operações intracomunitárias sem VIES check | Sinalizar; pode haver autoliquidação aplicável ou IVA português |
| Ganho em cripto sem registo de data de aquisição | Tratar como detenção inferior a 365 dias (Categoria G, 28%); sinalizar |
| IBAN do contribuinte em falta (reembolso) | Sinalizar para obtenção; sem IBAN, o reembolso atrasa |
| Cessação de atividade declarada no ano sem regularização do IVA | Sinalizar para regularização (IVA art. 24.º) |
| Pagamentos por conta efetuados mas sem comprovativo | Excluir do crédito; sinalizar para reconciliação com o extrato da AT |
| Dúvida entre englobamento e taxa liberatória / especial (CIRS arts. 22.º, 71.º, 72.º) | Apresentar simulação dos dois cenários no brief; deixar decisão ao revisor |
| Regime de transparência fiscal aplicável incerto | Aplicar o regime que produz tributação superior (conservador); sinalizar |
| Taxas ou regras de 2027 aplicadas ao período de 2026 | Rejeitar; 2026 usa as regras de 2026 (por exemplo, IRC 19%, não 18%) |

- **Regra de tolerância (reforço)**: tolerância de €1. Qualquer discrepância superior é escalada, não absorvida.

## Secção 12: Catálogo de Recusas

- **R-PT-ASM-1**: Skill upstream não correu. Nomear a skill em falta. Continuar com os dados disponíveis; sinalizar a lacuna; não fabricar a computação em falta.
- **R-PT-ASM-2**: Auto-verificação upstream falhou. Registar a verificação específica; continuar mas sinalizar.
- **R-PT-ASM-3**: Reconciliação cross-skill superior a €1. Levantar como "Necessita Input"; não arredondar silenciosamente.
- **R-PT-ASM-4**: Declaração já submetida no Portal das Finanças e o pedido é submeter declaração nova "em cima". Recusar e explicar o procedimento de declaração de substituição (CIRC art. 122.º; CIRS art. 60.º, n.º 2, e Portaria n.º 104/2026/1, art. 3.º). Produzir o working paper da substituição se solicitado, com indicação clara de que se trata de substituição.  _(CIRC art. 122.º / CIRS art. 60.º)_
- **R-PT-ASM-5**: Falta de Contabilista Certificado quando obrigatório. As entidades obrigadas a contabilidade organizada (CIRC art. 123.º, n.º 1; Categoria B em contabilidade organizada, obrigatória quando os rendimentos do ano anterior ultrapassaram €200.000, CIRS art. 28.º, n.º 2) entregam declarações assinadas por CC (Estatuto da OCC, art. 10.º, n.º 1, al. b)). Sinalizar como bloqueador; não submeter sem CC.  _(Estatuto da OCC, art. 10.º)_
- **R-PT-ASM-6**: Inconsistências entre Modelo 3 e Modelo 22 do mesmo contribuinte. Sócio-gerente que receba remuneração deve aparecer simultaneamente no Modelo 22 da sociedade (gasto com pessoal) e no Modelo 3 do próprio (Categoria A). Se houver inconsistência superior a €1, levantar para reconciliação antes de submeter qualquer das duas declarações.
- **R-PT-ASM-7**: Fora do âmbito: regime da Zona Franca da Madeira (Centro Internacional de Negócios), isenções de IRC para entidades com estatutos especiais (cooperativas em certos regimes, IPSS), companhias de seguros e instituições de crédito, atividades petrolíferas, jogos e apostas, organismos de investimento coletivo (Anexo F) e regime especial do transporte marítimo (Anexo G). Encaminhar para especialista; não tentar.
- **R-PT-ASM-8**: Fora do âmbito: não-residentes fiscais sem estabelecimento estável em Portugal, residentes que mudaram durante o ano (dois estatutos de residência no mesmo ano exigem uma declaração por estatuto, CIRS art. 57.º, n.º 6), expatriados com obrigações em múltiplas jurisdições, determinação de estabelecimento estável ao abrigo de CDT. Encaminhar para `pt-cross-border` ou especialista internacional; esta skill assume residência fiscal portuguesa anual completa.
- **R-PT-ASM-9**: Fora do âmbito: contencioso tributário, reclamações graciosas, impugnações judiciais, recursos hierárquicos, ações junto do CAAD (Centro de Arbitragem Administrativa), defesa em inspeção tributária. Encaminhar para advogado ou consultor fiscal com prática contenciosa.
- **R-PT-ASM-10**: Intake incompleto. Nomear o campo de intake em falta (NIF, NIPC, NISS, CAE, residência fiscal, regime de IVA, etc.). Não é possível finalizar a declaração até ser fornecido.
- **R-PT-ASM-11**: Pedido para submeter diretamente no Portal das Finanças. Esta skill produz um working paper. A submissão é ação do contribuinte ou do CC, após revisão e atestação. Recusar educadamente; fornecer as instruções de submissão.
- **R-PT-ASM-12**: Aplicação de regras de outro ano ao período de 2026 (taxas ou limiares de 2027 a 2026, ou de 2026 a 2025). As datas de produção de efeitos governam; não aplicar retroativamente. Recusar educadamente; explicar as regras transitórias.
- **R-PT-ASM-13**: Fora do âmbito: regimes setoriais especiais (banca, seguros, exploração de jogos, atividades extrativas, agricultura e silvicultura com regime especial), SIGI e OIC, SGPS, fusões/cisões com regime de neutralidade fiscal complexa, reorganizações empresariais transfronteiriças, fiscalidade verde (carbono, plástico). Encaminhar para especialista.
- **R-PT-ASM-14**: Pedido envolve criptoativos / NFTs / DeFi com perfil ambíguo. Sinalizar para análise especializada (a skill `portugal-crypto-tax` cobre os casos standard; perfis complexos exigem opinião escrita).

## Secção 13: Auto-verificações

- **Verificação PT-ASM-1**: Todas as skills upstream exigidas para o tipo de declaração escolhido produziram output, ou a lacuna está sinalizada.
- **Verificação PT-ASM-2**: O volume de negócios reconcilia entre `portugal-bookkeeping`, `portugal-vat-return`, e a skill de imposto sobre o rendimento aplicável (`pt-income-tax` / `pt-corporate-tax`) dentro de €1.
- **Verificação PT-ASM-3**: As retenções na fonte declaradas (Anexo A / Anexo B / Modelo 22) estão suportadas pelos documentos comprovativos e pelas declarações Modelo 10 / Modelo 39 dos substitutos tributários; cada retenção tem comprovativo.
- **Verificação PT-ASM-4**: A soma das 12 DMR mensais reconcilia com a folha salarial anual; o Anexo A do Modelo 3 dos colaboradores é coerente.
- **Verificação PT-ASM-5**: Contribuições SS pagas nos prazos; nenhuma em mora; certidão de situação contributiva regularizada verificada.
- **Verificação PT-ASM-6**: Pro-rata IVA definitivo (se aplicável) calculado e regularização incluída na última declaração do ano.
- **Verificação PT-ASM-7**: Faturas comunicadas (e-fatura / SAF-T) reconciliam com a contabilidade (volume de negócios e IVA liquidado).
- **Verificação PT-ASM-8**: Tributações autónomas calculadas com as taxas de 2026, com agravamento de 10 pp em caso de prejuízo, e acrescidas ao imposto no Modelo 22.
- **Verificação PT-ASM-9**: Derrama municipal aplicada com a taxa de 2026 do município; Anexo A do Modelo 22 preenchido quando exigido. Derrama estadual aplicada por parcelas se lucro tributável superior a €1.500.000.
- **Verificação PT-ASM-10**: Adicional de solidariedade IRS aplicado por escalão se rendimento coletável superior a €80.000.
- **Verificação PT-ASM-11**: Coeficientes do regime simplificado da Categoria B aplicados corretamente (CIRS art. 31.º, n.º 1: 0,15 / 0,75 / 0,35 / 0,95 / 0,30 / 0,10 / 1, consoante a natureza do rendimento).  _(CIRS art. 31.º)_
- **Verificação PT-ASM-12**: Prejuízos fiscais deduzidos (CIRC art. 52.º) dentro do limite de 65% do lucro tributável (75% na parte de prejuízos de 2020 e 2021), sem limite temporal, e sem perda por alteração de titularidade.  _(CIRC art. 52.º)_
- **Verificação PT-ASM-13**: Benefícios fiscais (RFAI, SIFIDE II e outros) declarados no Anexo D do Modelo 22, com os limites calculados por `pt-corporate-tax`.
- **Verificação PT-ASM-14**: Prazos explícitos na lista de ações: 5 jan (faturas), 10 jan (DMR), 20 jan (retenções e documento comprovativo), 31 jan (declaração trimestral SS / inventário), 20 fev e 25 fev (IVA), final fev (Modelo 10 / Modelo 39), 31 mai (Modelo 22), 1 abr a 30 jun (Modelo 3), 15 jul (IES).
- **Verificação PT-ASM-15**: Fluxo Portal das Finanças descrito: submissão, nota de liquidação ou autoliquidação, referência de pagamento, pagamento, comprovativo.
- **Verificação PT-ASM-16**: Período de conservação de documentos (10 anos civis, CIVA art. 52.º; 4 anos de caducidade, LGT art. 45.º) declarado.
- **Verificação PT-ASM-17**: Brief do revisor contém referências legais para cada posição adotada (CIRS, CIRC, CIVA, LGT, EBF, Portarias).
- **Verificação PT-ASM-18**: Para sociedades: CC identificado. Para Categoria B em contabilidade organizada: CC identificado.
- **Verificação PT-ASM-19**: Notas de planeamento para 2027 (IRC 18%, RNH transitório, IFICI, Pilar Dois, DAC8 cripto, evolução do SAF-T) incluídas no brief; regras de 2027 NÃO aplicadas a 2026.
- **Verificação PT-ASM-20**: IBAN do contribuinte registado no Portal das Finanças para reembolso (se aplicável); confirmado coincidir com a titularidade do NIF.

## Secção 14: Output Files (PDF / Excel package)

O output final é um conjunto de três ficheiros, colocados em `/mnt/user-data/outputs/`:

1. `[slug_contribuinte]_2026_pt_master.xlsx`: master workbook. Folhas:
   - Cover (identificação)
   - Identidade & regime fiscal
   - Modelo 3 (se aplicável): todos os Anexos preenchidos linha a linha
   - Modelo 22 (se aplicável): rosto + Anexos A/C/D/E (F/G/AIMI se aplicáveis)
   - IES: anexos principais
   - Apuramento de IRC / IRS (memória de cálculo)
   - Mapa de depreciações (Modelo 32)
   - Reconciliação faturas comunicadas ↔ contabilidade ↔ IVA
   - Reconciliação DMR ↔ Modelo 10 ↔ folha salarial
   - Reconciliação cross-skill (síntese das 9 verificações)
   - Calendário 2027: pagamentos por conta + obrigações declarativas
   - Tracker de comprovativos de pagamento
   - Sinalizações para o revisor
   Usar fórmulas vivas onde possível; verificar ausência de `#REF!`.

2. `reviewer_brief.md`: ficheiro markdown com todo o conteúdo da Secção 4 (estrutura do working paper para o CC), com os blocos headline da Secção 5 e o bloco de atestação da Secção 10.

3. `taxpayer_action_list.md`: ficheiro markdown com a lista de ações da Secção 8, mais o bloco de instruções de pagamento da Secção 6 e o bloco de instruções de submissão da Secção 7.

Os três ficheiros são apresentados ao utilizador no final.

Se a execução esgotar o contexto a meio da construção, completar primeiro o trabalho de cálculo / reconciliação e produzir os outputs formatados que forem possíveis, indicando claramente quais os deliverables que ficaram parciais.

## Secção 15: Limitações Conhecidas + Change Log

### 15.1 Limitações conhecidas

1. O preenchimento direto dos formulários oficiais da AT não é automatizado; o CC ou o contribuinte introduz os valores no Portal das Finanças usando o working paper como guia.
2. O Portal das Finanças aceita ficheiros gerados por software de contabilidade; esta skill não gera o ficheiro, gera os valores que o alimentam.
3. Demonstrações financeiras (SNC, NCM, NCM-ME) são geradas pelas skills `portugal-financial-statements` e `portugal-bookkeeping`; a montagem apenas confirma a sua existência e consistência.
4. Dossier completo de Preços de Transferência (Portaria n.º 268/2021) não é montado aqui; ver `pt-transfer-pricing`.
5. Regimes setoriais especiais (banca, seguros, jogos, Zona Franca da Madeira, OIC, SGPS, transporte marítimo, agricultura) estão fora do âmbito.
6. Pilar Dois: apenas sinalização para entidades de grupos abrangidos; a declaração GloBE carece de skill própria.
7. Declaração financeira e fiscal por país (CIRC art. 121.º-A) está fora do âmbito de montagem aqui.
8. As regras de 2027 ainda por legislar (Orçamento do Estado para 2027) podem mudar as notas de planeamento da Secção 9; re-verificar quando a lei for publicada no Diário da República.
9. Submissão automática no Portal das Finanças não é executada pela skill; fica a cargo do CC / contribuinte.
10. A comunicação mensal de faturas ocorre em paralelo durante o ano, não no momento da montagem; a skill apenas confirma que está em dia.
11. Cripto DeFi avançado (LP tokens, yield farming, NFTs, DAOs) pode exceder o enquadramento padrão do CIRS art. 10.º; a skill `portugal-crypto-tax` cobre casos standard.
12. A skill assume um único CC vinculado; se houver mudança de CC durante o exercício, há obrigações de comunicação ao Portal das Finanças que ficam fora do âmbito desta capstone.
13. Os campos do Modelo 22 indicados (Quadro 10) são os do impresso do Despacho n.º 320/2026, e da declaração periódica de IVA só os campos 40, 41 e 93 a 96; confirmar no impresso aprovado para a campanha de 2027 e em `portugal-vat-return`.

### 15.2 Change log

- v1.1 (2026-10-30): Período de tributação 2026 (campanha 2027). Prazos movidos para 2027 a partir dos códigos (CIRS art. 60.º, CIRC arts. 104.º, 120.º e 121.º, CIVA arts. 27.º e 41.º, CIRS art. 119.º). Anexos do Modelo 3 alinhados com a Portaria n.º 104/2026/1 (G1, I e SS acrescentados) e do Modelo 22 com o Despacho n.º 320/2026 (Anexo B só para períodos anteriores a 2011; F, G e AIMI acrescentados). Taxas de IRC 19% / 15% (Lei n.º 64/2025), tributações autónomas de 2026, prejuízos a 65% sem limite temporal, retenções da Categoria B a 23% / 16,5% / 11,5% / 20%, pagamentos por conta de IRS a 65%, Modelo 10 e Modelo 39 até ao final de fevereiro (DL 49/2025), pagamento do IVA até dia 25, coimas do RGIT corrigidas, base legal do CC corrigida para o Estatuto da OCC, conservação de 10 anos pelo CIVA art. 52.º. Removidos valores sem fonte oficial lida (IBAN da AT, número de dígitos de referências, números de campos); ver a linha "Not yet confirmed". Revisão independente (2026-10-30): títulos dos anexos F, G1, I e L confirmados (Portarias 72-B/2025/1 e 39-B/2024); campos do Quadro 10 do Modelo 22 (Despacho 320/2026) e nota de que esse impresso ainda traz as taxas de 2025; taxas e prazos da Segurança Social do empregador (Código Contributivo arts. 40.º, 43.º, 53.º e 69.º); juros de mora de 7,221% (Aviso 18/2026/2); campos 40, 41 e 93 a 96 da declaração de IVA e novo modelo de julho de 2027; prazo da declaração por país (CIRC art. 121.º-A); IVA mensal de dezembro de 2026 até 22 de fevereiro de 2027.
- v1.0 (2026-05): Versão inicial. Modelada sobre `ng-return-assembly`, `id-return-assembly`, `mt-return-assembly` e `us-ca-return-assembly`. Adaptada para Modelo 3 IRS + Anexos, Modelo 22 IRC + Anexos, IES, SAF-T (PT), DMR, declaração periódica de IVA, submissão via Portal das Finanças e impacto prospetivo do OE 2026. Coordena as skills upstream Portugal. Atestação requer Contabilista Certificado membro da OCC.

## Secção 16: Fontes

**Tabela de fontes (legislação de base)**

| Fonte | Referência |
| --- | --- |
| Código do IRS (CIRS), Decreto-Lei n.º 442-A/88 | Arts. 10.º (mais-valias, cripto), 12.º-B (IRS Jovem), 25.º (dedução específica), 28.º e 31.º (regime simplificado), 57.º (declaração e anexos), 60.º (prazo do Modelo 3), 68.º e 68.º-A (taxas e adicional de solidariedade), 69.º (tributação conjunta), 71.º e 72.º (taxas liberatórias e especiais), 78.º-B (faturas e deduções), 81.º (dupla tributação), 98.º e 101.º (retenções), 102.º (pagamentos por conta), 119.º (DMR, Modelo 10, Modelo 39, Modelo 30) |
| Código do IRC (CIRC), Decreto-Lei n.º 442-B/88 | Arts. 6.º, 8.º, 23.º-A, 51.º, 52.º (prejuízos), 63.º (preços de transferência), 67.º, 87.º (taxas), 87.º-A (derrama estadual), 88.º (tributações autónomas), 91.º, 104.º a 107.º (pagamentos), 117.º, 120.º (Modelo 22), 121.º (IES), 122.º (substituição), 123.º (contabilidade organizada, SAF-T) |
| Código do IVA (CIVA), Decreto-Lei n.º 394-B/84 | Arts. 23.º (pro-rata), 27.º (pagamento), 29.º (obrigações), 41.º (declaração periódica), 52.º (conservação), 53.º (isenção) |
| Lei Geral Tributária (LGT), Decreto-Lei n.º 398/98 | Arts. 35.º (juros compensatórios), 44.º (juros de mora), 45.º (caducidade) |
| Regime Geral das Infrações Tributárias (RGIT), Lei n.º 15/2001 | Arts. 26.º, 29.º, 114.º, 116.º, 117.º |
| Código do IMI | Art. 120.º (prestações) |
| Decreto-Lei n.º 198/2012 | Art. 3.º (comunicação de faturas, dia 5), art. 3.º-A (comunicação de inventários) |
| Lei n.º 64/2025 | Taxas de IRC 2026 (19%) e 2027 (18%); taxa PME de 15% |
| Lei n.º 73-A/2025 (Orçamento do Estado para 2026) | Escalões de IRS de 2026 |
| Portaria n.º 104/2026/1 e Portaria n.º 136-C/2026/1 | Modelo 3 e anexos |
| Despacho n.º 320/2026 | Modelo 22 e anexos |
| Portaria n.º 268/2021 | Preços de transferência: dossier e dispensas |
| Estatuto da Ordem dos Contabilistas Certificados | Art. 10.º, n.º 1, al. b) (assinatura das declarações fiscais) |
| Código Contributivo, Lei n.º 110/2009 e ISS, Guia Prático dos Trabalhadores Independentes | Arts. 40.º, 43.º, 53.º, 69.º, 155.º e 168.º (taxas, declaração de remunerações, pagamento); rendimento relevante, declaração trimestral, Anexo SS |
| Aviso n.º 18/2026/2 (IGCP) | Taxa de juros de mora de 2026 (7,221%) |
| Portarias n.º 72-B/2025/1 e n.º 39-B/2024 | Anexos F, G1, L e I do Modelo 3 |
| Ofício-Circulado n.º 25119/2026 (AT) e Portaria n.º 298/2026/1 | Declaração periódica de IVA: campos 40, 41, 93 a 96; novo modelo a partir de julho de 2027 |

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| CIRS art. 60 (Modelo 3, 1 April to 30 June; foreign tax credit extension) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs60.aspx | 2026-10-30 |
| CIRS art. 57 (return and annexes; two residence statuses) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs57.aspx | 2026-10-30 |
| Portaria n.º 104/2026/1 (Modelo 3 annexes, electronic filing, CC password, 30-day correction) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/portaria-104-2026-1.pdf | 2026-10-30 |
| Portaria n.º 136-C/2026/1 (Anexo H instructions) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/portaria-136-c-2026-1.pdf | 2026-10-30 |
| Despacho n.º 320/2026 (Modelo 22 and annexes in force in 2026) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/despacho-320-2026.pdf | 2026-10-30 |
| AT, Modelo 22 annex forms A, C, D, E, F, G (form titles) | https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/modelos_formularios/irc/Documents/M22ANA.PDF (and M22ANC, M22AND, M22ANE, M22ANF, M22ANG) | 2026-10-30 |
| CIRC art. 87 and Lei 64/2025 art. 3 (19% 2026, 18% 2027, 17%, 15% SME, 12.5% startups) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87.aspx | 2026-10-30 |
| CIRC art. 87-A (derrama estadual) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87a.aspx | 2026-10-30 |
| CIRC art. 88 (autonomous taxation) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc88.aspx | 2026-10-30 |
| CIRC art. 52 (losses 65%, no time limit, change of ownership) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc52.aspx | 2026-10-30 |
| Lei n.º 27-A/2020 art. 11(2) (extra 10 points for 2020 and 2021 losses) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Lei_27_A_2020.pdf | 2026-10-30 |
| CIRC arts. 104, 105, 106, 107 (payment rules, payments on account, PEC repealed, limits) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc104.aspx (and irc105, irc106, irc107) | 2026-10-30 |
| CIRC arts. 117, 120, 121, 122, 123 (returns, Modelo 22 and IES deadlines, substitution, organised accounts, SAF-T export) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc120.aspx (and irc117, irc121, irc122, irc123) | 2026-10-30 |
| CIRS art. 68-A (solidarity surcharge) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs68a.aspx | 2026-10-30 |
| CIRS art. 25 (Category A deduction 8.54 x IAS) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs25.aspx | 2026-10-30 |
| CIRS arts. 28 and 31 (EUR 200,000 limit; coefficients; invoices by end February) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs31.aspx (and irs28) | 2026-10-30 |
| CIRS arts. 71, 72, 10 (28% and 35% final withholding; 28% special rate; crypto 365 days) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs71.aspx (and irs72, irs10) | 2026-10-30 |
| CIRS art. 78-B (invoices by end February, 15 March, 31 March) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs78b.aspx | 2026-10-30 |
| CIRS arts. 98 and 101 (withholding paid by the 20th; Category B 23% / 16.5% / 11.5% / 20%, Category F 25% / 10%) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs101.aspx (and irs98) | 2026-10-30 |
| CIRS art. 102 (payments on account: 20 July, September, December; 65%; penultimate year) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs102.aspx | 2026-10-30 |
| CIRS art. 119 (20 January statement, DMR by the 10th, Modelo 10 and Modelo 39 by end February, Modelo 30, end of July return) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs119.aspx | 2026-10-30 |
| CIRS art. 12-B (IRS Jovem bar for NHR / IFICI) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs12b.aspx | 2026-10-30 |
| CIVA arts. 41, 27, 52 (return by the 20th, payment by the 25th, 10-year retention) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/iva41.aspx (and iva27, iva52) | 2026-10-30 |
| CIVA art. 53 (EUR 15,000 exemption) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/artigo-53-o-do-civa.aspx | 2026-10-30 |
| Decreto-Lei n.º 198/2012, arts. 3 and 3-A (invoice reporting by the 5th; inventory by 31 January) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Decreto-Lei%20n%20_198_2012_24_08.pdf | 2026-10-30 |
| RGIT arts. 26, 29, 114, 116, 117 (fines) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit116.aspx (and rgit26, rgit29, rgit114, rgit117) | 2026-10-30 |
| LGT arts. 35, 44, 45 (compensatory interest, late interest, 4-year limitation) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/lgt/Pages/lgt45.aspx (and lgt35, lgt44) | 2026-10-30 |
| CIMI art. 120 (IMI instalments) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cimi/Pages/cimi120.aspx | 2026-10-30 |
| ISS, Guia Prático, Trabalhadores Independentes (21.4%, 25.2%, 70% / 20%, EUR 20, IAS 2026 EUR 537.13, quarterly declaration, payment 10th to 20th, Anexo SS) | https://www.seg-social.pt/ptss/pssd/documento/cmc1xyfxz00dekl2ynxz676sw | 2026-10-30 |
| Portaria n.º 268/2021 (transfer pricing file: EUR 10,000,000, EUR 100,000 / EUR 500,000) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Portaria_268_2021.pdf | 2026-10-30 |
| Estatuto da Ordem dos Contabilistas Certificados (2024 edition), art. 10 | https://www.occ.pt/sites/default/files/public/2024-09/Estatuto_2024.pdf | 2026-10-30 |
| Portaria n.º 72-B/2025/1 (Modelo 3 annexes F, G1, L and their titles) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Portaria_72_B_2025_1.pdf | 2026-10-30 |
| Portaria n.º 39-B/2024 (Modelo 3 Anexo I, rendimentos de herança indivisa) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Portaria_39_B_2024.pdf | 2026-10-30 |
| Despacho n.º 320/2026, Modelo 22 form, Quadro 10 (field numbers; field 347 still at 20% / 16%) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/despacho-320-2026.pdf | 2026-10-30 |
| Código dos Regimes Contributivos (Lei 110/2009), arts. 40(8), 43, 53, 69(2), 155(2), 168 (34.75% = 23.75% + 11%; declaration by the 20th; employer payment 1st to 25th from 1 January 2026, DL 127/2025) | https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575 | 2026-10-30 |
| IGCP, Aviso n.º 18/2026/2 (late-payment interest 7.221% from 1 January 2026) | https://diariodarepublica.pt/dr/detalhe/aviso/18-2026-993315668 | 2026-10-30 |
| AT, Ofício-Circulado n.º 25119/2026 (VAT return: fields 40, 41, 93 to 96; Portaria 298/2026/1 new model for periods from 1 July 2027; VAT groups box from 1 July 2026) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/instrucoes_administrativas/Documents/Oficio-Circulado-25119-2026.pdf | 2026-10-30 |
| CIRC art. 121-A (country-by-country report: EUR 750,000,000, 12 months, notification by the Modelo 22 deadline) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc121a.aspx | 2026-10-30 |

Not yet confirmed: the act approving Anexo SS to the Modelo 3 (the ISS guide describes it, the approving act was not read); the Modelo 22 form and Quadro 10 field numbers for the 2027 campaign (the 2026 period), because that form is not yet approved: the field map in Section 2.2 is from the Despacho 320/2026 form; the other Modelo 22 quadros and the periodic VAT return field numbers other than 40, 41 and 93 to 96 (an earlier version listed Modelo C fields 1, 4, 5, 7 and 22); the Modelo 22 annex subjects of B (pre-2011 only) beyond what the AT form titles show; the IES annex letters and contents (an earlier version said Anexo L related parties, R intra-EU, Q offshore); the 18.4% rate an earlier version gave for self-employed pensioners (not found in the consolidated Contributions Code); the first-job youth hiring relief (Decreto-Lei 72/2017) an earlier version cited; RFAI and SIFIDE II percentages and the SIFIDE carry-forward period an earlier version gave as 8 years (see pt-corporate-tax); whether CFEI II and DLRR can still be claimed for 2026; the treatment of unused special payments on account (PEC) paid before 2022; the Pillar Two transposing act (an earlier version said Lei 41/2024), the EUR 750 million group threshold for Pillar Two and the 15% minimum rate; the DAC8 start date for crypto reporting; the date for direct filing of the accounting SAF-T; the IUC payment month rule; the validity period of tax and social security clearance certificates (an earlier version said 3 months); the 15-day Social Security deadline for start, cessation or suspension of activity and the January "Folha de Férias / Mapa de Encargos" an earlier version listed; the AT IBAN and the digit counts of NIF, NISS and Multibanco references an earlier version gave; the IRS deduction caps and band table, which this skill takes from pt-income-tax and pt-irs-employees-investment.

## Disclaimer final

OpenAccountants: skills de contabilidade open-source para IA.
Isto não constitui aconselhamento fiscal. Todos os outputs devem ser revistos e, quando a declaração assenta em contabilidade organizada, assinados por um Contabilista Certificado inscrito na OCC (Ordem dos Contabilistas Certificados), antes de submissão no Portal das Finanças, na Segurança Social Direta, ou em qualquer outra plataforma oficial.

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
