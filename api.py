from fastapi import FastAPI

from graph.planner_v2 import (
    planner_v2_node
)

from graph.plan_executor import (
    execute_plan_node
)

from graph.plan_response import (
    plan_response_node
)

app = FastAPI(
    title="SRECopilot API"
)


@app.get("/")
def health():

    return {
        "status": "healthy"
    }


@app.post("/chat")
def chat(request: dict):

    question = request["query"]

    state = {
        "user_input": question
    }

    state = planner_v2_node(
        state
    )

    state = execute_plan_node(
        state
    )

    state = plan_response_node(
        state
    )

    return {
        "answer":
            state["final_answer"]
    }