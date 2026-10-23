---
name: malta-formation
description: "Use this skill whenever asked about forming, incorporating or registering a company in Malta in 2026. Covers the entity types (sole trader, partnership en nom collectif, private limited company, single member company, public limited company), the Companies Act rules on name, memorandum, minimum share capital (EUR 1,164.69 private, EUR 46,587.47 public) and paid-up share (20% and 25%), directors and the company secretary, the Malta Business Registry registration fee (EUR 100 electronic up to EUR 1,500 authorised capital), beneficial owner filings, the annual return (EUR 85 electronic fee, 42 days), accounts deadlines, tax and VAT registration, and post-formation compliance. Trigger on: set up a company in Malta, Malta Ltd, MBR registration, BAROS, incorporate in Malta, Malta company costs, Malta share capital, Malta memorandum and articles, company secretary Malta."
version: 1.1
jurisdiction: MT
tax_year: 2026
last_updated: 2026-10-23
verified_by: pending
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - company-formation-workflow-base
category: formation
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Malta Formation v1.1

Built by Michael Cutajar and the OpenAccountants team. **Source-cited draft: not reviewed by an accountant.**

Tax year 2026. This skill is the workflow for setting up a Maltese company. It does not repeat the tax computations: company tax and refunds are in `mt-corporate-tax`; accounts and audit in `malta-financial-statements`; VAT registration in `malta-vat-return`; employer registration and payroll in `malta-payroll`; the owner's personal tax in `malta-income-tax`; selling the shares later in `selling-a-company-in-malta`; company residence and substance in `mt-company-residence-and-substance`.

## Section 1: Quick Reference

| Field | Value | Source |
| --- | --- | --- |
| Registrar | Registrar of Companies at the Malta Business Registry (MBR); online filing through BAROS | mbr.mt |
| Key law | Companies Act, Cap. 386; Companies Act (Fees) Regulations, S.L. 386.03; Register of Beneficial Owners Regulations, S.L. 386.19 | legislation.mt |
| Minimum authorised capital, private company | EUR 1,164.69 | Cap. 386 art. 72(1) |
| Minimum authorised capital, public company | EUR 46,587.47 | Cap. 386 art. 72(1) |
| Paid up on signing the memorandum | At least 20% of each share taken up (private); at least 25% (public) | Cap. 386 art. 72(3) |
| Registration fee, electronic, authorised capital up to EUR 1,500 | EUR 100 (paper: EUR 245) | S.L. 386.03 Schedule (a)(i); MBR fee page |
| Annual return fee, electronic, authorised capital up to EUR 1,500 | EUR 85 (paper: EUR 100) | S.L. 386.03 Schedule (i)(i) |
| Company tax rate | 35%, with shareholder refunds; see `mt-corporate-tax` | Cap. 123 art. 56(6) |

## Section 2: Entity Types Comparison

| Feature | Sole trader | Partnership en nom collectif | Private limited company | Public limited company (p.l.c.) | Source |
| --- | --- | --- | --- | --- | --- |
| Legal personality | No | Yes, distinct from the partners | Yes | Yes | Cap. 386 art. 4(4) |
| Liability | Unlimited | Unlimited, joint and several (partnership assets first) | Limited to amount unpaid on shares | Same | Cap. 386 art. 7, 67 |
| Members | 1 | 2 or more | At least 2; 1 for a single member company (an exempt company whose objects state its main activity); at most 50 | At least 2 | Cap. 386 art. 7, 68, 209, 212 |
| Directors | Not applicable | Not applicable | At least 1 | At least 2 | Cap. 386 art. 137 |
| Company secretary | No | No | Yes | Yes | Cap. 386 art. 138 |
| Minimum authorised capital | Not applicable | Not applicable | EUR 1,164.69 | EUR 46,587.47 | Cap. 386 art. 72 |
| Tax | Individual rates (`malta-income-tax`) | Each partner taxed on their share, unless the partnership has elected to be treated as a company (Cap. 372 art. 27) | 35% with refunds (`mt-corporate-tax`) | Same | |
| Audit | No | No | Required unless the micro exemption applies (`malta-financial-statements`) | Always | Cap. 386 art. 185(2) |

Recommended default for a trading business with outside customers: a private limited company. Run the sole trader or company comparison in `malta-tax-optimization` first.

## Section 3: Registration Steps

