---
name: at-svs-contributions
description: Use this skill whenever asked about Austrian SVS (Sozialversicherungsanstalt der Selbständigen) social insurance contributions for self-employed individuals. Trigger on phrases like "SVS contributions", "Austrian social insurance", "GSVG", "self-employed Austria contributions", "Pensionsversicherung self-employed", "SVS Vorschreibung", or any question about social insurance obligations for a self-employed client in Austria. Covers pension (18.5%), health (6.8%), accident (flat monthly), and Selbständigenvorsorge. ALWAYS read this skill before touching any Austria social contributions work.
version: 2.0
jurisdiction: AT
tax_year: 2026
last_updated: 2026-09-22
review_status: pending_review
drafted_by: OpenAccountants
approved_by: pending
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# SVS social insurance contributions for the self-employed in Austria

How the SVS (Sozialversicherungsanstalt der Selbständigen) charges pension, health and accident insurance and the Selbständigenvorsorge to trade licence holders (Gewerbetreibende) and Neue Selbständige under the GSVG, and pension insurance to FSVG freelancers. Figures are for tax year 2026, from SVS pages and the 2026 contribution sheet; the deduction rule is from the USP. Farmers (BSVG) and employees (ASVG) are out of scope.

## Section 1: Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Country | Austria (Republic of Austria) |
| Authority | SVS (Sozialversicherungsanstalt der Selbständigen) |
| Primary legislation | GSVG (Gewerbliches Sozialversicherungsgesetz) |
| Supporting legislation | ASVG; FSVG (Freiberuflich); BSVG (Farmers); BMSVG (Selbständigenvorsorge); EStG |
| Pension rate | See the Section 4 rates table |
| Health rate | See the Section 4 rates table |
| Accident insurance | Fixed monthly amount, not a percentage. See Section 4 |
| Selbständigenvorsorge | Share of the provisional health insurance base. Compulsory for everyone in compulsory GSVG health insurance, including Neue Selbständige. Not compulsory for health insurance by opting in, or for freelancers health insured under GSVG Sections 14a and 14b. Voluntary for freelancers insured only in pension insurance because their profession opted out of GSVG health insurance, such as doctors. See Section 4 |
| Minimum and maximum monthly base | See the Section 4 thresholds table |
| Payment frequency | Charged quarterly (Beitragsvorschreibung); monthly direct debit possible |
| Due dates | 28 February (29 in a leap year), 31 May, 31 August, 30 November |
| Currency | EUR only |
| Contributor | Open Accountants |
| Validated by | Pending: needs an Austrian Steuerberater or Wirtschaftsprüfer |
| Validation date | Pending |

**Monthly contributions at the minimum and maximum base, as SVS prints them**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.svs.at/cdscontent/load?contentid=10008.763406&version=1672393252 |
| Minimum monthly base, pension and health (GSVG) | EUR 551.10 | "Mindest 551,10 101,95 1 Gewerbetreibende/-gesellschafter" |
| Pension contribution at the minimum base (GSVG) | EUR 101.95 | "Mindest 551,10 101,95" |
| Health contribution at the minimum base (GSVG) | EUR 37.48 | "Mindest1) 551,10 37,48 1 Aktive Freiberufler" |
| Maximum monthly base, pension and health | EUR 8,085.00 | "Höchst 8.085,00 1.495,73" |
| Pension contribution at the maximum base (GSVG) | EUR 1,495.73 | "Höchst 8.085,00 1.495,73" |
| Health contribution at the maximum base (GSVG) | EUR 549.79 | "Höchst 8.085,00 549,79" |
| Accident insurance per month, as this sheet prints it | EUR 12.95 | "Monatsbeitrag zur Unfallversicherung: 12,95 Euro" |
| Maximum base per year | EUR 97,020 | "8.085,00 Euro monatlich (97.020 Euro pro Jahr)" |

SVS web pages print a different accident figure (Section 11). No SVS page prints a monthly total, so this Guide states none.

## Section 2: Required inputs and refusal catalogue

### Required inputs

