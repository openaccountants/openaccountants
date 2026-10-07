---
name: netherlands-formation
description: Use this skill whenever asked about forming, incorporating, or registering a company in the Netherlands. Trigger on phrases like "set up a company in the Netherlands", "Dutch BV", "BV formation", "KvK registration", "Kamer van Koophandel", "Dutch company formation", "register a business Netherlands", "besloten vennootschap", "eenmanszaak", "VOF", "NV formation", "DGA salary", or any question about starting a business entity in the Netherlands. Covers entity types (BV, NV, eenmanszaak, VOF, CV), registration process, capital requirements, costs, post-formation compliance, and bank account opening. ALWAYS read this skill before advising on Dutch company formation.
version: 1.0
jurisdiction: NL
tax_year: 2026
last_updated: 2026-10-01
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - company-formation-workflow-base
category: formation
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Netherlands: starting a business (eenmanszaak, VOF or BV)

## Scope

This Guide covers starting a business in the Netherlands in tax year 2026 (calendar year):

- choosing between an **eenmanszaak** (sole trader), a **VOF** (general partnership) and a **BV**
  (private limited company), with the NV only as a comparison point;
- registration in the **Handelsregister** kept by KVK, and the notarial deed a BV needs;
- the **UBO** (ultimate beneficial owner) entry in the Handelsregister;
- tax registration with the **Belastingdienst**: the VAT ID and OB number, the small-business VAT
  scheme (**KOR**) and the **registration threshold** for very small businesses;
- **payroll registration** (loonheffingen), including the director-major shareholder (DGA);
- the **ondernemer** tests for income tax, the **urencriterium**, and the self-employed deductions
  (zelfstandigenaftrek, startersaftrek, MKB-winstvrijstelling).

It does not compute the corporate tax bill, VAT returns or payroll. Route those to:

- **nl-corporate-tax**: corporate income tax (vennootschapsbelasting, VPB) for the BV;
- **nl-vat-return** / **netherlands-vat-return**: filing VAT returns;
- **netherlands-payroll**: running payroll, the expat scheme (known as the thirty-percent ruling)
  and employer contributions.

The current law was checked on 28 September 2026. This guide does not approve a filing, notarial transaction or bank application. Sources are belastingdienst.nl and wetten.overheid.nl (Burgerlijk Wetboek Book 2, Handelsregisterwet
2007, Wet inkomstenbelasting 2001, Wet op de omzetbelasting 1968). KVK's own site is not used as a
source here, so **KVK fees, portal steps and processing times are marked "check at KVK"**.

## Ask the client first

- **Who is starting the business?** One person, several people, or an existing company? Are the
  people EU nationals? (The Act provides online BV formation for EU nationals.)
- **Where is the business established?** A business established in the Netherlands registers in
  the Handelsregister. The KOR is only for businesses established in the Netherlands (a business
  established elsewhere in the EU has its own rule, below).
- **When does trading start, or when was the deed signed?** Registration deadlines run from that
  date.
- **Expected turnover this calendar year and last calendar year?** This decides the KOR
  (€20,000) and the registration threshold (€2,200).
- **Is the business VAT-taxed, VAT-exempt, or a mix?** Exempt supplies change the VAT position and
  which turnover counts.
- **Hours per calendar year in the business, and hours in any other work?** This decides the
  urencriterium (at least 1,225 hours, and in most cases more time than in other work).
- **Was the person an ondernemer in any of the five previous calendar years, and how often did they
  claim the zelfstandigenaftrek?** This decides the startersaftrek.
- **Has the person reached AOW (state pension) age at the start of the calendar year?** The
  deductions are halved if so.
- **For a BV: who holds the shares, and what percentage?** A holder of at least 5% (with a partner)
  has a substantial interest (aanmerkelijk belang); if that person works for the BV, the customary
  salary rule applies.
- **Will anyone be employed, including the DGA?** When does the first employee start?
- **Any contribution in kind** (assets, an existing sole-trader business) into the BV?
- **Any partner who is a spouse or family member** in a VOF, doing mainly support work? This can
  stop their hours counting.

## The method, step by step

1. **Pick the legal form.**

### Step 1: Pick the legal form ([source](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/tarieven_vennootschapsbelasting))

| Point | Eenmanszaak | VOF | BV |
| --- | --- | --- | --- |
| Legal personality | No | No | Yes |
| Liability | Owner liable for all business debts | Each partner liable for all debts of the VOF | The BV itself; shareholders not personally liable beyond what is due on their shares; directors can be liable for mismanagement |
| Founders | One person | Two or more partners | One or more persons |
| Notarial deed | No | No | Yes (BW 2:175 lid 2) |
| Minimum capital | None | None | No minimum; at least one voting share held by someone other than the BV or its subsidiaries (BW 2:175 lid 1) |
| Income tax / corporate tax | Owner pays income tax; ondernemer reliefs if the tests are met | Each partner who meets the tests is an ondernemer for income tax | BV pays VPB on its profit |
| VAT | Owner is the VAT entrepreneur | The VOF as a whole is the VAT entrepreneur | The BV is the VAT entrepreneur |
| Payroll | If staff are hired | If the VOF hires staff | If staff are hired; also on the DGA's salary |

