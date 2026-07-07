class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        args = [0, 0]
        check = []
        row, col = len(grid), len(grid[0])

        for r in range(row):
            for c in range(col):
                if grid[r][c] in seen:
                    args[0] = grid[r][c]
                seen.add(grid[r][c])
                check.append(grid[r][c])
        dim = row*col
        for num in range(dim+1):
            if num not in seen:
                args[1] = num
        return args


        #1, 3, 2, 2