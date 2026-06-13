from LLM.ollama_llm import llm

from graph.schemas import ToolSelection


def k8s_router(state):

    question = state["user_input"]

    prompt = f"""
You are a Kubernetes tool selector.

Available tools:

get_pods
get_pods_default
describe_pod
pod_logs
delete_pod

get_deployments
describe_deployment
rollout_restart_deployment

get_services
describe_service

get_nodes
describe_node

get_namespaces

get_events

cluster_info
cluster_version

Return ONLY the tool name.

Question:
{question}
"""

    structured_llm = llm.with_structured_output(
        ToolSelection
    )

    response = structured_llm.invoke(
        prompt
    )

    state["tool_name"] = (
        response.tool_name
    )

    print(
        f"\n=== K8S TOOL ===\n"
        f"{state['tool_name']}"
    )

    return state