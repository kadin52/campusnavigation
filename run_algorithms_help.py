
def calc_distance(G,path):
    distance =0
    for i in range(len(path)-1):
        node1,node2 = path[i],path[i+1]
        if G.has_edge(node1,node2):
            distance +=G[node1][node2]['weight']
    distance = 110/66 * distance
    return distance

def convert_abbr_to_index(abbr, manual_nodes):
    index = -999
    for i, ((lon, lat), node_abbr) in manual_nodes.items():
        if node_abbr == abbr:
            index = i
            return index


def convert_graph_to_adj_list(G):
    adj_list_with_weights = {}

    for node in G.nodes():
        adj_list_with_weights[node] = []
        for neighbor in G.neighbors(node):
            weight = G[node][neighbor]['weight']
            adj_list_with_weights[node].append((neighbor, weight))

    return adj_list_with_weights

