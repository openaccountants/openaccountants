---
name: brazil-einvoice
description: Use esta skill sempre que for questionado sobre nota fiscal eletrônica no Brasil, NF-e (Nota Fiscal Eletrônica), NFS-e (Nota Fiscal de Serviço Eletrônica), NFC-e (Nota Fiscal de Consumidor Eletrônica), CT-e (Conhecimento de Transporte Eletrônico), MDF-e, SEFAZ (Secretaria da Fazenda), DANFE, chave de acesso, layout XML 4.00, certificado digital A1/A3, ICMS, IPI, PIS, COFINS, CBS, IBS, ou qualquer questão sobre geração, transmissão, validação ou troubleshooting de documentos fiscais eletrônicos brasileiros. Acione também ao orientar sobre integração SEFAZ, modos de contingência (EPEC, SVC), eventos (cancelamento, carta de correção), sistema nacional NFS-e (SNNFSe) e a Reforma Tributária 2026 (CBS/IBS). SEMPRE leia esta skill antes de tocar em qualquer trabalho de nota fiscal eletrônica do Brasil. — Use this skill whenever asked about Brazil e-invoicing (NF-e, NFS-e, NFC-e, CT-e, MDF-e), SEFAZ integration, XML 4.00 layout, ICP-Brasil certificates, ICMS/IPI/PIS/COFINS, or the 2026 CBS/IBS Tax Reform impact on electronic fiscal documents. ALWAYS read this skill before touching any Brazil e-invoice work.
version: 1.0
jurisdiction: BR
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Ariane Marrocos
review_status: current
depends_on:
  - einvoice-workflow-base
category: invoicing
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Brazil Einvoice

## Brasil — Notas Fiscais Eletrônicas e Coretax (NF-e/NFS-e/CT-e) — Skill v1.1

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **Ariane Marrocos** on 2026-06-03.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### Nota Fiscal Eletrônica

- **NF-e (modelo 55)** — Venda B2B de mercadorias, interestadual — SEFAZ  _(Ajuste SINIEF 07/2005)_
- **NFC-e (modelo 65)** — Varejo B2C ponto de venda — SEFAZ  _(Ajuste SINIEF 19/2016)_
- **NFS-e** — Serviços — municipal → SNNFSe nacional  _(LC 116/2003)_
- **CT-e** — Frete/transporte — SEFAZ  _(Ajuste SINIEF 09/2007)_
- **2026 (fase teste) — CBS+IBS** — CBS 0,9% + IBS 0,1% = 1% simbólico nos documentos  _(Emenda Constitucional nº 132/2023 Lei Complementar nº 214/2025 Nota Técnica 2025.002)_
- **2027 — CBS plena** — CBS plena; PIS/Cofins extintos dos campos da NF  _(LC 214/2025)_
- **2033 — ICMS/ISS extintos** — ICMS/ISS totalmente extintos dos documentos  _(Emenda Constitucional nº 132/2023 Lei Complementar nº 214/2025)_
- **ICP-Brasil A1** — Arquivo .pfx, validade 1 ano  _(ICP-Brasil)_
- **ICP-Brasil A3** — Certificado Digital ICP-Brasil A3: certificado armazenado em token criptográfico ou smart card, com validade definida pela Autoridade Certificadora, geralmente entre 1 e 5 anos.  _(ICP-Brasil)_
- **Assinatura** — XMLDSig enveloped, SHA-256  _(World Wide Web Consortium (W3C) ICP-Brasil Manual de Orientação do Contribuinte da NF-e)_
- **Composição** — 44 dígitos: UF(2) + AAMM(4) + CNPJ(14) + Modelo(2) + Série(3) + Número(9) + tpEmis(1) + Código(8) + DV(1)  _(Manual de Orientação do Contribuinte da NF-e Ajuste SINIEF 07/2005)_
- **Cancelamento (110111)** — Prazo definido pela legislação estadual (tradicionalmente 24 horas após autorização).  _(Ajuste SINIEF 07/2005; legislação da UF)_
- **Carta de Correção (110110)** — Correção de erros não financeiros e sem impacto tributário  _(Ajuste SINIEF 07/2005)_

## Seção 1 — Referência Rápida

**Referência Rápida**

