# Case A: Lin's Coupon Programme: Instructor Version

**Meetings 1–7. Instructor only: contains every answer and all future releases.** Distribute the student parts one at a time, on paper or as single-part files, never the full student file in advance.

## 1. What the case does

One decision runs through seven meetings: *should this coffee chain send coupons, to whom, and was the programme it ran worth it?* Every meeting adds one reason the previous number was not yet the decision number.

Each meeting follows the course spine (`course-spine.md`): **estimand → identification → estimation**, with uncertainty taken from the design.

| Meeting | Estimand (and the number that decides it) | Assignment mechanism → identification | Estimation and uncertainty |
|---|---|---|---|
| M1 | sample ATE in the Q2 region; the pilot's ATT/ATU; net per coupon vs $p_1/3$ | the seed: complete randomisation, contrasted with marketing's selection | difference in means (= OLS on a dummy); spread over redraws |
| M2 | sample ATE and net value (CI vs 0.167); ATE on other lists; a store-level offer | randomisation; transport via stable segment effects; cluster assignment | Fisher test; **Neyman variance, conservative**; net-value CI; CUPED; MDE; DEFF |
| M3 | $\tau(x)$; the rule $\tau(x) > \mu_1(x)/3$; a list's ATE under target weights | randomisation within $x$; overlap by design; support only for pre-Q2 members | interaction model, S/T learners; SE of the segment gap |
| M4 | leaf effects of a frozen partition vs each line's break-even | randomisation within the partition committed before half B | honest leaf means and SEs; winner's-curse arithmetic |
| M5 | gain of a frozen list vs ¥1.50 | known coin probability $e$ | IPW contributions; paired SE between lists |
| M6 | net value under a cap, budget and risk | push-test randomisation; transport to Q4 | plug-in $v_i$; ranking; $\lambda^*$; reserve; value lower bound |
| M7 | ATT of the programme as run vs 0.133 | the engine's rule is the assignment mechanism: unconfoundedness given its inputs, overlap by band | **outcome-free design stage first**; standardisation; IPW; ESS; trimming |

All numbers match the current decks in `meetings/m01`–`m07`. Numbers marked **(sim)** below are simulation outputs still flagged `\NUM` in the decks; check them when the simulations are rerun.

## 2. The AI thread (four roles, no new lecture content)

| Role | Where in this case |
|---|---|
| AI as a source of data | **M3-R6** (Lab 2 opener): a language model labels members from free text, and misclassification weakens the targeting field. |
| AI as the decision-maker | **M5-R1/R4**: the automated campaign engine proposes lists and its own cut-off; the CFO's freeze rule is the check. **M7**: the engine's live rule is now the confounder, and its send probabilities are the propensity score. |
| AI as a tool / intervention | Not in this case. See Lab 1 and Case C. |

Say the M5 → M7 link out loud: *the system that made the decisions in Q3 is exactly what we must adjust for in the Q3 logs.*

## 3. Release schedule

Minutes are elapsed minutes in the meeting and approximate. **Retime when each deck is rebuilt.** The times below come from the v2 calendar:
- they leave minutes 0–15 of block A in M2, M3, M5 and M7 for a critique case, and reading-and-critique exercises are now dropped, so those meetings gain about 15 minutes;
- they put Exam I in M6 block A, but it is now in M5 block A, so the M5 releases move to block B and M6 regains block A;
- M1 and M2 are already retimed to the current schedule.

