class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            length = len(word)
            encoded += str(length)
            encoded += '#'
            for c in word:
                encoded += c
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        #  5#Hello5#World

        decoded = []
        l, r = 0, 0
        while r < len(s):
            curr = ""
            l=r
            while s[r] != '#':
                r+=1
            length = int(s[l:r])
            
            for _ in range(length):
                r+=1
                curr += s[r]
            r+=1
            print(curr)
            decoded.append(curr)
        return decoded
            


        


        