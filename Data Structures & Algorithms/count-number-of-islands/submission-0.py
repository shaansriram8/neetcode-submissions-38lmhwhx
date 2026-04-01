class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])

        seen = set()
        islands = 0

        def dfs(r, c):
            q = deque()
            q.append((r, c))
            seen.add((r, c))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    new_row, new_col = row+dr, col+dc
                    if (new_row < rows and new_col < cols and (new_row, new_col) not in seen
                    and new_row >= 0 and new_col >= 0 and grid[new_row][new_col] == '1'):
                        q.append((new_row, new_col))
                        seen.add((new_row, new_col))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in seen:
                    dfs(r, c)
                    islands+=1

        return islands