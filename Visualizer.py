import matplotlib.pyplot as plt
import networkx as nx
import math


class Visualizer:
    @staticmethod
    def draw_mst_to_terminal(mst_edges):
        print("Минимальное остовное дерево:")
        for edge in mst_edges:
            u_index, v_index, weight = edge
            print(f"Вершина {u_index} <-> Вершина {v_index}, вес: {weight}")

    @staticmethod
    def draw_mst_to_window(mst_edges, n):
        G = nx.Graph()

        for edge in mst_edges:
            u_index, v_index, weight = edge
            G.add_edge(u_index, v_index, weight=weight)

        col = math.ceil(math.sqrt(n))
        row = math.ceil(n / col)

        pos = {i: (i % col, row - 1 - i // col) for i in range(n)}
        labels = nx.get_edge_attributes(G, 'weight')

        nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightgrey')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.title("Лабиринт")
        plt.show()
