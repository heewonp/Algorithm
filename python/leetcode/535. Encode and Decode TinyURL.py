class Codec:
    
    def __init__(self):
        
        self.dict={}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        short_url = hash(longUrl)
        self.dict[short_url] = longUrl
        return short_url
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.dict[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))