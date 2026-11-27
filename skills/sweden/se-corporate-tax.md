---
name: se-corporate-tax
description: "Swedish corporate income tax (bolagsskatt) for aktiebolag, ekonomiska föreningar and other legal persons resident in Sweden, and for foreign companies with a permanent establishment (fast driftställe) in Sweden. Covers the 20.6% rate under Inkomstskattelagen 65 kap. 10 §, the taxable base, periodiseringsfond (25%, six years, schablonintäkt), inventarier depreciation, tax-exempt dividends and gains on näringsbetingade andelar, the interest limitation rule (30% of tax EBITDA, SEK 5 million), loss carry-forward and the ownership-change restrictions, koncernbidrag, Inkomstdeklaration 2 deadlines, preliminärskatt, kostnadsränta, förseningsavgift, skattetillägg and kupongskatt. Tax year 2026. Trigger on: bolagsskatt, Swedish corporate tax, aktiebolag tax, INK2, periodiseringsfond, koncernbidrag, näringsbetingade andelar, ränteavdragsbegränsning, underskottsavdrag, kupongskatt. Out of scope: sole traders (se-income-tax), egenavgifter (se-social-contributions), payroll (sweden-payroll), VAT (sweden-vat-return), individual capital gains (se-capital-gains)."
version: 0.5
jurisdiction: SE
tax_year: 2026
last_updated: 2026-11-27
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: corporate-tax
type: computation
---

# Sweden: corporate income tax (bolagsskatt), tax year 2026

> **General reference only.** Not yet approved by an accountant. Do not rely on it to file, pay or take a tax position without review by a qualified professional in Sweden.

Ordinary Swedish corporate income tax is 20.6% of taxable income. Legal persons pay state income tax on business income, rather than municipal income tax (IL 1 kap. 3 §; 65 kap. 10 §). Separate Pillar Two rules can apply to large groups; the ordinary rate does not settle that liability. The law is Inkomstskattelagen (1999:1229), “IL” below; procedure is in Skatteförfarandelagen (2011:1244), “SFL”. Amounts are in Swedish kronor (SEK).

Before computing, obtain the financial-year dates, accounts and tax adjustments, opening losses and allocation reserves by year, ownership history, shareholdings, group relationships and net interest. The ordinary calculations below do not decide a point explicitly held for an accountant.
See also, in this pack: `se-income-tax` (enskild firma), `se-social-contributions` (egenavgifter), `sweden-payroll` (employer contributions and PAYE), `sweden-vat-return` (moms), `se-capital-gains` (individuals), `sweden-bookkeeping` (K2/K3, BAS accounts).

## Who this applies to

