class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        out = []
        r, c = len(grid), len(grid[0])
        a, b = 0, 0
        for row in range(r):
            for col in range(c):
                if grid[row][col] in seen:
                    a = grid[row][col]
                    out.append(a)
                seen.add(grid[row][col])
        for i in range(1, (r**2)+1):
            if i not in seen:
                out.append(i)
        return out
        