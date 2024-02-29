from typing import Union

from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import asyncio
import httpx
import json
from functools import lru_cache
from typing import Annotated

from config import Settings

app = FastAPI()

#import secret.client


@lru_cache
def get_settings():
    return Settings()

async def request(client, URL):
    headers = {
        "accept" : "application/vnd.github+json"
    }
    response = await client.get(URL, headers=headers)
    return response.text

def process_data(data):
    wanted_data = []
    for item in data:
        if item["private"] == False:
            wanted_data.append(item)
    return wanted_data

        

async def task(URL):
    async with httpx.AsyncClient() as client:
        result = await request(client, URL)
        #result = await asyncio.gather(*tasks)
        return result
    
async def get_data(acces_token):
    URL = f"https://api.github.com/user/starred"
    headers = {
        'X-GitHub-Api-Version': '2022-11-28',
        "Authorization" : f"Bearer {acces_token["access_token"]}",
        "accept" : "application/vnd.github+json"
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(URL, headers=headers)
        return response.text

@app.get("/git/noauth/{username}")
async def get_git(username: str):
    URL = f"https://api.github.com/users/{username}/starred"
    return await task(URL)

@app.get("/git/auth/")
async def git_auth(code: str, settings: Annotated[Settings, Depends(get_settings)]):
    URL = f"https://github.com/login/oauth/access_token"
    params = {
        "client_id" : settings.ID, 
        "client_secret" : settings.SECRET,
        "code" : code
    }
    headers = {
        "Accept": "application/json"
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(URL, params=params, headers=headers)
        access_token = json.loads(response.text)
        #return access_token
        data = await get_data(access_token)
        data = json.loads(data)
        return process_data(data)

    
@app.get("/git/auth/{username}")
async def git_login(username: str, settings: Annotated[Settings, Depends(get_settings)]):
    #?login={username}&client_id={secret.client.ID}
    URL = f"https://github.com/login/oauth/authorize?login={username}&client_id={settings.ID}"
    params = {
        "login" : username,
        "client_id" : settings.ID
    }
    return RedirectResponse(URL)