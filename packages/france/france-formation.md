---
name: france-formation
description: Use this skill whenever asked about forming, incorporating, or registering a company in France. Trigger on phrases like "set up a company in France", "SAS formation", "SARL création", "Guichet unique INPI", "French company formation", "register a business France", "société par actions simplifiée", "société à responsabilité limitée", "Kbis", "RCS registration", "annonce légale", or any question about starting a business entity in France. Covers entity types (SAS, SARL, EURL, SASU, SA, auto-entrepreneur), registration process, capital requirements, costs, post-formation compliance, and bank account opening. ALWAYS read this skill before advising on French company formation.
version: 1.0
jurisdiction: FR
tax_year: 2026
last_updated: 2026-09-23
review_status: pending_review
drafted_by: OpenAccountants
approved_by: pending
depends_on:
  - company-formation-workflow-base
category: formation
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Forming a business in France: micro-entrepreneur, EI, SARL, SAS and SA

How to set a business up in France: which legal form to choose, what the founder is liable for, the manager's social status, the steps from the articles to the register, the capital that must be paid in, the official fees, and the duties that begin the day the business exists. Figures are for tax year 2026. Most of the official pages used here were checked by the administration during 2026. Five carry an earlier check date, and their figures are printed exactly as those pages print them: the share capital deposit page (checked 20 October 2025), the company creation overview (12 September 2025), the annual accounts filing page (11 June 2025), the statutory auditor page (10 April 2025) and the equity page (10 April 2024). Every amount and percentage sits in a table naming the official page it was read on. Where no official page prints a number, this Guide says so and gives none.

## Section 1: Quick Reference

| Field | Value |
| --- | --- |
| Country | France (French Republic) |
| Currency | Euro |
| Where every formality is filed | Guichet des formalités des entreprises, the one-stop desk run by the INPI, at https://www.formalites.entreprises.gouv.fr |
| Registers the filing feeds | Registre national des entreprises (RNE) and, for a commercial company, the Registre du commerce et des sociétés (RCS) |
| Key legislation | Code de commerce, Code civil, Code général des impôts. Legifrance cannot be read by this Guide's fetcher, so every article named below is cited from the government page that names it |
| Typical formation time | No official page states a formation time. Section 10 gives the legacy estimate and the two delays the pages do fix |
| Corporate tax | See the corporation tax table in Section 6 |
| Formation fees | See the tables in Section 5 |
| Tax authority | Service des impôts des entreprises (SIE), https://www.impots.gouv.fr |
| Social body | Urssaf, https://www.urssaf.fr |

Read Section 2 to choose the form, Section 3 for the steps in order, Section 4 for capital, Section 5 for what it costs, and Section 6 for what falls due once the business exists.

## Section 2: Entity Types Comparison

The forms below are the ones the state's own business portal describes for a founder. Amounts are not repeated here. They are in the tables of Section 4, Section 5 and Section 6.

| Feature | Micro-entrepreneur | Entrepreneur individuel (EI) | EURL and SARL | SASU and SAS | SA |
| --- | --- | --- | --- | --- | --- |
| Separate legal person | No. It is an individual business | No. It is an individual business | Yes | Yes | Yes |
| Liability | Professional and personal assets are separated by law. Tax and social debts can still be recovered against both | Same separation, same exception for tax and social debts | Partners answer up to their contribution. A manager at fault can be ordered to pay part of the debts | Partners answer up to their contribution | Shareholders answer up to their contribution |
| Founders | 1 | 1 | EURL: 1. SARL: at least 2 and at most 100 | SASU: 1. SAS: at least 2 | At least 2, or 7 if listed |
| Partners may be companies | Not applicable | Not applicable | Yes | Yes | Yes |
| Articles and share capital | None | None | Required | Required | Required |
| Who may be the legal representative | The entrepreneur | The entrepreneur | The gérant must be an individual, not a company | The président may be an individual or a company | Individuals, plus a company as a board member represented by a permanent representative |
| Profit taxed as | Income tax under the micro regime, unless a real regime is chosen | Income tax, with an option to be treated as an EURL and taxed as a company | Corporation tax by default, with a time limited option for income tax | Corporation tax by default, with the same time limited option | Corporation tax by default, with the same time limited option |
| Manager's social status | Self-employed | Self-employed | Majority gérant: self-employed (TNS). Otherwise treated as an employee | Président: treated as an employee, general scheme, without unemployment insurance | Président and directeur général: treated as an employee |
| Listed on a regulated market | No | No | No | No. The page says a SAS cannot be listed | Yes |

Sources for this table: https://entreprendre.service-public.fr/vosdroits/F37398 for the micro-entrepreneur, https://entreprendre.service-public.fr/vosdroits/F37396 for the individual business, https://entreprendre.service-public.fr/vosdroits/F37411 for the SARL and EURL, https://entreprendre.service-public.fr/vosdroits/F37366 for the SAS and SASU, and https://entreprendre.service-public.fr/vosdroits/F37402 for the SA.

