---
name: fr-corporate-tax
description: "French corporate income tax (impôt sur les sociétés, IS) for companies resident in France and for foreign companies with an establishment in France, financial years closing in 2026. Covers the 25% standard rate and the 15% SME rate on the first EUR 42,500 (CGI art. 219), the 3.3% social contribution (art. 235 ter ZC), the exceptional contribution on large companies for the first two years closed from 31 December 2025, the taxable base, the parent-subsidiary regime, losses (EUR 1m plus 50% cap, one-year carry-back), tax consolidation at 95%, the interest cap (EUR 3m or 30%), form 2065, the four acomptes and the balance, penalties, and outbound withholding tax. Trigger on: IS France, impôt sur les sociétés, taux réduit PME, 2065, acompte IS, report en arrière, intégration fiscale, régime mère-fille, contribution exceptionnelle grandes entreprises. Out of scope: CFE and CVAE (fr-cfe), VAT (france-vat-return), transfer pricing (france-transfer-pricing), individual income tax (fr-personal-income-tax)."
version: 0.4
jurisdiction: FR
tax_year: 2026
last_updated: 2026-10-31
authored_by: Ryan Duguid
review_status: pending_review
trust_label: Accountant-authored
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# France: corporate income tax (impôt sur les sociétés, IS) v0.4

> **General reference only.** This skill is general tax reference material for AI-assisted work. It has not been reviewed for any company's facts. Do not file, pay or take a tax position on it without review by a qualified professional in France.

**Tax year.** Figures are for financial years (exercices) closing in 2026. France taxes companies by financial year, not calendar year. The original source-reading notes dated 22 October 2026 are preserved below; the selected corporate provisions used in this repair were reread on 29 October 2026. The current article 219 supplies the rates, SME conditions and participation-share accounting-entry rule set out here. Its effect annotation and article 15-II of loi n° 2026-103 du 19 février 2026 state application to years closed from 31 December 2025. The retained article 15 consolidation record shows a modification index and that effect clause, not the full enacted amendment wording. It does not by itself prove the earlier assertion that a complete comparison of the 20 and 22 February versions showed only one accounting-entry change and no rate/SME change; that historical comparison is not relied on as current evidence.

**Sibling skills.** The local business taxes (CFE, CVAE and the CET cap) are in `fr-cfe`; do not compute them here. Bookkeeping, the annual closing and non-deductible charges in day-to-day practice are in `fr-business-accounting` and `france-bookkeeping`. Intercompany pricing is in `france-transfer-pricing`. Penalties procedure in an audit is in `fr-tax-audit`. Dividends received by individuals are in `fr-capital-gains`.

## Who this applies to

