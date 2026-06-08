from graph.tool_registry import TOOLS


def execute_tool_node(state):

    tool_name = state["tool_name"]

    tool_args = state.get(
        "tool_args",
        {}
    )

    print(
        f"\n=== EXECUTING TOOL ===\n"
        f"{tool_name}\n"
        f"{tool_args}"
    )

    tool = TOOLS.get(
        tool_name
    )

    if tool is None:

        state["tool_output"] = (
            f"Tool Not Found: {tool_name}"
        )

        return state

    try:

        result = tool.invoke(
            tool_args
        )

        state["tool_output"] = result

    except Exception as e:

        state["tool_output"] = (
            f"Execution Error:\n{str(e)}"
        )

    return state