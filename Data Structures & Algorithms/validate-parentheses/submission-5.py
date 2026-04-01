class Solution:
    def isValid(self, s: str) -> bool:

        charmap = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }
        # ({[]})
        stack = []
        #if we see a opening bracket, append to stack. when we see a clsoing 
        #bracket, see if it corresponds to the correct opening one in map.
        #If it doesnt, return false
        #return not stack
        for char in s:
            if char in charmap.keys(): #if opening
                stack.append(char)
            elif stack and charmap[stack[-1]] == char: #if closing
                stack.pop()
            else:
                return False
        return not stack







        
        