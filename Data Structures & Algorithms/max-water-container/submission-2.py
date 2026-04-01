class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        maxvol = 0
        while l <= r:
            bound = min(heights[r], heights[l])
            vol = bound * (r-l)
            if heights[r] < heights[l]:
                r-=1
            else:
                l+=1
            maxvol = max(vol, maxvol)
        return maxvol
        