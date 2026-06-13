from pydantic import BaseModel, Field
from typing import Any, Dict, List

class PlannerOutput(BaseModel):

    route: str

class ToolSelection(BaseModel):

    tool_name: str

class ToolArguments(BaseModel):

    arguments: Dict[str, Any] = Field(
        default_factory=dict
    )
# class DockerToolOutput(BaseModel):

#     tool_name: str

# from typing import List


from typing import Literal

class PlanStep(BaseModel):

    tool_name: Literal[
        "docker_ps",
        "docker_ps_all",
        "docker_logs",
        "inspect_container",
        "start_container",
        "stop_container",
        "restart_container",
        "remove_container",
        "container_stats",
        "docker_images",
        "inspect_image",
        "remove_image",
        "pull_image",
        "get_pods",
        "describe_pod",
        "pod_logs",
        "delete_pod",
        "get_deployments",
        "describe_deployment",
        "rollout_restart_deployment"
    ]

    arguments: Dict[str, Any] = Field(
        default_factory=dict
    )

class Plan(BaseModel):

    steps: List[PlanStep]


class ReplanOutput(BaseModel):

    action: str

    new_plan: List[PlanStep] = Field(
        default_factory=list
    )