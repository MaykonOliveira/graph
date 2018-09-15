class Node(object):

    def __init__(self, key, value):
        self.__key = key
        self.__value = value
        self.__edges = []

    def get_key(self):
        return self.__key

    def get_value(self):
        return self.__value

    def get_edges(self):
        return self.__edges

    def add_edge(self, edge):
        self.__edges.append(edge)

    def remove_edge(self, destiny_node_key):
        for edge in self.__edges:
            if edge.get_destiny_node() == destiny_node_key:
                self.__edges.remove(edge)
                return edge.get_value()
