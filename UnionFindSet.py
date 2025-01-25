class UnionFindSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find_set(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find_set(self.parent[x])
        return self.parent[x]

    def union_sets(self, a, b):
        root_a = self.find_set(a)
        root_b = self.find_set(b)

        if root_a != root_b:
            if self.rank[root_a] > self.rank[root_b]:
                self.parent[root_b] = root_a
            elif self.rank[root_a] < self.rank[root_b]:
                self.parent[root_a] = root_b
            else:
                self.parent[root_b] = root_a
                self.rank[root_a] += 1
