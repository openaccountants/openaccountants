import math
def tarif(x):
    x=math.floor(x)
    if x<=12348: return 0
    if x<=17799:
        y=(x-12348)/10000; return math.floor((914.51*y+1400)*y)
    if x<=69878:
        z=(x-17799)/10000; return math.floor((173.10*z+2397)*z+1034.87)
    if x<=277825: return math.floor(0.42*x-11135.63)
    return math.floor(0.45*x-19470.38)
def st56(zx):
    def mst(z):
        d=2*(tarif(z*1.25)-tarif(z*0.75)); return max(d, math.floor(z*0.14))
    W1,W2,W3=14071,34939,222260
    if zx<=W1: return mst(zx)
    if zx<=W2:
        st=mst(W1); return min(st+math.floor((zx-W1)*0.42), mst(zx)) if False else st+math.floor((zx-W1)*0.42) if mst(zx)>st+(zx-W1)*0.42 else mst(zx)
    raise
def vsp(re4,stkl,health=True,pvsat=0.024,kvz=2.9):
    r=min(re4,101400)*0.093
    kv=min(re4,69750)*(kvz/200+0.07+pvsat) if health else 0
    v=r+kv
    if stkl!=6:
        hb=min(1900,min(re4,101400)*0.013+kv); v=max(v,r+hb)
    return math.ceil(v)
for h in (True,False):
    re4=20000; z=re4-vsp(re4,6,h); print('VI',h,z,st56(z))
re4=20000; z=re4-1266-vsp(re4,5); print('V',z,st56(z))
