# Meeting 9 pipeline testbed: two simulators of different model classes, three pipelines, with and without planted confounding.
import numpy as np, warnings
from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import HistGradientBoostingRegressor, HistGradientBoostingClassifier
from sklearn.model_selection import KFold
warnings.filterwarnings('ignore')
rng=np.random.default_rng(3)
# ---- "real" courier data from a past randomised bonus test (the backtest data) ----
N=6000; p=5
Xr=rng.normal(size=(N,p))
mu0=lambda X: 10+3*X[:,0]+1.5*np.abs(X[:,1])+np.where(X[:,2]>0,1.5,0)
tau=lambda X: 2.0+1.5*np.tanh(2*X[:,2])-1.2*X[:,0]+np.where(X[:,3]>0.5,1.0,0)
Dr=rng.binomial(1,0.5,N); Yr=mu0(Xr)+Dr*tau(Xr)+rng.normal(0,2,N)
mlp=lambda: MLPRegressor(hidden_layer_sizes=(32,32),max_iter=600,random_state=0,early_stopping=True)
gbr=lambda: HistGradientBoostingRegressor(max_iter=200,learning_rate=0.05,max_depth=3)
def fit_sim(cls):
    m1=cls().fit(Xr[Dr==1],Yr[Dr==1]); m0=cls().fit(Xr[Dr==0],Yr[Dr==0])
    return m0,m1
sims={'Neural':fit_sim(mlp),'Boosted':fit_sim(gbr)}
VAL,COST=30,60          # yuan per extra peak hour; bonus cost
BUD=0.30                # pay top 30%
def run(sim,conf,rep):
    m0,m1=sims[sim]; r=np.random.default_rng(100+rep)
    n=4000; X=r.normal(size=(n,p))
    s0=m0.predict(X); s1=m1.predict(X); t=s1-s0             # simulator truth
    U=r.normal(size=n)
    logit=0.8*X[:,0]+0.5*X[:,1]+(1.2*U if conf else 0)
    D=r.binomial(1,1/(1+np.exp(-logit)))
    Y=s0+D*t+(1.5*U if conf else 0)+r.normal(0,2,n)
    k=int(BUD*n); net=VAL*t-COST
    def value(score):
        idx=np.argsort(-score)[:k]; return net[idx].clip(min=None).sum()/n*1000
    oracle=np.sort(net)[::-1][:k]; oracle=oracle[oracle>0].sum()/n*1000
    def value_pos(score):
        idx=np.argsort(-score)[:k]; return net[idx].sum()/n*1000
    # pipeline 1: predict-then-optimise (rank by predicted hours if paid)
    pr=gbr().fit(np.c_[X,D],Y); s_pred=pr.predict(np.c_[X,np.ones(n)])
    # pipeline 2: DR-learner with cross-fitted boosting
    phi=np.zeros(n)
    for tr,te in KFold(2,shuffle=True,random_state=rep).split(X):
        e=HistGradientBoostingClassifier(max_depth=3).fit(X[tr],D[tr]).predict_proba(X[te])[:,1].clip(0.05,0.95)
        a1=gbr().fit(X[tr][D[tr]==1],Y[tr][D[tr]==1]).predict(X[te]); a0=gbr().fit(X[tr][D[tr]==0],Y[tr][D[tr]==0]).predict(X[te])
        phi[te]=a1-a0+D[te]*(Y[te]-a1)/e-(1-D[te])*(Y[te]-a0)/(1-e)
    s_dr=gbr().fit(X,phi).predict(X)
    # pipeline 3: neural T-learner
    s_nt=mlp().fit(X[D==1],Y[D==1]).predict(X)-mlp().fit(X[D==0],Y[D==0]).predict(X)
    return oracle,value_pos(s_pred),value_pos(s_dr),value_pos(s_nt)
R=20
for sim in ['Neural','Boosted']:
    for conf in [False,True]:
        A=np.array([run(sim,conf,i) for i in range(R)]); res=A.mean(0)
        d=(A[:,2]-A[:,3]); 
        print(sim,'moderate' if conf else 'none',' '.join(f'{v:.0f}' for v in res),' regret',' '.join(f'{res[0]-v:.0f}' for v in res[1:]), ' NT-DR diff mean %.0f se %.0f'%((-d).mean(), d.std()/np.sqrt(R)))
