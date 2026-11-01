---
name: portugal-einvoice
description: "Utilize esta skill sempre que lhe forem colocadas questões sobre faturação eletrónica em Portugal em 2026: códigos ATCUD, comunicação mensal dos elementos das faturas (SAF-T(PT) até ao dia 5), código QR, software de faturação certificado pela AT (volume de negócios acima de EUR 50.000, uso de programa informático ou contabilidade organizada), aplicações de faturação da AT, portal e-fatura, faturas em PDF aceites até 31 de dezembro de 2026 e assinatura ou selo eletrónico qualificado a partir de 2027, faturação eletrónica nos contratos públicos (CCP art. 299.º-B, PME obrigadas a partir de 1 de janeiro de 2027), SAF-T da contabilidade (períodos de 2027, entregue em 2028), arquivo por 10 anos e coimas do RGIT. Fora do âmbito: taxas e declaração periódica de IVA (portugal-vat-return), IES e demonstrações financeiras (portugal-financial-statements), lançamentos (portugal-bookkeeping). LEIA SEMPRE esta skill antes de tocar em qualquer trabalho de conformidade de faturação em Portugal. Trigger also on: \"ATCUD\", \"SAF-T Portugal\", \"e-fatura\", \"QR code invoice\", \"certified software AT\", \"Peppol Portugal\", \"B2G e-invoice\", \"invoice hash chain\", \"Portaria 195/2020\", \"Decreto-Lei 28/2019\", \"PDF invoices Portugal 2027\", or \"Qualified Electronic Signature Portugal\"."
version: 1.2
jurisdiction: PT
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - einvoice-workflow-base
category: invoicing
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Portugal Einvoice

## Portugal: Faturação Eletrónica (ATCUD / SAF-T(PT) / e-Fatura), Skill v1.1 (2026)

## Rates and thresholds

> Source-cited draft: not reviewed by an accountant.

Todos os valores foram lidos em 30 de outubro de 2026 nos textos publicados pela AT no Portal das Finanças ou no Diário da República. As fontes estão na secção final. Para as taxas de IVA, a skill `portugal-vat-return` manda se houver divergência.

### Faturação Eletrónica

- **Software certificado obrigatório**: volume de negócios do ano anterior > €50.000, ou uso de programa informático de faturação, ou contabilidade organizada (basta uma das três) _(DL 28/2019, art. 4.º, n.º 1)_
- **ATCUD**: obrigatório em todas as faturas e documentos fiscalmente relevantes, seja qual for o meio de emissão _(Portaria 195/2020, art. 4.º, n.º 1)_
- **Código QR**: obrigatório nos documentos emitidos por programas certificados _(Portaria 195/2020, art. 6.º, n.º 1)_
- **Comunicação mensal dos elementos das faturas**: até ao dia 5 do mês seguinte ao da emissão _(DL 198/2012, art. 3.º, n.º 2, redação da Lei 12/2022)_
- **Faturas em PDF**: aceites como faturas eletrónicas até 31 de dezembro de 2026 _(Lei 73-A/2025, art. 95.º, n.º 3)_
- **A partir de 1 jan 2027**: fatura eletrónica com autenticidade e integridade garantidas, nomeadamente por assinatura eletrónica qualificada, selo eletrónico qualificado ou EDI _(DL 28/2019, art. 12.º, n.º 2)_
- **B2G (contratos públicos)**: faturas eletrónicas obrigatórias; para os cocontratantes que não sejam PME nem entidades públicas, desde 1 de janeiro de 2021; regime transitório das micro, pequenas e médias empresas e das entidades públicas cocontratantes prorrogado até 31 de dezembro de 2026 _(CCP, art. 299.º-B; DL 111-B/2017, art. 9.º, n.os 3 e 4; Lei 73-A/2025, art. 260.º, n.º 2)_
- **SAF-T(PT) da contabilidade**: aplica-se aos períodos de 2027 e seguintes, a entregar em 2028 _(Lei 73-A/2025, art. 95.º, n.º 2)_
- **Emissão da fatura**: até ao 5.º dia útil seguinte ao momento em que o IVA é devido _(CIVA, art. 36.º, n.º 1, al. a))_
- **Fatura simplificada**: até €1.000 (retalhistas a não sujeitos passivos), até €100 (restantes), ou qualquer valor no regime de isenção do art. 53.º _(CIVA, art. 40.º, n.º 1)_
- **Arquivo**: 10 anos _(DL 28/2019, art. 19.º, n.º 1; CIVA, art. 52.º, n.º 1)_
- **Não emissão ou emissão tardia de faturas**: €150 a €3.750 _(RGIT, art. 123.º, n.º 1)_
- **Falta de software certificado**: €1.500 a €18.750 _(RGIT, art. 128.º, n.º 2)_
- **Falta ou atraso da comunicação dos elementos das faturas (SAF-T mensal)**: €200 a €10.000, contraordenação grave _(RGIT, art. 117.º, n.º 9)_
- **Pessoas coletivas**: os limites mínimo e máximo das coimas elevam-se para o dobro _(RGIT, art. 26.º, n.º 4)_

## Secção 1: Referência Rápida

**Referência Rápida**

