# INTALATION AND SETUP

```sh
pipenv install
```

# RUN API

```sh
pipenv run uvicorn main:app
```

# TEST ENDPOINT

```sh
curl -v -X POST -H "Content-Type: application/json" -d "{\"key\": \"foo\", \"value\":\"bar\"}" "http://127.0.0.1:8000/"
```
# AUTOMATED TESTSING

```sh
pipenv run pytest main.py
```

# RUN LINTERS

```sh
pipenv run pre-commit
```
