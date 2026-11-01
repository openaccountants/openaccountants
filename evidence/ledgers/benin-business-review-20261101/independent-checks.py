#!/usr/bin/env python3
"""Additive, frozen source-fidelity review. Never edits writer or earlier evidence."""
from pathlib import Path
from decimal import Decimal as D
import hashlib, json, re, subprocess, sys, unicodedata

R=Path(__file__).resolve().parents[3]
O=Path(__file__).parent
W=R/'evidence/ledgers/benin-business-20261101'
S=R.parent/'sources'
F='cf0afc121b77fe7457fefc8bd639bf720e32c98b'
C='99b3a5980edf872c0271d6de96581058e125ca0b'
B='251813c96f7b883f2adc4c1bb72bc175a288bd83'
M='59c23acba2ad66dd2bb29ffc81ffbb9289769ef8'
G='skills/benin/bj-business-income-tax.md'
sys.path.insert(0,str(R/'scripts'))
import skill_checks

def git(*a): return subprocess.check_output(['git',*a],cwd=R)
def sha(b): return hashlib.sha256(b).hexdigest()
def norm(t):
    t=unicodedata.normalize('NFKC',t).replace('’',"'").replace('‘',"'")
    return re.sub(r'\s+',' ',t).strip()
def save(n,d):
    p=O/n
    assert not p.exists(), 'Immutable record already exists: '+n
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def clean_page(t): return re.sub(r'(?m)^\s*\d+\s*$','',t)

