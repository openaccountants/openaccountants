---
name: sm-company-formation
description: >
  Forming a company in San Marino in 2026 under Law 47/2006 on companies as amended by Law 80/2022: choice between general partnership (società in nome collettivo), SRL and SPA, minimum capital of EUR 25,500 for an SRL and EUR 77,000 for an SPA, the EUR 9,000 SRL paid in full within 60 days, contribution timing (half within 120 days, all within three years), cash deposit or bank guarantee, sole-member rules, the notarial deed and its contents, registration with the Economic Activities Office, legal personality on registration, directors and remote board meetings, beneficial owners and the link to tax residence and the new-company tax incentive. Use for setting up a San Marino SRL or SPA, capital requirements, incorporation steps and director questions. Regulated activities and licences need their own law.
jurisdiction: SM
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: formation
version: 0.3
---

# San Marino company formation and entity choice v0.3

The company-law text used is the official coordinated collection updated to 27 November 2024, read with Law 80/2022. Amendments to company and licensing law made in 2025 and 2026 are not covered (see the end of Sources).

## Section 1: Scope

This skill covers:

- Choosing between a general partnership, an SRL (società a responsabilità limitata) and an SPA (società per azioni).
- Capital, contributions and their timing.
- The incorporation deed, registration and the start of legal personality.
- Directors, ownership disclosure and the link to tax.

It does not cover: regulated financial, insurance, fiduciary, cooperative, professional-company or technology regimes; activity licences; residence permits; fees.

## Section 2: Entity choice

- **General partnership:** partners are jointly and without limit liable ([Law 47/2006, art 4][companies]). Profit is taxed in the partners' hands ([IGR art 10(3)][igr]).
- **SRL and SPA (capital companies):** company obligations belong to the company, subject to special liability rules. Individuals and legal persons can hold shares ([Law 47/2006, arts 2, 4][companies]).
- **Sole member:** a capital company can have one member, at formation or later. Sole-member status must be registered. If the company becomes insolvent, the sole member is liable without limit for debts arising while they held all the shares, where registration of sole-member status was late, or (for a company formed by unilateral act) capital was not paid half within 120 days and in full within three years ([Law 47/2006, art 12, as amended by Law 80/2022][companies]).
- **Professional companies** have their own eligibility and activity limits ([Law 47/2006, art 3][companies]).
- Sole traders and professionals register as economic operators under the activity laws, not company law.

## Section 3: Capital and contributions

| Item | Rule | Source |
|---|---|---|
| Minimum capital, SRL | 25,500 | [Law 47/2006, art 13(1)][companies] |
| Minimum capital, SPA | 77,000 | [Law 47/2006, art 13(1)][companies] |
| Alternative SRL capital | 9,000, all paid within 60 clear days after registration, in cash at a San Marino bank and blocked as security for company debts until liquidation, or by bank guarantee | [Law 47/2006, art 13(1-bis), added by Law 80/2022, art 4][amendment] |
| Ordinary payment timing | At least half within 120 clear days after registration; all within three years | [Law 47/2006, art 10(3)-(4), as amended by Law 80/2022, art 2][amendment] |
| Form of cash contributions | Deposit at a San Marino bank, or a bank guarantee to the company valid for at least three years | [Law 47/2006, art 10(8)][companies] |
| Proof of payment | Directors file a sworn, notarised declaration with the Economic Activities Office within 30 days | [Law 47/2006, art 10(5)][companies] |
| Contributions in total | Not less than share capital; in cash unless the statutes allow otherwise; in kind needs valuation evidence | [Law 47/2006, art 10(1)-(2), (7)][companies] |

Failure to pay contributions on time is a cause of dissolution and liquidation; the court can give directors up to 60 days to regularise ([Law 47/2006, art 10(6)][companies]). If a guarantee is not renewed or replaced by cash 30 days before it expires, the guarantee is enforced ([Law 47/2006, art 10(8)][companies]). Services and personal-use rights are not contributable assets.

## Section 4: Incorporation steps

1. **Owners and managers.** Check each owner, beneficial owner and director against the eligibility and certification rules; collect certificates and translations ([Law 47/2006, definitions and arts 16-17][companies]).
2. **Seat, object and permissions.** The registered office must be in San Marino ([Law 47/2006, art 8][companies]).
   Fix a lawful, possible and determined object ([Law 47/2006, art 9][companies]). Some activities or types need special-law authorisation or a Congress of State clearance ([Law 47/2006, art 16][companies]).
