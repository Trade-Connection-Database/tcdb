from crud import NodeOperations, EdgeOperations
from fastapi import APIRouter, Depends
from fastapi.security.api_key import APIKey
from scemas import NodeIn, EdgeIn
from typing import List
from dependencies import get_api_key, get_node_operations, get_edge_operations

router = APIRouter(prefix="/api/write")


@router.post("/add_nodes")
async def add_nodes(nodes: List[NodeIn],
                    api_key: APIKey = Depends(get_api_key),
                    db: NodeOperations = Depends(get_node_operations)):
    node_ids = await db.add(nodes)
    return list(node_ids)


@router.post("/add_edges")
async def add_edges(edges: List[EdgeIn],
                    api_key: APIKey = Depends(get_api_key),
                    db: EdgeOperations = Depends(get_edge_operations)):
    proof_ids = await db.add(edges)
    return proof_ids




