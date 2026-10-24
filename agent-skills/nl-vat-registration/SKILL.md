---
name: nl-vat-registration
description: "Netherlands VAT (btw, omzetbelasting) registration for 2026: who is an entrepreneur for VAT, how a Dutch business gets its btw-id and ob-nummer through the KVK, how a business not established in the Netherlands registers with the Aanmelding Onderneming buitenland form, when the reverse charge (art. 12 Wet OB 1968) means it need not register, and when a fiscal representative is required. Covers the small business scheme (KOR, EUR 20,000), the EU-KOR (EUR 100,000), joining and leaving deadlines, the EUR 10,000 EU distance-sales threshold, registration for the OSS Union, non-Union and import schemes and their quarterly and monthly returns, and penalties. Trigger on \"do I need a Dutch VAT number\", \"register for btw\", \"join the KOR\", \"OSS Netherlands\", \"foreign company VAT Netherlands\", \"fiscal representative Netherlands\". Out of scope: filling in the return boxes (nl-vat-return, netherlands-vat-return), income tax (nl-income-tax), cross-border income (nl-cross-border)."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/nl-vat-registration"
  jurisdiction: "NL"
  tax_year: "2026"
  last_updated: "2026-10-23"
  authored_by: "Ryan Duguid"
  trust_label: "Accountant-authored"
  review_status: "pending_review"
---

# Netherlands VAT registration, KOR, OSS and non-established businesses (2026)

This skill answers one question: does this business need to be registered for Dutch VAT, and if so, how and under which scheme? It does not fill in returns. For the boxes, rates per supply, input VAT and corrections, use [nl-vat-return](nl-vat-return.md) or [netherlands-vat-return](netherlands-vat-return.md).

Tax year 2026 (calendar year). Law: Wet op de omzetbelasting 1968 (Wet OB 1968) as in force from 1 January 2026.

## Who this applies to

**Entrepreneur for VAT.** Anyone who carries on a business independently is an entrepreneur (ondernemer). Business includes a profession and the exploitation of an asset to obtain lasting income from it (art. 7(1) and (2) Wet OB 1968). A person who is not an entrepreneur cannot get a VAT number.

Sort the client into one of four groups before doing anything else:

| Group | Test | Route |
|---|---|---|
| A. Established in the Netherlands | Lives in or is established in the Netherlands, or has a fixed establishment (vaste inrichting) there | Register at the KVK; the Belastingdienst then decides on VAT registration |
| B. EU business, not established in the Netherlands | Established in another EU state, no Dutch fixed establishment | Registers in the Netherlands only if it must file a Dutch return; OSS and EU-KOR run through its home state |
| C. Non-EU business, not established in the Netherlands | Established outside the EU, no Dutch fixed establishment | Registers with the Aanmelding Onderneming buitenland form when it must file, wants a refund, or wants to use OSS through the Netherlands |
| D. Fixed establishment not involved | Has a Dutch fixed establishment, but that establishment takes no part in the supply | Treated as non-established for that supply (art. 12(4) Wet OB 1968) |

The Belastingdienst treats a business as foreign when it is an entrepreneur for VAT, does not live in or is not established in the Netherlands, and has no fixed establishment there.

**When a non-established business must register (groups B and C).** It registers with the Dutch Belastingdienst if:
- it is an entrepreneur and must file a Dutch VAT return; or
- it is a non-EU business with no Dutch return to file and wants a refund of Dutch VAT; or
- it is a non-EU business and wants to use OSS through the Netherlands.

**When it does not need to register.** No Dutch registration is needed if:
- it is an EU business that does not have to file a Dutch return (for example, all its Dutch supplies are reverse-charged to the customer);
- it is an EU business that only wants Dutch VAT back: it claims through its own state's refund portal instead;
- it is a non-EU business selling goods already in the EU to Dutch consumers and is registered for the OSS Union scheme in another EU state;
- it is a non-EU business selling goods through a platform where the platform is the deemed supplier;
- it is a non-EU business supplying services to Dutch consumers and reports them through the non-Union scheme in another EU state.

