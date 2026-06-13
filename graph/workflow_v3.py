from langgraph.graph import (
    StateGraph,
    END
)

from graph.state import AgentState

from graph.planner_v2 import (
    planner_v2_node
)

from graph.plan_executor import (
    execute_plan_node
)

from graph.plan_response import (
    plan_response_node
)

from graph.checkpointer import (
    checkpointer
)


# ==========================
# GRAPH BUILDER
# ==========================

builder = StateGraph(
    AgentState
)


# ==========================
# NODES
# ==========================

builder.add_node(
    "planner",
    planner_v2_node
)

builder.add_node(
    "executor",
    execute_plan_node
)

builder.add_node(
    "response",
    plan_response_node
)


# ==========================
# ENTRY POINT
# ==========================

builder.set_entry_point(
    "planner"
)


# ==========================
# EDGES
# ==========================

builder.add_edge(
    "planner",
    "executor"
)

builder.add_edge(
    "executor",
    "response"
)

builder.add_edge(
    "response",
    END
)


# ==========================
# COMPILE
# ==========================

graph = builder.compile(
    checkpointer=checkpointer
)