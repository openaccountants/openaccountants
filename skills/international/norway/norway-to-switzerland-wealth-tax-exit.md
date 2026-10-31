---
name: norway-to-switzerland-wealth-tax-exit
description: "Moving from Norway to Switzerland, for income year 2026: why owners leave (wealth tax of 1.0% and 1.1% on net wealth above NOK 1,900,000, shares valued at 80%, dividends taxed at an effective 37.84%), the new three-year wealth tax deferral, the three-year residence tail for people resident ten years or more (61 days and no dwelling), the exit tax on shares under skatteloven § 10-70 (NOK 3,000,000 threshold, 12-year deferral, the 0.7 dividend rule, return within 12 years cancels it, no loss deduction on a move outside the EEA), what stays Norwegian under the Norway-Switzerland treaty (15% dividend tax, real estate, the five-year rule for holdings over 25%, company residence), and the Swiss landing (lump-sum taxation with a CHF 435,000 federal minimum and the treaty rule that forces the modified version). Trigger phrases: move from Norway to Switzerland, utflyttingsskatt, exit tax Norway, Norway Switzerland tax treaty, Pauschalbesteuerung Norway."
version: 0.2
jurisdiction: "NO"
category: international
tax_year: 2026
last_updated: 2026-10-30
authored_by: Michael Cutajar, CPA, ACCA
review_status: pending_review
trust_label: Accountant-authored
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Norway to Switzerland: the wealth-tax corridor, the 3-year tail, and the exit tax

**Why this corridor needs a skill.** Norway levies an annual net wealth tax that falls on shareholdings, and the owner of a company usually funds it with dividends, which are taxed at an effective 37.84%. Switzerland also has a wealth tax, but it does not tax private capital gains on movable assets. The Norwegian exit tax on shares has been changed for moves from 29 November 2022, 20 March 2024 and 7 October 2024 _(skatteloven § 10-70, amendment history)_. The current text has no five-year expiry: the tax is settled within a 12-year period _(§ 10-70 seventh paragraph)_. The residence rules have not changed: a person resident for ten years or more needs three full income years abroad to stop being resident. Plan the move as a multi-year project.

**Who it is for.** Norwegian tax residents (owners, founders, investors) planning a move to Switzerland, and their advisers on both sides. Figures are for income year 2026.

---

## Part 1: Why people leave (the arithmetic)

- **Wealth tax (formuesskatt), 2026.** Municipal tax up to 0.35% and state tax of 0.65% on net wealth above NOK 1,900,000, and state tax of 0.75% on the part above NOK 21,500,000. The combined rate is 1.0%, and 1.1% above NOK 21,500,000 _(Stortingets skattevedtak 2026 §§ 2-1, 2-3; Skatteetaten, Formuesskatt 2026)_. Spouses taxed together have NOK 3,800,000 and NOK 43,000,000 _(skattevedtak § 2-1 second paragraph, § 2-3)_.
- **Valuation.** Listed shares are valued at 80% of the market price at 1 January of the assessment year. Unlisted Norwegian shares are valued at 80% of the share's part of the company's tax wealth value at 1 January of the year before _(skatteloven § 4-12 first and second paragraphs)_. Debt is reduced in proportion where assets are discounted _(skatteloven § 4-19)_. The primary home is valued at 25% of estimated market value, and 70% of the part above NOK 14,000,000; secondary homes at 100% _(skatteloven § 4-10 second and third paragraphs)_.
- **The funding loop.** An owner whose shares have a wealth value of NOK 500,000,000 enters NOK 400,000,000 (80%). Wealth tax is 1.0% x (21,500,000 - 1,900,000) = NOK 196,000, plus 1.1% x (400,000,000 - 21,500,000) = NOK 4,163,500, so NOK 4,359,500 in total (ignoring debt and other assets). Dividends to individuals are multiplied by 1.72 and taxed at 22%, an effective 37.84% _(skatteloven § 10-11 first paragraph; skattevedtak § 3-2 third paragraph)_. To keep NOK 4,359,500 after dividend tax, before any shielding deduction, the company must pay out about NOK 7,013,353. The tax is due in a loss year too.
- **New in 2026: deferral of wealth tax on business wealth.** An owner can defer wealth tax on shares, share savings accounts, partnership interests, business assets of a sole proprietorship and commercial property for up to three income years when the deferred tax exceeds NOK 30,000 in the year _(skattebetalingsloven § 9-3)_. Deferred tax and interest fall due on 31 May in the third year after the assessment year _(skattebetalingsloven § 10-51 fourth paragraph)_. The interest rate is 9% from 1 January 2026 and 9.25% from 1 July 2026 _(Skatteetaten, Renter ved utsatt betaling av formuesskatt)_. Deferral spreads the bill; it does not remove it.
- **Who pays wealth tax.** From income year 2026 the duty to pay wealth tax depends on living in Norway at 31 December of the year before the assessment year _(skatteloven § 2-1 seventh paragraph, lov 22 December 2025 nr. 119)_.
- **Switzerland** also has a wealth tax: every canton must levy income and wealth tax on individuals _(StHG art. 2 para. 1 letter a)_, so this is not a zero-tax move. Switzerland does not tax capital gains on movable private assets, at federal or cantonal level _(DBG art. 16 para. 3; StHG art. 7 para. 4 letter b)_.

