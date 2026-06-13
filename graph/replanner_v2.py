from LLM.ollama_llm import llm

from graph.schemas import (
    ReplanOutput
)
from langsmith import traceable

@traceable(name="Replanner")
def replanner_v2_node(state):

    question = state["user_input"]

    results = state["step_results"]

    prompt = f"""
You are a DevOps replanner.

Original Request:

{question}

Execution Results:

{results}

AVAILABLE TOOLS:

docker_ps
Arguments: {{}}

docker_ps_all
Arguments: {{}}

docker_logs
Arguments:
{{
    "container_identifier":"..."
}}

inspect_container
Arguments:
{{
    "container_identifier":"..."
}}

start_container
Arguments:
{{
    "container_identifier":"..."
}}

stop_container
Arguments:
{{
    "container_identifier":"..."
}}

restart_container
Arguments:
{{
    "container_identifier":"..."
}}

remove_container
Arguments:
{{
    "container_identifier":"..."
}}

docker_images
Arguments: {{}}

inspect_image
Arguments:
{{
    "image_name":"..."
}}

remove_image
Arguments:
{{
    "image_name":"..."
}}

pull_image
Arguments:
{{
    "image_name":"..."
}}

IMPORTANT:

1. Use ONLY the tools listed above.
2. Use ONLY the argument names shown above.
3. Never use:
   - container_name
   - container_id
4. Always use:
   - container_identifier

If the task is completed:

action = complete

new_plan = []

If more actions are needed:

action = replan

Generate a new plan.
"""

    structured_llm = llm.with_structured_output(
        ReplanOutput
    )

    response = structured_llm.invoke(
        prompt
    )

    state["replan_action"] = response.action

    state["new_plan"] = [
        step.model_dump()
        for step in response.new_plan
    ]

    print("\n=== REPLANNER V2 ===\n")

    print(
        f"Action: {response.action}"
    )

    print(
        f"Plan: {state['new_plan']}"
    )

    return state