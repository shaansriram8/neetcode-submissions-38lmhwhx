class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        seen = set()
        def bfs(r, c) -> None:
            queue = deque([(r, c)])
            seen.add((r, c))
            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr, nc) not in seen and nr in range(ROWS) and nc in range(COLS) and board[nr][nc] == "O":
                        board[nr][nc] = "#"
                        queue.append((nr, nc))
                        seen.add((nr, nc))
        
        for i in range(ROWS):
            for j in range(COLS):
                if i == 0 or i == ROWS-1 or j == 0 or j == COLS-1:
                    if (i, j) not in seen and board[i][j] == "O":
                            board[i][j] = "#"
                            bfs(i, j)

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "#":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
        

            
