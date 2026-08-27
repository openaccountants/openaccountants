---
name: portugal-einvoice
description: "Utilize esta skill sempre que lhe forem colocadas questões sobre facturação electrónica em Portugal, códigos ATCUD, comunicação do SAF-T(PT), requisitos do QR Code nas facturas, software certificado AT (Portaria/Modelo 24), portal e-fatura, Assinatura Electrónica Qualificada (AEQ) para facturas, CIUS-PT, facturação electrónica B2G via Peppol/FE-AP, ou qualquer questão relativa à emissão, transmissão, validação ou arquivo de facturas electrónicas ao abrigo da lei portuguesa. Trigger also on: \"ATCUD\", \"SAF-T Portugal\", \"e-fatura\", \"QR code invoice\", \"certified software AT\", \"Peppol Portugal\", \"B2G e-invoice\", \"invoice hash chain\", \"Portaria 363/2010\", \"Decreto-Lei 28/2019\", or \"Qualified Electronic Signature Portugal\". LEIA SEMPRE esta skill antes de tocar em qualquer trabalho de conformidade de facturação em Portugal."
version: 1.0
jurisdiction: PT
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Mário Jorge da costa Vale
review_status: current
depends_on:
  - einvoice-workflow-base
category: invoicing
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Portugal Einvoice

## Portugal — Facturação Electrónica (ATCUD / SAF-T(PT) / e-Fatura) — Skill v1.1

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **Mário Jorge da costa Vale** on 2026-06-04.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### Faturação Eletrónica

- **QR codes obrigatórios** — Janeiro 2022  _(Portaria 195/2020)_
- **ATCUD obrigatório** — Janeiro 2023  _(DL 28/2019)_
- **B2G e-fatura (todas as entidades)** — Janeiro 2024  _(DL 111-B/2017)_
- **QES em faturas PDF** — Janeiro 2027  _(DL 28/2019)_
- **SAF-T Contabilidade** — Esta portaria entrou em vigor em 2017  _(dispõe sobre a obrigatoriedade de disponibilizar o SAF-T-Contabilidade, se solicitado)_
- **Prazo de entrega** — Até ao 5.º dia do mês seguinte  _(DL 28/2019)_
- **Não emissão de faturas** — €150–€3.750 (PF) / €300–€7.500 (PJ)  _(RGIT)_
- **Software não certificado** — €3.000–€18.750  _(RGIT)_
- **ATCUD/QR em falta** — €200–€1.000 por fatura  _(RGIT)_

## Secção 1 -- Referência Rápida

**Referência Rápida**

| Campo | Valor |
| --- | --- |
| País | Portugal (República Portuguesa) |
| Moeda | EUR |
| Nome do sistema de facturação electrónica | e-fatura (portal de comunicação) + enquadramento ATCUD/QR Code |
| Entidade reguladora | Autoridade Tributária e Aduaneira (AT) |
| Legislação principal | Decreto-Lei 28/2019; Portaria 363/2010 (certificação de software); Portaria 321-A/2007 (SAF-T); Portaria 195/2020 (especificações do QR Code); RGIT (sanções) |
| Calendário de implementação | QR Code obrigatório desde Janeiro de 2022; ATCUD obrigatório desde Janeiro de 2023; facturação electrónica B2G desde Janeiro de 2024 para todas as entidades; AEQ para facturas em PDF desde Janeiro de 2027; SAF-T da Contabilidade em 2028 (período de tributação 2027) |
| Estado actual (2026) | ATCUD e QR Code totalmente em vigor; SAF-T(PT) de Facturação mensal activo; B2G via Peppol/CIUS-PT; B2B ainda não obrigatório como factura electrónica estruturada; AEQ obrigatória a partir de Janeiro de 2027 |
| Versão da skill | 1.1 |

## Secção 2 -- Âmbito da Obrigação

### Quem Deve Cumprir

