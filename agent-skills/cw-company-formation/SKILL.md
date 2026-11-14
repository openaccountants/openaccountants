---
name: cw-company-formation
description: "How to start a business in Curacao and register it for tax, 2026. Choosing the legal form (sole trader, V.O.F., maatschap, C.V., B.V., N.V., foundation, SPF) and the taxes each pays, the notary deed for a B.V., N.V. or foundation, registration in the Chamber of Commerce trade register with its fees by invested capital, the CRIB number and tax registration with the Belastingdienst, SVB registration for staff, permits including the establishment permit, and record keeping. Trigger phrases include start a company in Curacao, Curacao B.V., KvK Curacao, CRIB number, vestigingsvergunning, Curacao Chamber of Commerce fees."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/cw-company-formation"
  jurisdiction: "CW"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Curacao company formation and tax registration v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Year: 2026. Bodies: the Curacao Chamber of Commerce and Industry (trade register), the Belastingdienst Curacao (CRIB number and tax registration), the SVB (staff), and the government permit desks.

## Scope

Covers: choosing the legal form, the steps to register it, registry fees, tax and staff registration, permits and records. Does not cover: drafting articles or company law (refer to a civil-law notary), the taxes themselves (`cw-income-tax`, `cw-corporate-income-tax`, `cw-vat-gst`, `cw-payroll-social`), residence and work permits in detail, or regulated licences (banking, gaming, trust services).

## Ask the client first

1. Alone or with others? Is limited liability needed?
2. Will the business employ staff, and when?
3. How much capital will be invested (it sets the Chamber fee scale)?
4. What activity, and does it need a permit?
5. Are the owners or directors foreign nationals needing residence or work permits?

## The method, step by step

1. **Choose the legal form.** The Belastingdienst's own summary ([Tax Office Curacao handbook 2026](https://belastingdienst.cw/wp-content/uploads/2026/08/FIN_Succesvol_Ondernemen_versie2-1.pdf); [Tax Office Curacao, Startende ondernemers](https://belastingdienst.cw/ondernemer/themas/startende-ondernemers/)):

| Form | Liability | Taxes | Register with |
|---|---|---|---|
| Sole trader (eenmanszaak) | Owner, with private assets | Income tax on profit, OB, wage tax for staff | Chamber of Commerce, Belastingdienst, SVB |
| V.O.F. | All partners, privately | Each partner income tax on their share; OB; wage tax | Chamber, Belastingdienst, SVB |
| Maatschap (professional partnership) | Partners | Each partner income tax; OB; wage tax | Chamber, Belastingdienst, SVB |
| C.V. | Managing partners; silent partners bring capital | Managing partners income tax on their share, silent partners on their return; OB; wage tax | Chamber, Belastingdienst |
| B.V. or N.V. | The company | Profit tax, OB, wage tax for directors and staff | Notary, Chamber, Belastingdienst, SVB |
| Foundation or association | The body, not the board (unless mismanagement) | Profit tax on business activity, OB possibly | Notary, Chamber |
| Stichting Particulier Fonds (SPF) | The foundation | Often exempt from profit tax; payments to beneficiaries taxed | Notary, Chamber |

