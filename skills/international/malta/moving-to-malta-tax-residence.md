---
name: moving-to-malta-tax-residence
description: "Cross-border skill for individuals moving to Malta, tax year 2026. Maps the residence routes and what each one taxes: ordinary residence on the remittance basis for non-domiciled residents (EUR 5,000 minimum tax where foreign income is EUR 35,000 or more), the Global Residence Programme (15% on remitted foreign income, EUR 15,000 minimum, property from EUR 220,000 or rent from EUR 8,750) and its EU counterpart, the Malta Permanent Residence Programme as an immigration status, the 2026 Highly Skilled Individuals Rules (15% on employment income of at least EUR 65,000), the Nomad Residence Permit (10% after 12 months) and the Malta Retirement Programme. Also lists what Malta does tax: Malta work, rent, property transfers, duty. Trigger on: move to Malta, Malta non-dom, Malta GRP, Malta nomad tax, Malta HQP."
jurisdiction: MT
category: international
tax_year: 2026
last_updated: 2026-10-23
version: 1.1
verified_by: pending
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Moving to Malta: residence routes, the remittance basis, and what Malta actually taxes v1.1

Built by Michael Cutajar and the OpenAccountants team. **Source-cited draft: not reviewed by an accountant.** Figures are for tax year 2026 (basis year 2026, assessed in 2027).

**Why this corridor needs a skill.** Malta takes in more relocating wealth per capita than
almost any EU state, yet most arrival advice is sold by visa agencies and stops at the permit.
The tax layer is where Malta actually competes: a **remittance-basis system** open to any
resident non-domiciled person (not a special permit — the default law), **no wealth tax, no
inheritance or estate tax, no gift tax, no personal exit tax**, and a treaty network of 70+
conventions inside the EU's legal order. The catch is that "Malta is tax-free" is wrong in
five specific ways, and the people who get burned are the ones who never learned what Malta
*does* tax. This skill is written from the Maltese end of the corridor.

**Who it's for.** Individuals relocating to Malta (from the UK, EU, or further), and their
accountants on the origin side. Corporate structuring (the 35%/refund imputation system,
Pillar Two) is flagged but not the focus.

## Part 2 — The residence routes

**1. Ordinary residence (the default, and often the best).** EU/EEA nationals can simply
move: register, spend **more than 183 days** in Malta in a year (or come to establish Malta as
the regular base), and you are resident. Taxed at progressive rates on Malta-source income and on **remitted** foreign
income; the remittance basis applies automatically to anyone resident but **not domiciled**
in Malta. No programme fee, no minimum property value.

**2. The Residence Programme (TRP, EU/EEA nationals) / Global Residence Programme (GRP,
third-country nationals).** The classic "15% ticket": foreign income **remitted** to Malta is
taxed at a flat **15%** (instead of progressive rates), with a **minimum tax of €15,000 per
year** covering the beneficiary and dependants. GRP requirements: qualifying property bought
for at least **€275,000** (€220,000 in the south of Malta or Gozo) or rented for at least
**€9,600 a year** (€8,750 in the south or Gozo), not spending more than 183 days in any other
single jurisdiction, health insurance, and an authorised registered mandatory. Other income,
including Malta-source income, is taxed at a flat 35%. The Residence Programme is the
EU/EEA/Swiss counterpart; its figures are in `mt-residence-programmes-for-wealthy-families`. Worth running the arithmetic:
if your remitted income is modest, ordinary residence with progressive rates can be *cheaper*
than the €15k minimum.

**3. Malta Permanent Residence Programme (MPRP, third-country nationals).** Residence by
investment: a non-refundable administrative fee of **€60,000**, a government contribution of
**€37,000** (plus €7,500 per adult dependant other than the spouse), property bought for at
least **€375,000** or rented for at least **€14,000 a year** and held for 5 years, a €2,000
donation to a registered NGO, and capital of at least €500,000 (€150,000 of it financial) or
€650,000 (€75,000 financial). MPRP is an **immigration** status, not
a tax status: holders who become resident are taxed like any other resident non-dom
(remittance basis; 15% only if they *also* take GRP).