- **B2G (Empresa para Estado)** — Todos os fornecedores de entidades públicas portuguesas devem emitir facturas electrónicas estruturadas via Peppol (CIUS-PT / Peppol BIS Billing 3.0). Obrigatório para grandes empresas desde 2021, alargado a PME e micro-empresas a partir de 1 de Janeiro de 2024.
- **B2B (Empresa para Empresa)** — Portugal não impõe actualmente a troca de facturas electrónicas estruturadas entre entidades privadas. Em vez disso, a conformidade é assegurada através de um enquadramento por camadas: (1) software certificado AT, (2) códigos únicos de documento ATCUD, (3) QR Code em todas as facturas, e (4) comunicação mensal do SAF-T(PT) de Facturação à AT. Isto confere à AT visibilidade em tempo quase real sem exigir a troca directa de facturas electrónicas B2B.
- **B2C (Empresa para Consumidor)** — Idêntico ao B2B -- as facturas (incluindo facturas-recibo) devem incluir ATCUD e QR Code, ser emitidas através de software certificado AT, e ser comunicadas no SAF-T(PT) de Facturação. Os consumidores podem verificar as facturas no portal e-fatura para efeitos de deduções pessoais em sede de IRS.

### Limiares e Isenções

- **Limiar de volume de negócios geral** — Sem limiar de volume de negócios -- todos os sujeitos passivos que efectuem operações tributáveis em sede de IVA em Portugal devem cumprir.
- **Obrigação de software certificado AT** — Aplica-se a sujeitos passivos com volume de negócios superior a 50 000 EUR; empresas não residentes com registo de IVA em Portugal também devem utilizar software certificado AT (desde 2021).
- **Facturas simplificadas** — Até 100 EUR, ou até 1 000 EUR em determinados sectores, continuam a exigir ATCUD e QR Code.

### Fases do Calendário

**Fases do Calendário**

| Data | Marco |
| --- | --- |
| Janeiro de 2020 | Enquadramento de certificação de software AT ao abrigo da Portaria 363/2010 |
| Janeiro de 2022 | QR Code obrigatório em todos os documentos fiscalmente relevantes |
| Janeiro de 2023 | ATCUD obrigatório em todas as facturas e documentos fiscalmente relevantes |
| Janeiro de 2024 | Facturação electrónica B2G obrigatória para todas as entidades (incluindo PME e micro) |
| Janeiro de 2025 | Prazo do SAF-T(PT) de Facturação mensal (até dia 5) rigorosamente aplicado |
| Janeiro de 2027 | AEQ obrigatória em todas as facturas em PDF; PDFs sem AEQ deixam de ter validade legal |
| 2028 | Primeiro SAF-T(PT) da Contabilidade obrigatório (período de tributação 2027) |

## Secção 3 -- Formato Técnico

### Normas de Formato da Factura

- **B2G** — XML em UBL 2.1 via CIUS-PT (Core Invoice Usage Specification for Portugal), alinhado com a norma EN 16931. Transmitido na rede Peppol utilizando Peppol BIS Billing 3.0, através da FE-AP (Facturação Electrónica na Administração Pública).
- **B2B/B2C** — Não existe um formato XML estruturado de troca obrigatório. As facturas podem ser emitidas em PDF, papel ou outros formatos, desde que sejam geradas por software certificado AT e contenham ATCUD + QR Code. Os dados da factura são comunicados à AT via SAF-T(PT) em XML.

### Esquema do SAF-T(PT)

- **Estrutura XML** — Estrutura XML definida pela Portaria 321-A/2007 (actualizada periodicamente).  _(Portaria 321-A/2007)_
- **SAF-T(PT) de Facturação - conteúdo** — Contém: Header, Customer, TaxTable, Payments, Supplier, Product, SalesInvoices, MovementOfGoods, WorkingDocuments.
- **SAF-T(PT) da Contabilidade - conteúdo** — Contém: Header, Customer, TaxTable, Payments, GeneralLedgerAccounts, Supplier, GeneralLedgerEntries, FixedAssets, Inventory.

### Estrutura do ATCUD

- **Formato ATCUD** — Formato: `ATCUD:CódigoValidação-NúmeroSequencial`. O código de validação é obtido junto da AT no momento do registo de uma série documental. O número sequencial é atribuído pelo software certificado. Exemplo: `ATCUD:TES123TE-4561`. No QR Code e no XML do SAF-T(PT) apenas é utilizado `TES123TE-4561` (sem o prefixo `ATCUD:`).

### Especificação do QR Code

- **Conteúdo do QR Code** — Definida pela Portaria 195/2020. O QR Code codifica: NIF do emitente, NIF do adquirente, país do adquirente; Tipo de documento, estado do documento, data do documento, identificador único do documento, ATCUD; Espaço fiscal, base tributável e montantes de imposto por taxa de IVA (campos I1-I8, J1-J8, K1-K8 para os espaços fiscais PT, PT-AC, PT-MA); Total bruto, montante de retenção na fonte, hash (hash de 4 caracteres da assinatura RSA).  _(Portaria 195/2020)_

