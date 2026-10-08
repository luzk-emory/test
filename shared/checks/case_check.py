"""Arithmetic checks for the case parts rewritten on 8 October 2026 (cases/*/student.md and instructor.md):
Case A Part M2-R6 (noncompliance and the LATE), Case B Meeting 9 (simulators, PPI, text controls),
Case C Meeting 11 (synthetic control vs DiD, memo margins); and, from the M7 to M11 case alignment, Case A Meeting 7,
Case B Meeting 8 and Case C Meeting 10. Run: python3 case_check.py"""
from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction as F
import math
FAIL = []
def check(label, claimed, computed, tol=None):
    """claimed: string as printed; computed rounded half-up to the same decimals."""
    s = str(claimed); d = len(s.split('.')[1]) if '.' in s else 0
    c = Decimal(repr(round(float(computed), 12))).quantize(Decimal(1).scaleb(-d), ROUND_HALF_UP)
    ok = abs(float(c) - float(s)) < 1e-12 if tol is None else abs(float(computed) - float(s)) <= tol
    print(f"{'OK ' if ok else 'MISMATCH'} | {label}: text {s}, computed {float(computed):.6g}")
    if not ok: FAIL.append(label)

# ---------------- Case A, Part M2-R6 ----------------
n1, open1, buy_o1, buy_n1 = 500, 400, 230, 20      # coupon arm
n0, open0, buy_o0, buy_n0 = 500, 360, 180, 20      # control arm
check("A coupon arm bought 250", "250", buy_o1 + buy_n1); check("A control bought 200", "200", buy_o0 + buy_n0)
itt = F(buy_o1 + buy_n1, n1) - F(buy_o0 + buy_n0, n0)
check("A ITT 0.10", "0.10", itt)
check("A openers-only 0.575 - 0.500", "0.075", F(buy_o1, open1) - F(buy_o0, open0))
check("A openers rate coupon 0.575", "0.575", F(buy_o1, open1))
saw_vs_not = F(buy_o1, open1) - F(buy_n1 + buy_o0 + buy_n0, (n1 - open1) + n0)
check("A as-treated 0.208", "0.208", saw_vs_not); check("A not-seen rate 0.367", "0.367", F(240 - 20, 600))
fs = F(open1, n1); check("A first stage 0.80", "0.80", fs)
late = itt / fs; check("A Wald ratio 0.125", "0.125", late)
nt = F(buy_n1, n1 - open1); check("A never-taker rate 0.20", "0.20", nt)
mu_c0 = (F(buy_o0 + buy_n0, n0) - (1 - fs) * nt) / fs
check("A complier untreated rate 0.45", "0.45", mu_c0); check("A 0.36/0.8", "0.36", F(buy_o0 + buy_n0, n0) - (1 - fs) * nt)
check("A complier treated - untreated", "0.125", F(buy_o1, open1) - mu_c0)
m, c = 30, 10
check("A complier break-even 10 x 0.575 / 30", "0.192", c * F(buy_o1, open1) / m)
net_c = m * late - c * F(buy_o1, open1); check("A net per seen coupon", "-2.00", net_c)
check("A complier cost 5.75", "5.75", c * F(buy_o1, open1))
net_n = -c * nt; check("A never-taker cost", "-2.00", net_n)
check("A overall net = M1's -2.00", "-2.00", fs * net_c + (1 - fs) * net_n)
check("A overall net, M1 formula 0.10x30 - 10x0.50", "-2.00", m * itt - c * F(1, 2))

