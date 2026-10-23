---
name: de-treaty-withholding-rates
description: "Use this skill when a German company, bank or licensee pays dividends, interest or royalties to a person outside Germany, tax year 2026. Covers the domestic withholding (Kapitalertragsteuer 25% plus 5.5% solidarity surcharge, 26.375% in all; § 50a 15% on royalties), the treaty limits for Germany's main partners (Austria, Switzerland, Netherlands, France, Italy, Spain, UK, Ireland, Luxembourg, US, Poland, Czech Republic) read from the treaty texts, the exemption certificate and refund at the BZSt (§ 50c EStG), the EU Parent-Subsidiary exemption (§ 43b), the Interest and Royalties exemption (§ 50g), the two-fifths refund for foreign companies (§ 44a(9)) and the anti-treaty-shopping rule (§ 50d(3)). Trigger on: Quellensteuer Deutschland, Kapitalertragsteuer Erstattung, Freistellungsbescheinigung, § 50c, § 43b, § 50g, § 50d Abs. 3, DBA Quellensteuersatz, German withholding tax rate treaty. Out of scope: assessing non-residents (de-non-resident-tax), foreign tax on a German resident's income (de-capital-gains), Swiss commuters (germany-to-switzerland-cross-border-tax)."
jurisdiction: DE
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
verified_by: pending
---

# Germany: withholding on dividends, interest and royalties paid abroad, and the treaty rates, tax year 2026

This skill works out how much German tax is withheld when a German payer pays dividends, interest or royalties to a non-resident, what the treaty with the recipient's country allows, and how the recipient gets the difference: an exemption certificate before payment, or a refund after it. It also covers the two EU directive exemptions and the anti-treaty-shopping rule.

See also, and do not repeat here:

- **de-non-resident-tax**: when a non-resident is taxed in Germany at all, the § 50a basics (artists, athletes, supervisory boards), and the § 34c and § 32d(5) credits for German residents with foreign income.
- **de-corporate-tax**: the 95% exemption for dividends between companies (§ 8b KStG), which matters for a German permanent establishment.
- **germany-to-switzerland-cross-border-tax**: employment income across the Swiss border.
- **germany-transfer-pricing**: the arm's length price of royalties and interest between related companies.

## Who this applies to

- **The German payer.** A German company paying dividends, the German bank or custodian paying dividends on shares held in collective custody, or a German business paying royalties or certain interest to a non-resident. The payer withholds and pays the tax over. It is liable for tax it should have withheld (§ 44(5), § 50a(5) EStG).
- **The foreign recipient.** A person or company with neither residence nor management in Germany. It carries the tax, and claims the treaty or directive relief from the Bundeszentralamt für Steuern (BZSt), not from the payer.
- **Withholding comes first.** The payer withholds the full domestic rate even when a treaty or directive limits German tax, unless the recipient holds an exemption certificate from the BZSt (§ 50c(1), (2) EStG). The payer cannot rely on the recipient's treaty rights itself.

Which income is caught:

- **Dividends** from a company with its seat or management in Germany (§ 49(1) no. 5(a); § 43(1) no. 1 EStG).
- **Interest.** Ordinary interest on a loan, bank account or listed bond paid to a non-resident is not German-source income and has no German tax (see de-non-resident-tax). Interest on convertible bonds, profit-sharing bonds (Gewinnobligationen) and profit-participation rights carries Kapitalertragsteuer (§ 43(1) no. 2). Loans secured on German land are German-source income too (§ 49(1) no. 5(c)). So a treaty interest rate matters only for these cases.
- **Royalties** for the use of rights, know-how, plans or processes, used in Germany (§ 50a(1) no. 3; § 49(1) nos. 2, 3, 6, 9 EStG).

## Rates, bands and thresholds

