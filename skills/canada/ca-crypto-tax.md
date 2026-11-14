---
name: ca-crypto-tax
description: Prepare Canadian crypto tax workings from reconciled exchange and wallet records. Determine capital versus business character, Canadian-dollar values, identical-property ACB, income receipts and later disposals, superficial losses and GST/HST. Covers 2026 with a separately dated 2025 filing bridge; unresolved ownership, cost or legal character remains unresolved.
version: "1.1"
jurisdiction: CA
tax_year: 2026
last_updated: 2026-11-14
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: crypto
type: computation
---

# Canadian crypto tax: records, income, gains and GST/HST

## Scope

Prepare a Canadian resident individual's crypto transaction working, including a sole proprietor's activity. Start with beneficial ownership and capital versus business character, then reconcile quantities and CAD values before computing. Crypto assets include payment, utility and security tokens, NFTs and stablecoins; their names do not decide income tax or GST/HST treatment. [K01](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-transactions.html)[K08](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/crypto-assets-tax-obligations.html)[K09](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-3.html)[K10](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-9.html)[K15](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-39.html)

This method supplies the crypto component of a return, not the person's complete income tax bill. Corporations, trusts, partnerships, registered plans, immigration, emigration and estates need the applicable entity or event rules. Keep their crypto records and the explicit boundaries below. Province and residence remain required for the complete return; a federal Canadian method does not make an Ontario client a Quebec filer. [K14](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.html)[K23](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-73.html)[K24](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-128.1.html)[K44](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html)[K45](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/last-year.html)

**Version and approval:** this is a substantively changed method. The earlier file recorded Nathan Wiebe's approval dated 3 November 2026. That historical approval does not establish his approval of this version, of these new workings, or of the user's return. No new professional sign-off is claimed. The served approval must come from the actual version's approval record, not a country directory or a copied prose sentence.

### Rates, bands and thresholds

| Item | Applicable rule or figure | Source |
|---|---|---|
| Ordinary capital gains and losses, 2025 and 2026 | One-half inclusion for an ordinary capital gain; one-half allowable ordinary capital loss. No general CAD 250,000 breakpoint or two-thirds rate. Specific statutory exceptions still require their own tests. | ITA 38(a), (b); [K14](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.html) |
| Business activity | Compute profit, not half of sales or receipts. Revenue less the supported costs and deductions, with inventory where applicable. | ITA 9, 10 and 18; [K10](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-9.html)[K11](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-10.html)[K13](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-18.html) |
| 2026 federal taxable income | First 58,523 at 14%; excess over 58,523 through 117,045 at 20.5%; excess over 117,045 through 181,440 at 26%; excess over 181,440 through 258,482 at 29%; excess over 258,482 at 33%. | ITA 117(2), 117.1 and CRA actual 2026 table; [K27](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-117.html)[K28](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-117.1.html)[K38](https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/adjustment-personal-income-tax-benefit-amounts.html)[K44](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html) |
| 2025 federal taxable income, historical filing bridge | First 57,375 at 14.5%; excess through 114,750 at 20.5%; excess through 177,882 at 26%; excess through 253,414 at 29%; excess over 253,414 at 33%. The annual first rate is 14.5%, not 15% or the current consolidated statute's 14%. | CRA actual 2025 table and T1 rate worksheet; [K45](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/last-year.html)[K46](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-r/5006-r-25e.pdf) |
| Superficial-loss acquisition period | Begins 30 days before and ends 30 days after the loss disposition, with a separate ownership or right-to-acquire test at the end. | ITA 54; [K20](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-54.html) |
| Ordinary net capital loss carry | Three years back, indefinitely forward against taxable capital gains, subject to actual limits and historical inclusion adjustments. | ITA 111 and CRA capital losses; [K29](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-111.html)[K40](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/line-12700-capital-gains/capital-losses-deductions.html) |
| Ordinary GST small-supplier threshold | CAD 30,000 of relevant worldwide taxable supplies of the person and associates, tested for a single calendar quarter and the preceding four quarters. Exclude financial services and sales of capital property; not a threshold on every wallet movement or all crypto sales. | ETA 148 and 240; [K33](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-148.html)[K36](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-240.html) |
| GST on a taxable Canadian supply | Federal GST 5%; participating-province tax applies additionally where required. Zero-rated supplies have a zero rate; exempt supplies are a different category. Determine the actual place, supply and registration before using a provincial rate. | ETA 165; [K34](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-165.html) |
| Virtual payment instrument provisions | Effective 18 May 2019, not 2021. Apply the statutory definition rather than treating every token as an exempt instrument. | ETA 123 and CRA Notice 324; [K31](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-123.html)[K06](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/notice324/mining-activities-in-respect-of-cryptoassets.html) |
| Mining-activity GST/HST provisions | Section 188.2 applies from 5 February 2022, subject to its actual exception. An income-tax business is not automatically a commercial activity for ITCs. | ETA 188.2 and CRA Notice 324; [K07](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-188.2.html)[K06](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/notice324/mining-activities-in-respect-of-cryptoassets.html) |
| Ordinary record retention | At least six years from the end of the last tax year to which records relate, with late-filing, objection/appeal and CRA-demand extensions. | ITA 230 and CRA crypto records; [K25](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-230.html)[K04](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/books-records-crypto.html) |

The federal brackets apply progressively to total taxable income after the return's deductions, not separately to each sale. Provincial tax, credits, CPP, losses, AMT and other return items can change the result. An inclusion amount is not tax payable. The dated 2025 form fields below are evidence for that edition, not a declaration that the final 2026 annual forms are available. [K44](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html)[K45](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/last-year.html)[K46](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-r/5006-r-25e.pdf)

## Ask the client first

1. Whose assets and accounts are these? Obtain the legal owner, beneficial owner, individual or entity status, co-ownership shares, Canadian residence dates, province, tax year and any immigration, emigration, death, trust or registered-plan event. A bank payer or wallet controller is not necessarily the beneficial owner. [K01](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-transactions.html)[K23](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-73.html)[K24](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-128.1.html)[K26](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-248.html)
2. What is the activity? Obtain the reason for acquiring and selling, transaction frequency, holding periods, knowledge, time spent, financing, promotion, organization and history. Ask about isolated commercial ventures as well as regular trading. Employment outside crypto does not itself make crypto capital property. [K01](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-transactions.html)[K10](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-9.html)[K15](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-39.html)
3. Obtain all exchange exports, trade confirmations, wallet addresses, transaction hashes, custodial statements, opening holdings and cost records, rewards, referral agreements, lending and pool contracts, and any relevant slips or prior-year workings. Include closed platforms and self-custody accounts. Never request seed phrases, private keys or trading access. The records, not access credentials, are required. [K04](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/books-records-crypto.html)
4. Identify each token, chain and legal right. Include wrapped assets, bridges, receipt tokens, liquidity positions, NFTs, derivatives, locked rewards and changes in beneficial ownership. Ask what a protocol can do with the deposited assets and what the client can demand back. [K08](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/crypto-assets-tax-obligations.html)[K26](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-248.html)
5. Obtain execution times and time zones, units, CAD consideration, FX source, gross and net cash, separately charged fees, embedded spread and any fee paid in another token. Ask whether exports already include those fees. [K03](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/value-crypto.html)[K04](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/books-records-crypto.html)[K16](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html)[K17](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-47.html)
6. For a loss, obtain acquisitions and rights held by the client and affiliated persons for the complete 30-day-before/after period, including the end-date holdings. Ask about spouse/common-law partner, controlled entities and registered plans. Related and affiliated are not interchangeable categories. [K20](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-54.html)[K52](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-251.1.html)
7. For mining and staking, distinguish validator operations, delegated participation, central-exchange rewards, pool sharing and fixed computing-service compensation. Obtain when rewards were earned or credited, quantities, restrictions, CAD values, costs and hardware use. [K02](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-mining-staking-activities.html)[K06](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/notice324/mining-activities-in-respect-of-cryptoassets.html)[K07](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-188.2.html)
8. For GST/HST, obtain registration status, supply descriptions, place and recipient, token rights, associated persons' relevant turnover, reporting periods and input use. Separate merchant sales, token transactions, platform services and mining. [K05](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/gst-hst-crypto-transactions.html)[K31](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-123.html)[K33](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-148.html)[K35](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-169.html)[K36](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-240.html)

