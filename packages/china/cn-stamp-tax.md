---
name: cn-stamp-tax
description: 使用本技能处理一切与中国印花税相关的问题。触发短语包括“中国印花税”、“印花税法 2022”、“合同印花税”、“证券交易印花税”、“权证许可证印花税”、“产权转移书据印花税”、“营业账簿印花税”、“印花税申报”、“印花税税目税率表”、“按次申报印花税”、“按期申报印花税”、“涉外合同印花税”、“借款合同印花税”、“技术合同印花税”、“租赁合同印花税”。亦在英文短语出现时触发：“China stamp tax”、“China stamp duty”、“China stamp tax law 2022”、“PRC stamp duty”。涵盖范围包括《中华人民共和国印花税法》（2022年7月1日施行）下的13类合同税率、5项产权转移书据、营业账簿、证券交易印花税、计税依据、申报周期（按次/按期）、电子税务局申报流程、计算实例及小微企业优惠政策。在处理任何中国印花税工作之前，务必先阅读本技能。
jurisdiction: CN
tax_year: 2026
last_updated: 2026-09-27
authored_by: OpenAccountants team
review_status: pending_review
trust_label: Written by the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# China Stamp Tax (印花税): taxable documents, rates, securities trading, exemptions, the small-business halving and filing for 2026

## Scope and who this is for ([Stamp Tax Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/yhs/202106/t458595.html); [MOF/STA announcement 2022 No. 22](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/yhs/202206/t463167.html))

This Guide covers mainland China stamp tax (印花税) for tax year 2026, the calendar year 1 January to 31 December 2026. It is for companies, individuals and advisers who need to decide whether a document is taxable, compute the tax, and file it.

The legal base is the **Stamp Tax Law of the PRC (中华人民共和国印花税法)**, adopted on 10 June 2021 and in force since 1 July 2022. It replaced the 1988 Provisional Regulations (印花税暂行条例), which were repealed on the same day (Law Art. 20). The law has no annual figures. What changes year to year are the reliefs, several of which end on 31 December 2027.

Who pays (Law Art. 1):
- Units and individuals who **sign (书立) a taxable document in China**, or who **carry out securities trading** in China.
- Units and individuals who **sign a taxable document outside China that is used in China**. The older idea of tax on "receiving" (领受) a document is gone.
- The taxpayer is each party with a direct right or obligation under the document (MOF/STA announcement 2022 No. 22 Art. 1(1)). For an entrusted loan the taxpayers are the trustee and the borrower, not the principal. For an auction confirmation taxed as a sale or transfer, they are the owner and the buyer, not the auctioneer.

The tax is a **positive list**. Only documents in the rate table attached to the law are taxable: certain written contracts, property-transfer documents, business account books, plus securities trading (Law Art. 2-3). A document that is not on the list is not taxed, whatever it is called.

Out of scope: Hong Kong, Macao and Taiwan; deed tax (契税) and land appreciation tax on property; VAT and surcharges; stamp tax audits and disputes. Related Guides: **cn-vat** and **china-vat** (VAT, which is excluded from the stamp tax base when stated separately), **cn-corporate-tax** (the small low-profit enterprise test used by the halving relief), and **cn-iit** (individual income tax on share and property sales).

## What is current for 2026 ([MOF/STA announcement 2023 No. 39](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/yhs/202308/t468451.html); [MOF/STA announcement 2023 No. 12](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/202308/t468162.html); [MOF/STA announcement 2023 No. 13](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202308/t468161.html); [MOF/STA announcement 2024 No. 14](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/yhs/202409/t473303.html); [Caishui 2025 No. 10](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/yhs/202503/t475883.html))

| Topic | Position in 2026 | Source |
|---|---|---|
| Securities trading | Statutory rate one per thousand of the trade value, charged at **half** since 28 August 2023. No end date is stated | MOF/STA announcement 2023 No. 39 |
| Small-business halving | Small-scale VAT taxpayers, small low-profit enterprises and individual businesses pay **half** the stamp tax (not securities stamp tax), 1 January 2023 to 31 December 2027 | MOF/STA announcement 2023 No. 12 Art. 2 |
| Loans to small and micro enterprises | Loan contracts between financial institutions and small or micro enterprises are exempt until 31 December 2027 | MOF/STA announcement 2023 No. 13 Art. 2, 5 |
| Restructuring | Account-book, contract and transfer-document reliefs for restructurings, 1 October 2024 to 31 December 2027 | MOF/STA announcement 2024 No. 14 |
| Offshore trade | Sale contracts for offshore merchanting by enterprises registered in named free trade zones are exempt, 1 April 2025 to 31 December 2027 | Caishui 2025 No. 10 |

