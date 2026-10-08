# Slides rebuild (2026-10-08)

## Schedule and syllabus
- `schedule.xlsx`: M5B adds isotonic recalibration and the paired comparison of two policies; M6A adds the price of fairness and capacity (critical fractile); M6B replaces "plug-in vs direct learning" with the predict-then-optimise / decision-focused / policy-learning spectrum; M7B adds the outcome-free design stage. New column G lists each meeting's handout.
- `syllabus.tex`, draft 3, regenerated from the spreadsheet: Tuesday/Thursday calendar; exams at M5 and M11 (block A); proposal presentations at M8; assignments A1 to A4 and Labs 0 to 10 replace projects P1 to P4 and notebooks; handouts H1 to H6 (not examined); examinable material is the slides plus notes Sections 1 and 2; AI policy per lab and assignment; bonus reading; final-project appendices as in judgement call 6; lecture cases versus the notes' worked examples. M9 (generative AI) replaces IV in the "where the counterfactual comes from" table. Weights carried over from draft 2 and marked for confirmation. Undecided items are shown in red brackets (`\tbd`), replacing the `soul` highlighter, which is not in the course's TeX setup.

## Meeting 1 (slides)
- Rebuilt on the lecture's own case (Lin's coupon programme at the coffee chain, case A releases R1 to R5), aligned with notes v4.1 in estimands, assumptions, notation, Result statements (1.1 to 1.13, same numbers and titles) and topic order. The notes' FitLife example is not reproduced; the summary frame points to it.
- 44 frames: title, block A (notes 1.1 to 1.3) 21, block boundary, block B (notes 1.4 to 1.6) 20, summary.
- New in block B, on the coffee-chain case: graph frames (chain, fork, collider; blocked paths; backdoor paths with segment and app opens; graph surgery), a Q3 win-back campaign as the Simpson reversal (pooled -0.22, within +0.05 and +0.20; standardised ATE 0.125, ATT 0.17), and a collider question on `app_opens_q2`.
- Removed: Today's Plan, the Floyd frames (two sentences kept on the SUTVA frame), the prediction-approach frame (one sentence kept), Verifying with the Two Segments, the workshop frame (block C is now Lab 0). Merged the two type-count frames into one.
- Notation now follows `shared/notation.tex` (ATE, ATT, ATU, $\tau_i$, $\Pr$); box colours follow the notes.
- New check script `shared/checks/slides01_check.py` covers every number on the slides; `run_all.sh` now also runs `slides*_check.py`.

# v4.1 (2026-10-07): items brought back from the old decks, plus calibration and decision-focused learning

## Meeting 5 (notes05)
- New: "Recalibrating a score" with Result "Isotonic calibration" (block averages of transformed or DR outcomes; order preserved; proof).
- Worked example Step 5: one sentence on what isotonic calibration would have done.
- New computation exercise: pool-adjacent-violators on six bins, threshold before and after.
- Goals and reading list updated (van der Laan et al., ICML 2023).

## Meeting 6 (notes06), 7 -> 10 pages
- New subsection "Group constraints and the price of fairness": Result (group-specific thresholds, multiplier, dV/dgamma), four-fifths rule, illustration 3:1 -> 1.25:1, price about 585 (555/445 customers), eta about 6,667.
- New subsection "When the mean is not enough: capacity": Result (nonlinear payoff needs each arm's distribution, not the joint), two kitchens (same CATE, opposite decisions), Result (critical fractile) with pinball loss, z_alpha versus kappa, CQTE remark.
  Correction to the old deck: the fractile sets a capacity; the binary promote decision needs E[pi(Y(1))] and E[pi(Y(0))], which experiments identify. The old deck's "quantile of the effect distribution" is not identified and is not needed.
- "Learning the policy directly" rewritten as "From predict-then-optimise to policy learning": three routes, decision-focused learning as policy learning over the optimiser-induced class, DR scores as labels. New Result "Policy learning is weighted classification" (proof); Step 5 reinterpreted with it.
- Two new exercises (capacity computation; fairness plus conservative rule judgement).
- Section 3: fairness stub replaced by "Decision-focused learning in practice" and "Distributional effects". Reading: Elmachtoub-Grigas 2022, Zhao et al. 2012, Kasy-Abebe 2021.
- Goals and pitfall box updated. Section reference to "What the sum assumes" now uses \ref.

## Meeting 9 (notes09), 7 -> 8 pages
- One sentence after "Regret counts only misclassified units" linking it to Meeting 6.
- New extension: three routes on one testbed (optional lab or assignment).

## Notation sheet
- Added F_d(y|x), Gamma_i, c_u, c_o, kappa. Margins tightened to stay on one page.

## Combined PDFs
- all: 110 -> 115 pages; keys rebuilt.
