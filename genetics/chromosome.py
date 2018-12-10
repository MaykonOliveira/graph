import random


class Chromosome(object):

    def __init__(self, graph):
        self._graph = graph
        self._fitness = 0
        self._genes = []

    def define_genes(self, nodes):
        self._genes = random.sample(nodes, len(nodes))
        self.calculate_fitness()

    def calculate_fitness(self):
        self._fitness = 0
        for index, gene in enumerate(self._genes[:-1]):
            value = self._value_of_link(gene, self._genes[index + 1])
            self._fitness += value
            if value == float("inf"):
                return
        self._fitness += self._value_of_link(self._genes[-1], self._genes[0])

    def _value_of_link(self, start_node, final_node):
        node = self._graph.get_node_by_key(start_node)
        edges = node.get_edges()
        for edge in edges:
            if edge.get_destiny_node() == final_node:
                return edge.get_value()
        return float("inf")

    def get_genes(self):
        return self._genes
    
    def set_genes(self, new_genes):
        self._genes = new_genes

    def get_fitness(self):
        return self._fitness
        