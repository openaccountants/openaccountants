from writer import *
for a,qs in [('128',[(4,12),(49,59),(65,69)]),('130',None),('131',[(4,14),(19,25)]),('132',None),('133',None),('135',None),('136',None),('137',None),('138a',None),('141',[(4,10)]),('143',[(4,16)]),('239',None),('240',[(4,23)])]:section('Social'+a,10,a,quotes=qs)
section('Social138',10,'138',1,151,[(4,22),(24,53),(69,75),(80,104),(114,149),(150,151)])
section('Social4',10,'4')
for a,lo,hi,qs in [('5',1,7,None),('19',19,27,None),('21',1,107,[(5,15),(17,39),(41,59),(61,107)]),('136a',1,4,None),('231',1,69,[(4,15),(35,46)]),('293gma',1,41,[(3,11),(21,26)])]:scope('Social'+a,10,EVID/f'shared/10-article-{a}.txt',lo,hi,'Act461/2003 §'+a,qs,'For293gma only(1)/(4) are adopted; former(2)/(3)/(5) displaced from1July by own293gnb.')
for a,lo,hi,qs in [('12',1,35,[(4,7),(27,35)]),('13',1,90,[(4,18),(45,58),(82,83)]),('13a',1,36,[(4,9),(25,36)]),('16',1,110,[(4,18),(27,38),(44,68),(95,110)]),('16a',1,33,None),('17',1,31,[(4,11)]),('18',1,30,[(4,11)]),('19',1,163,[(45,49),(127,131)]),('20',1,48,[(4,10),(34,42)]),('26',1,37,[(4,23)]),('38ezk',1,16,None),('38ezl',1,19,[(9,11)])]:
 scope('Health'+a,18,EVID/f'shared/18-article-{a}.txt',lo,hi,'Act580/2004 §'+a,qs)
# Actual-read intervals where unneeded material between them was not read.
scopes['Health19']['actual_read_ranges']=[[1,52],[123,163]];scopes['Health19']['read_mode']='Selected intervals actually read; LF53–122 not read for this ledger and not quoted.'
scope('SP.table',60,'sources/60.txt',30,266,'SP2026 contribution table and notes',[(38,67),(80,113),(127,157),(229,236),(254,266)])
scopes['SP.table']['actual_read_ranges']=[[30,157],[227,266]];scopes['SP.table']['read_mode']='Selected employee/employer/SZCO table and operative notes read; voluntary table/unused navigation excluded.'
scope('SP.pillar2',61,'sources/61.txt',200,203,'SP2026 item13, unchanged4% allocation',[(200,202)],'The January overview is not used for superseded July coverage rules.')
scope('MinimumWage2026',36,'sources/36.txt',62,67,'Ministry of Labour minimum wage2026',[(63,65)])
scope('Health.report-decree',23,'sources/23.txt',356,369,'Decree159/2018 §2(1)–(4)',[(356,368)])
scope('VszP.employer',66,'sources/66.txt',351,377,'VszP registration and monthly514 report',[(355,357),(366,366),(376,376)])
for a,lo,hi,qs in [('35',1,124,[(3,22),(47,60),(67,89),(95,124)]),('38',34,84,[(37,41),(43,48),(58,69),(75,84)]),('39',87,121,[(87,107),(110,121)]),('48',1,22,[(4,22)])]:section('ITA'+a+'.payroll',13,a,lo,hi,qs)
scope('FS.monthly', 't05','sources/t05.txt',21,26,'FS monthly Prehlad filing duty/tolerance',[(22,26)])
scope('SP.A1','u01','sources/u01.txt',281,506,'SP actual A1 application/instructions pp6–9',[(314,341),(344,354),(380,389),(396,411),(472,480),(486,502)],'Original-language official administrative instructions. Their nonbinding practical criteria are not silently converted to new absolute statutory numerical gates.')
# Additional current bodies retained by the earlier full review; raw identities are independent of its verdict.
fresh=ARCH/'final-full-pack-review/fresh'
for sid,name,url in [('SPJuly','sp-szco-july-current','https://www.socpoist.sk/nastroje-sluzby/kalkulacky/kalkulacky-pre-szco/kalkulacka-na-informativny-vypocet-poistneho-pre-5'),('SPOctober','sp-szco-october-current','https://www.socpoist.sk/news/v-oktobri-2026-dostane-takmer-92-tisic-zivnostnikov-szco-od-socialnej-poistovne-oznamenia-o'),('SPpartial','sp-partial-month-current','https://www.socpoist.sk/socialne-poistenie/platenie-poistneho/poistne-szco-dpo-po-prerusenom-poisteni'),('Social122','social-amendment-122','https://static.slov-lex.sk/pdf/SK/ZZ/2026/122/ZZ_2026_122_20260701.pdf')]:
 raw=fresh/(name+('.pdf' if sid=='Social122' else '.html'));receipts[sid]={'file':str(raw),'sha256':sha(raw),'url':url}
 scope(sid,sid,fresh/(name+'.txt'),71 if sid=='Social122' else 28 if sid in ['SPJuly','SPpartial'] else 26,211 if sid=='Social122' else 137 if sid=='SPJuly' else 90 if sid=='SPpartial' else 76,'Act122/2026 ArtI1–3/9+ArtII' if sid=='Social122' else 'SP current official '+sid,[(71,94),(96,140),(157,204),(208,211)] if sid=='Social122' else [(55,65),(74,82),(83,98),(112,135)] if sid=='SPJuly' else [(64,87)] if sid=='SPpartial' else [(41,75)])
CAT.write_text(json.dumps(scopes,ensure_ascii=False,indent=2)+'\n');render_sources()

scope('Social138c',10,'sources/10.txt',9219,9224,'§ 138c',[(9219,9224)],'Actual retained current provision read 2026-10-29; €300 monthly deduction limited to the lower assessment base.')

scope('Health10b',18,'sources/18.txt',3435,3494,'Health Act §10b(1)(a), (2)–(4)',[(3435,3466),(3480,3494)],'Employee health scope read separately from social insurance; intervening other-income categories3467–3479 read but not quoted.')
render_sources()

# Current administrative A1 observation retained by root; no direct EU-law acquisition claim.
A=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27/sk-ledger-independent-review-2026-10-29/root-SK-A1-current-source')
sid='SP.A1.current-admin'
receipts[sid]={'file':str(A/'official-tool-response.json'),'sha256':sha(A/'official-tool-response.json'),'url':json.loads((A/'source-observation.json').read_text())['official_url']}
scope(sid,sid,A/'official-selected-reader.txt',51,126,'Sociálna poisťovňa: current administrative one-state/work-state, multistate/A1 and Article16 guidance',[(51,51),(119,121),(124,126)],'Retained official web-tool response JSON acquired/read by root; this writer actually read physical LF51–52,119–126. Web labels are one less than physical LF. This is administrative guidance, not the direct text of Regulation883. Failed EUR-Lex robot receipts remain failed acquisitions.')
scopes[sid]['actual_read_ranges']=[[51,52],[119,126]]
scopes[sid]['source_kind']='Retained official web-tool response JSON, not original HTML or direct EU regulation'
CAT.write_text(json.dumps(scopes,ensure_ascii=False,indent=2)+'\n');render_sources()