| Campo | Valor |
| --- | --- |
| País | Portugal (República Portuguesa) |
| Moeda | EUR |
| Nome do sistema | e-fatura (comunicação dos elementos das faturas à AT) com ATCUD e código QR |
| Entidade reguladora | Autoridade Tributária e Aduaneira (AT) |
| Legislação principal | Decreto-Lei 28/2019 (processamento de faturas e arquivo; alterado pelos DL 48/2020 e DL 49/2025); Decreto-Lei 198/2012 (comunicação das faturas); Portaria 195/2020 (código QR e ATCUD); Portaria 363/2010 (certificação de software; os arts. 1.º, 2.º, 8.º e 9.º foram revogados pelo DL 28/2019, art. 44.º, al. i)); Portaria 321-A/2007 (SAF-T(PT)); CIVA arts. 36.º, 40.º e 52.º; CCP art. 299.º-B (contratos públicos); RGIT (coimas) |
| Regras transitórias de 2026 | Lei 73-A/2025 (Orçamento do Estado para 2026): art. 95.º (PDF até 31 dez 2026; SAF-T da contabilidade a partir dos períodos de 2027) e art. 260.º, n.º 2 (regime transitório B2G das PME até 31 dez 2026) |
| Estado atual (2026) | ATCUD e código QR em vigor; comunicação mensal dos elementos das faturas até ao dia 5; PDF ainda aceite como fatura eletrónica; B2G obrigatório para grandes empresas e transitório para PME até ao fim de 2026; B2B sem obrigação de troca estruturada |
| Versão da skill | 1.1 |

## Secção 2: Âmbito da Obrigação

### Quem Deve Cumprir

- **B2G (empresa para Estado)**: no âmbito da execução de contratos públicos, os cocontratantes são obrigados a emitir faturas eletrónicas no modelo da norma europeia aprovada pela Comissão Europeia e publicitada no portal dos contratos públicos (CCP, art. 299.º-B, n.os 1 e 3). Os cocontratantes puderam usar outros mecanismos de faturação até 31 de dezembro de 2020 (DL 111-B/2017, art. 9.º, n.º 3), pelo que, desde 1 de janeiro de 2021, a fatura eletrónica é obrigatória para quem não esteja no regime do n.º 4. As micro, pequenas e médias empresas (definidas pela Recomendação 2003/361/CE) e as entidades públicas enquanto cocontratantes beneficiam desse regime transitório (art. 9.º, n.º 4, que na redação consolidada termina a 31 de dezembro de 2025), prorrogado até 31 de dezembro de 2026 (Lei 73-A/2025, art. 260.º, n.º 2). Quem use outros mecanismos dentro destes prazos não pode ser discriminado pelos contraentes públicos (art. 9.º, n.º 5). Os contraentes públicos estão obrigados a receber e processar faturas eletrónicas desde 18 de abril de 2019, ou 18 de abril de 2020 para os que não integrem as alíneas a) e d) do n.º 1 do art. 2.º do CCP (art. 9.º, n.os 1 e 2). Se nada mudar no Orçamento do Estado para 2027, as PME passam a ter de faturar eletronicamente às entidades públicas a partir de 1 de janeiro de 2027. Contratos secretos ou com medidas especiais de segurança estão excluídos (art. 299.º-B, n.º 2).
- **B2B (empresa para empresa)**: Portugal não impõe a troca de faturas eletrónicas estruturadas entre privados. A conformidade assenta em camadas: (1) meios de processamento autorizados e, quando aplicável, software certificado pela AT (DL 28/2019, arts. 3.º e 4.º); (2) ATCUD em todas as faturas (Portaria 195/2020, art. 4.º); (3) código QR nos documentos de software certificado (Portaria 195/2020, art. 6.º); (4) comunicação dos elementos das faturas à AT até ao dia 5 do mês seguinte (DL 198/2012, art. 3.º). A fatura eletrónica entre privados depende da aceitação do destinatário (DL 28/2019, art. 12.º, n.º 1; CIVA, art. 36.º, n.º 10).
- **B2C (empresa para consumidor)**: as mesmas regras do B2B. O NIF do consumidor só consta da fatura quando este o pede (CIVA, art. 36.º, n.º 16, e art. 40.º, n.º 3). O consumidor que não deu o NIF pode comunicar a fatura à AT através do código QR ou do ATCUD (CIRS, art. 78.º-B, n.º 3).

### Limiares e Isenções