**The reverse charge removes most B2B registrations.** If a supplier not established in the Netherlands, with no Dutch fixed establishment involved, supplies goods or services to an entrepreneur established in the Netherlands, or to a Dutch-established legal entity, the customer pays the VAT, not the supplier (art. 12(3) Wet OB 1968). The supplier writes "btw verlegd" on the invoice and the customer reports it in box 2a of its own return. This does not apply to intra-EU supplies of goods at 0% (Table II, a, item 6). For general-rule B2B services (art. 6(1)) the customer accounts whenever it has a Dutch btw-id (art. 12(2)). For goods already in the Netherlands, bought from a seller not established there, the reverse charge also applies.

So a non-established business that sells **only** to Dutch businesses normally has no Dutch return to file. It has to register when it sells to Dutch consumers (and is not in OSS), makes intra-EU acquisitions or intra-EU supplies from Dutch stock, imports goods, or otherwise owes Dutch VAT itself.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Standard VAT rate | 21% | 2026 | https://wetten.overheid.nl/BWBR0002629/2026-01-01 (art. 9(1)) |
| Reduced rate (Table I) | 9% | 2026 | https://wetten.overheid.nl/BWBR0002629/2026-01-01 (art. 9(2)(a)) |
| KOR: annual turnover in the Netherlands, Dutch-established business | Not more than EUR 20,000, in the year of joining and the year before | 2026 | https://wetten.overheid.nl/BWBR0002629/2026-01-01 (art. 25a(1)); https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/kor-voorwaarden |
| KOR in the Netherlands for an EU business established elsewhere: Union turnover | Not more than EUR 100,000 (and Dutch turnover not more than EUR 20,000) | 2026 | https://wetten.overheid.nl/BWBR0002629/2026-01-01 (art. 25a(2)) |
| EU-KOR (Dutch business exempt in other EU states): Union turnover | Not more than EUR 100,000 | 2026 | https://wetten.overheid.nl/BWBR0002629/2026-01-01 (art. 25c(5)(a)) |
| KOR notice period to join | At least 4 weeks before the first day of the return period | 2026 | https://wetten.overheid.nl/BWBR0002629/2026-01-01 (art. 25a(5)); https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/aanmelden-kor |
| KOR: last date to join from 1 January 2027 (quarterly filer) | 3 December 2026 | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/aanmelden-kor |
| KOR: wait after leaving | Rest of the year of leaving plus the next calendar year | 2026 | https://wetten.overheid.nl/BWBR0002629/2026-01-01 (art. 25a(7) and (9)); https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/afmelden-kor |
| EU-KOR: deadline for the Belastingdienst to issue the EX number | 35 working days after the prior notification | 2026 | https://wetten.overheid.nl/BWBR0002629/2026-01-01 (art. 25c(5)) |
| EU distance sales of goods and B2C digital services: threshold for Dutch VAT to keep applying | EUR 10,000 a year (excluding VAT), this year and last year, all EU states together | 2026 | https://wetten.overheid.nl/BWBR0002629/2026-01-01 (art. 6k(1)(c)); https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/btw-goederen-eu-particulieren |
| Opting for destination-state VAT below EUR 10,000 | Binding for at least 2 calendar years | 2026 | https://wetten.overheid.nl/BWBR0002629/2026-01-01 (art. 6k(4)) |
| Import scheme (IOSS): consignment value limit | Not more than EUR 150 intrinsic value, excise goods excluded | 2026 | https://wetten.overheid.nl/BWBR0002629/2026-01-01 (art. 28t) |
| Intra-EU acquisitions by exempt businesses and non-business legal entities: threshold | EUR 10,000 a year, this year and last year | 2026 | https://wetten.overheid.nl/BWBR0002629/2026-01-01 (art. 1a(2)) |
| Time for the Belastingdienst to decide on VAT registration after KVK registration | Up to 10 working days | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/btw-identificatienummer-en-omzetbelastingnummer |

There is no general registration threshold. A Dutch-established entrepreneur with taxable supplies is registered whatever its turnover; the KOR is an exemption it can choose after registration, not a threshold below which it stays unregistered.

## The taxable base

