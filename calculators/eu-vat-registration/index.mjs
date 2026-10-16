// EU VAT registration check: "I sell to customers in other EU countries. Do I have to
// register for VAT elsewhere, and whose VAT do I charge?"
//
// Pure function over rules.json. No network, no dates read from the clock: the caller
// decides which year's figures it holds. The same file is served on
// openaccountants.com/tools/eu-vat-registration and can be embedded anywhere
// (AGPL-3.0-or-later). Figures carry their official source; see rules.json.
//
// Rules in plain words (Council Directive 2006/112/EC as amended from 1 July 2021):
//  - Business customers (B2B): the customer accounts for the VAT (reverse charge for
//    services, Art. 196; intra-EU supplies of goods zero-rated to a VAT-registered
//    customer, Art. 138). No registration in the customer's country in the usual case.
//  - Stock held in another member state (e.g. a marketplace warehouse): local
//    registration there, OSS cannot report domestic sales from that stock.
//  - Non-EU seller: no threshold. Digital services to EU consumers: destination VAT
//    from the first sale, via non-Union OSS or local registrations. Goods shipped
//    from outside the EU: IOSS for consignments up to EUR 150 (or the marketplace
//    collects as deemed supplier); above EUR 150, import VAT at the border.
//  - EU seller, consumers in other member states, goods and digital services
//    together: EUR 10,000 across all other member states, current and previous
//    calendar year. At or under: home-country VAT (may opt for destination). Over:
//    destination VAT from the sale that crosses the line, reported through Union
//    OSS (one quarterly return) or local registrations.
//  - Other services to consumers: generally the seller's country (Art. 45), with
//    exceptions this check does not model.

import rules from "./rules.json" with { type: "json" };

/**
 * @typedef {Object} Input
 * @property {"eu"|"non_eu"} seller            Where the business is established.
 * @property {"goods"|"digital_services"|"other_services"} supply  What is sold.
 * @property {"consumers"|"businesses"|"both"} customers  Who buys.
 * @property {number} [b2cCrossBorderEurThisYear]  Cross-border B2C sales to OTHER EU countries, this calendar year, EUR.
 * @property {number} [b2cCrossBorderEurLastYear]  Same, previous calendar year, EUR.
 * @property {boolean} [stockInOtherEuCountry]      Goods held in a member state other than the seller's (warehouse, FBA).
 * @property {boolean} [goodsShippedFromOutsideEu]  Goods enter the EU from a third country when sold.
 * @property {boolean} [viaMarketplace]             Sales made through an online marketplace that collects payment.
 * @property {boolean} [registeredForOss]           Already registered for Union or non-Union OSS (or IOSS).
 */

/**
 * @typedef {Object} Result
 * @property {"home_vat"|"destination_vat"|"local_registration"|"customer_accounts"|"import_scheme"|"check_with_accountant"} verdict
 * @property {string} headline   One sentence, plain words.
 * @property {string[]} reasons  Why, each tied to a rule.
 * @property {string[]} actions  What to do next, in order.
 * @property {string[]} figures  Keys of rules.json figures used.
 * @property {string[]} sources  Official pages behind the answer.
 * @property {string} as_of
 * @property {string[]} limits
 * @property {"high"|"medium"|"low"} confidence
 */

const F = rules.figures;
const eur = (n) => `EUR ${Number(n).toLocaleString("en-GB")}`;

