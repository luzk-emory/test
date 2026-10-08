# Case B: Wen's Rate Decisions: Instructor Version

**Meetings 8–9. Instructor only: contains every answer and all future releases.** Meeting 9 was rewritten on 8 October for the generative-AI meeting; its old IV parts are kept at the end as a bonus (Parts B1–B4).

## 1. What the case does

Two meetings, one question: *what happens to bookings if Meridian changes its rate, and how should it set rates?*

- **M8** answers it from the RM system's logs (adjustment and DML) and ends on the assumption the logs cannot check: unlogged overrides.
- **M9** keeps the question and brings in generative AI in both of its roles. A simulator learned from the M8 logs tests the M8 estimator against the override problem, and tests whole pricing pipelines (block A). A language model reads guest reviews for a randomised rate test's guardrail, and text becomes DML controls (block B). The M8 breakdown is the motivation for M9; do not let the two meetings read as separate cases.

Each meeting follows the course spine (`course-spine.md`): estimand → identification → estimation.

| Meeting | Estimand (vs break-even) | Assignment mechanism → identification | Estimation and uncertainty | Destination |
|---|---|---|---|---|
| M8 | average price elasticity of premium bookings: local and variance-weighted (vs −1.32) | the RM system's rule; unconfoundedness given the signals **measured as of pricing time**; overlap = off-rule variation | partially linear model; DML with cross-fitting (folds by night); date-clustered SE; partial-$R^2$ sensitivity | −1.56 [−1.64, −1.51]: **do not raise** |
| M9 | the elasticity again (vs −1.32); regret of a pricing pipeline against an oracle; the rise's effect on value complaints (guardrail: 5 points) | a simulator's effects are g-formula effects: the M8 assumption, with the truth planted; the Q3 test is randomised | estimator and pipeline testbeds on two simulators; backtest; PPI with a gold subsample; text embeddings as controls | Q3 test −1.72 [−2.07, −1.38]: **do not raise**; pilot DML pricing inside the logged range with a holdout; guardrail 0.03 (SE 0.023): not tripped, not cleared |

M8 numbers match `meetings/m08`. M9 numbers are the case's own (the M9 notes use a food-delivery example) and are checked by `shared/checks/case_check.py`. **(sim)** marks simulation outputs still `\NUM`-flagged or figure-based in the decks.

**AI thread.** In M8, AI as the decision-maker: the RM system is an automated pricer, and its decisions are the confounder. This is M7's lesson with a continuous treatment: *the rule that set the treatment is what you must adjust for, and it must enter as flexibly as it was written.* In M9, generative AI as a simulator (block A) and as a source of data (block B), with the vendor's engine as a candidate decision-maker.

**Not in class time:** regression discontinuity (Handout H2, with M8) and instrumental variables beyond M2 (Handout H1). The bonus Parts B1–B4 are for students who want the IV version of Wen's question.

## 2. Release schedule

M8 has no slack. If the meeting runs long, cut the elasticity discussion first and the partial-$R^2$ sensitivity second. M9's times are provisional until the M9 deck is written.

