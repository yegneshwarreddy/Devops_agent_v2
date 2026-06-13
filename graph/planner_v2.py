from LLM.ollama_llm import llm
from langsmith import traceable

from graph.schemas import (
    Plan
)

@traceable(name="Planner")
def planner_v2_node(state):

    question = state["user_input"]

    prompt = f"""
You are a DevOps planning agent.

Your job is to create a sequence of tool calls
needed to satisfy the user's request.

IMPORTANT:

1. Use ONLY the tools listed below.
2. Use the EXACT argument names shown below.
3. Create multiple steps if required.
4. Return only the structured plan.

=========================
DOCKER TOOLS
=========================

docker_ps
Arguments: {{}}

docker_ps_all
Arguments: {{}}

docker_logs
Arguments:
{{
    "container_identifier": "..."
}}

inspect_container
Arguments:
{{
    "container_identifier": "..."
}}

start_container
Arguments:
{{
    "container_identifier": "..."
}}

stop_container
Arguments:
{{
    "container_identifier": "..."
}}

restart_container
Arguments:
{{
    "container_identifier": "..."
}}

remove_container
Arguments:
{{
    "container_identifier": "..."
}}

container_stats
Arguments: {{}}

docker_images
Arguments: {{}}

inspect_image
Arguments:
{{
    "image_name": "..."
}}

remove_image
Arguments:
{{
    "image_name": "..."
}}

pull_image
Arguments:
{{
    "image_name": "..."
}}

docker_networks
Arguments: {{}}

inspect_network
Arguments:
{{
    "network_name": "..."
}}

docker_volumes
Arguments: {{}}

inspect_volume
Arguments:
{{
    "volume_name": "..."
}}

docker_system_info
Arguments: {{}}

docker_version
Arguments: {{}}

docker_disk_usage
Arguments: {{}}

=========================
KUBERNETES TOOLS
=========================

get_pods
Arguments: {{}}

describe_pod
Arguments:
{{
    "pod_name": "..."
}}

pod_logs
Arguments:
{{
    "pod_name": "..."
}}

delete_pod
Arguments:
{{
    "pod_name": "..."
}}

get_deployments
Arguments: {{}}

describe_deployment
Arguments:
{{
    "deployment_name": "..."
}}

rollout_restart_deployment
Arguments:
{{
    "deployment_name": "..."
}}

get_services
Arguments: {{}}

describe_service
Arguments:
{{
    "service_name": "..."
}}

get_nodes
Arguments: {{}}

describe_node
Arguments:
{{
    "node_name": "..."
}}

cluster_info
Arguments: {{}}

cluster_version
Arguments: {{}}

=========================
EXAMPLES
=========================

User:
Restart nginx container

Plan:
[
    {{
        "tool_name": "restart_container",
        "arguments": {{
            "container_identifier": "nginx"
        }}
    }}
]

User:
Show running containers and restart nginx

Plan:
[
    {{
        "tool_name": "docker_ps",
        "arguments": {{}}
    }},
    {{
        "tool_name": "restart_container",
        "arguments": {{
            "container_identifier": "nginx"
        }}
    }}
]

=========================
USER REQUEST
=========================

{question}
"""

    structured_llm = llm.with_structured_output(
        Plan
    )

    response = structured_llm.invoke(
        prompt
    )

    state["plan"] = [
        step.model_dump()
        for step in response.steps
    ]

    state["current_step"] = 0

    state["step_results"] = []

    print("\n=== PLAN ===\n")

    for step in state["plan"]:
        print(step)

    return state