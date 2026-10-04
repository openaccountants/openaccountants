---
name: cyprus-tax-optimization
description: Use this skill whenever asked about reducing tax in Cyprus, tax planning, or legal strategies to minimise tax for an individual, freelancer, or company in Cyprus. Trigger on phrases like "reduce tax Cyprus", "Cyprus non-dom", "non-domiciled", "0% dividend tax", "SDC exemption", "Cyprus IP box", "3% tax IP", "Cyprus company dividends", "60-day rule", "save tax Cyprus", "tax planning Cyprus". This skill covers the non-dom regime (17 years 0% SDC on dividends/interest/rents), the company-plus-dividend extraction structure, the IP Box (~3% on qualifying IP), self-employment vs company, the personal-income reliefs, and the substance/anti-avoidance red lines. ALWAYS read this skill before advising on any Cyprus tax optimisation.
version: 0.1
jurisdiction: CY
tax_year: 2026
last_updated: 2026-10-02
authored_by: OpenAccountants team
review_status: pending_review
trust_label: Written by the OpenAccountants team
category: tax-optimization
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Cyprus tax planning: the legal levers after the 2026 reform

This Guide sets out the lawful ways a person or a company in Cyprus can lower tax, and the condition that each one depends on. Figures are for tax year 2026. The 2026 tax reform (Law 244(I)/2025 for income tax, in force from 1 January 2026, and the amended Special Defence Contribution law) changed most of the old planning figures, so do not reuse pre-2026 numbers. Every lever below rests on a rule printed by the Tax Department. Where a lever needs a judgement (domicile, substance, management and control, the IP box), the Guide describes the rule and refers the work to a Cyprus tax adviser. For the full income tax computation use `cyprus-income-tax`; for domicile and Special Defence Contribution (SDC) detail use `cy-non-dom`; for VAT use `cyprus-vat-return`.

## Section 1: Quick reference

| Field | Value |
| --- | --- |
| Country | Republic of Cyprus |
| Authority | Tax Department (Ministry of Finance), www.gov.cy/mof-tax |
| Currency | EUR |
| Tax year | Calendar year |
| Main levers | Non-domiciled status (no SDC on dividends and interest); the company route (corporate tax, then dividends); the new-resident employment exemptions; the special rates on crypto gains, approved share plans (not for a shareholder-director who is a connected person) and foreign pensions |
| Lever that needs an adviser | The IP box (article 9, paragraph (k), of the Income Tax Law, "nexus"): no allowed page prints its percentage; see Section 4 |
| Anti-avoidance | General anti-abuse rule, article 33A, extended from 2026 to arrangements involving individuals |

### Personal income tax scale, from tax year 2026

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/media/sites/167/2026/05/FAQs-110526.pdf |
| Rate on chargeable income up to the tax-free amount | 0% | "Φορολογικός συντελεστής" (tax rate) |
| Tax-free amount (top of the 0% band), per individual | EUR 22,000 | "Το αφορολόγητο ποσό" (the tax-free amount) |
| Rate on the next slice, up to the amount in the next row | 20% | "Φορολογικός συντελεστής" (tax rate) |
| Top of the 20% band | EUR 32,000 | "Φορολογητέο εισόδημα" (taxable income) |
| Rate on the next slice | 25% | "Φορολογικός συντελεστής" (tax rate) |
| Top of the 25% band | EUR 42,000 | "Φορολογητέο εισόδημα" (taxable income) |
| Rate on the next slice | 30% | "Φορολογικός συντελεστής" (tax rate) |
| Top of the 30% band | EUR 72,000 | "Φορολογητέο εισόδημα" (taxable income) |
| Top rate, on chargeable income above the top of the 30% band | 35% | "και άνω" (and above) |

## Section 2: Non-domiciled status and Special Defence Contribution

### Who pays SDC

SDC is charged only on a "resident of the Republic" for SDC purposes. The Tax Department defines that as an individual who is Cyprus tax resident for income tax AND has a domicile in Cyprus. An individual who is either not domiciled in Cyprus (non-domiciled) OR not Cyprus tax resident is not subject to SDC on interest income or dividend income. Rental income was subject to SDC up to and including tax year 2025 only. SDC on rent is abolished from 1 January 2026 for everyone, so it is no longer a planning point.

### Tax residence (income tax)

An individual is Cyprus tax resident under either of two tests:

