---
name: poland-einvoice
description: "Polish KSeF e-invoicing (Krajowy System e-Faktur) for tax year 2026: who must issue structured FA(3) invoices and from when (1 February 2026 for businesses with 2024 sales over PLN 200 million including VAT, 1 April 2026 for the rest), who is outside KSeF (businesses with no seat or fixed establishment in Poland, consumer invoices, OSS, IOSS and EU SME scheme invoices, tolls and single tickets), the 2026 carve-outs for PLN 10,000 a month and for cash-register invoices, receiving invoices, the offline24, unavailability and failure modes with their deadlines, QR codes, storage for 10 years, what KSeF means for input VAT, and the fines from 1 January 2027. Trigger on: KSeF, e-faktura, faktura ustrukturyzowana, FA(3), offline24, tryb awaryjny, numer KSeF, kod QR, art. 106ga, art. 145m. Out of scope: VAT rates, JPK_V7 and the VAT return (poland-vat-return), income tax (pl-income-tax, pl-cit-corporate-tax)."
version: 1.2
jurisdiction: PL
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Poland KSeF e-invoicing (2026)

Source-cited draft: not reviewed by an accountant. Built by Michael Cutajar and the OpenAccountants team.

This skill covers the duty to issue and receive invoices through KSeF, Poland's national e-invoicing system, under the VAT Act (ustawa o podatku od towarów i usług, consolidated text Dz.U. 2026 poz. 1263). Article numbers below are to that act unless another act is named. It links to the other Poland skills and does not repeat them:

- [poland-vat-return](poland-vat-return.md): VAT registration, rates, the JPK_V7 file, split payment and the white list.
- [pl-cit-corporate-tax](pl-cit-corporate-tax.md) and [pl-income-tax](pl-income-tax.md): income tax.

## Who this applies to

**Issuing.** Every VAT taxpayer must issue structured invoices (faktury ustrukturyzowane) through KSeF (art. 106ga ust. 1). A structured invoice is an invoice issued through KSeF together with the KSeF number the system gives it (art. 2 pkt 32a). The duty does not cover invoices (art. 106ga ust. 2):

1. issued by a business with no seat and no fixed establishment in Poland, even if it is registered for Polish VAT;
2. issued by a business with no seat in Poland whose Polish fixed establishment takes no part in the supply invoiced;
3. issued under the non-EU OSS, the scheme for international occasional road passenger transport, or IOSS (Division XII chapters 7, 7a and 9), for supplies under those schemes;
4. issued to a private individual not in business;
5. covered by the Minister's regulation under art. 106s (Dz.U. 2025 poz. 1740): paid motorway tolls and single passenger tickets on simplified invoices, air navigation route charges invoiced by EUROCONTROL, insurance and financial services exempt under art. 43 ust. 1 pkt 7 and 37-41 on simplified invoices, and self-billed invoices where the buyer or the seller has no Polish NIP for that supply;
6. issued by a business using the EU SME exemption (art. 113a ust. 1).

Those invoices are issued on paper or as ordinary electronic invoices (art. 106ga ust. 3). Groups 1, 2 and 4 may choose to use KSeF (art. 106ga ust. 4). EU buyers who self-bill an intra-EU supply under an EU VAT number may also choose KSeF (regulation 1740, § 3).

**Start dates.** The duty began on 1 February 2026. Until 31 March 2026, a business whose 2024 sales including VAT were PLN 200,000,000 or less could still issue paper or ordinary electronic invoices (art. 145l). From 1 April 2026 it applies to everyone in scope.

**2026 carve-outs.** A business in scope may still issue paper or ordinary electronic invoices:

