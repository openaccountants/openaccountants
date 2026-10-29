from writer import *
for key,name,lo,hi,article,qs in [
 ('ITA1.treaty','13-article-1.txt',1,14,'§1(2)',[(6,14)]),
 ('ITA17f.exit','13-article-17f.txt',1,84,'§17f',[(4,17),(36,59),(61,84)]),
 ('ITA17g.instalments','13-article-17g.txt',1,57,'§17g',[(4,20),(22,45),(46,56)]),
 ('ITA43a.challenge','13-article-43a.txt',1,24,'§43a',[(4,17)])]:scope(key,13,EVID/'shared'/name,lo,hi,article,qs)
section('ITA16.source',13,'16',1,114,[(4,15),(24,74),(76,101),(103,114)])
section('ITA16.PE',13,'16',115,154,[(115,142),(143,154)])
section('ITA13.EU-interest',13,'13',50,70,[(50,70)])
section('ITA13.EU-royalty',13,'13',74,113,[(74,94),(109,113)])
section('ITA12.dividends',13,'12',40,55,[(46,55)])
section('ITA43.nonresident',13,'43',1,104,[(4,20),(24,38),(84,104)])
section('ITA43.credit-election',13,'43',137,166,[(137,162)])
section('ITA43.collection',13,'43',170,231,[(170,175),(190,195),(205,216),(228,231)])
section('ITA43.EU-refund',13,'43',316,325,[(317,325)])
section('ITA43.unknownBO',13,'43',349,371,[(364,371)])
section('ITA44.security',13,'44')
section('ITA2.BO',13,'2',227,233,[(227,233)])
scope('MF.cooperation2026',56,'sources/56.txt',1,872,'Official §2(x) cooperating-state list, effective1January2026',[(3,15),(407,410),(800,807)],'All138 numbered entries actually read. Totals138/71 treaty-labelled entries and absence of Russia are computed inventory observations, not quoted invented sentences; full native table remains retained. List membership does not establish operative treaty articles.')
render_sources()
