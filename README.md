# INTALATION AND SETUP

pipenv install

# RUN API

pipenv run uvicorn main:app

# TEST ENDPOINT

curl -v -X POST -H "Content-Type: application/json" -d "{\"key\": \"foo\", \"value\":\"bar\"}" "http://127.0.0.1:8000/"

# AUTOMATED TESTSING

pipenv run pytest main.py

# RUN LINTERS

pipenv run pre-commit