- **Sem limiar de volume de negócios para ATCUD e comunicação**: o ATCUD é obrigatório em todas as faturas, por qualquer meio de processamento (Portaria 195/2020, art. 4.º, n.º 1); a comunicação abrange todos os que estejam sujeitos às regras de faturação portuguesas e pratiquem operações sujeitas a IVA (DL 198/2012, art. 3.º, n.º 1).
- **Software certificado pela AT** (DL 28/2019, art. 4.º, n.º 1): obrigatório para quem tenha sede, estabelecimento estável ou domicílio em Portugal, e para outros sujeitos passivos cuja faturação siga as regras portuguesas (CIVA, art. 35.º-A), sempre que se verifique **qualquer** destas condições: (a) volume de negócios do ano anterior acima de EUR 50 000 (ou anualizado no ano de início); (b) uso de programas informáticos de faturação; (c) contabilidade organizada, obrigatória ou por opção. A AT publica a lista de programas certificados (art. 4.º, n.º 3).
- **Aplicações de faturação da AT** (DL 28/2019, art. 4.º-A, desde 1 de julho de 2025): podem ser usadas em alternativa; quem pratique uma só operação tributável tem de faturar através delas.
- **Outros meios eletrónicos** (máquinas registadoras, terminais, balanças) só servem para faturas simplificadas (DL 28/2019, art. 4.º, n.º 5).
- **Faturas simplificadas** (CIVA, art. 40.º, n.º 1): transmissões de bens por retalhistas ou vendedores ambulantes a não sujeitos passivos até EUR 1 000; outras operações até EUR 100; e operações de sujeitos passivos no regime de isenção do art. 53.º. Continuam a exigir ATCUD (Portaria 195/2020, art. 4.º) e, se emitidas por software certificado, código QR (art. 6.º).

### Fases do Calendário

**Fases do Calendário**

| Data | Marco | Base |
| --- | --- | --- |
| 18 abr 2019 / 18 abr 2020 | Contraentes públicos obrigados a receber e processar faturas eletrónicas (18 abr 2020 para os que não integrem as als. a) e d) do n.º 1 do art. 2.º do CCP) | DL 111-B/2017, art. 9.º, n.os 1 e 2 |
| 1 jan 2020 | Comunicação prévia das séries documentais à AT (art. 35.º do DL 28/2019) produz efeitos | DL 28/2019, art. 45.º, n.º 2 |
| 1 jan 2021 | Portaria 195/2020 (código QR e ATCUD) entra em vigor | Portaria 195/2020, art. 8.º |
| 1 jan 2021 | Fatura eletrónica B2G obrigatória para os cocontratantes fora do regime transitório das PME e entidades públicas | DL 111-B/2017, art. 9.º, n.º 3 |
| 2022 | Prazo de comunicação dos elementos das faturas passa para o dia 5 do mês seguinte (Lei 12/2022, de 27 de junho) | DL 198/2012, art. 3.º, n.º 2 |
| 1 jul 2025 | Aplicações de faturação da AT reguladas no art. 4.º-A do DL 28/2019 | DL 49/2025 |
| 31 dez 2026 | Último dia em que faturas em PDF são aceites como faturas eletrónicas | Lei 73-A/2025, art. 95.º, n.º 3 |
| 31 dez 2026 | Fim do regime transitório B2G das micro, pequenas e médias empresas | Lei 73-A/2025, art. 260.º, n.º 2 |
| 1 jan 2027 | Fatura eletrónica exige um meio que garanta autenticidade e integridade (art. 12.º, n.º 2 do DL 28/2019): assinatura eletrónica qualificada, selo eletrónico qualificado ou EDI | DL 28/2019, art. 12.º; Lei 73-A/2025, art. 95.º, n.º 3 |
| 2028 | Primeira entrega do SAF-T(PT) da contabilidade (períodos de 2027) | Lei 73-A/2025, art. 95.º, n.º 2 |

As datas a partir das quais o código QR e o ATCUD passaram a ser exigidos na prática (o texto anterior indicava janeiro de 2022 e janeiro de 2023) resultam de despachos de adiamento que não foram relidos hoje (ver "Not yet confirmed").

## Secção 3: Formato Técnico

### Normas de Formato da Fatura

- **B2G**: modelo da norma europeia aprovada pela Comissão Europeia (CCP, art. 299.º-B, n.º 3), ou seja a EN 16931. Em Portugal usa-se a especificação CIUS-PT em XML UBL 2.1, transmitida pela rede Peppol (Peppol BIS Billing 3.0). Os elementos que a fatura B2G tem de conter, quando aplicáveis, constam do art. 299.º-B, n.º 1: identificadores do processo e da fatura, período de faturação, cocontratante, contraente público, entidade beneficiária, representante fiscal, referência do contrato, condições de entrega, instruções de pagamento, ajustamentos e encargos, rubricas e totais.
- **B2B/B2C**: não há formato XML estruturado obrigatório. As faturas podem ser em papel ou eletrónicas, desde que processadas por um meio autorizado (DL 28/2019, art. 3.º) e com ATCUD e, quando aplicável, código QR. Os dados das faturas são comunicados à AT por SAF-T(PT), em tempo real ou por inserção direta no Portal das Finanças (DL 198/2012, art. 3.º, n.º 1).

### Esquema do SAF-T(PT)

- **Estrutura XML**: definida pela Portaria 321-A/2007 (DL 198/2012, art. 3.º, n.º 1, al. b)).  _(Portaria 321-A/2007)_
- **SAF-T(PT) de faturação, conteúdo**: Header, Customer, TaxTable, Payments, Supplier, Product, SalesInvoices, MovementOfGoods, WorkingDocuments.
- **SAF-T(PT) da contabilidade, conteúdo**: Header, Customer, TaxTable, Payments, GeneralLedgerAccounts, Supplier, GeneralLedgerEntries, FixedAssets, Inventory.
- **Exportação**: os sistemas de faturação ou contabilidade têm de conseguir exportar o ficheiro de auditoria tributária (DL 28/2019, art. 11.º, n.º 5).

