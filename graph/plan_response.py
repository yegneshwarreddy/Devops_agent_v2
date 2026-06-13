from LLM.ollama_llm import llm
from langsmith import traceable


@traceable(name="ResponseGenerator")
def plan_response_node(state):

    question = state["user_input"]

    results = state["step_results"]

    prompt = f"""
You are a DevOps AI assistant.

User Request:

{question}

Execution Results:

{results}

Explain:

1. What actions were executed.
2. Which actions succeeded.
3. Which actions failed.
4. Suggested next steps.

Keep response concise.
"""

    response = llm.invoke(
        prompt
    )

    state["final_answer"] = (
        response.content
    )

    return state