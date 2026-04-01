class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #distance between pointers
        #height of min(heights[l], heights[r])

        l, r = 0, len(heights)-1
        maxseen = 0

        while l < r:
            height = min(heights[r], heights[l])
            vol = (r-l)* height
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
            maxseen = max(vol, maxseen)
        return maxseen

        