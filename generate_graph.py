from graph.workflow import graph

from IPython.display import Image

png_data = graph.get_graph().draw_mermaid_png()

with open(
    "graph.png",
    "wb"
) as f:

    f.write(
        png_data
    )

print(
    "Graph saved as graph.png"
)