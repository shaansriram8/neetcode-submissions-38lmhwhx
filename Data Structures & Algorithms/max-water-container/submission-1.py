class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        res = 0
        l, r = 0, n-1
        volume = 0
        while l < r:
            curr_volume = (r-l) * min(heights[r], heights[l])
            if heights[l] <= heights[r]:
                l +=1
            else:
                r -=1
            volume = max(curr_volume, volume)
        return volume
        