### German domestic withholding

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Kapitalertragsteuer on dividends and profit-dependent interest | 25% of gross | 2026 | https://www.gesetze-im-internet.de/estg/__43a.html |
| Solidarity surcharge on Kapitalertragsteuer and § 50a tax | 5.5% of the tax withheld | 2026 | https://www.gesetze-im-internet.de/solzg_1995/__3.html |
| Total withheld on a dividend | 26.375% of gross | 2026 | https://www.bzst.de/DE/Unternehmen/Kapitalertraege/Kapitalertragsteuerentlastung/Sonderkonstellation/Erstattungsverfahren_50c/erstattungsverfahren_50c_node.html |
| Foreign company without treaty or directive relief | Refund of two fifths of the Kapitalertragsteuer withheld and of the surcharge on it | 2026 | https://www.gesetze-im-internet.de/estg/__44a.html (§ 44a(9)); BZSt refund page (surcharge) |
| § 50a on royalties | 15% of gross receipts, plus 5.5% surcharge (15.825% in all) | 2026 | https://www.gesetze-im-internet.de/estg/__50a.html (§ 50a(2)) |
| Small royalties under a treaty that bars German tax | No withholding if royalties from that payer in the year stay at or below EUR 10,000; the return is still filed | 2026 | https://www.gesetze-im-internet.de/estg/__50c.html (§ 50c(2) no. 2) |
| Exemption certificate | Valid for at most five years, from the day the application reaches the BZSt; for treaty relief on dividends only for a company that is subject to tax at home without exemption and holds at least 10% of the nominal capital directly | 2026 | Same, § 50c(2) sentences 4, 5 |
| Refund deadline | Four years from the end of the year of receipt; not before one year after payment, nor before a longer treaty period | 2026 | Same, § 50c(3) sentence 2 |
| § 43b EU parent | At least 10% direct holding; held without break for 12 months | 2026 | https://www.gesetze-im-internet.de/estg/__43b.html |
| § 50g associated companies | At least 25% direct holding, in either direction or by a common parent | 2026 | https://www.gesetze-im-internet.de/estg/__50g.html (§ 50g(3) no. 5(b)) |

### Treaty limits on German tax, by country of the recipient

Rates are the maximum German tax a treaty allows on the gross amount when the recipient is the beneficial owner and resident in the other state. The domestic rate applies until relief is granted. "0%" means the other state alone may tax. A blank means the rate was not read on an official page.

