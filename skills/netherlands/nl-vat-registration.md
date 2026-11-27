---
name: nl-vat-registration
description: >
  Netherlands VAT (btw, omzetbelasting) registration for 2026: who is an entrepreneur
  for VAT, how a Dutch business gets its btw-id and ob-nummer through the KVK, how a
  business not established in the Netherlands registers with the Aanmelding Onderneming
  buitenland form, when the reverse charge (art. 12 Wet OB 1968) means it need not
  register, and when a fiscal representative is required. Covers the small business
  scheme (KOR, EUR 20,000), the EU-KOR (EUR 100,000), joining and leaving deadlines, the
  EUR 10,000 EU distance-sales threshold, registration for the OSS Union, non-Union and
  import schemes and their quarterly and monthly returns, and penalties. Trigger on "do
  I need a Dutch VAT number", "register for btw", "join the KOR", "OSS Netherlands",
  "foreign company VAT Netherlands", "fiscal representative Netherlands". Out of scope:
  filling in the return boxes (nl-vat-return), income tax
  (nl-income-tax), cross-border income (nl-cross-border).
version: 0.4
jurisdiction: NL
tax_year: 2026
last_updated: 2026-11-27
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: filing-howto
---

# Netherlands VAT registration, KOR, OSS and non-established businesses (2026)

This Guide answers one question: does this business need to be registered for Dutch VAT, and if so, how and under which scheme? It does not fill in returns. For the boxes, rates per supply, input VAT and corrections, use [nl-vat-return](nl-vat-return.md).

Tax year 2026 (calendar year). Law: Wet op de omzetbelasting 1968 (Wet OB 1968) as in force from 1 January 2026.

## Who this applies to

**Entrepreneur for VAT.** Anyone who carries on a business independently is an entrepreneur (ondernemer). Business includes a profession and the exploitation of an asset to obtain lasting income from it (art. 7(1) and (2) Wet OB 1968). Do not use that definition to refuse identification to a non-business legal entity with taxable intra-EU acquisitions. Special deemed-entrepreneur cases, including a new means of transport sent to another EU state: Check this point with one of our partner accountants.

Sort the client into one of four groups before doing anything else:

| Group | Test | Route |
|---|---|---|
| A. Established in the Netherlands | Lives in or is established in the Netherlands, or has a fixed establishment (vaste inrichting) there | Use the KVK route where Handelsregister registration is required; otherwise use the direct route below |
| B. EU business, not established in the Netherlands | Established in another EU state, no Dutch fixed establishment | Register if a Dutch return is required; Dutch refunds without a return go through the home state. See the separate OSS and EU-KOR rules below |
| C. Non-EU business, not established in the Netherlands | Established outside the EU, no Dutch fixed establishment | Registers with the Aanmelding Onderneming buitenland form when it must file, wants a refund, or wants to use OSS through the Netherlands |
| D. Fixed establishment not involved | Has a Dutch fixed establishment, but that establishment takes no part in the supply | Treated as non-established for that supply (art. 12(4) Wet OB 1968) |

The Belastingdienst treats a business as foreign when it is an entrepreneur for VAT, does not live in or is not established in the Netherlands, and has no fixed establishment there.

**When a non-established business must register (groups B and C).** It registers with the Dutch Belastingdienst if:
- it is an entrepreneur and must file a Dutch VAT return; or
- it is a non-EU business with no Dutch return to file and wants a refund of Dutch VAT; or
- it is a non-EU business and wants to use OSS through the Netherlands.

**When it does not need to register.** For the following transactions, if they are actually covered by the stated scheme/treatment and there is no separate Dutch filing obligation:
- it is an EU business that does not have to file a Dutch return (for example, all its Dutch supplies are reverse-charged to the customer);
- it is an EU business with no Dutch return to file that only wants Dutch VAT back: it claims through its own state's refund portal instead;
- it is a non-EU business selling goods already in the EU to Dutch consumers and is registered for the OSS Union scheme in another EU state;
- it is a non-EU business selling goods through a platform where the platform is the deemed supplier;
- it is a non-EU business supplying services to Dutch consumers and reports them through the non-Union scheme in another EU state.