### Step 1: Choose the name

A private company's name must end with "private limited company", "limited" or "ltd." (art. 70(2)). A public company's name ends with "public limited company" or "p.l.c." (art. 70(1)). Name reservation costs EUR 10 a name (S.L. 386.03 Schedule (s)). The Registrar refuses a name that is the same as, or confusingly close to, another partnership's name, is offensive or undesirable, or is already reserved (art. 70(4)). A name with "fiduciary", "nominee" or "trustee" needs authorisation to act as a trustee (art. 70(5)).

### Step 2: Draft the memorandum and articles

The memorandum must state (art. 69(1)):

- private or public company;
- name and residence of each subscriber;
- the company name;
- the registered office in Malta and the company's e-mail address;
- the objects (not simply "any lawful purpose", art. 71);
- authorised capital, its division into shares, shares taken up by each subscriber and the amount paid up on each;
- number of directors, the first directors, and how the company is represented;
- the first company secretary.

Where authorised capital equals the minimum, it must be fully subscribed in the memorandum (art. 72(2)). Articles are optional; the First Schedule model regulations apply where they are silent (art. 75). The Act does not require a notary for a private writing; a public deed is optional (art. 76(2)).

### Step 3: Pay up the share capital

At least 20% of each share taken up (private) or 25% (public) is paid on signing (art. 72(3)). Shares may be paid for in assets "capable of economic assessment", but not in future services (art. 73(1)). A non-cash contribution needs an independent expert's report approved by the Registrar, or a director's declaration where it does not exceed EUR 50,000, delivered before registration (art. 73(4) to (6)). Keep evidence of the cash paid up; MBR's current document checklist is on mbr.mt.

### Step 4: Appoint the officers

- Each director must sign the memorandum or a written consent to act (art. 139(1)).
- Every company has a company secretary (art. 138(1)). The Act sets no residence requirement for the secretary. A company cannot have its sole director as secretary, except an exempt company (art. 138(2)(a), 211(4)). A body corporate can be secretary only if it is a registered company service provider (art. 138(2)(c)).

### Step 5: Register with MBR

Deliver the memorandum and articles to the Registrar (art. 76), electronically through BAROS or on paper, with the registration fee and the beneficial owner declaration (S.L. 386.19). The company exists from the date on its certificate of registration (art. 77(1)). Anyone who trades in the company's name before then is personally liable unless agreed otherwise (art. 78).

Registration fee, electronic format (S.L. 386.03 Schedule (a); MBR fee page):

| Authorised capital | Fee |
| --- | --- |
| Up to EUR 1,500 | EUR 100 |
| Over EUR 1,500, up to EUR 5,000 | EUR 210 plus EUR 12 for each EUR 500 or part over EUR 1,500 |
| Over EUR 5,000, up to EUR 10,000 | EUR 294 plus EUR 17 for each EUR 1,000 or part over EUR 5,000 |
| Over EUR 10,000, up to EUR 50,000 | EUR 379 plus EUR 17 for each EUR 2,500 or part over EUR 10,000 |
| Over EUR 2,500,000 | EUR 1,900 (the bands in between are in the Schedule) |

### Step 6: Tax registration

The company is resident in Malta from incorporation (Cap. 123 art. 2(1)). It needs a tax number with MTCA, and only a registered tax practitioner can file its return, after the company authorises the practitioner on form MTCA02 (see `mt-corporate-tax`).

### Step 7: VAT registration

Register under Article 10 within thirty days of the first taxable supply, unless the company qualifies for and chooses Article 11 (turnover in the preceding calendar year not above EUR 35,000). Article 12 applies to EU acquisitions above EUR 10,000 and to reverse-charge services. Detail: `malta-vat-return`.

### Step 8: Employer registration (if it will employ staff)

Register as a payer under the FSS Rules before the first payroll and report employees to Jobsplus. Detail: `malta-payroll`.

## Section 4: Capital Requirements

| Entity | Minimum authorised capital | Paid up on signing | Non-cash consideration | Source |
| --- | --- | --- | --- | --- |
| Private company | EUR 1,164.69 | 20% of each share taken up | Expert report, or director's declaration if not over EUR 50,000 | Cap. 386 art. 72, 73 |
| Single member company | Same as private | Same | Same | Cap. 386 art. 212 |
| Public company | EUR 46,587.47 | 25% of each share taken up | Same rules | Cap. 386 art. 72, 73 |

