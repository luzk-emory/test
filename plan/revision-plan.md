# Course revision plan (fall 2026)

The brief for any new working session: why the course is being revised, how generative AI enters it, and the work
that remains. Status, layout, conventions and decisions on record are in `README.md`; the calendar, labs, assignments
and deadlines are in `schedule.xlsx` and the syllabus; decisions waiting on the instructor are in `FLAGS.md`; working
rules are in `AGENTS.md` and `editorial-guide.md`.

## 1. Purpose of the revision

- **Course thesis.** AI makes prediction and code cheap, so identification and verification are the scarce skills.
  - Lectures teach causal reasoning.
  - LLM and agent work happens in labs, assignments and projects.
- **What changed from the previous version.**
  - Generative AI moves from a side topic to a full meeting (M9) plus a thread through the labs and assignments.
  - Exams sit at M5 and M11. Proposals are presented at M7.
  - Classical instrumental variables (outside shifters of treatment, 2SLS, weak instruments), regression discontinuity,
    staggered DiD and synthetic DiD leave the core lectures. They become bonus reading and handouts.
  - Noncompliance in an RCT (the ITT, compliance types and the LATE) is not classical IV: it needs only potential
    outcomes and the draw, and it closes M2, in the lecture and in the notes.
  - The technical notes were rebuilt (v4) with proofs of the key results and a consistent house style.
- **Writing standard.** Readable by someone not taking the course, and not like AI-generated prose; the rules are in
  `editorial-guide.md`.

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
| Lab 2 | AI as **tool**: an LLM writes the A/B readout; students verify it with simulation tests |
| Lab 5 | AI as **decision-maker**: an LLM ranks customers from text profiles, evaluated by IPW against model rules |
| Lab 7 (optional) | AI as **analyst**: audit a tool-calling agent's observational analysis, then add a guardrail |
| Lab 9 | AI as **source of data**: LLM labels versus gold, PPI, embeddings as DML controls, a leakage demo |
| Lab 10 | AI as **intervention**: evaluate an AI staffing-tool rollout with DiD |
| A1 | Write the readout once by hand, then delegate it to an LLM and verify |
| A3 | A simulator fitted to the coupon logs, with a planted effect and a confounding dial, as the testbed for the logs-based estimators and policy (an LLM-coded feature to be decided) |
| M9 Section 3 (optional lab) | Three routes compared on the simulator: plug-in, decision-focused, policy tree |

## 3. Work remaining, in suggested order

1. **Instructor decisions and the technical pass.** Settle the items in `FLAGS.md`, then fix the technical statements
   it lists (in notes, slides and check scripts together).
2. **Slides: instructor review.** All eleven decks follow the pattern title, road map, block A, block boundary, block B,
   summary (exam meetings M5 and M11 have one lecture block), with the notes' Results in the notes' order and a
   `slidesNN_check.py` for every number.
3. **Labs 1–11.** Data and tasks are specified in the spreadsheet's Labs tab. The heaviest preparation is Lab 9
   (cached LLM outputs, gold labels) and Lab 7 (agent harness; optional for students).
4. **Assignments.**
   - A1 to A4 handouts.
   - The locked RCT evaluation set and an autograder for A2 and A3.
   - A simulator of the coupon logs with a planted effect and a confounding dial for A3, built on the generator
     behind Lab 7's logs; `m09_sim.py` is a template. An LLM-coded feature for A3 is to be decided.
   - A4 on panel data, built on the Rossmann rollout of Lab 10.
5. **Review passes.** Pass 2: independent check of every numbered Result. Pass 3: a student reads each meeting one
   week ahead.
6. **Optional.**
   - A pricing handout, "From elasticity to price": pricing from $\hat\theta(x)$, coupon menus, capacity. Source is old
     deck L9. Handouts are numbered in meeting order, so if it is written, it takes its meeting's place and the later
     handouts renumber.
   - Tag releases when the instructor asks.
   - Seed the M8 simulation.

## 4. Open judgement calls

Decide before building the affected pieces. Calls already settled are recorded in `README.md` (Decisions on record),
the syllabus and `CHANGELOG.md`.

1. Staggered DiD: the warning frame is in the M10 deck; whether Lab 10 adds it as an optional extension.
2. A2 and A3 pose the same decision (RCT-trained versus logs-trained), so both need an autograder and a locked set.
3. The proposal is due Sunday 8 November and presented two days later.
4. Whether A3 includes an LLM-coded feature (depends on the problem and the data available).
5. Final-project appendices: an LLM review of the draft plus responses, and a planted-effect validation of the design.
6. Exam weights: Exam II covers more lectures than Exam I; consider weighting it more.