- **Resident companies.** A legal person is fully taxable in Sweden (obegränsat skattskyldig) if it is a Swedish legal person by registration or, if not registered, by the seat of its board or a similar factor (IL 6 kap. 3 §). It is taxed on all its income from Sweden and abroad (IL 6 kap. 4 §). In practice: aktiebolag (AB), ekonomiska föreningar, and taxable foundations and associations.
- **Foreign companies.** A foreign legal person has limited tax liability (begränsat skattskyldig) (IL 6 kap. 7 §). It pays Swedish tax on income from a permanent establishment (fast driftställe) or real property in Sweden, and on a short list of other items such as reversed periodiseringsfond deductions (IL 6 kap. 11 §). The complete taxable-income list is in IL 6 kap. 11 §; this is not an exhaustive list. Royalty exemptions and treaty outcomes are held below.
- **Out of scope here.** Handelsbolag and kommanditbolag are not taxed themselves; their partners are (IL 5 kap.). Swedish värdepappersfonder and specialfonder are not taxable on income from assets in the fund (IL 6 kap. 5 §). Investmentföretag, privatbostadsföretag, foundations and non-profit associations with exemptions (IL 7 kap.), shipping tonnage tax and life insurance are outside this ordinary computation. Check this point with one of our partner accountants.

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| Corporate income tax (statlig inkomstskatt for juridiska personer) | 20.6% of taxable income | 2026 | IL 65 kap. 10 §, https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/inkomstskattelag-19991229_sfs-1999-1229/ ; Skatteverket, Belopp och procent inkomstår 2026 |
| Rounding of taxable income | Down to the nearest SEK 10 | 2026 | IL 1 kap. 7 §, https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/inkomstskattelag-19991229_sfs-1999-1229/ |
| Municipal or local tax on company profit | None. Legal persons pay only state income tax on business income | 2026 | IL 1 kap. 3 § second paragraph, https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/inkomstskattelag-19991229_sfs-1999-1229/ |
| Small-company rate or minimum tax | No separate small-company band in IL 65 kap. 10 §; separate Pillar Two scope must still be screened | 2026 | IL 65 kap. 10 §, https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/inkomstskattelag-19991229_sfs-1999-1229/ |
| Periodiseringsfond (tax allocation reserve) | Up to 25% of taxable business surplus after earlier losses and reserve reversals, before this allocation; AB must book it | 2026 | IL 30 kap. 5 §; Skatteverket, Periodiseringsfond, https://www.skatteverket.se/foretag/drivaforetag/foretagsformer/aktiebolag/periodiseringsfond.4.4887341d16e1e2b8ddf30e.html |
| Periodiseringsfond reversal | By the sixth tax year after the allocation (2026 allocations by 2032) | 2026 | IL 30 kap. 7 §; Skatteverket, Belopp och procent inkomstår 2026, https://www.skatteverket.se/privat/skatter/beloppochprocent/2026.4.1522bf3f19aea8075ba21.html |
| Uplift on reversal of old periodiseringsfonder | 106% of the allocation for funds allocated in tax years beginning before 1 January 2019; 104% for tax years beginning 1 January 2019 to 31 December 2020; 100% for later funds (reversals in tax years beginning after 31 December 2020) | 2026 | Transitional rule 5 to SFS 2018:1206 (IL); Skatteverket, Periodiseringsfond, https://www.skatteverket.se/foretag/drivaforetag/foretagsformer/aktiebolag/periodiseringsfond.4.4887341d16e1e2b8ddf30e.html |
| Schablonintäkt on periodiseringsfonder | Statslåneränta at end of November of the prior year (2.55% at 30 November 2025, floor 0.5%) times opening funds; proportionately adjust for a tax year shorter or longer than twelve months | Tax years ending in 2026 | IL 30 kap. 6 a §; Skatteverket, Periodiseringsfond, https://www.skatteverket.se/foretag/drivaforetag/foretagsformer/aktiebolag/periodiseringsfond.4.4887341d16e1e2b8ddf30e.html |
| Inventarier (machinery and equipment) | Main rule up to 30% of adjusted depreciation basis with matching year-end depreciation; supplementary rule uses 20% annual acquisition-cost reduction; residual method up to 25%; adjust main/residual limits for non-twelve-month years | 2026 | IL 18 kap. 13 §, 17 §, https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/inkomstskattelag-19991229_sfs-1999-1229/ |
| Immediate write-off of low-value equipment | Acquisition cost excluding VAT below half a prisbasbelopp: below SEK 29,600 (derived: 59,200 ÷ 2); aggregate naturally connected items and larger equipment purchases; excludes IL 18 kap. 1 § second-paragraph rights | 2026 | IL 18 kap. 4 §; Skatteverket, Belopp och procent inkomstår 2026, https://www.skatteverket.se/privat/skatter/beloppochprocent/2026.4.1522bf3f19aea8075ba21.html |
| Interest limitation | Otherwise deductible negative net interest: up to 30% of statutory tax basis, or fem miljoner kronor (SEK 5 million) shared by the statutory intressegemenskap; same-filing-time open allocation required | 2026 | IL 24 kap. 24-25 §§, https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/inkomstskattelag-19991229_sfs-1999-1229/ |
| Carry-forward of disallowed net interest | Six years | 2026 | IL 24 kap. 26 §, https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/inkomstskattelag-19991229_sfs-1999-1229/ |
| Group contributions (koncernbidrag) | Parent must own more than 90% of the shares | 2026 | IL 35 kap. 2-3 §§, https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/inkomstskattelag-19991229_sfs-1999-1229/ |
| Loss restriction after a change of control (beloppsspärr) | Where the beloppsspärr applies, old losses above 300% of adjusted acquisition expenditure are forfeited; ownership changes after 31 December 2024; see exceptions below | 2026 | IL 40 kap. 15 §; transitional rules to SFS 2024:1131, https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/inkomstskattelag-19991229_sfs-1999-1229/ |
| Group-contribution block (koncernbidragsspärr) | Where the block applies, restricted profit basis through the fifth tax year after the change year; qualifying pre-existing-group contributions can count; see below | 2026 | IL 40 kap. 18 §, https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/inkomstskattelag-19991229_sfs-1999-1229/ |
| Kupongskatt (dividend withholding tax) | 30% of the dividend | 2026 | Kupongskattelagen (1970:624) 5 §, https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/kupongskattelag-1970624_sfs-1970-624/ |
| Preliminary tax (F-skatt) by default | 110% of latest final tax, or 105% if it was below originally charged preliminary tax; not below latest charged preliminary tax; estimate route below | 2026 | SFL 55 kap. 3 §, https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/skatteforfarandelag-20111244_sfs-2011-1244/ |
| Pillar Two | Initial scope screen (not clearance of special group structures): at least EUR 750 million consolidated revenue in at least two of the four preceding financial years; proportionately adjust threshold for non-twelve-month years; excluded entities excepted. Computation and separate return are held for an accountant | 2026 | Lag (2023:875), https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-2023875-om-tillaggsskatt_sfs-2023-875/ |
| Gift tax reduction for legal persons (skattereduktion för gåvor) | 20.6% of qualifying money gifts to a Skatteverket-approved recipient for social help or scientific research; at least SEK 2,000 per gift; basis at most SEK 800,000 a calendar year | Gifts from calendar year 2026 | https://www.skatteverket.se/foretag/skatterochavdrag/gavortillideellaverksamheter.4.1522bf3f19aea8075ba3df3.html |
| Pension cost deduction cap per employee | Ordinary rule for qualifying secured pension promises: 35% of pensionable pay for this or the preceding tax year, capped at 10 prisbasbelopp: SEK 592,000 (derived: 10 × 59,200). Supplementary-rule cases held below | 2026 | IL 28 kap. 5-6 §§, https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/inkomstskattelag-19991229_sfs-1999-1229/ ; prisbasbelopp https://www.skatteverket.se/privat/skatter/beloppochprocent/2026.4.1522bf3f19aea8075ba21.html |
| Finance leases outside IL 24 a kap. | Total financial-lease charges of the company and its intressegemenskap below SEK 1 million (en miljon kronor) for the tax year | 2026 | IL 24 a kap. 2 §, https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/inkomstskattelag-19991229_sfs-1999-1229/ |
| Inventory valued at the 97% alternative | At least 97% of the total acquisition cost; not for property and similar assets; shares, bonds, loan receivables and similar assets; electricity certificates; emission allowances, emission-reduction units or certified emission reductions | 2026 | IL 17 kap. 4 §, https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/inkomstskattelag-19991229_sfs-1999-1229/ |

