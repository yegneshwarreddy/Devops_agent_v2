from memory.postgres_memory import (
    save_message,
    load_messages
)

SESSION_ID = "test_session"


save_message(
    SESSION_ID,
    "user",
    "Hello PostgreSQL Memory"
)

messages = load_messages(
    SESSION_ID
)

print(messages)