### Estrutura do ATCUD

- **Formato** (Portaria 195/2020, arts. 3.º e 4.º): `ATCUD:CódigoValidação-NúmeroSequencial`. O código de validação da série é atribuído pela AT depois da comunicação da série (DL 28/2019, art. 35.º) e tem no mínimo 8 carateres (art. 3.º, n.º 1). O número sequencial é o número do documento dentro da série, a sequência numérica a seguir à barra (/) da identificação do documento (art. 3.º, n.º 3). Exemplo: `ATCUD:TES123TE-4561`.
- **Onde aparece**: em todas as páginas do documento e, quando há código QR, imediatamente acima dele (art. 4.º, n.º 3).
- No código QR e no SAF-T(PT) usa-se apenas `TES123TE-4561`, sem o prefixo `ATCUD:` (ver "Not yet confirmed").

### Especificação do Código QR

- **Conteúdo**: as especificações técnicas são definidas pela AT e publicadas no Portal das Finanças (Portaria 195/2020, art. 5.º). Segundo a especificação da AT, o código QR codifica: NIF do emitente, NIF do adquirente e país do adquirente; tipo, estado e data do documento, identificação única do documento e ATCUD; espaço fiscal, bases tributáveis e IVA por taxa (campos I1 a I8, J1 a J8 e K1 a K8 para PT, PT-AC e PT-MA); total do documento, retenção na fonte e 4 carateres do hash (ver "Not yet confirmed").
- **Posição**: dentro do corpo do documento, legível em qualquer suporte; em documentos com várias páginas, na primeira ou na última (Portaria 195/2020, art. 6.º, n.os 2 e 3).

### Cadeia de Hash (Assinatura Digital RSA)

- **Cadeia de hash**: cada fatura emitida por software certificado inclui uma assinatura RSA que liga cada documento ao anterior, garantindo a inviolabilidade. Os primeiros 4 carateres do hash aparecem na fatura impressa ou em PDF. Os requisitos constam da Portaria 363/2010 e não foram relidos hoje (ver "Not yet confirmed"). Os programas têm de detetar alterações à informação e impedir a continuação do uso do sistema quando a integridade é posta em causa (DL 28/2019, art. 11.º, n.º 2).

## Secção 4: Campos Obrigatórios

### Campos Exigidos nas Faturas Portuguesas

**Campos Exigidos nas Faturas Portuguesas**

| Campo | Descrição | Base |
| --- | --- | --- |
| Data e numeração sequencial | Datada e numerada sequencialmente, dentro de cada série, por um período não inferior a um ano fiscal | CIVA, art. 36.º, n.º 5; DL 28/2019, art. 7.º, n.º 4 |
| Fornecedor | Nome, firma ou denominação, sede ou domicílio e NIF | CIVA, art. 36.º, n.º 5, al. a) |
| Adquirente sujeito passivo | Nome, sede ou domicílio e NIF | CIVA, art. 36.º, n.º 5, al. a) |
| Adquirente consumidor | NIF só quando o consumidor o pede | CIVA, art. 36.º, n.º 16 |
| Bens ou serviços | Quantidade e denominação usual, com os elementos necessários para determinar a taxa | CIVA, art. 36.º, n.º 5, al. b) |
| Preço | Preço líquido de imposto e outros elementos do valor tributável | CIVA, art. 36.º, n.º 5, al. c) |
| Taxas e IVA | Taxas aplicáveis e montante de imposto, separados por taxa | CIVA, art. 36.º, n.º 5, al. d) e parágrafo final |
| Isenção | Motivo justificativo da não aplicação do imposto | CIVA, art. 36.º, n.º 5, al. e) |
| Data da operação | Data da entrega ou da prestação, se diferente da data da fatura | CIVA, art. 36.º, n.º 5, al. f) |
| Autoliquidação | Menção "IVA - autoliquidação" quando o adquirente é o devedor | CIVA, art. 36.º, n.º 13 |
| Autofaturação | Menção "autofaturação" e acordo escrito prévio | CIVA, art. 36.º, n.º 11 |
| Representante fiscal | Nome, morada e NIF do representante de um não residente | CIVA, art. 36.º, n.º 9 |
| ATCUD | Código único de documento | Portaria 195/2020, art. 4.º |
| Código QR | Em documentos de software certificado | Portaria 195/2020, art. 6.º |
| Hash (4 carateres) e número de certificado do programa | Impressos na fatura | Portaria 363/2010 (ver "Not yet confirmed"); o número do certificado é comunicado à AT (DL 198/2012, art. 3.º, n.º 4, al. l)) |
| Moeda | EUR no mercado interno | Ver "Not yet confirmed" para regras de câmbio |

A fatura simplificada tem menos elementos: NIF e nome do fornecedor, quantidade e denominação, preço e IVA (ou preço com IVA e taxa), NIF do adquirente sujeito passivo e motivo de isenção (CIVA, art. 40.º, n.º 2).

### Campos Adicionais B2G (CIUS-PT / Peppol BIS 3.0)

**Campos Adicionais B2G (CIUS-PT / Peppol BIS 3.0)**

