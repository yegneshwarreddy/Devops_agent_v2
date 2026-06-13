from graph.workflow_v3 import graph


config = {
    "configurable": {
        "thread_id": "planner-thread"
    }
}


question = input(
    "Enter Request: "
)

result = graph.invoke(
    {
        "user_input": question
    },
    config=config
)

print(
    "\nAnswer:\n"
)

print(
    result["final_answer"]
)