## The taxable base

Start from the profit before tax in the annual accounts. Taxable income is the surplus in the business income category (näringsverksamhet), less any general deductions, rounded down to the nearest SEK 10 (IL 1 kap. 7 §).

**Add back (main items).**
- Swedish income tax and kupongskatt booked as an expense (IL 9 kap. 4 §).
- Fines and public-law sanction charges (IL 9 kap. 9 §), bribes (IL 9 kap. 10 §), and kostnadsränta on the tax account (IL 9 kap. 8 §).
- Gifts and the company's own living-type costs (IL 9 kap. 2 §).
- Representation without an immediate business connection or beyond a reasonable amount. Food is deductible only for refreshments or other simple food of small value that is not a meal (IL 16 kap. 2 §).
- Capital losses on näringsbetingade andelar are not deductible when a gain would have been tax-free (IL 25 a kap. 5 § second paragraph).
- Gifts remain non-deductible even if a separate gift tax reduction is available. For gifts from calendar year 2026, an ordinary income-tax-paying AB can request a reduction of 20.6% of qualifying money gifts, each at least SEK 2,000, for social help or scientific research to a recipient approved at the gift date. Calendar-year basis is capped at SEK 800,000 (maximum reduction SEK 164,800, derived); it offsets available state income tax only; unused basis cannot be carried into a later year. Request it in the income return due next after that calendar year. Entities covered by IL 7 kap. exemptions do not qualify. Commission-agent structures, partnerships and estates are outside this AB calculation: Check this point with one of our partner accountants. (IL 9 kap. 2 §; 67 kap. 2, 21, 23, 24 a, 25 a, 26 a §§; SFS 2025:1361 transitional rule 4.)
- Pension promises must be secured in a qualifying way under IL 28 kap. 3 §. The ordinary deduction under 5–6 §§ is at most 35% of the employee's pensionable contractual pay for this or the previous tax year, and at most 10 prisbasbelopp (SEK 592,000 for 2026, derived). The supplementary rule and other securing arrangements are a non-usable hold: Check this point with one of our partner accountants. For the separate payroll-tax topic, load `sweden-payroll`.

