# Course revision plan (fall 2026): where things stand and what comes next

This is the brief for any new working session. It sits above `design-plan.md`, which records the design of the v4
notes and handouts. Read it together with `README.md` (layout, build, checks) and `AGENTS.md` (working rules).
Status as of 8 October 2026.

## 1. Purpose of the revision

- **Course thesis.** AI makes prediction and code cheap, so identification and verification are the scarce skills.
  - Lectures teach causal reasoning.
  - LLM and agent work happens in labs, assignments and projects.
- **What changed from the previous version.**
  - Generative AI moves from a side topic to a full meeting (M9) plus a thread through the labs and assignments.
  - Exams sit at M5 and M11. Proposals are presented at M8.
  - Classical instrumental variables (outside shifters of treatment, 2SLS, weak instruments), regression discontinuity,
    staggered DiD and synthetic DiD leave the core lectures. They become bonus reading and handouts.
  - Noncompliance in an RCT (the ITT, compliance types and the LATE) is not classical IV: it needs only potential
    outcomes and the draw, and it closes M2, in the lecture and in the notes.
  - The technical notes were rebuilt (v4) with proofs of the key results and a consistent house style.
- **Writing standard.** Readable by someone not taking the course. No em-dashes. Must not read like AI-generated prose.

## 2. How generative AI enters the course

There are two categories, and the course keeps them distinct.

**A. Generative models as simulators.**
- **The positive case.** A generative model trained on real logs, with the effect and the confounding planted by the
  analyst. Its effects are g-formula effects, so it rests on the same unconfoundedness assumption. That assumption is
  the price of making a business decision at all: unlike research, the business cannot decline to decide.
- **Two uses.**
  - As an estimator testbed: bias and coverage on this business's data shape.
  - As a pipeline testbed: run the whole predict-then-optimise pipeline and measure regret against the oracle. This
    persuades stakeholders far more than a textbook y = ax + b.
- **Credibility checks.** Backtests against past experiments; staying within the data's support; compounding error;
  "home advantage" (rank pipelines across simulators of different model classes).
- **The negative case.** Asking a language model for counterfactuals ("silicon samples"). Here the truth is asserted
  by the model's priors, not planted by the analyst. CEVAE sits on the same side: its identification rests on
  structure it does not state.

**B. Language models as variable generators.**
- LLM labels and embeddings are measurements with error. The consequence depends on the variable's role (outcome,
  treatment, control, effect modifier).
- Differential error, meaning accuracy that differs by treatment arm, can create an effect from nothing.
- Correction uses a gold subsample (PPI, DSL).
- Embeddings can serve as DML controls, subject to leakage (text written after treatment) and overlap collapse.

**Where each piece lives:**

| Place | GenAI content |
|---|---|
| M3 notes and lecture | TARNet as a shared representation, between the S- and T-learners |
| Handout H2 | TARNet, CFR, DragonNet, the CEVAE critique, in-context estimators (Do-PFN), benchmark pitfalls |
| M6 notes | Predict-then-optimise → decision-focused learning → policy learning, as one spectrum; policy learning as weighted classification |
| **M9 (whole meeting)** | A: learned simulators. B: LLM-generated variables. Worked examples: courier-bonus pipelines on two simulators; LLM-coded review outcome with PPI |
| Lab 1 | AI as **tool**: an LLM writes the A/B readout; students verify it with simulation tests |
| Lab 4 | AI as **decision-maker**: an LLM ranks customers from text profiles, evaluated by IPW against model rules |
| Lab 6 | AI as **analyst**: audit a tool-calling agent's observational analysis, then add a guardrail |
| Lab 8 | AI as **source of data**: LLM labels versus gold, PPI, embeddings as DML controls, a leakage demo |
| Lab 9 | AI as **intervention**: evaluate an AI staffing-tool rollout with DiD |
| A1 | Write the readout once by hand, then delegate it to an LLM and verify |
| A4 | Stress-test a pricing pipeline on two pretrained simulators with a confounding dial; regret against the oracle |
| M9 Section 3 (optional lab) | Three routes compared on the simulator: plug-in, decision-focused, policy tree |

