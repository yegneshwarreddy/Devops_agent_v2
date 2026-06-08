from typing import TypedDict

class AgentState(TypedDict):

    user_input: str

    route: str             #planner 1 o/p

    tool_name: str         # router o/p (devops or k8s router)

    tool_args: dict 

    approval_required: bool

    approved: bool
      

    tool_output: str       # node o/p (function op)

    final_answer: str       # llm answer