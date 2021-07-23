#!/usr/bin/python3

from fastapi import FastAPI
from starlette.responses import HTMLResponse

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
# but we will Custom our Response
@app.get("/", response_class=HTMLResponse)
def index():
    
    # This is a simple Template for the index ,
    # based on this : https://codepen.io/ma_suwa/pen/QWWqJBK
    return """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="shortcut icon" type="image/icon"
        href="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Apollo_13-insignia.png/1022px-Apollo_13-insignia.png" />
    <style>
        * {
            margin: 0;
            padding: 0;
        }

        html,
        body {
            box-sizing: border-box;
            height: 100%;
            width: 100%;
        }

        body {
            background: #FFF;
            font-family: 'fantasy', emoji;
            font-weight: 400;
        }

        .buttons {
            display: flex;
            flex-direction: row;
            flex-wrap: wrap;
            justify-content: center;
            text-align: center;
            width: 100%;
            height: 100%;
            margin: 0 auto;
            /*   padding: 2em 0em; */
        }

        .container {
            align-items: center;
            display: flex;
            flex-direction: column;
            justify-content: center;
            text-align: center;
            background-color: #FFF;
            padding: 40px 0px;
            width: 240px;
        }

        h1 {
            text-align: left;
            color: #444;
            letter-spacing: 0.05em;
            margin: 0 0 0.4em;
            font-size: 1em;
        }

        p {
            text-align: left;
            color: #444;
            letter-spacing: 0.05em;
            font-size: 0.8em;
            margin: 0 0 2em;
        }


        .btn {
            letter-spacing: 0.1em;
            cursor: pointer;
            font-size: 14px;
            font-weight: 400;
            line-height: 45px;
            max-width: 160px;
            position: relative;
            text-decoration: none;
            text-transform: uppercase;
            width: 100%;
        }

        .btn:hover {
            text-decoration: none;
        }

        /*btn_background*/
        .effect04 {
            --uismLinkDisplay: var(--smLinkDisplay, inline-flex);
            display: var(--uismLinkDisplay);
            color: #000;
            outline: solid 2px #000;
            position: relative;
            transition-duration: 0.4s;
            overflow: hidden;
        }

        .effect04::before,
        .effect04 span {
            margin: 0 auto;
            transition-timing-function: cubic-bezier(0.86, 0, 0.07, 1);
            transition-duration: 0.4s;
        }

        .effect04:hover {

            background-color: #000;
        }

        .effect04:hover span {
            -webkit-transform: translateY(-400%) scale(-0.1, 20);
            transform: translateY(-400%) scale(-0.1, 20);
        }


        .effect04::before {
            content: attr(data-sm-link-text);
            color: #FFF;
            position: absolute;
            left: 0;
            right: 0;
            margin: auto;
            -webkit-transform: translateY(500%) scale(-0.1, 20);
            transform: translateY(500%) scale(-0.1, 20);
        }

        .effect04:hover::before {
            letter-spacing: 0.05em;
            -webkit-transform: translateY(0) scale(1, 1);
            transform: translateY(0) scale(1, 1);
        }
    </style>
    <title>Apollo-Auth</title>
</head>

<body>
    <div class="buttons">
        <div class="container">
            <h1>Apollo-Auth</h1>
            <p>Get Started</p>
            <a href="/docs" class="btn effect04" data-sm-link-text="SwaggerUI"><span>FastAPI</span></a>
        </div>
    </div>
</body>

</html>
"""
