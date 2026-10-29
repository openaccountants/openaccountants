from ledger_common import *
slug='de-self-employed-income-tax';rel='skills/international/germany/'+slug+'.md';raw=(R/rel).read_bytes();rows=list(units(raw.decode()));prior=json.loads((P/'support/de-income-tax/claim-rows.json').read_text());exact={x['wording']:x for x in prior};A={x['id']:x for x in json.loads((P/'support/de-income-tax/actual-read-quotes.json').read_text())}
for z in rows:
 if z['wording']in exact:
  s=exact[z['wording']];z.update({k:v for k,v in s.items()if k not in ['lf','section','wording']})
 elif z['wording'].startswith('| Transfers between own accounts'):z.update(anchors=['CASH','BUSCOST','INTEREST'],kind='positive statutory business-interest rule; root correction awaited')
 elif z['wording'].startswith('**Losses.**'):z.update(anchors=['E10d-1','E10d-2'],kind='positive loss-offset rule; root correction awaited')
 elif z['wording'].startswith('- **Foreign tax, foreign establishment'):z.update(anchors=['FOREIGNCREDIT','PROGRESSION','PROGEXCEPTIONS','PROGINTRO','PROGAPPLY'],kind='positive treaty/progression referral; root correction awaited')
 elif z['wording'].startswith('> Contributed'):z.update(anchors=[],kind='protected attribution')
 else:z.update(anchors=[],kind='UNCLASSIFIED')
old=[]
for ref in ['4aac878b58b4a12ba61221dd88be2f79d95e04c2',REF]:
 body=subprocess.check_output(['git','show',ref+':'+rel],cwd=R).decode()
 for z in units(body):
  same=next((x for x in rows if x['wording']==z['wording']),None)
  if same:d='Exact wording retained at current LF'+str(same['lf'])+', '+same['section']
  elif z['wording'].startswith('| Immediate write-off (GWG)') or z['wording'].startswith('| Low-value asset'):d='DE-B04 currentLF65: eligibility uses cost less containedVAT, not only recoverableVAT; actual expense retains irrecoverableVAT. Historical deductible-only wording corrected by own6(2)/9b and2026EÜRline37.'
  elif z['wording'].startswith('| Investment deduction (§ 7g)'):d='DE-B03 source correction: current investment-deduction table tests profit before BOTH7g deductions and add-backs against EUR200000. Own7g(1) full clause is quoted; historic deduction-only shorthand is corrected, not preserved as correct.'
  elif z['wording'].startswith('| Transfers between own accounts'):d='DE-L07 source correction at current LF94; interest remains a business classification subject to own4(4a) overwithdrawal adjustment and precise multi-year/mixed-debt boundary.'
  elif z['wording'].startswith('**Losses.**'):d='DE-L06 source correction at current LF108; actual10d(1) includes second preceding year under statutory cap, not the historical one-year limitation.'
  elif z['wording'].startswith('- **Foreign tax, foreign establishment'):d='DE-L09 source correction at current LF132; treaty/progression and credit/exit referrals retained with actual32b exceptions.'
  else:d='PENDING semantic destination'
  old.append(dict(ref=ref,old_lf=z['lf'],section=z['section'],wording=z['wording'],destination=d))
C=json.loads((P/'support/de-income-tax/supplementary-controls.json').read_text())
write(slug,raw,rows,A,old,C,'This Guide is the separately named self-employed copy introduced in actual commit4aac878b; every substantive/operational unit of that actual first body and public main is mapped. The predecessor of that introduction has no file at this path; no fictitious earlier platform body is used. All current shared clauses and both worked examples exactly match the separately sourced de-income-tax methods apart from the recorded root corrections. Same-writer actual source reads are reused with exact source identities and nativeLF coordinates, not represented as an independent review. Full statutory bank and supplementary exactFraction controls are preserved. Current exact church/2026-form/multi-year4(4a) limits remain ordinary precise boundaries. Root, not this ledger writer, owns Guide corrections. No independent or country PASS.')
