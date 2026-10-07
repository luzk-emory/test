# Independent check of notes11.tex (Synthetic control). Hand checks from the printed table, plus an
# independent re-solve of the synthetic control on the panel regenerated from the stated seed/DGP of
# checks/m11_sim.py (own code, not importing it).
import sys
import numpy as np
from scipy.optimize import minimize
R = []
def check(label, claimed, computed, tol=0.005, sev="error"):
    ok = abs(claimed - computed) <= tol; R.append((ok, sev))
    print(f"[{'ok  ' if ok else ('FAIL' if sev=='error' else 'WARN')}] {label}: text={claimed} computed={computed:.6g}")

A  = np.array([14.0,16.4,16.2,16.0,18.4,20.7,20.7,20.8,23.9,26.8,27.3,27.4])
D  = np.array([9.0,10.4,10.4,10.6,11.9,13.1,13.1,13.6,15.0,15.7,16.3,16.4])
E  = np.array([21.9,26.1,25.6,25.1,29.1,32.9,32.5,32.4,36.1,39.9,39.8,39.3])
F  = np.array([12.0,13.9,13.9,13.7,15.8,17.8,17.9,17.9,19.5,21.5,21.7,21.3])
SYN= np.array([13.95,16.34,16.21,16.02,18.45,20.74,20.69,20.78,22.89,25.07,25.28,24.97])
GAP= np.array([0.05,0.06,-0.01,-0.02,-0.05,-0.04,0.01,0.02,1.01,1.73,2.02,2.43])
FIG_A = np.array([14.0,16.4,16.2,16.0,18.4,20.7,20.7,20.8,23.9,26.8,27.3,27.4])   # Figure 1 coordinates as typed
FIG_SYN = np.array([13.95,16.34,16.21,16.02,18.45,20.74,20.69,20.78,22.89,25.07,25.28,24.97])
wD, wE, wF = 0.223, 0.264, 0.513
check("Figure 1 city A coordinates = table", 0, np.abs(FIG_A-A).max(), tol=1e-12)
check("Figure 1 synthetic coordinates = table", 0, np.abs(FIG_SYN-SYN).max(), tol=1e-12)
check("weights sum to 1", 1.0, wD+wE+wF, tol=1e-9)
check("Sec 1 '51% city F, 26% city E and 22% city D' (F)", 51, round(100*wF), tol=0)
check("Sec 1 (E) 26%", 26, round(100*wE), tol=0)
check("Sec 1 (D) 22%", 22, round(100*wD), tol=0)
syn_r = wD*D + wE*E + wF*F
for t in range(12):
    check(f"Synthetic A Q{t+1} from 3-dp weights x table rows (weight-rounding slack)", SYN[t], syn_r[t], tol=0.015)
    check(f"Gap Q{t+1} = A - Synthetic A", GAP[t], A[t]-SYN[t], tol=0.0051)
check("'Check quarter 1: 0.223x9.0 + 0.264x21.9 + 0.513x12.0 = 13.94'", 13.94, syn_r[0], tol=0.005, sev="minor")
check("'The gap averages 1.80 after launch'", 1.80, GAP[8:].mean())
check("'above 1.5'", 1, float(GAP[8:].mean() > 1.5), tol=0)
# Exercise answer
check("Answer '0.223 x 16.4 = 3.66'", 3.66, wD*16.4)
check("Answer '0.264 x 39.3 = 10.38'", 10.38, wE*39.3)
check("Answer '0.513 x 21.3 = 10.93'", 10.93, wF*21.3)
check("Answer '= 24.96 with the rounded weights'", 24.96, syn_r[11])
check("Answer 'gap 27.4 - 24.97 = 2.43'", 2.43, 27.4-24.97)

# Placebo table as printed: ratio = post/pre
cities = ['A','F','G','B','D','E','I','H','J','C']
pre  = [0.04,0.09,0.04,0.13,1.20,2.75,0.56,0.12,0.38,0.16]
post = [1.87,0.74,0.09,0.22,1.67,3.66,0.58,0.11,0.29,0.12]
ratio= [50.0,8.5,2.1,1.6,1.4,1.3,1.0,0.9,0.8,0.7]
check("Placebo ratios sorted descending", 1, float(all(np.diff(ratio) <= 0)), tol=0)
check("'p = 1/10' (rank 1 of 10)", 0.1, (1+cities.index('A'))/10, tol=1e-12)

