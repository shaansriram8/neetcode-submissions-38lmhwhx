class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            '{':'}',
            '[':']',
            '(':')'
        }
        for c in s:
            if c not in mapping:
                if stack:
                    if mapping[stack[-1]] == c:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            else:
                stack.append(c)
        return not stack