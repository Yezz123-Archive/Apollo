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

# add to cart by username and the items to be added API
@router.post("/add_to_cart/{username}", response_model=schemas.CartOwnerInfo)
def add_item(username, items: schemas.CartInfo, db: Session = Depends(get_db)):
    db_cart = crud.add_to_cart(db=db, username=username, items=items)
    if db_cart:
        raise HTTPException(status_code=200, detail="Registered to The Cart")
    return {"Cart": "Item Not Registered to the Cart!"}
