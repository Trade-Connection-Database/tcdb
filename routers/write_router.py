from fastapi import APIRouter, Security, HTTPException, Depends
from fastapi.security.api_key import APIKeyHeader, APIKey
from starlette.status import HTTP_403_FORBIDDEN

API_KEY = "samplekey"
API_KEY_NAME = "admin"

router = APIRouter(prefix="/api/write")

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


async def get_api_key(key_header: str = Security(api_key_header)):
    if API_KEY == key_header:
        return key_header
    else:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="invalid api key")


@router.post("/securitytest")
async def security_test(api_key: APIKey = Depends(get_api_key)):
    response = "I let you in"
    return response


