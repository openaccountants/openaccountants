---
name: ie-formation
description: "Use this skill whenever asked about forming, incorporating, or registering a business in Ireland. Trigger on phrases like \"Ireland company formation\", \"CRO registration\", \"LTD Ireland\", \"DAC Ireland\", \"sole trader Ireland\", \"Form A1 Ireland\", \"PPS number business\", \"incorporate Ireland\", \"CORE portal\", \"register business Ireland\", \"RBO Ireland\", \"TR1 Ireland\", \"TR2 Ireland\", \"Companies Act 2014\", \"CLG Ireland\", \"PLC Ireland\", or any question about choosing or registering an Irish entity. Covers entity comparison (Sole Trader, Partnership, LP, LLP, LTD / CLS, DAC, CLG, PLC), CRO online portal (CORE) registration steps, Revenue TR1 / TR2 tax registration, sector-specific licensing (Central Bank, CCPC, DPC), RBO beneficial ownership filing, PPS number requirements for directors and shareholders, and tax treatment by entity type including the 12.5% trading CT rate and PRSI Class S. Out of scope: immigration / employment permits for non-EEA founders, bank account opening procedures (high-level only), full corporate governance and shareholders' agreement drafting, deep sector-specific regulatory licensing beyond signposting, listing on Euronext Dublin / ISEQ, and Irish Collective Asset-management Vehicles (ICAV). ALWAYS read this skill before advising on Irish entity formation."
jurisdiction: IE
tax_year: 2026
last_updated: 2026-09-27
authored_by: OpenAccountants team
review_status: pending_review
trust_label: Written by the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Forming a business in Ireland (2026): sole trader, partnership or company, CRO, RBO and Revenue registration

## Scope

This Guide is for someone starting a business in the Republic of Ireland, or an adviser helping them. It covers choosing the vehicle (sole trader, partnership, limited partnership, LTD, DAC, CLG, PLC, unlimited company), forming a company under the Companies Act 2014, directors and secretary, the EEA-resident director rule, the constitution, beneficial ownership (RBO) filing, registering with Revenue (Form TR1 / TR2, eRegistration on ROS), and the first compliance dates.

Figures are for tax year 2026 (calendar year 2026 for income tax, USC and VAT thresholds; accounting periods in 2026 for Corporation Tax). A short dated section near the end covers returns being filed now for 2025.

What this Guide does not cover, with where to go instead:

- VAT returns, rates and reverse charge: the Guide **ireland-vat-return**.
- Corporation Tax computations, preliminary tax, close-company surcharges in detail, start-up relief (s.486C), R&D credit, Knowledge Development Box, Pillar Two: the Guide **ie-corporation-tax**.
- PRSI rates (they change each October), payroll operation, benefit in kind.
- Immigration permissions for non-EEA founders, bank account opening, shareholders' agreements, funds (ICAV, ILP), listing on Euronext Dublin, and sector licensing beyond signposting.

