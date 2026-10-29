from pathlib import Path
from html.parser import HTMLParser
import json,re,hashlib,subprocess
O=Path(__file__).resolve().parent;D=Path('/Users/michaelcutajar/Downloads/oa-f1-wt/sources/DE')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
class Reader(HTMLParser):
 def __init__(s):super().__init__();s.buf=[];s.out=[];s.skip=0
 def handle_starttag(s,t,a):
  if t in ['script','style']:s.skip+=1
  if t in ['div','p','tr','h1','h2','h3','li','br']:s.flush()
 def handle_endtag(s,t):
  if t in ['script','style']:s.skip-=1
  if t in ['div','p','tr','h1','h2','h3','li']:s.flush()
 def handle_data(s,d):
  if not s.skip:s.buf.append(d)
 def flush(s):
  t=' '.join(''.join(s.buf).split());s.buf=[]
  if t:s.out.append(t)
C=json.loads((O/'source-candidate-catalog.json').read_text());M=json.loads((O/'selected-existing-evidence-map.json').read_text())
manual={'brkg_2005':'brkg','svbezgrv_2026':'svbezgrv-2026','rvbeitrsbek_2026':'rvbeitrsbek-2026','aufag':'aag','pbav_2025':'pbav-2025','milov5':'milov5','milov4':'milov4','de_v':'deuev','muschg_2018':'muschg','entgbv':'ebv','invstg_2018':'invstg','aoeg_1977':'egao-97','svev':'svev-full'}
explicit={
 'https://www.recht.bund.de/bgbl/1/2024/108/VO.html':'bgbl-2024-I-108-20261024.pdf',
 'https://www.recht.bund.de/bgbl/1/2024/108/regelungstext.pdf':'bgbl-2024-I-108-20261024.pdf',
 'https://www.recht.bund.de/bgbl/1/2025/363/VO.html':'bgbl-2025-I-363-20261024.pdf',
 'https://www.recht.bund.de/bgbl/1/2026/14/VO.html':'bgbl-2026-I-14-20261024.pdf',
 'https://www.recht.bund.de/bgbl/1/2026/197/VO.html':'bgbl-2026-I-197-20261024.pdf',
 'https://www.recht.bund.de/bgbl/1/2023/240/regelungstext.pdf':'bgbl-2023-I-240-20261026.pdf',
 'https://www.recht.bund.de/bgbl/1/2025/278/regelungstext.pdf?__blob=publicationFile&v=3':'svbezgrv-2026-20261024.pdf',
 'https://www.bundesgesundheitsministerium.de/beitraege':'bmg-beitraege-20261024.html',
 'https://www.berlin.de/politik-und-verwaltung/rundschreiben/download.php/4330060':'berlin-rs-4330060-20261024.pdf',
 'https://www.minijob-zentrale.de/DE/die-minijobs/minijob-mit-verdienstgrenze':'mjz-verdienstgrenze-20261024.html',
 'https://www.minijob-zentrale.de/DE/die-minijobs/midijob':'mjz-midijob-20261024.html',
 'https://www.gesetze-im-internet.de/ksabg2026v/BJNR0DC0A0025.html':'ksabg2026v-20261026.html',
 'https://www.bundesfinanzministerium.de/Content/DE/FAQ/FAQ-zur-Aktivrente.html':'bmf-aktivrente-faq-20261024.html',
 'https://www.elster.de/eportal/helpGlobal?themaGlobal=help_est_ufa_10_2025':'elster-anlv-help-2025-20261024.html',
 'https://www.elster.de/eportal/helpGlobal?themaGlobal=help_est_ufa_10_2026':'elster-anlv-help-2026-20261024.html',
 'https://www.destatis.de/DE/Presse/Pressemitteilungen/2026/10/PD26_369_712.html':'destatis-pd26-369-20261024.html',
 'https://stadt.muenchen.de/service/info/gewerbesteuer/1074725/':'muenchen-gewst-20261024.html',
 'https://www.bsg.bund.de/SharedDocs/Entscheidungen/DE/2018/2018_03_14_B_12_KR_13_17_R.html':'bsg-b12kr1317r-20261024.html',
 'https://www.bsg.bund.de/SharedDocs/Verhandlungen/DE/2026/2026_07_23_B_12_BA_10_24_R.html':'bsg-b12ba1024r-20261024.html',
 'https://lsth.bundesfinanzministerium.de/lsth/2026/B-Anhaenge/Anhang-24/IV/IV-6/anhang-24-IV-6.html':'lsth2026-anh24-IV-6-20261024.html',
 'https://lsth.bundesfinanzministerium.de/lsth/2026/A-Einkommensteuergesetz/II-Einkommen-2-24b/4-Ueberschuss-d-Einnahmen-ueber-die-Werbungsk-8-9a/Paragraf-8/r-8-1-9.html':'lsth2026-r8-1-9-20261024.html',
 'https://lsth.bundesfinanzministerium.de/lsth/2026/B-Anhaenge/Anhang-24/IV/IV-1/anhang-24-IV-1.html':'lsth2026-anh24-IV-1-20261024.html',
 'https://lsth.bundesfinanzministerium.de/lsth/2026/B-Anhaenge/Anhang-23a/inhalt.html':'lsth2026-anh23a-20261024.html',
 'https://esth.bundesfinanzministerium.de/esth/2024/C-Anhaenge/Anhang-30/II/anhang-30-II.html':'esth-2024-anh30-II-20261024.html',
}
for g in M:
 for u in g['cited_URLs']:
  if u in C or u.startswith('https://www.openaccountants'):continue
  p=None
  if u in explicit:p=D/explicit[u]
  elif 'bundesfinanzministerium.de/' in u and '.pdf' in u:
   name=u.split('/')[-1].split('?')[0];p=D/name
   if not p.exists():
    specs={'steuern-von-a-z':'bmf-steuern-a-z-20261024.pdf','2026-09-01-anlage-EUER-2026':'bmf-euer-2026-20261026.pdf','2025-12-05-steuerliche-behandlung-reisekosten-2026':'bmf-reisekosten-2026-20251205.pdf','2025-11-12-PAP-2026-anlage-1':'pap-2026-anlage1-20261024.pdf','2025-01-22-geaenderte-PAP-2025-anlage-1':'pap-2025-geaendert-20261024.pdf','2025-05-21-anwendungsschreiben-7b-estg-neu':'bmf-7b-20250521.pdf','2025-11-05-gle-aufhebung-gle-01-10-20-anl':'bmf-gle-20251105.pdf','2025-12-22-verpflegungsdienstleistungen':'bmf-verpflegung-20251222.pdf','2025-10-15-einfuehrung-obligatorische-e-rechnung':'bmf-erechnung-20251015.pdf','2025-12-29-vordruckmuster-USt-voranmeldung-2026':'bmf-ustva-vordruck-2026-20251229.pdf'}
    p=next((D/v for k,v in specs.items() if name.startswith(k)),None)
  elif 'bmf-abgelt' in u or '2025-05-14-einzelfragen-zur-abgeltungsteuer' in u:p=D/'bmf-abgeltungsteuer-20250514.html'
  elif 'gesetze-im-internet.de/' in u:
   m=re.search(r'de/([^/]+)/([^/?]+)',u)
   if m:
    act,a=m.groups();stem=manual.get(act,act.split('_')[0].replace('sgb_','sgb'));stem=act.replace('sgb_','sgb') if act.startswith('sgb_') else stem
    if a.startswith('__'):stem+='-'+a[2:].removesuffix('.html')
    elif act=='aoeg_1977':stem+='-36'
    cs=sorted(D.glob(stem+'-*.html'));p=cs[-1] if cs else None
  if p and p.exists():C[u]={'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'official_url':u,'identity_status':'Newly located retained candidate, header/text to be actually checked; not a prior read or verdict.'}
rd=O/'readers';rd.mkdir(exist_ok=True)
ids={v['source_id'] for v in C.values() if 'source_id' in v};nextid=max(int(v[3:]) for v in ids)+1
for u,c in C.items():
 if 'source_id' not in c:c['source_id']=f'DEB{nextid:03d}';nextid+=1
 p=Path(c['path']);q=rd/(c['source_id']+'.txt')
 if not q.exists():
  if p.suffix=='.html':
   b=p.read_bytes();enc=re.search(br'charset\s*=\s*[\"\x27]?([^\"\x27\s;/>]+)',b[:4000],re.I);enc=enc.group(1).decode() if enc else 'utf-8';t=b.decode(enc);rr=Reader();rr.feed(t);rr.flush();q.write_text('\n'.join(rr.out)+'\n');c['html_title']=re.findall(r'<title[^>]*>(.*?)</title>',t,re.S|re.I)[:1]
  elif p.suffix=='.pdf':subprocess.run(['pdftotext','-layout',str(p),str(q)],check=True)
 if q.exists():c.update({'reader_path':str(q),'reader_sha256':sha(q),'extraction':'HTMLParser block text (whitespace joined within blocks) or pdftotext-layout PDF; nativeLF split onLF, full source not asserted read.'})
(O/'source-candidate-catalog.json').write_text(json.dumps(C,ensure_ascii=False,indent=2)+'\n');print(len(C),'located candidate URLs')
for g in M:
 miss=[u for u in g['cited_URLs'] if u not in C and not u.startswith('https://www.openaccountants')];print(g['slug'],'missing',len(miss))
