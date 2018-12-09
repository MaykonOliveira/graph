from models.Graph import Graph
from genetics.population import Population

graph = Graph(orientation=False)

graph.add_node("E", None)
graph.add_node("F", None)
graph.add_node("G", None)
graph.add_node("H", None)
graph.add_node("K", None)
graph.add_node("L", None)
graph.add_node("N", None)

graph.add_edge("1", "E", "K", 10)
graph.add_edge("2", "E", "F", 10)
graph.add_edge("3", "E", "L", 5)
graph.add_edge("4", "E", "H", 60)
graph.add_edge("5", "E", "G", 40)


graph.add_edge("6", "F", "N", 47)
graph.add_edge("7", "F", "K", 70)
graph.add_edge("8", "F", "H", 30)
graph.add_edge("9", "F", "L", 10)


graph.add_edge("10", "L", "H", 40)

graph.add_edge("11", "H", "K", 73)
graph.add_edge("12", "H", "G", 80)

graph.add_edge("13", "G", "K", 90)

graph.add_edge("14", "K", "N", 60)

population = Population(graph)

population.generate_initial_population()

for chromosomo in population.get_population():
    if chromosomo.get_genes()[0] == "G":
        print(chromosomo.get_genes(), chromosomo.get_fitness())

