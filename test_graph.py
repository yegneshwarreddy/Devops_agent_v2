from graph.workflow import graph

result = graph.invoke(
    {
        "user_input": input("Enter your DevOps request: ")
    }
)

print(result["final_answer"])


# Save graph image

png_data = graph.get_graph().draw_mermaid_png()

with open("graph.png", "wb") as f:
    f.write(png_data)

print("\nGraph saved as graph.png")