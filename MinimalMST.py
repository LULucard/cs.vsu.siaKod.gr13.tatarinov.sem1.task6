from UnionFindSet import UnionFindSet
from Graph import Graph


class MinimalMST:
    def __init__(self, adj_matrix):
        self.graph = Graph(adj_matrix)

    def create_mMST_by_Kruskal(self):
        edges = self.graph.to_edge_list()
        edges.sort(key=lambda x: x[2])

        ds = UnionFindSet(len(self.graph.adjacency_matrix))
        mst_edges = []

        for edge in edges:
            u, v, weight = edge

            if ds.find_set(u) != ds.find_set(v):
                ds.union_sets(u, v)
                mst_edges.append((u, v, weight))

        return mst_edges
