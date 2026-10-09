# Flags

Open issues logged under `plan/editorial-guide.md`, Section 10. Format:
`- [ ] path/to/file:line | section | issue | options`. Tick an item when it is resolved, and say how in the pull
request that resolves it.

## Data sources and licenses (guide Section 7; resolve before the labs are built)

- [ ] syllabus/syllabus.tex:234; plan/schedule.xlsx (Labs, Lab 8) | 7 | Dominick's orange-juice scanner data (James M. Kilts Center, University of Chicago Booth): its terms of use cover academic research; redistribution to students and the required attribution are not recorded | confirm the terms and add a source line; or use another public scanner panel
- [ ] syllabus/syllabus.tex:236–237; plan/schedule.xlsx (Labs, Labs 10 and 11) | 7 | Rossmann store sales (Kaggle competition data): competition rules may restrict use outside the competition, including teaching redistribution | confirm the license; or switch to an openly licensed retail panel or a simulated panel
- [ ] syllabus/syllabus.tex:235; plan/schedule.xlsx (Labs, Lab 9) | 7 | "Public hotel reviews": no source or license named | name the corpus and its license, or generate synthetic reviews
- [ ] syllabus/syllabus.tex:230–232; plan/schedule.xlsx (Labs, Labs 4–7) | 7 | "Coupon RCT": source not stated, and the Labs sheet calls it real data. If it is the data behind the old causal-module decks, the brand question below applies too | name the source and license; or simulate it from Case A's design
- [ ] syllabus/syllabus.tex:228, 237; plan/schedule.xlsx (Labs, Labs 2 and 11) | 7 | Hillstrom email data and the California Proposition 99 panel: both public, but neither has a source line or terms recorded | add source lines (Hillstrom's MineThatData challenge; Abadie, Diamond, and Hainmueller 2010)

## Confidentiality and brand (guide Section 7)

- [ ] shared/coursenotes.sty:21; syllabus/syllabus.tex:13; the preamble of every deck in meetings/*/slides.tex | 7 | The accent color `sbgreen` is #00704A, labelled "Starbucks green" in plan/old-decks/lecture01.tex:29. It colors every slide title bar, Result box, and handout header, so a brand element appears in every student-facing document | change the hex value (a style-only edit in coursenotes.sty and the deck preambles; the macro name can stay or be renamed); or keep it with a decision that it is generic enough
- [ ] cases/caseA-coffee-chain/student.md:15; meetings/m01 to m07 | 7 | Case A's core example carries over the old Starbucks module's example under a fictional name: 10,000 loyalty members, 500 per arm, purchase rates 0.50 against 0.40, and analysts against executives with lifts of 20 and 5 points. The case states that all data are invented. No brand names, products, or loyalty-program terms appear in any student-facing file | confirm that the old module's numbers were invented teaching values and not company data; if not, change them (a technical pass: the M1 to M7 decks, notes, and check scripts depend on them)

## Open decisions behind `\tbd` placeholders (guide Section 1; never delete, resolve with the instructor)

- [ ] syllabus/syllabus.tex:42 | 1 | Meeting time (the dates are now set: Tuesdays and Thursdays, 20 October to 1 December) | instructor
- [ ] syllabus/syllabus.tex:43 | 1 | Room | instructor
- [ ] syllabus/syllabus.tex:44 | 1 | Instructor email and office hours | instructor
- [ ] syllabus/syllabus.tex:45 | 1 | Teaching assistant and office hours | instructor
- [ ] syllabus/syllabus.tex:46 | 1 | Companion text: chapter mapping | instructor
- [x] syllabus/syllabus.tex:82 | 1 | "and Meeting 9" is still marked open, but Meeting 9 keeping the hotel case was decided on 8 October | remove the marker in the next editorial pass (done: "Meetings 8 and 9")
- [ ] syllabus/syllabus.tex:120 | 1 | Prerequisites | instructor
- [ ] syllabus/syllabus.tex:162 | 1 | Assessment weights carried over from the previous draft | instructor
- [ ] syllabus/syllabus.tex:171 | 1 | Split of the 40 exam points between Exam I and Exam II | instructor
- [ ] syllabus/syllabus.tex:172 | 1 | Assignment team size | instructor
- [ ] syllabus/syllabus.tex:173 | 1 | Final-project point breakdown | instructor
- [ ] syllabus/syllabus.tex:205 | 1 | Whether A3 includes an LLM-coded feature | instructor, once the problem and data are set
- [ ] syllabus/syllabus.tex:292 | 1 | Due times; late-work policy | instructor
- [ ] syllabus/syllabus.tex:306 | 1 | School policy on AI use | instructor
- [ ] syllabus/syllabus.tex:310 | 1 | Academic integrity, accommodations, attendance, late work | instructor
- [ ] syllabus/syllabus.tex:407–412 | 1 | Lab tooling: language model and provider, student access and cost, agent harness, autograder and locked set, A3 simulator, computing environment | instructor, before the labs are built

## Editorial pass findings

- [ ] meetings/m04/notes.tex:100; meetings/m04/slides.tex:538, 567, 599 | 5 | The honest-estimation protocol labels its steps H1 Discover, H2 Estimate, H3 Recommend, which collide with the handout labels H1 to H6; the frame titles "H2: The Same Leaves on Half B" and "H3: The Card" also read as "Label: Title". Kept unchanged | rename to Step 1 to Step 3 or plain Discover / Estimate / Recommend (notes, slides, and Case A Parts M4-R3 to M4-R5 together); or keep
- [ ] meetings/m01/notes.tex:124; meetings/m01/slides.tex:420 | 4 | The box title of Assumption 1.5, "SUTVA", is never spelled out inside the box; the editorial pass spelled it out in the text before the box in both files instead of editing the box wording | leave; or spell out the box title in both files at once
- [ ] meetings/m01/slides.tex:978 | 6 | "the coupon cannot change a customer's Q2 segment" in the Q3 win-back frame. Probably intended (the segment is fixed before the campaign) | keep; or say "pre-campaign segment"
- [ ] meetings/m03/handout-H2-neural-estimators.tex (reading list) | 7 | Page ranges omitted as unverified for the four NeurIPS papers (Shi et al.; Louizos et al.; Rissanen and Marttinen; Curth et al.) and for Robertson et al. 2025 (Do-PFN, arXiv number given) | add pages from the official proceedings if wanted
- [ ] meetings/m02/notes.tex:297; meetings/m02/slides.tex:807 | 7 | The box title "The LATE theorem (Imbens and Angrist)" cites without a year, and box wording is frozen in the editorial pass | add "1994" in both files at once; or drop the names from the title (the reference list already carries Imbens and Angrist 1994)
- [ ] meetings/m02/notes.tex, slides.tex, handout-H1-interference.tex (reference lists) | 7 | Details not verified online and left out or taken from a secondary source: Holtz et al. 2025 (authors' first names), Kohavi, Tang, and Xu 2020 (place of publication), Johari et al. 2022 (first name of Pekelis), Angrist, Imbens, and Rubin 1996 (DOI; the JSTOR URL is given), Ugander et al. 2013 (DOI; the arXiv identifier is given) | check against the publisher pages and fill in
- [ ] meetings/m05/notes.tex:44 | 6 | "It is reach times average effect" describes $G(\pi) = \Pr(\pi=1)\,\E[v \mid \pi=1]$, which is reach times average net value $v$, not the effect; the slides say "net value". A technical statement, so the editorial pass left it | change to "reach times average net value"; or confirm the looser wording
- [ ] meetings/m05/notes.tex:346 (reading list) | 7 | Radcliffe 2007, *Direct Marketing Analytics Journal*: pages 14–21 confirmed, volume (sources say 1 or 3) and issue not | check the original issue and add volume (issue)
- [ ] meetings/m08/handout-H5-rd.tex:58 | 6 | The Fuzzy RD identification box lists continuity, monotonicity, and a nonzero jump but not exclusion (crossing the cut-off moves $Y$ only through $D$); it holds only if continuity is read for $Y(d)$ with no direct effect of $Z$. A technical statement, so the pass left it | add exclusion to the box in a technical pass; or leave
- [ ] meetings/m08/slides.tex:942 | 7 | The event-flag benchmark ($R^2_D = 0.04$, $R^2_Y = 0.06$) is not in the Case B files; `slides08_check.py` takes it as a given input | add it to `cases/caseB-meridian`
- [ ] meetings/m08/notes.tex, handout-H5-rd.tex (reading lists) | 7 | Imbens and Lemieux 2008: DOI not confirmed, left out. Cattaneo, Idrobo, and Titiunik: dated 2020 (paperback; the online Element is 2019). Chernozhukov et al., "Long Story Short": cited as NBER Working Paper 30302 (2022); possibly forthcoming in the *Review of Economics and Statistics* | confirm and update