### Cadeia de Hash (Assinatura Digital RSA)

- **Cadeia de hash** — Cada factura emitida por software certificado inclui um hash de assinatura digital RSA. A cadeia de hash liga cada factura à anterior, garantindo a inviolabilidade. Os primeiros 4 caracteres do hash devem aparecer na factura impressa ou em PDF.

## Secção 4 -- Campos Obrigatórios

### Campos Exigidos em Todas as Facturas Portuguesas

**Campos Exigidos em Todas as Facturas Portuguesas**

| Campo | Descrição |
| --- | --- |
| NIF do emitente | Número de identificação fiscal português do fornecedor |
| Nome e morada do emitente | Denominação social completa e sede registada |
| NIF do adquirente | Obrigatório em B2B; "consumidor final" para B2C abaixo de 1 000 EUR |
| Nome e morada do adquirente | Obrigatórios quando é fornecido o NIF |
| Número da factura | Sequencial, único dentro da série (formato: CódigoTipo SérieID/NúmeroSequencial) |
| Data da factura | Data de emissão |
| ATCUD | Código único do documento (CódigoValidação-NúmeroSequencial) |
| QR Code | Código de barras 2D que codifica os dados da factura nos termos da Portaria 195/2020 |
| Hash (4 caracteres) | Primeiros 4 caracteres do hash da assinatura RSA |
| Número do software certificado | Número de certificação AT do programa de facturação |
| Data da operação | Data da entrega de bens / prestação de serviços |
| Descrição dos bens/serviços | Detalhe ao nível da linha |
| Quantidade e preço unitário | Por linha |
| Taxa e montante de IVA | Por taxa aplicável, por espaço fiscal (PT, PT-AC, PT-MA) |
| Total da base tributável | Soma de todas as linhas antes de IVA |
| Total do IVA | Soma do IVA em todas as taxas |
| Total bruto | Incluindo IVA |
| Moeda | EUR no mercado interno; moeda estrangeira com taxa de câmbio para EUR em operações transfronteiriças |
| Condições/forma de pagamento | Se aplicável |

### Campos Adicionais B2G (CIUS-PT / Peppol BIS 3.0)

**Campos Adicionais B2G (CIUS-PT / Peppol BIS 3.0)**

| Campo | Caminho (UBL 2.1) |
| --- | --- |
| Referência do adquirente | `cbc:BuyerReference` |
| Referência do contrato | `cac:ContractDocumentReference/cbc:ID` |
| Referência da encomenda | `cac:OrderReference/cbc:ID` |
| CustomizationID CIUS-PT | `cbc:CustomizationID` = `urn:cen.eu:en16931:2017#compliant#urn:feap.gov.pt:CIUS-PT:2.1.1` |
| Profile ID | `cbc:ProfileID` = `urn:fdc:peppol.eu:2017:poacc:billing:01:1.0` |
| Endpoint ID (Peppol) | `cbc:EndpointID` com identificador de esquema |

## Secção 5 -- Método de Transmissão

### Submissão do SAF-T(PT) de Facturação (B2B/B2C)

**Submissão do SAF-T(PT) de Facturação (B2B/B2C)**

| Canal | Detalhe |
| --- | --- |
| Webservice e-fatura | API SOAP/REST para submissão automatizada |
| Ferramenta de linha de comando | CLI disponibilizada pela AT para envios em lote |
| Portal das Finanças | Carregamento manual do ficheiro (XML) |
| Inserção directa | Emitentes de baixo volume podem introduzir manualmente os dados das facturas no portal |
| Prazo | Até ao dia 5 do mês seguinte ao do período de comunicação |
| Autenticação | Certificado digital (qualificado ou emitido pela AT) |

### Transmissão da Factura Electrónica B2G

**Transmissão da Factura Electrónica B2G**

| Canal | Detalhe |
| --- | --- |
| Rede Peppol | Através de um Access Point Peppol certificado |
| Formato | Peppol BIS Billing 3.0 (XML UBL 2.1) com CIUS-PT |
| Endpoint | Endpoint Peppol do adquirente registado no SMP |
| Autenticação | Certificados PKI Peppol |

### Registo de Séries