This skill does not compute VAT on supplies. The amounts that matter here are the turnover tests.

**KOR turnover in the Netherlands (art. 25(1)(a) and 25(2) Wet OB 1968).** Count, excluding VAT:
- supplies that would be taxed in the Netherlands without the KOR, at 21%, 9% or 0% (exports and intra-EU supplies count), and supplies where Dutch VAT is shifted to a Dutch customer (domestic reverse charge);
- some exempt supplies: real estate, financial services, means of payment and securities, and insurance, unless ancillary to other supplies.

Do not count:
- the sale of business real estate or of movable assets the business depreciates (or could depreciate) for income or corporate tax;
- private use of business goods and services;
- supplies taxed in another country;
- purchases where VAT is reverse-charged to the business, and intra-EU acquisitions.

Once in the KOR, the business charges no VAT, so turnover is the full amount it invoices. All sub-numbers (subnummers) of one business are added together, and the KOR applies to all of them or none.

**EU distance-sales threshold (art. 6k Wet OB 1968).** Add up, excluding VAT, all intra-EU distance sales of goods to non-taxable customers in other EU states and all telecom, broadcasting and electronic services to consumers in other EU states. The EUR 10,000 is one figure for the whole EU, not per country. It only applies to a supplier established in one EU state. A business with a fixed establishment, such as a shop, workshop or factory, in another EU state cannot use the threshold. A warehouse alone is not a fixed establishment for this purpose.

**What the KOR does once joined (art. 25a(3) and (4)).** Supplies are exempt, no VAT appears on invoices, and no input VAT can be deducted. The exemption does not cover new means of transport sent to another EU state or business real estate. Joining can trigger a revision of earlier input VAT on investment goods; that calculation is in [nl-vat-return](nl-vat-return.md).

## Deadlines and filing

### Registration for a Dutch-established business

1. Register the business in the KVK Handelsregister. A bv or nv is entered by the notary at incorporation.
2. The KVK passes the details to the Belastingdienst, which decides within up to 10 working days whether the business is an entrepreneur for VAT.
3. If so, the Belastingdienst sends two numbers by post: the **btw-id** (format NL + 9 digits + B + 2 digits, for invoices and customers) and the **ob-nummer** (for contact with the Belastingdienst only). For a sole trader the ob-nummer contains the BSN and the btw-id does not, so a sole trader gets two separate letters.
4. Bodies that are not entered at the KVK (for example, a silent partnership without a business, informal associations, sole-trader activities the Handelsregister does not treat as a business, foreign legal forms with no Dutch establishment, mutual funds) request a number with the Belastingdienst form "Opgaaf Startende onderneming".

### Registration for a business not established in the Netherlands

- Form: **Aanmelding Onderneming buitenland** (English: Registration Form Foreign Companies). It covers VAT, OSS, corporate tax, payroll taxes, transfer tax and dividend tax refunds. Fill it in on a computer, print, sign and post it with the attachments to Belastingdienst/Klantgegevens, Postbus 2892, 6401 DJ Heerlen.
- Office: the Belastingdienst/Kennis- en Expertisecentrum Buitenland handles all foreign businesses, unless a fiscal representative is appointed. Then the representative's tax office handles the file.
- Returns: usually quarterly, always filed, even for a period with no Dutch activity. The non-resident deadline is the last day of the **second** month after the period (one month later than for Dutch businesses). For 2026: Q3 2026 by 30 November 2026, Q4 2026 by 28 February 2027; monthly October 2026 by 31 December 2026; annual 2026 by 31 March 2027. Return and payment must both arrive by that date.

### Fiscal representative (art. 33g Wet OB 1968)

A non-established business may appoint a Dutch fiscal representative, who needs a licence (vergunning) from the inspector and takes over the filing and payment obligations. A **general licence** covers all the client's taxable supplies, intra-EU acquisitions and imports. A **limited licence** covers a narrow set of transactions, such as imports and the supplies that follow, or excise or bulk goods. The representative is jointly liable up to the amount of the security given.