- from 1 April to 31 December 2026, if the invoices it issues outside KSeF in a month total PLN 10,000 or less including VAT. It loses the right from the invoice that takes the month over PLN 10,000 (art. 145m). The Ministry of Finance counts only invoices that would otherwise have to go through KSeF, counts each invoice in the month of its issue date, and says that once the limit is crossed the business uses KSeF for that invoice and every later one (KSeF FAQ, rules section, questions 16, 17 and 22);
- from 1 February to 31 December 2026, for invoices issued from a cash register, and for fiscal receipts showing the buyer's NIP that count as simplified invoices (up to PLN 450 or EUR 100, art. 106e ust. 5 pkt 3) (art. 145n).

**Receiving.** A structured invoice is issued and received through KSeF (art. 106gb ust. 1), so from 1 February 2026 every Polish VAT business receives its structured purchase invoices there. The seller passes the invoice on in a way agreed with the buyer instead when the buyer has no seat or fixed establishment in Poland (or its Polish establishment is not involved), is an EU SME scheme user, has no Polish tax number, is a private individual, or when the place of supply is outside Poland (art. 106gb ust. 4). KSeF is not used to report purchases from foreign suppliers (KSeF FAQ, rules section, question 11).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| 2024 sales including VAT above which KSeF applied from 1 February 2026 | PLN 200,000,000 | 2026 | https://api.sejm.gov.pl/eli/acts/DU/2026/1263/text.pdf (art. 145l) |
| Invoices outside KSeF allowed if the month's total, including VAT, is at or below | PLN 10,000 a month, 1 April to 31 December 2026 | 2026 | https://api.sejm.gov.pl/eli/acts/DU/2026/1263/text.pdf (art. 145m) |
| Fiscal receipt with buyer's NIP that counts as a simplified invoice, outside KSeF to 31 December 2026 | up to PLN 450 or EUR 100 | 2026 | https://api.sejm.gov.pl/eli/acts/DU/2026/1263/text.pdf (art. 106e ust. 5 pkt 3, art. 145n) |
| Fine for an invoice that should have gone through KSeF, from 1 January 2027 | up to 100% of the VAT shown | 2027 | https://api.sejm.gov.pl/eli/acts/DU/2026/1263/text.pdf (art. 106ni ust. 1) |
| Same fine where the invoice shows no VAT | up to 18.7% of the invoice total | 2027 | https://api.sejm.gov.pl/eli/acts/DU/2026/1263/text.pdf (art. 106ni ust. 1) |
| Time to pay a fine | 14 days from delivery of the decision | 2027 | https://api.sejm.gov.pl/eli/acts/DU/2026/1263/text.pdf (art. 106ni ust. 3) |
| Storage of invoices in KSeF | 10 years from the end of the year of issue | 2026 | https://api.sejm.gov.pl/eli/acts/DU/2026/1263/text.pdf (art. 112aa) |

## The taxable base

KSeF changes how an invoice is issued and received. It does not change what is taxed, the rates or the tax point; those are in [poland-vat-return](poland-vat-return.md). What it changes:

