# Writing Schools: Cagan Outcome Brief vs Shape Up Pitch

Two coherent contracts with engineering exist. Pick one per document; blending is the failure mode this file prevents.

## The positions

- **Cagan outcome brief (SVPG)** — the team is given a business problem and full solution autonomy. The document defines problem, evidence, the four risks, and the outcome metric; it deliberately does NOT define the solution. Fix outcome, flex solution.
- **Shape Up pitch (Ryan Singer)** — the bet is a shaped solution at medium abstraction: appetite (fixed time), breadboard (places + actions), fat-marker boundaries, explicit no-gos. Engineers own implementation details inside the boundaries. Fix time, flex scope.

## Decision criteria

Choose **Shape Up pitch** if:
- The team is drowning in backlog grooming or slipping estimates.
- Engineers explicitly want bounded autonomy over a shaped bet.
- The cycle rhythm is already 6-week big batches / 2-week small batches.

Choose **Cagan outcome brief** if:
- The team is empowered and mature: it should discover the solution, not receive one.
- The solution space is genuinely unknown and shaping now would be guesswork.
- The domain is regulated or safety-critical (billing, medical, compliance) where exhaustive specs are contractual.

Choose **Cagan regardless** when in doubt for a first document with a new team: outcome contracts degrade more gracefully than half-shaped bets.

## Blend detection (reject these on review)

- A document with both an "Appetite: 6 weeks" field AND a numbered requirements backlog.
- "Engineers own the solution" next to pixel-specified MUST statements.
- A breadboard plus a "to be discovered in sprint" solution section.

Rectification: if scope control is the pain, convert to a shaped pitch and move the backlog items to Explicit Out of Bounds. If solution autonomy is real, convert to an outcome brief and delete the breadboard.

## Sources

- Ryan Singer, *Shape Up* — [basecamp.com/shapeup](https://basecamp.com/shapeup)
- Marty Cagan, *Empowered* / SVPG — [svpg.com/articles](https://svpg.com/articles/)
