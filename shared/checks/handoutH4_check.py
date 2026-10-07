"""Arithmetic checks for handoutH4.tex (Interference). Run: python3 handoutH4_check.py"""
from decimal import Decimal, ROUND_HALF_UP
import numpy as np
FAIL = []
def check(label, claimed, computed, tol=None):
    s = str(claimed); d = len(s.split('.')[1]) if '.' in s else 0
    c = Decimal(repr(round(float(computed), 12))).quantize(Decimal(1).scaleb(-d), ROUND_HALF_UP)
    ok = abs(float(c) - float(s)) < 1e-12 if tol is None else abs(float(computed) - float(s)) <= tol
    print(f"{'OK ' if ok else 'MISMATCH'} | {label}: text {s}, computed {float(computed):.6g}")
    if not ok: FAIL.append(label)

q0, q1, K = 0.30, 0.40, 0.30
comp = lambda p, K=K: min(1.0, K / (p * q1 + (1 - p) * q0))
gte = lambda K=K: min(q1, K) - min(q0, K)   # everyone treated vs no one
print("INFO | Result 'Shared supply' precondition q0 <= K < q1:", q0 <= K < q1)
# Step 1: 50/50
check("requests average 0.35", "0.35", 0.5 * q1 + 0.5 * q0)
c50 = comp(0.5)
check("completion 0.30/0.35 = 0.857", "0.857", c50)
check("treated orders 0.343", "0.343", q1 * c50); check("control orders 0.257", "0.257", q0 * c50)
check("lift 0.086", "0.086", (q1 - q0) * c50); check("lift = 33%", "33", 100 * (q1 - q0) / q0)
check("decision box '33% more'", "33", 100 * (q1 * c50) / (q0 * c50) - 100)
check("net per treated 8x0.086 - 3x0.343 = -0.34", "-0.34", 8 * (q1 - q0) * c50 - 3 * q1 * c50)
check("net per treated with rounded inputs", "-0.34", 8 * 0.086 - 3 * 0.343)
# Step 2
check("GTE = 0", "0", gte()); check("citywide cost 3 x 0.30 = 0.90", "0.90", 3 * min(q1, K))
# Step 3 table
for h, cc, tr, co, de in [(0.2, '0.938', '0.375', '0.281', '0.094'), (0.5, '0.857', '0.343', '0.257', '0.086'), (0.8, '0.789', '0.316', '0.237', '0.079')]:
    c = comp(h)
    check(f"h={h} completion", cc, c); check(f"h={h} treated orders", tr, q1 * c)
    check(f"h={h} control orders", co, q0 * c); check(f"h={h} DE(h)", de, (q1 - q0) * c)
check("control curve at h=0 -> 0.30 (model)", "0.30", q0 * comp(0)); check("treated curve at h=1 -> 0.30 (model)", "0.30", q1 * comp(1))
hs = np.array([.2, .5, .8]); ctrl = np.array([q0 * comp(h) for h in hs]); trt = np.array([q1 * comp(h) for h in hs])
check("linear extrapolation of control orders to h=0 ~ 0.30", "0.30", np.polyval(np.polyfit(hs, ctrl, 1), 0), tol=0.006)
check("linear extrapolation of treated orders to h=1 ~ 0.30", "0.30", np.polyval(np.polyfit(hs, trt, 1), 1), tol=0.006)
check("GTE from extrapolation = 0", "0", q1 * comp(1) - q0 * comp(0))
# Exercise: K = 0.35
K2 = 0.35
print("INFO | exercise precondition q0 <= K < q1:", q0 <= K2 < q1)
c2 = comp(0.5, K2)
check("exercise completion = 1", "1", c2); check("exercise treated 0.40", "0.40", q1 * c2); check("exercise control 0.30", "0.30", q0 * c2)
check("exercise lift 0.10", "0.10", (q1 - q0) * c2); check("exercise GTE 0.05", "0.05", gte(K2))
check("exercise GTE is half the test estimate", "0.5", gte(K2) / ((q1 - q0) * c2))
print(f"\n{len(FAIL)} mismatches: {FAIL}")