**What "treated as an employee" changes.** A majority SARL gérant is a travailleur non salarié and pays the self-employed contributions. A SAS président is assimilé salarié: the company pays contributions under the general scheme on his pay, but he gets no unemployment insurance. Neither status is cheaper in the abstract, and no page in this Guide's allowed set prints a single combined contribution rate for either. Price both before advising: the French self-employed social contributions Guide
(fr-social-contributions) carries the cotisations of a TNS gérant, and the French payroll Guide
(france-payroll) carries the cost of an assimilé salarié président.

**Who may not be the gérant of a SARL.** The SARL page says the gérant is necessarily an individual. A company can be a partner in a SARL but cannot manage it. A SAS may appoint a company as its président, and Section 8 lists the extra documents that then go into the filing.

**Micro-entrepreneur turnover limits.** These are income tax limits, tested on earlier calendar years, and they are not the VAT limits in Section 6.

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.fr/vosdroits/F23267 |
| Selling goods, food to take away or eat in, and supplying accommodation | EUR 203,100 | Limit for income received in 2026, tested on turnover of 2025 or 2024 |
| Services and the liberal professions | EUR 83,600 | Limit for income received in 2026, tested on turnover of 2025 or 2024 |
| Selling goods: the limit that governed income received in 2025 | EUR 188,700 | Use this one for the 2025 income being declared in 2026 |
| Services: the limit that governed income received in 2025 | EUR 77,700 | Use this one for the 2025 income being declared in 2026 |

**A business created this year is not tested against those limits yet.** The same page states the rule for a new business: the micro regime applies automatically in the year of creation (N) and in the following year (N+1), and only from year N+2 does the turnover test start, looking at years N and N-1. Where the activity starts during the year, the first year's limit is cut in proportion to the number of days the business existed, unless the business is seasonal. A founder can still opt out of the micro regime for a real regime from the start.

**Micro-entrepreneur social contributions**, charged on turnover and not on profit. These are the full rates. A founder with the Acre start-up relief pays a reduced rate in the first period, and the reduced rates are on the same page.

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.autoentrepreneur.urssaf.fr/portail/accueil/sinformer-sur-le-statut/lessentiel-du-statut.html |
| Selling goods and supplying accommodation | 12.3% | Applied to declared turnover for 2026 |
| Commercial and craft services (BIC) | 21.2% | Applied to declared turnover for 2026 |
| Other liberal services (BNC) outside Cipav | 25.6% | Final step of the phased rise, reached on 1 January 2026 |
| Liberal professions attached to Cipav | 23.2% | These professions did not move to the rate above |

**Recommended default.** The state recommends no form. What the pages let you compare is liability, who may manage, how profit is taxed and how the manager is insured. A SAS or SASU gives the widest freedom in the articles and can admit investors. A SARL or EURL is more prescribed by the Code de commerce and its majority gérant is self-employed. A micro-entreprise or an EI has no share capital and no shares at all.

## Section 3: Registration Process

Since 1 January 2023 every creation, change and closure is filed on the one-stop desk at https://www.formalites.entreprises.gouv.fr The old CFE centres are gone, and nothing is sent directly to the commercial court registry: the desk forwards the file to the registry itself. Any checklist that still names a centre de formalités des entreprises is out of date.

### Step 1: Choose Company Name (Dénomination Sociale)

A company must be named, and the name goes into the articles. It is what identifies the company as a legal person. The official pages describe no reservation procedure: the name is secured by the registration itself. Searching the INPI trademark register first is prudent and is not a legal step. See https://entreprendre.service-public.fr/vosdroits/F32886

### Step 2: Draft Statuts (Articles of Association)

The articles are written and signed by the partners, or by the sole partner in a one-person company. They must state the form, the duration, which cannot exceed 99 years, the name, the registered office, the objects, the share capital and each partner's contribution, whether in cash, in kind or in industry. Each form adds its own compulsory clauses. If a notary drew the articles up, the notary's name and address must appear in them. Where real
property is contributed to the capital, a notary must draw the articles up. In most cases, and in
particular where the contributions are all in cash, the articles do not have to be registered
with the tax office. They must be registered with the Service des impôts des entreprises, within
one month of their date, in four cases: the articles carry a transfer of a business, a transfer
of ownership or usufruct of real property, or a transfer of shares, or a notary or a commissaire
de justice drew them up. Registration comes after signature and before the legal notice. The cost of using a lawyer or a notary is in Section 5. See https://entreprendre.service-public.fr/vosdroits/F32232

### Step 3: Deposit Share Capital

The cash is paid into a blocked account opened in the name of the company being formed. The page
puts this step early: for a commercial company the deposit must be made before the articles are
drafted and signed, and before registration. That is why the depositary asks for a complete draft
of the articles and not a signed set. The legal representative makes the deposit, and the depositary can only be a credit institution or a notary. A payment institution may not take the deposit, and the Caisse des dépôts et consignations has not accepted one since 1 June 2021. The depositary issues an attestation de dépôt des fonds, which the registration file needs. The funds are released once the company is registered. The deposit is compulsory for a commercial company (SAS, SARL, SA) and optional for a civil company such as an SCI or an SCM. The amounts are in Section 4. See https://entreprendre.service-public.fr/vosdroits/F32333