## 3. Current schedule (source of truth: `schedule.xlsx`)

Meetings are on Tuesday and Thursday in Weeks 1 to 5, and on Thursday in Weeks 6 and 7. Each meeting has lecture
blocks A and B (50 minutes each) and lab C (60 minutes).

| M | A | B | C (lab) | Notes / handout |
|---|---|---|---|---|
| 1 | Potential outcomes | Causal graphs | Lab 0 review | M1 |
| 2 | Experiments: estimation | Experiments: design; to close, noncompliance and the LATE | Lab 1 (LLM readout) | M2, H1 interference |
| 3 | CATE basics | Meta-learners, TARNet | Lab 2 | M3, H2 neural |
| 4 | Causal trees | Causal forests | Lab 3 | M4 |
| 5 | **Exam I (M1–M4)** | Evaluating targeting policies | Lab 4 (LLM as decision-maker) | M5 |
| 6 | Allocation | Policy learning | Lab 5 | M6, H3 sequential |
| 7 | Adjustment | Propensity scores, AIPW | Lab 6 (agent audit) | M7, H4 IV |
| 8 | DML I | DML II | **Proposal presentations** (Lab 7 take-home) | M8, H5 RD |
| 9 | GenAI I: simulators | GenAI II: LLM variables | Lab 8 | M9 |
| 10 | Panel basics | DiD | Lab 9 (AI rollout) | M10, H6 staggered |
| 11 | **Exam II (M5–M10)** | Synthetic control | Lab 10 | M11 |
| 12 | Final presentations | | | |

**Assignments.**
- A1 (M1–M2): delegate and verify.
- A2 (M3–M6): coupon targeting under a budget, scored by an autograder on a locked RCT set.
- A3 (M6–M8): the same decision from observational logs, scored on the same locked set.
- A4 (M8–M9): pipeline stress test on simulators.

**Deadline rules.**
- One major deliverable per week.
- At most two graded deadlines in any 72 hours.
- Nothing due on an exam day or the weekend before an exam.

