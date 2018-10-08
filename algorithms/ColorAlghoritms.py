class Color(object):

    def __init__(self):
        pass

    def welshPowell(self, G):
        node_list = sorted(G.nodes())
        col_val = {}
        col_val[node_list[0]] = 0
        for node in node_list[1:]:
            available = [True] * len(G.nodes())
            for adj_node in G.neighbors(node):
                if adj_node in col_val.keys():
                    col = col_val[adj_node]
                    available[col] = False
            clr = 0
            for clr in range(len(available)):
                if available[clr]:
                    break
            col_val[node] = clr
        return col_val
