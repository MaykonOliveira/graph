from models.graph import Graph

graph = Graph(orientation=True)

graph.add_node("A", "xundas1")
graph.add_node("B", "xundas2")
graph.add_edge("SUM", "A", "B", "xundas")

graph.plot_graph()