- **Required inputs before computing**:
  1. Registration status: Gewerbetreibender, Neuer Selbständiger, or FSVG freelancer (doctor, pharmacist, patent attorney, civil engineer)?
  2. Income type: gewerbliche or freiberufliche Einkünfte?
  3. Income: the provisional base comes from the third prior year's income (2023 for 2026); the final base comes from the income tax assessment (Einkommensteuerbescheid) of the contribution year itself.
  4. Start year: in the first three years the provisional base is the minimum base; each year's final base follows its own income tax assessment.
  5. Any concurrent employment or pension? ASVG employment can push the GSVG base below the minimum and triggers the Differenzbeitragsvorschreibung at the maximum.
  6. Is the client in compulsory GSVG health insurance? Then the Selbständigenvorsorge is compulsory. Health insurance by opting in, or under GSVG Sections 14a and 14b, does not make it compulsory; pension only insurance makes it voluntary.
- **Unknown registration type stop rule**: If registration type is unknown, STOP; do not compute, since it determines which provisions apply.

### Refusal catalogue

- **R-AT-SVS-1: BSVG farmer regime**. Trigger: activity falls under BSVG (farmers, agriculture). Message: "BSVG farmer social insurance is outside this Guide's scope. Refer to a qualified Steuerberater with agricultural expertise."
- **R-AT-SVS-2: Disability pension interaction**. Trigger: receiving or applying for disability pension while self-employed. Message: "Disability pension interaction with GSVG contributions requires specialist review. Escalate to qualified Steuerberater."
- **R-AT-SVS-3: Cross-border determination**. Trigger: working in multiple EU/EEA states or Switzerland. Message: "Cross-border social insurance determination requires A1 certificate analysis under EU Regulation 883/2004. Escalate to qualified adviser."

### Prohibitions

- **Prohibitions list**:
  - NEVER compute SVS contributions without knowing the registration type.
  - NEVER ignore the minimum and maximum contribution base; clamp to these bounds, except the GSVG base may fall below the minimum with ASVG insurance (Section 7).
  - NEVER tell a new entrant that provisional pension contributions are final; Nachbemessung will occur, except a Gewerbetreibender's health base in the first two calendar years, which is fixed and not re-assessed.
  - NEVER forget that accident insurance is a flat monthly amount, NOT percentage-based.
  - NEVER state SVS contributions are NOT tax-deductible; compulsory GSVG contributions are deductible (Section 6).
  - NEVER confuse the Versicherungsgrenze (Neue Selbständige), the SVS small business income limit (sole traders and FSVG doctors, on application) and the yearly minimum contribution base, even though all three are the same number in 2026 (Section 7).
  - NEVER apply GSVG rules to farmers (BSVG) or to employed persons (ASVG).
  - NEVER present SVS figures as final until the Einkommensteuerbescheid for that year is issued.

## Section 3: Contribution base

Legislation: GSVG Section 25

### Provisional vs final base

- **Provisional/final system**: Until the income tax assessment of a year exists, SVS charges on a provisional base. From year four, it is the third prior year's insurable income plus that year's pension and health contributions, revalued by the factor below and divided by months insured. New entrants (years 1 to 3): the provisional base is the minimum base.

**Provisional base from the fourth year: the SVS worked example**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.svs.at/cdscontent/?contentid=10007.816634&portal=svsportal |
| Insurable income 2023, incl. contributions charged, 10 insured months | EUR 32,000 | "32.000 ab versicherungspflichtigen Einkünften" |
| Revalued total for 2026 (factor 1.181) | EUR 34,784 | "32.000 x 1,181" |
| Provisional monthly base 2026 | EUR 3,478.40 | "(34.784 ÷ 10)" |
| Revaluation factor 2026, applied to 2023 income | 1.181 | "Faktor 2026 : 1,181" |

### Contribution base formula

- **Contribution base formula**: contribution_base = insurable income per the income tax assessment + pension and health contributions charged (vorgeschrieben) for the year + any voluntary unemployment insurance, additional insurance or co-insured-relative supplement, divided by months of compulsory insurance.
- **Hinzurechnung, not a circular calculation**: The contributions added back are those SVS charged for that year (Sources list).

