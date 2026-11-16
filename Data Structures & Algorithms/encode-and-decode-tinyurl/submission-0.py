class Solution:
    def __init__(self):
        self.kv = {}
    def encode(self, longUrl: str) -> str:
        i = str(len(self.kv))
        self.kv[i] = longUrl
        return i
    def decode(self, shortUrl: str) -> str:
        return self.kv[shortUrl]