**Apply the reverse charge per transaction.** For taxable supplies in the Netherlands outside art. 12(2), if a supplier not established in the Netherlands, with no Dutch fixed establishment involved, supplies goods or services to an entrepreneur resident or established in the Netherlands or with a Dutch fixed establishment, or to a Dutch-established body within the AWR definition, the customer pays the VAT, not the supplier (art. 12(3) Wet OB 1968). For a domestic reverse charge the supplier writes "btw verlegd" on the invoice; the customer uses the domestic reverse-charge section of its return. This does not apply to intra-EU supplies of goods at 0% (Table II, a, item 6). For general-rule B2B services (art. 6(1)) taxable in the Netherlands, the non-established supplier uses art. 12(2) where the customer has a Dutch btw-id. Goods already in the Netherlands follow the recipient and supplier conditions above.

Test each transaction separately: reverse-charged sales alone may not require a Dutch return, but Dutch stock movements, intra-EU acquisitions or supplies, imports and consumer sales can create separate obligations. Do not treat OSS or platform treatment as covering these other transactions. For import arrangements or unusual stock movements: Check this point with one of our partner accountants.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Narrow registration exception (all art. 25b conditions below) | Dutch annual turnover no more than EUR 2,200 | 2026 | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002634/2026-04-01_0/xml/BWBR0002634_2026-04-01_0.xml (art. 25) |
| Standard VAT rate | 21% | 2026 | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002629/2026-01-01_0/xml/BWBR0002629_2026-01-01_0.xml (art. 9(1)) |
| Reduced rate (Table I) | 9% | 2026 | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002629/2026-01-01_0/xml/BWBR0002629_2026-01-01_0.xml (art. 9(2)(a)) |
| KOR: annual turnover in the Netherlands, Dutch-established business | Not more than EUR 20,000, in the year of joining and the year before | 2026 | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002629/2026-01-01_0/xml/BWBR0002629_2026-01-01_0.xml (art. 25a(1)); https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/kor-voorwaarden |
| KOR in the Netherlands for an EU business established elsewhere: Union turnover | Not more than EUR 100,000 (and Dutch turnover not more than EUR 20,000), current and prior year | 2026 | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002629/2026-01-01_0/xml/BWBR0002629_2026-01-01_0.xml (art. 25a(2)) |
| EU-KOR (Dutch business exempt in other EU states): Union turnover | Not more than EUR 100,000 | 2026 | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002629/2026-01-01_0/xml/BWBR0002629_2026-01-01_0.xml (art. 25c(5)(a)) |
| KOR notice period to join | At least 4 weeks before the first day of the return period | 2026 | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002629/2026-01-01_0/xml/BWBR0002629_2026-01-01_0.xml (art. 25a(5)); https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/aanmelden-kor |
| KOR: last date to join from 1 January 2027 (quarterly filer) | 3 December 2026 | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/aanmelden-kor |
| KOR: wait after leaving | Rest of the year of leaving plus the next calendar year | 2026 | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002629/2026-01-01_0/xml/BWBR0002629_2026-01-01_0.xml (art. 25a(7) and (9)); https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/afmelden-kor |
| EU-KOR: ordinary period for issuing or confirming the EX number | 35 working days after notification/update, subject to turnover, destination-state eligibility and additional anti-evasion checks | 2026 | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002629/2026-01-01_0/xml/BWBR0002629_2026-01-01_0.xml (art. 25c(5)-(6)) |
| EU distance sales of goods and B2C digital services: threshold for Dutch VAT to keep applying | EUR 10,000 a year (excluding VAT), this year and last year, all EU states together | 2026 | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002629/2026-01-01_0/xml/BWBR0002629_2026-01-01_0.xml (art. 6k(1)(c)); https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/btw-goederen-eu-particulieren |
| Opting for destination-state VAT below EUR 10,000 | Binding for at least 2 calendar years | 2026 | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002629/2026-01-01_0/xml/BWBR0002629_2026-01-01_0.xml (art. 6k(4)) |
| Import scheme (IOSS): consignment value limit | Not more than EUR 150 intrinsic value, excise goods excluded | 2026 | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002629/2026-01-01_0/xml/BWBR0002629_2026-01-01_0.xml (art. 28t) |
| Intra-EU acquisitions by exclusively non-deducting businesses and non-business legal entities | EUR 10,000 this year and last year; excludes new means of transport and excise goods; taxable-acquisition election overrides | 2026 | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002629/2026-01-01_0/xml/BWBR0002629_2026-01-01_0.xml (art. 1a(2)) |
| Time for the Belastingdienst to decide on VAT registration after KVK registration | Up to 10 working days | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/btw-identificatienummer-en-omzetbelastingnummer |

