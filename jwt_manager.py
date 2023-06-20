from jwt import encode, decode

def create_token(data : dict):
    token: str = encode(payload= data, key = "my_secret", algorithm="HS256")
    print(token)
    return token

def validate_token(token: str)-> dict:
    data: str = decode(token, key = "my_secret", algorithms=['HS256'])
    return data