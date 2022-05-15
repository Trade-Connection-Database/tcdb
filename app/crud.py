from .models import Node, Edge, Proof
from .scemas import NodeIn, EdgeIn
from typing import List, Tuple
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.dialects import postgresql
from sqlalchemy.future import select
from sqlalchemy.sql import text
from abc import ABC, abstractmethod


class DBOperator(ABC):
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session


class NodeOperations(DBOperator):
    async def add(self, nodes: List[NodeIn]):
        db_nodes = list(map(lambda node: Node(**node.dict()), nodes))
        self.db_session.add_all(db_nodes)
        await self.db_session.commit()
        return map(lambda node: node.id, db_nodes)


class EdgeOperations(DBOperator):
    async def add(self, edges: List[EdgeIn]):
        proofs, edges = zip(*list(map(lambda edge: (
            Proof(date=edge.date_proof, proof=edge.proof, start_id=edge.start_id, end_id=edge.end_id),
            Edge(edge_type=edge.edge_type, start_id=edge.start_id, end_id=edge.end_id)), edges)))

        [await self.db_session.merge(edge) for edge in edges]
        clust = text("CLUSTER edges USING direction;")
        self.db_session.add_all(proofs)
        await self.db_session.commit()
        await self.db_session.execute(clust)
        await self.db_session.commit()
        return list(map(lambda proof: proof.id, proofs))
