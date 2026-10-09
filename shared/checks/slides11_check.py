"""Arithmetic checks for meetings/m11/slides.tex (lecture case: Dana's AI assistant rollout, Case C, Meeting 11 parts).
The slides use their own numbers, not the notes' worked example. The three-donor table is read from slides.tex;
everything else is recomputed from it or from the case's stated givens. Run: python3 slides11_check.py"""
from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction as F
from math import sqrt
from pathlib import Path
import re
FAIL = []
def check(label, claimed, computed, tol=None):
    """claimed: string as printed in the .tex; computed rounded half-up to the same decimals."""
    s = str(claimed); d = len(s.split('.')[1]) if '.' in s else 0
    c = Decimal(repr(round(float(computed), 12))).quantize(Decimal(1).scaleb(-d), ROUND_HALF_UP)
    ok = abs(float(c) - float(s)) < 1e-12 if tol is None else abs(float(computed) - float(s)) <= tol
    print(f"{'OK ' if ok else 'MISMATCH'} | {label}: text {s}, computed {float(computed):.6g}")
    if not ok: FAIL.append(label)

tex = (Path(__file__).resolve().parents[2] / 'meetings/m11/slides.tex').read_text()

# ── Case givens (student.md Parts M11-R1, R3; Meeting 10's estimate) ──
now, live_fl, live_c1, donors = 104, 20, 53, 59
cost, margin = 2500, F(1, 4)
check("break-even 2,500/0.25 = 10,000", "10000", cost / margin)
check("break-even in 000: 10", "10", cost / margin / 1000)
check("flagship 33 weeks before cohort 1", "33", live_c1 - live_fl)
check("flagship 84 weeks live by week 104", "84", now - live_fl)
T0 = live_fl - 1; check("T0 = 19", "19", T0); check("J = 59 donors", "59", donors)
check("fitting window ends at week 19", "19", T0)
check("held-out weeks 15 to 19: five weeks", "5", 19 - 15 + 1)
check("60 units in the placebo set", "60", donors + 1)

# ── The three-donor table, read from the slide ──
def row(name):
    m = re.search(name + r'\s*&\s*(\d+)\s*&\s*(\d+)\s*&\s*(\d+)\s*&\s*(?:\\textbf\{)?(\d+)', tex)
    return [F(int(x)) for x in m.groups()]
Fl, A, B, C = row('Flagship'), row('Donor A'), row('Donor B'), row('Donor C')
assert (Fl, A, B, C) == ([100, 110, 120, 141], [90, 100, 110, 118], [110, 120, 130, 138], [120, 140, 160, 165])
T0toy = 3; check("toy T0 = 3", "3", T0toy)
syn = lambda w, units: [sum(wj * u[t] for wj, u in zip(w, units)) for t in range(4)]
sse = lambda w, units, T=3: sum((Fl[t] - syn(w, units)[t]) ** 2 for t in range(T))

# convex least squares over (A, B, C), on a fine simplex grid (non-circular: no weights assumed)
def best_convex(units, T=3, n=200):
    best = None
    for i in range(n + 1):
        if len(units) == 2:
            w = (F(i, n), 1 - F(i, n)); cand = [w]
        else:
            cand = [(F(i, n), F(j, n), 1 - F(i, n) - F(j, n)) for j in range(n + 1 - i)]
        for w in cand:
            v = sse(w, units, T)
            if best is None or v < best[0]: best = (v, w)
    return best
v, w = best_convex([A, B, C], n=100)
check("full pool: exact fit", "0", v); check("w_A 0.5", "0.5", w[0]); check("w_B 0.5", "0.5", w[1]); check("w_C 0", "0", w[2])
growth = lambda u: [u[t + 1] - u[t] for t in range(2)]
check("A grows 10", "10", growth(A)[0]); check("B grows 10", "10", growth(B)[0]); check("C grows 20", "20", growth(C)[0])
check("flagship grows 10", "10", growth(Fl)[0])
assert all(len(set(growth(u))) == 1 for u in (A, B, C, Fl))          # equal steps before week 4
check("synthetic growth 10 + 10 w_C at w_C = 0", "10", 10 + 10 * 0)
wA = F(110 - 100, 110 - 90); check("week-1 equation gives w_A = 1/2", "0.5", wA)
s0 = syn((F(1, 2), F(1, 2), 0), [A, B, C])
for t, val in enumerate(["100", "110", "120"]): check(f"half A + half B week {t+1}", val, s0[t])
check("synthetic week 4 = 128", "128", s0[3]); check("tau_4 = 13", "13", Fl[3] - s0[3])
check("13,000 of sales", "13000", 1000 * (Fl[3] - s0[3]))