# ---------------- Case A, Meeting 7 (R2 tasks 5-6, R4, R4b) ----------------
w = [(4000, 0.25), (1000, 4)]
sw = sum(n * x for n, x in w); sw2 = sum(n * x * x for n, x in w)
check("A M7 sum of ATT weights", "5000", sw); check("A M7 sum of squared weights", "16250", sw2)
check("A M7 ESS 1,538", "1538", sw ** 2 / sw2); check("A M7 ATE-weight ESS 3,200", "3200", (1000 * 5 + 4000 * 1.25) ** 2 / (1000 * 5 ** 2 + 4000 * 1.25 ** 2))
check("A M7 OLS segment weight 800", "800", 5000 * 0.2 * 0.8); check("A M7 OLS with lapsed dummy", "0.125", (0.05 + 0.20) / 2)
bands = [(2500, 200, 160, 1725, 0.05), (2500, 800, 640, 1275, 0.05), (2500, 1550, 465, 95, 0.20), (2500, 2450, 735, 5, 0.20)]
eh = [F(c, n) for n, c, *_ in bands]
for b, (claim, e) in enumerate(zip(["0.08", "0.32", "0.62", "0.98"], eh)): check(f"A M7 e-hat band {b+1}", claim, e)
wts = [e / (1 - e) for e in eh]
for b, (claim, x) in enumerate(zip(["0.087", "0.47", "1.63", "49"], wts)): check(f"A M7 ATT weight band {b+1}", claim, x)
n0 = [n - c for n, c, *_ in bands]
tot_w = sum(x * m for x, m in zip(wts, n0)); check("A M7 weighted non-recipients", "5000", tot_w)
check("A M7 band 4 share of weight 49%", "49", 100 * wts[3] * n0[3] / tot_w)
ess = lambda idx: sum(wts[i] * n0[i] for i in idx) ** 2 / sum(wts[i] ** 2 * n0[i] for i in idx)
check("A M7 ESS all bands 203", "203", ess(range(4))); check("A M7 ESS trimmed 2,225", "2225", ess(range(3)))
check("A M7 trimmed non-recipients 4,950", "4950", sum(n0[:3])); check("A M7 trimmed recipients 2,550", "2550", sum(c for _, c, *_ in bands[:3]))
check("A M7 trimmed share active 39%", "39", 100 * F(1000, 2550))
check("A M7 SMD of lapsed share", "1.50", (0.80 - 0.20) / math.sqrt((0.16 + 0.16) / 2))
p1 = [F(y1, c) for n, c, y1, y0, _ in bands]; p0 = [F(y0, n - c) for n, c, y1, y0, _ in bands]
check("A M7 pooled", "-0.22", F(sum(y for _, _, y, _, _ in bands), 5000) - F(sum(y for *_, y, _ in bands), 5000))
vw = [n * e * (1 - e) for (n, *_), e in zip(bands, eh)]
check("A M7 OLS band-dummy weights total 1,366", "1366", sum(vw)); check("A M7 OLS band 4 weight 49", "49", vw[3])
check("A M7 OLS on band dummies", "0.120", sum(x * (a - b) for x, a, b in zip(vw, p1, p0)) / sum(vw))
def att(idx):
    n1 = sum(bands[i][1] for i in idx)
    est = sum(F(bands[i][1], n1) * (p1[i] - p0[i]) for i in idx)
    var = sum(float(F(bands[i][1], n1)) ** 2 * (float(p1[i] * (1 - p1[i])) / bands[i][1] + float(p0[i] * (1 - p0[i])) / n0[i]) for i in idx)
    return est, math.sqrt(var), var
e_all, se_all, v_all = att(range(4)); e_tr, se_tr, _ = att(range(3)); e_4, se_4, _ = att([3])
check("A M7 IPW all", "0.17", e_all); check("A M7 IPW SE", "0.022", se_all); check("A M7 IPW interval lower", "0.127", float(e_all) - 1.96 * se_all)
v4 = (2450 / 5000) ** 2 * (0.21 / 2450 + 0.09 / 50); check("A M7 band 4 share of variance 93%", "93", 100 * v4 / v_all)
check("A M7 IPW trimmed", "0.141", e_tr); check("A M7 trimmed SE", "0.011", se_tr)
p1_tr = F(160 + 640 + 465, 2550); check("A M7 trimmed E[Y(1)|D=1]", "0.496", p1_tr)
check("A M7 trimmed break-even", "0.165", 10 * p1_tr / 30); check("A M7 trimmed net", "-0.73", 30 * float(e_tr) - 10 * float(p1_tr))
check("A M7 band 4 lift", "0.20", e_4); check("A M7 band 4 SE", "0.043", se_4); check("A M7 band 4 interval lower", "0.115", float(e_4) - 1.96 * se_4)
check("A M7 band 4 break-even", "0.100", 10 * F(735, 2450) / 30); check("A M7 band 4 net", "3.00", 30 * 0.20 - 10 * 0.30)
check("A M7 active net per coupon", "-6.50", 30 * 0.05 - 10 * 0.80)

# ---------------- Case B, Meeting 9 ----------------
truth = -1.50
for lab, est, bias in [("OLS none", 0.42, "1.92"), ("OLS bands", -1.18, "0.32"), ("DML boost", -1.49, "0.01"),
                       ("DML lasso", -1.41, "0.09"), ("DML boost, overrides", -1.37, "0.13")]:
    check(f"B bias {lab}", bias, est - truth)
