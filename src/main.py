from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
import asyncio
import httpx

app = FastAPI()



class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


async def request(client, URL):
    response = await client.get(URL)
    return response.text

async def task(URL):
    async with httpx.AsyncClient() as client:
        result = await request(client, URL)
        #result = await asyncio.gather(*tasks)
        return result


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.get("/git/{username}")
async def get_git(username: str):
    URL = f"https://api.github.com/users/{username}/starred"
    return await task(URL)