- The 183-day rule: they stay in Cyprus for one or more periods exceeding 183 days in total in the tax year. The day of arrival counts as a day in Cyprus; the day of departure counts as a day outside.
- The 60-day rule: they meet ALL of these in the tax year: at least 60 days in Cyprus; not resident for more than 183 days in any other country; they carry on a business in Cyprus and/or are employed in Cyprus or hold an office in Cyprus; and they keep a permanent residence in Cyprus that they own or rent. If the Cyprus business or employment ends during the year, they stop being resident under this rule for that year.

From 1 January 2026 the 60-day rule applies whether or not the person is also tax resident in another country; the other 60-day conditions still apply.

### Domicile

- In general an individual is domiciled in Cyprus if their domicile of origin is in Cyprus.
- A person with a Cypriot domicile of origin may be treated as not domiciled if they acquired and keep a domicile of choice outside Cyprus AND were not Cyprus tax resident for at least 20 consecutive years immediately before the tax year, OR they resided abroad for more than 20 consecutive years before 16 July 2015.
- Whatever their domicile of origin, an individual who has been Cyprus tax resident for at least 17 out of the last 20 years immediately before the tax year is deemed domiciled in Cyprus. They keep that domicile until they complete 20 years in which they are not Cyprus tax resident.
- A person who considers they are not domiciled may apply for exemption from SDC on Form T.D.38.

### Extending non-dom treatment past the 17-year point (article 3D, from 2026)

An individual who does NOT have a Cypriot domicile of origin, and who becomes deemed domiciled under the 17-of-20-years rule, may elect the Alternative Method of Imposition of SDC. Under it they extend the exemption for up to two further five-year periods by paying the lump sum in the table below for each five-year period. The election is irrevocable, needs a separate application and approval for each five-year period, and the amount is not refundable for any reason and is not set off against other tax liabilities or credits. The application (Form TD 631) is filed through the Tax For All (TFA) portal by 30 June of the first year of the five-year period it covers, or up to two years in advance. The lump sum for the whole five-year period is due by the end of the month after the month in which the Commissioner approves the application. The required documents include a clean criminal record certificate and a Tax Department certificate of non-domicile. A person with a Cypriot domicile of origin cannot use this route.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/media/sites/167/2026/06/Application-Extension-of-Non-Dom.pdf |
| Lump-sum SDC for the whole five-year extension period (paid once per period, up to two periods) | EUR 250,000 | "for the entire 5‑year period" |

The residency page states the same rule ("by paying" the amount "for each five-year period"): https://www.gov.cy/mof-tax/en/documents/tax-residency-domicility/

### SDC rates for a resident AND domiciled individual (and the company rules)

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/media/sites/167/2026/03/EEA-%CE%A6%CE%9A%CE%9A-%CE%9C%CE%95%CE%A4%CE%91%CE%A1%CE%A1%CE%A5%CE%98%CE%9C%CE%99%CE%A3%CE%97-06032026.pdf |
| SDC on dividends received by an individual, out of profits of 2026 onward | 5% | "Άτομα σε ποσοστό" (individuals at) |
| SDC on dividends received by an individual from a Cyprus-resident company up to and including 31/12/2031, paid out of profits of the 8 tax years up to and including 2025 | 17% | "μέχρι και το φορολογικό έτος 2025" |
| SDC on interest received by or credited to an individual (general rate) | 17% | "τόκο που λαμβάνει ή πιστώνεται" |
| Deemed distribution: share of a Cyprus-resident company's profits of tax years 2024 and 2025 only, deemed distributed two years after the end of the year the profits relate to | 70% | "στα φορολογικά έτη 2024 και 2025" |
| SDC on that deemed distribution | 17% | "λογιζόμενη διανομή" (deemed distribution) |
| SDC on a disguised (hidden) dividend distribution, new article 3A from 2026 | 10% | "συγκεκαλυμμένη διανομή" (disguised distribution) |

What this means for planning:

- The 5% rate applies to dividends out of profits of 2026 onward. A dividend paid out of profits of 2025 or earlier is still charged at the 17% rate in the table above when it falls within that row's conditions. The Tax Department's own example: an individual who in 2027 receives one dividend from 2025 profits and one from 2026 profits pays the 17% rate on the first and the 5% rate on the second. Ask which year's profits a dividend comes out of.
- The deemed distribution rule now covers only profits of tax years 2024 and 2025. It is abolished for profits of 2026 onward. It applies only to the share of profits that belongs, directly or indirectly, to an individual who is resident (resident AND domiciled, for SDC) on the date of the deemed distribution. No SDC is charged on an actual dividend paid out of profits that were already treated as distributed.
- The disguised distribution rule (article 3A) applies to individuals resident for SDC purposes in their dealings with a Cyprus-resident company. It catches the market value of a company asset used by a shareholder or a person connected with them, and the difference between market value and the price when the company passes an asset to a shareholder or connected person. Do not plan a shareholder's private use of company property as tax-free.
- SDC does not apply to a non-domiciled or non-resident individual on dividends or interest (see "Who pays SDC" above), so these rates matter only for a resident AND domiciled individual.

