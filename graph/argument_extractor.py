from LLM.ollama_llm import llm

from graph.schemas import (
    ToolArguments
)


def argument_extractor_node(state):

    question = state["user_input"]

    tool_name = state["tool_name"]

    prompt = f"""
You are a DevOps argument extractor.

User Question:
{question}

Selected Tool:
{tool_name}

Extract arguments for the selected tool.

Return arguments as structured data.

Examples:

docker_logs
container_identifier

inspect_container
container_identifier

restart_container
container_identifier

start_container
container_identifier

stop_container
container_identifier

remove_container
container_identifier

inspect_image
image_name

pull_image
image_name

remove_image
image_name

describe_pod
pod_name

pod_logs
pod_name

delete_pod
pod_name

describe_node
node_name

describe_service
service_name

describe_deployment
deployment_name

If no arguments are required,
return empty arguments.
IMPORTANT:

Return ONLY the arguments.

DO NOT wrap them inside the tool name.

Correct:

{{
    "container_identifier":"nginx"
}}

Incorrect:

{{
    "docker_logs":{{
        "container_identifier":"nginx"
    }}
}}

The selected tool has already been chosen.

Your ONLY task is to extract argument values.

If the selected tool is describe_deployment and the user says:

"describe deployment backend"

return:

{{
    "deployment_name":"backend"
}}
"""

    structured_llm = llm.with_structured_output(
        ToolArguments
    )

    response = structured_llm.invoke(
        prompt
    )

    state["tool_args"] = (
        response.arguments
    )
    if (
    len(state["tool_args"]) == 1
    and tool_name in state["tool_args"]
    ):
     state["tool_args"] = (
        state["tool_args"][tool_name]
    )

    print(
        f"\n=== TOOL ARGS ===\n"
        f"{state['tool_args']}"
    )

    return state