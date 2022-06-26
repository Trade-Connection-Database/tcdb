from fastapi import Security, HTTPException
from fastapi.security.api_key import APIKeyHeader, APIKeyQuery
from starlette.status import HTTP_403_FORBIDDEN
from .database import SessionLocal, client
from .crud import NodeOperations, EdgeOperations


API_KEY = "samplekey"
API_KEY_NAME = "admin"

TYPESENSE_KEY_NAME = "X-TYPESENSE-API-KEY"

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)
typesense_api_key_header = APIKeyHeader(name=TYPESENSE_KEY_NAME, auto_error=False)
typesense_api_key_query = APIKeyQuery(name=TYPESENSE_KEY_NAME.lower(), auto_error=False)


async def get_api_key(key_header: str = Security(api_key_header)):
    if API_KEY == key_header:
        return key_header
    else:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="invalid api key")


async def get_tcdb_or_typesense_key(key_header: str = Security(api_key_header),
                                    typesense_header: str = Security(typesense_api_key_header),
                                    typesense_lower: str = Security(typesense_api_key_query),
                                    path: str = None):
    print(typesense_header)
    if API_KEY in [key_header, typesense_header, typesense_lower] or path == "health":
        return API_KEY
    else:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="neither tcdb key nor typesense key were provided")


async def get_node_operations():
    db = SessionLocal()
    try:
        yield NodeOperations(db, client)
    finally:
        await db.close()


async def get_edge_operations():
    db = SessionLocal()
    try:
        yield EdgeOperations(db, client)
    finally:
        await db.close()
