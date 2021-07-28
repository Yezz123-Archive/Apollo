#!/usr/bin/python3
from sqlalchemy.orm import Session
from models import models
from schemas import schemas
import bcrypt
import requests
from requests.auth import HTTPBasicAuth
import json
from datetime import datetime
import base64


# Get user by username function


def get_user_by_username(db: Session, username: str):
    return db.query(models.UserInfo).filter(models.UserInfo.username == username).first()

# User registration function


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = bcrypt.hashpw(
        user.password.encode('utf-8'), bcrypt.gensalt())
    db_user = models.UserInfo(username=user.username,
                              password=hashed_password, fullname=user.fullname)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Login Function


def get_Login(db: Session, username: str, password: str):
    db_user = db.query(models.UserInfo).filter(
        models.UserInfo.username == username).first()
    print(username, password)
    passw = bcrypt.checkpw(password.encode('utf-8'), db_user.password)
    return passw

# Get item by id function


def get_item_by_id(db: Session, id: int):
    return db.query(models.ItemInfo).filter(models.ItemInfo.id == id).first()

# Add items to DB function


def add_table(db: Session, item: schemas.ItemInfo):
    db_item = models.ItemInfo(itemname=item.itemname, itemprice=item.itemprice)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Delete item from DB by id function


def delete_item_by_id(db: Session, id: int):
    delitem = db.query(models.ItemInfo).filter(
        models.ItemInfo.id == id).first()
    if delitem is None:
        return
    db.delete(delitem)
    db.commit()
    return delitem

# Add to cart function


def add_to_cart(db: Session, username: str, items: models.CartInfo):
    user = db.query(models.UserInfo).filter(
        models.UserInfo.username == username).first()
    db_cart = models.CartInfo(
        ownername=user.id, itemname=items.itemname, itemprice=items.itemprice)
    db.add(db_cart)
    db.commit()
    db.refresh(db_cart)
    return db_cart

# Delete item in the cart by id


def delete_cart_item_by_id(db: Session, id: int):
    delitem = db.query(models.CartInfo).filter(
        models.CartInfo.id == id).first()
    if delitem is None:
        return
    db.delete(delitem)
    db.commit()
    return delitem

# money processing function(Not Complete Yet)


def payment(db: Session, phone_number: int, total: int):
    consumer_key = 'consumer_key'
    consumer_secret = 'consumer_secret'
    api_URL = 'https://api-m.sandbox.paypal.com/v1/payments'

    req = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    money_access_token = json.loads(req.text)
    validated_money_access_token = money_access_token['access_token']

    time = datetime.now().strftime('%Y%m%d%H%M%S')
    Business_code = 'short_code'  # replace with the business short code
    passkey = "pass_key"
    data_to_encode = Business_code + passkey + time
    online_password = base64.b64encode(data_to_encode.encode())
    decode_password = online_password.decode('utf-8')

    access_token = validated_money_access_token
    api_url = "https://api-m.sandbox.paypal.com/v1/payments/payment?count=10&start_index=0&sort_by=create_time&sort_order=desc"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": Business_code,
        "Password": decode_password,
        "Timestamp": time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": total,
        "PhoneNumber": phone_number,
        "CallBackURL": "https://127.0.0.1:8000/callback",  # Money Callback
        "AccountReference": "User Payment",
        "TransactionDesc": "Testing stk push"
    }
    response = requests.post(api_url, json=request, headers=headers)
    return response.text
