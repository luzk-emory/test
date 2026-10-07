"""Arithmetic check for notes08.tex (Meeting 8, Double machine learning). Run: python3 notes08_check.py

Hand-computable values only. The simulation outputs (naive +1.20, DML -0.575 / -0.524, SEs, R^2 0.74,
residual SDs 0.304 / 0.101, rain benchmark 0.18 / 0.32) come from checks/m08_sim.py, which takes > 5 min;
they are listed at the bottom as SIM values and only checked for mutual consistency here.
"""
import os
import numpy as np
from scipy.optimize import brentq

fails = []
HERE = os.path.dirname(os.path.abspath(__file__))


def chk(label, claimed, computed, tol):
    ok = abs(claimed - computed) <= tol
    print(f"[{'OK ' if ok else 'BAD'}] {label}: text {claimed}, computed {computed:.5f}")
    if not ok:
        fails.append(label)


# ---- Setting --------------------------------------------------------------
f, m = 4.0, 6.0
chk("profit elasticity add-on f/(6+f) = 0.4 at f=4", 0.4, f / (m + f), 1e-12)
breakeven = -0.4

# ---- Step 2: six rows -----------------------------------------------------
Dt = np.array([0.12, -0.05, 0.08, -0.10, 0.02, -0.07])
Yt = np.array([-0.09, 0.01, -0.03, 0.08, -0.02, 0.03])
chk("sum D~Y~ = -0.0242", -0.0242, (Dt * Yt).sum(), 1e-10)
chk("sum D~^2 = 0.0386", 0.0386, (Dt**2).sum(), 1e-10)
chk("theta_hat six rows = -0.63", -0.63, (Dt * Yt).sum() / (Dt**2).sum(), 5e-3)

# ---- Step 3 ---------------------------------------------------------------
theta = -0.575
chk("'a quarter of fee variation is left' (1 - 0.74)", 0.25, 1 - 0.74, 0.011)
fac = 1.1 ** theta * (m + 4.4) / (m + 4.0)
chk("profit factor (1.1)^-0.575 x 10.4/10 = 0.985", 0.985, fac, 5e-4)
chk("'a 1.5% loss'", 0.015, 1 - fac, 5e-4)
true_theta = -0.6
print(f"      'Both estimates sit below the truth': -0.575 and -0.524 vs truth {true_theta}: "
      f"numerically ABOVE (closer to zero); below only in magnitude")

# ---- Figure 1 -------------------------------------------------------------
res = np.loadtxt(os.path.join(HERE, "..", "..", "meetings", "m08", "m08_resid_sample.csv"), delimiter=",")
chk("figure: 300 residual pairs", 300, res.shape[0], 0)
xin = (np.abs(res[:, 0]) <= 0.35).mean()
yin = (np.abs(res[:, 1]) <= 1.1).mean()
print(f"      figure: share of points inside x-range +/-0.35: {xin:.3f}, y-range +/-1.1: {yin:.3f}")
sl = (res[:, 0] * res[:, 1]).sum() / (res[:, 0] ** 2).sum()
print(f"      figure: slope through the 300 plotted points = {sl:.3f} (line drawn at -0.575; sample of 300 is noisy)")
print(f"      figure: sd(D~)={res[:,0].std():.3f}, sd(Y~)={res[:,1].std():.3f} on the 300 points")

# ---- Step 4: sensitivity (Cinelli-Hazlett style) -------------------------
sdY, sdD = 0.304, 0.101
ratio = sdY / sdD
chk("ratio 0.304/0.101 = 3.0", 3.0, ratio, 0.05)


def bound(r2y, r2d, ratio=3.0):
    return np.sqrt(r2y * r2d / (1 - r2d)) * ratio


b05 = bound(0.05, 0.05)
chk("bound at R2 = 0.05 both sides = 0.15", 0.15, b05, 5e-3)
chk("interval lower -0.73", -0.73, theta - b05, 5e-3)
chk("interval upper -0.42", -0.42, theta + b05, 5e-3)
assert theta + b05 < breakeven
print("[OK ] interval upper end still below -0.4")
need = abs(theta - breakeven)
chk("bias needed to reach break-even 0.175", 0.175, need, 1e-9)
rv = brentq(lambda r: bound(r, r) - need, 1e-6, 0.9)
chk("robustness value (equal R2) about 0.057 (ratio 3.0)", 0.057, rv, 5e-4)
rv_u = brentq(lambda r: bound(r, r, ratio) - need, 1e-6, 0.9)
print(f"      (ref) robustness value with unrounded ratio {ratio:.4f}: {rv_u:.4f}")

# Benchmark: rain explains 0.18 (fee) and 0.32 (orders)
r2d_rain, r2y_rain = 0.18, 0.32
b_third = bound(r2y_rain / 3, r2d_rain / 3)
print(f"      benchmark: k=1/3 of rain on BOTH sides -> bias bound {b_third:.3f} (need {need})")
b_third_d = bound(r2y_rain, r2d_rain / 3)
print(f"      benchmark: 1/3 rain on fee side, full rain on order side -> {b_third_d:.3f}")
b_third_d_only = bound(0.0, r2d_rain / 3)
assert b_third > need
print("[OK ] 'a third as strong as rain ... would overturn' (true for k=1/3 on both sides)")
kstar = brentq(lambda k: bound(k * r2y_rain, k * r2d_rain) - need, 1e-6, 1 / 0.18 - 1e-6)
print(f"      (ref) smallest common fraction k of rain that flips: {kstar:.3f}")
# required order-side R2 if the fee side is exactly 1/3 of rain
r2y_need = (need / 3.0) ** 2 * (1 - r2d_rain / 3) / (r2d_rain / 3)
print(f"      (ref) with fee-side R2 = 0.06, order-side R2 needed to flip = {r2y_need:.3f}")

# ---- Exercise ---------------------------------------------------------------
chk("exercise: profit elasticity at f=4 = -0.575 + 0.4 < 0", -0.175, theta + f / (m + f), 1e-9)
assert theta + f / (m + f) < 0
print("[OK ] exercise answer: profit elasticity negative -> small cut")

# ---- SIM values (from m08_sim.py, not re-run here) ----------------------------
print("\nSIM values quoted in text (verify by running m08_sim.py, ~5+ min):")
for k, v in [("naive slope", "+1.20"), ("DML-GB theta (SE)", "-0.575 (0.015)"),
             ("DML-lasso theta (SE)", "-0.524 (0.015)"), ("fee model OOF R2", "0.74"),
             ("sd(Y~ - theta D~), sd(D~)", "0.304, 0.101"), ("rain partial R2 fee, orders", "0.18, 0.32")]:
    print(f"      {k}: {v}")

print("\nFAILURES:", fails if fails else "none")
