from models.Graph import Graph


class Prim(object):

    def __init__(self, graph, initial_node_key):
        self._graph = graph
        self._initial_node_key = initial_node_key

    def minimum_spanning_tree(self):
        minimum_graph = Graph()
        minimum_graph.add_node(self._initial_node_key, self._graph.get_node_value(self._initial_node_key))
        visited = {self._initial_node_key}
        weight_sum = 0
        while len(visited) != len(self._graph.get_nodes()):
            minimum_weight = float("inf")
            minimun_node_reference = None
            node_reference = None
            edge_reference = None
            for node in visited.copy():
                current_edges = self._graph.get_node_from_key(node).get_edges()
                for edge in current_edges:
                    if edge.get_destiny_node() not in visited:
                        if edge.get_value() < minimum_weight:
                            node_reference = node
                            edge_reference = edge
                            minimun_node_reference = edge.get_destiny_node()
                            minimum_weight = edge.get_value()
            minimum_graph.add_node(minimun_node_reference, self._graph.get_node_value(minimun_node_reference))
            minimum_graph.add_edge(edge_reference.get_key(), node_reference,
                                   minimun_node_reference, edge_reference.get_value())
            visited.add(minimun_node_reference)
            weight_sum += minimum_weight
        return minimum_graph, weight_sum
