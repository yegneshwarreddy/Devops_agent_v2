from database.postgres import conn, cursor


def save_message(session_id, role, content):

    cursor.execute(
        """
        INSERT INTO chat_messages
        (session_id, role, content)
        VALUES (%s, %s, %s)
        """,
        (session_id, role, content)
    )

    conn.commit()


def load_messages(session_id):

    cursor.execute(
        """
        SELECT role, content
        FROM chat_messages
        WHERE session_id=%s
        ORDER BY created_at
        """,
        (session_id,)
    )

    return cursor.fetchall()

def create_session(session_id):
    """
    Create a session if it doesn't exist.
    """

    cursor.execute(
        """
        INSERT INTO sessions(session_id)
        VALUES (%s)
        ON CONFLICT DO NOTHING
        """,
        (session_id,)
    )
    conn.commit()