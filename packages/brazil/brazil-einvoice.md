---
name: brazil-einvoice
description: >
  Prepare and review Brazilian electronic invoice working papers for 2026. Covers
  NF-e, NFC-e and national NFS-e routing, authorisation, XML groups, invoice keys,
  certificates, events, rejection diagnosis, records and downstream tax handoffs.
  Separates legal IBS/CBS duties from model-specific technical releases, testing
  and production dates, including enacted later changes. Trigger on nota fiscal,
  NF-e 55, NFC-e 65, NFS-e, CT-e, SEFAZ, XML, DANFE, cancellation, CC-e, IBS/CBS
  fields,2025.002, CNPJ alfanumérico or invoice rejection. Retains transport and
  other fiscal-document routing without treating all models as NF-e 4.00. State
  penalties, complete executable schemas and unsupported provider claims remain
  explicit gaps; invoice evidence does not itself establish a tax credit or replace
  the tax return.
jurisdiction: BR
category: invoicing
domain: tax
tax_year: 2026
tier: 2
last_updated: 2026-11-11
version: 1.1
type: filing-howto
depends_on:
  - einvoice-workflow-base
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Brazil electronic invoices v 1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Brazilian issuers, recipients and their authorised preparers reviewing 2026 electronic fiscal documents. Confirm the document model, transaction date, issuer's tax regime and authorising UF/municipality before selecting a layout. A national reform act, a published technical note, its test deployment and production enforcement are different facts. This reference is checked as at 11 November 2026; enacted later dates below are labelled as future.

