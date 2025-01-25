from MinimalMST import MinimalMST
from Visualizer import Visualizer

adjacency_matrix = [
    [0, 10, 0, 30, 100],
    [10, 0, 50, 0, 0],
    [0, 50, 0, 20, 10],
    [30, 0, 20, 0, 60],
    [100, 0, 10, 60, 0]
]

mst_calculator = MinimalMST(adjacency_matrix)
mst_edges = mst_calculator.create_mMST_by_Kruskal()
Visualizer.draw_mst(mst_edges)
