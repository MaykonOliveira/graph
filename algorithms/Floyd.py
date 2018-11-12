import numpy as np


class Floyd(object):

    def __init__(self, graph, debug=False):
        self.__debug = debug
        self.__graph = graph
        self.__nodes = self.__graph.get_nodes()
        self.__cost_matrix = self.__new_cost_matrix()
        self.__predecessors_matrix =  self.__predecessors_matrix()

        self.__final_cost_matrix = None
        self.__final_predecessors_matrix = None

        if debug:
            self.__debug_log()

        self.__run(self.__debug)

    def minimum_distance(self, node_1_key, node_2_key):
        node_1_index = None
        node_2_index = None

        for index, node in enumerate(self.__nodes):
            if node.get_key() == node_1_key:
                node_1_index = index
            if node.get_key() == node_2_key:
                node_2_index = index
                
        return self.__final_cost_matrix[node_1_index][node_2_index]

    def minimum_path(self, node_1_key, node_2_key):
        node_1_index = None
        node_2_index = None
        current_node_index = None
        minimum_path = []

        for index, node in enumerate(self.__nodes):
            if node.get_key() == node_1_key:
                node_1_index = index
            if node.get_key() == node_2_key:
                node_2_index = index

        current_node_index = int(self.__final_predecessors_matrix[node_1_index][node_2_index] - 1)
        minimum_path.append(node_2_index + 1)
        minimum_path.append(current_node_index + 1)                

        while (current_node_index != node_1_index ):
            current_node_index = int(self.__final_predecessors_matrix[node_1_index][current_node_index] - 1)
            minimum_path.append(current_node_index + 1)

        return minimum_path

    def __run(self, debug):
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
            
            old_cost_matrix = new_cost_matrix
            old_predecessors_matrix = new_predecessors_matrix

            if debug:
                print("Step: " + str(k+1))
                print(15 * '-' + "Cost Matrix" + 15 * '-')
                print(new_cost_matrix)
                print(15 * '-' + "Predecessor Matrix" + 15 * '-')
                print(new_predecessors_matrix)
                input("Press any key to continue")

        self.__final_cost_matrix = new_cost_matrix
        self.__final_predecessors_matrix = new_predecessors_matrix

    def __debug_log(self):
        print(30 * '*' + "Debug Activated" + 30 * '*')
        input("Press any key to continue")

        print(15 * '-' + "Node List" + 15 * '-')
        for index, node in enumerate(self.__nodes):
            print("Node {}: {}".format(index, node.get_key()))
        input("Press any key to continue")
        
        print(15 * '-' + "Cost Matrix" + 15 * '-')
        print(self.__cost_matrix)
        input("Press any key to continue")

        print(15 * '-' + "Predecessor Matrix" + 15 * '-')
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
        predecessors_matrix = np.zeros((len(self.__nodes), len(self.__nodes)), dtype=int)

        for i in range(len(self.__nodes)):
            for j in range(len(self.__nodes)):
                if i != j:
                    predecessors_matrix[i][j] = i+1
                else:
                    predecessors_matrix[i][j] = 0

        return predecessors_matrix
