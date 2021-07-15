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

# payment API
@router.post("/payment")
def add_item(userphone: schemas.UserPayment, db: Session = Depends(get_db)):
    user_payment = crud.payment(
        db=db, phone_number=userphone.phonenumber, total=userphone.total)
    if user_payment:
        raise HTTPException(status_code=200, detail="payment Started")
    return

# Callback API
@router.post("/callback")
def money_callback(db: Session = Depends(get_db)):
    return {'success': "Payment was made successfully"}