| Part | Meeting, block | About | Hand out at the deck marker | Hold back until the attempt is written |
|---|---|---|---|---|
| M1-R1 | M1 A | 0–10 | `[RELEASE R1]` "The Coffee Chain, Before the Experiment" | "The Number That Decides It" |
| M1-R2 | M1 A | 25–35 | `[RELEASE R2]` type counts | the `\pause` on "Confounded Assignment"; "The Pilot, Decomposed" |
| M1-R3 | M1 A | 40–50 | `[RELEASE R3]` | "Who Got the Coupon Decides the Sign" |
| M1-R4 | M1 B | 60–75 | `[RELEASE R4]` | "The Test Against the Break-Even" |
| M1-R5 | M1 B | 95–110 | `[RELEASE R5]` | "The Average Coupon Loses Money…"; "Data Roles" |
| M2-R1 | M2 A | 0–10 | `[RELEASE R1]` | SE and interval frames |
| M2-R2 | M2 A | 40–50 | `[RELEASE R2]` | "Transport the Decision, Not Just the Effect" |
| M2-R3 | M2 B | 60–80 | `[RELEASE R3]` | "The Lapsed Test Is Too Small"; CUPED frames |
| M2-R4 | M2 B | 80–90 | `[RELEASE R4]` | "The Design Effect" |
| M2-R6 | M2 B | 92–110 | `[RELEASE R6]` | "Assignment and Receipt" to "Which Number for Which Decision" |
| M2-R5 | take-home | | with "Lin's Test Plan" | (the memo is finished at home) |
| M3-R1 | M3 A | 15–25 | `[RELEASE R1]` | the table on "The Number That Decides It" |
| M3-R2 | M3 A | 40–50 | `[RELEASE R2]` | the `\pause` on the interaction frame |
| M3-R2b | M3 B | 60–65 | after "From Two Segments to Fourteen Fields" | the new SE-of-the-gap frame |
| M3-R3 | M3 B | 85–95 | `[RELEASE R3]` | the table on "Same RMSE, Opposite Decisions" |
| M3-R4 | M3 B | 95–100 | `[RELEASE R4]` | "The Ladder" (`[RELEASE R5]` is a reveal, not a handout) |
| M3-R6 | M3 C | 120–125 | Lab 2 opener | answers come out of the lab |
| M4-R1 | M4 A | 0–5 | `[RELEASE R1]` | |
| M4-R2 | M4 A | 5–15 | `[RELEASE R2]` | "The Number That Decides It" |
| M4-R3 | M4 A | ~45–50 | `[RELEASE R3]` | **half-B outcomes: nothing until every pair has submitted** |
| M4-R4 | M4 B | 60–75 | `[RELEASE R4]` | winner's-curse frame |
| M4-R5 | M4 B | 100–110 | `[RELEASE R5]` | |
| M5-R1 | M5 A | 15–25 | `[RELEASE R1]` | "The Number That Decides It" |
| M5-R2 | M5 A | 40–50 | `[RELEASE R2]` | the count/rate split on "Denominators" |
| M5-R3 | M5 B | 60–80 | `[RELEASE R3]` and the row-contribution worksheet | "The Contributions, Added Up" |
| M5-R4 | M5 B | 90–105 | `[RELEASE R4]` | |
| M6-R1 | M6 B | 70–85 | `[RELEASE R1]`, after Exam I | Step 2 and cap frames |
| M6-R2 | M6 B | 85–100 | `[RELEASE R2]` | "Why Costs Are Not Uniform" table |
| M6-R3 | M6 B | 100–120 | `[RELEASE R3]` | "Knapsack", "Shadow Price", "The Q4 List" |
| M7-R1 | M7 A | 15–25 | `[RELEASE R1]` | "The Number That Decides It" |
| M7-R2 | M7 A | 25–40 | `[RELEASE R2]` | "Pooled, Then Within Segment" |
| M7-R3 | M7 B | ~75–82 | `[RELEASE R3]` | "The App-Open Answer" |
| M7-R4 | M7 B | 90–97 | `[RELEASE R4]` | "The Ladder" (`[RELEASE R5]` is a reveal) |
| Rivergate | take-home | | with the adjustment core | the key below; release it after Notebook 7 is due |

M7 must end by minute 110 because of the proposal presentations. M6-R1 to R3 fit block B only because the targeting core is done at home.

## 4. Key, part by part

### M1-R1
- Net per coupon $= 30\tau - 10p_1$, so $\tau^* = p_1/3$. At $p_1 = 0.68$, $\tau^* = 0.227$.
- At face value: $0.44 \times 30 - 6.8 = +¥6.40$ per coupon, **+¥64,000** across 10,000.
- Doubt: the coupon went to "the ones marketing judged most loyal". The comparison is loyal against not loyal.
- Board: put $p_1/3$ in a corner and leave it there for the whole meeting.

### M1-R2
- Warm-up:
  - A knows $Y(1) = 1$ → Sure Thing or Persuadable.
  - B knows $Y(0) = 1$ → Sure Thing or Do-Not-Disturb.
  - C knows $Y(1) = 0$ → Lost Cause or Do-Not-Disturb.
  - D knows $Y(0) = 0$ → Lost Cause or Persuadable.
  - More customers help estimate *averages*; they never reveal A's missing outcome.
- Rates: $(220+120)/500 = 0.68$; $(80+40)/500 = 0.24$; naive 0.44.
- True ATE $= (200-100)/1000 = 0.10$.
- ATT $= (120-60)/500 = 0.12$. $E[Y(0)\mid D=1] = (220+60)/500 = 0.56$ and $E[Y(0)\mid D=0] = 0.24$, so selection bias $= 0.32$ and $0.12 + 0.32 = 0.44$.
- ATU $= (80-40)/500 = 0.08$. $0.5(0.12) + 0.5(0.08) = 0.10$.
  - Relative to the ATE, the raw gap is off by $0.34 = 0.32$ (baseline selection) $+ 0.02$ (selection on gains: marketing also picked slightly better responders).
- Recipients: $0.12 \times 30 - 6.8 = -¥3.20$. **Three quarters of the lift is who was picked.**
- Per-type margins: Persuadable +¥20; **Sure Thing −¥10**; Lost Cause **¥0** (the coupon is paid only on purchase); Do-Not-Disturb −¥30. Averaging gives net $= 20p_1 - 30p_0 = 30\tau - 10p_1$: M2's "test the profit directly" formula, one meeting early. (The deck's "Lost Cause → coupon is wasted" bullet is wrong for this coupon; see `course-spine.md` §4.)