check("B M8 -1.56 shifted by testbed bias", "-1.69", -1.56 - 0.13)
regret = {"RM": (1450, 1520), "vendor": (380, 2240), "DML": (690, 760)}
worst = {k: max(v) for k, v in regret.items()}
best = min(worst, key=worst.get); print(f"OK  | B minimax-regret pipeline: {best} ({worst[best]})"); assert best == "DML"
assert sorted(regret, key=lambda k: regret[k][0]) == ["vendor", "DML", "RM"]
assert sorted(regret, key=lambda k: regret[k][1]) == ["DML", "RM", "vendor"]
itt_rate, se_itt = 4.8, 20 * math.sqrt(2 / 500)
check("B member-rate ITT SE", "1.3", se_itt)
check("B backtest gap boosted", "0.2", itt_rate - 4.6); check("B backtest gap neural", "1.4", itt_rate - 3.4)
check("B neural gap in SEs (about one)", "1.1", (itt_rate - 3.4) / se_itt)
# R5: reviews
N = 5000; nG = 200
llm = {"hi": F(22, 100), "cur": F(15, 100)}
conf = {"hi": dict(tp=34, fn=2, fp=12, tn=152), "cur": dict(tp=26, fn=2, fp=4, tn=168)}
check("B model-label effect 0.07", "0.07", llm["hi"] - llm["cur"])
gold, model_g, tpr, fpr, ppi, var_r = {}, {}, {}, {}, {}, {}
for a, k in conf.items():
    assert sum(k.values()) == nG
    gold[a] = F(k["tp"] + k["fn"], nG); model_g[a] = F(k["tp"] + k["fp"], nG)
    tpr[a] = F(k["tp"], k["tp"] + k["fn"]); fpr[a] = F(k["fp"], k["fp"] + k["tn"])
    corr = gold[a] - model_g[a]; ppi[a] = llm[a] + corr
    r = [-1] * k["fp"] + [1] * k["fn"] + [0] * (k["tp"] + k["tn"])
    mu = sum(r) / nG; var_r[a] = sum((x - mu) ** 2 for x in r) / nG
check("B gold rate higher 0.18", "0.18", gold["hi"]); check("B gold rate current 0.14", "0.14", gold["cur"])
check("B gold effect 0.04", "0.04", gold["hi"] - gold["cur"])
check("B catches higher 34/36", "0.944", tpr["hi"]); check("B flags higher 12/164", "0.073", fpr["hi"])
check("B catches current 26/28", "0.929", tpr["cur"]); check("B flags current 4/172", "0.023", fpr["cur"])
check("B 1 - alpha - beta, current arm", "0.905", tpr["cur"] - fpr["cur"])
check("B non-differential effect 0.905 x 0.04", "0.036", (tpr["cur"] - fpr["cur"]) * (gold["hi"] - gold["cur"]))
check("B model rate in subsample, higher 46/200", "0.23", model_g["hi"]); check("B model rate in subsample, current 30/200", "0.15", model_g["cur"])
check("B correction higher", "-0.05", gold["hi"] - model_g["hi"]); check("B correction current", "-0.01", gold["cur"] - model_g["cur"])
check("B PPI higher 0.17", "0.17", ppi["hi"]); check("B PPI current 0.14", "0.14", ppi["cur"])
check("B PPI effect 0.03", "0.03", ppi["hi"] - ppi["cur"])
check("B rectifier variance higher", "0.0675", var_r["hi"]); check("B rectifier variance current", "0.0299", var_r["cur"])
se_hi = math.sqrt(float(llm["hi"] * (1 - llm["hi"])) / N + var_r["hi"] / nG)
se_cu = math.sqrt(float(llm["cur"] * (1 - llm["cur"])) / N + var_r["cur"] / nG)
check("B PPI SE higher arm", "0.019", se_hi); check("B PPI SE current arm", "0.013", se_cu)
se_ppi = math.sqrt(se_hi ** 2 + se_cu ** 2); check("B PPI SE of effect", "0.023", se_ppi)
se_gold = math.sqrt(0.18 * 0.82 / nG + 0.14 * 0.86 / nG); check("B gold-only SE", "0.037", se_gold)
check("B PPI CI lower", "-0.015", 0.03 - 1.96 * 0.023); check("B PPI CI upper", "0.075", 0.03 + 1.96 * 0.023)
check("B outcome variance higher 0.18x0.82", "0.15", 0.18 * 0.82); check("B outcome variance current", "0.12", 0.14 * 0.86)
el = lambda x: math.log(1 + x) / math.log(1.08)
check("B Q3 elasticity", "-1.72", el(-0.124))
check("B Q3 CI lower", "-2.07", el(-0.124 - 1.96 * 0.012)); check("B Q3 CI upper", "-1.38", el(-0.124 + 1.96 * 0.012))
check("B SE factor 9% -> 1%", "3", math.sqrt(0.09 / 0.01)); check("B SE factor 9% -> 6%", "1.22", math.sqrt(0.09 / 0.06))
check("B SE at 6%", "0.04", 0.03 * math.sqrt(0.09 / 0.06)); check("B SE at 1%", "0.09", 0.03 * math.sqrt(0.09 / 0.01))
check("B model-label rise in points", "7", 100 * (llm["hi"] - llm["cur"]))

