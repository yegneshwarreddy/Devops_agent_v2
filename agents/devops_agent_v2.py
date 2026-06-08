from tools.docker_tools import docker_ps

##node 1
def docker_node(state):

    result = docker_ps.invoke({})

    state["tool_output"] = result

    return state

def response_node(state):

    state["final_answer"] = (
        f"Docker Output:\n\n"
        f"{state['tool_output']}"
    )

    return state