class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #[a, b] means a is dependent on b 
        out = []
        n = numCourses
        degree = [0] * n
        adj = [[] for _ in range(n)] #each node gets its own list

        #start by populating adj list and degrees
        for a, b in prerequisites:
            adj[b].append(a)
            degree[a] += 1
        
        #we need to prepopulate queue now
        queue = deque()
        for ind, num in enumerate(degree): #ind = node, num = degree
            if num == 0: #if the degree is 0, valid starting point
                queue.append(ind)

        while queue:
            node = queue.popleft()
            out.append(node)
            for neighbor in adj[node]:
                degree[neighbor] -=1
                if degree[neighbor] == 0:
                    queue.append(neighbor)
        return [] if len(out) != n else out




