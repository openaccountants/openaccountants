---
name: saudi_arabia-references
jurisdiction: SA
last_updated: "2026-11-16"
version: "1.1"
description: "Saudi Arabia software-reference and tax-method router for 2026. Compares pinned README and MIT licence evidence for SallaApp/ZATCA, wes4m/zatca-xml-js and axenda/zatca; distinguishes basic QR, simplified-invoice and broader claimed capabilities, official specifications and untested runtime assertions. Routes VAT, FATOORA, WHT, Zakat, CIT, payroll, formation, excise and property questions to their owning Saudi methods. Read when choosing implementation references; contains no independent tax-rate or filing computation."
tier: 2
tax_year: 2026
type: "router"
domain: "references"
---

# Saudi Arabia software references and tax-work routing: 2026

> **Produced by OpenAccountants (openaccountants.com)**
>
> General reference only. These are third-party software references, not an accountant's approval, a tax source, a security audit or certification by ZATCA. No package was installed, executed or tested against a live invoice service for this comparison.

## Scope

Use this router when selecting Saudi e-invoicing implementation references or deciding which Saudi tax method to load. It preserves the three original projects and their useful subject areas, while distinguishing upstream feature claims from current legal requirements and tested behaviour. It contains **no independent tax-rate, filing-deadline or Zakat computation method**.

Do not use a package's sample amounts, tax identifiers, enums or bundled old PDF as authority for the current VAT treatment of a transaction. For a live integration, first load [FATOORA implementation](saudi-einvoice.md) and [VAT](saudi-arabia-vat.md), establish the actual taxpayer/document/environment, then assess a pinned package release against the official requirements.

## The method, step by step

### 1. Establish the actual job before selecting a package

Record the implementation language/runtime, QR-only versus complete XML/signing requirement, standard versus simplified document support, credit/debit/advance requirements, EGS architecture, certificate lifecycle, environment, actual notification and needed tax decisions. Separate a formatting task from a tax calculation or an authorised production submission.

A package that renders a QR image can be useful for that isolated task without supporting clearance, reporting, certificate renewal, statutory archiving or the complete invoice lifecycle. Do not rank projects by GitHub stars as if popularity proves current compatibility, security or ZATCA acceptance.

### 2. Compare the pinned upstream descriptions and licences

Read on **16 November 2026**. The linked commits identify the comparison snapshot; use the exact release/commit selected for implementation and re-read its current source, dependency and security information before adopting it.