# The independent reader read these clauses in full and their cited neighbours.
# Full decisive French clauses are retained below, not just substring matches.
NOTES=[
'Article54 is the annual natural-person own-account habitual lucrative-activity charge. It is a separate job from salary ITS and company IS.',
'Article55(1),(3),(4) names these classes. Article55(2) and58(1) were also read: the agriculture/livestock/fishing exemption screen is retained rather than omitted.',
'Article55(5) expressly subordinates the residual habitual/exceptional class to the four other named taxes. No general salary or capital-income charge is imported.',
'Article56(1)-(4) covers equipped undertaking leases, property/business intermediaries, habitual property purchases for resale and subdivisions. Ordinary property rent is not assumed.',
'Article57 expressly reserves101(2), then charges members/co-owners by their profit rights. Article101(2) is a turnover-based property-predominance exception; the new job requires classification first.',
'Article58(1)-(3) supports the specific IBA exemptions. Own-art-sales and performance-income predicates are retained; a universal tax exemption is not granted.',
'Article58(4)-(6) supports funds entrusted for at least three years, gambling gains and TPS taxpayers. The minimum duration is not a general IBA loss period.',
'Article178 delegates the numerical turnover threshold to a ministerial order. No actual order is available in this source chain, so the Guide correctly holds numerical TPS eligibility and a first classification.',
'Article179 excludes all persons subject to IS as of right or by option regardless of turnover. No TPS entitlement is inferred from low turnover alone.',
'Article181(1)-(2) expressly permits a request at any time, requires acceptance/refusal within eight days and treats silence as acceptance. This is an option for an established TPS taxpayer.',
'Article181(3)-(4) supplies first-day-of-following-month effect and irrevocability. No current-year retroactive effect is invented.',
'Article182(1)-(2) links movement to the month after the finding of breach, except December to next year. The purchases/services/equipment and signed-contract tests are retained.',
'Article182(4)-(5) supports control reclassification and two consecutive below-limit exercises before return to TPS. Neither is reduced to a one-year turnover snapshot.',
'Article182(3) divides pre-switch TPS credit50/50 between local and State taxes; it does not permit allocating the whole sum to IBA.',
'Signed June LFR8 adds CGI146(2)(a),(b),(d) only to CGI180(3). The turnover exclusion in146(2)(c) is not imported. First operative period and transition-credit instructions remain unresolved.',
'Article63 sets30% for ordinary IBA and only the stated25% education exception. Company industrial relief in46 is not carried into IBA.',
'Article63(2) expressly names private school/university/technical/professional education. This is not a general industrial rate.',
'Article64(1) expressly says1.5% and imports the definition in47. Article47(2), not its1% company rate, defines the financial-flow or potential-flow base and exclusions.',
'Article64(2)(a) names the building/public-works3% minimum on produits encaissables. No profit-base substitution is made.',
'Article64(2)(b) names10% with the101(2) reservation. Resolving property predominance first is a sound classification hold.',
'Original LF14 scan changes article64(3)(a) from500000 to250000; CGI64(3)(a) has the same250000. Actual income-period application remains tied to LF1/48, not intake metadata.',
'Article64(2)(c) delegates the amounts and collection method for used vehicles/specified consumer products; only the used-vehicle importer per-sale minimum is expressly liberatory. Missing regulation is not guessed.',
'Article64(3)(b) gives0.60FCFA/litre plus its250000 floor and extends this to the stated non-importers sourcing from approved importers with homologated prices. No blanket fuel-distributor concession is granted.',
'Article64(4) adds4000FCFA ORTB and explicitly refers to the10March instalment in51. Keeping it separate prevents turning it into a percentage minimum.',
'Article60(1)-(2)(b) imports the common computation subject to the three-year override. Article43(3),(5) retains proof, unused losses, enterprise identity and first profitable result. The five-year company period is not used.',
'Article60(3) allows voluntary retirement and life-insurance payments within5% of profit before those payments. The denominator is stated correctly.',
'Article60(4) supplies30% only when sufficient evidence does not establish the professional allocation. Article20 remains the general deductibility gateway; this is not permission to deduct personal expenditure.',
'Article65 is a half-tax reduction with exclusive home piecework, client-provided materials and the enumerated family/one companion/one under18 regular apprentice limit. The artisan limb sells mainly own work and imports that help restriction. Minimum interaction is expressly held.',
'Articles145-149 confirm separate art-dealing/new-enterprise/CGA/employment-credit regimes. The Guide grants no unworked entitlement or numerical incentive amount. Ordinary examples assume these do not apply.',
'Article60(1) imports IS profit determination subject to overrides. Articles8-9 and20 support the linked period/net-profit/support rules. The link is expressly narrowed to common methods, not rates or losses.',
'Original LF1 scan says income-tax measures apply to the exercise closed31December2025 absent contrary specification. An intake year alone cannot choose the income period.',
'Original LF47-48 scan repeals contrary prior provisions and expressly commences1January2026. This express wording is not transferred to the June law.',
'June LFR1 repeats the prior-exercise income-tax clause. Signed final48-49 repeal/execute without an express January date. The Guide does not certify the TPS overlay first operative period.',
'Article67(1) requires accrual compliant with accounting law for professional/habitual business profits. No automatic cash basis follows from being an individual.',
'Article67(2) limits cash election to liberal/non-commercial/intellectual-or-industrial-property income activities and requires election before30November of the preceding year, effective following1January. Both eligibility and timely proof are retained.',
'Article67(2) literally says tacit renewal unless denounced before30November of the second year. The Guide quotes that boundary and holds interpretation of later renewal periods and transition adjustments.',
'Article67(3) sends simultaneous industrial/commercial and non-commercial profits back to paragraph1 accrual. Cash is not extended to a combined commercial business.',
'Article60(2)(a) requires straight-line depreciation for IBA. No company accelerated method is imported.',
'Article60(3) spouse remuneration requires actual participation, a non-abnormally-high salary, social-security contributions and source withholding. All four predicates are retained.',
'Article60(3) other-family pay must be in normal conditions, really paid and for effective work. Mere booking is not made sufficient.',
'Article61(1)-(3) disallows own-work drawings, personal expenses and own-capital/funds remuneration. No operator salary deduction is invented.',
'REPAIR REQUIRED: Article60(5) excludes from the non-professional-income diversion amounts used to determine fixed-asset disposal gain/loss. The Guide/ledger omits that express exception, so its removal-to-IRF statement is too broad. Retain the carve-out next to it; precise allocation can stay held.',
'Articles63-64 and66 support the ordinary max calculation plus separate levy and documented credits. Regulatory minima, reductions and transitions are stopped rather than priced by the ordinary example.',
'Article62(1) defers the business-fund gain on continuation by direct-line heirs/spouse until their cessation/disposal, provided deceased-last-balance-sheet asset values are not raised. It does not waive other filing.',
'Article62(2) extends the condition to succession allocation and an exclusively heirs/spouse entity outside IS without valuation increase on partition/conversion. No general inheritance exemption is claimed.',
'Article66 expressly imports IS declaration/payment and entity payment on behalf of members under51. Linked49-52 supply the shared dates/procedure; its corporate rate and five-year losses are explicitly excluded.',
'Article133(2) requires the offset amount on a receipt-supported declaration. Article133(1)-(3) monthly AIB machinery was read too; the Guide does not compute a withholding-agent return.',
'Article133(4) applies unused31December AIB to profit tax, later instalments and profit-tax arrears. No immediate cash refund is asserted.',
'Signed June LFR9 retains prior written/electronic notice and adds an up-to-date tax position. CGI476 neighbouring suspension/return/death workflow is a separate unresolved job; the Guide does not certify its full operation.',
'Articles485,487-488 match the linked overview filing/payment/interest owner. Original LF3 scan conditions first historical declarations on spontaneity, first time, full payment and no ongoing control/investigation. No blanket current late-return waiver is asserted.',
'Article59 expressly limits IBA to Benin profits and treaty allocation under5-6. Article5 company-residence wording is not promoted to a verified natural-person residence test or a generic worldwide charge/foreign credit.',
'Article45 expressly applies to income tax or IS and foreign dependent/control profit transfers. The TP/XB links retain distinct jobs; treaty/credit/final-withholding results remain case-specific holds. QUOTE REPAIR F2: the original clause starts with capital Pour, while the ledger exact quote starts with lower-case pour.',
'Independent Decimal arithmetic gives30000 profit tax,300000 percentage minimum,300000 IBA,1000000 crossover and304000 with levy. Assumed established ordinary status does not prove TPS classification.',
'Independent Decimal arithmetic gives5m cash profit/7m accrual profit,375000 common percentage minimum,1.5m/2.1m IBA and600000 timing difference. Cash requires the hypothetical valid eligible election; no lifetime saving or basis-transition adjustment is implied.',
]
assert len(NOTES)==54