# ---------------- Case C, Meeting 11 ----------------
fl = [100, 110, 120, 141]; A = [90, 100, 110, 118]; B = [110, 120, 130, 138]; C = [120, 140, 160, 165]
syn = [(a + b) / 2 for a, b in zip(A, B)]
assert syn[:3] == fl[:3]; check("C synthetic week 4", "128", syn[3]); check("C SC effect", "13", fl[3] - syn[3])
pre = lambda x: sum(x[:3]) / 3
dd = lambda donors: (fl[3] - pre(fl)) - (sum(d[3] for d in donors) / len(donors) - sum(pre(d) for d in donors) / len(donors))
check("C flagship pre mean", "110", pre(fl)); check("C donors pre mean (A,B,C)", "120", sum(pre(d) for d in (A, B, C)) / 3)
check("C donors week 4 (A,B,C)", "140.3", sum(d[3] for d in (A, B, C)) / 3)
check("C flagship change", "31", fl[3] - pre(fl)); check("C donors change (A,B,C)", "20.3", sum(d[3] for d in (A, B, C)) / 3 - 120)
check("C equal-weight DiD (A,B,C)", "10.7", dd((A, B, C)))
check("C donors change (A,B)", "18", (A[3] + B[3]) / 2 - (pre(A) + pre(B)) / 2); check("C equal-weight DiD (A,B)", "13", dd((A, B)))
# leave-B-out refit, as in the key: 0.76 A + 0.24 C
w = 0.76; loo = [w * a + (1 - w) * c for a, c in zip(A, C)]
check("C no-B synthetic wk1", "97.2", loo[0]); check("C no-B synthetic wk4", "129.3", loo[3], tol=0.05)
check("C no-B effect", "11.7", fl[3] - loo[3], tol=0.05)
margin = 0.25
check("C memo margin, 11,000", "250", margin * 11000 - 2500)
check("C memo margin, first quarter 8,000", "-500", margin * 8000 - 2500)
check("C memo margin, second quarter 14,000", "1000", margin * 14000 - 2500)
check("C flagship margin 15,900", "1475", margin * 15900 - 2500)
check("C flagship margin almost six times the cohort's", "5.9", (margin * 15900 - 2500) / (margin * 11000 - 2500))
# Case C, Meeting 10 (R3 task 6, R4, R5)
c1 = [176, 178, 180, 182, 192, 200]; c0 = [146, 148, 150, 152, 154, 156]
gap = [a - b for a, b in zip(c1, c0)]
check("C TWFE six quarters 17 - 6", "11", (sum(c1[4:]) / 2 - sum(c1[:4]) / 4) - (sum(c0[4:]) / 2 - sum(c0[:4]) / 4))
check("C cohort 1 change 17", "17", sum(c1[4:]) / 2 - sum(c1[:4]) / 4); check("C comparison change 6", "6", sum(c0[4:]) / 2 - sum(c0[:4]) / 4)
es = [g - gap[3] for g in gap]; assert es == [0, 0, 0, 0, 8, 14]
se_s = math.sqrt(36 / 30 + 25 / 89); check("C store-level SE 1.22", "1.22", se_s)
d_hat = -(1 * es[2] + 2 * es[1] + 3 * es[0]) / 14; check("C drift estimate 0", "0", d_hat)
check("C drift SE 1.22/sqrt(14)", "0.33", 1.22 / math.sqrt(14)); check("C drift bound 1.96 x 0.326", "0.64", 1.96 * 1.22 / math.sqrt(14))
check("C delta* four cells", "0.5", (11 - 10) / (5.5 - 3.5)); check("C delta* TWFE six quarters", "0.33", (11 - 10) / (5.5 - 2.5))
check("C delta* Q6 coefficient", "2.0", (14 - 10) / (6 - 4))
rho, T = 0.8, 26
cov = lambda i, j: rho ** abs(i - j)
before, after = range(T), range(T, 2 * T)
v = (sum(cov(i, j) for i in after for j in after) + sum(cov(i, j) for i in before for j in before)
     - 2 * sum(cov(i, j) for i in after for j in before)) / T ** 2