### Gewerbetreibende vs Neue Selbständige

**Gewerbetreibende vs Neue Selbständige**

| Feature | Gewerbetreibende | Neue Selbständige |
| --- | --- | --- |
| Registration | Gewerbeberechtigung (trade licence) | No trade licence; freelancers, IT contractors, etc. |
| Insurance obligation | Automatic on registration (small-business exemption on application, Section 7) | Only if yearly income exceeds the Versicherungsgrenze below, regardless of other work or a pension |
| Health base, first two calendar years | Fixed at the minimum base, not re-assessed | Re-assessed like later years |
| Selbständigenvorsorge | Due (share of the health base) | Due (share of the health base) |
| Accident insurance | Mandatory | Mandatory once insurance obligation triggered |

**Versicherungsgrenze for Neue Selbständige**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.svs.at/cdscontent/?contentid=10007.816855&portal=svsportal |
| Versicherungsgrenze 2026, per year, the same whether or not the client also has a job or a pension | EUR 6,613.20 | "6.613,20 jährlich" |
| Surcharge on pension and health contributions if the tax office reveals the excess | 9.3% | "Beitragszuschlag in Höhe von 9,3 Prozent" |

A client who ends up over the limit pays the insurance and Selbständigenvorsorge contributions later; the surcharge is avoided by reporting the excess within eight weeks of the income tax assessment.

## Section 4: Rates and thresholds (2026)

Legislation: GSVG Sections 25-27; SVS contribution values, 2026

**Rates table**

| Component | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.svs.at/cdscontent/?contentid=10007.816638 |
| Pension insurance (Pensionsversicherung), GSVG | 18.5% | "beträgt der Beitragssatz in der Pensionsversicherung 18,50 Prozent" |
| Health insurance (Krankenversicherung), GSVG | 6.8% | "in der Krankenversicherung 6,8 Prozent" |
| Pension insurance, FSVG | 20% | "beträgt der Beitragssatz in der Pensionsversicherung 20 Prozent" |
| Accident insurance (Unfallversicherung), fixed per month | EUR 12.96 | "12,96 monatlich" |
| Selbständigenvorsorge, share of the provisional health base | 1.53% | "Selbständigenvorsorge beträgt 1,53 Prozent" |
| Minimum monthly base, first three years (pension and health) | EUR 551.10 | "551,10 monatlich in der Pensionsversicherung" |

An FSVG-only freelancer who chooses the Selbständigenvorsorge pays the same share of the provisional pension base instead.

**Thresholds table**

| Threshold | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.svs.at/cdscontent/?contentid=10007.816635&portal=svsportal |
| Maximum contribution base, per year | EUR 97,020.00 | "97.020,00" |
| Minimum contribution base, per year of full insurance (twelve times the monthly minimum; for fewer insured months the monthly minimum applies per month) | EUR 6,613.20 | "6.613,20 begrenzt" |
| Fixed health base, Gewerbetreibende, first two calendar years, per month | EUR 551.10 | "Wert 2026" |

The monthly minimum and maximum are in the Section 1 table.

### Voluntary higher health coverage (Krankengeld opt-in)

Legislation: GSVG Zusatzversicherung (section number not confirmed on an allowed page)

**Krankengeld opt-in table**

| Option | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.svs.at/cdscontent/?contentid=10007.816678&portal=svsportal |
| Zusatzversicherung, share of the provisional health base | 2.5% | "Zusatzversicherung beträgt 2,5 Prozent" |
| Minimum monthly contribution | EUR 30.77 | "Mindestbeitrag" |
| Maximum monthly contribution | EUR 202.13 | "202,13 monatlich" |

**Krankengeld and Unterstützungsleistung amounts**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.svs.at/cdscontent/?contentid=10007.816735&portal=svsportal |
| Krankengeld, share of daily contribution base | 60% | "Ihrer täglichen Beitragsgrundlage" |
| Krankengeld, daily minimum | EUR 11.02 | "11,02" |
| Source | all figures below | https://www.svs.at/cdscontent/?contentid=10007.816734&portal=svsportal |
| Unterstützungsleistung per day, not income-related | EUR 40.04 | "40,04 (Wert 2026 )" |

