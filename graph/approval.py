DANGEROUS_TOOLS = {
    "remove_container",
    "remove_image",
    "delete_pod",
    "rollout_restart_deployment"
}


def approval_node(state):

    tool_name = state["tool_name"]

    state["approval_required"] = (
        tool_name in DANGEROUS_TOOLS
    )

    return state