from enum import Enum


class NodeType(Enum):
    EVENT = 1
    PERSON = 2
    FOUNDATION = 3
    COMPANY = 4


class EdgeType(Enum):
    TRADE_DEAL = 1
    OWNERSHIP = 2
    AFFILIATION = 3