| Recipient's country | Dividends, general | Dividends, qualifying holding | Interest | Royalties | Source (treaty text read) |
|---|---|---|---|---|---|
| Austria | 15% | 5%: company (not a partnership) holding at least 10% of capital directly | 0% (profit-participating income may be taxed in Germany, art. 11(2)) | 0% | https://www.bundesfinanzministerium.de/Content/DE/Standardartikel/Themen/Steuern/Internationales_Steuerrecht/Staatenbezogene_Informationen/Laender_A_Z/Oesterreich/2024-11-28-Oesterreich-Abkommen-DBA-Bekanntmachung.pdf?__blob=publicationFile&v=2 (arts. 10 to 12) |
| Switzerland | 15% | 0%: company (not a partnership) holding at least 10% of capital directly for 365 days including the payment day; not for a REIT-AG or investment fund | 0% | 0% | https://www.bundesfinanzministerium.de/Content/DE/Standardartikel/Themen/Steuern/Internationales_Steuerrecht/Staatenbezogene_Informationen/Laender_A_Z/Schweiz/2026-07-15-Schweiz-DBA-Bekanntmachung-Neufassung.pdf?__blob=publicationFile&v=2 (arts. 10 to 12) |
| Netherlands | 15% | 5%: company holding at least 10% of capital directly for 365 days; 10% to a Dutch pension fund | 0% | 0% | https://www.bundesfinanzministerium.de/Content/DE/Standardartikel/Themen/Steuern/Internationales_Steuerrecht/Staatenbezogene_Informationen/Laender_A_Z/Niederlande/2026-05-18-Niederlande-Abkommen-DBA-Bekanntmachung.pdf?__blob=publicationFile&v=2 (arts. 10 to 12) |
| France | 15% | 5%: French company holding at least 10% of capital; for 365 days from 2025 (MLI art. 8) | 0% (art. 10) | 0% (art. 15) | https://www.bundesfinanzministerium.de/Content/DE/Standardartikel/Themen/Steuern/Internationales_Steuerrecht/Staatenbezogene_Informationen/Laender_A_Z/Frankreich/2025-01-01-Abkommen-Synthetisierter-Text.pdf?__blob=publicationFile&v=3 (art. 9(2), (5), arts. 10, 15) |
| Italy | 15% | 15% (the 10% rate in art. 10(3) covers only Italian dividends paid to German companies) | 10%; 0% on credit sales of goods or equipment, on government bonds and on interest paid to a government or central bank (art. 11(3)), and on loans of any kind from one bank to another (protocol no. 11) | 5%; 0% for copyright in literary, dramatic, musical or artistic works and films (art. 12(3)) | https://www.bundesfinanzministerium.de/Content/DE/Standardartikel/Themen/Steuern/Internationales_Steuerrecht/Staatenbezogene_Informationen/Laender_A_Z/Italien/1990-08-18-Italien-Abkommen-DBA-Gesetz.pdf?__blob=publicationFile&v=1 (arts. 10 to 12) |
| Spain | 15% | 5%: company (not a partnership or REIT) holding at least 10% of capital directly; for 365 days from 2025 (MLI art. 8) | 0% | 0% | https://www.bundesfinanzministerium.de/Content/DE/Standardartikel/Themen/Steuern/Internationales_Steuerrecht/Staatenbezogene_Informationen/Laender_A_Z/Spanien/2025-01-01-Abkommen-Synthetisierter-Text.pdf?__blob=publicationFile&v=3 (arts. 10 to 12) |
| United Kingdom | 15% | 5%: company (not a partnership) holding at least 10% of capital directly; 10% to a pension scheme | 0% | 0% | https://www.bundesfinanzministerium.de/Content/DE/Standardartikel/Themen/Steuern/Internationales_Steuerrecht/Staatenbezogene_Informationen/Laender_A_Z/Grossbritannien/2010-11-23-Grossbritannien-Abkommen-DBA-Gesetz.pdf?__blob=publicationFile&v=1 (arts. 10 to 12; rates not changed by the 2021 protocol) |
| Ireland | 15% | 5%: company (not a partnership or REIT) holding at least 10% of capital directly for 365 days | 0% | 0% | https://www.bundesfinanzministerium.de/Content/DE/Standardartikel/Themen/Steuern/Internationales_Steuerrecht/Staatenbezogene_Informationen/Laender_A_Z/Irland/2025-04-10-Irland-Abkommen-DBA-Bekanntmachung.pdf?__blob=publicationFile&v=3 (arts. 10 to 12, protocol no. 3) |
| Luxembourg | 15% | 5%: company holding at least 10% of capital directly (from 2024; only 15% for a REIT-AG or a collective investment body) | 0% | 5% | https://www.bundesfinanzministerium.de/Content/DE/Standardartikel/Themen/Steuern/Internationales_Steuerrecht/Staatenbezogene_Informationen/Laender_A_Z/Luxemburg/2023-12-13-Luxemburg-Abkommen-DBA-Gesetz.pdf?__blob=publicationFile&v=3 (protocol of 6 July 2023, arts. 4, 5); art. 12 in https://www.bundesfinanzministerium.de/Content/DE/Standardartikel/Themen/Steuern/Internationales_Steuerrecht/Staatenbezogene_Informationen/Laender_A_Z/Luxemburg/2012-12-10-Luxemburg-Abkommen-DBA-Gesetz.pdf?__blob=publicationFile&v=1 |
| United States | 15% | 5%: company owning at least 10% of the voting stock directly; 0%: a company that has owned directly at least 80% of the votes for the 12 months ending on the day entitlement is fixed and that qualifies under art. 28 (listed company, ownership and base erosion with the active business test, derivative benefits, or a competent authority decision; art. 10(3)(a)), or a US pension fund whose dividends do not come from carrying on a business (art. 10(3)(b)). RICs and REITs: art. 10(4) | 0% | 0% | https://www.bundesfinanzministerium.de/Content/DE/Standardartikel/Themen/Steuern/Internationales_Steuerrecht/Staatenbezogene_Informationen/Laender_A_Z/Verein_Staaten/2008-06-23-USA-Abkommen-DBA-Bekanntmachung.pdf?__blob=publicationFile&v=1 (arts. 10 to 12) |
| Poland | 15% | 5%: company (not a partnership) holding at least 10% of capital directly | 5%; 0% to the government, on export-credit loans, on credit sales of equipment or goods, and on bank loans (art. 11(3)) | 5% | https://www.bundesfinanzministerium.de/Content/DE/Standardartikel/Themen/Steuern/Internationales_Steuerrecht/Staatenbezogene_Informationen/Laender_A_Z/Polen/2004-04-29-Polen-Abkommen-DBA-Gesetz.pdf?__blob=publicationFile&v=1 (arts. 10 to 12) |
| Czech Republic | 15% | 5%: company holding at least 25% of capital directly | 0% | 5% | https://www.bundesfinanzministerium.de/Content/DE/Standardartikel/Themen/Steuern/Internationales_Steuerrecht/Staatenbezogene_Informationen/Laender_A_Z/Tschechien/2025-06-18-Abkommen-Synthetisierter-Text.pdf?__blob=publicationFile&v=3 (arts. 10 to 12) |

