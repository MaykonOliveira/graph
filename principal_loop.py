from models.Graph import Graph
from algorithms import SearchAlgorithms
from algorithms import ColorAlghoritms

graph = Graph(orientation=False)
color = ColorAlghoritms.Color()

############################### Three colors graph ###############################
graph.add_node("1", "xundas1")
graph.add_node("2", "xundas1")
graph.add_node("3", "xundas1")
graph.add_node("4", "xundas1")
graph.add_node("5", "xundas1")


graph.add_edge("1", "1", "2", 100)
graph.add_edge("2", "1", "3", 200)
graph.add_edge("3", "1", "4", 300)
graph.add_edge("4", "1", "5", 400)
graph.add_edge("5", "2", "3", 500)
graph.add_edge("6", "2", "4", 600)
graph.add_edge("7", "3", "5", 700)
graph.add_edge("8", "4", "5", 800)
##################################################################################


map = color.welsh_powell(graph)

graph.plot_graph(color_map=map)
