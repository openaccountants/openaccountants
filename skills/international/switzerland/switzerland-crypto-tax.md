---
name: switzerland-crypto-tax
description: Use this skill whenever asked about Switzerland cryptocurrency or digital asset taxation. Trigger on phrases like "crypto tax Switzerland", "Bitcoin Switzerland", "cryptocurrency gains Switzerland", "crypto income Switzerland", "staking Switzerland", "mining income Switzerland", "NFT tax Switzerland", "wealth tax crypto", "Vermögenssteuer crypto", "ESTV crypto", "Kursliste crypto", "Kreisschreiben 36", "professional trader crypto Switzerland", "gewerbsmässiger Handel", "Steuererklärung crypto", "Wertschriftenverzeichnis crypto", "canton crypto tax", "Zug crypto", "Swiss crypto valuation", "CARF Switzerland", or any question about the income tax, wealth tax, capital gains, or reporting treatment of cryptocurrency, tokens, or digital assets for Swiss tax residents. Covers tax-free capital gains for private investors, annual wealth tax, ESTV crypto valuations, Kreisschreiben Nr. 36 safe-haven criteria, professional trader classification, and cantonal variations. ALWAYS read this skill before touching any Switzerland crypto work.
version: 1.0
jurisdiction: CH
tax_year: 2026
last_updated: 2026-09-26
authored_by: OpenAccountants team
review_status: pending_review
trust_label: Written by the OpenAccountants team
depends_on:
  - switzerland-income-tax
category: crypto
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Switzerland: crypto-asset tax for individuals (tax year 2026, with 2025 returns)

## Scope

This Guide covers Swiss-resident individuals who hold, trade, stake, mine or receive crypto-assets. It covers tax year 2026 (the calendar year that is running now) and has a short dated section for the 2025 return that people are filing now.

It covers:

- income tax: private wealth management versus professional ("quasi") trading, under the ESTV criteria in Circular No. 36 (Kreisschreiben Nr. 36, KS 36);
- income from staking, mining, lending, airdrops and tokens paid as salary;
- the three token classes the ESTV uses: payment tokens, asset tokens and utility tokens;
- cantonal wealth tax on crypto at its 31 December value, using the ESTV price list (Kursliste / ICTax);
- VAT (MWST) on mining, staking and validation services;
- automatic exchange of information (CRS and CARF);
- record keeping.

It does not cover companies that issue tokens (ICO/ITO issuers), withholding tax and stamp duty planning for issuers, or cantonal tariffs. Wealth tax rates, allowances, filing deadlines and cantonal practice differ by canton. Where a canton's rule decides the answer, this Guide says so and refers you to the canton.

The ESTV's position is set out in its working paper on cryptocurrencies and ICOs/ITOs. The current edition replaces the version of 27 August 2019 and reflects the facts put to the ESTV up to the end of December 2020 ([ESTV working paper, "Kryptowährungen – Besteuerung"](https://www.estv.admin.ch/de/kryptowaehrungen-besteuerung)). The working paper states federal practice. Cantons apply the harmonised rules, but they may apply them differently in detail.

## Ask the client first

- **Canton and commune of residence on 31 December.** Wealth tax and the cantonal and communal income tax depend on them. If the canton is unknown, stop.
- **Every wallet and exchange account held on 31 December**, with the quantity of each token.
- **All disposals in the year**: date bought, date sold, purchase price and sale proceeds in CHF.
- **Securities and cash balances at 1 January**, the start of the tax period. KS 36's volume test uses this figure.
- **Borrowing**: margin, Lombard loans or any loan used to buy crypto, and the interest paid.
- **Derivatives**: futures, options or perpetual swaps, and whether they only hedged tokens the client owned.
- **Net income for the year** (Reineinkommen) from all other sources. Also ask whether trading gains pay living costs.
- **Income events**: staking rewards (pool or own validator?), mining, lending interest, airdrops, and tokens received as salary or fringe benefits. For each, get the date received and the CHF value at that time.
- **Tokens bought in an ICO/ITO**, with the token terms: repayment, profit share, or only a right to use a service.
- **Occupation**: whether the client works in finance or crypto, and whether they trade systematically (bots, full-time).
- **VAT registration**, if the client validates transactions for fees or runs a mining or staking service for others.
- **Losses, hacks or lost keys** during the year, with the evidence.

