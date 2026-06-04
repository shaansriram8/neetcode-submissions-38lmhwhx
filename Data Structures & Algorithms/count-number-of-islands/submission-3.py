class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        seen = set()
        queue = deque()
        def bfs(x, y):
            seen.add((x, y))
            queue.append([x, y])
            neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            while queue:
                r, c = queue.popleft()
                for dr, dc in neighbors:
                    new_row, new_col = r + dr, c + dc
                    if new_row in range(rows) and new_col in range(cols) and (new_row, new_col) not in seen and grid[new_row][new_col] == '1':
                        seen.add((new_row, new_col))
                        queue.append([new_row, new_col])
            return 1
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in seen:
                    islands += bfs(r, c)
        return islands



        