NF-e is a digital document whose validity requires qualified signature and tax-administration authorisation. A DANFE, an accepted network request or a document stored by a private provider does not establish an authorised, uncancelled invoice. [Ajuste SINIEF 7/05 clauses 1,4,7,9](https://www.confaz.fazenda.gov.br/legislacao/ajustes/2005/AJ007_05).

This Guide prepares model/version selection, field mapping, validation and authorisation evidence. It is partial for unsupported complete schema constraints, state-specific obligations/penalties and the gaps listed in Sources. Refer the affected integration or tax component while continuing the supported invoice work. Use `br-indirect-tax`/`brazil-vat` for the pack's designated consumption-tax computation, `br-simples-nacional` for elections and DAS, and the income/corporate/payroll owners for their tax calculations. Do not load the freelance intake merely to answer an invoice question.

First obtain issue/event dates, model, issuer/recipient, UF/municipality, CRT/regime/election, operation/product/service classification, XML/protocol/event history and the target test/production environment. The detailed input list is below.

## Rates, bands and thresholds

These figures govern the stated reform periods; they are not a universal invoice tax calculation.

| Item and conditions | Figure / period | Official source and exact anchor |
|---|---|---|
| IBS ordinary test rate, subject to art 348 regimes/reductions/exclusions |2026: state 0.1%; not an equal state/municipality split | [LC 214 art 343](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm): “alíquota estadual de 0,1%” |
| CBS ordinary test rate, subject to art 348 |2026:0.9% | [LC 214 art 346](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm): “alíquota de 0,9%” |
| Enacted subsequent IBS test split |2027–2028: state 0.05% and municipal 0.05% | [LC 214 art 344](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm): “alíquota estadual de 0,05%”; “alíquota municipal de 0,05%” |
| Simples operations in 2026 | The art 343/346 rates do not apply | [LC 214 art 348 III(c)](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm): “não serão aplicadas ... contribuintes optantes pelo Simples Nacional” |
|2026 payment waiver | Requires compliance with the accessory obligations; existing PIS/Cofins payments remain due in full | [LC 214 art 348§§1–2](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm): “que cumprirem as obrigações acessórias previstas na legislação” |
|2026 accessory-infringement cure after the statutory notice |60 days from notification; compliance extinguishes the imposed penalty | [LC 214 art 348§§3–4](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm): “prazo de 60 ... dias contado da intimação”; “extinção da penalidade” |

Do not calculate a credit merely because the supplier is regular-regime or an XML shows IBS/CBS. The owner tax Guide must establish the acquisition's eligibility, regime, effective date and applicable payment/credit conditions. If tax is actually collected in 2026, art 348 I–II provides compensation against the specified PIS/Cofins liabilities in the same period, then the prescribed alternative federal compensation/refund route if insufficient. That mechanism is distinct from an assumed input credit. [LC 214 art 348](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm).

## The base

### Model and authoriser selection

| Document / model | Route and source |
|---|---|
| NF-e 55 and NFC-e 65 | NF-e ecosystem; choose the actual operation and applicable UF rules, not a universal B 2 B/B 2 C or buyer-identification shortcut. [Current NF-e documents](https://dfe-portal.svrs.rs.gov.br/Nfe/Documentos), [SINIEF 7/05](https://www.confaz.fazenda.gov.br/legislacao/ajustes/2005/AJ007_05) |
| NFS-e | Service/DPS ecosystem; check national emitter versus the municipality's compatible own emitter/ADN sharing and current production documentation. [NFS-e production](https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica/documentacao-atual), [LC 214 art 62](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm) |
| CT-e 57, CT-e OS 67 | Transport models with their own technical notes, not NF-e's schema. [Joint Act 4 art 1 IV–V](https://cgibs.gov.br/upload/arquivos/202607/31091735-20260730-16h30-ato-conjunto-rfb-cgibs-na-c2-ba-4-260731-090909.pdf) |
| BP-e 63, MDF-e 58, GTV-e 64, NF 3 e 66, NFCom 62 | Route to that document's official portal, authoriser and current schema. Do not copy NF-e fields or deadlines wholesale. [Joint Act 4 art 1 VI–X](https://cgibs.gov.br/upload/arquivos/202607/31091735-20260730-16h30-ato-conjunto-rfb-cgibs-na-c2-ba-4-260731-090909.pdf) |
| NFAg 75, NFGas 76, NF-e ABI 77, DC-e 99 and NFS-e Via | Distinct models/systems and implementation dates; future duty does not establish present production availability. [Joint Act 4 art 1 XI–XVIII](https://cgibs.gov.br/upload/arquivos/202607/31091735-20260730-16h30-ato-conjunto-rfb-cgibs-na-c2-ba-4-260731-090909.pdf) |

Municipalities/DF must, from 1 January 2026 through 31 December 2032, permit national NFS-e issuance or share their own compatible documents in the national environment, together with the other specified declarations. This is not proof that every municipality abolished its own emitter or that one private provider supports every municipality. [LC 214 art 62§§1–6](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm).

MEI service suppliers already use national NFS-e for the applicable PJ-customer supplies from 1 September 2023; the cited CGSN guidance retains optional issuance for PF customers. The 2026 test-tax exclusion does not remove that existing duty. [Official NFS-e/CGSN 169 guidance](https://www.gov.br/nfse/pt-br/noticias/resolucao-cgsn-no-169-traz-novos-beneficios-ao-mei).

### Select the technical version before mapping fields

The current approved NF-e/NFC-e reform note is **NT 2025.002 v 1.53**, published 30 October 2026. Technical Joint Act 10 also approves NF-e/NFC-e NT 2026.005 v 1.00(Simples), .006 v 1.01(payment linkage), .007 v 1.11(exclusive IBS/CBS taxpayer) and .008 v 1.01(net product value). The classification table/Informe Técnico 2025.002 v 1.71 is a separate artefact. Other document models have their own specified notes. [Technical Joint Act 10 art 1](https://www.cgibs.gov.br/upload/arquivos/202610/30102301-atc-10-vf-assinado-assinado-261030-102245.pdf), [official SVRS index](https://dfe-portal.svrs.rs.gov.br/Nfe/Documentos).

As at 11 November, do not treat the note's 16 November production changes as already live. NTv 1.53 changes return-document referencing, including header-or-item reference and optional item number, with its stated future production schedule. The absence-of-IBSCBS rejection UB 12-10(1115) remains **future in production**, even though the legislative duty exists and filled groups are validated. The note expressly separates legal validity from technical implementation. Apply its transaction-specific exceptions, including the stated return/complement of pre 2027 documents and listed monophase fuel cases. [NTv 1.53 pp 6–8, UB 12-10](https://dfe-portal.svrs.rs.gov.br/NFE/DownloadArquivoEstatico/?sistema=NFE&tipoArquivo=3&nomeArquivo=NT_2025.002_v1.53_RTC_NF-e_IBS_CBS_IS.pdf).

NT 2026.005's new Simples fields have production scheduled 16 November 2026; its automated taxation event 412140 is still future. `tpRegimeIBSCBS`, `cAtivSN` and regular-regime versus `gTribSN` choices depend on its actual CRT/election/pending-option cases. Published schema support does not start the Simples tax itself in 2026. [NT 2026.005 v 1.00 pp 3–8](https://dfe-portal.svrs.rs.gov.br/NFE/DownloadArquivoEstatico/?sistema=NFE&tipoArquivo=3&nomeArquivo=NT_2026.005_v1.00_RTC_SimplesNacional.pdf).

### NF-e XML, keys and certificates

NF-e/NFC-e continue in the 4.00 layout family, with the current amending notes. Use the official schema package applicable to the model/date/environment. Base roots include `NFe/infNFe`, the relevant submission envelope and authorised `nfeProc` package; namespace `http://www.portalfiscal.inf.br/nfe`, UTF-8 and the specified XML signature structure. A partial fragment is not a schema-valid signed invoice. [MOC 7 integration specifications](https://dfe-portal.svrs.rs.gov.br/NFE/DownloadArquivoEstatico/?sistema=NFE&tipoArquivo=1&nomeArquivo=moc7-visao-geral.pdf), [current NF-e documents](https://dfe-portal.svrs.rs.gov.br/Nfe/Documentos).

An access key remains 44 characters. Its components include UF, year/month, issuer identification, model, series, document number, emission type, numeric code and check digit. From the CNPJ-alpha schema's 1 July 2026 production date, CNPJ and affected access-key fields accept characters rather than a digits-only assumption; referenced keys remain length 44 and CNPJ length 14. Preserve leading zeros and literal valid characters. Do not apply the old numeric-only check-digit implementation to the new format without the current joint technical specification. [NT 2026.004 v 1.01 pp 3–5](https://dfe-portal.svrs.rs.gov.br/NFE/DownloadArquivoEstatico/?sistema=NFE&tipoArquivo=3&nomeArquivo=NT_2026.004_v1.01_AlteraSchemaNFCeNFeCNPJAlfa.pdf), [MOC 7 AnnexI](https://dfe-portal.svrs.rs.gov.br/NFE/DownloadArquivoEstatico/?sistema=NFE&tipoArquivo=1&nomeArquivo=moc7-anexo-i-leiaute-e-rv.pdf).

Use the authorised ICP-Brasil signing/transmission facility and validate the certificate/issuer relationship, expiry and allowed chain/signature requirements for the current integration. The base MOC describes A 1/A 3, XMLDSig and `X509Certificate`; that is not a universal statement of current certificate duration, physical-token storage or a recommendation to replace its algorithm with SHA-256. Keep private keys and passwords out of working papers. Unsupported certificate-duration/algorithm details are listed in Sources. [SINIEF 7/05 clauses 1,3,7](https://www.confaz.fazenda.gov.br/legislacao/ajustes/2005/AJ007_05), [MOC 7 signature specifications](https://dfe-portal.svrs.rs.gov.br/NFE/DownloadArquivoEstatico/?sistema=NFE&tipoArquivo=1&nomeArquivo=moc7-visao-geral.pdf).

### Field map retained from the old integration

This map preserves the input topics; **it is not a declaration that every field is mandatory in every model**. Resolve type, occurrence, length, enum and conditional rules against the applicable schema and current note before generation. [MOC 7 AnnexI groupsB–W](https://dfe-portal.svrs.rs.gov.br/NFE/DownloadArquivoEstatico/?sistema=NFE&tipoArquivo=1&nomeArquivo=moc7-anexo-i-leiaute-e-rv.pdf), [NT 2025.002 v 1.53 layoutsB/UB/W](https://dfe-portal.svrs.rs.gov.br/NFE/DownloadArquivoEstatico/?sistema=NFE&tipoArquivo=3&nomeArquivo=NT_2025.002_v1.53_RTC_NF-e_IBS_CBS_IS.pdf).

| Group | Fields / preparation checks |
|---|---|
| Identification `ide` | UF/numeric code, nature, model, series, number, issue/exit dates, direction/destination, municipality, print/emission/environment, check digit, purpose, final consumer/presence and software/process fields: `cUF,cNF,natOp,mod,serie,nNF,dhEmi,dhSaiEnt,tpNF,idDest,cMunFG,tpImp,tpEmis,cDV,tpAmb,finNFe,indFinal,indPres,procEmi,verProc`; current reform additions where applicable |
| Issuer `emit` | `CNPJ` or applicable CPF case, legal/trade names, address, IE/IM/CNAE and CRT; reconcile actual registration and election. CRT includes MEI 4, not only 1/2/3 |
| Recipient `dest` | `CNPJ/CPF/idEstrangeiro`, name/address and `indIEDest/IE` as applicable; recipient identification depends on model/operation, not an invented nationwide R$ 200 cutoff |
| Product/service `det/prod` | `cProd,cEAN,xProd,NCM,CFOP,uCom,qCom,vUnCom,vProd,cEANTrib,uTrib,qTrib,vUnTrib,indTot,CEST` where applicable; verify actual product/classification and GTIN status |
| Item taxes `det/imposto` | Applicable ICMS,IPI,PIS,COFINS,II,ISSQN and reform IS/IBSCBS groups. A tax-specific choice cannot be inferred just from the company's broad tax regime |
| Legacy totals `total/ICMSTot` | Relevant bases/taxes, product/freight/insurance/discount/other charges and invoice total, including `vBC,vICMS,vProd,vFrete,vSeg,vDesc,vII,vIPI,vPIS,vCOFINS,vOutro,vNF`; preserve applicable ancillary/ST/FCP/devolution fields if present |
| Reform items and totals | CST/classification, applicable IBS/CBS base/state/municipal/CBS groups and current totals. Do not replace them with standalone sibling`IBS`/`CBS` blocks |

`finNFe` now includes normal 1, complement 2, adjustment 3, return 4, credit 5 and debit 6, with further note-type/reference conditions. For a regular branch the item hierarchy is `det/imposto/IBSCBS`, with `CST,cClassTrib` and the applicable choice; `gIBSCBS` contains `vBC,gIBSUF,gIBSMun,vIBS,gCBS`. Totals sit under `total/IBSCBSTot`. The current indicator tables govern required/forbidden groups. [NTv 1.53 B 25, UB 12–UB 15, W 34](https://dfe-portal.svrs.rs.gov.br/NFE/DownloadArquivoEstatico/?sistema=NFE&tipoArquivo=3&nomeArquivo=NT_2025.002_v1.53_RTC_NF-e_IBS_CBS_IS.pdf).

Retain full precision in the calculation ledger, then use each field's permitted decimals and each active validation's rounding/tolerance. The old universal 2/4/10 decimal and one-cent-per-tax-group assertion is not an executable specification. Use the current rule's reductions, deferment, returns, monophase and classification exceptions before comparing totals. [NTv 1.53 UB/W rules](https://dfe-portal.svrs.rs.gov.br/NFE/DownloadArquivoEstatico/?sistema=NFE&tipoArquivo=3&nomeArquivo=NT_2025.002_v1.53_RTC_NF-e_IBS_CBS_IS.pdf).

### National NFS-e is a separate implementation

Use [NFS-e production documentation](https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica/documentacao-atual) for the live DPS/NFS-e XSD, APIs and annexes, and its separate [deployment table](https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica/atualizacoes-e-implantacoes). The RTC index links NT 009 v 1.01 and its new classification/adjustment/address/foreign-operation/condominium/Simples changes, but the 20 October changes were listed under **restricted production/testing**, not the production column. Do not copy a new tag into production merely because it is published. [NT 009 v 1.01 introduction](https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica/rtc/nota-tecnica-009-se-cgnfs-e-v-1-01.pdf).

AnnexVIII's service/NBS/cClassTrib correlation is explicitly preliminary and has no production or pilot business rules based on it. Obtain the actual applicable service code and classification, rather than treating this draft correlation as a tax determination. [Official RTC index](https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica/rtc).

## Deadlines and filing

### Legislative IBS/CBS document starts

The following are Joint Act 4's **reform document duties**, subject to its exceptions; they do not repeal earlier ICMS/ISS/MEI invoice duties or guarantee every validation is deployed. [Joint Act 4 art 1](https://cgibs.gov.br/upload/arquivos/202607/31091735-20260730-16h30-ato-conjunto-rfb-cgibs-na-c2-ba-4-260731-090909.pdf).

| Model / operation, subject to exceptions below | Start date | Official source |
|---|---|---|
| NF-e 55,NFC-e 65,CT-e 57,CT-e OS 67,MDF-e 58,GTV-e 64,NF 3 e 66,DC-e 99,NFS-e Via |3 August 2026 | [Act 4 art 1 I–II,IV–V,VII–IX,XII–XIII](https://cgibs.gov.br/upload/arquivos/202607/31091735-20260730-16h30-ato-conjunto-rfb-cgibs-na-c2-ba-4-260731-090909.pdf) |
| BP-e 63, except semiurban/metropolitan/aerial passenger sectors below |3 August 2026 | [Act 4 art 1 VI(c)](https://cgibs.gov.br/upload/arquivos/202607/31091735-20260730-16h30-ato-conjunto-rfb-cgibs-na-c2-ba-4-260731-090909.pdf) |
| Ordinary NFS-e services listed for ISS, excluding art 1 III(a)–(c) cases |1 October 2026 | [Act 4 art 1 III(d)](https://cgibs.gov.br/upload/arquivos/202607/31091735-20260730-16h30-ato-conjunto-rfb-cgibs-na-c2-ba-4-260731-090909.pdf) |
| NFCom 62 and import remittance DIR |1 October 2026 | [Act 4 art 1 X/XV](https://cgibs.gov.br/upload/arquivos/202607/31091735-20260730-16h30-ato-conjunto-rfb-cgibs-na-c2-ba-4-260731-090909.pdf) |
| Platform services/intermediated cases specified in art 1 III(a); ISS subitems 1.03/1.05/1.09 and 16.01; remaining art 1 III categories including specified immaterial goods, condominium receipts and leasing |1 December 2026, future at this read date | [Act 4 art 1 III(a)–(c),(e)–(h)](https://cgibs.gov.br/upload/arquivos/202607/31091735-20260730-16h30-ato-conjunto-rfb-cgibs-na-c2-ba-4-260731-090909.pdf) |
| Semiurban/metropolitan/aerial BP-e; NFGas 76,NFAg 75,NF-e ABI 77 |1 December 2026, future | [Act 4 art 1 VI(a)–(b),XI,XVI,XVIII](https://cgibs.gov.br/upload/arquivos/202607/31091735-20260730-16h30-ato-conjunto-rfb-cgibs-na-c2-ba-4-260731-090909.pdf) |
| Duimp and material-import NF-e under the specified substitution |1 January 2027, future | [Act 4 art 1 XIV/§3](https://cgibs.gov.br/upload/arquivos/202607/31091735-20260730-16h30-ato-conjunto-rfb-cgibs-na-c2-ba-4-260731-090909.pdf) |
| Simples taxpayer documents; NF-e monophase supplies |1 January 2027, future | [Act 4 art 1§§1–2](https://cgibs.gov.br/upload/arquivos/202607/31091735-20260730-16h30-ato-conjunto-rfb-cgibs-na-c2-ba-4-260731-090909.pdf) |
| NF-e by the specified IBS/CBS taxpayer who is not an ICMS contributor |1 December 2026, future | [Act 4 art 1§4](https://cgibs.gov.br/upload/arquivos/202607/31091735-20260730-16h30-ato-conjunto-rfb-cgibs-na-c2-ba-4-260731-090909.pdf) |
| DeRE table events; first monthly events; remaining events | Table reception 1 October 2026; first monthly events 15 November 2026 covering October; thereafter day 15 following period; remaining events 1 January 2027 | [Act 4 art 1 XVII/§5](https://cgibs.gov.br/upload/arquivos/202607/31091735-20260730-16h30-ato-conjunto-rfb-cgibs-na-c2-ba-4-260731-090909.pdf) |

For the longer transition, route the actual period to the consumption-tax owner rather than adding unsupported fixed post-test rates or assuming that all legacy documents become NFS-e. Retain separate legacy tax groups while the applicable law/schema requires them. [LC 214 arts 343–348 and subsequent transition provisions](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm).

### Issuance and authorisation workflow

1. Confirm issuer registration/credentialing with the actual UF or municipal authoriser, model and legal duty. Select that official portal's live endpoint/WSDL or national NFS-e API. Do not construct`sefaz{UF}.{domain}` or substitute a provider's URL for an authority source. [Official NF-e/SVRS services](https://dfe-portal.svrs.rs.gov.br/NFE/Servicos), [NFS-e API documentation](https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica/documentacao-atual).
2. Record the model, issue date, authoriser, environment and pinned MOC/NT/XSD/table versions. Map source invoice data and owner-approved tax classifications to fields. Resolve unknown legally decisive fields before issuing; keep other preparation independent.
3. Validate XML structure, signature/certificate, registration, number/key, classifications, permitted groups, item calculations and totals against the actual active rules. Test and production are separate. [MOC 7 AnnexI validation sections](https://dfe-portal.svrs.rs.gov.br/NFE/DownloadArquivoEstatico/?sistema=NFE&tipoArquivo=1&nomeArquivo=moc7-anexo-i-leiaute-e-rv.pdf), [NTv 1.53](https://dfe-portal.svrs.rs.gov.br/NFE/DownloadArquivoEstatico/?sistema=NFE&tipoArquivo=3&nomeArquivo=NT_2025.002_v1.53_RTC_NF-e_IBS_CBS_IS.pdf).
4. Submit through the authorised integration, retain request/response and follow that deployed service's protocol/receipt flow. Submission or batch processing alone is not invoice authorisation. Query an uncertain result before generating another invoice. The published NT 2023.002 v 1.02 announces changes to asynchronous authorisation/inutilisation; the complete implementation schedule is not established here, so do not hardcode one permanent polling architecture. [Official current-note index](https://dfe-portal.svrs.rs.gov.br/Nfe/Documentos).
5. Match authorised protocol and key to the signed XML, then retain the authorised package and associated events. For merchandise recipients the issuer must send/download-enable XML+protocol immediately after authorisation; the service taker provides it to the contracted carrier before service begins. [SINIEF 7/05 clause 7§§5–7](https://www.confaz.fazenda.gov.br/legislacao/ajustes/2005/AJ007_05).
6. Keep a status/event ledger. A rejected document requires diagnosis, while an authorised document generally cannot be edited. Use the proper cancellation, CC-e, return, credit/debit or contingency procedure and retain its response. [SINIEF 7/05 clauses 7,11–15](https://www.confaz.fazenda.gov.br/legislacao/ajustes/2005/AJ007_05).

### Status and rejection diagnosis

| Code / old issue | Correct interpretation and action | Official source |
|---|---|---|
|100 | Authorised use; verify matching document/key and later events | [MOC 7 AnnexI cStat table](https://dfe-portal.svrs.rs.gov.br/NFE/DownloadArquivoEstatico/?sistema=NFE&tipoArquivo=1&nomeArquivo=moc7-anexo-i-leiaute-e-rv.pdf) |
|101;135 | Cancellation homologated; event registered and linked, respectively. These are not interchangeable with original-use authorisation | [MOC 7 AnnexI cStat table](https://dfe-portal.svrs.rs.gov.br/NFE/DownloadArquivoEstatico/?sistema=NFE&tipoArquivo=1&nomeArquivo=moc7-anexo-i-leiaute-e-rv.pdf) |
|204;539 | Duplicate; duplicate with different access key. Query the original key/number/protocol and reconcile before retrying; do not blindly change`nNF`/`cNF` | [MOC 7 AnnexI cStat/RV table](https://dfe-portal.svrs.rs.gov.br/NFE/DownloadArquivoEstatico/?sistema=NFE&tipoArquivo=1&nomeArquivo=moc7-anexo-i-leiaute-e-rv.pdf) |
|215;225 | XML schema validation failure;225 concerns the NF-e batch's XML schema, not destination/CFOP | [MOC 7 AnnexI D 01/cStat table](https://dfe-portal.svrs.rs.gov.br/NFE/DownloadArquivoEstatico/?sistema=NFE&tipoArquivo=1&nomeArquivo=moc7-anexo-i-leiaute-e-rv.pdf) |
|611 | Invalid GTIN(`cEAN`); diagnose the actual product data/rule instead of falsely claiming a CCG lookup result | [MOC 7 AnnexI I 03-10](https://dfe-portal.svrs.rs.gov.br/NFE/DownloadArquivoEstatico/?sistema=NFE&tipoArquivo=1&nomeArquivo=moc7-anexo-i-leiaute-e-rv.pdf) |
|778 | Nonexistent NCM, not a general NCM/CFOP mismatch | [MOC 7 AnnexI I 05-20](https://dfe-portal.svrs.rs.gov.br/NFE/DownloadArquivoEstatico/?sistema=NFE&tipoArquivo=1&nomeArquivo=moc7-anexo-i-leiaute-e-rv.pdf) |
|110/301 historical denegation | Do not use the 2020 denegation entries as current instructions: clause 7 II and related denial provisions were repealed from 1 August 2024; issuer/recipient irregularities are now rejection cases under I(g)/(h). Never label all 301–999 statuses rejections | [Current SINIEF 7/05 clause 7](https://www.confaz.fazenda.gov.br/legislacao/ajustes/2005/AJ007_05) |

### Events and corrections

| Event | Conditions / timing | Official source |
|---|---|---|
| Cancellation 110111 | Ordinary NF-e: within 24 hours of authorisation, with no goods circulation, service or escritural-duplicata linkage. Special contingency substitution under clause 12-A has its own maximum 168 hours, reducible by UF; do not turn that into a universal 7-day permission | [SINIEF 7/05 clauses 12–13](https://www.confaz.fazenda.gov.br/legislacao/ajustes/2005/AJ007_05), [MOC 7 event table](https://dfe-portal.svrs.rs.gov.br/NFE/DownloadArquivoEstatico/?sistema=NFE&tipoArquivo=1&nomeArquivo=moc7-visao-geral.pdf) |
| CC-e 110110 | Issuer correction only within clause 14-A limits; cannot change tax-determining variables, issuer/recipient identity, issue/exit date, export fields informed in DU-E or instalment-sale parcels. Consolidate prior corrections in the latest CC-e; protocol does not validate its content | [SINIEF 7/05 clause 14-A](https://www.confaz.fazenda.gov.br/legislacao/ajustes/2005/AJ007_05), [MOC 7 event table](https://dfe-portal.svrs.rs.gov.br/NFE/DownloadArquivoEstatico/?sistema=NFE&tipoArquivo=1&nomeArquivo=moc7-visao-geral.pdf) |
| Recipient confirmation 210200 / unknown operation 210220 and operation-not-performed | The duty/party and AnnexII exceptions matter. Through 31 May 2026 the general cap was 180 days; from 1 June it is 90 days after authorisation. With no stated event after the current 90 days, clause 15-C§6 gives confirmation effects. Do not read the older alternative text as current | [SINIEF 7/05 clauses 15-B/C](https://www.confaz.fazenda.gov.br/legislacao/ajustes/2005/AJ007_05), [MOC 7 event table](https://dfe-portal.svrs.rs.gov.br/NFE/DownloadArquivoEstatico/?sistema=NFE&tipoArquivo=1&nomeArquivo=moc7-visao-geral.pdf) |
| Recipient event corrections / Ciência | Specified events may be recorded up to twice, latest valid; changes within 30 days of first manifestation. Ciência may be recorded within 10 days and requires a definitive event. Apply the separate AnnexII deadlines where relevant | [SINIEF 7/05 clause 15-C§§1–5](https://www.confaz.fazenda.gov.br/legislacao/ajustes/2005/AJ007_05) |
| EPEC 110140 / contingency | Use the applicable model/UF contingency process, signed event, permitted DANFE and later authorisation/reconciliation. EPEC alone is not final ordinary authorisation. For clause 11 II/III cases, transmit immediately after the problem ceases and within 168 hours of issue; clause 11 IV instead uses the first following business day. Clause 11§19 excludes EPEC in Paraíba and Paraná from 1 October 2026. Pending original invoices and substitutions must be reconciled to avoid duplicates | [SINIEF 7/05 clauses 11/11-A/17-D](https://www.confaz.fazenda.gov.br/legislacao/ajustes/2005/AJ007_05), [MOC 7 contingency/event sections](https://dfe-portal.svrs.rs.gov.br/NFE/DownloadArquivoEstatico/?sistema=NFE&tipoArquivo=1&nomeArquivo=moc7-visao-geral.pdf) |

Retain the full authorised XML, matching protocol, cancellation/correction/recipient/contingency events and accessible backups, indexed by issuer, key, date and model. Check status and authenticity of received documents before accounting/credit handoff. Apply the relevant tax legislation's retention period, including unresolved assessments/disputes, instead of automatically deleting on a blanket five-years-from-January rule. The issuer must retain the digital NF-e. Clause 10§2 expressly allows a recipient not credentialed to issue NF-e to keep the DANFE instead; do not apply that recipient exception to the issuer. [SINIEF 7/05 clauses 9–11](https://www.confaz.fazenda.gov.br/legislacao/ajustes/2005/AJ007_05).

## Penalties and interest

Do not reuse a source-less national 1%/minimum R$ 500 fine or the old SP/MG/RJ/PR percentages. Identify model, jurisdiction, offence, tax period, notice and cure status; obtain that authority's current penalty provision. The unresolved state figures remain listed in Sources. Preserve the actual notice and response deadline while the penalty calculation is referred.

For 2026 IBS/CBS, the statutory 60-day cure is described above. PNCT treats compliant taxpayers as included unless they opt out. A noncompliant taxpayer remains in the programme only on its cumulative conditions: progressively increasing correct fiscal documents, timely responses, notified inconsistencies corrected by 31 December 2026 and an indicated responsible accountant. Its specified monitoring communications preserve spontaneity only within the act's limits and do not remove the statutory cure period. Sharing/representation by the accountant also requires the stated authorisation and professional-registration conditions. This is not an unconditional temporary immunity. [Joint Act 5 arts 1–3](https://cgibs.gov.br/upload/arquivos/202608/13065932-ato-conjunto-rfb-cgibs-n-c2-ba-5-2026-regulamenta-o-programa-nacional-de-conformidade-tributaria-docx-assinado.pdf), [LC 214 art 348§§3–4](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm).

## Cross-border points

Imports/exports still need their operation, product/origin and customs-document mapping. Preserve DI/Duimp/DIR/DU-E references and linked invoices as applicable; do not select a generic import/export CFOP or tax rate from geography alone. Use the customs/cross-border owner for duties and tax classification, then reconcile its result with the invoice fields. Duimp's reform-document start and material-import exception are dated above. [Joint Act 4 art 1 XIV–XV/§3](https://cgibs.gov.br/upload/arquivos/202607/31091735-20260730-16h30-ato-conjunto-rfb-cgibs-na-c2-ba-4-260731-090909.pdf), [SINIEF 7/05 clauses 8,14-A](https://www.confaz.fazenda.gov.br/legislacao/ajustes/2005/AJ007_05).

Hand invoice/item/event data to EFD ICMS/IPI, EFD-Contribuições, accounting/ECD, profit-tax/ECF, municipal ISS, payroll/withholding and DCTFWeb/MIT owners where applicable. Bridge invoice value to revenue, receipts, tax bases and credits with timing/cancellation/return differences; never force equality or silently substitute invoices for those declarations. ICMS-ST/DIFAL/interstate rates, product-specific IPI and cumulative/noncumulative PIS/Cofins remain owner calculations, not universal rates inferred here from Lucro Real/Presumido labels.

## Two worked examples that recompute

**Invoice field calculation and payable distinction.** Assume a regular-regime NF-e domestic standard-rated item issued after its applicable 2026 duty date, a legally established base R$ 1,000, correct classification, and no reduction/deferment/monophase treatment. State IBS is R$ 1; municipal IBS R$ 0; CBS R$ 9. The item amounts sum to R$ 10. This is an illustration of field arithmetic, not proof R$ 10 is payable or that the recipient has a credit: apply art 348 compliance/payment and owner credit conditions separately. A Simples transaction cannot be run through these 2026 regular test rates. [LC 214 arts 343/346/348](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm), [NTv 1.53 UB 18/UB 37/UB 56](https://dfe-portal.svrs.rs.gov.br/NFE/DownloadArquivoEstatico/?sistema=NFE&tipoArquivo=3&nomeArquivo=NT_2025.002_v1.53_RTC_NF-e_IBS_CBS_IS.pdf).

```oa-check
name: Regular2026 invoice test fields
inputs:
  established_base: 1000
steps:
  ibs_state: established_base * 0.001
  ibs_municipal: established_base * 0
  cbs: established_base * 0.009
  field_sum: ibs_state + ibs_municipal + cbs
expected:
  ibs_state: 1
  ibs_municipal: 0
  cbs: 9
  field_sum: 10
```

**Authorisation decision.** If the sender times out after submission, the preparer queries the existing key/protocol before retrying. An authorised result is reconciled to that original document; a rejection is diagnosed and corrected under its actual rule. Creating another number solely to clear a duplicate error risks recording a second invoice. This qualitative case adds no invented statutory amount or deadline. [SINIEF 7/05 clause 7](https://www.confaz.fazenda.gov.br/legislacao/ajustes/2005/AJ007_05).

## Ask the client first

Read existing records before asking for these six fact groups:

1. Model, operation/service/product, issue/event dates and UF/municipality/authoriser.
2. Issuer/recipient identifiers, registrations, regime/CRT, election and any pending-option facts.
3. Classification and tax-owner inputs, special/reduced/monophase/export/import/return cases and source documents.
4. Existing signed XML, authorisation/receipt/protocol, access key and all related event/substitution history.
5. Technical versions, schema/table versions, environment, certificate validity and integration responses, without exposing signing secrets.
6. Notices, prior corrections, record gaps, accounting/tax handoffs and the action authorised for the current work.

Completion checks: model/date/regime matched; duty distinguished from technical enforcement; future changes labelled; field cardinalities and calculations validated against the actual schema; request/protocol and later events reconciled; duplicates resolved; source XML/protocol/events retained; owner tax outputs and unresolved gaps identified. Preparing a draft or validating a file does not itself authorise real issuance, cancellation, filing or payment.

## Sources

| Source and portion read | URL | Read on |
|---|---|---|
| Read in part: LC 214 current arts 62,343–348 and related transition/effect provisions; current amendments distinguished | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm |2026-11-11 |
| Read in part: Joint Act 4, signed original 3 pages in full; model/sector/regime dates and exceptions | https://cgibs.gov.br/upload/arquivos/202607/31091735-20260730-16h30-ato-conjunto-rfb-cgibs-na-c2-ba-4-260731-090909.pdf |2026-11-11 |
| Read in part: Joint Act 5, signed original in full; PNCT inclusion, cure/accountant and communication conditions | https://cgibs.gov.br/upload/arquivos/202608/13065932-ato-conjunto-rfb-cgibs-n-c2-ba-5-2026-regulamenta-o-programa-nacional-de-conformidade-tributaria-docx-assinado.pdf |2026-11-11 |
| Read in part: Technical Joint Act 10, original 3 pages in full; approved versions and effective publication | https://www.cgibs.gov.br/upload/arquivos/202610/30102301-atc-10-vf-assinado-assinado-261030-102245.pdf |2026-11-11 |
| Read in part: NF-e NT 2025.002 v 1.53; historypp 3–8, groupsB/UB/W, relevant validations/events; not every 96-page rule audited | https://dfe-portal.svrs.rs.gov.br/NFE/DownloadArquivoEstatico/?sistema=NFE&tipoArquivo=3&nomeArquivo=NT_2025.002_v1.53_RTC_NF-e_IBS_CBS_IS.pdf |2026-11-11 |
| Read in part: CNPJ alpha NT 2026.004 v 1.01; history, introduction and affected-field tables | https://dfe-portal.svrs.rs.gov.br/NFE/DownloadArquivoEstatico/?sistema=NFE&tipoArquivo=3&nomeArquivo=NT_2026.004_v1.01_AlteraSchemaNFCeNFeCNPJAlfa.pdf |2026-11-11 |
| Read in part: Simples NT 2026.005 v 1.00; chronology and sections 2–3, including future event | https://dfe-portal.svrs.rs.gov.br/NFE/DownloadArquivoEstatico/?sistema=NFE&tipoArquivo=3&nomeArquivo=NT_2026.005_v1.00_RTC_SimplesNacional.pdf |2026-11-11 |
| Read in part: MOC 7 base integration, XML/signature and event tables; later notes/law override historical entries | https://dfe-portal.svrs.rs.gov.br/NFE/DownloadArquivoEstatico/?sistema=NFE&tipoArquivo=1&nomeArquivo=moc7-visao-geral.pdf |2026-11-11 |
| Read in part: MOC 7 AnnexI; selected layout groups, result/error tables and validations, not every field independently certified | https://dfe-portal.svrs.rs.gov.br/NFE/DownloadArquivoEstatico/?sistema=NFE&tipoArquivo=1&nomeArquivo=moc7-anexo-i-leiaute-e-rv.pdf |2026-11-11 |
| Read in part: Current SINIEF 7/05 consolidated text; clauses 1,3–15,17-D; dates distinguish historical/future alternatives | https://www.confaz.fazenda.gov.br/legislacao/ajustes/2005/AJ007_05 |2026-11-11 |
| Read in part: Official SVRS current documents index, MOC/NT versions and asynchronous-change title | https://dfe-portal.svrs.rs.gov.br/Nfe/Documentos |2026-11-11 |
| Read in part: National NFS-e live production index, updated 4 November; deployment table, updated 21 October | https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica/documentacao-atual ; https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica/atualizacoes-e-implantacoes |2026-11-11 |
| Read in part: National NFS-e RTC index and NT 009 v 1.01 introduction/affected topics; provisional correlations not mandatory rules | https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica/rtc ; https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica/rtc/nota-tecnica-009-se-cgnfs-e-v-1-01.pdf |2026-11-11 |
| Read in part: Official MEI NFS-e/CGSN 169 guidance; September 2023 duty and PF-customer distinction | https://www.gov.br/nfse/pt-br/noticias/resolucao-cgsn-no-169-traz-novos-beneficios-ao-mei |2026-11-11 |

Not yet confirmed: complete executable current XSD types/cardinalities/decimal constraints for every field/model, joint CNPJ-alpha check-digit algorithm, current certificate duration/storage/algorithm changes, full NT 2023.002 implementation schedule, state-specific NFC-e identification and extraordinary cancellation rules, all state invoice penalties and the old SP/MG/RJ/PR percentages, the old national 1%/minimum R$ 500 fine, blanket IPI 0–365% range, uniform five-year retention starting 1 January, complete special-sector/monophase/classification-table computations, blanket tax-credit availability, and provider coverage/capability promises. The CGIBS index's signed Act 6 attachment bears a MINUTA heading; its nanoentrepreneur exemption is not asserted here without a confirmed final published text. These are partial components, not reasons to refuse all ordinary invoice preparation.

Find Brazil Guides and professional-review options at [OpenAccountants](https://openaccountants.com). Check the version, date and approval shown there; this Guide is **Not yet approved** and does not claim to be the platform's current verified version.
