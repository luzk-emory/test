# Pass 1 review: mechanical checks, wording and flow (2026-10-07)

> **Handout numbers (8 October 2026).** Handouts were renumbered to follow the meetings. This document and earlier
> records use the old numbers: old H1 (IV) is now H4, H2 (RD) is H5, H3 (staggered adoption) is H6, H4 (interference) is
> H1, H5 (sequential decisions) is H3, and H6 (neural estimators) is H2.

Scope: all 11 meeting notes, 6 handouts, the notation sheet and `v4notes.sty`. Builds are clean: no LaTeX errors, no undefined references, no em-dashes. Two harmless underfull-box warnings remain (M2, M3).

## 1. Arithmetic: every computed number re-derived

There are now 17 check scripts in `notes-v4-shared/checks/`, one per document (`notesNN_check.py`, `handoutHN_check.py`), about 850 checks in total. `checks/run_all.sh` reruns them all; every script currently passes. The three simulation scripts (`m08_sim.py`, `m09_sim.py`, `m11_sim.py`) were rerun where feasible (`m09_sim.py` takes more than 5 minutes; only its first table row was rerun, and it matches).

### Errors fixed (wrong number or wrong conclusion)

| Where | Problem | Fix |
|---|---|---|
| M4 Step 4 (GATES) | Said only quintile 4 straddles the 0.06 break-even; in fact quintiles 2, 3 and 4 straddle it and the bottom quintile lies wholly below | Sentence corrected |
| M4 Setting / Step 1 | The "discovery half" split table used 2,000 units, the whole stated sample | Sample is now 4,000 shoppers, split into two halves of 2,000. Consistent with the exercise's 300-per-arm leaf |
| H5 Step 3 | Said the week-1 coupon "mostly pulls forward orders" (1.5 vs 1.6). The g-formula shows it *raises* orders by 0.425 a customer, worth ¥4.25 against a ¥5 coupon. The 1.5 vs 1.6 comparison conditions on response, the error the handout itself warns against | Rewritten with the correct reason |
| H5 judgement exercise | Premise "finds it slightly negative" was false for the handout's numbers (the coefficient is +0.04) | Premise removed; answer now lists the within-group gaps |
| M6 fairness (new section) | The 556/444 split broke the γ = 1.25 constraint by one customer | Now 555.6/444.4 (555/445 in whole customers), value ≈ ¥5,415, price ≈ ¥585 |

### Minor fixes (rounding, presentation)
- M2 Step 4: n = 8,174.3, so 8,175 per arm (was "≈ 8,170"); exercise answer updated (24,480 customers, still 62 zones).
- M3 Step 1 table: CIs now at 3 dp, computed from unrounded SEs; header now reads "z vs τ*".
- M4 Step 3: the forest-by-hand table now carries 0.01875 and 0.13125 exactly.
- M8 Step 3: "estimates sit below the truth" changed to "smaller in magnitude than the truth".
- M8 cross-reference: "(Section 1.6)" pointed to the wrong place; now points to Meeting 7.
- M8 Figure 1: the old 300 points were the first 300 rows, whose own slope (−1.12) did not match the plotted line. Now a random 300 points plus 20 binned means of all 40,000 rows; the binned means follow −0.575. Data come from the new `checks/m08_fig.py`.
- M10 Step 5: drift interval is now centred on the estimate, [−0.055, 0.051]. Downstream check: 0.60 − 3 × 0.055 = 0.435 > 0.3.
- M10 exercise: the original SDs (0.40, 0.35) implied an SE for the 6-month DiD (0.110) larger than the single-month event-study SE (0.06). Now SDs are 0.20 and 0.18, giving SE 0.055 and interval [0.39, 0.61]. The answer now makes the point that clustering by only 6 regions may push the interval to the break-even.
- M10 Figure 1 caption states that only months −3 to +2 are shown.
- M11: quarter-1 check now gives 13.94, with 13.95 noted as the unrounded-weights value.
- H1 exercise: SE(π̂) is 0.0034, so F ≈ 35.
- H2 table, h = 30 row: 0.084 (SE 0.012). The interval at h = 20 is [0.057, 0.117], so it falls just below the break-even rather than "touching" it.

### Known, not changed
- **M8 simulation is not seeded.** Gradient boosting in `m08_sim.py` has no `random_state`, so reruns give −0.574 to −0.578. With a fixed seed (`m08_fig.py`) it gives −0.578. The text keeps −0.575, within run-to-run noise. Seeding `m08_sim.py` and updating the text (about six numbers) is a 15-minute job if you want it exact.
- **M9 PPI.** Result PPI assumes the gold sample is independent of the N units; in the example it is a subsample of them. The SE arithmetic is fine; the approximation could be stated in one clause.
- **Citations to confirm before release:**
  - Do-PFN (Robertson et al. 2025): venue given as NeurIPS.
  - "Long story short" (Chernozhukov et al.): listed as a working paper; it may now be published.
  - Mandi et al. 2024: JAIR.

## 2. Notation and cross-references
- Net value is now *v(x)* everywhere. M5 and M9 had used ν, which clashed with M6 and the notation sheet. ν survives only in M8, for D − r(X).
- M9's first pipeline was called "predict-then-optimise". It predicts outcomes, not effects, and the name clashed with M6's new meaning. It is now "outcome prediction"; the table column is "Outcome"; one sentence notes that all three pipelines are plug-in rules in M6's sense.
- Section references inside M6 use `\ref`.

## 3. Wording and labels
- **"Not examinable".** Previously it appeared in three places on every page that had an extension: the header box, the Section 3 title, and every extension box title. Now:
  - It is stated once, in the header box ("For students in the course, Sections 1 and 2 are examinable and Section 3 is not").
  - Section 3 is titled "Extensions and further reading".
  - Extension boxes carry only their topic as title.
  - Handouts have a grey "About this handout" box, no longer the red "Not examinable" banner, ending "It is not examined."
- **Goals line.** Now reads "After reading this, you should be able to:", so it fits both notes and handouts.
- **Phrasing.** Patterns that read as generated were rewritten:
  - "the X is not A but B" decision boxes (M2, H5);
  - stock aphorisms ("precisely wrong", "the mechanics are the point", "earns its keep", "in disguise", "pay for themselves", "quietly");
  - verbless fragments ("One formula, two readings:", "Same CATE, opposite decisions.", "Three readings.");
  - generic "honest" (kept only where it is the technical term, honest trees);
  - a tautology in M7 ("disagreement points to where they differ").

  About 40 edits in all, each local; no section was restructured.

## 4. Page counts
M1 9, M2 8, M3 8, M4 7, M5 8, M6 10, M7 7, M8 6, M9 8, M10 7, M11 6; handouts 5–6. Combined: 116 pages; keys: 120.

## 5. Not covered by this pass
- An independent proof check of each numbered Result (pass 2).
- A student-perspective read (pass 3).
- A full rerun of `m09_sim.py`.