| Project / snapshot | What the upstream README actually supports or claims | Limit of this comparison |
|---|---|---|
| [SallaApp/ZATCA](https://github.com/SallaApp/ZATCA/tree/716862a80612715b677810e5f7161a84b6098ab1), PHP | The unofficial package describes both generation and integration phases, CSR/key generation, XML invoice signing, certificate/secret handling and QR/TLV generation. It shows distinct sandbox/simulation/core environment settings and a basic QR-only API | These are README capabilities, not proof of current end-to-end API conformance. A code example exporting a key does not override the official key-protection requirements. Assess the actual key storage, hash/signature behaviour and selected runtime/dependencies before use. [README](https://github.com/SallaApp/ZATCA/blob/716862a80612715b677810e5f7161a84b6098ab1/README.md) |
| [wes4m/zatca-xml-js](https://github.com/wes4m/zatca-xml-js/tree/41a2c7d9075cb1a4b0b0e39f30a887337d778c73), TypeScript | README calls the release **experimental**, describes EGS onboarding, cryptographic stamps and creation/signing/compliance/reporting of **simplified** tax invoices. Its key/CSR module depends on OpenSSL; bundled documentation includes older official specifications | The README explicitly says standard tax invoices are not supported/planned by that author; renewal/revocation are roadmap items. The old “full implementation” and “most complete” claims are unsupported. Do not approve it for standard-invoice clearance or complete lifecycle management without separate implementation evidence. [README](https://github.com/wes4m/zatca-xml-js/blob/41a2c7d9075cb1a4b0b0e39f30a887337d778c73/README.md) |
| [axenda/zatca](https://github.com/axenda/zatca/tree/0aadfdeca9333787a7424763aad1cb541e61ac89), TypeScript/Node/browser | README describes an unofficial basic QR/TLV/Base64 renderer, usable in frontend/backend contexts, taking invoice total and VAT total as caller-provided strings | Its roadmap marks the basic generation-phase QR feature complete and integration-phase QR support incomplete. Its assertion of matching official SDK output is expressly historical; it is **not a test performed for this rewrite** or proof of present integration-phase compatibility. [README](https://github.com/axenda/zatca/blob/0aadfdeca9333787a7424763aad1cb541e61ac89/README.md) |

All three checked upstream **LICENSE files contain MIT terms**, including retention of the copyright/permission notice in copies or substantial portions and the stated warranty disclaimer. Read the actual selected files, rather than relying only on a badge or an incorrect README licence filename: [Salla LICENSE](https://github.com/SallaApp/ZATCA/blob/716862a80612715b677810e5f7161a84b6098ab1/LICENSE), [wes4m LICENSE](https://github.com/wes4m/zatca-xml-js/blob/41a2c7d9075cb1a4b0b0e39f30a887337d778c73/LICENSE), [axenda LICENSE](https://github.com/axenda/zatca/blob/0aadfdeca9333787a7424763aad1cb541e61ac89/LICENSE). This identifies those files' terms; it is not a blanket legal opinion that every transitive dependency, combined product, content copy or distribution is fully licensed.

**OpenAccountants is mixed-licence.** Its software is **AGPL-3.0-only**; its skill content and content exports use the applicable **Open Accountants Skills/Guide licence**, with commercial tracks and prior-release/third-party exceptions described in repository policy. Do not call the entire collection MIT, or infer that copying MIT tooling grants rights to redistribute the OpenAccountants content. Consult [repository licensing at the reviewed base](https://github.com/openaccountants/openaccountants/blob/2844c309238b4fdb63be0a3d0ad9ae99a8ea89c8/LICENSING.md). Existing platform licence metadata in other skills is not silently rewritten by this comparison.

### 3. Route implementation details to the official specification

Use [FATOORA implementation](saudi-einvoice.md) for the current official XML/security documents, actual wave/scope, document and transaction flags, correct production/simulation routes, certificate lifecycle, hash/ICV/PIH, QR/TLV and clearance/reporting controls. Repository copies of a ZATCA PDF retain the provenance of that document but do **not** establish that they are the latest official publication. The official website and operative version control current requirements.

Preserve the original extraction topics without promoting sample values to law:

| Original data topic | How to use it safely / destination |
|---|---|
| Sample standard VAT percentage | An input or fixture does not establish the rate, place/time of supply, exemptions or a “single-rate-only” system. Use [VAT](saudi-arabia-vat.md) for the transaction |
| Category codes `S`, `Z`, `E`, `O` | **O means not subject to VAT; Z means zero-rated; E means exempt.** Do not merge O with zero rating because a sample uses zero tax. Use the official taxonomy through [FATOORA](saudi-einvoice.md) |
| Invoice/debit/credit codes and payment means | Check the official code list and actual document/transaction. An enum in an old package can be incomplete or stale; do not add a competing code list here |
| SAR currency assumption | A package's fixed currency is an implementation restriction, not proof that all commercial invoice amounts must be SAR. Check document currency and SAR tax requirements in [FATOORA](saudi-einvoice.md) |
| VAT line formula and rounding | Evaluate quantity/base quantity, discounts, charges, category/document totals and the official precision rules. A sample multiplication is not a complete VAT engine |
| Tax-inclusive amount | Distinguish tax-exclusive, tax-inclusive, advance and amount-due fields before reusing sample strings. QR total/VAT inputs are not themselves a rate calculation |
| Basic/enhanced QR fields | Compare against the current official TLV/byte and standard/simplified stamping rules. A basic renderer does not prove enhanced cryptographic support |
| Seller tax-number formatting | Example strings are placeholders. Format validation is distinct from a real VAT registration, correct taxpayer identity or the appropriate other-ID scheme |
| Bundled official PDFs | Follow the official source link and version/read date in [FATOORA](saudi-einvoice.md); a vendored copy is not an independent legal authority |
| Claim of official SDK validation | Treat as the upstream's stated test scope/date. No present runtime, byte-vector, security or live-service validation was performed here |

Tax-code distinctions above follow [ZATCA XML standard §§8, 11.2.4 and BR-S/BR-Z/BR-E/BR-O](https://zatca.gov.sa/ar/E-Invoicing/SystemsDevelopers/Documents/20230519_ZATCA_Electronic_Invoice_XML_Implementation_Standard_%20vF.pdf); remaining technical instructions are in the owning FATOORA method. The repositories' README/code claims are primary evidence only of **what their maintainers describe**, not primary evidence of Saudi tax law.

### 4. Load the owning Saudi method for the tax/compliance job

| Question or data gap | Skill to load / handoff |
|---|---|
| VAT registration eligibility, taxable/zero/exempt/out-of-scope supplies, input recovery, rate and return frequency | [VAT](saudi-arabia-vat.md). Do not confuse a return-frequency turnover threshold with the VAT-registration threshold |
| Structured invoice, legal document type, issue/clear/report, signature/QR, rejected/warning result, retention | [FATOORA](saudi-einvoice.md), followed by VAT for the underlying supply |
| Corporate taxable income, natural-gas/oil boundaries, ownership allocation, financing costs, losses and related-party documentation | [Corporate tax](sa-corporate-tax.md) |
| Non-resident management, royalty, technical/service, financing, rent, dividend or other payment; treaty/PE/gross-up | [Withholding tax](sa-withholding-tax.md). The old management/service-rate summary here was wrong and is superseded by that source-based method |
| ZATCA-administered business Zakat, ownership, equity/liabilities, deductible assets and calendar-dependent charge | [Zakat](sa-zakat.md). A flat percentage of “net assets” is not the complete statutory base method |
| Staff contributions, old/new insured cohort, occupational localization and bank wage-file reporting | [GOSI, Saudization and WPS](sa-gosi-saudization.md) |
| Entity/branch choice, investment/CR/beneficiary registration, RHQ and regulatory permissions | [Formation](sa-formation.md) |
| Tobacco, energy drinks, electronic-smoking goods and sweetened-drink excise | [Excise](sa-excise-tax.md) |
| Saudi property/right/share disposition and claimed relief | [RETT](sa-rett.md); VAT for any separate property-supply issue |
| Establishing an individual's case and preparing an assembled annual workpaper | [Freelance intake](sa-freelance-intake.md), then the owning substantive methods, then [return assembly](sa-return-assembly.md) |
| Customs/tariff, another jurisdiction, a special tax sector, treaty dispute or an unconfirmed law | Obtain the actual official rule and competent specialist. None of these three repositories fills that gap |

The original conclusion remains only in its supported form: these are **e-invoicing implementation references**, not substitutes for a current tax-law library. Do not claim an exhaustive source-code audit proved that no tax constants or calculations exist anywhere in them; this comparison read their README/licence and identified source snapshot, without auditing every file.

### 5. Produce a reviewable implementation handoff

Record the chosen job, language, package/release/commit and file hashes; the actual licence/dependency notices; features required versus upstream-supported/unsupported features; official-specification versions; and the test plan. Before production adoption, the implementation owner must test the actual XML/QR/signing vectors, rounding, document variants, environment/credential lifecycle, queue/retries and storage controls relevant to that job. Use non-sensitive fixtures and authorised test credentials; keep live invoice data and private keys out of public examples.

Report the result as **upstream description reviewed / code inspected / offline tests run / official test environment exercised / production outcome verified**, only where each step actually occurred. A licence read or README claim cannot be upgraded into any of the later outcomes. Stars, download counts and unexamined badges do not fill a missing test.

## When to refuse or refer

Do not approve a basic QR-only package for a complete integration mandate, a simplified-only library for standard clearance, an unsupported certificate lifecycle for a production estate, or an old test assertion as current certification. Stop if legal invoice/tax classification, actual taxpayer/wave, selected version, required capability, key protection or the applicable licence is unresolved.

Refer a real licensing question about a combined/distributed product to the relevant licence texts and qualified advice. Refuse to copy private keys, secrets, OTPs or real taxpayer documents into an upstream issue, public workpaper or third-party decoding site. Use the tax method and primary ZATCA source for any number or rule; do not extract a tax position from a convenient sample.

## Sources

Read date: **16 November 2026**. GitHub source snapshots were fetched through the connected GitHub service and pinned against the matching README/licence blob hashes. No upstream package was executed.

| Source | What was read and used |
|---|---|
| [Salla README](https://github.com/SallaApp/ZATCA/blob/716862a80612715b677810e5f7161a84b6098ab1/README.md) and [LICENSE](https://github.com/SallaApp/ZATCA/blob/716862a80612715b677810e5f7161a84b6098ab1/LICENSE) | Read on 2026-11-16. Read the complete README, requirements, phase/CSR/signing/QR usage and licence text. Scope is an upstream description, not a runtime/security audit |
| [wes4m README](https://github.com/wes4m/zatca-xml-js/blob/41a2c7d9075cb1a4b0b0e39f30a887337d778c73/README.md) and [LICENSE](https://github.com/wes4m/zatca-xml-js/blob/41a2c7d9075cb1a4b0b0e39f30a887337d778c73/LICENSE) | Read on 2026-11-16. Read the complete experimental-status/support/dependency/roadmap/non-affiliation statements and licence; standard-invoice exclusion and lifecycle roadmap retained |
| [axenda README](https://github.com/axenda/zatca/blob/0aadfdeca9333787a7424763aad1cb541e61ac89/README.md) and [LICENSE](https://github.com/axenda/zatca/blob/0aadfdeca9333787a7424763aad1cb541e61ac89/LICENSE) | Read on 2026-11-16. Read the complete basic-QR usage, caller-provided amounts, historical SDK-match claim, roadmap and licence; no new validation performed |
| [OpenAccountants licensing at the reviewed base](https://github.com/openaccountants/openaccountants/blob/2844c309238b4fdb63be0a3d0ad9ae99a8ea89c8/LICENSING.md) | Read on 2026-11-16 from the actual Git object. Read the software/content mapping, current version, prior-release and third-party exceptions; not a change to platform licence keys |
| [ZATCA XML implementation standard](https://zatca.gov.sa/ar/E-Invoicing/SystemsDevelopers/Documents/20230519_ZATCA_Electronic_Invoice_XML_Implementation_Standard_%20vF.pdf) | Read on 2026-11-16. Read for category distinctions and the implementation code/amount boundaries; the detailed method and other official sources remain in FATOORA |

**Not yet confirmed:** current popularity/star counts, registry release freshness, every upstream implementation file or dependency licence, vulnerability/security status, actual runtime/platform compatibility, full standard/simplified/lifecycle coverage beyond README statements, official present conformance, SDK byte-vector equality, test/live API success and a particular product's combined-licensing position. The old star counts and blanket “fully compatible/most complete” rankings are excluded from current guidance. Tax amounts, rates and filing decisions require the owning method and actual facts.
