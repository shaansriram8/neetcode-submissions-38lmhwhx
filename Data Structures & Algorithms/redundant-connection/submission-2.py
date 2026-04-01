class UnionFind():
    def __init__(self, n):
        self.parents = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        self.seen = set()
    
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)

        if ra == rb:
            self.seen.add((a, b))
            return False
        if self.rank[ra] < self.rank[rb]:
            self.parents[ra] = rb
        elif self.rank[rb] < self.rank[ra]:
            self.parents[rb] = ra
        else:
            self.parents[rb] = ra
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n)
        final = 0
        for u, v in edges:
            uf.union(u, v)
        
        for a, b in edges:
            if (a, b) in uf.seen:
                final = [a, b]
            elif (b, a) in uf.seen:
                final = [b, a]
        return final
        