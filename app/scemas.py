from pydantic import BaseModel
from datetime import datetime
from .enums import NodeType, EdgeType
from .database import BaseModel as TypesenseBaseModel
from typesense_orm import int32, Field


class NodeIn(TypesenseBaseModel):
    name: str = Field(..., index=True)
    node_type: NodeType
    country: int32  # by iso 3166 standard
    in_country_id: str


class EdgeIn(BaseModel):
    edge_type: EdgeType
    start_id: int
    end_id: int
    proof: str
    date_proof: datetime



