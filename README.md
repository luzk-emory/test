# SHBI-GB 7342 Applied Causal Inference for Business: core materials

This folder holds the working core of the course: current sources, the scripts that verify every number, and the
documents that record the decisions. It is a git repository: each document has one file name, and its history lives in
git commits and tags, not in versioned copies (rules for AI assistants are in `AGENTS.md`). The pre-git material is in
`../_archive-2026-10-07.zip`.

## Layout

```
meetings/m01 ... m11/   notes.tex (technical notes), slides.tex (lecture slides), handout-*.tex,
                        coursenotes.sty (a synced copy, so each folder compiles on its own), figure files
shared/                 coursenotes.sty (master copy), notation.tex, build.sh, build_all.sh, checks/
pdf/                    combined notes, combined answer keys, notation sheet (generated; not tracked by git)
plan/                   schedule.xlsx, design-plan.md (the v4 design and decisions), CHANGELOG.md
syllabus/               syllabus.tex (needs updating, see below)
cases/                  case studies A to C, student and instructor versions (drafts)
reviews/                pass-1 review report (2026-10-07)
```

## Status of each kind of material

| Material | Version | State |
|---|---|---|
| Technical notes, M1–M11 | v4.1 (git tag `v4.1`) | Current. Pass 1 (arithmetic, wording) done; pass 2 (independent proof check) not yet |
| Handouts H1–H6 | v4.1 | Current, same review state as the notes |
| Lecture slides | v2 content | **Not yet revised to match v4 notes or the current schedule** |
| Schedule, labs, assignments, deadlines | `plan/schedule.xlsx` | Current source of truth |
| Syllabus | 24 Sep draft | **Out of date**: still has the older calendar (Exam I at M6, Monday meetings). Update from the spreadsheet |
| Cases A–C | draft | Developed separately from the schedule |

## Course structure (from the spreadsheet)

Meetings on Tuesday and Thursday. Each meeting has two 50-minute lectures (A, B) and a 60-minute lab (C).

| M | Topic | Handout | Notes |
|---|---|---|---|
| 1 | Causal basics | | |
| 2 | Experiments | H4 Interference | |
| 3 | Conditional effects | H6 Neural estimators | |
| 4 | Causal trees and forests | | |
| 5 | Evaluating targeting policies | | Exam I (M1–M4) |
| 6 | Allocation and policy learning | H5 Sequential decisions | |
| 7 | Observational data | H1 Instrumental variables | |
| 8 | Double machine learning | H2 Regression discontinuity | Proposal presentations |
| 9 | Generative AI in causal analysis | | |
| 10 | Panel data and DiD | H3 Staggered adoption | |
| 11 | Synthetic control (SDID, matrix completion in Section 3) | | Exam II (M5–M10) |
| 12 | Final presentations | | |

Four assignments; Labs 0–10; bonus reading is optional. Running cases: FitLife (fitness chain) in M1, M3, M7, M10,
H2, H3; QuickBite (food delivery) everywhere else.

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

`bash shared/checks/run_all.sh` reruns about 850 checks, one script per document, and prints only failures. It needs
Python 3 with numpy, scipy and scikit-learn.

Simulation scripts behind worked examples:
- `m08_sim.py`: M8 DML;
- `m08_fig.py`: M8 figure data, written into `meetings/m08/`;
- `m09_sim.py`: M9 simulators, slow, more than 5 minutes;
- `m11_sim.py`: M11 synthetic control;
- `h2_sim.py`: H2 regression discontinuity, writes `meetings/m08/h2_bins.csv`;
- `h3_check.py`: H3 staggered adoption.

After editing a number in the notes, update its check script, then rerun.

## Decisions on record

- Simulators and LLM-generated variables get a full meeting (M9), after DML. A learned simulator is both a data
  generator and the testbed for a whole predict-then-optimise pipeline.
- Proofs are light, for key results; identification theorems always get one.
- Six handouts. Synthetic DiD and matrix completion stay in M11, Section 3.
- Ported from the old causal-module decks (October 2026):
  - newsvendor and capacity, M6;
  - fairness as a priced constraint, M6;
  - causal (isotonic) calibration, M5;
  - predict-then-optimise / decision-focused / policy-learning spectrum, M6 and M9.
- Deferred: H7 "From elasticity to price" (pricing from $\hat\theta(x)$, coupon menus, capacity). Material is in the
  old L9 deck, now in the archive.

## Open items

1. Revise slides to match the v4 notes and the current schedule.
2. Update the syllabus from the spreadsheet.
3. Pass 2: independent check of every numbered Result. Pass 3: a student read, one meeting ahead.
4. Seed the M8 simulation so its numbers are exactly reproducible (text uses $-0.575$; runs give $-0.574$ to $-0.578$).
5. Confirm three citations:
   - Do-PFN (venue);
   - Chernozhukov et al., "Long story short" (still a working paper?);
   - Mandi et al. 2024, JAIR.
6. Optional: H7 handout; the M9 "three routes" lab (described in M9 Section 3).

Details for items 3–5 are in `reviews/pass1-mechanical-2026-10-07.md` and `plan/CHANGELOG.md`.
