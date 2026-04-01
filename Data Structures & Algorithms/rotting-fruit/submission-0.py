class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()


        #this allows us to find starting points for our multi source BFS
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    visit.add((r, c))
                    queue.append([r, c])
        t = 0
        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)] #possible movements
        while queue:
            changed = False
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in neighbors:
                    newrow, newcol = r + dr, c + dc #new direction
                    if newrow in range(ROWS) and newcol in range(COLS) and (newrow, newcol) not in visit and grid[newrow][newcol] == 1:
                        visit.add((newrow, newcol))
                        queue.append([newrow, newcol])
                        grid[newrow][newcol] = 2
                        changed = True
            if changed:
                t+=1

        for r in range(ROWS):
            for c in range(COLS):
                print(grid[r][c])
                if grid[r][c] == 1:
                    return -1
        return t



        
        