assert git('rev-parse','HEAD').decode().strip()==F
assert git('merge-base','origin/main','HEAD').decode().strip()==M
assert sha((R/G).read_bytes())=='09111922111237db1e9ea8fdaa5667371ebc292e031f438e5ab748709a503fd0'
assert git('show',C+':'+G)==git('show',F+':'+G)==(R/G).read_bytes()
frozen=[]
for name in git('diff','--name-only',B,F).decode().splitlines():
    data=git('show',F+':'+name)
    if (R/name).exists(): assert (R/name).read_bytes()==data,name
    frozen.append(dict(path=name,git_blob=git('rev-parse',F+':'+name).decode().strip(),sha256=sha(data)))

sources=json.loads((W/'source-identities.json').read_text())
for s in sources:
    data=(S/s['file']).read_bytes()
    assert sha(data)==s['sha256'] and len(data)==s['bytes'],s['file']
cgi=subprocess.check_output(['pdftotext','-layout',str(S/'cgi2026.pdf'),'-']).decode()
assert cgi==(S/'cgi2026.txt').read_text()
pages=cgi.split('\f')
clean='\n'.join(clean_page(p) for p in pages)
def article(n):
    m=re.search(r'\bArticle '+str(n)+r'\s*:',clean)
    assert m,n
    end=re.search(r'\bArticle \d+\s*:',clean[m.end():])
    return norm(clean[m.start():m.end()+end.start()]) if end else norm(clean[m.start():])
contexts={str(n):article(n) for n in [5,6,8,9,20,43,45,46,47,49,50,51,52,53,*range(54,69),101,130,131,132,133,134,*range(145,150),*range(178,186),476,485,487,488]}

