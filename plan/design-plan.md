# Notes v4: design record

**SHBI-GB 7342, technical notes and handouts.** Written 2026-10-07 after comparing v3 (`notes01–11.tex`, generated
2026-10-06 from the v3 schedule) with v2 (`meetings/mXX/notes-v2.tex`), `course-spine.md` and the three Codex reviews
(all pre-git; they are in `../_archive-2026-10-07.zip`). Updated 2026-10-08 to record what was built and what changed
since. For the revision as a whole (slides, labs, assignments, syllabus) see `revision-plan.md`.

**Decision in one line:** v4 keeps v3's look and its meeting structure, takes back v2's rigour
(proofs, the estimand → identification → estimation spine, design-based inference, exercises), fixes
the errors and conflicts listed in Section 2, and moves six bonus topics into stand-alone handouts.

## 0. Status (8 October 2026)

- **Built.** All eleven notes and six handouts, v4.1 (commit `5522695`, not yet tagged), with answer keys, a notation
  sheet and a check script per document. Pass 1 review (arithmetic, wording, flow) is done; pass 2 (an independent
  check of every proof) and pass 3 (a student read) are not.
- **Size.** Notes run 6 to 10 pages (86 pages in all); handouts 5 to 6 pages (31 pages). Both came in shorter than the
  estimates in Sections 4 and 6, mainly because proofs are light (Decision 2).
- **Changed since v4.1 (8 Oct).**
  - M2 gains Section 1.9, "Noncompliance: the ITT and the LATE": Assumptions 1.11 (exclusion) and 1.12 (monotonicity),
    Results 1.13 (two effects of assignment), 1.14 (type shares), 1.15 (the LATE theorem) and 1.16 (one-sided
    noncompliance). These were ported from the IV handout and restated for a randomised offer, since they need only
    potential outcomes and the draw. M2 Step 6 now uses 15% redemption.
  - The IV handout (now H4) covers classical IV only: from a randomised offer to an outside shifter, arguing for an
    instrument, complier means, exclusion and monotonicity failures, 2SLS with strata, weak instruments and locality.
    It cites M2 Results 1.13–1.15 instead of restating them, and has a new QuickBite worked example.
  - Handouts are numbered in meeting order (H1 with M2 to H6 with M10). This document uses the new numbers. Older
    records (`CHANGELOG.md` entries before the renumbering, the pass-1 review) use the old ones: old H1 (IV) is now H4,
    H2 (RD) is H5, H3 (staggered adoption) is H6, H4 (interference) is H1, H5 (sequential decisions) is H3, and H6
    (neural estimators) is H2.
- **Where things are.** Notes and handouts are `meetings/mNN/notes.tex` and `meetings/mNN/handout-HN-topic.tex`; the
  style is `shared/coursenotes.sty`; checks are in `shared/checks/`; changes are recorded in `plan/CHANGELOG.md`.
  Sections 5 and 6 below give the names used in the original plan and what they became.

Sections 1 to 3 describe the starting point and the plan as written on 7 October; every item in Section 2 was
addressed in v4.

---

## 1. Where v3 stands

| | v2 | v3 | v4 target |
|---|---|---|---|
| Words per meeting | 3,500–5,200 | 1,400–2,250 | 3,500–5,000 |
| Proofs | 70 in total (2–9 per meeting) | 1 in total | Light proofs for key results (Section 7) |
| Organising spine | Estimand → identification → estimation, design-based | Topic order, superpopulation by default | v2 spine |
| "What happened in class" | Yes (Section 0) | No | No (self-contained); each note opens with the decision instead |
| Worked example | Different business, with an exercise | Different business, no exercise | Different business, two exercises, answers in an instructor key |
| Visual design | Plain | Coloured result and extension boxes | v3 boxes, extended (Section 5) |
| Figures | Few | One (Meeting 1 DAG) | At least one per meeting |
| Bonus reading | Section 3 subsections | Short, unannotated lists | Annotated lists, plus six handouts (Section 4) |

v3's strengths are the design, short readable paragraphs, the new topics (DAGs, meta-learners beyond
S/T, forests' weights, RATE, policy learning, Meeting 9) and the worked examples in new businesses. Its
weaknesses are the missing proofs, the departure from the course spine, and a few content errors.

