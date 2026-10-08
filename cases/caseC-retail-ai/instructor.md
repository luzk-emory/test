# Case C: Dana's AI Assistant Rollout: Instructor Version

**Meetings 10–11. Instructor only: contains every answer and all future releases.** This case replaces the floor-lead staffing story. Meeting 11 was rewritten on 8 October for the synthetic-control meeting; its old staggered-adoption parts are kept at the end as a bonus (Parts B1–B3).

## 1. What the case does

A retail chain has rolled a generative-AI assistant out to its stores in stages. Should it confirm the next cohort (M10), and extend it to everyone, given what one early store shows (M11)?

This is **AI as an intervention to evaluate**: the chain tests an AI product the way it would test any other change, and the vendor's own metric is the first thing to set aside.

Each meeting follows the course spine (`course-spine.md`): estimand → identification → estimation. Here identification is **assumption-based, not design-based**. Say so out loud: go-live timing was not randomised.

| Meeting | Estimand (vs ¥10,000 sales per store-week) | Identification | Estimation and uncertainty | Destination |
|---|---|---|---|---|
| M10 | $ATT = E[Y_{it}(53) - Y_{it}(\infty) \mid G = 53]$, weeks 53–78 | parallel untreated trends, no anticipation, no spillovers; the threat is the sign-off order | 2 × 2 DiD; TWFE (= 2 × 2 with one date); SE clustered by store, then region; drift $\delta^*$ | 12.4 (SE 1.2); ramp 11.2 → 13.8: **confirm, keep the schedule** |
| M11 | flagship: $Y_{F,t}(20) - Y_{F,t}(\infty)$, one store | a donor trajectory fitted before week 20, frozen before the post-period; the flagship's treatment differs (co-development) | synthetic control; leave-one-out; in-place and in-time placebos (descriptive); comparison with DiD | flagship 15.9 (sim) = a ceiling for a different treatment; M10's 12.4 is the forecast: **roll out; stagger at random** |

The design-based alternative, randomising go-live dates (Athey and Imbens 2022), is in the M11 notes. It is what the memo's "two random halves" recommendation would make possible.

### Why the numbers were kept

Every exhibit uses the numbers in `meetings/m10` and `m11` unchanged: 120 stores, cohorts at weeks 53 and 79, ¥2,500 per store-week, 25% margin, the four cells, six quarters, three stores, three donors and the simulation outputs. The staffing arithmetic is sound and the simulation (`staffing-panel v1`) already exists. The AI story fits the same shape, including the ramp: associates learn the tool while its store catalogue fills in. So the slides need only a re-skin (Section 5).

New numbers, all narrative:
- the cost split (¥1,700 licence, ¥300 handsets, ¥500 champion allowance);
- the vendor dashboard's ¥38,000 "AI-assisted sales" and the claim of "fifteen times the fee";
- version 2 released in week 66.

None of them enters any estimate.

### What the AI context adds

