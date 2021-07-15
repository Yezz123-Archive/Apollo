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

# delete item by id API


@router.delete("/del_item/{id}", response_model=schemas.ItemAInfo)
def del_user(id, db: Session = Depends(get_db)):
    db_item = crud.delete_item_by_id(db, id=id)
    if db_item:
        raise HTTPException(status_code=200, detail="Item found to delete")
    else:
        raise HTTPException(status_code=400, detail="Item Not found to delete")
    return
