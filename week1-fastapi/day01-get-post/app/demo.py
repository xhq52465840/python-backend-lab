from fastapi import FastAPI
from enum import Enum

class Item(str,Enum):
    JACK="jack"
    JILL="jill"
    XIANG = "xiang"
 
class ItemInt(int,Enum):
    THIRTY_THREE=33
    TWO_THOUSAND_TWENTY=2020


pages = [{
    'id':1,'title':'Page 1'
},
{'id':2,'title':'Page 2'},
{'id':3,'title':'Page 3'},
{'id':4,'title':'Page 4'},
{'id':5,'title':'Page 5'}  
]
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
@app.get("/items/jack")
async def read_item_jack():
    return {"item_id": "jack"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if(item_id is ItemInt.THIRTY_THREE):
        return {"item_id": item_id, "message": "thirty-three",'source':ItemInt.THIRTY_THREE}
    else:
        return {"item_id": item_id}
@app.post("/items/")
async def create_item(item: dict):
    return {"item": item}

@app.get('/pages')
async def read_pages(pageNo: int,pageSize: int|None=2):
    # 分页而已，实际应用中应该从数据库中查询数据
    return pages[(pageNo-1)*pageSize:pageNo*pageSize]
