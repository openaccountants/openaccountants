---
name: malta-formation
description: "Use this skill whenever asked about forming, incorporating or registering a company in Malta in 2026. Covers the entity types (sole trader, partnership en nom collectif, private limited company, single member company, public limited company), the Companies Act rules on name, memorandum, minimum share capital (EUR 1,164.69 private, EUR 46,587.47 public) and paid-up share (20% and 25%), directors and the company secretary, registration through BAROS at the Malta Business Registry with the S.L. 386.03 fees (EUR 100 electronic up to EUR 1,500 authorised capital), beneficial owner declarations, tax, VAT and employer registration, the annual return and accounts deadlines, the 2026 penalties, and foreign founders. Trigger on set up a company Malta, incorporate Malta, Malta Ltd, MBR registration, BAROS, memorandum and articles Malta, beneficial owner Malta."
version: "2.1"
jurisdiction: MT
tax_year: 2026
last_updated: 2026-11-26
depends_on:
  - company-formation-workflow-base
category: formation
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: formation
type: filing-howto
---

# Malta company formation, 2026

## Scope

The workflow for setting up a Maltese company in 2026 under the Companies Act, Cap. 386, with the Malta Business Registry (MBR) through BAROS. It does not repeat the tax work: company tax and refunds [mt-corporate-tax](mt-corporate-tax.md); accounts and audit [malta-financial-statements](malta-financial-statements.md); VAT registration and its thresholds [malta-vat-return](malta-vat-return.md); employer registration and payroll [malta-payroll](malta-payroll.md); the owner's personal tax [malta-income-tax](malta-income-tax.md); selling the shares [selling-a-company-in-malta](selling-a-company-in-malta.md); residence and substance [mt-company-residence-and-substance](mt-company-residence-and-substance.md); sole trader or company [malta-tax-optimization](malta-tax-optimization.md).

