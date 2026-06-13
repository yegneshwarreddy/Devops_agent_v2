from graph.planner_v2 import (
    planner_v2_node
)

state = {
    "user_input":
    "show running containers and restart nginx"
}

result = planner_v2_node(
    state
)

print(
    result["plan"]
)