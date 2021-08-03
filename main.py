#!/usr/bin/python3

from fastapi import FastAPI, Request
from starlette.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# import locale files
from models import models
from data.database import engine

# import router files
from core.cart import add_to_cart, delete_cart_item, payment
from core.items import add_item, delete_item, get_item
from core.users import login, register, get_user

# Create the database tables
models.Base.metadata.create_all(bind=engine)

# Create the instance
app = FastAPI(
    title="Apollo - Auth",
    description="A basic Application with multiple functionality",
    version="1.0.0",
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# includes all users routes
app.include_router(login.router)
app.include_router(register.router)
app.include_router(get_user.router)

# includes all items routes
app.include_router(add_item.router)
app.include_router(get_item.router)
app.include_router(delete_item.router)

# includes all cart
app.include_router(add_to_cart.router)
app.include_router(payment.router)
app.include_router(delete_cart_item.router)

# By default FastAPI return the response using JSONResponse,
# but we will Custom our Response using the HTMLResponse
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
