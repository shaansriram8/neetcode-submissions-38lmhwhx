class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #identify the start of a sequence
        #cannot sort 

        seen = set(nums)
        maxseen = 0
        for num in nums:
            cnt = 1
            if num-1 not in seen:
                curr = num
                while curr+1 in seen:
                    cnt+=1
                    curr+=1
            maxseen = max(maxseen, cnt)
        return maxseen