**Deduct or exclude (main items).**
- **Dividends on näringsbetingade andelar.** For an ordinary Swedish AB or economic association that is not an investmentföretag, a capital-asset share qualifies if unlisted, or the holding has at least 10% of votes, or it is required by the owner's or a closely connected company's business. Privatbostadsföretag shares do not qualify (IL 24 kap. 32–33 §§). Dividends are normally excluded, subject to the investment-company, deductible-foreign-dividend and hybrid exceptions in 38–39 §§ and 24 b kap. 7 §. A listed share sold or ceasing to qualify within one year triggers dividend taxation in that later year (40–42 §§). Exception cases, other eligible owner types and the EU capital-holding route under 34 and 36 §§ are a non-usable hold: Check this point with one of our partner accountants.
- **Capital gains and losses.** For the same eligible owners, qualifying-share gains are normally excluded, with the shell-company exception reserved. Listed shares must have qualified continuously for the year immediately before disposal. A loss is deductible only if a corresponding gain would be taxable, ignoring shell-company taxation for that comparison (IL 25 a kap. 3, 5–8 §§). Shell-company and related-right cases: Check this point with one of our partner accountants.
- **Depreciation.** For ordinary machinery/equipment, use the adjusted basis in IL 18 kap. 13 §: opening book value (accounts-linked method) or tax value (residual method), plus acquisitions still held at year end, minus the special deductions under 15–16 §§. Maximum annual deductions are 30% and 25% respectively, proportionately adjusted for a short or long year. The accounts-linked method requires orderly bookkeeping, year-end accounts and matching depreciation. Its supplementary rule permits a closing tax value based on acquisition cost less 20% annual depreciation (17 §).
- **Immediate equipment deduction.** Cost excluding VAT below half the 2026 prisbasbelopp is below SEK 29,600 (derived). Alternatively, economic life can be at most three years. Aggregate naturally connected items and acquisitions forming a larger equipment purchase for the low-value test; the rights listed in IL 18 kap. 1 § second paragraph are excluded (4 §).
- **Överavskrivningar and buildings.** An extra deduction under the accounts-linked method must correspond to year-end depreciation (IL 18 kap. 14 §); do not deduct an unbooked excess. Entries for accumulated excess depreciation and building-specific depreciation under IL 19 kap. are a non-usable hold: Check this point with one of our partner accountants.
- **Periodiseringsfond.** A legal person may deduct up to 25% of the business surplus before the allocation (IL 30 kap. 5 §). The allocation must also be booked in the accounts (IL 30 kap. 3 §). Each year's allocation is a separate fund, reversed oldest first, by the sixth tax year after the allocation at the latest (IL 30 kap. 4 §, 7 §). Earlier reversal is required on cessation of business, a liquidation decision or bankruptcy. Mergers, loss of Swedish tax liability, foreign moves and fund transfers require the exceptions in IL 30 kap. 8 and 14 §§ and are held for individual review: Check this point with one of our partner accountants. Each year the company adds a schablonintäkt (deemed income): the statslåneränta at the end of November of the year before the tax year ends, at least 0.5%, times the funds held at the start of the tax year (IL 30 kap. 6 a §). For a twelve-month tax year ending in 2026 the rate is 2.55%; proportionately adjust deemed income for shorter or longer tax years. Funds allocated when the corporate rate was higher are reversed with an uplift: 106% for allocations in tax years beginning before 1 January 2019 and 104% for tax years beginning in 2019 or 2020 (transitional rule 5 to SFS 2018:1206). A fund from tax year 2020 reversed in 2026 is therefore taxed at 104% of the amount set aside.

**Interest limitation (IL 24 kap. 21–29 §§).** Negative net interest is otherwise deductible interest expense less taxable interest income, when positive. Ordinary deductions are limited to 30% of the statutory avdragsunderlag. Alternatively, the SEK 5,000,000 simplification limit is shared by the entire intressegemenskap defined in 22 §; disclose the allocation openly in returns with the same filing time (24 §).

