class Graph:
    def __init__(self, adj_matrix):
        self.adjacency_matrix = adj_matrix

    def to_edge_list(self):
        edges = []
        n = len(self.adjacency_matrix)
        for i in range(n):
            for j in range(i + 1, n):
                if self.adjacency_matrix[i][j] != 0:
                    edges.append((i, j, self.adjacency_matrix[i][j]))
        return edges
