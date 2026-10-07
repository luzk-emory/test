"""Arithmetic check for notes05.tex (Evaluating Targeting Policies).
Run: python3 checks/notes05_check.py   (numpy only)
"""
import numpy as np

N_PASS, N_FLAG = 0, 0


def check(label, computed, claimed, tol):
    global N_PASS, N_FLAG
    ok = abs(computed - claimed) <= tol
    N_PASS += ok; N_FLAG += (not ok)
    print(f"{'PASS' if ok else 'FLAG'}  {label}: claimed {claimed}, computed {computed:.6g}")
    return ok


print("== Section 1 ==")
check("25%-treated: treated buyer counts 1/0.25 = 4 times", 1/0.25, 4, 0)
eff = np.array([.20, .10, .00, -.10])
check("four groups: ATE 0.05", eff.mean(), 0.05, 1e-12)
for j, q in enumerate([.050, .075, .075, .050]):
    phi = (j+1)/4
    check(f"Q(phi={phi}) = {q}", phi*eff[:j+1].mean(), q, 1e-12)

print("== Section 2: setting ==")
check("break-even lift 1/120 = 0.0083", 1/120, 0.0083, 0.00005)

print("== Step 1: ten rows ==")
score = np.array([.09, .08, .07, .06, .04, .03, .02, .01, .00, -.01])
pi = (np.argsort(-score).argsort() < 4).astype(int)
D = np.array([1, 0, 1, 0, 1, 0, 1, 0, 1, 0]); Y = np.array([1, 0, 0, 0, 1, 1, 0, 1, 0, 0])
check("pi column = top four", float((pi == [1, 1, 1, 1, 0, 0, 0, 0, 0, 0]).all()), 1, 0)
agree = (D == pi)
check("D=pi? column", float((agree == np.array([1, 0, 1, 0, 0, 1, 0, 1, 0, 1], bool)).all()), 1, 0)
last = pi*(2*D-1)*2*Y
check("last column = [2,0,...,0]", float((last == [2, 0, 0, 0, 0, 0, 0, 0, 0, 0]).all()), 1, 0)
check("agreeing rows outcomes 1,0,1,1,0", float(list(Y[agree]) == [1, 0, 1, 1, 0]), 1, 0)
V = np.mean(agree*Y/0.5)
V0 = np.mean((1-D)*Y/0.5)
check("V_hat(pi) = 0.6", V, 0.6, 1e-12)
check("V_hat(0) = 0.4", V0, 0.4, 1e-12)
check("gain 0.2", V-V0, 0.2, 1e-12)
check("average of last column 2/10", last.mean(), 0.2, 1e-12)

print("== Step 2: decile table ==")
e = np.array([.050, .035, .025, .015, .010, .005, .002, .000, -.002, -.005])
inc_c = [100, 170, 220, 250, 270, 280, 284, 284, 280, 270]
prof_c = [10000, 16400, 20400, 22000, 22400, 21600, 20080, 18080, 15600, 12400]
mean_c = [.0500, .0425, .0367, .0313, .0270, .0233, .0203, .0178, .0156, .0135]
toc_c = [.0365, .0290, .0232, .0178, .0135, .0098, .0068, .0043, .0021, .0000]
inc = np.cumsum(2000*e)
prof = 120*inc - 1.00*2000*np.arange(1, 11)
mean_t = np.cumsum(e)/np.arange(1, 11)
ate = e.mean()
toc = mean_t - ate
for k in range(10):
    check(f"decile {k+1} incremental {inc_c[k]}", inc[k], inc_c[k], 1e-9)
    check(f"decile {k+1} net profit {prof_c[k]}", prof[k], prof_c[k], 1e-6)
    check(f"decile {k+1} mean effect {mean_c[k]}", mean_t[k], mean_c[k], 0.00005 + 1e-12)
    check(f"decile {k+1} TOC {toc_c[k]}", toc[k], toc_c[k], 0.00005 + 1e-12)
check("emailing everyone nets 12,400", prof[-1], 12400, 1e-6)
check("profit peaks at five deciles", np.argmax(prof)+1, 5, 0)
check("peak 22,400", prof.max(), 22400, 1e-6)
check("decile 5 (0.010) is last above 0.0083", float(e[4] > 1/120 and e[5] < 1/120), 1, 0)
fig = [0, 10, 16.4, 20.4, 22, 22.4, 21.6, 20.08, 18.08, 15.6, 12.4]
check("figure profit-curve coords = table / 1000", np.abs(np.r_[0, prof/1000] - fig).max(), 0, 1e-9)
check("random-order line ends at 12.4", prof[-1]/1000, 12.4, 1e-9)

