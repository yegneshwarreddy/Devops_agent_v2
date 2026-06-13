
from tools.docker_tools import docker_ps
from LLM.ollama_llm import llm
from tools.k8s_tools import get_pods
from graph.schemas import PlannerOutput

#node 1
def docker_node(state):

    result = docker_ps.invoke({})

    state["tool_output"] = result

    return state

def k8s_node(state):

    result = get_pods.invoke({})

    state["tool_output"] = result

    return state

def response_node(state):

    # Approval Required Case
    if state.get("approval_required"):

        state["final_answer"] = f"""
⚠️ Approval Required

Tool:
{state['tool_name']}

Arguments:
{state['tool_args']}

Type CONFIRM to continue.
"""

        return state

    # Normal Flow
    question = state["user_input"]

    tool_output = state["tool_output"]

    prompt = f"""
You are a DevOps AI Assistant.

User Request:
{question}

Tool Output:
{tool_output}

Your task:

1. Explain the result clearly.
2. If there is an error, explain the error.
3. Suggest next steps if applicable.
4. Keep response concise.

Answer:
"""

    print("\n=== Generating Response ===\n")

    response = llm.invoke(prompt)

    state["final_answer"] = response.content

    return state

##planner node

def planner_node(state):

    question = state["user_input"]

    prompt = f"""
You are a DevOps router.

Classify the user request into ONLY ONE category:

docker
kubernetes

Examples:

Show running containers -> docker
Restart nginx container -> docker
List docker images -> docker

Show pods -> kubernetes
Describe deployment -> kubernetes
Get pod logs -> kubernetes

Return ONLY:

docker

or

kubernetes

Question:
{question}
"""

    structured_llm = llm.with_structured_output(
        PlannerOutput
    )

    response = structured_llm.invoke(
        prompt
    )

    state["route"] = response.route

    print(
        f"\n=== PLANNER DECISION ===\n"
        f"{response.route}"
    )

    return state