Compute the basis under 25 §, before this restriction and before old net-interest deductions: add otherwise deductible interest, specified depreciation and special building/land deductions, and the allocation-reserve deduction; subtract interest income, partnership-profit shares and reserve reversals. A loss before restriction can require an add-back of earlier-year losses, capped at that pre-restriction loss. This is a tax basis, not book EBITDA. Interactions with group-contribution-blocked losses, cooperative dividend deductions, intragroup debt (including the EEA artificial-arrangement rule from years beginning after 31 December 2025), and EU-listed non-cooperative lender jurisdictions are a non-usable hold: Check this point with one of our partner accountants.

Net interest left under the EBITDA rule or its statutory adjustment may be used within six years, oldest first, only within unused current deduction space after current net interest. The simplification route does not itself create such a carry-forward (26 §). A corporate acquisition of control normally extinguishes old net interest, but not an acquisition within the same pre-existing group; resolution exceptions are held (27 §). Check this point with one of our partner accountants before applying an ownership-change exception.

**Losses (IL 40 kap.).** Earlier business losses are deducted in the next year under 2 §, subject to restrictions; do not assume that no ownership change means every loss is available. Carry-back, bankruptcy, debt reduction and reorganisations are a non-usable hold: Check this point with one of our partner accountants.

For ownership changes after 31 December 2024 where the beloppsspärr applies, old losses exceeding 300% of adjusted acquisition expenditure are forfeited (15 §; SFS 2024:1131). Capital contributions and multiple acquired loss companies affect that expenditure/allocation (15 a–16 §§). It is not automatically three times the headline purchase price. Determine the trigger under 10–14 §§ first: control acquisitions, same-group exceptions, specified individual acquirers and aggregation of acquisitions can differ. Acquisitions of at least 20% of votes by each relevant acquirer, together exceeding 50% over at most three successive loss-company tax years, are one trigger under 12 §; inheritance/family and prior-control exceptions are in 13 §. Complex triggers are held: Check this point with one of our partner accountants.

Where the koncernbidragsspärr applies, it lasts through the fifth tax year after the change year. The statutory profit basis excludes restricted group contributions, but qualifying contributions from the pre-existing group can count; indirect new-group contributions and certain mergers prevent that exception (18–19 §§). Interaction with net-interest restrictions is held. If old losses were the predominant reason for an ownership change covered by 10–13 §§, the entire right to old losses ends (17 a §). Check this point with one of our partner accountants for a restricted-loss computation.

**Group contributions (koncernbidrag, IL 35 kap. 1–3 §§).** For an ordinary Swedish parent/subsidiary contribution, more than 90% ownership is required for both parties' whole tax years, or since the subsidiary began any business. Neither party may be an investmentföretag or privatbostadsföretag. Show the contribution openly in returns with the same filing time, and transfer corresponding value by the payer's return deadline. The recipient must not be treaty-resident abroad, subject to the specific EEA exception, and the relevant business must not be treaty-exempt in Sweden. An upstream contribution also requires that the subsidiary's dividend would not be taxed at the parent. Qualifying contributions are deductible to the payer and taxable to the recipient. Sister-company, EEA, merger/intermediary and final-loss koncernavdrag routes under IL 35 a kap. are held: Check this point with one of our partner accountants.

## Deadlines and filing

- **Return.** Inkomstdeklaration 2 (INK2) for aktiebolag and ekonomiska föreningar. One return per financial year (räkenskapsår).
- **Filing deadline** (SFL 32 kap. 2 §, and one month later when filed electronically). Skatteverket's dates for financial years ending in 2026:

| Financial year ends | File by (electronic filing) |
|---|---|
| January to April 2026 | 1 December 2026 |
| May to June 2026 | 15 January 2027 |
| July to August 2026 | 1 April 2027 |
| September to December 2026 | 2 August 2027 |

