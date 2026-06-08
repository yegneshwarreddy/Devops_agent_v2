from langchain_core.tools import tool
from utils.command_runner import run_command


# ==========================
# CONTAINERS
# ==========================

@tool
def docker_ps():
    """
    List running docker containers.
    """
    print("\n=== TOOL EXECUTED: docker_ps ===\n")
    return run_command(["docker", "ps"])


@tool
def docker_ps_all():
    """
    List all docker containers including stopped containers.
    """
    print("\n=== TOOL EXECUTED: docker_ps_all ===\n")
    return run_command(["docker", "ps", "-a"])


@tool
def docker_logs(container_name: str):
    """
    Get logs of a docker container.
    """
    print("\n=== TOOL EXECUTED: docker_logs ===\n")
    return run_command(["docker", "logs", container_name])


@tool
def inspect_container(container_name: str):
    """
    Inspect a docker container.
    """
    print("\n=== TOOL EXECUTED: inspect_container ===\n")
    return run_command(["docker", "inspect", container_name])


@tool
def start_container(container_name: str):
    """
    Start a stopped container.
    """
    print("\n=== TOOL EXECUTED: start_container ===\n")
    return run_command(["docker", "start", container_name])


@tool
def stop_container(container_name: str):
    """
    Stop a running container.
    """
    print("\n=== TOOL EXECUTED: stop_container ===\n")
    return run_command(["docker", "stop", container_name])


@tool
def restart_container(container_name: str):
    """
    Restart a container.
    """
    print("\n=== TOOL EXECUTED: restart_container ===\n")
    return run_command(["docker", "restart", container_name])


@tool
def remove_container(container_name: str):
    """
    Remove a container.
    """
    print("\n=== TOOL EXECUTED: remove_container ===\n")
    return run_command(["docker", "rm", container_name])


@tool
def container_stats():
    """
    Show resource usage of running containers.
    """
    print("\n=== TOOL EXECUTED: container_stats ===\n")
    return run_command(["docker", "stats", "--no-stream"])


# ==========================
# IMAGES
# ==========================

@tool
def docker_images():
    """
    List docker images available on the machine.
    """
    print("\n=== TOOL EXECUTED: docker_images ===\n")
    return run_command(["docker", "images"])


@tool
def inspect_image(image_name: str):
    """
    Inspect a docker image.
    """
    print("\n=== TOOL EXECUTED: inspect_image ===\n")
    return run_command(["docker", "image", "inspect", image_name])


@tool
def remove_image(image_name: str):
    """
    Remove a docker image.
    """
    print("\n=== TOOL EXECUTED: remove_image ===\n")
    return run_command(["docker", "rmi", image_name])


@tool
def pull_image(image_name: str):
    """
    Pull an image from Docker Hub.
    """
    print("\n=== TOOL EXECUTED: pull_image ===\n")
    return run_command(["docker", "pull", image_name])


# ==========================
# NETWORKS
# ==========================

@tool
def docker_networks():
    """
    List docker networks.
    """
    print("\n=== TOOL EXECUTED: docker_networks ===\n")
    return run_command(["docker", "network", "ls"])


@tool
def inspect_network(network_name: str):
    """
    Inspect a docker network.
    """
    print("\n=== TOOL EXECUTED: inspect_network ===\n")
    return run_command(["docker", "network", "inspect", network_name])


# ==========================
# VOLUMES
# ==========================

@tool
def docker_volumes():
    """
    List docker volumes.
    """
    print("\n=== TOOL EXECUTED: docker_volumes ===\n")
    return run_command(["docker", "volume", "ls"])


@tool
def inspect_volume(volume_name: str):
    """
    Inspect a docker volume.
    """
    print("\n=== TOOL EXECUTED: inspect_volume ===\n")
    return run_command(["docker", "volume", "inspect", volume_name])


# ==========================
# SYSTEM
# ==========================

@tool
def docker_system_info():
    """
    Show docker system information.
    """
    print("\n=== TOOL EXECUTED: docker_system_info ===\n")
    return run_command(["docker", "info"])


@tool
def docker_version():
    """
    Show docker version.
    """
    print("\n=== TOOL EXECUTED: docker_version ===\n")
    return run_command(["docker", "version"])


@tool
def docker_disk_usage():
    """
    Show docker disk usage.
    """
    print("\n=== TOOL EXECUTED: docker_disk_usage ===\n")
    return run_command(["docker", "system", "df"])