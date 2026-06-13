from LLM.ollama_llm import llm


def replanner_node(state):

    question = state["user_input"]

    results = state["step_results"]

    prompt = f"""
You are a DevOps replanner.

Original User Request:

{question}

Execution Results:

{results}

Determine:

1. Is the task complete?

If complete:

Return:

COMPLETE

If not complete:

Return:

REPLAN

and explain what should happen next.
"""

    response = llm.invoke(
        prompt
    )

    decision = (
        response.content.strip()
    )

    print(
        "\n=== REPLANNER ===\n"
    )

    print(
        decision
    )

    state["replan_decision"] = (
        decision
    )

    return state