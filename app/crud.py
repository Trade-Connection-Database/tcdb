from .models import Node, Edge, Proof
from .scemas import NodeIn, Event, CorpFund, Person, EdgeIn
from typing import List, Tuple, Union
from sqlalchemy.ext.asyncio import AsyncSession
from typesense_orm import Client, ApiCallerAsync
from sqlalchemy.dialects import postgresql
from sqlalchemy.future import select
from sqlalchemy.sql import text
from abc import ABC, abstractmethod


class DBOperator(ABC):
    def __init__(self, db_session: AsyncSession, api_client: Client[ApiCallerAsync]):
        self.db_session = db_session
        self.typesense_client = api_client


class NodeOperations(DBOperator):
    async def add(self, nodes: List[Union[Person, CorpFund, Event]]):
        db_nodes = list(map(lambda node: Node(**node.dict()), nodes))
        self.db_session.add_all(db_nodes)
        # await self.db_session.stream(Node.insert(), nodes)
        # for response streaming
        await self.db_session.commit()
        list_of_entries = list(map(lambda a: NodeIn(**a.dict()), nodes))
        res = await self.typesense_client.import_objects(list_of_entries)
        print("IMPORT RES")
        async for item in res:
            print(item)
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