### M1-R3
- (a) $0.80 - 0.10 = +0.70 = 0.05$ (ATT) $+ 0.65$ (bias).
- (b) $0.30 - 0.75 = -0.45 = 0.20 - 0.65$.
- Manager (b) concludes the coupon hurts. Same coupon, opposite sign. **Keep (b) on the board: it returns in M7.**

### M1-R4
- $\hat\tau = 0.10$. A random half-split of the types gives 200/150/100/50 per arm, so rates $(150+100)/500 = 0.50$ and $(150+50)/500 = 0.40$.
- Sentences: RNG + seed → independence, since nobody chose. No opt-in or removal → the arms are still the draw. One design, single-use, tied to the account → consistency, one version, codes can't be passed on. Staff blind → no second treatment travels with the coupon.
- $\tau^* = 0.50/3 = 0.167$. Net $= 0.10 \times 30 - 5 = -¥2.00$ per coupon, **−¥20,000** against marketing's +¥64,000.
- Line to leave them with: *it works; it does not pay.*
- Task 4: coupon-arm buyers $155 + 105 = 260$ (0.52); control buyers $145 + 55 = 200$ (0.40); $\hat\tau = 0.12$ against a true 0.10.
  - The draw is not broken. Randomisation is unbiased *over draws*, not exact in each one.
  - This is the workshop's 200-seed histogram, one draw at a time. M2 puts a number on the spread.

### M1-R5
- Active: $0.05 \times 30 - 0.80 \times 10 = 1.50 - 8.00 = -¥6.50$, break-even 0.267. Lapsed: $6.00 - 3.00 = +¥3.00$, break-even 0.100.
- Everyone: $5{,}000(-6.50) + 5{,}000(3.00) = -¥17{,}500$. Lapsed only: **+¥15,000**.
- Roles: `member_id` unit; `coupon` treatment; `purchase_7d` outcome; `tier`, `recency`, `spend_q1` pre-treatment; `redeemed`, `app_opens_q2` post-treatment (never a control); `seed`, `draw_time` audit.
- Exit ticket, expected answers:
  1. The same members with vs without the coupon.
  2. 0.44 = 0.12 effect + 0.32 who was picked.
  3. The Q2 effect is real but the coupon loses ¥2 each; other lists and populations differ; one draw is noisy.

### M2-R1
- $\widehat{SE} = \sqrt{0.25/500 + 0.24/500} = 0.0313$; CI $[0.039, 0.161]$.
- $z$ vs 0 $= 3.19$; $z$ vs 0.167 $= -2.13$. The interval excludes both 0 and the break-even: *works and does not pay.*
- Net $= 20p_1 - 30p_0 = -¥2.00$. $\mathrm{Var} = 400(0.0005) + 900(0.00048) = 0.632$, SE 0.795, CI **[−¥3.56, −¥0.44]**. Both marketing and the CFO are right; they asked different questions.
- Task 5: opening the app is post-treatment, partly caused by the coupon. Dropping non-openers compares selected groups; this previews M7's collider. The comparison of all members as drawn is the **ITT**: the effect of *sending* the coupon, which is the decision. The effect of *seeing* it is M2-R6.
- Task 6, **the design-based point**:
  - With the 1,000 members fixed, Neyman's variance is $S_1^2/n_1 + S_0^2/n_0 - S_\tau^2/n$.
  - The last term is unobservable, because it needs both potential outcomes of each member. The plug-in SE drops it, so **0.0313 is conservative**.
  - For the M1 type population: $S_1^2 = 250/999$, $S_0^2 = 240/999$, $S_\tau^2 = 290/999$. The variance is $0.000691$, giving SD **0.026**.
  - **Check before handing out:** 0.026 assumes the M1 workshop simulation uses the 400/300/200/100 region. If it does not, quote the simulation's own SD.

### M2-R2
- Both tests are internally valid, and each measures its own list's effect.
- A: $\tau = \tfrac23(0.05)+\tfrac13(0.20) = 0.10$; $p_1 = 0.633$; $\tau^* = 0.211$; net −¥3.33.
- Base: 0.125 / 0.55 / 0.183 / −¥1.75.
- B: $\tau = 0.15$; $p_1 = 0.467$; $\tau^* = 0.156$; net **−¥0.17**. B has a higher lift than the base and still loses, because the break-even moves with the mix.
- The licence is *"same coupon, same app, same quarter"*: segment effects carry over.

