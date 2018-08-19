class Edge(object):

    def __init__(self, id, node_key, value):
        self.__id = id
        self.__destiny_node = node_key
        self.__value = value

    def get_value(self):
        return self.__value

    def get_destiny_node(self):
        return self.__destiny_node
