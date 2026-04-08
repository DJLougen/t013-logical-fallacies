# T013: Reasoning Depth Assessment - Logical Fallacies

A psychometric benchmark for evaluating AI agent reasoning quality using Item Response Theory (IRT) principles.

## Overview

This benchmark tests whether an AI can think logically like a trained reasoner — not just get the right answer, but demonstrate the right reasoning process, catch its own errors, and verify conclusions.

## Task Definition

Analyze **10 logical arguments** and:
1. Classify each as valid or invalid
2. Identify specific fallacies (undistributed middle, affirming consequent, etc.)
3. Explain reasoning for each classification
4. Show step-by-step analysis for each argument

## Psychometric Properties

| Parameter | Value | Meaning |
|-----------|-------|---------|
| **Difficulty (b)** | 0.0 | Baseline difficulty — targets average ability level |
| **Discrimination (a)** | 1.2 | Good at separating different ability levels |
| **Target θ Range** | [-1.0, +1.0] | Average to above-average reasoners |
| **Par Steps** | 15 | Expected efficient completion steps |

## Scoring Dimensions

This task focuses on **3 of the 7 Caduceus dimensions:**

| Dimension | Weight | Target Score |
|-----------|--------|--------------|
| **Thinking Depth** | 17% | ≥ 2.0 (thorough analysis) |
| **Self-Correction** | 17% | ≥ 1.5 (catches own errors) |
| **Verification** | 14% | ≥ 1.5 (multiple verification approaches) |

## Directory Structure

```
├── README.md                 # This file
├── task.json                 # Task definition (Caduceus format)
├── problems/
│   ├── logical_arguments.txt   # 10 arguments to analyze
│   ├── scoring_rubric.md       # 7-dimensional rubric
│   └── expected_analysis.md    # Reference solutions
└── scoring/
    └── evaluate.py             # Automated scoring script
```

## Running the Benchmark

```bash
# Download problems
git clone https://github.com/DJLougen/t013-logical-fallacies
cd t013-logical-fallacies

# Run with your agent
python3 scoring/evaluate.py --agent <your-agent> --problems problems/
```

## Success Criteria

To pass, an agent must:
- ✓ Correctly classify all 10 arguments
- ✓ Identify fallacies accurately
- ✓ Show thinking depth ≥ 2.0
- ✓ Demonstrate self-correction ≥ 1.5
- ✓ Use verification ≥ 1.5
- ✓ Enable IRT ability estimate (θ) calculation

## License

MIT License — See LICENSE file.

## References

- [Caduceus Benchmark Framework](https://djlougen.github.io/caduceus/)
- [Item Response Theory](https://en.wikipedia.org/wiki/Item_response_theory)
- [Logical Fallacies](https://en.wikipedia.org/wiki/Fallacy)
