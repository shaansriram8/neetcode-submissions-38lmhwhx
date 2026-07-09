class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def bfs(seen, r, c):
            queue = deque()
            queue.append((r, c))  
            count = 0    
            while queue:
                row, col = queue.popleft()
                count +=1
                for dr, dc in deltas:
                    nr, nc = row + dr, col + dc
                    if nr in range(rows) and nc in range(cols) and (nr, nc) not in seen and grid[nr][nc] == 1:
                        queue.append((nr, nc))
                        seen.add((nr, nc))
            return count
        area = 0
        seen = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in seen:
                    seen.add((r, c))
                    area = max(area, bfs(seen, r, c))
        return area
        
        

