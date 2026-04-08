# Caduceus Scoring Rubric

## Overview

Every trajectory is scored 0-100 on seven orthogonal dimensions. Scores are computed by a combination of automated validators and LLM-based judges, then statistically normalized across all submissions.

## Dimension Definitions

### 1. Thinking Depth (Weight: 17%)

Measures the quality of reasoning before and during action.

| Score Range | Description |
|-------------|-------------|
| 80-100 | Plans before acting, considers edge cases, reasons about tradeoffs, updates mental model as new info arrives |
| 60-79 | Shows planning but occasionally jumps to action prematurely, misses some edge cases |
| 40-59 | Minimal planning, reactive approach, follows obvious path without considering alternatives |
| 0-39 | No visible reasoning, trial-and-error, random tool calls |

### 2. Self-Correction (Weight: 17%)

Measures the ability to detect and fix own mistakes mid-trajectory.

| Score Range | Description |
|-------------|-------------|
| 80-100 | Notices errors immediately, diagnoses root cause of own mistake, corrects without repeating the same pattern |
| 60-79 | Catches most errors but sometimes repeats a failed approach once before changing |
| 40-59 | Slow to recognize failures, may repeat the same broken approach 2-3 times |
| 0-39 | Loops on failed approaches indefinitely, never adjusts strategy |

### 3. Verification (Weight: 14%)

Measures whether the agent confirms its work actually succeeded.

| Score Range | Description |
|-------------|-------------|
| 80-100 | Always checks output, runs tests, reads results, confirms fix before declaring done |
| 60-79 | Usually verifies but occasionally declares success without checking |
| 40-59 | Sporadic verification, often assumes success based on lack of errors |
| 0-39 | Never verifies, moves on immediately after attempting a fix |

### 4. Tool Diversity (Weight: 14%)

Measures breadth and appropriateness of tool selection.

| Score Range | Description |
|-------------|-------------|
| 80-100 | Uses the right tool for each subtask, leverages multiple tools effectively, doesn't over-rely on any single tool |
| 60-79 | Good tool selection but occasionally uses a suboptimal tool when a better one is available |
| 40-59 | Over-relies on 1-2 tools, ignores available alternatives |
| 0-39 | Uses only terminal for everything, or only one tool regardless of task requirements |

### 5. Recovery Rate (Weight: 14%)

Measures graceful handling of unexpected failures.

| Score Range | Description |
|-------------|-------------|
| 80-100 | Handles permission errors, missing files, crashed services gracefully — reads error, adapts approach, finds workaround |
| 60-79 | Recovers from most failures but struggles with uncommon error types |
| 40-59 | Gets stuck on unexpected errors, slow to adapt |
| 0-39 | Crashes on first unexpected error, gives up or loops |

### 6. Efficiency (Weight: 12%)

Measures task completion with minimal waste, contextualized by par step count.

| Score Range | Description |
|-------------|-------------|
| 80-100 | At or under par steps, no redundant commands, clean trajectory |
| 60-79 | Slightly over par, minor redundancies (re-reading files, unnecessary checks) |
| 40-59 | Significantly over par, noticeable wasted steps, repeated commands |
| 0-39 | Extreme waste — many times over par, loops, unnecessary tool calls |

### 7. Proactiveness (Weight: 12%)

Measures anticipatory behavior — acting without being explicitly told.

| Score Range | Description |
|-------------|-------------|
| 80-100 | Checks permissions before writing, verifies services before connecting, anticipates follow-up issues, preemptively gathers context |
| 60-79 | Occasionally proactive but mostly reactive to errors as they occur |
| 40-59 | Purely reactive — only acts on explicit errors |
| 0-39 | Doesn't even react to obvious upcoming problems |

## Weight Profiles

Different use cases weight dimensions differently:

| Profile | THK | COR | VER | TDV | REC | EFF | PRO |
|---------|-----|-----|-----|-----|-----|-----|-----|
| General | 17% | 17% | 14% | 14% | 14% | 12% | 12% |
| Security-first | 10% | 10% | 25% | 10% | 25% | 10% | 10% |
| Performance-first | 20% | 10% | 10% | 10% | 10% | 25% | 15% |
| Reasoning-first | 25% | 20% | 10% | 10% | 10% | 5% | 20% |

## Statistical Normalization

Raw scores are normalized using:

1. **Z-score normalization** per dimension across all submissions — centers each dimension to mean=0, std=1
2. **IQR scaling** to handle outliers — clips at 1.5x IQR
3. **Parameter-count bucketing** — results are contextualized within size tiers (≤9B, 10-35B, 36-72B, 72B+) so a strong small model gets appropriate credit
4. **Composite score** = weighted sum of normalized dimension scores, scaled back to 0-100

## Anti-Gaming Safeguards

- Tasks use held-out test sets never exposed during training
- Prompt templates rotate between runs
- Variance tracking flags agents with suspiciously low score variance
- Full trajectory recording enables manual audit of any run
- Par step counts are recalibrated periodically as models improve
