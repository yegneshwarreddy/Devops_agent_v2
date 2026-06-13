from dotenv import load_dotenv

load_dotenv()

from langsmith import traceable
from LLM.ollama_llm import llm


@traceable
def test():

    return llm.invoke(
        "What is Docker?"
    )


response = test()

print(
    response.content
)