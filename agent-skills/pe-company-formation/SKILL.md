---
name: pe-company-formation
description: "Form a company or individual limited liability enterprise in Peru in 2026. Use this Guide for entity choice, SAC versus SA versus SRL versus EIRL, the SACS digital alternative, name reservation, capital contributions, constitutive documents, the SID SUNARP notary workflow, digital signatures, registration evidence, and SUNAT RUC activation. It distinguishes subscribed capital from paid capital, bank deposit evidence from payment method rules, and registration review periods from the time needed to complete formation. It also sets the first compliance handoffs for income tax, IGV, payroll, accounting records, annual corporate decisions and beneficial ownership. Match questions about incorporating in Peru, opening a Peruvian company, obtaining a company RUC or choosing a legal form."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/pe-company-formation"
  jurisdiction: "PE"
  tax_year: "2026"
  last_updated: "2026-11-11"
---

# Peru Company Formation and Entity Choice v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to


For 2026, use this workflow to choose and register an ordinary Peruvian SA, SAC, SRL or EIRL, or an eligible SACS, then activate its tax registration. Start with the ownership and contribution facts. Registration with SUNARP creates the legal person; an assigned RUC still needs activation with SUNAT. [Ley 26887, art. 6](https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=15); [Decreto Ley 21621, art. 13](https://www.leyes.congreso.gob.pe/Documentos/Leyes/21621.pdf); [SUNAT company registration flow](https://centrovirtual.sunat.gob.pe/tramites/inscribete-ruc).

This is a formation and onboarding Guide. It does not compute annual income tax, IGV or payroll liabilities. Open companies, securities offerings, regulated financial businesses, reorganisations and foreign-company branches need a separate legal analysis before using standard incorporation documents.

### Quick reference: choose the form before opening the application

| Form | Ownership, governance and capital conditions | Official text and short original wording |
|---|---|---|
| Sociedad Anónima, SA | At least 2 founders, natural or legal persons, subject to the statutory plurality exceptions. Capital is divided into shares; shareholders do not personally answer for company debts. Board and management are required; a board has at least 3 directors. Check whether the open-company rules apply before using the ordinary SA route. | [Ley 26887, arts. 4, 51, 152, 155 and 249](https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=15): “cuando menos por dos socios”; “no es menor de tres”. |
| Sociedad Anónima Cerrada, SAC | 2 to 20 shareholders under the general plurality rule and the SAC ceiling. Its shares cannot be registered in the public securities market register. The constitution may dispense with the board; in that case the general manager exercises its functions. | [Ley 26887, arts. 4, 234, 236 and 247](https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=15): “no más de veinte accionistas”; “no tiene directorio”. |
| Sociedad Comercial de Responsabilidad Limitada, SRL | 2 to 20 partners, subject to the general plurality exceptions. Interests are participaciones, not shares or negotiable securities. Partners do not personally answer for company obligations; management is by one or more managers. | [Ley 26887, arts. 4, 283 and 287](https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=15): “ni denominarse acciones”. |
| Empresa Individual de Responsabilidad Limitada, EIRL | A single natural-person owner, with its own separate patrimony. Liability is limited to the enterprise's patrimony subject to the personal-liability exceptions in art. 41. This is not a corporation with a sole corporate shareholder. | [Decreto Ley 21621, arts. 1, 3, 4 and 41](https://www.leyes.congreso.gob.pe/Documentos/Leyes/21621.pdf): “constituida por voluntad unipersonal”; “Sólo las personas naturales”. |
| Sociedad por Acciones Cerrada Simplificada, SACS | 2 to 20 natural-person founders. On formation, contributions can only be money, movable assets not subject to registration, or both; capital must be fully subscribed and paid. Limited liability is subject to the decree's labour-fraud and tax qualifications. A board is optional. | [DL 1409, arts. 4 and 6; DS 312-2019-EF, arts. 6 and 11](https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=31): “personas naturales”; “pagado totalmente”. |

SUNARP's [live entity comparison](https://sid.sunarp.gob.pe/sid/informa.htm?method=goConstEmp) separately lists SAC and SACS with and without a board. Choose the actual governance arrangement, rather than assuming that every company needs a board or that the simplified route accepts a corporate investor.

**MYPE switch:** establish eligibility for the special formation simplification before applying the general capital-payment or minuta rules below. A small capital amount alone does not establish MYPE status.

### Required inputs at a glance

Founder types and count; ownership/control; business activity and location; cash/assets and paid capital; administrators and digital-signature access; start date and tax profile. Obtain the detailed facts listed under Ask the client first before opening the application.

## Rates, bands and thresholds

| Rule for the chosen form | Required action and condition | Official source |
|---|---|---|
| SA and SAC general payment proportion | Outside the MYPE simplification below, subscribe all capital and pay at least one quarter of **each** subscribed share on formation. A total payment that leaves some shares below the required proportion does not satisfy the rule. No services may be contributed as SA share capital. | [Ley 26887, arts. 51, 52 and 236](https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=15): “cada acción suscrita pagada por lo menos en una cuarta parte”. |
| Ordinary company cash contributions | Outside the MYPE evidence exception below, the contribution shown as paid must be deposited in the company's name when the deed is executed, in a national financial-system entity or a qualifying registered Coopac. The Coopac must operate only with members, have no authorisation to take public deposits or operate with third parties, and be in the statutory national register. | [Ley 26887, art. 23, amended by Ley 30822 art. 9](https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=15): “debe estar depositado, a nombre de la sociedad”. |
| Ordinary company non-cash assets | Prepare the valuation report identifying the assets or credit rights, valuation criteria and value for insertion in the deed. Complete delivery under the applicable asset rule. | [Ley 26887, arts. 25 to 27](https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=15): “debe insertarse un informe de valorización”. |
| SRL general capital rule | Outside the MYPE simplification below, pay at least 25% of each participation on constitution, with the deposit required by art. 285 in a national banking or financial entity in the company's name. Arrange the evidence for any non-cash contribution with the notary. | [Ley 26887, arts. 22 to 27 and 285](https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=15): “veinticinco por ciento de cada participación”. |
| EIRL money or assets | Outside the MYPE cash-evidence exception below, deposit cash in a bank account in the enterprise's name and insert the receipt in the deed. For non-cash contributions, insert the detailed valued inventory under the notary's responsibility. | [DL 21621, arts. 18 to 21](https://www.leyes.congreso.gob.pe/Documentos/Leyes/21621.pdf): “El comprobante del depósito será insertado”; “inventario detallado y valorizado”. |
| SACS fully paid capital | Pay all subscribed capital. For financial-system payment use the module's **Constancia de constitución en trámite** and upload deposit evidence; see the MYPE cash option below. For eligible non-cash movables, prepare the valuation and the general manager's digitally signed receipt declaration. | [DL 1409, art. 6; DS 312-2019-EF, arts. 9, 12, 13 and 19](https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=31). |
| MYPE formation simplification | Eligible MYPE using the ordinary deed route do not need a separate minuta or payment of a minimum proportion of subscribed capital. A manager's sworn declaration accredits cash shown as paid and is recorded in the deed. This evidence exception does not waive applicable means-of-payment law or the SACS requirement for fully paid capital. | [DS 013-2013-PRODUCE TUO, arts. 4 to 6 and 10, incorporating Ley 29566 art. 3](https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=76): “no requieren del pago de un porcentaje mínimo”; “declaración jurada del gerente”. |
| S/1,000 bank practice | Official business guidance recommends this amount to open an account because of bank account costs. It is a recommendation, not a statutory capital floor and not a guaranteed requirement at every bank. | [PRODUCE, Abono de capital y bienes](https://www.gob.pe/273-abono-de-capital-y-bienes): “La recomendación es contar con un monto mínimo de S/ 1,000.00”. |
| Separate means-of-payment rule | Cash payments for acquiring, increasing or reducing a participation in a legal person's capital, at amounts **equal to or greater than 1 UIT**, must use the statutory payment means, including partial payments. The 2026 UIT is S/5,500. Keep supporting payment documents for the formalising instrument. This rule does not replace the formation deposit rules above. | [TUO Ley 28194, art. 3, as amended by DL 1529](https://www.sunat.gob.pe/legislacion/itf/ds150_07.pdf): “iguales o superiores a una (1)”; [SUNAT UIT table, DS 301-2025-EF](https://www.sunat.gob.pe/indicestasas/uit.html): “2026”, “5,500”. |

The general SA/SAC and SRL articles above prescribe subscription and payment proportions, rather than a general S/1,000 capital amount. Assess the business's funding needs, MYPE eligibility and special-sector capital requirements before approving the proposed capital. Do not turn a bank's commercial opening condition into company law.

## The base

### Confirm the MYPE branch

For the formation simplification, identify an eligible micro or small enterprise under [DS 013-2013-PRODUCE TUO, arts. 4 to 6 and 10](https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=76): microenterprise annual sales up to **150 UIT**, small enterprise above **150 UIT** and up to **1,700 UIT**. Apply the economic-group, linkage, false-information and business-splitting exclusions. Do not confuse this enterprise classification with electing the Régimen MYPE Tributario for income tax.

**Transition check:** Ley 32353 makes its own commencement conditional on the day after publication of its regulation, under its ninth final provision. The official compilation read for this Guide still annotates that the regulation has not been published. Accordingly, this Guide uses the existing TUO formation exception and does not activate the replacement law's new filing arrangements merely because the law was published. [Official MYPE compilation, opening annotation and Ley 32353 ninth final provision](https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=76).

### Constitutive documents

The constitutive act (**minuta**) records the founders' intention to form the enterprise and its business activities. For an ordinary non-MYPE route, prepare it before the public-deed stage. The MYPE exception above removes the requirement for a separate minuta, not the need to settle and record the constitutive terms. [PRODUCE, Elaborar un acto constitutivo (minuta)](https://www.gob.pe/272-elaborar-el-acto-constitutivo-minuta).


For an SA or SAC, prepare the **pacto social** and **estatuto**: founders and representation evidence; intention to incorporate; capital, shares and each contribution; first administrators; name, object, domicile, duration, paid amount per share, governance, capital changes, annual approval and distributions. Record explicitly whether a SAC has no board. [Ley 26887, arts. 5, 54, 55 and 247](https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=15).

For an SA or an SAC with a board, obtain each elected director's express written acceptance of office, with the signature legalised before a notary or judge as applicable. Annex the acceptance to the incorporation documents for SUNARP registration. This covers titular, alternate, substitute and replacement directors as applicable; it is not a requirement for a SAC that validly has no board. [Ley 26887, art. 152-A](https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=15): “acepta el cargo de director de manera expresa por escrito”; “legaliza su firma ante notario público o ante juez”. The separate SACS route below generates its applicable director-acceptance declaration for digital signature.

For an SRL, use participations and manager-based governance in the SRL document, not an SA share template. [Ley 26887, arts. 283 to 287](https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=15).

For an EIRL, identify its natural-person owner, nationality, marital and spouse information where relevant, domicile, enterprise name and object, contributions and valuation, capital, organs and first manager. The public deed and registration are required under [DL 21621, arts. 13 to 16](https://www.leyes.congreso.gob.pe/Documentos/Leyes/21621.pdf). Do not copy obsolete or unrelated provisions from a historical scan into the application without checking later amendments.

### Boundary and exception table


| Fact that changes the answer | Result |
|---|---|
| One natural-person founder | Assess EIRL; do not invent a second shareholder or use SAC/SACS with only one founder. [LGS art. 4](https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=15); [DL 21621, arts. 1 and 4](https://www.leyes.congreso.gob.pe/Documentos/Leyes/21621.pdf). |
| A corporate investor or registered immovable contribution at formation | SACS is unavailable on these facts. Consider an ordinary form and its contribution requirements. [DL 1409, arts. 4 and 6](https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=31). |
| SAC without a board | Put the choice in its pacto or statute; the general manager takes the board's statutory functions. [LGS art. 247](https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=15). |
| SACS documents not signed before the formation clock expires | The formation process expires; name protection and non-refund consequences must be checked before restarting. [DS 312-2019-EF, arts. 8, 17 and 18](https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=31). |
| Foreign founder, overseas corporate chain or documents signed abroad | Resolve identity, representation and document acceptance with the notary/registry before submission. SACS natural-person ownership and digital-certificate requirements still apply. Do not infer tax residence or treaty entitlement from incorporation alone. [LGS art. 54](https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=15); [DS 312-2019-EF, arts. 6, 9 and 16](https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=31). |

## Deadlines and filing

### Select the legal route and name


Use the notary route below for SA, SAC, SRL and EIRL. Use the separate SACS module only when its founder, contribution and digital-signature conditions are met. SUNARP's [ordinary SID service](https://www.gob.pe/10580-constituir-tu-empresa-a-traves-de-la-plataforma-sistema-de-intermediacion-digital-sid-sunarp) generates constitution formats for the four ordinary forms and sends them to a chosen notary. Its [SACS service](https://www.gob.pe/26692-constituir-tu-empresa-como-sociedad-por-acciones-cerradas-simplificadas-sacs) expressly says “no requiere de una escritura pública”.

For ordinary name reservation, open [SID Ciudadanos](https://sidciudadano.sunarp.gob.pe/sid/sesion.htm), sign in or register, select **Reserva de Nombre**, complete the requested data, review the service terms, choose **Enviar a Sunarp**, select the payment method and send the paid application. Keep the submission and payment evidence. The [current reservation service instructions](https://www.gob.pe/271-buscar-y-reservar-el-nombre-de-una-empresa) say “No es un trámite obligatorio”, but recommend it. The ordinary SID formation page asks for reservation before that workflow, so complete it as a preparation step for that route. Do not present this portal instruction as a universal statutory obligation or confuse a name reservation with incorporation.

For SACS, validate the name inside **Genera tu acto constitutivo de la SACS**. The provisional name protection forms part of that process and can expire when the formation period expires. [DS 312-2019-EF, arts. 7 and 8](https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=31).

### Complete ordinary SID filing with the notary


Follow the [SUNARP citizen requirements, steps 3 to 5](https://sid.sunarp.gob.pe/sid/recursos/Requisitos/requisitos_para_el_cumplimiento.pdf), together with the [ordinary SID service instructions](https://www.gob.pe/10580-constituir-tu-empresa-a-traves-de-la-plataforma-sistema-de-intermediacion-digital-sid-sunarp):

1. Enter [SID SUNARP](https://sid.sunarp.gob.pe/sid/login.htm) through the citizen/notary access and use the registered account. Select **Solicitud de trámite de constitución de empresa** or the **Solicitud de Constitución de Empresas** icon.
2. Review and accept the terms, select the notary and then the legal-person type.
3. Verify **datos del Solicitante**. Complete the company data, **domicilio**, **objeto social**, **capital social** and **participantes**. Check these against the approved constitution and contribution evidence.
4. Download and review the generated constitutive-act PDF. Select **FINALIZAR** to send it to the selected notary. Save the **Constancia de envío de solicitud de constitución de empresas** and the application number for the notary.
5. Attend the notary to execute the public deed and provide the contribution and identity documents, plus each applicable director's written acceptance with legalised signature for annexing to the incorporation documents under [Ley 26887, art. 152-A](https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=15). The citizen instructions give **30 calendar days after sending the information** to sign; otherwise the submitted information is removed. This portal window differs from the legal filing period below.
6. The notary processes the request and transmits the digitally signed notarial instrument to SUNARP. Monitor the email containing the title number, presentation date/time and registration review result. Retain any observation and the correction submitted.
7. Once registered, download the registration entry, registration annotation and assigned RUC evidence from the email links. Proceed to activation; receiving the number alone does not finish tax onboarding.

**Timing:** [Ley 26887, art. 16](https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=15) requires presentation of the pacto and statute within **30 days from execution of the public deed**. [DL 21621, art. 16](https://www.leyes.congreso.gob.pe/Documentos/Leyes/21621.pdf) states the EIRL inscription period from its deed. SUNARP's ordinary SID page states a **24-hour calificación period**. That is not an end-to-end promise covering document preparation, bank arrangements, notary execution and corrections. Do not reuse a generic completion estimate as a filing deadline.

The older citizen PDF also prints historical fee amounts. Use it for the named workflow controls, not as the current tariff schedule.

### Complete the SACS digital route


Use the [SACS service page](https://www.gob.pe/26692-constituir-tu-empresa-como-sociedad-por-acciones-cerradas-simplificadas-sacs) and [DL 1409, arts. 6 to 10; DS 312-2019-EF, arts. 7 to 23](https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=31):

Before reserving the denomination, identify every required signer and confirm that each has an activated DNIe or other accredited digital certificate and the equipment needed to use it. Include the founders, general manager, other managers whose signatures the generated application requires, directors where there is a board, and the applicable spouse of a founder contributing nonregistrable movables. The spouse prerequisite is tied to that contribution condition, not to every married founder in an all-cash case. [SUNARP SACS manual v1.3, p. 4](https://cdn.www.gob.pe/uploads/document/file/5377042/4813673-manual-de-usuario-modulo-sacs-sid-sunarp.pdf?v=1699296963): “Este requisito aplica también para el (la) cónyuge del socio (a) que aporta bienes muebles no registrables”.

1. In SID SUNARP select **constitución de empresas sin intervención del notario - módulo SACS**, then **Genera tu acto constitutivo de la SACS** and validate the denomination.
2. Complete the structured fields: founders' identity, birth date, nationality, occupation, marital status, spouse/registered partner where applicable, address and residence country; company domicile, duration and object; fully paid capital, number and nominal value of shares, each founder's contribution and allocation; first administrators and their powers; governance and statute.
3. For cash capital choose the contribution payment route. For a financial-system deposit, obtain the pending-constitution certificate, make the deposit, then use **Elegir archivo** and **Adjuntar** to upload the supporting image in JPG, JPEG or PNG. The official manual enables **entrega en efectivo** when the SACS MYPE checkbox is selected; use the generated manager's cash-receipt declaration where lawful, and do not treat this checkbox as overriding mandatory payment-method evidence. For eligible non-cash movables include the valuation and identify the goods in the manager's receipt declaration.
4. Review the generated PDF and use **Anterior** to correct it before **Enviar**. Once sent for signatures, it cannot be modified. Signatories receive an email link or use **FIRMA TU SACS**. Review the generated pacto, statute and declarations: truth of information, lawful origin of funds, asset receipt where applicable, and director acceptance if applicable. Obtain the required digital signatures from the founders, general manager, applicable other managers and directors, and the spouse where the nonregistrable-movable contribution condition above applies. Each uses DNIe with reader or another accredited digital certificate. Repeat the signing process for every required intervener before the 72-hour formation period expires. [SUNARP SACS manual v1.3, pp. 4, 25 and 29](https://cdn.www.gob.pe/uploads/document/file/5377042/4813673-manual-de-usuario-modulo-sacs-sid-sunarp.pdf?v=1699296963).
5. Finish document formation and all required signatures within **72 hours** from provisional name incorporation in the module. The period includes the bank document image and declarations; expiration automatically ends the formation process. The electronic formation service fee is not refunded on expiry or withdrawal. Do not start the name clock before the signatories and bank arrangements are ready.
6. In **Acto Constitutivo pendiente de Concluir**, select the application marked **Firmado y listo para enviar a SUNARP** and use **Enviar a SUNARP**. Select payment of the review charge or the full review/registration charges as offered by the module. Complete the generated **solicitud de inscripción** and include the **número y fecha de constancia de pago de derechos**. After payment use **Validar y enviar a SUNARP**. The system generates the title number and **cargo de recepción de solicitud**; retain them and monitor **Estado del trámite Registral**. Send the electronic constitutive document, required declarations and applicable contribution evidence through SID. If only the review charge was paid, pay the remaining registration charge when assessed. Observations, corrections and registration annotations also use SID.
7. The regulation specifies **1 business day** for the registrar's review, including the specified re-entries, within the presentation entry's validity. Prior evaluation is subject to negative administrative silence; elapsed time is not an approval. Check the email for the registration annotation, entry, RUC and any observation. The representative then obtains Clave SOL and activates the RUC.

The [official SACS manual, pp. 4, 14 to 25, 29 and 31 to 34](https://cdn.www.gob.pe/uploads/document/file/5377042/4813673-manual-de-usuario-modulo-sacs-sid-sunarp.pdf?v=1699296963) supplies the signer prerequisites, MYPE checkbox, contribution route, upload controls, signature sequence and final submission states above. A cash-receipt declaration is also published among [SUNARP's standard forms](https://www.gob.pe/institucion/sunarp/informes-publicaciones/4084275-formatos-estandarizados-de-constitucion-de-sacs). Do not reuse the old monetary brackets in that 2020 form list as 2026 banking limits.

The digital route dispenses with the public deed for the constitutive act. Later corporate acts follow the general statutory formalities; the original digital incorporation is not an exemption for every later amendment. [DL 1409, art. 11](https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=31).

### Activate the RUC and select the tax obligations


The RUC has **11 digits**. SUNAT's [RUC onboarding page](https://centrovirtual.sunat.gob.pe/tramites/inscribete-ruc) distinguishes company registration through SID from personal registration through App Personas. Do not send a company's representative through the personal new-business route as though the person and the company were the same taxpayer.

First obtain the company's access through [Genera tu Clave SOL](https://ww1.sunat.gob.pe/ol-ti-itadminforuc-inscripcion/inscripcion). The public form has **Persona Jurídica**, **Número de RUC**, representative's identity-document type and number, and DNI issue date where applicable. Complete the official identity and contact validation. [SUNAT's Clave SOL instructions](https://centrovirtual.sunat.gob.pe/tramites/clave-sol) say the representative enters the company's RUC and validates the selected email or mobile contact through a verification code. The representative completes credential creation personally.

Then follow [SUNAT, Activar RUC de persona jurídica](https://www.gob.pe/11125-activar-ruc-de-persona-juridica):

1. Log into [SUNAT Operaciones en Línea](https://e-menu.sunat.gob.pe/cl-ti-itmenu/MenuInternet.htm) with Clave SOL and choose **Empresas**.
2. Follow **Mi RUC y otros Registros / Inscripción al RUC de Personas Jurídicas / RUC PJ / Inscripción al RUC de Personas Jurídicas**.
3. Enter the trading name, start date, principal and secondary activities, fiscal address and contact information in the online registration form. Identify the activity using CIIU, as required by SUNAT's onboarding guidance.
4. Select the eligible **Especial**, **MYPE Tributario** or **General** regime after checking activity and projected-income conditions. A legal person cannot use Nuevo RUS; the [official regime comparison](https://emprender.sunat.gob.pe/ruc/regimenes-tributarios-mype/regimenes-tributarios) restricts it to natural persons. Choosing a company form does not itself prove eligibility for a particular business tax regime.
5. Check the preview of the registration record before activation and retain the resulting RUC information. On the next login complete the security question/answer requested by SUNAT. Reconcile the name, representative, start date, fiscal address, activity and tax obligations with the incorporation file before preparing returns.

These are public official instructions and publicly visible form fields, not a claim that a client account was accessed or a registration submitted during preparation of this Guide.

### Establish the first compliance calendar


Formation does not make every subsequent filing apply automatically. Record the applicable regime and actual activities, then assign these tasks:

| Topic | Onboarding action and condition | Official source |
|---|---|---|
| Income tax and IGV | RER has monthly declarations; RMT and General have monthly and annual declarations. Establish the applicable monthly income-tax and IGV obligations from the selected regime and transactions. Use the separate corporate income tax and IGV Guides for computation and return preparation. | [SUNAT regime comparison, declaration and obligations rows](https://emprender.sunat.gob.pe/ruc/regimenes-tributarios-mype/regimenes-tributarios): “Sólo Declaración Mensual”; “Declaración Mensual y Anual”. |
| Books and electronic records | Determine the records required by regime and income level; for a business starting during the year use projected income. Separately establish whether the company must use electronic records and which system applies. Do not promise that the same electronic books apply to every new company. | [SUNAT, Libros y Registros Obligatorios](https://orientacion.sunat.gob.pe/libros-y-registros-obligatorios): “considerarán los ingresos que estimen obtener”. |
| Payroll and service-provider reporting | Where Planilla Electrónica applies, register the employer using **Alta** in T-Registro and complete the applicable labour/social-security indicators. Establish monthly PLAME reporting for covered workers and other reportable persons. Use the payroll Guide for the current filing channel and calculation. | [SUNAT employer registration](https://www.sunat.gob.pe/ayuda/tributos/tregistro-E-P/T-Registro-H01.html); [SUNAT PLAME FAQs](https://orientacion.sunat.gob.pe/3246-05-preguntas-frecuentes-pdt-plame), including reportable fourth-category service providers. |
| SA/SAC annual meeting | Schedule the mandatory annual general meeting at least once within **3 months after the financial year ends**, including financial results and appropriation of profits; apply SAC's supplementary SA rules and SACS's supplementary LGS/SAC rules. Do not impose a shareholders' meeting on an EIRL. | [Ley 26887, arts. 114 and 236](https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=15), and [DL 1409 seventh final provision](https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=31): “dentro de los tres meses siguientes”. |
| SRL and EIRL decisions | Follow the SRL statute and partner-decision rules. For EIRL, the owner approves or rejects each year's accounts and balance and records decisions in the legalised minutes book. | [Ley 26887, art. 286](https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=15); [DL 21621, arts. 39 and 40](https://www.leyes.congreso.gob.pe/Documentos/Leyes/21621.pdf). |
| Beneficial ownership | Collect the natural-person ownership/control evidence, establish the first filing period below and retain subsequent update obligations. The declaration is not an automatic annual return. | [SUNAT beneficial-owner guidance](https://emprender.sunat.gob.pe/declaracion-pagos/declaracion/beneficiario-final): “No, solo cuando la información declarada deba ser actualizada”. |

**Beneficial-owner first filing for a new domestic company:** [RS 000168-2025/SUNAT, art. 3(a)(ii.4) and (c)](https://www.sunat.gob.pe/legislacion/superin/2025/000168-2025.pdf) places companies registering/obtaining and, where needed, activating their RUC between **1 January 2025 and 30 November 2026** in the **November 2026 period** timetable. If activation in that case occurs from **1 December 2026**, use the activation-period timetable. Companies registering/obtaining a RUC after **30 November 2026** use the registration/activation-period timetable, as applicable. These are tax periods: use the corresponding monthly due date for the RUC, not the last day of the named month. Existing companies must also test earlier commencement cohorts rather than assuming this new-company route resets a missed obligation.

For filing, use SOL: **Mis declaraciones informativas / Presento mis declaraciones informativas / Informativas / Presentación de declaraciones informativas**, then **Formulario Virtual 3800 - Declaración de Beneficiario Final**. Enter the requested ownership/control information and use the required Excel-generated files for cases outside the simplified form. Direct entry alone is allowed only for a single beneficial owner resident in Peru with at least **10% direct capital ownership**. Keep the system's filing confirmation in the electronic mailbox. [SUNAT filing instructions](https://emprender.sunat.gob.pe/declaracion-pagos/declaracion/beneficiario-final), implementing RS 185-2019/SUNAT, art. 6.

### Filing payments


Pay the applicable registry and service charges through the selected portal and retain the reference, date and receipt. Agree notarial charges with the selected notary for the ordinary route. Keep capital deposits separate from fees and taxes in the working papers. Neither the subscription amount nor the S/1,000 account recommendation estimates total formation costs. Current 2026 fees are not established by the old PDF or a historical webpage amount.

For SUNAT filings, set the calendar using the activated RUC, applicable regime, transaction profile and monthly schedule. The November 2026 beneficial-owner period above does not remove monthly tax obligations arising before that period.

### Completion checklist


- The chosen legal form matches founder types, contribution types and governance, and the constitutive document matches the actual share/participation allocation.
- Paid and subscribed capital reconcile per founder and per share/participation; deposit or asset-valuation evidence supports the document.
- The application, payment references, notarial instrument where applicable, observations and corrections are retained.
- SUNARP's registration entry and annotation have been downloaded; the assigned RUC agrees with the registered enterprise.
- Clave SOL and RUC activation are complete; the fiscal address, CIIU, start date and regime have been checked against the client facts.
- The first tax, payroll, books, annual corporate decision and beneficial-owner tasks have owners and due-date calculations.

## Penalties and interest

Do not treat registration as approval of tax elections, licensing, immigration, a foreign founder's residence, or every liability protection. For example, [LGS art. 7](https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=15) conditions pre-registration company acts on registration and ratification within **3 months afterwards**, otherwise exposing the actors to personal, unlimited and joint liability. [DL 21621, arts. 3, 14 and 41](https://www.leyes.congreso.gob.pe/Documentos/Leyes/21621.pdf) also prevents an unconditional EIRL liability promise.

The SACS formation fee is not refunded when the formation period expires or the applicant withdraws. [DS 312-2019-EF, art. 18](https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=31). No general incorporation penalty or interest amount is asserted here; tax penalties depend on the missed obligation and belong in the relevant filing Guide.

## Cross-border points

Stop the standard application and obtain Peruvian legal review if the facts concern a public offering/open company, a regulated activity, disputed ownership, an unsuitable contribution, unsupported identity or representative authority, or a SACS signatory unable to complete accredited digital signing. Refer valuation and foreign-document acceptance issues before the signing clock starts.

For an overseas founder, identify the actual investor and representative and check document acceptance before execution. Do not infer residence or treaty entitlement from registration. The founder and residence fields in [LGS art. 54](https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=15) and [DS 312-2019-EF, art. 9](https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=31) must still be completed.

## Two worked examples that recompute


### Case A: cash-funded SAC or SACS

Assume two natural-person founders want equal ownership, no board and only cash capital. Assume the business is outside the MYPE formation simplification. They can consider a SAC or, with all required digital certificates and other eligibility conditions met, a SACS. They propose **80 shares of S/100**, or **S/8,000** total subscribed capital.

For a SAC, paying **S/25 on every share** meets the one-quarter rule: **S/2,000** paid capital, with **S/6,000** remaining subscribed but unpaid. The deed must accurately show that distinction and the paid cash needs the general deposit evidence. For an eligible MYPE, re-run the decision with its separate formation simplification rather than imposing this minimum. A SACS instead requires the whole **S/8,000** paid on formation. A preference for paying only S/2,000 therefore points to SAC rather than SACS on these assumed non-MYPE facts; this is a legal-payment comparison, not a forecast of formation costs. [LGS arts. 23, 52, 236 and 247](https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=15); [DL 1409, art. 6](https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=31).

```oa-check
name: SAC minimum paid capital versus fully paid SACS
inputs:
  shares: 80
  nominal_per_share: 100
  sac_paid_fraction: 0.25
steps:
  - subscribed_capital: shares * nominal_per_share
  - sac_paid_per_share: nominal_per_share * sac_paid_fraction
  - sac_paid_capital: shares * sac_paid_per_share
  - sac_unpaid_capital: subscribed_capital - sac_paid_capital
  - sacs_paid_capital: subscribed_capital
  - additional_cash_for_sacs: sacs_paid_capital - sac_paid_capital
expected:
  subscribed_capital: 8000
  sac_paid_per_share: 25
  sac_paid_capital: 2000
  sac_unpaid_capital: 6000
  sacs_paid_capital: 8000
  additional_cash_for_sacs: 6000
```

### Case B: change one founder and the route changes

Keep Case A's ownership percentages and capital, but replace a founder with a legal person. The SACS route fails because its shareholders must be natural persons; an ordinary SAC can have natural or legal-person founders. Alternatively, if the business has only a single natural-person founder, assess EIRL and its owner/deposit rules. These changes cannot be fixed by selecting a different option in the same SACS form. [LGS art. 4](https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=15); [DL 1409, art. 4 and DS 312-2019-EF, art. 6](https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=31); [DL 21621, arts. 1, 4 and 20](https://www.leyes.congreso.gob.pe/Documentos/Leyes/21621.pdf).

## Ask the client first


Obtain these six fact groups before choosing the form or entering data:

1. The number and identity of founders, whether each is a natural or legal person, nationality, residence, marital status and any spouse or registered partner details relevant to contributions.
2. The business activity and proposed object, intended operating locations, registered domicile and fiscal address, and whether the activity requires a special legal form or permission.
3. Who will own each share or participation, who ultimately owns or controls those investors, and whether later corporate investment or a securities offering is planned.
4. Total subscribed capital, nominal value and allocation, amount paid by each founder, cash versus assets, asset registration status, valuation and source of funds, plus MYPE eligibility and group connections.
5. Proposed managers, representative powers and board choice; ordinary-route directors' written acceptance with legalised signatures where required; and accredited digital-certificate access for every SACS signer, including applicable other managers, directors and the spouse of a founder contributing nonregistrable movables. [Ley 26887, art. 152-A](https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=15); [SUNARP SACS manual v1.3, pp. 4, 25 and 29](https://cdn.www.gob.pe/uploads/document/file/5377042/4813673-manual-de-usuario-modulo-sacs-sid-sunarp.pdf?v=1699296963).
6. Intended start date, projected business income and transactions, employees or service providers, contact details, selected notary where applicable, and whether a RUC or Clave SOL has already been assigned.

The document fields come from [Ley 26887, arts. 54 and 55](https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=15), [DL 21621, art. 15](https://www.leyes.congreso.gob.pe/Documentos/Leyes/21621.pdf), [DS 312-2019-EF, arts. 9 and 10](https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=31), and [SUNAT's RUC activation requirements](https://www.gob.pe/11125-activar-ruc-de-persona-juridica).

## Sources


Read dates below mean actual content reads on 2026-11-11. Official PDFs were downloaded directly after the web reader could not extract some texts; the EIRL scan was read through OCR and rendered page images. The cited legislative extracts are primary texts, not an accountant's approval of this version.

| Source | URL | Read on | Content actually read |
|---|---|---|---|
| Official consolidated Ley 26887, General Companies Law | https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=15 | 2026-11-11 | Arts. 1 to 11, 16 to 27, 50 to 55, 111 to 115, 152 to 155 including art. 152-A, 234 to 249 and 283 to 287: formation, capital, governance, directors' written acceptance and legalised signatures, annual meeting and neighbouring conditions; art. 23 amendment by Ley 30822 checked against the amending text. |
| Decreto Ley 21621, original Congress scan | https://www.leyes.congreso.gob.pe/Documentos/Leyes/21621.pdf | 2026-11-11 | Pages 1 to 3 and 5 to 6, arts. 1 to 24 and 33 to 49: owner, deed, capital, annual decisions and liability; historical provisions not adopted indiscriminately. |
| DL 1409 and DS 312-2019-EF, official legal compilation | https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=31 | 2026-11-11 | DL arts. 4 to 15 and final provisions, especially supplementary LGS rules; regulation arts. 6 to 24: fields, signing, capital evidence, timing, result and RUC. |
| Ley 30822 cash-deposit amendment | https://busquedas.elperuano.pe/api/visor_html/1671756-1 | 2026-11-11 | Art. 9 replacing LGS art. 23, and thirteenth final provision on commencement: qualifying Coopac conditions. |
| Official MYPE compilation, DS 013-2013-PRODUCE and Ley 32353 | https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=76 | 2026-11-11 | Opening annotation; TUO arts. 4 to 10, especially minimum-payment and sworn-declaration exception; Ley 32353 art. 10 and ninth final provision on conditional commencement. |
| SUNARP SACS module manual, version 1.3 | https://cdn.www.gob.pe/uploads/document/file/5377042/4813673-manual-de-usuario-modulo-sacs-sid-sunarp.pdf?v=1699296963 | 2026-11-11 | Read for pp. 4 and 14 to 34, especially pp. 25 and 29: certificates and applicable spouse/other-manager signers, MYPE checkbox, contribution method, image upload, PDF review, signing and final submission/payment controls. |
| SUNARP SACS standard form list | https://www.gob.pe/institucion/sunarp/informes-publicaciones/4084275-formatos-estandarizados-de-constitucion-de-sacs | 2026-11-11 | Read in normal browser: manager cash-receipt declaration and constitution options; old monetary brackets not used as current law. |
| SUNARP SACS cash-receipt declaration | https://cdn.www.gob.pe/uploads/document/file/4347884/Declaraci%C3%B3n%20jurada%20de%20recepci%C3%B3n%20de%20aporte%20en%20efectivo.docx?v=1680197785 | 2026-11-11 | Read for manager identity, company denomination, cash received and contributor fields in the official declaration. |
| SUNARP live entity comparison | https://sid.sunarp.gob.pe/sid/informa.htm?method=goConstEmp | 2026-11-11 | Read for entity table: SA, SAC, SRL, EIRL and SACS, organs and contribution types. |
| SUNARP name reservation service | https://www.gob.pe/271-buscar-y-reservar-el-nombre-de-una-empresa | 2026-11-11 | Read in normal browser: optional/recommended nature, citizen portal, reservation and payment controls; displayed historical amount not adopted as 2026 tariff. |
| PRODUCE constitutive act guidance | https://www.gob.pe/272-elaborar-el-acto-constitutivo-minuta | 2026-11-11 | Read in normal browser: definition of the constitutive act, activity description and preparation before the notarial stage. |
| PRODUCE capital contribution guidance | https://www.gob.pe/273-abono-de-capital-y-bienes | 2026-11-11 | Read in normal browser: money/assets evidence, bank opening recommendation and related qualification. |
| SUNARP ordinary SID formation service | https://www.gob.pe/10580-constituir-tu-empresa-a-traves-de-la-plataforma-sistema-de-intermediacion-digital-sid-sunarp | 2026-11-11 | Read in normal browser: four legal forms, notary request, fields, digital transmission, review period and assigned RUC activation. |
| SUNARP citizen formation requirements | https://sid.sunarp.gob.pe/sid/recursos/Requisitos/requisitos_para_el_cumplimiento.pdf | 2026-11-11 | Read for both pages, especially steps 3 to 5: field labels, PDF review, FINALIZAR, submission receipt, signing window and result documents; historical fees excluded. |
| SUNARP SACS formation service | https://www.gob.pe/26692-constituir-tu-empresa-como-sociedad-por-acciones-cerradas-simplificadas-sacs | 2026-11-11 | Read in normal browser: no deed, account and digital-certificate prerequisites, module options, data and email results. |
| SUNAT updated TUO Ley 28194, DS 150-2007-EF | https://www.sunat.gob.pe/legislacion/itf/ds150_07.pdf | 2026-11-11 | Current arts. 3 to 5 and neighbouring prior-text warnings; special capital-participation payment condition under DL 1529 distinguished from corporate deposit evidence. |
| SUNAT UIT values, 2026 DS 301-2025-EF | https://www.sunat.gob.pe/indicestasas/uit.html | 2026-11-11 | Read for 2026 row and legal basis: S/5,500. |
| SUNAT RUC onboarding | https://centrovirtual.sunat.gob.pe/tramites/inscribete-ruc | 2026-11-11 | Read for RUC definition, CIIU/regime preparation and separate natural/legal-person registration flows. |
| SUNAT Clave SOL instructions | https://centrovirtual.sunat.gob.pe/tramites/clave-sol | 2026-11-11 | Read for generation steps: representative's company RUC, contact selection and verification code. |
| SUNAT public Clave SOL form | https://ww1.sunat.gob.pe/ol-ti-itadminforuc-inscripcion/inscripcion | 2026-11-11 | Read for public legal-person tab, RUC and representative identity fields; no credentials entered and no submission made. |
| SUNAT legal-person RUC activation | https://www.gob.pe/11125-activar-ruc-de-persona-juridica | 2026-11-11 | Read in normal browser: inactive RUC, SOL menu path, information, preview, regime and subsequent security prompt. |
| SUNAT business tax-regime comparison | https://emprender.sunat.gob.pe/ruc/regimenes-tributarios-mype/regimenes-tributarios | 2026-11-11 | Read for entity eligibility, monthly/annual filing and records rows; activity/income selection conditions. |
| SUNAT mandatory accounting records guidance | https://orientacion.sunat.gob.pe/libros-y-registros-obligatorios | 2026-11-11 | Read for regime/income-based obligations and projected income for new activities; no universal electronic-record assertion adopted. |
| SUNAT employer registration help | https://www.sunat.gob.pe/ayuda/tributos/tregistro-E-P/T-Registro-H01.html | 2026-11-11 | Read for Alta fields, modification and RUC-origin data; employer registration before Planilla Electrónica. |
| SUNAT PLAME questions | https://orientacion.sunat.gob.pe/3246-05-preguntas-frecuentes-pdt-plame | 2026-11-11 | Read for T-Registro relationship and fourth-category payee reporting conditions; payroll computation referred to separate Guide. |
| SUNAT RS 000168-2025 | https://www.sunat.gob.pe/legislacion/superin/2025/000168-2025.pdf | 2026-11-11 | Arts. 2 to 4, especially 3(a)(ii.4), 3(c) and period-end information: new-company beneficial-owner filing periods. |
| SUNAT beneficial-owner filing guidance | https://emprender.sunat.gob.pe/declaracion-pagos/declaracion/beneficiario-final | 2026-11-11 | Read for ownership/control, SOL path, FV 3800, simplified/attachment conditions, confirmation and update rather than automatic annual filing. |

Not yet confirmed: the old Guide's claim that SAC is the most common SME vehicle; a blanket absence of minimum capital across all activities and regulated sectors; its S/10,000 cash-contribution bank-receipt threshold, which is not retained as law because the operative deposit and payment-method rules above differ; its generic 7 to 10 business-day total formation estimate; current 2026 registry, electronic-service and notarial charges; bank-specific account opening conditions beyond the official S/1,000 recommendation. These points must not be supplied from the old secondary sources.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-11. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `pe-company-formation` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/pe-company-formation. If neither is available, confirm every figure against the official source pages cited above before relying on it.
