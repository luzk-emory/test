# Independent arithmetic check of notes09.tex (Generative AI in causal analysis).
# The Part A table itself comes from checks/m09_sim.py (slow; run separately); here we check the
# claims derived from the table, the Part B PPI example, and the computation exercise.
import sys
from math import sqrt
R = []
def check(label, claimed, computed, tol=0.0005, sev="error"):
    ok = abs(claimed - computed) <= tol; R.append((ok, sev))
    print(f"[{'ok  ' if ok else ('FAIL' if sev=='error' else 'WARN')}] {label}: text={claimed} computed={computed:.6g}")

# ---------------- Part A table (as printed) ----------------
tab = {  # (sim, conf): oracle, predict, DR, NT  (regrets)
 ('Neural','none'):     (22761, 18838, 1891,  858),
 ('Neural','moderate'): (22761, 17362, 2038,  968),
 ('Boosted','none'):    (23464, 18680, 2200, 1621),
 ('Boosted','moderate'):(23464, 17083, 2383, 1668)}
for k,(o,p,dr,nt) in tab.items():
    check(f"'Predict-then-optimise gives up about 80%' {k}", 0.80, p/o, tol=0.08)
    check(f"'neural T-learner has the lowest regret' {k} (NT<DR<Predict)", 1, float(nt < dr < p), tol=0)
check("'lead over the DR-learner ... from ¥1,033' (Neural, none)", 1033, 1891-858, tol=0)
check("'... to ¥579' (Boosted, none)", 579, 2200-1621, tol=0)
check("'its lead ... halves' ratio 579/1033", 0.5, 579/1033, tol=0.07)
check("'confounder barely changes the causal pipelines' regret' max |change| DR/NT (yuan)", 0,
      max(abs(tab[(s,'moderate')][i]-tab[(s,'none')][i]) for s in ['Neural','Boosted'] for i in (2,3)), tol=200)

# ---------------- Part B: PPI ----------------
N1 = N0 = 10000; n = 1000
f1, f0 = 0.080, 0.100
eff_f = f1 - f0
check("Step 1 'an effect of -0.020'", -0.020, eff_f)
se_f = sqrt(f1*(1-f1)/N1 + f0*(1-f0)/N0)
check("Step 1 'SE 0.004'", 0.004, se_f, tol=0.0005)
check("Step 1 interval lower -0.028", -0.028, eff_f-1.96*se_f)
check("Step 1 interval upper -0.012", -0.012, eff_f+1.96*se_f)
r1, r0 = 0.012, 0.002
t1, t0 = f1+r1, f0+r0
check("Step 3 'Treated 0.080 + 0.012 = 0.092'", 0.092, t1, tol=1e-9)
check("Step 3 'control 0.100 + 0.002 = 0.102'", 0.102, t0, tol=1e-9)
check("Step 3 'effect -0.010'", -0.010, t1-t0, tol=1e-9)
vr = 0.05
se1 = sqrt(f1*(1-f1)/N1 + vr/n); se0 = sqrt(f0*(1-f0)/N0 + vr/n)
check("Step 3 'SE_treated = sqrt(0.080x0.920/10,000 + 0.05/1,000) = 0.0076'", 0.0076, se1, tol=0.00005)
check("Step 3 '0.0077 for control'", 0.0077, se0, tol=0.00005)
se = sqrt(se1**2+se0**2)
check("Step 3 'the effect's SE is 0.0108'", 0.0108, se, tol=0.00005)
check("Step 3 interval lower -0.031", -0.031, (t1-t0)-1.96*se)
check("Step 3 interval upper 0.011", 0.011, (t1-t0)+1.96*se)
check("Step 3 'Half the apparent effect was a measurement artefact'", 0.5, 1-(t1-t0)/eff_f, tol=1e-9)
se_gold = sqrt(t1*(1-t1)/n + t0*(1-t0)/n)
check("Step 3 'Gold labels alone would give SE 0.0132'", 0.0132, se_gold, tol=0.00005)
check("Step 3 'PPI's is about 18% smaller' (stated SEs)", 0.18, 1-0.0108/0.0132, tol=0.005)
check("Step 3 'PPI's is about 18% smaller' (unrounded)", 0.18, 1-se/se_gold, tol=0.005)
check("Step 3 interval includes 0 ('not distinguishable from zero')", 1, float((t1-t0)-1.96*se < 0 < (t1-t0)+1.96*se), tol=0)

# ---------------- Exercise (computation) ----------------
a, b = 0.02, 0.20
check("Answer '-0.020/(1 - 0.02 - 0.20) = -0.026'", -0.026, -0.020/(1-a-b))
p = 0.10; a1, a0 = 0.01, 0.02
t_a = (1-a1-b)*p; t_b = (1-a0-b)*p
check("Answer '(1 - 0.01 - 0.20)(0.10) = 0.079'", 0.079, t_a, tol=1e-9)
check("Answer '(1 - 0.02 - 0.20)(0.10) = 0.078'", 0.078, t_b, tol=1e-9)
check("Answer '+ (0.01 - 0.02) = -0.010'", -0.010, a1-a0, tol=1e-9)
coded = t_a - t_b + (a1-a0)
check("Answer '= -0.009'", -0.009, coded, tol=1e-9)
# direct check against the proposition's E[f|D=d] = alpha_d + (1-alpha_d-beta_d) p_d
Ef1 = a1*(1-p) + (1-b)*p; Ef0 = a0*(1-p) + (1-b)*p
check("Answer -0.009 via E[f|D=d] = alpha_d(1-p_d) + (1-beta_d)p_d", -0.009, Ef1-Ef0, tol=1e-9)

# ---------------- Section 1 propositions: numeric sanity ----------------
tau1, tau0, q = 3.0, 1.0, 0.15
lhs = ((1-q)*tau1 + q*tau0) - (q*tau1 + (1-q)*tau0)
check("Prop modifier: difference = (1-2q)(tau1-tau0)", (1-2*q)*(tau1-tau0), lhs, tol=1e-12)

nbad = [s for ok,s in R if not ok]
print(f"\n{len(R)} checks; {len(R)-len(nbad)} ok; {nbad.count('error')} FAIL; {nbad.count('minor')} WARN")
sys.exit(1 if 'error' in nbad else 0)
