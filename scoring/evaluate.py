#!/usr/bin/env python3
"""
Evaluate agent performance on the T013 Logical Fallacies benchmark.
Scores responses on the 3 primary Caduceus dimensions for this task.
"""

import json
import argparse
from pathlib import Path

# Expected answers
EXPECTED = {
    1: {"valid": False, "fallacy": "affirming consequent"},
    2: {"valid": False, "fallacy": "affirming consequent"},
    3: {"valid": False, "fallacy": "false premise"},
    4: {"valid": False, "fallacy": "undistributed middle"},
    5: {"valid": False, "fallacy": "affirming consequent"},
    6: {"valid": True, "fallacy": None},
    7: {"valid": False, "fallacy": "hasty generalization"},
    8: {"valid": True, "fallacy": None},
    9: {"valid": False, "fallacy": "affirming consequent"},
    10: {"valid": False, "fallacy": "false premise"}
}

def score_classification(agent_answer, expected_answer):
    """Score correctness of classification."""
    score = 0
    if agent_answer.get("valid") == expected_answer["valid"]:
        score += 50  # 50 points for correct valid/invalid
    if agent_answer.get("fallacy") and expected_answer["fallacy"]:
        if agent_answer["fallacy"].lower() in expected_answer["fallacy"].lower():
            score += 50  # 50 points for correct fallacy
    return score

def score_thinking_depth(analysis_text):
    """Score depth of reasoning (0-100)."""
    depth_indicators = [
        "premise", "conclusion", "therefore", "because",
        "this shows", "this indicates", "the logical form",
        "syllogism", "categorical", "conditional", "valid",
        "invalid", "fallacy", "counter-example", "verification"
    ]
    
    text_lower = analysis_text.lower()
    indicator_count = sum(1 for ind in depth_indicators if ind in text_lower)
    
    # Score based on depth indicators and length
    base_score = min(70, indicator_count * 10)
    length_bonus = min(30, len(text_lower) // 50)
    
    return base_score + length_bonus

def score_self_correction(trajectory):
    """Score self-correction behavior (0-100)."""
    correction_keywords = [
        "wait", "actually", "let me reconsider", "correction",
        "on second thought", "I need to revise", "that's not right",
        "let me verify", "checking again", "rethinking"
    ]
    
    if not trajectory:
        return 50  # Default score if no trajectory provided
    
    corrections = sum(1 for step in trajectory 
                     if any(kw in str(step).lower() for kw in correction_keywords))
    
    if corrections > 0:
        return min(100, 50 + corrections * 15)  # Bonus for self-correction
    return 50  # Baseline score

def score_verification(analysis_text):
    """Score verification behavior (0-100)."""
    verification_keywords = [
        "verification", "check", "counter-example", "counterexample",
        "verify", "confirm", "test", "alternative", "consider",
        "another way", "cross-check", "double-check"
    ]
    
    verification_count = sum(1 for kw in verification_keywords 
                           if kw in analysis_text.lower())
    
    if verification_count >= 2:
        return 100
    elif verification_count == 1:
        return 70
    else:
        return 30

def evaluate_agent_response(agent_response, trajectory=None):
    """
    Evaluate a complete agent response.
    
    Args:
        agent_response: dict with keys per argument (1-10)
        trajectory: optional list of reasoning steps for scoring
        
    Returns:
        dict with scores for each dimension and overall score
    """
    # Score classifications
    classification_scores = []
    for arg_num in range(1, 11):
        if str(arg_num) in agent_response:
            score = score_classification(
                agent_response[str(arg_num)],
                EXPECTED[arg_num]
            )
            classification_scores.append(score)
    
    # Average classification accuracy
    avg_classification = sum(classification_scores) / len(classification_scores) if classification_scores else 0
    
    # Extract analysis text for dimension scoring
    all_analysis = ""
    for arg_num in agent_response.values():
        if "analysis" in arg_num:
            all_analysis += arg_num["analysis"] + " "
    
    # Score dimensions
    thinking_depth = score_thinking_depth(all_analysis)
    self_correction = score_self_correction(trajectory)
    verification = score_verification(all_analysis)
    
    # Calculate weighted score
    overall_score = (
        0.17 * thinking_depth +
        0.17 * self_correction +
        0.14 * verification +
        0.52 * avg_classification  # Remaining weight to classification
    )
    
    return {
        "overall_score": round(overall_score, 2),
        "classification_accuracy": round(avg_classification, 2),
        "dimension_scores": {
            "thinking_depth": round(thinking_depth, 2),
            "self_correction": round(self_correction, 2),
            "verification": round(verification, 2)
        },
        "passed": overall_score >= 70  # Pass threshold
    }

def main():
    parser = argparse.ArgumentParser(description="Evaluate T013 benchmark responses")
    parser.add_argument("--response", required=True, help="JSON file with agent response")
    parser.add_argument("--trajectory", help="Optional JSON file with agent trajectory")
    args = parser.parse_args()
    
    # Load response
    with open(args.response) as f:
        agent_response = json.load(f)
    
    # Load trajectory if provided
    trajectory = None
    if args.trajectory:
        with open(args.trajectory) as f:
            trajectory = json.load(f)
    
    # Evaluate
    results = evaluate_agent_response(agent_response, trajectory)
    
    # Print results
    print(json.dumps(results, indent=2))
    
    # Exit with appropriate code
    exit(0 if results["passed"] else 1)

if __name__ == "__main__":
    main()
