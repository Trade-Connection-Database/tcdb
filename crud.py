import models
import scemas
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession


class NodeOperations:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def add(self, nodes: List[scemas.NodeIn]):
        db_nodes = list(map(lambda node: models.Node(**node.dict()), nodes))
        self.db_session.add_all(db_nodes)
        await self.db_session.commit()
        return map(lambda node: node.id, db_nodes)