- **Companies liable by their form.** CGI art. 206-1 makes liable to IS, whatever their purpose, the sociétés anonymes (SA), sociétés en commandite par actions, sociétés à responsabilité limitée (SARL) that have not opted for partnership treatment, cooperatives, and other legal persons carrying on a profit-making activity. The SAS and SASU are joint-stock companies and are taxed the same way.
- **Territorial base.** Under CGI art. 209-I, profits liable to IS are computed "en tenant compte uniquement des bénéfices réalisés dans les entreprises exploitées en France", plus profits that a tax treaty gives France the right to tax. A French company's foreign branch profits are, as a rule, outside the French base. A foreign company is taxed in France on the profits of an enterprise it operates in France, typically through a branch or other establishment.
- **Out of scope here.** Partnerships (sociétés de personnes) and most SCIs are taxed in the hands of their partners unless they opt for IS (CGI art. 206-3 lists the entities that may opt, among them the SNC, the sociétés civiles of art. 8-1°, and the SARL whose single partner is an individual; the option itself is governed by art. 239); see `fr-rental-income` for the SCI. A sole trader (entreprise individuelle) is ordinarily taxed under income tax, but an EI that has validly opted for assimilation to an EURL can be subject to IS. Establish that actual option before routing the ordinary IR case to `fr-income-tax`; legal form alone does not settle the tax regime.
- **Pillar Two.** Groups with consolidated turnover of at least EUR 750 million in at least two of the four preceding years are subject to the minimum tax (CGI art. 223 VJ and 223 VL). This skill does not compute it.

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| Standard IS rate | 25% ("Le taux normal de l'impôt est fixé à 25 %") | Years closed from 31 Dec 2025 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000046868562 |
| SME reduced rate | 15% | Same | Same (art. 219-I-b) |
| Profit taxed at the reduced rate | First EUR 42,500 "de bénéfice imposable par période de douze mois" | Same | Same |
| SME condition 1: turnover of the year, restated to 12 months (summed across the group for a consolidation parent) | Not more than EUR 10 million | Same | Same |
| SME condition 2: capital fully paid up and held continuously at least this share by individuals, or by a company meeting the same CGI art. 219-I-b conditions whose capital is at least75% held by individuals; apply the actual specified investment-fund exclusions only where their no-dependence condition is met | 75% | Same | Same |
| Long-term net gains on participation shares (titres de participation) | 0%, with 12% of the gross gain added back as a share of costs (art. 219-I-a quinquies) | Same | Same |
| Social contribution on IS (contribution sociale sur l'IS) | 3.3% of IS after an abatement | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000031011715 |
| Annual abatement before the 3.3% | EUR 763,000 per 12 months, prorated for a short or long year | 2026 | Same |
| Exemption from the social contribution | Turnover below EUR 7,630,000 AND capital fully paid up and held continuously at least 75% by individuals, or by a company itself so held | 2026 | Same |
| Exceptional contribution on large companies, rate where BOTH current-year and prior-year turnover are below EUR 3 billion | 20.6% of the average IS of the year and the prior year, subject to the applicable art. 48 IV-A taper | First two years closed from 31 Dec 2025 | https://www.legifrance.gouv.fr/loda/id/JORFARTI000051168626 |
| Exceptional contribution, rate where EITHER current-year or prior-year turnover is EUR 3 billion or more | 41.2%, subject to the specific two-year art. 48 IV-B taper conditions | Same | Same |
| Exceptional contribution, entry threshold, second year (the year closing in 2026 for a calendar-year company) | French turnover of EUR 1.5 billion or more | Same | Same |
| No quarterly instalments where IS is below | EUR 3,000 | 2026 | https://entreprendre.service-public.gouv.fr/vosdroits/F23575 |
| Late payment interest | 0.20% per month | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051213330 |
| Local business taxes on companies (CFE, CVAE) | Not set out here | 2026 | See `fr-cfe` |
| Pillar Two minimum tax | In force (CGI art. 223 VJ, introduced by the 2024 finance law); groups at EUR 750m or more | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048846056 |

**The exceptional contribution (contribution exceptionnelle sur les bénéfices des grandes entreprises).** It was created by article 48 of the 2025 finance law (loi n° 2025-127 du 14 février 2025) for the first year closed from 31 December 2025 only. Article 12 of the 2026 finance law extended it. The consolidated text read today says: "Il est institué, au titre des deux premiers exercices clos à compter du 31 décembre 2025, une contribution exceptionnelle". So it **does apply** to the second year, which for a calendar-year company is the year closing 31 December 2026. What the enacted text says for that second year:

- Liable: IS payers with French turnover of EUR 1 billion or more for the first year or the year before, "et à 1,5 milliard d'euros au titre du second exercice". The parent of a tax-consolidated group pays it, on the group's summed turnover.
- Base: the average of the IS due for the year and for the previous year, on all profits taxed at the art. 219 rates, before reductions, credits and tax receivables.
- Rates: 20.6% where both current-year and prior-year turnover are below EUR 3 billion; 41.2% where either year is at least EUR 3 billion. Apply the separate statutory smoothing conditions in IV-A and IV-B before treating those as the final rates. In particular, the EUR 3 billion to EUR 3.1 billion taper requires both years to be in that interval and uses the higher turnover. The second-year EUR 1.5 billion to EUR 1.6 billion taper has its own IV-A conditions. The rates in the text are the same for both years.
- No reduction or tax credit may be set against it (part V), and it is not deductible (part VI).
- Payment: an advance payment of 98% of the estimated contribution at the date of the last IS instalment, and the balance by the IS balance date (part VIII).

The BOFiP comment on the extension (ACTU-2026-00097) could not be opened today (see Sources). Rely on the statute above.

## The taxable base

Start from the accounting result and make the tax adjustments on the liasse fiscale. Apply CGI art. 1657 whole-euro assessment rounding to the direct-tax assessment base and assessed tax: a fraction below EUR 0.50 is discarded and EUR 0.50 or more counts as one euro. CGI art. 1724 requires the liquidation rounding at the computation of each separate tax. Keep the actual rounded assessment and actual rounded instalments for the payment reconciliation; the instalment rule below does not replace assessment rounding. For example, an independently established pre-rounding IS assessment of EUR 2,500.25 becomes EUR 2,500.

1. **Add back taxes that are not deductible.** CGI art. 213: "L'impôt sur les sociétés, la contribution sociale mentionnée à l'article 235 ter ZC et l'impôt sur le revenu ne sont pas admis dans les charges déductibles". The exceptional contribution is also non-deductible (art. 48-VI of the 2025 finance law). Other common add-backs, such as luxury spending and excessive pay, are in `fr-business-accounting`.
2. **Interest limitation (CGI art. 212 bis).** For a company outside a tax-consolidated group, the general part-I limit on otherwise deductible net financial charges is the higher of "Trois millions d'euros" and "30 % de son résultat" (tax EBITDA defined in part II). The EUR 3 million is per year, prorated to 12 months. This is not always the final deduction. Under VI bis, a company that is outside a consolidated accounting group, has no establishment outside France and has no associated enterprise within the first four paragraphs of Directive (EU) 2016/1164 art. 2(4) also deducts 75% of the charges denied under part I in that same year. For example, with all those conditions met, tax EBITDA EUR 5 million and net charges EUR 4 million, the general limit is EUR 3 million, the additional deduction is EUR 750,000 and EUR 250,000 remains denied. Parts IV and VIII do not apply for a year using VI bis; do not put that remainder into the generic VIII carry-forward. Part VI separately allows conditional equity-ratio relief for a member of a consolidated accounting group; part VII has separate thin-capitalisation rules. Apply the applicable conditions before finalising deductions or carry-forwards. Tax-consolidated groups have their own rule, which is not set out here.
3. **Depreciation.** Tax depreciation follows the accounts; the rules and the EUR 500 small-equipment tolerance are in `france-bookkeeping` and `fr-business-accounting`.
4. **Parent-subsidiary regime (régime mère-fille, CGI art. 145 and 216).** A recipient subject to IS at the normal rate can remove qualifying participation income from taxable profit after the share of costs. Under article 145, the securities must be registered or deposited/entered with an authorized account-keeping/custody intermediary: the specified French or EU institutions, or a qualifying third-state intermediary with the required assistance/information access and equivalent professional obligations. Full or bare ownership must represent at least 5% of the issuer’s capital, measured at the dividend-payment date, with the two-year holding condition. The existing alternative for a participant controlled by qualifying non-profit bodies requires 2.5% of capital and 5% of voting rights, held for five years. Article 216 normally keeps a 5% share of total participation income, including the tax credit. Its 1% branch applies to income from another member of the same tax-consolidated group that has been a member for more than one financial year, or from an EU/qualifying-EEA subsidiary subject to equivalent corporate tax where the companies would have met the group conditions for more than one financial year if the subsidiary were French; the EEA state needs the required administrative-assistance agreement. Thus the ordinary qualifying deduction is 95%, or 99% only where the actual 1% branch is established, not solely because the subsidiary is geographically in the EU/EEA. Keep the source’s special holding/title and other exclusions separate.
5. **Gains on participation shares.** Net long-term gains on titres de participation are taxed at 0%, but 12% of the gross gain is added to the taxable result (art. 219-I-a quinquies). A gain is long-term only if the shares were held for at least two years: under CGI art. 39 duodecies-2-a, gains on assets "acquis ou créés depuis moins de deux ans" are short-term and taxed at the normal rate. Gains on property-rich company shares and shares in non-cooperative states are excluded.
6. **Losses carried forward (CGI art. 209-I).** A loss is deducted from the next year's profit "dans la limite d'un montant de 1 000 000 € majoré de 50 % du montant correspondant au bénéfice imposable dudit exercice excédant ce premier montant". The rest carries forward without time limit, under the same cap each year.
7. **Loss carried back (CGI art. 220 quinquies).** On option, the current-year loss can be set against the previous year only, up to the lowest of the loss, eligible undistributed prior profit and EUR 1,000,000. Eligible prior profit excludes the exempt profits listed in article I, profit benefiting from art. 219-I-f's first-paragraph regime, and profit that gave rise to IS paid using tax credits or reductions. Do not treat retained profit as eligible without checking how its IS was paid; the article supplies no blanket allocation assumption for a mixed credit-funded year. Elect by the loss year's results-return deadline. The option is unavailable for a year involving a transfer or total cessation, a merger or assimilated operation, or a judgment ordering judicial liquidation (II). The tax overpaid becomes a non-taxable receivable on the State. It can be used to pay IS during the next five years and is refunded at the end of five years if unused.
8. **Tax consolidation (intégration fiscale, CGI art. 223 A).** A parent can elect to pay IS for a group of companies held directly or through the permitted chains continuously through the year. In the ordinary route, “95% of capital” means full ownership of at least 95% of both dividend rights and voting rights, not nominal capital alone. Group members must consent and be subject to ordinary IS or the article 214 conditions; they must open and close their financial years on the same dates, subject to the actual statutory exceptions. The ordinary parent must also satisfy the restriction on being at least 95% owned by another qualifying IS person; the article has distinct non-resident-parent, indirect-holding and other exceptions, so do not assume every upper-parent structure is barred or eligible. Notify the option by the results-return deadline for the preceding year. It lasts five financial years; obtain each member’s agreement within the actual III timetable, ordinarily by its preceding-year results-return deadline, with the separate three-month acquisition route where applicable. Options/agreements renew tacitly unless validly renounced; maintain the annual group list. Only after these gates are met are members’ profits and losses pooled. Read article 223 A for its nonstandard ownership, calendar and agreement exceptions before using them.

## Deadlines and filing

| Step | Rule | Source |
|---|---|---|
| Results return | Form 2065 with the liasse fiscale, filed electronically through the professional space. Due within 3 months of the year end; for a year closed on 31 December, by the second working day after 1 May (CGI art. 223) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000034387974 |
| Extra time for e-filing | The administration allows 15 more calendar days. For a year closed on 31 December 2025, the deadline was 20 May 2026 | https://entreprendre.service-public.gouv.fr/vosdroits/F23575 |
| Quarterly instalments (acomptes) | Four instalments on 15 March, 15 June, 15 September and 15 December, on form 2571, paid electronically. Compute the statutory reference IS from the last closed year under CGI art. 1668-1, then round each instalment to the nearest whole euro, with a EUR 0.50 fraction rounded up. The sum of the rounded payments can differ from the unrounded reference IS; calculate the balance using the actual rounded instalments paid. The special last-instalment rules below remain separate. | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000033836779 |
| Who pays no instalments | A company whose IS is below EUR 3,000, and a company in its first year of activity or first year under IS | F23575; art. 1668-1 |
| Large companies, last instalment | Turnover EUR 250 million to EUR 1 billion: the last instalment must bring the total to at least 95% of the estimated IS for the current year. Turnover above EUR 1 billion: at least 98%. Turnover is summed across a tax-consolidated group. There is no other band (point c of the article is repealed) | art. 1668-1 |
| Balance (solde) | Form 2572, by the 15th day of the 4th month after the year end; for a 31 December year end, 15 May of the next year. Any overpayment is refunded | art. 1668-2; F23575 |
| Year closing 31 December 2026 | By the rules above: instalments 15 March, 15 June, 15 September and 15 December 2026; return due the second working day after 1 May 2027 plus 15 days for e-filing (1 May 2027 is a Saturday, so by our count Tuesday 4 May 2027, or 19 May 2027 with the extra 15 days); balance by 15 May 2027. The administration had not published its 2027 calendar on the pages read today | As above |

## Penalties and interest

| What | Figure | Source |
|---|---|---|
| Late return, no formal notice, or filed within 30 days of a formal notice (mise en demeure) | 10% surcharge on the tax due | CGI art. 1728: https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053546784 |
| Return still not filed 30 days after a formal notice | 40% | Same |
| Hidden activity (activité occulte) | 80% | Same |
| Deliberate failure (manquement délibéré) | 40% of the extra tax | CGI art. 1729: https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000020051904 |
| Abuse of law (abus de droit) | 80%, reduced to 40% where the company was not the main initiator or beneficiary | Same |
| Fraudulent manoeuvres | 80% | Same |
| Late payment of IS | 5% surcharge on the amount paid late, except under article 1731-2 where a late declaration or assessment/liquidation act is accompanied by payment of all corresponding tax. That exception does not itself cancel separate late-filing consequences or article 1727 interest. | CGI art. 1731: https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000033812315 |
| Late payment interest | 0.20% per month on top of the surcharges ("Le taux de l'intérêt de retard est de 0,20 % par mois") | CGI art. 1727: https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051213330 |

For the audit procedure, reductions for good faith and the appeal steps, use `fr-tax-audit`.

## Cross-border points

- **Dividends paid abroad.** CGI art. 119 bis-2 levies withholding tax at the art. 187 rate where the beneficial owner has no tax domicile or seat in France. Art. 187-1 sets it at the art. 219 standard rate (25%) for companies, 12.8% for individuals, and, under article 187-2, 75% for the covered distributions paid outside France in a non-cooperative state or territory other than the article 238-0 A-2 bis-2° subpopulation. That override does not apply if the debtor proves the distributions there have neither the purpose nor the effect of locating the income there for tax-fraud purposes. Establish the otherwise applicable rate, exemption and treaty conditions separately; this rebuttal does not establish zero withholding. Treaties usually reduce these rates.
- **EU parent-subsidiary exemption (CGI art. 119 ter).** No withholding applies to a distribution by a company or body subject to IS at the normal rate only if the recipient establishes to the debtor or paying person that it is the beneficial owner and satisfies article 119 ter-2. Its effective management must be in the EU or in an EEA state with the required French anti-fraud/anti-evasion administrative-assistance agreement; a third-state tax treaty must not treat it as resident outside the EU/EEA. It must have a Directive 2011/96/EU Annex I-A form, or an equivalent form for an EEA recipient, and be subject in that state to corporate tax without an option and without exemption. It must directly hold at least 10% of the distributing company’s capital in full or bare ownership continuously for two years, or undertake that holding and appoint the representative responsible for withholding if the undertaking fails. The threshold drops to 5% where the beneficial owner meets article 145 and cannot credit the French withholding. A qualifying permanent-establishment recipient follows the separate article 119 ter-2 bis conditions. The exemption does not apply to a non-genuine arrangement whose main purpose or one of its main purposes is the contrary tax advantage (article 119 ter-3).
- **Royalties and service fees.** Payments to a non-resident with no permanent installation in France, for intellectual property or for services supplied or used in France, bear withholding at the art. 219 standard rate (CGI art. 182 B-II), or, under article 182 B-III, 75% on covered non-salary payments to persons domiciled or established in a non-cooperative state or territory other than the article 238-0 A-2 bis-2° subpopulation. That override does not apply if the debtor proves actual operations with a principal purpose and effect other than locating the income in a non-cooperative state. Determine the otherwise applicable base, rate, exemption and treaty separately; the rebuttal is not automatic zero withholding. Under I bis, the starting base is gross payments. Deduct a 10% expense allowance if the recipient is a legal person or body whose results are not taxed as an individual partner's income, and its seat or the permanent establishment including the income is in the EU or an EEA state with the required French administrative-assistance agreement, and is not non-cooperative under art. 238-0 A. Thus a qualifying EUR 10,000 payment has a EUR 9,000 base and EUR 2,250 withholding at 25%, before any applicable treaty or associated-company relief. Establish the recipient and location conditions before applying the allowance. Royalties between associated EU companies are exempt under CGI art. 182 B bis only after the incorporated article 119 quater conditions and proof are met. The payer must be an eligible SA, SAS, SCA, SARL, EPIC or public enterprise subject to IS without exemption, or a qualifying permanent establishment dependent on an eligible company. Association requires a direct holding of at least 25% by one company in the other, or direct holdings of at least 25% in both by a third company, continuously for two years or under a two-year undertaking; an undertaking by a company effectively managed outside France requires the responsible representative. The recipient must prove to the debtor or paying person that it is the beneficial owner, has effective management in an EU member state, has an eligible Directive 2003/49/EC form, and is subject there to corporate tax, including on the royalty income, without exemption. A recipient permanent establishment must itself prove beneficial ownership and taxation of the income in its member state to corporate or equivalent tax, and its company must satisfy the incorporated conditions, including the participation where association depends on it. A payer permanent establishment uses the article 119 quater association rule through its company. Article 182 B bis-3 excludes the specified non-EU-controlled participation chains where obtaining the exemption is a main purpose; special related-party pricing grants relief only to the arm’s-length amount, not the excess.
- **Interest.** Under CGI art. 125 A-III a compulsory levy applies to interest paid by a French debtor into a non-cooperative state or territory, whoever the beneficiary is, unless the debtor shows the main purpose and effect of the transactions was not to locate the income there. The rate is 75% (art. 125 A-III bis, 2°). Interest paid to non-residents outside that case is not subject to this levy.
- **Branch profits (CGI art. 115 quinquies).** Profits made in France by a foreign company are deemed distributed each year to shareholders outside France, on the total result after IS, and bear the art. 119 bis-2 withholding at the art. 187 rate. The company can ask for a refund to the extent the amounts exceed its actual distributions, or were paid to shareholders in France. The rule does not apply to a company with its seat in the EU or EEA that is liable there to corporate tax without option or exemption. Treaties often cancel or reduce it.
- **CFC rules (CGI art. 209 B).** A French IS payer that holds more than 50% of a foreign entity, or runs a foreign enterprise, subject to a privileged tax regime is taxed in France on that entity's profits. Under CGI art. 238 A, a regime is privileged if the foreign tax is at least 40% lower than the French tax would have been. The article has exceptions that this skill does not set out; read the article before applying it.
- **Exit tax on companies (CGI art. 221-2).** Moving the seat or an establishment to a state outside the EU or qualifying EEA recovery-assistance area is treated as a cessation. For a transfer of an asset, seat or establishment to another EU state, or an EEA state with a French mutual-recovery-assistance convention of scope similar to Directive 2010/24/EU, the tax on the transferred fixed assets’ latent gains and deferred/suspended gains is due within two months. Pay it in full or, on the company’s express request, one-fifth initially and equal parts by the anniversaries of the first payment over the next four years; earlier payment of the remaining balance is possible. Within five years, disposal of the transferred assets, their transfer to a nonqualifying state or dissolution accelerates the remaining tax immediately. Missing a payment date also makes the tax immediately due. Send the prescribed annual monitoring statement to the non-resident tax service. These destination, event and reporting conditions apply to the payment route; five instalments are not unconditional.
- **Exceptional contribution.** Treaty credits and other tax credits cannot be set against it (art. 48-V of the 2025 finance law).

## Worked examples

### Example 1: an SME on the reduced rate

A SAS closes its year on 31 December 2026. Turnover is EUR 4,000,000. Its capital is fully paid up and held 100% by two individuals. Taxable profit after all adjustments is EUR 200,000. Both art. 219-I-b conditions are met, so the first EUR 42,500 is taxed at 15% and the rest at 25%. Turnover is below EUR 7,630,000 and the capital test is met, so no social contribution is due. The four 2026 instalments were based on the 2025 tax of EUR 40,000, so the balance due by 15 May 2027 is the difference.

```oa-check
name: SAS, profit EUR 200,000, reduced rate, year closing 31 Dec 2026
inputs:
  profit: 200000
  sme_band: 42500
  instalments_paid: 40000
steps:
  - reduced_part: min(profit, sme_band) * 0.15
  - standard_part: max(profit - sme_band, 0) * 0.25
  - is_due: reduced_part + standard_part
  - balance: is_due - instalments_paid
expected:
  reduced_part: 6375.00
  standard_part: 39375.00
  is_due: 45750.00
  balance: 5750.00
```

### Example 2: losses brought forward and the social contribution

A SA closes its year on 31 December 2026. Turnover is EUR 60,000,000, so the reduced rate does not apply and the company is not exempt from the social contribution. Profit before losses is EUR 12,000,000. Losses brought forward are EUR 9,000,000. Art. 209-I caps the deduction at EUR 1,000,000 plus 50% of the profit above EUR 1,000,000, which is EUR 6,500,000. Taxable profit is EUR 5,500,000 and EUR 2,500,000 of losses carry forward. IS at 25% is EUR 1,375,000. The social contribution is 3.3% of the IS above the EUR 763,000 abatement. Turnover is far below EUR 1.5 billion, so the exceptional contribution does not apply.

```oa-check
name: SA, profit EUR 12m, losses EUR 9m brought forward, social contribution
inputs:
  profit_before_losses: 12000000
  losses_bf: 9000000
  abatement: 763000
steps:
  - loss_cap: 1000000 + max(profit_before_losses - 1000000, 0) * 0.5
  - loss_used: min(losses_bf, loss_cap)
  - taxable: profit_before_losses - loss_used
  - losses_cf: losses_bf - loss_used
  - is_due: taxable * 0.25
  - social_contribution: max(is_due - abatement, 0) * 0.033
  - total: is_due + social_contribution
expected:
  loss_cap: 6500000.00
  loss_used: 6500000.00
  taxable: 5500000.00
  losses_cf: 2500000.00
  is_due: 1375000.00
  social_contribution: 20196.00
  total: 1395196.00
```

## Ask the client first

1. Turnover for both the current and previous year, restated to 12 months, and whether the company heads a tax-consolidated group (the turnover is then summed). The current year affects the reduced rate and social contribution; both years are needed for the exceptional contribution rate and its taper conditions.
2. Who holds the capital, whether it is fully paid up, and whether 75% has been held by individuals continuously through the year.
3. The year-end date and whether the year is shorter or longer than 12 months (the EUR 42,500 band, the EUR 763,000 abatement and the EUR 3 million interest floor are set per 12 months).
4. Losses brought forward by year, and whether a carry-back of this year's loss is wanted. For carry-back, supply prior undistributed profit, exempt or preferential-regime profit, how prior IS was paid (including credits/reductions), and any event covered by article 220 quinquies II.
5. Shareholdings of 5% or more held for two years, intragroup dividends, and any 95% subsidiaries.
6. Payments to non-residents (dividends, royalties, service fees, interest), the recipient's entity/tax status, the seat or relevant permanent-establishment country, and whether it is a non-cooperative state. Those facts affect withholding and the art. 182 B-I bis base allowance.

## Sources

| Source | URL | Read on |
|---|---|---|
| CGI art. 219 (rates, SME rate, participation gains) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000046868562 | 2026-10-22 |
| CGI art. 235 ter ZC (social contribution) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000031011715 | 2026-10-22 |
| Loi n° 2025-127, art. 48, consolidated as amended by loi n° 2026-103 art. 12 (exceptional contribution) | https://www.legifrance.gouv.fr/loda/id/JORFARTI000051168626 | 2026-10-22 |
| CGI art. 206 (companies liable; option for IS in 206-3) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000054373514 | 2026-10-22 |
| 2026 finance law, art. 15 (change to art. 219) | https://www.legifrance.gouv.fr/loda/id/LEGIARTI000053511649/2026-02-21 | 2026-10-22 |
| CGI art. 219, historical version in force on 20 February 2026 (the earlier complete-comparison assertion is unconfirmed from the selected retained evidence) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000046868562/2026-02-20 | 2026-10-22 |
| CGI art. 39 duodecies (short-term and long-term gains, two-year holding) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006307676 | 2026-10-22 |
| CGI art. 209 (territoriality, loss carry-forward) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048847486 | 2026-10-22 |
| CGI art. 220 quinquies (loss carry-back) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053560738 | 2026-10-22 |
| CGI art. 213 (IS not deductible) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000054373444 | 2026-10-22 |
| CGI art. 212 bis (interest limitation) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000049641637 | 2026-10-22 |
| CGI art. 145 (parent-subsidiary conditions) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051203497 | 2026-10-22 |
| CGI art. 216 (share of costs) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048831340 | 2026-10-22 |
| CGI art. 223 A (tax consolidation) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048834056 | 2026-10-22 |
| CGI art. 223 (results return deadline) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000034387974 | 2026-10-22 |
| CGI art. 1668 (instalments and balance); CGI arts. 1657/1724 (separate direct-tax assessment/liquidation rounding) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000033836779 ; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051219510 ; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006312863 | 2026-10-22; retained rounding scopes2026-10-31 |
| CGI art. 1727 (late interest) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051213330 | 2026-10-22 |
| CGI art. 1728 (late filing) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053546784 | 2026-10-22 |
| CGI art. 1729 (inaccuracy penalties) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000020051904 | 2026-10-22 |
| CGI art. 1731 (late payment surcharge) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000033812315 | 2026-10-22 |
| CGI art. 119 bis (withholding on distributions) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051218411 | 2026-10-22 |
| CGI art. 187 (withholding rates) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051218440 | 2026-10-22 |
| CGI art. 119 ter (EU parent-subsidiary exemption) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000031815505 | 2026-10-22 |
| CGI art. 182 B (royalties and services withholding) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000045765660 | 2026-10-22 |
| CGI art. 182 B bis (EU royalties exemption) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000039382322 | 2026-10-22 |
| CGI art. 125 A (levy on interest, 75% rate in III bis) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000037526745 | 2026-10-22 |
| CGI art. 119 quater (associated companies, 25%) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006302662 | 2026-10-22 |
| CGI art. 115 quinquies (branch profits) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000042159010 | 2026-10-22 |
| CGI art. 209 B (CFC rules) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000029355796 | 2026-10-22 |
| CGI art. 238 A (privileged tax regime) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000037526846 | 2026-10-22 |
| CGI art. 221 (cessation, exit tax) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051765018 | 2026-10-22 |
| CGI art. 223 VJ and 223 VL (Pillar Two) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048846056 and https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048803788 | 2026-10-22 |
| Service-public.gouv.fr, IS rates, filing and payment (page last checked by its publisher on 17 February 2026) | https://entreprendre.service-public.gouv.fr/vosdroits/F23575 | 2026-10-22 |
| BOFiP, social contribution (BOI-IS-AUT-10-20) | https://bofip.impots.gouv.fr/bofip/3492-PGP.html | Could not be fetched on 2026-10-22 (connection refused, and timed out again on a second attempt); not relied on |
| BOFiP, extension of the exceptional contribution (ACTU-2026-00097) | https://bofip.impots.gouv.fr/bofip/15092-PGP.html/ACTU-2026-00097 | Could not be fetched on 2026-10-22 (timed out again on a second attempt); not relied on |
| impots.gouv.fr, professional IS pages and form 2065 | https://www.impots.gouv.fr/professionnel/impot-sur-les-societes | Site in maintenance on 2026-10-22 (still in maintenance on a second attempt); not relied on |
| CGI art. 212 bis I, VI, VI bis, VII and VIII: selected general/standalone/equity/thin-cap/carry-forward conditions reread | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000049641637/2026-10-29 | 2026-10-29 |
| CGI art. 220 quinquies I/II: eligible prior profit, credits/reductions exclusion and election conditions reread | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053560738/2026-10-29 | 2026-10-29 |
| Loi n° 2025-127, art. 48, consolidated: selected article only, including both turnover years and own taper conditions | https://www.legifrance.gouv.fr/loda/id/JORFARTI000051168626/2026-10-29 | 2026-10-29 |
| CGI art. 182 B I bis/II: gross base, full eligible recipient population and 10% expense allowance reread | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000045765660/2026-10-29 | 2026-10-29 |
| Selected corporate repair clauses: CGI arts. 1668, 119 ter, 182 B bis/119 quater, 1731, 223 A, 145/216, 187/182 B and 221; F23575 EI option; current 219 and art. 15-II effect clause. Rendered official captures, selected native clauses only; not a full amendment comparison. | Existing official URLs above, with exact quotation/range/hash/read attribution in the corporate ledger | 2026-10-29 |

Not yet confirmed: the conditions of the option for IS under CGI art. 239 (not read today); the interest limitation rules for tax-consolidated groups; and the official 2027 filing calendar for years closed on 31 December 2026 (the dates given above are computed from the statute and the 15-day extension, not taken from a published calendar).

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