Built from the law: not yet approved by an accountant. Formation services for third parties by way of business fall within the company-services regime ([Cap. 529 arts. 2–3](https://legislation.mt/eli/cap/529/eng/pdf)). For the provider's authorisation, registration, notification or exception: Check this point with one of our partner accountants.

## Ask the client first

1. Who will the shareholders and beneficial owners be, and where do they live? One owner or several?
2. Who will be director and who company secretary?
3. What will the company do, and does that activity need a licence?
4. How much authorised capital, and paid in cash or in assets?
5. Will it employ staff or make taxable supplies in Malta soon?
6. Will profits be paid out or kept (feeds [mt-corporate-tax](mt-corporate-tax.md))?

## The method, step by step

1. **Choose the entity** (comparison below). Default for a trading business with outside customers: a private limited company.
2. **Name.** A private company ends with "private limited company", "limited" or "ltd." (art. 70(2)); a public company with "public limited company" or "p.l.c." (art. 70(1)). The Registrar refuses a name the same as or confusingly close to another partnership's, offensive or undesirable, or reserved for another commercial partnership by written notice to the Registrar not more than three months before the second request (art. 70(4)); "fiduciary", "nominee" or "trustee", including derivatives, needs trustee authorisation or permission from the relevant competent authority (art. 70(5)). Reservation: EUR 10 a name.
3. **Memorandum** (art. 69(1)): private or public; name and residence of each subscriber; company name; registered office in Malta and the company's e-mail address; the objects (not just "any lawful purpose", art. 71); authorised capital, its division into shares, shares taken up by each subscriber and the amount paid up on each share, with rights of each class where shares have different classes; number, name and residence of the first directors (corporate names and registered/principal offices where relevant), the manner of representation and the first persons vested with it; first company secretary name and residence, or corporate name, registration number and registered office; and any fixed company duration. A public company also needs the article 69(2) formation-cost/special-advantage document; for its timing where commencement is deferred: Check this point with one of our partner accountants. Monitor the registered e-mail under article 69(4). At minimum authorised capital it must be fully subscribed; above it, at least the statutory minimum must be subscribed (art. 72(2)). Articles are optional; the First Schedule model applies where silent (art. 75). Where the memorandum or articles are a public deed or private writing enrolled with a notary, deliver an authentic copy instead of the original (art. 76(2)).
4. **Pay up the capital.** At least 20% of each share taken up (private) or 25% (public) on signing (art. 72(3)). Non-cash consideration must be "capable of economic assessment", never future services (art. 73(1)), with a report from an independent expert approved by the Registrar, or a director's declaration where it does not exceed EUR 50,000, before registration (art. 73(4) to (6)); the report describes assets and valuation methods and checks nominal value plus any premium. On original subscription, transfer the full non-cash consideration within five years after authorisation to commence business (art. 73(2)). For a founder asset acquired after formation or a subsequent issue: Check this point with one of our partner accountants.
5. **Officers.** Each director personally signs the memorandum indicating consent, or signs and delivers written consent to the Registrar (art. 139(1)), and submits the prescribed declaration about known disqualification circumstances (art. 139(5)). For director disqualification or a constitutional share qualification: Check this point with one of our partner accountants. Every company has a secretary (art. 138(1)); the sole director cannot be secretary except in an exempt company (arts 138(2)(a), 211(4)); a corporate secretary must satisfy article 138(2)(c), which also contains a statutory exception to the registered-CSP rule; for corporate eligibility and that exception: Check this point with one of our partner accountants. Directors must take reasonable steps to ensure an individual secretary has requisite knowledge and experience (art. 138(3)). Do not use a corporate sole director whose own sole director is the company secretary (art. 138(2)(b)). For officers' residence and regulatory status: Check this point with one of our partner accountants.
6. **Register with MBR.** Deliver the memorandum and articles (art. 76) on BAROS or paper, with the fee and the applicable beneficial-owner declaration and supporting documents (S.L. 386.19; conditions below). The company exists from the registration date shown in its certificate, or the later commencement date fixed in the memorandum and recorded in the certificate (art. 77(1)). Do not trade before that date; the pre-existence liability and subsequent good-faith dealings rules in article 78 need case-specific advice: Check this point with one of our partner accountants. Registration does not grant any activity licence (art. 77(3)).
7. **Tax.** Check that the company's income-tax registration and number have been generated. [MTCA](https://mtca.gov.mt/business-tax/corporate/Income_Tax) says this generally happens automatically after incorporation. For residence/substance and the tax computation, use the companion Guides. A registered tax practitioner files through the practitioner services after access is established; retain MTCA02 signed by the company director (same MTCA source).
8. **VAT**: register under the right article within the time the VAT Act sets ([malta-vat-return](malta-vat-return.md)).
9. **Employer**: start the FSS and Jobsplus registration workflow with [malta-payroll](malta-payroll.md). For the precise trigger, deadline and employee notification in the actual case: Check this point with one of our partner accountants.
10. **Bank account**: the bank runs its own due diligence. As a preparation prompt, collect the certificate of registration, memorandum and articles, a board resolution, identity and address documents for every director, shareholder and beneficial owner, and a business description; this is not a bank's verified complete or universal document list.

### Entity types

| Feature | Sole trader | Partnership en nom collectif | Private limited company | Public limited company |
|---|---|---|---|---|
| Legal personality | Outside this company-incorporation workflow | Yes, distinct from the partners (art. 4(4)) | Yes | Yes |
| Liability | Check this point with one of our partner accountants | Unlimited, joint and several, partnership assets first | Limited to the amount unpaid on shares | Same |
| Members | 1 | 2 or more | At least 2; 1 for a single member company (an exempt company whose objects specify its main activity and whose business consists principally of it, art. 212); at most 50 | At least 2 |
| Directors | n/a | n/a | At least 1 | At least 2 (art. 137) |
| Secretary | Not a company office in this workflow | Not decided by this company workflow | Yes | Yes (art. 138) |
| Tax | Use malta-income-tax | Check this point with one of our partner accountants for partnership elections and treatment | Use mt-corporate-tax for rates, refunds and elections | Same |
| Audit | Outside this workflow | Check this point with one of our partner accountants | Apply malta-financial-statements | Apply malta-financial-statements |

A private company's memorandum/articles must restrict share transfers, limit members to fifty and prohibit invitations to the public to subscribe for shares or debentures (art. 209). The comparison does not decide a sole trader's or partnership's separate tax, registration or professional obligations.

### Rates, bands and thresholds

| Item | Figure | Conditions | Source |
|---|---|---|---|
| Minimum authorised capital, private | EUR 1,164.69 | Fully subscribed where capital is the minimum | Cap. 386 art. 72(1), (2): https://legislation.mt/eli/cap/386/eng/pdf |
| Minimum authorised capital, public | EUR 46,587.47 | same | same |
| Paid up on signing | At least 20% of each share (private); 25% (public) | Art. 72(3) | same |
| Non-cash contribution, director's declaration route | Not exceeding EUR 50,000 | Deliver declaration before registration; above it use independent Registrar-approved expert report meeting art. 73(5)-(6) | Cap. 386 art. 73: https://legislation.mt/eli/cap/386/eng/pdf |
| Registration fee, authorised capital up to EUR 1,500 | EUR 100 electronic, EUR 245 paper | S.L. 386.03 Schedule (a)(i) | S.L. 386.03: https://legislation.mt/eli/sl/386.3/eng/pdf |
| Registration fee, over EUR 1,500 to EUR 5,000 | EUR 210 plus EUR 12 per EUR 500 or part over EUR 1,500 (electronic) | Paper EUR 245 plus EUR 15 | same |
| Registration fee, over EUR 5,000 to EUR 10,000 | EUR 294 plus EUR 17 per EUR 1,000 or part over EUR 5,000 (electronic) | Paper EUR 350 plus EUR 20 | same |
| Registration fee, over EUR 10,000 to EUR 50,000 | EUR 379 plus EUR 17 per EUR 2,500 or part over EUR 10,000 (electronic) | Paper EUR 450 plus EUR 20 | same |
| Registration fee, over EUR 2,500,000 | EUR 1,900 electronic, EUR 2,250 paper | Bands in between in the Schedule | same |
| Name reservation | EUR 10 a name | Schedule (s) | same |
| Annual return fee (company other than a SICAV), up to EUR 1,500 | EUR 85 electronic, EUR 100 paper | Schedule (i)(i) | same |
| Annual return fee (company other than a SICAV), over EUR 1,500 to EUR 5,000 | EUR 120 electronic, EUR 140 paper | Schedule (i)(ii) | same |
| Annual return fee (company other than a SICAV), over EUR 5,000 to EUR 10,000 | EUR 135 electronic, EUR 160 paper | Schedule (i)(iii) | same |
| Annual return fee (company other than a SICAV), over EUR 10,000 to EUR 50,000 | EUR 300 electronic, EUR 350 paper | Schedule (i)(iv) | same |
| Annual return fee (company other than a SICAV), over EUR 2,500,000 | EUR 1,200 electronic, EUR 1,400 paper | Schedule (i)(x) | same |
| Annual return | Within 42 days after each anniversary of registration | Art. 184 | Cap. 386: https://legislation.mt/eli/cap/386/eng/pdf |
| Accounts laid before the general meeting | Ten months after the accounting reference period ends (private), seven months (public) | Art. 182; long first/shortened period exceptions in malta-financial-statements | same |
| Accounting records | Ten years | Bound or unified records: from the last entry; art. 163(5) | same |
| Penalty, annual return not filed | Up to EUR 2,329 plus EUR 46 a day | Eleventh Schedule, art. 184(3) | same |
| Penalty, annual accounts not delivered | Up to EUR 2,329 plus EUR 46 a day | Eleventh Schedule, art. 183(6) | same |
| Beneficial owners: applicable change notice or annual confirmation late | Maximum EUR 5,000 plus EUR 100 daily | Reg. 5(3) first-proviso cases excluded; regs 6(5), 6A(2), 15 and Second Schedule | S.L. 386.19: https://legislation.mt/eli/sl/386.19/eng/pdf |
| Beneficial owners: transitional reg. 5(6) non-compliance | Maximum EUR 10,000 plus EUR 500 daily | Applies to the pre-existing-company transition, not every newly formed company; scope and six-month assessment from 10 July 2026 under reg. 5(3) second proviso. For the actual transitional filing/penalty: Check this point with one of our partner accountants | same |

Increasing authorised capital later costs the difference between the registration fees at the new and old capital (Schedule (e)). Penalties under Cap. 386 are imposed by the Registrar up to the Eleventh Schedule maxima (art. 427).

## Boundary and exception table

| Question | Answer |
|---|---|
| Non-resident directors or secretary | Check this point with one of our partner accountants for actual residence, eligibility and regulatory questions |
| Registered office | Must be in Malta (art. 69(1)) |
| Nominee or fiduciary holdings | Assess actual beneficial ownership and control; the natural-shareholder deemed-register exception does not apply to trustee/fiduciary holdings. Provider regulation: Check this point with one of our partner accountants |
| Management and control abroad | Double residence questions: [mt-company-residence-and-substance](mt-company-residence-and-substance.md) |
| Regulated activity | Registration grants no licence (art. 77(3)) |
| Sole director as secretary | Not allowed unless exempt company (arts 138(2)(a), 211(4)) |
| Single member company | Art. 212(1): meet the full article 211 exempt-company conditions, specify the main activity in the objects and carry on principally that activity. The article 211 conditions must be in the memorandum/articles: at most fifty debenture holders, no corporate director, and no arrangement placing policy with persons other than directors, members or debenture holders |

## Worked cases

### Case 1: EUR 20,000 authorised capital, electronic

Fully subscribed, 20% paid up, filed on BAROS. Band: over EUR 10,000 to EUR 50,000: EUR 379 plus EUR 17 for each EUR 2,500 or part over EUR 10,000. Excess EUR 10,000 = 4 blocks: EUR 68. Registration fee EUR 447; paid up EUR 4,000; annual return fee EUR 300 assuming the same authorised capital and an ordinary company other than a SICAV. At the smallest common set-up, EUR 1,200 authorised, the fee is EUR 100, paid up EUR 240, annual return EUR 85.

```oa-check
name: Registration fee for EUR 20,000 authorised capital, electronic, and paid-up share
inputs:
  authorised: 20000
steps:
  - blocks: ceil((authorised - 10000) / 2500)
  - registration_fee: 379 + 17 * blocks
  - paid_up: authorised * 0.20
  - first_year_fees: registration_fee + 300
expected:
  blocks: 4
  registration_fee: 447
  paid_up: 4000
  first_year_fees: 747
```

## When to refuse or refer

- **R-MT-F1, shell company.** Refuse to help form a company whose stated purpose is to hold no real activity in order to hide income or ownership.
- **R-MT-F2, hiding beneficial ownership.** Refuse concealment; apply the actual declaration and register rules below, including their exceptions.
- **R-MT-F3, regulated activity.** For financial services, gaming, crypto, insurance or investment authorisations: Check this point with one of our partner accountants. Registration alone grants no activity licence.
- **R-MT-F4, sole director as secretary**, **R-MT-F5, single member without the conditions**: fix the memorandum before filing.
- Formation by way of business for third parties: Check this point with one of our partner accountants for the applicable Cap. 529 authorisation, registration, notification or exception.

## Filing and payment

1. Reserve the name on BAROS (EUR 10).
2. Prepare the signed memorandum, any articles, directors' consents and declarations, applicable beneficial-owner declaration with certified ID, name-reservation confirmation, officers/shareholders' ID and paid-up-capital evidence. The [MFSA/MBR overview, page 65](https://www.mfsa.mt/wp-content/uploads/2024/11/MFSA-Regulatory-Brochure-Financial-Services-in-Malta.pdf) describes BAROS submission and these broad document categories. For the current portal fields, signing route, required attachments and any extra due diligence: Check this point with one of our partner accountants. Pay the applicable registration fee.
3. Receive the certificate; apply its registration or later fixed commencement date under article 77(1).
4. After registration: confirm the tax number and establish MTCA02 access; route VAT, FSS and Jobsplus to the companion Guides.
5. Calendar the article 184 annual return within 42 days after the registration anniversary. Apply the separate beneficial-owner rules below. Notify director, secretary or representation changes within fourteen days of the event (art. 146). For accounts, apply the article 182 reference-period deadline and article 183 delivery period; use **malta-financial-statements**, including long-first-period exceptions. Route the company return and provisional-tax calendar to **mt-corporate-tax** and **mt-estimated-tax**; this Guide supplies no independent tax deadline or first-year exemption.

### Beneficial ownership: apply the actual exception before filing

[Source: S.L. 386.19 regs. 2–6A, 15 and Second Schedule](https://legislation.mt/eli/sl/386.19/eng/pdf), read 26 November 2026, including the consolidated L.N. 226 of 2026 amendment.

- For ordinary in-scope incorporations, reg. 3 requires the First Schedule declaration with the memorandum and any articles, signed by one proposed director, with the required beneficial-owner information and certified identification copies. For listed companies or their indirectly fully owned subsidiaries within reg. 2(3), or uncertain beneficial-owner identification: Check this point with one of our partner accountants.
- Reg. 5 requires adequate, accurate and up-to-date ownership/control information and a register in Malta. Its first proviso deems the register of members to be the beneficial-owner register only while **all** registered shareholders are natural persons, none acts as trustee or in another fiduciary capacity, no undisclosed natural person ultimately owns or controls more than 25% of voting or other ownership interests or exercises control by other means, and no natural person holds the position of senior managing official.
- While that complete first-proviso test applies, regs. 6 and 6A(1)-(2) exclude the ordinary ownership-change notice and annual confirmation. Otherwise file an ownership-change notice within fourteen days after the change is recorded with the company (reg. 6(1)); the anniversary confirmation is due within forty-two days after its made-up date, signed by a director or secretary (reg. 6A(1)-(2)). A change in senior managing officials has its own fourteen-day notice from recording with the company (reg. 6A(3)).
- Companies formed before 10 July 2026 must assess within six months from that date whether the first proviso applies (reg. 5(3) second proviso); reg. 5(6) governs the non-qualifying transition. For the transitional filing and any penalty in the actual case: Check this point with one of our partner accountants.
- The Second Schedule figures are maxima. Under reg. 15, a penalty is due on default and the daily amount starts the following day; the company is jointly and severally liable with officers, and recovery has a five-year limit. The reg. 5(5) officer defence requires all due diligence and no personal act, omission or negligence causing default.

## Completion checklist

- [ ] Entity chosen; name checked and reserved.
- [ ] Memorandum complete under art. 69(1); capital at or above the minimum and paid up 20% or 25%.
- [ ] Directors' consents; secretary valid.
- [ ] Applicable beneficial-owner declaration and supporting ID filed; ongoing register/notice exception tested in full.
- [ ] Certificate received; tax, VAT and employer registrations started.
- [ ] Annual calendar set: annual return, BO confirmation, accounts, tax return.

## Sources

| Source | URL | Read on |
|---|---|---|
| Read for Cap. 386 arts. 4, 7, 67–78, 137–139, 146, 163(5), 182–184, 209–212, 427 and relevant Eleventh Schedule rows; accounts provisions reuse the completed same-day financial-statements read | https://legislation.mt/eli/cap/386/eng/pdf | 2026-11-26 |
| Read for S.L. 386.03 Schedule (a), (e), (i), (s): capital bands, annual-return exclusion, name fee | https://legislation.mt/eli/sl/386.3/eng/pdf | 2026-11-26 |
| Read for S.L. 386.19 regs. 2–6A, 15 and Second Schedule, including current reg. 5 register exception and transitional proviso | https://legislation.mt/eli/sl/386.19/eng/pdf | 2026-11-26 |
| Read for Cap. 529 arts. 2–3 company-services definitions and regulation; individual applicability referred | https://legislation.mt/eli/cap/529/eng/pdf | 2026-11-26 |
| Read for MTCA general automatic tax-number issue and practitioner/MTCA02 signed-authorisation process | https://mtca.gov.mt/business-tax/corporate/Income_Tax | 2026-11-26 |
| Read for MFSA/MBR overview p. 65: BAROS and broad incorporation document categories, not current portal fields | https://www.mfsa.mt/wp-content/uploads/2024/11/MFSA-Regulatory-Brochure-Financial-Services-in-Malta.pdf | 2026-11-26 |

Not yet confirmed: none in the usable guidance. Referred topics above supply no operative conclusion.