# ── Unconstrained exact fits: w = (1/2 - 5s, 1/2 + 3s, s) ──
for s, (wa, wb, wc, sm, s4, tau) in {F(-1, 2): ("3", "-1", "-0.5", "1.5", "133.5", "7.5"),
                                      F(0): ("0.5", "0.5", "0", "1", "128", "13"),
                                      F(1, 2): ("-2", "2", "0.5", "0.5", "122.5", "18.5"),
                                      F(1): ("-4.5", "3.5", "1", "0", "117", "24")}.items():
    w = (F(1, 2) - 5 * s, F(1, 2) + 3 * s, s); y = syn(w, [A, B, C])
    assert y[:3] == Fl[:3]                                             # exact pre-period fit for every s
    check(f"s={s} w_A", wa, w[0]); check(f"s={s} w_B", wb, w[1]); check(f"s={s} w_C", wc, w[2])
    check(f"s={s} sum of weights 1 - s", sm, sum(w)); check(f"s={s} synthetic week 4", s4, y[3])
    check(f"s={s} effect 13 + 11s", tau, Fl[3] - y[3]); check(f"s={s} effect formula", tau, 13 + 11 * s)
check("range of effects low 7.5", "7.5", 13 + 11 * F(-1, 2)); check("range of effects high 24", "24", 13 + 11 * 1)
assert all(x >= 0 for x in (F(1, 2), F(1, 2), 0)) and [s for s in (F(-1, 2), 0, F(1, 2), 1) if min(F(1, 2) - 5 * s, F(1, 2) + 3 * s, s) >= 0 and 1 - s == 1] == [0]

# ── Factor representation in weeks 1-3: Y = mu1 + t mu2 ──
mu = {}
for k, u in {'A': A, 'B': B, 'C': C, 'F': Fl}.items():
    slope = u[1] - u[0]; level = u[0] - slope; mu[k] = (level, slope)
    assert all(u[t] == level + (t + 1) * slope for t in range(3))
for k, (l, g) in {'A': ("80", "10"), 'B': ("100", "10"), 'C': ("100", "20"), 'F': ("90", "10")}.items():
    check(f"mu_{k} level", l, mu[k][0]); check(f"mu_{k} growth", g, mu[k][1])
check("half mu_A + half mu_B level 90", "90", (mu['A'][0] + mu['B'][0]) / 2); check("growth 10", "10", (mu['A'][1] + mu['B'][1]) / 2)

# ── Fit on week 1 alone: two exact convex fits ──
w2 = (F(2, 3), 0, F(1, 3)); y2 = syn(w2, [A, B, C])
assert y2[0] == Fl[0] == s0[0] and min(w2) >= 0 and sum(w2) == 1
check("2/3 A + 1/3 C week 2", "113.3", y2[1]); check("2/3 A + 1/3 C week 3", "126.7", y2[2])
check("off by 6.7 in week 3", "6.7", y2[2] - Fl[2])
check("its mu level 86.7", "86.7", F(2, 3) * mu['A'][0] + F(1, 3) * mu['C'][0])
check("its mu growth 13.3", "13.3", F(2, 3) * mu['A'][1] + F(1, 3) * mu['C'][1])

# ── Held-out check in the toy: fit on weeks 1-2, predict week 3 ──
v, w = best_convex([A, B, C], T=2, n=100)
check("weeks 1-2 fit exact", "0", v); check("weeks 1-2 w_A", "0.5", w[0]); check("weeks 1-2 w_C", "0", w[2])
check("predicted week 3 = 120", "120", syn(w, [A, B, C])[2]); check("held-out gap 0", "0", Fl[2] - syn(w, [A, B, C])[2])
check("1/2 x 110 + 1/2 x 130", "120", F(110 + 130, 2))

# ── Placebo arithmetic ──
check("smallest p with 3 donors 1/4", "0.25", F(1, 4)); check("smallest p with 59 donors 1/60", "0.017", F(1, donors + 1))
check("toy pre-period RMSPE 0", "0", sqrt(float(sse((F(1, 2), F(1, 2), 0), [A, B, C])) / 3))
check("in-time placebo: fit weeks 1-9 before fake go-live week 10", "9", 10 - 1)

