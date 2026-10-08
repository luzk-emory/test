"""Arithmetic checks for handoutH2.tex (Neural estimators). Run: python3 handoutH2_check.py"""
from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction as F
import numpy as np
FAIL = []
def check(label, claimed, computed, tol=None):
    s = str(claimed); d = len(s.split('.')[1]) if '.' in s else 0
    c = Decimal(repr(round(float(computed), 12))).quantize(Decimal(1).scaleb(-d), ROUND_HALF_UP)
    ok = abs(float(c) - float(s)) < 1e-12 if tol is None else abs(float(computed) - float(s)) <= tol
    print(f"{'OK ' if ok else 'MISMATCH'} | {label}: text {s}, computed {float(computed):.6g}")
    if not ok: FAIL.append(label)

def joint(pU, pD_U, pY_UD):
    """Return P(D=d, Y=y) as dict from P(U=1), P(D=1|U=u), P(Y=1|U=u,D=d)."""
    J = {}
    for d in (0, 1):
        for yv in (0, 1):
            tot = 0
            for u in (0, 1):
                pu = pU if u else 1 - pU; pd = pD_U(u) if d else 1 - pD_U(u); py = pY_UD(u, d) if yv else 1 - pY_UD(u, d)
                tot += pu * pd * py
            J[(d, yv)] = tot
    return J
def summarise(J):
    pD1 = J[(1, 0)] + J[(1, 1)]
    return pD1, J[(1, 1)] / pD1, J[(0, 1)] / (1 - pD1)

# Result 'nonid': model A vs model B
A = joint(F(1, 2), lambda u: F(1, 2), lambda u, d: F(2, 5) + F(1, 5) * d)
B = joint(F(1, 2), lambda u: F(1, 5) + F(3, 5) * u, lambda u, d: F(1, 3) + F(1, 3) * u)
tauA = F(1, 5); tauB = sum((F(1, 2)) * ((F(1, 3) + F(1, 3) * u) - (F(1, 3) + F(1, 3) * u)) for u in (0, 1))
check("model A tau = 0.2", "0.2", tauA); check("model B tau = 0", "0", tauB)
pA, a1, a0 = summarise(A); pB, b1, b0 = summarise(B)
check("model A P(D=1)=0.5", "0.5", pA); check("model B P(D=1)=0.5 (same D margin)", "0.5", pB)
check("A: P(Y=1|D=1)=0.6", "0.6", a1); check("A: P(Y=1|D=0)=0.4", "0.4", a0)
check("B: P(Y=1|D=1)=0.6", "0.6", b1); check("B: P(Y=1|D=0)=0.4", "0.4", b0)
ok = A == B; print(f"{'OK ' if ok else 'MISMATCH'} | joint (D,Y) identical in A and B: {ok}")
if not ok: FAIL.append("joint A==B")
check("B: P(U=1|D=1)=0.8", "0.8", F(1, 2) * F(4, 5) / pB); check("B: P(U=1|D=0)=0.2", "0.2", F(1, 2) * F(1, 5) / (1 - pB))
check("B: 0.8*2/3+0.2*1/3 = 0.6", "0.6", F(4, 5) * F(2, 3) + F(1, 5) * F(1, 3))
check("B: 0.2*2/3+0.8*1/3 = 0.4", "0.4", F(1, 5) * F(2, 3) + F(4, 5) * F(1, 3))

# Section 2 worked example (CFR)
check("CFR tau_hat(c) = 0.6 - 0.2 = 0.4", "0.4", 0.6 - 0.2); check("true tau(c) = 0.6 - 0.5 = 0.1", "0.1", 0.6 - 0.5)
check("reported chain effect 0.40 equals mu1(c) minus region-(a) control mean", "0.40", 0.6 - 0.2)

# Exercise: P(D=1|U) = 0.3 + 0.4U
pU = F(1, 2); pD = lambda u: F(3, 10) + F(2, 5) * u
pD1 = pU * pD(1) + (1 - pU) * pD(0)
check("exercise P(D=1) still 0.5", "0.5", pD1)
check("exercise P(U=1,D=1) = 0.35", "0.35", pU * pD(1)); check("exercise P(U=1,D=0) = 0.15", "0.15", pU * (1 - pD(1)))
r1 = pU * pD(1) / pD1; r0 = pU * (1 - pD(1)) / (1 - pD1)
check("exercise P(U=1|D=1)=0.7", "0.7", r1); check("exercise P(U=1|D=0)=0.3", "0.3", r0)
M = np.array([[float(r1), float(1 - r1)], [float(r0), float(1 - r0)]])
a1_, a0_ = np.linalg.solve(M, [0.6, 0.4])
check("exercise a1 - a0 = 0.5", "0.5", a1_ - a0_); check("exercise a0 = 0.25", "0.25", a0_); check("exercise a1 = 0.75", "0.75", a1_)
ok = 0 <= a0_ <= 1 and 0 <= a1_ <= 1; print(f"{'OK ' if ok else 'MISMATCH'} | exercise a0,a1 in [0,1]: {ok}")
if not ok: FAIL.append("valid probability")
Jx = joint(pU, pD, lambda u, d: a0_ + (a1_ - a0_) * u); _, e1, e0 = summarise({k: float(v) for k, v in Jx.items()})
check("exercise reproduces P(Y=1|D=1)=0.6", "0.6", e1); check("exercise reproduces P(Y=1|D=0)=0.4", "0.4", e0)
print("INFO | weaker U-D link (0.4 vs 0.6) needs stronger U-Y link (0.5 vs 1/3):", float(a1_ - a0_) > 1 / 3)
print(f"\n{len(FAIL)} mismatches: {FAIL}")
