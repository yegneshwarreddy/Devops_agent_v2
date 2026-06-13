from graph.planner_v2 import (
    planner_v2_node
)

from evaluation.planner_dataset import (
    PLANNER_TEST_CASES
)

correct = 0

total = len(
    PLANNER_TEST_CASES
)

for case in PLANNER_TEST_CASES:

    state = {
        "user_input":
        case["question"]
    }

    state = planner_v2_node(
        state
    )

    predicted_tool = (
        state["plan"][0]["tool_name"]
    )

    expected_tool = (
        case["expected_tool"]
    )

    if predicted_tool == expected_tool:

        correct += 1

        print(
            f"PASS: {case['question']}"
        )

    else:

        print(
            f"FAIL: {case['question']}"
        )

        print(
            f"Expected: {expected_tool}"
        )

        print(
            f"Got: {predicted_tool}"
        )

accuracy = (
    correct / total
) * 100

print(
    f"\nPlanner Accuracy: {accuracy:.2f}%"
)