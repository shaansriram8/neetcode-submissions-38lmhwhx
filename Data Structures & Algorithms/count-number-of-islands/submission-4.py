class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0
        queue = deque()
        seen = set()
        neighbors = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def dfs(r, c):
            queue.append((r, c))
            seen.add((r, c))
            while queue:
                row, col = queue.popleft()
                for dr, dc in neighbors:
                    nr = row + dr
                    nc = col + dc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == '1' and (nr, nc) not in seen:
                        queue.append((nr, nc))
                        seen.add((nr, nc))
            return 1
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in seen:
                    islands += dfs(r, c)
        return islands
    





        