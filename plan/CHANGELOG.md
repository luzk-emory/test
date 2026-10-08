# Slides rebuild (2026-10-08)

## Meeting 1 (slides)
- Rebuilt to match notes v4.1: 39 frames (title, block A 20, block boundary, block B 16, summary). Block A follows notes Sections 1.1 to 1.3, block B Sections 1.4 to 1.6; each part of the FitLife worked example follows the Results it uses.
- Results 1.1 to 1.13 appear as statements with the notes' numbers, titles and box colours; proofs stay in the notes.
- Removed the coffee-chain story (marketing pilot, type counts, segments, Q2 test, rollout totals), whose numbers were not in the notes, and the Floyd, data-roles, exit-ticket and workshop frames. The audit-study point survives as two sentences on the SUTVA frame.
- New frames for block B (causal graphs): chain, fork and collider; blocked paths; Result 1.10 (collider bias); backdoor paths; Result 1.11; standardisation and graph surgery; Simpson's paradox with the FitLife group-class table; the class-attendance question.
- Every number is covered by `shared/checks/notes01_check.py`.

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
