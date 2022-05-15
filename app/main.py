from fastapi import FastAPI
from .routers import html_router, write_router
from .database import engine, Base

app = FastAPI()

app.include_router(html_router.router)
app.include_router(write_router.router)


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        pass


@app.on_event("shutdown")
async def shutdown():
    await engine.dispose()

