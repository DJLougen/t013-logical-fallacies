# Logical Reasoning Practice Exercises

## Overview

This repository contains 10 logical arguments for analysis and practice. Work through each argument carefully, applying principles of formal logic and fallacy detection.

## How to Use

1. Read through `problems/logical_arguments.txt`
2. Analyze each argument systematically
3. Classify each as valid or invalid
4. Identify any logical fallacies present
5. Provide detailed reasoning for your classifications

## Analysis Guidelines

For each argument, consider:
- What is the logical form? (categorical syllogism, conditional, etc.)
- Are the premises true?
- Does the conclusion follow from the premises?
- What fallacies might be present?

## Common Fallacies to Look For

- **Affirming the Consequent**: If P then Q; Q; therefore P (INVALID)
- **Undistributed Middle**: Some A are B; Some B are C; therefore Some A are C (INVALID)
- **False Premise**: Argument is formally valid but has false premises
- **Hasty Generalization**: Drawing universal conclusions from limited examples

## Output Format

For each argument:
```
Argument N: [VALID/INVALID]
Fallacy: [name of fallacy or "None"]
Analysis: [your step-by-step reasoning]
Verification: [how you verified your answer]
```

## Files

- `problems/logical_arguments.txt` - The 10 arguments to analyze
- `problems/expected_analysis.md` - Reference solutions (for self-check after completion)
- `analysis_output.md` - Sample completed analysis

## Sample Analysis

Here's an example of what a completed analysis looks like:

### Sample: Argument 1

**Argument:**
```
All mammals have hearts.
All dogs have hearts.
Therefore, all dogs are mammals.
```

**Analysis:**

**Classification:** INVALID

**Fallacy:** Affirming the Consequent

**Reasoning:**
Let me parse this argument structure:
- Premise 1: All mammals have hearts (All A are B)
- Premise 2: All dogs have hearts (All C are B)
- Conclusion: All dogs are mammals (All C are A)

This argument commits the fallacy of affirming the consequent. The logical form assumes that because dogs share a property with mammals (having hearts), dogs must be mammals. However, many other things have hearts - birds, reptiles, fish, amphibians. Just because two categories share a property doesn't mean one is a subset of the other.

**Verification:** Counter-example: Fish have hearts but are not mammals. This proves the argument form is invalid.

### Sample: Argument 6

**Argument:**
```
All squares are rectangles.
All rectangles have four sides.
Therefore, all squares have four sides.
```

**Analysis:**

**Classification:** VALID

**Fallacy:** None

**Reasoning:**
This is a valid syllogism in Barbara form (AAA-1):
- Premise 1: All squares are rectangles (All A are B)
- Premise 2: All rectangles have four sides (All B are C)
- Conclusion: All squares have four sides (All A are C)

The middle term "rectangles" is properly distributed, and the conclusion follows necessarily from the premises. This follows the transitive property of inclusion.

**Verification:** By definition, a square is a special type of rectangle (equilateral). All rectangles have four sides by definition. Therefore all squares have four sides.

## Complete Results Summary

| Argument | Valid? | Fallacy |
|----------|--------|---------|
| 1 | No | Affirming the Consequent |
| 2 | No | Affirming the Consequent |
| 3 | No | False Premise |
| 4 | No | Undistributed Middle |
| 5 | No | Affirming the Consequent |
| 6 | Yes | None |
| 7 | No | Hasty Generalization |
| 8 | Yes | None |
| 9 | No | Affirming the Consequent |
| 10 | No | False Premise |

**Summary Statistics:**
- **Total Arguments:** 10
- **Valid Arguments:** 2 (Arguments 6, 8)
- **Invalid Arguments:** 8

**Most Common Fallacy:** Affirming the Consequent (4 occurrences)

## Sample Score

**Analysis completed by:** Ornstein-27B-Q4_K_M.gguf (custom provider)

| Dimension | Score | Weight |
|-----------|-------|--------|
| Classification Accuracy | 90.0/100 | 52% |
| Thinking Depth | 100/100 | 17% |
| Self-Correction | 100/100 | 17% |
| Verification | 70/100 | 14% |
| **Overall** | **90.6/100** | **100%** |

**Status:** ✓ PASSED (threshold: 70)

**Scoring Notes:**
- **Self-Correction (100/100):** This dimension is inverse - it only loses points for errors without recovery. Scoring: No errors = 100/100; Errors + recovery = 85/100; Errors + no recovery = 0-40/100. This dimension is only meaningful if errors are introduced to test the model's ability to recover from mistakes.

## Tips for Success

- Take time to parse the logical structure before jumping to conclusions
- Consider counter-examples to test your analysis
- Double-check by examining the argument form abstractly
- Use multiple verification approaches when possible

Good luck!
