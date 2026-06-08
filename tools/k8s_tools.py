from langchain_core.tools import tool
from utils.command_runner import run_command


# ==========================
# PODS
# ==========================

@tool
def get_pods():
    """
    List all Kubernetes pods across all namespaces.
    """
    print("\n=== TOOL EXECUTED: get_pods ===\n")
    return run_command(
        ["kubectl", "get", "pods", "-A"]
    )


@tool
def get_pods_default():
    """
    List pods in the default namespace.
    """
    print("\n=== TOOL EXECUTED: get_pods_default ===\n")
    return run_command(
        ["kubectl", "get", "pods"]
    )


@tool
def describe_pod(pod_name: str):
    """
    Describe a Kubernetes pod.
    """
    print("\n=== TOOL EXECUTED: describe_pod ===\n")
    return run_command(
        ["kubectl", "describe", "pod", pod_name]
    )


@tool
def pod_logs(pod_name: str):
    """
    Get logs from a Kubernetes pod.
    """
    print("\n=== TOOL EXECUTED: pod_logs ===\n")
    return run_command(
        ["kubectl", "logs", pod_name]
    )


@tool
def delete_pod(pod_name: str):
    """
    Delete a Kubernetes pod.
    """
    print("\n=== TOOL EXECUTED: delete_pod ===\n")
    return run_command(
        ["kubectl", "delete", "pod", pod_name]
    )


# ==========================
# DEPLOYMENTS
# ==========================

@tool
def get_deployments():
    """
    List all deployments across all namespaces.
    """
    print("\n=== TOOL EXECUTED: get_deployments ===\n")
    return run_command(
        ["kubectl", "get", "deployments", "-A"]
    )


@tool
def describe_deployment(deployment_name: str):
    """
    Describe a Kubernetes deployment.
    """
    print("\n=== TOOL EXECUTED: describe_deployment ===\n")
    return run_command(
        ["kubectl", "describe", "deployment", deployment_name]
    )


@tool
def rollout_restart_deployment(deployment_name: str):
    """
    Restart a deployment using rollout restart.
    """
    print("\n=== TOOL EXECUTED: rollout_restart_deployment ===\n")
    return run_command(
        [
            "kubectl",
            "rollout",
            "restart",
            f"deployment/{deployment_name}"
        ]
    )


# ==========================
# SERVICES
# ==========================

@tool
def get_services():
    """
    List all services.
    """
    print("\n=== TOOL EXECUTED: get_services ===\n")
    return run_command(
        ["kubectl", "get", "svc", "-A"]
    )


@tool
def describe_service(service_name: str):
    """
    Describe a Kubernetes service.
    """
    print("\n=== TOOL EXECUTED: describe_service ===\n")
    return run_command(
        ["kubectl", "describe", "service", service_name]
    )


# ==========================
# NODES
# ==========================

@tool
def get_nodes():
    """
    List Kubernetes nodes.
    """
    print("\n=== TOOL EXECUTED: get_nodes ===\n")
    return run_command(
        ["kubectl", "get", "nodes"]
    )


@tool
def describe_node(node_name: str):
    """
    Describe a Kubernetes node.
    """
    print("\n=== TOOL EXECUTED: describe_node ===\n")
    return run_command(
        ["kubectl", "describe", "node", node_name]
    )


# ==========================
# NAMESPACES
# ==========================

@tool
def get_namespaces():
    """
    List all namespaces.
    """
    print("\n=== TOOL EXECUTED: get_namespaces ===\n")
    return run_command(
        ["kubectl", "get", "namespaces"]
    )


# ==========================
# EVENTS
# ==========================

@tool
def get_events():
    """
    Get recent Kubernetes events.
    """
    print("\n=== TOOL EXECUTED: get_events ===\n")
    return run_command(
        ["kubectl", "get", "events", "-A"]
    )


# ==========================
# CLUSTER INFO
# ==========================

@tool
def cluster_info():
    """
    Get Kubernetes cluster information.
    """
    print("\n=== TOOL EXECUTED: cluster_info ===\n")
    return run_command(
        ["kubectl", "cluster-info"]
    )


@tool
def cluster_version():
    """
    Get Kubernetes cluster version.
    """
    print("\n=== TOOL EXECUTED: cluster_version ===\n")
    return run_command(
        ["kubectl", "version"]
    )