| Campo | Valor |
| --- | --- |
| País | República Federativa do Brasil |
| Moeda | BRL (Real) |
| Sistema de Nota Fiscal Eletrônica | Multi-documento: NF-e, NFS-e, NFC-e, CT-e, MDF-e |
| Órgãos Reguladores | Federal: Receita Federal, ENCAT, CGNFS-e; Estadual: SEFAZ (26 estados + DF); Municipal: cada município |
| Principal Legislação | Constituição Federal Art. 150/155; Lei Complementar 87/96 (ICMS); LC 116/2003 (ISS); Ajuste SINIEF 07/2005; EC 132/2023; LC 214/2025; LC 227/2026; NT 2025.002 (Reforma Tributária CBS/IBS) |
| Padrão de Schema | XML proprietário (compatível com W3C); layout versão 4.00 |
| Namespace | http://www.portalfiscal.inf.br/nfe |
| Início da Implantação | 2006 (piloto); obrigatório universalmente desde 2014 |
| Status Atual | Plenamente operacional; em adaptação à Reforma Tributária (IBS/CBS a partir de 2026) |
| Portal | www.nfe.fazenda.gov.br (NF-e); www.gov.br/nfse (NFS-e Nacional) |

### Panorama dos Tipos de Documento

**Panorama dos Tipos de Documento**

| Documento | Nome Completo | Esfera | Caso de Uso |
| --- | --- | --- | --- |
| NF-e (modelo 55) | Nota Fiscal Eletrônica | Estadual (SEFAZ) | Venda B2B de mercadorias, operações interestaduais |
| NFC-e (modelo 65) | Nota Fiscal de Consumidor Eletrônica | Estadual (SEFAZ) | Varejo B2C ponto de venda |
| NFS-e | Nota Fiscal de Serviço Eletrônica | Municipal → Nacional (SNNFSe) | Serviços |
| CT-e | Conhecimento de Transporte Eletrônico | Estadual (SEFAZ) | Frete/transporte |
| MDF-e | Manifesto Eletrônico de Documentos Fiscais | Estadual (SEFAZ) | Manifesto de transporte |
| BP-e | Bilhete de Passagem Eletrônico | Estadual (SEFAZ) | Transporte de passageiros |
| GTV-e | Guia de Transporte de Valores Eletrônica | Estadual (SEFAZ) | Transporte de valores |

## Seção 2 — Reforma Tributária 2026: NF-e/NFS-e com CBS e IBS

### Visão Geral da Reforma

- **CBS/IBS/IS** — A Emenda Constitucional 132/2023, regulamentada pela Lei Complementar 214/2025 e complementada pela LC 227/2026, instituiu o novo modelo de tributação sobre o consumo no Brasil, criando dois tributos no padrão IVA dual: CBS (Contribuição sobre Bens e Serviços) — tributo federal que substituirá PIS e Cofins; IBS (Imposto sobre Bens e Serviços) — tributo estadual/municipal que substituirá ICMS e ISS; IS (Imposto Seletivo) — tributo federal sobre bens e serviços prejudiciais à saúde ou ao meio ambiente  _(Emenda Constitucional 132/2023; Lei Complementar 214/2025; LC 227/2026)_

### Marco Legal

**Marco Legal**

| Norma | Conteúdo |
| --- | --- |
| EC 132/2023 | Reforma constitucional que cria CBS, IBS e IS |
| LC 214/2025 | Lei Geral do IBS, CBS e IS — regras materiais |
| LC 227/2026 | Lei Complementar do Comitê Gestor do IBS e regras processuais |
| Ajuste SINIEF (a publicar 2026) | Layout dos novos campos nos documentos fiscais eletrônicos |
| Notas Técnicas SEFAZ 2026 | NT 2025.002 e suplementares — leiaute XML para CBS/IBS |

### Obrigatoriedade dos Novos Campos (2026)

- **Novos campos obrigatórios** — A partir de 1º de janeiro de 2026, todos os documentos fiscais eletrônicos devem incluir os novos campos de CBS e IBS: NF-e modelo 55 (mercadorias); NFS-e nacional (serviços, padrão unificado); NFC-e modelo 65 (consumidor final); CT-e (transporte de cargas); MDF-e (manifesto); BP-e e GTV-e (quando aplicável)  _(NT 2025.002)_

### Alíquotas 2026 — Fase de Teste

**Alíquotas 2026 — Fase de Teste**

