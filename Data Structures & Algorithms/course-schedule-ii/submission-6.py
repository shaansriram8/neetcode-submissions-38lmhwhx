class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #b->a
        out = []
        n = numCourses
        degree = [0] * n
        adj = [[] for _ in range(n)]
        
        for a, b in prerequisites:
            adj[b].append(a)
            degree[a] +=1
        
        queue = deque()

        for ind, deg in enumerate(degree):
            if deg == 0:
                queue.append(ind)
        
        while queue:
            node = queue.popleft()
            out.append(node)
            for neighbor in adj[node]:
                degree[neighbor] -=1
                if degree[neighbor] == 0:
                    queue.append(neighbor)
        return [] if n != len(out) else out

