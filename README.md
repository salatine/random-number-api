# random-number-api

Basic API written in Python using Flask, which provides a random number, between min and max.

## Setup
We use [Poetry](https://python-poetry.org/docs/#installation) to manage dependencies. After installing it, create a venv for this project and install the dependencies by running the following:
```
$ poetry shell
$ poetry install
```

## Run
To run the API, run the following:
```
$ python random-number-api/app.py
```

## Usage
The API has two endpoints:
- `/randomNumber/<min>/<max>` - returns a random number between min and max, if an API key is provided in the `Authorization` header.
- `/randomNumber` - a form to register an API key.

For example, to get a random number between 1 and 10, you can run the following, where API-KEY is the API key:
```
curl -H "Authorization: "API-KEY" http://127.0.0.1:5000/randomNumber/1/10
```

And this will return the random number in the header contents:
```
> GET /randomNumber/1/100 HTTP/1.1
> Host: 127.0.0.1:5000
> User-Agent: curl/8.4.0
> Accept: */*
> Authorization: 4a916cc4-ddf2-4f7c-88f7-047ffde2c09a
> 
< HTTP/1.1 200 OK
< Server: Werkzeug/3.0.1 Python/3.11.5
< Date: Sun, 12 Nov 2023 18:05:14 GMT
< Content-Type: application/json
< Content-Length: 3
< Connection: close
< 
63
```

