#!/usr/bin/python3
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from data import database

# import locale files
from schemas import schemas
from api import crud
from data.database import get_db

# Create the Payment Router
router = APIRouter(
    tags=["Payment"],
    prefix="/cart"
)
get_db = database.get_db

# delete items in the cart by id API
@router.delete("/delete_cart_item/{id}", response_model=schemas.CartItemAInfo)
def del_user(id, db: Session = Depends(get_db)):
    db_item = crud.delete_cart_item_by_id(db, id=id)
    if db_item:
        raise HTTPException(status_code=200, detail="Item deleted")
    else:
        raise HTTPException(status_code=400, detail="Item Not found!")
    return