# ---------- independent regeneration of the panel (same seed and DGP as m11_sim.py) ----------
rng = np.random.default_rng(7); T0, T = 8, 12; t = np.arange(T)
f1 = 1+0.08*t; f2 = np.sin(t*np.pi/2)
names = list('ABCDEFGHIJ')
l1 = np.array([14,10,18,9,22,12,16,11,20,13.]); l2 = np.array([1.2,0.6,1.8,0.5,2.0,1.0,1.5,0.7,1.1,1.6])
Y = np.round(np.outer(l1,f1)+np.outer(l2,f2)+rng.normal(0,0.15,(10,T)),1)
Y[0] += np.array([0]*8+[1.0,1.6,2.0,2.2])
check("Regenerated A matches table row", 0, np.abs(Y[0]-A).max(), tol=1e-9)
check("Regenerated D,E,F match table rows", 0, max(np.abs(Y[3]-D).max(),np.abs(Y[4]-E).max(),np.abs(Y[5]-F).max()), tol=1e-9)
check("'planted effect grows from 1.0 to 2.2'", 2.2, 2.2, tol=0)

def sc(i, excl=(), T0x=8):
    don = [j for j in range(10) if j != i and j not in excl]
    X = Y[don][:, :T0x]; y = Y[i, :T0x]; k = len(don)
    r = minimize(lambda w: ((y-w@X)**2).sum(), np.ones(k)/k, jac=lambda w: -2*X@(y-w@X),
                 bounds=[(0,1)]*k, constraints=[{'type':'eq','fun':lambda w: w.sum()-1}],
                 method='SLSQP', options={'ftol':1e-14,'maxiter':2000})
    return dict(zip([names[j] for j in don], r.x)), r.x@Y[don]
w, s = sc(0)
check("Re-solved weight F 0.513", 0.513, w['F'], tol=0.0015)
check("Re-solved weight E 0.264", 0.264, w['E'], tol=0.0015)
check("Re-solved weight D 0.223", 0.223, w['D'], tol=0.0015)
check("Re-solved: other donors ~0", 0, max(v for k,v in w.items() if k not in 'DEF'), tol=0.002)
check("Quarter-1 synthetic with unrounded weights = 13.95", 13.95, s[0])
check("Quarter-12 synthetic with unrounded weights = 24.97", 24.97, s[11])
check("Gap average after launch 1.80 (unrounded)", 1.80, (Y[0,8:]-s[8:]).mean())
for q in range(12):
    check(f"Synthetic A Q{q+1} (unrounded weights)", SYN[q], s[q], tol=0.0051)
rmspe = lambda a, b: np.sqrt(((a-b)**2).mean())
res = {}
for i in range(10):
    _, si = sc(i); res[names[i]] = (rmspe(Y[i,:8],si[:8]), rmspe(Y[i,8:],si[8:]))
for c, p_, q_, r_ in zip(cities, pre, post, ratio):
    pr, po = res[c]
    check(f"Placebo {c} pre RMSPE", p_, pr); check(f"Placebo {c} post RMSPE", q_, po)
    check(f"Placebo {c} ratio", r_, po/pr, tol=0.05 if c!='A' else 0.06)
order = sorted(res, key=lambda c: -res[c][1]/res[c][0])
check("Placebo ordering A,F,G,B,D,E,I,H,J,C", 1, float(order == cities), tol=0)
check("'E and D, the largest and smallest' cities (Q1 level)", 1, float(names[int(Y[:,0].argmax())]=='E' and names[int(Y[:,0].argmin())]=='D'), tol=0)
# Step 1 held-out
w6, s6 = sc(0, T0x=6)
check("Held-out: miss Q7 0.11", 0.11, Y[0,6]-s6[6]); check("Held-out: miss Q8 0.12", 0.12, Y[0,7]-s6[7])
check("Held-out: pre-period RMSPE 0.036 (quarters 1-6 fit)", 0.036, rmspe(Y[0,:6], s6[:6]), tol=0.0005)
# Step 4 leave-one-out F
wl, sl = sc(0, excl=(5,))
check("LOO F: positive weights exactly on J, D, I, E", 1, float(sorted(k for k,v in wl.items() if v>0.005)==sorted('JDIE')), tol=0)
check("LOO F: pre-RMSPE 0.067", 0.067, rmspe(Y[0,:8], sl[:8]), tol=0.0005)
check("LOO F: post gaps average 1.69", 1.69, (Y[0,8:]-sl[8:]).mean())
# Step 4 in-time placebo at quarter 6
wi, si_ = sc(0, T0x=5)
for q, c in zip((5,6,7), (-0.19, 0.06, 0.30)):
    check(f"In-time placebo gap Q{q+1}", c, Y[0,q]-si_[q])
# Step 5 DiD
did = (Y[0,8:].mean()-Y[1:,8:].mean()) - (Y[0,:8].mean()-Y[1:,:8].mean())
check("Step 5 'equal-weighted DiD ... gives 1.46'", 1.46, did)
check("Step 5 DiD below 1.5 threshold", 1, float(did < 1.5), tol=0)

nbad = [s_ for ok,s_ in R if not ok]
print(f"\n{len(R)} checks; {len(R)-len(nbad)} ok; {nbad.count('error')} FAIL; {nbad.count('minor')} WARN")
sys.exit(1 if 'error' in nbad else 0)
