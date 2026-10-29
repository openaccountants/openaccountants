from pathlib import Path
import json,sys,hashlib
R=Path(__file__).parent;D=R.parent/'germany-root-rental-ledger-2026-10-29';mode=sys.argv[1];lo,hi=map(int,sys.argv[2:4])
if mode=='claims':
 for n,x in enumerate(json.loads((D/'current-rule-rows.json').read_text())[lo-1:hi],lo):print('ROW',n,'native',x['native_LF'],'SECTION',x['section'],'ANCHORS',x['anchors'],'\n'+x['wording']+'\n')
elif mode=='newquotes':
 a=[x for x in json.loads((R/'de-rental-income-quote-reuse-plan.json').read_text())if'pending_direct_read'in x]
 for n,x in enumerate(a[lo-1:hi],lo):
  q=x['source'];s=x['identity'];l,h=q['reader_native_LF'];assert q['exact_original_language_quote']in'\n'.join(Path(s['reader_path']).read_text().split('\n')[l-1:h]);print('NEW',n,q['id'],q['act_article'],q['official_url'],'\n',s['reader_path'],'native',l,h,'SHA',q['reader_sha256'],'SOURCE_KIND',s.get('source_kind','raw body + derivative reader'),'\n'+q['exact_original_language_quote']+'\n')