ratio = v / (2 / T); check("C AR(1) variance ratio", "6.70", ratio); check("C SE factor", "2.59", math.sqrt(ratio))
se_naive = 1.22 / 2.59; check("C naive SE", "0.47", se_naive)
check("C naive CI lower", "10.1", 11 - 1.96 * 0.47); check("C naive CI upper", "11.9", 11 + 1.96 * 0.47)
check("C store CI lower", "8.6", 11 - 1.96 * 1.22); check("C store CI upper", "13.4", 11 + 1.96 * 1.22)
se_r = math.sqrt(9 / 3 + 6.25 / 9); check("C region SE", "1.92", se_r)
check("C region CI lower", "6.7", 11 - 2.23 * 1.92); check("C region CI upper", "15.3", 11 + 2.23 * 1.92)
# Case B, Meeting 8 (R3 interval, R4 discount, R5 sensitivity)
check("B clustered CI lower", "-1.62", -1.56 - 1.96 * 0.03); check("B clustered CI upper", "-1.50", -1.56 + 1.96 * 0.03)
pstar = lambda k: 200 * k / (k - 1)
check("B P* at kappa 1.50", "600", pstar(1.50)); check("B P* at kappa 1.62", "523", pstar(1.62))
e_a, e_r, m0a, m1a, m0r, m1r = 0.5, 0.9, 50, 54, 60, 72
with_ = (0.5 * e_a * m1a + 0.5 * e_r * m1r) / (0.5 * e_a + 0.5 * e_r)
without = (0.5 * (1 - e_a) * m0a + 0.5 * (1 - e_r) * m0r) / (0.5 * (1 - e_a) + 0.5 * (1 - e_r))
check("B discount with 65.6", "65.6", with_); check("B discount without 51.7", "51.7", without)
check("B discount naive 13.9", "13.9", with_ - without)
wa, wr = e_a * (1 - e_a), e_r * (1 - e_r)
check("B PLM weight airport", "0.25", wa); check("B PLM weight resort", "0.09", wr)
check("B PLM theta 6.1", "6.1", (wa * 4 + wr * 12) / (wa + wr))
check("B ATE 8.0", "8.0", 0.5 * 4 + 0.5 * 12); check("B ATT 9.1", "9.1", (0.5 * e_a * 4 + 0.5 * e_r * 12) / (0.5 * e_a + 0.5 * e_r))
check("B weighting alone 81", "81", e_r * m1r / 0.8); check("B AIPW 71.75", "71.75", 74 + e_r * (m1r - 74) / 0.8)
check("B AIPW error -0.25", "-0.25", (74 - m1r) * (1 - e_r / 0.8))
check("B AIPW score 42.0", "42.0", 12 - (57 - 60) / (1 - e_r))
ovb = lambda ry, rd: math.sqrt(ry * rd / (1 - rd)) * 3.0
for q, b in [(0.01, "0.03"), (0.02, "0.06"), (0.05, "0.15"), (0.10, "0.32")]:
    check(f"B OVB at {q:.0%}", b, ovb(q, q))
check("B 10% range lower", "-1.88", -1.56 - ovb(0.10, 0.10)); check("B 10% range upper", "-1.24", -1.56 + ovb(0.10, 0.10))
q = 0.05
while q / math.sqrt(1 - q) * 3.0 < 0.24: q += 1e-6
check("B robustness value 7.7%", "7.7", 100 * q)
check("B event flag 1x bias", "0.15", ovb(0.06, 0.04)); check("B event flag 2x bias", "0.31", ovb(0.12, 0.08))
check("B 1x range lower", "-1.71", -1.56 - ovb(0.06, 0.04)); check("B 1x range upper", "-1.41", -1.56 + ovb(0.06, 0.04))
check("B 2x range lower", "-1.87", -1.56 - ovb(0.12, 0.08)); check("B 2x range upper", "-1.25", -1.56 + ovb(0.12, 0.08))
k = 1.0
while ovb(0.06 * k, 0.04 * k) < 0.24: k += 1e-4
check("B overturned at about 1.6x the flag", "1.6", k)

print(f"\n{len(FAIL)} mismatches: {FAIL}")
