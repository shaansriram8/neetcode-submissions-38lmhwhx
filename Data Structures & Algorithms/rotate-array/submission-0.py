class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = nums[-1]
        ctr = 0
        while ctr < k:
            nums[1:] = nums[0:len(nums)-1]
            nums[0] = temp
            temp = nums[-1]
            ctr +=1
        return nums
        