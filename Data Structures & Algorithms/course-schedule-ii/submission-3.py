class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #given [a, b], b->a (a depends on b)
        out = []
        n = numCourses
        degree = [0] * n #each node gets a degree of how many dependencies it has
        adj = [[] for _ in range(n)] #each node gets an adjacency list

        for a, b in prerequisites:
            adj[b].append(a)
            degree[a] += 1

        queue = deque() #queue holds all degree 0 nodes to process first

        for node, deg in enumerate(degree):
            if deg == 0:
                queue.append(node)
        
        while queue:
            node = queue.popleft()
            out.append(node)
            for neighbor in adj[node]:
                degree[neighbor] -=1
                if degree[neighbor] == 0:
                    queue.append(neighbor)
        return [] if len(out) != n else out




