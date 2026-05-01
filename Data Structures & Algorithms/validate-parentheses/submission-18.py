class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            '{': '}',
            '(': ')',
            '[': ']',
        }
        stack = []
        for char in s:
            if char in hashmap.values():
                if stack and char == hashmap[stack[-1]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack