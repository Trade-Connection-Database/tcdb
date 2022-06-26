from fastapi import FastAPI, Request, Depends
from fastapi.responses import StreamingResponse
from fastapi.security.api_key import APIKey
from fastapi.staticfiles import StaticFiles
from .dependencies import get_tcdb_or_typesense_key, TYPESENSE_KEY_NAME
from .routers import html_router, write_router
from .database import engine, Base, client

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(html_router.router)
app.include_router(write_router.router)


async def _proxy(request: Request, path: str):
    new_headers = dict(**request.headers)
    new_headers.pop(TYPESENSE_KEY_NAME, None)
    new_headers.pop(TYPESENSE_KEY_NAME.lower(), None)
    new_headers["accept-encoding"] = "deflate"
    resp = await client.api_caller.session.request(request.method, "/" + path, data=await request.body(),
                                                   headers=new_headers)

    response = StreamingResponse(resp.content, status_code=resp.status, headers=resp.headers, media_type="application/json")
    return response


@app.api_route("/search:{port}/{path}", methods=["GET", "POST", "PUT", "DELETE"])
async def redirect_to_typesense(request: Request, path: str, port: int,
                                api_key: APIKey = Depends(get_tcdb_or_typesense_key)):
    return await _proxy(request, path)

@app.api_route("/search/{path}", methods=["GET", "POST", "PUT", "DELETE"])
async def redirect_without_port(request: Request, path: str,
                                api_key: APIKey = Depends(get_tcdb_or_typesense_key)):
    return await _proxy(request, path)



@app.api_route("/search:{port}/health")
async def do_healthcheck(request: Request, port: int):
    return await _proxy(request, "health")

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        pass


@app.on_event("shutdown")
async def shutdown():
    await engine.dispose()

