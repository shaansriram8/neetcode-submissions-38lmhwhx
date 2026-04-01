class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        island_area = 0

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visit.add((r, c))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            area = 1
            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if nr in range(rows) and nc in range(cols) and (nr, nc) not in visit and grid[nr][nc] == 1:
                        queue.append((nr, nc))
                        visit.add((nr, nc))
                        area+=1
            return area



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    curr_island_area = bfs(r, c)
                    island_area = max(curr_island_area, island_area)
        
        return island_area


        