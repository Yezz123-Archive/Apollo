#!/usr/bin/python3
from sqlalchemy import Column, Integer, String
from data.database import Base

# User Database Model


class UserInfo(Base):
    __tablename__ = "user_info"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    fullname = Column(String, unique=True)

# Items Database Model


class ItemInfo(Base):
    __tablename__ = "item_info"

    id = Column(Integer, primary_key=True, index=True)
    itemname = Column(String, unique=True)
    itemprice = Column(Integer)


# Cart Database Model


class CartInfo(Base):
    __tablename__ = "cart_info"

    id = Column(Integer, primary_key=True, index=True)
    ownername = Column(Integer, unique=True)
    itemname = Column(String, unique=True)
    itemprice = Column(Integer)
