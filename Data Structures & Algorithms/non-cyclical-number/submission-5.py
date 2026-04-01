class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()
        while n not in seen:
            digits = []
            seen.add(n)
            num = 0
            while n > 0:
                digits.append(n%10)
                n = n // 10
            for ind, val in enumerate(digits):
                digits[ind] = digits[ind] ** 2
                num += digits[ind] 
            if num == 1:
                return True
            n = num
        return False
            




        