```oa-check
name: Norway 2026 wealth tax on NOK 500m of shares and the dividend needed to fund it
inputs:
  share_value: 500000000
  valuation_rate: 0.80
  threshold: 1900000
  upper_threshold: 21500000
  dividend_rate: 0.3784
steps:
  - wealth_value: share_value * valuation_rate
  - tax_band_1: (upper_threshold - threshold) * 0.010
  - tax_band_2: (wealth_value - upper_threshold) * 0.011
  - wealth_tax: tax_band_1 + tax_band_2
  - dividend_needed: wealth_tax / (1 - dividend_rate)
expected:
  wealth_value: 400000000
  tax_band_1: 196000
  tax_band_2: 4163500
  wealth_tax: 4359500
  dividend_needed: 7013352.64
```

---

## Part 2: The 3-year tail

Residence in Norway does not end when you board the plane _(skatteloven § 2-1 third paragraph)_.

- **Resident at least ten years before the year you move:** residence ends only after the end of the third income year after the year you take up permanent residence abroad. In each of those three years you must show that you have not been in Norway for periods exceeding 61 days in the year, and that neither you nor a close relative has had a dwelling at your disposal in Norway _(§ 2-1 third paragraph letter b)_.
- **Resident fewer than ten years:** residence ends for the income year in which you show the same two things (61 days and no dwelling). It never ends before you and your close relatives stop having a dwelling at your disposal in Norway _(§ 2-1 third paragraph letter a)_.
- **Close relatives** are a spouse, cohabitant or minor children _(§ 2-1 fourth paragraph)_.
- **"Dwelling at your disposal"** means owning, renting or otherwise having a right to use a dwelling, directly or indirectly _(§ 2-1 fifth paragraph)_. A dwelling is a unit with year-round running water and drainage (unless planning rules bar its use as a home), and any unit actually used as a home. A unit acquired at least five years before the year you move, and not used as a home by you or close relatives in that period, does not count _(§ 2-1 sixth paragraph)_.
- **Until the tail ends** you remain resident under Norwegian law and taxable on worldwide wealth and income _(skatteloven § 2-1 first and ninth paragraphs)_, subject to the treaty.
- **The treaty overlay.** If you are resident in both states under domestic law, the treaty tie-breaker gives residence to the state where you have a permanent home; if you have one in both, to the state of your centre of vital interests; then habitual abode; then nationality _(Norway-Switzerland treaty art. 4 para. 2)_. In the year you move, each state taxes you as a full resident only for the part of the year you are its resident _(art. 4 para. 3)_. Once you are treaty-resident in Switzerland, wealth other than Norwegian real estate and Norwegian business property can be taxed only in Switzerland _(art. 22 paras. 1, 2 and 4)_.