- **Krankengeld opt-in details**: Zusatzversicherung Krankengeld runs from day 4 of incapacity for at most 26 weeks, after a six-month wait (waived after a post-application work accident). It must start before age 60, begins the month after application (or with compulsory insurance if applied within four weeks of the notice), and is not re-assessed. Separately, with no opt-in, the Unterstützungsleistung pays from day 4 once incapacity exceeds 42 days, for at most 20 weeks, to owners with fewer than 25 staff whose business depends on their own work. Both benefits are taxable business income.

## Section 5: Computation steps

Legislation: GSVG Sections 25-27

### Step 5.1: Determine provisional monthly contribution base

- **Provisional base formula**: IF new_entrant (years 1 to 3): provisional_base = minimum_contribution_base (Section 1). ELSE: provisional_base = (income_of_third_prior_year + contributions_charged_that_year) x revaluation factor / months_insured_that_year (Section 3). provisional_base = clamp(provisional_base, minimum_base, maximum_base). The client may apply to lower or raise it (EC3).

### Step 5.2: Compute monthly contributions

- **Monthly contributions formula**: pension_monthly = provisional_base x pension rate; health_monthly = provisional_base x health rate; accident_monthly = fixed accident amount; vorsorge_monthly = provisional health base x Selbständigenvorsorge rate; total_monthly = sum of the four (rates and the accident amount are in the Section 4 rates table). The full monthly contribution is due even if the activity starts mid-month (Sources list).

### Step 5.3: Compute quarterly payment

- **Quarterly payment formula**: quarterly_payment = total_monthly x 3

### Step 5.4: Final reconciliation (Nachbemessung)

- **Final reconciliation formula**: final_base_monthly = (insurable income per the assessment + pension and health contributions charged for the year) / months insured, clamped to the minimum and maximum base; recompute pension and health at the same rates. adjustment = final minus provisional contributions. IF positive: Nachbelastung, in four instalments from next year's first quarter if still insured (twelve quarters on application in the first three years). IF negative: Gutschrift. Accident insurance, Selbständigenvorsorge, and a Gewerbetreibender's first-two-calendar-year health base are NOT re-assessed (Sources list).

## Section 6: Payment schedule and tax deductibility

Legislation: GSVG Section 35; EStG Section 4(4)

### Payment schedule

**Payment schedule table**

| Quarter | Covers | Due date |
| --- | --- | --- |
| Q1 | January to March | 28 February (29 in a leap year) |
| Q2 | April to June | 31 May |
| Q3 | July to September | 31 August |
| Q4 | October to December | 30 November |

Source for the due dates: https://www.svs.at/cdscontent/?contentid=10007.816647&portal=svsportal

- **Late payment and Vorschreibung notes**: If unpaid within 18 days of the due date, SVS sends a reminder and charges late interest (Verzugszinsen) from the 16th day after the due date; no allowed page prints the rate. SVS can offer a lower provisional base, a payment plan or deferral (Sources list).

### Tax deductibility

**Tax deductibility table**

| Question | Answer |
| --- | --- |
| Are SVS contributions deductible from taxable income? | YES; GSVG contributions are deductible separately, even under the flat-rate expense method (USP Basispauschalierung page, Sources) |
| Which contributions are deductible? | Compulsory GSVG and Selbständigenvorsorge contributions (same page). Zusatzversicherung contributions too (SVS) |
| When are they deductible? | Legacy text: in the year paid; not confirmed on an allowed page (Section 11) |
| Does the Nachbemessung payment also get deducted? | Legacy text: yes, in the year paid; not confirmed on an allowed page (Section 11) |

## Section 7: Special regimes and concurrent activity

### Kleinstunternehmerregelung (small business exemption)