Sources: Belastingdienst legal-form pages for the
[eenmanszaak](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/ondernemen/onderneming_starten/rechtsvorm/eenmanszaak),
[VOF](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/ondernemen/onderneming_starten/rechtsvorm/vennootschap-onder-firma-vof)
and [BV](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/ondernemen/onderneming_starten/rechtsvorm/besloten-vennootschap-bv);
[BW Book 2](https://wetten.overheid.nl/BWBR0003045/2026-07-01).

The **NV** (public company) is rarely right for a start-up: its authorised and issued capital must each
be at least forty-five thousand euro ("vijfenveertigduizend euro"), and the **paid-up** part of the
issued capital must also be at least that amount (BW 2:67 lid 2 and lid 3). Older texts that say only a
quarter must be paid up are wrong for the company as a whole.

A **BV pays VPB** at 19% on taxable profit up to €200,000 and 25.8% above it (rates for 2026, unchanged
from 2025). The owner then takes a salary and/or dividends. Whether a BV saves tax depends on profit,
the customary salary and dividend taxation; work that out with **nl-corporate-tax** rather than with a
rule of thumb.

2. **Register the business.**

### Step 2: Register the business (KVK Handelsregister)

- **Who must register.** An enterprise established in the Netherlands and owned by a natural person, a
  VOF, a BV, an NV and other listed forms is entered in the Handelsregister (Handelsregisterwet 2007,
  art. 5 and 6). The owner, or for a legal person each director, must file (art. 18).
- **Deadline for a business.** The first registration is made in a two-week window that starts one week
  **before** and ends one week **after** the business starts (art. 20 lid 1).
- **Deadline for a legal person (BV).** Within one week of the event that creates the duty (for a BV,
  its incorporation) (art. 20 lid 1). The directors must have the BV registered and file an authentic
  copy of the deed (BW 2:180 lid 1).
- **Later changes.** Other required filings, including changes, are made at the latest one week after the
  event (art. 20 lid 2).
- **KVK passes the data to the Belastingdienst.** This supplies the ordinary starting-business information; employer registration in Step 6 remains a separate required action. A sole trader
  is registered with their citizen service number (BSN); other forms get an RSIN from KVK. The
  Belastingdienst uses the BSN or RSIN to issue the VAT (OB) number and any payroll tax number. **Its published
  registration target is at most 10 working days**, after which it writes about the taxes that apply.
- **When KVK registration is not possible** (for example a sole trader whose activity does not count as
  an enterprise for the Handelsregister, or a foreign legal form with no establishment in the
  Netherlands), register with the Belastingdienst on the form "Opgaaf startende onderneming (niet
  ingeschreven in het Handelsregister)".
- **KVK fee and online steps: check at KVK.** This Guide does not state a fee.