### Step 4: Publish Annonce Légale (Legal Notice)

The notice of formation is published after the articles are signed and before the registration is applied for, in a journal d'annonces légales or an online press service authorised in the department where the registered office is. The request must give the name, the short form, the legal form, the share capital, the address of the registered office, the objects, the duration, the name of the director or directors, and the register the company will be entered in. The publisher then issues an attestation de parution or a copy of the notice, which goes into the registration file. The tariffs are in Section 5. See https://entreprendre.service-public.fr/vosdroits/F35957

### Step 5: File on Guichet Unique (INPI)

The registration application goes on https://www.formalites.entreprises.gouv.fr The file carries the creation form completed online, the beneficial owners form, the articles dated and signed, proof of the registered office address, the attestation de parution, the original certificate of the depositary of the funds with the dated and signed list of subscribers showing what each person subscribed and paid, and the director's identity document with an original signed declaration of no criminal conviction and of parentage. A regulated activity adds the authorisation, diploma or title. A company acting as director adds its own documents, listed in Section 8. See https://entreprendre.service-public.fr/vosdroits/F35934

### Step 6: Obtain Kbis and SIRET

Once the file is lodged, the desk returns a récépissé de dépôt de dossier de création d'entreprise marked "En attente d'immatriculation". It lets the company deal with other bodies while it waits, and it is valid for at most one month. If the file is incomplete, the desk sends a récépissé listing what is missing and the missing items must be sent within 15 working days of receiving it. Once registered, the company is given two identification numbers, the Siren which identifies the company and the Siret which identifies the establishment, plus the APE activity code. The Kbis extract is the commercial register's own extract of the entry. See https://entreprendre.service-public.fr/vosdroits/F35934

### Step 7: Déclaration des Bénéficiaires Effectifs (UBO Register)

Every company entered on the RCS, apart from a company listed on a stock exchange, must file a
declaration of beneficial owners with the registration application. The declaration is charged with the registration fee and is not optional: the amount is in Section 5.

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.fr/vosdroits/F32886 |
| Holding that makes a person a beneficial owner | 25% | "une personne qui détient plus de 25 % du capital, ou plus de 25 % des droits de vote de la société". It is capital OR voting rights, and the test is "more than", not "at least" |

The declaration must be updated when the beneficial owners change. The pages in this Guide's allowed set do not print a deadline in days for that update, so none is given here.

### Step 8: Tax Registration

The one-stop desk passes the file to the tax administration and the company is attached to its Service des impôts des entreprises. Four things have to be settled straight away: the corporation tax position, the VAT position, the first CFE return, and the electronic invoicing platform. All four are in Section 6. See https://entreprendre.service-public.fr/vosdroits/F35934

## Section 4: Capital Requirements

Three separate rules apply: the minimum share capital for the form, how much of the cash must actually be paid in at creation, and when a contribution in kind must be valued by a commissaire aux apports.

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.fr/vosdroits/F37366 |
| SAS and SASU: lowest share capital allowed | EUR 1 | "Le montant du capital social est déterminé librement par les associés ( 1 € minimum)". Half of a cash contribution must be paid at incorporation and the other half within 5 years of registration |
| Highest value any single contribution in kind may have if the partners skip the valuer | EUR 30,000 | The SAS page prints the same test as the SARL page: the partners may agree unanimously to skip the commissaire aux apports only if no single contribution in kind is worth more than this AND the contributions in kind together are not more than half the share capital. Both conditions must hold |

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.fr/vosdroits/F37411 |
| SARL and EURL: share of a cash contribution paid at creation | 20% | "20 % des apports lors de la création de la société". The balance is due within 5 years of registration |
| Highest value any single contribution in kind may have if the partners skip the valuer | EUR 30,000 | The partners may agree unanimously to skip the commissaire aux apports only if no single contribution in kind is worth more than this AND the contributions in kind together are not more than half the share capital. Both conditions must hold |

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.fr/vosdroits/F37402 |
| SA: lowest share capital allowed | EUR 37,000 | "doit être au minimum de 37 000 €". Contributions in kind to an SA must always be valued by a commissaire aux apports, and contributions in industry are forbidden |

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.fr/vosdroits/F32333 |
| SAS, SASU and SA: share of a cash contribution paid at creation | 50% | "le versement initial doit être au minimum de 50 % de la somme indiquée". The balance is due within 5 years of registration |
| Civil company such as an SCI, SCM or SCP: lowest share capital allowed | EUR 1 | "Aucun capital social minimum n’est imposé pour les sociétés civiles". The partners fix the capital freely and the page adds that it is not recommended to stop at the floor. The deposit itself is optional for a civil company |

