import numpy as np


class Floyd(object):

    def __init__(self, graph, debug=False):
        self.__debug = debug
        self.__graph = graph
        self.__nodes = self.__graph.get_nodes()
        self.__cost_matrix = self.__new_cost_matrix()
        self.__predecessors_matrix =  self.__predecessors_matrix()

        if debug:
            self.__debug_log()

    def run(self):
        old_cost_matrix = self.__cost_matrix
        old_predecessors_matrix = self.__predecessors_matrix 

        new_cost_matrix = None
        new_predecessors_matrix = None

        for k in range(len(self.__graph.get_nodes())):
            new_cost_matrix = np.zeros((len(self.__nodes), len(self.__nodes)))
            new_predecessors_matrix = np.zeros((len(self.__nodes), len(self.__nodes)))

            for i in range(len(self.__nodes)):
                for j in range(len(self.__nodes)):
                    new_cost_matrix[i][j] = min(old_cost_matrix[i][j],(old_cost_matrix[i][k]+old_cost_matrix[k][j]))
            
            for i in range(len(self.__nodes)):
                for j in range(len(self.__nodes)):
                    if new_cost_matrix[i][j] != old_cost_matrix[i][j]:
                        new_predecessors_matrix[i][j] = old_predecessors_matrix[k][j]
                    else:
                        new_predecessors_matrix[i][j] = old_predecessors_matrix[i][j]
            
            old_predecessors_matrix = new_predecessors_matrix
            old_cost_matrix = new_cost_matrix

            if self.__debug:
                print("Passo: " + str(k+1))
                print(15 * '-' + "Matriz de Custos" + 15 * '-')
                print(new_cost_matrix)
                print(15 * '-' + "Matriz de Predecessores" + 15 * '-')
                print(new_predecessors_matrix)
                input("Press any key to continue")

    def __debug_log(self):
        print(30 * '*' + "Debug Activated" + 30 * '*')
        input("Press any key to continue")

        print(15 * '-' + "Lista de Nodos" + 15 * '-')
        for index, node in enumerate(self.__nodes):
            print("Node {}: {}".format(index, node.get_key()))
        input("Press any key to continue")
        
        print(15 * '-' + "Matriz de Custos" + 15 * '-')
        print(self.__cost_matrix)
        input("Press any key to continue")

        print(15 * '-' + "Matriz de Predecessores" + 15 * '-')
        print(self.__predecessors_matrix)
        input("Press any key to continue")


    def __new_cost_matrix(self):
        cost_matrix = np.zeros((len(self.__nodes), len(self.__nodes)))

        for i in range(len(self.__nodes)):
            for j in range(len(self.__nodes)):
                edge = self.__graph.exist_edge(self.__nodes[i].get_key(), self.__nodes[j].get_key())

                if i == j:
                    pass
                elif edge:
                    cost_matrix[i][j] = edge.get_value()
                else:
                    cost_matrix[i][j] = float("inf")

        return cost_matrix

    def __predecessors_matrix(self):
        predecessors_matrix = np.zeros((len(self.__nodes), len(self.__nodes)))

        for i in range(len(self.__nodes)):
            for j in range(len(self.__nodes)):
                if i != j:
                    predecessors_matrix[i][j] = i+1
                else:
                    predecessors_matrix[i][j] = 0

        return predecessors_matrix
