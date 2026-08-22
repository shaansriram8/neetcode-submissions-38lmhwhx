class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1

        maxseen = 0

        while l <= r:
            length = r-l
            height = min(heights[l], heights[r])
            curr_area = height * length
            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1
            maxseen = max(curr_area, maxseen)
        return maxseen
        