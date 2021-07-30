![apollo](.github/header.svg)

# Apollo

A basic Application with multiple functionalities built with FastAPI aim to help Users Buy New Items Provided by PaypalAPI to Complete the Payment and Check it.

## Getting Started

Apollo provide a Basic API Compose :

<ol>
    <li>Users</li>
<ol>
        <li>login : <code>http://localhost:8000 user/login</code> </li>
        <li>Register : <code>http://localhost:8000/user/register</code></li>
        <li>Get User : <code>http://localhost:8000/user/get_user/{username}</code></li>
</ol>
    <li>Items</li>
<ol>
        <li>Add Item : <code>http://localhost:8000/item/add_item</code></li>
        <li>Get Item : <code>http://localhost:8000/item/get_item/{id}</code></li>
        <li>Delete Item : <code>http://localhost:8000/item/get_item/{id}</code></li>
</ol>
    <li>Payment</li>
<ol>
        <li>Add Item to Cart : <code>http://localhost:8000/cart/add_to_cart/{username}</code></li>
        <li>Provide Item to Payments : <code>http://localhost:8000/cart/payment</code></li>
        <li>Money Callback : <code>http://localhost:8000/cart/callback</code></li>
        <li>Delete Cart Item : <code>http://localhost:8000/cart/delete_cart_item/{id}</code></li>
</ol>
</ol>

> I pre-configured the Cruds with the payment process based on `PaypalAPI`, you can read the Official docs here [REST APIs / API Requests](https://developer.paypal.com/docs/api/reference/api-requests/)

### Prerequisites

- Python 3.9.2 or higher
- FastAPI
- Docker

### Project setup

```sh
# clone the repo
$ git clone https://github.com/yezz123/Apollo.git

# move to the project folder
$ cd Apollo
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

- Here we can Switch Between using [SWAGGER UI](https://swagger.io/tools/swagger-ui/) or [Redoc](https://redocly.github.io/redoc/) to Play around the API.

- You can Now Start using the Application, i use a simple Template for the `index` file to simply launch `/docs` : <https://codepen.io/ma_suwa/pen/QWWqJBK>

### Configured Enviromment

- To Provide a good work, i choose a `SQLite` Database using `SQLAlchemy`.
- If you want to configure the Database with an other Provider like `MySQL` or `PostgreSQL` you can change the `Database_URL` here :

- [Database.py](data/database.py) :

```py
# here you need to insert the Connection URL.
SQLALCHEMY_DATABASE_URL = 'sqlite:///apollo.db'
```

- For Example

```py
SQLALCHEMY_DATABASE_URL = 'mysql://username:password@server/apollo'
```

## Running the Docker Container

- We have the Dockerfile created in above section. Now, we will use the Dockerfile to create the image of the FastAPI app and then start the FastAPI app container.

```sh
$ docker build
```

- list all the docker images and you can also see the image `apollo:latest` in the list.

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
$ docker container run -p 5000:5000 -dit --name Apollo apollo:latest
```

- Check the status of the docker container

```sh
$ docker container ps
```

## Preconfigured Packages

Includes preconfigured packages to kick start Apollo API by just setting appropriate configuration.

| Package                                                      | Usage                                                                                                                           |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| [uvicorn](https://www.uvicorn.org/)                          | a lightning-fast ASGI server implementation, using uvloop and httptools.                                                        |
| [PaypalAPI](https://developer.paypal.com/docs/api/overview/) | exchange these credentials for an access token that authorizes your REST API calls. To test your web and mobile apps.           |
| [SQLAlchemy](https://www.sqlalchemy.org/)                    | is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL. |
| [starlette](https://www.starlette.io/)                       | a lightweight ASGI framework/toolkit, which is ideal for building high performance asyncio services.                            |

`yapf` packages for `linting and formatting`

## Contributing

- Join the Apollo Creator and Contribute to the Project if you have any enhancement or add-ons to create a good and Secure Project, Help any User to Use it in a good and simple way.

## License

This program is free software under MIT license. Please see the [LICENSE](LICENSE) file in our repository for the full text.
