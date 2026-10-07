# Case B: Wen's Rate Decisions — Instructor Version

**Meetings 8–9. Instructor only: contains every answer and all future releases.**

## 1. What the case does

Two meetings, one question: *what happens to bookings if Meridian changes its rate?*

- **M8** answers it from the RM system's logs (adjustment and DML) and ends on the assumption the logs cannot check: unlogged overrides.
- **M9** answers it from a coin the booking engine flipped (IV). The M8 breakdown is the motivation for M9; do not let the two meetings read as separate cases.

Each meeting follows the course spine (`course-spine.md`): estimand → identification → estimation.

| Meeting | Estimand (vs break-even) | Assignment mechanism → identification | Estimation and uncertainty | Destination |
|---|---|---|---|---|
| M8 | average price elasticity of premium bookings: local and variance-weighted (vs −1.32) | the RM system's rule; unconfoundedness given the signals **measured as of pricing time**; overlap = off-rule variation | partially linear model; DML with cross-fitting (folds by night); date-clustered SE; partial-$R^2$ sensitivity | −1.56 [−1.64, −1.51]: **do not raise** |
| M9 | ITT of the member-rate offer; LATE on complier nights (vs −1.35) | the coin within hotel × month; exclusion, monotonicity, relevance (compliance types) | Wald ratio, 2SLS with strata; F-guard; direct-effect sensitivity | −1.55 (0.08): **roll out on complier nights** |

All numbers match `meetings/m08` and `m09`. **(sim)** marks simulation outputs still `\NUM`-flagged or figure-based in the decks.

**AI thread: AI as the decision-maker.** The RM system is an automated pricer, and its decisions are the confounder. This is M7's lesson with a continuous treatment: *the rule that set the treatment is what you must adjust for, and it must enter as flexibly as it was written.* In M9 the booking engine's coin is the only part of the system nobody could steer.

**Removed from class time:** the fish-market log-price IV and regression discontinuity (sharp and fuzzy) are in the M9 notes only. Exam II has no RD items. This case contains neither.

## 2. Release schedule

M8 has no critique case and no slack. If the meeting runs long, cut the elasticity discussion first and the partial-$R^2$ sensitivity second. In M9, critique C5 takes about minutes 0–15.

