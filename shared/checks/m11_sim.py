import numpy as np
from scipy.optimize import minimize
rng=np.random.default_rng(7)
T0,T=8,12
t=np.arange(T)
# factor model: two factors
f1=1+0.08*t; f2=np.sin(t*np.pi/2)  # trend + seasonality
names=['A','B','C','D','E','F','G','H','I','J']
load1=np.array([14,10,18,9,22,12,16,11,20,13.])
load2=np.array([1.2,0.6,1.8,0.5,2.0,1.0,1.5,0.7,1.1,1.6])
Y=np.outer(load1,f1)+np.outer(load2,f2)+rng.normal(0,0.15,(10,T))
Y=np.round(Y,1)
eff=np.array([0,0,0,0,0,0,0,0,1.0,1.6,2.0,2.2])
Y[0]+=eff
def sc(i):
    don=[j for j in range(10) if j!=i]
    X=Y[don][:, :T0]; y=Y[i,:T0]
    k=len(don)
    obj=lambda w: ((y-w@X)**2).sum()
    r=minimize(obj,np.ones(k)/k,bounds=[(0,1)]*k,constraints=[{'type':'eq','fun':lambda w:w.sum()-1}],method='SLSQP',options={'ftol':1e-12,'maxiter':1000})
    w=r.x; syn=w@Y[don]
    pre=np.sqrt(((Y[i,:T0]-syn[:T0])**2).mean()); post=np.sqrt(((Y[i,T0:]-syn[T0:])**2).mean())
    return dict(zip([names[j] for j in don],w.round(3))),syn,pre,post,post/pre
w,syn,pre,post,ratio=sc(0)
print('Y A',Y[0]);print('syn',syn.round(2));print('gap',(Y[0]-syn).round(2))
print('weights',{k:v for k,v in w.items() if v>0.005});print('pre',pre,'post',post,'ratio',ratio)
rs=[]
for i in range(10):
    _,_,p,q,r=sc(i); rs.append((names[i],round(p,3),round(q,3),round(r,2)))
rs.sort(key=lambda x:-x[3]);print(rs)
# DiD equal-weight
don=list(range(1,10));pre_d=Y[0,:T0].mean()-Y[don,:T0].mean();post_d=Y[0,T0:].mean()-Y[don,T0:].mean();print('DiD',post_d-pre_d, 'SC avg gap post',(Y[0,T0:]-syn[T0:]).mean())
# np.save('Y.npy',Y)  # optional
for i,n in enumerate(names): print(n,Y[i])
# leave-one-out drop F
def sc_d(i,excl,T0x):
    don=[j for j in range(10) if j!=i and j not in excl]
    X=Y[don][:, :T0x]; y=Y[i,:T0x];k=len(don)
    r=minimize(lambda w: ((y-w@X)**2).sum(),np.ones(k)/k,bounds=[(0,1)]*k,constraints=[{'type':'eq','fun':lambda w:w.sum()-1}],method='SLSQP',options={'ftol':1e-12,'maxiter':1000})
    syn=r.x@Y[don];return dict(zip([names[j] for j in don],r.x.round(3))),syn
w2,s2=sc_d(0,[5],8);print('LOO F',{k:v for k,v in w2.items() if v>.005},'pre rmspe',np.sqrt(((Y[0,:8]-s2[:8])**2).mean()),'post gap',(Y[0,8:]-s2[8:]).round(2),(Y[0,8:]-s2[8:]).mean())
w3,s3=sc_d(0,[],5);print('in-time Q6',(Y[0,5:8]-s3[5:8]).round(2))
# held-out pre-period check: fit on quarters 1-6, predict 7-8
w4,s4=sc_d(0,[],6);print('heldout fit weights',{k:v for k,v in w4.items() if v>.005},'gap Q7-8',(Y[0,6:8]-s4[6:8]).round(2),'pre rmspe q1-6',np.sqrt(((Y[0,:6]-s4[:6])**2).mean()).round(3))
# SDID-like comparison omitted; DiD equal weights printed above