Sources: [Handelsregisterwet 2007](https://wetten.overheid.nl/BWBR0021777/2025-07-16);
[Belastingdienst: schrijf uw onderneming in](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/ondernemen/onderneming_starten/schrijf-uw-onderneming-in/schrijf-uw-onderneming-in).

3. **Execute the BV formation process.**

### Step 3: For a BV, the notarial deed

- **Deed.** A BV is incorporated by one or more persons by notarial deed, signed by every founder and
  everyone who takes shares under the deed (BW 2:175 lid 2). A notary is therefore always needed.
- **Online formation.** A BV can be incorporated by electronic notarial deed by one or more **nationals
  of an EU member state** (BW 2:175a lid 1). If only natural persons use the model deed, the notary
  completes the formation within five working days, otherwise within ten, counted from the later of
  meeting all formal requirements and paying up the shares (lid 3). Electronic notarial incorporation permits only monetary contributions: a contribution in kind cannot be agreed through this route (BW 2:191a lid 4). For assets or an existing business contributed in kind, arrange the ordinary notarial route and the required description below.
- **Content.** The articles state the nominal value of the shares; the deed states the issued and paid-up
  capital and who takes which shares (BW 2:178 lid 1). On taking a share, its nominal amount must be paid,
  unless it is agreed that payment is due later or on call (BW 2:191 lid 1).
- **Contribution in kind.** Any contribution other than cash must be set out in the deed or an attached
  document (BW 2:204 lid 1). The founders make a **description** of what is contributed, with the value
  and the valuation method, relating to a date no more than six months before incorporation, signed by all
  founders (BW 2:204a lid 1). If it is known before the contribution that the value has fallen
  considerably since the description date, a new description is required (lid 2). No auditor's statement
  is required by this article for a BV.
- **Acts before incorporation ("BV i.o.").** A contract made in the name of a BV still to be formed binds
  the BV only once it ratifies it. Until then, those who acted are jointly and severally bound, unless it
  was expressly agreed otherwise with the other party for that contract (BW 2:203 lid 1 and 2).
- **Ratification does not end all exposure.** If the BV then fails to perform the ratified contract, those
  who acted for it are jointly and severally liable for the other party's loss if they knew or ought
  reasonably to have foreseen that the BV could not perform. That is presumed if the BV is declared
  bankrupt within one year of incorporation (BW 2:203 lid 3).
- **Directors, residence and foreign documents: check with the notary.** Whether non-resident directors,
  signing the deed by power of attorney, and apostilled or translated foreign documents are acceptable is a
  notarial and anti-money-laundering matter; confirm the actual requirements with the notary before proceeding.
- **Acts before registration.** Directors are jointly and severally liable, alongside the BV, for every
  act binding the BV done before the first registration in the Handelsregister, with the copies of the
  deed, has been made (BW 2:180 lid 2). Register quickly.
- **Notary fees: not stated here.** Get a quote.

### Step 4: UBO entry

- The Handelsregister records the ultimate beneficial owner(s) of companies and other legal entities
  entered under art. 5 or 6, with some exceptions (for example associations of owners)
  (Handelsregisterwet 2007, art. 15a lid 1). It records, among other things, the BSN or foreign tax
  number, name, birth details, residence, nationality, and the nature and size of the interest in bands
  (art. 15a lid 2).
- The people obliged to register must file what KVK needs to keep this information correct and complete
  at all times (art. 19 lid 1), and changes are due at the latest one week after the event (art. 20
  lid 2).
- Non-compliance is a prohibited act (art. 47); the Minister of Finance can impose an order subject to
  penalty payments or an administrative fine for UBO failures (art. 47a and 47b). Amounts: check.
- Who counts as a UBO is defined in anti-money-laundering law (the Wwft), not here. Public access to UBO
  data and the KVK filing steps: **check at KVK**.

### Step 5: VAT registration, the KOR and the registration threshold ([source](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/kor-voorwaarden))

**Who is a VAT entrepreneur.** Anyone who independently carries on a business or profession with
regular income, or exploits an asset or a right (for example letting property). Profit or loss does not
matter. A person can be an entrepreneur for VAT without being an ondernemer for income tax, and the
other way round
([Belastingdienst: ondernemer voor de btw](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/hoe_werkt_de_btw/voor_wie_geldt_de_btw/ondernemer)).

**Numbers.** After KVK registration the Belastingdienst decides, within at most 10 working days, whether
the business is a VAT entrepreneur. If so, it sends a **VAT identification number** (btw-id, format
NL + 9 digits + B + 2 digits, used with customers and suppliers) and an **OB number** (used only with the
Belastingdienst). For a sole trader the OB number contains the BSN and the VAT ID does not
([Belastingdienst: btw-id en ob-nummer](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/btw-identificatienummer-en-omzetbelastingnummer)).

**Late KVK registration.** If one or more VAT periods have already ended when the business registers,
the first return(s) for those periods must be filed on paper
([Belastingdienst: eerste btw-aangifte](https://www.belastingdienst.nl/wps/wcm/connect/nl/startende-ondernemer/content/btw-aangifte-startende-ondernemer)).

**KOR (kleineondernemersregeling), 2026.**
- **Who:** a business **established in the Netherlands** with relevant turnover in the Netherlands of **not more
  than €20,000** in a calendar year (Wet OB art. 25a lid 1). Open to sole traders, partnerships such as a
  VOF, and legal persons such as a BV.
- **Both years:** the €20,000 limit applies to the calendar year of joining **and** the year before
  ([KOR voorwaarden](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/kor-voorwaarden)).
- **Turnover that counts:** supplies taxed at 21%, 9% and 0% Dutch VAT (including exports and
  intra-EU supplies) and domestic reverse-charge supplies; certain exempt supplies (real estate,
  financial and insurance services). Not counted: sales of business assets used in the business, supplies
  taxed abroad, intra-EU acquisitions, and supplies where VAT is reverse-charged to the business.
  Margin-scheme sellers count the full sale price. Add all sub-numbers together; the KOR applies per
  entrepreneur, to all activities.
- **Effect:** no VAT charged, no VAT invoices needed for VAT purposes (keep purchase invoices), no VAT
  returns (except incidental returns), **no input VAT deduction**, and an earlier deduction may need to be
  revised.
- **Joining:** only after receiving the OB number and VAT ID; apply in Mijn Belastingdienst Zakelijk.
  Participation starts at the earliest from the next quarter or return period, allowing 4 weeks'
  processing: to start on 1 January 2027 the application must arrive by 4 December 2026. Keep filing VAT
  returns until the Belastingdienst confirms the start date
  ([aanmelden KOR](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/aanmelden-kor)).
- **Leaving:** you may give notice without the former multi-year lock-in; voluntary exit takes effect on the first day of the next calendar quarter beginning at least four weeks after receipt of notice. Re-entry is barred for the remainder of the exit year and the following calendar year (Wet OB art. 25a lid 7). **If turnover
  passes €20,000 in a calendar year you must deregister at once**, from the supply causing the excess; exclusion continues for the rest of that year and the next calendar year
  ([wat betekent meedoen](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/hoe_werkt_de_btw/kleineondernemersregeling/wat-betekent-meedoen-met-de-kleineondernemersregeling)).
- **Never under the KOR:** supplies of real estate used in the business, and new means of transport
  shipped to another EU country. Also: no opted-taxable letting while in the KOR.
- **Business established elsewhere in the EU:** may opt in only if its EU-wide turnover is also not more
  than €100,000 (Wet OB art. 25a lid 2), through the EU-KOR. Refer to **nl-vat-return**.
- **Dutch business trading in other EU countries (EU-KOR):** total EU turnover, including the Netherlands,
  must not exceed €100,000 in a calendar year, tested for **this year and last year**, and each chosen
  country's own threshold applies
  ([EU-KOR](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/kleineondernemersregeling-in-de-europese-unie-eu-kor)).
  Refer to **nl-vat-return**.

**Registration threshold (registratiedrempel), 2026.** A business with annual turnover of **at most
€2,200** that is **not required to register with KVK** can use the ordinary domestic VAT registration relief. This does not remove incidental obligations for reverse-charged supplies or services received and relevant intra-EU acquisitions: apply Wet OB art. 25b lid 3 and refer these transactions to the VAT Guide before assuming no reporting or payment is needed. It does
not apply if the business must register with KVK or is already registered for VAT, or applies the small-business exemption in another EU member state (Wet OB art. 25b). Once a supply takes
turnover above €2,200 in a calendar year, normal VAT applies **from that supply** and the business must
register
([registratiedrempel](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/hoe_werkt_de_btw/kleineondernemersregeling/registratiedrempel-voor-kleine-ondernemers)).

Confirm the statutory start, exit and cross-border conditions in [Wet OB arts. 25a–25e](https://wetten.overheid.nl/BWBR0002629). Domestic KOR and EU-KOR cannot be combined with the import scheme; EU-KOR also requires quarterly turnover reports and country-specific eligibility checks.

**Deciding on the KOR.** It usually suits a business selling to private customers with low costs. It
usually does not suit a business that sells to VAT-registered customers, or expects large investments
or a VAT refund.

### Step 6: Payroll registration and the DGA salary ([source](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/vermogen_en_aanmerkelijk_belang/aanmerkelijk_belang/loon_en_aanmerkelijk_belang/loon_en_aanmerkelijk_belang))

**Register as an employer.** When hiring staff for the first time, register with the Belastingdienst
on a form, **at the latest on the day the first employee starts**. A business established in the
Netherlands uses "Melding Loonheffingen Aanmelding werkgever"; one established abroad uses "Aanmelding
Onderneming buitenland". After the first employee starts, the Belastingdienst sends a **loonheffingen
number** and an **Aangiftebrief loonheffingen** that sets the return periods (renewed each November),
usually within 1 week. If employee-insurance premiums are due, a sector letter follows (within at most 8
weeks, usually 3) and the Whk premium letter within 4 weeks
([aanmelden als werkgever](https://www.belastingdienst.nl/wps/wcm/connect/nl/personeel-en-loon/content/aanmelden-als-werkgever)).
Running payroll: **netherlands-payroll**.

**The DGA is on the payroll.** A BV withholds payroll taxes on the salary of its director-major
shareholder like any employee
([Belastingdienst: bv](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/ondernemen/onderneming_starten/rechtsvorm/besloten-vennootschap-bv)).
So a BV whose owner works in it normally needs employer registration from the start.

**Customary salary (gebruikelijk loon), 2026.** It applies to an employee of a company in which they hold
a substantial interest, normally including at least 5% of issued capital (with a partner, direct or indirect), but share classes, rights and statutory deemed interests also need checking
(Wet IB 2001 arts. 4.6–4.11). The customary salary is at least the **highest** of:
1. the salary for the most comparable employment;
2. the salary of the best-paid employee of the company or of a related company;
3. **€58,000 in 2026** (€56,000 in 2025 and 2024).

Two exits:
- if the holder shows that comparable work is usually paid **less**, the Belastingdienst sets the salary
  at that lower amount (the comparison is with ordinary employment where no substantial interest plays a
  role);
- if the customary salary is **€5,000 or lower** in total across all companies in which the person has a
  substantial interest, and this can be shown, the actual salary is reported.

The start-up relief that allowed the statutory minimum wage **closed to new cases from 2023**
([Belastingdienst: loon en aanmerkelijk belang](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/vermogen_en_aanmerkelijk_belang/aanmerkelijk_belang/loon_en_aanmerkelijk_belang/loon_en_aanmerkelijk_belang)).
There is no "dispensation" form in this source: the lower amount is a position the BV must be able to
prove.

### Step 7: Ondernemer for income tax, and the self-employed deductions ([source](https://wetten.overheid.nl/BWBR0011353/2026-02-21))

This step applies to the owner of an eenmanszaak and to each VOF partner. It does not apply to a BV
shareholder (the BV is taxed separately).

**Is there an enterprise?** Being registered with KVK or for VAT does not make someone an ondernemer for
income tax. Wet IB 2001 art. 3.4 defines the ondernemer as the taxpayer for whose account an enterprise is
run and who is directly bound for its obligations. The Belastingdienst looks at, among other things:
whether profit is made (and how much), independence, capital, time spent, **number of clients**, visibility
to the market, entrepreneurial risk, and liability for debts. Activity in the hobby or family sphere is
not an enterprise. If there is a taxable income source but no entrepreneurship, distinguish employment income from "resultaat uit overig werk"; a hobby without an income source is not automatically taxable other work. For taxable other work, profit principles apply but **no zelfstandigenaftrek or investment deduction**
([wanneer bent u ondernemer](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/wanneer_bent_u_ondernemer_voor_de_inkomstenbelasting)).

**Urencriterium (Wet IB art. 3.6).**
- At least **1,225 hours** in the calendar year on one or more enterprises from which the person draws
  profit as an ondernemer; **and**
- more than half of the person's working time goes to those enterprises, **unless** the person was not an
  ondernemer in one or more of the five previous calendar years (then the hours test alone applies).
- The 1,225 hours are **not** pro-rated for a part-year start: someone starting on 1 July still needs
  1,225 hours.
- All hours on the business count (quotes, bookkeeping, the website), not only billed hours; being on call
  without working does not count. Keep records (diary, quotes, timesheets, invoices).
- In a partnership with a household or close family member, hours do not count if the person does 70% or
  more support work in an unusual partnership (the example is a dentist and a dental assistant), or if the
  partnership serves an enterprise from which only the related person draws profit.
- Pregnancy leave of up to 16 weeks in total counts as hours worked.
- A reduced hours test (verlaagd-urencriterium, at least 800 hours) applies only to the startersaftrek for
  ondernemers who are incapacitated for work (startersaftrek bij arbeidsongeschiktheid). Refer that case.
([voorwaarden urencriterium](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/voorwaarden_urencriterium))

**Zelfstandigenaftrek (Wet IB art. 3.76).**
- For an ondernemer who meets the urencriterium and has not reached AOW age at the start of the calendar
  year: **€1,200 in 2026** (€2,470 in 2025).
- The tax benefit is capped: in 2026 it is worked out at a rate of 37.56% (37.48% in 2025).
- It cannot exceed the profit before ondernemersaftrek, **unless** the person qualifies for the
  startersaftrek.
- Unused zelfstandigenaftrek can be carried forward for the next 9 years, set by a decision (beschikking),
  only where the taxpayer is entitled to the current-year zelfstandigenaftrek and has profit exceeding that current-year deduction. Use the oldest eligible unused amount first, within the remaining profit limit. Retain the assessment decisions and expiry schedule (Wet IB art. 3.76 lid 7).
- Not available on profit earned as a co-entitled person (medegerechtigde).
([zelfstandigenaftrek 2026](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/ondernemersaftrek-2026/zelfstandigenaftrek-2026);
[zelfstandigenaftrek 2025](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/verandering_inkomstenbelasting_vorige_jaren/veranderingen-inkomstenbelasting-2025/ondernemersaftrek-2025/zelfstandigenaftrek-2025))

**Startersaftrek (Wet IB art. 3.76 lid 3).**
- Adds **€2,123** to the zelfstandigenaftrek (2026 and 2025) if the person was not an ondernemer in one or
  more of the five previous calendar years **and** claimed the zelfstandigenaftrek no more than twice in
  that period. A previous year whose deduction was reduced to nil by the profit cap still counts as a year in which the zelfstandigenaftrek was applied (Wet IB art. 3.76 lid 5). Do not infer the count from cash tax benefit or assume every newly registered person qualifies.
- Requires entitlement to the zelfstandigenaftrek (so the urencriterium must be met).
- Not available after a "silent return" from a BV (geruisloze terugkeer) in the year or the five years
  before.
- It is not optional: if it applies, it is added. The combined deduction can create a loss, which is set
  off against other box 1 income or carried to other years.
([startersaftrek](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/ondernemersaftrek/startersaftrek))

**AOW age.** If the person has reached AOW age at the start of the calendar year, the zelfstandigenaftrek
and the startersaftrek are 50% of the normal amounts.

**MKB-winstvrijstelling (Wet IB art. 3.79a).** Every ondernemer (no hours test) gets an exemption of
**12.7%** of profit after ondernemersaftrek (2025 and 2026; 13.31% in 2024). Its benefit is capped at a rate
of 37.56% in 2026. It is automatic. With a loss it **reduces** the loss. Not available on profit as a
co-entitled person
([mkb-winstvrijstelling](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/mkb_winstvrijstelling)).

**Order of calculation:** profit → minus ondernemersaftrek (zelfstandigenaftrek incl. startersaftrek, and
other items) → minus 12.7% MKB-winstvrijstelling → taxable profit in box 1.

Do not finalize the legal-form recommendation or relief calculation while ownership, work pattern, residency, turnover or prior assessment history is missing. Record the missing input and refer to the corresponding specialist or calculation Guide. A salary reference amount is not a universal profit threshold for choosing a BV.

For banking, working capital and professional costs, obtain current written requirements and quotes from the selected bank and notary. Budget operating cash, payroll, accounting and any required audit separately; do not promise approval or a completion date from generic bank examples.

## Figures, with years

| Figure | Value | Year | Source |
| --- | --- | --- | --- |
| Zelfstandigenaftrek (below AOW age) | €1,200 | 2026 | Wet IB art. 3.76 lid 2 ([Wet IB 2001](https://wetten.overheid.nl/BWBR0011353/2026-02-21)); [Belastingdienst 2026 page](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/ondernemersaftrek-2026/zelfstandigenaftrek-2026) |
| Zelfstandigenaftrek | €2,470 | 2025 | Belastingdienst 2025 page |
| Startersaftrek (added to the above) | €2,123 | 2026 and 2025 | Wet IB art. 3.76 lid 3 |
| Deductions at or above AOW age | 50% of normal | 2026 | Wet IB art. 3.76 lid 4 |
| Rate that caps the benefit of the deductions | 37.56% | 2026 (37.48% in 2025) | Belastingdienst |
| MKB-winstvrijstelling | 12.7% of profit after ondernemersaftrek | 2025 and 2026 (13.31% in 2024) | Wet IB art. 3.79a |
| Urencriterium | at least 1,225 hours | every year | Wet IB art. 3.6 |
| Substantial interest | at least 5% | every year | Wet IB art. 4.6 |
| Customary salary floor | €58,000 | 2026 (€56,000 in 2025 and 2024) | Belastingdienst |
| Customary salary de minimis | €5,000 or lower | 2026 | Belastingdienst |
| KOR turnover limit | not more than €20,000 in this year and in last year | 2026 | Wet OB art. 25a lid 1 |
| KOR, EU turnover limit (EU-established, not NL) | not more than €100,000 | 2026 | Wet OB art. 25a lid 2 |
| Registration threshold | at most €2,200 turnover | 2026 | Belastingdienst |
| VAT rates that count toward turnover | 21%, 9% and 0% | 2026 | Belastingdienst KOR page |
| VPB rates | 19% up to €200,000; 25.8% above | 2026 (same in 2025) | Belastingdienst |
| NV minimum capital (authorised, issued and paid-up) | forty-five thousand euro | current | BW 2:67 |
| BV minimum capital | none | current | BW 2:175, 2:178 |

Figures from 2027 are not covered. Wet IB art. 3.76 shows a future amendment from 1 January 2027: check
the 2027 amounts when they are published.

## Boundaries and exceptions ([source](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/voorwaarden_urencriterium))

| Situation | Rule |
| --- | --- |
| Registered with KVK and for VAT, but few clients or tiny profit | May still not be an ondernemer for income tax: no zelfstandigenaftrek |
| Started mid-year | Still needs 1,225 hours; no pro-rating |
| New starter who also has a job | Only the 1,225 hours test applies if not an ondernemer in one of the 5 previous years; the "more than half" test is dropped |
| Starter with profit lower than the deductions | Startersaftrek case: full zelfstandigenaftrek allowed, creating a loss |
| Not a starter, low profit | Zelfstandigenaftrek capped at profit; the rest carries forward 9 years, usable only with current-year entitlement and profit exceeding that year's deduction; oldest unused amount first |
| Partner in family VOF doing mostly support work | 70% or more support work in an unusual partnership: hours do not count |
| Turnover this year at most €20,000 but last year above | KOR not available this year |
| Turnover passes €20,000 while in KOR | Must leave the KOR at once |
| Turnover at most €2,200, KVK registration required | Registration threshold does not apply; KOR may |
| Sale of a used business asset | Not counted toward the KOR limit |
| Working shareholder with a holding below 5% | Do not conclude from that percentage alone: check direct/indirect holdings, partner holdings, share classes, options and applicable statutory deemed-interest rules; refer uncertain cases |
| DGA can prove comparable work pays less | Customary salary set at the lower amount |
| BV contract signed before the deed | Signers jointly and severally liable until the BV ratifies it, unless expressly agreed otherwise; after ratification still liable for loss if they knew or should have foreseen the BV could not perform (presumed if bankrupt within one year of incorporation) |
| BV trading before first KVK registration | Directors jointly and severally liable with the BV |
| Annual accounts not adopted within two months after the preparation deadline | Board must publish the prepared accounts at once, marked "not yet adopted" (2:394 lid 2) |
| Annual accounts published late | Presumption of mismanagement if the BV goes bankrupt (2:248 lid 2); minor lapses ignored |
| Non-EU founders wanting online formation | BW 2:175a provides it for EU nationals; otherwise plan on the usual deed before a notary (check with the notary) |

## Worked cases ([source](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/ondernemersaftrek-2026/zelfstandigenaftrek-2026))

**Case 1: first-year sole trader (2026).** Sanne starts an eenmanszaak on 1 February 2026. She is below AOW age at the start of the year, was never an
ondernemer before, works 1,400 hours, and has no other job. Profit before deductions: €40,000.
- Urencriterium met (at least 1,225 hours; as a starter, the "more than half" test does not apply).
- Zelfstandigenaftrek €1,200 + startersaftrek €2,123 = €3,323.
- Profit after ondernemersaftrek: €40,000 − €3,323 = €36,677.
- MKB-winstvrijstelling: 12.7% × €36,677 = €4,657.98.
- Taxable profit in box 1: €36,677 − €4,657.98 = €32,019.02.

**Case 2: late start, hours missed (2026).** Daan starts on 1 September 2026 and works 600 hours by year-end.
Profit €10,000. He fails the urencriterium (hours are not pro-rated), so no zelfstandigenaftrek and no
startersaftrek. He is still an ondernemer, so he gets the MKB-winstvrijstelling: 12.7% × €10,000 = €1,270.
Taxable profit: €8,730.

**Case 3: starter with low profit (2026).** Eva is below AOW age at the start of the year, qualifies for the startersaftrek and has profit of €2,000.
Because she qualifies for the startersaftrek, the zelfstandigenaftrek is not capped at profit. Deduction
€3,323, so a loss of €1,323. The MKB-winstvrijstelling reduces the loss by 12.7% × €1,323 = €168.02, leaving
a loss of €1,154.98, which she can set off against other box 1 income or carry to other years.

**Case 4: KOR timing (2026).** A hairdresser (sole trader) had turnover of €22,500 in 2025 and expects €15,000
in 2026. The KOR is not available in 2026, because 2025 turnover was above €20,000. If 2026 turnover stays
at or below €20,000 and 2027 turnover is also expected to stay at or below €20,000 (the limit applies to the
year of joining and the year before), she can join from 1 January 2027; the application must arrive by 4
December 2026.

**Case 5: registration threshold crossed.** A seller not required to register with KVK has turnover of
€1,500 by 15 September and receives an advance of €800 on 16 September. Turnover is now €2,300, above
€2,200. From 16 September normal VAT rules apply, the advance is treated as including VAT, and the seller
must register as a VAT entrepreneur (and may then consider the KOR).

**Case 6: DGA customary salary (2026).** Mila owns all the shares in a new BV. Its best-paid employee earns €64,000.
The customary salary is at least the highest of the comparable-job salary, €64,000 and €58,000, so at least
€64,000, unless the BV can make a lower comparable salary plausible. Employer registration is required at the latest on the first working day of the first employee, including the working DGA; do not wait for the salary payment date.

**Case 7: unused deduction but no current entitlement.** A profitable former entrepreneur has an unused-deduction assessment but does not satisfy the current-year hours criterion. Do not offset the old deduction merely because there is sufficient profit; current-year entitlement is required. If entitled in a later year within the carry period, use eligible amounts oldest first.

**Case 8: nil-cap starter lookback.** A previous ordinary zelfstandigenaftrek was reduced to nil by the profit cap. Count that year as an application for the starter lookback, even though no cash deduction was obtained. Check the complete previous five-year record.

**Case 9: electronic formation with assets.** EU founders propose an electronic deed and contribution of equipment. The electronic route cannot accept that in-kind contribution; obtain the ordinary notarial route and required description. Cash-only formation may use the electronic route if all its other conditions are met (BW 2:191a lid 4).

**Case 10: first-year audit classification.** A new ordinary BV meets the applicable small-company size criteria at the end of its first financial year. Do not demand two historical balance dates before considering the exemption: article 398 lid 1 applies to the first and second years. Still check group aggregation, assembly decisions and statutory exclusions before confirming the exemption.

## When to refuse or refer

- **Refer to a notary** for the BV deed, articles, share classes and contributions in kind.
- **Refer to KVK (check)** for fees, online steps, UBO filing mechanics and public access to UBO data.
- **Refer to nl-corporate-tax** for the BV's VPB computation, fiscal unity, participation exemption and
  the choice between salary and dividend.
- **Refer to netherlands-payroll** for running payroll, the expat scheme, employee insurance and the
  Whk premium.
- **Refer to nl-vat-return / netherlands-vat-return** for VAT returns, the EU-KOR and cross-border supplies.
- **Refuse to confirm ondernemer status** as certain: it is a facts-and-circumstances test decided by the
  Belastingdienst after registration. Give the criteria and the risk.
- **Refer to a specialist** for converting an eenmanszaak into a BV (tax-neutral transfer), holding and
  financing structures (substance and treaty access), foreign legal forms (since 2025 some foreign
  partnership-like entities are treated as transparent;
  [buitenlandse rechtsvormen](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/ondernemen/onderneming_starten/rechtsvorm/buitenlandse-rechtsvormen)),
  work permits, and director liability claims.
- **Do not state a KVK fee, notary fee or bank timeline** as fact.

## Filing and payment ([source](https://www.belastingdienst.nl/wps/wcm/connect/nl/belastingaangifte/content/wat-gebeurt-er-als-ik-geen-aangifte-doe-of-te-laat-of-onvolledig))

| Obligation | Who | When |
| --- | --- | --- |
| VAT return and payment | VAT entrepreneurs not in the KOR | By the last day of the month after the period. Quarterly 2026: Q3 by 31 October 2026, Q4 by 31 January 2027. Annual filers: the 2026 return by 31 March 2027. Businesses established abroad have other dates ([dates](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/uiterste-aangifte-en-betaaldatums)) |
| Payroll tax return | Employers, including a BV paying its DGA | Periods set in the Aangiftebrief loonheffingen; see netherlands-payroll |
| Income tax return | Eenmanszaak owner, each VOF partner | By the date in the letter, usually 1 May; with an extension, use the actual granted date |
| VPB return | BV | Calendar-year BV: before 1 June of the next year; otherwise within 5 months of year-end; a short year ending on 31 December: by 1 June of the next year, ending in another month: before 1 April of the next calendar year; extension can be requested ([aangifte vpb](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/aangifte-vennootschapsbelasting-doen)) |
| Annual accounts prepared | BV board | Within five months of year-end, extendable by the general meeting by up to five months for special reasons (BW 2:210 lid 1) |
| Annual accounts published | BV | Within eight days of adoption; if not adopted within two months after the preparation deadline, publish the prepared accounts at once marked "not yet adopted"; at the latest twelve months after year-end (BW 2:394 lid 1, 2 and 3) |
| Statutory audit | BV | The accounts must be audited by a registeraccountant or other qualified auditor (BW 2:393 lid 1), unless the small-company exemption applies (BW 2:396 lid 7 disapplies 2:393 lid 1 for companies meeting the size criteria in 2:396 lid 1 on two consecutive balance sheet dates; for the first and second financial years, article 398 lid 1 permits the exemption where the first-year balance date meets the relevant criteria. Check group aggregation under article 396 lid 2, assembly decisions and exclusions under article 398, including public-interest entities; refer the size classification to the financial-statements method) |
| Shareholders' register | BV board | Kept by the board with names and addresses of all shareholders, date of acquisition, class of shares and amount paid on each share (BW 2:194 lid 1); keep it updated on every transfer |
| Handelsregister changes, including UBO | Obliged persons | At the latest one week after the change (Handelsregisterwet art. 20 lid 2) |

**Late income tax return.** After a reminder and a formal demand, a return filed more than 10 working days
after the demand date gets a default penalty of €469, which can rise to €6,709 for repeat lateness; late
filing also costs interest (belastingrente)
([Belastingdienst: te laat aangifte](https://www.belastingdienst.nl/wps/wcm/connect/nl/belastingaangifte/content/wat-gebeurt-er-als-ik-geen-aangifte-doe-of-te-laat-of-onvolledig)).

**Director liability for accounts.** If the BV goes bankrupt and the board did not comply with the
publication duty in BW 2:394 (or the bookkeeping duty in BW 2:10), the board is deemed to have performed
improperly and this is presumed to be an important cause of the bankruptcy; minor lapses are ignored
(BW 2:248 lid 2). The publication duty includes BW 2:394 lid 2: if the accounts are not adopted within two
months after the preparation deadline (five months, or the extended period, under BW 2:210 lid 1), the board
must publish the prepared accounts at once, stating that they are not yet adopted. With a standard five-month
deadline that is seven months after year-end, well before the twelve-month backstop. If all shareholders are
also directors, signing by all directors and supervisory directors also counts as adoption, provided the other
persons entitled to attend meetings have been able to see the accounts and agreed to this way of adoption,
unless the articles exclude it (BW 2:210 lid 5). The claim covers improper performance in the three years
before the bankruptcy (lid 6).
Distributions need board approval, which must be refused if the BV would then be unable to keep paying its
due debts (BW 2:216 lid 2).

**Returns being filed now for 2025.** A 2025 income tax return for a sole trader or VOF partner was due by
the date in the letter (usually 1 May 2026), or by the actual granted extended date. It uses the
2025 figures: zelfstandigenaftrek €2,470, startersaftrek €2,123, MKB-winstvrijstelling 12.7%, deduction benefit
capped at 37.48%. A calendar-year BV's 2025 VPB return was due before 1 June 2026 unless extended. The 2025
customary salary floor was €56,000.

## Completion checklist ([source](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/ondernemen/onderneming_starten/schrijf-uw-onderneming-in/schrijf-uw-onderneming-in))

- [ ] Legal form chosen, with liability explained (Step 1).
- [ ] For a BV: notary engaged; deed signed; contributions in kind described (dated within six months and
      signed by all founders; new description if value fell considerably); pre-incorporation contracts ratified,
      and the BV able to perform them.
- [ ] Shareholders' register set up by the board; audit requirement checked against the size criteria.
- [ ] Accounts calendar set: prepared within five months, adopted within two months after the statutory preparation deadline, including a valid extension (or published
      at once as "not yet adopted"), published within eight days of adoption.
- [ ] Handelsregister entry filed in time: business within one week before or after the start; BV within one
      week of incorporation (check KVK fee and steps).
- [ ] UBO details filed and kept up to date; changes within one week.
- [ ] Belastingdienst letters received (using the published processing target, with delayed letters followed up): VAT ID and OB number, or confirmation
      that the business is not a VAT entrepreneur.
- [ ] KOR decision made: turnover this year and last year at most €20,000; application only after receiving
      the numbers; VAT returns filed until the start date is confirmed.
- [ ] Registration threshold considered only if KVK registration is not required and turnover is at most
      €2,200.
- [ ] Employer registration made at the latest on the day the first employee (or DGA) starts.
- [ ] DGA customary salary set: highest of comparable job, best-paid employee, and €58,000 (2026), or a
      documented lower amount.
- [ ] Ondernemer status assessed against the Belastingdienst criteria.
- [ ] Hours log kept from day one (1,225 hours; no pro-rating).
- [ ] Startersaftrek eligibility checked (previous five years; at most two earlier claims; no silent return
      from a BV).
- [ ] Filing calendar set: VAT, payroll, income tax or VPB, annual accounts.
- [ ] Hand-offs made to nl-corporate-tax, netherlands-payroll and the VAT Guides where relevant.

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
