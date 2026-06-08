def print_memory(chat_history):

    print("\n========= MEMORY =========")

    for role, content in chat_history:

        print(f"\n[{role.upper()}]")
        print(content)

    print("\n==========================\n")