No rate in the table attached to the law has changed since 1 July 2022.

## Ask the client first

- What exactly is the document? A written contract, an order form that stands in for a contract, a property-transfer document, an account book, or a share trade? Get a copy, not a description.
- Who signed it, and where is each party? A foreign party that signs a document used in China is also a taxpayer.
- What amount does it state, and is VAT stated as a separate amount? Is only a VAT rate mentioned?
- Does it cover more than one kind of transaction? Are the amounts for each kind shown separately?
- Is the amount fixed, or will it be settled later?
- For a loan: is the lender a bank or another licensed financial institution? Is the borrower a small or micro enterprise?
- For a transfer of shares: are the shares listed or traded on a national exchange, or are they in a private company? Has all the subscribed capital been paid in?
- For account books: what were paid-in capital (股本) and capital reserve (资本公积) when stamp tax was last paid, and what are they now?
- Is the client a small-scale VAT taxpayer, a small low-profit enterprise or an individual business (个体工商户)? Get the evidence.
- Has the contract been amended, cancelled, or never performed?
- Which province is the client in, and has the local bureau set it up for quarterly, annual or per-occurrence filing?

## The method, step by step

1. **Is it on the list?** Match the document to an item in the rate table below by its substance, not its title. If no item fits, there is no stamp tax (Law Art. 2). Check the out-of-scope list and exemptions before going further.
2. **Is there a China link?** Signed in China, or signed abroad and used in China under the tests in MOF/STA announcement 2022 No. 22 Art. 2(1).
3. **Find the tax base.** For contracts and transfer documents, it is the amount stated, excluding VAT only if the VAT amount is stated separately (Law Art. 5). No amount stated: use the amount actually settled, then market price (Law Art. 6). Account books: paid-in capital plus capital reserve, and in later years only the increase (Law Art. 5, 11). Securities: the trade value (Law Art. 5).
4. **Split by item.** Separate amounts for different items use their own rates. If they are not separated, the highest rate applies to the whole amount (Law Art. 9).
5. **Split by party.** Each party pays on the amount that concerns it (Law Art. 10). If a document with several taxpayers does not say what each one's share is, divide the stated amount equally (MOF/STA announcement 2022 No. 22 Art. 3(1)).
6. **Convert currency.** Use the RMB central parity rate on the day the document is signed (MOF/STA announcement 2022 No. 22 Art. 3(5)).
7. **Apply the rate.** Tax = base x rate (Law Art. 8). There is no minimum amount and no rounding rule in the law.
8. **Apply reliefs.** Statutory exemptions (Law Art. 12), then special exemptions, then the small-business halving, which can be stacked on top of other reliefs (MOF/STA announcement 2023 No. 12 Art. 4). Claims are self-assessed. Keep the supporting papers on file (STA announcement 2022 No. 14 Art. 1(5)).
9. **Fix the tax point and period.** Tax arises on the day the document is signed or the trade completes (Law Art. 15). Put it in the quarter, year or single filing that the local bureau has set.
10. **File and pay** through the e-tax bureau on the stamp tax source detail form within the combined property-and-behaviour tax return, within fifteen days of the period end or of the tax point.

## Rates for tax year 2026 ([Stamp Tax Law rate table, reproduced by the Zhongshan Tax Bureau](https://guangdong.chinatax.gov.cn/gdsw/zssw_nsrwkt_sphg_zbsp/2022-07/08/b5cbcdef663d476bbcb821cb6ab21a8c/files/5e07417a94ab464895b4c817b3e75c5c.pdf); [Stamp Tax Law Art. 2-4](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/yhs/202106/t458595.html))

The rates below are the ones in the table attached to the law, unchanged since 1 July 2022. They are written as the law writes them: 万分之三 means three per ten thousand of the base.

