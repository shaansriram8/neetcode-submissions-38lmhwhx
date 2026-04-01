class Solution:
    def confusingNumber(self, n: int) -> bool:
        mappings = {
            '0' : '0',
            '1' : '1',
            '6' : '9',
            '8' : '8', 
            '9' : '6'
        }

        string = str(n)
        new_str = ""
        for ind, char in enumerate(string):
            if char not in mappings:
                return False
            new_str += mappings[char]
        return new_str[::-1] != string


        