**Practical points.** The 61-day test is per income year: count every day and keep evidence. Selling, letting on terms that do not let you return, or giving up a home is part of the exit. A holiday cabin with year-round water and drainage is a dwelling unless the five-year rule protects it.

---

## Part 3: The exit tax on shares (skatteloven § 10-70)

- **Trigger.** Gains on shares and similar assets you own when your Norwegian residence ends under § 2-1 third paragraph, or when you become resident in another state under a treaty, are taxed as if you had sold the assets on the last day before _(§ 10-70 first paragraph)_. The same applies when you transfer such assets to a person or company not taxable in Norway, for example a gift to a child living abroad _(§ 10-70 first paragraph, second sentence)_.
- **What it covers.** Shares and equity certificates in Norwegian companies, share savings accounts, interests in Norwegian partnerships, corresponding foreign shares and interests, subscription rights and options over them, and certain capital insurance _(§ 10-70 second paragraph)_.
- **Thresholds.** On a move, only the part of your total net gain (gains less deductible losses) above NOK 3,000,000 is taxed. On a transfer to a non-resident, the whole net gain is taxed when the net gain or loss exceeds NOK 100,000 in the income year _(§ 10-70 fourth paragraph)_. Skatteetaten computes each latent gain as market value less cost and unused shielding (risk-free return allowance), adds the gains up (on a move outside the EEA, losses are left out) and takes the NOK 3,000,000 basic deduction off that total; the 1.72 factor is not part of that sum _(Skatteetaten, Exit tax, worked examples)_.
- **Losses.** Losses are deductible only on a move or transfer to another EEA state _(§ 10-70 third paragraph)_. Switzerland is not in the EEA, so a move to Switzerland gives no loss deduction.
- **Computation.** The gain is the market value at the deemed sale less the cost; the ordinary share rules in skatteloven §§ 10-30 to 10-36 apply so far as they fit _(§ 10-70 fifth paragraph)_. Under those rules a personal shareholder's gain, after unused shielding, is multiplied by 1.72 and taxed at 22% _(skatteloven § 10-31 first paragraph; Forskuddsutskrivingen 2026)_. For assets you owned when you moved to Norway, the cost is their market value when you became resident _(§ 10-70 sixth paragraph)_.
- **Deferral for 12 years.** You can be given 12 years to pay, counted from the end of the year the exit tax is timed to. Security is required. For a move to another EEA state security is required only where there is a real risk the tax cannot be collected; Switzerland is outside the EEA, so the general rule applies _(§ 10-70 seventh paragraph)_. Security is, for example, a pledge of shares or real estate _(Skatteetaten, Exit tax)_. You choose how to pay:
  - a) one twelfth of the tax each year; or
  - b) all of it at the end of the period, with interest from the date the tax would have been due without deferral until payment _(§ 10-70 seventh paragraph letters a and b)_.
- **When the deferral ends early.** On sale, on your death, on a transfer to a non-resident, and when a partnership in scope stops its business. Death does not end the deferral if your personal heirs take over your duties under § 10-70 _(§ 10-70 eighth paragraph)_. A withdrawal from a share savings account beyond the deposits ends the deferral for a proportional amount _(§ 10-70 eighth paragraph, third sentence)_.
- **Dividend rule.** A dividend or other distribution on an asset that carries exit tax ends the deferral for an amount equal to the distribution multiplied by 0.7 _(§ 10-70 eighth paragraph, fourth sentence)_. You cannot empty the company while the exit tax is deferred.
- **Return within 12 years cancels it.** If you become resident in Norway again within 12 years after the end of the year the exit tax is timed to, the tax and accrued interest lapse for the assets you still own _(§ 10-70 ninth paragraph)_. If you return later than that, having paid the exit tax in full, the cost of the assets you still own is adjusted by the change in value that was taxed on exit _(same paragraph)_.
- **Information duty.** You must give the tax office all information relevant to the exit tax without being asked and without undue delay; a breach ends the deferral _(§ 10-70 eleventh paragraph)_.
- **Long reopening window.** Where exit tax under § 10-70 first paragraph was not assessed, the tax office has 15 years to reopen _(skatteforvaltningsloven § 12-6 first paragraph)_.

