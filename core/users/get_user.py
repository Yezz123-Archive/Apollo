#!/usr/bin/python3
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from data import database

# import locale files
from schemas import schemas
from api import crud
from data.database import get_db

router = APIRouter(
    tags=["Users"],
    prefix="/user"
)
get_db = database.get_db

# get user by username API


@router.get("/get_user/{username}", response_model=schemas.UserInfo)
def get_user(username, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=username)
    return db_user
