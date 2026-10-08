import numpy as np
rng=np.random.default_rng(5)
n=60000
R=rng.integers(40,161,n).astype(float)
age=30+0.05*(R-100)+rng.normal(0,8,n)
D=(R>=100).astype(float)
p=0.55+0.004*(R-100)-0.00002*(R-100)**2+0.08*D
Y=rng.binomial(1,np.clip(p,0,1))
def ll(Y,R,h,c=100):
    w=np.clip(1-np.abs(R-c)/h,0,None); m=w>0
    Xm=np.c_[np.ones(m.sum()),(R[m]>=c),R[m]-c,(R[m]-c)*(R[m]>=c)]
    W=w[m]; XtW=Xm.T*W; b=np.linalg.solve(XtW@Xm,XtW@Y[m])
    e=Y[m]-Xm@b; meat=(Xm.T*(W*e)**2)@Xm; bread=np.linalg.inv(XtW@Xm); V=bread@meat@bread
    return b[1],np.sqrt(V[1,1]),m.sum()
for h in [10,20,30]:
    print(h,[round(x,4) for x in ll(Y,R,h)])
print('age jump',[round(x,3) for x in ll(age,R,20)])
# density: counts just below/above
print('counts 95-99',((R>=95)&(R<100)).sum(),'100-104',((R>=100)&(R<105)).sum())
bins=np.arange(40,161,5); mids=(bins[:-1]+bins[1:])/2
means=[Y[(R>=a)&(R<a+5)].mean() for a in bins[:-1]]
np.savetxt('../../meetings/m08/h5_bins.csv',np.c_[mids,means],delimiter=',',fmt='%.3f')
# naive difference above vs below overall
print('naive',Y[D==1].mean()-Y[D==0].mean())
