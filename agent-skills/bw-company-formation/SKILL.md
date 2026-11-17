---
name: bw-company-formation
description: "Botswana formation preparation and BURS onboarding for 2026-27: taxpayer registration, company documents and tax handoffs. CIPA company-law, fees and live filing steps remain on hold; this is not a complete incorporation procedure."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/bw-company-formation"
  jurisdiction: "BW"
  tax_year: "2026"
  last_updated: "2026-11-16"
---

# Botswana Company Formation and Entity Choice v1.1

> **General reference only.** This Guide is general tax reference material. It has not been reviewed for any specific person's facts. Check figures against the official sources named here.

## Scope

Botswana, tax year 2026-27 (1 July 2026 to 30 June 2027). This is a limited formation preparation and tax-registration procedure. It can support BURS onboarding for an existing company; it cannot complete a CIPA incorporation, choose a legally suitable entity, quote current CIPA fees or certify company-law compliance. The CIPA requirements listed under Sources are **not usable filing instructions** until their current official text is read.

The Tax Administration Act, 2026 (No. 14 of 2026) and its SI 90 Regulations operate from 1 July 2026 (SI 91 para 2; SI 90 reg 1, in the [BURS official bundle](https://www.burs.org.bw/index.php/tax/tax-laws-2026?download=955:tax-administration-act-2026)).

## Ask the client first

- New incorporation, business-name registration, existing Botswana company or foreign entity registering locally? Obtain its CIPA certificate and current registry record if it already exists.
- Proposed name, activity, owners, beneficial owners, directors, secretary or accounting officer, addresses and any constitution or controller documents already prepared?
- Date the potentially taxable activity started, date it became a withholding agent, and any existing BURS registration or TIN?
- Botswana-incorporated or foreign-established entity, and which supporting certificates are available?
- Local or remote taxable supplies, actual and forecast taxable turnover, and any employees or payments subject to withholding?

## The method, step by step

1. **Resolve the CIPA gate first for an unformed entity.** The existing research identifies CIPA and its Online Business Registration System (OBRS), at https://www.cipa.co.bw/, as the company-registration route. Live company-law, fee and submission instructions could not be read in this session. Record the intended entity type and proposed name, but stop before giving a definitive incorporation checklist or filing/payment instruction. The historical requirements and every old fee are preserved as holds under Sources.
2. **Check whether BURS registration is required.** An unregistered person must apply when it starts an activity that may result in tax liability or becomes a withholding tax agent. Apply in the approved form within **21 days** of that event, unless BURS allows more time. The exception is a non-resident whose only liability is income tax collected by withholding as a final tax. A person proposing an activity requiring a licence may apply before starting. [TAA s 6(1)–(5)](https://www.burs.org.bw/index.php/tax/tax-laws-2026?download=955:tax-administration-act-2026).
3. **Prepare the current company evidence.** For a Botswana-incorporated or formed company, supply its incorporation or registration number. A certified incorporation/registration certificate is required if BURS cannot confirm that number through the CIPA interface. This replaces the old unconditional certified-company-document checklist as the operative rule. [SI 90 reg 5](https://www.burs.org.bw/index.php/tax/tax-laws-2026?download=955:tax-administration-act-2026).
4. **For a foreign-established entity, use the separate document rule.** Supply a certified foreign incorporation/registration certificate or another certified document evidencing its creation or existence; provide a certified English translation if necessary, and a certified CIPA registration certificate. Here “non-resident entity” means an entity not incorporated or established in Botswana. Do not substitute a tax-residence assumption for that definition. [SI 90 reg 8](https://www.burs.org.bw/index.php/tax/tax-laws-2026?download=955:tax-administration-act-2026).
5. **Deal with identification requests within their stated scope.** BURS may require an individual's biometric data for identification and fraud prevention. It may request beneficial-ownership information by written notice if it cannot access that information through CIPA; meet the time in the notice. These are conditional powers, not an automatic biometric or beneficial-owner upload requirement for every application. [SI 90 regs 10–11](https://www.burs.org.bw/index.php/tax/tax-laws-2026?download=955:tax-administration-act-2026).
6. **Submit through the approved channel and keep the outcome.** The official electronic route is https://eservices.burs.org.bw/; SI 90 regs 28–29 allow approved paper or electronic forms and the manner determined by BURS. The [BURS Registration page](https://www.burs.org.bw/index.php/tax/registration) names **BURS 1**, but its document list predates the new Act. Current screen/field numbers and the current approved registration form have not been confirmed; stop if they cannot be identified. BURS issues a registration certificate and TIN; registration takes effect on the certificate's specified date. One TIN serves all tax laws. An existing taxpayer need not lodge additional registration forms for another tax where s 7(4) applies, but BURS may request more information. [TAA ss 7, 10–11](https://www.burs.org.bw/index.php/tax/tax-laws-2026?download=955:tax-administration-act-2026).
7. **Finish the tax handoff.** Load [VAT](bw-vat-gst.md) for compulsory, voluntary, remote-supplier or reverse-charge registration; a company certificate alone does not decide those tests. Load [company tax](bw-corporate-income-tax.md) for the accounting period, returns and instalments, [payroll](bw-payroll-social.md) for employees, and [cross-border](bw-cross-border.md) for foreign payments. Keep CIPA ongoing compliance separate from BURS tax compliance; the current CIPA annual-return, constitution and secretary requirements remain held below.

## Worked cases

An already-incorporated Botswana company, not yet BURS-registered, starts potentially taxable activity. Assume 17 whole days of the statutory 21-day window have elapsed, with no extension. Four days of that window remain: 21 − 17 = 4. Prepare its incorporation number under reg 5; a certified certificate is conditional on the interface check failing. This is a remaining-window calculation, not a calendar-date or incorporation-completion opinion. [TAA s 6(4)(c), SI 90 reg 5](https://www.burs.org.bw/index.php/tax/tax-laws-2026?download=955:tax-administration-act-2026).

```oa-check
name: Botswana taxpayer registration window
inputs:
  window_days: 21
  elapsed_days: 17
steps:
  - remaining_days: window_days - elapsed_days
expected:
  remaining_days: 4
```

## When to refuse or refer

Do not state that an entity is incorporated, lawfully constituted or ready to trade from this Guide. Refer the CIPA portion for a current official-source completion before relying on it. Stop at the BURS submission stage if the approved form/channel cannot be identified, a certificate is missing, or residence and beneficial ownership facts are unresolved. The tax-registration exception does not establish an exemption from CIPA or other business requirements.

## Sources

| Source and actual scope | URL | Read |
|---|---|---|
| Tax Administration Act, 2026 No. 14, ss 6–11; SI 90 regs 1, 3–12, 28–29; SI 91 commencement para 2. Complete operative provisions and adjacent provisions read for this procedure | https://www.burs.org.bw/index.php/tax/tax-laws-2026?download=955:tax-administration-act-2026 | 2026-11-16 |
| BURS Registration page: company, individual and other-entity document lists and BURS 1 label; page still refers to 2011/2007 requirements. Used only to identify the historical form label and explain the conflict with SI 90 | https://www.burs.org.bw/index.php/tax/registration | 2026-11-16 |
| Archived CIPA entity-name page; completed earlier entity research preserved, not a current incorporation procedure. Current live access blocked; no fresh read claimed | https://web.archive.org/web/20260926061814/https://www.cipa.co.bw/selecting-and-reserving-an-entity-name | Earlier read 2026-11-01; reuse limited to intake route |
| Archived CIPA fees, historical record only; not current fee authority | https://web.archive.org/web/20251014004157/https://www.cipa.co.bw/wp-content/uploads/2019/10/fees-for-frequently-used-services.pdf | Earlier read 2026-11-01; not re-read |
| Archived CIPA FAQ, historical record only; not current company-law or filing authority | https://web.archive.org/web/20230423011758/https://www.cipa.co.bw/frequently-asked-questions | Earlier read 2026-11-01; not re-read |

Not yet confirmed: **all the following are nonusable CIPA holds, not advice or current fees.** The old entity descriptions were private company up to 25 shareholders, at least one shareholder/director and “(Proprietary) Limited”; public company any number of shareholders, “Limited”, usually listed; close company up to five individuals, no corporate members or banking/insurance, suffix “CC”; guarantee company no dividends; business name a trading style rather than a separate entity (“it is you”); and external company a foreign company registering locally. Current Companies Act qualifications, counting exceptions and 2018/2022/2025 amendments have not been established here. Historical online/counter fees were name reservation P20/P60; private/public/close registration P360/P900; guarantee/external registration P4,600/P6,000; business-name registration P150/P450; name change P1,000/P1,500. Current fee authority is unread. Also held: exact OBRS fields and beneficiary/owner documents; card payment or deposit at CIPA/FNB; secretary appointment within three months and the close-company accounting-officer exception; annual return in the incorporation month, deregistration and restoration fees; minimum capital, 30-day name reservation, one-to-three-week formation timeline; Companies (Amendment) Act, 2025 constitution, licensed-secretary and 12/24-month transition rules, commencement and subsequent deadline extensions. CIPA live fetches returned 403, ordinary browser automation failed before a page read, and archive requests returned 429; a Gazette mirror had an invalid certificate and was not bypassed. Also unconfirmed: current BURS registration screen/field numbers and approved form identifier; the old BURS 1 certificate/director/secretary/share-capital checklist is historical only where inconsistent with SI 90.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-16. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `bw-company-formation` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/bw-company-formation. If neither is available, confirm every figure against the official source pages cited above before relying on it.
