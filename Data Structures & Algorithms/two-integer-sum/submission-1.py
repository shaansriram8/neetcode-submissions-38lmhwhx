class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        #return nums[i], nums[j]

        for i, n in enumerate(nums):
            complement = target - n
            if complement in hashmap:
                return [hashmap[complement], i]
            else:
                hashmap[n] = i
        return []    
            
            
            

             

        