There is no general EUR 20,000 registration threshold: ordinary KOR entry follows VAT registration. A narrow exception permits a Dutch-established business with Dutch annual turnover no more than EUR 2,200 to apply the exemption without notification only if it has not registered with the inspector or KVK, is not required to do so, and does not use another member state’s small-business exemption (art. 25b; Uitvoeringsbeschikking art. 25). This exception does not discharge incoming reverse-charge or taxable-acquisition liabilities under art. 25b(3).

## The taxable base

This skill does not compute VAT on supplies. The amounts that matter here are the turnover tests.

**KOR turnover in the Netherlands (art. 25(1)(a) and 25(2) Wet OB 1968).** Count, excluding VAT:
- supplies that would be taxed in the Netherlands without the KOR, at 21%, 9% or 0% (exports and intra-EU supplies count), and supplies where Dutch VAT is shifted to a Dutch customer (domestic reverse charge);
- some exempt supplies: real estate, financial services, means of payment and securities, and insurance, unless ancillary to other supplies.

Do not count:
- the sale of real estate used in the business or of movable assets the business depreciates (or could depreciate) for income or corporate tax;
- private use of business goods and services;
- supplies taxed in another country;
- purchases where VAT is reverse-charged to the business, and intra-EU acquisitions.

Once in the KOR, the business charges no VAT, so turnover is the full amount it invoices. All sub-numbers (subnummers) of one business are added together, and the KOR applies to all of them or none.

**EU distance-sales threshold (art. 6k Wet OB 1968).** Qualifying distance sales exclude margin-scheme goods, new means of transport and goods installed/assembled by the supplier; the supplier must arrange or participate in cross-border transport. Add up, excluding VAT, all intra-EU distance sales of goods to non-taxable customers in other EU states and all telecom, broadcasting and electronic services to consumers in other EU states. The EUR 10,000 is one figure for the whole EU, not per country. Apply this Dutch threshold method only to a supplier established solely in the Netherlands, with goods dispatched from the Netherlands. Foreign-stock dispatch requires its own place-of-supply assessment. A business with a fixed establishment, such as a shop, workshop or factory, in another EU state cannot use the threshold. A warehouse alone is not a fixed establishment for this purpose.

**What the KOR does once joined (art. 25a(3) and (4)).** Supplies are exempt, no VAT appears on invoices, and no input VAT can be deducted. The exemption does not cover new means of transport sent to another EU state, or real estate/rights used in the business. The KOR does not exempt incoming reverse-charge VAT, taxable acquisitions or imports. For investment-goods revision on entry, use [nl-vat-return](nl-vat-return.md). Check this point with one of our partner accountants.

## Deadlines and filing

### Registration for a Dutch-established business

1. Check whether Handelsregister registration is required and whether the narrow art. 25b exception applies. Where required, register with KVK.
2. The KVK passes the details to the Belastingdienst, which decides within up to 10 working days whether the business is an entrepreneur for VAT.
3. If so, the Belastingdienst sends two numbers by post: the **btw-id** (format NL + 9 digits + B + 2 digits, for invoices and customers) and the **ob-nummer** (for contact with the Belastingdienst only). For a sole trader the ob-nummer contains the BSN and the btw-id does not, so a sole trader gets two separate letters.
4. A Dutch business that cannot register at KVK uses **Opgaaf startende onderneming (niet ingeschreven in het Handelsregister)**: the relevant online form or the signed PDF sent to Belastingdienst, Postbus 2891, 6401 DJ Heerlen. The authority processes the declaration within 10 working days. A foreign address or foreign legal form uses **Aanmelding Onderneming buitenland**, not the domestic starter form.

