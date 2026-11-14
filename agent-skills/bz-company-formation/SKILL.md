---
name: bz-company-formation
description: "How to form and keep a Belize company in good standing in 2026. Covers the entity types the Belize Companies and Corporate Affairs Registry (BCCAR) registers, incorporation through the Online Business Registry System (OBRS), what the registry asks for, who must use a licensed registered agent, the official fee schedule (incorporation, annual return, name reservation), tax registration with the Belize Tax Service on IRIS Belize, and how LLCs are treated for tax. Trigger phrases include form a company in Belize, Belize incorporation, BCCAR, OBRS, Belize LLC, Belize annual return fee and register a business in Belize."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/bz-company-formation"
  jurisdiction: "BZ"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Belize company formation v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Forming a company in Belize at the Belize Companies and Corporate Affairs Registry (BCCAR) and registering it for tax at the Belize Tax Service (BTS), for 2026. BCCAR registers companies (private, public, special purpose, segregated portfolio, private trust and foreign companies, CARICOM and non-CARICOM), business names, limited liability partnerships, international LLCs, international trusts and international foundations ([BCCAR company incorporation](https://bccar.bz/services/company-incorporation/)). Taxes after formation are in [bz-corporate-income-tax](bz-corporate-income-tax.md), [bz-vat-gst](bz-vat-gst.md) and [bz-payroll-social](bz-payroll-social.md).

**Quick answer.** A shareholder (or guarantee member) incorporates a local company online in OBRS; a company with foreign participants, and a foreign company, must use a licensed registered agent. The registry fee for incorporating a company with share capital below 50,000 is BZD 300 for a verified natural person registering on their own, or USD 150 through a registered agent; the annual return is BZD 200 (local filer) or USD 250 (agent). Then obtain a TIN from BTS on IRIS Belize.

## Ask the client first

1. Who are the shareholders, members and directors, and are any of them foreign? (Foreign participants mean a licensed registered agent is required.)
2. What type of entity: private company, public company, special purpose or segregated portfolio company, foreign company, business name, LLP or international LLC?
3. Proposed share capital (the fee schedule changes at 50,000).
4. Nature of the business (the BTS registration form ranks activities by revenue; the activity sets the business tax rate).
5. Does each participant have a Belize social security number, a principal address, email and phone?

## The method, step by step

1. **Check and reserve the name.** Search existing names at the BCCAR company search. A name can be reserved in OBRS free for up to 10 days, or for 90 days for a fee. Restricted words apply and every company name must carry a suffix ([BCCAR company incorporation](https://bccar.bz/services/company-incorporation/); [BCCAR fees schedule](https://bccar.bz/library/fees-schedule/)).
2. **Prepare the documents:** Articles or By-laws of the company; social security ID, principal address, email and phone of each participant (shareholders, members, directors); nature of business.
3. **File in OBRS.** Self-register in the Online Business Registry System. Only a shareholder or guaranteed member may incorporate the company there. A foreign company, or a company with foreign participants, must file through a licensed registered agent; special purpose, segregated portfolio and private trust companies can only be incorporated by a licensed registered agent.
4. **Pay the registry fee** from the fee schedule below and receive the certificate of incorporation.
5. **Register for tax.** Create an account on [IRIS Belize](https://irisbelize.bts.gov.bz) and apply for a TIN; the same TIN covers business tax, GST and customs ([BTS registration guide](https://bts.gov.bz/guide/registration)). On paper, BTS Form 100 asks for the registration number and date from the certificate, the business activities ranked by revenue, start dates and revenue information for GST ([BTS100a instructions](https://media.bts.gov.bz/uploads/BTS_100a_Instructions_for_filling_out_BTS_Registration_form_100_4cc9c69f9c.pdf)).
6. **Register as an employer with the Social Security Board** before the first payroll ([bz-payroll-social](bz-payroll-social.md)).
7. **Keep it in good standing:** file the annual return or renewal each year, record changes of shareholders, directors, name or address with the registry, and file monthly business tax returns (nil if no revenue) from the first month ([bz-corporate-income-tax](bz-corporate-income-tax.md)).

### Registry fees

| Service | Natural person registering on their own (BZD) | Through a registered agent (USD) | Source |
|---|---|---|---|
| Incorporation, share capital below 50,000 | 300.00 | 150.00 | [BCCAR fees schedule](https://bccar.bz/library/fees-schedule/) |
| Incorporation, share capital over 50,000 | 2,000.00 | 1,000.00 | same |
| Foreign company incorporation | n/a | 200.00 | same |
| Annual return or renewal, Belize company (50,000 share capital) | 200.00 | 250.00 | same |
| Annual return or renewal, foreign company | 250.00 | 350.00 | same |
| Change of shareholders or directors | 100.00 | 50.00 | same |
| Name change | 100.00 | 50.00 | same |
| Name reservation for 90 days | 50.00 | 25.00 | same |
| Certificate of good standing | 30.00 | 15.00 | same |
| Restoration | 2,000.00 | 1,000.00 | same |
| Dissolution or liquidation | 200.00 | 100.00 | same |
| Business name registration | 25.00 | n/a | same |

The BCCAR page states that fees are based on the corresponding regulations and in the currency stated there.

## Worked cases

**Formation budget (filing case).** Two Belizean shareholders incorporate a private company with share capital of 10,000 on their own in OBRS, reserve the name for 90 days first, and budget for the first annual return. Registry fees: 50 (name) + 300 (incorporation) + 200 (annual return) = BZD 550, before any professional fees. A company with a foreign shareholder would have to use a licensed registered agent and pay the agent column: USD 25 + USD 150 + USD 250 = USD 425 in registry fees.

```oa-check
name: Belize company formation registry fees, local filer and agent route
inputs:
  name_reservation_bzd: 50
  incorporation_bzd: 300
  annual_return_bzd: 200
  name_reservation_usd: 25
  incorporation_usd: 150
  annual_return_usd: 250
steps:
  - local_total_bzd: name_reservation_bzd + incorporation_bzd + annual_return_bzd
  - agent_total_usd: name_reservation_usd + incorporation_usd + annual_return_usd
expected:
  local_total_bzd: 550.00
  agent_total_usd: 425.00
```

**LLC tax treatment.** Limited liability companies with tax residence in Belize are subject to all Belize tax laws (International Limited Liability Companies (Amendment) Act No. 29 of 2023). For tax, a single-member LLC is treated as a sole proprietorship, two or more members as a partnership, or the LLC may opt to be treated as a company; BTS Form 100 is filed with the registration certificate and Articles of Organization ([BTS notice to LLCs](https://media.bts.gov.bz/uploads/Notice_to_Limited_Liability_Companies_008_bd20925785.pdf)).

## When to refuse or refer

- Special purpose, segregated portfolio and private trust companies, international trusts and foundations, and any structure for non-resident owners: refer to a licensed registered agent; these can only be formed through one.
- Economic substance, IBC and international financial services licensing questions: refer to a specialist; not covered here.
- Do not quote the old figure of about USD 330 for an LLC: the official schedule above is the source.

## Filing and payment

- Registry filings and fees: OBRS (BCCAR). Customer service +501-223-4701 ([BCCAR](https://bccar.bz/services/company-incorporation/)).
- Tax registration: IRIS Belize, TIN application from the online account; helpdesk at BTS ([BTS registration guide](https://bts.gov.bz/guide/registration)).
- After registration: business tax monthly by the 15th; GST registration once supplies reach BZD 75,000 in twelve months.

## Completion checklist

- Name searched and reserved; suffix included.
- Articles or By-laws and participants' details ready; registered agent engaged if any participant is foreign.
- Incorporation filed in OBRS and fee paid; certificate received.
- TIN obtained on IRIS Belize; SSB employer registration if staff.
- Annual return date diarised; first monthly business tax return filed (nil if no revenue).

## Sources

| Source | URL | Read on |
|---|---|---|
| BCCAR company incorporation page, read for entity categories, requirements, OBRS self-registration, free 10-day name reservation and the registered agent rule | https://bccar.bz/services/company-incorporation/ | 2026-11-14 |
| BCCAR fees schedule, read for company, foreign company, annual return, amendment, name reservation, good standing, restoration, dissolution and business name fees | https://bccar.bz/library/fees-schedule/ | 2026-11-14 |
| BTS registration guide, read for the TIN application on IRIS Belize | https://bts.gov.bz/guide/registration | 2026-11-14 |
| BTS100a instructions for registration form 100, read for the information the form asks for | https://media.bts.gov.bz/uploads/BTS_100a_Instructions_for_filling_out_BTS_Registration_form_100_4cc9c69f9c.pdf | 2026-11-14 |
| BTS notice to limited liability companies (29 May 2024), read for LLC tax residence and classification | https://media.bts.gov.bz/uploads/Notice_to_Limited_Liability_Companies_008_bd20925785.pdf | 2026-11-14 |

Not yet confirmed: the Belize Companies Act 2022 text itself (minimum directors and shareholders, beneficial ownership filing and annual attestation, which the old file mentioned); the annual return due date; minimum share capital; incorporation timelines; economic substance requirements.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `bz-company-formation` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/bz-company-formation. If neither is available, confirm every figure against the official source pages cited above before relying on it.