A fiscal representative is **compulsory** when:
- a non-EU business owes Dutch VAT on distance sales and does not report that VAT through the Union scheme or the import scheme (general licence required);
- a foreign business buys or sells excise goods or mineral oils, or bulk goods, at 0%;
- a foreign business buys mineral oils or bulk goods that are then removed from a bonded or VAT warehouse and owes VAT on that removal.

### KOR

- **Joining:** only after the business has its btw-id and ob-nummer. Apply online in Mijn Belastingdienst Zakelijk. The application must arrive at least 4 weeks before the first day of the return period it should start from. The law starts the exemption from the first return period that begins at least 4 weeks after the Belastingdienst receives the application (art. 25a(5)). For a quarterly filer the Belastingdienst's last dates are: 3 March (from 1 April), 2 June (from 1 July), 2 September (from 1 October), and **3 December 2026 (from 1 January 2027)**. A late application starts the KOR one quarter later. A monthly filer starts from the first day of a month; its application must arrive at least 4 weeks before that day. The Belastingdienst confirms the final start date within 8 weeks; keep filing returns until that letter arrives.
- **Leaving voluntarily:** online in Mijn Belastingdienst Zakelijk. The exit takes effect on the first day of the next calendar quarter that starts at least 4 weeks after the Belastingdienst receives the notice (art. 25a(7)). The Belastingdienst page says "the first day of your return period"; for a quarterly filer that is the same date, and in every case the law decides. The letter with the final end date follows within 8 weeks.
- **Leaving compulsorily:** as soon as turnover in the Netherlands passes EUR 20,000 in a calendar year, the exemption stops. The supply that takes turnover over the limit is itself taxed in full, and the business deregisters at once (art. 25a(9)).
- **No lock-in while in the scheme.** Since 1 January 2025 the law has no minimum participation period. The old three-year minimum no longer applies. The only bar is after leaving: the business cannot rejoin for the rest of that calendar year and the following calendar year (art. 25a(7) and (9)).
- **EU-KOR (Dutch business exempt in other states):** prior notification to the Belastingdienst; the exemption starts when the inspector issues an individual number with the suffix "EX", within 35 working days unless Union turnover is above EUR 100,000 (art. 25c). It then files a quarterly turnover report; the detail is in [nl-vat-return](nl-vat-return.md).
- **EU business using the Dutch KOR:** it notifies its own state (art. 25a(6)); the exemption starts on the date that state issues or confirms its individual number.

### OSS: Union scheme (art. 28s to 28sj Wet OB 1968)

- **Who:** a business making intra-EU distance sales of goods; a platform that is the deemed supplier for goods moving within one state; a business not established in the state of consumption that supplies services to consumers there.
- **Member state of identification:** where the business has its seat. A non-EU business with no EU establishment uses the state where dispatch begins; if dispatch begins in more than one state, it picks one of them and is bound for that year and the two following years (art. 28s(b)).
- **Registering in the Netherlands:** in Mijn Belastingdienst Zakelijk, "btw", then "E-commerce", then "Registratie". A non-established business first registers with the Aanmelding Onderneming buitenland form. In a VAT group (fiscale eenheid), each member registers with its own btw-id.
- **Start date:** normally the first day of the quarter after registration. If the business makes its first qualifying supply before that, it may report that supply through OSS straight away, provided the registration arrives **by the 10th day of the month after the month of that first supply**.
- **Returns (btw-melding):** one per calendar quarter, also when nothing was supplied, filed and paid by the last day of the month after the quarter (Q3 by 31 October, Q4 by 31 January). It cannot be filed before the quarter ends. Amounts in euro, converted at the ECB rate on the last day of the quarter. Corrections to an earlier OSS return go in a later return, up to three years after the original due date.
- **No input VAT in OSS:** input VAT related to OSS supplies is reclaimed on the Dutch return if the business is registered here anyway, or otherwise through the EU refund procedure (art. 28sh).
- **Exclusion:** three consecutive quarters with no return, or three consecutive quarterly reminders not paid within 10 days, lead to exclusion from both the Union scheme and the import scheme for 2 years. Two years of nil returns also end participation.

### OSS: non-Union scheme (art. 28r to 28rl)

