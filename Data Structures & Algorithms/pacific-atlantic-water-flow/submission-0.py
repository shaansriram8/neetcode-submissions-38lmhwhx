#start at nodes on each coast
#append all nodes that can reach this coast by working backwards
#at the end, the union of these two sets is the solution

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = []
        def bfs(r, c, cache) -> None:
            queue = deque([(r, c)])
            cache.add((r, c))
            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if nr in range(ROWS) and nc in range(COLS) and heights[nr][nc] >= heights[row][col] and (nr, nc) not in cache:
                        queue.append((nr, nc))
                        cache.add((nr, nc))
        
        for i, level in enumerate(heights):
            for j, val in enumerate(level):
                if i == 0:
                    bfs(i, j, pacific)
                elif j == 0:
                    bfs(i, j, pacific)
        
        for i, level in enumerate(heights):
            for j, val in enumerate(level):
                if i == ROWS-1:
                    bfs(i, j, atlantic)
                elif j == COLS-1:
                    bfs(i, j, atlantic)

        combined = pacific & atlantic
        for val in combined:
            res.append(list(val))
        return res




        