Profit-dependent income needs care. Several treaties let Germany tax income from a silent partnership, a profit-participating loan or profit-sharing bonds at its domestic rate where the payer can deduct it: for example Austria art. 11(2), France art. 9(9), Ireland protocol no. 3, Netherlands protocol no. IX, US art. 10(6). Switzerland caps it at 30% instead of 15% (art. 10(2)(b)). Read the treaty before applying a 0% interest rate to such income.

## The taxable base

### Step 1: what is withheld

1. **Dividends.** 25% Kapitalertragsteuer on the gross dividend, plus 5.5% surcharge on that tax: 26.375% (§ 43a(1), (2) EStG). The full gross is the base; no costs are deducted. The tax arises on the day the dividend is paid as fixed in the distribution resolution (§ 44(2)). The company withholds; for shares in collective custody, the German custodian bank does (§ 44(1) sentence 3).
2. **Profit-dependent interest.** The same 26.375% (§ 43(1) no. 2, § 43a(1) no. 1).
3. **Royalties.** 15% of gross receipts plus surcharge: 15.825% (§ 50a(2)). Costs can be deducted only for the receipts listed in § 50a(3), which does not include royalties.

### Step 2: what the recipient can get back

Pick the best relief that applies; they do not add up.

| Relief | Who | Result | How |
|---|---|---|---|
| Treaty | Resident of the treaty state who is the beneficial owner | German tax cut to the treaty rate | Exemption certificate before payment (§ 50c(2) no. 1), or refund after (§ 50c(3)) |
| § 43b EU Parent-Subsidiary Directive | EU parent company (form in Anlage 2 EStG) holding at least 10% directly; 12 months without break | No Kapitalertragsteuer on profit distributions (not on liquidation or reorganisation payouts) | Exemption certificate; if the 12 months end after payment, refund only (§ 43b(2) sentence 5) |
| § 50g EU Interest and Royalties Directive | EU company (Anlage 3 form, subject to a listed tax and not exempt) that is the beneficial owner, and associated by at least 25% directly; Swiss companies count too (§ 50g(6)) | No Kapitalertragsteuer on interest and no § 50a tax on royalties | Exemption certificate or refund; refunds carry interest (§ 50c(4)) |
| § 44a(9) | Any foreign company with limited corporate tax liability | Two fifths of the Kapitalertragsteuer and of the surcharge back (BZSt) | Refund; further treaty or directive claims stay open |

**Portfolio holdings below 15% (§ 50j).** Where a treaty cuts German tax on dividends below 15% for a shareholder that is not a company holding at least 10% (for example the US pension fund at 0%, or the Dutch pension fund and UK pension scheme at 10%), the refund needs the recipient to have been the beneficial owner for 45 days within 45 days either side of the due date, carrying at least 70% of the risk of a fall in value, and not to pass the dividend on (§ 50j EStG).

§ 50g does not cover interest treated as a profit distribution, interest on profit-participating claims, or the part of interest or royalties above an arm's length amount (§ 50g(2)).

**Refund amount on a treaty dividend.** Refund = tax withheld − treaty limit × gross dividend. For a 15% treaty: 26.375% − 15% = 11.375% of the gross. This holds where the treaty's covered taxes include the solidarity surcharge. Austria, Luxembourg, the Netherlands, Spain, the UK, Ireland and Poland list German taxes "including the supplements levied thereon" (art. 2); Switzerland and France cover taxes levied "also in the form of surcharges" (art. 2(1), art. 1(2)). Italy, the US and the Czech Republic do not name supplements; there the surcharge comes in only as a later tax of a similar kind (Italy art. 2(4), US art. 2(2), Czech Republic art. 2(5)).

### Step 3: the anti-treaty-shopping test (§ 50d(3) EStG)