- **Preliminary tax.** Normally a decision is made by the 20th of the first tax-year month; a later-arising liability is decided as soon as possible. Tax below SEK 2,400 for the year is not charged (SFL 55 kap. 2 §). The default is 110% of latest final tax, or 105% if that final tax was below originally charged preliminary tax; the standard calculation cannot fall below latest charged preliminary tax (3 §). An initial preliminary income return/no prior final tax, or an estimate giving a material improvement, permits the estimate route (4 §).
- **Instalments.** Normally equal monthly amounts from the second tax-year month to the month after year end: the 12th, or 17th in January/August. August is instead the 12th when the statutory annual VAT basis excluding intra-EU acquisitions and imports exceeds SEK 40 million. Follow adjusted due dates in the decision (SFL 62 kap. 4 §). A three-month start deferral requires a request; it is unavailable for a post-year-end decision, acquired business, someone already trading, or special contrary reasons (7 §). Late decisions and seasonal schedules are held: Check this point with one of our partner accountants.
- **Top-up and final payment.** Kostnadsränta runs on unpaid final tax from the 13th of the second month after the financial year ends. Amounts up to SEK 30,000 carry no interest until the 3rd of the fifth month (SFL 65 kap. 4 § second paragraph, 6 §). For a calendar year 2026, pay a top-up (fyllnadsinbetalning) above SEK 30,000 by 12 February 2027, and up to SEK 30,000 by 3 May 2027, to avoid interest. Any remaining kvarskatt is due on the first statutory due date after 90 days have passed from the final tax decision (SFL 62 kap. 8 §).
- **Channel and form.** For an ordinary AB, submit the first page plus INK2R (accounts) and INK2S (tax adjustments), with applicable schedules. Use accounting software, Filöverföring, or the full-return service **Inkomstdeklaration 2, 3 och 4**. Complete the return, submit it, have the authorised representative sign on Mina sidor, and retain the receipt. The older **Inkomstdeklaration 2** service handles only the first page and closes on 29 December 2026; other parts must be sent separately on paper if using that old route. It is open for January–August 2026 year ends until then. Do not confuse its closure with the filing deadline. See the linked Skatteverket filing instructions in Sources.
- **Pillar Two.** The ordinary INK2 does not resolve top-up-tax calculations or separate return/report obligations. Non-usable hold: Check this point with one of our partner accountants.

## Penalties and interest

- **Late filing (förseningsavgift).** SEK 6,250 for an aktiebolag or ekonomisk förening return (SFL 48 kap. 6 §). A second fee is charged if the return is still missing three months after the deadline, and a third after a further two months (SFL 48 kap. 7 §). For these counts the one-month extension for electronic filing is ignored. Tilläggsskattedeklaration: SEK 25,000.
- **Incorrect return (skattetillägg).** 40% of the tax that would have been avoided (SFL 49 kap. 11 §); 10% for a final-tax timing error (SFL 49 kap. 13 §). A correction genuinely on the company’s own initiative avoids the surcharge; after an announced general control, a connected correction made more than two months after the announcement month is not treated as voluntary (SFL 49 kap. 10 §). Reconciliation-data, insignificant-tax and other statutory exclusions apply; unreasonable fees can be fully or partly remitted under SFL 51 kap. 1 §. Loss-only errors and contested penalties are held: Check this point with one of our partner accountants.
- **Interest (kostnadsränta).** Based on the basränta, set from 125% of the six-month treasury bill rate with a floor of 1.25% (SFL 65 kap. 3 §). Low kostnadsränta equals the basränta; payment after the due date carries basränta plus 15 percentage points until enforcement registration, then basränta (SFL 65 kap. 4 §, 13 §). Skatteverket's rates from 1 December 2024, still shown as current on 2026-11-27: basränta 2.5%, low kostnadsränta 2.5%, high kostnadsränta 17.5%, intäktsränta 1.125%. Kostnadsränta is not deductible (IL 9 kap. 8 §).

## Cross-border points

- **Dividends paid abroad.** The domestic kupongskatt rate is 30% for covered non-resident recipients where the dividend is not attributable to a Swedish permanent establishment (Kupongskattelagen 4–5 §§). EU parent-company, qualifying foreign-company and fund exemptions, anti-abuse conditions, treaty reductions and refunds must be settled before withholding. Non-usable hold for those outcomes: Check this point with one of our partner accountants.
- **Interest.** There is no general separate Swedish withholding tax on ordinary interest paid to a foreign company; this does not exempt interest attributable to its Swedish permanent establishment (IL 6 kap. 11 §).
- **Royalties and EU directives.** A royalty or periodic payment for use of tangible/intangible assets from business with a Swedish permanent establishment is treated as Swedish PE income under IL 6 kap. 11 §. The EU royalty exemption in IL 6 a kap., treaty relief, and the Parent-Subsidiary routes in IL 24 kap. 34 and 36 §§ require individual conditions. Non-usable hold: Check this point with one of our partner accountants.
- **CFC rules (IL 39 a kap.).** Ownership, low-tax testing, white-list restrictions and the EEA genuine-establishment exception are a non-usable hold; do not infer exemption from a jurisdiction alone. Check this point with one of our partner accountants.
- **Exit tax and reserve reversals.** Withdrawal valuation, EU/EEA recovery-assistance conditions, yearly deferral applications and the payment schedule under IL 22 kap., IL 30 kap. 8 § and SFL 63 kap. are a non-usable hold. Check this point with one of our partner accountants.

