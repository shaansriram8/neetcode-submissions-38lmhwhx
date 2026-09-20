class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for string in strs:
            length = len(string)
            out += str(length) + '#' + string
        print(out)
        return out
    def decode(self, s: str) -> List[str]:
        l, r = 0, 0
        out = []
        while r < len(s):
            length = 0
            word = ""
            while s[r] != '#':
                r+=1
            print(s[l:r])
            length = int(s[l:r])
            r+=1 #once we reach '#', move forward to start reading the string
            for i in range(length):
                word+= s[r]
                r+=1
            out.append(word)
            l=r
        return out


                


