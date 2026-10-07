"""Arithmetic check for notes04.tex (Causal Trees and Forests).
Run: python3 checks/notes04_check.py   (numpy/scipy only)
Each line: PASS/FLAG, a label quoting the claim, claimed vs computed.
"""
import numpy as np
from scipy import integrate, stats

N_PASS, N_FLAG = 0, 0


def check(label, computed, claimed, tol):
    global N_PASS, N_FLAG
    ok = abs(computed - claimed) <= tol
    if ok:
        N_PASS += 1
    else:
        N_FLAG += 1
    print(f"{'PASS' if ok else 'FLAG'}  {label}: claimed {claimed}, computed {computed:.6g}")
    return ok


def flag(label, msg):
    global N_FLAG
    N_FLAG += 1
    print(f"FLAG  {label}: {msg}")


def emax(k):
    """E[max of k iid N(0,1)] by numerical integration."""
    f = lambda z: z * k * stats.norm.pdf(z) * stats.norm.cdf(z) ** (k - 1)
    return integrate.quad(f, -12, 12)[0]


print("== Section 1 ==")
for k, c in [(4, 1.03), (10, 1.54), (20, 1.87), (50, 2.25)]:
    check(f"E[max Z] is {c} for k={k}", emax(k), c, 0.005)
print(f"info  sqrt(2 ln k) for 4,10,20,50: {[round(np.sqrt(2*np.log(k)),2) for k in (4,10,20,50)]} (text: 'roughly')")
# squared bias (s E max)^2 exceeds s^2 once k >= 4 equal candidates
check("squared bias > s^2 at k=4 (E[max]^2 > 1)", float(emax(4) ** 2 > 1), 1, 0)
check("squared bias < s^2 at k=3 (so 'four or more' is the threshold)", float(emax(3) ** 2 < 1), 1, 0)
# leaf with 100 per arm, rates .30 vs .10
check("leaf 100/arm, .30 vs .10 has SE 0.055", np.sqrt(.3*.7/100 + .1*.9/100), 0.055, 0.0005)
check("each half has SE 0.077", np.sqrt(.3*.7/50 + .1*.9/50), 0.077, 0.0005)
# checkpoint: 20 segments, SE 0.03, null 0.06 -> expected reported winner
print(f"info  checkpoint: null winner expectation 0.06+0.03*E[max_20] = {0.06+0.03*emax(20):.4f} (consistent with observed 0.12)")

print("== Section 2, Step 1: split table ==")
nP = 2000
splits = {"A": (1200, .03, 800, .09, 1.73), "B": (600, .11, 1400, .03, 2.69)}
for k, (nL, tL, nR, tR, sc) in splits.items():
    check(f"split {k} unnormalised score {sc}", nL*nR/nP*(tL-tR)**2, sc, 0.005)
    check(f"split {k} children consistent with overall 0.054", (nL*tL + nR*tR)/nP, 0.054, 1e-9)
    # identity: weighted form equals n_L n_R/n_P^2 (tL-tR)^2 when parent is size-weighted mean
    tP = (nL*tL + nR*tR)/nP
    lhs = nL/nP*(tL-tP)**2 + nR/nP*(tR-tP)**2
    check(f"split {k}: Delta identity holds", lhs, nL*nR/nP**2*(tL-tR)**2, 1e-12)
check("tree splits on B (higher score)", float(splits["B"][4] > splits["A"][4]), 1, 0)
# consistency: setting has 4,000 shoppers, so the discovery half has 2,000
for k, (nL, tL, nR, tR, sc) in splits.items():
    check(f"split {k} sizes sum to discovery half 2,000", nL + nR, 2000, 0)

print("== Step 2: winner's curse ==")
rep = 0.05 + 0.02*1.54
check("reported winner averages 0.081", rep, 0.081, 0.0005)
check("a 62% overstatement", (rep-0.05)/0.05*100, 62, 0.5)
check("(using exact E[max_10]) winner", 0.05 + 0.02*emax(10), 0.081, 0.0005)