### General Healthcare System (GHS) contribution still applies

Dividend income of a Cyprus tax resident is not subject to income tax, but it IS subject to SDC (if domiciled) and to the GHS contribution. Non-dom status removes SDC only; it does not remove GHS; only the insurance-abroad exemption described in step 2 of Section 3 does (EEA state, Switzerland or an exempt international organisation; S1, A1 or a Ministry of Health exemption certificate). The 2025 return guide states that the general GHS rate applies to all income except self-employed income, which has its own rate (see the self-employed table in Section 3). The general rate and the annual cap are in the table below.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/media/sites/167/2026/02/IR59_2026_English__.pdf |
| GHS contribution rate withheld on employment income (Form T.D.59A 2026) | 2.65% | "you must withhold" |
| Annual income above which GHS withholding stops (all listed income added together) | EUR 180,000 | "stop withholding" |

Return guide wording on dividends: https://www.gov.cy/media/sites/167/2026/06/Guide-for-completion-of-tax-return-2025.pdf

**AUDIT FLASH POINT.** Non-dom status rests on genuine Cyprus tax residence (183-day or 60-day rule) and on facts about domicile. The 60-day rule needs a real Cyprus business, employment or office AND a permanent home owned or rented in Cyprus. Confirm both tests before relying on any SDC exemption.

## Section 3: The company route, compared with self-employment

### Corporate tax and the company's residence

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/media/sites/167/2026/03/2026-%CE%A6%CE%BF%CF%81%CE%9C%CE%B5%CF%84%CE%B1%CF%81%CF%81%CF%8D%CE%B8%CE%BC%CE%B9%CF%83%CE%B7-%CE%A6%CF%8C%CF%81%CE%BF%CF%82-%CE%95%CE%B9%CF%83%CE%BF%CE%B4%CE%AE%CE%BC%CE%B1%CF%84%CE%BF%CF%82.pdf |
| Corporate income tax rate, from 1 January 2026 | 15% | "Από την 1/1/2026, οι εταιρείες" |
| Additional (super) deduction for scientific research and R&D spending, extended up to and including tax year 2030 | 20% | "επιπρόσθετης έκπτωσης" (additional deduction) |
| Special rate on gains from disposing of crypto-assets (new article 20E), for any person; disposal of crypto-assets acquired by mining is excluded and taxed normally; crypto losses offset only against same-year crypto gains | 8% | "κρυπτοστοιχείων" (crypto-assets) |
| Special rate on the benefit from an approved employee or director share option or share award plan (new article 20D), for an employee or director who is Cyprus resident and is NOT a connected person of the employer company (article 33), with a minimum 3-year vesting period, taxed separately; capped at twice that person's income from the employer in the year the vesting period ends and at the amount in the next row | 8% | "δεν προστίθεται σε οποιοδήποτε άλλο εισόδημα" (not added to other income) |
| Cap on the share-plan benefit taxed at the special rate, per rolling ten-year period | EUR 1,000,000 | "ανά κυλιόμενη δεκαετία" (per rolling decade) |
| Optional special rate on a pension for services rendered abroad, on the amount above the threshold in the next row | 5% | "δύναται" (may) |
| Annual foreign-service pension threshold, from 2026 | EUR 5,000 | "Αυξάνεται το όριο" (the limit is raised) |

An owner-manager who is a connected person of the company cannot use the article 20D rate.

Company residence, from 2026: a company is Cyprus resident if it is managed and controlled in Cyprus (unchanged), OR if it is incorporated in Cyprus under the Companies Law, unless a double tax treaty provides otherwise. A company that moves its registered office or seat to Cyprus is treated as incorporated in Cyprus. The old condition that the company must not be resident in another state was deleted. Tax losses can now be carried forward for 7 years instead of 5.

### How the route works, and its limits