### M2-R3
- The MDE must be at most the gap to break-even: $0.20 - 0.10 = 0.10$.
- $\sigma_1^2 + \sigma_0^2 = 0.21 + 0.09 = 0.30$. $n = 7.84 \times 0.30 / 0.01 = 235.2$, so **236 per arm** are needed. At 175: MDE $= 2.80\sqrt{0.30/175} = 0.116$.
- CUPED with $\rho = 0.6$ multiplies variance by 0.64: $n = 151$ per arm; MDE at 175 $= 0.093$. **The test fits.**
- Q1 purchases are fixed before the draw. `app_opens_q2` is partly caused by the coupon, and adjusting for it biases the estimate.
- Task 5, fixed in writing before launch:
  1. unit of assignment and allocation;
  2. outcome and window;
  3. the decision threshold (test against 0.10, not 0);
  4. sample size and stopping rule (no peeking);
  5. exposure logging and guardrails.

  First-day check: **sample-ratio mismatch** (are the arms 175/175?) and whether exposure is being logged. These are P4's planted issues; cite the ExP pre-experiment patterns.
- Aside if asked: Q2's MDE was 0.088, but the CFO's gap was $0.167 - 0.10 = 0.067$. It was under-powered for the profit question and separated them anyway on this draw.

### M2-R4
- The unit is the **store**: everyone in a store sees the menu board.
- DEFF $= 1 + 399 \times 0.01 = 4.99$. 20,000 customers carry the information of about 4,000. The SE is $\sqrt{4.99} = 2.23$ times the customer-level SE.
- Marketing would report the customer-level SE. Compare store means, or cluster by store.
- Task 4:
  - **Till push** → staff behaviour is store-level, so the store is the unit (as planned). Keep till scripts identical across arms.
  - **Two-store customers** → spillover across stores. Randomise catchment clusters of nearby stores instead: fewer, larger units.
  - **Carry-over** → time-block designs need washout gaps. Each fix reduces the number of independent units and widens the SE.

### M2-R5
A model memo:
1. Randomised: a causal effect for the 1,000-member region.
2. 0.10, 95% CI [0.039, 0.161]; net −¥2.00 per coupon [−¥3.56, −¥0.44].
3. Coupon-everyone does not pay.
4. Next: a lapsed-only test with CUPED (175 per arm fits), and the BOGO randomised by store.

### M2-R6
This part closes M2 with noncompliance and the LATE, the experimental core of instrumental variables (Handout H1 goes further). The draw $Z$ is the instrument and seeing the coupon is $D$.
1. Three comparisons:
   - **as drawn (ITT):** $0.50 - 0.40 =$ **0.10**;
   - **openers only:** $230/400 - 180/360 = 0.575 - 0.500 =$ **0.075**;
   - **saw vs did not see (as treated):** $230/400 - (20 + 200)/600 = 0.575 - 0.367 =$ **0.208**.
2. First stage $= 400/500 = 0.80$; Wald ratio $= 0.10/0.80 =$ **0.125**. It is the effect of seeing the coupon on **compliers**: members who see it if they are sent it. Nobody in the control arm can see one, so there are no always-takers and no defiers (one-sided noncompliance). Compliers are then exactly the members who saw it, and the ratio is also the effect on those who saw it.
3. Coupon-arm non-openers are **never-takers**: $20/100 = 0.20$, an untreated rate, by exclusion. In the control arm $0.40 = 0.8\,\mu_{C0} + 0.2 \times 0.20$, so compliers' untreated rate $\mu_{C0} = 0.36/0.8 =$ **0.45**. Their treated rate is the coupon-arm openers' $0.575$, and $0.575 - 0.45 = 0.125$.
4. Opening is partly caused by the draw: the notification brings in openers. The 360 control openers are members who open the app anyway, while the 400 coupon-arm openers are all compliers. Members who open anyway buy more without a coupon ($0.50$) than compliers as a whole ($0.45$), so openers-only is **too low** ($0.075$). "As treated" is too high ($0.208$): it compares compliers with a mix that includes never-takers, who buy at $0.20$. This is M1's selection bias, created by conditioning on a post-treatment variable (the M7 collider, previewed).
5. Sentence 1: independence (the draw), plus no always-takers. Sentence 2: **exclusion**. The draw moves purchases only through seeing the coupon; a notification without the amount carries no offer. Sentence 3 is about cost, not identification. If the notification had shown "¥10 off", non-openers would be partly treated. The ITT would include that direct effect, and dividing by 0.80 inflates it: the ratio **moves up** (an upward bias of direct effect $\times\, 0.2/0.8$).
6. For compliers, $\tau^\ast = 10 \times 0.575/30 = 0.192 > 0.125$: **it does not pay**. Net per seen coupon $= 0.125 \times 30 - 5.75 =$ **−¥2.00**. Never-takers cost $10 \times 0.20 = $ ¥2.00 each through the automatic discount, with no effect. Overall, $0.8(-2.00) + 0.2(-2.00) = -$¥2.00, which is M1's number, as it must be.
   - **The text message:** the LATE describes compliers, not non-openers. Non-openers buy at 0.20 without a coupon, against 0.45 for compliers. Their effect is unknown, and they already cost ¥2 each through the automatic discount. Reaching them is a new treatment, so test it.
   - **For the deck:** the closing message is that the decision (send or not) needs the ITT; the LATE answers a narrower question, for a population the data choose.

