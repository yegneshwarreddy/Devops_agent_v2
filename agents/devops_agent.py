from langchain.agents import create_agent

from LLM.ollama_llm import llm

from tools.docker_tools import (
   
    docker_ps,
    docker_ps_all,
    docker_logs,
    inspect_container,
    start_container,
    stop_container,
    restart_container,
    remove_container,
    container_stats,
    docker_images,
    inspect_image,
    remove_image,
    pull_image,
    docker_networks,
    inspect_network,
    docker_volumes,
    inspect_volume,
    docker_system_info,
    docker_version,
    docker_disk_usage
)

from tools.k8s_tools import (
     get_pods,
    get_pods_default,
    describe_pod,
    pod_logs,
    delete_pod,

    get_deployments,
    describe_deployment,
    rollout_restart_deployment,

    get_services,
    describe_service,

    get_nodes,
    describe_node,

    get_namespaces,

    get_events,

    cluster_info,
    cluster_version

)

all_tools = [
    docker_ps,
    docker_ps_all,
    docker_logs,
    inspect_container,
    start_container,
    stop_container,
    restart_container,
    remove_container,
    container_stats,
    docker_images,
    inspect_image,
    remove_image,
    pull_image,
    docker_networks,
    inspect_network,
    docker_volumes,
    inspect_volume,
    docker_system_info,
    docker_version,
    docker_disk_usage,
     get_pods,
    get_pods_default,
    describe_pod,
    pod_logs,
    delete_pod,

    get_deployments,
    describe_deployment,
    rollout_restart_deployment,

    get_services,
    describe_service,

    get_nodes,
    describe_node,

    get_namespaces,

    get_events,

    cluster_info,
    cluster_version
]

agent = create_agent(
    model=llm,

    tools=all_tools,

    system_prompt="""
    You are an expert DevOps AI agent.

    Help users with:
    - Docker
    - Kubernetes
    - Container debugging
    - Logs
    - Deployments

    Use tools whenever required.
    """
)
