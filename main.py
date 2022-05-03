from fastapi import FastAPI
from routers import html_router, write_router


app = FastAPI()

app.include_router(html_router.router)
app.include_router(write_router.router)

