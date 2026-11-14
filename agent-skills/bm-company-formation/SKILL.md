---
name: bm-company-formation
description: "How to form a Bermuda company under the Companies Act 1981 in 2026, local or exempted, limited by shares, by guarantee or unlimited. Covers name reservation, restricted activities, the memorandum and bye-laws, beneficial ownership under the Beneficial Ownership Act 2025, the local-company advert, registered office, the resident director, secretary or representative for exempted companies, the economic substance and CIT declarations, continuance, annual filings and the economic substance declaration. Trigger phrases include incorporate in Bermuda, exempted company, local company 60% Bermudian, Registrar of Companies Bermuda, beneficial owner 25%."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/bm-company-formation"
  jurisdiction: "BM"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Bermuda company formation v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Forming a company under the Bermuda Companies Act 1981 with the Registrar of Companies, in 2026. Covers local and exempted companies limited by shares or guarantee, or unlimited. Partnerships, LLCs, segregated accounts companies and regulated financial businesses are named but not walked through. Taxes after formation: [bermuda-tax](bermuda-tax.md), [bm-payroll-social](bm-payroll-social.md), [bm-corporate-income-tax](bm-corporate-income-tax.md).

## Ask the client first

1. Will the company trade in Bermuda (local company) or outside Bermuda (exempted company)?
2. Who will own and control it, directly and through other entities, and are any owners Bermudian?
3. What will it do: anything on the Ninth Schedule restricted list (financial institution, digital asset issuance, professional services to the public, holding land) or the Tenth Schedule prohibited list?
4. Will it carry on a relevant activity for economic substance, and will it be a Bermuda Constituent Entity of a group with EUR 750 million revenue?
5. Is it a new company or a foreign company continuing into Bermuda?

## The method, step by step

### Rates, bands and thresholds