# These three anchors require the rendered scan, not an OCR substring claim.
visual=json.loads((W/'visual-quote-anchors.json').read_text())
for x in visual:
    assert sha((S/x['scan_file']).read_bytes())==x['scan_sha256']
    x['independent_visual_verdict']='Confirmed by independent reader in the original cached signed scan; OCR is not controlling.'
    x['review_date']='2026-11-01'
texts={'cgi2026.pdf':norm(cgi),'lf2026.pdf':norm((S/'lf2026-ocr.txt').read_text()),'lfr2026.pdf':norm((S/'lfr2026-ocr.txt').read_text())}
vset={(x['row_id'],x['quote']) for x in visual}
rows=json.loads((W/'bj-business-income-tax.json').read_text())
human=(W/'bj-business-income-tax.md').read_text()
guide=(R/G).read_text()
assert len(rows)==54 and len({x['id'] for x in rows})==54
row_checks=[]
for r,note in zip(rows,NOTES):
    assert r['id'] in human and r['rule'] in human and r['exact_french_quote'] in human and r['official_url'] in human
    assert r['section'] in guide
    matches=[]
    qresults=[]
    for q in [r['exact_french_quote']]+r.get('additional_quote_anchors',[]):
        quote_to_check=q
        case_repair=r['id'].endswith(':52') and q==r['exact_french_quote']
        if case_repair: quote_to_check='P'+q[1:]
        found=norm(quote_to_check) in texts[r['source_file']]
        assert found or (r['id'],q) in vset,(r['id'],q)
        if r['source_file']=='cgi2026.pdf':
            foundpages=[i+1 for i,p in enumerate(pages) if norm(quote_to_check) in norm(p)]
            if not foundpages:
                foundpages=[i+1 for i in range(len(pages)-1) if norm(q) in norm(clean_page(pages[i])+clean_page(pages[i+1]))]
            assert foundpages,(r['id'],q)
            matches+=foundpages
        qresults.append(dict(quote=q,method='fresh cached PDF extraction' if r['source_file']=='cgi2026.pdf' else 'cached OCR plus scan reading',visual_exception=(r['id'],q) in vset,capitalization_repair_required=case_repair,actual_quote=quote_to_check))
    if r['source_file']=='cgi2026.pdf': assert r['source_pdf_page'] in matches,(r['id'],matches)
    supports=[]
    for a in r.get('additional_sources',[]):
        s=next(s for s in sources if s['sha256']==a['source_sha256'])
        for q in a['exact_french_quotes']: assert norm(q) in texts[s['file']],(r['id'],q)
        supports.append(a)
    # Full original-language CGI clauses, including conditions, live in this review's
    # context file; preserve the writer's exact anchors and source identity as well.
    article_nums=[int(n) for n in re.findall(r'(?:art(?:icle)?s?\.?|CGI)\s*(\d+)',r['act_article'],re.I)]
    primary={'01':54,'02':55,'03':55,'04':56,'05':57,'06':58,'07':58,'08':178,'09':179,'10':181,'11':181,'12':182,'13':182,'14':182,'16':63,'17':63,'18':64,'19':64,'20':64,'22':64,'23':64,'24':64,'25':60,'26':60,'27':60,'28':65,'29':145,'30':60,'34':67,'35':67,'36':67,'37':67,'38':60,'39':60,'40':60,'41':61,'42':60,'43':64,'44':62,'45':62,'46':66,'47':133,'48':133,'50':485,'51':59,'52':45,'53':64,'54':67}.get(r['id'][-2:])
    decisive=contexts[str(primary)] if primary else None
    verdict='repair required F1' if r['id'].endswith(':42') else ('rule accepted; exact quotation repair F2' if r['id'].endswith(':52') else 'accepted within stated partial preparation scope')
    row_checks.append({**r,'verdict':verdict,'review_date':'2026-11-01','independent_reason':note,'quote_checks':qresults,'primary_anchor_pdf_pages':sorted(set(matches)) or [r['source_pdf_page']],'independent_decisive_CGI_clause':decisive,'additional_sources_checked':supports})