---

## 2. Content problems found in v3 (fix in v4)

### Conflicts with decisions already made in `course-spine.md` and the reviews

1. **Inference is superpopulation by default (M1, M2).** The spine says finite population first:
   Fisher's test and Neyman's variance, with the usual SE introduced as the conservative
   approximation. v3 M2 gives only the superpopulation formula. Port v2 M2's Fisher, Neyman,
   conservativeness and superpopulation propositions.
2. **The synthetic-control placebo rank is called a $p$-value (M11).** The accepted M11 correction says
   the rank is descriptive unless the treated unit was as likely as any donor to be treated. v3 states
   "$p = 1/(J+1)$" without that condition, and its worked example leans on an RMSPE ratio of 50 built on
   a near-perfect pre-fit (pre-RMSPE 0.037), which is the unstable case the review flagged.
3. **Break-even ignores how the treatment is paid for (M1, M6).** v2 uses $V = m\tau - c\,p_1$ (coupon
   paid on redemption, so sure things cost money and lost causes do not). v3 M1 uses $\tau^\ast = c/m$
   with cost per unit sent. v4 states both cost models and uses v2's in the coffee-chain-aligned results.
4. **No adoption-date potential outcomes (M10, M11).** The spine indexes panel outcomes by adoption date,
   $Y_{it}(g)$, with $g=\infty$ for never-treated, and says out loud that DiD identification is
   assumption-based. v3 uses $Y_{it}(1), Y_{it}(0)$.
5. **No outcome-free design stage (M7, M8, M11).** The spine requires reconstructing assignment,
   checking overlap and fixing trimming before outcomes are opened, and freezing donors before the
   post-period in synthetic control. v3 mentions none of it.
6. **Paired comparison of two policies missing (M5).** Review A6 replaced "one SE of the difference"
   with a paired SE. v3 has no comparison of lists at all.

### Errors and loose statements

7. **Notation clash.** v3 uses $m$ for the margin (M1, M3, M6) and $m(x) = \E[Y \mid X = x]$ (M3, M4).
   v4 adopts v2's names: margin $m$, outcome regression $\ell(x)$, treatment regression $r(x)$,
   propensity $e(x)$.
8. **M10 trend sensitivity.** "Pre-period data cannot rule out a drift of about 0.04 per month" is
   asserted, not derived. Replace with v2's linear-differential-trend proposition and compute the bound.
9. **M8 sensitivity bound** is the Cinelli–Hazlett OLS bound applied to the residualised regression. That
   is correct for the partially linear model but should say so, and give the Chernozhukov et al. (2022)
   version for the interactive model in Section 3.
10. **Invented headline numbers.** M8's full-sample DML results ($-0.62$, SE 0.08; lasso $-0.58$) and the
    whole M9 regret table are made up. M9 labels them "illustrative"; M8 does not. v4 generates both from a
    simulation script shipped with the notes, so every number reproduces.
11. **M3 T-learner.** "Differences in the two models' errors show up as spurious heterogeneity" is the
    right idea stated loosely. Replace with v2's proposition in its corrected form (review A): variances
    add; biases can cancel or reinforce.
12. **M4 forest intervals.** "Honest causal forests are asymptotically normal" is unqualified. Add the
    conditions in review A (honesty, subsampling, overlap, smoothness), and cite correlated trees in
    "variable importance is not a test".
13. **M5 AUTOC and Qini values** are discrete averages over ten deciles. Say so, or compute the integrals.
14. **M6 greedy rule.** Ratio-greedy is exact only for the LP relaxation (divisible segments). Add v2's
    0–1 knapsack counterexample (review A).
15. **References.** Several citations need checking before release (for example the publication status of
    Chernozhukov, Demirer, Duflo and Fernández-Val; the year of Yadlowsky et al.; Do-PFN author list).
    Every reference in v4 is verified against the publisher page.

---

## 3. Coverage: what each meeting needs

"Port" means bring the result and its proof from the v2 file named. "New" means write it. Proposition
names are v2's where they exist.

