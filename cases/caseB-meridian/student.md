# Case B: Wen's Rate Decisions

**Meridian Hotels, Meetings 8–9.** Fictional teaching case: the company, the people and all data are invented.

This case is handed out one part at a time. When a task says *commit*, write your answer down before the class discusses it.

Throughout: the current midweek premium rate is **¥800** a night, and the variable cost of an occupied room is **¥200**.

---

## Meeting 8: Flexible Controls and Double Machine Learning

### Part M8-R1. The proposal

**Wen** is commercial director of Meridian Hotels, a group of 80 properties.

A revenue management (RM) system sets the rate for every hotel-night. It uses forecast demand, competitor rates, booking pace and the event calendar. **No human sets these rates night by night**: the system is an automated decision-maker, and it has been for three years.

On Wen's desk: sales proposes raising midweek premium rates by **8%** across the portfolio. Their evidence is the RM system's own reporting: nights with higher rates sell more rooms. (The exhibit is projected in class.) Sales' reading: *demand is strong; the system is under-pricing.*

Wen has three years of logs: 80 hotels × 1,095 nights, with 47 recorded signals per night.

Six comparable nights from one hotel:

| Night | Category | Price $P$ | Demand $Q$ |
|---|---|---:|---:|
| 1 | Standard | 30 | 110 |
| 2 | Standard | 40 | 100 |
| 3 | Standard | 50 | 90 |
| 4 | Premium | 70 | 210 |
| 5 | Premium | 80 | 200 |
| 6 | Premium | 90 | 190 |

**Tasks**
1. An 8% rise changes contribution per occupied room from ¥600 to what? For the rise to pay, bookings must fall by less than what percentage? Express the break-even as an elasticity.
2. In pairs: compute the pooled slope of $Q$ on $P$ across the six nights.
3. Commit: does Wen raise rates?

### Part M8-R2. Subtract what the system already knew

Within each category the mean price and mean demand are:

| Category | Mean price | Mean demand |
|---|---:|---:|
| Standard | 40 | 100 |
| Premium | 80 | 200 |

What Wen's team says about the RM system:
- "The RM system is the only thing setting rates."
- "Every input it used is in the feed."
- "Rates still move for reasons unrelated to demand."

**Tasks**
1. For each night, subtract its category's means from its price and its demand. Regress one residual on the other.
2. Why did the pooled slope and the within-category slope differ in sign? Draw the arrows.
3. For each of the team's three sentences, say what it guarantees. What does a night priced exactly by the rule contribute to the estimate?

### Part M8-R3. The real logs

| | |
|---|---:|
| Hotel-nights | 87,600 |
| Recorded signals | 47 |
| Median rate | ¥803 (5th–95th percentile: ¥439–¥1,920) |
| Median premium rooms booked | 61 |

The RM system is **rule-based**. Log rate is a step function of bucketed signals:
- six forecast-occupancy bands, plus competitor-index bands and booking-pace bands;
- an event flag interacted with a lead-time tercile;
- day-of-week and month adjustments, plus a weekend rule that differs by occupancy band.

Around that rule, rates still move for reasons tied to no recorded signal.

**Tasks. In pairs**
1. Predict three log–log slopes of bookings on rate: with no controls; controlling for the hotel; controlling for the hotel and six forecast-occupancy bands.
2. Write down the model you would fit to get the elasticity. Three proposals go on the board.
3. For each proposal, say what could go wrong with it.
4. Signals are recorded throughout the day. Name two of the 47 that would be *post-treatment* if recorded after the rate was posted. When must every control be measured?

### Part M8-R5. One more thing, says Wen

> Property revenue managers **override** the system on about **8% of nights**. They override on local knowledge: a wedding block, a competitor closing a wing, a conference that never reached the event calendar. The override is logged. **The reason is not.**

**Tasks**
1. Which of the team's three sentences in Part R2 is now false? What does that do to the estimate?
2. Can a more flexible model of the signals repair it? Why or why not?
3. The estimate sits 0.24 from the break-even. What would you need to know about the overrides to decide whether they could close that gap?

---

## Meeting 9: Rates the Hotel Did Not Choose

### Part M9-R1. The member-rate test

Meeting 8's estimate rests on an assumption the logs cannot check: nothing unrecorded moved both rates and bookings. The overrides break it.

**What Wen did next.** For six months the booking engine flipped a coin for every premium hotel-night:
- **heads:** loyalty members see a **member rate 8% below** the system's rate;
- **tails:** they see the system's rate.

Managers kept their override. On a heads night they could block the member rate; on a tails night they could apply it by hand.

On Wen's desk: make the member rate permanent, portfolio-wide.

**Tasks**
1. An 8% member rate changes contribution per occupied room from ¥600 to what? By what percentage must bookings rise for the cut to pay? Express the break-even as an elasticity.
2. What did the coin make random, and what did it not?

### Part M9-R2. The test log