**4. Highly Skilled Individuals (formerly Highly Qualified Persons) and similar employment
regimes.** From 1 January 2026 the Tax Treatment of Highly Skilled Individuals Rules (LN 20 of
2026) replace the Highly Qualified Persons, innovation and creativity, aviation, maritime and
family-office employee rules. A qualifying employee may elect a flat **15%** on employment
income up to **€7 million** (above that, 35%), where income from the qualifying contract is at
least **€65,000** (rising by €10,000 every five years; former aviation offices start at
€45,000). The benefit runs for five years with up to two five-year extensions, and never
beyond 31 December 2040. This is the one route where Malta-source salary escapes progressive
rates.

**5. Nomad Residence Permit (third-country remote workers).** Permit to live in Malta while
working for foreign employers/clients; income from authorised work is taxed at a flat
**10%**, with no tax for the first 12 months from the later of the permit's issue and
1 January 2024 (the holder can waive that by declaration). An explicit carve-out from the
"work done in Malta is Malta-source at progressive rates" default.

**6. Malta Retirement Programme.** 15% on foreign pension income remitted, minimum tax
€7,500 (+€500 per dependant and per household staff); the pension must be received in Malta
and form at least 75% of chargeable income.

**Citizenship by investment is not the route.** The CJEU ruled against Malta's
exceptional-investment naturalisation in April 2025; the corridor now runs through residence,
not passports.

---

## Part 3 — Remittance-basis mechanics (where the value lives)

A resident **non-dom** is taxed on:
1. Malta-source income and gains — always;
2. Foreign-source **income** — only to the extent **received in / remitted to** Malta;
3. Foreign-source **capital gains** — **never**, even if remitted the same day.

That third leg is the headline: sell a foreign portfolio, wire the proceeds to Malta, and the
gain element is outside the charge. Discipline still matters:

- **Segregate accounts before arriving.** Pre-arrival capital ("clean capital") remits
  tax-free forever, but only if you can *prove* what was capital on the landing date. Keep
  three buckets: clean capital / post-arrival foreign income / post-arrival gains. Mixed
  accounts remit on a worst-first basis in practice, and unpicking them years later is
  forensic accounting at hourly rates.
- **"Remitted" is broad**: card spending in Malta from a foreign account, paying a Maltese
  bill from foreign income, moving money to a Maltese brokerage — all remittances. Loans
  secured on foreign income used in Malta can be too.
- **The €5,000 minimum tax**: non-domiciled residents with foreign income of €35,000+ who
  aren't in a programme pay a minimum €5,000/yr even if they remit nothing. A married couple
  tests the €35,000 on their combined income and pays one €5,000. Anyone whose worldwide-basis
  tax would be lower can opt to be taxed on the worldwide basis instead. That is the floor of the
  whole system — often the entire Maltese tax bill of a careful non-dom.
- **No deemed-domicile clock.** Unlike the UK's old regime, Malta's remittance basis does not
  expire after N years. Domicile shifts only if you genuinely adopt Malta as your permanent
  home — long-term residents keep the basis, but a person who dies domiciled elsewhere also
  keeps their *origin* country's succession reach; plan the estate on both ends.

---

## Part 4 — What Malta actually taxes (the honest list)

| Item | Treatment |
|---|---|
| Malta employment / self-employment | Progressive to **35%** (unless Highly Skilled Individuals or nomad regime) |
| Malta rental income | 15% **final** flat option on gross rent (form TA24 by 30 April), or progressive net basis; elect yearly |
| Sale of Malta immovable property | **8% final tax on the transfer value** (not the gain); 5% within 5 years of buying, 10% if bought before 2004; main-home exemption after 3 years' occupation (sale within 12 months of vacating) |
| Buying Malta property | Duty **5%** (1% provisional at promise of sale; first-time-buyer and other reliefs exist) |
| Foreign income remitted | Progressive, or **15%** under GRP/Residence Programme with the €15k minimum |
| Foreign income kept offshore | Not taxed (but counts toward the €35k trigger for the €5k minimum) |
| Foreign capital gains | **Not taxed**, remitted or not |
| Wealth, inheritance, estate, gifts | **No such taxes.** Transfers of Malta situs property on death attract duty: 5% on property (3.5% on the first €400,000 of an inherited home used as the heir's residence, from 28 October 2025), 2% on shares (5% for property companies). A transfer cost, not an estate tax |
| Social security | Class 1/Class 2 contributions apply to Malta work — capped, but real |

**VAT and daily life:** standard 18% — Malta is a normal EU consumption-tax country.

**Companies, in one paragraph:** Malta's 35% corporate rate with shareholder refunds
(typically 6/7ths) yields the famous ~5% effective rate on trading profits of
non-resident-owned companies, and full participation exemption on qualifying holdings. It
still works, but layer in substance requirements, your origin country's CFC rules (a UK or
German resident owner drags the company back home), and Pillar Two for large groups (Malta
elected the transitional deferral — verify current status). A personal relocation should
never be designed around the company trick; get the personal residence right first.

