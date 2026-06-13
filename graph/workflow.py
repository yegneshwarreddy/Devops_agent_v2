from langgraph.graph import (
    StateGraph,
    END
)

from graph.state import AgentState

from graph.nodes import (
    planner_node,
    response_node
)

from graph.docker_router import (
    docker_router
)

from graph.k8s_router import (
    k8s_router
)

from graph.argument_extractor import (
    argument_extractor_node
)

from graph.executor import (
    execute_tool_node
)

from graph.approval import (
    approval_node
)

from graph.checkpointer import (
    checkpointer
)


# ==================================
# GRAPH BUILDER
# ==================================

builder = StateGraph(
    AgentState
)


# ==================================
# NODES
# ==================================

builder.add_node(
    "planner",
    planner_node
)

builder.add_node(
    "docker_router",
    docker_router
)

builder.add_node(
    "k8s_router",
    k8s_router
)

builder.add_node(
    "argument_extractor",
    argument_extractor_node
)

builder.add_node(
    "approval_check",
    approval_node
)

builder.add_node(
    "executor",
    execute_tool_node
)

builder.add_node(
    "response",
    response_node
)


# ==================================
# ENTRY POINT
# ==================================

builder.set_entry_point(
    "planner"
)


# ==================================
# MAIN ROUTER
# ==================================

def route_decision(state):

    return state["route"]


# ==================================
# CONDITIONAL ROUTING
# ==================================

builder.add_conditional_edges(
    "planner",
    route_decision,
    {
        "docker": "docker_router",
        "kubernetes": "k8s_router"
    }
)


# ==================================
# NORMAL EDGES
# ==================================

builder.add_edge(
    "docker_router",
    "argument_extractor"
)

builder.add_edge(
    "k8s_router",
    "argument_extractor"
)

builder.add_edge(
    "argument_extractor",
    "approval_check"
)

builder.add_edge(
    "approval_check",
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


# ==================================
# COMPILE
# ==================================

graph = builder.compile(
    checkpointer=checkpointer
)