print("== Step 3: forest by hand ==")
leaves = [{1, 2, 3, 4}, {1, 2, 5, 6}]
alpha = {i: np.mean([(i in L)/len(L) for L in leaves]) for i in range(1, 7)}
for i, a in [(1, .25), (2, .25), (3, .125), (4, .125), (5, .125), (6, .125)]:
    check(f"alpha_{i} = {a}", alpha[i], a, 1e-12)
check("alphas sum to 1.000", sum(alpha.values()), 1.0, 1e-12)
D = np.array([1, 0, 1, 0, 1, 0]); Y = np.array([1, 0, 1, 1, 0, 0]); ell = np.array([.6, .5, .4, .6, .3, .4])
a = np.array([alpha[i] for i in range(1, 7)])
prod = (Y-ell)*(D-.5)
for i, (p, ap) in enumerate([(.20, .05), (.25, .0625), (.30, .0375), (-.20, -.025), (-.15, -.01875), (.20, .025)]):
    check(f"unit {i+1}: (Y-l)(D-.5) = {p}", prod[i], p, 1e-9)
    check(f"unit {i+1}: alpha x previous = {ap}", a[i]*prod[i], ap, 0.00005 + 1e-9)
num = (a*prod).sum(); den = (a*(D-.5)**2).sum()
check("sum 0.13125", num, 0.13125, 1e-9)
check("denominator 0.25", den, 0.25, 1e-12)
check("tau_hat(x) = 0.13125/0.25 = 0.525", num/den, 0.525, 1e-9)

print("== Step 4: calibration and GATES ==")
check("heterogeneity z = 0.64/0.21 = 3.05", .64/.21, 3.05, 0.005)
check("calibration z = (1-0.64)/0.21 = 1.71", (1-.64)/.21, 1.71, 0.005)
check("1.71 < 1.96 so 'not significantly' too spread", float((1-.64)/.21 < 1.96), 1, 0)
g = {"Bottom": .010, "2": .030, "3": .045, "4": .068, "Top": .107}
check("error bars 0.039 = 1.96 x SE 0.02", 1.96*0.02, 0.039, 0.0005)
check("group effects average 0.052", np.mean(list(g.values())), 0.052, 1e-9)
be = 0.06
status = {}
for k, v in g.items():
    lo, hi = v - 1.96*.02, v + 1.96*.02
    status[k] = "above" if lo > be else ("below" if hi < be else "straddles")
    print(f"info  GATES {k}: [{lo:.3f}, {hi:.3f}] -> {status[k]}")
check("only the top quintile's interval lies wholly above 0.06",
      float([k for k, s in status.items() if s == "above"] == ["Top"]), 1, 0)
strad = [k for k, s in status.items() if s == "straddles"]
check("quintiles 2 to 4 straddle, bottom wholly below", float(strad == ["2","3","4"] and status["Bottom"] == "below"), 1, 0)

print("== Exercise (computation) ==")
se_now = np.sqrt(.31*.69/300 + .20*.80/300)
se_half = np.sqrt(.31*.69/150 + .20*.80/150)
check("leaf SE now 0.0353", se_now, 0.0353, 0.00005)
check("0.31*0.69 = 0.2139", .31*.69, 0.2139, 1e-12)
check("halves SE 0.0499", se_half, 0.0499, 0.00005)
check("gap SE sqrt2 x 0.0499 = 0.0706", np.sqrt(2)*0.0499, 0.0706, 0.00005)
check("multiplier 2.8 = z_.975 + z_.80", stats.norm.ppf(.975)+stats.norm.ppf(.8), 2.8, 0.005)
check("detectable gap 2.8 x 0.0706 ~ 0.20", 2.8*0.0706, 0.20, 0.005)
check("leaf's whole effect 0.11", .31-.20, 0.11, 1e-12)
print(f"info  ratio detectable/effect = {2.8*0.0706/0.11:.2f} ('nearly twice')")
check("leaf size 300/arm = 600 matches table's first-time n", 600, 2*300, 0)

print(f"\nnotes04: {N_PASS} pass, {N_FLAG} flagged")
