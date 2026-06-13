from graph.argument_extractor import (
    argument_extractor_node
)

from evaluation.argument_dataset import (
    ARGUMENT_TEST_CASES
)

correct = 0

total = len(
    ARGUMENT_TEST_CASES
)

for case in ARGUMENT_TEST_CASES:

    state = {
        "user_input":
            case["question"],

        "tool_name":
            case["tool_name"]
    }

    state = argument_extractor_node(
        state
    )

    predicted_args = (
        state["tool_args"]
    )

    expected_args = (
        case["expected_args"]
    )

    if predicted_args == expected_args:

        correct += 1

        print(
            f"PASS: {case['question']}"
        )

    else:

        print(
            f"FAIL: {case['question']}"
        )

        print(
            f"Expected: {expected_args}"
        )

        print(
            f"Got: {predicted_args}"
        )

accuracy = (
    correct / total
) * 100

print(
    f"\nArgument Accuracy: {accuracy:.2f}%"
)