| Campo | Caminho (UBL 2.1) |
| --- | --- |
| Referência do adquirente | `cbc:BuyerReference` |
| Referência do contrato (CCP, art. 299.º-B, n.º 1, al. g)) | `cac:ContractDocumentReference/cbc:ID` |
| Referência da encomenda | `cac:OrderReference/cbc:ID` |
| CustomizationID CIUS-PT | `cbc:CustomizationID` = `urn:cen.eu:en16931:2017#compliant#urn:feap.gov.pt:CIUS-PT:2.1.1` (versão não confirmada hoje) |
| Profile ID | `cbc:ProfileID` = `urn:fdc:peppol.eu:2017:poacc:billing:01:1.0` |
| Endpoint ID (Peppol) | `cbc:EndpointID` com identificador de esquema |

## Secção 5: Método de Transmissão

### Comunicação dos Elementos das Faturas (B2B/B2C)

**Comunicação dos Elementos das Faturas (B2B/B2C)** _(DL 198/2012, art. 3.º)_

| Canal | Detalhe |
| --- | --- |
| Tempo real | Transmissão eletrónica de dados em tempo real (art. 3.º, n.º 1, al. a)) |
| Ficheiro SAF-T(PT) | Remessa do ficheiro normalizado SAF-T(PT) (art. 3.º, n.º 1, al. b)) |
| Portal das Finanças | Inserção direta no Portal (art. 3.º, n.º 1, al. c)); não serve a quem é obrigado a produzir SAF-T(PT), que tem de usar tempo real ou ficheiro (art. 3.º, n.º 3) |
| Prazo | Até ao dia 5 do mês seguinte ao da emissão (art. 3.º, n.º 2) |
| O que se comunica | Faturas, documentos de conferência de mercadorias ou de prestação de serviços e recibos (art. 3.º, n.º 1) |
| Dados por documento | NIF do emitente, número, data, tipo de documento, NIF do adquirente quando inserido, valor tributável, taxas, motivo de isenção, IVA ou Imposto do Selo, menção IVA de caixa, número do certificado do programa, documento de origem, documento retificado, país ou região do imposto e ATCUD (art. 3.º, n.º 4) |
| Autenticação | Credenciais do Portal das Finanças (ver "Not yet confirmed") |

### Transmissão da Fatura Eletrónica B2G

**Transmissão da Fatura Eletrónica B2G**

| Canal | Detalhe |
| --- | --- |
| Rede Peppol | Através de um Access Point Peppol certificado |
| Formato | Peppol BIS Billing 3.0 (XML UBL 2.1) com CIUS-PT, conforme à norma europeia (CCP, art. 299.º-B, n.º 3) |
| Endpoint | Endpoint Peppol do adquirente registado no SMP |
| Autenticação | Certificados PKI Peppol |

### Fatura Eletrónica B2B a partir de 2027

- Até 31 de dezembro de 2026, uma fatura em PDF é considerada fatura eletrónica para todos os efeitos fiscais (Lei 73-A/2025, art. 95.º, n.º 3).
- Daí em diante aplica-se só o DL 28/2019, art. 12.º, n.º 2: considera-se garantida a autenticidade da origem e a integridade do conteúdo se for adotado, nomeadamente, um destes procedimentos: (a) assinatura eletrónica qualificada; (b) selo eletrónico qualificado nos termos do Regulamento (UE) 910/2014; (c) sistema EDI com acordo segundo o "Acordo tipo EDI europeu".
- Se o cliente envia faturas em PDF por email, a partir de 1 de janeiro de 2027 o PDF deixa de valer por si como fatura eletrónica. O cliente precisa de um procedimento que garanta a autenticidade e a integridade; os três que a lei dá como suficientes são a assinatura eletrónica qualificada, o selo eletrónico qualificado e o EDI (a lista do art. 12.º, n.º 2 diz "nomeadamente", ou seja não é fechada). A alternativa é a fatura em papel. O software de faturação tem ainda de garantir validação cronológica, não repúdio, não duplicação e verificação do certificado (DL 28/2019, art. 13.º).

### Registo de Séries

- **Registo de Séries**: antes de as usar, cada série de faturas e documentos fiscalmente relevantes é comunicada à AT, por meio de processamento (DL 28/2019, art. 35.º, n.º 1). A AT atribui a cada série um código de validação que integra o ATCUD (art. 35.º, n.º 2). A comunicação indica o identificador da série, o tipo de documento, o início da numeração e a data prevista de início de utilização (Portaria 195/2020, art. 2.º).

## Secção 6: Regras de Validação

### Validação do Lado da AT (SAF-T)

- **Validação do Lado da AT (SAF-T)**: validação de esquema face ao XSD em vigor do SAF-T(PT); unicidade do ATCUD; integridade da cadeia de hash; validação dos NIF face ao cadastro da AT; consistência das taxas de IVA com o espaço fiscal; numeração sequencial sem lacunas nem duplicados dentro da série; tipos de documento alinhados com a tabela do SAF-T. As regras exatas de validação da AT não foram relidas hoje (ver "Not yet confirmed").

### Verificações Pré-Submissão