| Tributo | Alíquota 2026 | Observação |
| --- | --- | --- |
| CBS | 0,9% | Alíquota simbólica federal |
| IBS | 0,1% | Alíquota simbólica estadual/municipal |
| **Total** | **1,0%** | Carga simbólica destinada apenas a testar layout e apurações |

- **Recolhimento efetivo 2026** — Em 2026, os contribuintes calculam, declaram e demonstram CBS e IBS nos documentos fiscais, mas não há recolhimento adicional efetivo — os valores podem ser compensados com PIS/Cofins na sistemática vigente.
- **Multas suspensas** — Multas suspensas por 3 meses após a publicação dos regulamentos finais, desde que o contribuinte demonstre boa-fé e cumpra com as obrigações acessórias mínimas.

### Layouts Atualizados — NF-e 4.00

- **Novos grupos XML CBS/IBS/IS** — A NT 2025.002 e suplementares introduzem novos grupos XML na NF-e versão 4.00: Grupo <CBS> por item (det/imposto/CBS); Grupo <IBS> por item (det/imposto/IBS), subdividido em <IBS> estadual e <IBS> municipal; Grupo <IS> por item (Imposto Seletivo), quando aplicável; Totais consolidados em total/IBSCBSTot; Novos códigos de CST específicos para CBS/IBS (em coexistência transitória com CST de ICMS/IPI/PIS/COFINS)  _(NT 2025.002)_

Exemplo (estrutura simplificada do grupo CBS/IBS por item):

```xml
<imposto>
  <ICMS>...</ICMS>
  <PIS>...</PIS>
  <COFINS>...</COFINS>
  <CBS>
    <CST>000</CST>
    <vBC>1000.00</vBC>
    <pCBS>0.9000</pCBS>
    <vCBS>9.00</vCBS>
  </CBS>
  <IBS>
    <IBSUF>
      <CST>000</CST>
      <vBC>1000.00</vBC>
      <pIBSUF>0.0500</pIBSUF>
      <vIBSUF>0.50</vIBSUF>
    </IBSUF>
    <IBSMun>
      <CST>000</CST>
      <vBC>1000.00</vBC>
      <pIBSMun>0.0500</pIBSMun>
      <vIBSMun>0.50</vIBSMun>
    </IBSMun>
  </IBS>
</imposto>
```

### NFS-e Padrão Nacional Unificado

- **NFS-e Padrão Nacional Unificado** — Padrão nacional consolidado conforme LC 175/2020 e o Convênio NFS-e (assinado entre Receita Federal, estados e municípios via CGNFS-e). A partir de 2026, o padrão nacional torna-se obrigatório em todos os municípios, com os campos de CBS e IBS embutidos nativamente. Os municípios que ainda operam sistemas próprios devem migrar para o Sistema Nacional NFS-e (SNNFSe) ou adotar layout compatível. A NFS-e nacional passa a ser o documento integrador entre prestador, tomador, município (IBS-Municipal) e União (CBS).  _(LC 175/2020)_

### Cronograma da Transição

**Cronograma da Transição**

| Ano | Fase |
| --- | --- |
| **2026** | Fase de teste — CBS 0,9% + IBS 0,1% simbólicos em todos os DF-e. Multas suspensas 3 meses. |
| **2027** | CBS plenamente vigente; PIS e Cofins **extintos** dos campos da NF; IPI praticamente extinto (alíquota zero, exceto bens da Zona Franca de Manaus e produtos sujeitos ao Imposto Seletivo). |
| **2028** | Continuação da CBS plena; ajustes de alíquotas; IBS permanece em alíquota de teste (0,1%). |
| **2029** | **IBS em cobrança gradual** — alíquotas estaduais/municipais aumentam progressivamente; ICMS e ISS reduzem proporcionalmente. |
| **2030–2032** | Transição contínua: IBS aumenta 10% ao ano; ICMS/ISS diminuem 10% ao ano. |
| **2033** | **ICMS e ISS totalmente extintos** dos documentos fiscais eletrônicos. CBS e IBS plenamente vigentes em alíquotas finais. |

### Implicações Operacionais Imediatas (2026)

