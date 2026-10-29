from writer import *
from decimal import Decimal as D, ROUND_FLOOR
from datetime import date
checks=[]
def test(name,actual,expected):
    assert actual==expected,(name,str(actual),str(expected));checks.append({'name':name,'actual':str(actual),'expected':str(expected),'pass':True})
def dime(x):return x.quantize(D('.1'),rounding=ROUND_FLOOR)
def tp_controls():
    test('TP management fee addback',D(250000)-D(180000),D(70000))
    test('TP expense-side additional tax',D(70000)*D('.21'),D(14700))
    test('TP 2027 counted days',(date(2027,12,31)-date(2027,3,31)).days,275)
    test('TP 2028 counted days',(date(2028,6,30)-date(2027,12,31)).days,182)
    p=D(14700)*D('.1')*(D(275)/365+D(182)/366)
    test('TP audit calendar/dime penalty',dime(p),D('1838.5'))
    test('TP early payment two thirds',dime(dime(p)*2/3),D('1225.6'))
    test('TP minimum audit penalty',D(14700)*D('.01'),D(147))
    test('TP royalty addback',D(1200000)-D(1080000),D(120000))
    test('TP royalty additional tax',D(120000)*D('.24'),D(28800))
    test('TP self-correction days',(date(2026,11,30)-date(2026,3,31)).days,244)
    test('TP supplementary penalty',dime(D(28800)*D('.03')*244/365),D('577.5'))
    test('TP late interest variant',dime(D(28800)*D('.15')*10/365),D('118.3'))
    test('TP small income-side cliff',D(21000)*D('.21')-D(20000)*D('.1'),D(2410))
    test('TP large income-side cliff',D(201000)*D('.24')-D(200000)*D('.21'),D(6240))
    test('TP exactly100000 lower band', D(100000)<=100000,True)
    test('TP exactly5000000 middle band',D(5000000)>5000000,False)
    test('TP fine threshold500 not imposed',D('5.00')<=5,True)
    test('TP fine threshold510 exceeds',D('5.10')<=5,False)

def pit_controls():
    from decimal import ROUND_HALF_UP
    def cent(x):return x.quantize(D('.01'),rounding=ROUND_HALF_UP)
    z=D('284.13')
    for name,multiple,value in [('PIT band1','154.8','43983.32'),('PIT band2','212.4','60349.21'),('PIT band3','264','75010.32'),('PIT personal','21','5966.73'),('PIT personal threshold','91.8','26083.13'),('PIT personal phaseout constant','51.6','14661.11'),('PIT spouse','19.2','5455.30'),('PIT spouse phaseout constant','70.8','20116.40')]:test(name,cent(z*D(multiple)),D(value))
    test('PIT filing threshold',cent(z*21/2),D('2983.37'))
    test('PIT Jana flat cap',min(D(48000)*D('.6'),D(20000)),D(20000))
    test('PIT Jana partial base',D(48000)-20000-6000,D(22000))
    test('PIT Jana taxable base',D(22000)-D('5966.73'),D('16033.27'))
    test('PIT Jana tax',cent(D('16033.27')*D('.15')),D('2404.99'))
    test('PIT Jana last-known tax at statutory19%',D(22000)*D('.19'),D(4180))
    test('PIT Jana no next advances',D(4180)>5000,False)
    test('PIT earliest45000fixture current2026 tax',cent((D(45000)-20000-6000-D('5966.73'))*D('.15')),D('1954.99'))
    test('PIT Peter allowance',cent(D('14661.11')-D(36000)/3),D('2661.11'))
    test('PIT Peter tax',cent(D('33338.89')*D('.19')),D('6334.39'))
    test('PIT child taper threshold',D('1.5')*12*1524,D(27432))
    test('PIT Peter child bonus',D(1200)-(D(36000)-27432)/10,D('343.2'))
    test('PIT Peter after child credit',D('6334.39')-D('343.2'),D('5991.19'))
    test('PIT Peter returned employer bonus reconciliation',D('5991.19')+100-5500,D('591.19'))
    for name,actual,expected in [('PIT15birthdayJune',6*100+6*50,900),('PIT18birthdayJune',6*50,300),('PITbirthJune',7*100,700),('PIT old mortgageOctober firstcap',D(400)*3/12,D(100)),('PIT old mortgage last9months',D(400)*9/12,D(300)),('PIT new mortgageOctober firstcap',D(1200)*3/12,D(300)),('PIT new mortgage last9months',D(1200)*9/12,D(900)),('PIT new mortgageJuly',min(D(2000)*D('.5'),D(1200)*6/12),D(600))]:test(name,actual,expected)
    test('PIT low-base child cap',D(2000)*D('.29'),D(580))
    test('PIT parent augmentation bonus',min(D(1200),D(6000)*D('.29')),D(1200))
    test('PIT half-year parent augmentation bonus',min(D(1200),D(4000)*D('.29')),D(1160))
    test('PIT changing child-count cap',D(4000)*(D('.29')*6/12+D('.36')*6/12),D(1300))
    test('PIT exactly5000 no advances',D(5000)>5000,False)
    test('PIT exactly16600 quarterly',D(16600)>16600,False)
    test('PIT DDS combined cap',min(D(240)+60,D(180)),D(180))
    test('PIT500 shared rental taxable receipts',D(6000)-500,D(5500))
    test('PIT proportional rental costs',cent(D(2000)*5500/6000),D('1833.33'))
    test('PIT micro loss',min(D(8000),D(10000)),D(8000))
    test('PIT excluded micro loss',min(D(8000),D(10000)*D('.5')),D(5000))
    test('PIT exactly60000 micro revenue gate',D(60000)<=60000,True)
    test('PIT60000.01 micro revenue gate',D('60000.01')<=60000,False)

def literal_checks():
    for key,s in scopes.items():
        test('raw hash '+key,sha(s['raw_path']),s['raw_sha256'])
        test('reader hash '+key,sha(s['reader_path']),s['reader_sha256'])
        text=lf(s['reader_path'])
        for i,q in enumerate(s['quotations'],1):test('literal quote '+key+':'+str(i),ws('\n'.join(text[q['LF_start']-1:q['LF_end']])),q['quote'])

def guide_identity_checks():
    m=json.loads((EVID/'current-guide-identities.json').read_text())
    # Accept list or map shape without changing the pinned manifest.
    for slug in ['slovakia-pit','sk-corporate-income-tax','sk-payroll-social','sk-cross-border','sk-transfer-pricing','slovakia-vat-return','slovakia-vat-registration-4-7-7a']:
        p=REPO/f'skills/international/slovakia/{slug}.md'
        r=next((x for x in m if isinstance(x,dict) and Path(x.get('path',x.get('file',''))).stem==slug),None) if isinstance(m,list) else m.get(slug,m.get(slug+'.md'))
        if r:test('Guide unchanged '+slug,sha(p),r['sha256'])

if __name__=='__main__':
    tp_controls();pit_controls();literal_checks()
    (EVID/'writer-checks.json').write_text(json.dumps({'scope':'Writer controls and literal evidence identity only; no independent review or whole-country verdict.','date':DATE,'checks':checks},ensure_ascii=False,indent=2)+'\n')
    print(f'{len(checks)} writer controls / exact hash / literal quote checks passed')