### Registration for a business not established in the Netherlands

- Form: **Aanmelding Onderneming buitenland** (English: Registration Form Foreign Companies). It covers VAT, OSS, corporate tax, payroll taxes, transfer tax and dividend tax refunds. Fill it in on a computer, print, sign and post it with the attachments to Belastingdienst/Klantgegevens, Postbus 2892, 6401 DJ Heerlen.
- Office: the Belastingdienst/Kennis- en Expertisecentrum Buitenland handles all foreign businesses, unless a fiscal representative is appointed. Then the representative's tax office handles the file.
- Returns: usually quarterly, always filed, even for a period with no Dutch activity. The non-resident deadline is the last day of the **second** month after the period (one month later than for Dutch businesses). For 2026: Q3 2026 by 30 November 2026, Q4 2026 by 28 February 2027; monthly October 2026 by 31 December 2026; annual 2026 by 31 March 2027. Return and payment must both arrive by that date.

### Fiscal representative (art. 33g Wet OB 1968)

A non-established business may appoint a licensed fiscal representative for VAT returns, payments and ICP obligations (art. 33g). Under Uitvoeringsbesluit art. 24c, a **general licence** covers all liable supplies, acquisitions and imports except transactions covered by a limited representative; its liability per calendar year is capped at the security. A **limited licence** covers only the enumerated import/subsequent-supply and warehouse transactions; its liability is not given that general-licence cap.

Under art. 24d(1), a general representative is compulsory for Dutch-taxable intra-EU distance sales under art. 5a(1)(a) where the head office or establishment is in a third country without the specified mutual-assistance instrument, unless the Union scheme is used. Do not replace this test with “every non-EU business”. IOSS has its own intermediary test below.

Excise goods, mineral oils, bulk goods, zero-rated warehouse transactions and removal from an excise/VAT warehouse have separate representation conditions, including art. 24d(2) and Table II posts 7–8. Do not act on the old blanket “all purchases/sales at 0%” rule. Check this point with one of our partner accountants.

### KOR

- **Joining:** obtain the btw-id/ob-nummer first, then apply in Mijn Belastingdienst Zakelijk. The first eligible return period starts at least 4 weeks after receipt (art. 25a(5)). For quarterly entry: apply by 3 March/2 June/2 September/3 December for 1 April/1 July/1 October/1 January respectively. Thus 3 December 2026 is the published deadline for 1 January 2027. Monthly entry uses a month beginning at least four weeks after receipt. The authority confirms within 8 weeks; keep submitting prepared returns until the confirmed start date.
- **Voluntary exit:** notify in Mijn Belastingdienst Zakelijk. Article 25a(7) starts the exit on the next **calendar quarter** beginning at least four weeks after receipt; this statutory rule controls over the webpage’s “return period” wording. The final-date letter follows within 8 weeks.
- **Compulsory exit:** when counted Dutch turnover exceeds EUR 20,000, deregister immediately; the whole crossing supply is taxed. No three-year minimum participation applies. After voluntary or threshold exit, re-entry is barred for the rest of that calendar year and the next year (art. 25a(7), (9)).
- **EU-KOR (Dutch business exempt in other states):** notify the Belastingdienst beforehand and obtain/confirm the EX number before applying the exemption. Union turnover must not exceed EUR 100,000 in the preceding or current year, and each destination state’s turnover and eligibility conditions must also be met. The ordinary 35-working-day period does not apply where additional anti-evasion checks require more time (art. 25c(5)-(6)). Report turnover quarterly within one month after the quarter; report crossing EUR 100,000 within 15 working days with turnover since the quarter began (art. 25e).
- **EU business using the Dutch KOR:** it notifies its own state (art. 25a(6)); the exemption starts on the date that state issues or confirms its individual number.

### OSS: Union scheme (art. 28s to 28sj Wet OB 1968)

