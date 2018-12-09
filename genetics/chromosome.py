import random


class Chromosome(object):

    def __init__(self, graph):
        self._graph = graph
        self._fitness = 0
        self._genes = []

    def define_genes(self, nodes):
        invalid = True
        while invalid:
            invalid = False
            self._genes = random.sample(nodes, len(nodes))
            for index, gene in enumerate(self._genes[:-1]):
                if not (self._graph.verify_node_is_adjacent(gene, self._genes[index + 1])):
                    invalid = True
            if not (self._graph.verify_node_is_adjacent(self._genes[0], self._genes[-1])):
                invalid = True
        self._calculate_fitness()

    def _calculate_fitness(self):
        self._fitness = 0
        for index, gene in enumerate(self._genes[:-1]):
            self._fitness += self._value_of_link(gene, self._genes[index + 1])
        self._fitness += self._value_of_link(self._genes[-1], self._genes[0])

    def _value_of_link(self, start_node, final_node):
        node = self._graph.get_node_by_key(start_node)
        edges = node.get_edges()
        for edge in edges:
            if edge.get_destiny_node() == final_node:
                return edge.get_value()
        return 0

    def get_genes(self):
        return self._genes
    
    def set_genes(self, new_genes):
        self._genes = new_genes

    def get_fitness(self):
        return self._fitness
