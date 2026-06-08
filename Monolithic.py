# import subprocess
# from langchain_ollama import ChatOllama
# from langchain_core.tools import tool
# from langchain.agents import create_agent

# #LLM calling
# llm=ChatOllama(
#     model="llama3",
#     temperature=0,
#     system_prompt=""
# )


# #tool
# @tool
# def get_pods():
#     """
#     list the pods of running kubernetes cluster
#     """
#     result=subprocess.run(["kubectl","get","pods","-A"],capture_output=True,text=True)
#     return result.stdout

# print(get_pods())

# @tool
# def get_dockerimages():
#     """
#     list the docker container running in machine
#     """
#     result=subprocess.run(["docker","ps"],capture_output=True,text=True)
#     return result.stdout
# print(get_dockerimages())



# #agent
# agent=create_agent(
#     model=llm,
#     tools=[get_dockerimages,get_pods]
#     system_prompt="you are a helpful agent that can help in docker and kubernetes tasks using the tools get_pods,get_dockerimages"
# )

# question=input("ASK YOUR devops agent a Question:>")
# response=agent.invoke({"messages":[("user",question)]})
# print(response["messages"][-1])

