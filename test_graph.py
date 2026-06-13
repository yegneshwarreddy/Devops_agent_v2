from graph.workflow import graph
from langgraph.types import Command


config = {
    "configurable": {
        "thread_id": "devops-thread"
    }
}


question = input(
    "Enter your DevOps request: "
)

result = graph.invoke(
    {
        "user_input": question
    },
    config=config
)


if "__interrupt__" in result:

    interrupt_data = result["__interrupt__"][0]

    print(
        interrupt_data.value
    )

    approval = input(
        "\nApproval: "
    )

    result = graph.invoke(
        Command(
            resume=approval
        ),
        config=config
    )

print(
    "\nAnswer:\n"
)

print(
    result["final_answer"]
)