print("== Step 3: RATE ==")
q = np.arange(1, 11)/10
check("AUTOC ~ 0.0143 (mean of TOC column)", np.mean(toc_c), 0.0143, 0.00005)
check("AUTOC from exact TOC", toc.mean(), 0.0143, 0.00005)
check("Qini-type RATE 0.0046 (mean of q*TOC)", np.mean(q*np.array(toc_c)), 0.0046, 0.00005)

print("== Step 4/5 ==")
check("70-subscription gap", 340-270, 70, 0)
check("gap worth ~ 8,400", 70*120, 8400, 0)
check("top half on eval sample = 270 (table decile 5)", inc[4], 270, 1e-9)
thr = 0.0083/2
sel = e > thr
check("scores x2: true effect above 0.0042", thr, 0.0042, 0.00005)
check("deciles 1-6 emailed", sel.sum(), 6, 0)
check("earn 21,600", prof[sel.sum()-1], 21600, 1e-6)
check("800 less", prof.max()-prof[5], 800, 1e-6)

print("== Exercise 1 (paired comparison) ==")
m, k = 120, 1.0
vals = {"emailed subscriber": 2*(m-k), "emailed non-sub": 2*(-k), "non-emailed sub": -2*m, "non-emailed non-sub": 0}
for lab, cl in zip(vals, [238, -2, -240, 0]):
    check(f"d_i {lab} = {cl}", vals[lab], cl, 1e-12)
p1, p0 = .04, .03
mean5 = .5*(p1*238 - (1-p1)*2) - .5*(p0*240)
check("decile-5 mean 0.20", mean5, 0.20, 1e-9)
check("= 120*0.01 - 1", 120*.01-1, 0.20, 1e-9)
Ed2 = .5*(p1*238**2 + (1-p1)*4) + .5*(p0*240**2)
check("E[d^2] on decile-5 rows ~ 1,999", Ed2, 1999, 0.5)
sd = np.sqrt(0.1*Ed2 - (0.1*mean5)**2)
check("sd(d) ~ 14.1", sd, 14.1, 0.05)
se = sd/np.sqrt(20000)
check("SE = 0.10 per customer", se, 0.10, 0.005)
check("difference 0.02 per customer", 0.1*mean5, 0.02, 1e-9)
check("~ 400 in total", 0.1*mean5*20000, 400, 1e-6)
check("matches table 22,400 - 22,000", prof[4]-prof[3], 400, 1e-6)
check("a fifth of one SE", 0.02/se, 0.2, 0.01)
check("decile 5 effect 0.04-0.03 = table 0.010", p1-p0, e[4], 1e-12)
# simulation sanity check of the SE
rng = np.random.default_rng(0)
n = 20000; ins = np.arange(n) < 2000; Dm = rng.integers(0, 2, n)
reps = []
for _ in range(400):
    Ys = np.where(Dm == 1, rng.random(n) < .04, rng.random(n) < .03)
    R = 120*Ys - Dm
    d = ins*(Dm*R/.5 - (1-Dm)*R/.5)
    reps.append(d.mean())
check("simulated SD of mean d over 400 reps ~ 0.10", np.std(reps), 0.10, 0.01)

print("== Exercise 2 (PAV) ==")


def pav(y, w=None):
    y = list(map(float, y)); w = [1.0]*len(y) if w is None else list(w)
    blocks = [[y[i], w[i], 1] for i in range(len(y))]
    i = 0
    while i < len(blocks)-1:
        if blocks[i][0] > blocks[i+1][0] + 1e-15:
            a, b = blocks[i], blocks[i+1]
            nw = a[1]+b[1]
            blocks[i] = [(a[0]*a[1]+b[0]*b[1])/nw, nw, a[2]+b[2]]
            del blocks[i+1]
            i = max(i-1, 0)
        else:
            i += 1
    out = []
    for v, _, c in blocks:
        out += [v]*c
    return np.array(out)


psi = [.002, .006, .004, .010, .018, .016]
cal = pav(psi)
check("PAV result 0.002,0.005,0.005,0.010,0.017,0.017",
      np.abs(cal - [.002, .005, .005, .010, .017, .017]).max(), 0, 1e-12)
sc = np.array([.004, .008, .012, .016, .020, .024])
raw_bins = list(np.where(sc > 0.0083)[0]+1); cal_bins = list(np.where(cal > 0.0083)[0]+1)
check("raw scores treat bins 3-6", float(raw_bins == [3, 4, 5, 6]), 1, 0)
check("calibrated treat bins 4-6", float(cal_bins == [4, 5, 6]), 1, 0)

print(f"\nnotes05: {N_PASS} pass, {N_FLAG} flagged")
