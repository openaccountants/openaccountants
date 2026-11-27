---
name: ie-formation
description: "Use this skill whenever asked about forming, incorporating, or registering a business in Ireland. Trigger on phrases like \"Ireland company formation\", \"CRO registration\", \"LTD Ireland\", \"DAC Ireland\", \"sole trader Ireland\", \"Form A1 Ireland\", \"PPS number business\", \"incorporate Ireland\", \"CORE portal\", \"register business Ireland\", \"RBO Ireland\", \"TR1 Ireland\", \"TR2 Ireland\", \"Companies Act 2014\", \"CLG Ireland\", \"PLC Ireland\", or any question about choosing or registering an Irish entity. Covers entity comparison (Sole Trader, Partnership, LP, LLP, LTD / CLS, DAC, CLG, PLC), CRO online portal (CORE) registration steps, Revenue TR1 / TR2 tax registration, sector-specific licensing (Central Bank, CCPC, DPC), RBO beneficial ownership filing, PPS number requirements for directors and beneficial owners, and tax treatment by entity type including the 12.5% trading CT rate and PRSI Class S. Out of scope: immigration / employment permits for non-EEA founders, bank account opening procedures (high-level only), full corporate governance and shareholders' agreement drafting, deep sector-specific regulatory licensing beyond signposting, listing on Euronext Dublin / ISEQ, and Irish Collective Asset-management Vehicles (ICAV). ALWAYS read this skill before advising on Irish entity formation."
jurisdiction: IE
tax_year: 2026
last_updated: 2026-11-27
version: 1.2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: formation
type: filing-howto
---

# Forming a business in Ireland (2026): sole trader, partnership or company, CRO, RBO and Revenue registration

## Scope

This skill is for someone starting a business in the Republic of Ireland, or an adviser helping them. It covers choosing the vehicle (sole trader, partnership, limited partnership, LTD, DAC, CLG, PLC, unlimited company), forming a company under the Companies Act 2014, directors and secretary, the EEA-resident director rule, the constitution, beneficial ownership (RBO) filing, registering with Revenue (Form TR1 / TR2, eRegistration on ROS), and the first compliance dates.

Figures are for tax year 2026 (calendar year 2026 for income tax, USC and VAT thresholds; accounting periods in 2026 for Corporation Tax). A dated section covers 2025 returns, and the original 2025 software-developer case is retained separately from the 2026 cases.

What this skill does not cover, with where to go instead:

- VAT returns, rates and reverse charge: the skill **ie-vat-return**.
- Corporation Tax computations, preliminary tax, close-company surcharges in detail, start-up relief (s.486C), R&D credit, Knowledge Development Box, Pillar Two: the skill **ie-corporation-tax**.
- Full payroll operation and benefit in kind; the Class S annual rates used below do not replace a payroll calculation by payment date.
- Immigration permissions for non-EEA founders, bank account opening, shareholders' agreements, funds (ICAV, ILP), listing on Euronext Dublin, and sector licensing beyond signposting.