For a business with no seat or fixed establishment in the EU that supplies services to EU consumers. Quarterly returns, due by the end of the month after the quarter (art. 28rf).

### OSS: import scheme, IOSS (art. 28t to 28tn)

- For distance sales of goods imported from outside the EU in consignments of not more than EUR 150 (no excise goods). The import itself is then VAT-free.
- **Monthly** return, also when nothing was sold, by the end of the following month (art. 28th).
- A non-EU business with no Dutch fixed establishment can only register here through an **intermediary** (tussenpersoon) established in the Netherlands; one intermediary at a time. An EU business may use an intermediary but does not have to. A Norwegian business needs no intermediary for consignments from Norway.

## Penalties and interest

| Failure | Penalty | Source |
|---|---|---|
| Return filed late or not at all (Dutch and foreign businesses) | EUR 82 per return, after a 7-calendar-day grace period | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/boetes/u_doet_geen_of_te_laat_aangifte |
| VAT paid late, or not, or too little | 3% of the late or unpaid amount, minimum EUR 50, maximum EUR 6,709 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/boetes/u_betaalt_niet_te_laat_of_te_weinig |
| No return filed | Estimated additional assessment (naheffingsaanslag) on top of the penalties | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/internationaal/btw_voor_buitenlandse_ondernemers/btw_aangifte_doen_en_betalen/uiterste_ontvangstdatum_aangifte_en_betaling_btw_aangifte |
| Union scheme: three consecutive quarters with no return, or three consecutive quarterly reminders not paid within 10 days. Import scheme: the same over three consecutive months | Exclusion from both the Union scheme and the import scheme for 2 years | https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/btw-melden-eenloketsysteem |

The first late payment that is paid within the grace period gets a notice, not a penalty, if the previous return was paid on time and in full. Failing to register is not a separate fixed fine: the Belastingdienst raises an additional assessment for the VAT that should have been charged, with tax interest (belastingrente) and, where there was gross negligence or intent, a penalty of up to 100% of the tax. Those rules and the 2026 tax interest rate are in [nl-vat-return](nl-vat-return.md).

## Cross-border points

- **Dutch business selling to EU consumers.** Below EUR 10,000 in both last year and this year, Dutch VAT applies and the sales go on the normal Dutch return. The supply that takes the year's total above EUR 10,000 is the first one taxed in the customer's state (art. 6k(2)), and the following calendar year starts above the threshold too. Dutch VAT can apply again only from 1 January after a full calendar year at or below EUR 10,000. The business then either registers in each customer state or uses the Union scheme from the Netherlands.
- **EU business selling to Dutch consumers from stock in its own state.** It reports Dutch VAT through its own state's OSS; no Dutch registration.
- **Goods stored in the Netherlands.** A foreign seller holding stock in a Dutch warehouse makes domestic Dutch supplies. B2B sales from that stock are reverse-charged to Dutch business customers. Sales to Dutch consumers are not distance sales and need a Dutch registration. Moving its own goods into the Netherlands is an intra-EU acquisition, which also needs a Dutch number.
- **Non-EU business.** If it owes Dutch VAT on distance sales and does not use the Union or import scheme, it must appoint a fiscal representative with a general licence.
- **A Dutch fixed establishment that is not involved** in a supply does not make the supplier "established" for that supply (art. 12(4)), so the reverse charge still applies.
- **Refunds.** An EU business with no Dutch return claims Dutch VAT through its own state's portal. A non-EU business with no Dutch return registers first. The non-resident refund form for that purpose is OB 075.

## Worked examples

### Example 1: Dutch webshop crosses the EUR 10,000 EU threshold in 2026

A bv established only in the Netherlands sells clothes from its Dutch warehouse to consumers in Belgium, Germany and France. Its EU distance sales in 2025 were EUR 7,400, so it started 2026 under the threshold and charged Dutch VAT at 21%. By 30 September 2026 those sales reach EUR 9,600. On 5 October 2026 it makes a sale of EUR 800, taking the year to EUR 10,400. That sale is the first one taxed in the customer's state. Further EU consumer sales in the rest of Q4 2026 are EUR 4,200.

