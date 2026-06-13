from tools.docker_tools import *

from tools.k8s_tools import *


TOOL_REGISTRY = {

    # Docker
    "docker_ps": docker_ps,
    "docker_ps_all": docker_ps_all,
    "docker_logs": docker_logs,
    "inspect_container": inspect_container,
    "start_container": start_container,
    "stop_container": stop_container,
    "restart_container": restart_container,
    "remove_container": remove_container,
    "container_stats": container_stats,

    "docker_images": docker_images,
    "inspect_image": inspect_image,
    "remove_image": remove_image,
    "pull_image": pull_image,

    "docker_networks": docker_networks,
    "inspect_network": inspect_network,

    "docker_volumes": docker_volumes,
    "inspect_volume": inspect_volume,

    "docker_system_info": docker_system_info,
    "docker_version": docker_version,
    "docker_disk_usage": docker_disk_usage,


    # Kubernetes
    "get_pods": get_pods,
    "get_pods_default": get_pods_default,
    "describe_pod": describe_pod,
    "pod_logs": pod_logs,
    "delete_pod": delete_pod,

    "get_deployments": get_deployments,
    "describe_deployment": describe_deployment,
    "rollout_restart_deployment":
        rollout_restart_deployment,

    "get_services": get_services,
    "describe_service": describe_service,

    "get_nodes": get_nodes,
    "describe_node": describe_node,

    "get_namespaces": get_namespaces,

    "get_events": get_events,

    "cluster_info": cluster_info,
    "cluster_version": cluster_version
}