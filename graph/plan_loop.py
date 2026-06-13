from graph.plan_executor import (
    execute_plan_node
)

from graph.replanner_v2 import (
    replanner_v2_node
)


def execute_with_replanning(
    state,
    max_iterations=3
):

    for iteration in range(
        max_iterations
    ):

        print(
            f"\n=== ITERATION {iteration + 1} ===\n"
        )

        state = execute_plan_node(
            state
        )

        state = replanner_v2_node(
            state
        )

        if (
            state["replan_action"]
            == "complete"
        ):

            print(
                "\nTASK COMPLETE\n"
            )

            return state

        state["plan"] = (
            state["new_plan"]
        )

    return state