class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        seen = set()
        queue = deque()
        def bfs(x, y):
            seen.add((x, y))
            queue.append((x, y))
            area = 1
            while queue:
                r, c = queue.popleft()
                for dr, dc in neighbors:
                    new_row, new_col = dr + r, dc + c
                    if new_row in range(rows) and new_col in range(cols) and (new_row, new_col) not in seen and grid[new_row][new_col] == 1:
                        queue.append((new_row, new_col))
                        seen.add((new_row, new_col))
                        area += 1
            return area
        
        max_area = 0

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in seen and grid[r][c] == 1:
                    max_area = max(max_area, bfs(r, c))
        return max_area



        