**Missing facts:** do not replace an unknown opening cost with zero, an unclassified activity with capital gains, or a disputed FMV with the most favourable quote. Reconstruct the records and record the affected unresolved amount. Show conditional alternatives only when their assumptions are explicit and supported. An acquisition date matters for actual cost, FX, ownership and timing even though Canada has no general short-term versus long-term crypto capital-gain rate. [K01](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-transactions.html)[K03](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/value-crypto.html)[K04](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/books-records-crypto.html)[K14](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.html)[K17](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-47.html)

## The method, step by step

### 1. Establish character before choosing the calculation

CRA considers the full facts, including frequency, holding periods, knowledge, time, financing and promotion. These are indicators, not a trade-count threshold or a safe harbour for a salaried person. An isolated adventure or concern in the nature of trade can be business activity even without habitual dealing. ITA 9 and 39 separate business profit from capital gains. [K01](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-transactions.html)[K10](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-9.html)[K15](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-39.html)

Document a conclusion for each distinct activity and the evidence supporting it. Do not relabel the same holdings between inventory and capital solely to improve a year's tax result. Material changes of use or rights require their own legal analysis. A business loss is not automatically deductible against every other item without the actual income computation and loss limitations. [K09](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-3.html)[K10](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-9.html)[K11](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-10.html)[K15](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-39.html)[K29](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-111.html)

**Source conflict:** CRA's crypto valuation page calls an adventure in the nature of trade “habitual,” while the transaction page describes a non-habitual activity. Do not use that one word to require regular trading. The separate cost rule in ITA 10(1.01) applies to an adventure or concern in the nature of trade. Record the conflict and follow the enacted provision and the actual character facts. [K01](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-transactions.html)[K03](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/value-crypto.html)[K11](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-10.html)

### 2. Reconcile records and separate events

Create one ledger per beneficial owner and tax year, with linked records across exchanges and wallets. For each asset, reconcile opening units plus receipts and acquisitions less disposals and transfers out to closing units. Match internal transfers by hash, units, timing and addresses so an exchange withdrawal and a wallet receipt are not two sales or two purchases. Reconcile any fee-unit difference separately. Keep an unresolved transfer queue and do not invent a sale to force a zero difference. [K01](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-transactions.html)[K04](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/books-records-crypto.html)

Use columns for source file/row, event id, timestamp and time zone, owner, wallet/platform, token/chain, units in/out, event character, CAD FMV and price source, gross proceeds, cash paid/received, fee units/value/purpose, income inclusion, cost added, cost released, remaining pool, gain/loss, GST/HST and unresolved facts. This is a record design, not a claim that CRA mandates those exact column names. [K03](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/value-crypto.html)[K04](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/books-records-crypto.html)[K16](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html)[K17](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-47.html)

One economic event may have several tax components. A swap has an outgoing asset and an incoming asset; a reward can have income now and a later disposal; paying gas in a token can dispose of that token even if the main wallet transfer preserves ownership. Link the components rather than forcing every export row into exactly one universal category. [K01](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-transactions.html)[K02](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-mining-staking-activities.html)[K16](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html)[K26](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-248.html)

### 3. Value in CAD and control fees once

Use a reasonable, consistently applied CAD FMV method supported by the execution records. Where appropriate, use the actual trading pair or a documented reliable multi-exchange method; retain the timestamp, quantity, price and conversion. USD proceeds, a stablecoin label or a quoted “dollar” is not proof of a CAD amount. CRA's examples of pricing methods are not a permission to select a different favourable exchange retrospectively for each trade. [K01](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-transactions.html)[K03](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/value-crypto.html)[K04](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/books-records-crypto.html)

For capital property, distinguish purchase costs properly forming cost from outlays incurred to make a disposition. Do not add an embedded spread again when it is already in the executed CAD cost, or subtract a selling fee twice from already-net cash. For any fee paid in crypto, record the fee token's disposal and supported treatment of the service cost separately; do not deduct and capitalize the same amount. A wallet network fee is not automatically a new cost of all the transferred principal. Business expenditure must meet its actual income-purpose and capital/personal limitations. [K13](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-18.html)[K16](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html)[K17](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-47.html)[K39](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html)

**Authority arithmetic is also checked:** CRA's valuation example lists prices 350, 320, 330 and 345 for one asset but gives an average of 336.50. Their arithmetic mean is 336.25. Recompute the selected documented method, units and rounding from the underlying figures; do not copy a published illustration's wrong total into a client working. [K03](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/value-crypto.html)

### 4. Apply the event and ownership rules

| Event | Canadian treatment and evidence needed | Source |
|---|---|---|
| Sale for CAD or other fiat | Disposal when the rights are disposed of; compute proceeds in CAD, cost and disposition expenses. Do not wait for a bank withdrawal. | [K01](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-transactions.html)[K16](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html) |
| Crypto-for-crypto swap | Barter disposal of the outgoing property plus acquisition of the new property. Support a consistent CAD FMV and fees for both legs; no exemption simply because no fiat changed hands. | [K01](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-transactions.html)[K03](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/value-crypto.html) |
| Purchase of goods/services with crypto | Disposal of crypto and a separate purchase of goods/services. For a merchant receiving crypto, recognize the sale under the ordinary business rules and address GST/HST; later token appreciation is a separate matter. | [K01](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-transactions.html)[K05](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/gst-hst-crypto-transactions.html)[K10](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-9.html)[K32](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-153.html) |
| Own-wallet or own-exchange transfer | No disposal of the principal where beneficial ownership is unchanged, subject to the actual rights and statutory exceptions. Keep the existing cost; separately examine fee-token disposal and service cost. | [K01](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-transactions.html)[K26](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-248.html)[K16](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html) |
| Ordinary gift | Normally FMV disposal and recipient cost, subject to the specific rules below. A missing sale payment does not make a gift exempt. | ITA 69; [K21](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-69.html) |
| Donation to a qualified donee | Separate disposal, receipt and credit analysis. Ordinary crypto is not automatically a qualifying listed security under 38(a.1), so there is no blanket zero-inclusion crypto donation rule. Test deemed FMV/cost limits, advantage, qualified-donee status and token rights before any receipt or tax result. | ITA 38 and 248(35)–(37); [K14](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.html)[K26](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-248.html) |
| Spouse/common-law partner transfer | For eligible capital property under 73(1)/(1.01), both must be Canadian resident at transfer and the transferee must qualify; generally ACB rollover unless the transferor elects out. Former-spouse property settlements and eligible trusts have their own conditions. Later attribution is a separate question, not settled by a rollover. | [K23](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-73.html) |
| Death | Default 70(5) capital-property FMV disposal and beneficiary FMV cost; conditional spouse/qualifying testamentary-trust rollover under 70(6), subject to residence, indefeasible vesting and election rules. Inventory and accrued income are not all converted into capital gains by death. | [K22](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-70.html)[K10](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-9.html) |

For a donation, 248(35) can deem FMV to the lower of actual FMV and cost/ACB for tax-shelter gifts and specified recent acquisitions, subject to 248(37) exceptions and other anti-avoidance rules. Thus even the ordinary FMV disposal description cannot replace the actual gift computation. Selling crypto for cash and then donating the cash is a different sequence from giving the token itself. Do not certify a receipt value or donation credit from this method alone. [K21](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-69.html)[K26](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-248.html)

### 5. Maintain the capital identical-property pool

For identical capital properties under section 47, use the owner's combined remaining pool across their accounts, not FIFO, specific lots or one average per exchange. Different token rights, chains, wrapped claims or NFTs are not automatically identical merely because a software ticker matches. Establish identity first. A pooled ordinary token example is not an inventory valuation election. [K17](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-47.html)[K08](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/crypto-assets-tax-obligations.html)[K11](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-10.html)

Before a sale, average cost per unit = remaining pool ACB divided by remaining units. Cost released = units disposed of multiplied by that average. Gain/loss = gross CAD proceeds minus that cost minus supported disposition outlays. Reduce units and ACB by the actual disposed amount. On a later acquisition, add the new cost to the **remaining** ACB, then divide by all units now held. Never re-add cost belonging to units already sold. Reconcile closing cost and units without rounding the running average prematurely. [K16](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html)[K17](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-47.html)[K39](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html)