### M3-R1
- Rule: coupon iff $\tau(x) > \mu_1(x)/3$.
- Marketing (active): $0.05 < 0.267$, −¥6.50 per coupon, **−¥32,500** for 5,000. Lin (lapsed): $0.20 > 0.100$, +¥3.00, **+¥15,000**.
- Sentences: 50/50 everywhere → independence within every $x$ and overlap by design. Frozen CRM → $X$ pre-treatment. **New joiners not in the draw → the Q3 list includes people outside the test's support.** That one is about the decision, not the estimate.

### M3-R2
| Customer | $\hat\mu_0$ | $\hat\mu_1$ | Decision |
|---|---|---|---|
| A, B (active) | 0.75 | 0.80 | $0.05 < 0.267$: no |
| C, D (lapsed) | 0.10 | 0.30 | $0.20 > 0.100$: yes |

- ATE $= 0.20 - 0.15 \times 0.5 = 0.125$.
- Stress *aligned predictions*: both columns come from the same row's $x$, whatever arm the row was in.
- A lapsed customer's $\hat\tau = 0.20$ means about 200 extra purchases per 1,000 similar members, not knowledge of *which* 200.
- Task 3: $\tau = 0.05 + 0.15L$, the same two effects. The sign of the interaction depends only on which group is coded 1.
- Task 4: $0.8(0.05) + 0.2(0.20) = $ **0.08**. The coefficient on $D$ is the effect at the reference group, $X = 0$ (lapsed), so it is not an average. **Standardise with the target's weights**: M2's transport again, and M7's standardisation ahead.

### M3-R2b
- Active: $0.80 - 0.75 = 0.05$, $SE = \sqrt{0.16/200 + 0.1875/200} = 0.0417$. Lapsed: $0.30 - 0.10 = 0.20$, $SE = 0.0387$.
- Gap 0.15, $SE = \sqrt{0.0417^2 + 0.0387^2} = 0.0569$, **2.64 SEs**: distinguishable from noise at 5%.
- Task 3: "significant here, not there" is not a test of a difference. Active's 0.05 is 1.2 SEs, "not significant", but its interval [−0.03, 0.13] does not rule out a sizeable effect. The two labels say nothing about the difference; test the gap itself.

### M3-R3
- Model I: 0.05 / 0.20. Model A: 0.125 for everyone. Model A is off by ±0.0375 in every cell; check it at one cell, e.g. active–coupon $0.1375 + 0.575 + 0.125 = 0.8375$ vs 0.80.
- Irreducible part: $(0.16 + 0.1875 + 0.21 + 0.09)/4 = 0.16188$. RMSE: I $= 0.4023$; A $= \sqrt{0.16188 + 0.0375^2} = 0.4041$.
- Lists: I = lapsed first, **+¥15,000**. A = random, $5{,}000 \times \tfrac12(-6.50 + 3.00) = $ **−¥8,750**.
- **0.4% of RMSE, ¥23,750 of decision.**
- Task 5: A misses each outcome by 0.04 but gets the effect exactly (0.20). B misses by only 0.02 but gets **0.24**. The effect's error is the *difference* of the two outcome errors. Their variances add; their biases can cancel (A) or compound (B).

### M3-R4 (sim)
Ladder: interaction OLS RMSE 0.412, +¥4,100; S-lasso 0.409, −¥6,800; **S-boosted best RMSE 0.401**, +¥1,900; **T-boosted best list +¥9,300** (RMSE 0.406); oracle +¥16,200; marketing's purchase model −¥29,400. The best RMSE and the best list come from different learners.

### M3-R6 (Lab 2 opener; new to this case)
1. **Only comments written before the freeze date (the day before the draw).** A comment written after a coupon arrived can be caused by the coupon. A label built from it is post-treatment, M1's data-roles rule applied to text.
2. With 80% accuracy both ways on a 50/50 base, the 5,000 labelled "drifting" are 4,000 lapsed + 1,000 active.
   - Lift $= 0.8(0.20) + 0.2(0.05) = 0.17$.
   - $\mu_1 = 0.8(0.30) + 0.2(0.80) = 0.40$, so break-even 0.133.
   - Net $= 0.17 \times 30 - 4.00 = +¥1.10$ per coupon.
   - The "not drifting" group: lift 0.08, $\mu_1 = 0.70$, net −¥4.60.
