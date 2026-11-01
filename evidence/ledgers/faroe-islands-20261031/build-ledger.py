from pathlib import Path
import subprocess,json,hashlib
r=Path(__file__).resolve().parents[3]; p=Path(__file__).resolve().parent
sources=json.loads((p/'sources.json').read_text());urls={x['name']:x['url'] for x in sources}
form='https://taks.cdn.fo/media/1938/v01-skr%C3%A1setingarskjal-til-vinnuskr%C3%A1nna-161220.pdf?s=5Yrnkhknbc6vaTXl_Pu3BDPa7b8'
reg='https://taks.cdn.fo/media/2583/veglei%C3%B0ing-til-skr%C3%A1setingarskjali%C3%B0-til-vinnuskr%C3%A1nna-v01-091220.pdf?s=DItd4f8Ry-pMJPvdHTj67_QvgYo'
rows=[];lines=(p/'sources/payroll-levy.reader.txt').read_text().splitlines()
specs=[
('Who this applies to','§1(1)',305,308,'Enumerated paid healthcare, insurance, finance and necessary electronic-service activities; not all exempt businesses.'),
('Who this applies to','§1(2)',309,309,'Express named-institution exceptions, not a purpose-based extension.'),
('Who this applies to','§§1–5',305,320,'No MVG small-sales threshold appears in this levy charging/base text; mixed activities separately allocated.'),
('Rates, bands and thresholds','§4(1)',315,315,'Healthcare 2.5%.'),
('Rates, bands and thresholds','§4(2)',316,316,'Insurance 10%; finance including specified electronic services 12%.'),
('Rates, bands and thresholds','§6(1)–(3)',322,324,'Quarterly period and 25% provisional B-income component.'),
('Rates, bands and thresholds','§6(7)',328,328,'Below DKK50 payment may be waived, not automatic exemption.'),
('Rates, bands and thresholds','§7(6)',336,336,'Below DKK50 annual refund not paid.'),
('The base','§5(1)',317,317,'Healthcare paid A-wages plus taxable business profit or minus taxable business loss.'),
('The base','§5(2)',318,318,'Insurance/finance paid A-wages only, no healthcare profit component.'),
('The base','§5(3)',319,319,'Benefits in kind included to extent giving holiday compensation entitlement.'),
('The base','§5(4)',320,320,'Mixed activities split wages and profit/loss by business division; no statutory turnover safe harbour supplied.'),
('The base','§§6(3),7(1)',324,330,'Provisional base and final annual reconciliation distinguished.'),
('Deadlines and filing','§§2,3(1)',310,311,'TAKS registration and registration notice.'),
('Deadlines and filing','§3(2)',312,312,'Registration eight days before start; changes eight days after change.'),
('Deadlines and filing','§6(2)',323,323,'Provisional demand within seven days of quarter end.'),
('Deadlines and filing','§6(4)',325,325,'Ordinary quarterly payment one month and ten days after end, including Q2 10August.'),
('Deadlines and filing','§6(6)',327,327,'Saturday/Sunday/holiday last timely date moves to first working day.'),
('Deadlines and filing','§§9–10',341,348,'Short duration/nonpayment/insolvency shortening powers; specific demand considered.'),
('Deadlines and filing','§7(1)',330,331,'Annual reconciliation and exact original final-demand phrase; detailed date interpretation remains open.'),
('Deadlines and filing','§7(2)',332,332,'Timely return overpayment refund within three weeks of last timely submission date.'),
('Deadlines and filing','§7(3)–(6)',333,336,'Inspection obstruction suspends refund period, previous returns required, earlier debts offset, minimum payout.'),
('Penalties and interest','§6(5)',326,326,'0.7% each commenced month from due date, including booked interest.'),
('Penalties and interest','§8',339,340,'Late return 1% min300 max1000, special-circumstances waiver.'),
('Penalties and interest','§11(1)',349,349,'Correction underpayment payable within14days of demand.'),
('Penalties and interest','§11(2)',350,350,'Estimated base on missing return/inadequate accounts.'),
('Penalties and interest','§11(3)',351,351,'DKK50 reminder-letter fee.'),
('Penalties and interest','§12',352,352,'Operator liability; foreign representative and business joint liability.'),
('Penalties and interest','§18',366,371,'Intentional/gross negligence fines, evasion maximum2years, no fixed fine invented.'),
('Cross-border points','§3(3)',313,313,'Foreign local representative, only extent of Hoyvík treaty exception.'),
('Sources','Title/commencement',294,296,'Current consolidation title through31/2023.'),
]
for heading,article,a,b,claim in specs:
 quote='\n'.join(lines[a-1:b]);rows.append(dict(id=f'PL-{len(rows)+1:03}',section=heading,claim=claim,act_article='Payroll Levy Act193/1993 '+article,url=urls['payroll-levy'],read_date='2026-10-31',source_file='sources/payroll-levy.reader.txt',reader_lines=[a,b],original_language_quote=quote,kind='statute'))
pay=(p/'sources/payment-agreements.reader.txt').read_text().splitlines()
for needle,claim in [ ('Ein gjaldsavtala','Payment agreement viaTAKS,bank orhomebank.'),('Fyll út og send','Two official business payment agreement applications.'),('51087485LA:','PBS5108748,debtorgroup5,typeLA,GS BO+LA+Vtal+00000; neveruse sample taxpayer id.')]:
 matches=[(i+1,x) for i,x in enumerate(pay) if needle in x];assert matches,needle
 i,q=matches[0];rows.append(dict(id=f'PL-{len(rows)+1:03}',section='Deadlines and filing',claim=claim,act_article='TAKS business payment agreement guidance',url=urls['payment-agreements'],read_date='2026-10-31',source_file='sources/payment-agreements.reader.txt',reader_lines=[i,i],original_language_quote=q,kind='official guidance'))
