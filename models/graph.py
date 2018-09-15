import networkx as nx
import matplotlib.pyplot as plt

from models.node import Node
from models.edge import Edge


class Graph(object):

    def __init__(self, orientation=False):
        self.__nodes = []
        self.__orientation = orientation

    def add_node(self, node_key, node_value):
        if self._verify_node_exist(node_key):
            print("Node already exist in the graph!")
        else:
            print("Added node {} with value {}!".format(node_key, node_value))
            self.__nodes.append(Node(node_key, node_value))

    def remove_node(self, node_key):
        index = self._get_node_index(node_key)
        if index is not None:
            print("Removed node {} with value {}!".format(node_key, self.__nodes[index].get_value()))
            self.__nodes.pop(index)
        else:
            print("Node not exist in the graph!")

    def add_edge(self, key, node_key_1, node_key_2, edge_value):
        node_1_index = self._get_node_index(node_key_1)
        node_2_index = self._get_node_index(node_key_2)
        if node_1_index is not None and node_2_index is not None:
            print("Added edge {} with value {}!".format((node_key_1, node_key_2), edge_value))
            self.__nodes[node_1_index].add_edge(Edge(key, node_key_2, edge_value))
            if not self.__orientation:
                print("Added edge {} with value {}!".format((node_key_2, node_key_1), edge_value))
                self.__nodes[node_2_index].add_edge(Edge(key, node_key_1, edge_value))
        else:
            print("One of the informed nodes not exist!")

    def remove_edge(self, node_key_1, node_key_2):
        node_1_index = self._get_node_index(node_key_1)
        node_2_index = self._get_node_index(node_key_2)
        if node_1_index is not None and node_2_index is not None:
            edge_value = self.__nodes[node_1_index].remove_edge(node_key_2)
            self.__nodes[node_1_index].remove_edge(node_key_2)
            self.__nodes[node_2_index].remove_edge(node_key_1)
            print("Removed edge with value {}!".format(edge_value))
        else:
            print("One of the informed nodes not exist!")

    def get_node_value(self, node_key):
        node_index = self._get_node_index(node_key)
        if node_index is not None:
            print("Node {} have a value {}!".format(node_key, self.__nodes[node_index].get_value()))
            return self.__nodes[node_index].get_value()
        else:
            print("Node {} not exist!".format(node_key))

    def get_edge_value(self):
        pass

    def verify_node_is_adjacent(self, node_key_1, node_key_2):
        node_1_index = self._get_node_index(node_key_1)
        if node_1_index is not None and self._verify_node_exist(node_key_2):
            for edge in self.__nodes[node_1_index].get_edges():
                if edge.get_destiny_node() == node_key_2:
                    print("Node {} and {} are adjacents!".format(node_key_1, node_key_2))
                    return True
            print("Node {} and {} are not adjacents!".format(node_key_1, node_key_2))
        else:
            print("One of the informed nodes not exist!")
        return False

    def _verify_node_exist(self, node_key):
        return any(node.get_key() == node_key for node in self.__nodes)

    def _get_node_index(self, node_key):
        for index, node in enumerate(self.__nodes):
            if node_key == node.get_key():
                return index
        return None

    def plot_graph(self, png_create=False):
        if self.__orientation:
            graph = nx.DiGraph()
        else:
            graph = nx.Graph()
        for node in self.__nodes:
            graph.add_node(node.get_key(), size=node.get_value())
            for edge in node.get_edges():
                graph.add_edge(node.get_key(), edge.get_destiny_node(), attr=edge.get_value())
        if png_create:
            plt.savefig("graph.png")
        nx.draw(graph)
        plt.show()
