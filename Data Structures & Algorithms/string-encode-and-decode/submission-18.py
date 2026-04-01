class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for i in strs:
            string = string + i + "|"
        print(""+string+"")
        return string 

    def decode(self, s: str) -> List[str]:
        dummy = ""
        arr = []
        for char in s:
            if char != '|': #if were at a letter
                dummy = dummy + char + "" #builds the word
            else:
                arr.append(dummy)
                dummy = ""
        return arr