3. List value $= 5{,}000 \times 1.10 = $ **+¥5,500**, against +¥15,000 on the true flag. Check: $4{,}000(3.00) - 1{,}000(6.50) = 5{,}500$.
4. The gap between groups shrinks from 0.15 to 0.09, a factor $1 - 2(0.2) = 0.6$. **Misclassification attenuates heterogeneity toward the average.** Here the decision survives but two-thirds of the value is gone.
5. With accuracy $a$ in both directions: net per coupon $= 30(0.05 + 0.15a) - 10(0.80 - 0.50a) = 9.5a - 6.5$. It is zero at **$a = 0.684$**. At 70% the list earns about ¥0.15 a coupon; at 65% it loses ¥0.33.

   Lab 2 then measures accuracy against gold labels and redoes this with estimated, not stipulated, segment effects.

### M4-R1
The middle sentence (half B held until every partition is in) is the one broken most often, by an analyst who "just checks" B while tuning the tree. After one look, B is discovery data too.

### M4-R2
- Type modifies the effect; spending shifts the purchase level by ±0.15 only.
- Lines: E–High 0.217, −¥5.00; E–Low 0.117, −¥2.00; A–High 0.167, **+¥1.00**; A–Low 0.067, +¥4.00.
- A–High clears its break-even by only 0.033. An error of that size flips the card.

### M4-R3 (sim)
If believed, half A says coupon for the first three leaves. **"App user" is a noise split**: nothing in M1–M3 said app use modifies the effect. Collect every partition before releasing R4, with no exceptions.

### M4-R4 (sim)
- Every leaf the search liked came back lower. Exec–app collapsed from 0.19 to 0.04 and leaves the card. A–High (0.18, SE 0.04) now straddles 0.167. A–Low stays on.
- Task 2: $\Delta_A = 0.5(0.08^2) + 0.5(0.08^2) = 0.0064$ and $\Delta_B = 0.0001$, so A wins. Fresh data shrink its gap from 0.16 to **0.04**: it was chosen *for* being large.
- Task 3: $SE = \sqrt{0.21/100 + 0.09/100} = 0.055$. Two halves of 50 per arm give 0.077 each. Same effects, more noise: a split must earn its cost.
- Winner's curse by hand: $0.125 + 1.87 \times 0.04 = 0.20$. That is a segment that "beats" the A–High break-even in data where nothing differs.

### M4-R5 (sim)
- Card: A–Low **coupon**; A–High **test, then decide**; executives **no coupon**.
- A–High: real (interval excludes 0); does not yet pay (straddles 0.167); the 38% sub-segment is a candidate for M5, not for this card.

### M5-R1
- Gain $G(\pi) = E[\pi(X)\,\mathrm{net}(X)]$ per member.
- Nobody 0; everyone −¥1.75 (−¥17,500); segment rule **+¥1.50** (+¥15,000). **A model's list must beat ¥1.50**, the list that needed no model.

### M5-R2
- 78 mixes arm sizes: $540(0.40) - 460(0.30) = 78 = 50 + 28$.
- Right count: $(0.40 - 0.30) \times 1{,}000 = 100$.
- Lift per member targeted 0.10; per member of the fold, $Q(0.2) = 0.02$.

### M5-R3
1. With $e = 0.5$, a treated buyer contributes $20/0.5 = 40$ (¥30 margin less the ¥10 coupon). A control buyer contributes $-30/0.5 = -60$.
2. Segment rule $120/80 = $ **1.50**; everyone $-140/80 = -1.75$; active only $-260/80 = -3.25$. The fold's rates equal the M1 segment rates, so these equal the hand values.
3. Contributions: six 40s, two −60s, 72 zeros. sd ≈ 14.5, SE $= 14.5/\sqrt{80} = 1.62$. Two lists ¥1 apart cannot be told apart on 80 rows.
4. M4's honesty rule, applied to a policy instead of a partition.
5. With $e = 0.25$: a coupon-arm buyer contributes $20/0.25 = +80$; a control buyer $-30/0.75 = -40$. **Use the design's $e$**, not a universal factor of 2. Rare arms carry big weights and make evaluation noisy. In M7, $e$ becomes the engine's rule.

### M5-R4 (sim)
- Forecast with the **evaluation-fold** numbers. Selection-fold values are inflated by selection.
- The engine's tuned cut-off fell furthest (2.31 → 1.82): it was tuned on that fold's noise.
- Task 3: the two estimates share members and outcomes, so they are positively correlated. The SE of the difference is **paired**: compute $d_i = g_{\text{forest},i} - g_{\text{segment},i}$ for every fold member, then $SD(d)/\sqrt n$. Combining 0.21 and 0.21 as if independent (0.30) overstates the uncertainty. **The deck needs the paired SE from the simulation**; until then, say "the paired SE decides whether the 0.26 edge is real".
- To the CFO: send the forest list. Its edge over the segment rule (1.79 vs 1.53) is about one SE of the difference, which is modest. The segment rule is the fallback if the engine cannot be maintained. The ranking is good; the magnitudes of the top bin are optimistic.