The capital deposit page prints the same minimum of one euro for a SARL or an EURL as it does for a SAS, and it prints the SARL initial payment as twenty per cent, so the two pages agree. The page also warns against the legal floor in terms: it says one euro is possible "bien que cela ne soit pas recommandé", because a higher capital helps with bank finance and reduces the risk of the compulsory procedure that starts when equity falls below half the share capital. No official page names a recommended amount, so this Guide names none.

Contributions in industry, meaning know-how or work, never count towards share capital in any form. A SARL may accept them without their entering the capital. An SA may not accept them at all.

## Section 5: Costs Breakdown

There are three separate government-side costs at formation: the registration fee, the beneficial owners declaration charged with it, and the legal notice. Optional professional help is a fourth. No official page adds them into a single formation cost, and this Guide does not add them either.

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.fr/vosdroits/F35934 |
| Registering a commercial company on the RCS | EUR 33.83 | "est de 33,83 €" |
| Declaration of beneficial owners, charged on top and compulsory | EUR 19.33 | "À cela s’ajoute obligatoirement la déclaration des bénéficiaires effectifs qui s'élève à 19,33 €" |
| Registering a civil company | EUR 60.38 | The beneficial owners declaration is charged on top of this one too |
| Commercial agent: the second registration on the RSAC, on top of the RCS one | EUR 23.21 | Applies to an agent commercial only |
| Fine for knowingly giving inaccurate or incomplete information at registration | EUR 4,500 | With imprisonment of 6 months, Code de commerce article L123-38 |
| Fine for carrying on a commercial, craft or liberal activity without being registered on the RNE | EUR 7,500 | Code de commerce article L123-38-1 |

The legal notice is a separate compulsory cost. The tariff is a flat amount, fixed by legal form and by department, and quoted excluding VAT.

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.fr/vosdroits/F35957 |
| First table on the same page, captioned as the tariff for a SARL | EUR 148 | Metropolitan France and most overseas departments. Tarif en euros HT, so before VAT |
| SARL, La Réunion and Mayotte | EUR 173 | Same notice, higher tariff |
| EURL, metropolitan France and most overseas departments | EUR 124 | |
| EURL, La Réunion and Mayotte | EUR 147 | |
| SAS, metropolitan France and most overseas departments | EUR 199 | |
| SAS, La Réunion and Mayotte | EUR 233 | |
| SASU, metropolitan France and most overseas departments | EUR 142 | |
| SASU, La Réunion and Mayotte | EUR 167 | |
| SA, metropolitan France and most overseas departments | EUR 399 | |
| SA, La Réunion and Mayotte | EUR 466 | |
| Second table on the same page, also captioned as the tariff for a SARL | EUR 220 | Metropolitan France and most overseas departments. It sits under the société en nom collectif heading. The page gives two different amounts under the same caption and does not say which governs a SARL |
| The same sixth table, La Réunion and Mayotte | EUR 259 | |

The page therefore prints two different tariffs under the same caption, "Tarifs de la publication
d'un avis de constitution d'une SARL". The first table sits in the part of the page about the
SARL. The second sits in the part headed "Société en nom collectif (SNC)", whose text and forms
are about an SNC. The page disagrees with itself and this Guide does not pick a winner: for a
SARL, confirm the tariff with the journal d'annonces légales or the online press service that
will publish the notice before quoting a client a figure.

Help with the articles is optional and is the one professional cost the state quantifies.

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.fr/vosdroits/F32232 |
| Lawyer or notary drafting the articles, low end | EUR 1,000 | "Le coût de cette intervention varie entre 1 000 € et 2 500 €" |
| Lawyer or notary drafting the articles, high end | EUR 2,500 | Same sentence |

A founder budgeting the legal minimum needs the registration fee, the beneficial owners declaration and the legal notice for the chosen form. Bank charges for the capital deposit account are set by the bank and are not published by the state, so no figure is given for them.

### Annual Maintenance

The recurring fees a firm charges, for an expert-comptable or a commissaire aux comptes, are not published by the state, so no amount for them is given here. What the state does publish is what it costs to get the recurring duties wrong, and what the local business property tax can be.

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.fr/vosdroits/F31214 |
| Criminal fine on the director for not filing the annual accounts | EUR 1,500 | The offence can be prosecuted for one year from the date the accounts should have been filed |
| The same fine where the failure is repeated | EUR 3,000 | "En cas de récidive, l'amende passe à 3 000 €" |

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.fr/vosdroits/F37169 |
| Fine for not keeping the accounting records for the required period | EUR 10,000 | Records and supporting documents must be kept for at least 10 years from the close of the financial year |