**Sources.** The law is the Companies Act 2014 (section links below), the Taxes Consolidation Act 1997, the VAT Consolidation Act 2010, the [Registration of Business Names Act 1963](https://www.irishstatutebook.ie/eli/1963/act/30/enacted/en/print) and the [beneficial ownership regulations (S.I. No. 110 of 2019)](https://www.irishstatutebook.ie/eli/2019/si/110/made/en/print). Companies Act links below use the Law Reform Commission’s Revised Act, including commenced amendments; prospective amendments are not treated as operative. Revenue's guidance is on [revenue.ie](https://www.revenue.ie/en/starting-a-business/index.aspx).

**Filing route.** Use [CORE](https://core.cro.ie/) for Form A1. The [current statutory fee](https://www.irishstatutebook.ie/eli/2025/si/329/made/en/print) is €50 electronically; paper incorporation is not offered in the current fee table. CRO acceptance and a certificate of incorporation complete incorporation. Identity verification, name acceptance and any sector permission are separate steps. Do not promise a fixed turnaround; the [CRO processing queue](https://cro.ie/about-cro/whats-new/) changes.

## Ask the client first

- Who are the founders? Where does each one live (inside or outside the EEA), and does each have an Irish PPS number?
- What will the business do, and from where? Is any part of it regulated (financial services, credit, insurance, payments, crypto-assets, alcohol, food, childcare, health, transport, broadcasting, gambling)?
- Will it trade under a name other than the owner's own name?
- How much risk does the activity carry (liability to customers, product safety, debts to suppliers)? Does the owner need limited liability?
- Expected turnover and profit for the first two years, and how much profit the owner needs to draw to live on.
- Will it sell goods or services, to whom (Irish consumers, EU businesses, outside the EU), and will it buy goods from other EU countries?
- Will it employ anyone, or pay the directors a salary?
- Is it a non-profit, charity, club or owners' management company?
- Will outside investors come in, or will shares be offered to the public?
- Is there already a business (sole trader or partnership) that will be transferred into a company?
- Who will be the company secretary, and where will the registered office be?

## The method, step by step

1. **Check whether the plan is one this skill can handle.** Regulated activity, a charity, a fund, or a founder who needs an immigration permission all need a specialist in addition (see "When to refuse or refer").
2. **Choose the vehicle.** Use the decision rules below. For most owner-managed businesses the choice is sole trader or LTD; the deciding facts are liability risk, how much profit will be left in the business, and whether investors are coming.
3. **If a sole trader or partnership:** register a business name with the CRO within one month of adopting any name other than the owner's true name(s), then register with Revenue (TR1 or eRegistration) for Income Tax, and for VAT, employer PAYE and RCT if they apply.
4. **If a company:** pick the company type; confirm an EEA-resident first director or arrange a section 137 bond (an existing company can rely on an in-force section 140 certificate); appoint a secretary (not the sole director); draft the constitution; file Form A1 and the constitution through CORE, with the €50 fee and directors’ verified identity details.
5. **After incorporation:** keep the company's own beneficial ownership register and file with the RBO within 5 months; register with Revenue (TR2 or ROS through an agent) for Corporation Tax and, as needed, VAT, employer PAYE (compulsory if the directors are paid) and RCT.
6. **Diary the first compliance dates:** first annual return to the CRO; first Corporation Tax return and preliminary tax (see ie-corporation-tax); VAT returns (see ie-vat-return); Form 11 for self-employed individuals and proprietary directors.
7. **Record the reasons.** Write down why the vehicle was chosen and the facts it depends on (profit level, drawings, risk), so the choice can be revisited when they change.

## Choosing the vehicle

| Vehicle | Separate legal person? | Owner's liability | Tax on profits | Main uses | Official source |
| --- | --- | --- | --- | --- | --- |
| Sole trader | No | Unlimited | Income tax, USC and PRSI on profits, via Form 11 | One owner, low risk, profits mostly drawn | https://www.revenue.ie/en/starting-a-business/index.aspx |
| Partnership (Partnership Act 1890) | No | Unlimited: debts jointly; specified wrongs and misapplication jointly and severally (ss.9–12) | Each partner taxed on their share; the partnership registers on TR1 | Two or more people in business together, professional firms | https://www.irishstatutebook.ie/eli/1890/act/39/enacted/en/print |
| Limited partnership (Limited Partnerships Act 1907) | No | General partner unlimited; limited partner’s protection depends on registration, no management and no returned contribution | As a partnership | Specialist structures; at least one general and one limited partner | https://www.irishstatutebook.ie/eli/1907/act/24/enacted/en/print |
| LTD: private company limited by shares (Part 2, Companies Act 2014) | Yes | Limited to unpaid share capital | Corporation Tax; owners taxed when paid salary or dividends | The default company for owner-managed businesses | https://cro.ie/information-leaflets/company-incorporation-leaflet-1/ |
| DAC: designated activity company (Part 16) | Yes | Limited (by shares, or by guarantee with a share capital) | Corporation Tax | Where an objects clause is needed: joint ventures, special purpose vehicles, some regulated firms | https://cro.ie/information-leaflets/company-incorporation-leaflet-1/ |
| CLG: company limited by guarantee (Part 18) | Yes | Limited to the guarantee | Corporation Tax unless an exemption (such as charitable status) applies | Non-profits, clubs, charities, owners' management companies | https://cro.ie/information-leaflets/company-incorporation-leaflet-1/ |
| PLC: public limited company (Part 17) | Yes | Limited to unpaid share capital | Corporation Tax | Offering shares to the public, listing | https://cro.ie/information-leaflets/company-incorporation-leaflet-1/ |
| Unlimited company (Part 20) | Yes | Unlimited | Corporation Tax | Specialist uses (refer) | https://cro.ie/information-leaflets/company-incorporation-leaflet-1/ |

### Decision rules

- **Non-profit, club, charity or owners' management company:** consider a CLG. Charitable tax exemption is a separate application (Charities Regulator, then Revenue); forming a CLG does not give it.
- **Shares to be offered to the public, or a listing planned:** consider a PLC; incorporation alone does not authorise an offer or listing.
- **An objects clause is required** (by a regulator, a lender, or the joint-venture parties): DAC.
- **One owner, low risk, profit mostly drawn for living costs, or testing an idea:** sole trader.
- **Two or more professionals who want to share profits informally and accept unlimited liability:** partnership. Solicitors can use a limited liability partnership under the Legal Services Regulation Act 2015 (refer).
- **Otherwise** (limited liability wanted, profit to be kept in the business, investors expected, or trading income large enough that the 12.5% company rate on trading income ([Revenue: basis of charge](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax/basis-of-charge.aspx)) beats personal marginal rates on retained profit): LTD.

### Company filing details

Use the full proposed company name and a registered office in the State. An LTD name ends in Limited or Teoranta on registration; abbreviations are permitted afterwards. Name reservation, if used, is for the period notified by the Registrar, at most 28 days; it is not trade-mark protection. Prepare the principal activity description/NACE classification, first officers’ consents and the State-activity declaration.

### Partnership limits and specialist forms

A general partnership ordinarily needs at least two persons and the statutory 20-person limit applies, subject to s.1435 exceptions: each partner a statutory auditor for the accountancy exception, each a solicitor for the solicitors exception, specified thoroughbred horse-breeding LPs, and specified investment/loan-finance LPs with up to 50 persons. Banking has a separate 10-person restriction under s.1436. The old blanket “50 accountants” cap was wrong. Do not apply general LP rules to an investment limited partnership or assume an LLP is a separate corporation or can elect its tax treatment. Solicitors’ LLP approval, ILP/ICAV funds and qualifying-partnership accounting are **NON-USABLE HOLDS** for structure-specific advice. Check this point with one of our partner accountants.

For a 1907 Act LP, registration is essential: otherwise limited partners are treated as general partners. A limited partner taking part in management is liable for debts incurred while managing; withdrawing a contribution restores liability up to the amount withdrawn. Use CRO Forms LP1 and LP3 through the specialist registration route. [CRO partnership guidance](https://cro.ie/registration/qualifying-limited-partnerships/) and [ss.1435–1436](https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC1435).

### LTD: the rules that matter at formation (Companies Act 2014, Part 2)

- **Members.** One or more; the number of members may not exceed 149, excluding current employee-members and former employees who became members during employment and remained members continuously afterwards; joint holders count as one ([s.17](https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC17)).
- **Capacity.** An LTD has full and unlimited capacity to carry on any business or activity, whatever its constitution says ([s.38](https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC38)). It has no objects clause; if the founders need one, use a DAC.
- **Directors.** At least one ([s.128](https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC128)). DACs, CLGs and PLCs need at least two ([s.985](https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC985), [s.1194](https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC1194), [s.1088](https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC1088)).
- **Secretary.** Every company must have a secretary, who may be one of the directors, but where a company has only one director that person may not also be the secretary. The directors must make sure the secretary has the skills or resources to do the job ([s.129](https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC129)). A PLC secretary must also meet one of the qualification conditions in [s.1112](https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC1112).
- **Constitution.** One document in the form in Schedule 1 (or as near to it as possible), stating the name, that it is a private company limited by shares, that members' liability is limited, and the share capital. It may state an authorised share capital or simply state that the shares are divided into shares of a fixed amount; each subscriber takes at least one share ([s.19](https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC19)).
- **Registration documents.** The constitution goes to the Registrar with the statement of first directors, secretary and registered office (s.22), and a declaration (s.24) that the registration requirements are met and that the company is being formed to carry on an activity in the State ([s.21](https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC21), [s.24](https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC24)). The declaration may be made by a director, the secretary or the solicitor forming the company.
- **AGM.** An LTD need not hold an AGM in a year if all members entitled to attend and vote sign a written resolution before the latest date for the meeting that acknowledges receipt of the financial statements, resolves everything the AGM would have resolved, and confirms no change of auditor ([s.175](https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC175)). PLC and other company-type AGM adaptations require separate governance advice.

### PLC capital ([s.1000](https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC1000), [s.1026](https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC1026))

- The authorised minimum is €25,000. A newly incorporated PLC must obtain the Registrar’s s.1010 trading certificate before doing business or borrowing, proving allotted nominal capital at least equal to that minimum. This is distinct from incorporation.
- Subject to the statutory employee-share-scheme exception, a PLC may not allot a share unless at least one-quarter of nominal value and the whole premium is paid. For €25,000 ordinary nominal capital without premium, one-quarter is €6,250.

### The EEA-resident director rule ([s.137](https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC137), [s.140](https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC140))

At least one director must be resident in an EEA state (the EU plus Iceland, Liechtenstein and Norway; the UK is not in the EEA). Alternate directors do not count. There are two ways out:

- **A bond.** The company holds a bond in the prescribed form, in force, to the value of €25,000, which pays fines under the Companies Act and certain tax penalties if the company fails to pay them. The [prescribed minimum term is two years](https://www.irishstatutebook.ie/eli/2015/si/215/made/en/print). Arrange the prescribed bond before filing where no proposed director is EEA-resident (s.22(6)); a future hope of obtaining a s.140 certificate is insufficient.
- **A section 140 certificate.** The Registrar grants a certificate that the company has a real and continuous link with an economic activity carried on in the State. A written statement from Revenue, given within the 2 months before the application, that it has reasonable grounds to believe the link exists, is treated as proof. The link exists if the company is managed from a place of business in the State by people it authorises, carries on a trade in the State, or is in a group with a company that meets either test.

Breaking the rule is a category 4 offence for the company and every officer in default.

### Business names ([Registration of Business Names Act 1963](https://www.irishstatutebook.ie/eli/1963/act/30/enacted/en/print))

- An individual, partnership or company carrying on business under a name other than its true name (for a company, its corporate name) must register the business name with the CRO. For companies the Companies Act repeats this for each company type.
- The particulars must be furnished within one month after the business name is adopted (s.6), and any change within one month after the change (s.7).
- The certificate must be displayed at the principal place of business (or corporate registered/principal office) and every branch or place where business is normally carried on (s.8), and the true names must appear on business letters and similar documents (s.18).
- Forms and fees: RBN1 (individual), RBN1A (partnership), RBN1B (company). [Fees](https://cro.ie/publications/business-names-forms-fees/): €20 electronic or €40 paper. Changes use RBN2 / RBN2A / RBN2B; RBN3 is cessation, not renewal. Do not use the historical three-year renewal claim.

### Beneficial ownership: the RBO ([S.I. No. 110 of 2019](https://www.irishstatutebook.ie/eli/2019/si/110/made/en/print))

- **Who:** every company and other body corporate incorporated in the State (a "relevant entity"), including LTDs, DACs, CLGs, PLCs, unlimited companies and registered societies. The regulations do not apply to a company listed on a regulated market subject to EU-consistent disclosure requirements, or subject to equivalent international standards (reg. 4(2)).
- **Own register:** the company must keep its own beneficial ownership register (reg. 15). "Beneficial owner" takes its meaning from Article 3(6)(a) of the Fourth Anti-Money Laundering Directive: the natural persons who ultimately own or control the entity (more than 25% of shares or voting rights is an indicator, not the sole test: control by other means also counts). If all possible means have been exhausted with no grounds for suspicion and no owner is identified, or there is doubt about an identified owner, record the investigation and enter its senior managing officials (the directors and any chief executive) instead, stating the nature and extent of their control.
- **Central register:** a company formed now must deliver the information to the Registrar of Beneficial Ownership within 5 months from its incorporation (reg. 20(2)). After that, whenever the company must enter, change or delete information in its own register, it must file the matching change with the RBO within 14 days from the date the entry in its own register was due (reg. 23).
- **Penalties:** failing to keep the register or to file is an offence: on summary conviction a class A fine, on indictment a fine of up to €500,000 (regs. 15 and 28).
- **Public access:** **NON-USABLE HOLD:** do not promise unrestricted public access or a particular access entitlement from the historical 22 November 2022 discussion. Check this point with one of our partner accountants.
- **Filing mechanics:** use the RBO online portal separately from CRO incorporation. Obtain beneficial owners’ PPSNs where issued; do not use an IPN to avoid an existing PPSN. A person without a PPSN uses the CRO VIF/IPN process. [RBO FAQs](https://rbo.gov.ie/faqs/) confirm there is no beneficial-owner filing fee.

### Registering with Revenue ([Revenue: registering for tax](https://www.revenue.ie/en/starting-a-business/registering-for-tax/index.aspx))

A Tax Reference Number is not issued automatically on incorporation. A company must also submit its Statement of Particulars (Form 11F CRO) to Revenue within 30 days after it begins trading; see [Revenue: business types](https://www.revenue.ie/en/starting-a-business/what-is-a-business/index.aspx). You must register with Revenue when you become a sole trader, set up a partnership or trust, or start a new company.

| Who | How | Taxes the form covers |
| --- | --- | --- |
| Sole trader ([Revenue](https://www.revenue.ie/en/starting-a-business/registering-for-tax/how-to-register-for-tax-as-a-sole-trader.aspx)) | Needs a PPSN first; the PPSN becomes the TRN once registered. Register on ROS (eRegistration) or, if a PAYE employee, for Income Tax on myAccount. Non-residents who cannot register online use Form TR1 (FT) | Income Tax, employer PAYE, VAT, RCT (and CGT on TR1 (FT)) |
| Partnership or trust ([Revenue](https://www.revenue.ie/en/starting-a-business/registering-for-tax/how-to-register-for-tax-as-a-trust-or-partnership.aspx)) | Tax agent registers online through ROS; otherwise Form TR1 (non-resident: TR1 (FT)) | Income Tax, employer PAYE, VAT, RCT |
| New company ([Revenue](https://www.revenue.ie/en/starting-a-business/registering-for-tax/how-to-register-for-tax-as-a-new-company.aspx)) | Needs a CRO number first. A tax agent must register it online through ROS; a company without an agent submits Form TR2 (foreign company: TR2 (FT)) | Corporation Tax, employer PAYE, VAT, RCT |

- **Paper when online was required:** Revenue returns a paper application that should have been made online, unprocessed.
- **Not eligible for eRegistration** ([Revenue: eRegistration](https://www.revenue.ie/en/starting-a-business/registering-for-tax/eregistration.aspx)) include companies that have no Irish-resident directors and unincorporated bodies and non-profits not represented by an agent. They use the paper TR forms.
- **After registration:** companies, sole traders and partnerships must file returns and pay through ROS.
- **Employer PAYE** ([Revenue: registration of employers](https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/registration-of-employers-for-paye-purposes/index.aspx)): register before paying any employee, and report pay and deductions on or before each payday. A company must register as an employer and operate PAYE on its directors' pay even if it has no other employees; a director of an Irish-incorporated company pays PAYE on director's pay wherever resident.
- **VAT:** see the thresholds below and the skill ie-vat-return.
- **RCT:** register if the business is a principal contractor in construction, forestry or meat processing (see Revenue's RCT pages).
- **Tax residence of the company** ([Revenue: company residency rules](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax/company-residency-rules.aspx)): a company incorporated in Ireland on or after 1 January 2015 is tax resident here unless a tax treaty makes it resident in another country. A foreign-incorporated company is resident here if centrally managed and controlled here.

## Figures for 2026

### Corporation Tax rates ([Revenue: basis of charge](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax/basis-of-charge.aspx))

| Item | 2026 | Condition | Official source |
| --- | --- | --- | --- |
| Trading income | 12.5% | Profits of a trade carried on by the company | https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax/basis-of-charge.aspx |
| Non-trading income and excepted trades | 25% | Rental and investment income; income of an "excepted trade" as defined in the Taxes Consolidation Act | same |
| Accounting period | at most 12 months | A longer set of accounts is split into two CT periods | same |

### Income tax bands and credits for 2026 ([Revenue: tax rates, bands and reliefs](https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/tax-relief-charts/index.aspx))

| Item | 2026 | 2025 | Official source |
| --- | --- | --- | --- |
| Standard rate band, single person without qualifying children | €44,000 @ 20%, balance @ 40% | €44,000 @ 20%, balance @ 40% | https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/tax-relief-charts/index.aspx |
| Single Person tax credit | €2,000 | €2,000 | same |
| Employee (PAYE) tax credit (maximum; qualifying PAYE income) | €2,000 | €2,000 | same |
| Earned Income Tax Credit (maximum) | €2,000 | €2,000 | same |

The Employee Credit is capped at 20% of qualifying PAYE income below €10,000. The Earned Income Credit is for self-employed earned income and for pay earned by proprietary directors, who cannot get the Employee Tax Credit on that pay. It is the lower of €2,000 or 20% of qualifying earned income, and where someone has both kinds of income the two credits together cannot exceed the Employee Tax Credit maximum ([Revenue: Earned Income Credit](https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/income-and-employment/earned-income-credit/index.aspx)).

### Universal Social Charge for 2026 ([Revenue: USC rates](https://www.revenue.ie/en/jobs-and-pensions/usc/standard-rates-thresholds.aspx))

| Band | 2026 rate | Official source |
| --- | --- | --- |
| First €12,012 | 0.5% | https://www.revenue.ie/en/jobs-and-pensions/usc/standard-rates-thresholds.aspx |
| Next €16,688 | 2% | same |
| Next €41,344 | 3% | same |
| Balance | 8% | same |

A USC surcharge of 3% applies if non-PAYE income is more than €100,000 a year, so self-employed income above that level bears 11% ([Revenue: other rates of USC](https://www.revenue.ie/en/jobs-and-pensions/usc/other-rates.aspx)). Aggregate income not exceeding €13,000 is exempt from USC; above that boundary the full chargeable income is assessed. For those aged 70 or over, or holding a full medical card, with aggregate income no more than €60,000, reduced rates are 0.5% on €12,012 and 2% on the balance. The cases below assume ordinary rates, no other income or reliefs.

PRSI: annual self-assessed Class S income uses 4.125% for 2025 and 4.2375% for 2026, with a €650 annual minimum where liable. The ordinary Class S entry threshold is €5,000 annual reckonable income; age, pension and cross-border coverage conditions matter. A working director controlling at least 50% is outside ordinary employed-contributor treatment; do not assume Class A for a sole owner. Directors below that level and overseas social-security cases need a status assessment. Payroll Class S rates are 4.2% through 30 September 2026 and 4.35% from 1 October 2026: a salary’s actual PRSI needs payment dates and payroll reconciliation, rather than automatically applying the self-assessment blend. See [DSP contribution guide](https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf) and [director employment exclusion](https://www.irishstatutebook.ie/eli/2013/act/20/section/16/enacted/en/html).

### VAT registration thresholds ([Revenue: VAT thresholds](https://www.revenue.ie/en/vat/vat-registration/who-should-register-for-vat/persons-required-register-goods-services-abroad.aspx))

Registration is obligatory when annual turnover (calendar year, excluding VAT) exceeds the threshold. Below the threshold a business may elect to register.

| Supplies | Threshold | Official source |
| --- | --- | --- |
| Services only | €42,500 | https://www.revenue.ie/en/vat/vat-registration/who-should-register-for-vat/persons-required-register-goods-services-abroad.aspx |
| Goods at the reduced or standard rate that the business made from zero-rated materials | €42,500 | same |
| Goods and services, where 90% or more of turnover is from goods (other than the above) | €85,000 | same |
| Goods | €85,000 | same |
| Distance sales of goods and cross-border telecoms, broadcasting and electronic services to other EU consumers (EU-wide total; supplier established only in Ireland) | €10,000 | https://www.revenue.ie/en/vat/vat-registration/who-should-register-for-vat/elect-register-vat.aspx |
| Acquisitions of goods from other EU Member States | €41,000 | same |

For domestic threshold eligibility, test the current and preceding calendar year under the SME rules, not only the current projection. A non-established supplier making supplies taxable in Ireland generally has no registration threshold, but first identify the person liable: general-rule services supplied from abroad to an Irish business are normally accounted for by that customer under reverse charge. Eligible EU-established businesses may use the separately registered cross-border SME exemption; this is not automatic and is unavailable merely because turnover is low. The scheme requires the relevant domestic thresholds and Union turnover not exceeding €100,000 in the current and previous calendar year, identification through the establishment Member State with a valid EX number for the exempt state, and quarterly reporting. For Irish businesses using the scheme abroad, establishment must be in Ireland only. Occasional disposals of business assets are excluded from annual turnover. See [place-of-supply rules](https://www.revenue.ie/en/vat/vat-on-services/when-is-vat-charged-on-services/general-place-of-supply-rules-for-services.aspx), [SME conditions](https://www.revenue.ie/en/vat/vat-registration/eu-vat-sme-scheme/index.aspx) and ie-vat-return.

The €10,000 distance-sales/TBE figure is a place-of-supply boundary, using both the current and preceding calendar year; it is not a general tax-free sales allowance. Destination VAT can be reported through Union OSS where applicable. EU acquisitions and imported services can create separate registration duties even below the domestic turnover thresholds.

### Company law figures (Companies Act 2014)

| Rule | Figure | Section | Official source |
| --- | --- | --- | --- |
| Bond instead of an EEA-resident director | €25,000 | [s.137](https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC137) | https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC137 |
| PLC authorised minimum share capital | €25,000 | [s.1000](https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC1000) | https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC1000 |
| PLC shares paid up at allotment | at least one-quarter of nominal value plus all premium | [s.1026](https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC1026) | https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC1026 |
| RBO fine on indictment | up to €500,000 | [S.I. No. 110 of 2019, reg. 28](https://www.irishstatutebook.ie/eli/2019/si/110/made/en/print) | https://www.irishstatutebook.ie/eli/2019/si/110/made/en/print |

## Boundaries and exceptions

| Situation | Rule | What to do | Official source |
| --- | --- | --- | --- |
| Sole director wants to be secretary too | Not allowed where the company has only one director (s.129(6)) | Appoint a second person as secretary, or a second director who can also be secretary | https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC129 |
| No director lives in the EEA | [s.137](https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC137) applies unless a bond or a s.140 certificate is in force | Bond (€25,000), a s.140 certificate backed by a Revenue statement, or appoint a genuine EEA-resident director. Never a nominee with no real role | https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC137 |
| UK-resident director only | The UK is not an EEA state | Same as above | https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC137 |
| Wants an objects clause | An LTD has unlimited capacity (s.38) | Form a DAC | https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC38 |
| DAC, CLG or PLC with one director | At least two directors required | Appoint a second director | https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC985 |
| More than 149 members in an LTD or DAC | Registration above the limit is void (ss.17 and 965) | Apply the precise employee/former-employee exclusions and joint-holder rule; otherwise consider another form | https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC17 |
| Trading under a name other than the true name | Business name must be registered within one month of adopting it | File RBN1 / RBN1A / RBN1B with the CRO | https://www.irishstatutebook.ie/eli/1963/act/30/enacted/en/print |
| Company with no Irish-resident directors | Cannot use eRegistration unless through an agent | Agent registers on ROS, or paper TR2 / TR2 (FT) | https://www.revenue.ie/en/starting-a-business/registering-for-tax/eregistration.aspx |
| Company pays only its directors | Must still register as an employer and operate PAYE | Register before the first payment | https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/registration-of-employers-for-paye-purposes/index.aspx |
| Turnover exactly at a VAT threshold | Obligation arises only when turnover exceeds the threshold | Monitor the calendar-year total; may elect to register earlier | https://www.revenue.ie/en/vat/vat-registration/who-should-register-for-vat/persons-required-register-goods-services-abroad.aspx |
| Non-established business selling into Ireland | Identify supply location and liable person first; no general turnover threshold where supplier is liable | General-rule B2B services normally reverse-charged by customer; test separately registered EU SME eligibility for supplier-liable supplies | https://www.revenue.ie/en/vat/vat-registration/who-should-register-for-vat/option-to-tax-lettings.aspx |
| CLG wanting charity tax exemption | Incorporation does not give charitable tax exemption | Charity registered with Charities Regulator can apply to Revenue; detailed conditions require separate advice | https://www.revenue.ie/en/companies-and-charities/charities-and-sports-bodies/charitable-tax-exemption/index.aspx |
| Incorporated in Ireland but run from abroad | Resident here from incorporation (on or after 1 January 2015) unless a treaty says otherwise | Do not structure around residence; refer if a treaty tie-breaker is relied on | https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax/company-residency-rules.aspx |
| Company formed with no activity in the State | The s.24 declaration must state that a purpose is carrying on an activity in the State | Refer | https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC24 |

## Worked cases

### Case 1: Aoife, software developer, sole trader, 2026 ([Revenue: tax rates, bands and reliefs](https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/tax-relief-charts/index.aspx))

Aoife lives in Dublin, is single with no children, and expects revenue of €120,000 and expenses of €25,000 in 2026, so taxable profit of €95,000. She sells services to Irish and EU businesses.

Income tax 2026 ([Revenue: tax rates, bands and reliefs](https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/tax-relief-charts/index.aspx)):

- €44,000 at 20% = €8,800
- €51,000 at 40% = €20,400
- Gross tax €29,200, less Single Person credit €2,000 and Earned Income Credit €2,000 (credits €4,000) = **€25,200**

USC 2026 ([Revenue: USC rates](https://www.revenue.ie/en/jobs-and-pensions/usc/standard-rates-thresholds.aspx)):

- €12,012 at 0.5% = €60.06
- €16,688 at 2% = €333.76
- €41,344 at 3% = €1,240.32
- Balance €24,956 (€95,000 less €70,044) at 8% = €1,996.48
- Total USC **€3,630.62**. Her non-PAYE income is not more than €100,000, so no 3% surcharge.

Assuming ordinary Class S liability on all €95,000, annual self-assessed PRSI is €95,000 × 4.2375% = **€4,025.63**, giving Income Tax + USC + PRSI of **€32,856.25** (rounded components). VAT: do not treat all €120,000 as Irish taxable turnover without checking where the services are supplied. Separate the Irish and EU business sales, verify customer status, and address EU reverse-charge invoices/VIES as well as the €42,500 domestic threshold ([Revenue: VAT thresholds](https://www.revenue.ie/en/vat/vat-registration/who-should-register-for-vat/persons-required-register-goods-services-abroad.aspx)). Registration: eRegistration on ROS for Income Tax and VAT; a business name only if she trades under a name other than her own.

### Case 2: Aoife through an LTD, 2026 ([Revenue: basis of charge](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax/basis-of-charge.aspx))

Same business through Aoife Dev Studio Limited. Aoife is the sole director and sole shareholder; her brother is the secretary (s.129(6)). She is EEA resident, so no bond is needed. The company pays her a salary of €60,000 and has profit after the salary of €35,000 (€120,000 less €25,000 less €60,000), all trading income.

- Corporation Tax at 12.5% ([Revenue: basis of charge](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax/basis-of-charge.aspx)): €35,000 x 12.5% = **€4,375**, leaving €30,625 after tax in the company.
- Income tax on the salary: €44,000 at 20% = €8,800 plus €16,000 at 40% = €6,400, so €15,200; less Single Person credit €2,000 and, as a proprietary director, the Earned Income Credit €2,000 (not the Employee Tax Credit) ([Revenue: Earned Income Credit](https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/income-and-employment/earned-income-credit/index.aspx)) = **€11,200**.
- USC on the salary ([Revenue: USC rates](https://www.revenue.ie/en/jobs-and-pensions/usc/standard-rates-thresholds.aspx)): €60.06 + €333.76 + (€60,000 less €28,700 = €31,300 at 3% = €939) = **€1,332.82**.
- The company must register for Corporation Tax and as an employer (PAYE on her salary is compulsory even with no other staff), file with the RBO within 5 months, and file its first annual return. Apply Case 1’s sales-location/customer-status analysis for VAT.
- **PRSI:** as the sole working owner, use Class S rather than automatically Class A; the €60,000 gross salary alone does not establish payment dates or final payroll PRSI. The €35,000 profit assumes the stated expenses already cover all other business costs.
- **Close service company surcharge.** A close company whose main income comes from a profession, such as a computer programmer, pays a surcharge of 15% on one half of its undistributed trading income if the income is not distributed within 18 months of the end of the accounting period ([Revenue: surcharge on undistributed income](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/close-companies/surcharge.aspx)). Leaving the €30,625 in the company is not free; compute the exposure with ie-corporation-tax.

Comparing the two: the company route defers tax on the profit left in the company, but that profit is taxed again when paid out, the surcharge can apply, and running a company costs more (accounts, annual return, payroll). No net saving is established without actual PRSI, distributions, surcharge and compliance costs. Record those assumptions before recommending either route.

### Case 3: two founders in the United States

Two US-resident founders want an Irish LTD to sell software into the EU. Neither is EEA resident, so s.137 bites. At incorporation use a genuine EEA-resident first director or a €25,000 bond in the prescribed form ([s.137](https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC137)); once incorporated, the company can instead obtain a s.140 certificate for an actual real and continuous Irish economic link, supported by the Revenue statement given within the preceding 2 months. As the company has no Irish-resident directors it cannot use eRegistration itself; an agent registers it on ROS or it files a paper TR2 ([Revenue: eRegistration](https://www.revenue.ie/en/starting-a-business/registering-for-tax/eregistration.aspx)). The directors' Irish pay is subject to PAYE. Their immigration position and US tax treatment are out of scope: refer. For directors without a PPSN, complete the CRO VIF/IPN identity process; an existing usable RBO/IPN number avoids a duplicate application. Since 30 April 2026, the CRO requires the witness and declarant physically in the same room for VIF verification; no online witnessing. See [CRO identity guidance](https://cro.ie/registration/beneficial-ownership/rbo-no-ppsn/) and [CRO announcements](https://cro.ie/about-cro/whats-new/).

### Case 4: key dates for a company incorporated on 10 March 2026

- RBO filing: within 5 months from incorporation, so by 10 August 2026 ([S.I. No. 110 of 2019, reg. 20(2)](https://www.irishstatutebook.ie/eli/2019/si/110/made/en/print)).
- First annual return date: 6 months after incorporation, 10 September 2026 ([s.345](https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC345)); the return must be delivered not later than 56 days after that date, so by **5 November 2026** (the former 8 October result used the superseded 28-day rule) ([s.343](https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC343)). Financial statements need not be annexed to the first annual return ([s.349](https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC349)). Later returns fall on the anniversary of the first annual return date.
- Corporation Tax: if the first accounting period ends on 31 December 2026, the CT1 is due, and any balance payable, by 23 September 2027 ([Revenue: payment and filing](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax-payment-and-filing/payment-and-filing.aspx)). Preliminary tax: see ie-corporation-tax.

### Case 5: services business under the VAT threshold

A new consultancy expects services turnover of €40,000 in 2026. Assuming Irish-established, taxable domestic services, no previous-year threshold breach and no other registration trigger, compulsory registration does not arise from €40,000 turnover alone because it does not exceed €42,500, but it may elect to register (for example to recover VAT on start-up costs, or because its customers are VAT-registered businesses). Once turnover exceeds €42,500 it must register ([Revenue: VAT thresholds](https://www.revenue.ie/en/vat/vat-registration/who-should-register-for-vat/persons-required-register-goods-services-abroad.aspx)). The timing and mechanics are in ie-vat-return.

### Recomputed checks for the first two cases

```oa-check
name: Aoife, sole trader, profit EUR 95,000 (2026)
inputs:
  profit: 95000
steps:
  - gross: min(profit, 44000) * 0.20 + (profit - 44000) * 0.40
  - income_tax: gross - 4000
  - usc: 12012 * 0.005 + 16688 * 0.02 + 41344 * 0.03 + (profit - 70044) * 0.08
expected:
  income_tax: 25200.00
  usc: 3630.62
```

```oa-check
name: Same business through a company, taxable profit EUR 35,000, salary EUR 60,000
inputs:
  profit: 35000
  salary: 60000
steps:
  - corporation_tax: profit * 0.125
  - salary_gross_tax: 44000 * 0.20 + (salary - 44000) * 0.40
expected:
  corporation_tax: 4375.00
  salary_gross_tax: 15200.00
```

## When to refuse or refer

- **Sham nominee directors.** Do not arrange an EEA-resident "director" who has no real role just to satisfy s.137. Use the bond, a s.140 certificate, or a genuine appointment.
- **Residence engineering.** Do not advise incorporating in Ireland while arranging for the company to be tax resident nowhere or in a no-tax country. An Irish-incorporated company is resident here unless a treaty makes it resident elsewhere; reliance on a treaty tie-breaker goes to a specialist.
- **Company formed only to shelter a person's income.** Moving personal service income into a company with no commercial reason, while drawing everything out, does not itself establish either an anti-avoidance assessment or a surcharge. Apply the proven close-service-company conditions; any proposed s.811C conclusion is a **NON-USABLE HOLD**. Check this point with one of our partner accountants.
- **Regulated activity: NON-USABLE HOLD for a licensing conclusion.** Preserve the original signposts: Central Bank (banking, insurance, investment/fund management, payments/e-money, consumer credit, crypto-assets); Revenue/courts (alcohol); food registration; Tusla (childcare); HIQA/HPRA (health, medicines); ComReg; Coimisiún na Meán; Gambling Regulatory Authority; IAA. CRO registration is not a sector-specific permission. Do not use this Guide to determine the licence, capital floor or commencement date. Check this point with one of our partner accountants.
- **Charities.** [Revenue](https://www.revenue.ie/en/companies-and-charities/charities-and-sports-bodies/charitable-tax-exemption/index.aspx) accepts applications for charitable tax exemption from charities registered with the Charities Regulator; CLG incorporation alone grants no exemption. Detailed charity conditions are a **NON-USABLE HOLD**. Check this point with one of our partner accountants.
- **Immigration: NON-USABLE HOLD:** non-EEA founders’ right to live/work, STEP, the former IIP (historical closure date 15 February 2023), Stamp 0/1/4 and employment permits require individual assessment. Check this point with one of our partner accountants.
- **Funds and investment vehicles:** ICAVs, investment limited partnerships, section 110 companies: refer.
- **Transferring an existing business into a company:** capital gains tax, stamp duty, VAT on the transfer and the treatment of goodwill need specialist advice: refer.
- **Data protection: NON-USABLE HOLD for a legal assessment:** GDPR, Data Protection Act 2018, DPO thresholds and any DPC filing require specialist assessment. Check this point with one of our partner accountants.
- **Bank accounts.** Banks apply their own anti-money-laundering checks; no outcome can be promised.

## Filing and payment

**Company, every year**

- Annual return to the CRO within 56 days after its effective date, with the statutory financial statements annexed (except the first return) ([s.343](https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC343), [s.345](https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC345)). The B1 fee is €20; late filing adds €100 plus €3 per day, capped at €1,200 extra per return. Where accounts are required, the deadline is the earlier of ARD + 56 days and financial year-end + nine months + 56 days. For the non-group audit exemption, the 2025 amendment to s.363 removed automatic audit-exemption loss on a single late return: the relevant-year failure plus a previous failure in the preceding five financial years causes loss for the following two financial years; disregard the first return and pre-operative-date failures when applying the previous-failure test. The operative date was 16 July 2025. See [s.363](https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC363) and [CRO deadlines](https://cro.ie/Annual-Return/Missed-Deadlines/).
- Corporation Tax ([Revenue: payment and filing](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax-payment-and-filing/payment-and-filing.aspx)): pay preliminary tax by its due date; file the CT1 and Form 46G (Company) and pay any balance by the 23rd of the ninth month after the end of the accounting period, through ROS. Filing late adds a surcharge of 5% of the tax (up to €12,695) if within two months of the deadline, or 10% (up to €63,485) after that, and restricts some reliefs. Late tax carries interest at 0.0219% a day.
- RBO: file any change to beneficial ownership within 14 days of the date the company's own register had to be updated.
- Payroll: report pay and deductions to Revenue on or before each payday.
- VAT returns: see ie-vat-return.

For preliminary CT, a small company’s prior-period CT does not exceed €200,000 (annualise a short prior period, excluding surcharges and s.239 Income Tax); it can use 100% of the prior CT or 90% of current CT, with the prescribed payment timing. A new company with first-period CT **less than** €200,000 (excluding surcharges but including s.239 tax) need not pay preliminary CT for that first period. Larger-company instalments and exact due dates belong in ie-corporation-tax, not the CT1 filing deadline. [Revenue: preliminary CT](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax-payment-and-filing/preliminary-ct.aspx).

**Sole trader or partner**

- Income Tax return (Form 11) and self-assessment through ROS by 31 October of the following year, with an extended date if filing and paying on ROS ([Revenue: filing your tax return](https://www.revenue.ie/en/self-assessment-and-self-employment/filing-your-tax-return/index.aspx)). Preliminary tax for the current year is paid at the same time.
- A partnership files Form 1 (Firms), completed by the precedent partner; each partner reports their own share in their own return.
- Business name changes to the CRO within one month.

**Dated: 2025 returns (deadlines already passed by 27 November 2026)**

- The Pay and File deadline for the 2025 Form 11 is Saturday 31 October 2026; filing the 2025 Form 11 and paying both the 2025 balance and appropriate 2026 preliminary tax through ROS extended it to Wednesday 18 November 2026 ([Revenue: filing your tax return](https://www.revenue.ie/en/self-assessment-and-self-employment/filing-your-tax-return/index.aspx)). The 2025 bands and credits were the same as 2026 (€44,000 standard rate band; €2,000 credits), but the 2025 USC bands differed: first €12,012 at 0.5%, next €15,370 at 2%, next €42,662 at 3%, balance at 8% ([Revenue: USC rates](https://www.revenue.ie/en/jobs-and-pensions/usc/standard-rates-thresholds.aspx)).
- A company with a 31 December 2025 year end had to file its CT1 and pay the balance by 23 September 2026.

## Completion checklist

- [ ] Founders' residence, PPS numbers and activity recorded; regulated or out-of-scope matters referred.
- [ ] Vehicle chosen, with the reasons and the profit and drawings assumptions written down.
- [ ] Company: type confirmed; at least one director (two for a DAC, CLG or PLC); secretary appointed and not the sole director.
- [ ] Company: EEA-resident director, or s.137 bond, or s.140 certificate in place before filing.
- [ ] Constitution in the right form for the company type; s.22 statement and s.24 declaration ready.
- [ ] Form A1, €50 electronic fee and directors’ PPSN/IPN identity details ready; no paper-incorporation or turnaround promise.
- [ ] Business name registered if trading under another name (within one month).
- [ ] Company's own beneficial ownership register set up; RBO filing diarised within 5 months of incorporation.
- [ ] Revenue registration made by the right route (ROS through an agent, eRegistration, or TR1 / TR2); taxes chosen: Income Tax or Corporation Tax, VAT, employer PAYE (compulsory if directors are paid), RCT.
- [ ] VAT threshold tested on the correct category; non-established rule considered.
- [ ] First annual return date, CT1 date, preliminary tax, payroll and VAT dates in the diary.
- [ ] Companion Skills consulted where needed: ie-corporation-tax and ie-vat-return.


## Original 2025 case and historical topic destinations

### Aoife’s original 2025 comparison: same inputs, corrected arithmetic

The original scenario is retained: Aoife, Irish-resident, age 31 in 2025, single with no children, freelance software developer in Dublin, no employees, home office, €120,000 revenue from Irish/EU SME clients and one US client, €25,000 expenses, €95,000 profit. Business name: **Aoife Dev Studio**. This is a 2025 case, not a substituted 2026 estimate.

- Sole trader: Income Tax €25,200; USC €12,012 × 0.5% + €15,370 × 2% + €42,662 × 3% + €24,956 × 8% = **€3,643.80**. Annual self-assessed Class S €95,000 × 4.125% = **€3,918.75**. Total **€32,762.55**, or **34.4869%** of profit, assuming those are the only taxable/USC/PRSI amounts. The old approximate €35,000 total and USC estimate are withdrawn. No 3% USC excess-income surcharge arises at €95,000.
- Company: **Aoife Dev Studio Limited**, €100 issued as €1 shares, Aoife owns 100%, is sole director, and a separate secretary is her spouse or a corporate secretary service (the 2026 case instead uses her brother). Salary €60,000; business profit after salary €35,000; CT **€4,375**, retained after CT **€30,625**. Salary Income Tax **€11,200** uses the Earned Income Credit, not Employee Credit; 2025 USC **€1,346.00**. She is not automatically Class A. Actual Class S payroll depends on payment dates; **only if paid evenly over the year**, €60,000 × 4.125% = €2,475, giving personal tax/USC/PRSI **€15,021.00**, and combined with CT **€19,396.00** before surcharge or later distributions. This is a timing comparison, not a final lifetime tax saving.
- If all €30,625 is undistributed income within the service-company surcharge rules, 15% × one-half × €30,625 = **€2,296.88**; confirm the statutory distributable-income base, distributions within 18 months and adjustments before using that illustrative amount. Estate/investment income uses the separate 20% rule, not 15% of half.
- VAT: confirm the Irish/EU/US sales split, each customer’s business status and service classification. General-rule B2B services are supplied where the customer belongs; EU invoices/VIES and overseas evidence remain necessary. The original “23% on all Irish/EU consumer sales” cannot be used for every service, especially electronic services. SaaS/OSS requires its own place-of-supply analysis.

### Recomputed original 2025 check

```oa-check
name: Original 2025 software-developer inputs
inputs:
  revenue: 120000
  expenses: 25000
  salary: 60000
steps:
  profit: revenue - expenses
  income_tax: 44000 * 0.20 + (profit - 44000) * 0.40 - 4000
  usc: 12012 * 0.005 + 15370 * 0.02 + 42662 * 0.03 + (profit - 70044) * 0.08
  prsi: profit * 0.04125
  sole_total: income_tax + usc + prsi
  salary_usc: 12012 * 0.005 + 15370 * 0.02 + (salary - 27382) * 0.03
  corporation_tax: (profit - salary) * 0.125
expected:
  profit: 95000
  income_tax: 25200.00
  usc: 3643.80
  prsi: 3918.75
  sole_total: 32762.55
  salary_usc: 1346.00
  corporation_tax: 4375.00
```

### Historical specialist figures and decisions: non-usable holds

These destinations preserve the older research without treating it as 2026 authority. Every row marked **NON-USABLE HOLD** requires the same action: **Check this point with one of our partner accountants.** Routine company formation and the rate/filing matrix above are not held.

| Original topic / inputs preserved | Current destination and permitted use |
| --- | --- |
| Turnarounds: LTD 5–10 working days; business name 1–2 days; PLC 3–6 weeks; CLG 4–8 weeks; DAC 2–4 weeks | **NON-USABLE HOLD** as service promises. Use the current CRO queue; acceptance dates vary. |
| Formation budget €400–€800 professional fees, €500–€900 all-in; annual LTD €1,500–€3,000 versus sole trader €500–€1,000; 5–10 year horizon, €70,000 comparison heuristic and micro turnover below €40,000 | **NON-USABLE HOLD** as a recommendation or quoted market price. Keep these original planning assumptions; obtain actual fees and drawings. No statutory entity-selection threshold follows from them. |
| Historic €100 paper A1 / €50 electronic; €100 issued LTD capital / €1 shares; nominal CLG guarantee €1; PLC €25,000 / quarter €6,250 | Current A1 electronic €50; no paper route in current fee schedule. LTD €100 is the case’s chosen capital, not a statutory floor. CLG/PLC structure and capital conditions are in the formation matrix; specialist drafting governs guarantee terms. |
| Start-up s.486C relief: old three years, €40,000 / €60,000 limits; R&D 30%, three instalments, €75,000 first instalment; KDB 6.25%, 1 January 2027 sunset | **NON-USABLE HOLD** for those historical figures and eligibility. Retained destination: ie-corporation-tax; this Guide does not establish a current relief or entitlement. |
| Pillar Two 15%, €750 million groups; gains 33%; Entrepreneur Relief 10% / €1 million; Retirement Relief age 55+; capital allowances 12.5% / eight years or 4% / 25 years | **NON-USABLE HOLD** for those original rate/limit/condition claims. Use ie-corporation-tax or individual disposal advice; they do not establish that an LTD is better for this founder. |
| VAT rates 23%, 13.5%, 9%, 4.8%, 0%; MOSS/OSS/IOSS; Intrastat arrivals €500,000 / dispatches €635,000 (2025); employer PRSI 11.15% / 11.25% (2025) | **NON-USABLE HOLD** as rates, statistical thresholds or an automatic registration instruction. Retained destinations: ie-vat-return and payroll/Intrastat assessment. Domestic VAT-registration thresholds and both dated cases are proved above. |
| Historic one-member CLG audit ban; blanket LP/ILP/LLP annual-return/audit rules; separate ILP/LLP personality or elective tax treatment | **NON-USABLE HOLD**; do not apply those assertions. Core legal-person/liability distinctions, Companies Act partnership limits and current late-return audit rule replace the misleading generalisations. Assess actual audit eligibility by entity, size/group status and members’ rights. |
| Stamp duty on issue/transfer of shares: old 1% transfer rate and purported abolition order; existing-business CGT, goodwill, stamp duty and VAT transfer treatment | **NON-USABLE HOLD** for transaction-specific liability or relief. Incorporation is not evidence of a tax-free transfer. |
| Single-parent €53,000 / married €88,000 bands (2025); historical PRSI 4.1% / 4.2%; old USC €13,748 band or about €6,000 / salary about €2,200 | **NON-USABLE HOLD** for the family bands without assessment facts. Ordinary single-person bands and the complete 2025/2026 USC and PRSI calculations above replace the inaccurate estimates; family assessment is separate. |
| PLC prospectus/listing: EU 2017/1129, SI 380/2019 and SI 277/2007; MiCA 30 December 2024 transition; CCPC €60 million worldwide / €10 million each Irish turnover merger test; charity/OMC/fund formation; immigration and data protection | **NON-USABLE HOLD** for a licence, notification, listing or legal conclusion. Preserve each specialist destination and refer; a CRO certificate does not decide these issues. |
| Restricted company-name words including Bank, Insurance, Society, University, Group and Holding; historical suffix translations; shareholder PPSN assertion; banks’ in-person/notarial requirements or named fintech comparisons | **NON-USABLE HOLD** for blanket restrictions or guarantees. Apply actual CRO name acceptance and directors’/beneficial owners’ identity process; do not demand every shareholder’s PPSN solely for incorporation. Obtain the relevant bank’s requirements. |

## Sources

Additional official reads on 27 November 2026: [CRO incorporation](https://cro.ie/information-leaflets/company-incorporation-leaflet-1/), [business-name forms/fees](https://cro.ie/publications/business-names-forms-fees/), [identity](https://cro.ie/registration/beneficial-ownership/rbo-no-ppsn/), [announcements](https://cro.ie/about-cro/whats-new/), [RBO FAQs](https://rbo.gov.ie/faqs/), [bond order](https://www.irishstatutebook.ie/eli/2015/si/215/made/en/print), [fees regulations](https://www.irishstatutebook.ie/eli/2025/si/329/made/en/print), [Partnership Act 1890](https://www.irishstatutebook.ie/eli/1890/act/39/enacted/en/print), [Limited Partnerships Act 1907](https://www.irishstatutebook.ie/eli/1907/act/24/enacted/en/print), [current VAT Act](https://revisedacts.lawreform.ie/eli/2010/act/31/revised/en/html), [RCT](https://www.revenue.ie/en/self-assessment-and-self-employment/rct/index.aspx), and the DSP contribution guide linked above. Tax bands, credits, USC, annual PRSI and dated Form 11 deadlines reuse matching 2025/2026 primary-source reads completed on 27 November 2026.

| Source | URL | Read on |
| --- | --- | --- |
| Registration of Business Names Act 1963 | https://www.irishstatutebook.ie/eli/1963/act/30/enacted/en/print | 2026-11-27 |
| beneficial ownership regulations (S.I. No. 110 of 2019) | https://www.irishstatutebook.ie/eli/2019/si/110/made/en/print | 2026-11-27 |
| revenue.ie | https://www.revenue.ie/en/starting-a-business/index.aspx | 2026-11-27 |
| Revenue: basis of charge | https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax/basis-of-charge.aspx | 2026-11-27 |
| s.17 | https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC17 | 2026-11-27 |
| s.38 | https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC38 | 2026-11-27 |
| s.128 | https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC128 | 2026-11-27 |
| s.985 | https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC985 | 2026-11-27 |
| s.1194 | https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC1194 | 2026-11-27 |
| s.1088 | https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC1088 | 2026-11-27 |
| s.129 | https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC129 | 2026-11-27 |
| s.1112 | https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC1112 | 2026-11-27 |
| s.19 | https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC19 | 2026-11-27 |
| s.21 | https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC21 | 2026-11-27 |
| s.24 | https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC24 | 2026-11-27 |
| s.175 | https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC175 | 2026-11-27 |
| s.1000 | https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC1000 | 2026-11-27 |
| s.1026 | https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC1026 | 2026-11-27 |
| s.137 | https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC137 | 2026-11-27 |
| s.140 | https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC140 | 2026-11-27 |
| Revenue: registering for tax | https://www.revenue.ie/en/starting-a-business/registering-for-tax/index.aspx | 2026-11-27 |
| Revenue | https://www.revenue.ie/en/starting-a-business/registering-for-tax/how-to-register-for-tax-as-a-sole-trader.aspx | 2026-11-27 |
| Revenue | https://www.revenue.ie/en/starting-a-business/registering-for-tax/how-to-register-for-tax-as-a-trust-or-partnership.aspx | 2026-11-27 |
| Revenue | https://www.revenue.ie/en/starting-a-business/registering-for-tax/how-to-register-for-tax-as-a-new-company.aspx | 2026-11-27 |
| Revenue: eRegistration | https://www.revenue.ie/en/starting-a-business/registering-for-tax/eregistration.aspx | 2026-11-27 |
| Revenue: registration of employers | https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/registration-of-employers-for-paye-purposes/index.aspx | 2026-11-27 |
| Revenue: company residency rules | https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax/company-residency-rules.aspx | 2026-11-27 |
| Revenue: tax rates, bands and reliefs | https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/tax-relief-charts/index.aspx | 2026-11-27 |
| Revenue: Earned Income Credit | https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/income-and-employment/earned-income-credit/index.aspx | 2026-11-27 |
| Revenue: USC rates | https://www.revenue.ie/en/jobs-and-pensions/usc/standard-rates-thresholds.aspx | 2026-11-27 |
| Revenue: other rates of USC | https://www.revenue.ie/en/jobs-and-pensions/usc/other-rates.aspx | 2026-11-27 |
| Revenue: VAT thresholds | https://www.revenue.ie/en/vat/vat-registration/who-should-register-for-vat/persons-required-register-goods-services-abroad.aspx | 2026-11-27 |
| Revenue: electing to register for VAT (read for the EUR 10,000 distance sales and EUR 41,000 EU acquisitions thresholds) | https://www.revenue.ie/en/vat/vat-registration/who-should-register-for-vat/elect-register-vat.aspx | 2026-11-27 |
| Revenue: surcharge on undistributed income | https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/close-companies/surcharge.aspx | 2026-11-27 |
| s.345 | https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC345 | 2026-11-27 |
| s.343 | https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC343 | 2026-11-27 |
| s.349 | https://revisedacts.lawreform.ie/eli/2014/act/38/revised/en/html#SEC349 | 2026-11-27 |
| Revenue: payment and filing | https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax-payment-and-filing/payment-and-filing.aspx | 2026-11-27 |
| Revenue: filing your tax return | https://www.revenue.ie/en/self-assessment-and-self-employment/filing-your-tax-return/index.aspx | 2026-11-27 |

Not yet confirmed: the specialized outcomes explicitly labelled NON-USABLE HOLD in the historical topic table and referral section. They are not filing instructions. Check this point with one of our partner accountants. Routine formation, Revenue registration, rates and original examples remain usable subject to their stated facts.
