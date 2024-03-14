import networkx as nx
import matplotlib.pyplot as plt


def toString(page_rank):
    return {f"Website {node}": rank for node, rank in page_rank.items()}


def draw_graph(adjacency_list):
    G = nx.DiGraph()

    for node, edges in adjacency_list.items():
        for edge in edges:
            G.add_edge(node, edge)
    plt.figure(figsize=(10, 7))
    nx.draw(G, with_labels=True, node_color='skyblue', node_size=700,
            edge_color='k', linewidths=1, font_size=15,
            arrows=True, arrowsize=20)
    plt.show()