### M6-R1
1. Free push: $\hat\tau > 0$, so all 10,000. A push *without* the coupon is a different treatment, whose effects were never measured (M1: a well-defined intervention). The deck's Step 1 wording must change accordingly.
2. Opt-out: $c = 150 \times 0.01 = ¥1.50$; threshold $c/m = 5\%$. Analysts only; executives sit exactly at the threshold, so no.
3. Cap: every analyst has $v = 0.20 \times 30 - 1.50 = ¥4.50$, and any 1,000 earn ¥4,500. The forest's top 1,000 (lift 0.30) have $v = ¥7.50$ and earn **¥7,500**. The cap, not the threshold, binds, and it makes within-segment ranking worth money.

### M6-R2
| Cell | $\hat c(x) = 1.50 + 5P(Y_1)$ | $v = 30\hat\tau - \hat c$ | Split: $25\hat\tau$ − $5P(Y_0)$ − 1.50 |
|---|---:|---:|---|
| Analyst–Low | 2.50 | **3.50** | 5.00 − 0 − 1.50 |
| Analyst–High | 4.00 | 2.00 | 5.00 − 1.50 − 1.50 |
| Exec–Low | 3.25 | −1.75 | 1.25 − 1.50 − 1.50 |
| Exec–High | 4.75 | −3.25 | 1.25 − 3.00 − 1.50 |

- Same lift, different sure-thing cost. **The prognostic field that was irrelevant for estimation returns on the cost side.**
- All analysts: $2{,}500(4.00) + 2{,}500(2.50) = ¥16{,}250$ expected. To answer finance you need the variance of realised cost: each member costs 6.50 or 1.50.
  - With independent redemptions, $SD = \sqrt{25[2{,}500(0.16) + 2{,}500(0.25)]} = ¥160$. Then $z = (18{,}000 - 16{,}250)/160 = 10.9$: **the chance is essentially zero**.
  - The 95th percentile is $16{,}250 + 1.645(160) = ¥16{,}513$.
  - Common demand shocks and estimated probabilities make real risk larger than this.

### M6-R3
1. Ratios: 2.40, 1.50, 0.46, 0.32. Fill: all 2,500 A–Low (¥6,250), then $1{,}750/4.00 = 437$ A–High. Marginal cell A–High, $\lambda^* = 0.50$: the next ¥1 returns ¥1.50.
2. With 391 A–High: $\hat\sigma_C = \sqrt{2{,}500(25)(0.16) + 391(25)(0.25)} = 111.6$; reserve $1.645 \times 111.6 = ¥184$; $(8{,}000 - 184 - 6{,}250)/4.00 = 391$. The guarantee costs 46 pushes, **¥92** of expected net.
3. The cap does not bind: the send is spread over three days.
4. Final list: 2,500 + 391 = **2,891** pushes; cost ¥7,814; net **¥9,532**.

5. (Optional) Each arm's SE is $0.03/\sqrt2 = 0.021$. $SE(\hat v) = \sqrt{25^2 + 30^2} \times 0.021 = 0.83$, and the lower bound is $2.00 - 1.645(0.83) = $ **¥0.64 > 0**, so it stays. (Analyst–low: $v = 3.50$, SE 1.38, bound ¥1.23.) The bound sits on money, not on the lift, because the cost threshold itself depends on an estimated $\mu_1$.

Take-home check (conservative rule, SE 6%): the A–High lower bound is $0.20 - 1.645(0.06) = 0.101 < 4.00/30 = 0.133$, so it **drops off**.

### M7-R1
- $\tau^* = 10 \times 0.40 / 30 = 0.133$.
- The rule targeted members *unlikely to buy* (lapsed), so recipients' $Y(0)$ is low and the bias is **negative**, possibly enough to flip the sign.
- Sentences: rule and nothing else → exchangeability, nobody hand-picked. Every field in the export → exchangeability, $X$ holds the rule's inputs. Cap → overlap within bands. One design → consistency. *Hold onto the first sentence*; M8 and M9 show how such a sentence fails.

