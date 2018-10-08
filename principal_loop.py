from models.Graph import Graph
from algorithms import SearchAlgorithms
from algorithms import ColorAlghoritms

graph = Graph(orientation=False)
color = ColorAlghoritms.Color()

# graph.add_node("A", "xundas1")
# graph.add_node("B", "xundas2")
# graph.add_node("C", "xundas3")
# graph.add_node("D", "xundas4")
# graph.add_node("E", "xundas5")
# graph.add_node("F", "xundas6")
#
# graph.add_edge("1", "A", "B", "xundas")
# graph.add_edge("2", "A", "C", "xundas")
# graph.add_edge("4", "B", "C", "xundas")
# graph.add_edge("5", "B", "D", "xundas")
# graph.add_edge("6", "C", "E", "xundas")
# graph.add_edge("7", "D", "E", "xundas")
# graph.add_edge("8", "D", "F", "xundas")
# graph.add_edge("9", "E", "F", "xundas")

graph.add_node("1", "xundas1")
graph.add_node("2", "xundas1")
graph.add_node("3", "xundas1")
graph.add_node("4", "xundas1")
graph.add_node("5", "xundas1")
graph.add_node("6", "xundas1")
graph.add_node("7", "xundas1")
graph.add_node("8", "xundas1")
graph.add_node("9", "xundas1")

graph.add_edge("1", "1", "2", "xundas")
graph.add_edge("2", "1", "3", "xundas")
graph.add_edge("3", "2", "4", "xundas")
graph.add_edge("4", "3", "4", "xundas")
graph.add_edge("5", "3", "5", "xundas")
graph.add_edge("6", "4", "6", "xundas")
graph.add_edge("7", "4", "7", "xundas")
graph.add_edge("8", "5", "7", "xundas")
graph.add_edge("9", "6", "8", "xundas")
graph.add_edge("10", "7", "8", "xundas")
graph.add_edge("11", "7", "9", "xundas")

map = color.welshPowell(graph.get_graph())

graph.plot_graph(col_val=map)