- **Verificações Pré-Submissão**: ATCUD presente e no formato CódigoValidação-NúmeroSequencial; série comunicada e código de validação atribuído; dados do código QR iguais aos da fatura; cadeia de hash ininterrupta; número do certificado do programa válido; documentos anulados registados na base de dados (DL 28/2019, art. 7.º, n.º 5); documentos em modo de treino identificados como tal (art. 7.º, n.º 6); todos os campos obrigatórios preenchidos.

### Motivos Comuns de Rejeição

**Motivos Comuns de Rejeição**

| Motivo | Detalhe |
| --- | --- |
| ATCUD inválido | Código de validação não atribuído pela AT para a série |
| Cadeia de hash quebrada | Hash não referencia corretamente o documento anterior |
| NIF inválido | NIF do fornecedor ou do adquirente falha o dígito de controlo |
| Discrepância de taxa | A taxa de IVA não corresponde à taxa legal para os bens ou serviços e para o espaço fiscal |
| Campos em falta | Campos obrigatórios omitidos no XML do SAF-T |
| Não conformidade com o esquema | XML não conforme com o XSD em vigor do SAF-T(PT) |
| Submissão duplicada | Mesma fatura já comunicada num período anterior |

## Secção 7: Regras de Apuramento

### Taxas de IVA (2026)

**Taxas de IVA (2026)** _(continente: CIVA, art. 18.º, n.º 1; regiões autónomas: CIVA, art. 18.º, n.º 3, valores conforme `portugal-vat-return`)_

| Taxa | Continente (PT) | Açores (PT-AC) | Madeira (PT-MA) |
| --- | --- | --- | --- |
| Normal | 23% | 16% | 22% |
| Intermédia | 13% | 9% | 12% |
| Reduzida | 6% | 4% | 4% |
| Isenta | 0% | 0% | 0% |

A taxa reduzida da Madeira é 4% desde 1 de outubro de 2024 (o texto anterior desta skill indicava 5%), conforme a skill `portugal-vat-return`, que cita o Ofício Circulado 25045/2024 da AT.

### Regras de Arredondamento

- **Regras de Arredondamento**: a prática seguida nesta skill é calcular o IVA por linha, arredondar a 2 casas decimais e somar as linhas arredondadas para o total. O SAF-T(PT) exige base tributável e imposto separados por taxa e por espaço fiscal. A regra de arredondamento consta das especificações técnicas da AT, não relidas hoje (ver "Not yet confirmed").

### Tratamento de Faturas Multi-Taxa

- **Tratamento de Faturas Multi-Taxa**: quando a fatura tem bens ou serviços a taxas diferentes, a quantidade e denominação, o preço e o imposto indicam-se separadamente por taxa (CIVA, art. 36.º, n.º 5, parágrafo final). No código QR, os campos I1 a K8 permitem codificar até 8 combinações de taxa e espaço fiscal (ver "Not yet confirmed").

### Retenção na Fonte

- **Retenção na Fonte**: quando aplicável (por exemplo, serviços profissionais), a retenção na fonte é indicada separadamente. O código QR tem um campo próprio para o montante retido (ver "Not yet confirmed").

## Secção 8: Requisitos de Arquivo

**Requisitos de Arquivo**

| Requisito | Detalhe | Base |
| --- | --- | --- |
| Prazo de conservação | 10 anos, se outro prazo não resultar de disposição especial; mais tempo se a caducidade do imposto for mais longa | DL 28/2019, art. 19.º, n.os 1 e 2; CIVA, art. 52.º, n.º 1 |
| Faturas eletrónicas | Conservadas sem alterações, por ordem cronológica de emissão e receção, exclusivamente em formato eletrónico | DL 28/2019, art. 28.º, n.º 1 |
| Acessibilidade | Armazenamento seguro, legível e com controlos de integridade durante todo o prazo; exportação de cópias exatas para a AT | DL 28/2019, art. 19.º, n.º 3 |
| Migração | Permitida para novo suporte se o anterior ficar obsoleto ou houver risco para a legibilidade | DL 28/2019, art. 25.º, n.º 3 |
| Cópias de segurança | Obrigatórias, guardadas em local diferente dos originais | DL 28/2019, art. 27.º |
| Digitalização | Documentos em papel podem ser digitalizados; os originais só podem ser destruídos depois dos controlos e, nas faturas de compra, depois de exercido o direito à dedução | DL 28/2019, art. 23.º |
| Localização | Papel em Portugal; arquivo eletrónico em qualquer Estado membro da UE; fora da UE só com autorização prévia da AT; a localização é indicada na declaração de início ou de alterações | DL 28/2019, arts. 20.º e 21.º |
| SAF-T(PT) a pedido | Os sistemas têm de poder exportar o ficheiro de auditoria tributária | DL 28/2019, art. 11.º, n.º 5 |
| Integridade | Mensagens sem código executável ou macros | DL 28/2019, art. 29.º |
| Faturas com assinatura ou selo qualificado (a partir de 2027) | Arquivadas com a assinatura ou selo intactos e verificáveis | DL 28/2019, arts. 12.º e 28.º |

## Secção 9: Sanções por Incumprimento

**Sanções por Incumprimento** _(RGIT; limites para pessoas singulares. Para pessoas coletivas, os limites mínimo e máximo elevam-se para o dobro, art. 26.º, n.º 4)_