**CFE, the local business property tax.** A new business is exempt for the year it is created, and only until 31 December of the year the activity starts. Its base is then reduced by half for the following year. To get the exemption the business must file the déclaration initiale n° 1447-C-SD on paper with its SIE before 31 December of the year of creation, so that the figures are in place for the following year. There is no single CFE amount: each turnover band gives a range, and the commune picks the figure inside it, so two identical businesses in two communes pay different amounts. The French local business property tax Guide (fr-cfe) covers the CFE itself once the business is
running.

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.fr/vosdroits/F23547 |
| Exempt where turnover excluding VAT of year N-2 did not exceed | EUR 5,000 | "n'a pas dépassé 5 000 €" |
| The lowest minimum base a commune may set, the same for every band | EUR 250 | Every band below starts at this figure |
| Band 1: turnover of year N-2 up to | EUR 10,000 | Minimum base between the floor above and the ceiling below |
| Band 1 ceiling | EUR 597 | |
| Band 2: turnover of year N-2 up to | EUR 32,600 | Band 2 starts one euro above band 1 |
| Band 2 ceiling | EUR 1,194 | |
| Band 3: turnover of year N-2 up to | EUR 100,000 | |
| Band 3 ceiling | EUR 2,509 | |
| Band 4: turnover of year N-2 up to | EUR 250,000 | |
| Band 4 ceiling | EUR 4,183 | |
| Band 5: turnover of year N-2 up to | EUR 500,000 | |
| Band 5 ceiling | EUR 5,974 | |
| Top band, turnover above band 5 | EUR 7,769 | This is the ceiling, not the turnover |

## Section 6: Post-Formation Compliance

| Obligation | When | Who to |
| --- | --- | --- |
| Approve the annual accounts in general meeting | SARL and SA: within 6 months of the year end. SAS and SASU: a period set freely by the partners in the articles, in practice 6 months, because a dividend must be paid within 9 months of the year end | The partners |
| File the annual accounts | Within the month following approval, or within 2 months following approval where the filing is made electronically. For a SARL or an EURL the page words the same two limits as filing at the registry and filing on the one-stop desk | Greffe du tribunal de commerce, through https://www.formalites.entreprises.gouv.fr |
| Corporation tax return, form n° 2065 | Within 3 months of the year end. If the year ends on 31 December, or if no year ends during the calendar year, by the second working day after 1 May | SIE, https://www.impots.gouv.fr |
| VAT returns | Monthly, quarterly or yearly, according to the regime | SIE, https://www.impots.gouv.fr |
| Déclaration sociale nominative, once there are employees | Monthly | Urssaf through https://www.net-entreprises.fr |
| First CFE return, n° 1447-C-SD | Before 31 December of the year of creation | SIE, on paper |
| Update the beneficial owners declaration | When the beneficial owners change | One-stop desk, https://www.formalites.entreprises.gouv.fr |
| Be able to receive electronic invoices | From 1 September 2026, whatever the size of the business | Through an approved platform |

The accounts approval and filing rules are on https://entreprendre.service-public.fr/vosdroits/F31214 and the corporation tax return deadline is on https://entreprendre.service-public.fr/vosdroits/F37366

**Corporation tax.** A SAS, SASU, SA, SARL or EURL pays corporation tax by default. The reduced rate is not automatic: both conditions in the table must be met, and the capital must be fully paid up.

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.fr/vosdroits/F23575 |
| Standard rate on profits made in France in the accounting period | 25% | Applies to the whole profit unless the reduced rate conditions are met |
| Reduced rate on the first slice of profit | 15% | Profit above the slice is taxed at the standard rate |
| The slice of profit the reduced rate covers | EUR 42,500 | Not an allowance for everyone: a cap on the slice taxed at the lower rate |
| First condition: turnover of the accounting period, restated to 12 months if needed, at or below | EUR 10,000,000 | |
| Second condition: share of the capital held by individuals, capital fully paid up | 75% | Held by individuals, or by a company itself held at least 75% by individuals |
| Corporation tax below this amount is paid in one go, with no instalments | EUR 3,000 | |
| Income tax option: voting rights held by individuals, at least | 50% | One of the conditions for electing income tax instead |
| Income tax option: voting rights held by the président, directeur général, président du conseil de surveillance, a member of the directoire or the gérant and their household, at least | 34% | Another condition for the same election |
| Income tax option: annual turnover or balance sheet total, below | EUR 10,000,000 | A different test from the reduced rate condition above, which is met at or below the same amount |

The income tax election is open only to a company that carries on a commercial, craft, agricultural or liberal activity as its main activity, is not listed, employs fewer than 50 people, has annual turnover or a balance sheet total below the amount in the income tax option row of the
table, and was created less than 5 years before the election is asked for. The election lasts 5 accounting periods and cannot be renewed. It taxes the result in the partners' hands in proportion to their holdings. Going the other way, a company that has elected corporation tax may withdraw the election up to the fifth period following the one it was made for, after which the corporation tax election is irrevocable.

**VAT.** A new business charges no VAT while it is inside the franchise en base, and deducts none either. The single EUR 25,000 franchise threshold proposed for 2026 was abandoned, so the limits below are the ones in force. They are VAT limits and are not the micro income tax limits in Section 2.

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.fr/vosdroits/F21746 |
| Selling goods and supplying accommodation: turnover of the previous calendar year | EUR 85,000 | Crossing this one brings the business into VAT from 1 January of the following year |
| Selling goods and supplying accommodation: turnover of the current year | EUR 93,500 | Crossing this one brings the business into VAT from the first day of the overrun |
| Services: turnover of the previous calendar year | EUR 37,500 | Crossing this one brings the business into VAT from 1 January of the following year |
| Services: turnover of the current year | EUR 41,250 | Crossing this one brings the business into VAT from the first day of the overrun |
| The single threshold proposed for 2026 and then dropped | EUR 25,000 | "La proposition issue de la loi de finances pour 2025 visant à instaurer un seuil unique de franchise en base de TVA de 25 000 € a été abandonnée." Do not use this figure |

