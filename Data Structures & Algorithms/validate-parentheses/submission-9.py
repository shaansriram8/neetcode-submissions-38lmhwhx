class Solution:
    def isValid(self, s: str) -> bool:

         pairs = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
         }
         if len(s)%2 != 0:
            return False 

         stack = []

         for char in s:
             if char in pairs: #if opening
                 stack.append(char)
             elif stack and pairs[stack[-1]] == char:
                 stack.pop()
             else:
                return False
         return not stack



                
