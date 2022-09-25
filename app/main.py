from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routers import html_router, write_router, typesense_redirect
from .database import engine, Base, client

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(html_router.router)
app.include_router(write_router.router)
app.include_router(typesense_redirect.router)


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        pass


@app.on_event("shutdown")
async def shutdown():
    await engine.dispose()