1. Atualizar ERPs/emissores de DF-e para gerar os novos grupos <CBS> e <IBS> em todos os itens.
2. Cadastrar novos CSTs específicos de CBS/IBS no plano fiscal.
3. Validar parametrização de produtos (NCM) — a Reforma traz nova classificação para regimes diferenciados (alimentos da cesta básica, saúde, educação, transporte coletivo etc.).
4. Testar transmissão em homologação antes de 1º/jan/2026; SEFAZ disponibilizará ambiente de testes a partir do 2º semestre de 2025.
5. Treinar equipes — contabilidade, fiscal e TI — sobre a coexistência transitória dos dois sistemas (ICMS/ISS/PIS/COFINS + CBS/IBS) em 2026.

## Seção 3 — Escopo da Obrigatoriedade

### NF-e (Mercadorias) — Obrigatoriedade Universal

- **NF-e obrigatoriedade** — Todos os contribuintes que realizam comércio interestadual ou operações com mercadorias sujeitas ao ICMS. Sem limite de faturamento — obrigatória para praticamente todos os estabelecimentos comerciais/industriais. Obrigatória para: indústrias, atacadistas, importadores, exportadores. Cobertura: vendas, devoluções, transferências entre filiais, remessas, notas complementares/de ajuste

### NFC-e (Varejo B2C)

- **NFC-e características** — Substitui o antigo cupom fiscal em papel (ECF). Obrigatória para estabelecimentos varejistas (implantação faseada por estado; hoje universal). Formato simplificado; identificação do comprador é opcional para compras inferiores a BRL 200

### NFS-e (Serviços)

- **NFS-e características** — Historicamente emitida segundo regras municipais (cada um dos 5.570 municípios tinha sistema próprio). Sistema Nacional NFS-e (SNNFSe) lançado para emissão unificada. Em transição para uso obrigatório da plataforma SNNFSe com campos de CBS/IBS (Reforma 2026). Prestadores de serviço em todos os municípios devem atender ao padrão nacional

### Eventos do Documento

**Eventos do Documento**

| Evento | Código | Descrição |
| --- | --- | --- |
| Cancelamento | 110111 | Cancelamento em até 24 horas (7 dias em alguns estados) |
| Carta de Correção | 110110 | Carta de correção para erros não financeiros |
| Confirmação | 210200 | Destinatário confirma o recebimento |
| Desconhecimento | 210220 | Destinatário desconhece a operação |
| EPEC | 110140 | Registro prévio em contingência |

## Seção 4 — Formato Técnico

### Schema XML da NF-e (Layout 4.00)

**Schema XML da NF-e (Layout 4.00)**

| Aspecto | Detalhe |
| --- | --- |
| Formato | XML |
| Versão do Layout | 4.00 (vigente desde 2019; mantida na Reforma 2026 com extensões CBS/IBS) |
| Elemento Raiz (lote) | `<enviNFe>` |
| Elemento Raiz (NF-e unitária) | `<NFe>` contendo `<infNFe>` |
| Namespace | http://www.portalfiscal.inf.br/nfe |
| Namespace da Assinatura Digital | http://www.w3.org/2000/09/xmldsig# |
| Arquivos de Schema | enviNFe_v4.00.xsd, leiauteNFe_v4.00.xsd, etc. |
| Codificação | UTF-8 |
| Padrão de Assinatura | XMLDSig (enveloped) com certificado ICP-Brasil |

### Chave de Acesso — 44 Dígitos

**Chave de Acesso — 44 Dígitos**

| Posição | Dígitos | Conteúdo |
| --- | --- | --- |
| 1-2 | 2 | Código da UF (IBGE) |
| 3-6 | 4 | Ano/Mês (AAMM) |
| 7-20 | 14 | CNPJ do emitente |
| 21-22 | 2 | Modelo (55=NF-e, 65=NFC-e) |
| 23-25 | 3 | Série |
| 26-34 | 9 | Número da NF-e |
| 35 | 1 | Tipo de emissão (tpEmis) |
| 36-43 | 8 | Código numérico (aleatório) |
| 44 | 1 | Dígito verificador (mod 11) |

### Requisitos de Certificado Digital

**Requisitos de Certificado Digital**

| Tipo | Descrição |
| --- | --- |
| ICP-Brasil A1 | Certificado em software (arquivo .pfx); validade de 1 ano |
| ICP-Brasil A3 | Certificado em hardware (smart card/token); validade de 3 anos |
| Assinatura | XMLDSig enveloped; SHA-256 recomendado |
| Certificado no XML | Elemento X509Certificate dentro de `<Signature>` |