# Exact hand transcription from original signed scans inspected by this reviewer.
scan_clauses={
'LF1':"En ce qui concerne les impôts sur le revenu, sauf précision contraire contenue dans le texte des mesures fiscales énoncées, les dispositions de la présente loi s’appliquent aux revenus de l’exercice clos au 31 décembre 2025.",
'LF3':"Du 1er janvier au 31 décembre 2026, les pénalités, amendes et majorations fiscales ne sont pas applicables aux contribuables qui souscrivent spontanément, pour la première fois, leurs déclarations des affaires réalisées au titre des exercices antérieurs et qui procèdent au paiement intégral des droits dus. Le bénéfice de cette mesure est subordonné à l’absence d’une procédure de contrôle fiscal ou d’une enquête fiscale en cours chez le contribuable.",
'LF14':"Au paragraphe 3 a) de l’article 64 du code général des impôts, le groupe de mots « cinq cent mille (500 000) » est remplacé par « deux cent cinquante mille (250.000) ».",
'LF47':"Sont abrogées, toutes dispositions antérieures contraires à celles de la présente loi.",
'LF48':"La présente loi qui entre en vigueur à compter du 1er janvier 2026, sera exécutée comme Loi de l’Etat.",
'LFR1':"En ce qui concerne les impôts sur le revenu, sauf précision contraire contenue dans le texte des mesures fiscales énoncées, les dispositions de la présente loi s’appliquent aux revenus de l’exercice clos au 31 décembre 2025.",
'LFR8':"Le point 3 de l’article 180 du code général des impôts est complété par la phrase ci-après : « L’exonération d’impôt ne s’applique pas dans les cas prévus aux alinéas a, b et d du paragraphe 2 de l’article 146 du présent code ».",
'LFR9':"Toute cessation d’activité ou cession d’une entreprise fait l’objet d’une information préalable, par écrit ou par voie électronique, adressée à l’administration fiscale trois mois avant le jour de la cessation ou de la cession. Cette information est accompagnée de la situation fiscale à jour de l’entité.",
'LFR48':"Sont abrogées, toutes dispositions antérieures contraires à celles de la présente loi.",
'LFR49':"La présente loi de finances rectificative sera exécutée comme Loi de l’Etat.",
}
for r in row_checks:
    k={'15':['LFR8'],'21':['LF14'],'31':['LF1'],'32':['LF47','LF48'],'33':['LFR1','LFR48','LFR49'],'49':['LFR9'],'50':['LF3']}.get(r['id'][-2:],[])
    r['independent_decisive_signed_scan_clauses']={key:scan_clauses[key] for key in k}
    if r['id'].endswith(':15'): r['independent_additional_CGI_clause']=contexts['146']

baseline=json.loads((W/'preservation-baseline.json').read_text())
assert baseline['base_commit']==B and baseline['main_base']==M
preserved=[]
for x in baseline['files']:
    old=git('show',B+':'+x['path'])
    assert sha(old)==x['sha256'] and git('rev-parse',B+':'+x['path']).decode().strip()==x['git_blob'],x['path']
    if x['path']=='skills/benin/README.md': continue
    assert git('show',F+':'+x['path'])==old,x['path']
    if (R/x['path']).exists(): assert (R/x['path']).read_bytes()==old,x['path']
    preserved.append({**x,'exact':True})
assert sum(x['path'].startswith('skills/') for x in preserved)==10
assert sum(x['path'].startswith('evidence/') for x in preserved)==43
prior_guides=git('ls-tree','-r','--name-only',B,'skills/benin').decode().splitlines()
assert set(prior_guides)=={x['path'] for x in preserved if x['path'].startswith('skills/')}|{'skills/benin/README.md'}
route=json.loads((W/'readme-routing-change.json').read_text())
old=git('show',B+':skills/benin/README.md')
new=(R/'skills/benin/README.md').read_bytes()
assert new==old+route['literal_append'].encode()
assert sha(old)==route['old_sha256'] and sha(new)==route['new_sha256']
partial=new.decode().split('partial:\n')[1].split('---')[0]
assert set(re.findall(r'^  ([A-Z-]+):',partial,re.M))=={'IT-IND','IT-CORP','VAT','SC','PR','TP','XB'}