At the minimum private capital, fully subscribed, 20% paid up is EUR 232.94 (1,164.69 × 20%, rounded to the cent).

## Section 5: Costs

Only statutory fees are listed. Professional fees, registered office services and bank fees are set by each provider.

| Fee | Electronic | Paper | Source |
| --- | --- | --- | --- |
| Registration, authorised capital up to EUR 1,500 | EUR 100 | EUR 245 | S.L. 386.03 (a)(i) |
| Name reservation | EUR 10 a name | | S.L. 386.03 (s) |
| Annual return, authorised capital up to EUR 1,500 | EUR 85 | EUR 100 | S.L. 386.03 (i)(i) |
| Annual return, over EUR 1,500 up to EUR 5,000 | EUR 120 | EUR 140 | S.L. 386.03 (i)(ii) |
| Annual return, over EUR 5,000 up to EUR 10,000 | EUR 135 | EUR 160 | S.L. 386.03 (i)(iii) |
| Annual return, over EUR 2,500,000 | EUR 1,200 | EUR 1,400 | S.L. 386.03 (i)(x) |
| Certificate about the directors | EUR 10 | | S.L. 386.03 (p) |

Increasing authorised capital later costs the difference between the registration fee at the new and old capital (S.L. 386.03 (e)).

## Section 6: Post-Formation Compliance

| Obligation | Deadline | Source |
| --- | --- | --- |
| Annual return, made up to each anniversary of registration | Within 42 days after the anniversary | Cap. 386 art. 184 |
| Beneficial owners: annual return confirming or changing details | Within 42 days after each anniversary | S.L. 386.19 reg. 6A |
| Beneficial owners: notice of a change | Within 14 days after the change is recorded with the company | S.L. 386.19 reg. 6(1) |
| Change of directors, secretary or representation | Within 14 days | Cap. 386 art. 146 |
| Annual accounts laid before the general meeting | Within 10 months of year end (private); 7 months (public) | Cap. 386 art. 181, 182 |
| Annual accounts delivered to the Registrar | Within 42 days after the end of that laying period | Cap. 386 art. 183 |
| Accounting records kept | 10 years | Cap. 386 art. 163(5) |
| Company tax return and tax | Later of 9 months after year end and 31 March of the year of assessment; 30 September 2027 for a 31 December 2026 year end | S.L. 372.16 rule 2(c)(i); see `mt-corporate-tax` |
| Provisional tax | 30 April, 31 August, 21 December (nil benchmark in the first year of assessment) | S.L. 372.18; see `mt-estimated-tax` |
| VAT returns | As set by registration type | `malta-vat-return` |
| FSS payroll filings | Monthly payments; annual FS3 and FS7 | `malta-payroll` |

Penalties: the Registrar imposes penalties up to the maxima in the Eleventh Schedule to Cap. 386 (art. 427). As the consolidated text reads, a failure to file the annual return carries up to EUR 2,329 plus up to EUR 46 a day (art. 184(3)), and a failure to deliver annual accounts the same (art. 183(6)). Beneficial owner defaults carry up to EUR 5,000 plus up to EUR 100 a day (S.L. 386.19, penalty schedule).

### Bank account

Banks run their own due diligence on directors, shareholders and beneficial owners, the business and the source of funds. Expect to provide the certificate of registration, memorandum and articles, a board resolution, identity and address documents for every director, shareholder and beneficial owner, and a business description.

## Section 7: Foreign Founder Considerations

| Question | Answer | Source |
| --- | --- | --- |
| Non-resident directors | Allowed; the Act has no residence requirement for directors or the secretary | Cap. 386 art. 137, 138 |
| Registered office | Must be in Malta | Cap. 386 art. 69(1)(d) |
| Nominee shareholders or directors | Beneficial owners must still be declared to MBR. Acting as nominee or company officer by way of business is a regulated company service | S.L. 386.19; Company Service Providers Act, Cap. 529 |
| Company residence and tax | A Malta-incorporated company is resident in Malta; management and control abroad raises double residence questions | `mt-company-residence-and-substance` |
| Regulated activity | Registration does not replace any licence the activity needs | Cap. 386 art. 77(3) |

## Section 8: Common Mistakes and Refusals

