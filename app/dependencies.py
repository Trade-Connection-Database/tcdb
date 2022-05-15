from fastapi import Security, HTTPException
from fastapi.security.api_key import APIKeyHeader
from starlette.status import HTTP_403_FORBIDDEN
from database import SessionLocal
from crud import NodeOperations, EdgeOperations


API_KEY = "samplekey"
API_KEY_NAME = "admin"

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


async def get_api_key(key_header: str = Security(api_key_header)):
    if API_KEY == key_header:
        return key_header
    else:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="invalid api key")


async def get_node_operations():
    db = SessionLocal()
    try:
        yield NodeOperations(db)
    finally:
        await db.close()


async def get_edge_operations():
    db = SessionLocal()
    try:
        yield EdgeOperations(db)
    finally:
        await db.close()