1. The company pays corporate tax at the rate in the table above on its taxable profit.
2. Dividends paid to a Cyprus tax resident individual are not subject to income tax. They bear SDC only if the shareholder is resident AND domiciled (Section 2 rates), and they bear the GHS contribution up to the annual cap in Section 2, unless the person is insured in another EEA state, Switzerland or an exempt international organisation and holds an S1 or A1 document or a Ministry of Health exemption certificate.
3. Salary paid by the company to the owner as an employee is employment income, taxed on the personal scale in Section 1; employee and employer social insurance and the GHS contribution also apply. Use `cyprus-income-tax` and `cyprus-payroll` for the computation and the deductions.
4. Do not quote a combined or "effective" rate. Model the client's actual figures with an adviser: the result depends on SDC status, the profit year behind each dividend, GHS, social insurance on any salary, and the deemed distribution rule for 2024 and 2025 profits.

The disguised distribution rule (Section 2) and the general anti-abuse rule (Section 6) apply to the route. A company with no real management in Cyprus may still be resident by incorporation, but treaty residence and substance questions go to an adviser.

### Self-employment

A self-employed individual is taxed on profits on the personal scale in Section 1, and pays social insurance and GHS on top.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.businessincyprus.gov.cy/social-insurance-registration-and-contributions/ |
| Social insurance paid by a self-employed person on insurable income (the state adds its own share) | 16.6% | "paid by the self-employed" |
| Annual income above which a self-employed individual must submit audited financial statements | EUR 70,000 | "audited financial statements" |

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/media/sites/167/2026/06/Guide-for-completion-of-tax-return-2025.pdf |
| GHS rate on self-employed income (2025 return guide; no 2026 guide yet) | 4% | "self- employed taxpayers" |

## Section 4: IP box

Cyprus has an IP box under article 9, paragraph (k), of the Income Tax Law, which the Tax Department labels "IP Box regime" with the word "nexus". No allowed government page that we could read prints the deduction percentage, the nexus calculation or the qualifying-asset list, so this Guide states no percentage, no effective rate and no qualifying conditions for it. One interaction is printed: the additional R&D deduction in the Section 3 table is NOT granted for an intangible asset if the IP box provisions were claimed for that same asset in any tax year. Refer every IP box question to a Cyprus tax adviser.

## Section 5: Personal reliefs and new-resident exemptions

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/media/sites/167/2026/06/Article-8-21B-of-the-Income-Tax-Law-N.118-I-2002.pdf |
| Article 8(21B) exemption on remuneration from employment in Cyprus or profits of business in Cyprus | 25% | "can claim an income tax exemption" |
| Gross earnings the person must exceed in the year (and in the first 12 months) | EUR 30,000 | "has gross earnings exceeding" |
| Maximum exemption per tax year | EUR 25,000 | "cannot exceed" |

Article 8(21B) conditions, ALL required: not Cyprus tax resident in the 7 years before starting work or business in Cyprus (for a 2026 start, 2019 to 2025); Cyprus tax resident in some year before those 7 years; started employment or self-employment between 1/1/2025 and 31/12/2030; earnings above the threshold in the first 12 months; and either a recognised university degree plus at least 36 months of full-time work abroad for a foreign employer in the 84 months before, OR at least 84 months of full-time work abroad for a foreign employer. It runs for 7 consecutive tax years from the start year, but only in years when earnings exceed the threshold and (except the start year) the person is Cyprus tax resident.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/media/sites/167/2026/06/%CE%A0%CE%AF%CE%BD%CE%B1%CE%BA%CE%B1%CF%82-%CE%B1%CF%80%CE%B1%CE%BB%CE%BB%CE%B1%CE%B3%CF%8E%CE%BD-823-%CE%BA%CE%B1%CE%B9-823%CE%91.pdf |
| Article 8(23A) exemption on remuneration from first employment in Cyprus (employment from 1/1/2022) | 50% | "απαλλαγή της αμοιβής" (exemption of remuneration) |
| Minimum remuneration for article 8(23A) | EUR 55,000 | "Ελάχιστη αμοιβή" (minimum remuneration) |

Article 8(23A): granted for 17 years. The person must not have been Cyprus tax resident for at least 10 years before the year the first employment in Cyprus started; where the employment starts after 15 consecutive tax years without any employment in Cyprus, the test is at least 15 years. For the first-employment limb the table also says the exemption ends when the first employment ends, if that is earlier. The exemptions apply whether or not the person becomes Cyprus tax resident after starting work. The older article 8(23) (employment from 2012 to 2021) is not covered here.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/media/sites/167/2026/02/IR59_2026_English__.pdf |
| Article 8(21) and 8(21A) maximum exemption per tax year (20% of remuneration from any employment in Cyprus, for a person who started first employment in Cyprus) | EUR 8,550 | "with a maximum of" |

