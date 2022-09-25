from fastapi import APIRouter, Depends, Request
from fastapi.responses import StreamingResponse
from ..dependencies import get_tcdb_or_typesense_key, TYPESENSE_KEY_NAME
from ..database import client
from fastapi.security.api_key import APIKey

router = APIRouter(prefix="/search")


async def _proxy(request: Request, path: str):
    new_headers = dict(**request.headers)
    new_headers.pop(TYPESENSE_KEY_NAME, None)
    new_headers.pop(TYPESENSE_KEY_NAME.lower(), None)
    new_headers["accept-encoding"] = "deflate"
    resp = await client.api_caller.session.request(request.method, "/" + path, data=await request.body(),
                                                   headers=new_headers)

    response = StreamingResponse(resp.content, status_code=resp.status, headers=resp.headers, media_type="application/json")
    return response


@router.api_route("{path}", methods=["GET", "POST", "PUT", "DELETE"])
async def redirect_without_port(request: Request, path: str,
                                #api_key: APIKey = Depends(get_tcdb_or_typesense_key)
                                ):
    return await _proxy(request, path)


@router.get("/search:{port}/health")
async def do_healthcheck(request: Request, port: int):
    return await _proxy(request, "health")