| Part | Meeting, block | About | Hand out at | Hold back until the attempt |
|---|---|---|---|---|
| M8-R1 | M8 A | 0–15 | `[RELEASE R1]` "Meridian Hotels" + "The Exhibit" | "The Number That Decides It"; "Pooled, Then Within Category" |
| M8-R2 | M8 A | 25–45 | `[RELEASE R2]` | the $\hat\theta = -1.0$ line; residual vectors |
| M8-R3 | M8 A/B | 45–65 | **at "Predict Before You Look"** (before the deck's R3 marker) | "The Ladder"; Attempts 1–3 |
| (R4) | M8 B | ~95 | `[RELEASE R4]` Wen's table | a reveal; no handout |
| M8-R5 | M8 B | 100–110 | `[RELEASE R5]` | "How Strong Would It Have To Be?" |
| M9-R1 | M9 A | 15–20 | `[RELEASE R1]` | "The Number That Decides It" |
| M9-R2 | M9 A | 20–50 | `[RELEASE R2]` | "As Shown, Then As Assigned"; "Four Kinds of Night"; "What the Ratio Estimates" |
| M9-R3 | M9 B | 60–75 | `[RELEASE R3]` | "A Placebo for Exclusion"; "Controls for Independence" |
| M9-R4 | M9 B | 80–95 | `[RELEASE R4]`; the city-hotel paragraph at "Weak Instruments" | "The Ladder"; the weak-instrument table |
| M9-R5 | M9 B | 95–103 | `[RELEASE R5]` | "The Audit, Answered" |
| M9-R6 | M9 B | 103–110 | "Wen's Table" | "The Recommendation" |

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
1. Contribution goes from 600 to 536. Bookings must rise more than $600/536 - 1 = $ **11.9%**. $\eta^* = \ln(600/536)/\ln(0.92) = $ **−1.35**. M8's DML said −1.56, but only if the overrides did no harm.
2. The coin randomises **what members were offered**. It does not randomise **what they were shown**, because managers could block or add.

### M9-R2
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

### M9-R3
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

### M9-R4
Ladder (sim):

| Comparison | Elasticity (SE) |
|---|---|
| shown vs not shown | +0.35 |
| pooled Wald ratio | −3.10 |
| 2SLS, hotel × month | −1.86 (0.15) |
| 2SLS + 47 signals | −1.84 (0.08) |
| **email-corrected** | **−1.55 (0.08)** |

The signals halved the SE but barely moved the estimate. The email correction moved it more than any control, because it is the only step that addresses an assumption.

City hotels:

| | Hand log | City hotels |
|---|---|---|
| First stage | 0.60 | 0.05 |
| SE of first stage | $\sqrt{(0.21 + 0.09)/500} = 0.024$ | $\sqrt{(0.1275 + 0.09)/200} = 0.033$ |
| $F$ | **600** | **2.3** |
| SE of ratio | 2.1 | $2.0/0.05 = $ **40** |
| Email bias | 2.0 | $1.2/0.05 = $ **24** |

- *Weak and slightly invalid is the worst combination.*
- The guard, written down in advance: report the first stage and $F$, clustered as the estimate will be. If $F < 10$, report the ITT and the first stage only. If $F$ is just above 10, use a weak-IV-robust interval (Anderson–Rubin, notes).
- $F > 10$ is a floor, not a certificate: a standard 5% t-test needs $F$ near 105 for correct size (Lee et al. 2022). Our 600 and 410 clear either bar.
- Full test $F$ = 410 (sim). The M9 workshop's perturbation shows the ratio drifting toward the "as shown" answer and coverage collapsing as the first stage falls.

### M9-R5

| Candidate | Relevance | Independence | Exclusion | Monotonicity |
|---|---|---|---|---|
| Competitor's rate | ✓ the system reacts to it | ✗ competitors see the same demand | ✗ guests compare rates directly | ? |
| Rainfall | ? weak | ✓ | ✗ rain moves demand itself | ? |
| System outage | ✓ | ? outages cluster at peak load | ✓ plausible | ✗ freezing raises some rates, lowers others |
| Manager on shift | ✓ managers differ | ✓ if the rota is set in advance | ? managers also upsell and handle groups | ? strict on weddings, lenient on conferences |
| Member-rate coin | ✓ 0.60 | ✓ within strata | ✗ the email, fixable | ✓ no reversals |

Most fail on **exclusion**, which the data cannot test in general. The coin passes because someone designed it, and even it failed once.

### M9-R6 (model memo)
> Switch the member rate on for nights managers now leave to the system and that are not forecast to sell out. The full test puts their elasticity at −1.55 ± 0.16, past the break-even of −1.35, worth about +1.7% of contribution. This is the complier nights' elasticity. It says nothing about peak nights, where a cut cannot sell rooms that do not exist. It rests on a correction that assumes the email works the same everywhere. Rerun with the email on both arms, and test the city hotels with a coin managers cannot override.

- Arithmetic: at −1.50, bookings $\times 1.133$ and contribution $536 \times 1.133/600 - 1 = +1.2\%$. At −1.55: +1.7%. Marketing's email-inflated −1.85 gives +4.2%: that is the number marketing will quote.
- **L8's DML and today's LATE average over different nights.** DML covers nights where the system left room to vary; the LATE covers compliers. A disagreement is not by itself a contradiction.

Grade memos on the same five dimensions as Case A. A memo that recommends the portfolio-wide rollout loses the "population" mark.

## 4. Deck issues found while aligning the case

The complete accepted change list, including the Codex-review corrections, is in `course-spine.md` §4.

1. **M8 release order.** The deck marker `[RELEASE R3]` sits after "Predict Before You Look" and "The Ladder", which already refer to 80 hotels and 47 signals. Move the marker before "Predict Before You Look" or hand R3 out there (as scheduled above).
2. **M8 outputs are figures.** "The Exhibit" and "Wen's Table" are figures (`fig-exhibit.pdf`, `fig-decision.pdf`). Their numbers are not in the slide text, so check them against the key above when the figures are regenerated.
3. **Simulation numbers.** M9's ladder, $F$ = 410 and the corrected estimate are `\NUM`-flagged.
4. **Case framing to add to the slides.** State on the M8 opening frame that the RM system is an automated decision-maker (the AI-as-decision-maker thread).
