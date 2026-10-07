# Rules for AI assistants working in this repository

This is the course repository for SHBI-GB 7342, Applied Causal Inference for Business. Read `README.md` first: it says
what is current, how to build, and what is open.

## Files and versions
- **Edit files in place.** Never create versioned copies (`notes-v5.tex`, `slides_new.tex`, `notes-final.tex`,
  `backup/`). Git keeps the history.
- **One name per document:** `meetings/mNN/notes.tex`, `slides.tex`, `handout-HN-topic.tex`. Don't rename a file
  without being asked.
- Don't create new top-level folders or scratch files in the repository. Put scratch work outside it, or in a
  `build/` folder, which git ignores.
- Edit the style only in `shared/coursenotes.sty`. `shared/build_all.sh` copies it into each meeting folder.

## Git
- Before starting, run `git status`. If there are uncommitted changes you did not make, stop and ask.
- Commit after each coherent change, with a message saying what changed and why (for example,
  `M6: add capacity section; fix fairness split to 555/445`). Don't bundle unrelated changes.
- Tag only when the instructor asks (releases such as `v4.2`, `fall2026-week5`).
- Never rewrite history (`rebase`, `reset --hard`, force push) or delete tags.

## Content
- Every number in the notes is checked by `shared/checks/`. After changing a number, update the matching
  `*_check.py`, then run `bash shared/checks/run_all.sh`. Commit only when it passes.
- Rebuild what you changed (`bash ../../shared/build.sh notes` in a meeting folder) and confirm there are no LaTeX
  errors or undefined references.
- Record substantive content changes in `plan/CHANGELOG.md`, and update the "Open items" in `README.md` when you
  close or open one.
- Writing style: no em-dashes; direct, technically precise prose; follow `shared/notation.tex`.