/** @param {Input} input @returns {Result} */
export function assessEuVatRegistration(input) {
  const i = normalise(input);
  const base = { figures: [], sources: new Set(), as_of: rules.as_of, limits: rules.limits, confidence: "high" };
  const cite = (key) => { base.figures.push(key); base.sources.add(F[key].source); };
  const done = (verdict, headline, reasons, actions, confidence = "high") => {
    // Every answer names at least the directive it rests on.
    const sources = base.sources.size ? [...base.sources] : [rules.sources[0]];
    return { verdict, headline, reasons, actions, figures: base.figures, sources, as_of: rules.as_of, limits: rules.limits, confidence };
  };

  // 1. Business customers only: the customer accounts for the VAT.
  if (i.customers === "businesses") {
    base.sources.add(F.eu_b2c_threshold_eur.source);
    return done(
      "customer_accounts",
      "You normally do not register in your customers' countries: a VAT-registered business customer accounts for the VAT itself.",
      [
        i.supply === "goods"
          ? "Intra-EU sales of goods to a VAT-registered business are zero-rated by you and taxed by the customer (Article 138); you report them on your EC Sales List and check the customer's VAT number in VIES."
          : "Services to a business in another member state are taxed where the customer is, by the customer, under the reverse charge (Articles 44 and 196). You invoice without VAT and state the reverse charge.",
        "Registration abroad becomes necessary only when you hold stock there, sell to consumers, or make supplies outside the general rule (land, events, transport).",
      ],
      [
        "Validate every business customer's VAT number in VIES before you invoice without VAT.",
        "Keep the EC Sales List (recapitulative statement) up to date in your home country.",
        i.stockInOtherEuCountry ? "You said you hold stock in another member state: that needs a local registration there regardless." : "Re-run this check if you start selling to consumers abroad.",
      ],
      i.stockInOtherEuCountry ? "medium" : "high",
    );
  }

  // 2. Stock in another member state overrides everything else for goods.
  if (i.supply === "goods" && i.stockInOtherEuCountry) {
    cite("eu_b2c_threshold_eur");
    cite("oss_return_deadline");
    return done(
      "local_registration",
      "Register for VAT in every member state where you hold stock. OSS does not cover sales made from stock inside the customer's own country.",
      [
        "Moving your own goods into another member state is a deemed intra-EU supply and acquisition there; domestic sales from that stock are local supplies taxed under that country's VAT.",
        "Cross-border consumer sales shipped FROM that stock to OTHER member states can still go through Union OSS once you are over the EUR 10,000 threshold or have opted in.",
        i.viaMarketplace ? "Marketplace warehouses (fulfilment programmes) count as your stock in that country." : "",
      ].filter(Boolean),
      [
        "Register in each country where goods are stored, before the first local sale.",
        "Report cross-border consumer sales to the remaining member states through Union OSS (quarterly, " + F.oss_return_deadline.value + ").",
        "Speak to an accountant about which registrations are already overdue.",
      ],
      "high",
    );
  }

  // 3. Non-EU seller: no threshold.
  if (i.seller === "non_eu") {
    if (i.supply === "digital_services") {
      cite("eu_b2c_threshold_eur");
      cite("oss_return_deadline");
      return done(
        "destination_vat",
        "Charge the VAT of each customer's country from the first sale. A non-EU seller has no EUR 10,000 threshold; the non-Union OSS lets you report it all in one quarterly return.",
        [
          "Digital (electronically supplied) services to EU consumers are taxed where the consumer lives (Article 58).",
          "The EUR 10,000 threshold applies only to sellers established in one member state (Article 59c); a seller established outside the EU charges destination VAT on every sale.",
          i.viaMarketplace ? "If an EU marketplace or app store takes the payment, check whether it is the deemed supplier for VAT; then it, not you, charges and reports the VAT." : "",
        ].filter(Boolean),
        [
          i.registeredForOss ? "You said you are already in OSS: keep filing quarterly, " + F.oss_return_deadline.value + "." : "Register for the non-Union OSS in one member state of your choice, or register locally in every country where you have consumers.",
          "Collect and keep two pieces of evidence of each customer's location (billing address, bank country, IP address).",
          "Apply each country's standard or reduced rate for the service; the rates differ.",
        ],
        "high",
      );
    }
    if (i.supply === "goods") {
      cite("ioss_consignment_limit_eur");
      cite("oss_return_deadline");
      const shipped = i.goodsShippedFromOutsideEu !== false; // default: a non-EU seller ships from outside
      return done(
        shipped ? "import_scheme" : "destination_vat",
        shipped
          ? `Goods shipped from outside the EU to EU consumers: use the Import One Stop Shop for consignments up to ${eur(F.ioss_consignment_limit_eur.value)} so VAT is charged at checkout; above that, import VAT is due at the border.`
          : "Goods already inside the EU sold to consumers in other member states: charge the customer's country's VAT from the first sale and report through Union OSS, or register locally.",
        [
          shipped
            ? `IOSS (Articles 369l to 369x) covers consignments with an intrinsic value up to ${eur(F.ioss_consignment_limit_eur.value)}; the import is then VAT-exempt and you charge the destination rate to the customer.`
            : "Without an EU establishment there is no EUR 10,000 threshold; every intra-EU distance sale to a consumer is taxed in the customer's country.",
          i.viaMarketplace ? "When an online marketplace facilitates the sale, it is usually the deemed supplier and charges the VAT; confirm with the marketplace what it reports for you." : "",
          shipped ? `Consignments above ${eur(F.ioss_consignment_limit_eur.value)} fall outside IOSS: import VAT and customs duty are collected on import, by you or the customer depending on the delivery terms.` : "",
        ].filter(Boolean),
        [
          shipped ? "Register for IOSS through an EU intermediary (required for most non-EU sellers), or let the marketplace handle it." : "Register for Union OSS through a member state (you need an EU VAT identification) or register in each country of your consumers.",
          "File the quarterly OSS or monthly IOSS return on time; " + F.oss_return_deadline.value + " for OSS.",
          "Have an accountant confirm the customs and delivery-terms side (DDP vs DAP).",
        ],
        "medium",
      );
    }
    return done(
      "check_with_accountant",
      "Services other than digital ones follow place-of-supply rules that depend on the kind of service. This check does not decide them.",
      ["Consumer services are generally taxed where the supplier is established (Article 45), but land, events, transport, hiring of goods and several others follow their own rules (Articles 46 to 59)."],
      ["Name the service to an accountant in the customer's country; the answer differs by service type."],
      "low",
    );
  }

  // 4. EU seller, consumers (or both), goods or digital services: the EUR 10,000 test.
  if (i.supply === "goods" || i.supply === "digital_services") {
    cite("eu_b2c_threshold_eur");
    cite("oss_return_deadline");
    const limit = F.eu_b2c_threshold_eur.value;
    const thisYear = i.b2cCrossBorderEurThisYear;
    const lastYear = i.b2cCrossBorderEurLastYear;
    const known = thisYear !== null || lastYear !== null;
    const over = (thisYear ?? 0) > limit || (lastYear ?? 0) > limit;
    if (!known) {
      return done(
        "check_with_accountant",
        `Whose VAT you charge depends on one number: your total cross-border consumer sales to other EU countries, this year and last. Enter it to get an answer; the line is ${eur(limit)}.`,
        ["Article 59c sets a single EU-wide threshold of EUR 10,000 for goods and digital services together, tested for the current and the previous calendar year."],
        ["Add up all B2C sales shipped or supplied to consumers in other member states for this year and last year, then run the check again."],
        "low",
      );
    }
    if (!over) {
      return done(
        "home_vat",
        `You are at or under ${eur(limit)} of cross-border consumer sales in both years, so you charge your own country's VAT on those sales. No registration elsewhere is required.`,
        [
          `Article 59c: when total cross-border B2C sales of goods and digital services to other member states did not exceed ${eur(limit)} in the previous year and do not exceed it in the current year, the place of supply stays the seller's member state.`,
          "You may opt to tax at destination anyway (binding for two calendar years), which only makes sense if the customer's rates are lower or you expect to cross the line soon.",
          i.viaMarketplace && i.supply === "goods" ? "Selling through a marketplace does not change this while you ship from your own country and stay under the threshold." : "",
        ].filter(Boolean),
        [
          `Track the running total; the sale that takes you over ${eur(limit)} is taxed in the customer's country, and every sale after it.`,
          `Consider registering for Union OSS before you cross, so the switch is one quarterly return (${F.oss_return_deadline.value}) instead of several local registrations.`,
          i.customers === "both" ? "Business customers are unaffected: they account for the VAT themselves (reverse charge or intra-EU acquisition)." : "",
        ].filter(Boolean),
        "high",
      );
    }
    return done(
      "destination_vat",
      `You are over ${eur(limit)}, so you charge the VAT of each customer's country on cross-border consumer sales. Report it through Union OSS in one quarterly return, or register in each country.`,
      [
        `Article 59c: once cross-border B2C sales of goods and digital services to other member states exceed ${eur(limit)} in the current or the previous calendar year, each sale is taxed where the customer is.`,
        "The threshold is EU-wide and counts goods and digital services together; it is not EUR 10,000 per country.",
        i.viaMarketplace ? "If a marketplace facilitates the sale, check whether it is the deemed supplier for VAT on those sales; it is for goods shipped from outside the EU and for non-EU sellers, usually not for an EU seller shipping from the EU." : "",
      ].filter(Boolean),
      [
        i.registeredForOss ? "You are in OSS: report every cross-border consumer sale at the customer's country rate, " + F.oss_return_deadline.value + "." : "Register for Union OSS in your own member state (one return, one payment, all countries), or register separately in each country where you have consumers.",
        "Apply each country's correct rate (standard or reduced) to each sale; keep two pieces of evidence of the customer's location for digital services.",
        "If you crossed the line in a past period without charging destination VAT, have an accountant quantify the catch-up before the next return.",
      ],
      "high",
    );
  }

  // 5. EU seller, other services to consumers.
  return done(
    "home_vat",
    "Services other than digital ones sold to consumers are generally taxed in your own country, so you charge your home VAT. Some service types follow their own rules.",
    ["Article 45: B2C services are taxed where the supplier is established, unless a special rule applies (services connected to land, admission to events, passenger transport, hiring of means of transport, restaurant and catering, and a few more)."],
    ["If your service touches land, events or transport in another country, check that country's rule with an accountant before invoicing.", "Keep the EUR 10,000 test in mind if you also sell goods or digital services to consumers abroad."],
    "medium",
  );
}

function normalise(input) {
  const num = (v) => (v === undefined || v === null || v === "" || Number.isNaN(Number(v)) ? null : Math.max(0, Number(v)));
  const bool = (v) => v === true || v === "true" || v === "1" || v === "on" || v === "yes";
  return {
    seller: input?.seller === "non_eu" ? "non_eu" : "eu",
    supply: ["goods", "digital_services", "other_services"].includes(input?.supply) ? input.supply : "goods",
    customers: ["consumers", "businesses", "both"].includes(input?.customers) ? input.customers : "consumers",
    b2cCrossBorderEurThisYear: num(input?.b2cCrossBorderEurThisYear),
    b2cCrossBorderEurLastYear: num(input?.b2cCrossBorderEurLastYear),
    stockInOtherEuCountry: bool(input?.stockInOtherEuCountry),
    goodsShippedFromOutsideEu: input?.goodsShippedFromOutsideEu === undefined ? undefined : bool(input.goodsShippedFromOutsideEu),
    viaMarketplace: bool(input?.viaMarketplace),
    registeredForOss: bool(input?.registeredForOss),
  };
}

export { rules };