One thousand premium hotel-nights from hotels where the coin was 50/50. Member bookings per night:

| Coin | Member rate shown? | Nights | Mean bookings |
|---|---|---:|---:|
| Heads | yes | 350 | 64.0 |
| Heads | no | 150 | 90.0 |
| Tails | yes | 50 | 40.0 |
| Tails | no | 450 | 70.0 |

Nightly bookings have a standard deviation of about 20.

From Wen's description of the test:
- "The engine drew the coin within each hotel and month; resorts drew heads more often than airport hotels."
- "Heads changed one thing: the rate members were shown."
- "Managers honoured most heads and added the member rate on few tails."
- "A manager could block the member rate or add it by hand; none reversed the coin."

**Tasks. In pairs, commit first**
1. Compare bookings on nights the member rate was **shown** with nights it was not.
2. Compare bookings on **heads** nights with tails nights.
3. Compare the share of nights the rate was shown on heads nights with the share on tails nights.
4. Commit: does Wen roll it out?

Then:

5. Combine 2 and 3 into one number. What does it measure, and for which nights? Give its standard error (treat the share of nights the rate was shown as known) and a 95% interval.
6. Classify nights by what would have been shown under each coin. What share of nights is of each kind?
7. Complier nights book 60 without the member rate. Convert your number into an elasticity. Does it clear the break-even?
8. Match each of the four description sentences to the assumption it supports.

### Part M9-R3. Two things nobody mentioned

**Marketing's email.** Marketing confirms that on every heads night the engine also emailed *"Members' Week at Meridian"* to members who had searched that hotel, **whether or not the manager blocked the rate**.

**Two old-engine hotels.** Two hotels ran an old booking engine that **could not display** member rates. Their coin still flipped and the email still went out.

| Old-engine hotels, 200 nights | Heads | Tails |
|---|---:|---:|
| Mean member bookings | 51.2 | 50.0 |

**Two kinds of hotel.** The coin was 70/30 at resorts and 30/70 at airport hotels, and resorts book more:

| Hotel | Nights | Heads nights | Tails mean | Heads mean |
|---|---:|---:|---:|---:|
| Resort | 500 | 350 | 80.0 | 84.8 |
| Airport | 500 | 150 | 50.0 | 54.8 |

The share of nights the member rate was shown is 0.70 on heads and 0.10 on tails in both kinds of hotel.

**Tasks**
1. Suppose the email alone adds 1.2 bookings on every heads night. Recompute the ratio and the elasticity. How large is the bias, and why is it larger than 1.2?
2. What do the old-engine hotels measure? Correct the ratio.
3. Compute the ratio within each kind of hotel, then pooled across both, ignoring hotel type. Why do they differ?
4. Which controls must the analysis include, which may it include, and which must it never include?
5. Let $a$ be the email's direct effect on bookings per heads night, whatever its size. Write the complier elasticity as a function of $a$, using the hand log with the email (ITT 6.0). How large would $a$ have to be for the member rate to stop paying? Compare it with what the old-engine hotels measured.
6. The permanent programme would keep sending the "Members' Week" email. Is the email's effect still a bias? Which number does Wen's decision need?

### Part M9-R4. The full test

The full test covers 80 hotels, 182 nights, **14,560 premium hotel-nights**. The coin probability was set by hotel × month.

**Task 1. In pairs, predict three elasticities:**
- the ratio pooled over all hotels, with no controls;
- two-stage least squares (2SLS) with hotel × month strata;
- 2SLS with strata and the 47 signals, corrected for the email using the old-engine hotels.

Against the break-even, which ones roll out the member rate? Commit.

**The city hotels.** In the 12 city-centre hotels, managers overrode the coin almost always. The member rate was shown on 15% of heads nights and 10% of tails nights, with 200 nights per arm. The standard error of the heads-minus-tails booking difference is about 2.0.

**Task 2**
1. Compute the city hotels' first stage, its standard error and $F = (\text{first stage}/\text{SE})^2$. Do the same for the hand log of Part R2.
2. Approximate the SE of the city hotels' ratio. How large would the email's bias be there?
3. Write the rule you would commit to *before* seeing any ratio.

### Part M9-R5. Candidate-instrument audit

Analysts across the group propose other instruments for the rate. **In pairs:** mark each assumption ✓, ✗ or ?, with one reason.

| Candidate | Relevance | Independence | Exclusion | Monotonicity |
|---|---|---|---|---|
| A competitor's rate the same night | | | | |
| Rainfall in the city | | | | |
| Nights the RM system was down and rates froze at yesterday's level | | | | |
| Which revenue manager was on shift | | | | |
| The member-rate coin | | | | |

Then answer: which assumption do most candidates fail, and why can the data not settle it?

### Part M9-R6. The memo

Write the memo to Wen, in five sentences or fewer:
1. what to do, and on which nights;
2. the number and its interval;
3. whose elasticity it is;
4. the assumption that could overturn it;
5. what the next test should change.