- **Kleinstunternehmerregelung rule**: The VAT small business exemption (see the Austrian VAT Guide) does not itself change SVS obligations. SVS has its own exemption from GSVG pension and health insurance (or FSVG pension insurance) for sole traders and FSVG doctors, on application. Both limits in the table below must be met: income from the self employed activity AND turnover from all business activities. Age conditions: under 57, the client may not have been compulsorily insured under the GSVG or FSVG for more than twelve months in the last 60 calendar months; from 57 until the women's standard pension age, the limits must have been met in the last five calendar years; from that age, the limits apply to the current year. Not available to Neue Selbständige (they use the Versicherungsgrenze) or to partners. Accident insurance stays. It starts at the earliest on 1 January of the application year, never retroactively; SVS checks it later against the tax assessments.

**SVS small business exemption limits**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.svs.at/cdscontent/?contentid=10007.816718&portal=svsportal |
| Yearly income limit 2026 | EUR 6,613.20 | "Einkommensgrenze" |
| Yearly turnover limit 2026 | EUR 55,000.00 | "Umsatzgrenze" |

The same yearly number serves three separate rules in 2026. (a) Versicherungsgrenze: a Neuer Selbständiger with yearly income at or below it is not insured at all; no application is needed, and there is no turnover test and no age test. (b) SVS small business exemption: a sole trader or FSVG doctor at or below it, and at or below the turnover limit, who meets the age and prior insurance conditions, may apply to leave pension and health insurance; accident insurance stays. (c) Minimum contribution base: an insured person whose income is lower still pays on this base. Never apply one rule's consequence to another rule's group.

Conditions: https://www.svs.at/cdscontent/?contentid=10007.846813&portal=svsportal

### Concurrent ASVG employment (Differenzvorschreibung)

- **Concurrent ASVG employment rule**: Client is employed (ASVG) and self-employed (GSVG); each base is computed separately, but the combined bases for the year are capped at the monthly maximum base times total months of compulsory insurance, for pension AND health. If the cap is (expected to be) exceeded, SVS automatically issues a Differenzbeitragsvorschreibung: ASVG ranks first, so the GSVG base is set low enough to keep the total under the cap. Checked again once all bases are final, which can mean back-payments or refunds. The GSVG base may also fall below the GSVG minimum: if the ASVG base already reaches it, a client with a loss or no assessment pays no GSVG pension or health contributions. For health benefits the client picks which insurer to claim from. The Selbständigenvorsorge is then computed on the reduced (Differenz) base (Sources list).

### Retirement while self-employed

- **Retirement while self-employed rule**: Client drawing a pension but continuing self-employment: legacy text says GSVG pension contributions continue and add to entitlements, and health insurance depends on the coverage choice. Not confirmed on an allowed page. Confirm with SVS before advising. The compulsory Selbständigenvorsorge stops automatically once the client draws an own pension (https://www.svs.at/selbstaendigenvorsorge).

## Section 8: Edge case registry

### EC1: New entrant in first 3 years

Situation: Client started self-employment 18 months ago, no prior tax assessment available.
Resolution: Provisional base = minimum contribution base (Section 1), plus the Selbständigenvorsorge share. Warn the client: pension will be re-assessed, and high income means a large back-payment. For a Gewerbetreibender the health base of the first two calendar years stays fixed; a July start keeps it fixed for 18 months, because the rule counts calendar years.

### EC2: Income below insurance threshold (Neue Selbständige)

Situation: Freelancer expects income below the Versicherungsgrenze and has no other employment.
Resolution: Below the Versicherungsgrenze (Section 3), there is no GSVG compulsory insurance, whether or not the client has other work or a pension. A client can declare at registration that they will stay below it, and may opt into health and accident cover; SVS checks actual income later. A client outside insurance has NO health or pension coverage: flag this.

### EC3: Opting to increase provisional base

Situation: Client knows current-year income will be much higher than in the third prior year.
Resolution: The client can apply to raise the provisional base (Hinaufsetzung) up to the maximum, stating the expected final base; this avoids a large Nachbemessung later. SVS warns: an over-estimate creates a large credit, and a raised base can become final for the pension if a pension starts first. A founder can also apply, at the latest with the pension application, to raise the first three calendar years' pension base to the maximum (Hinaufsetzung pages, Sources list).

### EC4: Multiple activities

Situation: Client has a Gewerbeberechtigung AND freelance (Neue Selbständige) income.
Resolution: Legacy text: all self-employed income combines into one GSVG contribution base, with no double insurance obligation; not confirmed on an allowed page for this refresh (Section 11). Flag if activities fall under different regimes (GSVG vs FSVG).

### EC5: Cross-border EEA worker

Situation: Client lives in Austria but performs work in Germany.
Resolution: Under EU Regulation 883/2004, social insurance is generally due in only one member state. Self-employed in Austria and employed abroad: the country of employment's law applies and Austria is insurance-free. Employed in Austria and self-employed abroad: Austrian law applies and SVS asks for the foreign tax assessment (Sources list). Other combinations need an A1 certificate determination; escalate to reviewer.

## Section 9: Reviewer escalation protocol

When a situation requires reviewer judgement:

~~~
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Qualified Steuerberater must confirm before advising client.
~~~

When a situation is outside Guide scope:

~~~
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside Guide scope]
Action Required: Do not advise. Refer to qualified Steuerberater. Document gap.
~~~

