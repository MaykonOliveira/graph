import numpy as np


class Dijkstra(object):

    def __init__(self, graph, start_node_key, debug=False):
        self.__debug = debug
        self.__graph = graph
        self.__start_node_key = start_node_key
        self.__nodes = self.__graph.get_nodes()
        self.__closed_nodes = []
        self.__cost_matrix = self.__new_cost_matrix()
        self.__predecessors_matrix = ['-' for i in range(len(self.__nodes))]

        if debug:
            self.__debug_log()
        self.__run()

    def minimum_distance(self, destiny_node_key):
        for index, node in enumerate(self.__nodes):
            if node.get_key() == destiny_node_key:
                return self.__cost_matrix[index]

    def minimum_path(self, destiny_node_key):
        node_1_index = None
        node_2_index = None
        current_index = None
        minimum_path = []

        for index, node in enumerate(self.__nodes):
            if node.get_key() == self.__start_node_key:
                node_1_index = index
            if node.get_key() == destiny_node_key:
                node_2_index = index
        minimum_path.append(destiny_node_key)
        
        while destiny_node_key != self.__start_node_key:
            for index, key in enumerate(self.__predecessors_matrix):
                if index == node_2_index:
                    minimum_path.append(key)
                    destiny_node_key = key
                    for index, node in enumerate(self.__nodes):
                        if node.get_key() == destiny_node_key:
                            node_2_index = index

        return minimum_path[::-1]

    def __get_open_sucessors(self, node):
        sucessors_keys = self.__graph.get_node_neighbors(node)
        open_sucessors = [node for node in self.__nodes if
         (self.__nodes.index(node) not in self.__closed_nodes) and (node.get_key() in sucessors_keys) ]

        return open_sucessors

    def __get_node_cost(self, node):
        return self.__cost_matrix[self.__nodes.index(node)]

    def __get_minimun_cost_open_node(self):
        open_nodes = [node for node in self.__nodes if self.__nodes.index(node) not in self.__closed_nodes]
        return min(open_nodes, key=self.__get_node_cost)

    def __run(self):
        cont = 0
        while len(self.__closed_nodes) != len(self.__nodes):
            cont += 1
            k = self.__get_minimun_cost_open_node()
            self.__closed_nodes.append(self.__nodes.index(k))
  
            open_sucessors = self.__get_open_sucessors(k)
                  
            for j in open_sucessors:
                cost = self.__cost_matrix[self.__nodes.index(k)] + self.__graph.exist_edge(k.get_key(), j.get_key()).get_value()

                if cost < self.__cost_matrix[self.__nodes.index(j)]:
                    self.__cost_matrix[self.__nodes.index(j)] = cost
                    self.__predecessors_matrix[self.__nodes.index(j)] = k.get_key()

            if self.__debug:
                print(15 * '-' + "Iteration: " + str(cont) + 15 * '-')
                print("Node Closed: " + k.get_key())
                print(15 * '=' + "Closed Nodes" + 15 * '=')
                print([ self.__nodes[node_index].get_key() for node_index in self.__closed_nodes])
                input("Press any key to continue")

                print(15 * '=' + "Open Sucessors of '{}'".format(k.get_key()) + 15 * '=')
                print([node.get_key() for node in open_sucessors])
                input("Press any key to continue")

                print(15 * '=' + "Cost Matrix" + 15 * '=')
                print(self.__cost_matrix)
                input("Press any key to continue")

                print(15 * '=' + "Predecessor Matrix" + 15 * '=')
                print(self.__predecessors_matrix)
                input("Press any key to continue") 

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
        start_node_index = None
        cost_matrix = np.zeros(len(self.__nodes))

        for index, node in enumerate(self.__nodes):
            if node.get_key() == self.__start_node_key:
                start_node_index = index

        for index, _ in enumerate(cost_matrix):
            if index == start_node_index:
                cost_matrix[index] = 0
            else:
                cost_matrix[index] = float("inf")

        return cost_matrix 