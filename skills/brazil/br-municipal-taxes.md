---
name: br-municipal-taxes
description: >
  Resolve Brazilian municipal tax questions for service providers, service purchasers,
  property owners and property transferees in 2026. Determine the ISS municipality,
  service item, ordinary local rate, withholding responsibility and evidence needed
  before issuing an invoice or calculating a payment. Includes capital-city profiles
  with item-specific IT, consulting and construction distinctions, conditional local
  incentives, registration and filing routes, the limits of the national NFS-e rate
  dataset, and separate Distrito Federal treatment. Covers IPTU versus rural ITR,
  ITBI valuation, capital contributions and unresolved assignments of acquisition
  rights. Use for ISS local rates, municipal registration, retained ISS, construction
  materials, service imports or exports, IPTU and ITBI. Municipal profiles have
  explicit coverage limits; this is not a complete local tax code for every city.
jurisdiction: BR
category: international
tax_year: 2026
tier: 2
last_updated: 2026-11-11
version: 0.1
type: situation-rules
job: municipal-tax-profiles
depends_on:
  - br-indirect-tax
  - brazil-einvoice
  - br-simples-nacional
---

# Brazil municipal taxes v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Not yet approved.** Source-cited draft, checked against the stated official materials on 11 November 2026. A profile confirms only the items, conditions and source portions stated here. It does not attest that every local benefit, administrative calendar or special regime has been exhausted.

## Who this applies to

Use this Guide for a provider or purchaser of a listed service, an owner or possessor of urban property, or a party to an onerous property transaction. Select the municipality of the taxable event before selecting its rate. A customer's address, the invoice emitter and the place where a bank pays are different facts.

| Answer needed | Start here | Output boundary |
|---|---|---|
| Which municipality receives ISS? | Situs sequence below | Actual establishment, service item and exception; not a nationwide destination rule |
| IT or consulting rate? | Exact service description, then the capital profile | Distinguish IT consultancy from residual general consultancy; substantiate every incentive |
| Should the purchaser retain ISS? | Liability sequence, then local designation | A withholding entry must name its legal basis and municipality |
| National invoice standard? | [Brazil e-invoicing](brazil-einvoice.md) | This Guide supplies local registration and payment facts, not XML implementation |
| CBS/IBS, federal service contributions or ICMS? | [Indirect-tax classifier](br-indirect-tax.md), then [federal contributions](brazil-vat.md) | Municipal ISS remains a separate analysis in 2026 |
| Simples or MEI? | [Simples Nacional](br-simples-nacional.md) | The ordinary municipal rates below do not replace the regime's ISS component or retention rules |
| IPTU or ITBI? | Property sequence below | A local valuation, rate, benefit and payment act is still required for a payable amount |

This is a new job. It supplements the national owners and does not rewrite their national rate cards. The capital matrix covers every state capital as a research destination and separately explains Brasília/DF. Entries marked pending cannot produce a supported local payable amount. Non-capital municipalities use the same legal method and the national dataset as a locator, followed by their own current legislation.

## Rates, bands and thresholds

### Service classification and local rate selection