The full calendar is in the spreadsheet. Its Schedule sheet lists, for each meeting, the lecture blocks, the lab,
what is released (case parts, assignments, the lab's notebook), what is due, the bonus reading and the handout. The
syllabus's weekly table follows it, with an "Out / due" column.

## 4. Status by component

| Component | State |
|---|---|
| Technical notes M1–M11 | **Done (v4.1, commit `5522695`).** Pass 1 review done. Since then (8 Oct): M2 gains Section 1.9, noncompliance (Assumptions 1.11–1.12, Results 1.13–1.16), and its Step 6 now uses 15% redemption |
| Handouts H1–H6 | **Done.** Renumbered in meeting order on 8 Oct (H1 interference, M2, to H6 staggered adoption, M10). H4 (IV) refocused on classical IV, with a new worked example, so it no longer repeats M2 Section 1.9 |
| Notation sheet, style, build and check scripts | Done. `run_all.sh` runs the notes, handout, slide and case checks |
| Schedule, labs, assignments, deadlines, bonus reading | Planned in `schedule.xlsx` (Release and Due columns since 8 Oct); judgement calls in Section 7 still open |
| Lecture slides | **M1 to M6 rebuilt on the coffee-chain case, under review**: M1 44 frames, M2 37, M3 30, M4 33, M5 21 (one lecture block; block A is Exam I), M6 34. Each checked by `slidesNN_check.py`. M7–M11 hold v2 content, built for the old calendar |
| Syllabus | Draft 3 (8 Oct), matches `schedule.xlsx`, handouts H1–H6 in meeting order, no critique exercises. Undecided items marked `\tbd` (dates, weights, policies) |
| Lab notebooks 0–10 | Not built |
| Assignments A1–A4, autograder, locked RCT set | Not built |
| Lecture cases A–C | Drafts. Rewritten 8 Oct: Case A Part M2-R6 (noncompliance), Case B's M9 part (generative AI), Case C's M11 part (synthetic control); their old IV and staggered-DiD parts kept at the end as bonus. Checked by `case_check.py`. Other parts' release times to be retimed with each deck |
| Reading-and-critique exercises | Dropped for now (instructor, 8 Oct); may return later. Frames C2–C6 remain in the v2 decks for M3, M5, M7, M9 and M11 |
| Releases and tags | Pull request luzk-emory/test#3 merged into `main` (up to the H4 refocus). The renumbering, the schedule columns and this update are on `claude/slides-rebuild`, not yet merged. No git tags yet; `v4.1` (commit `5522695`) is to be tagged when the instructor asks |
| `plan/old-decks/map.md` | Missing: the old decks are in `main`, but the frame-by-frame map was not committed |

## 5. Work remaining, in suggested order

1. **Slides, M7 to M11** (M1 to M6 are done and under review). Rebuild each deck to match its v4.1 notes and its
   schedule row, one deck at a time, stopping for the instructor's review after each. Lecture slides carry the
   intuition and the lecture's own running case; proofs stay in the notes. Slides and notes share the method, not the
   example (Section 6). M1 and M2 set the pattern: title, road map, block A, block boundary, block B, summary;
   Results with the notes' numbers and titles in the notes' order; a `slidesNN_check.py` for every number.
   - Exam meetings (M5, M11) have only block B of lecture.
   - M9 needs a new deck. New material for other decks:
     - M3: TARNet slide (done, on the coffee chain's 14 CRM fields; instructor to confirm the case);
     - M5: isotonic calibration (done, on the coffee chain);
     - M6: capacity and the critical fractile, fairness as a priced constraint, the predict-then-optimise spectrum (done, on
       the Region 2 push: two stores for capacity, North and South districts for fairness);
     - M8: DML II with sensitivity bounds;
     - M10: a warning slide on staggered timing;
     - M11: synthetic control only.
   - Done on 8 Oct: M2 closes with noncompliance in an RCT (ITT, compliance types, the LATE), on Case A Part M2-R6,
     matching M2 notes Section 1.9. Classical IV stays in Handout H4 (M7, bonus).
   - Tested slides from the instructor's other course (the Starbucks causal module) are in `plan/old-decks/`. Reuse them
     where a topic matches (Section 6). The frame-by-frame map (`plan/old-decks/map.md`) still needs to be committed.
2. **Syllabus.** Draft 3 matches `schedule.xlsx`. Remaining: settle the items marked `\tbd` (dates, weights, policies;
   see the open calls in Section 7) and keep it in step with the spreadsheet when either changes.
3. **Labs 0–10.** Data and tasks are specified in the spreadsheet's Labs tab. The heaviest preparation is Lab 8
   (cached LLM outputs, gold labels) and Lab 6 (agent harness).
4. **Assignments.**
   - A1 to A4 handouts.
   - The locked RCT evaluation set and an autograder for A2 and A3.
   - The two hotel-demand simulators with a confounding dial for A4. This is the largest single build; `m09_sim.py`
     is the template.
5. **Review passes.** Pass 2: independent check of every numbered Result. Pass 3: a student reads each meeting one
   week ahead.
6. **Optional.**
   - A pricing handout, "From elasticity to price": pricing from θ̂(x), coupon menus, capacity. Source is old deck L9.
     Handouts are numbered in meeting order (H1 with M2 to H6 with M10), so if it is written, it takes its meeting's
     place and the later handouts renumber.
   - Tag releases when the instructor asks (for example `v4.1` at commit `5522695`).
   - Seed the M8 simulation.
   - Confirm three citations (listed in `README.md`).

## 6. Notes for the slide rebuild

- **Deck structure (instructor, 8 Oct).** Slide 1 is the title. Slide 2 is a road map of the meeting's topics, by
  block, in the order they are taught. The deck ends with a summary frame, and nothing follows it.
- **Slides are self-contained.** No lab previews, assignment or project notices, case-handout instructions, exit
  tickets, "in pairs" or other in-class activity prompts, and no pointers to the notes or handouts. A question on a
  slide is answered on the slide or the next one. The running case is the lecture's example, so its story and numbers
  stay; the `% [RELEASE ...]` comments in the source are for the instructor and do not print. Short references to
  another meeting, where a topic continues, may stay in the text.

- **Carried frames.** The frames taken from the old decks into the v2 decks for M1 to M6 have all been reworked or
  deleted in the rebuilds. For M7 to M11, reuse `plan/old-decks/` only where a topic matches, and rework what you take.
- **M9 and M11 decks are replaced, not revised.** The current M9 deck teaches instrumental variables (hotel example) and
  the current M11 deck is mostly staggered DiD. Both topics are now handouts (H4, H6). Write new decks to the M9 and
  M11 notes. The old frames stay in git history (commit `5522695`, the v4.1 state), so no separate copy is needed.
- **Lectures keep their own case; the notes use a different one on purpose.** Each lecture has its own running case
  (the coffee chain in M1, the hotel in M8, and so on). The notes' Section 2 worked example uses a different business
  (FitLife or QuickBite) so students see the method transfer. Do not move a slide example to the notes' business.
  - *Shared between slides and notes:* the estimands, the assumptions, the notation (`shared/notation.tex`), the
    statement of each Result (same number and title), and the order of topics.
  - *Not shared:* the worked example and its numbers. Slide numbers are the lecture's own; they must be internally
    consistent and checked by a script in `shared/checks/` (`slidesNN_check.py`), not matched to `notes.tex`.
  - A slide may point to the notes ("a second worked example, on a fitness chain, is in the notes") but does not
    reproduce it.
  - New material (M9, and the additions in M3, M5, M6 and M11): before writing frames, propose which lecture case
    carries it, consistent with the case that meeting's existing slides use, and get the instructor's agreement.
- **Source decks.** `plan/old-decks/lecture01.tex` to `lecture09.tex` are reference material only: do not build or
  edit them.
- **No critique frames.** Reading-and-critique exercises are dropped for now. Delete the v2 critique frames when
  rebuilding those decks: C1 to C3 are gone with the M2, M3 and M5 rebuilds; C4 to C6 remain in the M7, M9 and M11 decks, along
  with their "Today's plan" rows.
- **Block order follows the notes.** Where the v2 deck or the old schedule ordered topics differently, the notes win,
  and `schedule.xlsx` and the syllabus are updated to match (as in M2: transport ends block A, CUPED moves to block B).
- **Checks and release tables.** Each rebuilt deck gets `shared/checks/slidesNN_check.py`, run by `run_all.sh`, and
  the lecture case's release table is updated to the new frames.

## 7. Judgement calls

Decided on 8 October:
- Noncompliance in an RCT (ITT, compliance types, the LATE) closes M2, lecture and notes. Classical IV stays in
  Handout H4 with M7 as bonus reading, and H4 no longer repeats the M2 material.
- M2 Step 6 uses 15% redemption (¥1.50 per offer).
- A3 is due Friday of Week 5, so nothing is due the weekend before Exam II.
- Reading-and-critique exercises are dropped for now.
- M9 keeps the hotel case (Case B) and M11 keeps the retail case (Case C), both rewritten, with the old IV and
  staggered-DiD parts kept as bonus.
- Handouts are numbered in meeting order: H1 interference (M2), H2 neural estimators (M3), H3 sequential decisions
  (M6), H4 instrumental variables (M7), H5 regression discontinuity (M8), H6 staggered adoption (M10).
- `schedule.xlsx` splits the old Misc column into Release and Due.

Still open (decide before building the affected pieces):

1. Staggered DiD: a warning slide in Panel II plus an optional extension in Lab 9.
2. A2 and A3 pose the same decision (RCT-trained versus logs-trained), so both need an autograder and a locked set.
3. Proposal due Sunday of Week 3.
4. No panel-data assignment.
   - As planned, DiD is tested on Exam II and practised in Labs 9 and 10.
   - Alternative: make A4 a DiD evaluation and fold the simulator into Lab 8.
5. Final-project appendices: an LLM review of the draft plus responses, and a planted-effect validation of the design.
6. Exam weights: Exam II covers more lectures than Exam I; consider weighting it more.