- **Issue date.** A structured invoice is issued on the day it is sent to KSeF (art. 106na ust. 1). An invoice issued in an offline mode is issued on the date the seller puts on it, field P_1 (art. 106nda ust. 10, art. 106nf ust. 9).
- **Receipt date.** A structured invoice is received on the day KSeF assigns its number (art. 106na ust. 3). If it is passed to a buyer listed in art. 106gb ust. 4 outside KSeF, it is received when the buyer actually gets it (art. 106na ust. 4).
- **Input VAT.** The right to deduct arises in the period the tax point arose, but not before the period in which the buyer received the invoice (art. 86 ust. 10 and 10b pkt 1). For a structured invoice that is the period in which KSeF assigned the number. The Ministry gives the same answer (KSeF FAQ, local government section, question 26).
- **Invoices that should have gone through KSeF but did not.** The Ministry of Finance says a buyer does not have to check whether an invoice should have been issued in KSeF or in another form, and that this is not a condition for the right to deduct (KSeF FAQ, local government section, question 47). The act says the same by omission: art. 86 does not make deduction depend on KSeF, and the list in art. 88 ust. 3a of invoices that cannot support deduction (non-existent issuer, non-taxable or exempt transaction, transactions that did not happen, untrue amounts, sham transactions, self-billed invoices the seller did not accept, VAT shown where none should be) does not include an invoice issued outside KSeF. From 1 January 2027 the sham-transaction item becomes transactions made in abuse of law under art. 5 ust. 5 (Dz.U. 2026 poz. 1270, art. 1 pkt 16). The consequence of skipping KSeF falls on the seller: the art. 106ni fine from 1 January 2027. Art. 106na does not set a receipt date for such an invoice, because it is not a structured invoice.
- **Corrections.** A seller reduces its taxable base in the period in which it issues a corrective structured invoice (art. 29a ust. 13). A corrective invoice outside KSeF still needs proof that the buyer received it (art. 29a ust. 13a).
- **Attachments.** Invoices with complex unit, quantity or price data (utilities, telecoms, fuel) may carry a KSeF attachment after the business notifies the Head of the National Revenue Administration (Szef KAS), which is done through e-Urząd Skarbowy (art. 106gba ust. 2; Ministry of Finance, scope page).
- **QR codes.** A structured invoice handed to a buyer outside KSeF, or used outside KSeF, carries a QR code that links to it in KSeF (art. 106gb ust. 5). An offline invoice handed over before it is in KSeF carries a second code that proves who issued it, made with a KSeF certificate (art. 106nda ust. 6 and 7).
- **Format.** The structured invoice follows the FA(3) schema, which replaced FA(2) on 1 February 2026 (Ministry of Finance, FA(3) page). B2G invoices sent through the public procurement platform (PEF) or Peppol become structured invoices once they are in KSeF with a number (art. 106gb ust. 7).

## Deadlines and filing

