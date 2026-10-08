"""Arithmetic check for handoutH5.tex (Regression discontinuity). Run: python3 handoutH5_check.py

Re-runs the data-generating process of checks/h5_sim.py in memory (same seed, < 1 s) without
writing any file, and compares with the numbers quoted in the text and with h5_bins.csv.
"""
import os
import numpy as np

fails = []
HERE = os.path.dirname(os.path.abspath(__file__))


def chk(label, claimed, computed, tol):
    ok = abs(claimed - computed) <= tol
    print(f"[{'OK ' if ok else 'BAD'}] {label}: text {claimed}, computed {computed:.5f}")
    if not ok:
        fails.append(label)


# ---- Setting ---------------------------------------------------------------
chk("break-even: perks Y60 / renewal Y1,000 = 0.06", 0.06, 60 / 1000, 1e-12)

# ---- Simulation (identical to h5_sim.py) -----------------------------------
rng = np.random.default_rng(5)
n = 60000
R = rng.integers(40, 161, n).astype(float)
age = 30 + 0.05 * (R - 100) + rng.normal(0, 8, n)
D = (R >= 100).astype(float)
p = 0.55 + 0.004 * (R - 100) - 0.00002 * (R - 100) ** 2 + 0.08 * D
Y = rng.binomial(1, np.clip(p, 0, 1))
chk("true jump 0.08 (DGP coefficient)", 0.08, 0.08, 0)


def ll(Y, R, h, c=100):
    w = np.clip(1 - np.abs(R - c) / h, 0, None)
    m = w > 0
    Xm = np.c_[np.ones(m.sum()), (R[m] >= c), R[m] - c, (R[m] - c) * (R[m] >= c)]
    W = w[m]
    XtW = Xm.T * W
    b = np.linalg.solve(XtW @ Xm, XtW @ Y[m])
    e = Y[m] - Xm @ b
    meat = (Xm.T * (W * e) ** 2) @ Xm
    bread = np.linalg.inv(XtW @ Xm)
    V = bread @ meat @ bread
    return b[1], np.sqrt(V[1, 1]), int(m.sum())


chk("naive gap 0.33", 0.33, Y[D == 1].mean() - Y[D == 0].mean(), 0.005)

table = {10: (9375, 0.091, 0.022), 20: (19197, 0.087, 0.015), 30: (28983, 0.084, 0.012)}
est = {}
for h, (nu, t, s) in table.items():
    tt, ss, mm = ll(Y, R, h)
    est[h] = (tt, ss)
    chk(f"table h={h}: members used {nu}", nu, mm, 0)
    chk(f"table h={h}: tau {t}", t, tt, 5e-4)
    chk(f"table h={h}: SE {s}", s, ss, 5e-4)
avg = np.mean([v[0] for v in est.values()])
chk("'Stable across bandwidths, about 0.085'", 0.085, avg, 0.003)

c_lo = int(((R >= 95) & (R < 100)).sum())
c_hi = int(((R >= 100) & (R < 105)).sum())
chk("count 95-99 = 2,503", 2503, c_lo, 0)
chk("count 100-104 = 2,472", 2472, c_hi, 0)
ta, sa, _ = ll(age, R, 20)
chk("age jump 0.30", 0.30, ta, 5e-3)
chk("age jump SE 0.25", 0.25, sa, 5e-3)

# ---- Step 4: interval at h = 20 -------------------------------------------
t20, s20 = est[20]
lo_r, hi_r = 0.087 - 1.96 * 0.015, 0.087 + 1.96 * 0.015
lo_u, hi_u = t20 - 1.96 * s20, t20 + 1.96 * s20
print(f"      CI from rounded table (0.087, 0.015): [{lo_r:.4f}, {hi_r:.4f}]")
print(f"      CI from unrounded sim  ({t20:.4f}, {s20:.4f}): [{lo_u:.4f}, {hi_u:.4f}]")
chk("95% CI lower 0.057 (from unrounded sim)", 0.057, lo_u, 5e-4)
chk("95% CI upper 0.117 (from unrounded sim)", 0.117, hi_u, 5e-4)
print(f"      lower end vs break-even 0.06: lower end is below 0.06 by {0.06 - lo_u:.4f} "
      "(text: 'lower end just touches it')")

# ---- Figure: h5_bins.csv ---------------------------------------------------
bins = np.arange(40, 161, 5)
mids = (bins[:-1] + bins[1:]) / 2
means = np.array([Y[(R >= a) & (R < a + 5)].mean() for a in bins[:-1]])
csv = np.loadtxt(os.path.join(HERE, "..", "..", "meetings", "m08", "h5_bins.csv"), delimiter=",")
ok = csv.shape == (len(mids), 2) and np.allclose(csv[:, 0], mids) and np.allclose(csv[:, 1], means, atol=5e-4)
print(f"[{'OK ' if ok else 'BAD'}] figure h5_bins.csv matches regenerated bin means ({len(mids)} bins)")
if not ok:
    fails.append("h5_bins.csv")
inside = (csv[:, 1] >= 0.2).all() and (csv[:, 1] <= 0.9).all() and (csv[:, 0] >= 40).all() and (csv[:, 0] <= 160).all()
print(f"[{'OK ' if inside else 'BAD'}] figure points inside axis box [40,160]x[0.2,0.9]")
print(f"      note: bins cover R in [40,160); R = 160 ({int((R == 160).sum())} members) is not in any bin")

# ---- Exercise (fuzzy) ------------------------------------------------------
chk("fuzzy RD 0.052/(0.65-0.05) = 0.087", 0.087, 0.052 / (0.65 - 0.05), 5e-4)

print("\nFAILURES:", fails if fails else "none")
