class Solution:
    def minOperations(self, logs: List[str]) -> int:
        #../ -> pop
        #./ -> do nothing
        #x (anything else) -> 
        stack = []
        for log in logs:
            if log == '../':
                if stack:
                    stack.pop()
            elif log != './':
                stack.append(log)
        return len(stack)