Apply these ordinary ad valorem rates only after establishing that the service is taxable in the named jurisdiction, the operation date falls within the cited rule, and neither Simples, fixed professional taxation, immunity, exemption nor a special assessment changes the result. The federal list identifies services; it does not set one local IT rate. The [LC 116/2003 list, items 1, 7 and 17](https://www2.camara.leg.br/legin/fed/leicom/2003/leicomplementar-116-31-julho-2003-492028-normaatualizada-pl.html) distinguishes IT consultancy in 1.06 from residual consultancy in 17.01. CNAE is activity evidence and can be an express eligibility condition; it does not replace the actual supplied service.

| Jurisdiction and legal provision | Ordinary item-specific result | Conditions and narrower branches | Official text |
|---|---|---|---|
| São Paulo, Lei 13.701/2003 art. 16 III, I(a), IV | Item 1 except 1.09: **2.9%**; 1.09: **2%**; residual 17.01: **5%** | Item 1 includes genuine IT consultancy. Streaming has its separate item; general management consultancy does not become IT because software is used. Test the complete current art. 16 exceptions and any evidenced special regime. | https://legislacao.prefeitura.sp.gov.br/lei-13701-de-24-de-dezembro-de-2003/consolidado |
| Belo Horizonte, Lei 8.725/2003 art. 14 II(a), II(b), IV | Item 1: **2.5%**; residual 17.01: **5%** | Public-opinion research within 17.01 is **2.5%** under II(b), not the residual rate. Do not reverse the columns in the authority's historical rate-change table: the IT rate shown from May 2014 is 2.5%. Professional societies and qualifying cooperatives require separate analysis. | https://fazenda.pbh.gov.br/legislacao/formkey.asp?key=542 |
| Curitiba, LC 40/2001 art. 4 IV and I(e), §1 | Ordinary IT and residual general consultancy: **5%** | **2%** is available to the actual call-centre/remote technical-assistance activities described in §1, performed through telephone, email, chat and fax treatment. A label such as software support does not establish that branch. | https://legisladocexterno.curitiba.pr.gov.br/VisualizarHTML.aspx?id=41 |
| Fortaleza, LC 159/2013 art. 245 II, III, consolidated through LC 452/2025 | Ordinary item 1 and residual 17.01: **5%**; construction 7.02, 7.04 and 7.05: **3%** | The list in art. 245 I contains specific reduced services, not a generic IT category. Distinguish the service-price regime from autonomous-professional and professional-society taxation. | https://www.sefin.fortaleza.ce.gov.br/anexoCT/24/fak3yj2cw.3541423/pdf/C%C3%B3digo%20Tribut%C3%A1rio%20do%20Munic%C3%ADpio%20de%20Fortaleza%20atualizado%20at%C3%A9%20Dez-2025%20-%20LC%20452-2025 |
| Macapá, LC 144/2021 arts. 276-277 and Annex XI | IT 1.01-1.09 and residual 17.01: **5%** | Read LC 209/2025 with the code for construction deductions, licensing and local fees. Its amended fee annex is not a replacement ISS rate list. Fixed autonomous-professional taxation is separate. | https://macapa.ap.gov.br/portal/wp-content/uploads/2023/03/LEI_COMPLEMENTAR_N_144_2021_PMM_com_alteracoes.pdf |
| Porto Velho, Decreto 18.749/2023 art. 563 I(e), II, implementing LC 878/2021 | **2%** for 1.04 only when the corresponding activity is the provider's principal activity; **5%** for remaining ordinary services | Do not extend the 1.04 principal-activity condition to 1.06 IT consultancy or to 1.05 licensing. Confirm actual principal activity, actual contract and current municipal registration. The cited rate authority is the municipal regulation; the complete current statutory amendment chain remains a stated limit. | https://sapl.portovelho.ro.leg.br/ta/7519/text |
| Rio de Janeiro, Lei 691/1984 art. 33 I, II(6), II(19), II(23), authority rate card | Residual service: **5%**; bespoke computer-program generation: **2%**; 1.09: **2%** | Other item 1 services can be **2%** under II(19) only with the specified provider location in the Ilha do Bom Jesus/UFRJ technology-park areas or Porto urban-operation area, excluding Avenida Presidente Vargas and Avenida Rio Branco. This authority card contains expired unrelated entries; the complete 2026 consolidated code was not accessible. Do not use the card to certify every benefit's continuing availability. | https://carioca.rio/wp-content/uploads/2022/02/Aliquotas-de-ISS-atualizado.pdf |
| Salvador, Lei 7.186/2006 Annex III, Tabela de Receita II, 2026 table items 28 and 21 | Remaining listed services: **5%** | Item 21's **2%** IT branch requires a company outside Simples established in an eligible RENOVACENTRO property. Separate high-technology and geographic benefit lines have their own qualifications. Being an IT company or using a virtual office does not establish entitlement. Formal admission and current implementing conditions are required. | https://www2.sefaz.salvador.ba.gov.br/storage/9732/3.-Anexo-III--Tabela-Receita-II---ISS---Alt-Lei-9.534-9.562-e-9.601-24%2C-9.767-23-E-9.823.2024.pdf |
| Goiânia, LC 344/2021 art. 226 §1 III(a), VIII, §§9-10 | Remaining company activities: **5%**; qualifying item 1 branch: **2%** | The law gives item 1 a transitional 2% rule while the specified technology/innovation pole is not implemented; after implementation the territorial/program conditions and the Estação Digital concession's term matter. **The implementation fact and the taxpayer's applicable branch are not confirmed here. Do not select either IT rate from the platform alone.** General residual consultancy follows VIII unless a separate evidenced regime applies. | https://www.goiania.go.gov.br/html/gabinete_civil/sileg/dados/legis/2021/lc_20210930_000000344.html |
| Porto Alegre, LC 7/1973 art. 21 and Tabela XII, LC 966/2022, LC 998/2023; official consolidated collection dated 2024 | 1.01, 1.02 and 1.04-1.09: **2%**; 1.03 processing/data-processing services: **5%**, remaining 1.03 services: **2%**; residual 17.01: **5%** | Do not collapse every item 1 service to 2%. The collection shows **2.5%** for 7.02/7.05 from June 2024 under LC 998/2023. Its stated 2038 end date cannot override the national ISS transition. The collection is a dated consolidation, not a complete 2026 amendment search certificate. | https://prefeitura.poa.br/sites/default/files/usu_doc/sites/smf/Colet%C3%A2nea%20da%20legisla%C3%A7%C3%A3o%20do%20ISS%20-%202024%20v10_04_2024%20VF.pdf |
| Distrito Federal, LC 963/2020 art. 1 and Annex | **2%** on the enumerated IT services supplied by a legal person whose **principal activity** is classified in the Annex | Retain principal CNAE evidence and actual IT-service facts. Annex families cover software development, web design, customisable/non-customisable programs, IT consultancy and support. The data-hosting service description alone does not add a principal CNAE missing from the Annex. Do not apply this rule to residual management consultancy. | https://www.sinj.df.gov.br/sinj/Norma/40ee803e42a8482399d4507a0c86c9c1/Lei_Complementar_963_03_01_2020.html |

**Aracaju's technology incentive is a separate conditional profile.** The municipal transparency site hosts a reproduction of LC 183/2022 arts. 1-8, printed in March 2025. It describes a reduction from **5% to 2%** for qualifying Aracaju-established technology, innovation, research and scientific-qualification services; other services of the same company are excluded. Concession requires a jobs/investment intentions protocol, annual reassessment, and continued compliance. Following notice and failure to cure, revocation brings the rate back to **5% for the noncompliance period**, crediting the 2% already paid. The original gazette, current implementing act and complete later amendment chain have not been confirmed, so this Guide does not apply the incentive automatically to an invoice or to Simples. [LC 183/2022, municipality-hosted reproduction, arts. 1-8](https://transparencia.aracaju.se.gov.br/wp-content/uploads/desoneracoes/LC_183_2022_Tecnologia_e_Inovacao.pdf).

### Every state capital and Brasília: what can be concluded

The legal profiles above are substantive but bounded. This matrix identifies remaining work for each capital, including where a platform row exists but the actual current municipal law has not been read. A pending city is an ordinary local coverage gap, not a claim that its taxpayers or services are outside scope.

| State and capital | Evidence available and usable route | Remaining ordinary gap |
|---|---|---|
| AC, Rio Branco | [Municipal code and amendments index](https://cgm.riobranco.ac.gov.br/lai/legislacao/codigo-tributario/); platform snapshot contains dated service rows | Current consolidated ISS rate/benefit chain, registration, declaration and payment act not read; no local rate certified |
| AL, Maceió | [SEFAZ official service and tax-information route](https://maceio.al.gov.br/noticias/sefaz/prefeitura-de-maceio-concede-isencao-fiscal-a-contribuintes-em-situacoes-especiais) | Special disaster-area relief news does not establish ordinary IT rates; full current code and filing/payment conditions pending; snapshot has no capital rows |
| AP, Macapá | Legal profile above; [current municipal legislation index](https://macapa.ap.gov.br/leis-tributarias-municipais/) lists LC 209/2025 and the 2026 calendar | Apply the construction and TUFE changes below; read the actual period's calendar and extensions before generating a due date |
| AM, Manaus | [Câmara record for Lei 2.833/2021](https://sapl.cmm.am.gov.br/norma/3137); [SEMEF professional-society procedure](https://semefatende.manaus.am.gov.br/inventario.php?id=534) identifies Decreto 6.844/2026 | Complete current ISS law/regulation and ordinary rate list pending; do not use superseded Lei 1.089/2006 or old DAM dates as a 2026 certificate; snapshot has no rows |
| BA, Salvador | Conditional legal profile above; [SEFAZ legislation index](https://www2.sefaz.salvador.ba.gov.br/legislacao/leis/lei-1?filtro=ISS) | RENOVACENTRO admission/current implementing conditions and operation-specific extensions remain required; no blanket reduced IT rate |
| CE, Fortaleza | Current code through LC 452/2025; [SEFIN service route](https://www.sefin.fortaleza.ce.gov.br/Canal/16/Generico/18/Ler) and [activity/substitution query](https://issadmin.sefin.fortaleza.ce.gov.br/grpfor/pagesPublic/atividadeCPBS/consultarAtividadeCPBS.seam) | Actual CPBS classification, retained-service rule, calendar and deductions election must be matched to the taxpayer; no capital rows in snapshot |
| ES, Vitória | [SEMFA ISSQN procedure](https://www.vitoria.es.gov.br/semfa/issqn), registration/declaration route | Full current Lei 6.075/2003 and benefit amendments not read; authority general guidance and snapshot do not certify a current incentive or every IT rate |
| GO, Goiânia | [Current art. 226](https://www.goiania.go.gov.br/html/gabinete_civil/sileg/dados/legis/2021/lc_20210930_000000344.html) and relevant code context read; profile above | Pole implementation, actual qualifying site and concession term decide the IT branch; snapshot is insufficient |
| MA, São Luís | [SEMFAZ substitution/CENE/CNR procedure](https://semfaz.saoluis.ma.gov.br/substituto_tributario/), [municipal FAQ](https://www.saoluis.ma.gov.br/perguntas-frequentes---semfaz) | Current full local service-rate table, operative migration instructions and calendar pending. CENE absence is not alone authority for extra-territorial withholding |
| MT, Cuiabá | [Municipal ISSnet portal](https://onlinecba.issnetonline.com.br/cuiaba/Login/Login.aspx?ReturnUrl=%2Fcuiaba%2FLogin) advertises CTM 2026; older official code retained in source packet | The current notice requires national NFS-e emission from 1 November 2026 for all ISSQN taxpayers, including Simples, and ends Free Nota emission after 31 October. The linked current code could not be retrieved as a document; no current local rate is certified from the older consolidation or snapshot |
| MS, Campo Grande | [Municipal ISS service page](https://www.campogrande.ms.gov.br/servicos/iss/) and its code/amendment routes | Complete current LC 59/2003 rate annex and calendar not read; no snapshot rows for capital |
| MG, Belo Horizonte | Current art. 14 profile; [BHISS procedures and migration notices](https://prefeitura.pbh.gov.br/fazenda/bhiss) | Service-specific CTISS, actual migrated emitter, retention designation, DES/guia and calendar exceptions must be resolved; missing snapshot rows do not imply exemption |
| PA, Belém | [Municipal ISS PJ/PF service route](https://financas.belem.pa.gov.br/servicos-online/iss-pessoa-juridica-e-fisica/) | Older general page is not a complete 2026 legal rate certificate; full current law and PJ filing rules pending; snapshot has no rows |
| PB, João Pessoa | [Municipal legislation consultation](https://www.joaopessoa.pb.gov.br/pc/consultaLegislacao.xhtml?tipo=1) | Full current LC 53/2008 amendment chain, item rate and calendar pending. Historical snapshot rows ending earlier do not supply an active 2026 rate |
| PR, Curitiba | Current consolidated LC 40/2001 profile and [ISS-Curitiba procedure](https://www.curitiba.pr.gov.br/conteudo/iss-com-inscricao-municipal-para-empresas/357) | Apply actual remote-assistance conditions and current issuer/cancellation instructions; do not revive the code's unconstitutional outside-provider registration penalty |
| PE, Recife | [Portal Finanças FAQ](https://portalfinancas.recife.pe.gov.br/faq), including optional CPOM and establishment evidence | Complete current Lei 15.563/1991 rate/benefit amendments and calendar pending; no snapshot rows |
| PI, Teresina | [SEMF legislation route](https://antigo-semf.pmt.pi.gov.br/naf-legislacao/) | Current CTM, later amendments and 2026 calendar not read completely; no supported ordinary local rate or snapshot capital rows |
| RJ, Rio de Janeiro | Authority art. 33 card and geographic/bespoke distinctions above; [Câmara code record](https://aplicnt.camara.rj.gov.br/APL/Legislativos/contlei.nsf/b24a2da5a077847c032564f4005d4bf2/eda5d6a190cd4993032576ac00738dc8?OpenDocument) | Complete consolidated 2026 attachment, later benefits and current Nota Carioca/national migration conditions pending; snapshot has no rows |
| RN, Natal | [Municipal taxation route](https://www.natal.rn.gov.br/); dated snapshot rows | Full current CTM/rate and incentive provisions not read; platform entry alone is not a local legal certificate |
| RS, Porto Alegre | Tabela XII profile and [LC 998/2023 official record](https://legislacao.portoalegre.rs.gov.br/norma/47805) | Read later amendments and the actual current emitter/payment instructions; 2024 collection does not establish all 2026 procedures |
| RO, Porto Velho | [Regulation](https://sapl.portovelho.ro.leg.br/ta/7519/text) and signed LC 1.044/2025 amendment read | Principal-activity evidence, DMS/DMST, actual emitter and current calendar remain taxpayer-specific; complete statutory amendment chain is a stated limit |
| RR, Boa Vista | [Câmara Lei 1.223/2009 record and amendments](https://sapl.boavista.rr.leg.br/norma/2566) | Complete current rate annex and amendments not read; distinguish Boa Vista/RR from same-name municipalities; snapshot rates are not law confirmation |
| SC, Florianópolis | [Municipal finance legislation route](https://devportal.pmf.sc.gov.br/entidades/smdu/index.php?cms=legislacao&menu=0), current filing-notice route | Complete current LC 7/1997 rate, professional-society regime and operative 2026 instructions pending; do not substitute another city's LC 7 |
| SE, Aracaju | [Municipality-hosted LC 183/2022 reproduction](https://transparencia.aracaju.se.gov.br/wp-content/uploads/desoneracoes/LC_183_2022_Tecnologia_e_Inovacao.pdf) and incentive conditions above | Original gazette, implementation/admission and complete current ordinary rate/filing law pending; do not assume every IT service qualifies |
| SP, São Paulo | Current consolidated art. 16 profile; [Fazenda ISS payment instructions](https://coleta.prefeitura.sp.gov.br/web/fazenda/w/servicos/iss/2486) | Actual local service code, applicable designated retention and taxpayer's current national/local emission cohort remain required |
| TO, Palmas | [Câmara CTM consolidation route](https://legislativo.palmas.to.gov.br/media/leis/lei-complementar-285-2013-10-31-20-11-2023-16-47-59.pdf) and dated snapshot rows | Complete current LC 285/2013 and later amendments not read. Older reduced-rate announcements cannot establish 2026 liability |
| DF, Brasília | District legal profile above; use [SINJ](https://www.sinj.df.gov.br/) and the DF revenue authority, not a Brasília city hall | DF is not a municipality and cannot be divided into municipalities. It exercises municipal tax powers under CF arts. 32 §1 and 147; principal-CNAE qualification and current DF payment/retention procedure still required |

### National NFS-e platform rate data: reproducible lookup, not a legal rate engine

The [official NFS-e alíquotas page](https://www.gov.br/nfse/pt-br/biblioteca/aliquotas) describes registered platform rates covering **5,571 municipalities**. Its dated [3 September 2026 ZIP](https://www.gov.br/nfse/pt-br/biblioteca/aliquotas/aliquotas-municipios-20260903-extr1.zip) contains state CSVs and a combined text file. Its existence does not prove a row for every capital or taxpayer. The archive read here has no DF CSV; absent city rows, blank rates and ended intervals occur.

For an executable lookup, use the standard-library Python below on the downloaded ZIP. Supply the actual municipality's IBGE code, the **exact nine-digit snapshot service code** and operation date. The code preserves each matched record; it does not infer legal situs from `incidencia`, map an LC item to a code, choose a benefit or treat an empty result as zero. Check the current original municipal act and the invoice system's actual current configuration separately. A September snapshot cannot certify a November administrative change.

```python
import csv, io, json, zipfile
from datetime import date

archive = "aliquotas-municipios-20260903-extr1.zip"
ibge = "5208707"              # example lookup, not proof of situs
service = "01.06.01.000"      # exact snapshot code, not a CNAE
operation = date.fromisoformat("2026-11-11")

def source_date(value):
    return date.fromisoformat(value.strip()[:10]) if value.strip() else None

matches = []
with zipfile.ZipFile(archive) as z:
    for name in z.namelist():
        if not name.lower().endswith(".csv"):
            continue
        reader = csv.DictReader(io.TextIOWrapper(z.open(name), encoding="utf-8-sig"),
                                delimiter=";")
        for row in reader:
            if row["codigo_ibge"].strip() != ibge:
                continue
            if row["codigo_servico"].strip() != service:
                continue
            start, end = source_date(row["dt_ini"]), source_date(row["dt_fim"])
            if (start is None or start <= operation) and (end is None or operation <= end):
                matches.append({"archive_member": name, **row})
print(json.dumps({"rows": matches, "legal_rate_confirmed": False}, ensure_ascii=False))
```

The separate legal check matters in practice: Goiânia's art. 226 contains conditional and transitional IT rules that the archive's undifferentiated row cannot resolve. The lookup output is working-paper evidence of the platform registration, not permission to override that statute.

## The base

### ISS sequence: service, situs, liability, base, local rule

1. **Describe what is supplied.** Reconcile the contract, deliverable, invoice and actual work to the [LC 116 list](https://www2.camara.leg.br/legin/fed/leicom/2003/leicomplementar-116-31-julho-2003-492028-normaatualizada-pl.html). Separate 1.04 program creation, 1.05 licensing, 1.06 IT consultancy, 1.07 support and 17.01 residual consultancy where the facts support distinct services. Do not create artificial invoice splits. Under art. 1 §4, the name alone does not decide incidence. For software licensing/assignment, the [STF ADIs 1.945 and 5.659](https://www.stf.jus.br/arquivo/informativo/documento/informativo1007.htm) distinguish the ISS service from ICMS even for standardised software, including download/cloud delivery. Historical refunds and modulation require the actual period's decision, not a 2026 reclassification of all earlier payments.
2. **Find the actual establishment.** Art. 4 requires a permanent or temporary economic/professional unit where the service activity develops. A registered office, mailbox or invoice address alone does not prove that unit. Retain staff, premises, equipment, management and delivery evidence. Apply art. 3's provider-establishment rule only after checking the exceptions below.
3. **Select the proper municipality.** For ordinary listed IT and consultancy with no applicable exception, use the provider establishment or, absent it, domicile. A purchaser's preference for its city's code cannot move the tax. Test imports, construction and the specific situs exceptions before assigning a municipal revenue code.
4. **Determine who must pay.** Art. 5 makes the provider the taxpayer; art. 6 permits express local-law designation of a connected third party and separately identifies responsible purchasers. A contract's net-payment clause is not that law. Record the actual municipal provision, purchaser category, service, supplier regime, retention base/rate and proof of remittance. A legally responsible purchaser's duty is not erased by failure to deduct the tax from the supplier's cash payment.
5. **Build the taxable price.** Under art. 7 the base is the service price. Do not deduct operating costs, payroll, third-party bills or another tax merely because they appear on an invoice. Record a specific exclusion's legal basis, admissible documents and local treatment before reducing the base. For ordinary services, tax is supported service price multiplied by the applicable local rate. Reconcile retained tax and own remittance without paying the same liability twice or inventing an automatic cross-city credit.
6. **Apply the local regime and evidence.** Match the local service code, rate, incentive concession, valid registration and operation date. Link Simples cases to its national owner before computing. Fixed autonomous-professional or professional-society regimes require the profession, legal form, personal responsibility and current local admission/annual values; neither the word consultant nor a professional registration automatically qualifies.

| Service or fact | Situs or responsibility result | Source and limit |
|---|---|---|
| Imported service or service begun abroad | ISS is due at the recipient/intermediary establishment, or domicile if none; the taker/intermediary is responsible | LC 116 arts. 1 §1, 3 I, 6 §2 I: https://www2.camara.leg.br/legin/fed/leicom/2003/leicomplementar-116-31-julho-2003-492028-normaatualizada-pl.html |
| Scaffolding/stage/temporary-structure supply, 3.05 | Place of installation | LC 116 art. 3 II: same |
| Works 7.02, works supervision 7.19 and 14.14 | Place of works; current art. 3 III expressly includes 14.14 following LC 218/2025 | LC 116 art. 3 III: same |
| Demolition 7.04; repair/conservation/reform 7.05 | Demolition site; location of the relevant buildings/roads/bridges/ports | LC 116 art. 3 IV-V: same |
| Waste, cleaning, gardening, effluent treatment, forestry, shoring and dredging services | Apply the specific execution/location test for the exact subitem; not simply the supplier's registered office | LC 116 art. 3 VI-XIV: same |
| Parking/storage, guarded/monitored assets and people | Respect the distinct tests for 11.01, 11.02 and 11.04; monitoring/tracking must be classified before using a security exception | LC 116 art. 3 XV-XVII and art. 6 §2 II exception: same |
| Entertainment other than 12.13; municipal transport; supplied labour 17.05; fairs 17.10; ports/airports item 20 | Respectively actual execution, municipality of transport, taker's establishment/domicile, event and facility location | LC 116 art. 3 XVIII-XXII: same |
| Infrastructure use 3.04 across cities; toll-road 22.01 across cities | Allocate to each municipality's territorial extension; 3.04 base apportions by the statutory relevant extension or pole count | LC 116 art. 3 §§1-2 and art. 7 §1: same |
| Maritime services | Provider establishment, except the specific 20.01 facility rule | LC 116 art. 3 §3: same |
| Purchaser-domicile rules still printed for health plans, cards/funds/consortia and leasing | Do not apply invalidated destination provisions mechanically from a consolidated local code | STF ADI 5.835, ADI 5.862, ADPF 499, judgment June 2023: https://www.stf.jus.br/arquivo/informativo/documento/informativo1097.htm |
| Outside provider has not registered in the customer's city | Absence alone cannot support the unconstitutional outside-provider registration/retention mechanism | STF Tema 1020: https://portal.stf.jus.br/noticias/verNoticiaDetalhe.asp?idConteudo=461609&ori=1 ; this does not cancel a genuine local establishment's registration or lawful imported-service/construction responsibility |

The [STF's Tema 1020](https://portal.stf.jus.br/noticias/verNoticiaDetalhe.asp?idConteudo=461609&ori=1) is particularly important when a municipal code still displays an old CPOM/CENE withholding paragraph. São Paulo's current art. 9-A uses optional registration; Recife's FAQ describes optional CPOM with establishment evidence, and São Luís' substitution page distinguishes CENE from the non-retention certificate process. Do not infer that no municipal evidence or declaration is ever required. Resolve genuine situs, lawful responsibility and actual establishment first. [São Paulo current law](https://legislacao.prefeitura.sp.gov.br/lei-13701-de-24-de-dezembro-de-2003/consolidado), [Recife](https://portalfinancas.recife.pe.gov.br/faq), [São Luís](https://semfaz.saoluis.ma.gov.br/substituto_tributario/).

### Construction, service imports and exports

**Construction.** Separate execution 7.02, professional design/engineering, supervision 7.19, demolition, repair and actual materials sales. The service location and the rate item need not follow the same broad construction label. LC 116 art. 7 §2 I addresses materials for 7.02/7.05; it is not a universal percentage deduction and does not authorise deduction of every subcontract or reimbursed purchase. Obtain the current local deduction provision, election, project records and admissible invoices, and resolve any applicable judicial limitation before computing. The goods exception in the list for goods produced by the provider outside the worksite must also be tested. [LC 116 arts. 3, 6-7 and list item 7](https://www2.camara.leg.br/legin/fed/leicom/2003/leicomplementar-116-31-julho-2003-492028-normaatualizada-pl.html).

Macapá provides a concrete current branch: **LC 209/2025 art. 3 amended art. 247** to exclude materials produced by the provider outside the worksite only where separately identified and commercialised with ICMS incidence. Art. 4's amended art. 249 requires the provider's acquisition documents, identified issuer/recipient, full worksite address, legibility and submission for SEFIN analysis. Do not import another city's presumed deduction into Macapá. [Signed LC 209/2025 original, arts. 2-4](https://macapa.ap.gov.br/portal/wp-content/uploads/2026/01/LEI_COMPLEMENTAR_209_2025_COMPLETA0064.pdf).

**Imports.** Identify the Brazilian taker/intermediary, its establishment, exact service, price/currency evidence, invoice-equivalent/local declaration and retained ISS guide. A foreign supplier's lack of municipal registration does not remove imported-service liability. Federal contributions, cross-border withholding and CBS/IBS are additional questions routed to the national owners; local ISS does not answer them. [LC 116 arts. 1 §1, 3 I and 6 §2 I](https://www2.camara.leg.br/legin/fed/leicom/2003/leicomplementar-116-31-julho-2003-492028-normaatualizada-pl.html).

**Exports.** Under art. 2 I and its sole paragraph, services whose result occurs in Brazil are not excluded merely because a foreign resident pays. Record what the customer uses, where the result is verified, the contract, deliverable, beneficiary and evidence supporting that conclusion. Separate a genuine export exclusion from a municipality's reduced rate on a taxable service for an overseas recipient. Curitiba art. 4 §2 expressly describes the latter: services developed in Brazil with a Brazilian result despite foreign payment. Do not treat foreign currency or a foreign billing address as proof of exemption. [LC 116 art. 2](https://www2.camara.leg.br/legin/fed/leicom/2003/leicomplementar-116-31-julho-2003-492028-normaatualizada-pl.html), [Curitiba LC 40/2001 art. 4 §2](https://legisladocexterno.curitiba.pr.gov.br/VisualizarHTML.aspx?id=41).

### IPTU: property, location, use, base and assessment

Read the actual property's municipal legislation and assessment notice. Under [CTN arts. 32-34](https://www2.camara.leg.br/legin/fed/lei/1960-1969/lei-5172-25-outubro-1966-358971-normaatualizada-pl.html), the taxable interest includes ownership, domínio útil or possession in the legally defined urban area; the base is the property's valor venal, excluding movable property used there. The municipal law defines the urban zone, ordinarily requiring at least **two** statutory public improvements: curb/paving with drainage, water supply, sewerage, public lighting, or a primary school/health post within **three kilometres**. Approved subdivisions intended for housing, industry or commerce in urbanisable/expansion areas have the art. 32 §2 exception; do not reject an assessment solely by counting improvements without checking it.

Actual rural use also matters. [STJ Tema 174](https://processo.stj.jus.br/repetitivos/temas_repetitivos/pesquisa.jsp?cod_tema_final=174&cod_tema_inicial=174&novaConsulta=true&tipo_pesquisa=T) applies ITR rather than IPTU to an urban-located property proven to be used for extractive, vegetable, agricultural, livestock or agroindustrial exploitation. A cadastral urban label alone does not close that branch; retain actual use evidence and coordinate the federal rural-tax treatment.

For a computation, obtain the assessed land/building areas, use, valuation zone, value schedule, progressive/differential rate bands, exemption recognition, annual index/update act, payment calendar and property identifier. Under **CF art. 156 §1 III**, added by EC 132/2023, the executive may update the base according to criteria established by municipal law. Do not say every executive valuation change beyond inflation is automatically invalid without considering that current constitutional provision and its enabling local criteria. Payment instalments and rebates are city/year-specific; no national instalment or discount is assumed. [Current Constitution, arts. 147 and 156](https://www2.camara.leg.br/legin/fed/consti/1988/constituicao-1988-5-outubro-1988-322142-normaatualizada-pl.html).

### ITBI: transaction, valuation and corporate movements

1. Identify the onerous inter vivos transaction, property location, parties, actual rights transferred, instrument and registration status. **Current CTN art. 35**, amended by LC 227/2026 with effect from publication under its art. 182 III, separately includes ownership/domínio útil, non-security real rights, and assignments of acquisition rights. Gifts and inheritances require the state ITCMD owner, not an invented municipal ITBI rate. Under arts. 41-42 the situs municipality/DF is competent and local law selects the liable party. [Current CTN arts. 35-42](https://www2.camara.leg.br/legin/fed/lei/1960-1969/lei-5172-25-outubro-1966-358971-normaatualizada-pl.html), [LC 227 arts. 165 and 182](https://www2.camara.leg.br/legin/fed/leicom/2026/leicomplementar-227-13-janeiro-2026-798657-normaatualizada-pl.html).
2. Establish the taxable market value and local rate, distinguishing any financed portion or recognised local relief. **Current art. 38 §§1-3**, added in 2026, defines cash market value in normal conditions, permits specified technical criteria, requires disclosure of the valuation criteria and gives the taxpayer a contradictory-valuation route under local procedure. Preserve the transaction's condition, restrictions, financing, appraisal and comparables. Do not simply use the IPTU base as a statutory minimum. [CTN art. 38](https://www2.camara.leg.br/legin/fed/lei/1960-1969/lei-5172-25-outubro-1966-358971-normaatualizada-pl.html).
3. Read the established **STJ Tema 1113** with the new art. 38 and art. 148 procedure. Its propositions distinguish the actual transaction from the generic IPTU schedule, presume the declared transaction consistent with market value subject to proper proceedings, and reject unilateral advance reference-value arbitration. The new 2026 technical-valuation text must be considered; this Guide does not certify every post-amendment valuation dispute or automatic refund. [STJ decision explanation](https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias/09032022-Base-de-calculo-do-ITBI-e-o-valor-do-imovel-transmitido-em-condicoes-normais-de-mercado--define-Primeira-Secao.aspx), [CTN arts. 38 and 148](https://www2.camara.leg.br/legin/fed/lei/1960-1969/lei-5172-25-outubro-1966-358971-normaatualizada-pl.html).
4. For a **capital contribution**, distinguish the amount actually integralised as share capital from any excess and retain corporate instruments and valuations. On **20 October 2026**, the STF decided **Tema 1348**: the capital-realisation immunity is independent of predominantly real-estate activity, subject to simulation/fraud. The official docket read shows the judgment and published session record; this is not a claim of a final unappealable judgment or a complete modulation analysis. The separate **Tema 796** excludes value exceeding the capital being integralised from the immunity. Do not deny all capital-contribution immunity merely because the company rents or deals in real estate. [Tema 1348 current docket](https://portal.stf.jus.br/jurisprudenciaRepercussao/verAndamentoProcesso.asp?classeProcesso=RE&incidente=6929423&numeroProcesso=1495108&numeroTema=1348), [Tema 796](https://portal.stf.jus.br/jurisprudenciaRepercussao/verAndamentoProcesso.asp?classeProcesso=RE&incidente=4529914&numeroProcesso=796376&numeroTema=796).
5. Do not transplant that capital-contribution conclusion to a merger, incorporation, demerger or extinction. Analyse the separate constitutional/statutory reorganisation rule and its predominant-activity condition against the actual transaction. [CF art. 156 §2 I](https://www2.camara.leg.br/legin/fed/consti/1988/constituicao-1988-5-outubro-1988-322142-normaatualizada-pl.html), [CTN arts. 36-37](https://www2.camara.leg.br/legin/fed/lei/1960-1969/lei-5172-25-outubro-1966-358971-normaatualizada-pl.html).
6. **Assignments of acquisition rights remain a distinct unresolved judicial branch.** The current **Tema 1124** docket does not establish a final merits thesis that every assignment is untaxed until property registration. The earlier reaffirmation was not retained when the STF recognised repercussion without reaffirming jurisprudence in 2022. Match the current CTN, actual right and local act, and refer a disputed cession before recommending nonpayment. [Tema 1124 current docket](https://portal.stf.jus.br/jurisprudenciaRepercussao/verAndamentoProcesso.asp?classeProcesso=ARE&incidente=6031137&numeroProcesso=1294969&numeroTema=1124).

## Deadlines and filing

### Operational sequence

Create one record per establishment and competent municipality. Record the municipal registration number, actual service list item, municipal code, tax regime, liable person, invoice/declaration identifier, period, base, rate/benefit evidence, due-date act, guide and remittance receipt. Registration, permission to issue, reporting and paying are separate tasks. A federal CNPJ does not establish completion of each local registration. A paid fee does not establish a valid operating licence.

**NFS-e standard versus emitter.** [LC 214/2025 art. 62 §1 I-II](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm) requires municipalities/DF, from **1 January 2026**, to authorise the national-pattern NFS-e in the national environment or share their own emitter's standardised documents with the national environment, and to share the specified other electronic-declaration content. It does not command every provider to use the same screen or abolish all municipal returns. Load [brazil-einvoice](brazil-einvoice.md) for national layouts, migration and document checks. Use the municipality's actual current emitter/cohort notice for access, cancellation, substitution and RPS conversion; national schema compatibility does not prove live taxpayer authorisation.

For each period: reconcile issued/cancelled/replaced documents, services taken, imports and retained ISS; test a nil-return duty; close the applicable local declaration; generate the correct own/retained guide; check period and jurisdiction; pay; retain receipt; reconcile the next ledger period. Do not present an unsubmitted working paper or a national invoice transmission as a completed municipal return/payment. Preserve acknowledgement numbers only after the real system returns them.

| Profile | Supported local procedural fact | Conditions and official route |
|---|---|---|
| São Paulo | Ordinary ISS due **10th of the following month**; NFS-e/NFTS/DPS cases generate the guide directly in the NFS-e environment; other authorised DAMSP/payment routes remain identified by the authority | Own versus retained liability and actual document type must match. Special calendars/regimes and nonworking-day treatment require the applicable rule. https://coleta.prefeitura.sp.gov.br/web/fazenda/w/servicos/iss/2486 |
| Belo Horizonte | Regulation art. 13, as amended by Decreto 17.649/2021: ordinary ISS due **8th of the following month** | Use the actual current BHISS/national emitter route; separately resolve DES, retained services, special rules and banking-day treatment. https://fazenda.pbh.gov.br/internet/legislacao/formkey.asp?key=1124 |
| Curitiba | Municipal authority says providers/responsible persons pay by the **20th** through DAM; bookkeeping and DAM issuance are electronic in ISS-Curitiba | Its stated exception covers federal public bodies in Decreto 1.637/2005. Confirm the precise competence/calendar and applicable national/local emitter, rather than moving all taxpayers to another city's deadline. https://www.curitiba.pr.gov.br/conteudo/iss-com-inscricao-municipal-para-empresas/357 |
| Porto Velho | Decreto 18.749/2023 art. 571 II: ordinary PJ/responsible-party ISS by the **15th of the following month**; public-payer rule uses the payment month under §1 | Arts. 573 and 582 distinguish DMS/DMST, documents and regime exceptions. LC 1.044/2025 permits the own emitter while maintained and requires national fields; do not infer that DMS/DMST vanished. https://sapl.portovelho.ro.leg.br/ta/7519/text ; https://sapl.portovelho.ro.leg.br/media/sapl/public/normajuridica/2025/28711/lei_complementar_no_1.044_de_19_de_dezembro_de_2025_sei.pdf |
| Goiânia | LC 344 arts. 227-230: monthly homologation for ordinary companies, calendar-set payment dates, distinct annual fixed regimes, Cadastro Mobiliário | Use the actual calendar. Retention is on invoice emission, with the public-taker payment exception in current art. 228 §1; event advance-payment rules are distinct. https://www.goiania.go.gov.br/html/gabinete_civil/sileg/dados/legis/2021/lc_20210930_000000344.html |
| Cuiabá | Actual current municipal ISSnet notice: **national emitter mandatory from 1 November 2026 for all ISSQN taxpayers, including Simples**; Free Nota ends **31 October 2026** | The public menu links current municipal/national code correlations and later cancellation instructions. Their existence is not proof that the underlying code, attachment contents or every cancellation deadline was read. https://onlinecba.issnetonline.com.br/cuiaba/online/login/login.aspx |
| Macapá | LC 209/2025 establishes TUFE and local fiscal registration per location; it replaces specified location/operation and sanitary fees | The recurring-tax event is exceptionally **1 April 2026** under art. 15 §1, not the ordinary January event. Arts. 17 and 26 contain nonincidence/exemptions, including the specified home/nonpublic and service-at-client facts, MEI and registered autonomous professionals. DAM timing depends on the decree; no unconfirmed current UFM or discount is applied. https://macapa.ap.gov.br/portal/wp-content/uploads/2026/01/LEI_COMPLEMENTAR_209_2025_COMPLETA0064.pdf |

For other capitals, retain the city-specific pending item in the capital matrix until the actual current local registration, declaration and calendar text is available. Do not fill the missing date with the most common date in another municipality. IPTU and ITBI guides additionally require the correct property identifier, valuation/recognition decision and transaction-specific procedure.

## Penalties and interest

There is no supported uniform municipal late-payment percentage, grace period, fine cap or interest index in this Guide. Read the competent municipality's current penalty/interest provision, the period-specific calendar, the actual infraction and any valid instalment/settlement act before calculating arrears. Separate unpaid tax, delayed declaration, document failure and breach of incentive conditions. A timely invoice does not establish timely payment.

The [Aracaju LC 183/2022 reproduction, art. 6](https://transparencia.aracaju.se.gov.br/wp-content/uploads/desoneracoes/LC_183_2022_Tecnologia_e_Inovacao.pdf) illustrates a distinct incentive recapture, following notice and failure to cure, with credit for reduced-rate tax already paid; it is not a national late-payment formula. In Goiânia the specific call-centre noncompliance provision in [art. 226 §12](https://www.goiania.go.gov.br/html/gabinete_civil/sileg/dados/legis/2021/lc_20210930_000000344.html) addresses retroactive loss from the noncompliance date plus legal additions. Do not apply that specialised consequence to every other benefit without its own provision.

Produce an arrears working paper with the legal due date, actual payment date, calendar adjustments, each legal rate/index and its applicable period, tax already paid and the calculation result. If the current local penalty text is not confirmed, leave the arrears amount pending while completing the supported principal computation and declaration reconciliation. Disputed situs or duplicate municipal demands require a supported correction/refund route; do not offset one city's payment against another's without authority.

## Cross-border points

Domestic intermunicipal services are not exports. Test actual establishment and LC 116 situs before retaining for a purchaser in a different city. Foreign services require the import recipient/intermediary analysis; foreign payments alone do not prove export nonincidence. Use [Brazil cross-border tax](brazil-cross-border-tax.md) for nonmunicipal withholding and international-tax consequences, and [indirect tax](br-indirect-tax.md) for the federal/state classification. An ISS exclusion does not establish the same treatment for every federal levy or CBS/IBS.

Brasília is administered under DF tax competence, not by a municipality. [CF art. 32 §1 and art. 147](https://www2.camara.leg.br/legin/fed/consti/1988/constituicao-1988-5-outubro-1988-322142-normaatualizada-pl.html) allocate the relevant state/municipal powers to DF. Use district legislation and revenue procedures, not another capital's municipal rate or a missing DF row in the municipal CSV archive.

## Two worked examples that recompute

### Belo Horizonte: actual IT consultancy versus general management consultancy

Assume an ordinary service-price taxpayer with a genuine Belo Horizonte establishment, no Simples/fixed regime, exemption or incentive, and no applicable situs exception. The supported contract price is **R$100,000**, an illustrative fact. A contract actually supplying IT consultancy under 1.06 produces **R$2,500 ISS at 2.5%**. A different contract supplying residual management consultancy under 17.01 produces **R$5,000 at 5%**, absent another specific branch. The **R$2,500 difference** is a classification consequence, not an election to rename the same work. If the service is public-opinion research within 17.01, stop and apply art. 14 II(b), rather than the residual branch. [Lei 8.725/2003 art. 14 II(a), II(b), IV](https://fazenda.pbh.gov.br/legislacao/formkey.asp?key=542).

```oa-check
name: BH actual IT versus residual management consultancy
inputs:
  supported_price: 100000
  it_rate: 0.025
  residual_rate: 0.05
steps:
  it_iss: supported_price * it_rate
  residual_iss: supported_price * residual_rate
  difference: residual_iss - it_iss
expected:
  it_iss: 2500
  residual_iss: 5000
  difference: 2500
```

### Curitiba: which supported service branch fits the work?

Assume the same ordinary-regime and situs exclusions above, now with a genuine Curitiba provider and a **R$60,000** supported contract price. If actual performance is the remote technical-assistance service described in art. 4 I(e), §1, delivered through the specified remote channels and supported by the contract/work records, the **2%** branch produces **R$1,200**. If the facts instead establish ordinary IT consultancy outside that branch, **5%** gives **R$3,000**, a **R$1,800** difference. Decide from the actual work, not the more favourable result. Keep a merely unproved claim of remote assistance pending; do not approve the reduced amount from the invoice label. This example assumes no export, no competing specific classification and no special professional regime. [LC 40/2001 art. 4 I(e), IV, §1](https://legisladocexterno.curitiba.pr.gov.br/VisualizarHTML.aspx?id=41).

```oa-check
name: Curitiba actual remote assistance branch versus ordinary IT
inputs:
  supported_price: 60000
  qualifying_remote_rate: 0.02
  ordinary_it_rate: 0.05
steps:
  qualifying_iss: supported_price * qualifying_remote_rate
  ordinary_iss: supported_price * ordinary_it_rate
  difference: ordinary_iss - qualifying_iss
expected:
  qualifying_iss: 1200
  ordinary_iss: 3000
  difference: 1800
```

## Ask the client first

Before computing, obtain these facts from the record and supporting documents:

1. Operation/competence date, actual provider establishment(s), recipient/intermediary location, delivery location and the evidence of the economic/professional unit.
2. Exact contract and deliverable, proposed LC subitem and municipal code, including whether the work is creation, licensing, support, IT consultancy, general consultancy, construction, an import or an export.
3. Legal form, principal/secondary CNAEs where relevant, Simples/MEI or fixed-professional status, and any formal incentive concession, qualifying site, term and continued-compliance evidence.
4. Price, invoices, deductions/materials and supporting documents, purchaser responsibility category, tax already retained/paid, and who must issue, declare and remit in the competent jurisdiction.
5. For property: identifier, location, use, ownership/possession/right, transaction/registration instruments, assessed and declared market values, financed portions, capital allocation and corporate movement.
6. Existing local registration/emitter access, pending returns or assessments, calendar/extension notices, payments, disputes and acknowledgement evidence. Search existing workpapers before asking for facts already held.

## Sources

Read dates mean the stated portions were actually read, not that the whole city code or every amendment was certified. Download receipts and the complete national snapshot are retained in the author evidence packet. The separate [figure/rule ledger](../../library/ledgers/br-municipal-taxes.md) records exact Portuguese anchors, read portions, source limits and the new-file destination inventory. A municipal official host's reproduction and an authority rate card are identified as such; they are not silently described as signed originals.

| Source | Official URL | Read on; portion actually read |
|---|---|---|
| LC116/2003, current Câmara consolidation | https://www2.camara.leg.br/legin/fed/leicom/2003/leicomplementar-116-31-julho-2003-492028-normaatualizada-pl.html | 2026-11-11; Read in: Complete arts. 1-10; list item 1 and relevant item 7, 14.14, 17.01, 17.05 and 17.10, with all adjacent situs, base and responsibility conditions.. Printed destination paragraphs read with STF invalidation; no reliance on the older appendix in the POA collection |
| Current Constitution, CF arts32,147,156 | https://www2.camara.leg.br/legin/fed/consti/1988/constituicao-1988-5-outubro-1988-322142-normaatualizada-pl.html | 2026-11-11; Read in: Complete arts. 32, 147-148 and 156, including the new executive valuation power and corporate-transfer conditions.. No whole-Constitution read claim |
| CTN, current Câmara consolidation | https://www2.camara.leg.br/legin/fed/lei/1960-1969/lei-5172-25-outubro-1966-358971-normaatualizada-pl.html | 2026-11-11; Read in: Complete arts. 29-42 and relevant arts. 144-148 procedural context, including the 2026 amendments.. Includes LC227/2026 changes; current text not treated as proof of a local rate |
| LC227/2026 arts165,181-182 | https://www2.camara.leg.br/legin/fed/leicom/2026/leicomplementar-227-13-janeiro-2026-798657-normaatualizada-pl.html | 2026-11-11; Read in: Complete art. 165 CTN amendments and arts. 181-182 revocation and commencement rules.. CTN amendments fall within182III publication effect; unrelated future provisions not applied |
| LC214/2025 art62 | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm | 2026-11-11; Read in: Complete art. 62 and neighboring arts. 61 and 63; national owner retains implementation details.. National emitter implementation, layouts and CBS/IBS calculations remain sibling owner |
| São Paulo Lei13701/2003 consolidated | https://legislacao.prefeitura.sp.gov.br/lei-13701-de-24-de-dezembro-de-2003/consolidado | 2026-11-11; Read in: Arts. 9 and 9-A responsibility/CPOM context; complete current art. 16 and applicable exceptions.. No claim of a complete city-code audit; taxpayer-specific benefit/retention implementation still required |
| Belo Horizonte Lei8725/2003 consolidated | https://fazenda.pbh.gov.br/legislacao/formkey.asp?key=542 | 2026-11-11; Read in: Complete current art. 14 and sole paragraph; art. 13 professional conditions and arts. 15-22 assessment/retention context.. Historical struck text discarded; currentIIa rate2.5 confirmed |
| BH official historical rate-change table | https://fazenda.pbh.gov.br/bhissdigital/aliquota/index.asp | 2026-11-11; Read in: Table heading, date and column order, including all relevant item 1 and 1.06 rows.. Historical direction is FROM2 to2.5; not reversed |
| Curitiba LC40/2001 consolidated | https://legisladocexterno.curitiba.pr.gov.br/VisualizarHTML.aspx?id=41 | 2026-11-11; Read in: Complete current art. 4, including §§1-2; art. 4-A and relevant arts. 6, 6-A, 6-B, 8, 8-A and 8-B.. Historical duplicated/struck text excluded; CPOM penalty read subject to STF1020 |
| Fortaleza LC159/2013 consolidated throughLC452/2025 | https://www.sefin.fortaleza.ce.gov.br/anexoCT/24/fak3yj2cw.3541423/pdf/C%C3%B3digo%20Tribut%C3%A1rio%20do%20Munic%C3%ADpio%20de%20Fortaleza%20atualizado%20at%C3%A9%20Dez-2025%20-%20LC%20452-2025 | 2026-11-11; Read in: Arts. 240-246, including every current art. 245 clause and amended versions, base/election conditions, and relevant repeal/update notes.. No current indexed autonomous fixed amount inferred from old nominal figures |
| Macapá LC144/2021, official consolidated PDF | https://macapa.ap.gov.br/portal/wp-content/uploads/2023/03/LEI_COMPLEMENTAR_N_144_2021_PMM_com_alteracoes.pdf | 2026-11-11; Read in: Arts. 240-249 and 276-279; Annex XI item 1 and 17.01, with neighboring professional-society conditions.. Read alongside2025LC209 original; not LC110/2014 |
| Macapá signed LC209/2025 original | https://macapa.ap.gov.br/portal/wp-content/uploads/2026/01/LEI_COMPLEMENTAR_209_2025_COMPLETA0064.pdf | 2026-11-11; Read in: Complete arts. 1-42 on original pages 1-10; relevant quoted passages additionally checked visually; annex identity checked.. Unrelied51pagefee table not fully substantively audited; noUFM/taxamount inferred |
| Porto Velho Decreto18749/2023 consolidated | https://sapl.portovelho.ro.leg.br/ta/7519/text | 2026-11-11; Read in: Complete arts. 562-582 on rates, assessment and payment; relevant art. 513 software and base context.. Rate source is regulation implementingLC878; full later statutory amendment chain still partial |
| Porto Velho signed LC1044/2025 | https://sapl.portovelho.ro.leg.br/media/sapl/public/normajuridica/2025/28711/lei_complementar_no_1.044_de_19_de_dezembro_de_2025_sei.pdf | 2026-11-11; Read in: Complete four-page signed original, including amendments, commencement and signature.. Invoice changes effect1Jan2026; no assumption that platform is live for every taxpayer |
| Rio authority ISS rate card reproducing Lei691 art33 | https://carioca.rio/wp-content/uploads/2022/02/Aliquotas-de-ISS-atualizado.pdf | 2026-11-11; Read in: Complete authority rate card, all specific rows and notes, including bespoke software, geography and streaming.. URL2022 directory but text includes later laws; expired unrelated entries not applied; complete2026CTMattachment unavailable |
| Salvador 2026 AnnexIII/TabelaReceitaII | https://www2.sefaz.salvador.ba.gov.br/storage/9732/3.-Anexo-III--Tabela-Receita-II---ISS---Alt-Lei-9.534-9.562-e-9.601-24%2C-9.767-23-E-9.823.2024.pdf | 2026-11-11; Read in: 2026 rate table, especially items 7-8, 13, 21 and 28 and related notes as available through the official web rendering.. Document2026header not proof of extension of expired unrelated programs; currentadmissionrules not fullyconfirmed |
| Goiânia LC344/2021 current consolidation | https://www.goiania.go.gov.br/html/gabinete_civil/sileg/dados/legis/2021/lc_20210930_000000344.html | 2026-11-11; Read in: Complete art. 226, including §§1-14; relevant arts. 212-215 and 228-230 and Annex benefit 23.. Poleimplementation fact not established; historical duplicate versions distinguished |
| Porto Alegre official ISS collection,2024 consolidation | https://prefeitura.poa.br/sites/default/files/usu_doc/sites/smf/Colet%C3%A2nea%20da%20legisla%C3%A7%C3%A3o%20do%20ISS%20-%202024%20v10_04_2024%20VF.pdf | 2026-11-11; Read in: LC 7 art. 21 and Tabela XII item 1, 7.02, 7.05 and 17.01, with replacement and construction commencement notes.. Not a complete2026amendmentcertificate; expiredhealthresearchbenefit not applied |
| Porto Alegre LC998/2023 official record | https://legislacao.portoalegre.rs.gov.br/norma/47805 | 2026-11-11; Read in: Official legislative-record identity and amendment scope, read with the actual table in the full collection.. Record plus fullcollection; nofalseclaimof freshsignedoriginaldocxread |
| DF LC963/2020 current SINJ text | https://www.sinj.df.gov.br/sinj/Norma/40ee803e42a8482399d4507a0c86c9c1/Lei_Complementar_963_03_01_2020.html | 2026-11-11; Read in: Entire arts. 1-3 and Annex, including all IT descriptions and the principal-CNAE condition.. Annexprintedcode formatting typos not silently expanded to absentprincipalCNAEs |
| Aracaju LC183/2022 municipality-hosted reproduction | https://transparencia.aracaju.se.gov.br/wp-content/uploads/desoneracoes/LC_183_2022_Tecnologia_e_Inovacao.pdf | 2026-11-11; Read in: All three pages, complete arts. 1-8, print date and reproduction disclaimer.. LeisMunicipaisprint20Mar2025, not signedgazette; fullcurrentimplementation/amendments pending |
| STF Informativo1007, ADIs1945/5659 | https://www.stf.jus.br/arquivo/informativo/documento/informativo1007.htm | 2026-11-11; Read in: Complete software section, including reasoning, service distinctions, operative conclusion and historical modulation context.. No prior-periodrefundclaim |
| STF Informativo1097, ADIs5835/5862/ADPF499 | https://www.stf.jus.br/arquivo/informativo/documento/informativo1097.htm | 2026-11-11; Read in: Complete ISS destination section, including the actual invalidated provisions and case identities.. No claim to have read unrelatedcasesintheissue |
| STF official Tema1020 judgment explanation | https://portal.stf.jus.br/noticias/verNoticiaDetalhe.asp?idConteudo=461609&ori=1 | 2026-11-11; Read in: Entire official judgment article, including facts, national rule, dissent and thesis.. Thesis quoted from court page; lawfulgenuinelocalregistrationandretention not cancelled |
| STJ qualified precedent Tema174 | https://processo.stj.jus.br/repetitivos/temas_repetitivos/pesquisa.jsp?cod_tema_final=174&cod_tema_inicial=174&novaConsulta=true&tipo_pesquisa=T | 2026-11-11; Read in: Complete qualified-precedent record, including thesis, context, status and dates.. Actualruralusemustbeproven |
| STJ Tema1113 official judgment explanation | https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias/09032022-Base-de-calculo-do-ITBI-e-o-valor-do-imovel-transmitido-em-condicoes-normais-de-mercado--define-Primeira-Secao.aspx | 2026-11-11; Read in: Complete official article, including all three theses and the valuation/art. 148 reasoning.. Read with newCTN38; noautomaticpost2026litigation/refundconclusion |
| STF current Tema1348 docket | https://portal.stf.jus.br/jurisprudenciaRepercussao/verAndamentoProcesso.asp?classeProcesso=RE&incidente=6929423&numeroProcesso=1495108&numeroTema=1348 | 2026-11-11; Read in: Current decision and thesis, October judgment/session-publication entries and neighboring prior votes.. Noassertedacórdaofinality/transit/modulation |
| STF Tema796 docket | https://portal.stf.jus.br/jurisprudenciaRepercussao/verAndamentoProcesso.asp?classeProcesso=RE&incidente=4529914&numeroProcesso=796376&numeroTema=796 | 2026-11-11; Read in: Thesis, case issue, finality entry and neighboring judgment context.. Immunitylimitedtocapitalbeingintegralised; novaluationelectioninvented |
| STF current Tema1124 docket | https://portal.stf.jus.br/jurisprudenciaRepercussao/verAndamentoProcesso.asp?classeProcesso=ARE&incidente=6031137&numeroProcesso=1294969&numeroTema=1124 | 2026-11-11; Read in: Current latest entries, complete 2022 embargos context and the earlier 2021 decision distinguished.. No finalmeritsthesis; pendingassignmentbranch |
| São Paulo official ISS payment procedure | https://coleta.prefeitura.sp.gov.br/web/fazenda/w/servicos/iss/2486 | 2026-11-11; Read in: Complete operative payment paragraph and invoice/declaration-specific guide routes.. Specialregimes/calendar/bankingdayconditionsnotinferred |
| BH Decreto17649/2021 | https://fazenda.pbh.gov.br/internet/legislacao/formkey.asp?key=1124 | 2026-11-11; Read in: Complete decree arts. 1-3, including amended regulation art. 13 and effective-period clause.. Currentgeneraldeadline; separatespecialretention/exceptions stillrequirefacts |
| Curitiba registered-company ISS procedure | https://www.curitiba.pr.gov.br/conteudo/iss-com-inscricao-municipal-para-empresas/357 | 2026-11-11; Read in: Operative electronic bookkeeping, DAM and payment paragraphs, including the federal-body exception.. Exactcompetence/calendar/currentemittermustbematched |
| Cuiabá ISSnet public current notice/menu | https://onlinecba.issnetonline.com.br/cuiaba/online/login/login.aspx | 2026-11-11; Read in: Actual browser capture nodes 82-115 for the notice and 144-180 for current download identities; attachment contents not read.. Normalverificationcompletedautomatically; noCAPTCHAsolved; CTMattachmentstillnotread |
| NFS-e platform rates publication | https://www.gov.br/nfse/pt-br/biblioteca/aliquotas | 2026-11-11; Read in: Complete dataset-description section and the actual dated download identity.. Coverageassertionispublicationdescription, not everycapitalrowguarantee |
| NFS-e rate snapshot3Sep2026 | https://www.gov.br/nfse/pt-br/biblioteca/aliquotas/aliquotas-municipios-20260903-extr1.zip | 2026-11-11; Read in: ZIP inventory and header; all capital rows machine-extracted and selected exact service/date intervals read; CLI supports every municipality in the archive.. Platformregisteredrate only; noDFCSV; nolegalrateconfirmation |

Not yet confirmed: full current ordinary ISS rate/benefit and filing/payment law for Rio Branco, Maceió, Manaus, Vitória, São Luís, Cuiabá, Campo Grande, Belém, João Pessoa, Recife, Teresina, Natal, Boa Vista, Florianópolis and Palmas; current complete amendment chains/administrative calendars beyond the expressly read portions for other capitals; Goiânia pole implementation and taxpayer-specific entitlement; Salvador formal RENOVACENTRO admission/current implementing conditions and unresolved table-note sunsets; Aracaju original gazette/current implementing act and later amendment chain; Rio's complete 2026 consolidated attachment and unrelated benefits; Porto Alegre amendments after the dated 2024 collection; Porto Velho's complete statutory amendment chain and taxpayer-specific current issuer; local fixed-professional annual values, property rates/valuation schedules, discounts, nonworking-day adjustments, nil-return rules and penalty/interest computations not expressly confirmed above; definitive post-LC227/2026 valuation-litigation effects and final Tema1124 merits. These remain ordinary partial coverage; no unsupported rate, deadline or arrears amount is supplied.
