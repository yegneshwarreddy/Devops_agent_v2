from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("LANGCHAIN_TRACING_V2"))
print(os.getenv("LANGCHAIN_PROJECT"))
print(os.getenv("LANGCHAIN_API_KEY")[:15])