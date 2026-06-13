from dotenv import load_dotenv

load_dotenv()

from graph.planner_v2 import (
    planner_v2_node
)

from graph.plan_executor import (
    execute_plan_node
)

from graph.plan_response import (
    plan_response_node
)


def run_agent():

    print("\n=========================")
    print("SRECopilot")
    print("Autonomous DevOps AI Agent")
    print("=========================\n")

    while True:

        question = input(
            "\nAsk DevOps Agent: "
        )

        if question.lower() in [
            "exit",
            "quit"
        ]:
            print(
                "\nExiting SRECopilot..."
            )
            break

        state = {
            "user_input": question
        }

        try:

            state = planner_v2_node(
                state
            )

            state = execute_plan_node(
                state
            )

            state = plan_response_node(
                state
            )

            print(
                "\n=== ANSWER ===\n"
            )

            print(
                state["final_answer"]
            )

        except Exception as e:

            print(
                f"\nERROR: {str(e)}"
            )


if __name__ == "__main__":

    run_agent()