import networkx as nx
import matplotlib.pyplot as plt

from models.node import Node
from models.edge import Edge


class Graph(object):

    def __init__(self):
        self.__graph = nx.Graph()
        self.__nodes = []

    def add_node(self, node_key, node_value):
        if self._verify_node_exist(node_key):
            print("Node already exist in the graph!")
        else:
            print("Added node {} with value {}!".format(node_key, node_value))
            self.__nodes.append(Node(node_key, node_value))
            self.__graph.add_node(node_key)

    def remove_node(self, node_key):
        index = self._get_node_index(node_key)
        if index is not None:
            print("Removed node {} with value {}!".format(node_key, self.__nodes[index].get_value()))
            self.__nodes.pop(index)
            self.__graph.remove_node(node_key)
        else:
            print("Node not exist in the graph!")

    def add_edge(self, id, node_key_1, node_key_2, edge_value):
        if self._verify_node_exist(node_key_1) and self._verify_node_exist(node_key_2):
            print("Added edge {} with value {}!".format((node_key_1, node_key_2), edge_value))
            node_1_index = self._get_node_index(node_key_1)
            node_2_index = self._get_node_index(node_key_2)
            self.__nodes[node_1_index].add_edge(Edge(id, node_key_2, edge_value))
            self.__nodes[node_2_index].add_edge(Edge(id, node_key_1, edge_value))
            self.__graph.add_edge(node_key_1, node_key_2)
        else:
            print("One of the informed nodes not exist!")

    def remove_edge(self, node_key_1, node_key_2):
        node_1_index = self._get_node_index(node_key_1)
        node_2_index = self._get_node_index(node_key_2)
        edge_value = self.__nodes[node_1_index].remove_edge(node_key_2)
        self.__nodes[node_2_index].remove_edge(node_key_1)
        self.__graph.remove_edge(node_key_1, node_key_2)
        print("Removed edge with value {}!".format(edge_value))

    def verify_node_is_adjacent(self, node_key_1, node_key_2):
        node_1_index = self._get_node_index(node_key_1)
        for edge in self.__nodes[node_1_index].get_edges():
            if edge.get_destiny_node() == node_key_2:
                print("Node {} and {} are adjacents!".format(node_key_1, node_key_2))
                return True
        return False

    def _verify_node_exist(self, node_key):
        return any(node.get_key() == node_key for node in self.__nodes)

    def _get_node_index(self, node_key):
        for index, node in enumerate(self.__nodes):
            if node_key == node.get_key():
                return index
        return None

    def plot_graph(self, png_create=False):
        if png_create:
            plt.savefig("graph.png")
        nx.draw(self.__graph)
        plt.show()