registration=[('Section1','Businessname/addressandidentity','Her verður upplýst, hvør skal skrásetast í vinnuskránni, t.e. navn, bústaður o.s.fr.'),('Section2','Actualactivitystartdate','Byrjanardagur er tann dagur, tá ið farið verður undir virksemið, sama um fólk er sett í starv ella ikki.'),('Section3','Levyandstartdateseparateobligation','Her skal boðast frá, um virkið er mvg-skyldigt ella lønhæddaravgjaldsskyldigt, og nær skyldan byrjar.'),('Signature','Authorisedsignatureandattachments','Skrásetingarskjalið skal undirskrivast av stjóra felagsins ella teimum, sum hava tekningarrætt. Viðtøkur,\neigarabók, avrit av fráboðan um nýskráseting frá Skráseting Føroya og stovningarsamtykt skulu leggjast við.')]
for article,claim,q in registration:
 assert q in (p/'sources/registration-guidance.web-extract.txt').read_text()
 rows.append(dict(id=f'PL-{len(rows)+1:03}',section='Deadlines and filing',claim=claim,act_article='TAKS V01 guidance '+article,url=reg,read_date='2026-10-31',source_file='sources/registration-guidance.web-extract.txt',original_language_quote=q,kind='official guidance PDF read through web tool; selected exact-text extract, raw PDF not preserved'))
formquotes=[('V01 section4','Entitytypeattachmentsandsoletrader/partnershipplan','Fyriliggja skal:\nRakstrarætlan*)\nFyriliggja skulu:\nRakstrarætlan*),\níognarsáttmáli'),('V01 section5','Detailedactivityandprincipalactivity','5. Ítøkilig frágreiðing um, hvat virkið ger (Skal ásetast)'),('V01 section8','Staffidentityandrights','Niðanfyristandandi starvsfólk skulu hava fylgjandi rættindi til Vinnugluggan:'),('V01 section9','AccountantaccessVG03','Nummarið er VG03.'),('V01 page2','Securesubmission','Send umsóknina um álítandi postskipan til taks@taks.fo ella lat okkum hana á annan tryggan hátt.')]
for article,claim,q in formquotes:
 rows.append(dict(id=f'PL-{len(rows)+1:03}',section='Deadlines and filing',claim=claim,act_article='TAKS '+article,url=form,read_date='2026-10-31',source_file='sources/V01.web-extract.txt',original_language_quote=q,kind='official current-listed form PDF read through web tool; selected exact-text extract, raw PDF not preserved'))
(p/'fo-payroll-levy.rows.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
md=['# Faroe payroll levy: complete figure/rule ledger','', 'Read date:2026-10-31. New job, no prior Guide rewritten. Every factual legal rule is mapped below. All example money/wage/profit/allocation amounts are fictional inputs, not statutory thresholds. Derived results are arithmetic only. No accountant attestation or whole-country completeness is asserted.','', '| ID | Guide section and rule | Act/article and officialURL | Exact original-language quote | Read |','|---|---|---|---|---|']
for x in rows:md.append('| '+x['id']+' | '+x['section']+': '+x['claim']+' | '+x['act_article']+' '+x['url']+' | '+x['original_language_quote'].replace('\n',' / ').replace('|','\\|')+' | '+x['read_date']+' |')
md+=['','## Derived example controls','','Example1:fictional wages800000,profit400000,provisionalB300000. Quarter=(800000/4+300000/4)*.025=6875;annualprovisional27500;finalbase1200000;tax30000;shortfall2500.','','Example2:fictional wages1000000,insurance.10=>100000;finance.12=>120000;difference20000;directlyallocatedfinancewages300000=>36000. Profit600000 deliberatelynotused inwage-only bases.','','## Old-topic destinations','','This is a new job. No old payroll/social or MVG rule is moved or deleted. All eight existing Guides preserve their complete old substantive text. Table citation targets are expanded to inline URLs; formation gains canonical parent headings, two examples and client questions. The complete 1,520 old nonblank-unit destinations and exact transformations are in preservation.json. All310 historical evidence files are relocated byte-exact to evidence/ledgers/.','','## Read scope and limits','','Writer read own Act193/1993 §§1–21 and amendment footnotes through31/2023; current TAKS payment agreement body and LA row; current TAKS starting-business body; current forms listing through normal browser; original official V01 PDF both pages and guidancePDF allfourpages through webtool. CurrentCDN PDF links returned404 throughweb and browser produced no readablepixels; original officialCDN PDFs supplied readabletext. No original PDF bytes are claimed for these two extracts. No formal submission/contact/payment occurred.','','Not yet confirmed:healthcare loss exceeding wages; unsupported mixed allocation; disputed-demand amendment screens; precise final-demand calendar interpretation; fixed criminal fine practice. Country ordinary gaps and additional statutory tax jobs remain open.']
(p/'fo-payroll-levy.md').write_text('\n'.join(md)+'\n')
subprocess.run(['python3',str(p/'check-preservation.py')],cwd=r,check=True)
print('ledger rows',len(rows))
