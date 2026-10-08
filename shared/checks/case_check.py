"""Arithmetic checks for the case parts rewritten on 8 October 2026 (cases/*/student.md and instructor.md):
Case A Part M2-R6 (noncompliance and the LATE), Case B Meeting 9 (simulators, PPI, text controls),
Case C Meeting 11 (synthetic control vs DiD, memo margins). Run: python3 case_check.py"""
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
check("C memo margin, 12,400", "600", margin * 12400 - 2500)
check("C memo margin, first quarter 11,200", "300", margin * 11200 - 2500)
check("C memo margin, second quarter 13,800", "950", margin * 13800 - 2500)

print(f"\n{len(FAIL)} mismatches: {FAIL}")