| v3 meeting | Source in v2 | Port | New |
|---|---|---|---|
| **1** Causal basics | m01; m07 (collider) | ATE averages ATT and ATU; ATE in response types; selection-bias decomposition; two sources of bias; identification under random assignment; unbiasedness over the design; OLS on a dummy; net value and break-even; collider bias in the simplest case | Backdoor adjustment gives the g-formula (proof from conditional exchangeability; the graphical criterion stated with a reference); d-separation examples; figure: chain, fork, collider |
| **2** Experiments | m02; m09 (ITT, LATE) | Fisher test; Neyman variance; conservative estimator; superpopulation variance; inference on net value; transport by reweighting; sample size; CUPED; design effect | ITT and first stage identified by the draw (from v2 m09); SRM test; Holm's procedure (statement); peeking inflation (statement with simulation); pre-experiment checklist. Added 8 Oct: noncompliance as Section 1.9 (type shares, the LATE theorem, one-sided noncompliance, from v2 m09) |
| **3** CATE I–II | m03 | CATE identification; individual targeting rule; S-learner shrinkage; T-learner variances add; cost of ignoring heterogeneity; SE of the gap between segments | Value of targeting $\ge$ value of the best blanket rule (Jensen); $\E[Y^\ast \mid X] = \tau(X)$; DR pseudo-outcome is doubly robust; Robinson decomposition makes $\tau$ the R-loss minimiser; X-learner weights; TARNet (no proof) |
| **4** Causal forests | m04 | Causal criterion ignores prognostic splits; outcome gap of a split; winner's curse; honest leaves unbiased; asymptotic normality (statement); price of a split | Forest estimate as a weighted local moment (derivation, link to R-learner); BLP: $\beta_1 = $ ATE and $\beta_2 = \Cov(\tau,\hat\tau)/\Var(\hat\tau)$ (proof); GATES on held-out data unbiased |
| **5** Evaluation | m05 | Rates then scale; gain curves see only ranks; profit-curve peak; IPW value identity (with unequal $e$); row-contribution variance; selection value is optimistic; paired comparison | Policy-value identity $V(\pi) - V(0) = \E[\pi\tau]$; TOC, AUTOC and Qini as RATE weights; RATE $= 0$ under a random ranking |
| **6** Allocation and policy learning | m06 | Unconstrained rule; sure-thing decomposition; caps (exchange argument); greedy optimal for the relaxation; shadow price; spending risk and reserve; conservative rule | Several actions via the Lagrangian; 0–1 counterexample; $\E[\Gamma \mid X] = m\tau(X) - c(X)$; EWM regret bound (statement, Athey–Wager); holdout logging; bandits (Thompson sampling, logged propensities) |
| **7** Observational data | m07 | g-formula; IPW identity; ATT weights; balancing property; variance-weighted regression estimand; collider bias; ADRF; double robustness (moves from Section 3 to Section 1, since AIPW is now lectured); ESS | Outcome-free design stage as a numbered protocol; M-bias; trimming changes the estimand; simple OVB sensitivity |
| **8** DML | m08 | FWL in population form; $\ell$ is not $g$; why residualising both sides protects $\theta$; variance-weighted estimand; overlap with a continuous treatment; support of the decision | Orthogonality shown as a zero derivative (Section 1 version); cross-fitting under dependence (folds by cluster or night); DML asymptotics with rate conditions (statement); interactive model score; sensitivity bound with its source |
| **9** GenAI | none | Misclassified modifier attenuates heterogeneity (from v2 m03) | Simulator sampling equals the g-formula under the three assumptions (proof); what a calibrated simulator cannot contain; regret decomposition for the pipeline testbed; PPI unbiasedness and variance (proof); non-differential misclassification of a binary outcome scales the effect by $(1 - \alpha - \beta)$ (proof); bias under differential error (proof); embedding leakage as a bad control |
| **10** Panel data | m10 | DiD identification; what the two single differences contain; scale dependence; linear differential trend; TWFE by the within transformation; TWFE = DiD with one date; event-study regression; collapsing to one change per unit | Before–after = effect + trend + regression to the mean (derivation); adoption-date notation; balanced-panel caveat for double demeaning |
| **11** Synthetic control | m11 (SC part) | Factor-model rationale; three properties of the constraints; donor sensitivity; in-place and in-time placebos; design before the post-period; local-shock falsification | Permutation validity only under random selection of the treated unit (proof); held-out pre-period check as a numbered step; SC vs DiD as two weightings; synthetic DiD and matrix completion with formulas in Section 3 |