- **Registo de Séries** — Antes da emissão de facturas, cada série documental deve ser registada junto da AT no Portal das Finanças, a fim de obter o código de validação utilizado na geração do ATCUD.

## Secção 6 -- Regras de Validação

### Validação do Lado da AT (SAF-T)

- **Validação do Lado da AT (SAF-T)** — Validação de esquema face ao XSD em vigor do SAF-T(PT); Verificações cruzadas: unicidade do ATCUD, integridade da cadeia de hash, validação dos NIF face ao cadastro da AT; Consistência da tabela de impostos: as taxas de IVA devem corresponder às em vigor no respectivo espaço fiscal; Numeração sequencial: lacunas ou duplicados dentro de uma série geram avisos; Alinhamento dos tipos de documento: os tipos de factura devem corresponder aos códigos de tabela do SAF-T (4.1 SalesInvoices, 4.2 MovementOfGoods, etc.)

### Verificações Pré-Submissão

- **Verificações Pré-Submissão** — Confirmar que o ATCUD está presente e correctamente formatado (CódigoValidação-NúmeroSequencial); Confirmar que os dados do QR Code correspondem aos campos da factura; Confirmar que a cadeia de hash RSA é ininterrupta (cada factura referencia o hash anterior); Confirmar que o número do software certificado AT é válido e corresponde ao cadastro da AT; Confirmar que todos os campos obrigatórios estão preenchidos

### Motivos Comuns de Rejeição

**Motivos Comuns de Rejeição**

| Motivo | Detalhe |
| --- | --- |
| ATCUD inválido | Código de validação não registado na AT para a série |
| Cadeia de hash quebrada | Hash não referencia correctamente a factura anterior |
| NIF inválido | NIF do fornecedor ou do adquirente falha a validação do dígito de controlo |
| Discrepância de taxa | A taxa de IVA não corresponde à taxa legal em vigor para a categoria de bens/serviços |
| Campos em falta | Campos obrigatórios omitidos no XML do SAF-T |
| Não conformidade com o esquema | XML não conforme com a versão actual do XSD do SAF-T(PT) |
| Submissão duplicada | Mesma factura já comunicada num período anterior |

## Secção 7 -- Regras de Apuramento

### Taxas de IVA (2026)

**Taxas de IVA (2026)**

| Taxa | Percentagem (Continente) | PT-Açores | PT-Madeira |
| --- | --- | --- | --- |
| Normal | 23% | 16% | 22% |
| Intermédia | 13% | 9% | 12% |
| Reduzida | 6% | 4% | 5% |
| Isenta | 0% | 0% | 0% |

### Regras de Arredondamento

- **Regras de Arredondamento** — Os montantes de IVA são calculados por linha e arredondados a 2 casas decimais (cêntimos de EUR). Os totais correspondem à soma dos montantes de linha arredondados -- NÃO se deve voltar a arredondar o total. O SAF-T(PT) exige base tributável e montante de imposto separados por taxa e por espaço fiscal.

### Tratamento de Facturas Multi-Taxa

- **Tratamento de Facturas Multi-Taxa** — Cada taxa de IVA e espaço fiscal deve constar como subtotal de imposto separado, tanto na factura como no XML do SAF-T(PT). Os campos I1-K8 do QR Code permitem codificar até 8 combinações de taxa/espaço fiscal.

### Retenção na Fonte

- **Retenção na Fonte** — Quando aplicável (por exemplo, prestações de serviços profissionais), a retenção na fonte deve ser indicada separadamente. O QR Code inclui um campo dedicado para o montante da retenção na fonte.

## Secção 8 -- Requisitos de Arquivo

**Requisitos de Arquivo**

| Requisito | Detalhe |
| --- | --- |
| Prazo de conservação | 10 anos a contar do fim do período de tributação |
| Formato | Formato original de emissão; os registos electrónicos devem permanecer legíveis por máquina |
| Acessibilidade | Acesso ininterrupto durante todo o prazo de conservação, mesmo em caso de migrações de sistema |
| SAF-T(PT) a pedido | Os ficheiros SAF-T(PT) (Facturação e Contabilidade) devem poder ser produzidos a pedido em qualquer momento durante o período de 10 anos, para efeitos de inspecção tributária |
| Integridade | A cadeia de hash e as assinaturas digitais devem permanecer verificáveis |
| Localização | Pode ser conservado fora de Portugal, dentro da UE, desde que a AT seja notificada e seja garantido o acesso em tempo real |
| Arquivo de AEQ | A partir de 2027, as facturas em PDF com AEQ devem ser arquivadas com a assinatura intacta e verificável |

