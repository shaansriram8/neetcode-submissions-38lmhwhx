class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        
        temp = x
        rev = 0
        
        factor = pow(10, len(str(x))-1)
        while temp:
            rev = int(temp % 10)*factor + rev
            temp = int(temp / 10)
            factor = factor / 10
            print("rev:", rev)
            print("temp:", temp)
        return rev == x
        
        