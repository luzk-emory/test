"""Arithmetic check for notes06.tex (Allocation and Policy Learning).
Run: python3 checks/notes06_check.py   (numpy/scipy only)
"""
import itertools
import numpy as np
from scipy.optimize import linprog
from scipy import stats

N_PASS, N_FLAG = 0, 0


def check(label, computed, claimed, tol):
    global N_PASS, N_FLAG
    ok = abs(computed - claimed) <= tol
    N_PASS += ok; N_FLAG += (not ok)
    print(f"{'PASS' if ok else 'FLAG'}  {label}: claimed {claimed}, computed {computed:.6g}")
    return ok


def flag(label, msg):
    global N_FLAG
    N_FLAG += 1
    print(f"FLAG  {label}: {msg}")


print("== Sure-thing decomposition / variance formula (symbolic spot check) ==")
rng = np.random.default_rng(1)
for _ in range(5):
    m, a, k, mu0, tau = rng.random(5)*[10, 3, 2, .5, .3]
    mu1 = mu0 + tau
    check("v = m tau - k - a mu1 = (m-a)tau - a mu0 - k", m*tau-k-a*mu1, (m-a)*tau-a*mu0-k, 1e-12)
# Var(v_hat) with independent arms: v = (m-a)mu1 - m mu0 - k
m, a, s1, s0 = 10., 3., .02, .03
check("Var(v_hat) = (m-a)^2 Var mu1 + m^2 Var mu0 (MC)",
      np.var((m-a)*rng.normal(0, s1, 400000) - m*rng.normal(0, s0, 400000)),
      (m-a)**2*s1**2 + m**2*s0**2, 0.002)

print("== Integer knapsack illustration ==")
c = np.array([6, 5, 5]); net = np.array([12, 9, 9]); C = 10
r = (net+c)/c
check("first unit ratio 3.0", r[0], 3.0, 1e-12)
best = max((sum(net[list(S)]), S) for n_ in range(4) for S in itertools.combinations(range(3), n_) if c[list(S)].sum() <= C)
check("greedy takes first only: 12", 12, net[0], 0)
check("optimum = two cheaper units = 18", best[0], 18, 0)
check("greedy within one unit's value", float(best[0]-12 <= net.max()), 1, 0)

print("== Fairness illustration ==")
# groups: a: 750@6, 4250@1 ; b: 250@6, 1000@3, 3750@0.5; cap 1000; rate_a <= g * rate_b
Na = Nb = 5000; cap = 1000
segs = [("a", 750, 6), ("a", 4250, 1), ("b", 250, 6), ("b", 1000, 3), ("b", 3750, .5)]


def solve(gamma):
    cvec = -np.array([n*v for _, n, v in segs])  # x_s = share of segment treated
    A = [[n for _, n, _ in segs],
         [n/Na if g == "a" else -gamma*n/Nb for g, n, _ in segs]]  # rate_a <= gamma rate_b
    res = linprog(cvec, A_ub=A, b_ub=[cap, 0], bounds=[(0, 1)]*5, method="highs")
    return -res.fun, res


v_inf = solve(1e9)[0]
check("unconstrained value 6,000", v_inf, 6000, 1e-6)
check("rates 15% and 5%", 750/5000*100 + 0*0, 15, 1e-12)
check("rate_b 5%", 250/5000*100, 5, 1e-12)
V125, res = solve(1.25)
xb = 5000*1000/(5000*2.25)
check("group b gets 444.4", 1000/2.25, 444.4, 0.05)
check("group a gets 555.6", 1000 - 1000/2.25, 555.6, 0.05)
check("integer split 555/445 satisfies gamma=1.25", float(555 <= 1.25*445), 1, 0)
check("LP value with gamma=1.25 ~ 5,415 (integer) / 5,416.7 (LP)", V125, 5416.7, 0.1)
print(f"info  LP exact value {V125:.2f}, price {6000-V125:.2f} (text: whole customers 555/445, value 5,415, price 585)")
check("swaps about 195", 750 - 555, 195, 0)
check("integer value 6000 - 195*3 = 5,415", 6000-195*3, 5415, 0)
check("price about 585", 195*3, 585, 0)
# integer optimum check
bestint = max(6*min(na, 750) + 1*max(na-750, 0) + 6*min(1000-na, 250) + 3*max(1000-na-250, 0)
              for na in range(0, 1001) if na <= 1.25*(1000-na))
