import json,re,hashlib,math
from fractions import Fraction as F
from decimal import Decimal,ROUND_HALF_UP
from pathlib import Path
out=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27/spain-ledger-review')
p=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-spain/ledgers/spain-2026-evidence/es-corporate-tax');root=p.parents[2]
checks=[]
def c(name,actual,expected):
 assert actual==expected,(name,actual,expected)
 checks.append({'name':name,'actual':str(actual),'expected':str(expected),'pass':True})
def micro(base,days,lo,hi):
 b=min(F(base),F(50000*days,365));return b*F(lo,100)+(base-b)*F(hi,100)
def cents(v):return Decimal(v.numerator).__truediv__(Decimal(v.denominator)).quantize(Decimal('.01'),rounding=ROUND_HALF_UP)
c('ERD2026gross',F(100000)*F(23,100),23000);c('ERDbalance',23000-1000-7000,15000)
c('micro181band',F(50000*181,365),F(1810000,73));c('micro181excess',120000-F(50000*181,365),F(6950000,73));c('micro181tax',cents(micro(120000,181,19,21)),Decimal('24704.11'))
c('fullmicro120k',micro(120000,365,19,21),24200);c('shortbandnotfull',micro(120000,181,19,21)>micro(120000,365,19,21),True)
c('micro30kbasebelowband',micro(30000,365,19,21),5700);c('micro2025',micro(120000,365,21,22),25900);c('micro2027',micro(120000,365,17,20),22500)
for year,rate in [(2025,24),(2026,23),(2027,22),(2028,21),(2029,20)]:c('ERD'+str(year),100000*F(rate,100),rate*1000)
c('newfirstpositive',100000*F(15,100),15000);c('ordinary25',100000*F(25,100),25000)
for rate in [19,21,23,25,30]:
 c('inst5over7-'+str(rate),math.floor(F(5*rate,7)),{19:13,21:15,23:16,25:17,30:21}[rate]);c('inst19over20-'+str(rate),math.ceil(F(19*rate,20)),{19:19,21:20,23:22,25:24,30:29}[rate])
c('sixmillionstrict',6000000>6000000,False);c('sixmillionplus',6000001>6000000,True);c('tenmillioninclusive',10000000>=10000000,True)
c('lasttax18aftercredits',F(25000-2000-1000)*F(18,100),3960);c('lastnotnetbalance',F(25000-2000-1000-7000)*F(18,100),2700)
c('finance30percent',F(5000000)*F(30,100),1500000);c('financefloor',max(F(2000000)*F(30,100),1000000),1000000);c('finance181floor',F(1000000*181,365),F(36200000,73));c('financeexcesscarry',1800000-1500000,300000)
c('loss70ref',10000000*F(70,100),7000000);c('large20m50',10000000*F(50,100),5000000);c('large60m25',10000000*F(25,100),2500000);c('lossfloor',max(800000*F(70,100),1000000),1000000);c('lossactualbasecap',min(800000,max(800000*F(70,100),1000000)),800000)
c('capital20funds',100000*F(20,100),20000);c('capital23funds',100000*F(23,100),23000);c('capital265funds',100000*F(265,1000),26500);c('capital30funds',100000*F(30,100),30000);c('capital20basecap',min(30000,100000*F(20,100)),20000);c('capital25microcap',min(30000,100000*F(25,100)),25000)
c('level10',300000*F(10,100),30000);c('levelfullcap',min(20000000*F(10,100),1000000),1000000);c('levelbreachtaxuplift',2300*F(105,100),2415)
c('participation95',100000*F(95,100),95000);c('participationtaxable5',100000-95000,5000);c('participationforeignactualcap',min(12000,100000*F(25,100)),12000);c('foreignspanishcap',min(30000,100000*F(25,100)),25000)
c('charityrepeatedcap',min(20000,100000*F(15,100))*F(50,100),7500);c('charityordinary',10000*F(40,100),4000)
c('RDIexcess',100000*F(25,100)+20000*F(42,100),33400);c('tech12',50000*F(12,100),6000);c('filmfirstplus',1000000*F(30,100)+1000000*F(25,100),550000)
c('minimumbonifbelowfloor',min(15000,25000-12000),13000);c('minimumothercreditfloor',max(15000,25000-12000),15000);c('coopfloor',20000*F(60,100),12000)
c('ceutanew2staff',min(2*60000,1200000),120000);c('ceutafirst2period',min(2*120000,2400000),240000);c('ceutaold',min(2*50000,400000),100000);c('ceuta60gross',25000*F(60,100),15000);c('ceutaold50gross',25000*F(50,100),12500)
c('ZEC4',1000000*F(4,100),40000);c('ZECextra2jobs',1800000+2*500000,2800000)
c('publiclate0months',10000*F(1,100),100);c('publiclate11months',10000*F(12,100),1200);c('lateafter12',10000*F(15,100),1500);c('late25reduction',1500*F(75,100),1125);c('penalty50',10000*F(50,100),5000);c('nilvoluntary200half',F(200,2),100)
a=(p/'root-v1.3-repair/after.md').read_text();b=(p/'root-v1.3-repair/before.md').read_text();sentence=' Add back equity-interest impairment within the categories in art. 15.k, testing its incorporated art. 21 holding/foreign-tax conditions.'
restored=a.replace(sentence,'').replace('version: 1.3\n','version: 1.2\n').replace('last_updated: 2026-10-28\n','last_updated: 2026-10-27\n').replace('# Corporate income tax in Spain v1.3\n','# Corporate income tax in Spain v1.2\n')
c('repairfullinverse',restored==b,True)
c('casebytes',re.findall(r'```oa-check.*?```',a,re.S)==re.findall(r'```oa-check.*?```',b,re.S),True)
c('oldURLsequence',re.findall(r'https?://[^\s)>]+',a)==re.findall(r'https?://[^\s)>]+',b),True)
c('CTAexact',a[a.index('<!-- openaccountants-cta-block -->'):]==b[b.index('<!-- openaccountants-cta-block -->'):],True)
c('namedattributionexact',re.findall(r'^> Contributed.*$',a,re.M)==re.findall(r'^> Contributed.*$',b,re.M),True)
(out/'tranche10-controls.json').write_text(json.dumps({'count':len(checks),'checks':checks},indent=2)+'\n');print(len(checks),'PASS')
