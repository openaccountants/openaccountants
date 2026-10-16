# EU VAT registration check

**Question:** I sell to customers in other EU countries. Do I have to register for VAT elsewhere, and whose VAT do I charge?

Hosted: https://www.openaccountants.com/tools/eu-vat-registration

## Use it

```js
import { assessEuVatRegistration } from "./index.mjs";

const result = assessEuVatRegistration({
  seller: "eu",                       // "eu" | "non_eu"
  supply: "goods",                    // "goods" | "digital_services" | "other_services"
  customers: "consumers",             // "consumers" | "businesses" | "both"
  b2cCrossBorderEurThisYear: 12000,   // sales to consumers in OTHER EU countries, this calendar year
  b2cCrossBorderEurLastYear: 6000,    // same, last calendar year
  stockInOtherEuCountry: false,       // goods held in another member state (warehouse, FBA)
  goodsShippedFromOutsideEu: false,   // goods enter the EU when sold (non-EU sellers)
  viaMarketplace: false,              // an online marketplace takes the payment
  registeredForOss: false,            // already in Union / non-Union OSS or IOSS
});

result.verdict;   // "destination_vat"
result.headline;  // "You are over EUR 10,000, so you charge the VAT of each customer's country ..."
result.reasons;   // the rules, with articles
result.actions;   // what to do, in order
result.sources;   // official pages
result.as_of;     // date the figures were checked
```

Verdicts: `home_vat`, `destination_vat`, `local_registration`, `customer_accounts`, `import_scheme`, `check_with_accountant`.

## What it decides

- Business customers: the customer accounts for the VAT (reverse charge; intra-EU zero-rating). No registration abroad in the usual case.
- Stock in another member state: local registration there; OSS does not cover domestic sales from that stock.
- Non-EU seller: no threshold. Digital services: destination VAT from the first sale (non-Union OSS). Goods from outside the EU: IOSS up to EUR 150 per consignment, import VAT above.
- EU seller selling goods or digital services to consumers: the EUR 10,000 EU-wide test over this year and last. Under: home VAT. Over: destination VAT, via Union OSS or local registrations.
- Other services to consumers: usually home VAT; special rules flagged, not decided.

## What it does not cover

Excise goods, new means of transport, margin-scheme goods, services connected to land, admission to events, passenger transport, restaurant and catering, sellers established in more than one member state, and each country's own rates. An estimate from the rules, not advice on your situation.

## Figures

See `rules.json`: EUR 10,000 (Article 59c), EUR 150 IOSS limit, OSS deadline (end of the month after each quarter), UK GBP 90,000. Each carries its legal basis and official source; `as_of` is the date they were checked.