- **Who:** a business making intra-EU distance sales of goods; a platform deemed supplier for qualifying domestic goods; an **EU-established** business supplying consumer services in a member state where it has neither its seat nor a fixed establishment (arts. 28s–28sa). A business with no EU seat or fixed establishment uses the non-Union scheme for services.
- **Member state of identification:** the EU seat, or if there is no EU seat, the EU fixed establishment. If there are several EU fixed establishments, choose one. A business with neither an EU seat nor fixed establishment uses a state where goods dispatch begins; where more than one qualifies, choose one. Those multiple-state choices bind for that year and the next two years (art. 28s(b)).
- **Registering in the Netherlands:** in Mijn Belastingdienst Zakelijk, "btw", then "E-commerce", then "Registratie". A non-established business first registers with the Aanmelding Onderneming buitenland form. In a VAT group (fiscale eenheid), each member registers with its own btw-id.
- **Start date:** normally the first day of the quarter after registration. If the business makes its first qualifying supply before that, it may report that supply through OSS straight away, provided the member state of identification receives the start details **by the 10th day of the month after that first supply** (EU Implementing Regulation 282/2011, art. 57 quinquies(1), including non-established users).
- **Returns (btw-melding):** one per calendar quarter, also when nothing was supplied, filed and paid by the last day of the month after the quarter (Q3 by 31 October, Q4 by 31 January). It cannot be filed before the quarter ends. Amounts in euro, converted at the ECB rate on the last day of the quarter, or the next publication day if none was published that day. While registered, corrections to an earlier OSS return go in a later return, up to three years after the original due date. Corrections after the final return or outside that window go directly to the consumption state (EU Regulation arts. 61 and 61 bis).
- **No input VAT in OSS:** input VAT related to OSS supplies is reclaimed on the ordinary Dutch return if the business is identified here for activities outside OSS, or otherwise through the applicable refund route (art. 28sh); apply the foreign-business refund routes above.
- **Exclusion:** persistent non-compliance includes three immediately preceding periods for which reminders were sent and the return was still not filed within 10 days of each reminder; or full payment was still missing after 10 days, except where each unpaid balance is below EUR 100. Persistent non-compliance excludes the taxpayer from all special schemes for two years following the period of exclusion; an IOSS intermediary-fault exception applies. Two years without qualifying activity is treated as cessation, but does not bar restarting when activity resumes (EU Regulation arts. 58 bis–58 ter).

### OSS: non-Union scheme (art. 28r to 28rl)

For a business with no seat or fixed establishment in the EU that supplies services to EU consumers. It covers all qualifying EU consumer services, with quarterly returns including nil returns, due by the end of the following month (art. 28rf). The art. 57 quinquies(1) start rule above also applies.

### OSS: import scheme, IOSS (art. 28t to 28tn)

- For distance sales of goods imported from outside the EU in consignments of not more than EUR 150 (no excise goods). The import exemption requires VAT to be declared under IOSS and the IOSS number to reach the competent customs office no later than submission of the import declaration (art. 21(e)).
- **Monthly** return, also when nothing was sold, by the end of the following month (art. 28th).
- A business with no EU seat or fixed establishment generally registers here through an **intermediary** (tussenpersoon) established in the Netherlands; one intermediary at a time. An EU business may use an intermediary but does not have to. A Norwegian business needs no intermediary for consignments from Norway.

## Penalties and interest

| Failure | Penalty | Source |
|---|---|---|
| Ordinary return-filing default (Dutch and foreign businesses) | EUR 82 after a 7-calendar-day grace period; exceptional or disputed defaults require case-specific advice | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/boetes/u_doet_geen_of_te_laat_aangifte |
| VAT paid late, or not, or too little | 3% of the late or unpaid amount, minimum EUR 50, maximum EUR 6,709 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/boetes/u_betaalt_niet_te_laat_of_te_weinig |
| No return filed | Estimated additional assessment (naheffingsaanslag) on top of the penalties | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/internationaal/btw_voor_buitenlandse_ondernemers/btw_aangifte_doen_en_betalen/uiterste_ontvangstdatum_aangifte_en_betaling_btw_aangifte |
| OSS non-compliance | Apply the conditional exclusion rule above, rather than automatic exclusion after three late periods | https://eur-lex.europa.eu/legal-content/NL/TXT/?uri=CELEX:02011R0282-20250414 (arts. 58 bis–58 ter) |

