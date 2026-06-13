from evaluation.e2e_dataset import (
    E2E_TEST_CASES
)

from graph.planner_v2 import (
    planner_v2_node
)

from graph.plan_executor import (
    execute_plan_node
)

from graph.plan_response import (
    plan_response_node
)

success = 0

total = len(
    E2E_TEST_CASES
)

for case in E2E_TEST_CASES:

    print(
        f"\nTesting: {case['question']}"
    )

    state = {
        "user_input":
        case["question"]
    }

    try:

        state = planner_v2_node(
            state
        )

        state = execute_plan_node(
            state
        )

        state = plan_response_node(
            state
        )

        success += 1

        print(
            "PASS"
        )

    except Exception as e:

        print(
            f"FAIL: {str(e)}"
        )

success_rate = (
    success / total
) * 100

print(
    f"\nTask Success Rate: {success_rate:.2f}%"
)