| Item | Figure and conditions | Official source |
|---|---|---|
| Local company Bermudian control (Third Schedule Part I) | At least sixty per cent of voting rights exercisable by Bermudians, and not less than sixty per cent each of Bermudian directors and of shares beneficially owned by Bermudians; a licence under s.114A or s.114B can relax this | [Limited companies](https://www.gov.bm/limited-companies) |
| Beneficial owner test | 25% or more of shares, interests or voting rights, directly or indirectly; or ultimate effective control; or control by other means. If no one qualifies, the senior manager | same |
| Update the beneficial ownership register | Within 14 days of being notified of a change | same |
| Name reservation | Not more than three months before the application, for up to three months | same |
| Local company advert | In an appointed newspaper, not more than three months before the application | same |
| Processing time | About one day without Minister's consent; up to a week where consent is needed | same |
| Economic substance declaration | Due six months after the last day of the relevant financial period | [CITA, economic substance](https://www.cita.bm/economic-substance) |

### Steps

1. **Choose the form.** Limited by shares (most common; the memorandum states authorised capital and its division into shares of a fixed amount), limited by guarantee (only for art, science, religion, charity, sport, education or similar purposes with no dividends, or the other cases in s.5(3)), or unlimited (rare). Bearer shares are prohibited (ss.53A and 54). A single shareholder is allowed ([Limited companies](https://www.gov.bm/limited-companies)).
2. **Choose local or exempted.** A local company may only carry on business in Bermuda if it meets the 60% Bermudian test or holds a licence. An exempted company is exempt from that test but is restricted in what it does in Bermuda (s.129) and needs a s.129A licence to go beyond the permitted list. It must have a director ordinarily resident in Bermuda (not an alternate), or a resident secretary, or a resident representative (s.130).
3. **Engage a Bermuda law firm, accounting firm or licensed corporate service provider.** The Registrar requires one; corporate service providers are licensed under the Corporate Service Provider Business Act 2012.
4. **Reserve the name** (s.6A). The Registrar can refuse undesirable, identical or deceptively similar names (s.8).
5. **Check the activity.** Ninth Schedule activities need the Minister's consent (s.4A); Tenth Schedule activities (armaments trafficking, unauthorised gaming, unauthorised controlled drugs dealing) are barred (s.4B).
6. **Prepare the memorandum and bye-laws.** The memorandum (s.7) states the name ending in "Limited" (unless licensed under s.9), limited liability, objects or unrestricted objects, any secondary name, the subscribers' names, addresses, nationalities and Bermudian status, whether exempted, and any fixed duration. It is signed by each subscriber before a witness or authenticated electronically. Bye-laws are not filed; they become operative when approved at the statutory general meeting.
7. **Identify and verify the beneficial owners** under the Beneficial Ownership Act 2025 (in force 3 November 2025; the central register moved from the Bermuda Monetary Authority to the Registrar). File the minimum required information with the application. Only companies listed on the Bermuda Stock Exchange or an appointed exchange, and their subsidiaries, are exempt.
8. **Advertise** (local companies only), naming the company and its proposed objects (s.6(2)).
9. **Fix the registered office** in Bermuda (s.62; not a post office box), the directors, officers and secretary, and any licence the business needs.
10. **Declare** on the application whether the company will carry on a relevant activity for economic substance (s.5A) and whether it will be a Bermuda Constituent Entity under the Corporate Income Tax Act 2023 (s.5B; not public, may be shared with CITA).
11. **File** through www.registrarofcompanies.gov.bm (forms at www.gov.bm/services/registrar-companies-forms) and pay the government fees.
12. **After registration:** the Registrar issues the certificate of incorporation, which is conclusive evidence of incorporation and its date (ss.14 and 15). Enter the name, certificate, memorandum and registered office on the public register.
13. **Continuance instead of incorporation:** a foreign body corporate can continue as an exempted company (s.132C) with home-country authorisations, a memorandum of continuance and financial statements for a period ending within twelve months of the continuance date. No new legal entity is created (s.132E(2)).
14. **Each year:** file the annual declaration through the online register (economic substance relevant activity and, since December 2024, CIT information); local companies also file the annual return of shareholdings (s.117); keep the beneficial ownership register current; file the economic substance declaration with CITA six months after the period end; register for payroll tax and social insurance before paying staff.

## Worked cases

### Case 1: is an indirect shareholder a beneficial owner?

An individual owns 60% of HoldCo, which owns 50% of the new Bermuda company. Indirect ownership is 60% of 50% = 30%, which is 25% or more, so she is a beneficial owner and must be identified, verified and filed.

```oa-check
name: Bermuda beneficial owner test, indirect 30% holding
inputs:
  holding_in_holdco: 0.60
  holdco_in_company: 0.50
  threshold: 0.25
steps:
  - indirect_share: holding_in_holdco * holdco_in_company
  - margin_over_threshold: indirect_share - threshold
expected:
  indirect_share: 0.30
  margin_over_threshold: 0.05
```

## When to refuse or refer

- Ninth Schedule activities (banking, insurance outside the registered regimes, digital asset issuance, professional services to the public, land holding) and anything on the Tenth Schedule: refer to a Bermuda law firm; the Minister's consent or a licence is needed.
- Segregated accounts companies, LLCs, partnerships and investment funds: not walked through here.
- Economic substance tests for a relevant activity: refer to CITA guidance and an adviser.

## Filing and payment

Filing and payment go through the Registrar's online register at www.registrarofcompanies.gov.bm; a user account needs government-issued identification. Enquiries: helpcenter@rocbda.com, (441) 297-7574, 30 Parliament Street, Hamilton HM 12. Sanctions for beneficial ownership failures sit in the Registrar of Companies (Compliance Measures) Act 2017 (questionnaires, inspections, notices, default fines and civil penalties, with appeal to the Supreme Court) ([Limited companies](https://www.gov.bm/limited-companies)).

## Completion checklist

- Local or exempted decided; 60% test or licence confirmed for a local company.
- Resident director, secretary or representative for an exempted company.
- Name reserved; activity checked against the Ninth and Tenth Schedules.
- Beneficial owners identified at 25% and verified.
- s.5A and s.5B declarations made.
- Annual declaration, economic substance declaration and payroll registrations diarised.

## Sources

| Source | URL | Read on |
|---|---|---|
| Government of Bermuda, limited companies (last updated 4 September 2026): read for company forms, local and exempted rules, the incorporation steps, the memorandum, declarations, continuance, annual filings and the Beneficial Ownership Act 2025 | https://www.gov.bm/limited-companies | 2026-11-14 |
| CITA, economic substance: read for the declaration due date and the legislation list | https://www.cita.bm/economic-substance | 2026-11-14 |

Not yet confirmed: the annual government fee scale by assessable capital and the incorporation fees (the old file did not give them; the fee schedule was not found on the pages read); the old file's "typical authorised capital USD 12,000" (no official source; removed).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `bm-company-formation` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/bm-company-formation. If neither is available, confirm every figure against the official source pages cited above before relying on it.
