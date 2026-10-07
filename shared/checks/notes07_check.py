"""Arithmetic check for notes07.tex (Meeting 7, Observational data). Run: python3 notes07_check.py"""
import numpy as np

fails = []


def chk(label, claimed, computed, tol):
    ok = abs(claimed - computed) <= tol
    print(f"[{'OK ' if ok else 'BAD'}] {label}: text {claimed}, computed {computed:.5f}")
    if not ok:
        fails.append(label)


# ---- Setting ------------------------------------------------------------
chk("break-even: call Y30 / renewal Y500 = 0.06", 0.06, 30 / 500, 1e-12)

n = {"H": 1000, "L": 1000}
called = {"H": 800, "L": 100}
e = {s: called[s] / n[s] for s in n}
chk("e_hat high = 0.8", 0.8, e["H"], 1e-12)
chk("e_hat low = 0.1", 0.1, e["L"], 1e-12)
mu1 = {"H": 0.90, "L": 0.60}
mu0 = {"H": 0.85, "L": 0.50}
tau = {s: mu1[s] - mu0[s] for s in n}
chk("table Effect high = 0.05", 0.05, tau["H"], 1e-12)
chk("table Effect low = 0.10", 0.10, tau["L"], 1e-12)
unc = {s: n[s] - called[s] for s in n}

# ---- Step 1: effective sample sizes -------------------------------------
def ess(groups):  # groups: list of (count, weight)
    s = sum(c * w for c, w in groups)
    s2 = sum(c * w * w for c, w in groups)
    return s * s / s2

chk("ATE ESS called '356 of the 900'", 356, ess([(800, 1 / 0.8), (100, 1 / 0.1)]), 0.5)
chk("ATE ESS uncalled '655 of the 1,100'", 655, ess([(200, 1 / 0.2), (900, 1 / 0.9)]), 0.5)
chk("ATT odds weight high e/(1-e) = 4", 4, 0.8 / 0.2, 1e-12)
chk("ATT odds weight low = 1/9", 1 / 9, 0.1 / 0.9, 1e-12)
chk("ATT ESS uncalled '252 of 1,100'", 252, ess([(200, 4), (900, 1 / 9)]), 0.5)
share_hi = 200 * 4 / (200 * 4 + 900 / 9)
print(f"      ATT weight share on 200 uncalled high members = {share_hi:.3f} ('rests mostly on')")
assert share_hi > 0.5

# ---- Step 2: naive -------------------------------------------------------
yc = (800 * 0.90 + 100 * 0.60) / 900
yu = (200 * 0.85 + 900 * 0.50) / 1100
chk("called renew 0.867", 0.867, yc, 5e-4)
chk("uncalled renew 0.564", 0.564, yu, 5e-4)
chk("naive difference 0.303", 0.303, yc - yu, 5e-4)
chk("'five times the break-even' (ratio)", 5, (yc - yu) / 0.06, 0.1)
att = (800 * 0.05 + 100 * 0.10) / 900
chk("ATT 0.056", 0.056, att, 5e-4)
chk("selection bias 0.247 (= naive - ATT)", 0.247, (yc - yu) - att, 5e-4)
chk("ATT 0.056 + bias 0.247 = 0.303 (rounded parts add)", 0.303, 0.056 + 0.247, 1e-9)

# ---- Step 3: standardisation --------------------------------------------
ate = 0.5 * 0.05 + 0.5 * 0.10
chk("ATE 0.075", 0.075, ate, 1e-12)
chk("ATU 0.091", 0.091, (200 * 0.05 + 900 * 0.10) / 1100, 5e-4)

# ---- Step 4: IPW ---------------------------------------------------------
ey1 = (800 * 1.25 * 0.90 + 100 * 10 * 0.60) / 2000
ey0 = (200 * 5 * 0.85 + 900 * (1 / 0.9) * 0.50) / 2000
chk("IPW E[Y(1)] = 0.750", 0.750, ey1, 5e-4)
chk("IPW E[Y(0)] = 0.675", 0.675, ey0, 5e-4)
chk("IPW ATE = 0.075", 0.075, ey1 - ey0, 5e-4)

# ---- Step 5: OLS weights, verified by an actual regression ---------------
w = {s: n[s] * e[s] * (1 - e[s]) for s in n}
chk("OLS weight high n e(1-e) = 160", 160, w["H"], 1e-9)
chk("OLS weight low = 90", 90, w["L"], 1e-9)
tols = (w["H"] * 0.05 + w["L"] * 0.10) / (w["H"] + w["L"])
chk("tau_OLS = 0.068 (formula)", 0.068, tols, 5e-4)
# build the 2,000-row dataset with exact cell means and regress
rows = []
for s in n:
    hi = 1.0 if s == "H" else 0.0
    for d, cnt, mu in [(1, called[s], mu1[s]), (0, unc[s], mu0[s])]:
        k = int(round(mu * cnt))  # number renewing (exact integers here)
        assert abs(k - mu * cnt) < 1e-9
        rows += [(1, d, hi, 1.0)] * k + [(1, d, hi, 0.0)] * (cnt - k)
A = np.array(rows)
b = np.linalg.lstsq(A[:, :3], A[:, 3], rcond=None)[0]
chk("tau_OLS = 0.068 (regression on 2,000 rows)", 0.068, b[1], 5e-4)

# ---- Step 6: AIPW under misspecified outcome / propensity ---------------
def aipw(m1, m0, eh):
    tot = 0.0
    for s in n:
        # mean of phi over the stratum, using exact cell means
        tot += n[s] * (m1[s] - m0[s]
                       + e[s] * (mu1[s] - m1[s]) / eh[s]
                       - (1 - e[s]) * (mu0[s] - m0[s]) / (1 - eh[s]))
    return tot / sum(n.values())

chk("AIPW, pooled outcome model (0.867/0.564), right e -> 0.075", 0.075,
    aipw({s: yc for s in n}, {s: yu for s in n}, e), 1e-9)
chk("AIPW, right outcome model, e = 0.45 for all -> 0.075", 0.075,
    aipw(mu1, mu0, {s: 0.45 for s in n}), 1e-9)
print(f"      (contrast) AIPW with both wrong = {aipw({s: yc for s in n}, {s: yu for s in n}, {s: 0.45 for s in n}):.4f}")

# Result AIPW proof identity, random numeric check
rng = np.random.default_rng(0)
for _ in range(5):
    M1, M0, m1_, m0_, ee, et = rng.uniform(0.05, 0.95, 6)
    lhs = (m1_ - m0_ + ee * (M1 - m1_) / et - (1 - ee) * (M0 - m0_) / (1 - et)) - (M1 - M0)
    rhs = (M1 - m1_) * (ee / et - 1) - (M0 - m0_) * ((1 - ee) / (1 - et) - 1)
    assert abs(lhs - rhs) < 1e-12
print("[OK ] AIPW proof identity E[phi|X]-tau = (mu1-m1)(e/e~-1) - (mu0-m0){(1-e)/(1-e~)-1}")

# ---- Decision ------------------------------------------------------------
assert att < 0.06 and tau["L"] > 0.06 and tau["H"] < 0.06
print("[OK ] decision: ATT 0.056 < 0.06; low (0.10) pays; high (0.05) does not")

# ---- Exercise (elite stratum) -------------------------------------------
# e = 500/500 = 1 for elite; overlap-population ATE/ATT unchanged
assert 500 / 500 == 1.0
print("[OK ] exercise: elite e = 1; overlap-population ATE 0.075, ATT 0.056 unchanged")

print("\nFAILURES:", fails if fails else "none")
