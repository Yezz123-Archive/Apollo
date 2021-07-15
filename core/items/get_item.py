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

# get item by id API


@router.get("/get_item/{id}", response_model=schemas.ItemAInfo)
def get_user(id, db: Session = Depends(get_db)):
    db_item = crud.get_item_by_id(db, id=id)
    if db_item is None:
        raise HTTPException(status_code=400, detail="No item found")
    return db_item