A foreign company gets no treaty relief from Kapitalertragsteuer or § 50a tax to the extent that:

1. its shareholders or beneficiaries would not have the relief if they earned the income directly, and
2. the income has no substantial link to the company's own business. Earning the income and passing it on, and activity carried on with a business not set up adequately for its purpose, are not business.

The company escapes if it shows that none of the main purposes of its involvement is a tax advantage, or if its main class of shares is traded substantially and regularly on a recognised exchange. § 43b, § 50g and § 44a(9) apply § 50d(3) too. § 42 AO (abuse) still applies.

## Deadlines and filing

| Step | Rule |
|---|---|
| Payer remits Kapitalertragsteuer | Tax withheld in a month, to the tax office by the 10th of the next month (§ 44(1) sentence 5) |
| Payer files § 50a return | Each calendar quarter, by the 10th of the month after it, to the BZSt; also when nothing is withheld because of a certificate or the small-royalty rule (§ 50a(5) sentences 3, 4; § 50c(2) sentence 2) |
| Payer's certificate to the recipient | Tax certificate for Kapitalertragsteuer (§ 45a); § 50a certificate on request (§ 50a(5) sentence 7). Both are needed for a refund |
| Exemption certificate application | Before payment; to the BZSt, electronically; decided within three months of complete documents (§ 50c(2) sentence 6, (5)) |
| Refund application | Electronically at the BZSt online portal, form "Erstattung der deutschen Abzugsteuer auf Kapitalerträge"; with a residence confirmation from the recipient's tax authority (§ 50c(5)) |
| Refund deadline | Four years from the end of the year of receipt: for a 2026 dividend, by 31 December 2030 |
| Processing | The BZSt says refunds can take more than 20 months |
| New § 50a form | From 7 December 2026 only in the new BZSt online portal (BZSt notice) |

## Penalties and interest

- **Payer liability.** The payer is liable for Kapitalertragsteuer it should have withheld, unless it shows it did not breach its duties deliberately or with gross negligence (§ 44(5)). For § 50a tax the payer is liable without that defence; the recipient can also be pursued (§ 50a(5) sentences 5, 6).
- **Late payment (§ 240 AO).** 1% per started month on tax not paid over on time, rounded down to EUR 50.
- **Late filing of a withholding return (§ 152(1) AO).** The tax office may set a late-filing surcharge. The amount for withholding returns is not set out here.
- **Interest on § 50g refunds (§ 50c(4)).** 0.5% per full month (§ 238(1) AO; the 0.15% rate in § 238(1a) is only for § 233a interest), from 12 months after the month in which the complete application and evidence arrive, at the earliest from payment of the tax, until the refund decision takes effect. Treaty refunds carry no interest under § 50c(4).

## Cross-border points

- **The recipient's home country.** The tax that stays in Germany at the treaty rate is credited or relieved under the recipient's own law and the treaty's article on eliminating double tax. Not covered here.
- **Non-cooperative jurisdictions.** Since 2022 the Tax Haven Defence Act (StAbwG § 10) brings further payments to residents of listed non-cooperative jurisdictions into withholding (BZSt notice). Not set out here.
- **German permanent establishment.** If the shares, claim or right belong to a German permanent establishment of the recipient, the treaty article on business profits applies instead and the income is assessed (for example Austria art. 10(4)).
- **Investment funds and REITs.** Several treaties limit the reduced dividend rate for REIT-AGs and investment funds (Switzerland, Netherlands, Ireland, Spain, Luxembourg, US). Check the treaty text.
- **German residents receiving foreign income.** The other direction is in de-non-resident-tax and de-capital-gains.

## Worked examples

### Example 1: Austrian private investor, German dividend, 15% treaty rate

Petra lives in Graz. In 2026 a German AG pays her a dividend of EUR 10,000 gross. She holds the shares privately. The custodian withholds Kapitalertragsteuer and surcharge. (Invented case.)

- Kapitalertragsteuer: 25% × 10,000 = EUR 2,500.
- Surcharge: 5.5% × 2,500 = EUR 137.50. Total withheld EUR 2,637.50 (26.375%).
- Treaty limit (Austria art. 10(2)(b), general case): 15% × 10,000 = EUR 1,500. The covered German taxes include supplements (art. 2(3)(a)), so the 15% caps tax and surcharge together.
- Refund: 2,637.50 − 1,500 = EUR 1,137.50, which is 11.375% of the gross.
- Route: electronic refund application at the BZSt by 31 December 2030, with a residence confirmation from her Austrian tax office and the German tax certificate. She cannot get an exemption certificate in advance: for dividends those are given only to companies holding at least 10% (§ 50c(2) sentence 5).

