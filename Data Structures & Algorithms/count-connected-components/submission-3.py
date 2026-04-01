class UnionFind():
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [0] * n
        self.components = n
    
    def find(self, val): #want to return root of val
        if val != self.parents[val]: #if not root itself
            self.parents[val] = self.find(self.parents[val]) #path compress
        return self.parents[val]
    
    def union(self, a ,b):
        ra, rb = self.find(a), self.find(b)

        if ra == rb:
            return False
        
        if self.rank[ra] < self.rank[rb]:
            self.parents[ra] = rb
        elif self.rank[rb] < self.rank[ra]:
            self.parents[rb] = ra
        else:
            self.parents[rb] = ra
            self.rank[ra] +=1
        self.components -=1
        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for (u, v) in edges:
            uf.union(u, v)
        
        return uf.components
        
        