## Section 10: Test suite

### Test 1: New entrant, minimum base

Input: Gewerbetreibender, year 1, no prior income data.
Expected output: Minimum base. Pension and health as printed in Section 1; accident from the Section 4 rates table (see Section 11 on the two printed accident values); plus Selbständigenvorsorge. Health is final for the first two calendar years; pension is re-assessed.

### Test 2: Established self-employed, mid-range income

Input: Gewerbetreibender, fourth year or later, the SVS example in Section 3.
Expected output: Provisional base as in that table; apply the Section 4 rates, accident amount and Selbständigenvorsorge. Quarterly charge = three months.

### Test 3: High income, maximum base applies

Input: Gewerbetreibender with income well above the maximum base.
Expected output: Base capped at the maximum. Pension and health as printed in Section 1; accident from the Section 4 rates table (see Section 11 on the two printed accident values); plus Selbständigenvorsorge.

### Test 4: Neue Selbständige below threshold

Input: Freelance income below the Versicherungsgrenze, no other employment.
Expected output: No GSVG obligation. Flag: no social insurance cover unless the client opts in. Same answer if also employed.

### Test 5: Concurrent employment

Input: Employed (ASVG) and self-employed (GSVG), combined bases over the yearly cap.
Expected output: Differenzbeitragsvorschreibung. ASVG ranks first; the GSVG pension AND health base is cut to keep the total within the cap. Reviewed once all bases are final. Accident insurance is a flat amount.

### Test 6: Nachbemessung scenario

Input: Gewerbetreibender on the minimum base in year 1; the assessment shows income far above it.
Expected output: Pension re-assessed; back-payment in four quarterly instalments from next year's first quarter, or twelve quarters on application. Health, accident and Selbständigenvorsorge NOT re-assessed.

### Test 7: Krankengeld opt-in

Input: GSVG self-employed, under 60, opts into the Zusatzversicherung.
Expected output: Extra contribution at the Section 4 rate, within its minimum and maximum. Krankengeld from day 4 after a six-month wait. "Day 43" belongs to the separate Unterstützungsleistung.

## The method, step by step

1. Establish which law covers the client: Gewerbetreibender (automatic, trade licence), Neuer Selbständiger (only above the Versicherungsgrenze) or FSVG freelancer; check the small business exemption and Versicherungsgrenze first (Sections 3 and 7).
2. Fix the provisional base: the minimum base in the first three years (Section 4); from year four, third-prior-year income plus contributions, revalued, divided by months insured (Section 3).
3. Apply the rates and fixed accident amount, add Selbständigenvorsorge, and cap at the maximum base; allow for the Differenzbeitragsvorschreibung with ASVG employment (Section 7).
4. Pay the quarterly Beitragsvorschreibung by the Section 6 due dates; consider applying to raise or lower the provisional base if income differs a lot.
5. On the year's income tax assessment, SVS finalises the base and re-assesses pension and health (Nachbemessung), with the Section 5.4 exceptions.
6. Deduct the compulsory contributions as business expenses (Section 6).