| Part | Meeting, block | About | Hand out at | Hold back until the attempt |
|---|---|---|---|---|
| M8-R1 | M8 A | 0–15 | `[RELEASE R1]` "Meridian Hotels" + "The Exhibit" | "The Number That Decides It"; "Pooled, Then Within Category" |
| M8-R2 | M8 A | 25–45 | `[RELEASE R2]` | the $\hat\theta = -1.0$ line; residual vectors |
| M8-R3 | M8 A/B | 45–65 | **at "Predict Before You Look"** (before the deck's R3 marker) | "The Ladder"; Attempts 1–3 |
| (R4) | M8 B | ~95 | `[RELEASE R4]` Wen's table | a reveal; no handout |
| M8-R5 | M8 B | 100–110 | `[RELEASE R5]` | "How Strong Would It Have To Be?" |
| M9-R1 | M9 A | 0–10 | `[RELEASE R1]` | the frame that names the simulator's assumption |
| M9-R2 | M9 A | 10–25 | `[RELEASE R2]` | bias and coverage frames |
| M9-R3 | M9 A | 25–45 | `[RELEASE R3]` | regret table reveal; home advantage; support |
| M9-R4 | M9 A | 45–50 | `[RELEASE R4]` | "Planted vs asserted truth" |
| M9-R5 | M9 B | 60–85 | `[RELEASE R5]` | error-by-arm and PPI frames |
| M9-R6 | M9 B | 85–100 | `[RELEASE R6]` | leakage and overlap frames |
| M9-R7 | M9 B | 100–110 | "Wen's Table" | the recommendation (the memo can finish at home) |
| B1–B4 | take-home | | with the notes | the bonus key below |

Controlled projection copy for M8 is still required: do not project residual vectors before R2's attempt. **The simulation's true elasticities are never shown in lecture**; they appear only in the M8 and M9 workshop comparisons.

## 3. Key, part by part

### M8-R1
- Contribution goes from 600 to 664, up **10.7%**. Break-even: $\eta^* = \ln(600/664)/\ln(1.08) = $ **−1.32**. Bookings must fall by less than $1 - 600/664 = 9.6\%$.
- Pooled: deviations $P$ = −30, −20, −10, 10, 20, 30; $Q$ = −40, −50, −60, 60, 50, 40. $\sum \tilde P \tilde Q = 5{,}600$ and $\sum \tilde P^2 = 2{,}800$, so the slope is **+2.0**.
- Most pairs raise rates on the pooled number. That is the point of the commit.

### M8-R2
- Residuals: $\tilde P$ = −10, 0, 10, −10, 0, 10 and $\tilde Q$ = 10, 0, −10, 10, 0, −10. The slope is $-400/400 = $ **−1.0**: same six nights, opposite sign.
- DAG: demand signals → rate (+) and demand signals → bookings (+). The omitted-variable bias is positive and large enough to flip the sign.
- Sentences:
  - *Only the RM system sets rates* → no unrecorded input moves $P$.
  - *Every input is in the feed* → nothing it saw is missing from $X$.
  - *Rates still move* → there is residual variation to compare.
  - A night priced exactly by the rule has $\tilde P = 0$ and **answers nothing**.
- Tell students to **hold onto the first sentence**; R5 breaks it.

### M8-R3
- Ladder: pooled +0.40; within hotel +0.49 (the system charges different rates at the same hotel on different nights); hotel × occupancy band −0.07 (right sign, almost no magnitude). Destination −1.56.
- Typical proposals and their failures:
  1. **47 linear controls: −0.54.** The rule is a staircase and the model is a ramp. It misses the bands and the weekend × band interaction.
  2. **Boosted model with price as a feature: −1.03.** Price stands in for the signals. The competitor-index share falls from 4.2% to 0.9% when $\ln P$ is added.
  3. **Residualise both sides in-sample: −0.95.** The flexible model memorises rows; its in-sample $R^2$ is 0.97. Well-regularised in-sample gives −1.57 and cross-fitted −1.56. The bias grows with flexibility and cannot be sized from inside the fit.
- **DML** (residualise both sides + cross-fit, folds by night, date-clustered SE): −1.56, 95% CI [−1.64, −1.51].
  - The bias from nuisance errors is second-order: products of the two errors, plus the price model's squared error. That is why both sides are residualised.
- Task 4: same-night booking pace recorded after the rate posted is partly *caused* by the rate. So is a competitor index that reacts to Meridian's own rate. Both are post-treatment. **Every control must be measured as of the moment the RM system set the rate**; otherwise it enters as a mediator or a collider (M7).
- Decision table (the deck figure; sim):
  - +8% rate: bookings −11.3%, contribution −1.9%.
  - −4%: +0.9%. −8%: +1.7%.
  - **Do not raise.** A modest cut is worth testing deliberately.
  - The formula optimum ¥557 lies far outside the ¥703–910 range the system varied over, holding signals fixed. $\theta$ is a local slope.
  - The optimum also inherits the interval: $P^* = 200\kappa/(\kappa - 1)$ maps the CI $\kappa \in [1.51, 1.64]$ to **[¥513, ¥592]**. The whole range lies outside the support, which is one more reason to *test* a modest cut rather than jump.
- Overlap: on 12% of nights the rate is pinned to the rule. Those nights carry almost no weight.

### M8-R5
1. The first sentence, *the RM system is the only thing setting rates*, is false. The unlogged reason (local knowledge $U$) moves both rate and bookings.
2. No. $U$ is not in $X$, and flexibility in $g(X)$ cannot adjust for a variable that isn't there.
3. How much residual variation the overrides explain in **both** rate and bookings. The deck's sensitivity table: partial $R^2$ of 1% → bias 0.03; 2% → 0.06; 5% → 0.15; **10% → 0.32**, which reaches break-even.

   The recommendation survives **conditionally**. Sensitivity prices the doubt; it does not remove it. Bridge line: *"Next time: rates the hotel did not choose."*

### M9-R1
1. **Unconfoundedness given the signals**, with positivity and consistency: the M7 and M8 assumption. The simulator learned $\E[Y \mid D, X]$ and the distribution of $X$ from the logs; sampling from it at a new rate is the g-formula. Its "bookings at another rate" are causal only if the logs' rates were as good as random given the 47 signals. The overrides are exactly where that fails.
2. **From the data:** the signals' joint distribution, the shape of demand across nights, the noise. **From the analyst:** the elasticity −1.50, the override effect (+12% demand, +10% rate) and its 8% share.
3. **No.** A simulator learned from confounded logs inherits their confounding, and the truth inside it is planted by the team. It can test whether an estimator recovers a truth on data shaped like Meridian's. It cannot reveal Meridian's truth.

### M9-R2
1. Bias (mean − (−1.50)): **+1.92, +0.32, +0.01, +0.09, +0.13**.
2. DML with boosted trees: unbiased with near-nominal coverage (0.94) on this data shape. The RM rule is a step function of bucketed signals with interactions. Lasso fits it with smooth linear terms, so part of the rule stays in the residuals (regularisation bias), and coverage falls to 0.71.
3. If the real overrides act like the planted ones, DML is about 0.13 too close to zero, so the truth is near $-1.56 - 0.13 = $ **−1.69**. That is further from −1.32, so the decision **does not change: do not raise**.
4. Whether the real overrides look like the planted ones. Their size and correlation with demand were **chosen**; the logs cannot reveal them. Turn the dial (A4 does) and report the decision across settings: that is a sensitivity analysis, not a measurement.

### M9-R3
1. Boosted simulator: vendor 380 < DML 690 < RM 1,450. Neural: DML 760 < RM 1,520 < vendor 2,240. Worst-case regret: RM 1,520, vendor 2,240, **DML 760, the smallest**.
2. **Home advantage.** The vendor's demand model and the boosted simulator are the same model class fitted to the same logs, so the vendor's errors are the simulator's errors. The neural simulator does not share them. A pipeline should be ranked across simulators of different classes, never on its own class alone.
3. Neither simulator has data above ¥1,920; both extrapolate the shapes they learned. On 14% of the vendor's nights the regret measures one model against another, not against reality. Treat those nights as untested, or cap rates at the logged range.
4. **The optimiser's curse.** Choosing, every night, the rate with the highest *predicted* contribution selects the rates where the prediction is most optimistic. This is the winner's curse of M4, and it is why the realised loss exceeds the model's average error. Errors compound: the prediction error becomes a pricing error.
5. Near current rates both simulators pass: $4.6$ is 0.2 from 4.8 and $3.4$ is 1.4 from it, about one SE. The backtest is weak evidence (it rejects neither) and says nothing above ¥1,920, where the two pipelines differ most. A backtest earns trust only in the region it covers.
6. **DML elasticity, then optimise**: the smallest worst-case regret, and it stays inside the logged range. Run it with a **holdout**: a random 10% of hotel-nights stay on the current rule (or alternate by night, a switchback), so realised contribution can be compared. Pilot the vendor's engine the same way, only with rates capped at the logged range.

### M9-R4
1. In R1 the analyst planted the truth on top of what was learned from Meridian's own logs, so an estimator can be checked against it. Here the truth is **asserted**: it is whatever the language model's priors say about guests in general. Nobody planted it, and nothing ties it to Meridian's guests.
2. Believe the evidence with a design: M8 (−1.56, conditional on its assumption), the testbed (direction of the override bias), and above all a randomised test. The Q3 test (R5) settles it: −1.72. The synthetic number is a hypothesis, not evidence.
3. **No.** A testbed needs a known truth on the business's data shape; the synthetic guests' truth is unknown. (CEVAE sits on the same side: its identification rests on structure it does not state.)

### M9-R5
1. Model labels: $0.22 - 0.15 = $ **0.07**, which trips the 5-point guardrail.
2. Gold rates: higher $36/200 = 0.18$, current $28/200 = 0.14$, effect **0.04**. Higher arm: catches $34/36 = 0.944$, flags $12/164 = 0.073$. Current arm: catches $26/28 = 0.929$, flags $4/172 = 0.023$.
3. **Differential error.** On higher-rate nights more reviews mention the price without complaining (*"worth it even at this price"*), and the model flags them, so the false-positive share is three times higher. The treatment changed the text, and with it the model's error.
4. Non-differential error with the current arm's shares scales the effect by $26/28 - 4/172 = 0.905$: $0.905 \times 0.04 = $ **0.036**, attenuated toward zero. The actual 0.07 is **inflated**: differential error manufactured about 0.03 of the effect.
5. PPI. Higher: model rate in the subsample $46/200 = 0.23$, correction $0.18 - 0.23 = -0.05$, corrected **0.17**. Current: $30/200 = 0.15$, correction $-0.01$, corrected **0.14**. Effect **0.03**.
   - **Unbiased:** each arm's correction is estimated from a random subsample *of that arm*, so the corrected rate is unbiased whatever the error looks like, provided the gold labels are right.
   - **More precise:** the 5,000 model labels carry the level; gold labels only estimate a small correction, whose variance (about 0.07 and 0.03 per review) is far below the outcome's (about 0.15 and 0.12).
   - SEs: $\sqrt{0.22 \cdot 0.78/5000 + 0.0675/200} = 0.019$ and $\sqrt{0.15 \cdot 0.85/5000 + 0.0299/200} = 0.013$, so 0.023 for the effect; gold alone $\sqrt{0.18 \cdot 0.82/200 + 0.14 \cdot 0.86/200} = 0.037$. (The gold reviews are a subsample of the 5,000, so this SE is a slight approximation; the notes say how.)
6. Corrected 0.03, 95% CI $[-0.015, 0.075]$. Below the guardrail at the point estimate, but the interval includes 5 points: **not tripped, not cleared**. A larger gold sample would settle it; here the bookings result makes it moot.
7. $\ln(1 - 0.124)/\ln 1.08 = $ **−1.72**; interval from $-12.4\% \pm 1.96 \times 1.2\%$: **[−2.07, −1.38]**. That is consistent with M8 (−1.56) and the testbed (about −1.69), and it excludes the break-even of −1.32, narrowly. **Do not raise.**

### M9-R6
1. Listing pages **as of each night** are pre-treatment: written before the rate, they proxy for quality, a confounder. Legitimate. That night's **reviews** are written after the stay: caused by the rate (value perceptions) and by bookings (crowding). They are post-treatment, and they encode the outcome. **Leakage**; never a control.
2. DML uses only the variation in the rate left after the controls, so its SE scales roughly as $1/\sqrt{\text{share left}}$: from 9% to 1% is a factor of $\sqrt{9} = 3$ (0.03 → 0.09); from 9% to 6%, $\sqrt{1.5} = 1.22$ (0.04). **Overlap collapse**: almost no rate variation remains that the text cannot predict.
3. The reviews carry part of the effect and the outcome itself. Controlling for them absorbs the effect (as a mediator would) and opens collider paths, which pulls the estimate toward zero: −0.97.

### M9-R7 (model memo)
> Do not raise midweek premium rates by 8%. The Q3 test puts the elasticity at −1.72 (95% CI −2.07 to −1.38), past the break-even of −1.32, and it agrees with Meeting 8's −1.56 once the override bias the testbed found is allowed for. Pilot DML-based pricing, with rates capped at the logged range and 10% of hotel-nights held out on the current rule. Pilot the vendor's engine only on the same terms: it won only on a simulator built like itself. The synthetic-guest report is not evidence; its −0.9 is the model's prior, and the Q3 test contradicts it. On reviews, the model's labels said complaints rose 7 points, but the gold-corrected rise is 3 points, with an interval up to 7.5, so the guardrail neither tripped nor cleared. The advice rests on Q3 at 40 hotels carrying over to all 80.

Grade on the same five dimensions as Case A.

## Bonus key (Parts B1–B4)

These are the keys of the former Meeting 9 (instrumental variables), unchanged except for the part numbers. The full-test ladder and the city hotels (former R4) and the IV memo (former R6) were dropped.

### B1
1. Contribution goes from 600 to 536. Bookings must rise more than $600/536 - 1 = $ **11.9%**. $\eta^* = \ln(600/536)/\ln(0.92) = $ **−1.35**. M8's DML said −1.56, but only if the overrides did no harm.
2. The coin randomises **what members were offered**. It does not randomise **what they were shown**, because managers could block or add.

### B2
1. As shown: $(350 \cdot 64 + 50 \cdot 40)/400 = 61.0$ vs $(150 \cdot 90 + 450 \cdot 70)/600 = 75.0$, a difference of **−14.0**.
2. As assigned: heads 71.8, tails 67.0, **ITT = +4.8**.
3. First stage: $0.70 - 0.10 = $ **0.60**.
4. Most pairs who used row 1 say "never cut". Same log, opposite sign: managers chose which heads to honour.
5. Ratio: $4.8/0.60 = $ **8.0** extra bookings on nights the coin switched the rate on, for the **compliers**. $SE(\mathrm{ITT}) = 20\sqrt{2/500} = 1.26$, so $SE \approx 1.26/0.60 = 2.1$ and the CI is [3.9, 12.1].

   On a base of 60, that is an elasticity from −0.75 to −2.21. **It straddles −1.35**: a thousand nights cannot decide. Cluster by date in the full test.
6. Night types:
   - always-takers (dead nights; the manager applies the rate by hand): 0.10;
   - never-takers (near sell-out; the manager blocks it): 0.30;
   - compliers: 0.60;
   - defiers assumed 0.
7. $\ln(68/60)/\ln(0.92) = $ **−1.50**: past break-even, on complier nights.
8. Sentences:
   - within hotel × month → **independence given strata**;
   - one thing changed → **exclusion**;
   - most heads honoured → **relevance** (0.70 vs 0.10);
   - none reversed → **monotonicity**.

   Randomisation buys only the first. Hold onto the second.

### B3
1. ITT becomes 6.0, the ratio 10.0 and the elasticity $\ln(70/60)/\ln(0.92) = $ **−1.85**. Bias $= 1.2/0.60 = 2.0$ bookings: **the ratio divides the violation by the first stage.** Nothing in the test log shows it.
2. The old-engine hotels' first stage is zero by construction, so their heads–tails gap of 1.2 is the email alone. Corrected ratio $(6.0 - 1.2)/0.60 = $ **8.0**.
   - The correction assumes the email works the same everywhere: a patch, not a proof.
   - The clean fix is design: send the email on both sides of the coin.
   - A zero-first-stage group is almost the only place exclusion can be tested.
3. Within type: resort $4.8/0.60 = 8.0$; airport $4.8/0.60 = 8.0$. Pooled: heads $(350 \cdot 84.8 + 150 \cdot 54.8)/500 = 75.8$ and tails $(150 \cdot 80 + 350 \cdot 50)/500 = 59.0$, so the ratio is $16.8/0.60 = $ **28.0**. Heads nights are mostly resort nights. **Here controls buy independence, not precision.**
4. Controls:
   - **Required:** hotel × month, which sets the coin's probability.
   - **Optional:** the 47 signals, which shrink the SE.
   - **Never:** "manager overrode" and "rate shown", which the coin caused (M7's bad controls).
   - 2SLS is FWL applied to the ratio. Running the two stages by hand gives the right point estimate but the **wrong SE**, because the fitted regressor is treated as data. Take the SE from the IV routine.
5. With direct effect $a$: $\text{LATE} = (6.0 - a)/0.60$, and the elasticity is $\ln\{(60 + \text{LATE})/60\}/\ln 0.92$.

   | $a$ | 0 | 1.2 | **1.71** | 2.4 |
   |---|---|---|---|---|
   | elasticity | −1.85 | −1.50 | **−1.35 (break-even)** | −1.14 |

   The old-engine placebo measured 1.2, only about 0.5 bookings from the point where the cut stops paying. The data cannot say which column is true; the table prices the doubt.
6. **If the email continues, it is part of the policy, not a bias.** Exclusion matters only for attributing effects to the *rate*. Wen then needs the effect of the programme as it will run, which is the ITT side (ITT 6.0 bookings per heads night, with managers' overrides included), converted to contribution. The email-corrected elasticity answers a different question: the member rate *without* the email. Make students say which programme they are pricing.

### B4

| Candidate | Relevance | Independence | Exclusion | Monotonicity |
|---|---|---|---|---|
| Competitor's rate | ✓ the system reacts to it | ✗ competitors see the same demand | ✗ guests compare rates directly | ? |
| Rainfall | ? weak | ✓ | ✗ rain moves demand itself | ? |
| System outage | ✓ | ? outages cluster at peak load | ✓ plausible | ✗ freezing raises some rates, lowers others |
| Manager on shift | ✓ managers differ | ✓ if the rota is set in advance | ? managers also upsell and handle groups | ? strict on weddings, lenient on conferences |
| Member-rate coin | ✓ 0.60 | ✓ within strata | ✗ the email, fixable | ✓ no reversals |

Most fail on **exclusion**, which the data cannot test in general. The coin passes because someone designed it, and even it failed once.


## 4. Deck issues found while aligning the case

The complete accepted change list, including the Codex-review corrections, is in `course-spine.md` §4.

1. **M8 release order.** The deck marker `[RELEASE R3]` sits after "Predict Before You Look" and "The Ladder", which already refer to 80 hotels and 47 signals. Move the marker before "Predict Before You Look" or hand R3 out there (as scheduled above).
2. **M8 outputs are figures.** "The Exhibit" and "Wen's Table" are figures (`fig-exhibit.pdf`, `fig-decision.pdf`). Their numbers are not in the slide text, so check them against the key above when the figures are regenerated.
3. **The M9 deck is replaced.** The old IV deck's frames (Wald ratio, ladder, $F = 410$) survive only in git history (commit `5522695`) and in the bonus parts. The new deck follows the M9 notes' order with this case's numbers.
4. **Case framing to add to the slides.** State on the M8 opening frame that the RM system is an automated decision-maker (the AI-as-decision-maker thread).