# New addition replaces no old Guide. Map every old nonblank body paragraph,
# including table rows, examples and holds, to the exact same destination.
destinations=[]
for x in preserved:
    if not x['path'].startswith('skills/'): continue
    text=git('show',B+':'+x['path']).decode()
    body=text.split('---',2)[2]
    units=[u for u in re.split(r'\n\s*\n',body) if u.strip()]
    for i,u in enumerate(units,1):
        assert u in git('show',F+':'+x['path']).decode()
        destinations.append(dict(old_path=x['path'],old_body_unit=i,old_text=u,sha256=sha(u.encode()),destination=x['path'],status='retained byte-for-byte in same Guide',source='prior accepted commit '+B))
old_topics=git('show',F+':evidence/ledgers/benin-old-topics.md').decode()
assert old_topics==git('show',B+':evidence/ledgers/benin-old-topics.md').decode()
spotchecks=['family quotient','professional expenses allowance','Residence test','Annual IRPP filing deadline','Minimum tax (Impôt Minimum) rate','VAT registration threshold','Treaty relief','CNSS']
for term in spotchecks: assert term.lower() in old_topics.lower(),term

fm=skill_checks.read_frontmatter(guide)
shape=skill_checks.run_checks(str(R/G),guide,fm)
assert len(shape)==15 and not any(shape.values())
assert fm['tier']==2 and not any(k in fm for k in ['reviewed_by','reviewed_on','verified_by','review_status','license','trust_label','authored_by'])
assert 'openaccountants-cta-block' not in guide
commands=[
 ['python3','scripts/skill_checks.py',G],
 ['python3','scripts/validate-guides.py','--changed-only','--no-index-check'],
 ['python3','scripts/check-sync-integrity.py','--base',M,'--mode','audit','--strict-metadata'],
 ['python3','scripts/check-sync-integrity.py','--base',B,'--mode','audit','--strict-metadata'],
 ['python3','scripts/check-examples.py','--require',G],
 ['git','diff','--check',M,F],
 ['git','diff','--check',B,F],
]
results=[]
for cmd in commands:
    p=subprocess.run(cmd,cwd=R,capture_output=True,text=True)
    results.append(dict(command=cmd,returncode=p.returncode,stdout=p.stdout,stderr=p.stderr))
    assert p.returncode==0,results[-1]

examples=[
 dict(id='IBA-1',profit_tax=D(100000)*D('.30'),minimum=D(20000000)*D('.015'),annual_iba=max(D(100000)*D('.30'),D(20000000)*D('.015'),D(250000)),crossover=(D(20000000)*D('.015'))/D('.30'),with_levy=D(300000)+D(4000),decision='Percentage minimum binds; established ordinary IBA status is assumed, not derived from the hypothetical turnover.'),
 dict(id='IBA-2',cash_profit=D(20000000)-D(15000000),accrual_profit=D(25000000)-D(18000000),minimum=D(25000000)*D('.015'),cash_iba=max(D(5000000)*D('.30'),D(375000),D(250000)),accrual_iba=max(D(7000000)*D('.30'),D(375000),D(250000)),timing_difference=D(2100000)-D(1500000),decision='Default accrual versus permitted cash only with eligible activity and valid election. Same hypothetical reconciled minimum base. No basis-transition or permanent tax-saving claim.'),
]
assert [examples[0][k] for k in ['profit_tax','minimum','annual_iba','crossover','with_levy']]==list(map(D,[30000,300000,300000,1000000,304000]))
assert [examples[1][k] for k in ['cash_profit','accrual_profit','minimum','cash_iba','accrual_iba','timing_difference']]==list(map(D,[5000000,7000000,375000,1500000,2100000,600000]))
examples=[{k:str(v) if isinstance(v,D) else v for k,v in d.items()} for d in examples]