## Ask the client first

- Do you hold a trade licence (Gewerbeberechtigung), or are you a freelancer, or a doctor, pharmacist, patent attorney or civil engineer?
- In which year did your compulsory SVS insurance start (the first two calendar years fix the health base for trade licence holders; the first three set the provisional base)?
- What was your income in 2023, and what income do you expect this year?
- Are you also employed, or do you draw a pension?
- If you have no trade licence: will your yearly income stay under the Versicherungsgrenze? (Neue Selbständige only; there is no turnover test.)
- If you are a sole trader with a trade licence or a doctor under the FSVG: will your yearly income and your turnover stay under both SVS small business limits, and do you meet the age and prior insurance conditions? (Only on application.)
- Do you work in another EU/EEA country or Switzerland?

## When to refuse or refer

- Farmers and agricultural side activities (BSVG): out of scope.
- FSVG freelancers beyond the pension rate in Section 4.
- Disability pension, or any pension drawn alongside self-employment.
- Work in more than one EU/EEA state or Switzerland (A1 determination).
- Sale or restructuring gains that SVS may deduct from the base on application.
- Arrears, enforcement or deferral requests.

## Section 11: For the accountant who adopts this Guide

- Accident insurance: SVS web pages print EUR 12.96 a month for 2026; the contribution sheet prints EUR 12.95 (both tables above). Confirm which SVS charges.
- Legislation references (GSVG Sections 25-27, 27a, 28a, 35, ASVG Section 74, BMSVG Sections 52-53) are legacy and could not be checked; RIS is not an allowed host.
- Timing of the tax deduction (year of payment), the treatment of Nachbemessung payments, combining several self-employed activities into one base (EC4), and the retirement rule (Section 7) are legacy statements not confirmed on an allowed page.

## Sources

- https://www.svs.at/cdscontent/load?contentid=10008.763406&version=1672393252
- https://www.svs.at/cdscontent/?contentid=10007.816638
- https://www.svs.at/cdscontent/?contentid=10007.816634&portal=svsportal
- https://www.svs.at/cdscontent/?contentid=10007.816635&portal=svsportal
- https://www.svs.at/cdscontent/?contentid=10007.816610&portal=svsportal
- https://www.svs.at/cdscontent/?contentid=10007.816715&portal=svsportal
- https://www.svs.at/cdscontent/?contentid=10007.816718&portal=svsportal
- https://www.svs.at/cdscontent/?contentid=10007.816855&portal=svsportal
- https://www.svs.at/cdscontent/?contentid=10007.846813&portal=svsportal
- https://www.svs.at/cdscontent/?contentid=10007.816647&portal=svsportal
- https://www.svs.at/cdscontent/?contentid=10007.816712&portal=svsportal
- https://www.svs.at/cdscontent/?contentid=10007.816650&portal=svsportal
- https://www.svs.at/cdscontent/?contentid=10007.816651&portal=svsportal
- https://www.svs.at/cdscontent/?contentid=10007.816720&portal=svsportal
- https://www.svs.at/cdscontent/?contentid=10007.849620&portal=svsportal
- https://www.svs.at/cdscontent/?contentid=10007.816694&portal=svsportal
- https://www.svs.at/cdscontent/?contentid=10007.816678&portal=svsportal
- https://www.svs.at/cdscontent/?contentid=10007.816735&portal=svsportal
- https://www.svs.at/cdscontent/?contentid=10007.816734&portal=svsportal
- https://www.svs.at/selbstaendigenvorsorge
- https://www.usp.gv.at/themen/mitarbeiter-und-gesundheit/beendigung-des-arbeitsverhaeltnisses/weitere-informationen-beendigung/pflichtmodell-fuer-gewerbetreibende-und-neue-selbststaendige.html
- https://www.usp.gv.at/themen/steuern-finanzen/steuerliche-gewinnermittlung/weitere-informationen-zur-steuerlichen-gewinnermittlung/pauschalierung-weitere-infos/basispauschalierung-einkommensteuer.html

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

> Contributed by OpenAccountants.

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
