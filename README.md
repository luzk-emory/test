# SHBI-GB 7342 Applied Causal Inference for Business: core materials

This folder holds the working core of the course: current sources, the scripts that verify every number, and the
documents that record the decisions. It is a git repository: each document has one file name, and its history lives in
git commits and tags, not in versioned copies (rules for AI assistants are in `AGENTS.md`). The pre-git material is in
`../_archive-2026-10-07.zip`.

**Start here:** `plan/revision-plan.md` is the brief for the fall 2026 revision: its purpose, how generative AI enters
the course, the schedule, the status of each component and the work remaining, in order.

## Layout

```
meetings/m01 ... m11/   notes.tex (technical notes), slides.tex (lecture slides), handout-*.tex,
                        coursenotes.sty (a synced copy, so each folder compiles on its own), figure files
shared/                 coursenotes.sty (master copy), notation.tex, build.sh, build_all.sh, checks/
pdf/                    combined notes, combined answer keys, notation sheet (generated; not tracked by git)
plan/                   revision-plan.md (the brief for the whole revision), schedule.xlsx,
                        design-plan.md (the v4 notes design and decisions), CHANGELOG.md
syllabus/               syllabus.tex (draft 3, generated from plan/schedule.xlsx)
cases/                  case studies A to C, student and instructor versions (drafts)
reviews/                pass-1 review report (2026-10-07)
```

## Status of each kind of material

| Material | Version | State |
|---|---|---|
| Technical notes, M1–M11 | v4.1 (git tag `v4.1`) | Current. Pass 1 (arithmetic, wording) done; pass 2 (independent proof check) not yet |
| Handouts H1–H6 | v4.1 | Current, same review state as the notes |
| Lecture slides | M1–M2 rebuilt (lecture case kept); M3–M11 v2 content | M1 and M2 aligned with the v4 notes, under review. **M3–M11 not yet revised** |
| Schedule, labs, assignments, deadlines | `plan/schedule.xlsx` | Current source of truth |
| Syllabus | Draft 3 (8 Oct) | Matches `schedule.xlsx`. Undecided items are marked `\tbd` (dates, weights, policies) |
| Cases A–C (lecture cases) | draft | M2-R6 (Case A), M9 (Case B) and M11 (Case C) rewritten 8 Oct to the current schedule; other release times to be retimed with each deck. Numbers in the rewritten parts are checked by `shared/checks/case_check.py` |

## Course structure (from the spreadsheet)

Meetings on Tuesday and Thursday. Each meeting has two 50-minute lectures (A, B) and a 60-minute lab (C).

| M | Topic | Handout | Notes |
|---|---|---|---|
| 1 | Causal basics | | |
| 2 | Experiments (closing with noncompliance and the LATE) | H1 Interference | |
| 3 | Conditional effects | H2 Neural estimators | |
| 4 | Causal trees and forests | | |
| 5 | Evaluating targeting policies | | Exam I (M1–M4) |
| 6 | Allocation and policy learning | H3 Sequential decisions | |
| 7 | Observational data | H4 Instrumental variables | |
| 8 | Double machine learning | H5 Regression discontinuity | Proposal presentations |
| 9 | Generative AI in causal analysis | | |
| 10 | Panel data and DiD | H6 Staggered adoption | |
| 11 | Synthetic control (SDID, matrix completion in Section 3) | | Exam II (M5–M10) |
| 12 | Final presentations | | |

Four assignments; Labs 0–10; bonus reading is optional. Lecture cases (`cases/`): a coffee chain (Case A, M1–M7), Meridian
Hotels (Case B, M8–M9) and a home-goods retail chain (Case C, M10–M11). The notes' worked examples deliberately use other
businesses: FitLife (fitness chain) in M1, M3, M7, M10, H5, H6; QuickBite (food delivery) everywhere else.

## Conventions in the notes