## Seção 5 — Campos Obrigatórios

### Identificação (ide)

**Identificação (ide)**

| Tag | Descrição | Exemplo |
| --- | --- | --- |
| cUF | Código da UF (IBGE) | 35 (São Paulo) |
| cNF | Código aleatório de 8 dígitos | 12345678 |
| natOp | Natureza da operação | "Venda de mercadoria" |
| mod | Modelo | 55 |
| serie | Série | 1 |
| nNF | Número da NF-e | 000000001 |
| dhEmi | Data/hora de emissão | 2026-05-22T14:30:00-03:00 |
| tpNF | Tipo (0=entrada, 1=saída) | 1 |
| idDest | Destino (1=interna, 2=interestadual, 3=exportação) | 2 |
| cMunFG | Código do município (IBGE) do fato gerador | 3550308 |
| tpImp | Formato de impressão do DANFE | 1 (retrato) |
| tpEmis | Tipo de emissão | 1 (normal) |
| tpAmb | Ambiente (1=produção, 2=homologação) | 1 |
| finNFe | Finalidade (1=normal, 2=complementar, 3=ajuste, 4=devolução) | 1 |
| indFinal | Consumidor final (0=não, 1=sim) | 0 |
| indPres | Indicador de presença | 1 (presencial) |

### Emitente (emit)

**Emitente (emit)**

| Tag | Descrição |
| --- | --- |
| CNPJ | CNPJ de 14 dígitos |
| xNome | Razão social |
| xFant | Nome fantasia |
| IE | Inscrição Estadual |
| CRT | Regime tributário (1=Simples Nacional, 2=SN excesso de sublimite, 3=Normal) |
| enderEmit | Endereço completo (xLgr, nro, xBairro, cMun, UF, CEP) |

### Destinatário (dest)

**Destinatário (dest)**

| Tag | Descrição |
| --- | --- |
| CNPJ ou CPF | Identificação fiscal do destinatário |
| xNome | Nome |
| indIEDest | Indicador de IE (1=contribuinte de ICMS, 2=isento, 9=não contribuinte) |
| IE | Inscrição Estadual (se contribuinte) |
| enderDest | Endereço completo |

### Produtos (det/prod)

**Produtos (det/prod)**

| Tag | Descrição |
| --- | --- |
| cProd | Código interno do produto |
| cEAN | Código de barras GTIN (ou "SEM GTIN") |
| xProd | Descrição do produto |
| NCM | Nomenclatura Comum do Mercosul (8 dígitos) |
| CFOP | Código Fiscal de Operações e Prestações (4 dígitos) |
| uCom | Unidade comercial |
| qCom | Quantidade comercial |
| vUnCom | Valor unitário comercial |
| vProd | Valor total do produto (qCom × vUnCom) |
| cEANTrib | GTIN da unidade tributável |
| uTrib | Unidade tributável |
| qTrib | Quantidade tributável |
| vUnTrib | Valor unitário tributável |

### Tributos (det/imposto)

**Tributos (det/imposto)**

| Grupo de Tributo | Tags | Descrição |
| --- | --- | --- |
| ICMS | orig, CST/CSOSN, modBC, vBC, pICMS, vICMS | Imposto estadual sobre circulação de mercadorias |
| IPI | CST, vBC, pIPI, vIPI | Imposto federal sobre produtos industrializados |
| PIS | CST, vBC, pPIS, vPIS | Contribuição federal social |
| COFINS | CST, vBC, pCOFINS, vCOFINS | Contribuição federal social |
| **CBS** (2026+) | **CST, vBC, pCBS, vCBS** | **Contribuição sobre Bens e Serviços (Reforma)** |
| **IBS** (2026+) | **CST, vBC, pIBSUF, vIBSUF, pIBSMun, vIBSMun** | **Imposto sobre Bens e Serviços — UF e Município (Reforma)** |
| **IS** (2027+) | **CST, vBC, pIS, vIS** | **Imposto Seletivo (quando aplicável)** |

### Totais (total/ICMSTot e total/IBSCBSTot)

**Totais**

