class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        rows, cols = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
            return -1
        visit = set()
        queue = deque()
        visit.add((0, 0))
        queue.append((0, 0))
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, 1), (1, 1), (-1, -1), (1, -1)]
        length = 1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == rows-1 and c == cols-1:
                    return length
                for dr, dc in directions:
                    new_row, new_col = r + dr, c + dc
                    if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 0 and (new_row, new_col) not in visit:
                        queue.append((new_row, new_col))
                        visit.add((new_row, new_col))
            length+=1
        return -1
        