from jwt import encode

def create_token(data : dict):
    token: str = encode(payload= data, key = "my_secret", algorithm="HS256")
    print(token)
    return token
