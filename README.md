![apollo](.github/header.svg)

# Apollo - Auth

A basic Application with multiple functionalities built with FastAPI aim to help Users Buy New Items Provided by PaypalAPI to Complete the Payment and Check it.

## Getting Started

### Prerequisites

- Python 3.9.2 or higher
- FastAPI
- Docker

### Project setup

```sh
# clone the repo
$ git clone https://github.com/yezz123/Apollo-Auth.git

# move to the project folder
$ cd Apollo-Auth
```

### Creating virtual environment

- Install `pipenv` a global python project `pip install pipenv`
- Create a `virtual environment` for this project

```shell
# creating pipenv environment for python 3
$ pipenv --three

# activating the pipenv environment
$ pipenv shell

# if you have multiple python 3 versions installed then
$ pipenv install -d --python 3.8

# install all dependencies (include -d for installing dev dependencies)
$ pipenv install -d
```

### Running the Application

- To run the [Main](main.py) we need to use [uvicorn](https://www.uvicorn.org/) a lightning-fast ASGI server implementation, using uvloop and httptools.

```sh
# Running the application using uvicorn
$ uvicorn main:app

## To run the Application under a reload enviromment use -- reload
$ uvicorn main:app --reload
```

- You can Now Start using the Application, i use of the `/index` a simple Template based on this : <https://codepen.io/ma_suwa/pen/QWWqJBK>

```py
@app.get("/", response_class=HTMLResponse)
def index():
```

### Configured Enviromment

- To Provide a good work, i choose a `SQLite` Database using `SQLAlchemy`.
- If you want to configure the Database with an other Provider like `MySQL` or `PostgreSQL` you can change the `Database_URL` here :

- [Database.py](data/database.py) :

```py
# here you need to inster the  URI that should be used for the connection.
SQLALCHEMY_DATABASE_URL = 'sqlite:///apollo.db'
```

- For Example : 

```py
SQLALCHEMY_DATABASE_URL = 'mysql://username:password@server/apollo'
```

- For the Routes i register all the routes at the main file to create a good Path Flow for the Project.
- [main.py](main.py) :

```py
# includes all users routes
app.include_router(register.router)
app.include_router(login.router)
app.include_router(get_user.router)

# includes all items routes
app.include_router(add_item.router)
app.include_router(get_item.router)
app.include_router(delete_item.router)

# includes all cart 
app.include_router(add_to_cart.router)
app.include_router(payment.router)
app.include_router(delete_cart_item.router)
```

- Then i pre-configured the Cruds with the payment process that PaypalAPI provide, you can read the Official docs here [REST APIs / API Requests](https://developer.paypal.com/docs/api/reference/api-requests/)
- [Cruds.py](api/crud.py) :

```py
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
        "PartyA": phone_number,
        "PartyB": Business_code,
        "PhoneNumber": phone_number,
        "CallBackURL": "https://127.0.0.1:8000/callback",  # Money Callback
        "AccountReference": "User Payment",
        "TransactionDesc": "Testing stk push"
    }
    response = requests.post(api_url, json=request, headers=headers)
    return response.text
```

## Running the Docker Container

- We have the Dockerfile created in above section. Now, we will use the Dockerfile to create the image of the FastAPI app and then start the FastAPI app container.

```sh
$ docker build
```

- list all the docker images and you can also see the image `nectus:latest` in the list.

```sh
$ docker images
```

- run the application at port 5000. The various options used are:

> - `-p`: publish the container's port to the host port.
> - `-d`: run the container in the background.
> - `-i`: run the container in interactive mode.
> - `-t`: to allocate pseudo-TTY.
> - `--name`: name of the container

```sh
$ docker container run -p 5000:5000 -dit --name Apollo apollo-auth:latest
```

- Check the status of the docker container

```sh
$ docker container ps
```

## Preconfigured Packages

Includes preconfigured packages to kick start fastAPI app by just setting appropriate configuration.

| Package                                                      | Usage                                                                                                                           |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| [uvicorn](https://www.uvicorn.org/)                          | a lightning-fast ASGI server implementation, using uvloop and httptools.                                                        |
| [PaypalAPI](https://developer.paypal.com/docs/api/overview/) | exchange these credentials for an access token that authorizes your REST API calls. To test your web and mobile apps.           |
| [SQLAlchemy](https://www.sqlalchemy.org/)                    | is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL. |
| [starlette](https://www.starlette.io/)                       | a lightweight ASGI framework/toolkit, which is ideal for building high performance asyncio services.                            |

`yapf` packages for `linting and formatting`

## License

This program is free software under MIT license. Please see the [LICENSE](LICENSE) file in our repository for the full text.
