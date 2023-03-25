import datetime

from fastapi import HTTPException,Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

KEY = "wkjbnliwcbpc;wq2383r2733@#%#%^^"
TOKEN_EXPIRE = 60 * 24 * 7  # one week


def create_token(username: str):
    """
    Generate a token based on user information
    :param username:
    :return:
    """
    d = {
        "username": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=TOKEN_EXPIRE)
    }

    encoded = jwt.encode(d, KEY, algorithm='HS256')
    return encoded

def get_user(token:str=Depends(OAuth2PasswordBearer(tokenUrl='/login'))):
    """
    User information is resolved based on the token
    Go to the login interface to obtain bearer token
    :return:
    """
    try:
        d = jwt.decode(token, KEY, algorithms='HS256')
        # expire valid
        username = d.get("username","-1")
        #-1 default
    except(jwt.JWTError,):
        raise HTTPException(status_code=403, detail="token Authentication failure")

    if username == "-1":
        raise HTTPException(status_code=400, detail="username error")
    else:
        return username