3. **Deed.** A public deed under article 18 with the article 19 particulars: type and name, term, registered office, object, capital, owners and their contributions, governance and representation, first appointments and statutes ([Law 47/2006, arts 18-19][companies]).
4. **Registration.** The notary files with the Economic Activities Office ([Law 47/2006, arts 6, 20][companies]). The company acquires legal personality on registration; acts done before registration make the persons who did them jointly and without limit liable ([Law 47/2006, art 21][companies]).
5. **After registration.** Licence for the activity, tax registration, and ISS registration when hiring.

## Section 5: Directors, disclosure and ongoing duties

- Directors and their representation powers follow articles 48-52 and the statutes ([Law 47/2006, arts 48-52][companies]). Board meetings can be held remotely under article 50; where the chair is not in San Marino, a San Marino notary acts as secretary ([Law 47/2006, art 50][companies]). The company-law text read sets no general rule that a director must be resident in San Marino.
- Owners, directors, powers and sole-member status are registered ([Law 47/2006, art 6][companies]); beneficial owners are disclosed under article 17 and the anti-money-laundering rules.
- Books, accounts and financial statements: articles 72 onward ([Law 47/2006][companies]).
- **Tax residence** is a separate test: a company is resident if its registered office or effective management is in San Marino for most of the tax period ([IGR art 42(2)][igr]).
- **New-company incentive:** registration alone does not give the 50% rate cut. The company must opt in and meet the shareholder and hiring conditions of IGR article 73 (9% instead of 18% for 2026). See `sm-corporate-income-tax`.

## Section 6: Worked examples

### Example 1: two-owner ordinary SRL

Capital 25,500, owners 60% and 40%. Subscriptions 15,300 and 10,200. Paying half within 120 days: 7,650 and 5,100, total 12,750; the remaining 12,750 within three years.

```oa-check
name: San Marino ordinary SRL capital split and first half
inputs:
  srl_capital: 25500
  first_owner_fraction: 0.60
  second_owner_fraction: 0.40
  initial_fraction: 0.50
steps:
  first_owner_subscription: srl_capital * first_owner_fraction
  second_owner_subscription: srl_capital * second_owner_fraction
  first_owner_initial: first_owner_subscription * initial_fraction
  second_owner_initial: second_owner_subscription * initial_fraction
  initial_total: first_owner_initial + second_owner_initial
  remaining_total: srl_capital - initial_total
expected:
  first_owner_subscription: 15300
  second_owner_subscription: 10200
  first_owner_initial: 7650
  second_owner_initial: 5100
  initial_total: 12750
  remaining_total: 12750
```

### Example 2: 9,000 SRL is paid in full (edge case)

An SRL using the 9,000 route must pay all 9,000 within 60 clear days. Paying only half (4,500), as on the ordinary route, leaves 4,500 missing.

```oa-check
name: San Marino 9,000 SRL full payment requirement
inputs:
  alternative_srl_capital: 9000
  required_fraction: 1
steps:
  required_contribution: alternative_srl_capital * required_fraction
  shortfall_if_half_paid: required_contribution - alternative_srl_capital * 0.50
expected:
  required_contribution: 9000
  shortfall_if_half_paid: 4500
```

## Section 7: Ask the client first

1. What will the company do, and is the activity regulated?
2. Owners and beneficial owners, their nationality and residence, and any similar business in the last twelve months (for the tax incentive).
3. Proposed directors and where the board will meet.
4. Capital route (25,500 SRL, 9,000 SRL or SPA) and cash or guarantee.
5. Premises and hiring plan.

## Sources

| Source | URL | Read on |
|---|---|---|
| Official coordinated collection on companies and business (Law 47/2006 and related laws), updated to 27 November 2024: arts 2-6, 9-21, 48-52 | https://www.consigliograndeegenerale.sm/on-line/documento17113696.html | 2026-10-30 |
| Law 80/2022 (amendments to company capital and registration), arts 1-7 | https://www.consigliograndeegenerale.sm/on-line/home/archivio-leggi-decreti-e-regolamenti/documento17132480.html | 2026-10-30 |
| Law 166/2013 (IGR), official coordinated text updated to 22 December 2025: arts 10, 42, 73 | https://www.consigliograndeegenerale.sm/on-line/documento17086436.html | 2026-10-30 |

Not yet confirmed: company and licensing amendments after 27 November 2024; the earlier version's statement that an SPA's capital is deposited in full before incorporation; registration and licence fees; audit and statutory-auditor thresholds; financial-statement filing dates; beneficial-owner register procedure.

[companies]: https://www.consigliograndeegenerale.sm/on-line/documento17113696.html
[amendment]: https://www.consigliograndeegenerale.sm/on-line/home/archivio-leggi-decreti-e-regolamenti/documento17132480.html
[igr]: https://www.consigliograndeegenerale.sm/on-line/documento17086436.html

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
