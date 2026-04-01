class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        
        locations = {}
        for ind, char in enumerate(keyboard):
            locations[char] = ind

        pos = 0
        tot = 0
        for char in word:
            new_pos = locations[char]
            tot += abs(new_pos - pos)
            pos = new_pos
        return tot



            

        