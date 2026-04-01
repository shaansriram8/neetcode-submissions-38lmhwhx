class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        seen = set()
        n = len(edges)
        class UnionFind:
            def __init__(self, n):
                self.parent = [i for i in range(n+1)]
                self.rank = [0] * (n+1)
            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            def union(self, seen, a, b):
                ra, rb = self.find(a), self.find(b)
                if ra == rb:
                    seen.add((a, b))
                else:
                    if self.rank[ra] < self.rank[rb]:
                        self.parent[ra] = rb
                    elif self.rank[rb] < self.rank[ra]:
                        self.parent[rb] = ra
                    else:
                        self.parent[ra] = rb
                        self.rank[rb] +=1
        uf = UnionFind(n)
        out = 0
        for u, v in edges:
            uf.union(seen, u, v)
        
        for a, b in reversed(edges):
            if (a, b) in seen:
                return [a, b]
            elif (b, a) in seen:
                return [b, a]

        

                    

        