| What | When | Source |
|---|---|---|
| KSeF for businesses with 2024 sales over PLN 200,000,000 | from 1 February 2026 | art. 106ga, art. 145l |
| KSeF for all other businesses in scope | from 1 April 2026 | art. 145l |
| Receiving structured invoices through KSeF | from 1 February 2026 | art. 106gb; Ministry of Finance, scope page |
| Paper or ordinary e-invoices at PLN 10,000 a month or less | 1 April to 31 December 2026 | art. 145m |
| Cash-register invoices and fiscal receipts with the buyer's NIP outside KSeF | 1 February to 31 December 2026 | art. 145n |
| Issue an invoice | by the 15th of the month after the supply | art. 106i ust. 1 |
| Offline24 (the seller's own choice, for example no internet): send to KSeF | no later than the next working day after issue | art. 106nda ust. 2 |
| KSeF unavailable (announced maintenance): send to KSeF | no later than the next working day after the unavailability ends | art. 106nh ust. 2 |
| KSeF failure announced on the Ministry's BIP page: send to KSeF | within 7 working days after the announced end of the failure; the period restarts if a new failure is announced | art. 106nf ust. 4 and 5 |
| Total failure announced in the media | issue paper or ordinary e-invoices without QR codes; they are not sent to KSeF afterwards | art. 106ne ust. 3, art. 106ng, art. 106nf ust. 7, art. 106nha pkt 2; Ministry of Finance, total failure page |
| KSeF number in bank transfers and split payments between active VAT payers | payments from 1 January 2027 | art. 108g; art. 17 of the act of 16 June 2023 (Dz.U. 2023 poz. 1598), quoted in the notice to Dz.U. 2026 poz. 1263 |
| Fines for breaches of the KSeF duty | from 1 January 2027 | art. 106ni, footnote 23 |

Access is through the Ministry's KSeF interface software and free apps (art. 106gb ust. 2, art. 106nb). Under the regulation on using KSeF (Dz.U. 2025 poz. 1815, amended by Dz.U. 2026 poz. 169), a user authenticates with an electronic identification means connected to the national node (from 14 February 2026), a qualified electronic signature, a qualified electronic seal, or a KSeF certificate generated after one of those, valid for up to 2 years (§ 6 ust. 1 and 2, § 15 pkt 2). Old KSeF tokens still work until 31 December 2026 (§ 13 ust. 1 pkt 1). A taxpayer that is not a natural person and cannot authenticate with a qualified electronic seal names its first KSeF user on form ZAW-FA filed with its tax office (§ 5 ust. 1; KSeF FAQ, permissions section, question 5). Invoices issued in KSeF do not go into a JPK_FA file; invoices issued outside KSeF can still be requested in one (KSeF FAQ, rules section, question 15).

## Penalties and interest

- **Fine from 1 January 2027.** The head of the tax office may fine a taxpayer who, against the duty, did not issue a structured invoice in KSeF, issued an offline-mode invoice that does not follow the FA(3) template, or did not send an offline-mode invoice to KSeF in time. The fine is up to 100% of the VAT shown on that invoice or, if it shows no VAT, up to 18.7% of the invoice total (art. 106ni ust. 1). It is paid within 14 days of delivery of the decision, without a demand (art. 106ni ust. 3). The act sets a ceiling only; it does not fix the amount below it.
- **No criminal case.** Failing the KSeF duty or the offline send deadlines does not start fiscal penal proceedings (art. 106ni ust. 4). This rule has no 2027 start date and applies now.
- **During 2026.** There is no money fine for KSeF breaches before 1 January 2027 (art. 106ni, footnote 23). The VAT return penalties, interest and the 30% additional liability still apply to wrong VAT figures; see [poland-vat-return](poland-vat-return.md).
- **JPK_VAT errors linked to KSeF.** The Ministry says penalties for wrong JPK_VAT files are not automatic and follow only if the taxpayer does not correct the file after a call to do so (KSeF FAQ, rules section, question 23; art. 109 ust. 3e-3g).

## Cross-border points

- **Foreign businesses registered for Polish VAT.** A business with no seat and no fixed establishment in Poland does not have to issue invoices in KSeF (art. 106ga ust. 2 pkt 1). Nor does one with no Polish seat whose Polish fixed establishment is not involved in the supply (pkt 2). Either may use KSeF voluntarily (ust. 4). It may decide invoice by invoice. If it uses KSeF, it can act through a proxy named on ZAW-FA (KSeF FAQ, permissions section, question 18). The Ministry's tax explanations of 28 January 2026 say: the fixed establishment is the one in art. 11 ust. 2 of Regulation 282/2011, not the income-tax permanent establishment; it takes part in a supply only if it takes part actively, with enough permanence and staff and technical resources to make that supply; and Polish buyers do not have to check whether a foreign supplier has a Polish fixed establishment. A taxpayer that follows the explanations is protected under art. 14k-14m of the Tax Ordinance.
- **Polish seller, foreign buyer.** A Polish business invoicing a foreign customer still issues the invoice in KSeF. It then gives the buyer the invoice in an agreed way, for example as a PDF, with the QR code (art. 106gb ust. 4 and 5; KSeF FAQ, issuing section, question 36). To decide whether a foreign buyer has a Polish fixed establishment, the 28 January 2026 explanations let the seller assume none if it has no information; follow the buyer's own statement if it gives one; and assume one that takes part in the purchase if the buyer gives its Polish NIP and makes no statement to the contrary. Intra-EU supplies and exports are not excluded.
- **Foreign supplier, Polish buyer.** Invoices from foreign suppliers are not reported to KSeF (KSeF FAQ, rules section, question 11). The Polish buyer accounts for reverse charge in its JPK_V7 as before.
- **Self-billing.** A self-billed invoice is outside KSeF when the buyer or the seller has no Polish NIP for that supply (regulation 1740, § 2 pkt 5 and 6). An EU buyer self-billing an intra-EU supply under its EU VAT number may still choose KSeF (§ 3).
- **Special schemes.** Non-EU OSS, IOSS and international occasional road passenger transport invoices stay outside KSeF (art. 106ga ust. 2 pkt 3). The Ministry says they cannot be issued in KSeF voluntarily (scope page).

## Worked examples

### Example 1: a sole trader near the PLN 10,000 monthly limit in 2026

Marta runs a small translation business in Poland and is an active VAT payer. In June 2026 she issues paper invoices to business clients: PLN 2,000, PLN 3,000 and PLN 2,500 net, each with 23% VAT. She also invoices a private individual PLN 1,000 net. The consumer invoice is outside KSeF anyway (art. 106ga ust. 2 pkt 4), so it does not count towards the limit (KSeF FAQ, rules section, question 22). Her three business invoices total PLN 9,225 with VAT, so she is within PLN 10,000. On 28 June she invoices another business client PLN 1,000 net (PLN 1,230 with VAT). That takes the month to PLN 10,455. Under art. 145m ust. 2 that invoice, and every later one, must go through KSeF. The headroom before it was PLN 775.

```oa-check
name: Marta, June 2026, PLN 10,000 monthly limit under art. 145m
inputs:
  inv_1: 2000
  inv_2: 3000
  inv_3: 2500
  inv_4: 1000
  vat_rate: 23
  limit: 10000
steps:
  - gross_before: (inv_1 + inv_2 + inv_3) * (1 + vat_rate / 100)
  - headroom: limit - gross_before
  - gross_4: inv_4 * (1 + vat_rate / 100)
  - gross_after: gross_before + gross_4
  - excess: gross_after - limit
expected:
  gross_before: 9225
  headroom: 775
  gross_4: 1230
  gross_after: 10455
  excess: 455
```

### Example 2: the 2027 fine ceiling on two invoices issued outside KSeF

In February 2027 a Polish company issues two PDF invoices by email instead of through KSeF, with no offline mode applying. Invoice A is for consulting, PLN 20,000 net plus 23% VAT. Invoice B is for VAT-exempt training, PLN 15,000 with no VAT shown. Under art. 106ni ust. 1, the ceiling for A is 100% of the VAT shown, PLN 4,600. For B it is 18.7% of the total, PLN 2,805. The combined ceiling is PLN 7,405. The tax office may set a lower amount; the act fixes only the maximum. The buyer's right to deduct the VAT on invoice A does not depend on the invoice having gone through KSeF (KSeF FAQ, local government section, question 47).

```oa-check
name: Fine ceiling, two invoices outside KSeF, February 2027
inputs:
  net_a: 20000
  vat_rate: 23
  total_b: 15000
  cap_vat_pct: 100
  cap_total_pct: 18.7
steps:
  - vat_a: net_a * vat_rate / 100
  - cap_a: vat_a * cap_vat_pct / 100
  - cap_b: total_b * cap_total_pct / 100
  - cap_total: cap_a + cap_b
expected:
  vat_a: 4600
  cap_a: 4600
  cap_b: 2805
  cap_total: 7405
```

## Ask the client first

1. Where is the business's seat, and does it have a fixed establishment in Poland that takes part in the supplies? (Decides whether KSeF applies at all.)
2. What were 2024 sales including VAT, and how much is invoiced each month to business clients outside KSeF? (Start date and the PLN 10,000 carve-out.)
3. Who are the customers: Polish businesses, private individuals, foreign businesses, public bodies? (KSeF, agreed delivery with a QR code, or PEF.)
4. Are invoices issued from a cash register, by self-billing, or under OSS, IOSS or the EU SME scheme? (Exclusions in art. 106ga ust. 2, 145n and regulation 1740.)
5. Which software sends invoices to KSeF, who holds KSeF permissions, and is a KSeF certificate in place for offline invoices?

## Sources

| Source | URL | Read on |
|---|---|---|
| VAT Act, consolidated text Dz.U. 2026 poz. 1263, with art. 17 of the act of 16 June 2023 quoted in the notice (art. 2 pkt 32a, 29a, 86, 88, 106e, 106ga, 106gb, 106gba, 106i, 106na-106ni, 108g, 112aa, 145l-145n) | https://api.sejm.gov.pl/eli/acts/DU/2026/1263/text.pdf | 2026-10-23 |
| Regulation of 7 December 2025 on cases with no duty to issue structured invoices, Dz.U. 2025 poz. 1740 | https://api.sejm.gov.pl/eli/acts/DU/2025/1740/text.pdf | 2026-10-23 |
| Regulation of 12 December 2025 on using KSeF, Dz.U. 2025 poz. 1815 (§ 5, 6, 13 and 15) | https://api.sejm.gov.pl/eli/acts/DU/2025/1815/text.pdf | 2026-10-23 |
| Regulation of 13 February 2026 amending it, Dz.U. 2026 poz. 169 | https://api.sejm.gov.pl/eli/acts/DU/2026/169/text.pdf | 2026-10-23 |
| Amending act Dz.U. 2026 poz. 1270, mainly in force 1 January 2027 (checked: no KSeF changes; art. 1 pkt 16 amends art. 88 ust. 3a pkt 4 lit. c) | https://api.sejm.gov.pl/eli/acts/DU/2026/1270/text.pdf | 2026-10-23 |
| Ministry of Finance, KSeF scope (who is in and out, receiving from 1 February 2026) | https://ksef.podatki.gov.pl/informacje-ogolne-ksef-20/zakres-obowiazkowego-ksef | 2026-10-23 |
| Ministry of Finance, KSeF legal basis and key dates | https://ksef.podatki.gov.pl/informacje-ogolne-ksef-20/podstawy-prawne-oraz-kluczowe-terminy | 2026-10-23 |
| Ministry of Finance, KSeF questions and answers (page modified 8 October 2026). Question numbers restart in each section: rules section = "Zasady obowiązywania KSeF i przepisy prawne"; issuing section = "Wystawianie i otrzymywanie faktur"; permissions section = "Uprawnienia i autoryzacja"; local government section = "KSeF w Jednostkach Samorządu Terytorialnego" | https://ksef.podatki.gov.pl/pytania-i-odpowiedzi-ksef-20/ | 2026-10-23 |
| Ministry of Finance, special invoicing modes | https://ksef.podatki.gov.pl/informacje-ogolne-ksef-20/tryby-szczegolne-wystawiania-faktur | 2026-10-23 |
| Ministry of Finance, total failure (awaria całkowita) | https://ksef.podatki.gov.pl/informacje-ogolne-ksef-20/awaria-calkowita | 2026-10-23 |
| Ministry of Finance, tax explanations of 28 January 2026 on fixed establishment for KSeF (PT6.8101.4.2025) | https://www.gov.pl/web/finanse/objasnienia-podatkowe-z-28-stycznia-2026-r-dotyczace-zasad-ustalania-stalego-miejsca-prowadzenia-dzialalnosci-gospodarczej-na-terytorium-kraju-dla-potrzeb-wystawiania-faktur-przy-uzyciu-krajowego-systemu-e-faktur | 2026-10-23 |
| Ministry of Finance, FA(3) structure | https://ksef.podatki.gov.pl/informacje-ogolne-ksef-20/struktura-logiczna-fa-3 | 2026-10-23 |

Not yet confirmed: the Ministry's statement on deduction (question 47) is in the local government section of the FAQ and is not a tax explanation or interpretation, so it gives no protection under art. 14k-14m of the Tax Ordinance; no court ruling on the point was found. The Ministry's key-dates page swaps the numbers of Dz.U. 2025 poz. 1740 and 1742; the Sejm register confirms poz. 1740 is the exclusions regulation and poz. 1742 amends the invoicing regulation. KSeF permission types (§ 3 of regulation 1815), the FA(3) field list, GTU codes and the KSeF number format were not re-checked and are left out.

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
