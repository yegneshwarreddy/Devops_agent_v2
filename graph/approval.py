from langgraph.types import interrupt


DANGEROUS_TOOLS = {
    "remove_container",
    "remove_image",
    "delete_pod",
    "rollout_restart_deployment"
}


def approval_node(state):

    tool_name = state["tool_name"]

    if tool_name in DANGEROUS_TOOLS:

        approval = interrupt(
            f"""
Approval Required

Tool:
{tool_name}

Arguments:
{state['tool_args']}

Type CONFIRM to continue.
"""
        )

        if approval.strip().lower() != "confirm":

            raise ValueError(
                "Operation not approved."
            )

    return state