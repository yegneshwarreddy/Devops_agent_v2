from graph.tool_registry import TOOL_REGISTRY
from langsmith import traceable

@traceable(name="Executor")
def execute_plan_node(state):

    plan = state["plan"]

    results = []

    print("\n=== EXECUTING PLAN ===\n")

    for step in plan:

        tool_name = step["tool_name"]

        tool_args = step["arguments"]

        print(
            f"\nTool: {tool_name}"
        )

        print(
            f"Args: {tool_args}"
        )

        try:

            tool = TOOL_REGISTRY[
                tool_name
            ]

            result = tool.invoke(
                tool_args
            )

        except Exception as e:

            result = (
                f"ERROR: {str(e)}"
            )

        results.append(
            {
                "tool": tool_name,
                "result": result
            }
        )

    state["step_results"] = results

    return state