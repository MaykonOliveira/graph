from genetics.chromosome import Chromosome

import random
import copy
import operator
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

    def elitist_selection(self, elitist_treshold=0.75):
        selected_population = []
        
        for i in range(self._population_size):
            r = round(random.uniform(0, 1.0), 2)
            sample_1,sample_2 = None, None

            while sample_1 == sample_2:
                sample_1 = random.choice(self._population)
                sample_2 = random.choice(self._population)

            if r =< elitist_treshold:
                #choose best
                survivor = min((sample_1,sample_2), key=operator.methodcaller('get_fitness'))
            else:
                #choose worst
                survivor = max((sample_1,sample_2), key=operator.methodcaller('get_fitness'))

            selected_population.append(copy.deepcopy(survivor))
        
        self._population = selected_population
    

    def crossover(self, crossover_rate=0.60):
        pass

    
    def mutation(self, mutation_rate=0.01):
        for chromosome in self._population:
            for index, gene in enumerate(chromosome.get_genes()):
                r = round(random.uniform(0, 100.0), 3)
                rand_gene_index = None

                if r <= mutation_rate:
                    while rand_gene_index == index:
                        rand_gene_index = random.randint(0, len(chromosome.get_genes())

                    self._swap(gene[index], gene[rand_gene_index]) 


    def _swap(item_1, item_2):
        item_1, item_2 = item_2, item_1
