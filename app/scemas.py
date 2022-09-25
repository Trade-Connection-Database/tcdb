from pydantic import BaseModel
from datetime import datetime
from .enums import NodeType, EdgeType
from .database import BaseModel as TypesenseBaseModel
from typesense_orm import int32, Field, int64
from typing import Optional, Literal


class GeneralNode(BaseModel):
    full_name: str = Field(..., index=True)
    node_type: NodeType


class Event(GeneralNode):
    node_type: Literal[NodeType.EVENT]


class CorpFundPers(GeneralNode):
    node_type: Literal[NodeType.COMPANY, NodeType.FOUNDATION, NodeType.PERSON]
    country: int32  # by iso 3166 standard
    tax_id: str = Field(index=True)


class Person(CorpFundPers):
    node_type: Literal[NodeType.PERSON]


class CorpFund(CorpFundPers):
    node_type: Literal[NodeType.COMPANY, NodeType.FOUNDATION]
    address: str = Field(..., index=True)
    authorized_capital: int32
    date_found: datetime


class NodeIn(TypesenseBaseModel):
    full_name: str = Field(..., index=True)
    node_type: NodeType
    country: Optional[int32]  # by iso 3166 standard
    tax_id: Optional[str]
    address: Optional[str]
    authorized_capital: Optional[int32]
    date_of_being_found: Optional[int64]



class EdgeIn(BaseModel):
    edge_type: EdgeType
    start_id: int
    end_id: int
    proof: str
    date_proof: datetime