Article 8(21A) covers employment started between 26/7/2022 and 31/12/2027 by a person employed abroad by a non-resident employer for the 3 consecutive years before; it runs 7 years from the year after first employment starts, or until that first employment ends if earlier, with no minimum pay. Conditions table: https://www.gov.cy/media/sites/167/2026/01/implementation-of-sections-21-and-21A-of-article-8-24072023.pdf

The personal deductions (children, rent or housing-loan interest, green spending, insurance and contributions) are in `cyprus-income-tax`.

## Section 6: Red lines (do not cross)

- **Substance and management.** Since 2026 a company incorporated in Cyprus is resident unless a double tax treaty says otherwise; a company not incorporated here is resident only if it is managed and controlled in Cyprus. Where a treaty decides residence, or another country also claims the company, refer to an adviser. Do not present a company with no real activity or management as a planning tool.
- **Residence must be real.** Meet the day-count and tie tests in Section 2. Never construct residence on paper.
- **IP box.** The regime is labelled "nexus" by the Tax Department and its conditions are not printed on an allowed page here; refer it.
- **General anti-abuse rule.** Article 33A applies the anti-abuse provisions of the EU Anti-Tax Avoidance Directive (ATAD), and from 2026 it also covers transactions involving individuals.
- **Disguised distributions.** Private use of company assets by a shareholder is taxed under article 3A (Section 2).

## The method, step by step

