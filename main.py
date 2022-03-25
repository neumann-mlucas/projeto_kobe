import pytest
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.testclient import TestClient
from pydantic import BaseModel
from starlette.datastructures import MutableHeaders

app = FastAPI()


class Payload(BaseModel):
    key: str
    value: str


@app.post("/")
def main(request: Request, payload: Payload):
    new_header = MutableHeaders(request._headers)
    new_header[payload.key] = payload.value
    # avoid mismatch between header and response
    del new_header["Content-Length"]

    # not sure if the modify header should be the endpoint return or the header
    # of the response, so i'm doing both
    return JSONResponse(content=dict(new_header), headers=new_header)


# AUTOMATED TESTING

client = TestClient(app)


def test_main():
    response = client.post(
        "/",
        headers={"Content-Type": "application/json"},
        json={"key": "KEY", "value": "VALUE"},
    )
    # endpint exists
    assert response.status_code == 200
    # key:value in response headers
    assert "KEY" in response.headers
    assert "VALUE" in response.headers["KEY"]
    # check if response and request headers are similar
    # cannot be strictly the same 'cos Content-Length and key:value
    keys = response.request.headers.keys()
    for key in [key for key in keys if not key == "Content-Length"]:
        assert response.headers[key] == response.request.headers[key]