## Secção 9 -- Sanções por Incumprimento

**Sanções por Incumprimento**

| Infracção | Pessoas Singulares (EUR) | Pessoas Colectivas (EUR) |
| --- | --- | --- |
| Não emissão ou emissão tardia de facturas | 150 -- 3 750 | 300 -- 7 500 |
| Utilização de software de facturação não certificado AT | 3 000 -- 18 750 | 3 000 -- 18 750 |
| QR Code ou ATCUD em falta nas facturas | 200 -- 1 000 por factura | 200 -- 1 000 por factura |
| Facturação irregular (hash inválido, número de software certificado AT em falta) | 150 -- 3 750 | 150 -- 3 750 |
| Submissão tardia ou incompleta do SAF-T(PT) de Facturação | Coimas graduadas nos termos do RGIT | Coimas graduadas nos termos do RGIT |
| Falta de submissão do SAF-T(PT) | Até 5 000 | Até 5 000 |
| Atrasos nos registos contabilísticos (superiores a 90 dias) | Até 5 000 | Até 5 000 |

## Secção 9 -- Sanções por Incumprimento

As sanções são agravadas para o dobro em caso de infracções dolosas ou fraudulentas, nos termos do RGIT. As coimas por factura (ATCUD/QR Code) acumulam-se rapidamente em emitentes de elevado volume.

Os fornecedores B2G estão ainda sujeitos ao risco adicional de exclusão de procedimentos de contratação pública por incumprimento dos requisitos CIUS-PT.

## Secção 10 -- Interacção com Outras Skills Fiscais

### SAF-T(PT) de Facturação → Declaração Periódica de IVA

- **SAF-T(PT) de Facturação → Declaração Periódica de IVA** — Os dados mensais do SAF-T(PT) de Facturação alimentam directamente a Declaração Periódica de IVA. A AT pré-preenche os campos da declaração de IVA a partir das submissões do SAF-T(PT). Discrepâncias entre os dados do SAF-T(PT) e a declaração de IVA accionam sinalizações automáticas.

### Deduções dos Consumidores no e-fatura

- **Deduções dos Consumidores no e-fatura** — As facturas comunicadas via SAF-T(PT) de Facturação aparecem no perfil de e-fatura do consumidor. Os consumidores utilizam estes dados para reclamar deduções em sede de IRS (por exemplo, saúde, educação, despesas gerais familiares). Dados incorrectos ou em falta afectam os benefícios fiscais do consumidor.

### SAF-T(PT) da Contabilidade → IES/DA Anual

- **SAF-T(PT) da Contabilidade → IES/DA Anual** — A partir de 2028 (período de tributação 2027), o ficheiro do SAF-T(PT) da Contabilidade deve ser submetido e validado pela AT antes da entrega da IES/DA (Informação Empresarial Simplificada / Declaração Anual). A validação pela AT deverá ocorrer no prazo de 10 dias após a submissão.

### IRC e IRS

- **IRC e IRS** — Os dados de facturação do SAF-T(PT) suportam as pretensões de dedução e a verificação de rendimentos em sede de IRC e IRS. A AT cruza os dados das facturas com os rendimentos declarados.

### Pagamentos por Conta e Retenção na Fonte

- **Pagamentos por Conta e Retenção na Fonte** — Os dados de retenção na fonte comunicados nas facturas são integrados na declaração anual de retenções. O campo de retenção na fonte do QR Code permite à AT cruzar com as declarações dos empregadores/pagadores.

## Aviso Legal

Esta skill e os respectivos resultados são disponibilizados apenas para fins informativos e de cálculo, não constituindo aconselhamento fiscal, jurídico ou financeiro. A Open Accountants e os seus contribuidores não assumem qualquer responsabilidade por erros, omissões ou consequências decorrentes da utilização desta skill. Todos os resultados devem ser revistos e validados por um profissional qualificado (como um Contabilista Certificado, Revisor Oficial de Contas, advogado fiscalista ou equivalente licenciado na sua jurisdição) antes de serem entregues ou utilizados como base para qualquer actuação.

A versão mais actualizada e verificada desta skill é mantida em [openaccountants.com](https://openaccountants.com).

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
