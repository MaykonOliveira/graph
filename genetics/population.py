from genetics.chromosome import Chromosome

import signal


class Population(object):

    def __init__(self, graph, population_size=100):
        self._graph = graph
        self._population = []
        self._population_size = population_size

    def generate_initial_population(self):

        def timeout(signum, frame):
            raise Exception()

        signal.signal(signal.SIGALRM, timeout)
        signal.alarm(1)
        nodes = [node.get_key() for node in self._graph.get_nodes()]
        for i in range(self._population_size):
            new_chromosome = Chromosome(self._graph)
            exist = True
            try:
                while exist:
                    new_chromosome.define_genes(nodes)
                    if not self._is_in_population(new_chromosome):
                        exist = False
            except Exception:
                break
            self._population.append(new_chromosome)

    def _is_in_population(self, new_chromosome):
        for chromosome in self._population:
            if chromosome.get_genes() == new_chromosome.get_genes():
                return True
        return False

    def get_population(self):
        return self._population
