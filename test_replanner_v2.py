from graph.planner_v2 import (
    planner_v2_node
)

from graph.plan_executor import (
    execute_plan_node
)

from graph.replanner_v2 import (
    replanner_v2_node
)

state = {

    "user_input":
    "show running containers and restart nginx"

}

state = planner_v2_node(
    state
)

state = execute_plan_node(
    state
)

state = replanner_v2_node(
    state
)