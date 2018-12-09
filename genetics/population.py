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
        new_chromossomes = []
        crossover_indexes = self._crossover_indexes(crossover_rate)

        for i in range(0,len(self._crossover_indexes),2):
            new_chromossomes.extend(self._crossover_function(crossover_indexes[i],crossover_indexes[i+1]))

        for index, _ in self._population:
            if index not in crossover_indexes:
                new_chromossomes.append(self._population[index])
        
        self._population = new_chromossomes


    def _crossover_function(self, chromosome_index_1, chromosome_index_2):
        chromosome_1 = self._population[chromosome_index_1]
        chromosome_2 = self._population[chromosome_index_2]

        new_chromosome_1 = copy.deepcopy(chromosome_1)
        new_chromosome_2 = copy.deepcopy(chromosome_2)

        slice_pos = random.randint(0,len(chromosome_1.get_genes() - 1))
        
        new_genes_1 = chromosome_1.get_genes()[slice_pos:] + chromosome_2.get_genes()[:slice_pos]
        new_genes_2 = chromosome_1.get_genes()[:slice_pos] + chromosome_2.get_genes()[slice_pos:] 
        
        new_chromosome_1.set_genes(new_genes_1)
        new_chromosome_2.set_genes(new_genes_2)

        return list(new_chromosome_1, new_chromosome_2)


    def _crossover_indexes(self, crossover_rate):
        cross_amount = round(self._population_size * crossover_rate)
        cross_index = []

        if (cross_amount % 2) != 0:
            cross_amount -= 1

        for i in range(cross_amount):
            new_sample_index = None
            
            while new_sample_index in cross_index
                new_sample_index = self._population.index(random.choice(self._population))
                
            cross_index.append(new_sample_index)

        return cross_index

    
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