Each of these attaches to a concept already on the slides:
1. **The vendor dashboard** (M10-R1, R5 #7): attribution is not a counterfactual. This is M1's coupon-redemption problem, now in a vendor's report.
2. **Training before go-live** (M10-R2, R5 #5): anticipation.
3. **Region sign-off after a privacy review** (M10-R2): why the treated were chosen when they were.
4. **Rotas re-planned around the assistant** (M10-R2, R5 #3): a post-treatment control.
5. **Handset-locked licences** (M10-R2): no spillovers.
6. **Version 2 on a calendar date** (Bonus B1, B3 #4): the two clocks, and whether "the treatment" is one thing over time.
7. **The flagship as co-development store** (M11-R1): a different version of the treatment, which is one more reason it is a ceiling.

## 2. Release schedule

M10 no longer has an exam (Exam II is now in M11, block A). The M10 times below were set when the case ran in block B only; **retime them when the M10 deck is rebuilt**. M11: block A is Exam II and the case runs in block B. Controlled projection copies are required for both meetings.

| Part | Meeting, block | About | Hand out at | Hold back until the attempt |
|---|---|---|---|---|
| M10-R1 | M10 B | 70–78 | `[RELEASE R1]` | "The Number That Decides It" |
| M10-R2 | M10 B | 78–92 | `[RELEASE R2]` | "Before, Across, and Both"; "Three Ways Parallel Trends Fails" |
| M10-R3 | M10 B | 92–105 | `[RELEASE R3]` | SE, drift and scale frames |
| M10-R4 | M10 B | 108–112 | `[RELEASE R4]` | "The Ladder" |
| M10-R5 | M10 B | 112–120 | `[RELEASE R5]` | "The Audit, Answered"; the memo can finish at home |
| M11-R1 | M11 B | 60–67 | `[RELEASE R1]` | the flagship's treatment frame |
| M11-R2 | M11 B | 67–82 | `[RELEASE R2]` | "The Synthetic Flagship"; "Donor Sensitivity" |
| M11-R3 | M11 B | 82–95 | `[RELEASE R3]` | design-freeze, placebo and falsification frames |
| M11-R4 | M11 B | 95–102 | `[RELEASE R4]` | the SC-vs-DiD frame |
| M11-R5 | M11 B | 102–110 | "Dana's Table" | the recommendation (the memo can finish at home) |
| B1–B3 | take-home | | with Handout H6 | the bonus key below |

Synthetic control now has all of block B.

## 3. Key: Meeting 10

### M10-R1
1. $0.25 \times \Delta > 2{,}500 \Rightarrow \Delta^* = $ **¥10,000** per store-week.
2. The three numbers:
   - Before/after (+15k) keeps the chain's own trend.
   - Across stores (+41k) keeps the level gap: cohort 1 stores were bigger.
   - The dashboard (38k) is **not a comparison at all**. It counts sales in which the assistant was *used*, including sales that would have happened anyway. The customer came in for the frying pan; the associate just checked the back room. That is the Sure Thing problem, exactly like counting coupon redemptions as coupon-caused purchases in M1. It is measured only in treated stores, it has no counterfactual, and the vendor has an interest in it.

   None of the three is yet the effect.
3. $38{,}000/2{,}500 = 15.2$ compares **sales** with **cost**. At 25% margin, even taken at face value, it is $9{,}500/2{,}500 = 3.8\times$. And face value is wrong (point 2).

   Line for the board: *usage is not impact.*

### M10-R2
1. (a) $196 - 181 = $ **15**; (b) $196 - 155 = $ **41**; (c) $(196 - 181) - (155 - 151) = $ **11**.
2. (c) goes against the break-even: 11, above 10 by only ¥1,000, not "several times over". $15 = 11 + 4$ (what every store did anyway); $41 = 11 + 30$ (cohort 1 stores were bigger before).
3. Estimand: $E[Y_{it}(53) - Y_{it}(\infty) \mid G = 53]$ over weeks 53–78. **Parallel trends:** $E[Y_{\text{after}}(\infty) - Y_{\text{before}}(\infty) \mid G = 53] = E[\,\cdot \mid \text{comparison}]$. Had cohort 1 not gone live, its sales would have changed as much as the comparison's. Levels may differ; trends may not. Rollout-file sentences:

| Sentence | Supports / puts at risk |
|---|---|
| Region sign-off order, after privacy review | timing not chosen by the store; but parallel trends becomes a claim about **regions**. Review order may track a region's IT readiness, size or growth |
| Training weeks 51–52, off the floor | **no anticipation**, *if* pulling associates off the floor did not thin service. If it did, weeks 51–52 are depressed and the DiD is biased **up** |
| Comparison = 89 not yet signed off | same format and calendar; their levels don't matter |
| Handset-locked licences; no shared catchment | **no spillovers** |
| Rotas re-planned | nothing yet. It warns that staff hours are now **caused by** the assistant (R5 #3) |

4. Answers worth drawing out:
   - a keen regional manager whose region was growing faster anyway (differential growth);
   - a region that signed off *because* of a bad quarter (a dip, then rebound);
   - a region whose stores opened or closed mid-panel (composition).

   Each is a reason sign-off order relates to where sales were heading. The first two leave traces in the pre-period (R3).

### M10-R3
1. Gaps 30, 30, 30, 30 | 38, 44. Minus Q4: 0, 0, 0, base | **8, 14**. The pre-period is flat: no differential growth, no dip. The post-period is a **ramp**, below break-even in Q5 and above in Q6. The DiD of 11 averages the two: a fact about the window, not the assistant.
2. Store-weeks: the same store counted 78 times, with serially correlated sales, gives a far-too-small SE.
   - Stores: $\sqrt{36/30 + 25/89} = 1.22$, CI **[8.6, 13.4]**, which straddles 10.
   - Regions: $\sqrt{9/3 + 6.25/9} = 1.92$, CI $11 \pm 2.23 \times 1.92 = $ **[6.7, 15.3]**.
   - Neither clears 10. Cluster at the level the treatment was assigned; with 12 clusters, the notes give the wild cluster bootstrap.
3. $11 - 2\delta = 10 \Rightarrow \delta^* = $ **0.5**, i.e. ¥500 per store-week per quarter, ¥2,000 over a year. It would move the gap by 1.5 from Q1 to Q4, about one store-level SE. **Flat pre-trends cannot rule it out.** Report $\delta^*$ and argue from the case whether a regional drift that large is plausible.
4. Yuan: $181 + 4 = 185$, effect 11.0. Percent: $181 \times 155/151 = 185.8$, effect 10.2. The choice moves ¥800 of a ¥1,000 margin. The pre-period gaps are flat in yuan; in percent they shrink from 20.5% to 19.7%. So use yuan, and say so.
5. Margin $= 0.25\Delta - 2{,}500$. Store-clustered [8.6, 13.4] → **[−¥350, +¥850]** per store-week; region-clustered [6.7, 15.3] → **[−¥825, +¥1,325]**. Neither excludes a loss.
6. With store-group effects only, the coefficient is **15**, the before/after, because only cohort 1's cells vary in $D$. Period effects bring in the comparison's +4 and give **11**. Each fixed effect is one of the DiD's two subtractions. (In an unbalanced panel, with closures, run the regression rather than one-pass demeaning.)

### M10-R4 (sim)

| Estimate | Value |
|---|---|
| Before/after | 16.1 |
| Cross-section | 42.3 |
| **TWFE** | **12.4** |
| SE: store-weeks independent / clustered by store | 0.3 / **1.2** |
| Largest pre-period coefficient | 0.5 |
| Q5 / Q6 | **11.2 / 13.8** |

Clustering multiplies the SE by four; the interval $12.4 \pm 2.35$ reaches break-even. With one adoption date, TWFE *is* the 2 × 2: double-demeaning the four cells gives exactly 11.

### M10-R5
| # | Problem, and the fix |
|---|---|
| 1 | Before/after keeps the chain trend. Report the DiD. |
| 2 | Store-weeks are not independent. Cluster by store: SE 1.2, and the interval reaches 10. |
| 3 | Managers re-planned rotas **because of** the assistant: staff hours are a post-treatment control (M7). They absorb part of the effect. |
| 4 | Fine only if closures are unrelated to the rollout. Report closures by group; a balanced panel changes who is compared. |
| 5 | Training ran in weeks 51–52 with associates off the floor. End the base period at week 50 and check. |
| 6 | Flat pre-trends are consistent with parallel trends, not proof. Report $\delta^*$. |
| 7 | **New.** The dashboard measures use, not effect. It has no comparison group, counts sales that would have happened anyway, and is the vendor's number. It confirms nothing. Drop it or label it as usage. |

Four of the seven are about what was compared, one about the interval, one about what was assumed, and one about whose number it is. None is about the estimator.

**Model memo:**
> Confirm cohort 2 for week 79 and keep the regions on their schedule. Clustered by store, the assistant adds ¥12,400 (SE 1,200) a store-week against a break-even of ¥10,000. It ramps from ¥11,200 in the first quarter to ¥13,800 in the second, i.e. about +¥300 then +¥950 of margin per store-week. This assumes cohort 1's regions would have tracked the comparison stores. Pre-trends are flat, but a regional drift of ¥800 per store-week per quarter would erase the average margin, and clustered by region the interval includes ¥10,000. The vendor's "assisted sales" figure measures use, not effect, and is not part of the evidence.

## 4. Key: Meeting 11

### M11-R1
1. The other large-format store is in a different city: different local shocks and trend. The never-treated average is a different format with a different trend.
2. The flagship's treatment was **the assistant plus a vendor engineer on site plus custom tuning** on its own data. That is a different version from what the 59 would get (consistency), and the store was chosen first, almost certainly because it was expected to do well. Both make the flagship an upper bound for a *different* treatment.

### M11-R2
1. $\tfrac12 A + \tfrac12 B = (100, 110, 120)$: an exact fit. Week 4: $\tfrac12(118) + \tfrac12(138) = 128$.
2. Effect $141 - 128 = $ **13**.
3. Without B: best convex fit $0.76A + 0.24C$ (weight $= 3{,}800/5{,}000$). Synthetic 97.2, 109.6, 122.0 | 129.3, gaps 2.8, 0.4, −2.0, so the effect is **11.7** with an acceptable fit. Without A: no mix of B and C gets below 110 in week 1. The best is B alone, with gaps of 10 every week and an effect of 3: **not reportable**.
4. Report the leave-one-out range over refits whose fit is acceptable: **[11.7, 13.0]**. A refit that cannot match the pre-period is evidence about the donor pool, not about the effect.

### M11-R3
1. **Freeze the design first:** donor pool (never-treated, no spillovers), fitting weeks, predictors, and the fit criterion. Hold-out check: fit on weeks 1–14 and see whether the frozen synthetic store predicts weeks 15–19. If it does not, it has no claim on weeks 20 onwards. Never tune the weights after seeing the post-period gap.
2. **No.** Rank 1 of 60 is a permutation p-value only if the flagship was as likely as any donor to be the treated store. The case says it was chosen first, as the co-development store. Report it as a descriptive ranking. (In the three-donor toy the pre-fit is exact, so the post/pre ratio is undefined: another reason it is not a test statistic there.)
3. **Local-boom falsification.** Run a placebo DiD: the four same-city never-treated stores against the other never-treated stores, before vs after week 20.
   - They share the local shock but not the treatment, so a positive gap there is a local boom, not the assistant. That would worry you.
   - It needs no spillovers from the flagship to them; the case says no shared staff or customers.
   - This changes the recommendation (investigate), not automatically the estimate.
4. **In-time placebo.** Refit on weeks 1–9 with a fake go-live at week 10. Weeks 10–19 are before anything happened, so the synthetic store should track the flagship with gaps near zero. A clear gap there means the method finds "effects" where there are none (a poor donor pool, or a store-specific shock), and the week-20 gap cannot be trusted either.

Real flagship (sim): weight on 4 donors, 15.9, leave-one-out [13.1, 17.4], in-place placebo rank 1 of 60. There is no standard error. In-time placebos move the go-live date earlier and check that no effect appears before week 20.

### M11-R4
1. Equal weights on A, B, C: pre-period means are flagship 110 and donors $(100 + 120 + 140)/3 = 120$; week 4 is 141 against $(118 + 138 + 165)/3 = 140.3$. DiD $= (141 - 110) - (140.3 - 120) = 31 - 20.3 = $ **10.7**, against synthetic control's **13**.
2. Equal weights on A and B: donors' pre mean 110, week 4 is 128, so DiD $= 31 - 18 = $ **13**. Here $\tfrac12 A + \tfrac12 B$ tracks the flagship exactly, so the level shift DiD allows is zero and the two estimates coincide. Donor C grows twice as fast; giving it a third of the weight drags the equal-weight DiD down.
3. Both are weighted comparisons:
   - **DiD** fixes the weights in advance (here equal), and allows a constant level gap. It relies on parallel trends.
   - **Synthetic control** chooses the weights to match the pre-period path, with no level gap, and relies on the fit.
   - Synthetic DiD sits in between: it chooses weights and also allows a level shift (notes, Section 3).

### M11-R5 (model memo)
> Roll the assistant out to the remaining 59 stores. Meeting 10's comparison with never-treated stores puts the gain at ¥12,400 of sales a store-week (SE 1,200), about +¥600 of margin after the ¥2,500 cost, rising from +¥300 in the first quarter to +¥950 in the second. This assumes the 59 stores, whose regions signed off last, would see what cohort 1 saw. The flagship's ¥15,900 is one store, chosen first, with a vendor engineer on site and no interval: it bounds the upside of a different treatment and is not the forecast. Stagger the remaining rollout in two random halves six months apart, so the next review has a clean comparison.

Margin arithmetic: $0.25 \times 12{,}400 - 2{,}500 = +$¥600; first quarter $0.25 \times 11{,}200 - 2{,}500 = +$¥300; second $0.25 \times 13{,}800 - 2{,}500 = +$¥950.

## Bonus key (Parts B1–B3)

These are the keys of the former Meeting 11 parts on staggered adoption, unchanged except for the part numbers. The former memo key (cohort event-time numbers) was dropped.

### B1
1. Neither yet. Before/after (14.3) keeps the trend. TWFE (6.1) is below break-even for a reason revealed in Part B2. The right answer is "it depends which comparisons each number uses".
2. Two clocks:
   - **event time:** associates learning to phrase questions; the assistant's store index filling in; novelty wearing off;
   - **calendar time:** **version 2 in week 66**; seasons; chain-wide promotions.

### B2
- DiDs: 1 → **8**; 2 → **16**; 3 → **8**; 4 → **0**.
- True effects: E week 2 = 8, E week 3 = 16, L week 3 = 8. Comparison 4 subtracts the *growth in E's own effect*: $\Delta Y_E = 4 + (16 - 8) = 12$, so $12 - 12 = 0$. Parallel trends holds exactly; the failure is what was called a control.
- Growing effects bias an already-treated comparison **down**; fading effects bias it up.
- TWFE on the nine cells $= \tfrac13(12) + \tfrac13(8) + \tfrac16(8) + \tfrac16(0) = $ **8**, against a true average of **10.7**. TWFE says no; the truth says yes once the effect has grown.

### B3
1. (sim) Static TWFE **6.1**, with 22% of its weight on already-treated comparisons. ATT(e) against never-treated: **7.4** at $e = 0$, 10.9 at $e = 4$, **13.6** at $e = 12$. The largest pre-period coefficient is 0.6. The effect crosses ¥10,000 within the first month and plateaus by month six.
2. Rollout-file sentences:
   - region order → timing not a store's choice, but regions may differ in trend;
   - nobody moved between cohorts → timing did not respond to recent results;
   - never-treated = last to sign off → their trends are checkable, their levels irrelevant.

   Nothing rules out that the last regions are also the ones whose sales were about to turn. Price it with the M10 drift band.
3. **Control eligibility (new; about 3 minutes; complete before the cohort evidence frame).**

   | Target | Base week | Eligible comparison | Excluded |
   |---|---|---|---|
   | Cohort 1, weeks 53–76 | 50 | never-treated **and** cohort 2 (not yet treated) | |
   | Cohort 1, weeks 77–104 | 50 | never-treated | cohort 2: training from week 77, live from 79 |
   | Cohort 2, weeks 79–104 | 76 | never-treated | cohort 1: already treated (Part B2's contamination) |

   - **Base week $g - 3$, not $g - 1$:** weeks $g - 2$ and $g - 1$ are training weeks with associates off the floor (anticipation, M10 audit #5).
   - Eligibility is necessary, not sufficient: each comparison still needs a parallel-trends argument.
   - The deck's $ATT(g, t)$ frame uses base $g - 1$; change it when re-skinning.
4. **Version 2 (new; discussion, about 5 minutes).**
   - Learning shows up by **event time**; a version effect shows up by **calendar time**. If version 2 matters, cohort 1's ATT(g, t) steps up at week 66 (its $e = 13$), beyond its learning curve. Cohort 2, on version 2 from $e = 0$, would show larger early effects than cohort 1 had at the same event week.
   - Averaging across cohorts at each $e$ mixes version 1 (cohort 1, $e < 13$) with version 2 (cohort 2), so the event-time path is part learning and part version.
   - The comparison of cohorts at equal $e$ is also a comparison of regions, so the two causes cannot be fully separated. Say so.
   - For the forecast: the 59 remaining stores start on version 2 or later, so cohort 2's own path is the most relevant, though shorter and from later-signing regions.
   - Point out what version 2 does **not** break: the clean DiDs against never-treated stores. Those stores never had any version, so the upgrade is part of "the treatment", and the question becomes whether the treatment was one thing (M1's well-defined intervention).
   - **Simulation note.** The deck's cohort numbers describe effects that depend on event time only, so on the current simulation the honest answer is "no evidence of a version effect". To let students find one, add a step at calendar week 66 for treated stores to `staffing-panel`, then recompute the M11 `\NUM` values.


## 5. Deck edits needed for this case

The general corrections from the Codex review are also in `course-spine.md` §4:
- no error bar at the base period;
- the placebo rank is descriptive;
- unbalanced-panel demeaning;
- margin units in the recommendation.

| Deck frame | Change |
|---|---|
| M10 "Today's Plan"; M11 "Today's Plan" | "staffing rollout" → "AI assistant rollout" |
| M10 & M11 "The Floor-Lead Model" | Retitle "Store Assistant". Use the R1 narrative and cost split. In M10 add the dashboard row (¥38,000) and the vendor's line |
| M10 "The Assumptions, Sentence by Sentence" | Sentence 1: add "after each region's data-privacy review". Sentence 2 → training in weeks 51–52. Sentence 4 → handset-locked licences + catchments |
| M10 "Three Ways Parallel Trends Fails" | Optional: add "privacy-review order tracks IT readiness" to the first row |
| M10 "The Analyst's Draft" / "The Audit, Answered" | Add sentence 7 (dashboard). Answer 3: "the assistant changed the rota" |
| M10 "The Recommendation" | Add the margin figures, and the line that the dashboard is not evidence |
| M11 "Two Clocks" | "a floor lead in week 1 is learning the store" → "in week 1 associates are learning the assistant". Add "version 2 in week 66" as a calendar-time example |
| M11 "Who Adopted First?" | Optional: add the version-2 question. Delete "it is also A4's individual question" (A4 no longer exists) |
| M11 "One Store, Two Years Ahead" | Add co-development: vendor engineer, custom tuning |
| M11 "The Cohort Recommendation" | Fix the units (margin, not sales gaps). Fill the `\NUM{x}` trend-sensitivity placeholder |
| M11 "Key Takeaways" | "final slides 48 hours before L12" → 24 hours (schedule v2) |
| Both decks | `\NUM{…}{case04-staffing: …}` provenance notes → point to this case |

The M11 deck is replaced, not re-skinned: the M11 rows above apply only if frames are reused for the bonus parts.
