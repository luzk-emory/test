# Slides rebuild (2026-10-08)

## Schedule and syllabus
- `schedule.xlsx`: M5B adds isotonic recalibration and the paired comparison of two policies; M6A adds the price of fairness and capacity (critical fractile); M6B replaces "plug-in vs direct learning" with the predict-then-optimise / decision-focused / policy-learning spectrum; M7B adds the outcome-free design stage. New column G lists each meeting's handout.
- `syllabus.tex`, draft 3, regenerated from the spreadsheet: Tuesday/Thursday calendar; exams at M5 and M11 (block A); proposal presentations at M8; assignments A1 to A4 and Labs 0 to 10 replace projects P1 to P4 and notebooks; handouts H1 to H6 (not examined); examinable material is the slides plus notes Sections 1 and 2; AI policy per lab and assignment; bonus reading; final-project appendices as in judgement call 6; lecture cases versus the notes' worked examples. M9 (generative AI) replaces IV in the "where the counterfactual comes from" table. Weights carried over from draft 2 and marked for confirmation. Undecided items are shown in red brackets (`\tbd`), replacing the `soul` highlighter, which is not in the course's TeX setup.

## Meetings 4 to 6 (slides), Case A, schedule and syllabus
- M4 (33 frames): block A causal trees and honesty (Results 1.1-1.3; the winner's curse by hand; the discover/estimate/recommend protocol on Region 2's coupon test, now 4,000 members in two halves of 2,000), block B causal forests (Result 1.4, local centering, interval cautions, variable importance, Result 1.5, GATES). Half-B results now come from explicit counts; the simulated forest sub-segment (38%) and the merged executive interval are dropped.
- M5 (21 frames, one lecture block): Results 1.1-1.9 in the notes' order. New exact example: the forest splits each segment into two groups (L1, L2, A1, A2), carrying the gain, profit and Qini curves, RATE, ranking versus calibration, and the evaluation of three frozen lists (segment rule ¥1.50, forest top 5,000 ¥0.75, engine's cut-off ¥1.625; paired SEs 0.36 and 0.15). Isotonic recalibration on six bins; Result 1.8 with an exact K-candidate example; the paired SE by hand on the 80 rows. All simulated values (1.46 to 2.31) dropped.
- M6 (34 frames): block A allocation (Results 1.1-1.9) on the Region 2 push, with new coupon depths, the price of fairness (North/South, ¥470), and capacity with the critical fractile (two stores; plan for 480); block B policy learning (Results 1.10-1.11, the spectrum, DR scores, weighted classification on eight members, policy trees, regret, holdouts, bandits, what the sum assumes). The conservative rule now bounds net value, not the lift.
- New check scripts `slides04_check.py`, `slides05_check.py`, `slides06_check.py` (0 mismatches). No deck carries notes or handout pointers, lab material or in-class prompts.
- Case A: release table retimed for M4 to M6 (M4 all in block A; M5 in block B; M6 in block A). M4-R1 states the test size; M4-R3 gains the two-noisy-splits, winner's-curse and split-cost tasks (the split-cost task now uses 250 per arm at 0.50/0.30); M4-R4 gives counts; M4-R5 gives 95% and 98.75% intervals for the four committed leaves and drops the forest sub-segment. M5-R1's T-learner list becomes the engine's cut-off; M5-R4 uses the four-group example and paired SEs. M6's cap task moves to R2 with a one-day send (¥3,500 vs ¥4,750); the take-home check bounds money (-¥0.73). Instructor keys follow.
- `schedule.xlsx` and the syllabus: M4, M5 and M6 rows reordered to follow the notes (winner's curse before honesty; policy value before curves and calibration; sure-thing cost, spending risk and "what the sum assumes" added; EWM before weighted classification).

## Meeting 3 (slides)
- Rebuilt on the coffee-chain case (Case A, M3 releases R1, R2, R2b, R3), aligned with the M3 notes: Assumptions 1.1-1.2 and Results 1.3-1.11 with the notes' numbers and wording, in the notes' order. Block A follows notes 1.1 to 1.4 (estimand, prognostic versus modifier, identification and the support/confounding distinction, the targeting rule and the value of targeting, the interaction model, the gap test, multiple testing and GATEs); block B follows 1.5 and 1.6 (S-, T- and X-learners, transformed outcome, DR pseudo-outcome, R-learner, TARNet, why outcome accuracy cannot choose, fit/choose/assess, pitfalls).
- 30 frames: title, road map, block A 13, block boundary, block B 14, summary. Removed: the course-map frame (its M9 box was out of date), Today's Plan, critique C2, the two discussion frames (now one self-contained "Support or Confounding?" table), the in-pairs prediction frame and "The Ladder" (its numbers were unchecked `\NUM` placeholders from a simulation that does not exist yet), the Lab 2 frame and the deadline line. All CARRIED comments are gone.
- New, on the coffee-chain numbers: the value of targeting (-¥1.75 for everyone, ¥0 for nobody, +¥1.50 per member for the rule), multiple testing (p = 0.008 for the gap: it stands if pre-specified, fails Bonferroni at 0.0036 if found among 14 fields), the S-learner penalty on the 800-member segment test (lambda = 50 keeps 80% of beta and half of gamma), the X-learner, the transformed outcome and DR pseudo-outcome (SD 1.76 against 0.83 for active members), the R-learner's l(x), TARNet (new material; carried on the coffee chain's 14 CRM fields, to be confirmed by the instructor) and Result 1.11 tied to the 0.0375 of "Same RMSE, Opposite Decisions". The T-learner illustration now uses fits 0.35/0.15 and 0.33/0.07, distinct from the notes' 0.34/0.14 and 0.32/0.08; Case A Part M3-R3 task 5 and its key follow.
- New check script `shared/checks/slides03_check.py` (0 mismatches). Case A's release table updated; M3-R4 (the ladder) is on hold until a seeded simulation exists.
- `schedule.xlsx` and the syllabus: M3 block A no longer lists BLP, which the notes teach in M4.

## Slide design principles; M1 and M2 decks brought into line
- New principles (instructor): slide 2 is a road map of the meeting's topics; slides are self-contained (no lab previews, case-handout instructions, in-class prompts or other course logistics); every deck ends with its summary. Recorded in `revision-plan.md`, Section 6.
- M1: new road-map frame; removed the exit ticket, the case-handout instruction on the type table, the project remark on the data-roles frame, and the notes and Lab 0 lines in the summary. "Your Turn: Compare Only Customers Who Opened the App?" becomes a question with its answer on the frame (the collider). Still 44 frames.
- M2: new road-map frame; removed the Lab 0 remark on the design-based frame, "In pairs, commit first", and the notes, Lab 1 and A1 lines in the summary. 37 frames.

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
