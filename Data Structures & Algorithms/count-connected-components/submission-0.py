class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        class UnionFind:
            def __init__(self, n):
                self.parent = [i for i in range(n)]
                self.rank = [0]*n
                self.components = n
            
            def find(self, x):
                if x != self.parent[x]: #if x is not root, path compress
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            
            def union(self, a, b):
                ra, rb = self.find(a), self.find(b)

                if ra == rb:
                    return False
                
                if self.rank[ra] < self.rank[rb]:
                    self.parent[ra] = rb
                elif self.rank[rb] < self.rank[ra]:
                    self.parent[rb] = ra
                else:
                    self.parent[rb] = ra
                    self.rank[ra] +=1
                self.components -=1
                return True
        
        uf = UnionFind(n)
        for (u, v) in edges:
            uf.union(u, v)
        return uf.components
            
