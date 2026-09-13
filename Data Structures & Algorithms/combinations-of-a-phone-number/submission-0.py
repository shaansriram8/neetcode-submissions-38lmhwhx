class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        digit_to_letters = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        path, res = [], []

        def backtrack(i):
            if len(path) == len(digits):
                res.append("".join(path[:]))
                return
            
            for ch in digit_to_letters[digits[i]]:
                path.append(ch)
                backtrack(i+1)
                path.pop()

        backtrack(0)
        return res