### M7-R2
- Pooled: $0.40$ vs $0.62$, −0.22. Within: +0.05 and +0.20.
- ATT $= 0.2(0.05) + 0.8(0.20) = 0.17$; bias $= 0.23 - 0.62 = -0.39$.
- ATE 0.125; ATT **0.17**; ATU 0.08. The CFO needs the ATT: $0.17 \times 30 - 4 = +¥1.10$ per coupon, so **keep**.
- Extending to everyone uses the ATE against a break-even of $0.55/3 = 0.183$: loses.
- This is M1-R3(b) with the rule as the manager.
- Task 5: $\sum w = 400(0.25) + 100(4) = 500$ and $\sum w^2 = 25 + 1{,}600 = 1{,}625$, so ESS $= 500^2/1{,}625 = $ **154 of 500 controls**. The ATT leans on the 100 lapsed controls. (With ATE weights 5/1.25, each arm's ESS is 320 of 500.)

### M7-R3
Among openers: $250/500 = 0.50$ vs $250/250 = 1.00$, an "effect" of **−0.50** for a true 0. Restricting to openers kept every treated customer but only the high-intent untreated. The app-open column is a collider. "Fairer comparison" arguments usually propose one.

### M7-R4 (sim)
- Task 1, **the outcome-free design stage** (Rubin's design before analysis), written down before purchases open:
  - Reconstruct the assignment mechanism: $\hat e(x)$ = band × daily send probability, from the 14 fields and the coupon column.
  - Check overlap by band: the top band has 31 controls among 4,900 rows.
  - Fix the trimming rule ([0.05, 0.95]) and therefore the estimand: the ATT on the overlap region, 91% of recipients.
  - Check covariate balance after weighting; choose the estimator.

  Same logic as M4's partition and M5's frozen list: decisions made before outcomes cannot be tuned to them.
- Ladder: no controls −0.19; linear 14 fields +0.06; flexible standardisation +0.14 (top band has only 31 controls among 4,900 rows); IPW untrimmed +0.10 (SE 0.06, max weight 58); **IPW trimmed to [0.05, 0.95] +0.16 (SE 0.02)**; truth +0.17.
- The engine's rule, times the cap, *is* the propensity score. Report that the trimmed ATT describes the 91% of recipients in bands where the rule left something to chance. **For the top band the effect is not identified from Q3 data.**

## 5. Rivergate take-home key

1. Trained $(20 \cdot 90 + 80 \cdot 60)/100 = 66$; untrained $(80 \cdot 80 + 20 \cdot 54)/100 = 74.8$; pooled **−8.8**. Within skill: high +10, low +6. Eighty percent of trainees were low-skill; composition drives the pooled gap.
2. Controls:

| Column | Include? | Why |
|---|---|---|
| Skill grade | **yes** | measured before sign-up; drives both sign-up and output |
| Tenure at sign-up | optional | pre-treatment; include if it may drive sign-up; harmless otherwise |
| Follow-up shift | **no** | changed *by* training (mediator) |
| Supervisor rating | **no** | measured after, partly caused by output: a version of the outcome |
| Completed course | **no** | post-treatment; conditioning compares finishers with everyone. Keep $D$ = signed up |

3. Unrecorded **motivation** (or recent performance trend) plausibly raised both sign-up and output. Within skill that biases the +10 and +6 **upward**. Exchangeability is a claim, not a fact, for a voluntary pilot.
4. The 200 are 50/50, so the effect is $0.5(10) + 0.5(6) = $ **8** orders a week, an ATE on the rollout mix. The volunteers' ATT is $0.2(10) + 0.8(6) = 6.8$. Her decision needs the 8.
5. Value per trainee over four weeks $= 8 \times 4 \times 80 = ¥2{,}560 > ¥1{,}800$: pays. High: ¥3,200. Low: $6 \times 320 = ¥1{,}920$, which clears ¥1,800 by only ¥120, so a modest upward bias in the +6 would erase it. A good memo trains the high-skill group and runs a randomised pilot for the low-skill group.

AIPW and double robustness use this same table as the worked example in the M7 notes (Section 2); they are not part of the take-home.

## 6. Grading a recommendation (any part)

Score 0–2 on each of five dimensions:
1. action, population and horizon stated;
2. arithmetic and units;
3. the comparison named;
4. the assumption that matters named;
5. a proportionate next step.

A justified "test first" earns full marks.

## 7. Deck issues found while aligning the case

The case follows the decks as they are. Fix these when the slides are revised. The complete accepted change list, including the Codex-review corrections, is in `course-spine.md` §4.

1. **Population sizes conflict.**
   - M1–M2: the base is 10,000 members and the Q2 test ran in one 1,000-member region.
   - M3 R4 ("The Q2 Export") says 10,000 members were in the Q2 draw "all three test regions".
   - M5 uses an evaluation fold of 5,000 from that export.
   - M7 says the Q3 export has 40,000 customers and the rule sent coupons to 40% of the base, while M3/M5 planned 5,000 coupons (half the base).

   Suggested fix: keep the base at 10,000 throughout. State in M3 that the full Q2 draw covered all three test regions, with the pilot region as the one analysed by hand in M1–M2, and drop the "different populations" sentence in M1's data-roles frame. Resize M7's export to the base, or say the Q3 programme ran chain-wide on a larger base.

   The student case avoids stating the size of the M3 export for this reason.
2. **Retired assessments still named.** M2 ("A1 released tonight"), M4 ("Due before today: A1"), M5 ("A2", "commitment due 96 hours before L8") and M6 ("proposal due 48 hours before L7"; v2 says 72 hours).
3. **Simulation numbers** in M3 R5, M4 R3–R5, M5 R4 and M7 R4–R5 are still `\NUM`-flagged.
4. **M7 schematic.** The overlap figure is a placeholder ("replace with the sim's overlap figure").
5. **Case framing to add to the slides.** M5 R1: the automated campaign engine and the CFO's freeze rule. M7 R1: "the engine's rule". M3: a pointer to the Lab 2 opener.