Lawyers, authors and performers have their own pair of limits on the same page. A business outside the franchise files VAT returns, and the French VAT return Guide covers those.

**Electronic invoicing catches every new business.** From 1 September 2026 a business of any size must be able to receive its invoices in electronic form, which means choosing an approved platform before that date. Issuing electronic invoices starts on 1 September 2026 for large and intermediate companies, and
on 1 September 2027 for small and medium enterprises and micro-enterprises. The French electronic
invoicing Guide (france-einvoice) carries the formats, the platform rules and the reporting of
transaction data. A small business may enter early if it wants to. See https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/fiche-3_tpe_a-partir-de-quand-mon-entreprise-doit-etre-prete.pdf

**The legal reserve.** A company must set part of each year's profit aside before it can distribute freely.

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.fr/vosdroits/F24024 |
| Compulsory transfer out of each year's profit to the legal reserve | 5% | "Elle est constituée par un prélèvement d'au moins 5 % réalisé sur le bénéfice de chaque exercice". It is a minimum, not a fixed figure |
| The transfer stops being compulsory once the reserve reaches this share of the share capital | 10% | The legal reserve can never be distributed |

The French bookkeeping, financial statements, VAT return and payroll Guides cover the books, the accounts, the returns and the payroll themselves.

## Section 7: Bank Account Opening

### Documents Typically Required

To open the account that takes the capital, the legal representative or a proxy must give a request to deposit the share capital, the money itself, the representative's identity document and address, the list of subscribers with each partner's identity document, and a complete draft of the articles dated less than one year earlier. The depositary then issues the attestation de dépôt des fonds, which must name the company, its registered office, the total paid, the amount each partner paid, and the place and date of the deposit, with the depositary's stamp and signature. Note that the Kbis does not exist yet at this stage, so the bank cannot ask for it for the deposit account. See https://entreprendre.service-public.fr/vosdroits/F32333

### Typical Timeline

No official page states how long a bank takes. What the pages fix is the order: the deposit is made before the articles are drafted and signed, and before the registration is applied for, and the funds are unblocked only when the registration certificate is produced. The legacy estimate of one to three days for an online provider and one to three weeks for a branch bank is kept here as an estimate. It is not a published figure and should not be quoted as one.

### Common Banks

The state publishes no list of banks and this Guide recommends none. The rule that matters is on the deposit page: the depositary must be a credit institution or a notary, and a payment institution may not hold the capital. Several providers marketed to founders are payment institutions rather than credit institutions, so confirm the licence before paying the money in. The legacy Guide named BNP Paribas, Société Générale, Crédit Agricole and LCL as traditional banks and Qonto, Shine and Blank as digital providers. That list is the legacy Guide's own, is not published by the state, and is not a recommendation.

Opening a professional account is compulsory when the company is formed, because the capital has
to be deposited. Once the company is registered, keeping that account open is no longer a legal
duty, though the page calls it essential in practice. A micro-entrepreneur does not deposit capital, but must open an account dedicated to the business once turnover passes the limit below, and an individual business carrying on a commercial activity must hold one as well.

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.fr/vosdroits/F37369 |
| Turnover above which a micro-entrepreneur must hold a dedicated account | EUR 10,000 | The duty starts once annual turnover exceeds this in 2 consecutive years |

## Section 8: Foreign Founder Considerations

| Question | What the official pages say |
| --- | --- |
| Can a company be the director? | Yes for a SAS or SASU. No for a SARL or EURL, where the gérant must be an individual |
| A foreign company acting as director: what goes in the file | Its Kbis extract less than 3 months old, or its Siren, or a document proving it exists if it is not registered. If it is not registered inside the European Union, a copy of its articles translated into French and certified by its permanent representative. The permanent representative's identity card, and an original dated and signed declaration of no conviction and of parentage from that representative |
| Nationality or residence of an individual director | The registration pages set no nationality or residence condition and ask only for an identity document and the declaration of no conviction. They do not state a positive permission either, so treat this as the absence of a condition rather than as a published right |
| Registered office | Proof of the address must be in the file. It must be an address in France, evidenced by a utility bill, a commercial lease or a domiciliation contract |
| Hiding a home address | A director or an indefinitely liable partner may ask, when registering, that their home address be removed from the documents open to the public, including the articles filed at the RCS and the Kbis extract. Since 5 May 2026 a company may also file an extract of its constitutive or amending documents, so that less personal information reaches the register in the first place |
| Regulated activities | The authorisation, diploma or title must be in the file. Some sectors are closed to some forms: the SAS page names tobacco retail, insurance and the regulated liberal professions |

