from pydantic import BaseModel

class Item(BaseModel):
    a:int
    b:int

class LoginInfo(BaseModel):
    username:str
    password:str