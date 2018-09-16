from collections import deque


class Search(object):

    def __init__(self, graph, initial_node_key, result_node_key):
        self._graph = graph
        self._initial_node_key = initial_node_key
        self._result_node_key = result_node_key

    def breadthFirstSearch(self):
        if self._initial_node_key == self._result_node_key:
            return [self._initial_node_key]
        visited = {self._initial_node_key}
        queue = deque([(self._initial_node_key, [])])
        while queue:
            current, path = queue.popleft()
            current_edges = self._graph.get_node_from_key(current).get_edges()
            for edge in current_edges:
                destiny_node = edge.get_destiny_node()
                if destiny_node in visited:
                    continue
                if destiny_node == self._result_node_key:
                    return path + [current, destiny_node]
                queue.append((destiny_node, path + [current]))
                visited.add(destiny_node)
        return None
