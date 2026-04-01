class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        visit = set()
        queue.append((0, 0))
        visit.add((0, 0))
        length = 1
        if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
            return -1
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if (r == rows-1 and c == cols-1):
                    return length
                neighbors = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
                for dr, dc in neighbors:
                    new_row, new_col = r + dr, c + dc
                    if (min(new_row, new_col) < 0 or new_row == rows or new_col == cols or (new_row, new_col) in visit or grid[new_row][new_col] == 1):
                        continue
                    queue.append((new_row, new_col))
                    visit.add((new_row, new_col))
            length+=1
        return -1
        