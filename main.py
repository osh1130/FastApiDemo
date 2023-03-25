"""
@Author Vivi Zhao
HTTP--,RPC--Remote Procedure Call(TCP/IP)
"""

from fastapi import FastAPI, HTTPException, Depends

app = FastAPI()
from model import Item
from model import LoginInfo
from libs import create_token, get_user

_data={
    'user':{
        "username":"vivi",
        "password":"123456"
    }
}

@app.get("/")
def index():
    return {"msg":"hello world!"}

def add(a,b): #RPC provide function
    return a+b

@app.get("/add_by_get") # api url
def add_get(a:int,b:int): #api interface
    c=add(a,b)
    return {"c":c}

#res = add(1,2) # local call
#print(res)

@app.post("/add_by_post") # api url
#The interface requires the token information
def add_post(item:Item, user:str = Depends(get_user)): #object item
    #This request requires a login to be used
    #This interface has been secured(401)
    c=add(item.a,item.b)
    return {"c":c}

@app.post("/login")
def login(login_info:LoginInfo):
    if login_info.username != _data['user']["username"]:
        #username error
        raise HTTPException(status_code =400,detail="username error")
    if login_info.password != _data['user']["password"]:
        raise HTTPException(status_code =400,detail="password error")
    return {"token":create_token(login_info.username)}