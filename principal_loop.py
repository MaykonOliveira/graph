from models.graph import Graph

graph = Graph()

graph.add_node("A", "xundas1")
graph.add_node("B", "xundas2")
graph.add_edge("SUM", "A", "B", "xundas")
graph.remove_edge("A", "B")


graph.verify_node_is_adjacent("A", "B")

#graph.plot_graph()