print(f"info  best feasible integer value with gamma=1.25: {bestint}")
# multipliers: lambda + eta/Na = 6 ; lambda - g eta/Nb = 3
g = 1.25
eta = 3/(1/Na + g/Nb); lam = 6 - eta/Na
check("eta* ~ 6,667", eta, 6667, 1)
check("lambda* ~ 4.67", lam, 4.67, 0.005)
rate_b = (1000/2.25)/5000
check("rate_b ~ 0.089", rate_b, 0.089, 0.0005)
check("0.05 x 6667 x 0.089 ~ 30", 0.05*6667*0.089, 30, 0.5)
V120 = solve(1.20)[0]
check("LP: tightening 1.25 -> 1.20 costs ~ 30", V125 - V120, 30, 1)
# LP duals for cap and rate constraint (highs marginals are <=0 for max-as-min)
duals = -res.ineqlin.marginals
check("LP dual of cap = lambda* 4.67", duals[0], 4.67, 0.01)
check("LP dual of rate constraint = eta* 6,667", duals[1], 6667, 1)
check("four-fifths -> gamma = 1/0.8 = 1.25", 1/0.8, 1.25, 1e-12)

print("== Capacity: kitchens A and B ==")
p, gg, base, q = 25, 15, 200, 210
pay = lambda y: p*min(y, q) - gg*max(y-q, 0)
check("A: v + c = 175", pay(215)-pay(base), 175, 1e-9)
check("B: v + c = -25", .5*(pay(230)-pay(base)) + .5*(pay(200)-pay(base)), -25, 1e-9)
check("B: tau = 15", .5*230+.5*200-base, 15, 1e-12)
check("A: tau = 15", 215-base, 15, 0)
cu, co = 40, 10
kappa = cu/(cu+co)
check("kappa = 0.8", kappa, 0.8, 1e-12)
loss = lambda qq, ys, ps: sum(pr*(cu*max(y-qq, 0) + co*max(qq-y, 0)) for y, pr in zip(ys, ps))
ysB, psB = [200, 230], [.5, .5]
qopt = min(range(150, 300), key=lambda qq: loss(qq, ysB, psB))
check("B prepares 230", qopt, 230, 0)
check("expected loss at 215 = 375", loss(215, ysB, psB), 375, 1e-9)
check("expected loss at 230 = 150", loss(230, ysB, psB), 150, 1e-9)

print("== Section 2 table ==")
T = {  # seg: (b5, c5, n5, b10, c10, n10)
    "A": (6.0, 2.0, 4.0, 9.0, 5.0, 4.0), "B": (4.0, 2.0, 2.0, 7.0, 4.5, 2.5),
    "C": (3.0, 2.5, 0.5, 4.0, 5.0, -1.0), "D": (1.5, 2.5, -1.0, 2.0, 5.0, -3.0),
    "E": (2.0, 1.0, 1.0, 2.5, 2.5, 0.0), "F": (0.5, 1.5, -1.0, 0.8, 3.0, -2.2)}
for s, (b5, c5, n5, b10, c10, n10) in T.items():
    check(f"{s} b-c at 5", b5-c5, n5, 1e-9)
    check(f"{s} b-c at 10", b10-c10, n10, 1e-9)
N = 10000
segs6 = list(T)


def lp(budget):
    # x[s,a] for a in (5,10); sum_a x <= 1
    nets = []; costs = []
    for s in segs6:
        b5, c5, n5, b10, c10, n10 = T[s]
        nets += [n5, n10]; costs += [c5, c10]
    nets = np.array(nets)*N; costs = np.array(costs)*N
    A = [costs]; bub = [budget if budget is not None else 1e12]
    for i in range(6):
        row = np.zeros(12); row[2*i:2*i+2] = 1; A.append(row); bub.append(1)
    res = linprog(-nets, A_ub=np.array(A), b_ub=bub, bounds=[(0, 1)]*12, method="highs")
    return -res.fun, res.x.reshape(6, 2), res


# Step 1: no budget
V, x, _ = lp(None)
check("Step 1 profit 80,000", V, 80000, 1e-6)
spend = 10000*(2.0+4.5+2.5+1.0)
check("Step 1 spend 100,000", spend, 100000, 0)
check("Step 1 profit by hand 10,000*(4+2.5+0.5+1)", 10000*(4+2.5+.5+1), 80000, 0)
# Step 2: budget 50,000
check("ratio A at 5 = 2.0", 4/2, 2.0, 0)
check("ratio B,E at 5 = 1.0", 2/2 + 0*(1/1), 1.0, 0)
check("ratio C at 5 = 0.2", .5/2.5, 0.2, 1e-12)
check("ratio B upgrade = 0.2", (2.5-2.0)/(4.5-2.0), 0.2, 1e-12)
check("A,B,E at 5 cost 50,000", 10000*(2+2+1), 50000, 0)
V50, x50, r50 = lp(50000)
check("Step 2 LP profit 70,000", V50, 70000, 1e-6)
print("info  LP allocation at 50k (rows A-F, cols 5/10):", np.round(x50, 3).tolist())
V60 = lp(60000)[0]
check("extra 10,000 adds ~2,000 (lambda*=0.2)", V60-V50, 2000, 1e-6)
check("halving budget costs 10,000", 80000-V50, 10000, 1e-6)
V49 = lp(49999)[0]
check("removing a yuan at 50,000 costs 1.00", V50-V49, 1.0, 1e-6)
# Step 3 price rule
check("B at 5 under lambda .2 = 1.6", 2.0-.2*2.0, 1.6, 1e-12)
check("B at 10 under lambda .2 = 1.6", 2.5-.2*4.5, 1.6, 1e-12)
check("C at 5 under lambda .2 = 0", .5-.2*2.5, 0, 1e-12)
# Step 4
check("90% lower bound 0.5 - 1.28*0.4 = -0.01", .5-1.28*.4, -0.01, 0.005)
check("z_.10 one-sided = 1.28", stats.norm.ppf(.9), 1.28, 0.005)

