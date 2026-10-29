from writer import *
# Every expanded quotation below is an actually read retained operative scope.
scope('VAT68g.domesticSME',17,EVID/'shared/17-article-68g.txt',1,123,'VAT§68g(1)/(2)/(8)/(9)',[(4,16),(87,106),(112,123)])
scopes['VAT68g.domesticSME']['actual_read_ranges']=[[1,30],[70,106],[112,123]]
scope('VAT.annex7.goods5',9,'sources/09.txt',109,355,'VAT Annex7 points2–3',[(109,129),(134,155),(174,189),(208,218),(219,245)])
scope('FS.VAT2026foods',54,'sources/54.txt',92,116,'FS current2026 changes under Acts261/2025 and385/2025',[(92,103)])
scope('TC79.overpayment',20,EVID/'shared/20-article-79.txt',1,53,'TaxCode79(1)/(2)/(7)',[(3,12),(46,48)])
scope('Form.DPHv25', 's04','sources/s04.txt',51,296,'OfficialDPHv25 prescribed form',[(51,121),(122,180),(181,229),(230,296)],'Actual reader51–296 read; actual cached page2/3 PNGs visually read to disambiguate multicolumn layout. All field references are form coordinates, not tax constants.')
b=ARCH.parent/'sk-monthly-prehlad-sanction-research';r=json.loads((b/'source-receipts.json').read_text());rec=next(x for x in r if x['file'].endswith('bratislava-prehlad-decision-2025.pdf'));receipts['historicaldecision']={'file':rec['file'],'sha256':rec['sha256'],'url':rec['url']}
scope('Decision2025.monthly','historicaldecision',b/'bratislava-prehlad-decision-2025.txt',1,77,'Bratislava individual decision104440104/2025 dated28October2025',[(4,5),(26,34),(42,63)],'Historical individual facts/classification/payment clock only. Actual30–3000 is historical2025 range, not general2026 tariff. Printed appeal paragraph does not establish actual finality date.')
# Sparse-range display is literal and visibly distinct from bounding range.
CAT.write_text(json.dumps(scopes,ensure_ascii=False,indent=2)+'\n');render_sources()
