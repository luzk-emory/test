# Slides rebuild (2026-10-08)

## Schedule and syllabus
- `schedule.xlsx`: M5B adds isotonic recalibration and the paired comparison of two policies; M6A adds the price of fairness and capacity (critical fractile); M6B replaces "plug-in vs direct learning" with the predict-then-optimise / decision-focused / policy-learning spectrum; M7B adds the outcome-free design stage. New column G lists each meeting's handout.
- `syllabus.tex`, draft 3, regenerated from the spreadsheet: Tuesday/Thursday calendar; exams at M5 and M11 (block A); proposal presentations at M8; assignments A1 to A4 and Labs 0 to 10 replace projects P1 to P4 and notebooks; handouts H1 to H6 (not examined); examinable material is the slides plus notes Sections 1 and 2; AI policy per lab and assignment; bonus reading; final-project appendices as in judgement call 6; lecture cases versus the notes' worked examples. M9 (generative AI) replaces IV in the "where the counterfactual comes from" table. Weights carried over from draft 2 and marked for confirmation. Undecided items are shown in red brackets (`\tbd`), replacing the `soul` highlighter, which is not in the course's TeX setup.

## Planning documents brought up to date
- `revision-plan.md`: status table (M2 notes Section 1.9, H4 refocus, renumbering, schedule columns, rebuilt M1 and M2 decks with their checks, case checks, the merge state of this branch, no tags yet, `map.md` still missing; the README no longer claims a `v4.1` tag); work remaining now starts at M3 slides and the syllabus's `\tbd` items; slide-rebuild notes updated (50 carried frames left in M3 to M6, critique frames C2 to C6 left, notes' order wins, a check script per deck); decisions of 8 October listed one per line.
- `design-plan.md`: retitled as the design record, with a new Section 0 (what was built, actual page counts, changes since v4.1, where files are). It now uses the new handout numbers; the handout table gains built lengths and H4's classical-IV scope; the M2 coverage row adds Section 1.9; notes on how `v4notes.sty`, the separate key files and `notes-v4.tex` delivery became `coursenotes.sty`, `\def\KEY{}` and single files in git; new Decision 5 (noncompliance belongs to M2).

## Handouts renumbered in meeting order; schedule columns
- Handouts now follow the meetings: H1 interference (M2, was H4), H2 neural estimators (M3, was H6), H3 sequential decisions (M6, was H5), H4 instrumental variables (M7, was H1), H5 regression discontinuity (M8, was H2), H6 staggered adoption (M10, was H3). Files, headers, check scripts (`handoutHN_check.py`, `h5_sim.py`, `h6_check.py`, `meetings/m08/h5_bins.csv`) and every reference in the notes, handouts, slides, cases, syllabus, schedule, README and brief were updated. M4's protocol steps H1-H3 (discover, estimate, recommend) are unrelated and unchanged. Two references now point to Meeting 2 instead of the IV handout (M1 notes on monotonicity; the RD handout's use of the LATE theorem). Entries below this one, `design-plan.md` and the pass-1 review keep the old numbers, with a mapping note.
- `schedule.xlsx`: the Misc column is split into Release and Due. The syllabus's weekly table follows: the handout moves into the Block C cell, and a new "Out / due" column lists releases and deadlines.

## Handout H1 (instrumental variables)
- Refocused on classical IV, with no overlap with M2 Section 1.9. Section 1 now opens with "From a randomised offer to an outside shifter" (independence and relevance stated; exclusion, monotonicity and Results 1.13-1.15 cited from M2, not restated), adds "Arguing for an instrument" (origin of Z, balance, zero-first-stage groups, placebo outcomes), and keeps complier means, exclusion and monotonicity failures, 2SLS with strata, the delta method, Anderson-Rubin and locality. The former Results "Two effects of the instrument", "Type shares" and "The LATE theorem" are removed (they are M2 Results 1.13-1.15).
- New worked example: a QuickBite Plus campaign chosen by city managers, not randomised. Pooled ratio 4.4 (confounded by city size) against 1.2 within size and by 2SLS with size indicators (SE about 0.22); compliers order 5.8 without Plus and 7.0 with it; billboards give a direct effect of 0.05 (measured on corporate accounts), corrected LATE 1.0; the campaign and Plus decisions. The weak-instrument and rainfall exercises are kept. `handoutH1_check.py` rewritten for the new numbers.

