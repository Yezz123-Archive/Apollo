#!/usr/bin/python3
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
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


# login API


@router.post("/login")
def login_user(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = crud.get_Login(
        db, username=user.username, password=user.password)
    if db_user == False:
        raise HTTPException(status_code=400, detail="Wrong username or password")
    return {"message": "User found"}
