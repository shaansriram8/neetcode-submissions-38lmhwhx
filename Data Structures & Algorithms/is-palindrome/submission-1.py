class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = 0
        s = ''.join(ch for ch in s if ch.isalnum())
        R = len(s) - 1

        while L <= R:
            if s[L].lower() != s[R].lower():
                return False
            else:
                print(s[L], s[R])
                L+=1
                R-=1
        return True
        