## Worked examples

**Example 1: a simple trading AB, calendar year 2026.** Norrsken Konsult AB has a profit before tax of SEK 2,400,000. The accounts include SEK 16,000 of client meals (not deductible under IL 16 kap. 2 §) and an SEK 8,000 sanction charge (not deductible under IL 9 kap. 9 §). It has no earlier periodiseringsfonder and no losses. It allocates the maximum 25% to a periodiseringsfond and books it in the accounts. Taxable income is SEK 1,818,000 and tax at 20.6% is SEK 374,508. The company paid F-skatt of SEK 30,000 a month from February 2026 to January 2027, SEK 360,000 in total. The balance of SEK 14,508 is below SEK 30,000, so no kostnadsränta arises if it is on the tax account by 3 May 2027.

```oa-check
name: SE example 1, trading AB with 25% periodiseringsfond, calendar 2026
inputs:
  profit_before_tax: 2400000
  meals: 16000
  sanction_charge: 8000
  monthly_f_tax: 30000
steps:
  - surplus_before_pfond: profit_before_tax + meals + sanction_charge
  - pfond: surplus_before_pfond * 0.25
  - taxable: floor((surplus_before_pfond - pfond) / 10) * 10
  - tax: taxable * 0.206
  - f_tax_paid: monthly_f_tax * 12
  - balance_due: tax - f_tax_paid
expected:
  surplus_before_pfond: 2424000
  pfond: 606000
  taxable: 1818000
  tax: 374508
  f_tax_paid: 360000
  balance_due: 14508
```

**Example 2: losses brought forward, a forced periodiseringsfond reversal and the schablonintäkt.** Vinterbro Handel AB, calendar year 2026, has a tax loss of SEK 900,000 carried forward from 2025. Assume no ownership change, bankruptcy, debt reduction or other loss restriction applies. On 1 January 2026 it holds one periodiseringsfond of SEK 400,000, allocated in tax year 2020, which must be reversed in 2026 (the sixth year after 2020). Because the fund was set aside in a tax year beginning in 2020, the reversal is uplifted to 104%: SEK 416,000. Its 2026 business result before these items is SEK 699,800. The schablonintäkt is 2.55% of SEK 400,000, which is SEK 10,200. The surplus before the loss deduction is SEK 699,800 + SEK 10,200 + SEK 416,000 = SEK 1,126,000. After the loss of SEK 900,000, taxable income is SEK 226,000 and tax is SEK 46,556. The company makes no new allocation this year. For the original alternative purchase of control for SEK 200,000, a SEK 600,000 cap follows only if the beloppsspärr is triggered, adjusted acquisition expenditure remains SEK 200,000, and no overriding loss-forfeiture rule applies (IL 40 kap. 15–17 a §§). This is a conditional illustration, not clearance of an acquisition.

```oa-check
name: SE example 2, loss carry-forward with forced periodiseringsfond reversal at 104%, 2026
inputs:
  result_before_items: 699800
  pfond_opening: 400000
  statslaneranta_pct: 2.55
  loss_brought_forward: 900000
steps:
  - schablonintakt: pct(pfond_opening, statslaneranta_pct)
  - reversal: pfond_opening * 1.04
  - surplus_before_loss: result_before_items + schablonintakt + reversal
  - loss_used: min(loss_brought_forward, surplus_before_loss)
  - taxable: floor((surplus_before_loss - loss_used) / 10) * 10
  - tax: taxable * 0.206
expected:
  schablonintakt: 10200
  reversal: 416000
  surplus_before_loss: 1126000
  loss_used: 900000
  taxable: 226000
  tax: 46556
```

## Ask the client first