| Tag | Descrição |
| --- | --- |
| vBC | Base de cálculo total do ICMS |
| vICMS | Total de ICMS |
| vProd | Total de produtos |
| vFrete | Total de frete |
| vSeg | Total de seguro |
| vDesc | Total de descontos |
| vIPI | Total de IPI |
| vPIS | Total de PIS |
| vCOFINS | Total de COFINS |
| **vCBS** (2026+) | **Total de CBS** |
| **vIBS** (2026+) | **Total de IBS (UF + Município)** |
| **vIS** (2027+) | **Total de IS** |
| vNF | Valor total da NF-e |

## Seção 6 — Método de Transmissão

### Web Services da SEFAZ

**Web Services da SEFAZ**

| Serviço | Ação WSDL | Finalidade |
| --- | --- | --- |
| NfeAutorizacao | NfeAutorizacaoLote | Submeter lote de NF-e para autorização |
| NfeRetAutorizacao | NfeRetAutorizacaoLote | Consultar resultado da autorização |
| NfeConsultaProtocolo | NfeConsulta | Consultar status de uma NF-e |
| NfeInutilizacao | NfeInutilizacao | Inutilizar faixa de numeração |
| RecepcaoEvento | NfeRecepcaoEvento | Submeter eventos (cancelamento, correção etc.) |
| NfeStatusServico | NfeStatusServico | Verificar disponibilidade da SEFAZ |
| NfeDistribuicaoDFe | NFeDistribuicaoDFe | Baixar DF-e endereçados ao contribuinte |

### Ambientes SEFAZ

**Ambientes SEFAZ**

| Ambiente | Padrão de URL | Finalidade |
| --- | --- | --- |
| Produção | https://nfe.sefaz{UF}.{domain}/... | Transações reais |
| Homologação | https://homologacao.nfe.sefaz{UF}.{domain}/... | Testes |

### SEFAZ Virtual (SVRS / SVC)

- **SEFAZ Virtual** — Estados que não hospedam SEFAZ própria utilizam a SVRS (Sefaz Virtual RS) ou a SVAN (Sefaz Virtual AN). Modos de contingência: SVC-AN, SVC-RS (quando a SEFAZ primária está indisponível). EPEC: Evento Prévio de Emissão em Contingência (registro prévio offline)

### Fluxo de Autorização

1. Gerar o XML da NF-e (todos os campos obrigatórios, incluindo CBS/IBS a partir de 2026)
2. Assinar o XML com certificado ICP-Brasil (XMLDSig enveloped)
3. Submeter à SEFAZ pelo web service NfeAutorizacao (síncrono ou em lote)
4. SEFAZ valida schema, regras de negócio e assinatura digital
5. SEFAZ retorna o protocolo de autorização com código de status
6. Embarcar o protocolo de autorização no XML da NF-e (`nfeProc`) → documento juridicamente válido
7. Gerar o DANFE (documento auxiliar impresso) para acompanhar o transporte
8. Entregar o XML ao destinatário em até 24 horas

## Seção 7 — Regras de Validação

### Camadas de Validação da SEFAZ

- **Camadas de Validação** — 1. Validação de schema — XML conforme leiauteNFe_v4.00.xsd 2. Assinatura digital — Certificado ICP-Brasil válido; assinatura matematicamente correta 3. Regras de negócio — Mais de 900 regras definidas nas Notas Técnicas 4. Cálculo tributário — Valores de ICMS, IPI, PIS, COFINS (e a partir de 2026, CBS e IBS) verificados contra alíquotas e bases 5. Validação cadastral — CNPJ/IE devem estar ativos no cadastro da SEFAZ 6. Validação de GTIN — Código de barras deve existir no CCG (Cadastro Centralizado de GTINs) 7. Checagem de duplicidade — A mesma chave de acesso não pode ser autorizada duas vezes

### Códigos Comuns de Rejeição

**Códigos Comuns de Rejeição**

| Código | Descrição | Correção |
| --- | --- | --- |
| 204 | NF-e duplicada (mesma chave de acesso) | Usar novo nNF ou cNF |
| 215 | Erro de validação de schema | Corrigir a estrutura XML conforme o XSD |
| 225 | UF de destino inválida para o CFOP | Alinhar CFOP com idDest |
| 301 | Uso irregular da IE | Verificar se a IE está ativa na UF de destino |
| 539 | NF-e duplicada (conteúdo duplicado) | Revisar a sequência numérica da NF-e |
| 611 | GTIN não encontrado no CCG | Cadastrar o GTIN do produto ou usar "SEM GTIN" |
| 778 | NCM incompatível com o CFOP | Verificar alinhamento NCM-CFOP |