The payment concession lasts 7 calendar days after the deadline and requires the previous return to have been paid on time and in full. Repeated/aggravated defaults, culpability, tax interest and the consequences of failing to register require a case-specific assessment; the old statement that there is no separate registration offence is not a usable conclusion. Check this point with one of our partner accountants. Return and payment calculations are covered by [nl-vat-return](nl-vat-return.md).

## Cross-border points

- **EU consumer sales:** apply the place-of-supply threshold/election first. Only sales for which destination VAT is due and which are actually covered by home-state OSS avoid a separate registration on that basis. The crossing supply is taxed in the destination state. If the previous year exceeded EUR 10,000, destination taxation continues for the whole next year; the threshold can apply again after a full calendar year at or below it, unless an election still binds.
- **Dutch stock:** own-account consumer sales within the Netherlands are domestic, not intra-EU distance sales. Test platform treatment and other exceptions before registration. B2B sales follow the reverse-charge conditions above. Moving own stock can create an acquisition obligation; transfer exceptions and call-off stock: Check this point with one of our partner accountants.
- **Refunds:** EU businesses without a Dutch return use the home-state refund portal; non-EU businesses register first. The exact non-resident refund form (formerly stated as OB 075) and special refund conditions: Check this point with one of our partner accountants.

## Worked examples

### Example 1: Dutch webshop crosses the EUR 10,000 EU threshold in 2026

A bv established only in the Netherlands sells ordinary standard-rated clothes from its Dutch warehouse to consumers in Belgium, Germany and France. Assume no destination-taxation election and no applicable small-business exemption. Its EU distance sales in 2025 were EUR 7,400, so it started 2026 under the threshold and charged Dutch VAT at 21%. By 30 September 2026 those sales reach EUR 9,600. On 5 October 2026 it makes a sale of EUR 800, taking the year to EUR 10,400. That sale is the first one taxed in the customer's state. Further EU consumer sales in the rest of Q4 2026 are EUR 4,200.

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

Counted 2025 turnover: 15,800 + 1,500 = EUR 17,300. The van is a depreciated business asset and the Belgian services are taxed abroad, so neither counts. Counted 2026 turnover: 17,900 + 800 = EUR 18,700. These figures do **not** establish eligibility for a January 2027 start: the relevant years are 2026 and 2027, not 2025 and 2026. Confirm final 2026 turnover and expected 2027 counted turnover. To start on 1 January 2027, the application must arrive by 3 December 2026.

For the original 2027 illustration only, assume counted turnover remains EUR 18,700, the law remains unchanged, the EUR 700 input VAT is fully deductible outside KOR, and there are no reverse-charged purchases, taxable acquisitions/imports or revision liabilities. Then: outside the KOR it would pay 17,900 x 21% - 700 = EUR 3,059 net VAT. Inside the KOR those eligible sales bear no output VAT and the EUR 700 is not deductible. Ask whether customers can actually deduct the VAT and compare prices and revision effects before recommending entry. On the current rule, a 2028 exit would bar re-entry until 1 January 2030; confirm the law then.

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

1. Where is the business established, and what human and technical resources support any claimed Dutch or other EU fixed establishment? A warehouse label or server alone does not decide this. This decides group A, B, C or D.
2. Who are the customers: Dutch businesses, Dutch consumers, or consumers in other EU states? Business-only sales by a foreign supplier are usually reverse-charged and need no Dutch registration.
3. Where are the goods when sold: Dutch stock, stock in another EU state, or shipped from outside the EU, and in consignments above or below EUR 150?
4. What were the EU distance sales and B2C digital services in 2025 and so far in 2026, all EU states together?
5. For the KOR: counted turnover in the intended start year and preceding year (for January 2027: 2026 and 2027), whether customers can deduct VAT, and whether any large investment goods were bought in the last years (revision risk).
6. Is the business already registered for Dutch VAT, for OSS in any state, or part of a VAT group?

## Sources

