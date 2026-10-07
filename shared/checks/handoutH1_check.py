"""Arithmetic check for handoutH1.tex (Instrumental variables). Run: python3 handoutH1_check.py"""
import numpy as np

fails = []


def chk(label, claimed, computed, tol):
    ok = abs(claimed - computed) <= tol
    print(f"[{'OK ' if ok else 'BAD'}] {label}: text {claimed}, computed {computed:.5f}")
    if not ok:
        fails.append(label)


N = 20000
n1 = n0 = N // 2  # "a random half of 20,000"

# ---- Step 1 ---------------------------------------------------------------
p1, p0 = 0.30, 0.05
pi = p1 - p0
chk("pi = 0.25", 0.25, pi, 1e-12)
se_pi = np.sqrt(p1 * (1 - p1) / n1 + p0 * (1 - p0) / n0)
chk("SE(pi_hat) = 0.0051", 0.0051, se_pi, 5e-5)
chk("F approx 2,400 (using SE 0.0051)", 2400, (0.25 / 0.0051) ** 2, 50)
chk("F approx 2,400 (using unrounded SE)", 2400, (pi / se_pi) ** 2, 50)
itt = 4.30 - 4.00
chk("ITT = 0.30", 0.30, itt, 1e-12)
se_itt = np.sqrt(3.5**2 / n1 + 3.5**2 / n0)
chk("SE(ITT) about 0.05 (outcome SD 3.5)", 0.05, se_itt, 1e-3)

# ---- Step 2 ---------------------------------------------------------------
chk("pi_A = 0.05", 0.05, p0, 1e-12)
chk("pi_N = 0.70", 0.70, 1 - p1, 1e-12)
chk("pi_C = 0.25", 0.25, 1 - p0 - (1 - p1), 1e-12)
late = itt / pi
chk("LATE = 1.2", 1.2, late, 1e-9)
chk("SE(LATE) about 0.05/0.25 = 0.20", 0.20, 0.05 / 0.25, 1e-12)
# delta-method with first-stage term (cov ignored) for reference
se_late_full = np.sqrt(se_itt**2 + late**2 * se_pi**2) / pi
print(f"      (ref) delta-method SE incl. first-stage term, cov=0: {se_late_full:.4f}")
EYD1, EYD0, EY1D0, EY1D1 = 1.75, 0.35, 3.65, 2.55
chk("E[YD|Z=1]-E[YD|Z=0] = 1.40", 1.40, EYD1 - EYD0, 1e-12)
chk("E[Y(1)|C] = 1.40/0.25 = 5.6", 5.6, (EYD1 - EYD0) / pi, 1e-9)
chk("E[Y(0)|C] = 4.4", 4.4, (EY1D0 - EY1D1) / pi, 1e-9)
chk("consistency: E[Y|Z=1] = 1.75 + 2.55 = 4.30", 4.30, EYD1 + EY1D1, 1e-9)
chk("consistency: E[Y|Z=0] = 0.35 + 3.65 = 4.00", 4.00, EYD0 + EY1D0, 1e-9)
chk("consistency: complier means differ by LATE 1.2", 1.2, 5.6 - 4.4, 1e-9)
print(f"      implied E[Y(1)|A] = {EYD0 / p0:.3f}, E[Y(0)|N] = {EY1D1 / (1 - p1):.3f} (both nonnegative, plausible)")

# ---- Step 3 ---------------------------------------------------------------
chk("margin per invited 10 x 0.30 = 3.00", 3.00, 10 * itt, 1e-9)
chk("waived fees 0.25 x 15 = 3.75", 3.75, pi * 15, 1e-9)
chk("net -0.75", -0.75, 10 * itt - pi * 15, 1e-9)
chk("complier value 10 x 1.2 = 12", 12, 10 * late, 1e-9)
assert 10 * late < 15
print("[OK ] complier: Y12 < Y15 -> no")

# ---- Step 4 ---------------------------------------------------------------
delta = 0.05
chk("exclusion bias delta/pi = 0.2", 0.2, delta / pi, 1e-12)
chk("true complier effect 1.0", 1.0, (itt - delta) / pi, 1e-9)
assert 10 * (itt - delta) / pi < 15
print("[OK ] 'strengthening the conclusion' (Y10 < Y15)")

# ---- Exercise (weak instrument) -------------------------------------------
pi2 = 0.07 - 0.05
chk("ex: pi = 0.02", 0.02, pi2, 1e-12)
se_pi2 = np.sqrt(0.07 * 0.93 / n1 + 0.05 * 0.95 / n0)
chk("ex: SE(pi_hat) approx 0.0034 (binomial, 10,000 per arm)", 0.0034, se_pi2, 1e-4)
F2 = (0.02 / 0.0034) ** 2
chk("ex answer: F approx 35 (with stated SE 0.0034)", 35, F2, 0.5)
print(f"      (ref) F with unrounded SE {se_pi2:.5f}: {(pi2 / se_pi2) ** 2:.1f}")
chk("ex answer: ratio 15", 15, 0.30 / pi2, 1e-9)
chk("ex answer: SE before first-stage term 2.5", 2.5, 0.05 / pi2, 1e-9)
se_full2 = np.sqrt(0.05**2 + 15**2 * 0.0034**2) / pi2
print(f"      (ref) SE after first-stage term (cov=0): {se_full2:.2f}  ('and more after it')")
assert se_full2 > 2.5
chk("ex answer: delta multiplied by 1/0.02 = 50", 50, 1 / pi2, 1e-9)
assert 10 < F2 < 100
print("[OK ] ex answer: F in (10, 100) -> AR-set branch of the stated guard")

# ---- Section 1 constants ---------------------------------------------------
print("      Lee et al. (2022) 104.7 threshold: literature constant, not recomputed")

print("\nFAILURES:", fails if fails else "none")