---

## Part 5 — The corridor discipline (both ends)

1. **Exit the origin country properly.** Malta's low bar does not lower the origin bar: UK
   leavers still fight the SRT and the 5-year temporary-non-residence rule; French leavers
   carry art. 167 bis exit tax; Norwegians carry a 3-year residency tail. The origin-side
   skills in this corridor set cover the hard half.
2. **Mind the treaty tie-breaker.** Keep a home, spend the days, move the centre of vital
   interests. A Malta permit with a life still lived in the origin country resolves *against*
   you under every treaty Malta has.
3. **Get a Maltese tax number and actually file.** The remittance basis is a filing position,
   not an exemption from filing. Returns declare Malta-source and remitted amounts; the
   minimum-tax computation rides on the return.
4. **Bank before you land.** Maltese banks are slow to onboard; the clean-capital
   segregation must exist *before* the residence date, and opening the right account
   structure from abroad takes longer than the flight.
5. **Document the landing date.** Every bucket (clean capital vs post-arrival income) keys
   off it, exactly as the origin country's cessation date keys its side.

---

## The trap list

| Trap | Why it bites |
|---|---|
| "Malta is tax-free, I'll just invoice my clients from here" | Work done *in* Malta is Malta-source: progressive rates up to 35%, unless you're in the Highly Skilled Individuals or nomad regime. The remittance basis never shelters local work. |
| One mixed bank account for everything | Clean capital becomes unprovable; every remittance is presumptively income. Segregate before arrival or lose the benefit in practice. |
| Taking GRP with modest remitted income | The €15,000 minimum can exceed what ordinary progressive rates would have charged. Run both numbers before buying the 15% ticket. |
| Forgetting the €5,000 minimum | Foreign income ≥€35,000 triggers it even with zero remittances — budget it as the annual subscription fee. |
| Treating MPRP as a tax deal | It's a residence permit. The tax outcome is whatever your actual residence + non-dom status produces; some MPRP holders aren't even Maltese tax residents. |
| Buying property in year one "to qualify" | 5% duty in, then final tax on the full transfer value out (5% if sold within 5 years, 8% after); renting satisfies most programmes and keeps the exit cheap while you test the island. |
| Ignoring the origin country's estate reach | Malta not taxing inheritance doesn't stop a UK domicile (or the new residence-based UK IHT tail), French 750 ter, or US estate tax from reaching the same assets. |
| Assuming the corporate 5% is personal | Refund money landing in your hands is your income; your origin country's CFC/anti-avoidance rules may tax the structure anyway if you botched the personal move. |

---

---

*Built by Michael Cutajar and the OpenAccountants team, from the Malta end of the corridor. Malta's offer is simple
once stated precisely: it taxes the island and what you bring to it, and ignores what you
keep outside — with no wealth, inheritance, or exit taxes waiting behind the door. The craft
is all in the arrival: segregate the money before you land, pick the route by arithmetic
rather than brochure, and close the origin country properly with a named accountant on each
end.*

## Sources