2. **Notary deed** for a B.V., N.V., foundation or SPF: the handbook lists the notary as a registration step for these forms (same handbook). The deed is then filed with the tax registration (step 4).
3. **Register in the trade register** of the Chamber of Commerce. The fee has two parts, a registration fee and an annual contribution, both set by invested capital; see the rates table ([Curacao Chamber of Commerce, Tariffs](https://www.curacaochamberofcommerce.com/registry-services/tariffs/)). Excerpts are ordered by email to registry@curacao-chamber.cw with proof of payment, unless the business is in arrears with its annual contribution, in which case visit the registry (same page).
4. **Apply for a CRIB number** with the Belastingdienst through the contact form or info.belastingdienst@gobiernu.cw. Documents ([Tax Office Curacao, Omzetbelasting](https://belastingdienst.cw/ondernemer/themas/omzetbelasting/)):
   - N.V., B.V., foundation or association: the notarial deed of incorporation, the Chamber of Commerce extract, the representative's or director's details, a valid ID (sedula or passport);
   - sole trader: the Chamber extract and a valid ID;
   - V.O.F. or maatschap: the Chamber extract, the partners' agreement and a valid ID;
   - with employees: the number of employees, the first start date and the gross payroll.
   The CRIB number is emailed when ready. Every administratieplichtige must have one ([Tax Office Curacao handbook 2026](https://belastingdienst.cw/wp-content/uploads/2026/08/FIN_Succesvol_Ondernemen_versie2-1.pdf)).
5. **Open a portal account** to file returns online; all payments go by bank ([Tax Office Curacao, Omzetbelasting](https://belastingdienst.cw/ondernemer/themas/omzetbelasting/)).
6. **Register staff** with the Belastingdienst and the SVB before the first payroll (same handbook); see `cw-payroll-social`.
7. **Permits.** Check which permits the activity needs and start only once they are granted. The handbook points to the establishment permit (vestigingsvergunning) at loketdigital.gobiernu.cw, customs permits for import and export, and residence and work permits for foreign workers; enquiries go to the Ministry of Economic Development (info.meo@gobiernu.cw) and the permit desk of the Ministry of Administration, Planning and Service (infovergunningenloket@gobiernu.cw) (same handbook).
8. **Books and records:** keep proper books from day one and keep all records 10 years ([Tax Office Curacao, Startende ondernemers](https://belastingdienst.cw/ondernemer/themas/startende-ondernemers/)).
9. **Small sole traders:** with turnover of NAf 30,000 or less, consider the RKO turnover tax relief; see `cw-vat-gst`.

### Rates, bands and thresholds

Chamber of Commerce registry fees, "prices as of the 1st of January 2015", still shown on the Chamber's site for 2026:

| Scale and invested capital (XCG) | Registration fee | Annual contribution | Source |
|---|---|---|---|
| 1: 0 to 15,000 | 100 | 100 | [Curacao Chamber of Commerce, Tariffs](https://www.curacaochamberofcommerce.com/registry-services/tariffs/) |
| 2 to 4: 15,001 to 100,000 | 125 | 125 | same |
| 5: 100,001 to 150,000 | 160 | 160 | same |
| 6: 150,001 to 200,000 | 250 | 250 | same |
| 7: 200,001 to 500,000 | 325 | 352 (as printed) | same |
| 8: 500,001 to 1,000,000 | 440 | 440 | same |
| 9: 1,000,001 to 2,000,000 | 875 | 875 | same |
| 10: 2,000,001 to 3,000,000 | 1,000 | 1,000 | same |
| 11: 3,000,001 to 4,000,000 | 1,175 | 1,175 | same |
| 12 and 13: 4,000,001 and higher | 1,250 | 1,250 | same |
| Excerpt of registration | XCG 12.50 (the same page also says XCG 13.50) | | same |
| Originally signed excerpt | XCG 25 | | same |
| Declaration about a registration | XCG 10 to 25 | | same |
| Copy of deposited documents | XCG 1 per page side | | same |

## Boundary and exception table

| Situation | What to do | Source |
|---|---|---|
| Sole trader who wants limited liability | Use a B.V. or N.V.; a sole trader is liable with private assets | [Tax Office Curacao handbook 2026](https://belastingdienst.cw/wp-content/uploads/2026/08/FIN_Succesvol_Ondernemen_versie2-1.pdf) |
| Business in arrears with its annual Chamber contribution | Email excerpts are refused; visit the registry | [Curacao Chamber of Commerce, Tariffs](https://www.curacaochamberofcommerce.com/registry-services/tariffs/) |
| Activity started before the permit | Risk of fines or closure | [Tax Office Curacao handbook 2026](https://belastingdienst.cw/wp-content/uploads/2026/08/FIN_Succesvol_Ondernemen_versie2-1.pdf) |

## Worked cases

**Case 1: first-year Chamber costs for a B.V. with XCG 120,000 invested.** Scale 5: registration 160 plus the first annual contribution 160, plus one excerpt at 12.50 for the CRIB application: 332.50. Then the CRIB application with the notarial deed, the excerpt, the director's details and ID.

```oa-check
name: Curacao Chamber costs, B.V. with XCG 120000 invested
inputs:
  registration_fee: 160
  annual_contribution: 160
  excerpt: 12.50
steps:
  - first_year_cost: registration_fee + annual_contribution + excerpt
expected:
  first_year_cost: 332.50
```

## When to refuse or refer

- Drafting articles, shareholder agreements or choosing between a B.V. and N.V. on company-law grounds: refer to a Curacao civil-law notary.
- Regulated activities (banking, insurance, gaming, trust services): refer; separate licences apply.
- Residence and work permits: refer to the government permit desk.
- Minimum capital, local director or substance requirements: not on the pages read; refer to a notary.

## Filing and payment

- Chamber fees are paid with proof of payment sent with the request ([Curacao Chamber of Commerce, Tariffs](https://www.curacaochamberofcommerce.com/registry-services/tariffs/)).
- After the CRIB number: monthly OB and wage tax returns by the 15th (or the OB band), profit tax returns 3 and 6 months after year end; see the tax skills.

## Completion checklist

- [ ] Legal form chosen and, for a B.V., N.V., foundation or SPF, the notarial deed signed.
- [ ] Trade register entry, registration fee and annual contribution paid, excerpt obtained.
- [ ] CRIB number received and portal account opened.
- [ ] Staff registered with the Belastingdienst and the SVB.
- [ ] Permits granted before trading.
- [ ] Bookkeeping set up; records kept 10 years.

## Sources

| Source | URL | Read on |
|---|---|---|
| Curacao Chamber of Commerce and Industry, Tariffs: read for the 13 fee scales, the annual contribution and excerpt fees | https://www.curacaochamberofcommerce.com/registry-services/tariffs/ | 2026-11-14 |
| Tax Office Curacao handbook "De basis van succesvol ondernemen" (2026): read for the legal-form table, registration bodies, CRIB duty, permits and contacts | https://belastingdienst.cw/wp-content/uploads/2026/08/FIN_Succesvol_Ondernemen_versie2-1.pdf | 2026-11-14 |
| Tax Office Curacao, Startende ondernemers: read for legal forms, their taxes and the 10-year record duty | https://belastingdienst.cw/ondernemer/themas/startende-ondernemers/ | 2026-11-14 |
| Tax Office Curacao, Omzetbelasting: read for the CRIB application documents and portal | https://belastingdienst.cw/ondernemer/themas/omzetbelasting/ | 2026-11-14 |

Not yet confirmed: Book 2 of the Curacao Civil Code (minimum capital, no-minimum-capital rule for a B.V., share transfer rules), which the old file stated citing a law firm; local director and substance requirements; incorporation timelines; the director's licence for foreign directors; whether the excerpt costs XCG 12.50 or 13.50 (the Chamber page states both); the scale 7 annual contribution (printed 352 against a registration fee of 325).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `cw-company-formation` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/cw-company-formation. If neither is available, confirm every figure against the official source pages cited above before relying on it.