1. When does the financial year end, and is this the first year or a changed year? This sets the filing and payment dates.
2. Obtain the full ownership history, including control changes, acquisitions of at least 20% of votes by relevant acquirers over successive tax years, capital contributions, same-group history and other loss restrictions (IL 40 kap.).
3. What periodiseringsfonder exist, by year of allocation? Any fund from tax year 2020 must be reversed in 2026 at 104%, and all funds carry the schablonintäkt.
4. Does the company own shares in other companies (percentage, votes, listed or not, how long held), or pay dividends to foreign shareholders? This settles the participation exemption and kupongskatt.
5. Does it have net interest costs, and is it part of a group with other borrowers? The SEK 5 million amount is shared across the group (IL 24 kap. 24 §).
6. Is it part of a group with a parent owning more than 90%, and does the group want to move profit by koncernbidrag before the filing date?

## Sources

| Source and portions read | URL | Read on |
|---|---|---|
| IL: read ordinary corporate scope, base and rate (1, 5, 6, 9, 14, 16, 65 kap.); equipment/inventory, participation, pensions, reserves, group relief and losses (17–18, 24, 24 a, 25 a, 28, 30, 35, 40 kap.); gift provisions in 67 kap.; transitional rules SFS 2018:1206, 2024:1131, 2025:1333 and 2025:1361. Sections identified in the body, with dependencies, control the computation. | https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/inkomstskattelag-19991229_sfs-1999-1229/ | 2026-11-27 |
| SFL: read corporate return dates (32 kap.), late fees and surcharge/exclusions/remission (48–49, 51 kap.), preliminary tax (55 kap.), payment (62 kap.) and interest (65 kap.). | https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/skatteforfarandelag-20111244_sfs-2011-1244/ | 2026-11-27 |
| Kupongskattelagen: read domestic scope and rate, 4–5 §§; individual exemption/treaty outcomes are held. | https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/kupongskattelag-1970624_sfs-1970-624/ | 2026-11-27 |
| Lag (2023:875) om tilläggsskatt: read 1 kap. 3 § scope and neighbouring exclusions; computation/reporting held. | https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-2023875-om-tillaggsskatt_sfs-2023-875/ | 2026-11-27 |
| Skatteverket 2026 amounts: read prisbasbelopp SEK 59,200 and prior-November statslåneränta 2.55%; derived low-value and pension caps shown above. | https://www.skatteverket.se/privat/skatter/beloppochprocent/2026.4.1522bf3f19aea8075ba21.html | 2026-11-27 |
| Skatteverket allocation reserves: read deduction basis, reversal order/uplifts and deemed income; IL controls. | https://www.skatteverket.se/foretag/drivaforetag/foretagsformer/aktiebolag/periodiseringsfond.4.4887341d16e1e2b8ddf30e.html | 2026-11-27 |
| Skatteverket corporate declaration: read 2026 year-end deadline table, extra-payment table and legacy-service closure. | https://www.skatteverket.se/foretag/inkomstdeklaration/deklareraatettaktiebolagellerenekonomiskforening.4.46ae6b26141980f1e2d1261.html | 2026-11-27 |
| Skatteverket filing instructions: read all three return parts, full-return service, software/Filöverföring routes, signature and receipt, and old first-page-only service. | https://www.skatteverket.se/foretag/inkomstdeklaration/deklareraatettaktiebolagellerenekonomiskforening/saharlamnarduinochfylleriinkomstdeklarationen.4.262c54c219391f2e96322d7.html | 2026-11-27 |
| Skatteverket tax-account interest: read current rates and enforcement transition. Rates can change; refresh before computing interest for a later payment date. | https://www.skatteverket.se/privat/skatter/skattekontobetalaochfatillbaka/rantapaskattekontot.4.18e1b10334ebe8bc80002582.html | 2026-11-27 |
| Skatteverket corporate gifts: read eligibility, approved-recipient and gift conditions; operative IL provisions control. | https://www.skatteverket.se/foretag/skatterochavdrag/gavortillideellaverksamheter.4.1522bf3f19aea8075ba3df3.html | 2026-11-27 |

Not yet confirmed: usable individual outcomes for every explicitly held point above, including special entities, pension supplementary rules, investment/hybrid/shell-company cases, targeted debt restrictions and loss interactions, complex group relief, kupongskatt exemptions/treaties, EU royalties, CFC and exit/deferral. No number or outcome from those held cases may be used to file or pay. Check this point with one of our partner accountants.
