# analyse.py

Computes the standard views of an open or hybrid card sort from per-placement
data, and prints every setting that changes the answer.

Needs Python 3.9 or later, numpy and scipy:

```
python3 -m pip install numpy scipy
```

## Input

A CSV with one row per card placement:

| Column | Meaning |
|---|---|
| `participant_id` | any stable ID |
| `card` | card title |
| `category` | the name the participant gave the group. Blank means the card was left unsorted |
| `order` | optional, ignored by the analysis |

Different column names? Map them with `--col-participant`, `--col-card` and
`--col-category`. The script lists the columns it found if one is missing.

## Run it

```
python3 analyse.py results.csv --out analysis/
```

Useful options:

| Option | What it does |
|---|---|
| `--list-categories` | List the category names people typed, to help you build a merge file |
| `--merge-file FILE` | CSV with columns `raw,standard` to standardise category names. Affects the cards and categories views only, never the similarity matrix |
| `--exclude P3,P7` | Leave participants out. The checks flag odd sorts but never drop them for you |
| `--unsorted singleton\|pairwise` | How a card left unsorted counts toward a pair (default `singleton`, see below) |
| `--unsorted-label NAME` | Treat a category called NAME as "left unsorted" |
| `--cards FILE` | One card per line, to catch cards nobody sorted |
| `--linkage average\|complete\|single` | Clustering method (default `average`) |
| `--cut 0.5` | Similarity at which the tree is cut (default 0.5) |
| `--bootstrap N` | Resamples for the stability check (default 1000, `0` to skip) |
| `--explain "Card A" "Card B"` | Show the arithmetic behind one cell of the matrix |

## Choices it makes, and says it made

- **Similarity** is the share of participants who put a pair in the same
  group. **Distance** is 1 minus that.
- **Unsorted cards.** `singleton`: the card counts as "not together" with
  every other card, and the participant stays in the denominator. `pairwise`:
  the participant is left out of any pair involving the card. No published
  source settles which is right, so the choice is yours and is printed in
  every report. An "Unsorted" group is never treated as a real group.
- **The cut point is a judgement.** The output shows how the structure moves
  at other cuts and under a second linkage.
- **Thresholds in the contested-card and stability sections are this
  script's defaults**, not evidence-based cut-offs.

## Sort types

`--sort-type open` (the default) and `hybrid` run the similarity and
clustering analysis. `closed` runs placement agreement instead: the top
category per card with a 95% interval, the runner-up, a results matrix, and how
often each card's top placement holds when participants are resampled. A
similarity matrix and dendrogram are not computed for a closed sort, because the
supplied categories bias what ends up together.

For a hybrid sort, add a `category_preset` column (`true` for categories the
researcher supplied) and the script lists which categories were preset.

## The other two scripts

`render_report.py` builds the two-layer HTML report from `results.json` and a
findings file, using only the standard library. See
`references/reporting.md` for the findings file and
`examples/sample-findings.json` for a working one.

```
python3 render_report.py --findings findings.json --results analysis/results.json --out report.html
```

`to_long.py` converts a wide grid (one row per card, one column per
participant) into the shape `analyse.py` reads:

```
python3 to_long.py grid.csv --out results.csv
```

## What it does not do

- Optimal Workshop's Actual Agreement and Best Merge dendrogram methods.
  Its dendrogram may therefore differ from this one.
- Automatic merging of category names. You decide the merges.
- Chance-corrected agreement (kappa or alpha) for closed sorts. No
  card-sort-specific validation was found.
- It has been tested on synthetic data and a hand-worked example only, not on
  a real export from any card sorting tool.

## Tests

```
python3 -m unittest discover tests
```
