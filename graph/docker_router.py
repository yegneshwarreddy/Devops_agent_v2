from LLM.ollama_llm import llm


def docker_router(state):

    question = state["user_input"]

    prompt = f"""
You are a Docker tool selector.

Available tools:

docker_ps
docker_ps_all
docker_logs
inspect_container
start_container
stop_container
restart_container
remove_container
container_stats

docker_images
inspect_image
remove_image
pull_image

docker_networks
inspect_network

docker_volumes
inspect_volume

docker_system_info
docker_version
docker_disk_usage
Return ONLY tool name.

Question:
{question}
"""

    response = llm.invoke(prompt)

    state["tool_name"] = (
        response.content.strip()
    )

    print(
        f"\n=== DOCKER TOOL ===\n"
        f"{state['tool_name']}"
    )

    return state