Topics in v2 that v4 drops on purpose, because the v3 schedule dropped them from lectures: classical IV and RD as
lecture content (they move to handouts), staggered DiD (handout), v2 M3's misclassified modifier (moves to
Meeting 9). Noncompliance in an RCT is not dropped: it needs only potential outcomes and the draw, so it closes M2
(8 Oct).

---

## 4. Handouts: which bonus topics get their own document

The test is whether a reader can use the topic without the meeting it hangs off, and whether it needs
more than three pages to do properly. Six pass.

| Handout | Replaces bonus slot | Why stand-alone | Main source | Planned length | Built |
|---|---|---|---|---|---|
| **H1 Interference and marketplace experiments** | M2 | Changes the estimand itself; central to platform work | New, from v2 m02 §3 seeds: exposure mappings, direct and spillover estimands, cluster randomisation, two-sided marketplace bias, switchbacks, budget-split designs | 8–10 pp | 5 pp |
| **H2 Neural and foundation-model estimators** | M3 and M9 | Both bonus slots point at the same literature | New: TARNet, CFR, DragonNet, CEVAE and its critique, causal transformer, Do-PFN, benchmark pitfalls (IHDP) | 8–10 pp | 5 pp |
| **H3 Sequential decisions** | M6 | Dynamic regimes and bandits are a separate framework | New: dynamic treatment regimes, sequential exchangeability, Q-learning, G-estimation and SNMMs, off-policy evaluation from bandit logs | 10–12 pp | 5 pp |
| **H4 Instrumental variables** | M7 | A full design with its own assumptions, estimators and inference | v2 m09 plus its Section 3. Since 8 Oct, classical IV only: the two effects of assignment, type shares and the LATE theorem moved to M2 Section 1.9; H4 keeps complier means, exclusion and monotonicity failures, 2SLS with strata, the delta-method SE and Anderson–Rubin, and adds arguing for an instrument | 10–12 pp | 6 pp |
| **H5 Regression discontinuity** | M8 | Separate identification argument (continuity) and estimation toolkit | v2 m09 §3.1, expanded: sharp and fuzzy RD with proofs, local linear estimation, bandwidth and bias correction, density and covariate checks, business thresholds (loyalty tiers, free-shipping cut-offs, rating rounding); kinks in Section 3. The fuzzy case cites M2's LATE theorem | 8–10 pp | 5 pp |
| **H6 Staggered adoption** | M10 | Needs its own notation, estimators and the TWFE decomposition | v2 m11 DiD part (never-treated and not-yet-treated identification, contamination, Goodman-Bacon, aggregation, inference) plus the design-based view of randomised adoption dates (Athey and Imbens 2022), imputation estimators and honest DiD | 10–12 pp | 5 pp |

**Stay in Section 3 of their meeting** (they extend the meeting rather than stand alone): causal graphs
in depth (M1), forest theory (M4), RATE inference (M5), synthetic DiD and matrix completion (M11, with
estimator definitions). If you would rather have a seventh handout on panels with factor structure, SDID
and matrix completion are the candidate.

Handouts use the same three sections and boxes as the meeting notes, are marked "not examinable" on page
1, and carry their own exercises.

**Annotated bonus reading.** Every Section 3 reading list becomes a short table: reference, what it
gives you, which sections to read, prerequisite, and difficulty (one to three stars). No unannotated
lists.

---

## 5. Design changes

Keep v3's palette, fonts and boxes. Change `v3notes.sty` to `v4notes.sty` with the items below. (Built as
`shared/coursenotes.sty`, copied into each meeting folder by `shared/build_all.sh`. Results and Assumptions share one
counter per document.)

1. **Numbered result boxes.** Propositions in the green box with numbers (1.1, 1.2, …) and labels for
   cross-reference. Assumptions in a blue-outlined box. Definitions in a light grey box.
2. **Proofs** outside the box, set smaller, ending with □. Long proofs get a one-line idea first.
3. **Pitfall box** (red outline, already defined and unused in v3) for the errors students actually
   make: testing against zero, post-treatment controls, reading variable importance as a test.