| Item (税目) | Rate | Base | Notes in the table |
|---|---|---|---|
| Loan contract (借款合同) | half of one per ten thousand (万分之零点五) | Loan amount | Only loans from banking financial institutions and other financial institutions approved by the banking regulator, to borrowers. Interbank lending is excluded |
| Financial leasing contract (融资租赁合同) | half of one per ten thousand (万分之零点五) | Rent | |
| Sale contract (买卖合同) | three per ten thousand (万分之三) | Price | Sales of movable goods only. Excludes movable-goods sale contracts signed by individuals |
| Work contract (承揽合同) | three per ten thousand (万分之三) | Remuneration | |
| Construction project contract (建设工程合同) | three per ten thousand (万分之三) | Price | |
| Transport contract (运输合同) | three per ten thousand (万分之三) | Transport charges | Freight and multimodal transport. Excludes pipeline transport |
| Technology contract (技术合同) | three per ten thousand (万分之三) | Price, remuneration or royalty | Excludes transfers of patent rights and know-how use rights (taxed as transfer documents) |
| Lease contract (租赁合同) | one per thousand (千分之一) | Rent | |
| Custody contract (保管合同) | one per thousand (千分之一) | Custody fee | |
| Warehousing contract (仓储合同) | one per thousand (千分之一) | Warehousing fee | |
| Property insurance contract (财产保险合同) | one per thousand (千分之一) | Premium | Excludes reinsurance |
| Land use right grant document (土地使用权出让书据) | five per ten thousand (万分之五) | Price | |
| Transfer of land use rights or ownership of buildings and structures | five per ten thousand (万分之五) | Price | Excludes transfers of rural land contract and management rights. Transfer includes sale, inheritance, gift, exchange and division |
| Share transfer document (股权转让书据) | five per ten thousand (万分之五) | Price | Excludes transfers subject to securities stamp tax |
| Transfer of trademark, copyright, patent right or know-how use right | three per ten thousand (万分之三) | Price | |
| Business account books (营业账簿) | two and a half per ten thousand (万分之二点五) | Paid-in capital (share capital) plus capital reserve | |
| Securities trading (证券交易) | one per thousand (千分之一) | Trade value | Charged at half since 28 August 2023. See below |

Only **written** contracts are in the table. The table lists eleven contract items and four kinds of transfer document. There is no futures contract item and no item for "other" account books.

