import json

from LLM.ollama_llm import llm


def argument_extractor_node(state):

    question = state["user_input"]

    tool_name = state["tool_name"]

    prompt = f"""
You are a DevOps argument extractor.

User Question:
{question}

Selected Tool:
{tool_name}

Return ONLY valid JSON.

Rules:

docker_logs
{{
    "container_name":"..."
}}

inspect_container
{{
    "container_name":"..."
}}

restart_container
{{
    "container_name":"..."
}}

start_container
{{
    "container_name":"..."
}}

stop_container
{{
    "container_name":"..."
}}

remove_container
{{
    "container_name":"..."
}}

inspect_image
{{
    "image_name":"..."
}}

pull_image
{{
    "image_name":"..."
}}

remove_image
{{
    "image_name":"..."
}}

describe_pod
{{
    "pod_name":"..."
}}

pod_logs
{{
    "pod_name":"..."
}}

delete_pod
{{
    "pod_name":"..."
}}

describe_node
{{
    "node_name":"..."
}}

describe_service
{{
    "service_name":"..."
}}

describe_deployment
{{
    "deployment_name":"..."
}}

If no arguments are needed return:

{{}}
"""

    response = llm.invoke(prompt)

    raw_output = response.content.strip()

    try:

        args = json.loads(
            raw_output
        )

    except Exception:

        print(
            "\n=== ARG PARSE FAILED ===\n"
        )

        args = {}

    state["tool_args"] = args

    print(
        f"\n=== TOOL ARGS ===\n"
        f"{args}"
    )

    return state