| Infração | Pessoas singulares (EUR) | Pessoas coletivas (EUR) | Base |
| --- | --- | --- | --- |
| Não emissão ou emissão fora de prazo de faturas ou recibos | 150 a 3 750 | 300 a 7 500 | RGIT, art. 123.º, n.º 1 |
| Não exigir fatura ou não a conservar pelo prazo legal | 75 a 2 000 | 150 a 4 000 | RGIT, art. 123.º, n.º 2 |
| Falta de utilização de programa de faturação certificado | 1 500 a 18 750 | 3 000 a 37 500 | RGIT, art. 128.º, n.º 2 |
| Uso de programa de faturação ou contabilidade que não cumpre os requisitos legais | 1 500 a 18 750 | 3 000 a 37 500 | RGIT, art. 128.º, n.º 3 |
| Criar ou ceder programas concebidos para alterar a situação tributária | 3 750 a 37 500 | Dobro, dentro dos máximos do art. 26.º, n.º 1 | RGIT, art. 128.º, n.º 1 |
| Falta ou atraso da comunicação dos elementos das faturas e do inventário (DL 198/2012, arts. 3.º e 3.º-A) | 200 a 10 000 (grave) | 400 a 20 000 | RGIT, art. 117.º, n.º 9 |
| Ficheiro SAF-T(PT) produzido fora do modelo legal | 250 a 5 000 (grave) | 500 a 10 000 | RGIT, art. 121.º, n.º 3 |
| Atraso na execução da contabilidade ou dos registos além do prazo da lei fiscal | 250 a 5 000 (grave) | 500 a 10 000 | RGIT, art. 121.º, n.º 2 |
| Inexistência de contabilidade organizada ou do modelo de exportação de ficheiros obrigatórios | 225 a 22 500 | 450 a 45 000 | RGIT, art. 120.º, n.º 1 |
| ATCUD ou código QR em falta | Ver "Not yet confirmed" | Ver "Not yet confirmed" | |

O art. 26.º, n.º 1 do RGIT limita as coimas de pessoas coletivas a EUR 165 000 (dolo) e EUR 45 000 (negligência), salvo regra em contrário; nas pessoas singulares, a metade (n.º 2). O texto anterior desta skill indicava "software não certificado EUR 3 000 a EUR 18 750", "ATCUD/QR em falta EUR 200 a EUR 1 000 por fatura", "falta de submissão do SAF-T até EUR 5 000" e "atrasos nos registos superiores a 90 dias até EUR 5 000": os valores certos são os da tabela; os dois últimos correspondem aos arts. 117.º, n.º 9 e 121.º, n.º 2.

Os fornecedores B2G que não cumpram o art. 299.º-B do CCP arriscam consequências no contrato público (ver "Not yet confirmed").

## Secção 10: Interação com Outras Skills Fiscais

### Comunicação das Faturas e Declaração Periódica de IVA

- **Comunicação das Faturas e Declaração Periódica de IVA**: os dados comunicados mensalmente cruzam com a declaração periódica de IVA (ver `portugal-vat-return`). O pré-preenchimento da declaração a partir do e-fatura não foi relido hoje (ver "Not yet confirmed").

### Deduções dos Consumidores no e-fatura

- **Deduções dos Consumidores no e-fatura**: as faturas com NIF do consumidor comunicadas à AT entram nas deduções à coleta do IRS; as despesas gerais familiares dão 35% com limite de EUR 250 por sujeito passivo (CIRS, art. 78.º-B, n.º 1). O consumidor pode comunicar faturas sem NIF pelo código QR ou pelo ATCUD (art. 78.º-B, n.º 3). Ver `pt-irs-employees-investment`.

### SAF-T(PT) da Contabilidade e IES

- **SAF-T(PT) da Contabilidade**: a entrega do ficheiro SAF-T(PT) da contabilidade (Portaria 31/2019) aplica-se aos períodos de 2027 e seguintes, a entregar em 2028 (Lei 73-A/2025, art. 95.º, n.º 2). Para a IES ver `portugal-financial-statements`. A regra antiga de que a AT valida o ficheiro em 10 dias antes da IES não foi confirmada hoje.

### Inventário

- **Comunicação do inventário** (DL 198/2012, art. 3.º-A, n.º 1): quem tem contabilidade organizada e está obrigado a inventário comunica à AT, até 31 de janeiro, o inventário do último dia do exercício anterior. Ficam dispensados de o valorizar: todos, no período iniciado em 2025; quem não esteja obrigado a inventário permanente, no período iniciado em 2026 (Lei 73-A/2025, art. 95.º, n.º 1).

### IRC e IRS

- **IRC e IRS**: os titulares de rendimentos da Categoria B estão sujeitos às obrigações de faturação, recibo e arquivo do CIVA e do DL 28/2019 (CIRS, art. 118.º, n.º 1, na redação do DL 28/2019); a escrituração e contabilidade em IRC seguem o mesmo decreto-lei (CIRC, art. 124.º, n.º 5). Os dados de faturação suportam o cruzamento com os rendimentos declarados.

### Pagamentos por Conta e Retenção na Fonte

