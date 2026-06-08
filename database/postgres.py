import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="devops_agent_memory",
    user="postgres",
    password="12345678"
)

cursor = conn.cursor()

print("✅ PostgreSQL Connected")