from pydantic import BaseModel
from enum import Enum
from pycountry import countries

class NodeType(Enum):
    EVENT = 1
    PERSON = 2
    FOUNDATION = 3
    COMPANY = 4


class NodeIn(BaseModel):
    name: str
    node_type: NodeType

