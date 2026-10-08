# Course revision plan (fall 2026): where things stand and what comes next

This is the brief for any new working session. It sits above `design-plan.md`, which covers only the v4 notes. Read it
together with `README.md` (layout, build, checks) and `AGENTS.md` (working rules).

## 1. Purpose of the revision

- **Course thesis.** AI makes prediction and code cheap, so identification and verification are the scarce skills.
  - Lectures teach causal reasoning.
  - LLM and agent work happens in labs, assignments and projects.
  - Case critiques are read on paper, without AI.
- **What changed from the previous version.**
  - Generative AI moves from a side topic to a full meeting (M9) plus a thread through the labs and assignments.
  - Exams sit at M5 and M11. Proposals are presented at M8.
  - Instrumental variables, regression discontinuity, staggered DiD and synthetic DiD leave the core lectures. They
    become bonus reading and handouts.
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
| Handout H6 | TARNet, CFR, DragonNet, the CEVAE critique, in-context estimators (Do-PFN), benchmark pitfalls |
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
| 2 | Experiments: estimation | Experiments: design | Lab 1 (LLM readout) | M2, H4 interference |
| 3 | CATE basics | Meta-learners, TARNet | Lab 2 | M3, H6 neural |
| 4 | Causal trees | Causal forests | Lab 3 | M4 |
| 5 | **Exam I (M1–M4)** | Evaluating targeting policies | Lab 4 (LLM as decision-maker) | M5 |
| 6 | Allocation | Policy learning | Lab 5 | M6, H5 sequential |
| 7 | Adjustment | Propensity scores, AIPW | Lab 6 (agent audit) | M7, H1 IV |
| 8 | DML I | DML II | **Proposal presentations** (Lab 7 take-home) | M8, H2 RD |
| 9 | GenAI I: simulators | GenAI II: LLM variables | Lab 8 | M9 |
| 10 | Panel basics | DiD | Lab 9 (AI rollout) | M10, H3 staggered |
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

The full calendar is in the spreadsheet.

## 4. Status by component

| Component | State |
|---|---|
| Technical notes M1–M11, handouts H1–H6 | **Done (v4.1).** Pass 1 review done |
| Notation sheet, style, build and check scripts | Done |
| Schedule, labs, assignments, deadlines, bonus reading | Planned in `schedule.xlsx`; judgement calls below still open |
| Lecture slides | **M1 rebuilt, under review; it sets the pattern for the rest.** M2–M11 hold v2 content, built for the old calendar |
| Syllabus | Draft 3 (8 Oct), generated from `schedule.xlsx`; undecided items marked `\tbd` |
| Lab notebooks 0–10 | Not built |
| Assignments A1–A4, autograder, locked RCT set | Not built |
| Case critiques A–C | Drafts, developed separately; not in the schedule |

## 5. Work remaining, in suggested order

1. **Slides, all 11 meetings.** Rebuild each deck to match its v4.1 notes and its schedule row. Lecture slides carry
   the intuition and the lecture's own running case; proofs stay in the notes. Slides and notes share the method, not
   the example (Section 6).
   - Exam meetings (M5, M11) have only block B of lecture.
   - M9 needs a new deck. New material for other decks:
     - M3: TARNet slide;
     - M5: isotonic calibration;
     - M6: capacity and the critical fractile, fairness as a priced constraint, the predict-then-optimise spectrum;
     - M8: DML II with sensitivity bounds;
     - M10: a warning slide on staggered timing;
     - M11: synthetic control only.
   - Keep one noncompliance slide in Experiments II, pointing to H1.
   - Tested slides from the instructor's other course (the Starbucks causal module) are in `plan/old-decks/`, with a
     frame-by-frame map (`plan/old-decks/map.md`). Reuse them where a topic matches. See Section 6.
2. **Syllabus.** Regenerate from `schedule.xlsx`: calendar, assessment weights, AI policy per assignment, bonus reading.
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
   - Handout H7, "From elasticity to price": pricing from θ̂(x), coupon menus, capacity. Source is old deck L9.
   - Seed the M8 simulation.
   - Confirm three citations (listed in `README.md`).

## 6. Notes for the slide rebuild

- **Carried frames are a starting point.** The v2 decks for M1 to M6 already hold 69 frames taken from the old decks,
  each marked in the source with a comment such as `% [CARRIED VERBATIM from old-decks/lecture01.tex:121]`. Start from
  these frames; do not copy them from `plan/old-decks/` a second time. Once a frame is reworked, delete its comment.
- **M9 and M11 decks are replaced, not revised.** The current M9 deck teaches instrumental variables (hotel example) and
  the current M11 deck is mostly staggered DiD. Both topics are now handouts (H1, H3). Write new decks to the M9 and
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

## 7. Open judgement calls (decide before building the affected pieces)

1. Noncompliance: one slide in Experiments II; IV stays in bonus reading and H1.
2. Staggered DiD: a warning slide in Panel II plus an optional extension in Lab 9.
3. A2 and A3 pose the same decision (RCT-trained versus logs-trained), so both need an autograder and a locked set.
4. Proposal due Sunday of Week 3.
5. No panel-data assignment.
   - As planned, DiD is tested on Exam II and practised in Labs 9 and 10.
   - Alternative: make A4 a DiD evaluation and fold the simulator into Lab 8.
6. Final-project appendices: an LLM review of the draft plus responses, and a planted-effect validation of the design.
7. Exam weights: Exam II covers more lectures than Exam I; consider weighting it more.
8. A3 is due Sunday of Week 5, the weekend before Exam II (Thursday of Week 6). That breaks the rule "nothing due
   ... the weekend before an exam" if the rule counts the whole preceding weekend. Options: keep it (read the rule as
   the weekend right before a Monday or Tuesday exam), or move A3 to Friday of Week 5.
9. Reading-and-critique exercises: the brief and draft 2 of the syllabus have them, but `schedule.xlsx` does not say
   which meetings. Blocks A of M5 and M11 are exams, so draft 2's list (M2, M3, M5, M7, M9, M11) no longer fits.
10. Lecture case for M9: Case B (Meridian Hotels) teaches IV in its M9 part, and Case C's M11 part is mostly staggered
    DiD. Both parts need rewriting, and the M9 case needs choosing (the hotel group fits A4's hotel simulators).