Dutch VAT on the sales up to 30 September is 9,600 x 21% = EUR 2,016, reported on the normal Dutch return in box 1a. The EUR 800 sale and the EUR 4,200 after it, EUR 5,000 in all, carry the VAT of each customer's state. If the bv wants to use the Union scheme for them, its registration must arrive by 10 November 2026 (the 10th day of the month after the first such sale). Its first OSS return, for Q4 2026, is due by 31 January 2027. Because 2026 went over EUR 10,000, all of 2027 is taxed in the customer states from the first sale.

```oa-check
name: Webshop crosses the EUR 10,000 EU distance-sales threshold (2026)
inputs:
  sales_to_30_sep: 9600
  crossing_sale: 800
  later_q4_sales: 4200
  threshold: 10000
  nl_rate_pct: 21
steps:
  - total_2026: sales_to_30_sep + crossing_sale + later_q4_sales
  - headroom_before_crossing: threshold - sales_to_30_sep
  - excess_after_crossing: sales_to_30_sep + crossing_sale - threshold
  - dutch_vat_box_1a: pct(sales_to_30_sep, nl_rate_pct)
  - destination_state_sales: crossing_sale + later_q4_sales
expected:
  total_2026: 14600
  headroom_before_crossing: 400
  excess_after_crossing: 400
  dutch_vat_box_1a: 2016
  destination_state_sales: 5000
```

### Example 2: sole trader tests the KOR for 1 January 2027

A Dutch sole trader (eenmanszaak), filing quarterly, asks in November 2026 whether to join the KOR from 1 January 2027. In 2025 it had: taxable Dutch sales at 21% of EUR 15,800, an intra-EU supply of goods at 0% of EUR 1,500, the sale of its used business van for EUR 4,000, and services of EUR 2,600 taxed in Belgium. For 2026 it expects taxable Dutch sales of EUR 17,900 and 0% intra-EU supplies of EUR 800.

Counted 2025 turnover: 15,800 + 1,500 = EUR 17,300. The van is a depreciated business asset and the Belgian services are taxed abroad, so neither counts. Counted 2026 turnover: 17,900 + 800 = EUR 18,700. Both years are not more than EUR 20,000, so the trader qualifies. To start on 1 January 2027, the application must arrive by 3 December 2026.

The effect in 2027, if it expects the same Dutch sales and EUR 700 of input VAT: outside the KOR it would pay 17,900 x 21% - 700 = EUR 3,059 net VAT. Inside the KOR it pays nothing and loses the EUR 700 deduction. If its customers are mainly VAT-registered businesses, they lose nothing from a 21% charge they can deduct anyway, so ask who the customers are before recommending it. If it leaves in 2028, it cannot rejoin before 1 January 2030.

```oa-check
name: Sole trader KOR turnover test and 2027 effect
inputs:
  taxed_nl_2025: 15800
  intra_eu_0_2025: 1500
  van_sale_2025: 4000
  services_taxed_abroad_2025: 2600
  taxed_nl_2026: 17900
  intra_eu_0_2026: 800
  kor_limit: 20000
  input_vat_2027: 700
  nl_rate_pct: 21
steps:
  - counted_2025: taxed_nl_2025 + intra_eu_0_2025
  - counted_2026: taxed_nl_2026 + intra_eu_0_2026
  - headroom_2025: kor_limit - counted_2025
  - headroom_2026: kor_limit - counted_2026
  - net_vat_outside_kor_2027: pct(taxed_nl_2026, nl_rate_pct) - input_vat_2027
expected:
  counted_2025: 17300
  counted_2026: 18700
  headroom_2025: 2700
  headroom_2026: 1300
  net_vat_outside_kor_2027: 3059
```

## Ask the client first

1. Where is the business established, and does it have a Dutch fixed establishment (staff and equipment, not just a warehouse or a server)? This decides group A, B, C or D.
2. Who are the customers: Dutch businesses, Dutch consumers, or consumers in other EU states? Business-only sales by a foreign supplier are usually reverse-charged and need no Dutch registration.
3. Where are the goods when sold: Dutch stock, stock in another EU state, or shipped from outside the EU, and in consignments above or below EUR 150?
4. What were the EU distance sales and B2C digital services in 2025 and so far in 2026, all EU states together?
5. For the KOR: counted Dutch turnover in 2025 and expected for 2026, whether customers can deduct VAT, and whether any large investment goods were bought in the last years (revision risk).
6. Is the business already registered for Dutch VAT, for OSS in any state, or part of a VAT group?