| Source | URL | Read on |
|---|---|---|
| MTCA, Tax Residence (more than 183 days) | https://mtca.gov.mt/personal-tax/individual/tax-residence | 2026-10-23 |
| MTCA, Guidance Note on the Remittance Basis (EUR 5,000 minimum, EUR 35,000 threshold) | https://mtca.gov.mt/docs/default-source/documents/mtca-guidelines-on-the-remittance-under-the-income-tax.pdf | 2026-10-23 |
| MTCA, Special Schemes (15% remitted foreign income, other income at 35%) | https://mtca.gov.mt/personal-tax/individual/special-schemes | 2026-10-23 |
| MTCA, Global Residence Programme guidelines (EUR 15,000; EUR 275,000 / 220,000; EUR 9,600 / 8,750) | https://mtca.gov.mt/docs/default-source/documents/personal-tax/individual/special-schemes/the-global-residence-programme/guidelines-grp.pdf?sfvrsn=4c05bc98_1 | 2026-10-23 |
| MTCA, Malta Retirement Programme guidelines (EUR 7,500, EUR 500, 75%) | https://mtca.gov.mt/docs/default-source/documents/personal-tax/individual/special-schemes/the-malta-retirement-programme/guidelines-mrp.pdf?sfvrsn=62844ae3_1 | 2026-10-23 |
| MTCA, Guidelines on the Tax Treatment of Highly Skilled Individuals Rules (LN 20/2026) | https://mtca.gov.mt/docs/default-source/documents/personal-tax/legal-and-technical/guidelines/hqpr-new-amalgamated-rules---guidelines---branded-06-04-(002).pdf?sfvrsn=b605473e_1 | 2026-10-23 |
| MTCA, Overview of Legal Notices January to June 2026 (LN 20/2026: 15% up to EUR 7 million, 5+5+5 years, 2040) | https://mtca.gov.mt/docs/default-source/documents/legislative-developments/2026/overview-of-recently-published-legal-notices-january-to-june-2026-memo.pdf?sfvrsn=1191b20d_1 | 2026-10-23 |
| MTCA, Nomad Residence Permits guidelines (10%, 12 months) | https://mtca.gov.mt/docs/default-source/documents/personal-tax/legal-and-technical/guidelines/nomad-guidelines---12-03-2026.pdf?sfvrsn=f0cc9971_6 | 2026-10-23 |
| Residency Malta Agency, MPRP brochure (EUR 60,000 fee, EUR 37,000, EUR 375,000 / 14,000) | https://residencymalta.gov.mt/wp-content/uploads/2026/08/MPRP-Brochure-English.pdf | 2026-10-23 |
| MTCA, New Property Tax System - FAQ (8% / 5% / 10%, own-residence exemption) | https://mtca.gov.mt/personal-tax/property-taxes/faqs/new-property-tax-system---faq | 2026-10-23 |
| MTCA, General Information on Duty (5%, 1% provisional) | https://mtca.gov.mt/personal-tax/property-taxes/general-information-on-duty | 2026-10-23 |
| MTCA, Share Transfers FAQ (2%, 5% property companies) | https://mtca.gov.mt/personal-tax/sharetransfers/faqs-share-transfers | 2026-10-23 |
| MTCA, Overview of Legal Notices July to December 2025 (LN 306/2025: 3.5% on first EUR 400,000) | https://mtca.gov.mt/docs/default-source/documents/legislative-developments/2026/overview-of-recently-published-legal-notices-july-to-december-2025-memo.pdf?sfvrsn=eaa8dda1_1 | 2026-10-23 |
| MTCA, Rental Income Taxed at 15% - Article 31D FAQ | https://mtca.gov.mt/personal-tax/legal-and-technical/faqs/rental-income-taxed-at-15----article-31d-of-the-income-tax-act | 2026-10-23 |

Not yet confirmed:
- The Residence Programme (EU/EEA/Swiss) thresholds were not re-read in this refresh; this skill points to `mt-residence-programmes-for-wealthy-families` for them.
- The CJEU ruling on investor citizenship (C-181/23, April 2025), the size of Malta's treaty network, the 18% VAT rate and the Pillar Two deferral were not re-read from an official source today.
- legislation.mt was unavailable on 2026-10-23, so statutory texts (Cap. 123, S.L. 123.148, LN 20/2026) were checked through MTCA's published guidance only.
- Budget 2027 is presented on 26 October 2026; nothing from it is reflected here.

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
