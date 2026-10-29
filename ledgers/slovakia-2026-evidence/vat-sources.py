from writer import *
def sec(k,a,qs,lo=1,hi=None):return section(k,17,a,lo,hi,qs)
sec('VAT27.rates','27',[(4,10),(12,29),(35,38)])
for k,a,qs in [('VAT4.status','4',[(3,38),(40,60),(69,99),(96,118),(119,151),(151,170),(183,187)]),('VAT5.foreign','5',[(3,41),(43,77)]),('VAT7.goods','7',[(3,20)]),('VAT7a.services','7a',[(3,20)]),('VAT11.acquisitions','11',[(3,36),(37,52),(71,105)]),('VAT15.services','15',[(3,23)]),('VAT4a.group','4a',[(3,20)]),('VAT4b.group','4b',[(3,18),(18,37),(39,52)]),('VAT22.base','22',[(3,14)]),('VAT24.import','24',[(3,30)]),('VAT25.notes','25',[(3,24),(40,56)]),('VAT49.deduction','49',[(3,10),(11,24),(25,74)]),('VAT50.coefficient','50',[(3,36)]),('VAT51.documents','51',[(3,29)]),('VAT69.reverse','69',[(3,43),(47,94),(115,130)]),('VAT77.period','77',[(3,30)]),('VAT78.return','78',[(3,49),(65,70)]),('VAT78a.control','78a',[(3,16),(23,45),(61,75),(122,154)]),('VAT79.refund','79',[(3,40),(47,74)]),('VAT80.EC','80',[(3,42),(75,105)]),('VAT84a.import','84a',[(3,40)]),('VAT85n.vehicles','85n',[(3,35),(37,67),(80,107)]),('VAT52a.capital','52a',[(3,21)]),('VAT54.capital','54',[(15,26),(36,66)]),('VAT53.notes','53',[(3,22)])]:sec(k,a,qs)
for k,a,lo,hi,qs in [('VAT5a.number','5a',1,11,[(3,11)]),('VAT8.gifts','8',1,37,[(21,28)]),('VAT9.private','9',1,29,[(3,29)]),('VAT10.transfer','10',1,21,[(3,14)]),('VAT28.post','28',1,4,[(3,4)]),('VAT29.health','29',1,23,[(3,23)]),('VAT31.education','31',1,15,[(3,15)]),('VAT39.finance','39',1,41,[(3,28)]),('VAT41.gambling','41',1,11,[(3,11)]),('VAT43.EU','43',1,30,[(3,12),(25,30)]),('VAT46.transport','46',1,20,[(3,20)]),('VAT47.export','47',1,43,[(3,19),(40,43)]),('VAT54a.property','54a',1,33,[(3,18)]),('VAT54d.firstuse','54d',1,31,[(3,31)]),('VAT55.initial','55',1,22,[(3,15)]),('VAT68cb.smallimport','68cb',1,13,[(3,7)]),('VAT68f.foreignSME','68f',1,84,[(3,28),(56,71)]),('VAT68g.domesticSME','68g',70,123,[(87,106),(112,123)]),('VAT69a.representative','69a',1,61,[(3,18),(32,39),(59,61)]),('VAT70.records','70',1,55,[(3,14),(45,55)]),('VAT72.invoice','72',1,53,[(27,30)]),('VAT73.deadline','73',1,23,[(3,23)]),('VAT74.wording','74',1,89,[(3,39),(53,57)]),('VAT76.retention','76',1,42,[(3,26)]),('VAT81.dereg','81',1,75,[(2,14),(29,37),(60,68)]),('VAT82.dereg','82',1,20,[(2,20)]),('VAT85kn.oldtransition','85kn',1,16,[(1,4)]),('VAT85kp.capitaltransition','85kp',1,13,[(3,13)])]:scope(k,17,EVID/f'shared/17-article-{a}.txt',lo,hi,'VAT222/2004 §'+a,qs)
# Sparse actual reads above must not imply unread intervening paragraphs.
scopes['VAT68f.foreignSME']['actual_read_ranges']=[[1,28],[48,84]]
scopes['VAT68g.domesticSME']['actual_read_ranges']=[[70,106],[112,123]]
scopes['VAT69a.representative']['actual_read_ranges']=[[1,44],[58,61]]
scope('VAT2024.rates',16,EVID/'shared/16-article-27.txt',1,34,'Historical2024 VAT§27',[(3,27),(31,33)])
scope('VAT2024.registration',16,EVID/'shared/16-article-4.txt',1,58,'Historical2024 VAT§4',[(3,20)],'Historical rule only; not the 2026 threshold/deadline.')
scope('TC27.weekend',20,EVID/'shared/20-article-27.txt',1,25,'TaxCode563/2009 §27',[(13,16)])
scope('VAT.annex7.services',8,'sources/08.txt',1,51,'VAT Annex7a points1–2',[(10,40)])
for k,lo,hi,qs in [('VAT.annex7.goods19',1,189,[(6,12),(66,69),(107,108)]),('VAT.annex7.goods5',190,355,[(219,245)])]:scope(k,9,'sources/09.txt',lo,hi,'VAT Annex7 points1–3',qs)
scope('FS.VATrates',54,'sources/54.txt',39,65,'FS current VAT rates page §27',[(40,40),(57,60)])
scope('FS.EC.fineclass',44,'sources/44.txt',447,459,'FS2018 EC-sales methodology §6, classification only',[(448,452)],'Historical method supports j/e classification only; obsolete monetary range is not adopted. Current range comes from current TaxCode155.')
for k,lo,hi,qs in [('FS.registration.turnover',90,208,[(97,105),(163,181),(205,208)]),('FS.registration.decision',293,352,[(330,341)]),('FS.registration.voluntary',367,451,[(367,393),(406,441)])]:scope(k,45,'sources/45.txt',lo,hi,'FS2/DPH/2025/MP, current registration method',qs)
scope('FS.VATnumber',62,'sources/62.txt',148,160,'Official Vero VAT identifier formats, Slovakia',[(152,154)])
scope('Forms.VATcatalog', 's00','sources/s00.txt',219,280,'Official current form catalog',[(219,226),(272,280)])
scopes['Forms.VATcatalog']['actual_read_ranges']=[[219,226],[272,280]]
scope('Form.REGDPv24','t00','sources/t00.txt',1,246,'Official REGDPv24 form589, core and Annex1',[(2,6),(14,26),(184,246)],'Actual selected core and complete Annex1 read. Country dropdown contents are not statutory country eligibility claims.')
scopes['Form.REGDPv24']['actual_read_ranges']=[[1,49],[78,111],[151,246]]
scope('Form.KVDPHv25','t01','sources/t01.txt',1,218,'Official KVDPHv25 form607',[(1,14),(29,48),(70,103),(116,147),(169,206)],'Actual whole form reader read; duplicated interactive fields preserved literally.')
scope('Form.DPHv25','s04','sources/s04.txt',51,296,'Official DPHv25 form v.2025',[(51,121),(122,180),(181,229)],'Actual full reader51–296 read; page2/3 cached PNGs visually read to resolve multicolumn extraction. Coordinates are form fields, not statutory figures.')
CAT.write_text(json.dumps(scopes,ensure_ascii=False,indent=2)+'\n');render_sources()

scope('TC154.registration',20,scopes['TC154.return-duty']['reader_path'],13,14,'TaxCode §154(1)(b)',[(13,14)])
scope('VAT2024.goods-decision',16,'sources/16.txt',2446,2451,'Historical 2024 VAT §7(3)',[(2446,2451)],'Historical seven-day decision only, not the 2026 rule.')
scope('VAT2024.services-decision',16,'sources/16.txt',2468,2473,'Historical 2024 VAT §7a(3)',[(2468,2473)],'Historical seven-day decision only, not the 2026 rule.')
render_sources()