Source for this table: https://entreprendre.service-public.fr/vosdroits/F35934

## Section 9: Common Mistakes and Refusals

- **R-FR-F1: treating the SAS président as the cheap option.** The président of a SAS is assimilé salarié, so the company pays contributions under the general scheme on the pay, and he gets no unemployment insurance. A majority SARL gérant is TNS. No page in this Guide's allowed set prints a single combined rate for either status, so do not quote one, and do not repeat the old figures of about 22, 45 or 80 per cent that appeared in earlier versions of this Guide. Price both with the French self-employed social contributions Guide (fr-social-contributions)
and the French payroll Guide (france-payroll).
- **R-FR-F2: a capital of one euro with nothing behind it.** The state's own deposit page says the legal floor is possible "bien que cela ne soit pas recommandé", and explains why: bank finance and the compulsory procedure that starts when equity falls below half the share capital. The state names no recommended amount, so do not invent one.
- **R-FR-F3: filing before the legal notice is published.** The notice comes after the articles are signed and before the registration is applied for, and the attestation de parution is part of the file. Without it the file is incomplete, and an incomplete file must be corrected within 15 working days of the récépissé that lists what is missing.
- **R-FR-F4: forgetting the statutory auditor.** A commissaire aux comptes must be appointed once 2 of the 3 thresholds below are crossed. Crossing them does not create the duty for the year in which they are crossed: it starts with the following financial year. Partners holding a large enough share can ask a judge to appoint one even below the thresholds.

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.fr/vosdroits/F31440 |
| Balance sheet total | EUR 5,000,000 | One of the three thresholds. 2 of the 3 must be crossed |
| Turnover excluding VAT | EUR 10,000,000 | One of the three thresholds |
| Fine for not appointing an auditor when the law requires one | EUR 30,000 | With imprisonment of 2 years |
| Share of the capital that lets partners ask a judge to appoint one | 10% | The judge is free to refuse |

The third threshold is 50 employees. A compulsory mandate runs 6 years and is renewable. A voluntary appointment runs 3 years.

- **R-FR-F5: a micro-entrepreneur trying to raise investment.** The micro regime is an individual business. It has no share capital, no shares and no second partner, so it cannot take an equity investor. Moving to a SAS or a SARL is the route.
- **R-FR-F6: sending the client to a body that no longer handles this.** The CFE centres closed and nothing goes directly to the commercial court registry any more. Everything is filed on the one-stop desk at https://www.formalites.entreprises.gouv.fr and the desk forwards it.
- **R-FR-F7: applying the micro turnover limits to a business created this year.** The limits are tested on earlier calendar years. A business created in year N is on the micro regime for N and N+1 whatever it earns, and the test first bites in N+2 on the turnover of N and N-1, with the first year's limit cut in proportion to the days the business existed.
- **R-FR-F8: quoting the VAT franchise limits as the micro income tax limits.** They are different numbers on different pages and a business can be inside one and outside the other. Section 2 has the income tax limits, Section 6 the VAT limits.

## Section 10: Timeline

Two delays are fixed by the official pages and are the only ones stated as rules: the récépissé issued when the file is lodged is valid for at most one month, and an incomplete file must be completed within 15 working days of the récépissé listing what is missing. Both are on https://entreprendre.service-public.fr/vosdroits/F35934

| Step | Legacy estimate | Cumulative |
| --- | --- | --- |
| Open the account and deposit the capital | 1 to 5 days | Day 1 to 5 |
| Draft the articles and sign them | 1 to 5 days | Day 2 to 10 |
| Publish the legal notice | 1 to 2 days | Day 3 to 12 |
| File on the one-stop desk | 1 day | Day 4 to 13 |
| Registry processing | 5 to 10 working days | Day 9 to 23 |
| Registration certificate and Siret received | 1 to 3 days after registration | Day 10 to 26 |
| Tax and social registrations | Automatic with the filing | Day 10 to 26 |

The durations in this table are the legacy Guide's own estimate. No official page publishes a formation time, so treat them as planning assumptions and not as a service standard.

## The method, step by step