## Meeting 2 (slides)
- Rebuilt on the coffee-chain case (Case A, M2 releases R1 to R4 and R6; R5 memo at home), aligned with the M2 notes: Results 1.1 to 1.16 with the notes' numbers and wording, in the notes' order. Block A follows notes 1.1 to 1.5 (analyse as drawn, sample-ratio check, Fisher, Neyman and the conservative SE, superpopulation and robust SEs, the break-even test, net value, transport); block B follows 1.6 to 1.9 (the next test, sample size, CUPED, interference and the design effect, peeking, noncompliance and the LATE).
- 36 frames: title, block A 15, block boundary, block B 18, summary. Removed: the map frame (in M1), Today's Plan, critique C1, the Lab 1 frame (now one line in the summary). The two campaign frames are merged. New: sample-ratio check, the conservative-SE figure, peeking and many metrics, and six noncompliance frames.
- `schedule.xlsx` and the syllabus M2 rows now follow the notes' order: transport ends block A and CUPED is in block B.
- New check script `shared/checks/slides02_check.py` (0 mismatches). Case A's release table updated for the new deck.

## Decisions of 8 October, and the cases
- Noncompliance in an RCT (ITT, compliance types, LATE) closes M2; classical IV (outside shifters, 2SLS, weak instruments) stays in Handout H1 with M7, as bonus reading. `schedule.xlsx` (M2B, judgement call 1, M2 bonus reading adds Angrist, Imbens and Rubin 1996), the syllabus, the brief and the README updated.
- M2 notes: new Section 1.9 "Noncompliance: the ITT and the LATE" with Assumptions 1.11-1.12 (exclusion, monotonicity) and Results 1.13-1.16 (two effects of assignment, type shares, the LATE theorem, one-sided noncompliance), ported from H1 and stated for a randomised offer. Section 1.2, the judgement answer, Section 3 (new extension pointing to H1) and the reading list (Imbens and Rubin ch. 23-24; Angrist, Imbens and Rubin 1996) updated; one new goal. H1 gains a pointer to M2 Section 1.9.
- M2 notes Step 6, corrected: it said 40% of offered customers redeemed a ¥10 discount, which would cost ¥4.00 per offer, not the stated ¥1.50. Redemption is now 15% (0.15 x ¥10 = ¥1.50), and the step shows that the LATE (¥12.27) against ¥10 per user is the ITT against ¥1.50 per offer, rescaled. `notes02_check.py` updated.
- A3 is due Friday of Week 5, so nothing is due the weekend before Exam II.
- Reading-and-critique exercises are dropped for now: removed from the syllabus and the brief; v2 critique frames are to be deleted as decks are rebuilt.
- Case A: new Part M2-R6, "Who saw the coupon?" (one-sided noncompliance on the Q2 test: ITT 0.10, first stage 0.80, LATE 0.125, compliers' untreated rate 0.45; openers-only 0.075 and as-treated 0.208 shown wrong; net per seen coupon -¥2.00, consistent with M1). The till discount is stated so that M1's cost model holds.
- Case B: Meeting 9 rewritten for generative AI on Meridian (simulator, estimator and pipeline testbeds with a backtest, synthetic guests, LLM-coded reviews with PPI, text embeddings as controls, memo). The old IV parts are kept as Bonus B1–B4; the full-test ladder and the IV memo were dropped.
- Case C: Meeting 11 rewritten for synthetic control only (flagship, three donors, design freeze and placebos, SC vs DiD, memo using M10's estimate). The old staggered-adoption parts are kept as Bonus B1–B3.
- New check script `shared/checks/case_check.py` for the rewritten case parts; `run_all.sh` runs it.

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