- Three sections per document:
  - Section 1, the general result: numbered Results with short proofs; examinable.
  - Section 2, a worked example and exercises; examinable.
  - Section 3, extensions and further reading; not examined.
- Handouts are not examined.
- One PDF per meeting, plus its handout if it has one.
- Answer keys build from the same source: `\def\KEY{}`.
- Notation follows `shared/notation.tex`. Net value is always $v(x)$; adoption-date potential outcomes are $Y_{it}(g)$.
- Writing style: no em-dashes; direct, technically precise prose.

## How to build

From a meeting folder, `bash ../../shared/build.sh notes` writes `build/notes.pdf` and `build/notes-key.pdf`
(handouts the same way; slides with `bash ../../shared/build.sh slides nokey`). Compiling `notes.tex` directly in an
editor also works. From the repository root, `bash shared/build_all.sh` syncs the style copies, rebuilds every
document and key, and writes the combined PDFs to `pdf/`. Edit the style only in `shared/coursenotes.sty`.

## How to check the numbers

`bash shared/checks/run_all.sh` reruns about 850 checks, one script per document (notes, handouts, rebuilt slides, rewritten case parts), and prints only failures. It needs
Python 3 with numpy, scipy and scikit-learn.

Simulation scripts behind worked examples:
- `m08_sim.py`: M8 DML;
- `m08_fig.py`: M8 figure data, written into `meetings/m08/`;
- `m09_sim.py`: M9 simulators, slow, more than 5 minutes;
- `m11_sim.py`: M11 synthetic control;
- `h5_sim.py`: H5 regression discontinuity, writes `meetings/m08/h5_bins.csv`;
- `h6_check.py`: H6 staggered adoption.

After editing a number in the notes, update its check script, then rerun.

## Decisions on record

- Simulators and LLM-generated variables get a full meeting (M9), after DML. A learned simulator is both a data
  generator and the testbed for a whole predict-then-optimise pipeline.
- Proofs are light, for key results; identification theorems always get one.
- Six handouts, numbered in meeting order (8 Oct): H1 interference (M2), H2 neural estimators (M3), H3 sequential
  decisions (M6), H4 instrumental variables (M7), H5 regression discontinuity (M8), H6 staggered adoption (M10). Synthetic
  DiD and matrix completion stay in M11, Section 3.
- Noncompliance in an RCT (ITT, compliance types, LATE) closes M2, lecture and notes (8 Oct). Classical IV (outside shifters,
  2SLS, weak instruments) stays in Handout H4 with M7, as bonus reading.
- Reading-and-critique exercises are dropped for now (8 Oct).
- Slides and notes share estimands, assumptions, notation, Result statements and topic order, but not the example:
  lectures keep their own case.
- Ported from the old causal-module decks (October 2026):
  - newsvendor and capacity, M6;
  - fairness as a priced constraint, M6;
  - causal (isotonic) calibration, M5;
  - predict-then-optimise / decision-focused / policy-learning spectrum, M6 and M9.
- Deferred: a pricing handout, "From elasticity to price" (pricing from $\hat\theta(x)$, coupon menus, capacity). Material is in the
  old L9 deck, now in the archive.

## Open items

1. Revise slides to match the v4 notes and the current schedule.
2. Syllabus: settle the items marked `\tbd` in `syllabus/syllabus.tex` (see `plan/revision-plan.md`, Section 7).
3. Pass 2: independent check of every numbered Result. Pass 3: a student read, one meeting ahead.
4. Seed the M8 simulation so its numbers are exactly reproducible (text uses $-0.575$; runs give $-0.574$ to $-0.578$).
5. Confirm three citations:
   - Do-PFN (venue);
   - Chernozhukov et al., "Long story short" (still a working paper?);
   - Mandi et al. 2024, JAIR.
6. Optional: a pricing handout ("From elasticity to price"); the M9 "three routes" lab (described in M9 Section 3).

Details for items 3–5 are in `reviews/pass1-mechanical-2026-10-07.md` and `plan/CHANGELOG.md`.