## The method, step by step

### Step 1: Classify each token

The ESTV sorts tokens into three basic classes, following FINMA's guidance. In the working paper's words: "Zahlungs-Token (vorher Payment-Token), Anlage-Token (vorher Asset-Token) und Nutzungs-Token (vorher Utility-Token)". Hybrid tokens exist. Treat each feature on its own merits ([ESTV working paper](https://www.estv.admin.ch/de/kryptowaehrungen-besteuerung)).

| Class | What it is | Income tax for a private holder | Wealth tax |
| --- | --- | --- | --- |
| Payment token (Zahlungs-Token), e.g. BTC | A pure digital means of payment. The issuer owes the holder nothing | Holding it produces no income. Buying and selling are treated like currency trades: gains are tax-free, losses are not deductible | Yes, at market value at the end of the tax period |
| Asset token, debt type (Fremdkapital-Token) | Repayment of all or most of the investment, and perhaps interest | Treated as a bond: interest (periodic or one-off) is taxable when realised. Trading gains are tax-free in private wealth | Yes, at market value |
| Asset token, contract-based (Anlage-Token mit vertraglicher Grundlage) | A share of a figure such as EBIT, revenue or licence income. No repayment | Payments are fully taxable as income from movable assets. There is no tax-free repayment of the capital, and a loss is a non-deductible capital loss | Yes, at market value (founders' tokens at least at the pre-sale price) |
| Asset token with participation rights (Beteiligungsrechte) | Tokenised shares or participation certificates | Taxed like shares. Check the working paper's section on these | Yes |
| Utility token (Nutzungs-Token) | Only a right to use a digital service | Trading gains in private wealth are tax-free, and losses are not deductible | Yes |

For every class the working paper adds that, depending on the "Art, Umfang und Finanzierung der Transaktionen" (the kind, scale and financing of the dealings), the activity may be self-employment rather than private wealth management. That is Step 2.

### Step 2: Private wealth management or professional trading (KS 36)

Capital gains on private wealth are tax-free under Art. 16 para. 3 DBG. Gains on business assets are self-employment income under Art. 18 DBG. The working paper applies the KS 36 criteria for securities dealing to tokens "analog" (by analogy). KS 36 is dated 27 July 2012 and still sits in the ESTV's list of current circulars ([KS 36](https://www.estv.admin.ch/dam/de/sd-web/oOz28af293pZ/dbst-ks-2012-1-036-d-de.pdf); [ESTV circulars list](https://www.estv.admin.ch/de/kreisschreiben-direkten-bundessteuer)).

**2a. Safe harbour (Vorprüfung).** The tax authorities always treat the activity as private wealth management "wenn die nachfolgenden Kriterien kumulativ erfüllt sind", that is, when all five of these are met:

| # | KS 36 criterion | How to test it |
| --- | --- | --- |
| 1 | The tokens sold were held for **at least 6 months** | Check the holding period for each disposal. Six months exactly passes |
| 2 | Transaction volume in the calendar year is **not more than five times** the securities and balances held at the start of the tax period | Volume = the sum of all purchase prices plus all sale proceeds. Exactly five times passes |
| 3 | Capital gains are not needed to replace missing or lost income for living costs | KS 36: this "ist regelmässig dann der Fall, wenn die realisierten Kapitalgewinne weniger als 50% des Reineinkommens in der Steuerperiode betragen". Measure the gains against net income. Do not add the tax-free gain to the net income figure |
| 4 | The investments are not debt-financed, **or** the taxable investment income (interest, dividends and similar) is greater than the share of debt interest | Most tokens pay no income, so any borrowing usually fails this test |
| 5 | Derivatives (especially options) are bought and sold only to hedge the client's own positions | Speculative futures or perpetuals fail it |

**2b. If any criterion fails**, professional trading is not proven. KS 36: "Sind diese Kriterien nicht kumulativ erfüllt, kann gewerbsmässiger Wertschriftenhandel nicht ausgeschlossen werden." Judge the case on all its facts, weighing the factors as the Federal Supreme Court does (2C_868/2008, 2C_766/2010, 2C_385/2011):

| Weight | Factor (KS 36, section 4.3.2) |
| --- | --- |
| Primary | Transaction volume: frequent trades and short holding periods. "Unter Umständen kann schon eine einzige Transaktion dazu führen" (in some cases a single transaction is enough) |
| Primary | Use of substantial borrowed money. KS 36 calls debt financing the strongest single indicator |
| Primary | Derivatives used beyond hedging, with large volume relative to total wealth |
| Secondary | A systematic, planned approach, including reinvesting gains in similar assets |
| Secondary | A close link to the client's job and use of specialist knowledge |

The secondary factors "begründen für sich alleine keine selbständige Erwerbstätigkeit" (do not make it self-employment on their own). They only reinforce a primary factor. Trades made by a bank or an adviser under a mandate count as the client's own. The test is applied year by year, usually when there is a disposal. The authorities give binding rulings only in clear cases.

**2c. Consequences.**

| Point | Private wealth management | Professional (self-employed) trading |
| --- | --- | --- |
| Gains on disposal | Tax-free | Taxable self-employment income (Art. 18 para. 2 DBG) |
| Losses | Not deductible | Deductible if booked. Without formal books, lists of assets, liabilities, income and expenses are required (KS 36, section 4.4) |
| Transaction costs | Costs of buying, switching or selling are not deductible | Deductible as business costs |
| Unused losses | None | Deductible in the seven following years, to the extent not already used (Step 7) |
| Debt interest | Private interest deductible only up to gross investment income plus CHF 50'000 (federal, KS 36 section 5.2) | Business interest deductible without that limit |
| Social security | None on gains | Self-employment income is also the base for AHV/IV/EO contributions. **Check** the rate and assessment with the cantonal compensation office: AHV sources are not on a host this Guide may cite |
| Records | Keep them to prove private status | Keep them 10 years (Step 7) |

### Step 3: Tax the income events at their value on receipt

The ESTV treats income as realised at inflow ("Zufluss"): when the benefit is received, or when a firm legal claim to it arises. Convert it to CHF at that moment ([ESTV working paper](https://www.estv.admin.ch/de/kryptowaehrungen-besteuerung)).

| Event | ESTV treatment | Legal basis cited by the ESTV |
| --- | --- | --- |
| Staking through a staking pool | "qualifiziert grundsätzlich als Ertrag aus beweglichem Vermögen": taxable income from movable assets at the value on receipt | Art. 20 para. 1 DBG |
| Staking as your own validator (no pool) | Check whether the validator is self-employed. If so, the rewards are self-employment income | Art. 18 para. 1 DBG |
| Mining (proof of work) | The reward is taxable income. If the general criteria for self-employment are met, it is self-employment income | Art. 16 para. 1 and Art. 18 para. 1 DBG |
| Airdrop (free allocation) | Taxable as income from movable assets at market value on the date of allocation | Working paper, section 2.2.2 |
| Lending or interest on tokens | The working paper does not deal with DeFi lending. Debt-type asset tokens pay interest that is taxed like bond interest. Treat lending interest as taxable investment income, and say that the point is unsettled | Art. 20 para. 1 DBG (by analogy); **check** with the canton |
| Salary or fringe benefits paid in tokens | Taxable employment income, shown on the salary certificate (section 1 or 3) at the value on receipt | Art. 17 para. 1 DBG |
| Holding payment tokens | "generiert in aller Regel keine Einkünfte" (normally produces no income) | Art. 16 para. 1 DBG, e contrario |

Costs directly linked to earning investment income and needed to manage the assets are deductible (Art. 32 para. 1 DBG). Transaction costs of buying, switching or selling are not.

### Step 4: Wealth tax at the 31 December value

The Confederation does not tax the wealth of individuals. Every canton and commune does. The base is total net wealth, and ESTV guidance names crypto expressly among the assets: "Der Vermögenssteuer unterliegen alle der steuerpflichtigen Person zustehenden unbeweglichen und beweglichen Vermögenswerte (inklusive Kryptowährungen)". Tariffs, rates and tax-free allowances are "Sache der Kantone" (a matter for the cantons) ([ESTV guide for new taxpayers](https://www.estv.admin.ch/dam/de/sd-web/5-fLbzigwEtn/estv-leitfaden-neue-steuerpflichtige-de.pdf)). Wealth is measured on the reference date, normally the end of the tax period or of tax liability.

Value each token in this order ([ESTV working paper](https://www.estv.admin.ch/de/kryptowaehrungen-besteuerung); [ESTV Kurslisten](https://www.estv.admin.ch/de/kurslisten-ictax)):

1. **ESTV price list (Kursliste / ICTax).** The ESTV publishes tax values for the most widely held cryptocurrencies. The ESTV says of its price-list rates: "Diese Kurse gelten als Steuerwert am 31. Dezember (Art. 14 und 17 Abs. 1 StHG)". Look up the value for the year in ICTax. **Check:** the ICTax database is on a host this Guide may not cite, so it quotes no token values.
2. **Not on the list:** use the market value on one of the leading trading platforms at the end of the tax period. Keep a screenshot or export.
3. **No current price can be found:** declare the token at its original purchase price converted into CHF.

Staked or locked tokens, and tokens on an exchange, are still the client's wealth. List every token in the securities schedule (Wertschriften- und Guthabenverzeichnis) with the quantity, the CHF value per unit and the total. A client who moved canton during the year, or who has property in another canton, faces intercantonal allocation. Refer that case to the cantons concerned.

### Step 5: VAT (MWST)

Most private holders are not VAT-registered, and nothing here changes that. It matters when a person runs validation, mining or staking as a service. ESTV practice is in VAT Info 04, section 2.7.3.5 ([MWST-Info 04, 2.7.3.5](https://www.gate.estv.admin.ch/mwst-webpublikationen/public/pages/displayDocs/cipherPrinterFriendly.xhtml?componentId=1479334&publicationId=1003047&cipherKeyDate=&language=de)):

| Activity | VAT treatment |
| --- | --- |
| Validation (mining or staking) paid **only** with a block reward | There is no supply ("kein Leistungsverhältnis"). The block reward is a non-consideration under Art. 18 para. 2 MWSTG. The activity is not entrepreneurial, which limits input tax recovery |
| Validation paid with a **transaction fee** from the sender | A taxable supply. For a recipient in Switzerland it is an electronic service taxed at the standard rate |
| A miner working in a mining pool | Supplies between the miner and the pool are relevant for VAT. The place of supply follows Art. 8 para. 1 MWSTG |
| A holder staking through a staking pool | Supplies between the pool and the participant are relevant for VAT. The place of supply follows Art. 8 para. 1 MWSTG |
| Running nodes (e.g. masternodes, cloud mining) for a third party | In principle a taxable service |
| Buying, selling or exchanging payment tokens | **Check.** No page on a host this Guide may cite confirms the exemption for exchanging payment tokens. Confirm the treatment with the ESTV before advising |

### Step 6: Automatic exchange of information

Switzerland exchanges financial account data under the Common Reporting Standard (CRS). The legal basis came into force on 1 January 2017, and the first exchange took place in 2018. Swiss financial institutions report to the ESTV within six months after the end of the calendar year ([ESTV, AIA](https://www.estv.admin.ch/de/automatischer-informationsaustausch-aia)). The ESTV says the revised CRS "in der Schweiz seit dem 1. Januar 2026 in Kraft ist" (has been in force in Switzerland since 1 January 2026) ([ESTV notice, 4 September 2026](https://www.estv.admin.ch/de/newnsb/b2F6VQ9fb0D6)).

**CARF (the Crypto-Asset Reporting Framework): check.** This Guide gives no Swiss start date for CARF reporting by crypto service providers. The enacted date is published by the State Secretariat for International Finance (SIF) and in the official compilation of federal law, and neither is on a host this Guide may cite. Do not tell a client a date until you have read it in the enacted text. What is certain: foreign tax authorities already receive CRS data, and crypto holdings must be declared whether or not anyone reports them.

### Step 7: Records and losses

- **Self-employed traders and miners.** The federal return guide for tax period 2026 says: "Die mit der selbstständigen Erwerbstätigkeit zusammenhängenden Urkunden und sonstigen Belege sind während 10 Jahren aufzubewahren." (Documents linked to self-employment must be kept for 10 years.) Attach the annual accounts (balance sheet and profit and loss account). If there are no formal books, attach at least lists of assets and liabilities, income and expenses, and private withdrawals and contributions ([Wegleitung 2026](https://www.estv.admin.ch/dam/it/sd-web/oQ0wWcDmCJTS/2a-2026-de.pdf)).
- **Loss carry-forward.** For tax period 2026, self-employed persons may deduct losses from the seven preceding business years (2019–2025), to the extent the losses were not already used in earlier years (same source).
- **Private investors.** Keep, for each year, the exchange statements, wallet addresses, the 31 December valuations with their source, the income events with their date and CHF value, and the full trade history. The trade history is the only evidence for the KS 36 holding period and volume tests. Without it, private status cannot be shown if the canton challenges it.

## Figures, with their years

| Figure | Value | Year | Source |
| --- | --- | --- | --- |
| KS 36 criterion 3 marker: realised gains below this share of net income | 50% | Applies each tax period, KS 36 of 27 July 2012 | [KS 36](https://www.estv.admin.ch/dam/de/sd-web/oOz28af293pZ/dbst-ks-2012-1-036-d-de.pdf) |
| KS 36 criterion 1: minimum holding period | 6 months | Same | Same |
| KS 36 criterion 2: maximum volume | 5 times the securities and balances at the start of the period | Same | Same |
| Federal cap on deductible private debt interest | Gross investment income plus CHF 50'000 | Current federal rule quoted in KS 36 | Same |
| Federal income tax on higher taxable incomes | A flat 11.5% of the whole taxable income | Tax period 2026 tariff | [Wegleitung 2026](https://www.estv.admin.ch/dam/it/sd-web/oQ0wWcDmCJTS/2a-2026-de.pdf) |
| Loss carry-forward for the self-employed | 7 preceding years (2019–2025 for 2026) | Tax period 2026 | Same |
| Retention of self-employment records | 10 years | Tax period 2026 | Same |
| Cantonal and communal income tax, wealth tax rates and allowances | Set by each canton | Each year | Refer to the canton |
| Kursliste values at 31 December | Published by the ESTV in ICTax | Each year | **Check** in ICTax |

## Boundaries and exceptions

| Situation | Rule | Source |
| --- | --- | --- |
| Holding period exactly 6 months | Passes criterion 1 ("mindestens 6 Monate") | KS 36 |
| Volume exactly five times the opening balance | Passes criterion 2 ("nicht mehr als das Fünffache") | KS 36 |
| Gains exactly equal to half of net income | Criterion 3 asks whether the gains are needed to cover living costs. The marker is "weniger als 50%", so exactly half does not meet the marker. Assess the need test on the facts, or treat the safe harbour as failed | KS 36 |
| Any loan in the portfolio | Criterion 4 fails unless taxable investment income exceeds the share of debt interest. Borrowing is the strongest indicator of trading | KS 36 |
| Safe harbour failed | No automatic reclassification. Weigh the primary and secondary factors | KS 36, section 4.3 |
| A single large trade | Can be enough for self-employment in some cases | KS 36, section 4.3.2 |
| Client waives the debt interest deduction | That alone does not make leveraged holdings private wealth | KS 36, section 4.3.2 |
| Inherited tokens | The deceased's classification (private or business) carries over to the heirs | KS 36, section 5.3 |
| Token with no current price | Declare at the original purchase price in CHF | ESTV working paper |
| Contract-based asset token that fails | A non-deductible capital loss. There is no tax-free repayment | ESTV working paper |
| Contract-based asset tokens given free to an employee | The difference to market value is a taxable fringe benefit. They are not employee participations under Art. 17a or 17b DBG | ESTV working paper |
| DeFi lending, liquidity pools, wrapped tokens, hard forks, NFTs, lost keys | No ESTV guidance on a host this Guide may cite. The general rules apply: private gains are tax-free, income on receipt is taxable, and wealth is measured at the year-end value. Refer anything beyond that | Refer |

## Worked cases

**Case 1: private investor, safe harbour met (tax year 2026).** The client lives in Zurich. On 1 January 2026 the securities and balances are CHF 200,000. During 2026 the client buys crypto for CHF 150,000 and sells for CHF 350,000. Every token sold was held for more than 6 months. There is no borrowing and there are no derivatives. The realised gain is CHF 48,000 and net income from other sources is CHF 120,000. ([KS 36](https://www.estv.admin.ch/dam/de/sd-web/oOz28af293pZ/dbst-ks-2012-1-036-d-de.pdf))
- Volume: CHF 150,000 + CHF 350,000 = CHF 500,000. The limit is five times CHF 200,000 = CHF 1,000,000. Pass. ([KS 36](https://www.estv.admin.ch/dam/de/sd-web/oOz28af293pZ/dbst-ks-2012-1-036-d-de.pdf))
- Gains ratio: CHF 48,000 / CHF 120,000 = 40%, below 50%. Pass. ([KS 36](https://www.estv.admin.ch/dam/de/sd-web/oOz28af293pZ/dbst-ks-2012-1-036-d-de.pdf))
- All five criteria are met, so the activity is private wealth management and the CHF 48,000 gain is tax-free. Holdings at 31 December go into the securities schedule for wealth tax. ([KS 36](https://www.estv.admin.ch/dam/de/sd-web/oOz28af293pZ/dbst-ks-2012-1-036-d-de.pdf))

**Case 2: wealth tax valuation.** The client holds 3 BTC on 31 December 2026. **Suppose** the ICTax tax value is CHF 70,000 per BTC (a hypothetical figure; look up the real one). The wealth tax value is 3 × CHF 70,000 = CHF 210,000. It is added to the client's other net wealth and taxed at the canton's tariff after the canton's allowance. ([ESTV Kurslisten](https://www.estv.admin.ch/de/kurslisten-ictax))

**Case 3: pool staking and an airdrop.** In 2026 the client receives staking rewards from a staking pool worth CHF 1,200 in total at the moments of receipt, and an airdrop worth CHF 500 on the day of allocation. Both are taxable income from movable assets: CHF 1,200 + CHF 500 = CHF 1,700 of taxable income. The reward tokens and airdropped tokens held at 31 December are also wealth. A later private sale of them is a tax-free capital gain. ([ESTV working paper](https://www.estv.admin.ch/de/kryptowaehrungen-besteuerung))

**Case 4: exactly at the volume limit.** Securities and balances at 1 January 2026 are CHF 100,000, and volume in 2026 is CHF 500,000. That is exactly five times, which is "not more than" five times, so criterion 2 passes. The other four criteria must still be checked. ([KS 36](https://www.estv.admin.ch/dam/de/sd-web/oOz28af293pZ/dbst-ks-2012-1-036-d-de.pdf))

**Case 5: leveraged day trader.** The client trades daily on margin, and positions last days. Criteria 1, 2 and 4 fail. Borrowing and volume are both primary factors, so the activity is very likely professional trading. Result: the gains are self-employment income, booked losses are deductible, unused losses carry forward seven years, and AHV/IV/EO contributions apply (**check** the rate with the compensation office). Federal tax on higher incomes is a flat 11.5%. Cantonal and communal tax come on top. ([Wegleitung 2026](https://www.estv.admin.ch/dam/it/sd-web/oQ0wWcDmCJTS/2a-2026-de.pdf))

**Case 6: solo miner and VAT.** A client mines alone and is paid only in block rewards. For VAT there is no supply, so no VAT is due on the rewards. The ESTV treats the activity as not entrepreneurial, and input tax on the equipment follows its VAT Info on input tax deduction for non-entrepreneurial activity. For income tax, the rewards are taxable income on receipt, and self-employment income if the general criteria are met.

## When to refuse or refer

- **Canton unknown**: stop. Wealth tax and most of the income tax depend on the canton.
- **Safe harbour failed and the facts point both ways**: say that professional trading cannot be excluded. Set out the primary factors and refer to a Swiss tax adviser, or suggest the client ask the canton for a ruling. The authorities give binding rulings only in clear cases.
- **Anything needing a cantonal figure or practice**: rates, allowances, deadlines, the canton's view on mining scale, DeFi, NFTs, or valuing illiquid tokens. Refer to the canton's tax administration.
- **CARF start date, AHV rates, Kursliste values and the VAT exemption for exchanging payment tokens**: this Guide cannot cite them. Say "check" and name the official place to look (SIF and the federal law compilation, the compensation office, ICTax, the ESTV VAT division).
- **Issuers of tokens (ICO/ITO), foundations and companies**: out of scope.
- **Undeclared crypto from earlier years**: whether a voluntary disclosure (Selbstanzeige) meets the legal conditions is decided by the cantonal tax administration ([ESTV, AIA](https://www.estv.admin.ch/de/automatischer-informationsaustausch-aia)). Refer the client to a Swiss tax adviser before anything is filed.
- **Moving into or out of Switzerland during the year, or tax in two cantons**: refer.

## Filing and payment

- **Who files**: every taxpayer files one return each year. With present-year assessment (Gegenwartsbemessung) the income of the calendar year is taxed. The return must be completed truthfully and in full and filed on time. The return is filed with the canton of residence ([ESTV guide for new taxpayers](https://www.estv.admin.ch/dam/de/sd-web/5-fLbzigwEtn/estv-leitfaden-neue-steuerpflichtige-de.pdf)).
- **Deadline**: set by the canton and printed on the form. Where the ESTV guide describes the procedure, it says the period is "in der Regel 30 Tage". An extension can be requested before the deadline expires. A taxpayer who is reminded and still does not file, or files incomplete returns repeatedly, is assessed at discretion and fined (same source). Look up the canton's actual date and extension practice.
- **Where crypto goes on the return**: holdings in the securities schedule at the 31 December value; income from staking, airdrops and lending as investment income; mining or trading income as self-employment income with the accounts attached; token salary as employment income from the salary certificate.
- **Payment**: the canton sets the instalment and interest rules. Refer to the canton.

### The 2025 return being filed now (dated section)

- The rules above apply to tax period 2025 in the same way: the working paper, KS 36 and the valuation order were the same in 2025.
- Value holdings at 31 December 2025 with the ICTax values for 2025 (**check** them in ICTax; this Guide does not quote them).
- Test KS 36 against the balances at 1 January 2025, the 2025 trades and 2025 net income.
- For the self-employed, the seven-year loss carry-forward covers the seven business years before 2025. The 2026 federal return guide lists 2019–2025 for tax period 2026. Use the 2025 return guide for the 2025 range.
- The revised CRS has been in force in Switzerland since 1 January 2026. CARF: **check**, as in Step 6.

## Completion checklist

- [ ] Canton and commune at 31 December confirmed
- [ ] Every token classified: payment, asset (debt, contract-based, participation) or utility
- [ ] All five KS 36 criteria tested with the numbers: holding period, volume against the opening balance, gains against net income, borrowing, derivatives
- [ ] If the safe harbour fails, primary and secondary factors weighed and written down
- [ ] Income events listed with their date, CHF value on receipt and legal characterisation (pool staking, own validator, mining, airdrop, lending, salary)
- [ ] Every 31 December holding valued: ICTax first, then a leading platform, then the original cost in CHF
- [ ] Securities schedule completed with quantity, unit value and total
- [ ] Professional case: accounts or lists attached, losses booked, carry-forward tracked, AHV flagged "check"
- [ ] VAT considered for validation, pool or node services
- [ ] Items marked "check" (CARF date, AHV rate, ICTax values, VAT exemption on exchanges) either confirmed from the official source or left open in the advice
- [ ] Records kept: 10 years for the self-employed, and the full trade history for private investors

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