1. **Fix the form against the client's facts, not a default.** Compare the number of founders, the liability, who may manage, the tax treatment and the manager's social status on the state's own pages: https://entreprendre.service-public.fr/vosdroits/F37398 for the micro-entrepreneur, https://entreprendre.service-public.fr/vosdroits/F37396 for the individual business, https://entreprendre.service-public.fr/vosdroits/F37411 for the SARL and EURL, https://entreprendre.service-public.fr/vosdroits/F37366 for the SAS and SASU, and https://entreprendre.service-public.fr/vosdroits/F37402 for the SA. A micro-entrepreneur or an EI has no articles and no capital, so steps 2 to 4 below do not apply to them.
2. **Write and sign the articles.** Cover the compulsory clauses for the chosen form, keep the duration inside the limit the page states, and name the notary in the articles if a notary drew them. See https://entreprendre.service-public.fr/vosdroits/F32232
3. **Deposit the cash with a credit institution or a notary and collect the attestation de dépôt des fonds.** The page puts this step before the articles are drafted and signed, even though it is numbered after step 2 here: for a commercial company the deposit must come before the drafting and signing of the articles, and before registration. Pay in at least the share set for the form in Section 4, and check the depositary is a credit institution and not a payment institution. See https://entreprendre.service-public.fr/vosdroits/F32333
4. **Publish the notice of formation and collect the attestation de parution.** Use a journal or online press service authorised in the department of the registered office, and use the tariff for the form actually being created. See https://entreprendre.service-public.fr/vosdroits/F35957
5. **File the registration on the one-stop desk with the beneficial owners declaration.** Attach every document listed in Step 5 of Section 3, add the extra documents in Section 8 if a company is the director, and ask for the home address to be hidden at the same time if the client wants that. Watch the 15 working days if the desk comes back for something. See https://entreprendre.service-public.fr/vosdroits/F35934
6. **Release the capital and start the recurring duties.** Give the registration certificate to the depositary to unblock the funds, then settle the corporation tax position and the return n° 2065 deadline, the VAT position under the franchise limits, the first CFE return n° 1447-C-SD before 31 December, the electronic invoicing platform, and the monthly DSN if there are employees. See https://entreprendre.service-public.fr/vosdroits/F23575 and https://entreprendre.service-public.fr/vosdroits/F21746

## Ask the client first

- How many founders are there today, and is an outside investor expected? One founder with no investor can use a micro-entreprise or an EI, which cost nothing to register and have no capital. An investor needs shares, which means a SAS or a SARL.
- Will a founder be the gérant or the président, and will the business be run by an individual or by another company? A SARL cannot have a company as its gérant. A SAS can have a company as its président, and the filing then needs that company's own documents.
- Will the founder draw pay from the business, and how much? That decides whether the assimilé salarié or the TNS status costs more, and it is usually the biggest running difference between a SAS and a SARL.
- Is anything other than cash going into the capital? A contribution in kind can force a commissaire aux apports, and both of the conditions in Section 4 must hold before the partners can skip one.
- What turnover is expected in the first two years, and what will the business sell? It decides the micro limits, the VAT franchise limits and the reduced corporation tax band, and goods and services have different limits.
- Which year end is wanted? It sets the corporation tax return date and the accounts approval and filing dates in Section 6.

## When to refuse or refer

- Forms this Guide does not cover: SCI, SCM, SCP, SNC, SCA, SEL, the cooperative forms and the agricultural forms. Capital, liability and the manager's status differ for each, and the legal notice tariffs differ too.
- Anything turning on a regulated profession, a licence or a sector authorisation, including which legal forms that profession is allowed to use.
- Immigration, residence permits and the right to run a business in France as a non-EU national. No page in this Guide's allowed set covers it.
- Drafting the articles of a SAS. The freedom the form gives is exactly what makes the drafting a job for a specialist.
- Valuing a contribution in kind, or advising that the commissaire aux apports can be skipped, without testing both conditions in Section 4 against the actual contributions.
- Anything after formation that belongs to another Guide: payroll, the books, the annual accounts, the VAT returns, the founder's own income tax, and any restructuring or tax planning.
- Any figure a client brings from an older version of this Guide. The registration fee, the beneficial owners fee and the legal notice tariffs all changed, and the old totals were arithmetic rather than published amounts. Check Section 5 before quoting.

## Sources

- https://entreprendre.service-public.fr/vosdroits/F32886
- https://entreprendre.service-public.fr/vosdroits/F32232
- https://entreprendre.service-public.fr/vosdroits/F32333
- https://entreprendre.service-public.fr/vosdroits/F35957
- https://entreprendre.service-public.fr/vosdroits/F35934
- https://entreprendre.service-public.fr/vosdroits/F37411
- https://entreprendre.service-public.fr/vosdroits/F37366
- https://entreprendre.service-public.fr/vosdroits/F37402
- https://entreprendre.service-public.fr/vosdroits/F37396
- https://entreprendre.service-public.fr/vosdroits/F37398
- https://entreprendre.service-public.fr/vosdroits/F37369
- https://entreprendre.service-public.fr/vosdroits/F31214
- https://entreprendre.service-public.fr/vosdroits/F31440
- https://entreprendre.service-public.fr/vosdroits/F37169
- https://entreprendre.service-public.fr/vosdroits/F24024
- https://entreprendre.service-public.fr/vosdroits/F23575
- https://entreprendre.service-public.fr/vosdroits/F23547
- https://entreprendre.service-public.fr/vosdroits/F23267
- https://entreprendre.service-public.fr/vosdroits/F21746
- https://www.autoentrepreneur.urssaf.fr/portail/accueil/sinformer-sur-le-statut/lessentiel-du-statut.html
- https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/fiche-3_tpe_a-partir-de-quand-mon-entreprise-doit-etre-prete.pdf
- https://www.formalites.entreprises.gouv.fr

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute legal, tax, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional before acting upon.

The most up-to-date version of this Guide is maintained at openaccountants.com.

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