4. **Page 1 layout:** the decision and the number that settles it; three to five "you should be able
   to" lines; a notation table for the meeting.
5. **Section 1 subsections follow the spine:** estimand, identification, estimation and uncertainty, the
   decision, pitfalls.
6. **At least one figure per meeting** (TikZ or pgfplots, both available): M2 randomisation
   distribution; M3 four response types; M4 forest weights; M5 gain and profit curves; M6 shadow price;
   M7 overlap histograms; M8 residual-on-residual scatter; M9 simulator pipeline diagram; M10 event-study
   plot; M11 treated vs synthetic path.
7. **Exercises:** two per worked example (one computation, one judgement), with answers in an instructor key.
   (Built: the key compiles from the same source with `\def\KEY{}`; `shared/build.sh` writes both PDFs.)
8. **A one-page course notation sheet**, shared by all notes and handouts (`shared/notation.tex`).

---

## 6. Work order and checks

1. **Shared files:** `v4notes.sty`, notation sheet, a simulation script per worked example under
   `notes-v4/checks/`. (Built as `shared/coursenotes.sty`, `shared/notation.tex` and `shared/checks/`, with one
   `*_check.py` per document and `run_all.sh` to run them all.)
2. **Meetings 1–4** (Exam I scope), then **5–10** (Exam II scope), then **11**, then **the six handouts**.
   Exam scope first so the examinable material is stable earliest.
3. **For each note:** port the v2 propositions with proofs; rewrite to v3 style; generate every worked
   number from its script; add figure and exercises; write the key.
4. **Checks before release:**
   - every number in Section 2 reproduced by its script;
   - every proof read line by line by a second reader who has not seen the drafting (an independent
     agent, or the TA);
   - every reference checked against the publisher;
   - a scan for em-dashes, undefined references and overfull lines;
   - consistency with `course-spine.md` Section 4 (the master change list) item by item.
5. **Deliver** into `meetings/mXX/notes-v4.tex` beside v2, with a `CHANGES-v4.md` per meeting, as v2 did.
   (Superseded when the course moved to git: each document has one file, `meetings/mNN/notes.tex`, its history is in
   git, and changes are recorded in `plan/CHANGELOG.md`.)

Estimated size: 11 notes at 8–11 pages and 6 handouts at 8–12 pages, about 160 pages in total. (Built: 86 pages of
notes and 31 of handouts; see Section 0.)

---

## 7. Decisions (settled 2026-10-07; item 5 added 2026-10-08)

1. **Worked examples reuse a business when the context is close.** Two recurring businesses carry most
   examples:
   - **FitLife**, a fitness-club chain (memberships, renewals, staff outreach, club-level rollouts):
     Meetings 1, 3, 7 and 10;
   - **QuickBite**, a food-delivery platform (coupons, delivery fees, couriers, restaurant reviews, city
     launches): Meetings 2, 4, 5, 6, 8, 9 and 11.
   Handouts reuse them where natural (QuickBite for interference and IV; FitLife for RD and staggered
   adoption). Lecture slides keep their own running cases (`cases/`), so students see each method on two businesses.
2. **Light proofs for key results.** Every identification result gets a short proof (a few lines, idea
   first). Estimation and asymptotic results are stated with a one-line reason and a reference.
3. **Six handouts.** Synthetic DiD and matrix completion stay in the Meeting 11 notes (Section 3, with
   estimator definitions), since they extend the lecture directly.
4. **Files:** one PDF per meeting, plus a second PDF where a meeting has a handout:
   M2 + H1 interference, M3 + H2 neural estimators, M6 + H3 sequential decisions, M7 + H4 IV, M8 + H5 RD,
   M10 + H6 staggered adoption. Handouts are numbered in meeting order (8 Oct). Answer keys compile from the same
   source (`\def\KEY{}`).
5. **Noncompliance in an RCT belongs to M2** (8 Oct). The ITT, compliance types and the LATE need only potential
   outcomes and the draw, so they close M2 (Section 1.9) in the notes and the lecture. Classical IV, where the
   instrument is an outside shifter that was not randomised, stays in Handout H4 with M7 as bonus reading.
