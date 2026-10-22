# Customer Discovery Playbook

Deep-dive reference for the customer-discovery skill. Frameworks belong to their authors; sources repeat per framework.

## 1. Continuous Discovery Habits (Teresa Torres)

- **Definition:** A weekly cadence of discovery activities — customer interviews, assumption tests — in which a cross-functional product trio (PM, designer, tech lead) co-creates solutions with customers instead of handing requirements downhill.
- **When to use:** Established products guiding incremental iteration, optimization, and backlog refinement; any team whose research currently happens in one-off projects.
- **When NOT to use:** Highly speculative research on technology that does not yet exist; contexts with zero customer access (fix access first via incentives or proxies, §5).
- **Prerequisites:** A standing recruitment pipeline (auto-recruited panel, incentive offered on every request) so weekly scheduling never blocks the cadence.
- **Worked Example:** A billing team keeps an auto-recruited panel of finance admins offered a $50 gift card (`[ASSUMPTION]`-grade incentive). Every week the trio watches an admin walk through how they processed last month's invoices, logging recurring bugs and workarounds that feed the next cycle's tree.
- **Source URL:** [producttalk.org](https://www.producttalk.org)

## 2. Opportunity Solution Tree (Teresa Torres)

- **Definition:** A visual map linking a single measurable business outcome (root) to verified user opportunities (needs, pains, desires in the user's words), to candidate solutions (>= 3 per opportunity), to rapid experiments.
- **When to use:** Organizing brainstorms, structuring weekly research, and justifying roadmap priorities to stakeholders.
- **When NOT to use:** When the outcome cannot be measured — fix the outcome metric first; a tree rooted in "ship X" degenerates into a backlog.
- **Structure rules:** One outcome per tree. Opportunities in the customer's words, each with an evidence citation or `[ASSUMPTION]` tag. No solution without a parent opportunity. Every leading solution carries a smallest experiment with a quantitative success/kill threshold and an anchor.
- **Worked Example:** *Outcome:* food-app MAU +10% (anchor: trailing 3-month MAU). *Opportunity:* "I struggle to decide what to eat for dinner." *Solution:* randomized "Surprise Me" recipe button. *Experiment:* mock button in the UI; click-through vs median entry-point CTR (anchor: prior quarter telemetry) decides build-vs-kill.
- **Source URL:** [producttalk.org](https://www.producttalk.org)

## 3. The Mom Test (Rob Fitzpatrick)

- **Definition:** An interviewing framework that extracts objective facts about past behavior instead of opinions, guesses, or polite compliments about your idea — so named because it survives talking to your mom, who will lie to protect your feelings.
- **When to use:** Early problem validation and generative research; any interview where the idea might be mentioned.
- **When NOT to use:** Testing interactive prototypes (use usability sessions); investigating churn reasons alone (pair with telemetry, §5).
- **Rules:** (1) Talk about their life, not your idea. (2) Ask about specifics in the past, never generics or futures. (3) Talk less, listen more.
- **Worked Example:** *Bad:* "Would you buy an app that manages your gym workouts?" (polite lie). *Good:* "Walk me through how you planned last week's workouts. What did you track it with? Show me the last entry." (raw facts).
- **Source URL:** [momtestbook.com](https://www.momtestbook.com)

## 4. Commitment & Advancement Signals (Rob Fitzpatrick)

- **Definition:** Validating interest by requiring the user to give up something of value — time, reputation, or money — to advance the idea. Escalating asks separate real pain from politeness.
- **When to use:** At the end of discovery interviews and concept checks, to grade whether observed interest is genuine.
- **When NOT to use:** Churn research (churned users want to disengage, not advance) and general support conversations.
- **Application:** 1. *Time:* "Join a 1-hour trial with your team next Tuesday?" 2. *Reputation:* "Introduce me to your IT security director for the privacy review?" 3. *Money:* "We're taking $100 refundable deposits for early access — in?" (`[ASSUMPTION]`-grade amount). 4. *Score:* refusal of every ask reclassifies prior compliments as noise.
- **Worked Example:** A prospect says "this is exactly what we need." The PM answers, "Great — I'll need your IT security director's intro today to clear review. Can you make the email now?" Hesitation means the interest is unvalidated, whatever was said before.
- **Source URL:** [momtestbook.com](https://www.momtestbook.com)

## 5. Churn Interviews: Limits & Telemetry Triangulation

- **The limit:** Mom Test interviewing is weak on churned users. They offer polite rationalizations ("no time", "too expensive") to end the call and avoid confrontation. Stated churn reasons are hypotheses.
- **Triangulation procedure:**
  1. Never rely on interviews or surveys alone for churn causes.
  2. Before the call, review the user's session telemetry: drop-off at a specific onboarding step? crashes or latency errors? never reached the activation milestone?
  3. In the call, walk through the observed sessions before accepting stated reasons; note match/mismatch explicitly.
- **Sampling-bias mitigation:** Churned users who accept a call are vocal outliers. Counter with (a) compelling incentives (e.g. $100 gift card — `[ASSUMPTION]`-grade amount), (b) proxy populations — users whose activity decayed but who haven't formally canceled, who still remember the friction, (c) whole-database behavioral analysis of drop-off points so the majority pattern, not the interview sample, sets priorities.
- **Worked Example:** A churned user claims "we cut budget." Telemetry shows two logins, 12 minutes struggling on the integrations page, three latency errors. Verdict: usability/feasibility churn, labeled with the telemetry citation; the budget story is recorded as stated-but-contradicted.
- **Source URL:** [momtestbook.com](https://www.momtestbook.com) (interview limits); triangulation procedure is repo synthesis on standard product-analytics practice.

## 6. Assumption Mapping & Testing (four risks; Marty Cagan)

- **Definition:** Surfacing the leap-of-faith assumptions behind a candidate solution across Value, Usability, Feasibility, and Viability, then testing the riskiest before build.
- **When to use:** Before writing production code for any major feature.
- **When NOT to use:** Minor bug fixes and routine optimization.
- **Conversational-AI friction rule:** For chat-style AI features in task-focused tools, the primary Value risk is interaction friction, not model quality. Test a click-through comparing the prompt drawer against a one-click action button; if users choose the drawer below 20% of sessions (this skill's operating default, `[ASSUMPTION]`-grade), reject the conversational UI for structured buttons.
- **Worked Example:** B2B team-sharing workspace. Critical Value assumption: admins will let employees share company data externally. Test without backend: draft the policy doc and email template, ask enterprise admins to sign off; proceed only at >= 70% agreement (example threshold, `[ASSUMPTION]`-grade, anchor to your own pilot).
- **Source URL:** [svpg.com/articles](https://svpg.com/articles/)

## 7. Sources

- Continuous Discovery Habits, Opportunity Solution Tree: Teresa Torres — [producttalk.org](https://www.producttalk.org)
- Mom Test rules, commitment signals, interview limits: Rob Fitzpatrick — [momtestbook.com](https://www.momtestbook.com)
- Four product risks and assumption testing: Marty Cagan — [svpg.com/articles](https://svpg.com/articles/)
