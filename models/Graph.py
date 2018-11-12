import networkx as nx
import matplotlib.pyplot as plt

from models.Node import Node
from models.Edge import Edge


class Graph(object):

    def __init__(self, nodes=None, orientation=False):
        if nodes is None:
            nodes = []
        self.__nodes = nodes
        self.__edges_count = 0
        self.__orientation = orientation
    
    @property
    def orientation(self):
        return self.__orientation
        
    @orientation.setter
    def orientation(self, new_value):
        self.__orientation = new_value

    def exist_edge(self, source_node_key, destiny_node_key):
        for node in self.__nodes:
            for edge in node.get_edges():
                if(node.get_key() == source_node_key) and (edge.get_destiny_node() == destiny_node_key):
                    return edge
        return None

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
            for edge in self.__nodes[index].get_edges():
                self.remove_edge(edge.get_key())
            self.__nodes.pop(index)
        else:
            print("Node not exist in the graph!")

    def add_edge(self, key, node_key_1, node_key_2, edge_value):
        node_1_index = self._get_node_index(node_key_1)
        node_2_index = self._get_node_index(node_key_2)

        if node_1_index is not None and node_2_index is not None:
            if not self._get_references_of_edge_from_key(key):
                print("Added edge {} with value {}!".format((node_key_1, node_key_2), edge_value))
                self.__nodes[node_1_index].add_edge(Edge(key, node_key_2, edge_value))
                self.__edges_count += 1
                if not self.__orientation:
                    print("Added edge {} with value {}!".format((node_key_2, node_key_1), edge_value))
                    self.__nodes[node_2_index].add_edge(Edge(key, node_key_1, edge_value))
            else:
                print("Edge with key {} already exist in the graph!".format(key))
        else:
            print("One of the informed nodes not exist!")

    def remove_edge(self, edge_key):
        edge_references = self._get_references_of_edge_from_key(edge_key)
        if edge_references:
            value_removed = None
            for reference in edge_references:
                value_removed = self.__nodes[reference.get("node_index")].remove_edge(reference.get("edge_index"))
            print("Removed edge {} with value {}!".format(edge_key, value_removed))
            self.__edges_count -= 1
        else:
            print("Edge informed not exist!")

    def get_node_value(self, node_key):
        node_index = self._get_node_index(node_key)
        if node_index is not None:
            return self.__nodes[node_index].get_value()
        else:
            print("Node {} not exist!".format(node_key))

    def get_edge_value(self, edge_key):
        edge_references = self._get_references_of_edge_from_key(edge_key)
        if edge_references:
            node = self.__nodes[edge_references[0].get("node_index")]
            edge = node.get_edges()[edge_references[0].get("edge_index")]
            print("Edge {} have a value {}!".format(edge_key, edge.get_value()))
            return edge.get_value()

    def get_edge_reference_nodes(self, edge_key):
        references = self._get_references_of_edge_from_key(edge_key)
        if references:
            node_1_reference = self.__nodes[references[0].get("node_index")].get_key()
            node_2_reference = self.__nodes[references[1].get("node_index")].get_key()
            print("Edge {} reference nodes {} and {}!".format(edge_key, node_1_reference, node_2_reference))
            return node_1_reference, node_2_reference

    def get_nodes(self):
        return self.__nodes

    def get_node_neighbors(self, node):
        return [edge.get_destiny_node() for edge in node.get_edges()]

    def get_node_from_key(self, node_key):
        node_index = self._get_node_index(node_key)
        if node_index is not None:
            return self.__nodes[node_index]
        return None

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

    def _get_references_of_edge_from_key(self, edge_key):
        references = []
        for node_index, node in enumerate(self.__nodes):
            for edge_index, edge in enumerate(node.get_edges()):
                if edge.get_key() == edge_key:
                    references.append({"node_index": node_index, "edge_index": edge_index})
        return references

    def get_graph(self):
        if self.__orientation:
            graph = nx.DiGraph()
        else:
            graph = nx.Graph()
        for node in self.__nodes:
            graph.add_node(node.get_key())
            for edge in node.get_edges():
                graph.add_edge(node.get_key(), edge.get_destiny_node(), weight=edge.get_value())
        return graph

    def plot_graph(self, png_create=False, color_map=None):
        graph = self.get_graph()
        pos = nx.spring_layout(graph)

        edge_values = nx.get_edge_attributes(graph, 'weight')
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_values)
        if png_create:
            plt.savefig("graph.png")
        if color_map:
            color_values = [color_map.get(node, 'blue') for node in graph.nodes()]
        else:
            color_values = 'r'

        nx.draw(graph, pos, with_labels=True, node_color=color_values, edge_color='black', width=1, alpha=0.7)
        plt.show()

    def is_planar(self):
        result = True
        node_count = len(self.__nodes)
        region_count = 2 + self.__edges_count - node_count

        if (node_count - self.__edges_count + region_count) == 2:
            print("Euler test: OK")
        else:
            print("Euler test: FAIL")
            result = False

        if len(self.__nodes) >= 3:
            if self._has_three_level_cicle():
                print("This graph has a 3 level cicle!")
                if self.__edges_count <= 3 * node_count - 6:
                    print("Edges and Nodes Teorem: OK")
                else:
                    print("Edges and Nodes Teorem: FAIL")
                    result = False
            else:
                print("This graph do not have a 3 level cicle!")
                if self.__edges_count <= 2 * node_count - 4:
                    print("Edges and Nodes Teorem: OK")
                else:
                    print("Edges and Nodes Teorem: FAIL")
                    result = False
        return result

    def _get_node_by_key(self, key):
        for node in self.__nodes:
            if node.get_key() == key:
                return node
        return None

    def _has_three_level_cicle(self):
        for node in self.__nodes:
            start_node = node
            for edge in node.get_edges():
                second_node = self._get_node_by_key(edge.get_destiny_node())
                for second_edge in second_node.get_edges():
                    third_node = self._get_node_by_key(second_edge.get_destiny_node())
                    if third_node != start_node:
                        for last_edge in third_node.get_edges():
                            if self._get_node_by_key(last_edge.get_destiny_node()) == start_node:
                                return True
        return False
