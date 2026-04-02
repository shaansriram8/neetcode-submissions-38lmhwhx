class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ptr = 0
        while ptr < len(nums)-1:
            flag = False
            curr = nums[ptr]
            print("curr", curr)
            ret = 0
            best = (0, 0)
            for i in range(1, curr+1):
                if ptr+i > len(nums)-1:
                    return True
                if nums[ptr+i] != 0 or ptr+i == len(nums)-1:
                    print("new spot:", nums[ptr+i])
                    ret = ptr + i
                    best = max(best, (ret+nums[ret], ret))
                    flag = True
            print("best", nums[best[1]])
            ptr = best[1]
            if flag == False:
                return False
        return True

        