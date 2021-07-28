#!/usr/bin/python3
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from data import database

# import locale files
from schemas import schemas
from api import crud
from data.database import get_db

router = APIRouter(
    tags=["Items"],
    prefix="/item"
)
get_db = database.get_db


# add items to DB API


@router.post("/add_item", response_model=schemas.ItemInfo)
def add_item(item: schemas.ItemInfo, db: Session = Depends(get_db)):
    db_item = crud.add_table(db=db, item=item)
    if db_item:
        raise HTTPException(status_code=200, detail="item registered")
    return {"Item": "Not Foundfound"}
