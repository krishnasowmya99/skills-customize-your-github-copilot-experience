from typing import Dict, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True

items: Dict[int, Item] = {
    1: Item(name="Laptop", description="A portable computer", price=999.99),
    2: Item(name="Headphones", description="Noise-cancelling headphones", price=199.99),
}

@app.get("/items")
def list_items():
    return [item.dict() for item in items.values()]

@app.get("/items/{item_id}")
def get_item(item_id: int):
    item = items.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/items", status_code=201)
def create_item(item: Item):
    next_id = max(items.keys(), default=0) + 1
    items[next_id] = item
    return {"id": next_id, **item.dict()}
