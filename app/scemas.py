from pydantic import BaseModel
from datetime import datetime
from .enums import NodeType, EdgeType


class NodeIn(BaseModel):
    name: str
    node_type: NodeType
    country: int  # by iso 3166 standard
    in_country_id: str


class EdgeIn(BaseModel):
    edge_type: EdgeType
    start_id: int
    end_id: int
    proof: str
    date_proof: datetime



