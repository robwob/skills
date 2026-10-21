# How to analyse card sort results yourself

The `card-sort-analysis` skill does this work for you. This guide is for understanding what it
is doing, so you can check it, explain it to a colleague, or do a small study by hand.

Each section covers one view of a card sort. The views have different names in different tools, so
the sections use Playbook UX's names (Participants, Cards, Categories, Merged Matrix, Similarity
Matrix, Dendrogram) and the [tool map](#tool-names-compared) at the end lists the nearest
equivalents elsewhere.

Every section has the same six parts:

1. What the view shows
2. How it is calculated, by hand
3. How to read it
4. Common misreadings
5. Try it
6. What the skill does at this step

Claims carry their status: unmarked means a source was read directly, `(unverified)` means the
claim rests on a secondary description of a source, `(convention)` means common practice with no
evidence behind its threshold, and `(derived)` means this guide's own reasoning.

---

## The worked example

Five participants sorted six cards from an invented library website, naming their own groups
(an open sort). **It is far too small for a real study. It is small enough to calculate on paper.**

| Card | P1 | P2 | P3 | P4 | P5 |
|---|---|---|---|---|---|
| Renew a book | Borrowing | Loans | Books | Borrowing | Library services |
| Reserve a book | Borrowing | Loans | Books | Borrowing | Library services |
| Borrow an e-book | Borrowing | Digital | Books | Borrowing | Library services |
| Computer skills class | Events | Digital | What's on | Learning | Events and classes |
| Author talk | Events | Events | What's on | What's on | Events and classes |
| Opening hours | Info | Info | What's on | What's on | Library services |

The data is in `examples/guide-example.csv`, one row per card placement, and every figure below
is what `scripts/analyse.py` gives on it. The tests in `tests/` check the matrix, the join
heights, the groups at each cut, the cards and categories figures, the alignment scores and the
unsorted-card exercise against the numbers printed here, so the guide and the script cannot
drift apart without a test failing.

To follow along with the script:

```
python3 scripts/analyse.py examples/guide-example.csv --merge-file examples/guide-example-merge.csv --bootstrap 0
```

(Bootstrapping five participants would say nothing useful, so it is switched off here.)

---

## 1. Before you start: what a card sort can and cannot tell you

A card sort shows **how a group of people put content together and what they call the groups**.
It does not show whether they can find anything.

What it supports:

- **Candidate groupings.** NN/g: card sorting "provides ideas for possible groupings", and a
  researcher will not know the exact structure afterwards. Spencer says it helps you "learn some
  stuff, not give you an answer".
- **Candidate labels.** Category names people invent are suggestions, not final labels.
- **Cards that need rewording or testing**, because those are the ones people disagree about.
- **Differences between groups of users**, if you have enough people in each group.

What it does not support:

- **A validated navigation.** NN/g's sequence is to card sort, then tree test the structure that
  emerged. Findability and task success need a tree test or usability test.
- **Depth.** Participants make one level of groups, not subcategories.
- **Behaviour in context.** The cards are isolated labels, with no links or surrounding content.
- **The reason behind a grouping,** if the sort was unmoderated. The data shows what was grouped,
  not why.

**Sample size.** Sources disagree because they answer different questions.

| Question | Figure | Source |
|---|---|---|
| How many people before the similarity matrix stops changing much? | Correlation with a 168-person result: 5 people 0.75, 15 people 0.90, 30 people 0.95, 60 people 0.98. NN/g recommends 15, or about 30 for large projects. | NN/g's reading of Tullis and Wood (2004). The original paper was not available, so this is `(unverified)`. |
| How many for the best similarity estimate? | 10 to 15 | Lantz et al. 2019, abstract only |
| How many before the dendrogram's groups are stable? | 30 or more for Optimal Workshop's Actual Agreement method | Optimal Workshop and UXtweak guidance, which is vendor advice |
| How precisely do you need to know one card's placement? | 10 people gives about plus or minus 27 points, 30 gives 17, 93 gives 10 | MeasuringU |

Katsanos et al. (2019) found similarity matrices from different studies of the same content
agreed well, but the final structures cut from their dendrograms agreed less. **The matrix is
steadier than the structure you draw from it.**

**Try it.** None of the sample sizes above matches a five-person study. What does that mean for
what you can claim from the example in this guide? *(Answer at the end.)*

**What the skill does.** Reports your number of participants and how stable the groups are, and
never gives a pass or fail line for sample size.

---

## 2. Participants (cleaning the data)

### What it shows
Each participant's own sort: their groups and which cards went where. In Playbook UX, click a
participant to see their categories and cards.

### How it is calculated
Nothing is calculated. You read each sort and decide whether it is usable. Look for:

- Everything in one group, or every card in its own group.
- Many more or fewer groups than most people made.
- Cards left unsorted.
- Vague names such as "stuff" or "miscellaneous".
- Very short or very long completion times, if your tool records them.

In the example: P1 made 3 groups, P2 made 4, P3 made 2, P4 made 3, P5 made 2. Nothing unusual.

An extra measure the skill adds: **alignment**, the correlation between a participant's pairings
and everyone else's. For each pair of cards, score 1 if this participant put them together and
0 if not, and correlate those 15 scores with the others' average. It is a prompt to look, not a
score to act on.

| Participant | Groups | Alignment |
|---|---|---|
| P1 | 3 | 0.85 |
| P2 | 4 | 0.15 |
| P3 | 2 | 0.67 |
| P4 | 3 | 0.69 |
| P5 | 2 | 0.45 |

P2 stands out (0.15). P2 put "Computer skills class" with "Borrow an e-book" under "Digital", a
grouping nobody else made.

### How to read it
A low alignment or an odd flag means **look at that sort**, not delete it. Wolf et al. (2012)
found the biggest source of variation in a physics card sort was not expertise but whether a
person tended to make a few big groups or many small ones ("stackers" and "spreaders"). What
looks like an outlier may be a different sorting style, and removing it may remove a real
perspective.

### Common misreadings
- Treating a flag as a reason to drop someone.
- Dropping people silently. If you exclude a participant, say who and why in the write-up.
- Expecting a validated cut-off. No independent source gives one for time or number of groups.

### Try it
Why might P2's sort be worth keeping despite the 0.15?

### What the skill does
Flags, never drops. It lists the flags and waits for you to decide which participants to exclude,
and the exclusions appear in the report.

---

## 3. Cards

### What it shows
For each card, the categories it was placed in and how many people put it in each.

### How it is calculated
Count placements per category, then share of participants.

Before standardising names (see section 4), "Renew a book" went to Borrowing (P1, P4), Loans
(P2), Books (P3) and Library services (P5). That looks like four opinions, but Loans and Books
are the same idea as Borrowing. After merging them, it is two:

- Borrowing: P1, P2, P3, P4 = 4 of 5 = **80%**
- Library services: P5 = 1 of 5 = 20%

**The confidence interval.** With only five people, 80% is not a precise number. A 95% Wilson
interval is:

    centre = (p + z²/2n) / (1 + z²/n)
    half   = z × √( p(1−p)/n + z²/4n² ) / (1 + z²/n)

with p = 4/5 = 0.8, n = 5, z = 1.96. That gives **38% to 96%**. The true share, had you asked
everyone, could plausibly be anywhere in that range.

The full cards view after merging (the script's output):

| Card | Sorted by | Top category | Share | 95% interval |
|---|---|---|---|---|
| Renew a book | 5 | Borrowing | 80% | 38% to 96% |
| Reserve a book | 5 | Borrowing | 80% | 38% to 96% |
| Borrow an e-book | 5 | Borrowing | 60% | 23% to 88% |
| Computer skills class | 5 | Events and classes | 40% | 12% to 77% |
| Author talk | 5 | Events and classes | 60% | 23% to 88% |
| Opening hours | 5 | Info | 40% | 12% to 77% |

(Opening hours is a tie: "Info" 2 and "What's on" 2. A tie is a finding, not a rounding problem.)

### How to read it
- A card most people put in one category is a good candidate for that category.
- **A card spread across several categories is one to investigate,** not one to average.
  Sauro: "Items are almost always associated with multiple groups", so report the top few
  placements, not just the winner.
- Read the interval before the share. 60% from 5 people (23% to 88%) says almost nothing.

### Common misreadings
- Reading a share without its sample size.
- Treating the top category as the answer when the runner-up is close.
- Counting differently named but identical categories as separate opinions (section 4).

### Try it
After merging Loans and Books into Borrowing, what share put "Borrow an e-book" in Borrowing, and
what is the interval? *(Answer at the end.)*

### What the skill does
Reports the top placement, the runner-up, and the interval for every card, and tells you when a
tie or a near tie means the top category is not clearly ahead.

---

## 4. Categories (and standardising names)

### What it shows
Each category name people used, how many people used it, and which cards went in it.

### How it is calculated
**Step 1, standardise.** People rarely use identical names. "Loans", "Books" and "Borrowing" may
be the same idea. Standardising means merging them into one name. Judge by **what is inside
the category, not by the name**:

- "Loans" held Renew a book and Reserve a book. "Books" held all three borrowing cards. Merge
  both into Borrowing.
- "Events" and "Events and classes" held event cards. Merge them.
- **"What's on" held Computer skills class, Author talk and Opening hours.** It sounds like
  "Events" but it also holds opening hours. Do not merge it just because of the name. Optimal
  Workshop warns that "multiple participants may have created the same category label, but what
  lies beneath could be a very different story", and Fincher and Tenenberg describe the same
  problem from Deibel et al.: two people using the word "difficult" may mean quite different
  things.

**Step 2, agreement.** For a standardised category, the skill reports the mean, across the
unique cards in it, of the share of the category's participants who put each card there. This
is the definition Kuric et al. use (`(unverified)` as an exact match to any tool's own number,
since the tools do not publish theirs).

For Borrowing after merging: used by 4 participants, 3 unique cards. Renew a book 4, Reserve a
book 4, Borrow an e-book 3. So (4 + 4 + 3) / (3 × 4) = 11/12 = **92%**.

For What's on: used by 2 participants (P3, P4), 3 unique cards. Computer skills class 1, Author
talk 2, Opening hours 2. So (1 + 2 + 2) / (3 × 2) = 5/6 = **83%**.

The categories view after merging:

| Category | Participants | Unique cards | Agreement |
|---|---|---|---|
| Borrowing | 4 | 3 | 92% |
| Events and classes | 3 | 2 | 83% |
| Info | 2 | 1 | 100% |
| What's on | 2 | 3 | 83% |
| Digital | 1 | 2 | 100% |
| Learning | 1 | 1 | 100% |
| Library services | 1 | 4 | 100% |

### How to read it
- Categories used by many people are shared ideas. Categories used by one person are that
  person's idea, so a "100%" there means nothing.
- Vendors suggest bands (UXtweak: 80% and above great, 60% and above good, below 60% bad;
  Optimal Workshop: above 60% worth keeping). **These are conventions with no evidence behind
  the cut-offs.** Use them as a prompt, not a verdict.

### Common misreadings
- Reading agreement on a category only one or two people made.
- Merging by name and inflating agreement.
- Forgetting that merging is your judgement. Write down what you merged and why, so someone
  else can disagree.

### Try it
"Library services" has 100% agreement. Why should you not conclude it is a strong category?

### What the skill does
Lists the names people typed, proposes merges by content, shows you each one, and applies only
the ones you approve. Standardising changes this view and the Cards view, never the Similarity
Matrix (section 6).

---

## 5. Merged Matrix (cards by categories)

### What it shows
Cards down the side, categories across the top, and how many participants put each card in each
category. In Playbook UX there is a count and a percentage toggle. For closed sorts the same
idea is called a results matrix.

### How it is calculated
It is the Cards view as a grid. After merging, the example gives:

| Card | Borrowing | Digital | Events and classes | Info | Learning | Library services | What's on |
|---|---|---|---|---|---|---|---|
| Renew a book | 4 | | | | | 1 | |
| Reserve a book | 4 | | | | | 1 | |
| Borrow an e-book | 3 | 1 | | | | 1 | |
| Computer skills class | | 1 | 2 | | 1 | | 1 |
| Author talk | | | 3 | | | | 2 |
| Opening hours | | | | 2 | | 1 | 2 |

Each row adds up to 5, because every card was sorted by all five participants. Divide a count by
the row total for the percentage.

### How to read it
Darker cells mean more participants. Look across a **row** to see where one card went, and down a
**column** to see what a category contains. A row with one dark cell is a settled card. A row with
two similar cells is a contested one.

### Common misreadings
- Reading a column as if it were one group everyone agreed on. It is the pool of cards anyone put
  there, so it can hold cards that never appeared together in any one person's sort.
- Comparing percentages across rows with different numbers of sorters (when cards were skipped).

### Try it
Which row has two cells tied for the highest count?

### What the skill does
Builds the grid from your standardised categories, prints the numbers in the cells, and for a
closed sort adds the confidence interval for each card's top placement.

---

## 6. Similarity Matrix

### What it shows
For every pair of cards, the share of participants who put them in the same group. It ignores
what the groups were called, so it shows which cards belong together in people's heads, not
what the groups should be named.

### How it is calculated, cell by cell
For two cards, go down the participants and score 1 if they were in the same group, otherwise 0.
Add up and divide by the number of participants.

"Renew a book" and "Borrow an e-book":

| Participant | Renew a book | Borrow an e-book | Together? |
|---|---|---|---|
| P1 | Borrowing | Borrowing | yes |
| P2 | Loans | Digital | no |
| P3 | Books | Books | yes |
| P4 | Borrowing | Borrowing | yes |
| P5 | Library services | Library services | yes |

Four of five, so **80%**. (The script prints this table for any pair with
`--explain "Renew a book" "Borrow an e-book"`.)

The group's name does not matter, so P3's "Books" and P4's "Borrowing" are not compared. Only
whether the two cards shared a group within each person's sort.

The full matrix, with the cards ordered so similar ones sit together:

| | Borrow an e-book | Renew a book | Reserve a book | Opening hours | Computer skills class | Author talk |
|---|---|---|---|---|---|---|
| **Borrow an e-book** | 100 | 80 | 80 | 20 | 20 | 0 |
| **Renew a book** | 80 | 100 | 100 | 20 | 0 | 0 |
| **Reserve a book** | 80 | 100 | 100 | 20 | 0 | 0 |
| **Opening hours** | 20 | 20 | 20 | 100 | 20 | 40 |
| **Computer skills class** | 20 | 0 | 0 | 20 | 100 | 60 |
| **Author talk** | 0 | 0 | 0 | 40 | 60 | 100 |

**Distance** is 1 minus similarity (so 80% similar is a distance of 0.2). Clustering works on
distance, and section 7 uses it.

**What if a card was left unsorted?** There are two defensible choices and no source settles
which is right, so the skill makes you pick and reports which you picked:

- **Singleton:** the card counts as "not together" with every other card, and the participant
  stays in the denominator.
- **Pairwise:** the participant is left out of any pair involving that card.

If P5 had left "Opening hours" unsorted, the pair "Author talk" and "Opening hours" (together for
P3 and P4) would score 2 of 5 = **40%** under singleton and 2 of 4 = **50%** under pairwise.
**Never treat "unsorted" as a group.** If you did, any two cards that two different people
skipped would look similar to each other.

### How to read it
Darker means more people grouped the pair together. White (0%) means nobody did. The matrix is
usually reordered so that blocks of dark cells fall along the diagonal. **Those blocks come from
the reordering, not from categories people named.**

### Common misreadings
- **Reading a dark cell as "agreed what the group is called".** It means "often together". The
  naming question is the Categories view.
- **Reading it as a structure.** It records pairs only, so it loses nesting. Nawaz (2012) shows
  two different datasets can give the same pair counts. Take three cards, a, b and c. If one
  person puts all three together and two people keep them apart, each pair scores 1 of 3. If
  three people each make one pair (a and b, then a and c, then b and c), each pair also scores
  1 of 3. The two datasets are different sorts with an identical matrix.
- **Averaging away different mental models.** One matrix can hide two camps of users who sort
  differently.
- **Comparing matrices from two studies with a plain correlation.** The cells are not
  independent, and Katsanos et al. recommend a Mantel test instead.
- **Assuming a tool's percentages mean the same as another's.** UserTesting's distance matrix
  counts people who did **not** group two cards, so lower means more similar `(unverified)`.
  Check the legend.

### Try it
What share of participants put "Computer skills class" and "Opening hours" together?

### What the skill does
Computes it from the placements, prints the numbers in the cells, and on a screenshot route asks
which way the colour runs and what the percentages are before reading anything.

---

## 7. Dendrogram

### What it shows
A tree that joins the most similar cards first, then joins those groups, until everything is
one cluster. The height (or percentage) of each join tells you how similar the things being
joined were.

### How it is calculated (average linkage)
Start with every card on its own. Repeat: find the two most similar groups, join them, and
recalculate how similar the new group is to each of the others.

**Average linkage** measures similarity between two groups as the **average distance across every
pair of cards, one from each group**. On the example:

1. **Renew a book + Reserve a book.** Distance 0. Joined at **100%** similarity.
2. **Borrow an e-book joins them.** Distance to Renew a book 0.2 and to Reserve a book 0.2,
   average 0.2. Joined at **80%**.
3. **Computer skills class + Author talk.** Distance 0.4. Joined at **60%**. (This is the
   smallest remaining distance, so it goes next.)
4. **Opening hours joins that pair.** Distance to Computer skills class 0.8, to Author talk 0.6,
   average 0.7. That beats joining the borrowing group (0.8 on average). Joined at **30%**.
5. **The two groups join.** Nine cross-pairs: 1, 1, 0.8, 1, 1, 0.8, 0.8, 1, 0.8, adding to 8.2,
   divided by 9 is 0.911. Joined at **8.9%**.

The script's text version of the tree:

    Joined at 9% similarity (6 cards)
      Joined at 80% similarity (3 cards)
        Borrow an e-book
        Joined at 100% similarity (2 cards)
          Renew a book
          Reserve a book
      Joined at 30% similarity (3 cards)
        Opening hours
        Joined at 60% similarity (2 cards)
          Computer skills class
          Author talk

### Where to cut
A tree is not a set of groups until you cut it. Cut at 50% similarity and you keep every join at
or above 50%:

- Renew a book, Reserve a book, Borrow an e-book
- Computer skills class, Author talk
- Opening hours (alone, because it only joined at 30%)

**With average linkage, the average pairwise similarity inside each group is at least the cut.**
(`(derived)`: it follows because average linkage's join heights never go down as groups grow.)

**The cut is a judgement.** Move it and the structure moves:

| Cut | Groups | Groups of one card |
|---|---|---|
| 30% | 2 | 0 |
| 40% | 3 | 1 |
| 50% | 3 | 1 |
| 60% | 3 | 1 |
| 70% | 4 | 3 |

Katsanos et al. note that "given the same dendrogram, two people can produce different content
structures", and Wolf et al. call reading one "a subjective exercise". Nawaz found one dataset
gave 4, 9 or 8 groups depending on the method and cut. The skill shows this table so you can see
how much your answer depends on where you cut.

**The method matters too.** Average linkage is the convention (Katsanos et al. say it "usually
produces balanced clusters", citing a data-mining textbook, not a card sort study). Other
linkages give different trees from the same data. On the example, single linkage (which joins on
the closest pair) attaches Opening hours at 40%, not 30%, because Author talk and Opening hours
were together for 40% of people. At a 40% cut, single linkage puts Opening hours with the
events cards and average linkage does not.

### How to read it
- Lower joins (higher similarity) are stronger. A tight cluster joined at 100% is a firm pair.
- Look for a **gap**, a long stretch with no joins, as a hint of a natural cut. Some trees have
  no such gap, and then no cut is natural.
- Compare the clusters to the Cards and Categories views. A group the tree makes and the
  categories do not support deserves a second look.

### Common misreadings
- **Reading it as the site's menu structure.** Hudson: "the hierarchy is based entirely on how
  often items appeared together in the same groups, it is not a taxonomic hierarchy", and the
  analysis takes no notice of group names. Spencer warns against using the dendrogram as the
  site hierarchy.
- **Reading the percentage as the same thing in every tool.** In Optimal Workshop's Actual
  Agreement Method it means the share of people who made that exact group. In its Best Merge
  Method it means the share who agreed with parts of it, which can credit a group nobody made.
  UXtweak describes the same two methods. **A tool's dendrogram may therefore differ from the
  one in this guide**, which uses plain average linkage.
- **Reading axis direction.** In some tools further left or higher means more agreement. In
  others the axis is a distance, where lower means more similar. Playbook UX does not document
  which method or direction it uses `(unverified)`, so check its legend and do not read heights
  as percentages unless it says they are.
- **Treating a closed sort's tree as meaningful.** The categories were supplied, so cards that
  share one may be together because of your labels. Optimal Workshop and UXtweak recommend
  placement matrices instead.

### Try it
What groups do you get if you cut the average-linkage tree at 70%? Why is Computer skills class
on its own?

### What the skill does
Draws the tree, names the method and the cut, shows the table above for neighbouring cuts, shows
the same cut under a second linkage, and bootstraps the participants to check how often each
group re-forms. Each group is scored stable, doubtful or unstable using the clusterboot bands (0.75
and 0.60), which were written for clustering in general, not for card sorts `(convention)`.

---

## 8. Participant-level analysis

### What it shows
Whether people share **whole structures**, not just pairings. Optimal Workshop calls it
participant-centric analysis and UXtweak calls it respondent-centric analysis. Both look for
sorts that other sorts resemble.

### How it is calculated
Reduce each sort to the set of pairs of cards it put together. Two participants "support" each
other when they share enough of those pairs. UXtweak's default is 50% of pairings. The sorts
with the most support become candidate structures, and a candidate that real people made is more
credible than one assembled by averaging.

Exact formulas are not published for either tool, so the skill does not reproduce them. It uses
the alignment measure from section 2 as a lighter signal.

### How to read it
If one real participant's sort is supported by many others, it is a strong candidate to take
into a tree test. If no sort is supported by more than a few, the group may hold several
different mental models and you should check whether they follow user types.

### Common misreadings
Treating the most popular sort as the answer. Optimal Workshop notes it works best with 30 or
more sorts, and where at least one structure has 50% or more support.

### Try it
In the example, whose sort looks most like the group's, and whose least?

### What the skill does
Reports alignment, flags unusual sorts for you to review, and suggests checking user types when
disagreement looks like it has a pattern.

---

## 9. Cards no single group settles

### What it shows
The cards where the data does not give one clear answer. They are often the most useful finding.

### How it is calculated
For each card, compare its average similarity to the other cards in its own group with its
average similarity to the best alternative group. The skill lists a card when it:

- does not join any group at your cut,
- is only weakly similar to its own group,
- is within 15 points of another group, or
- moves group often when participants are resampled.

**These thresholds are the script's defaults, not evidence-based.** In the example, **Opening
hours** is listed: it did not join a group at 50% and was 30% similar to the events pair.

In a closed sort the test is different: a card is listed when no category holds half the
participants, when the runner-up's confidence interval overlaps the top placement's, or when its
top placement moves under resampling.

### How to read it
Spencer and Warfel list four possible reasons for disagreement: participants did not understand
the content, it fits several areas, there are alternative paths to it, or different types of
participant see it differently. **The data cannot tell these apart.** NN/g suggests running a few
moderated sessions to find out which applies.

### What to do about a contested card
- **Unclear label:** reword it and test again.
- **Fits several areas:** consider cross-listing it, sparingly, or splitting the concept.
- **Different user groups:** analyse the groups separately, if each has enough people.
- **Unsure which:** put its candidate homes in a tree test.

### Try it
Which card is contested in the example, and what would you ask a participant to find out why?

### What the skill does
Lists the card with the numbers behind the flag, the possible causes, and a suggested follow-up.

---

## 10. Closed sorts

In a closed sort the categories are supplied, so there is no similarity matrix or dendrogram.
The analysis is placement agreement: for each card, the share of participants who put it in each
category, with a confidence interval, as in sections 3 and 5.

NN/g prefers tree testing over a closed sort for checking an existing structure.

The skill's closed-sort output adds, for each card, whether its top placement is stable under
resampling, and lists cards where the runner-up's interval overlaps the top placement's.

---

## 11. Writing it up

Keep three things apart, as NN/g's data, findings and insights distinction does:

1. **Data:** what participants did. "4 of 5 put Renew a book in Borrowing."
2. **Findings:** the pattern in it. "Borrowing is a stable group, and the interval on its share
   is wide because there were only five people."
3. **Recommendations:** what you suggest, labelled as judgement, with a confidence level and its
   basis.

A card sort gives ideas, not a structure. State what it cannot tell you (findability, depth,
behaviour in context) and name the next round: tree testing the structure you propose. A study
that stops at a card sort has not tested whether anyone can find anything, and that is a normal
place to stop before the next study, not a failure.

State, in the write-up:
- how many participants, and who was excluded and why
- which cards were left unsorted and how you counted them
- how you standardised names
- which linkage and cut you used, and how much the groups move at the neighbouring cuts
- which numbers are vendor conventions rather than evidence

The skill's report puts the short version first (what was studied, a proposed structure labelled
a draft, findings, contested cards, recommendations with confidence, what it cannot tell you),
and the evidence behind it second.

---

## 12. An optional later step: merges that redefine groups

By default, standardising names does not change the matrix, because the matrix records what
participants did. Suppose P2 had made two groups, "Loans" (Renew a book, Reserve a book) and
"Digital" (Borrow an e-book, Computer skills class). If you merge both names into "Borrowing",
you could treat P2 as having made one group, which would raise several cells.

**Only do that after you have read what the participants actually did, and only if you want
to.** It treats a merge of labels as a claim that two groups were really one. That claim is your
judgement, so the matrix then depends on your choices, and someone who merges differently gets a
different matrix. The skill does not do this by default.

---

## Spreadsheet formulas

For a small study you can do sections 3 to 6 in Excel or Google Sheets. Lay the sort out with one
row per card and one column per participant, each cell holding that participant's category name
(blank if unsorted). Say cards are in rows 2 to 7 and participants in columns B to F.

| To get | Formula |
|---|---|
| Participants who put row 2 in "Borrowing" | `=COUNTIF(B2:F2,"Borrowing")` |
| Participants who sorted row 2 | `=COUNTIF(B2:F2,"?*")` |
| Similarity of the cards in rows 2 and 3 | `=SUMPRODUCT((B2:F2=B3:F3)*(B2:F2<>""))/COLUMNS(B2:F2)` |

**The `(B2:F2<>"")` part matters.** In a spreadsheet two blank cells are equal, so without it two
cards a participant left unsorted would count as "together". It also gives the singleton setting
from section 6. Check the category names are spelt identically, since a stray space makes two
names differ.

The 95% Wilson interval, with the count in `B10` and the number of participants in `B11`:

    Lower: =((B10/B11)+1.96^2/(2*B11)-1.96*SQRT((B10/B11)*(1-B10/B11)/B11+1.96^2/(4*B11^2)))/(1+1.96^2/B11)
    Upper: =((B10/B11)+1.96^2/(2*B11)+1.96*SQRT((B10/B11)*(1-B10/B11)/B11+1.96^2/(4*B11^2)))/(1+1.96^2/B11)

For 4 of 5 these give 37.6% and 96.4%, which match section 3. A dendrogram is not practical in
a spreadsheet beyond a handful of cards. Use the five steps in section 7, or the script.

---

## Tool names compared

The nearest equivalents. A blank means no equivalent was found in the documentation. Closest
means similar, not identical. Check your tool's help if the exact meaning matters.

| This guide (Playbook UX names) | UXtweak | Optimal Workshop | Maze | Lyssna |
|---|---|---|---|---|
| Participants | Respondents tab (includes each person's own sort) | Participants tab (include, exclude and segment; no per-person sort view documented) | | |
| Cards | Cards analysis | Cards tab | Cards and categories tab | Card view |
| Categories | Categories analysis | Categories tab | Cards and categories tab | Category view |
| Merged Matrix | Standardization grid (open and hybrid), Results matrix (closed) | Standardization grid, Results matrix (closed) | Agreement matrix | Agreement matrix |
| Similarity Matrix | Similarity matrix | Similarity matrix | Similarity matrix | Similarity matrix (open and hybrid) |
| Dendrogram | Dendrogram | Dendrograms | none documented | none documented |
| Participant-level analysis | Respondent-centric analysis | Participant-centric analysis | | |

UserTesting and Useberry offer comparable views, but their help pages could not be read, so they
are left out rather than guessed at `(unverified)`.

---

## Answers to the exercises

**Section 1.** Almost nothing. Five people is the point on NN/g's curve where the matrix
correlated about 0.75 with the 168-person result, so firm structure claims are not supported. The
example is for learning the arithmetic.

**Section 2.** P2 grouped a card with "Borrow an e-book" under "Digital", which is a coherent
idea (digital things) that nobody else had. It may be a real perspective, so read it before
dropping it.

**Section 3.** 3 of 5 = 60%, interval 23% to 88%. (Borrowing: P1, P3 as "Books", P4. P2 put it
under "Digital" and P5 under "Library services".)

**Section 4.** It is used by one person, so "100%" only says that person was consistent with
themselves.

**Section 5.** "Opening hours": Info 2 and What's on 2, with Library services 1 behind.

**Section 6.** 1 of 5, which is **20%**. Only P3 put them together, both under "What's on".

**Section 7.** At 70% the groups are {Renew a book, Reserve a book, Borrow an e-book}, {Computer
skills class}, {Author talk} and {Opening hours}. Computer skills class and Author talk joined at
60%, which is below the 70% cut, so they separate.

**Section 8.** P1's sort (alignment 0.85) is closest to the group's, and P2's (0.15) is furthest.

**Section 9.** Opening hours. Ask the participant where they would look for it and what else they
would expect to find beside it.

---

## Further reading

Sources read directly while writing the skill. Anything marked `(unverified)` above reached this
guide through a secondary description.

- NN/g, [Card Sorting: Uncover Users' Mental Models](https://www.nngroup.com/articles/card-sorting-definition/)
- NN/g, [Card Sorting: How Many Users to Test](https://www.nngroup.com/articles/card-sorting-how-many-users-to-test/)
- NN/g, [Card Sorting vs. Tree Testing](https://www.nngroup.com/articles/card-sorting-tree-testing-differences/)
- Spencer and Warfel, [Card sorting: a definitive guide](https://boxesandarrows.com/card-sorting-a-definitive-guide/) (2004)
- Lamantia, [Analyzing card sort results with a spreadsheet template](https://boxesandarrows.com/analyzing-card-sort-results-with-a-spreadsheet-template/) (2003)
- Katsanos et al., [Card sorting reliability across studies](https://arxiv.org/abs/1903.08644) (CHI 2019, late-breaking work)
- Kuric, Demcak and Krajcovic, [Card sorting with random subsets of cards](https://arxiv.org/abs/2509.03232) (the agreement formula in section 4)
- Nawaz, [A comparison of card-sorting analysis methods](https://research-api.cbs.dk/ws/files/58892620/Ather_Nawaz_2012.pdf) (2012)
- Fincher and Tenenberg, [Making sense of card sorting data](https://faculty.washington.edu/jtenenbg/publications/fincherMakingSenseOfCardSorting-expSys2005.pdf) (2005)
- Wolf, Dougherty and Kortemeyer, [Empirical card-sorting analysis](https://arxiv.org/abs/1201.6601) (2012)
- MeasuringU, [Card sorting](https://measuringu.com/card-sorting/) and [Card sorting for IA](https://measuringu.com/card-sorting-ia/)
- Optimal Workshop, [dendrograms](https://support.optimalworkshop.com/en/articles/2626862-interpret-dendrograms-for-open-and-hybrid-card-sorts) and [the similarity matrix](https://support.optimalworkshop.com/en/articles/2626857-understand-the-similarity-matrix)
- UXtweak, [dendrogram](https://www.uxtweak.com/help/card-sorting-results/analysis-dendrogram/) and [similarity matrix](https://www.uxtweak.com/help/card-sorting-results/analysis-similarity-matrix/)
- Playbook UX, [Analyzing your card sort](https://help.playbookux.com/en/articles/5366057-analyzing-your-card-sort)

---

## Change log

**21 October 2026.** Guide created alongside the analysis script. Every figure in the worked
example was produced by `scripts/analyse.py`, and the figures listed in the introduction are
checked by `tests/test_analyse.py`.
