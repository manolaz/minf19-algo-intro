from heapq import heappush, heappop
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

from networkx.drawing.nx_pydot import write_dot

# import matplotlib , inline

def dijkstra(graph, source):
    distance = {}
    queue = [(0, source)]
    while queue:
        # shortest unexplored path
        p, v = heappop(queue)
        if v in distance:
            continue
        # shortest path (source, ..., v)
        print('({} ===> {}) = {}'.format(source, v, p))
        distance[v] = p

        # extend path to (source, ..., v, u)
        for _, u, e in graph.edges(v, data=True):
            heappush(queue, (p + e['weight'], u))

    return distance

n = 8
graph = nx.Graph()
graph.add_nodes_from(range(n))
for u, v in np.random.randint(0, n, (n, 2)):
    graph.add_edge(u, v, weight=abs(u - v))

weights = [e['weight'] / n * 10  for (u, v, e) in graph.edges(data=True)]
#
# plt.figure(figsize=(12, 8))
# plt.axis('off')
#
# layout = nx.spring_layout(graph)
# nx.draw_networkx_nodes(graph, layout, node_color='steelblue', node_size=520)
# nx.draw_networkx_edges(graph, layout, edge_color='gray', width=weights)
# nx.draw_networkx_labels(graph, layout, font_color='white')
# # None
dict_list_graph = nx.convert.to_dict_of_dicts(graph)
edges_list = nx.convert.to_edgelist(graph)

for e in edges_list:
    print(e)

# distances = dijkstra(graph, 0)


# from networkx.drawing.nx_pydot import write_dot
# pos = nx.nx_agraph.graphviz_layout(graph)
# nx.draw(graph, pos=pos)
# write_dot(graph, 'file.dot')
# nx.draw(graph)
# plt.savefig("path.png")