1. Fix the year. Apply the rules for tax year 2026, the 2026 personal scale and the 15% corporate rate only to periods from 1 January 2026 (Income Tax (Amendment) Law 244(I)/2025, presentation: https://www.gov.cy/media/sites/167/2026/03/2026-%CE%A6%CE%BF%CF%81%CE%9C%CE%B5%CF%84%CE%B1%CF%81%CF%81%CF%8D%CE%B8%CE%BC%CE%B9%CF%83%CE%B7-%CE%A6%CF%8C%CF%81%CE%BF%CF%82-%CE%95%CE%B9%CF%83%CE%BF%CE%B4%CE%AE%CE%BC%CE%B1%CF%84%CE%BF%CF%82.pdf).
2. Test income tax residence under the 183-day or the 60-day rule (Income Tax Law article 2, https://www.gov.cy/mof-tax/en/documents/tax-residency-domicility/).
3. Test domicile: domicile of origin, the 20-year exceptions, and the 17-of-20-years deemed domicile. If the client is non-domiciled, the SDC exemption is claimed with Form T.D.38; if they are reaching the 17-year point without a Cypriot domicile of origin, consider Form TD 631 by 30 June of the first year of the period (https://www.gov.cy/media/sites/167/2026/06/Application-Extension-of-Non-Dom.pdf).
4. For any dividend, identify the profit year it comes out of and apply the matching SDC row; check whether 2024 or 2025 profits face a deemed distribution (Special Defence Contribution Law 117(I)/2002 as amended, presentation: https://www.gov.cy/media/sites/167/2026/03/EEA-%CE%A6%CE%9A%CE%9A-%CE%9C%CE%95%CE%A4%CE%91%CE%A1%CE%A1%CE%A5%CE%98%CE%9C%CE%99%CE%A3%CE%97-06032026.pdf).
5. Add GHS on dividends and other income up to the annual cap (Form T.D.59A 2026, https://www.gov.cy/media/sites/167/2026/02/IR59_2026_English__.pdf).
6. Check each new-resident exemption against its conditions: article 8(21B) (https://www.gov.cy/media/sites/167/2026/06/Article-8-21B-of-the-Income-Tax-Law-N.118-I-2002.pdf), article 8(23A) (https://www.gov.cy/media/sites/167/2026/06/%CE%A0%CE%AF%CE%BD%CE%B1%CE%BA%CE%B1%CF%82-%CE%B1%CF%80%CE%B1%CE%BB%CE%BB%CE%B1%CE%B3%CF%8E%CE%BD-823-%CE%BA%CE%B1%CE%B9-823%CE%91.pdf), article 8(21A) (https://www.gov.cy/media/sites/167/2026/01/implementation-of-sections-21-and-21A-of-article-8-24072023.pdf).
7. Check the special rates: crypto gains (article 20E), approved share plans (article 20D), foreign pensions (article 20), from the income tax presentation in step 1.
8. Compare company and self-employment using the client's own numbers, social insurance (https://www.businessincyprus.gov.cy/social-insurance-registration-and-contributions/) and the computation in `cyprus-income-tax`. State no combined rate.
9. Screen the plan against article 33A (anti-abuse) and article 3A (disguised distributions) before presenting it, and refer anything that depends on substance, treaty residence or the IP box.

## Ask the client first

- How many days were you in Cyprus this year, were you resident more than 183 days in any other country, and do you have a Cyprus business, job or directorship and a home you own or rent here?
- Where were you born and where was your father domiciled then, and how many of the last 20 years were you Cyprus tax resident?
- Will the dividends come out of profits of 2025 or earlier, or of 2026 onward, and are there undistributed 2024 or 2025 profits?
- Do you or anyone connected to you use company property (a car, a house, a loan) privately?
- When did you start work or business in Cyprus, what did you earn in the first 12 months, and where did you work in the 7 years before?
- Do you hold crypto-assets, an approved share plan, or a pension for work done abroad?

## When to refuse or refer

- Refuse to design residence or domicile on paper, or a company with no real management, to obtain an exemption.
- Refer every IP box question: the percentage and qualifying assets are not printed on an allowed page here.
- Refer domicile disputes (domicile of choice, the 20-year exceptions) and any Form T.D.38 or TD 631 application.
- Refer treaty residence of a company or individual, and any case where Cyprus and another country both claim residence.
- Refer dividends out of profits from before 2018 or received after 31/12/2031 from pre-2026 profits: the rate row above does not settle them.
- Refer any plan that depends on a combined or effective tax rate: this Guide does not compute one.

## Sources

- Tax Department FAQs on the 2026 reform: https://www.gov.cy/media/sites/167/2026/05/FAQs-110526.pdf
- Income tax reform presentation (Law 244(I)/2025): https://www.gov.cy/media/sites/167/2026/03/2026-%CE%A6%CE%BF%CF%81%CE%9C%CE%B5%CF%84%CE%B1%CF%81%CF%81%CF%8D%CE%B8%CE%BC%CE%B9%CF%83%CE%B7-%CE%A6%CF%8C%CF%81%CE%BF%CF%82-%CE%95%CE%B9%CF%83%CE%BF%CE%B4%CE%AE%CE%BC%CE%B1%CF%84%CE%BF%CF%82.pdf
- SDC reform presentation: https://www.gov.cy/media/sites/167/2026/03/EEA-%CE%A6%CE%9A%CE%9A-%CE%9C%CE%95%CE%A4%CE%91%CE%A1%CE%A1%CE%A5%CE%98%CE%9C%CE%99%CE%A3%CE%97-06032026.pdf
- Tax residency and domicile: https://www.gov.cy/mof-tax/en/documents/tax-residency-domicility/
- Non-dom extension application (Form TD 631): https://www.gov.cy/media/sites/167/2026/06/Application-Extension-of-Non-Dom.pdf
- Form T.D.59A 2026 (English): https://www.gov.cy/media/sites/167/2026/02/IR59_2026_English__.pdf
- Guide to the 2025 income tax return: https://www.gov.cy/media/sites/167/2026/06/Guide-for-completion-of-tax-return-2025.pdf
- Article 8(21B) exemption: https://www.gov.cy/media/sites/167/2026/06/Article-8-21B-of-the-Income-Tax-Law-N.118-I-2002.pdf
- Articles 8(23) and 8(23A) table: https://www.gov.cy/media/sites/167/2026/06/%CE%A0%CE%AF%CE%BD%CE%B1%CE%BA%CE%B1%CF%82-%CE%B1%CF%80%CE%B1%CE%BB%CE%BB%CE%B1%CE%B3%CF%8E%CE%BD-823-%CE%BA%CE%B1%CE%B9-823%CE%91.pdf
- Articles 8(21) and 8(21A) table: https://www.gov.cy/media/sites/167/2026/01/implementation-of-sections-21-and-21A-of-article-8-24072023.pdf
- Social insurance (government one-stop shop): https://www.businessincyprus.gov.cy/social-insurance-registration-and-contributions/

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a licensed tax adviser in Cyprus) before acting upon.

The most up-to-date version of this Guide is maintained at openaccountants.com. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
