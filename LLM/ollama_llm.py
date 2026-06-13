from dotenv import load_dotenv

from langchain_ollama import (
    ChatOllama
)

load_dotenv()

llm = ChatOllama(
    model="qwen3",
    temperature=0
)