- **R-MT-F1, shell company request.** Refuse to help form a company whose stated purpose is to hold no real activity in order to hide income or ownership. Refer to a licensed adviser.
- **R-MT-F2, hiding beneficial ownership.** Beneficial owners must be declared (S.L. 386.19). Refuse if the stated purpose is to hide who owns the company.
- **R-MT-F3, regulated activity.** Financial services, gaming, crypto, insurance and investment management need a licence before trading (art. 77(3)). Refer to a regulated-sector specialist.
- **R-MT-F4, sole director as secretary.** Not allowed unless the company is an exempt company (art. 138(2)(a), 211(4)). Fix the memorandum before filing.
- **R-MT-F5, single member without the conditions.** A single member company must be an exempt company whose objects state its main activity (art. 212(1)).

## Section 9: Worked Examples

### Example 1: smallest private company

Two founders form a private company with authorised capital of EUR 1,200, all subscribed, and pay 20% on signing. They file through BAROS.

- Paid up on signing: 1,200 × 20% = EUR 240.
- Registration fee (capital up to EUR 1,500, electronic): EUR 100.
- Annual return fee each year (electronic): EUR 85.

```oa-check
name: Private company, EUR 1,200 authorised capital, 20% paid up, electronic filing
inputs:
  authorised: 1200
  paid_share: 0.20
  registration_fee: 100
  annual_return_fee: 85
steps:
  - paid_up: authorised * paid_share
  - first_year_statutory_fees: registration_fee + annual_return_fee
expected:
  paid_up: 240
  first_year_statutory_fees: 185
```

### Example 2: EUR 20,000 authorised capital

A founder sets authorised capital at EUR 20,000, fully subscribed, 20% paid up, filed electronically.

- Fee band: over EUR 10,000 up to EUR 50,000: EUR 379 plus EUR 17 for each EUR 2,500 or part over EUR 10,000.
- Excess over EUR 10,000 is EUR 10,000, which is 4 blocks of EUR 2,500: 4 × 17 = EUR 68.
- Registration fee: EUR 447. Paid up: EUR 4,000. Annual return fee (over EUR 10,000 up to EUR 50,000, electronic): EUR 300.

```oa-check
name: Registration fee for EUR 20,000 authorised capital, electronic
inputs:
  authorised: 20000
steps:
  - blocks: ceil((authorised - 10000) / 2500)
  - registration_fee: 379 + 17 * blocks
  - paid_up: authorised * 0.20
expected:
  blocks: 4
  registration_fee: 447
  paid_up: 4000
```

## Section 10: Ask the Client First

1. Who will the shareholders and beneficial owners be, and where do they live? One owner or several?
2. Who will be director and who will be company secretary?
3. What will the company do, and does that activity need a licence?
4. How much capital, and paid in cash or in assets?
5. Will the company employ staff or make taxable supplies in Malta soon?
6. Will profits be paid out or kept? (This feeds the tax plan in `mt-corporate-tax`.)

## Sources

| Source | URL | Read on |
|---|---|---|
| Companies Act, Cap. 386 (arts. 4, 7, 67 to 79, 137 to 139, 146, 163, 181 to 185, 209 to 212, 427, Eleventh Schedule) | https://legislation.mt/eli/cap/386/eng/pdf | 2026-10-23 |
| Companies Act (Fees) Regulations, S.L. 386.03 | https://legislation.mt/eli/sl/386.3/eng/pdf | 2026-10-23 |
| Companies Act (Register of Beneficial Owners) Regulations, S.L. 386.19 | https://legislation.mt/eli/sl/386.19/eng/pdf | 2026-10-23 |
| Malta Business Registry, Fee Structure | https://mbr.mt/fees/ | 2026-10-23 |
| Income Tax Act, Cap. 123 (arts. 2, 56(6)) | https://legislation.mt/eli/cap/123/eng/pdf | 2026-10-23 |
| Income Tax (Statutory Dates) Rules, S.L. 372.16 | https://legislation.mt/eli/sl/372.16/eng/pdf | 2026-10-23 |

Not yet confirmed:
- Whether article 42 of Act I of 2026, which substituted the Eleventh Schedule penalties, is in force; the figures above are as the consolidated text reads.
- MBR's current document checklist for BAROS registration (evidence of paid-up capital, identity documents).
- How MTCA issues the company's tax number after MBR registration.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute legal, tax, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before acting upon.

The most up-to-date version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

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
