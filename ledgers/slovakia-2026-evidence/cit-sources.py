from writer import *
for k,a,lo,hi,qs in [('ITA17.accounts','17',1,22,[(4,18)]),('ITA17.paid','17',378,427,[(386,414)]),('ITA17.pre-adjustment','17',600,603,[(600,603)]),('ITA21.disallow','21',1,65,[(3,7),(28,38),(54,58)]),('ITA22.assets','22',1,115,[(4,13),(69,77)]),('ITA19.VAT','19',303,311,[(303,311)]),('ITA25.VAT','25',59,69,[(59,69)]),('ITA30c.pointer','30c',1,20,[(4,15)]),('ITA52zzr.interest','52zzr',1,5,[(3,5)]),('ITA52zzzf.assets','52zzzf',1,13,[(4,13)]),('ITA51eb.scope','51eb',1,6,[(4,6)])]:scope(k,13,EVID/f'shared/13-article-{a}.txt',lo,hi,'§ '+a,qs)
section('ITA26.depreciation',13,'26',1,83,[(4,33),(70,83)])
section('ITA27.straight',13,'27',1,36,[(4,36)])
section('ITA42.advances',13,'42',1,103,[(4,29),(58,79)])
section('ITA46b.minimum',13,'46b',1,92,[(4,36),(38,76)])
section('ITA17k.complete',13,'17k',1,94,[(4,14),(16,45),(47,61),(63,77),(79,94)])
section('ITA21a.complete',13,'21a',1,23,[(4,23)])
scope('ITA105b.entities',13,'sources/13.txt',15524,15528,'Footnote105b, incorporated by §§17k/21a')
scope('FTT6.pointer',25,'sources/25.txt',532,547,'Act279/2024 §6–7',[(534,543)])
scope('TopUp3.scope',24,'sources/24.txt',1315,1331,'Act507/2023 §3(1)–(2)',[(1318,1331)])
ann=ARCH/'final-full-pack-review/fresh/cit-annex1.pdf';receipts['CITannex']={'file':str(ann),'sha256':sha(ann),'url':'https://static.slov-lex.sk/pdf/prilohy/SK/ZZ/2003/595/20260101_5740211-2.pdf'}
for k,lo,hi,qr in [('CITannex.cars',1,56,[(4,10),(39,39),(52,56)]),('CITannex.furniture-improvements',114,132,[(117,117),(126,130)]),('CITannex.buildings',181,201,[(184,198)])]:scope(k,'CITannex',ann.with_suffix('.txt'),lo,hi,'ITA Annex1 selected actual CPA/KS entries',qr,'Original PDF text extraction has visible encoding artifacts; literal quotation retained, not silently normalized. Numeric codes and vehicle certificate condition read in context.')
raw=ARCH.parent/'sk-ordinary-completion/independent/fs-thin-cap.html';receipts['thinFAQ']={'file':str(raw),'sha256':sha(raw),'url':'https://podpora.financnasprava.sk/663968-Pravidl%C3%A1-n%C3%ADzkej-kapitaliz%C3%A1cie-'}
scope('FS.thin-negative','thinFAQ',EVID/'shared/fs-thin-cap.txt',48,51,'Financial Administration low-capitalisation FAQ5',[(48,51)],'Derived reader uses HTMLParser handle_data in document order; exact raw preserved. Only this actual Q5 scope read, not every FAQ.')
forms=ARCH.parent/'sk-income-forms-completion/independent'
for sid,name,url in [('Cform','forms--DPPOv26 v1.13_vzor','https://www.mfsr.sk/files/archiv/66/prispevok_16.zip'),('Cinstruction','instructions--Poučenie DPPO_2026','https://www.mfsr.sk/files/archiv/36/prispevok_18.zip')]:
 raw=forms/(name+'.pdf');receipts[sid]={'file':str(raw),'sha256':sha(raw),'url':url}
def f(k,sid,name,lo,hi,qs):scope(k,sid,forms/(name+'.txt'),lo,hi,'Actual DPPOv26 '+k,qs,'Actual archive member PDF and reader hashes identify the form/instructions. Only selected native ranges read; field numbers are form coordinates, not new statutory amounts.')
for k,lo,hi,qs in [('C.adjustments',70,205,[(73,88),(110,115),(159,178),(186,205)]),('C.minimum-settlement',211,282,[(211,242),(256,282)]),('C.tableA-B',315,383,[(341,343),(357,358),(369,375)]),('C.loss',436,546,[(467,483),(501,524),(526,546)]),('C.tableK-L',709,801,[(709,734),(741,747),(800,801)]),('C.attachments',1098,1144,[(1121,1124)])]:f(k,'Cform','forms--DPPOv26 v1.13_vzor',lo,hi,qs)
f('C.instructions-vintage','Cinstruction','instructions--Poučenie DPPO_2026',1,54,[(1,14),(25,30)])
f('C.instructions-payment','Cinstruction','instructions--Poučenie DPPO_2026',600,640,[(614,640)])
render_sources()
scope('ITA17.accounts',13,EVID/'shared/13-article-17.txt',1,48,'§17(1)–(2)',[(4,18),(28,39)])
section('ITA30.loss-CIT',13,'30',1,None,[(4,16),(17,28)])
section('ITA15.corporate',13,'15',46,65,[(46,65)])
scopes['ITA15.corporate']['read_date']=DATE
section('ITA12.nonprofit-scope',13,'12',1,38,[(14,32)])
section('ITA52zzzj.CIT',13,'52zzzj',1,18,[(6,9),(16,18)])
CAT.write_text(json.dumps(scopes,ensure_ascii=False,indent=2)+'\n');render_sources()