**Planning reads.**
- **The question is "pay when?", not "wait it out".** Compare paying in twelfths (option a) with paying at the end (option b, where the law sets interest), against liquidity and the chance you return.
- **Pre-departure steps** (realising gains or losses while resident, reorganising) are tested against the general anti-avoidance rule, which taxes an arrangement whose main purpose was a tax advantage on its economic substance _(skatteloven § 13-2)_.
- **The return option is real.** A founder unsure about the move can defer, live in Switzerland, and cancel the charge by moving back within 12 years.

---

## Part 4: What stays Norwegian while (and after) you leave

- **Dividends from Norwegian companies.** Norway's domestic withholding tax is 25% _(Stortingets skattevedtak 2026 § 3-5 third paragraph)_. Under the treaty, Norway's tax on dividends to a Swiss-resident individual is capped at 15%; a Swiss company holding at least 10% directly is exempt _(treaty art. 10 para. 2)_. Switzerland gives relief for the Norwegian tax on request, by credit, a lump-sum reduction or a partial exemption _(treaty art. 23 para. 2 letter b)_.
- **Large holdings: the five-year rule.** Norway may tax a gain on selling a holding of more than 25% in a Norwegian company if the seller was resident in Norway at some point in the five years before the sale and is not taxed on the gain in Switzerland _(treaty art. 13 para. 5)_. As Switzerland does not tax private gains on movable assets, this rule bites on a sale in the first five years after the move.
- **Norwegian real estate.** Income, gains and wealth from real estate in Norway can be taxed in Norway _(treaty arts. 6, 13 para. 1, 22 para. 1)_.
- **The company may follow you.** From 2026 a company incorporated under Norwegian law is resident in Norway, and a foreign company with its effective management in Norway is too _(skatteloven § 2-2 seventh paragraph)_. If both states treat the company as resident, the treaty gives residence to the state of its place of effective management _(treaty art. 4 para. 5)_. If a Norwegian company becomes resident in Switzerland, which is outside the EEA, its assets are taxed as if sold the day before _(skatteloven § 10-71 first and second paragraphs)_. Even short of that, a place of management in Switzerland is a permanent establishment _(treaty art. 5 para. 2 letter a)_, and Switzerland can tax the profits attributable to it _(treaty art. 7 para. 1)_. Keep real management (board meetings, decisions, minutes) in Norway if the company is to stay Norwegian.
- **Board fees** paid by a Norwegian company to a Swiss-resident director can be taxed in Norway _(treaty art. 16)_.
- **Pensions** for past employment paid from Norway can be taxed in Norway at no more than 15% _(treaty art. 18)_.
- **Treaty anti-abuse.** A treaty benefit is denied where obtaining it was one of the main purposes of an arrangement _(treaty art. 28a)_.

---

## Part 5: The Swiss landing

- **Ordinary taxation in a canton** is the default. Income and wealth tax rates differ by canton; this skill does not give cantonal rates.
- **Lump-sum taxation (Besteuerung nach dem Aufwand, forfait).** Available to individuals who are not Swiss citizens, who become fully taxable in Switzerland for the first time or after at least ten years away, and who do not work in Switzerland _(DBG art. 14 para. 1)_. For the federal tax, the base is annual living costs, but at least the highest of CHF 435,000 (from 1 January 2026), seven times the annual rent or rental value, or the Swiss-source items listed in the law _(DBG art. 14 para. 3)_. Cantons may offer it and set their own minimum _(StHG art. 6 paras. 1 and 3)_.
- **The Norwegian catch.** Under the treaty, a person who is not subject in Switzerland to the generally levied taxes on all income from Norway that Swiss law taxes generally is not treated as a Swiss resident for the treaty _(treaty art. 4 para. 4)_. A plain lump-sum resident therefore cannot rely on the treaty: no tie-breaker during the 3-year tail and no 15% dividend cap. Swiss law has a modified lump sum for this case: where another state grants relief only if Switzerland taxes the income, the base also includes all income from that state that the treaty assigns to Switzerland _(DBG art. 14 para. 5; StHG art. 6 para. 7)_. Price the modified lump sum against ordinary cantonal taxation; for owners whose assets are mostly Norwegian, ordinary taxation can come out lower.
- **No Swiss tax on private capital gains** on movable assets _(DBG art. 16 para. 3; StHG art. 7 para. 4 letter b)_. Growth after the move escapes both countries, provided the Norwegian exit tax on gains before the move was dealt with and the treaty five-year rule for holdings over 25% does not apply.

