from typing import TypedDict


class AgentState(TypedDict):

    # User Request
    user_input: str

    # Planner Output
    route: str

    # Current Tool
    tool_name: str
    tool_args: dict

    # Approval
    approval_required: bool
    approved: bool

    # Single Tool Output
    tool_output: str

    # Final Response
    final_answer: str

    # ======================
    # Multi-Step Planning
    # ======================

    plan: list

    current_step: int

    step_results: list

    replan_decision: str

    replan_action: str

    new_plan: list