class Edge(object):

    def __init__(self, key, node_key, value):
        self.__key = key
        self.__destiny_node = node_key
        self.__value = value

    def get_key(self):
        return self.__key

    def get_value(self):
        return self.__value

    def get_destiny_node(self):
        return self.__destiny_node
