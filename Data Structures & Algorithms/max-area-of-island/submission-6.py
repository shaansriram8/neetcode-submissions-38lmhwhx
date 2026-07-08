class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        out = 0
        if not grid: 
            return out
        rows, cols = len(grid), len(grid[0])

        def BFS(seen, neighbors, grid, row, col):
            count = 0
            queue = deque()
            queue.append((row, col))
            while queue:
                r, c = queue.popleft()
                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1 and (nr, nc) not in seen:
                        queue.append((nr, nc))                            
                        seen.add((nr, nc))
                count +=1
            return count

        seen = set()
        neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in seen:
                    seen.add((r, c))
                    out = max(out, BFS(seen, neighbors, grid, r, c))
        return out





