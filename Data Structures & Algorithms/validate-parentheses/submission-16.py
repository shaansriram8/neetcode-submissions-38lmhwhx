class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '(':')',
            '[':']',
            '{':'}'
        }
        stack = []
        for char in s:
            if char in pairs.values():
                if not stack or pairs[stack[-1]] != char:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)
                
        
        return not stack
            