finding=dict(id='F1',priority='P2',status='open',ledger_row='bj-business-income-tax:42',file=G,line=56,source_pdf_pages=[35,36],act_article='CGI60(5)',official_url=next(s['official_url'] for s in sources if s['file']=='cgi2026.pdf')+'#page=35',exact_decisive_quote="à l'exclusion de ceux pris en compte pour la détermination de la plus-value ou moins-value de cession d'un élément d'actif immobilisé",problem='The IBA-to-IRF removal summary omits the explicit fixed-asset disposal gain/loss carve-out. Its present wording can divert those amounts out of business profit.',repair='Add the exclusion next to the removal rule in The base step4 and mirror it in ledger row42 (JSON and Markdown), with the decisive quote and PDF35-36 locator. Do not invent the held partial-use charge allocation. Preserve the frozen writer/reviewer findings as separate historical evidence.')
quote_finding=dict(id='F2',priority='P3',status='open',ledger_row='bj-business-income-tax:52',file='evidence/ledgers/benin-business-20261101/bj-business-income-tax.json',act_article='CGI45(1)',source_pdf_pages=[28],official_url=next(s['official_url'] for s in sources if s['file']=='cgi2026.pdf')+'#page=28',exact_decisive_quote='Pour l’établissement de l’impôt sur le revenu',problem='The primary quote is labelled exact but starts with lower-case pour; the original starts with upper-case Pour. Rule substance is supported.',repair='Capitalise the initial P in the primary exact quote for row52 in both JSON and Markdown ledger forms.')
save('row-verdicts.json',row_checks)
save('source-clause-contexts.json',dict(source='cgi2026.pdf',source_sha256=sources[0]['sha256'],method='fresh pdftotext -layout from original cached bytes; whitespace and apostrophes normalized only for matching',CGI_decisive_clauses=contexts,signed_scan_transcriptions=scan_clauses,visual_confirmations=visual,read_scope='CGI54-67 full with53/68; common cited5-9,20,43-47,49-52,101(2),130-134,145-149,178-185,476,485/487-488. LF fiscal1-17/final47-48 and LFR fiscal1-19/final48-49 read with scanned decisive clauses. Not a whole-code or later-law currentness certificate.'))
save('findings.json',[finding,quote_finding])
save('examples.json',examples)
save('old-topic-destinations.json',dict(base_commit=B,frozen_commit=F,unit_definition='Every nonblank old body paragraph; complete byte-identical source files are additionally hashed',all_body_units=destinations,old_units_moved=0,old_units_removed=0,lost_content_restored=0,earlier_81_topic_map_preserved_exact=True,spotchecked_existing_map_terms=spotchecks))
save('mechanical-preservation.json',dict(frozen_commit=F,content_commit=C,actual_main_merge_base=M,prior_accepted_head=B,frozen_files=frozen,preserved_files=preserved,preserved_guides=10,preserved_prior_evidence=43,readme_append_only=True,all_seven_domains_partial=True,new_guide_shape_checks=shape,checks=results,independent_examples=examples,source_identities=sources,body_unit_destination_count=len(destinations),new_guide_tier=2,no_accountant_attestation=True,source_fidelity_only=True,network={'git_fetch_origin':'Failed: Could not resolve host github.com. No escalation or remote mutation. Frozen review remains bound to the full local commit; parent owns fresh remote reconciliation.','official_web_open':['CGI official host: tool internal error, no fresh content returned','Original LF official URL: PDF reachable,15pages,no text returned','June LFR official host: tool internal error, no fresh content returned'],'basis':'Previously captured hash-bound official PDFs. Read source bytes and scanned decisive clauses independently; no fresh retrieval/currentness claim.'}))
save('review-identities.json',dict(frozen_head=F,content_commit=C,guide=dict(path=G,sha256=sha((R/G).read_bytes()),git_blob=git('rev-parse',F+':'+G).decode().strip()),ledger_files=[dict(path=str(p.relative_to(R)),sha256=sha(p.read_bytes())) for p in sorted(W.iterdir()) if p.is_file()],review_result='53 rows substantively accepted,1 substantive repair row; row52 also needs exact-quote capitalisation.2 recomputations passed; closure not accepted until F1/F2 repaired',reviewer_role='fresh independent reader; no author or accountant-attestation role',source_identities=sources))

