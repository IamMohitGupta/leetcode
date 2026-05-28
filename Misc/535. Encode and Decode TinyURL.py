class Codec:

    def __init__(self):
        self.m = {}
        self.res = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        result = f"http://tinyurl.com/{self.res}"
        self.res+=1
        self.m[result] = longUrl
        return result

        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.m[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
