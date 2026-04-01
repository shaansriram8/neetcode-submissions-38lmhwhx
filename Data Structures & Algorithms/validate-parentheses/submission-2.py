class Solution:
    def isValid(self, s: str) -> bool:

        charmap = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }
        # ({[]})
        stack = []

        for char in s:
            if char in charmap: #if char is opening
                stack.append(char)
            elif char in charmap.values(): #if char is closing
                if not stack or char != charmap[stack[-1]]:
                    return False
                else:
                    stack.pop()
        
        return not stack




        
        