lines=['# Benin IBA independent row verdicts','',f'Frozen head `{F}`; content commit `{C}`.54rows checked against actual cached official clauses and neighbours on2026-11-01.53accepted, row42 requires F1 repair. Full decisive French clauses are retained in row-verdicts.json/source-clause-contexts.json. This is source fidelity of a partial preparation job, not complete operative-law approval or accountant attestation.','', '| Row | Act | Verdict and independent reason |','|---|---|---|']
for r in row_checks: lines.append('| '+r['id']+' | '+r['act_article']+' | '+r['verdict']+'. '+r['independent_reason'].replace('|','/')+' |')
(O/'row-verdicts.md').write_text('\n'.join(lines)+'\n')
(O/'review.md').write_text(f'''# Independent Benin natural-person IBA review\n\nFrozen head: `{F}`. Content: `{C}`. Prior accepted country checkpoint: `{B}`. Review date:2026-11-01.\n\n54 ledger rows checked against full cited clauses and neighbours.53rows accepted within the partial preparation scope; row42 has one open P2 repair. Both examples independently recomputed with Decimal and passed the repository checker. All15new-Guide shape checks pass; actual committed changed-only validation passes with the three expected job/domain warnings; strict metadata passes against actual main merge-base `{M}` and prior checkpoint. Whitespace checks pass.\n\n## F1: retain the fixed-asset disposal carve-out\n\nAt `{G}:56`, The base step4 diverts non-professional property income to IRF without the exception in CGI60(5): «{finding['exact_decisive_quote']}». Read in full across PDF35-36. Add the exclusion next to the diversion rule and mirror it in JSON/Markdown ledger row42. This prevents the rule from removing amounts used to determine a fixed-asset disposal gain/loss. Exact partial-use charge allocation can remain held. No other source-fidelity repair was found in the54rows.\n\n## Preservation and boundaries\n\nAll ten prior Guide bodies and43prior Benin evidence files are byte-identical to the prior accepted checkpoint. README is exact append-only. Every old body paragraph is mapped to its unchanged destination in old-topic-destinations.json. The earlier81-topic destination map is exact; salary allowances/residence/filing, company minimum, VAT threshold, treaty and CNSS destinations were spot-checked. No old units moved or removed; lost content restored:0.\n\nArticle64IBA1.5% and article60three-year losses remain distinct from company1%/five-year rules. Article67cash eligibility and filing date conditions are retained; transition/renewal detail stays held. Signed scans independently confirm all three writer OCR exceptions: LF14floor, LF48commencement, LFR9current tax position. Additional scans LF1/3and LFR1/48-49 were read. June TPS exclusions match LFR8plus CGI146(2)(a),(b),(d); no January operative date is invented. The numerical TPS order, transition credit, special relief interactions, natural-person residence/treaty/credit, later-law completeness and authenticated filing remain unresolved. All seven domains remain partial.\n\nThis independent AI source review is not a credentialed accountant attestation, an authenticated filing certificate, or approval of complete current operative law. Existing country/owner/licensing rules were read. Guide/README/writer/status files and earlier evidence were not changed, and no commit, push, GitHub mutation or subagent was used.\n\n## Network limitation\n\nReviewer git fetch failed DNS resolution for github.com. Official web opens returned no fresh CGI/LFR text; the original LF PDF was reachable with no text. Review uses the existing official cached PDFs whose complete byte hashes match source-identities. Parent must reconcile remote state; no fresh source retrieval or later-law currentness is claimed.\n\nEvidence: row-verdicts.json and.md; source-clause-contexts.json; findings.json; examples.json; mechanical-preservation.json; old-topic-destinations.json; review-identities.json. Original findings are immutable. Parent repairs F1 and requests separate focused closure.\n''')
print(json.dumps(dict(rows=54,substantive_rules_accepted=53,repair_required=['F1','F2'],examples=2,shape_checks=15,preserved_guides=10,preserved_prior_evidence=43,body_units=len(destinations),output=str(O)),indent=2))
