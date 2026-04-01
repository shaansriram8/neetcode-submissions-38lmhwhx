class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
         }
        stack = []
        if len(s)%2 != 0:
            return False
        
        for char in s:
            if char in pairs:
                stack.append(char)
            elif stack and pairs[stack[-1]] == char:
                stack.pop()
            else:
                return False
        return not stack
        



                