# ── Leave-one-out ──
check("without C: same weights, exact", "0", best_convex([A, B], n=200)[0])
num = sum((C[t] - Fl[t]) * (C[t] - A[t]) for t in range(3)); den = sum((C[t] - A[t]) ** 2 for t in range(3))
check("numerator 3,800", "3800", num); check("denominator 5,000", "5000", den); check("w_A without B 0.76", "0.76", F(num, den))
v, w = best_convex([A, C], n=100); check("grid optimum without B agrees", "0.76", w[0])
yl = syn((F(19, 25), F(6, 25)), [A, C])
for t, val in enumerate(["97.2", "109.6", "122.0", "129.3"]): check(f"without B synthetic week {t+1}", val, yl[t])
for t, val in enumerate(["2.8", "0.4", "-2.0"]): check(f"without B gap week {t+1}", val, Fl[t] - yl[t])
check("without B pre-period RMSPE 2.0", "2.0", sqrt(float(sum((Fl[t] - yl[t]) ** 2 for t in range(3)) / 3)))
check("without B effect 11.7", "11.7", Fl[3] - yl[3])
v, w = best_convex([B, C], n=200); check("without A: B alone", "1", w[0])
assert min(B[0], C[0]) == 110 > Fl[0]                                   # nothing convex gets below 110 in week 1
for t in range(3): check(f"without A gap week {t+1}", "-10", Fl[t] - B[t])
check("without A effect 3.0", "3.0", Fl[3] - B[3])
check("leave-one-out range low 11.7", "11.7", min(Fl[3] - yl[3], Fl[3] - s0[3]))
check("leave-one-out range high 13.0", "13.0", max(Fl[3] - yl[3], Fl[3] - s0[3]))

# ── Synthetic control or DiD ──
pre = lambda u: sum(u[:3]) / 3
check("flagship pre mean 110", "110", pre(Fl)); check("flagship change 31", "31", Fl[3] - pre(Fl))
ew = lambda us: [sum(u[t] for u in us) / len(us) for t in range(4)]
e3, e2 = ew([A, B, C]), ew([A, B])
check("ABC pre mean 120", "120", pre(e3)); check("ABC week 4 140.3", "140.3", e3[3]); check("ABC change 20.3", "20.3", e3[3] - pre(e3))
check("DiD ABC 10.7", "10.7", (Fl[3] - pre(Fl)) - (e3[3] - pre(e3)))
check("AB pre mean 110", "110", pre(e2)); check("AB week 4 128", "128", e2[3]); check("AB change 18", "18", e2[3] - pre(e2))
check("DiD AB 13", "13", (Fl[3] - pre(Fl)) - (e2[3] - pre(e2)))
assert e2[:3] == Fl[:3]
for t, val in enumerate(["106.7", "120", "133.3"]): check(f"ABC path week {t+1}", val, e3[t])
for t, val in enumerate(["-6.7", "-10.0", "-13.3"]): check(f"ABC gap week {t+1}", val, Fl[t] - e3[t])
check("gap widens 3.3 a week", "3.3", (Fl[0] - e3[0]) - (Fl[1] - e3[1]))
check("C grows twice as fast", "2", F(growth(C)[0], growth(A)[0]))
for t, val in enumerate(["106.667", "120", "133.333", "140.333"]): check(f"plot coordinate week {t+1}", val, e3[t])

# ── Dana's table and the memo (Meeting 10's estimate and the flagship's simulated results are case givens) ──
mg = lambda lift000: margin * F(lift000) * 1000 - cost
check("flagship SC margin +1,475", "1475", mg('15.9'))
check("LOO low margin +775", "775", mg('13.1')); check("LOO high margin +1,850", "1850", mg('17.4'))
# cohort numbers come from Meeting 10 (slides10_check.py): DiD 11 (SE 1.22), quarters 8 and 14
check("cohort average of quarters 8 and 14", "11.0", (8 + 14) / 2)
check("cohort margin +250", "250", mg('11.0')); check("first quarter -500", "-500", mg('8.0')); check("second quarter +1,000", "1000", mg('14.0'))
check("0.25 x 11,000 - 2,500", "250", margin * 11000 - cost)
check("CI low 8.6", "8.6", 11.0 - 1.96 * 1.22); check("CI high 13.4", "13.4", 11.0 + 1.96 * 1.22)
assert 11.0 - 1.96 * 1.22 < cost / margin / 1000 < 11.0 + 1.96 * 1.22  # interval includes the break-even
assert F('14.0') > 10 and F('11.0') > 10 and F('15.9') > 10              # point estimates clear the break-even
assert F('13.1') <= F('15.9') <= F('17.4') and F('15.9') < F('18.7') and F('11.0') < F('15.9')
check("flagship margin / cohort margin, almost six", "5.9", mg('15.9') / mg('11.0'))
check("comparison stores 120 - 30 - 1 = 89", "89", 120 - 30 - 1); check("never-treated after cohort 2: 89 - 30", "59", 89 - 30)
check("in 000: 11,000 -> 11.0", "11.0", F(11000, 1000)); check("15,900 -> 15.9", "15.9", F(15900, 1000))
check("18,700 -> 18.7", "18.7", F(18700, 1000))

print(f"\n{len(FAIL)} mismatches: {FAIL}")
