class Visualizer:
    @staticmethod
    def draw_mst(mst_edges):
        print("Минимальное остовное дерево:")
        for edge in mst_edges:
            u_index, v_index, weight = edge
            print(f"Вершина {u_index} <-> Вершина {v_index}, вес: {weight}")