```oa-check
name: DE dividend to Austrian individual 2026, refund down to 15% treaty rate
inputs:
  dividend: 10000
  kapest_rate: 0.25
  soli_rate: 0.055
  treaty_rate: 0.15
steps:
  - kapest: dividend * kapest_rate
  - soli: kapest * soli_rate
  - withheld: kapest + soli
  - treaty_tax: dividend * treaty_rate
  - refund: withheld - treaty_tax
  - refund_pct: refund / dividend * 100
expected:
  kapest: 2500
  soli: 137.50
  withheld: 2637.50
  treaty_tax: 1500
  refund: 1137.50
  refund_pct: 11.375
```

### Example 2: royalties to a Czech parent, § 50g exemption

A German GmbH pays EUR 200,000 of royalties in 2026 for a patent licence to its Czech shareholder, a společnost s ručením omezeným (s.r.o.) that holds 30% of the GmbH directly. The s.r.o. is subject to Czech corporate income tax, is the beneficial owner, runs its own development business, and the royalty is at arm's length. (Invented case.)

- Without relief: § 50a tax 15% × 200,000 = EUR 30,000, surcharge 5.5% × 30,000 = EUR 1,650, total EUR 31,650.
- Treaty only (Czech Republic art. 12(2)): German tax at most 5% of gross, EUR 10,000.
- § 50g: the s.r.o. is an EU company in a form listed in Anlage 3, subject to a listed tax ("Daň z příjmů právnických osob"), and associated by at least 25% directly. German tax: nil. § 50d(3) is passed because the royalty is linked to its own business.
- Route: the s.r.o. applies to the BZSt for an exemption certificate before the first payment. The GmbH then withholds nothing but still files the quarterly § 50a return (§ 50c(2) sentence 2). If the GmbH paid before the certificate arrived, it withholds EUR 31,650 and the s.r.o. claims a refund under § 50c(3), with interest from 12 months after its complete application (§ 50c(4)).
- Saving against the treaty alone: EUR 10,000.

```oa-check
name: DE royalties to Czech 30% parent 2026, § 50a vs treaty vs § 50g
inputs:
  royalties: 200000
  rate_50a: 0.15
  soli_rate: 0.055
  treaty_rate: 0.05
  holding_pct: 30
steps:
  - tax_50a: royalties * rate_50a
  - soli: tax_50a * soli_rate
  - withheld_no_relief: tax_50a + soli
  - treaty_max: royalties * treaty_rate
  - holding_margin: holding_pct - 25
  - tax_50g: 0
  - refund_if_withheld: withheld_no_relief - tax_50g
  - saving_vs_treaty: treaty_max - tax_50g
expected:
  tax_50a: 30000
  soli: 1650
  withheld_no_relief: 31650
  treaty_max: 10000
  holding_margin: 5
  refund_if_withheld: 31650
  saving_vs_treaty: 10000
```

## Ask the client first

1. Who receives the payment, where is it resident, and is it the beneficial owner or a nominee or conduit?
2. Individual, company or partnership? For a company: its legal form, whether it pays corporate tax at home, and its own staff, premises and business.
3. For dividends: the percentage held directly in the German company, since when, and whether the shares will be held for 365 days (or 12 months for § 43b).
4. For interest: is it ordinary interest, or does it depend on profit (silent partnership, profit-participating loan, convertible or profit-sharing bond)?
5. For royalties: what rights are licensed, the amounts per year, and whether the parties hold at least 25% of each other or share a 25% parent.
6. Has the recipient applied for an exemption certificate, and when are the payments due?

## Sources