Incorporate actual statutory cost adjustments, income-inclusion cost bridges, gifts, rollovers and any allowed superficial-loss adjustment at the proper time. Section 52(1) can add an amount included in income only under its actual conditions, including that it has not already been added to cost and its residence/income predicates. Do not assume the full FMV is a second cost addition after software has already recorded it. [K18](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-52.html)[K19](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-53.html)[K21](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-69.html)[K23](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-73.html)

### 6. Compute business profit and reward income without duplication

For a trading business, account for sales, opening inventory, purchases/costs, closing inventory and supported expenses. Ordinary business inventory under 10(1) is lower cost/FMV for the items or the prescribed whole-inventory FMV method, with applicable continuity rules. An adventure or concern in the nature of trade is at cost under 10(1.01). Different crypto asset types require separate inventory analysis. Do not impose the capital section 47 average as the only business inventory valuation method. [K03](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/value-crypto.html)[K10](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-9.html)[K11](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-10.html)[K37](https://laws-lois.justice.gc.ca/eng/regulations/c.r.c.,_c._945/page-30.html?wbdisable=true)

CRA states that mined crypto is valued as income when earned, with business character depending on the activity, and that most mining will be business activity. It now expressly addresses centralized-exchange staking: rewards will generally be income when credited to the platform wallet. “No definitive CRA staking guidance” is obsolete. Retain the actual earning/crediting date, restrictions and contract; do not delay income until conversion to fiat or apply that CEX sentence indiscriminately to every smart-contract arrangement. [K02](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-mining-staking-activities.html)

Separate validator/pool revenue from passive investment or contractual interest and from the return of the client's own principal. Genuine interest may engage 12(1)(c) and its timing rules; a product named “Earn” does not prove legal interest. Property/investment income belongs on its applicable return line, not automatically the other-income residual. [K12](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-12.html)[K48](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/line-12100-interest-other-investment-income.html)[K49](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/line-13000-other-income.html)

For a reward already included in income, identify the resulting cost/inventory treatment before its later sale. Reconcile income included, cost recognized, inventory and cost released so the same received value is not taxed twice as both revenue and a zero-cost sale, or deducted twice as a cost and an expense. For business-generated inventory, do not add an independent blanket “FMV acquisition expense” merely because there was a reward; use the actual income and inventory treatment. [K02](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-mining-staking-activities.html)[K10](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-9.html)[K11](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-10.html)[K18](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-52.html)

Mining electricity, pool charges and other expenses require the business-income and actual-use tests; hardware may be capital and require the correct CCA class and placed-in-use rules rather than an immediate full deduction. CRA says ASIC miners and GPUs **may** qualify as class 50, not that every device does. “Small operation” alone does not prove non-business status, and non-business mining does not establish a universal zero cost rule. Record the legal basis before a non-business cost or subsequent capital-gain claim. [K02](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-mining-staking-activities.html)[K13](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-18.html)

### 7. Investigate rewards and protocols instead of using labels as law

| Event or product | Required analysis | Source |
|---|---|---|
| Airdrop for services or promotion | Determine the underlying remuneration/business/income source, when the right/value arose and its cost consequences. An action such as clicking “claim” is not by itself a statutory income test. | ITA 3, 9 and 52; [K09](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-3.html)[K10](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-9.html)[K18](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-52.html) |
| Unsolicited airdrop or hard fork | Record control, rights, consideration, restrictions and value. This method establishes neither automatic FMV income nor automatic zero ACB for every distribution. Obtain authority for the particular receipt and cost before completing that component. | [K08](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/crypto-assets-tax-obligations.html)[K09](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-3.html)[K18](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-52.html)[K26](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-248.html) |
| Referral bonus | Obtain the agreement and services/conditions; assess the actual income source and timing. A software label cannot settle it. | [K09](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-3.html)[K10](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-9.html)[K18](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-52.html) |
| Cashback | Distinguish a purchase-price rebate, promotional compensation and another income receipt using the underlying purchase and agreement. No blanket “all cashback is income” or “all is exempt.” | [K09](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-3.html)[K10](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-9.html)[K18](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-52.html) |
| DeFi deposit, loan or liquidity pool | Read beneficial-ownership and disposal rights, redemption obligation, receipt token, interest/yield and fee terms. A deposit may dispose of the original property, but do not invent a universal taxable deposit or tax-free lending rule. Isolate principal, any new right, rewards and later redemption. | [K26](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-248.html)[K01](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-transactions.html)[K12](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-12.html) |
| Wrapped token or bridge | Determine whether original property is disposed of or only custody changes, and whether the received right is identical. If a taxable exchange occurs, an FMV acquisition of the new token does not cancel a gain on the old token. If not, support the continuity rather than recording an invented disposal. | [K26](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-248.html)[K16](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html)[K17](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-47.html) |
| NFT | Classify actual rights, creation/trading business, investment or personal use; value individually where not identical. The crypto label alone does not decide capital character, inventory, personal-use loss restrictions or GST/HST. | [K08](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/crypto-assets-tax-obligations.html)[K01](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-transactions.html)[K15](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-39.html)[K31](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-123.html) |

These topics remain in the method with the actual evidence and decision needed. No settled CRA position for every fork, airdrop, wrapper, liquidity token, NFT or non-business mining arrangement has been established by the sources read for this version. Hold that component rather than turning an uncertainty label into an automatic tax election. Continue reconciling and computing unrelated supported transactions.

### 8. Apply loss restrictions and aggregate correctly

For an ordinary loss, test section 54's **two** conditions: the taxpayer or affiliated person acquires the same or identical property during the period from 30 days before through 30 days after disposal, **and** the taxpayer or an affiliated person owns or has a right to acquire the substituted property at the end. Test actual statutory exceptions as well; deemed death/departure disposals, for example, have separate treatment. [K20](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-54.html)

Where a superficial loss is denied under 40(2)(g)(i), 53(1)(f) may increase the eligible substituted property's ACB for its owner. Do not put the seller's loss into the wrong person's pool or guarantee future relief from a registered-plan purchase. Partial repurchases, different quantities, rights, multiple affiliated accounts and other stop-loss rules need their actual allocation and ownership tests. The full same-owner/full-repurchase example below is not a universal partial-quantity formula. [K16](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html)[K19](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-53.html)[K20](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-54.html)[K52](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-251.1.html)[K40](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/line-12700-capital-gains/capital-losses-deductions.html)

Net allowable ordinary capital losses against taxable capital gains under the year's actual computation. An excess is a net capital loss, not a negative salary offset on line 12700. Track carryback/forward balances, year of origin and inclusion-rate adjustments. Historical losses, death-year relief, ABIL, personal-use and listed-personal-property rules need their own eligibility analysis. Business losses follow the business and non-capital-loss rules; do not label every crypto loss a business loss. [K09](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-3.html)[K14](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.html)[K29](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-111.html)[K40](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/line-12700-capital-gains/capital-losses-deductions.html)

### 9. Analyze GST/HST independently

A payment instrument under ETA 123 is a digital representation of value functioning as a medium of exchange and existing only at a publicly distributed ledger address, excluding the specified redemption, gaming/reward and prescribed categories. Do not certify VPI status just from “Bitcoin-like,” “stablecoin,” “utility” or “security” in a name. A token outside VPI can still meet another financial-instrument definition, such as an actual debt or equity instrument. [K31](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-123.html)

CRA describes a sale of a VPI as an exempt financial service: do not charge GST/HST on that exempt sale, and related inputs generally do not support ITCs. A non-VPI token's supply must be classified separately; it is not automatically taxable or exempt. Platform fees also require the actual service: arranging a financial service and excluded advice, administrative or preparatory services are not interchangeable. Obtain the invoice and contract before certifying GST/HST on the platform's charge. [K05](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/gst-hst-crypto-transactions.html)[K31](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-123.html)[K35](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-169.html)

When a registrant sells taxable goods/services for crypto, compute tax on the CAD value of the consideration at the supply time under 153, with the correct place-of-supply rate and tax-inclusive/exclusive agreement. Record the sales revenue, tax liability and token receipt separately, then account for the later token sale. A small supplier and exempt or zero-rated supply have different consequences. Test the applicable 148/240 registration rules using the person's and associates' relevant taxable supplies, not just fiat receipts. Refer non-resident/digital-economy or public-service-body special rules rather than applying the ordinary threshold mechanically. [K05](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/gst-hst-crypto-transactions.html)[K32](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-153.html)[K33](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-148.html)[K34](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-165.html)[K36](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-240.html)

**Mining from 5 February 2022:** 188.2 defines mining activities by actual validation/addition, ledger maintenance/access or computing-resource work, not the product's marketing name. Under (2)–(4), acquisitions/use in those activities are generally deemed non-commercial, and mining activity and associated mining payment are generally deemed not to be supplies, with the statutory ITC consequences. This can apply even when mining is a business for income tax. Do not claim hardware/electricity ITCs simply because there is mining revenue or GST registration. Passive staking rewards do not by their label prove the recipient performs a statutory mining activity. [K06](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/notice324/mining-activities-in-respect-of-cryptoassets.html)[K07](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-188.2.html)

The 188.2(5) exception requires **all** relevant conditions: the activity is performed for another person whose identity is known, that other person is not a mining-group operator in respect of a mining group including the supplier, and, where the recipient is both non-resident and not dealing at arm's length with the supplier, each property/service received from the supplier as a consequence of the mining activity is supplied, or used or consumed in making a supply, by that non-resident recipient to persons whose identities are known to that recipient and who deal at arm's length with it; where the specified mining-group condition applies, those onward persons must not be operators of that group including the recipient. “Known customer” alone is insufficient. Where the exception applies, analyze the ordinary GST/HST rules, not automatic exemption or automatic ITC entitlement. [K07](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-188.2.html)

Read the pool agreement. Sharing actual mining payments and success risk can form a mining group; fixed estimated compensation without actual-payment adjustment can instead be a computing-service supply. CRA's examples also distinguish a pool operator's supply to a member from a member's supply to the operator. Keep deductions from rewards separate from a claimed separate service where the contract does not establish one. Pre-5-February-2022 mining uses the then-applicable rules, not automatic retroactive 188.2 treatment. Imported equipment/hosting and non-resident arrangements need the separate Notice 324 analysis. [K06](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/notice324/mining-activities-in-respect-of-cryptoassets.html)

### 10. Map the working to the right-year return and preserve the evidence

| Output | Filing bridge and control | Source |
|---|---|---|
| 2025 capital crypto disposals | Actual 2025 Schedule 3, Part 3, crypto-assets row 7: description, units, columns for acquisition year, proceeds, ACB, outlays and gain/loss. Total proceeds 15200; total gain/loss 15301. Aggregate through the schedule, then positive taxable capital gains to T1 line 12700. Do not put a net loss there as negative other income. | [K41](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s3/5000-s3-25e.pdf)[K46](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-r/5006-r-25e.pdf)[K40](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/line-12700-capital-gains/capital-losses-deductions.html) |
| 2025 sole-proprietor business | Actual T2125, **Statement of Business or Professional Activities**, separately for each business/profession. Complete identity/fiscal period/industry and relevant internet-business fields, income and inventory/COGS, expenses and adjustments. T1 business gross 13499/net 13500, not all receipts at a capital half rate. | [K47](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf)[K46](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-r/5006-r-25e.pdf) |
| 2025 investment or other receipt | Identify its legal income source. Interest/other investment income belongs on applicable line 12100; line 13000 is residual taxable income not properly reportable elsewhere and requires the income type. A staking or “Earn” label alone does not determine that line. Match slips and the underlying ledger once. | [K12](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-12.html)[K48](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/line-12100-interest-other-investment-income.html)[K49](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/line-13000-other-income.html)[K46](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-r/5006-r-25e.pdf) |
| 2025 ordinary deadline | 30 April 2026; qualifying business filer/cohabiting spouse or partner generally 15 June 2026, but ordinary balance due 30 April. The statutory tax-shelter expenditure exception and death/special-return rules still apply. | ITA 150(1)(d); [K30](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html)[K42](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/important-dates-individuals.html) |
| 2026 ordinary deadline | 30 April 2027; qualifying business filer/cohabiting spouse or partner generally 15 June 2027, with the same tax-shelter exception. Ordinary balance due 30 April 2027. Determine GST/HST deadlines separately by account/reporting period. | ITA 150(1)(d); [K30](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html)[K43](https://www.canada.ca/en/services/taxes/resources-for-small-and-medium-businesses/2026-tax-deadlines-canadian-businesses-self-employed-individuals.html) |
| Filing channel | Use the actual eligible return-year software/channel, authorization and restrictions: self-filing through certified software/NETFILE, authorized professional through EFILE, or the appropriate paper route. CRA account access is not interchangeable with transmitting a normal crypto return. | [K50](https://www.canada.ca/en/services/taxes/income-tax/personal-income-tax/how-file/tax-software/send-return/netfile.html)[K51](https://www.canada.ca/en/services/taxes/income-tax/personal-income-tax/how-file.html) |

For T2125, retain the bridge from exported sales/receipts to gross income, opening inventory 8300, purchases 8320, other applicable direct costs, closing inventory 8500 and cost of goods sold 8518. The form includes adjustments and final net-income fields; a gross-profit subtotal is not necessarily final T1 net business income. Hardware/CCA and any personal-use allocation need their actual schedules. No current-year crypto loss or reward should be omitted merely because an exchange did not issue a slip. [K01](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-transactions.html)[K02](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-mining-staking-activities.html)[K04](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/books-records-crypto.html)[K47](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf)

As read on 14 November 2026, NETFILE's posted current window accepts initial 2018–2025 returns and ReFILE 2022–2025, subject to restrictions. Do not claim the 2026 annual return can already be transmitted. CRA also announces an invitation-only pre-filled CRA-account route from March 2027; that announcement does not establish eligibility for a particular crypto investor. Refresh the actual channel/year rules at filing. [K50](https://www.canada.ca/en/services/taxes/income-tax/personal-income-tax/how-file/tax-software/send-return/netfile.html)[K51](https://www.canada.ca/en/services/taxes/income-tax/personal-income-tax/how-file.html)

Preserve the submitted copy, required authorization, transmission confirmation or mailing evidence, and later notice of assessment/reassessment. A prepared import/working, a human approval, a submitted return, an assessment and a payment are different events. Keep unsupported positions and outstanding data separate; never describe an audit calculation as a completed filing.

Keep transaction records, exchange/platform exports, wallet addresses, timestamps, CAD valuations and price sources, ownership, contracts, invoices, opening/closing units and cost, tax workings, returns and notices. For mining include equipment, expense and pool records. Retain acquisition evidence through the last year it supports the cost or subsequent return, then the statutory retention period. Under 230, late returns can restart the six-year period from filing; objections/appeals and CRA demands extend retention. Electronic records must remain readable; early disposal requires the applicable written permission. [K04](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/books-records-crypto.html)[K25](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-230.html)

### Transaction-pattern library: evidence prompts, not automatic decisions

| Export or bank pattern retained from the original | What to match and decide | Source |
|---|---|---|
| NEWTON BUY / SHAKEPAY BUY | Match the actual fill, owner, units and total CAD cost. Do not add a quoted spread twice. The name does not prove the current fee schedule. | [K03](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/value-crypto.html)[K04](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/books-records-crypto.html)[K17](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-47.html) |
| BITBUY PURCHASE / COINSMART BUY | Match the gross purchase and separately charged fee against confirmation and cash; classify any fee token separately. | [K03](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/value-crypto.html)[K04](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/books-records-crypto.html)[K16](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html) |
| KRAKEN BUY (CAD pair) | Confirm the pair really is CAD and identify gross cost, fees and owner; combine identical capital holdings across accounts. | [K03](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/value-crypto.html)[K04](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/books-records-crypto.html)[K17](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-47.html) |
| WEALTHSIMPLE CRYPTO BUY | Use executed CAD cost and actual charge, not an assumed extra spread. | [K03](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/value-crypto.html)[K04](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/books-records-crypto.html)[K17](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-47.html) |
| SELL ORDER | Match execution, gross proceeds, fees and net cash. A later bank withdrawal is not a second disposal. | [K01](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-transactions.html)[K04](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/books-records-crypto.html)[K16](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html) |
| CONVERT / SWAP / TRADE | Match both token legs, quantity and FMV; ordinary crypto exchange is a barter disposal/acquisition, subject to actual rights. | [K01](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-transactions.html)[K03](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/value-crypto.html)[K26](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-248.html) |
| CAD WITHDRAWAL | Trace the existing account balance, any linked sale and fees. Withdrawal alone is not a second crypto sale or new income, but cannot erase the underlying sale. | [K01](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-transactions.html)[K04](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/books-records-crypto.html) |
| CAD DEPOSIT | Trace own funding versus another person's funds, loan, business receipt or connected trade. A cash-deposit label alone does not prove non-income. | [K01](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-transactions.html)[K04](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/books-records-crypto.html) |
| STAKING REWARD | Distinguish actual CEX credit, validation, contractual investment return and return of principal; income and cost must reconcile. | [K02](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-mining-staking-activities.html)[K12](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-12.html)[K18](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-52.html) |
| MINING PAYOUT | Match when earned, pool agreement, gross/net components, business character, inventory and the independent 188.2 analysis. No automatic hobby zero-cost branch. | [K02](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-mining-staking-activities.html)[K06](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/notice324/mining-activities-in-respect-of-cryptoassets.html)[K07](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-188.2.html)[K11](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-10.html) |
| REFERRAL BONUS (crypto) | Inspect agreement, consideration/services and income source; retain value/timing and any resulting cost. | [K09](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-3.html)[K10](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-9.html)[K18](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-52.html) |
| EARN / LENDING INTEREST | Read the actual lending/ownership/interest rights and accrual terms. The product title does not establish property income or no disposal. | [K12](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-12.html)[K26](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-248.html)[K48](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/line-12100-interest-other-investment-income.html) |
| CASHBACK REWARD (crypto) | Inspect original purchase and rebate/compensation terms before character and cost. | [K09](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-3.html)[K10](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-9.html)[K18](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-52.html) |
| TRANSFER TO COLD WALLET | Prove the same beneficial owner, match principal and fee units and preserve original cost. | [K01](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-transactions.html)[K04](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/books-records-crypto.html)[K26](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-248.html) |
| TRANSFER BETWEEN EXCHANGES | Match both sides and fee difference; do not treat all network costs as automatic capital additions or all custody changes as ownership continuity. | [K01](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-transactions.html)[K04](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/books-records-crypto.html)[K16](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html)[K26](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-248.html) |
| FIAT DEPOSIT / WITHDRAWAL | Reconcile cash and connected trades, FX or another person's funds; do not classify the bank text alone as crypto income or an exemption. | [K01](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-transactions.html)[K03](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/value-crypto.html)[K04](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/books-records-crypto.html) |

These exchange strings are historical examples from the original file, not fetched promises about a platform's current products, fees, ownership terms or availability. Confirm the actual records. If a shared global crypto workflow proposes FIFO, short/long-term tax rates, automatic zero costs, universal airdrop income, universal wrapping or DeFi outcomes, those assumptions are not this Canadian method and must not override the rules above.

## Worked cases

All cases are fictional. Legal character, ownership and other stated conditions are assumptions for each calculation, not facts inferred about a real client. Amounts are CAD. The blocks recompute the specified workings; passing them does not establish that a real transaction meets the assumed law.

### C1. Partial sale, another purchase and a second sale

Assume identical capital tokens, no loss restriction and purchase costs already inclusive of charges. Buy 2 units for 20,100 and 1 for 12,060: pool 3 units/32,160, average 10,720. Sell 1.5 for gross 21,000 with fee 150: release 16,080, gain 4,770, taxable gain 2,385; remaining 1.5 units/16,080. Buy 0.5 for 4,020: pool 2 units/20,100, average 10,050. Sell 0.5 for 6,000 with fee 30: gain 945, taxable gain 472.50; remaining 1.5 units/15,075. Do not restore the sold 16,080 to the new pool. [K14](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.html)[K16](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html)[K17](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-47.html)

```oa-check
name: ca-crypto-pool
inputs:
  first_cost: 20100
  second_cost: 12060
  first_units: 2
  second_units: 1
  sold_units: 1.5
  gross: 21000
  fee: 150
  later_cost: 4020
  later_units: 0.5
  second_gross: 6000
  second_fee: 30
steps:
- pool_cost: first_cost + second_cost
- pool_units: first_units + second_units
- average: pool_cost / pool_units
- released: average * sold_units
- gain: gross - released - fee
- taxable_gain: gain * 0.5
- remaining_cost: pool_cost - released
- remaining_units: pool_units - sold_units
- next_cost: remaining_cost + later_cost
- next_units: remaining_units + later_units
- next_average: next_cost / next_units
- next_released: next_average * later_units
- next_gain: second_gross - next_released - second_fee
- next_taxable: next_gain * 0.5
- closing_cost: next_cost - next_released
- closing_units: next_units - later_units
expected:
  pool_cost: 32160
  pool_units: 3
  average: 10720
  released: 16080
  gain: 4770
  taxable_gain: 2385
  remaining_cost: 16080
  remaining_units: 1.5
  next_cost: 20100
  next_units: 2
  next_average: 10050
  next_released: 5025
  next_gain: 945
  next_taxable: 472.5
  closing_cost: 15075
  closing_units: 1.5
```

### C2. Already-net sale and embedded spread

A fill spends 10,000 including its spread to acquire 1 token. Do not add an estimated 100 spread again. A later confirmation shows gross sale 13,000, fee 100 and net cash 12,900. With no other costs or adjustments, gain is 2,900, taxable 1,450. Using the already-net cash and deducting 100 again would wrongly report 2,800. [K14](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.html)[K16](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html)[K17](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-47.html)

```oa-check
name: ca-crypto-fees-once
inputs:
  purchase_total: 10000
  embedded_spread: 100
  gross: 13000
  fee: 100
steps:
- net_cash: gross - fee
- gain: gross - purchase_total - fee
- same_gain_from_net: net_cash - purchase_total
- taxable_gain: gain * 0.5
- wrong_double_fee_gain: net_cash - purchase_total - fee
- wrong_double_spread_cost: purchase_total + embedded_spread
expected:
  net_cash: 12900
  gain: 2900
  same_gain_from_net: 2900
  taxable_gain: 1450
  wrong_double_fee_gain: 2800
  wrong_double_spread_cost: 10100
```

### C3. Barter and a wrapping decision

Capital token A has ACB 6,000; it is exchanged for 10 units of token B worth 10,000 with no separate fee. A's gain is 4,000 and taxable gain 2,000; B's starting cost is 10,000. If these same values instead describe a wrapper, determine the actual legal disposal first. A taxable exchange would still produce that 4,000 gain even though the new token's cost and FMV are both 10,000. A supported no-disposal custody event would preserve the original 6,000 cost. These are alternatives, not simultaneous entries. [K01](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-transactions.html)[K14](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.html)[K16](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html)[K26](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-248.html)

```oa-check
name: ca-crypto-barter-wrapper
inputs:
  old_cost: 6000
  value: 10000
  new_units: 10
steps:
- disposal_gain: value - old_cost
- taxable_gain: disposal_gain * 0.5
- new_unit_cost_if_exchange: value / new_units
- continuing_cost_if_no_disposal: old_cost
expected:
  disposal_gain: 4000
  taxable_gain: 2000
  new_unit_cost_if_exchange: 1000
  continuing_cost_if_no_disposal: 6000
```

### C4. Income receipt, later capital sale and a fee-token disposal

Assume a CEX reward of 0.2 token is taxable income at a supported CAD 3,000 when credited. It is the first holding of this token; the actual 52(1) conditions support cost 3,000, with no duplicate cost already recorded. The subsequent disposal is established capital property and occurs for 3,600, with a 20 cash selling fee: later gain 580, taxable gain 290, separately from the original 3,000 income. A real activity with business inventory would need its business computation instead. [K02](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-mining-staking-activities.html)[K14](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.html)[K16](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html)[K18](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-52.html)

Separately, transferring 1 principal token between the same owner's wallets is not itself a sale. Suppose 0.01 of a distinct fee token is paid for the network service, with its own pool cost 200 per unit and FMV 3: fee token cost released 2 and gain 1, taxable 0.50 if capital. Do not call the principal a disposal or automatically add the service value to its ACB. The service cost's deductibility or capitalization remains a separate supported conclusion. [K01](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-transactions.html)[K14](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.html)[K16](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html)[K26](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-248.html)

```oa-check
name: ca-crypto-reward-fee-token
inputs:
  reward_units: 0.2
  income_value: 3000
  later_proceeds: 3600
  cash_sale_fee: 20
  fee_units: 0.01
  fee_token_unit_cost: 200
  fee_token_value: 3
steps:
- reward_unit_cost: income_value / reward_units
- later_gain: later_proceeds - income_value - cash_sale_fee
- later_taxable: later_gain * 0.5
- fee_cost_released: fee_units * fee_token_unit_cost
- fee_gain: fee_token_value - fee_cost_released
- fee_taxable: fee_gain * 0.5
expected:
  reward_unit_cost: 15000
  later_gain: 580
  later_taxable: 290
  fee_cost_released: 2
  fee_gain: 1
  fee_taxable: 0.5
```

### C5. Full superficial loss and an alternative outside the period

Assume the same taxpayer sells all 1 identical capital token on 10 March 2026: ACB 10,000, proceeds 8,000, no fee. They buy 1 on 25 March for 8,500 and still own it on 9 April, the end of the 30-day-after period. With both statutory conditions met and no exception, the 2,000 loss is denied; their eligible replacement ACB becomes 10,500. If instead the only new acquisition/right is on 15 April, with none by self or an affiliate in the complete 8 February–9 April period, the superficial-loss rule does not deny the 2,000 loss. Assuming no other restriction, allowable capital loss is 1,000. [K14](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.html)[K16](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html)[K19](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-53.html)[K20](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-54.html)

```oa-check
name: ca-crypto-superficial
inputs:
  cost: 10000
  proceeds: 8000
  replacement_cost: 8500
steps:
- economic_loss: cost - proceeds
- replacement_acb_if_denied: replacement_cost + economic_loss
- allowable_if_unrestricted: economic_loss * 0.5
expected:
  economic_loss: 2000
  replacement_acb_if_denied: 10500
  allowable_if_unrestricted: 1000
```

### C6. A business inventory computation and a source arithmetic check

Using CRA's fictional trading-business amounts: sales 240,000, opening inventory 180,000, purchases 30,000, closing inventory 12,000 and other deductible expenses 2,000 give COGS 198,000, gross profit 42,000 and business profit 40,000. Do not halve the profit or deduct all purchases again after COGS. This case does not settle the valuation method or costs for every mining operation. [K01](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-transactions.html)[K10](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-9.html)[K11](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-10.html)

For the separate CRA valuation illustration with four prices 350, 320, 330, 345 and 6 units, the arithmetic mean is 336.25 and value 2,017.50, not the page's 336.50/2,019. These are a source-quality check, not a price supplied for a client's assets. [K03](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/value-crypto.html)

```oa-check
name: ca-crypto-business-source-math
inputs:
  sales: 240000
  opening: 180000
  purchases: 30000
  closing: 12000
  expenses: 2000
  p1: 350
  p2: 320
  p3: 330
  p4: 345
  units: 6
steps:
- cogs: opening + purchases - closing
- gross_profit: sales - cogs
- net_business_profit: gross_profit - expenses
- price_mean: (p1 + p2 + p3 + p4) / 4
- valuation: price_mean * units
expected:
  cogs: 198000
  gross_profit: 42000
  net_business_profit: 40000
  price_mean: 336.25
  valuation: 2017.5
```

### C7. Merchant paid in crypto and GST mining distinction

Assume an ordinary registered merchant makes a taxable supply in a non-participating province, worth 1,000 before GST. They receive crypto worth 1,050 including 50 GST, and record 1,000 revenue plus 50 tax liability, not 1,050 revenue plus another 50 tax. The later token disposal needs its own character/cost working. This example uses federal 5% only under the stated place facts, not a Canada-wide combined rate. [K05](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/gst-hst-crypto-transactions.html)[K32](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-153.html)[K34](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-165.html)

Assume separately that 500 GST on an acquisition relates entirely to activities governed by 188.2(2), with no (5) exception. It does not become a 500 ITC merely because mining is an income-tax business: the covered acquisition is deemed non-commercial. If facts establish the exception, redo the ordinary entitlement and use allocation rather than carrying this result across. [K07](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-188.2.html)[K35](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-169.html)

```oa-check
name: ca-crypto-merchant-gst
inputs:
  tax_exclusive_sale: 1000
  gst_rate: 0.05
  input_gst: 500
  covered_commercial_fraction: 0
steps:
- output_gst: tax_exclusive_sale * gst_rate
- token_value_received: tax_exclusive_sale + output_gst
- recorded_revenue: token_value_received - output_gst
- covered_input_credit: input_gst * covered_commercial_fraction
expected:
  output_gst: 50
  token_value_received: 1050
  recorded_revenue: 1000
  covered_input_credit: 0
```

### C8. Federal bracket bridge, not a complete tax bill

Assume taxable income 120,000. Before credits, provincial tax and other adjustments, 2026 federal bracket tax is 58,523 × 14% + (117,045 − 58,523) × 20.5% + (120,000 − 117,045) × 26% = 20,958.53 after rounding the total to cents. The separately dated 2025 amount is 57,375 × 14.5% + (114,750 − 57,375) × 20.5% + (120,000 − 114,750) × 26% = 21,446.25. Do not use 2025's obsolete 158,468/220,000 limits or apply the marginal rate to gross crypto proceeds. [K44](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html)[K45](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/last-year.html)

```oa-check
name: ca-crypto-federal-bridge
inputs:
  taxable_income: 120000
  first_2026: 58523
  second_2026: 117045
  first_2025: 57375
  second_2025: 114750
steps:
- tax_2026: round(first_2026 * 0.14 + (second_2026 - first_2026) * 0.205 + (taxable_income - second_2026) * 0.26, 2)
- tax_2025: round(first_2025 * 0.145 + (second_2025 - first_2025) * 0.205 + (taxable_income - second_2025) * 0.26, 2)
expected:
  tax_2026: 20958.53
  tax_2025: 21446.25
```

### C9. Net capital loss and wallet reconciliation

Assume ordinary gains 6,000 and unrestricted ordinary losses 10,000, with no special adjustment: taxable gains 3,000 and allowable losses 5,000 give a net capital loss 2,000. Do not enter negative 2,000 on T1 line 12700 against employment income. Track the available loss for the appropriate carry application. [K09](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-3.html)[K14](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.html)[K29](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-111.html)[K40](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/line-12700-capital-gains/capital-losses-deductions.html)

An owner starts with 2 tokens, buys 1, sells 0.5 and transfers 1.2 internally between two of their accounts. Their combined closing holding is 2.5 before any separately identified fees; counting the internal debit without its matching receipt would incorrectly show 1.3. Reconcile both wallets before calculating proceeds or gains. [K01](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-transactions.html)[K04](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/books-records-crypto.html)

```oa-check
name: ca-crypto-loss-transfer
inputs:
  gross_gains: 6000
  gross_losses: 10000
  opening_units: 2
  bought: 1
  sold: 0.5
  internal_transfer: 1.2
steps:
- taxable_gains: gross_gains * 0.5
- allowable_losses: gross_losses * 0.5
- net_capital_loss: allowable_losses - taxable_gains
- combined_closing_units: opening_units + bought - sold
- wrong_one_sided_closing: combined_closing_units - internal_transfer
expected:
  taxable_gains: 3000
  allowable_losses: 5000
  net_capital_loss: 2000
  combined_closing_units: 2.5
  wrong_one_sided_closing: 1.3
```

## When to refuse or refer

- **Missing cost, ownership or complete records:** hold the affected result and identify the exact record needed. Do not substitute zero ACB, claim a missing receipt as an exemption, or hide a quantity mismatch in a balancing sale. [K04](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/books-records-crypto.html)[K16](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html)[K17](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-47.html)
- **Unresolved capital/business or income character:** complete the factual matrix and obtain the legal conclusion. Show conditional numbers separately where useful; do not default to the lower inclusion. [K01](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-transactions.html)[K09](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-3.html)[K10](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-9.html)[K15](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-39.html)
- **Airdrops, forks, DeFi, wrapping, NFTs or non-business mining:** preserve the transaction and test actual rights, source and cost; obtain specific authority where the published material does not settle the case. Do not announce blanket CRA approval of a treatment. [K08](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/crypto-assets-tax-obligations.html)[K18](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-52.html)[K26](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-248.html)
- **Immigration or emigration:** apply residence and the actual 128.1 events, timing and exceptions. Departure is not a deemed sale of every crypto holding without exception: Canadian-PE business property and the qualifying short-resident pre-arrival/inherited-property exception can matter. The latter tests residence of not more than 60 months in the preceding 120 months and the property's acquisition history. Transfer to a foreign wallet alone does not decide tax residence or statutory situs. [K24](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-128.1.html)
- **Death or spousal/trust transfer:** establish capital versus inventory, actual residence, qualifying transferee/trust, vesting and elections. For 70(6), the ordinary indefeasible-vesting period is 36 months with the stated timely application/extension route; the representative may elect under 70(6.2). Do not promise all gifts or all deaths roll over. [K21](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-69.html)[K22](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-70.html)[K23](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-73.html)
- **Donation:** qualified donee, token rights, advantage and 248(35)–(37) can change both disposal and receipt amounts. Obtain the correct gift/credit computation; do not use the original proposed zero-gain claim. [K14](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.html)[K26](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-248.html)
- **GST/HST:** uncertain token classification, platform service, mining group, related-party exception, imports/hosting, non-resident supplies or mixed commercial inputs need their actual analysis. A business classification for income tax does not settle commercial use for GST/HST. [K05](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/gst-hst-crypto-transactions.html)[K06](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/notice324/mining-activities-in-respect-of-cryptoassets.html)[K07](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-188.2.html)[K31](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-123.html)[K35](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-169.html)
- **Foreign information reporting, source tax or treaty issues:** test actual ownership, property situs, cost and reporting scope; use the Canadian foreign-reporting and residence methods as needed. Do not automatically classify every exchange or wallet as foreign reportable property. No United States domestic reporting or tax calculation is supplied here. [K24](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-128.1.html)[K26](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-248.html)
- **Corporations, trusts, partnerships, registered plans and special losses:** retain the records and route to the applicable return, attribution/stop-loss and entity rules. The ordinary half inclusion is not a substitute for a complete entity tax engine. [K14](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.html)[K16](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html)[K29](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-111.html)
- **Return submission or payment:** preparation and validation do not authorize access, filing, trades or payment. Confirm the actual human approval and eligible channel; keep submission, assessment and payment evidence distinct. [K50](https://www.canada.ca/en/services/taxes/income-tax/personal-income-tax/how-file/tax-software/send-return/netfile.html)[K51](https://www.canada.ca/en/services/taxes/income-tax/personal-income-tax/how-file.html)

Completion check: owner and year established; character documented; units reconciled; CAD values and fees supported; no duplicate spread, cost or income; capital pool or business inventory method justified; reward receipts linked to later disposals; losses tested through the full window; GST/HST analyzed separately; correct-year forms and channels checked; unresolved components listed; actual approval status preserved; no invented filing receipt.

## Sources

Official sources were read on 14 November 2026 for the bounded portions stated below. Same-day previously fetched official copies were reused where the audit manifest records that fact. A successful download alone was not counted as a legal read. Exact original-language locators, source hashes, each original topic's destination and independent review are attached to the country PR's audit ledger.

| ID and official source | Actual bounded portion read | Short exact locator | Read date |
|---|---|---|---|
| [K01](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-transactions.html) | Read for: Whole operative crypto dispositions, owner-wallet continuity, capital/business factors, isolated activity and examples | “wallets that you own” | 2026-11-14 |
| [K02](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-mining-staking-activities.html) | Read for: Whole operative mining/staking definitions, earning and CEX-credit timing, business and equipment guidance | “credited to the taxpayer’s wallet” | 2026-11-14 |
| [K03](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/value-crypto.html) | Read for: Whole operative CAD valuation methods, inventory choices and both numerical tables; arithmetic and habitual-word conflicts recorded | “whichever is lower” | 2026-11-14 |
| [K04](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/books-records-crypto.html) | Read for: Whole operative transaction fields, platform exports, opening/closing units/cost and mining/retention paragraphs | “last taxation year” | 2026-11-14 |
| [K05](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/gst-hst-crypto-transactions.html) | Read for: Whole operative crypto payment, VPI, non-VPI, registration and mining/ITC paragraphs; not a complete GST return | “virtual payment instrument” | 2026-11-14 |
| [K06](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/notice324/mining-activities-in-respect-of-cryptoassets.html) | Read for: Notice324 opening through current definitions, effective dates, 188.2(2)-(5), mining groups, risk/compensation examples, imports/hosting and pre-2022 boundary; not the complete historical section | “February 5, 2022” | 2026-11-14 |
| [K07](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-188.2.html) | Read for: Entire operative ETA188.2(1)-(5), including all exception predicates and group/onward-recipient conditions | “deemed not to be a supply” | 2026-11-14 |
| [K08](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/crypto-assets-tax-obligations.html) | Read for: Whole operative CRA crypto asset categories and general tax obligations, including tokens, NFTs and stablecoins | “Utility tokens” | 2026-11-14 |
| [K09](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-3.html) | Read for: All operative ITA3(a)-(f), income sources, taxable gains/allowable losses and loss interaction | “taxable capital gains” | 2026-11-14 |
| [K10](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-9.html) | Read for: All operative ITA9(1)-(3), business/property profit and capital separation | “profit” | 2026-11-14 |
| [K11](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-10.html) | Read for: ITA10(1),(1.01),(2),(2.1), item lower-cost/FMV, adventure-cost and opening/continuity; neighbouring special inventory provisions read for boundaries, not a special-industry engine | “adventure or concern in the nature of trade” | 2026-11-14 |
| [K12](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-12.html) | Read for: ITA12(1)(c) interest received/receivable and express timing exclusions; no complete investment-accrual engine | “depending on the method regularly followed” | 2026-11-14 |
| [K13](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-18.html) | Read for: ITA18(1)(a)-(h), actual income-purpose, capital/exempt/reserve/personal limits; not whole section18 | “purpose of gaining or producing income” | 2026-11-14 |
| [K14](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.html) | Read for: All operative ITA38(a)-(c), ordinary half and specified gift/partnership exceptions | “taxable capital gain” | 2026-11-14 |
| [K15](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-39.html) | Read for: ITA39(1)(a) capital-versus-income definition and previous same-day capital-audit read of (b)/loss exclusions, reused as scoped NFT/entity boundary | “Meaning of capital gain and capital loss” | 2026-11-14 |
| [K16](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html) | Read for: ITA40(1)(a),(b) gain/loss/outlay formula and 40(2)(g) superficial, debt, personal and registered-plan denials; same-day prior capital-audit reading reused, current relevant paragraphs reread | “a superficial loss” | 2026-11-14 |
| [K17](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-47.html) | Read for: ITA47(1) full existing-pool/new-cost averaging and boundary to following bond subsection; not all special security rules | “Identical properties” | 2026-11-14 |
| [K18](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-52.html) | Read for: ITA52(1)(a)-(d) entire operative income-to-cost bridge, exclusion of amounts already added and residence/income predicates | “otherwise added to the cost” | 2026-11-14 |
| [K19](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-53.html) | Read for: ITA53(1)(f) entire substituted-owner adjustment and share reduction, with adjacent distinct provisions; not whole section53 | “substituted property” | 2026-11-14 |
| [K20](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-54.html) | Read for: ITA54 ACB/capital definitions and entire superficial-loss definition, exceptions and rights; prior same-day PUP/LPP definition reads reused for NFT referral only | “at the end of that period” | 2026-11-14 |
| [K21](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-69.html) | Read for: ITA69(1)(a)-(c), full ordinary gift/nonarm/beneficial ownership FMV rules and express override | “Except as expressly otherwise provided” | 2026-11-14 |
| [K22](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-70.html) | Read for: ITA70(5),(6),(6.2), capital FMV/default cost, residence, qualifying spouse/trust, vesting and election; neighbouring income/rights rules read for boundary only | “36 months” | 2026-11-14 |
| [K23](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-73.html) | Read for: ITA73(1),(1.01),(1.02), capital property, both-party residence, spouse/former-spouse/trust and elect-out conditions; not entire farm/estate transfer rules | “both the individual and the transferee are resident in Canada” | 2026-11-14 |
| [K24](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-128.1.html) | Read for: ITA128.1(1)(b),(c) immigration context and (4)(a.1),(b),(c), departure timing and exclusions/60-of-120 history; no complete departure return engine | “60 months” | 2026-11-14 |
| [K25](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-230.html) | Read for: Entire operative ITA230(1)-(8), adequate/electronic/last relevant year, late filing, appeals, demand and early-disposal conditions | “last taxation year” | 2026-11-14 |
| [K26](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-248.html) | Read for: ITA248 disposition definition opening, beneficial-ownership non-disposition and trust exceptions; 248(35)-(37) gift FMV/cost/intent/nonarm and exceptions, neighbouring antiavoidance; not whole definitions section | “less than three years” | 2026-11-14 |
| [K27](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-117.html) | Read for: ITA117(2) current ordinary federal rates/base thresholds; consolidated14% not incorrectly applied to2025 transition | “14%” | 2026-11-14 |
| [K28](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-117.1.html) | Read for: ITA117.1(1)-(4), indexation and rounding/current-year thresholds; no full benefit engine | “rounded” | 2026-11-14 |
| [K29](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-111.html) | Read for: ITA111(1)(a),(b) noncapital/netcapital time windows and prior same-day capital-audit actual loss-limit/inclusion adjustments; not full special-loss engine | “three taxation years immediately following” | 2026-11-14 |
| [K30](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html) | Read for: ITA150(1)(d) ordinary/business/cohabiting spouse, tax-shelter and death extensions, with capital-disposal filing trigger150(1.1) | “the following June 15” | 2026-11-14 |
| [K31](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-123.html) | Read for: ETA123 financial instrument categories and financial service full inclusions/exclusions; actual VPI definition and statutory exclusions. Not whole definitions section | “virtual payment instrument” | 2026-11-14 |
| [K32](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-153.html) | Read for: ETA153(1)-(3), money/nonmoney FMV, allocation and special barter context; not full valuation/place engine | “fair market value” | 2026-11-14 |
| [K33](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-148.html) | Read for: Entire operative ETA148(1)-(4) preceding-four-quarter/single-quarter threshold, associates, exceptions and excluded consideration; ordinary30k scope only | “four calendar quarters” | 2026-11-14 |
| [K34](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-165.html) | Read for: Entire operative ETA165(1)-(4), federal5%, additional participating tax, zero-rating and offshore boundary | “rate of 5%” | 2026-11-14 |
| [K35](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-169.html) | Read for: ETA169(1) full general ITC formula/use conditions and adjacent improvement allocation context; not all special ITC rules | “commercial activities” | 2026-11-14 |
| [K36](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-240.html) | Read for: ETA240(1) ordinary registration and listed exceptions, neighbouring special registrants for boundary; not full application/timing engine | “small supplier” | 2026-11-14 |
| [K37](https://laws-lois.justice.gc.ca/eng/regulations/c.r.c.,_c._945/page-30.html?wbdisable=true) | Read for: Actual ITR1800 adequate inventory detail and1801 permitted all-inventory FMV paragraphs on normal published page30; no guessed section URL | “1801” | 2026-11-14 |
| [K38](https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/adjustment-personal-income-tax-benefit-amounts.html) | Read for: Actual2026/2025 bracket thresholds and indexation table only, not whole credit/benefit list | “$58,523” | 2026-11-14 |
| [K39](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html) | Read for: Actual2025 T4037 bounded capital/proceeds/ACB/outlays, identical pool and crypto/gift/loss portions, same-day prior capital-audit reads reused and relevant formula/pool paragraphs reread; not whole guide | “Outlays and expenses” | 2026-11-14 |
| [K40](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/line-12700-capital-gains/capital-losses-deductions.html) | Read for: CRA capital losses opening/application/inclusion/carryback/forward sections and prior same-day superficial-loss/death/special boundary reads; not full ABIL engine | “three previous years” | 2026-11-14 |
| [K41](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s3/5000-s3-25e.pdf) | Read for: Actual2025 Schedule3 Part3 crypto row7 and complete columns/15200/15301, inclusion/12700 bridge from previous same-day audit; rendered/visually inspected page3 in this pass | “Crypto-assets” | 2026-11-14 |
| [K42](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/important-dates-individuals.html) | Read for: Actual2025 CRA filing/payment/June15 and death qualification dates; not all annual contribution deadlines | “April 30, 2026” | 2026-11-14 |
| [K43](https://www.canada.ca/en/services/taxes/resources-for-small-and-medium-businesses/2026-tax-deadlines-canadian-businesses-self-employed-individuals.html) | Read for: Actualpublished2027 self-employed filing/payment and tax-shelter qualification; URL2026 slug is stale but actual title/body are2027, not inferred fromURL | “April 30, 2027” | 2026-11-14 |
| [K44](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html) | Read for: Actual2026 CRA federal rate/threshold table, progressive and provincial-residence context; no independent provincial engine | “14%” | 2026-11-14 |
| [K45](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/last-year.html) | Read for: Actual2025 CRA federal rate/threshold table including annual14.5% and July1transition note, progressive and province context | “14.5%” | 2026-11-14 |
| [K46](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-r/5006-r-25e.pdf) | Read for: Actual2025 T1 total-income12100/12700/13000/13499/13500 and federal rate lines70-76; prior same-day rendered page6 reused; Ontario package does not select taxpayer province | “14.5%” | 2026-11-14 |
| [K47](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf) | Read for: Actual2025 T2125 title, separate-business instruction, identification/internet, Part3D opening/purchases/closing/COGS and Part4/5 net-income bridge; rendered/visually inspected page3. Not a new audit of all deductions/CCA | “For each business or profession” | 2026-11-14 |
| [K48](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/line-12100-interest-other-investment-income.html) | Read for: CRA12100 opening/investment and paid/credited versus annual-earned interest timing, not all securities special cases | “Interest and other investment income” | 2026-11-14 |
| [K49](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/line-13000-other-income.html) | Read for: CRA13000 opening residual-taxable-income instruction and specify-type rule; no inference every staking receipt belongs here | “not reported or should not be reported elsewhere” | 2026-11-14 |
| [K50](https://www.canada.ca/en/services/taxes/income-tax/personal-income-tax/how-file/tax-software/send-return/netfile.html) | Read for: Whole operative currentNETFILE/ReFILE years/window/method/restrictions, no future service guarantee or foreign domestic analysis | “in tax software” | 2026-11-14 |
| [K51](https://www.canada.ca/en/services/taxes/income-tax/personal-income-tax/how-file.html) | Read for: Whole current how-file options and prospectiveMarch2027 invitation-only prefilledCRA-account route | “Starting March 2027” | 2026-11-14 |
| [K52](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-251.1.html) | Read for: ITA251.1(1) actual spouse/control/partnership/trust affiliation opening and prior same-day full conditions reused for affiliate boundary | “affiliated persons” | 2026-11-14 |

Not yet confirmed: final 2026 annual Schedule 3/T2125/T1 field editions and filing opening; a universal official treatment of every airdrop, fork, wrapper, liquidity token, NFT or non-business-mining cost; case-specific foreign reporting/situs, donation credit, estate, CCA, treaty, provincial and entity results. These are explicit work items or referral boundaries, not computed results. The guessed archived IT-479R URL returned 404 and is not evidence. No change to a source file alone proves that the live MCP/database has imported it or that an accountant has approved the changed method.