---

## Part 6: Sequenced checklist

**Before departure**
1. Count your Norwegian residence years (ten or more means the 3-year tail applies); plan the 61-day budget and the dwelling question for three full income years.
2. Value all shareholdings, compute the deemed gain above NOK 3,000,000 and the exit tax, and choose how to pay (twelfths, or at the end with interest) against liquidity and the chance you return. Remember there is no loss deduction on a move outside the EEA.
3. Decide where the company will be managed, so it does not become Swiss-resident by accident.
4. Decide what happens to each property: the home (it blocks the end of residence), the cabin (year-round water and drainage makes it a dwelling), and investment property (stays taxable in Norway regardless).
5. Choose the Swiss regime: ordinary cantonal taxation or the modified lump sum (a plain lump sum loses the treaty). Compare cantons in writing.

**Departure year**
6. Report the exit gain in the tax return that covers the day before the move (a move or treaty change on 1 January goes in the previous year's return); choose there between paying now, twelfths or payment at the end; provide security; diarise the information duty _(Skatteetaten, Exit tax)_.
7. Register in Switzerland and build the evidence for the treaty tie-breaker (permanent home, centre of vital interests).
8. Tell Norwegian payers (dividend withholding at 15% under the treaty, pensions).

**The three tail years**
9. Log every day in Norway against the 61-day limit; file Norwegian returns as required; claim treaty relief on both sides.
10. Before any dividend from the Norwegian company, price the 0.7 rule.

**After the tail**
11. Claim the end of Norwegian residence in the tax return (search "Emigration", then "Claim for cessation of tax residence (tax emigration)") _(Skatteetaten, Tax emigration)_; keep the 12-year exit tax calendar; within the first five years, price the treaty rule for holdings over 25% before any sale; review the return option before year 12 ends.

---

## The trap list

| Trap | Why it bites |
|---|---|
| 70 days in Norway in a tail year | More than 61 days fails that year's test, and residence continues. |
| Keeping the house "just in case" | A dwelling at your disposal stops residence from ending at all. |
| Assuming the old 5-year wait-out still works | The current § 10-70 has no expiry; the tax is settled within 12 years or cancelled only by moving back. |
| Taking the plain Swiss lump sum | Treaty art. 4 para. 4 denies treaty residence, so no tie-breaker and no 15% dividend cap. |
| A dividend during the deferral | Deferral ends for 0.7 times the distribution. |
| Owner moves, management moves too | The company can become Swiss-resident and trigger company exit tax under skatteloven § 10-71. |
| Dying abroad "solves it" | Not if personal heirs take over the duties; otherwise the deferred tax falls due. |
| Selling a large holding soon after arriving | Treaty art. 13 para. 5 lets Norway tax a sale of more than 25% within five years. |
| Counting on loss relief | Losses are deductible only on a move to an EEA state. |

---

## Sources

| Source | URL | Read on |
|---|---|---|
| Skatteloven § 2-1 (residence, 61 days, 10-year tail, dwelling, wealth tax duty) | https://lovdata.no/lov/1999-03-26-14/§2-1 | 2026-10-30 |
| Skatteloven § 2-2 (company residence from 2026) | https://lovdata.no/lov/1999-03-26-14/§2-2 | 2026-10-30 |
| Skatteloven §§ 4-10, 4-12, 4-19 (wealth valuation) | https://lovdata.no/lov/1999-03-26-14/§4-10 | 2026-10-30 |
| Skatteloven §§ 10-11, 10-31 (1.72 adjustment) | https://lovdata.no/lov/1999-03-26-14/§10-11 | 2026-10-30 |
| Skatteloven §§ 10-70, 10-71 (exit tax, individuals and companies) | https://lovdata.no/lov/1999-03-26-14/§10-70 | 2026-10-30 |
| Skatteloven § 13-2 (anti-avoidance) | https://lovdata.no/lov/1999-03-26-14/§13-2 | 2026-10-30 |
| Stortingets skattevedtak 2026 (FOR-2025-12-18-2747) §§ 2-1, 2-3, 3-2, 3-5 | https://lovdata.no/dokument/STV/forskrift/2025-12-18-2747 | 2026-10-30 |
| Skattebetalingsloven §§ 9-3, 10-51 (wealth tax deferral) | https://lovdata.no/dokument/NL/lov/2005-06-17-67 | 2026-10-30 |
| Skatteetaten, Exit tax (latent gain, basic deduction, security, reporting) | https://www.skatteetaten.no/en/person/to-from-norway/from/tax-when-you-move-abroad/exit-tax/ | 2026-10-30 |
| Skatteetaten, Tax emigration (how to claim) | https://www.skatteetaten.no/en/person/to-from-norway/from/tax-when-you-move-abroad/tax-emigration/ | 2026-10-30 |
| Skatteforvaltningsloven § 12-6 (15-year window) | https://lovdata.no/lov/2016-05-27-14/§12-6 | 2026-10-30 |
| Skatteetaten, Formuesskatt og verdsettingsrabatter (2026) | https://www.skatteetaten.no/satser/formuesskatt/ | 2026-10-30 |
| Skatteetaten, Renter ved utsatt betaling av formuesskatt (2026) | https://www.skatteetaten.no/satser/renter-ved-utsatt-betaling-av-fomuesskatt-beregnet-pa-virksomhetsformue/ | 2026-10-30 |
| Skatteetaten, Forskuddsutskrivingen 2026 | https://www.skatteetaten.no/rettskilder/type/uttalelser/uttalelser/forskuddsutskrivingen-2026/ | 2026-10-30 |
| Norway-Switzerland tax treaty, SR 0.672.959.81, consolidated 26 October 2020, arts. 4, 5, 6, 7, 10, 13, 16, 18, 22, 23, 28a | https://www.fedlex.admin.ch/eli/cc/1989/1356_1356_1356/de | 2026-10-30 |
| Swiss Federal Direct Tax Act (DBG), SR 642.11, as at 2 September 2026, arts. 14, 16 | https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de | 2026-10-30 |
| Swiss Tax Harmonisation Act (StHG), SR 642.14, as at 1 January 2025, arts. 6, 7 | https://www.fedlex.admin.ch/eli/cc/1991/1256_1256_1256/de | 2026-10-30 |

Not yet confirmed: the interest rate under § 10-70 seventh paragraph letter b; what the 7 October 2024 change to § 10-70 altered; how the 2026 wording of § 2-1 seventh paragraph ("bor i riket") applies to a person still resident during the 3-year tail; cantonal income and wealth tax rates and which cantons offer lump-sum taxation (the older version said Zurich and some others have abolished it); whether Switzerland publishes a list of countries that require the modified lump sum (the treaty text itself is relied on here); immigration and residence permits in Switzerland; the risk, named in the older version, that Switzerland treats an active investor as a professional securities trader whose gains are taxable.

---

*Built for the OpenAccountants migration desk. On this corridor the destination is straightforward and the exit is the project: a three-year residence tail, a twelve-year tax calendar, and a company that must not emigrate by accident. Fix the departure date, budget the 61 days, choose the payment path deliberately, and take the treaty-safe Swiss regime, with an adviser on each side.*

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
