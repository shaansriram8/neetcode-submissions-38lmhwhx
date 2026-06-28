class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        out = []
        n = numCourses
        degree = [0] * n
        adj = [[] for _ in range(n)] #each node gets its own adj list

        for a, b in prerequisites:
            adj[b].append(a)
            degree[a] += 1

        queue = deque()
        for ind, val in enumerate(degree):
            if val == 0:
                queue.append(ind)
        
        while queue:
            node = queue.popleft()
            out.append(node)
            for neighbor in adj[node]:
                degree[neighbor] -=1
                if degree[neighbor] == 0:
                    queue.append(neighbor)
        return len(out) == n