from agents.devops_agent import agent

from memory.postgres_memory import (
    save_message,
    load_messages,
    create_session
)

from utils.memory_debugger import print_memory


import uuid

SESSION_ID = str(uuid.uuid4())
create_session(
    SESSION_ID
)

EXIT_COMMANDS = {
    "exit",
    "quit",
    "bye",
    "goodbye",
    "stop"
}


print("\n🚀 DevOps Agent Started")
print("Type 'exit', 'quit', or 'bye' to stop.\n")


while True:

    question = input("Ask: ")

    # Exit
    if question.strip().lower() in EXIT_COMMANDS:
        print("\n👋 Shutting down DevOps Agent...")
        break

    # Save user message to PostgreSQL
    save_message(
        SESSION_ID,
        "user",
        question
    )
    

    # Load complete history from PostgreSQL
    chat_history = load_messages(
        SESSION_ID
    )

    print_memory(chat_history)

    response = agent.invoke({
        "messages": chat_history
    })

    ai_response = response["messages"][-1].content

    print(ai_response)

    # Save assistant response
    save_message(
        SESSION_ID,
        "assistant",
        ai_response
    )