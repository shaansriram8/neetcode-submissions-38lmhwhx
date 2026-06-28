class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        out = []
        n = numCourses #number of nodes
        g = [[] for _ in range(n)] #adjacency list
        degree = [0] * n #degree list

        for a, b in prerequisites: #build adjanceny list then populate degree values
            g[b].append(a)
            degree[a] += 1 

        queue = deque()
        for ind, val in enumerate(degree):
            if val == 0: #if degree is 0
                queue.append(ind) #append the corresponding node

        while queue:
            node = queue.popleft()
            out.append(node)
            for neighbor in g[node]:
                degree[neighbor] -= 1
                if degree[neighbor] == 0:
                    queue.append(neighbor)
        return len(out) == n


