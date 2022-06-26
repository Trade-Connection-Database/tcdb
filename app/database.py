from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
import os
from typesense_orm import Node, Client, ApiCallerAsync, create_base_model

db_url = os.environ["DATABASE_URL"]
engine = create_async_engine(db_url, future=True, echo=True)
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()


typesense_url = os.environ["TYPESENSE_URL"]
node = Node(url=typesense_url)
client = Client[ApiCallerAsync](api_key="abcd", nodes=[node])
client.start()

try:
    client.delete_collection("nodein")
except Exception:
    pass

BaseModel = create_base_model(client)
