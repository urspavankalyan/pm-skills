# Interview Guide Template

<!-- Load for every scheduled discovery call. Type = Generative (problem), Concept check, or Churn. Delete unused sections; never ship bracketed placeholders. -->

```markdown
# Interview Guide: [Opportunity / problem area]

**Trio:** PM [name] | Design [name] | Tech Lead [name] | **Date:** [YYYY-MM-DD]
**Interviewee:** [role, company size, segment] | **ICP verified:** [yes / no]
**Type:** [Generative / Concept check / Churn]

## Pre-call telemetry (required for Churn; recommended for existing users)
<!-- Review last 3 sessions before the call. Findings steer the question order. -->
- Drop-off step: [onboarding step / none observed]
- Errors or latency events: [count, screen]
- Activation milestone reached: [yes / no]
- If telemetry unavailable: mark all churn findings `[UNTRIANGULATED]` and use proxy-population sampling.

## Ground rules (trio reads before dialing)
<!-- 1. Talk about their life, not our idea. 2. Specifics in the past, never generics or futures.
     3. Talk less, listen more. 4. No pitching, no leading, no feature names before they raise them. -->

## Opening (2 min)
- "There are no right answers — we're learning how you work today, and blunt problems help us more than polite ones."
- Churn only: "In your words, what happened between you and the product?"

## Past-behavior block (pick 4-6; every question references a specific recent event)
- "Walk me through the last time you [job to be done], step by step."
- "What did you do right before and after? Which tools, sheets, or people were involved?"
- "When did it last break or take too long? What exactly happened, and what did you do?"
- "What have you already tried or bought to fix it? What did that cost?"
- "If this stays broken, what does it cost you per [week / month]?" <!-- severity anchor -->
- "Show me the artifact" (spreadsheet, inbox, log) where possible. <!-- facts beat recall -->
<!-- Banned AS VALIDATION QUESTIONS on the call: "would you use/pay/like", "could you imagine", "do you like", any pitch.
     The commitment ask below is a real ask for time/reputation/money, not a validation hypothetical - it stays. -->

## Commitment ask (pick ONE matching the idea stage; never skip)
- Time: "Book a 1-hour trial with your team next [weekday] - we'll set it up together on the call."
- Reputation: "Can you introduce me to your [IT / security / finance director] this week?"
- Money: "We're taking refundable $[100] deposits for early access — are you in?" <!-- amount is [ASSUMPTION]-grade -->
<!-- Record the answer verbatim. Hesitation or refusal => earlier compliments are noise. -->

## Close
- "Who else should we talk to?" <!-- referral = soft reputation signal -->

## Post-call notes (file within 24h; feeds the Opportunity Solution Tree)
- Facts (past behavior, verbatim quotes): [bullets]
- Opportunities in the user's words: [bullets -> OST]
- Commitment signal: [time / reputation / money / refused] — verbatim result: [quote]
- Telemetry match (churn): stated reason vs observed sessions: [match / mismatch + detail]
- Assumptions surfaced: `[ASSUMPTION]` [claim] — revisit trigger: [date or event]
```
