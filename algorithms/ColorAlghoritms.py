class Color(object):

    def __init__(self):
        pass

    def welsh_powell(self, graph):
        sorted_nodes = sorted(graph.get_nodes(), key=lambda x: len(x.get_edges()), reverse=True)
        nodes_number = len(graph.get_nodes())
        color_values = {sorted_nodes[0].get_key(): 0}

        for node in sorted_nodes[1:]:
            available_colors = [True] * nodes_number

            for adjacent_node in graph.get_node_neighbors(node):
                if adjacent_node in color_values.keys():
                    color = color_values[adjacent_node]
                    available_colors[color] = False

            new_color = 0
            for new_color in range(len(available_colors)):
                if available_colors[new_color]:
                    break
            color_values[node.get_key()] = new_color

        return color_values

