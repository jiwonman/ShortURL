import base64

class Base62():

    def encode(self, longUrl: str) -> str:
        encoded = base64.urlsafe_b64decode(bytes(longUrl, "UTF-8"))
        return encoded
        
