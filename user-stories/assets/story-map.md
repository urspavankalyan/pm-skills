# Story Map Template (Jeff Patton)

<!-- Build the backbone first, then the walking skeleton, then depth. Slices are learning bets, not committed dates. Delete unused sections; never ship bracketed placeholders. -->

```markdown
# Story Map: [Initiative, named as outcome hypothesis, e.g. "Merchants close the books without manual entry"]

**Outcome:** [ICP + metric, baseline -> target, date] | **Evidence:** [citations or [ASSUMPTION - outcome unvalidated]]

## Backbone (user activities, left to right, in narrative order)
1. [Activity 1, e.g. Capture orders]
2. [Activity 2, e.g. Prepare shipments]
3. [Activity 3, e.g. Export for accounting]
4. [Activity 4, e.g. Reconcile payments]

<!-- Backbone reads as the customer's end-to-end job; if it reads as a feature list, rewrite as activities. -->

## Steps (under each activity)
- [Activity 1]: [step 1a], [step 1b]
- [Activity 2]: [step 2a], [step 2b]
- [Activity 3]: [step 3a], [step 3b]
- [Activity 4]: [step 4a]

## Candidate stories (under each step, ordered by value)
- [step 1a]: [job-story title]; [job-story title]
- [step 2a]: [job-story title]
- [step 3a]: [job-story title]; [job-story title]
<!-- Stories use the user-story.md template when written out. -->

## Walking skeleton (first end-to-end slice)
[The thinnest story under each backbone activity that makes the whole flow work once, ugly but real]
- [Activity 1 slice story] -> [Activity 2 slice story] -> [Activity 3 slice story] -> [Activity 4 slice story]

## Release slices (ordered by evidence value)
**Slice 1 ([Now / next cycle]):** [stories] — expects [outcome delta or learning, anchored or [ASSUMPTION]]
**Slice 2:** [stories] — expects [delta / learning]
**Slice 3:** [stories] — expects [delta / learning]
<!-- Later slices are re-planned from what earlier slices teach; they are horizons, not promises. -->

## Out of bounds this map
- [explicit no-gos, e.g. "no API export until CSV slice shows demand twice"]
```