### Códigos de Status de Autorização

**Códigos de Status de Autorização**

| Código | Significado |
| --- | --- |
| 100 | Autorizado |
| 101 | Cancelamento autorizado |
| 110 | Uso denegado (registrado mas não autorizado) |
| 135 | Evento registrado |
| 301-999 | Diversos códigos de rejeição |

## Seção 8 — Regras de Cálculo Tributário

### ICMS (Tributo Estadual)

- **ICMS regras** — Alíquotas variam por estado e produto (7%, 12%, 17%, 18%, 19%, 20%, 25% são as mais comuns). Alíquotas interestaduais: 4% (mercadorias importadas), 7% (origens Sul/Sudeste → demais regiões), 12% (demais combinações). ICMS-ST (substituição tributária): tributo recolhido antecipadamente pelo fabricante/importador. DIFAL: diferencial de alíquota para operações interestaduais B2C ao consumidor final

### IPI (Imposto Federal sobre Produtos Industrializados)

- **IPI regras** — Aplicado sobre bens industrializados/importados. Alíquotas de 0% a 365% conforme o produto (tabela TIPI). Empresas do Simples Nacional geralmente não tomam crédito de IPI

### PIS/COFINS (Contribuições Sociais Federais)

**PIS/COFINS (Contribuições Sociais Federais)**

| Regime | Alíquota PIS | Alíquota COFINS | Método |
| --- | --- | --- | --- |
| Cumulativo (lucro presumido) | 0,65% | 3,00% | Sobre a receita bruta, sem créditos |
| Não cumulativo (lucro real) | 1,65% | 7,60% | Sobre a receita menos créditos |

### Reforma Tributária (IBS/CBS) — A Partir de 2026

- **Reforma Tributária IBS/CBS** — A NT 2025.002 e Notas Técnicas SEFAZ a serem publicadas em 2026 introduzem novos grupos XML para IBS (estadual/municipal) e CBS (federal). Período de transição: IBS/CBS coexistem com ICMS/ISS/PIS/COFINS até a substituição plena em 2033. Novos campos no XML da NF-e para os valores de IBS e CBS (por item e nos totais). Em 2026, alíquotas simbólicas (CBS 0,9% + IBS 0,1%) servem para testar o sistema; multas suspensas por 3 meses  _(NT 2025.002)_

### Regras de Arredondamento

- **Arredondamento** — Valores monetários: 2 casas decimais. Quantidades: até 4 casas decimais. Preços unitários: até 10 casas decimais. Alíquotas: até 4 casas decimais. Tolerância em totais tributários: BRL 0,01 por grupo de tributo

## Seção 9 — Requisitos de Guarda

**Requisitos de Guarda**

| Requisito | Detalhe |
| --- | --- |
| Período de Guarda | Mínimo de 5 anos a contar do primeiro dia do exercício seguinte (decadência tributária) |
| Formato | XML autorizado original (com o protocolo de autorização embarcado) |
| Obrigação do Destinatário | Deve armazenar o XML da NF-e recebida pelo mesmo período |
| DANFE | Não substitui o XML; impresso apenas para acompanhar o transporte |
| Eventos | Todos os eventos (cancelamento, cartas de correção) devem ser arquivados em conjunto |
| Assinatura Digital | Preservada dentro do XML; não há arquivo de assinatura separado |
| Acesso | Deve ser apresentável sob demanda em fiscalização (SEFAZ ou Receita Federal) |
| Backup | Recomenda-se armazenamento redundante; a SEFAZ mantém cópia, mas o contribuinte permanece responsável |

## Seção 10 — Penalidades por Não Conformidade

**Penalidades por Não Conformidade**

| Infração | Penalidade |
| --- | --- |
| Operar sem NF-e quando obrigatória | 1% do valor da operação (mínimo BRL 500) por documento; varia por estado |
| Emitir NF-e com dados incorretos | Multa varia por estado (tipicamente 1% do valor da NF-e) |
| Não transmitir a NF-e à SEFAZ | Apreensão das mercadorias durante o transporte + multa |
| Transportar mercadorias sem DANFE | Apreensão das mercadorias + multa (regulamento estadual) |
| Não entregar XML ao destinatário | Multa administrativa + destinatário não pode tomar créditos |
| Cancelamento extemporâneo | Multa; o cancelamento pode ser negado após o prazo |
| Operar com certificado revogado/expirado | Rejeição da NF-e; impossibilidade de operar |