Tianjin Tax Bureau answers confirm individual lines, for example the account-book rate ([Tianjin Q&A, 2025](https://tianjin.chinatax.gov.cn/nsrxt/11200000000/0500/050012/20250207161507617.shtml)) and the securities rate ([Tianjin Q&A, 2022](https://tianjin.chinatax.gov.cn/nsrxt/11200000000/0500/050012/20220725150043296.shtml)).

## What counts as a taxable document ([MOF/STA announcement 2022 No. 22](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/yhs/202206/t463167.html); [STA (89) Guoshuidizi No. 34 on technology contracts](https://fgk.chinatax.gov.cn/zcfgk/c100012/c5193073/content.html))

**Signed abroad, used in China.** A document signed outside China is taxable when (MOF/STA announcement 2022 No. 22 Art. 2(1)):
- it concerns **real estate** located in China;
- it concerns **shares** in a Chinese resident enterprise;
- it concerns **movable goods** or a trademark, copyright, patent or know-how right, and the seller or buyer is in China. A sale by a foreign party to a Chinese party of goods or rights used wholly outside China is not taxable;
- it concerns **services**, and the provider or the recipient is in China. Services provided by a foreign party to a Chinese party wholly outside China are not taxable.

**Orders and similar papers.** Orders, requisition forms and similar papers between enterprises that fix a sale and the parties' rights and duties are taxed as sale contracts when no separate sale contract is signed. Power purchase contracts between power plants and grids, or between grids, are sale contracts (MOF/STA announcement 2022 No. 22 Art. 2(2)-(3)).

**Not taxable at all** (MOF/STA announcement 2022 No. 22 Art. 2(4)):
- court judgments and rulings in force, arbitration awards, and supervisory documents;
- contracts and papers signed by government at county level or above when it expropriates, takes back or compensates and resettles for real estate (房地产) under its administrative powers;
- papers between a head office and its branches, or between branches, used to carry out internal plans.

**Loans outside the loan item.** Only loans from banks and other licensed financial institutions are in the table. Loans between non-financial companies, from shareholders, or between individuals are not taxed.

**Technology contracts.** Technology consulting covers analysis, evaluation and forecasting on technical or economic projects. Ordinary legal, regulatory, accounting and audit consulting is **not** technology consulting and is not taxed. Technology services exclude routine processing, repair, advertising, printing, surveying, testing, and survey or design work. Survey and design fall under construction project contracts. Vocational training and general education contracts are not technology training (STA (89) Guoshuidizi No. 34, shown as fully in force in the STA library). For a technology development contract, only the remuneration is taxed, not the research and development funds. But where the contract sets the remuneration as a proportion of the research funds, that proportion of the remuneration is taxed.

## Tax base: the rules that decide most disputes ([Stamp Tax Law Art. 5-11](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/yhs/202106/t458595.html); [MOF/STA announcement 2022 No. 22 Art. 3](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/yhs/202206/t463167.html); [Shanghai Tax Bureau stamp tax Q&A, 2023](https://shanghai.chinatax.gov.cn/zcfw/rdwd/202303/t466552.html); [Tianjin Tax Bureau VAT Q&A, 2026](https://tianjin.chinatax.gov.cn/nsrxt/11200000000/0500/050012/20260413100927171.shtml); [STA announcement 2022 No. 14](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/yhs/202206/t463170.html))

- **VAT.** The base is the amount stated, **not** including VAT that is **stated as an amount**. If the contract shows a VAT-inclusive price and only a VAT rate, or no VAT at all, tax the full amount. Do not work out the net figure yourself.
- **No amount stated.** Use the amount actually settled. If that still cannot be fixed, use the market price when the document was signed, or the government-set price where one applies (Law Art. 6). In practice: report the document in the first filing period after signing, then pay on the settled amount in the next filing period after settlement (STA announcement 2022 No. 14 Art. 1(2)).
- **Amount changes.** If the stated amount differs from the amount settled and the document is not changed, the stated amount stands. If the document is amended to a higher amount, pay tax on the increase. If it is amended to a lower amount, the taxpayer may ask for a refund of, or offset for, the tax on the decrease (MOF/STA announcement 2022 No. 22 Art. 3(2)).
- **VAT errors.** If the stated VAT was wrong, correct it and recompute the base. Pay on an increase, or claim a refund or offset on a decrease (Art. 3(3)).
- **Unperformed contracts** get no refund or offset. Excess stamps affixed are not refunded (Art. 3(7)-(8)).
- **Several items in one document.** Separate amounts use their own rates. Without separate amounts, the highest rate applies (Law Art. 9). A Shanghai Tax Bureau example: a contract covering freight and warehousing pays three per ten thousand on the freight and one per thousand on the warehousing fee if the two are shown separately, and one per thousand on the whole if they are not.
- **Several parties.** Each pays on its own amount (Law Art. 10). If the shares are not stated, split the amount equally (MOF/STA announcement 2022 No. 22 Art. 3(1)).
- **Share transfers.** The base is the stated price, excluding any stated part that relates to subscribed but unpaid capital (Art. 3(4)). State the two parts separately in the agreement.
- **Multimodal freight in China.** If freight for the whole journey is settled at the origin, the whole freight is the base, paid by the parties settling at the origin. If each leg is settled separately, each leg's freight is taxed on the parties that settle it (Art. 3(6)).
- **Foreign currency.** Convert at the RMB central parity rate on the signing day (Art. 3(5)).
- **Account books.** The base is paid-in capital (share capital) plus capital reserve as recorded. Once tax has been paid, later years are taxed only on an increase in that total (Law Art. 5, 11).

## Securities trading stamp tax ([Stamp Tax Law Art. 3, 5, 7, 14-16](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/yhs/202106/t458595.html); [MOF/STA announcement 2023 No. 39](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/yhs/202308/t468451.html); [Shanghai Tax Bureau securities Q&A, 2023](https://shanghai.chinatax.gov.cn/zcfw/rdwd/202309/t468612.html))

- **What is covered.** Transfers of shares, and depositary receipts based on shares, traded on a lawfully established stock exchange or another national securities trading venue approved by the State Council (Law Art. 3). Bonds and fund units are not in the definition.
- **Who pays.** The **seller** only. The buyer pays nothing (Law Art. 3).
- **Rate.** The statutory rate is one per thousand of the trade value. Since **28 August 2023** it has been charged at half, that is five per ten thousand (MOF/STA announcement 2023 No. 39). The announcement has no end date. It was still in force when this Guide was written.
- **Base.** The trade value. If there is no transfer price, use the closing price on the trading day before the transfer is registered. If there is no closing price, use par value (Law Art. 7).
- **Collection.** The securities depository and clearing body withholds the tax. It pays it over weekly, within five days after each week ends, with the bank interest (Law Art. 14, 16). The investor does not file.
- **Not halved again.** The small-business halving excludes securities stamp tax (MOF/STA announcement 2023 No. 12 Art. 2).
- **Unlisted shares.** A share transfer that is not securities trading is a share transfer document at five per ten thousand, paid by **both** parties.

## Exemptions and reliefs ([Stamp Tax Law Art. 12](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/yhs/202106/t458595.html); [MOF/STA announcement 2022 No. 22 Art. 4](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/yhs/202206/t463167.html); [MOF/STA announcement 2022 No. 23](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/yhs/202206/t463168.html) and [its Annex 1](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/yhs/202206/P020220630368115809685.pdf))

**Statutory exemptions** (Law Art. 12):
- copies and duplicates of a taxable document;
- documents signed by foreign embassies, consulates and international organisations' offices to obtain premises, where the law provides for exemption;
- documents signed by the People's Liberation Army and the People's Armed Police;
- sale contracts and agricultural insurance contracts signed by farmers, family farms, farmers' cooperatives, rural collective economic organisations and village committees to buy farm inputs or sell farm produce (a family farm must be on the national family farm register, MOF/STA announcement 2022 No. 22 Art. 4(2));
- interest-free or subsidised-interest loan contracts, and loan contracts for concessional loans from international financial organisations to China;
- transfer documents for gifts of property to government, schools, social welfare bodies and charities (each defined in MOF/STA announcement 2022 No. 22 Art. 4(3)-(5));
- sale contracts for drugs and medical supplies bought by non-profit medical institutions;
- electronic orders placed by individuals with e-commerce operators.

The State Council may add reductions or exemptions for housing, restructuring, bankruptcy and small and micro businesses (Law Art. 12). When an exemption applies to a document, every party that signs it may use it, unless the rule names a specific taxpayer (MOF/STA announcement 2022 No. 22 Art. 4(1)).

**Housing, kept in force by MOF/STA announcement 2022 No. 23:**
- Lease contracts for housing signed by an individual as landlord or tenant are exempt ([Caishui 2008 No. 24 Art. 2(2)](https://guangdong.chinatax.gov.cn/gdsw/grsdsgg_hmqsc_bzms_grzf/2021-08/31/content_30f96f132c0240c6b486a09f97d40dce.shtml)).
- Individuals selling or buying housing are temporarily exempt ([Caishui 2008 No. 137 Art. 2](https://fgk.chinatax.gov.cn/zcfgk/c102416/c5203534/content.html)). The text covers individuals and housing only. It does not extend to shops or offices. If a company is the other party, confirm its position with the local bureau.

**Small-business halving** ([MOF/STA announcement 2023 No. 12](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/202308/t468162.html)): from 1 January 2023 to 31 December 2027, small-scale VAT taxpayers, small low-profit enterprises and individual businesses pay half the stamp tax, excluding securities stamp tax. There is no cap on the amount. It stacks with other stamp tax reliefs. The small low-profit enterprise test is in Art. 5 of that announcement: the enterprise must be in an industry the state does not restrict or prohibit and meet all three size conditions, measured on annual quarterly averages, and confirmed by the annual corporate income tax settlement. See **cn-corporate-tax**. A newly set up general VAT taxpayer can apply the halving before its first settlement if it meets the headcount and asset limits at the end of the month before filing.

**Loans to small and micro enterprises** ([MOF/STA announcement 2023 No. 13](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202308/t468161.html)): loan contracts between financial institutions and small or micro enterprises (as defined in the 2011 SME classification rules) are exempt until 31 December 2027. The small-loan size limit in that announcement applies to the VAT exemption on interest, not to this stamp tax exemption.

**Restructuring** ([MOF/STA announcement 2024 No. 14](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/yhs/202409/t473303.html)), from 1 October 2024 to 31 December 2027:

| Situation | Treatment |
|---|---|
| New enterprise formed in a restructuring or public-institution conversion | Capital already taxed is not taxed again. Untaxed capital and later increases are taxed |
| Debt-for-equity swap | New capital is taxed, except in State Council-approved restructuring projects |
| Capital increase from revaluation, or other accounts moved into capital or capital reserve | Taxed |
| Contracts carried over unchanged to the successor, tax already paid | Not taxed again |
| Transfer documents for a qualifying conversion, merger, division, bankruptcy liquidation or public-institution conversion (tests below) | Exempt |
| Transfer documents for administrative adjustments of land use rights, buildings and structures, or shares, made under the rules by government at county level or above, or by its departments responsible for state assets | Exempt |
| Allocations (划转) of land use rights, buildings and structures, or shares within the same investor group: parent and wholly owned subsidiary; wholly owned subsidiaries of the same company; an individual and the sole proprietorship, one-person limited company or individual business (个体工商户) they set up | Exempt |

The tests in that announcement (Art. 4):
- **Conversion (改制)** means only three changes: a non-company enterprise becomes a limited liability company or a joint-stock company; a limited liability company becomes a joint-stock company; or a joint-stock company becomes a limited liability company. The original investors must continue and hold **more than 75%** of the converted company, and the converted company must take over the original enterprise's rights and obligations.
- **Merger (合并)** qualifies only where two or more companies merge into one and the original investors continue. A parent absorbing its wholly owned subsidiary, or the reverse, counts as a merger.
- **Division (分立)** qualifies only where a company divides into two or more companies with the same investors as the original.
- "Investors continue" (投资主体存续) means every original investor is still an investor after the change. "Same investors" (投资主体相同) means the investors do not change. In both cases their percentages may change.
- **Public-institution conversion** means converting a public institution into an enterprise, with the original investor continuing and holding **more than 50%** of the new enterprise.
- The enterprises and companies must be set up under Chinese law and registered in China.

**Offshore trade** ([Caishui 2025 No. 10](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/yhs/202503/t475883.html)): sale contracts for offshore merchanting are exempt from 1 April 2025 to 31 December 2027. This applies to enterprises registered in the Shanghai FTZ and Lingang area, the Suzhou area of the Jiangsu FTZ, the Zhejiang FTZ, the Xiamen area of the Fujian FTZ, the Qingdao area of the Shandong FTZ, the Guangdong FTZ, and the Hainan Free Trade Port. Offshore merchanting means a resident enterprise buys goods from a non-resident and resells them to another non-resident, and the goods never cross China's customs border.

Other targeted exemptions (for example social security funds, commodity reserves, rural drinking water, student housing, affordable housing and sporting events) are in the stamp tax section of the tax bureau policy library. Check the specific announcement and its end date before applying one.

## Boundary and exception table ([Stamp Tax Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/yhs/202106/t458595.html); [MOF/STA announcement 2022 No. 22](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/yhs/202206/t463167.html); [Shanghai Tax Bureau share-transfer Q&A, 2022](https://shanghai.chinatax.gov.cn/tax/zcfw/rdwd/202212/t465345.html))

| Situation | Treatment | Why |
|---|---|---|
| Contract states price and VAT amount separately | Tax the price only | Law Art. 5 |
| Contract states VAT-inclusive price and only the VAT rate | Tax the full amount | Law Art. 5; Shanghai and Tianjin bureau answers |
| Sale of goods between two individuals | Not taxed | Rate table note on sale contracts |
| Sale of goods by a company to an individual | The rate table excludes only sale contracts "signed by individuals". The individual's side is outside the item. The company's side is taxed in practice, so confirm with the local bureau | Rate table note on sale contracts |
| Loan from a shareholder or another non-financial company | Not taxed | Rate table note on loan contracts |
| Bank loan to a small or micro enterprise | Exempt until 31 December 2027 | MOF/STA announcement 2023 No. 13 |
| Interbank lending | Not taxed | Rate table note on loan contracts |
| Pipeline transport contract | Not taxed | Rate table note on transport contracts |
| Reinsurance contract; life and health insurance | Not taxed (only property insurance is listed) | Rate table |
| Patent or know-how transfer | Transfer document at three per ten thousand, not a technology contract | Rate table |
| Legal, accounting or audit consulting | Not taxed | STA (89) Guoshuidizi No. 34 |
| Transfer of listed shares on an exchange | Securities stamp tax, seller only | Law Art. 3 |
| Transfer of shares in a private company | Transfer document, both parties | Rate table |
| Rural land contract or management rights | Not taxed | Rate table note |
| Housing lease by an individual (landlord or tenant) | Exempt | Caishui 2008 No. 24 |
| Head office and branch internal plans | Not taxed | MOF/STA announcement 2022 No. 22 Art. 2(4) |
| Contract never performed | Tax stands, no refund | MOF/STA announcement 2022 No. 22 Art. 3(7) |
| Contract amended to a lower amount | Refund or offset may be claimed | MOF/STA announcement 2022 No. 22 Art. 3(2) |
| Price for unpaid subscribed capital stated separately in a share transfer | Excluded from the base | MOF/STA announcement 2022 No. 22 Art. 3(4) |

## Worked cases ([Stamp Tax Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/yhs/202106/t458595.html); [rate table](https://guangdong.chinatax.gov.cn/gdsw/zssw_nsrwkt_sphg_zbsp/2022-07/08/b5cbcdef663d476bbcb821cb6ab21a8c/files/5e07417a94ab464895b4c817b3e75c5c.pdf); [MOF/STA announcement 2023 No. 12](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/202308/t468162.html); [MOF/STA announcement 2023 No. 39](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/yhs/202308/t468451.html); [Shanghai filing periods](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/yhs/202206/t463184.html))

All amounts are in yuan and relate to tax year 2026. The filing dates assume a Shanghai taxpayer. Other provinces set their own periods.

**Case 1: technology development contract.** A Shanghai software company, not a small business, signs a development contract on 10 March 2026. The remuneration is 1,000,000, and VAT is stated as a separate amount. Tax = 1,000,000 × 3 ÷ 10,000 = 300. If the contract instead showed a VAT-inclusive price of 1,060,000 and only a VAT rate, tax = 1,060,000 × 3 ÷ 10,000 = 318. The first quarter return is due within fifteen days after 31 March 2026.

**Case 2: office lease.** Two companies sign a 12-month lease at 10,000 a month, so the rent is 120,000. Each party pays 120,000 × 1 ÷ 1,000 = 120. If the tenant is a small low-profit enterprise, it pays half: 60. The landlord still pays 120.

**Case 3: account books.** A company is set up in January 2026 with paid-in capital of 1,000,000 and capital reserve of 500,000. Base = 1,500,000. Tax = 1,500,000 × 2.5 ÷ 10,000 = 375, filed in Shanghai with the annual return within fifteen days after 31 December 2026. If the company is a small low-profit enterprise, it pays half: 187.5. In 2027 it adds 1,000,000 of capital. Tax on the increase only = 1,000,000 × 2.5 ÷ 10,000 = 250 before any halving.

**Case 4: private company share transfer (the Shanghai bureau's own example).** Party A owns all of company A. Registered capital is 10,000,000, of which 5,000,000 is paid in. A sells the whole holding to B for 6,000,000. The agreement shows 5,500,000 for the paid-in part and 500,000 for taking over the unpaid obligation. The base is 5,500,000. Each party pays 5,500,000 × 5 ÷ 10,000 = 2,750. In Shanghai, transfer documents are filed per occurrence within fifteen days of signing.

**Case 5: listed shares.** An investor sells A-shares for 1,000,000 on 3 June 2026. Statutory tax = 1,000,000 × 1 ÷ 1,000 = 1,000. Charged at half since 28 August 2023, so 500 is withheld by the clearing body. The buyer pays nothing. The investor files nothing.

**Case 6: contract signed abroad.** A Hangzhou importer and a Japanese supplier with no agent in China sign an equipment sale contract in Tokyo for 200,000 US dollars. The equipment is used in Hangzhou. The buyer is in China, so the contract is taxable, and **both** signatories are taxpayers. At an assumed central parity of 7.1 on the signing day, the base is 1,420,000. Each party pays 1,420,000 × 3 ÷ 10,000 = 426. The importer files through its normal return. The supplier must file itself, because it has no agent in China. In Shanghai a foreign party files per occurrence, or may choose annual filing. Use the real central parity rate for the signing day.

**Case 7: mixed freight and warehousing.** A logistics contract has freight of 200,000 and warehousing fees of 50,000. Shown separately: 200,000 × 3 ÷ 10,000 = 60, plus 50,000 × 1 ÷ 1,000 = 50, total 110. Not shown separately: 250,000 × 1 ÷ 1,000 = 250.

**Case 8: amended sale contract.** A sale contract for 2,000,000 paid 2,000,000 × 3 ÷ 10,000 = 600. If it is amended to 2,500,000, extra tax = 500,000 × 3 ÷ 10,000 = 150. If it is instead amended to 1,500,000, the seller may claim a refund or offset of 500,000 × 3 ÷ 10,000 = 150. If it is simply not performed, nothing is refunded.

## When to refuse or refer

- The document does not clearly fit one item in the rate table and the choice changes the rate, for example a technology service contract that is really processing or repair work. Refer, with the contract, to the local bureau or a Chinese tax adviser.
- The client wants to rely on a targeted exemption that is not listed above. Get the announcement and check its end date and conditions first.
- An individual sells shares in a private company and wants the small-business halving. The Shanghai bureau said yes in December 2022 under the earlier relief (Caishui 2019 No. 13). This Guide found no later official statement under MOF/STA announcement 2023 No. 12, so check with the local bureau before claiming it.
- A restructuring relief depends on the tests under "Restructuring" above: the three permitted conversion forms, with continuing investors holding more than three quarters and the successor taking over rights and obligations; a merger with continuing investors; a division into companies with the same investors; or a State Council-approved debt-for-equity project. Refer for a full review of the deal.
- A trade on a venue whose status as a State Council-approved national securities venue is unclear. Confirm with the broker or clearing body whether securities stamp tax was withheld.
- The contract amount will not be known for a long time, or the parties dispute it. Report the signing now, and get advice on when the amount counts as settled.
- There are signs of a sham contract or a side agreement with a different price. Do not compute tax on a document you believe is false.
- The client has missed several periods, faces an audit, or asks about penalties beyond the basic rules below.
- Anything in Hong Kong, Macao or Taiwan.

## Filing and payment ([Stamp Tax Law Art. 13-17](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/yhs/202106/t458595.html); [STA announcement 2022 No. 14](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/yhs/202206/t463170.html); [Shanghai Tax Bureau announcement 2022 No. 3](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/yhs/202206/t463184.html); [Tianjin Tax Bureau e-tax guide, 2024](https://tianjin.chinatax.gov.cn/nsrxt/11200000000/0500/050011/20240722144157010.shtml); [Tax Collection Administration Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/swzsgl/200609/t284229.html))

**Periods (national rule).** Stamp tax is assessed quarterly, annually or per occurrence. Contracts and transfer documents may be filed quarterly or per occurrence. Account books may be filed annually or per occurrence. Foreign parties may file quarterly, annually or per occurrence. Each provincial bureau sets the actual periods (STA announcement 2022 No. 14 Art. 1(3)). There is no monthly period.

**Deadlines (Law Art. 16).** Quarterly or annual: within fifteen days after the end of the quarter or year. Per occurrence: within fifteen days after the tax point. Securities: the clearing body pays over weekly, within five days after each week ends. Check the local bureau's published tax calendar for the exact due date.

**Shanghai's choices** (Shanghai Tax Bureau announcement 2022 No. 3):
- contracts: quarterly; taxpayers who seldom sign contracts may choose per occurrence;
- transfer documents: per occurrence; frequent signers may choose quarterly;
- account books: annually;
- foreign parties: per occurrence, or annually if per-occurrence filing is impractical.

**Where to file (Law Art. 13-14).** A unit files where it is established. An individual files where the document was signed or where they live. A transfer of real estate is filed where the property is. A foreign party with an agent in China has the agent withhold. Without an agent, it files itself, at the place of asset delivery, where the Chinese service provider or recipient is, or where the Chinese signatory is. Real estate goes to where the property is (STA announcement 2022 No. 14 Art. 1(4)).

**How to file.** Record each document on the stamp tax source detail form (印花税税源明细表), then file through the combined property-and-behaviour tax return (财产和行为税合并申报) (STA announcement 2022 No. 14 Art. 1(1)). In the e-tax bureau: 我要办税 → 税费申报及缴纳 → 财产和行为税税源采集及合并申报, add 印花税, then enter sources one at a time or import them from the template. Tick the relevant relief code where a relief applies.

**How to pay (Law Art. 17).** Either by stamps (印花税票), which are affixed to the document and cancelled across the edge, or by filing and paying and receiving a tax payment certificate. Filing and paying is the norm for businesses.

**Late payment and penalties** (Tax Collection Administration Law):
- late payment: a surcharge of five per ten thousand of the unpaid tax for each day late (Art. 32);
- late filing: an order to correct and a fine of up to two thousand yuan, or two thousand to ten thousand yuan in serious cases (Art. 62);
- evasion (false or missing declarations to underpay): the tax, the surcharge, and a fine of half to five times the tax underpaid; crimes are prosecuted (Art. 63).

## Returns for tax year 2025 being filed or corrected now ([Stamp Tax Law Art. 16](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/yhs/202106/t458595.html); [MOF/STA announcement 2022 No. 22 Art. 3](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/yhs/202206/t463167.html))

The rates and rules for 2025 were the same as for 2026. The small-business halving and the securities halving both applied throughout 2025. Account-book tax for 2025 on an annual period was due within fifteen days after 31 December 2025, and the fourth-quarter 2025 contract return was due within fifteen days after the same date (check the local tax calendar for the exact day). If a 2025 document was missed, file it now for the period in which it was signed, pay the tax, and expect the daily late-payment surcharge. If a 2025 contract was later amended to a lower amount, claim the refund or offset for the decrease.

## Completion checklist ([Stamp Tax Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/yhs/202106/t458595.html); [MOF/STA announcement 2022 No. 22](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/yhs/202206/t463167.html); [MOF/STA announcement 2023 No. 12](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/202308/t468162.html))

- [ ] Each document matched to one rate-table item, or recorded as not on the list, with the reason.
- [ ] China link confirmed for documents signed abroad, and every taxpayer on the document identified, including foreign parties.
- [ ] Base = stated amount; VAT excluded only where stated as an amount; no-amount documents reported and taxed on settlement.
- [ ] Mixed items split, or the highest rate applied; each party's share fixed.
- [ ] Foreign currency converted at the signing-day central parity rate.
- [ ] Account books: only the increase over the last taxed capital-plus-reserve total.
- [ ] Exemptions checked (Law Art. 12, housing, small-enterprise loans, restructuring, offshore trade), with end dates.
- [ ] Small-business halving applied only with evidence of status, and never to securities stamp tax.
- [ ] Amendments since the last return: extra tax paid, or refund or offset claimed.
- [ ] Period, filing place and deadline confirmed against the local bureau's notice and tax calendar.
- [ ] Supporting papers for every relief kept on file.

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