- **Retenção na Fonte**: os dados de retenção na fonte indicados nas faturas cruzam com as declarações dos pagadores. O mecanismo de cruzamento não foi relido hoje.

## Sources

| Source | URL | Read on |
|---|---|---|
| Decreto-Lei 28/2019 (AT consolidated copy, with DL 48/2020 and DL 49/2025): arts. 2, 3, 4, 4-A, 7, 11, 12, 13, 19 to 30, 35, 43, 45 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Decreto_Lei_28_2019.pdf | 2026-10-30 |
| Decreto-Lei 198/2012 (AT consolidated copy, last change DL 85/2022): art. 3 (day 5, channels, data elements), art. 3-A (inventory) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Decreto-Lei%20n%20_198_2012_24_08.pdf | 2026-10-30 |
| Portaria 195/2020 (QR code and ATCUD) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Portaria_195_2020.pdf | 2026-10-30 |
| Lei 73-A/2025 (State Budget 2026), art. 95 (PDF until 31 Dec 2026, accounting SAF-T from 2027 periods, inventory valuation) and art. 260(2) (B2G SME regime to 31 Dec 2026) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Lei-73-A-2025.pdf | 2026-10-30 |
| Decreto-Lei 111-B/2017 (original DR text): CCP art. 299-B | https://files.diariodarepublica.pt/1s/2017/08/16802/0189402052.pdf | 2026-10-30 |
| Decreto-Lei 111-B/2017, consolidated (last change 2025-03-10): art. 9 transitional rule, n.os 1 to 5 | https://diariodarepublica.pt/dr/legislacao-consolidada/decreto-lei/2017-108086636 | 2026-10-30 |
| Decreto-Lei 28/2019, consolidated on the Diário da República (last change 2025-03-27): arts. 4 and 12 | https://diariodarepublica.pt/dr/legislacao-consolidada/decreto-lei/2019-119662485 | 2026-10-30 |
| Lei 73-A/2025 on the Diário da República: arts. 95 and 260 | https://diariodarepublica.pt/dr/detalhe/lei/73-a-2025-993270096 | 2026-10-30 |
| CIVA art. 36, invoice deadline and content | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/iva36.aspx | 2026-10-30 |
| CIVA art. 40, simplified invoices | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/iva40.aspx | 2026-10-30 |
| CIVA art. 52, 10-year retention | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/iva52.aspx | 2026-10-30 |
| CIVA art. 18, mainland VAT rates | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/iva18.aspx | 2026-10-30 |
| CIRS art. 78-B, general family expenses and invoices without NIF | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs78b.aspx | 2026-10-30 |
| RGIT art. 26, fines for companies doubled | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit26.aspx | 2026-10-30 |
| RGIT art. 117, late declarations and communications (n.º 9: invoice and inventory communications) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit117.aspx | 2026-10-30 |
| RGIT art. 120, no organised accounts or export model | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit120.aspx | 2026-10-30 |
| RGIT art. 121, accounting not to standards, delays, SAF-T file | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit121.aspx | 2026-10-30 |
| RGIT art. 123, invoices not issued or not kept | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit123.aspx | 2026-10-30 |
| RGIT art. 128, certified software | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit-artigo-128-ordm-ra2021_02.aspx | 2026-10-30 |

Not yet confirmed: whether the 2027 State Budget postpones again the end of PDF invoices, the accounting SAF-T or the B2G SME regime, so check before 1 January 2027 (the proposal, Proposta de Lei 110/XVII/2.ª, would accept PDF invoices until 31 December 2027 and move the accounting SAF-T to periods from 2028, delivered in 2029, according to the Ordem dos Contabilistas Certificados analysis; it is not law on 2026-10-30); the dates from which the QR code (old version: January 2022) and ATCUD (old version: January 2023) became enforceable in practice, which came from postponement despachos not read today; the AT technical specification for the QR code (field list I1 to K8, withholding field, 4-character hash) and the ATCUD form used inside the QR code and SAF-T; the hash-chain and printed-mention requirements of Portaria 363/2010; the CIUS-PT version string (2.1.1) and the Peppol identifiers; the B2G sanctions in public contracts; a fine of EUR 200 to EUR 1,000 per invoice for missing ATCUD or QR code (old version; no source found); AT validation rules and rounding rules for SAF-T(PT); the authentication method for invoice communication; the claim that the accounting SAF-T must be validated by AT within 10 days before the IES; prefilling of the VAT return from e-fatura data; the rules for foreign-currency invoices; the Azores and Madeira VAT rates are taken from `portugal-vat-return` and were not re-read today.

## Aviso Legal

Esta skill e os respectivos resultados são disponibilizados apenas para fins informativos e de cálculo, não constituindo aconselhamento fiscal, jurídico ou financeiro. A Open Accountants e os seus contribuidores não assumem qualquer responsabilidade por erros, omissões ou consequências decorrentes da utilização desta skill. Todos os resultados devem ser revistos e validados por um profissional qualificado (como um Contabilista Certificado, Revisor Oficial de Contas, advogado fiscalista ou equivalente licenciado na sua jurisdição) antes de serem entregues ou utilizados como base para qualquer actuação.

A versão mais atualizada desta skill é mantida em [openaccountants.com](https://openaccountants.com).

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