## Sources

| Source | URL | Read on |
|---|---|---|
| Wet op de omzetbelasting 1968, version from 1 January 2026 (art. 1a, 6, 6h, 6k, 7, 9, 12, 25 to 25d, 28r to 28tn, 33g) | https://wetten.overheid.nl/BWBR0002629/2026-01-01 | 2026-10-23 |
| Belastingdienst: btw-id and ob-nummer, KVK route | https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/btw-identificatienummer-en-omzetbelastingnummer | 2026-10-23 |
| KVK: the VAT number, and registering without the KVK | https://www.kvk.nl/starten/alles-wat-je-moet-weten-over-het-btw-nummer/ | 2026-10-23 |
| Belastingdienst: what is a foreign business | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/internationaal/btw_voor_buitenlandse_ondernemers/wat_is_een_buitenlandse_ondernemer/ | 2026-10-23 |
| Belastingdienst: tax office and registration for foreign businesses | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/internationaal/btw_voor_buitenlandse_ondernemers/belastingkantoor_en_registratie/ | 2026-10-23 |
| Belastingdienst: Aanmelding Onderneming buitenland form | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/themaoverstijgend/programmas_en_formulieren/aanmelding-onderneming-buitenland | 2026-10-23 |
| Belastingdienst: fiscal representative | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/fiscaal_vertegenwoordiger/ | 2026-10-23 |
| Belastingdienst: reverse charge with foreign businesses | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_berekenen_aan_uw_klanten/waarover_btw_berekenen/verleggingsregeling/wanneer_btw_verleggen/verlegging_bij_zakendoen_met_het_buitenland | 2026-10-23 |
| Belastingdienst: return deadlines for foreign businesses | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/internationaal/btw_voor_buitenlandse_ondernemers/btw_aangifte_doen_en_betalen/uiterste_ontvangstdatum_aangifte_en_betaling_btw_aangifte | 2026-10-23 |
| Belastingdienst: filing returns for foreign businesses | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/internationaal/btw_voor_buitenlandse_ondernemers/btw_aangifte_doen_en_betalen/aangifte_doen/btw_aangifte_doen | 2026-10-23 |
| Belastingdienst: KOR conditions | https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/kor-voorwaarden | 2026-10-23 |
| Belastingdienst: joining the KOR | https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/aanmelden-kor | 2026-10-23 |
| Belastingdienst: leaving the KOR | https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/afmelden-kor | 2026-10-23 |
| Belastingdienst: One Stop Shop (Union and import schemes) | https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/btw-melden-eenloketsysteem | 2026-10-23 |
| Belastingdienst: distance sales of goods within the EU, EUR 10,000 threshold | https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/btw-goederen-eu-particulieren | 2026-10-23 |
| Belastingdienst: import scheme registration for non-EU businesses | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/internationaal/btw_voor_buitenlandse_ondernemers/e_commerce_en_diensten/ik_lever_goederen_van_buiten_de_eu_-_de_invoerregeling/invoerregeling_registratie/ | 2026-10-23 |
| Belastingdienst: late filing penalty | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/boetes/u_doet_geen_of_te_laat_aangifte | 2026-10-23 |
| Belastingdienst: late payment penalty | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/boetes/u_betaalt_niet_te_laat_of_te_weinig | 2026-10-23 |

Not yet confirmed: the exact OSS start rule for a non-EU business registering through the Netherlands (the Belastingdienst page read describes the route for Dutch businesses); the text of the Uitvoeringsbesluit omzetbelasting 1968 on when a fiscal representative is compulsory (the list above is the Belastingdienst's).

> Contributed by Ryan Duguid.

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-23. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `nl-vat-registration` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/nl-vat-registration. If neither is available, confirm every figure against the official source pages cited above before relying on it.