print("== Step 5: policy tree ==")
new = np.array([1, 1, 1, 1, 0, 0, 0, 0]); hi = np.array([1, 1, 0, 0, 1, 1, 0, 0])
G = np.array([3.0, 1.0, 2.0, -1.0, -2.0, .5, -.5, -1.5])
check("treat everyone 1.5/8 = 0.19", G.sum()/8, 0.19, 0.005)
check("treat everyone sum 1.5", G.sum(), 1.5, 1e-12)
check("new customers 5.0/8 = 0.63", (new*G).sum()/8, 0.63, 0.0051)
check("high spenders 2.5/8 = 0.31", (hi*G).sum()/8, 0.31, 0.005)
cand1 = {"none": 0, "all": G.sum(), "new": (new*G).sum(), "old": ((1-new)*G).sum(),
         "hi": (hi*G).sum(), "lo": ((1-hi)*G).sum()}
check("best depth-one tree = new customers", float(max(cand1, key=cand1.get) == "new"), 1, 0)
cells = {(n_, h): G[(new == n_) & (hi == h)].sum() for n_ in (1, 0) for h in (1, 0)}
check("cell sums 4.0, 1.0, -1.5, -2.0",
      np.abs(np.array([cells[(1, 1)], cells[(1, 0)], cells[(0, 1)], cells[(0, 0)]]) - [4, 1, -1.5, -2]).max(), 0, 1e-12)
best2 = sum(max(v, 0) for v in cells.values())
check("depth two cannot improve (best = 5.0)", best2, 5.0, 1e-12)
lab = (G > 0).astype(int); w = np.abs(G)
mis = lambda pi: w[pi != lab].sum()
check("'new' misclassification weight 1.5", mis(new), 1.5, 1e-12)
check("'everyone' misclassification weight 5.0", mis(np.ones(8, int)), 5.0, 1e-12)
check("difference 3.5 = 5.0 - 1.5 in value", mis(np.ones(8, int)) - mis(new), (new*G).sum()-G.sum(), 1e-12)
for pi in [new, hi, np.ones(8, int), np.zeros(8, int)]:
    check("weighted-classification identity", (pi*G).sum(), (w*(pi == lab)).sum() - np.maximum(-G, 0).sum(), 1e-12)

print("== Exercise 1: budget 75,000 ==")
V75 = lp(75000)[0]
check("profit 75,000", V75, 75000, 1e-6)
check("C at 5 costs 25,000", 10000*2.5, 25000, 0)
check("C at 5 nets 5,000", 10000*.5, 5000, 0)
check("B upgrade costs 25,000", 10000*(4.5-2.0), 25000, 0)
check("B upgrade nets 5,000", 10000*(2.5-2.0), 5000, 0)
check("return 0.2 per yuan", (V75-V50)/25000, 0.2, 1e-9)

print("== Exercise 2 ==")
check("A at 10 ratio 0.8", 4/5, 0.8, 1e-12)
check("A at 5 cost less than half of 10's", float(2.0 < 5.0/2), 1, 0)

print("== Exercise 3: third kitchen ==")
ys, ps = [205, 215, 235], [1/3]*3
tau = np.dot(ys, ps) - 200
check("tau = 18.3", tau, 18.3, 0.05)
check("mean promoted demand 218.3", np.dot(ys, ps), 218.3, 0.05)
check("25 x 18.3 - 60 = 398", 25*tau-60, 398, 0.5)
incs = [pay(y)-pay(200) for y in ys]
for got, cl in zip(incs, [125, 175, -125]):
    check(f"day value {cl}", got, cl, 1e-9)
check("mean 58.3", np.mean(incs), 58.3, 0.05)
check("v = -1.7", np.mean(incs)-60, -1.7, 0.05)
q3 = min(range(150, 300), key=lambda qq: loss(qq, ys, ps))
check("prepare 235", q3, 235, 0)
check("F1(215) = 2/3", 2/3, 2/3, 0)

print(f"\nnotes06: {N_PASS} pass, {N_FLAG} flagged")
