"""Arithmetic check for handoutH5.tex (Sequential Decisions).
Run: python3 checks/handoutH5_check.py   (numpy only)
"""
import itertools
import numpy as np

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


# SMART table: P(order wk1 | A1), E[Y | responder, A1], E[Y | non-resp, A1, A2]
P = {1: .40, 0: .25}
EYr = {1: 1.5, 0: 1.6}
EYn = {(1, 1): .9, (1, 0): .5, (0, 1): .9, (0, 0): .3}
M, CC = 10, 5  # yuan per order, per coupon


def regime(d1, d2):
    """d2 = coupon to non-responders (responders get nothing). Returns (value, orders incl. week-1 order)."""
    p = P[d1]
    orders = p*(1 + EYr[d1]) + (1-p)*EYn[(d1, d2)]
    cost = CC*d1 + CC*(1-p)*d2
    return M*orders - cost, orders


print("== Step 1: stage 2 ==")
check("2nd coupon adds 0.4 after week-1 coupon", EYn[(1, 1)]-EYn[(1, 0)], 0.4, 1e-12)
check("worth -1", 10*.4-5, -1, 1e-12)
check("adds 0.6 after none", EYn[(0, 1)]-EYn[(0, 0)], 0.6, 1e-12)
check("worth +1", 10*.6-5, 1, 1e-12)
d2opt = {a1: int(M*(EYn[(a1, 1)]-EYn[(a1, 0)]) - CC > 0) for a1 in (0, 1)}
check("d2opt: coupon only if no week-1 coupon", float(d2opt == {1: 0, 0: 1}), 1, 0)

print("== Step 2: stage 1 ==")
Q1_1 = .40*10*(1+1.5) + .60*10*.5 - 5
Q1_0 = .25*10*(1+1.6) + .75*(10*.9-5)
check("Q1(A1=1) pieces 10 + 3 - 5", .40*10*2.5, 10, 1e-12)
check("Q1(A1=1) = 8.0", Q1_1, 8.0, 1e-12)
check("Q1(A1=0) pieces 6.5 + 3", .25*10*2.6, 6.5, 1e-12)
check("Q1(A1=0) = 9.5", Q1_0, 9.5, 1e-12)
check("Q1 via regime() with optimal d2, A1=1", regime(1, d2opt[1])[0], 8.0, 1e-12)
check("Q1 via regime() with optimal d2, A1=0", regime(0, d2opt[0])[0], 9.5, 1e-12)

print("== Step 3: static vs optimal (g-formula) ==")
vals = {(d1, d2): regime(d1, d2) for d1, d2 in itertools.product((0, 1), (0, 1))}
check("coupon both weeks 7.40", vals[(1, 1)][0], 7.40, 1e-9)
check("week 1 only 8.00", vals[(1, 0)][0], 8.00, 1e-9)
check("never 8.75", vals[(0, 0)][0], 8.75, 1e-9)
check("optimal (week 2 to non-responders) 9.50", vals[(0, 1)][0], 9.50, 1e-9)
check("optimal regime is best of all 4", float(max(vals, key=lambda k: vals[k][0]) == (0, 1)), 1, 0)
check("both weeks orders 1.54", vals[(1, 1)][1], 1.54, 1e-9)
check("both weeks = most orders", float(max(vals, key=lambda k: vals[k][1]) == (1, 1)), 1, 0)
check("both weeks = least profit", float(min(vals, key=lambda k: vals[k][0]) == (1, 1)), 1, 0)
for k, (v, o) in vals.items():
    print(f"info  regime d1={k[0]}, d2(non-resp)={k[1]}: value {v:.3f}, orders {o:.4f}")

# 'pull-forward' claim: does the week-1 coupon lower or raise weeks 2-4 orders (Y)?
for d2 in (0, 1):
    y1 = P[1]*EYr[1] + (1-P[1])*EYn[(1, d2)]
    y0 = P[0]*EYr[0] + (1-P[0])*EYn[(0, d2)]
    print(f"info  effect of A1 on weeks 2-4 orders (d2={d2} for non-responders): {y1:.4f} - {y0:.4f} = {y1-y0:+.4f}")
y1 = P[1]*EYr[1] + (1-P[1])*EYn[(1, 0)]; y0 = P[0]*EYr[0] + (1-P[0])*EYn[(0, 0)]
check("text: week-1 coupon adds 1.30 - 0.875 = 0.425 total orders", (P[1]*(1+EYr[1]) + (1-P[1])*EYn[(1,0)]) - (P[0]*(1+EYr[0]) + (1-P[0])*EYn[(0,0)]), 0.425, 1e-9)
check("text: worth 4.25 < 5", float(10*0.425 < 5), 1, 0)

print("== Exercise 1 ==")
check("answer: 10 + 2.4 - 5 = 7.4", .40*10*2.5 + .60*(10*.9-5) - 5, 7.4, 1e-9)
check("answer: 0.60*(10*0.9-5) = 2.4", .60*(10*.9-5), 2.4, 1e-9)
check("answer orders 1.0 + 0.54 = 1.54", .40*2.5 + .60*.9, 1.54, 1e-9)

print("== Exercise 2: what the mediator-adjusted regression gives on the table's SMART data ==")
# cell masses: A1 ~ Bern(.5); X2 | A1; A2 ~ Bern(.5) among non-responders only
cells = []
for a1 in (1, 0):
    p = P[a1]
    cells.append((a1, 0, 1, .5*p, EYr[a1]))
    for a2 in (1, 0):
        cells.append((a1, a2, 0, .5*(1-p)*.5, EYn[(a1, a2)]))
X = np.array([[1, a1, a2, x2] for a1, a2, x2, _, _ in cells], float)
w = np.array([c[3] for c in cells]); y = np.array([c[4] for c in cells])
check("cell masses sum to 1", w.sum(), 1, 1e-12)
beta = np.linalg.solve(X.T @ (w[:, None]*X), X.T @ (w*y))
print(f"info  WLS Y ~ 1 + A1 + A2 + X2: coef on A1 = {beta[1]:+.4f}")
check("answer: within-group gaps -0.1, +0.2, 0.0", float(np.allclose([EYr[1]-EYr[0], EYn[(1,0)]-EYn[(0,0)], EYn[(1,1)]-EYn[(0,1)]], [-0.1, 0.2, 0.0])), 1, 0)

print(f"\nhandoutH5: {N_PASS} pass, {N_FLAG} flagged")