**Sources.** The law is the Companies Act 2014 (section links below), the Taxes Consolidation Act 1997, the VAT Consolidation Act 2010, the [Registration of Business Names Act 1963](https://www.irishstatutebook.ie/eli/1963/act/30/enacted/en/print) and the [beneficial ownership regulations (S.I. No. 110 of 2019)](https://www.irishstatutebook.ie/eli/2019/si/110/made/en/print). Statute links are to the enacted text on the Irish Statute Book; later amendments must be checked in the Law Reform Commission's Revised Acts. Revenue's guidance is on [revenue.ie](https://www.revenue.ie/en/starting-a-business/index.aspx).

**What to check on the CRO and RBO sites.** The Companies Registration Office (CRO, portal "CORE") and the RBO portal are not sources this Guide could verify. CRO and RBO filing fees, processing times, the CORE screens, name-approval practice, and the identity rules for directors without a PPS number (the PPSN / VIN process) are marked **check**: confirm them on the CRO and RBO websites before quoting them to a client.

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

1. **Check whether the plan is one this Guide can handle.** Regulated activity, a charity, a fund, or a founder who needs an immigration permission all need a specialist in addition (see "When to refuse or refer").
2. **Choose the vehicle.** Use the decision rules below. For most owner-managed businesses the choice is sole trader or LTD; the deciding facts are liability risk, how much profit will be left in the business, and whether investors are coming.
3. **If a sole trader or partnership:** register a business name with the CRO within one month of adopting any name other than the owner's true name(s), then register with Revenue (TR1 or eRegistration) for Income Tax, and for VAT, employer PAYE and RCT if they apply.
4. **If a company:** pick the company type; confirm at least one EEA-resident director or arrange a section 137 bond or a section 140 certificate; appoint a secretary (not the sole director); draft the constitution; file the incorporation with the CRO (Form A1 on CORE; fees and screens: **check**).
5. **After incorporation:** keep the company's own beneficial ownership register and file with the RBO within 5 months; register with Revenue (TR2 or ROS through an agent) for Corporation Tax and, as needed, VAT, employer PAYE (compulsory if the directors are paid) and RCT.
6. **Diary the first compliance dates:** first annual return to the CRO; first Corporation Tax return and preliminary tax (see ie-corporation-tax); VAT returns (see ireland-vat-return); Form 11 for self-employed individuals and proprietary directors.
7. **Record the reasons.** Write down why the vehicle was chosen and the facts it depends on (profit level, drawings, risk), so the choice can be revisited when they change.

## Choosing the vehicle

| Vehicle | Separate legal person? | Owner's liability | Tax on profits | Main uses |
| --- | --- | --- | --- | --- |
| Sole trader | No | Unlimited | Income tax, USC and PRSI on profits, via Form 11 | One owner, low risk, profits mostly drawn |
| Partnership (Partnership Act 1890) | No | Unlimited, joint and several | Each partner taxed on their share; the partnership registers on TR1 | Two or more people in business together, professional firms |
| Limited partnership (Limited Partnerships Act 1907) | No | General partner unlimited; limited partners up to their contribution | As a partnership | Mostly investment structures (refer) |
| LTD: private company limited by shares (Part 2, Companies Act 2014) | Yes | Limited to unpaid share capital | Corporation Tax; owners taxed when paid salary or dividends | The default company for owner-managed businesses |
| DAC: designated activity company (Part 16) | Yes | Limited (by shares, or by guarantee with a share capital) | Corporation Tax | Where an objects clause is needed: joint ventures, special purpose vehicles, some regulated firms |
| CLG: company limited by guarantee (Part 18) | Yes | Limited to the guarantee | Corporation Tax unless an exemption (such as charitable status) applies | Non-profits, clubs, charities, owners' management companies |
| PLC: public limited company (Part 17) | Yes | Limited to unpaid share capital | Corporation Tax | Offering shares to the public, listing |
| Unlimited company (Part 20) | Yes | Unlimited | Corporation Tax | Specialist uses (refer) |

### Decision rules

- **Non-profit, club, charity or owners' management company:** CLG. Charitable tax exemption is a separate application (Charities Regulator, then Revenue); forming a CLG does not give it.
- **Shares to be offered to the public, or a listing planned:** PLC.
- **An objects clause is required** (by a regulator, a lender, or the joint-venture parties): DAC.
- **One owner, low risk, profit mostly drawn for living costs, or testing an idea:** sole trader.
- **Two or more professionals who want to share profits informally and accept unlimited liability:** partnership. Solicitors can use a limited liability partnership under the Legal Services Regulation Act 2015 (refer).
- **Otherwise** (limited liability wanted, profit to be kept in the business, investors expected, or trading income large enough that the 12.5% company rate on trading income ([Revenue: basis of charge](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax/basis-of-charge.aspx)) beats personal marginal rates on retained profit): LTD.

### LTD: the rules that matter at formation (Companies Act 2014, Part 2)

- **Members.** One or more; the number of members may not exceed 149, not counting current and former employees who are members, and joint holders count as one ([s.17](https://www.irishstatutebook.ie/eli/2014/act/38/section/17/enacted/en/html)).
- **Capacity.** An LTD has full and unlimited capacity to carry on any business or activity, whatever its constitution says ([s.38](https://www.irishstatutebook.ie/eli/2014/act/38/section/38/enacted/en/html)). It has no objects clause; if the founders need one, use a DAC.
- **Directors.** At least one ([s.128](https://www.irishstatutebook.ie/eli/2014/act/38/section/128/enacted/en/html)). DACs, CLGs and PLCs need at least two ([s.985](https://www.irishstatutebook.ie/eli/2014/act/38/section/985/enacted/en/html), [s.1194](https://www.irishstatutebook.ie/eli/2014/act/38/section/1194/enacted/en/html), [s.1088](https://www.irishstatutebook.ie/eli/2014/act/38/section/1088/enacted/en/html)).
- **Secretary.** Every company must have a secretary, who may be one of the directors, but where a company has only one director that person may not also be the secretary. The directors must make sure the secretary has the skills or resources to do the job ([s.129](https://www.irishstatutebook.ie/eli/2014/act/38/section/129/enacted/en/html)). A PLC secretary must also meet one of the qualification conditions in [s.1112](https://www.irishstatutebook.ie/eli/2014/act/38/section/1112/enacted/en/html).
- **Constitution.** One document in the form in Schedule 1 (or as near to it as possible), stating the name, that it is a private company limited by shares, that members' liability is limited, and the share capital. It may state an authorised share capital or simply state that the shares are divided into shares of a fixed amount; each subscriber takes at least one share ([s.19](https://www.irishstatutebook.ie/eli/2014/act/38/section/19/enacted/en/html)).
- **Registration documents.** The constitution goes to the Registrar with the statement of first directors, secretary and registered office (s.22), and a declaration (s.24) that the registration requirements are met and that the company is being formed to carry on an activity in the State ([s.21](https://www.irishstatutebook.ie/eli/2014/act/38/section/21/enacted/en/html), [s.24](https://www.irishstatutebook.ie/eli/2014/act/38/section/24/enacted/en/html)). The declaration may be made by a director, the secretary or the solicitor forming the company.
- **AGM.** A company need not hold an AGM in a year if all members entitled to attend and vote sign a written resolution before the latest date for the meeting that acknowledges receipt of the financial statements, resolves everything the AGM would have resolved, and confirms no change of auditor ([s.175](https://www.irishstatutebook.ie/eli/2014/act/38/section/175/enacted/en/html)). A PLC with two or more members cannot use this.

### PLC capital ([s.1000](https://www.irishstatutebook.ie/eli/2014/act/38/section/1000/enacted/en/html), [s.1026](https://www.irishstatutebook.ie/eli/2014/act/38/section/1026/enacted/en/html))

- The authorised minimum share capital of a PLC is €25,000 (unless increased by ministerial order).
- A PLC may not allot a share unless it is paid up at least as to one-quarter of its nominal value and the whole of any premium.

### The EEA-resident director rule ([s.137](https://www.irishstatutebook.ie/eli/2014/act/38/section/137/enacted/en/html), [s.140](https://www.irishstatutebook.ie/eli/2014/act/38/section/140/enacted/en/html))

At least one director must be resident in an EEA state (the EU plus Iceland, Liechtenstein and Norway; the UK is not in the EEA). Alternate directors do not count. There are two ways out:

- **A bond.** The company holds a bond in the prescribed form, in force, to the value of €25,000, which pays fines under the Companies Act and certain tax penalties if the company fails to pay them. The bond's term and providers: **check** with the CRO.
- **A section 140 certificate.** The Registrar grants a certificate that the company has a real and continuous link with an economic activity carried on in the State. A written statement from Revenue, given within the 2 months before the application, that it has reasonable grounds to believe the link exists, is treated as proof. The link exists if the company is managed from a place of business in the State by people it authorises, carries on a trade in the State, or is in a group with a company that meets either test.

Breaking the rule is a category 4 offence for the company and every officer in default.

### Business names ([Registration of Business Names Act 1963](https://www.irishstatutebook.ie/eli/1963/act/30/enacted/en/print))

- An individual, partnership or company carrying on business under a name other than its true name (for a company, its corporate name) must register the business name with the CRO. For companies the Companies Act repeats this for each company type.
- The particulars must be furnished within one month after the business name is adopted (s.6), and any change within one month after the change (s.7).
- The certificate of registration must be displayed at the principal place of business (s.8), and the true names must appear on business letters and similar documents (s.18).
- Forms and fees: RBN1 (individual), RBN1A (partnership), RBN1B (company). Fees and processing time: **check** with the CRO.

### Beneficial ownership: the RBO ([S.I. No. 110 of 2019](https://www.irishstatutebook.ie/eli/2019/si/110/made/en/print))

- **Who:** every company and other body corporate incorporated in the State (a "relevant entity"), including LTDs, DACs, CLGs, PLCs, unlimited companies and registered societies. The regulations do not apply to a company listed on a regulated market subject to EU-consistent disclosure requirements, or subject to equivalent international standards (reg. 4(2)).
- **Own register:** the company must keep its own beneficial ownership register (reg. 15). "Beneficial owner" takes its meaning from Article 3(6)(a) of the Fourth Anti-Money Laundering Directive: the natural persons who ultimately own or control the entity (the ownership-percentage indicator is in the Directive: **check**). If no one is identified, or there is doubt, the company enters its senior managing officials (the directors and any chief executive) instead, stating the nature and extent of their control.
- **Central register:** a company formed now must deliver the information to the Registrar of Beneficial Ownership within 5 months from its incorporation (reg. 20(2)). After that, whenever the company must enter, change or delete information in its own register, it must file the matching change with the RBO within 14 days from the date the entry in its own register was due (reg. 23).
- **Penalties:** failing to keep the register or to file is an offence: on summary conviction a class A fine, on indictment a fine of up to €500,000 (regs. 15 and 28).
- **Public access:** access to the central register was restricted after the Court of Justice judgment of 22 November 2022 and later amending regulations. **check** the current access rules on the RBO site.
- **Filing mechanics** (online portal, PPS numbers for beneficial owners, who presents the filing): **check** on the RBO site.

### Registering with Revenue ([Revenue: registering for tax](https://www.revenue.ie/en/starting-a-business/registering-for-tax/index.aspx))

A Tax Reference Number is not issued automatically on incorporation. You must register with Revenue when you become a sole trader, set up a partnership or trust, or start a new company.

| Who | How | Taxes the form covers |
| --- | --- | --- |
| Sole trader ([Revenue](https://www.revenue.ie/en/starting-a-business/registering-for-tax/how-to-register-for-tax-as-a-sole-trader.aspx)) | Needs a PPSN first; the PPSN becomes the TRN once registered. Register on ROS (eRegistration) or, if a PAYE employee, for Income Tax on myAccount. Non-residents who cannot register online use Form TR1 (FT) | Income Tax, employer PAYE, VAT, RCT (and CGT on TR1 (FT)) |
| Partnership or trust ([Revenue](https://www.revenue.ie/en/starting-a-business/registering-for-tax/how-to-register-for-tax-as-a-trust-or-partnership.aspx)) | Tax agent registers online through ROS; otherwise Form TR1 (non-resident: TR1 (FT)) | Income Tax, employer PAYE, VAT, RCT |
| New company ([Revenue](https://www.revenue.ie/en/starting-a-business/registering-for-tax/how-to-register-for-tax-as-a-new-company.aspx)) | Needs a CRO number first. A tax agent must register it online through ROS; a company without an agent submits Form TR2 (foreign company: TR2 (FT)) | Corporation Tax, employer PAYE, VAT, RCT |

- **Paper when online was required:** Revenue returns a paper application that should have been made online, unprocessed.
- **Not eligible for eRegistration** ([Revenue: eRegistration](https://www.revenue.ie/en/starting-a-business/registering-for-tax/eregistration.aspx)) include companies that have no Irish-resident directors and unincorporated bodies and non-profits not represented by an agent. They use the paper TR forms.
- **After registration:** companies, sole traders and partnerships must file returns and pay through ROS.
- **Employer PAYE** ([Revenue: registration of employers](https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/registration-of-employers-for-paye-purposes/index.aspx)): register before paying any employee, and report pay and deductions on or before each payday. A company must register as an employer and operate PAYE on its directors' pay even if it has no other employees; a director of an Irish-incorporated company pays PAYE on director's pay wherever resident.
- **VAT:** see the thresholds below and the Guide ireland-vat-return.
- **RCT:** register if the business is a principal contractor in construction, forestry or meat processing (see Revenue's RCT pages).
- **Tax residence of the company** ([Revenue: company residency rules](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax/company-residency-rules.aspx)): a company incorporated in Ireland on or after 1 January 2015 is tax resident here unless a tax treaty makes it resident in another country. A foreign-incorporated company is resident here if centrally managed and controlled here.

## Figures for 2026

### Corporation Tax rates ([Revenue: basis of charge](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax/basis-of-charge.aspx))

| Item | 2026 | Condition |
| --- | --- | --- |
| Trading income | 12.5% | Profits of a trade carried on by the company |
| Non-trading income and excepted trades | 25% | Rental and investment income; income of an "excepted trade" as defined in the Taxes Consolidation Act |
| Accounting period | at most 12 months | A longer set of accounts is split into two CT periods |

### Income tax bands and credits for 2026 ([Revenue: tax rates, bands and reliefs](https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/tax-relief-charts/index.aspx))

| Item | 2026 | 2025 |
| --- | --- | --- |
| Standard rate band, single person without qualifying children | €44,000 @ 20%, balance @ 40% | €44,000 @ 20%, balance @ 40% |
| Single Person tax credit | €2,000 | €2,000 |
| Employee (PAYE) tax credit | €2,000 | €2,000 |
| Earned Income Tax Credit (maximum) | €2,000 | €2,000 |

The Earned Income Credit is for self-employed earned income and for pay earned by proprietary directors, who cannot get the Employee Tax Credit on that pay. It is the lower of €2,000 or 20% of qualifying earned income, and where someone has both kinds of income the two credits together cannot exceed the Employee Tax Credit maximum ([Revenue: Earned Income Credit](https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/income-and-employment/earned-income-credit/index.aspx)).

### Universal Social Charge for 2026 ([Revenue: USC rates](https://www.revenue.ie/en/jobs-and-pensions/usc/standard-rates-thresholds.aspx))

| Band | 2026 rate |
| --- | --- |
| First €12,012 | 0.5% |
| Next €16,688 | 2% |
| Next €41,344 | 3% |
| Balance | 8% |

A USC surcharge of 3% applies if non-PAYE income is more than €100,000 a year, so self-employed income above that level bears 11% ([Revenue: other rates of USC](https://www.revenue.ie/en/jobs-and-pensions/usc/other-rates.aspx)). Reduced USC rates for some people are not covered here.

PRSI: self-employed people pay Class S PRSI and most employees Class A; the class for a director who owns the company depends on the shareholding (**check** with the Department of Social Protection). Rates have been rising each October; take the rate in force (**check**).

### VAT registration thresholds ([Revenue: VAT thresholds](https://www.revenue.ie/en/vat/vat-registration/who-should-register-for-vat/vat-thresholds.aspx))

Registration is obligatory when annual turnover (calendar year, excluding VAT) exceeds the threshold. Below the threshold a business may elect to register.

| Supplies | Threshold |
| --- | --- |
| Services only | €42,500 |
| Goods at the reduced or standard rate that the business made from zero-rated materials | €42,500 |
| Goods and services, where 90% or more of turnover is from goods (other than the above) | €85,000 |
| Goods | €85,000 |
| Distance sales of goods and cross-border telecoms, broadcasting and electronic services to other EU consumers (EU-wide total; supplier established only in Ireland) | €10,000 |
| Acquisitions of goods from other EU Member States | €41,000 |

A business not established in Ireland that supplies taxable goods or services to taxable customers in Ireland must register whatever its turnover, unless it uses the VAT SME Scheme. Occasional disposals of business assets are left out of annual turnover. Details and returns: ireland-vat-return.

### Company law figures (Companies Act 2014)

| Rule | Figure | Section |
| --- | --- | --- |
| Bond instead of an EEA-resident director | €25,000 | [s.137](https://www.irishstatutebook.ie/eli/2014/act/38/section/137/enacted/en/html) |
| PLC authorised minimum share capital | €25,000 | [s.1000](https://www.irishstatutebook.ie/eli/2014/act/38/section/1000/enacted/en/html) |
| PLC shares paid up at allotment | at least one-quarter of nominal value plus all premium | [s.1026](https://www.irishstatutebook.ie/eli/2014/act/38/section/1026/enacted/en/html) |
| RBO fine on indictment | up to €500,000 | [S.I. No. 110 of 2019, reg. 28](https://www.irishstatutebook.ie/eli/2019/si/110/made/en/print) |
| CRO incorporation, business name and late annual return fees | **check** on the CRO site | CRO fee regulations |

## Boundaries and exceptions

| Situation | Rule | What to do |
| --- | --- | --- |
| Sole director wants to be secretary too | Not allowed where the company has only one director (s.129(6)) | Appoint a second person as secretary, or a second director who can also be secretary |
| No director lives in the EEA | [s.137](https://www.irishstatutebook.ie/eli/2014/act/38/section/137/enacted/en/html) applies unless a bond or a s.140 certificate is in force | Bond (€25,000), a s.140 certificate backed by a Revenue statement, or appoint a genuine EEA-resident director. Never a nominee with no real role |
| UK-resident director only | The UK is not an EEA state | Same as above |
| Wants an objects clause | An LTD has unlimited capacity (s.38) | Form a DAC |
| DAC, CLG or PLC with one director | At least two directors required | Appoint a second director |
| More than 149 members in an LTD or DAC | Registration above the limit is void (s.17(7)) | Leave out employee members when counting; otherwise a PLC or other form |
| Trading under a name other than the true name | Business name must be registered within one month of adopting it | File RBN1 / RBN1A / RBN1B with the CRO |
| Company with no Irish-resident directors | Cannot use eRegistration unless through an agent | Agent registers on ROS, or paper TR2 / TR2 (FT) |
| Company pays only its directors | Must still register as an employer and operate PAYE | Register before the first payment |
| Turnover exactly at a VAT threshold | Obligation arises only when turnover exceeds the threshold | Monitor the calendar-year total; may elect to register earlier |
| Non-established business selling to Irish taxable customers | No threshold | Register for VAT from the first supply, unless in the VAT SME Scheme |
| CLG wanting charity tax exemption | Incorporation does not give charitable status | Register with the Charities Regulator, then apply to Revenue |
| Incorporated in Ireland but run from abroad | Resident here from incorporation (on or after 1 January 2015) unless a treaty says otherwise | Do not structure around residence; refer if a treaty tie-breaker is relied on |
| Company formed with no activity in the State | The s.24 declaration must state that a purpose is carrying on an activity in the State | Refer |

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

Class S PRSI is due on top at the rate in force (**check**). VAT: her services turnover will exceed €42,500, so she must register for VAT ([Revenue: VAT thresholds](https://www.revenue.ie/en/vat/vat-registration/who-should-register-for-vat/vat-thresholds.aspx)). Registration: eRegistration on ROS for Income Tax and VAT; a business name only if she trades under a name other than her own.

### Case 2: Aoife through an LTD, 2026 ([Revenue: basis of charge](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax/basis-of-charge.aspx))

Same business through Aoife Dev Studio Limited. Aoife is the sole director and sole shareholder; her brother is the secretary (s.129(6)). She is EEA resident, so no bond is needed. The company pays her a salary of €60,000 and has profit after the salary of €35,000 (€120,000 less €25,000 less €60,000), all trading income.

- Corporation Tax at 12.5% ([Revenue: basis of charge](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax/basis-of-charge.aspx)): €35,000 x 12.5% = **€4,375**, leaving €30,625 after tax in the company.
- Income tax on the salary: €44,000 at 20% = €8,800 plus €16,000 at 40% = €6,400, so €15,200; less Single Person credit €2,000 and, as a proprietary director, the Earned Income Credit €2,000 (not the Employee Tax Credit) ([Revenue: Earned Income Credit](https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/income-and-employment/earned-income-credit/index.aspx)) = **€11,200**.
- USC on the salary ([Revenue: USC rates](https://www.revenue.ie/en/jobs-and-pensions/usc/standard-rates-thresholds.aspx)): €60.06 + €333.76 + (€60,000 less €28,700 = €31,300 at 3% = €939) = **€1,332.82**.
- PRSI on the salary: **check** her class and the rate in force.
- The company must register for Corporation Tax, VAT and as an employer (PAYE on her salary is compulsory even with no other staff), file with the RBO within 5 months, and file its first annual return.
- **Close service company surcharge.** A close company whose main income comes from a profession, such as a computer programmer, pays a surcharge of 15% on one half of its undistributed trading income if the income is not distributed within 18 months of the end of the accounting period ([Revenue: surcharge on undistributed income](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/close-companies/surcharge.aspx)). Leaving the €30,625 in the company is not free; compute the exposure with ie-corporation-tax.

Comparing the two: the company route defers tax on the profit left in the company, but that profit is taxed again when paid out, the surcharge can apply, and running a company costs more (accounts, annual return, payroll). If Aoife needs to draw nearly all the profit, the saving is small or negative. Record the assumption.

### Case 3: two founders in the United States

Two US-resident founders want an Irish LTD to sell software into the EU. Neither is EEA resident, so s.137 bites. Options: a €25,000 bond in the prescribed form ([s.137](https://www.irishstatutebook.ie/eli/2014/act/38/section/137/enacted/en/html)); a s.140 certificate if the company will be managed from a place of business in Ireland or carry on a trade here, supported by a Revenue statement dated within 2 months of the application; or a genuine EEA-resident director. As the company has no Irish-resident directors it cannot use eRegistration itself; an agent registers it on ROS or it files a paper TR2 ([Revenue: eRegistration](https://www.revenue.ie/en/starting-a-business/registering-for-tax/eregistration.aspx)). The directors' Irish pay is subject to PAYE. Their immigration position and US tax treatment are out of scope: refer. Identity requirements for directors without a PPS number: **check** with the CRO.

### Case 4: key dates for a company incorporated on 10 March 2026

- RBO filing: within 5 months from incorporation, so by 10 August 2026 ([S.I. No. 110 of 2019, reg. 20(2)](https://www.irishstatutebook.ie/eli/2019/si/110/made/en/print)).
- First annual return date: 6 months after incorporation, 10 September 2026 ([s.345](https://www.irishstatutebook.ie/eli/2014/act/38/section/345/enacted/en/html)); the return must be delivered not later than 28 days after that date, so by 8 October 2026 ([s.343](https://www.irishstatutebook.ie/eli/2014/act/38/section/343/enacted/en/html)). Financial statements need not be annexed to the first annual return ([s.349](https://www.irishstatutebook.ie/eli/2014/act/38/section/349/enacted/en/html)). Later returns fall on the anniversary of the first annual return date.
- Corporation Tax: if the first accounting period ends on 31 December 2026, the CT1 is due, and any balance payable, by 23 September 2027 ([Revenue: payment and filing](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax-payment-and-filing/payment-and-filing.aspx)). Preliminary tax: see ie-corporation-tax.

### Case 5: services business under the VAT threshold

A new consultancy expects services turnover of €40,000 in 2026. Registration is not obligatory because turnover does not exceed €42,500, but it may elect to register (for example to recover VAT on start-up costs, or because its customers are VAT-registered businesses). Once turnover exceeds €42,500 it must register ([Revenue: VAT thresholds](https://www.revenue.ie/en/vat/vat-registration/who-should-register-for-vat/vat-thresholds.aspx)). The timing and mechanics are in ireland-vat-return.

## When to refuse or refer

- **Sham nominee directors.** Do not arrange an EEA-resident "director" who has no real role just to satisfy s.137. Use the bond, a s.140 certificate, or a genuine appointment.
- **Residence engineering.** Do not advise incorporating in Ireland while arranging for the company to be tax resident nowhere or in a no-tax country. An Irish-incorporated company is resident here unless a treaty makes it resident elsewhere; reliance on a treaty tie-breaker goes to a specialist.
- **Company formed only to shelter a person's income.** Moving personal service income into a company with no commercial reason, while drawing everything out, may be challenged under the general anti-avoidance rule (s.811C of the Taxes Consolidation Act) and triggers the service company surcharge. Record the commercial reasons, or refer.
- **Regulated activity.** Banking, insurance, investment services, fund management, payments and e-money, consumer credit, crypto-asset services: Central Bank of Ireland authorisation, with capital requirements far above company law. Other sectors with their own licensing include alcohol (Revenue excise licence plus a court licence), food (food business registration), childcare (Tusla), health and social care (HIQA, HPRA), telecoms (ComReg), broadcasting and online media (Coimisiún na Meán), gambling (the Gambling Regulatory Authority), and aviation (IAA). Forming the company is not permission to trade: refer before quoting a timetable.
- **Charities.** Charitable status and Revenue's charitable tax exemption need separate applications; refer to someone who does charity registrations.
- **Immigration.** Non-EEA founders who will live or work in Ireland need an immigration permission: refer to an immigration adviser.
- **Funds and investment vehicles:** ICAVs, investment limited partnerships, section 110 companies: refer.
- **Transferring an existing business into a company:** capital gains tax, stamp duty, VAT on the transfer and the treatment of goodwill need specialist advice: refer.
- **Data protection.** Any business handling personal data must comply with the GDPR and the Data Protection Act 2018; this Guide only flags it.
- **Bank accounts.** Banks apply their own anti-money-laundering checks; no outcome can be promised.

## Filing and payment

**Company, every year**

- Annual return to the CRO within 28 days after the annual return date, with the statutory financial statements annexed (except the first return) ([s.343](https://www.irishstatutebook.ie/eli/2014/act/38/section/343/enacted/en/html), [s.345](https://www.irishstatutebook.ie/eli/2014/act/38/section/345/enacted/en/html)). Late filing fees and the loss of audit exemption for late filers: **check** with the CRO.
- Corporation Tax ([Revenue: payment and filing](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax-payment-and-filing/payment-and-filing.aspx)): pay preliminary tax by its due date; file the CT1 and Form 46G (Company) and pay any balance by the 23rd of the ninth month after the end of the accounting period, through ROS. Filing late adds a surcharge of 5% of the tax (up to €12,695) if within two months of the deadline, or 10% (up to €63,485) after that, and restricts some reliefs. Late tax carries interest at 0.0219% a day.
- RBO: file any change to beneficial ownership within 14 days of the date the company's own register had to be updated.
- Payroll: report pay and deductions to Revenue on or before each payday.
- VAT returns: see ireland-vat-return.

**Sole trader or partner**

- Income Tax return (Form 11) and self-assessment through ROS by 31 October of the following year, with an extended date if filing and paying on ROS ([Revenue: filing your tax return](https://www.revenue.ie/en/self-assessment-and-self-employment/filing-your-tax-return/index.aspx)). Preliminary tax for the current year is paid at the same time.
- A partnership also files a partnership return; each partner returns their share.
- Business name changes to the CRO within one month.

**Dated: returns being filed now for 2025**

- The Pay and File deadline for the 2025 Form 11 is Saturday 31 October 2026; paying and filing on ROS extends it to Wednesday 18 November 2026 ([Revenue: filing your tax return](https://www.revenue.ie/en/self-assessment-and-self-employment/filing-your-tax-return/index.aspx)). The 2025 bands and credits were the same as 2026 (€44,000 standard rate band; €2,000 credits), but the 2025 USC bands differed: first €12,012 at 0.5%, next €15,370 at 2%, next €42,662 at 3%, balance at 8% ([Revenue: USC rates](https://www.revenue.ie/en/jobs-and-pensions/usc/standard-rates-thresholds.aspx)).
- A company with a 31 December 2025 year end had to file its CT1 and pay the balance by 23 September 2026.

## Completion checklist

- [ ] Founders' residence, PPS numbers and activity recorded; regulated or out-of-scope matters referred.
- [ ] Vehicle chosen, with the reasons and the profit and drawings assumptions written down.
- [ ] Company: type confirmed; at least one director (two for a DAC, CLG or PLC); secretary appointed and not the sole director.
- [ ] Company: EEA-resident director, or s.137 bond, or s.140 certificate in place before filing.
- [ ] Constitution in the right form for the company type; s.22 statement and s.24 declaration ready.
- [ ] CRO fees, forms and identity requirements confirmed on the CRO site (**check**).
- [ ] Business name registered if trading under another name (within one month).
- [ ] Company's own beneficial ownership register set up; RBO filing diarised within 5 months of incorporation.
- [ ] Revenue registration made by the right route (ROS through an agent, eRegistration, or TR1 / TR2); taxes chosen: Income Tax or Corporation Tax, VAT, employer PAYE (compulsory if directors are paid), RCT.
- [ ] VAT threshold tested on the correct category; non-established rule considered.
- [ ] First annual return date, CT1 date, preliminary tax, payroll and VAT dates in the diary.
- [ ] Companion Guides consulted where needed: ie-corporation-tax and ireland-vat-return.

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
