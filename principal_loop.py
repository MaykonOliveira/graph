from models.graph import Graph

graph = Graph(orientation=False)

graph.add_node("A", "xundas1")
graph.add_node("B", "xundas2")
graph.add_node("C", "xundas3")
graph.add_node("D", "xundas4")
graph.add_node("E", "xundas5")
graph.add_node("F", "xundas6")

graph.add_edge("1", "A", "B", "xundas")
graph.add_edge("2", "A", "C", "xundas")
graph.add_edge("4", "B", "C", "xundas")
graph.add_edge("5", "B", "D", "xundas")
graph.add_edge("6", "C", "E", "xundas")
graph.add_edge("7", "D", "E", "xundas")
graph.add_edge("8", "D", "F", "xundas")
graph.add_edge("8", "E", "F", "xundas")


graph.plot_graph()