| Source | URL | Read on |
|---|---|---|
| EStG § 43 (income subject to Kapitalertragsteuer) | https://www.gesetze-im-internet.de/estg/__43.html | 2026-10-23 |
| EStG § 43a (25% rate) | https://www.gesetze-im-internet.de/estg/__43a.html | 2026-10-23 |
| EStG § 43b (EU parent companies) | https://www.gesetze-im-internet.de/estg/__43b.html | 2026-10-23 |
| EStG § 44 (when tax arises, remittance, liability) | https://www.gesetze-im-internet.de/estg/__44.html | 2026-10-23 |
| EStG § 44a(9) (two-fifths refund) | https://www.gesetze-im-internet.de/estg/__44a.html | 2026-10-23 |
| EStG § 49 (German-source income) | https://www.gesetze-im-internet.de/estg/__49.html | 2026-10-23 |
| EStG § 50a (15% on royalties, quarterly return) | https://www.gesetze-im-internet.de/estg/__50a.html | 2026-10-23 |
| EStG § 50c (exemption certificate, refund, interest) | https://www.gesetze-im-internet.de/estg/__50c.html | 2026-10-23 |
| EStG § 50d (anti-treaty-shopping, § 50d(3)) | https://www.gesetze-im-internet.de/estg/__50d.html | 2026-10-23 |
| EStG § 50g (interest and royalties between EU companies) | https://www.gesetze-im-internet.de/estg/__50g.html | 2026-10-23 |
| EStG Anlage 3 (company forms and taxes for § 50g) | https://www.gesetze-im-internet.de/estg/anlage_3.html | 2026-10-23 |
| SolzG § 3 (surcharge base) | https://www.gesetze-im-internet.de/solzg_1995/__3.html | 2026-10-23 |
| AO §§ 152, 238, 240 | https://www.gesetze-im-internet.de/ao_1977/__240.html | 2026-10-23 |
| BZSt, refund procedure § 50c(3) and § 44a(9) (26.375%, deadline, over 20 months) | https://www.bzst.de/DE/Unternehmen/Kapitalertraege/Kapitalertragsteuerentlastung/Sonderkonstellation/Erstattungsverfahren_50c/erstattungsverfahren_50c_node.html | 2026-10-23 |
| BZSt, exemption procedure § 50c(2) | https://www.bzst.de/DE/Unternehmen/Kapitalertraege/Kapitalertragsteuerentlastung/Sonderkonstellation/Freistellungsverfahren_50c/freistellungsverfahren_50c_node.html | 2026-10-23 |
| BZSt online portal, refund application form | https://online.portal.bzst.de/SharedDocs/Leistungsbeschreibung/DE/erstattung_abzugsteuer_kapitalertraege_50c_estg.html | 2026-10-23 |
| BZSt, Abzugsteuern nach § 50a (StAbwG, new form from 7 December 2026) | https://www.bzst.de/DE/Unternehmen/Abzugsteuern/abzugsteuern_node.html | 2026-10-23 |
| BMF treaty texts, one per country | See the table under "Treaty limits" | 2026-10-23 |
| EStG § 50j (45-day holding for treaty rates below 15%) | https://www.gesetze-im-internet.de/estg/__50j.html | 2026-10-23 |
| BMF letter of 7 January 2026, treaties in force on 1 January 2026 | https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Internationales_Steuerrecht/Allgemeine_Informationen/2026-01-07-stand-DBA-1-januar-2026.pdf?__blob=publicationFile&v=2 | 2026-10-23 |
| GOV.UK, 2010 UK-Germany convention as amended by the 2021 protocol (cross-check of the UK row) | https://www.gov.uk/government/publications/germany-tax-treaties/2010-uk-germany-double-taxation-convention-as-amended-by-the-2021-protocol-in-force | 2026-10-23 |
| Fedlex, Germany-Switzerland treaty (cross-check of the Swiss row) | https://www.fedlex.admin.ch/eli/cc/1972/3075_3128_2910/de | 2026-10-23 |

The Italian, Polish and Luxembourg (art. 12) rows are read from scanned treaty texts on the BMF site by text recognition; the BMF list of treaties in force on 1 January 2026 (letter of 7 January 2026) shows no later protocol for Italy or Poland and the 2023 Luxembourg protocol applying from 1 January 2024.

Not yet confirmed: whether the BZSt in practice applies the Italian, US and Czech limits to tax and surcharge together (those treaties do not name supplements; the refund formula assumes they do); the late-filing surcharge on withholding returns; the StAbwG rates; any BZSt country table of residual rates (the BZSt table found covers foreign tax credited to German residents, not German tax on payments abroad, so it was not used for the rates above).