| Source and scope read | URL | Read on |
|---|---|---|
| Wet OB 1968: arts. 1a, 2a, 3c, 5, 5a, 6k, 7, 9, 12, 17a, 21(e), 25–25e, 28r–28tl, 33g; effective 2026 edition | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002629/2026-01-01_0/xml/BWBR0002629_2026-01-01_0.xml | 2026-11-27 |
| Uitvoeringsbesluit OB 1968: arts. 24c–24d, licence scope, liability and compulsory representation | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002633/2026-01-01_0/xml/BWBR0002633_2026-01-01_0.xml | 2026-11-27 |
| Uitvoeringsbeschikking OB 1968: art. 25; unchanged January/April 2026 registration amount | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002634/2026-04-01_0/xml/BWBR0002634_2026-04-01_0.xml | 2026-11-27 |
| EU Implementing Regulation 282/2011: arts. 57 quinquies, 58 bis–58 ter, 61–61 bis; browser read | https://eur-lex.europa.eu/legal-content/NL/TXT/?uri=CELEX:02011R0282-20250414 | 2026-11-27 |
| Belastingdienst: KVK route, numbers and processing time | https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/btw-identificatienummer-en-omzetbelastingnummer | 2026-11-27 |
| Belastingdienst: domestic registration outside Handelsregister | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/themaoverstijgend/programmas_en_formulieren/opgaaf-startende-onderneming-niet-ingeschreven-handelsregister/opgaaf-startende-onderneming-niet-ingeschreven-in-handelsregister | 2026-11-27 |
| Belastingdienst: foreign address/legal-form registration route | https://www.belastingdienst.nl/wps/wcm/connect/nl/ondernemers/content/zo-werkt-eherkenning | 2026-11-27 |
| Belastingdienst: foreign-business registration, exemptions and refund routing | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/internationaal/btw_voor_buitenlandse_ondernemers/belastingkantoor_en_registratie/ | 2026-11-27 |
| Belastingdienst: foreign registration form, completion and postal address | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/themaoverstijgend/programmas_en_formulieren/aanmelding-onderneming-buitenland | 2026-11-27 |
| Belastingdienst: foreign return periods and nil returns | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/internationaal/btw_voor_buitenlandse_ondernemers/btw_aangifte_doen_en_betalen/aangifte_doen/btw_aangifte_doen | 2026-11-27 |
| Belastingdienst: foreign payment deadlines and estimated assessments | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/internationaal/btw_voor_buitenlandse_ondernemers/btw_aangifte_doen_en_betalen/uiterste_ontvangstdatum_aangifte_en_betaling_btw_aangifte | 2026-11-27 |
| Belastingdienst: counted KOR turnover and subnumbers | https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/kor-voorwaarden | 2026-11-27 |
| Belastingdienst: joining KOR and published entry dates | https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/aanmelden-kor | 2026-11-27 |
| Belastingdienst: leaving KOR and confirmation time | https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/afmelden-kor | 2026-11-27 |
| Belastingdienst: OSS portal, VAT-group members, returns and IOSS Norway condition | https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/btw-melden-eenloketsysteem | 2026-11-27 |
| Belastingdienst: EU distance sales and warehouse distinction | https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/btw-goederen-eu-particulieren | 2026-11-27 |
| Belastingdienst: IOSS intermediary and registration | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/internationaal/btw_voor_buitenlandse_ondernemers/e_commerce_en_diensten/ik_lever_goederen_van_buiten_de_eu_-_de_invoerregeling/invoerregeling_registratie/ | 2026-11-27 |
| Belastingdienst: ordinary filing default | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/boetes/u_doet_geen_of_te_laat_aangifte | 2026-11-27 |
| Belastingdienst: ordinary payment default and concession | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/boetes/u_betaalt_niet_te_laat_of_te_weinig | 2026-11-27 |

Not yet confirmed: no unverified conclusion is usable. The express partner-accountant holds above preserve the special identification, import/stock-transfer, warehouse/commodity representation, refund-form and registration-offence/interest topics. The 2027 and 2028/2030 case illustrations are conditional applications of the rule read for 2026, not a statement that future law has been confirmed.