### Faixas de Multa por Estado (Exemplos)

**Faixas de Multa por Estado (Exemplos)**

| Estado | Multa Típica por NF-e Ausente |
| --- | --- |
| São Paulo (SP) | 50% do valor da operação (vinculada ao ICMS) |
| Minas Gerais (MG) | 40% do valor da operação |
| Rio de Janeiro (RJ) | Mínimo de 5 UFIR-RJ por documento |
| Paraná (PR) | 30% do valor da operação |

As penalidades se acumulam quando múltiplas infrações ocorrem no mesmo período fiscalizado.

### Penalidades Específicas para a Reforma 2026

- **Multas suspensas / descumprimento** — Multas suspensas por 3 meses após a publicação dos regulamentos finais para erros relativos aos novos campos de CBS/IBS, desde que o contribuinte demonstre boa-fé e cumpra as obrigações acessórias mínimas. A não inclusão dos campos de CBS/IBS após o término do período de tolerância caracteriza descumprimento de obrigação acessória, sujeita à multa prevista na LC 214/2025.  _(LC 214/2025)_

## Seção 11 — Interação com Outras Skills Tributárias

### SPED Fiscal (EFD ICMS/IPI)

- **SPED Fiscal** — Obrigação acessória mensal de escrituração digital que referencia todas as NF-e emitidas/recebidas. Bloco C (mercadorias) alimentado a partir dos dados do XML da NF-e. Validação cruzada: lançamentos do SPED devem coincidir exatamente com os registros de NF-e autorizadas pela SEFAZ. Divergências disparam notificações automáticas de fiscalização

### EFD-Contribuições (PIS/COFINS)

- **EFD-Contribuições** — Escrituração digital federal de PIS/COFINS. Detalhe linha a linha da NF-e alimenta o cálculo de créditos/débitos. Códigos CST na NF-e determinam o tratamento de PIS/COFINS na EFD. A partir de 2027, com a extinção de PIS/Cofins, a EFD-Contribuições será adaptada ou substituída pela apuração consolidada da CBS

### SPED ECD / ECF (Contabilidade / Tributo sobre o Lucro)

- **SPED ECD/ECF** — A receita reconhecida nos livros contábeis deve estar alinhada à emissão das NF-e. A Receita Federal cruza as declarações ECF com os dados agregados das NF-e

### NFS-e → Apuração do ISS / IBS

- **NFS-e apuração ISS/IBS** — Os dados da NFS-e alimentam a apuração municipal do ISS (Imposto Sobre Serviços). Com o SNNFSe (Sistema Nacional NFS-e), os dados fluirão para o cálculo do IBS-Municipal na Reforma. Em 2033, o ISS é extinto; o IBS-Municipal é apurado integralmente a partir da NFS-e nacional

### DCTF / DARF

- **DCTF/DARF** — Pagamentos de tributos federais (IPI, PIS, COFINS) reconciliados com obrigações derivadas das NF-e. Na Reforma Tributária: a CBS substitui PIS/COFINS, com dados originários da NF-e/NFS-e. A apuração da CBS migrará para a DCTFWeb ou para uma nova declaração específica do Comitê Gestor

### Importação/Exportação (DI/DUE)

- **Importação/Exportação** — NF-e de exportação vinculada à DU-E (Declaração Única de Exportação). NF-e de importação referencia o número da DI (Declaração de Importação). CFOPs 3.xxx (importações) e 7.xxx (exportações) se vinculam à documentação aduaneira

## Aviso Legal

Esta skill e suas saídas são fornecidas apenas para fins informativos e computacionais e não constituem aconselhamento tributário, jurídico ou financeiro. A Open Accountants e seus colaboradores não se responsabilizam por quaisquer erros, omissões ou resultados decorrentes do uso desta skill. Toda saída deve ser revisada e validada por um profissional qualificado (Contador registrado no CRC ou profissional licenciado equivalente em sua jurisdição) antes da entrega ou ato fiscal.

A versão mais atualizada e verificada desta skill é mantida em [openaccountants.com](https://openaccountants.com).

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
