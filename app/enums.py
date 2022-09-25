from enum import Enum, IntEnum


class NodeType(IntEnum):
    EVENT = 1
    PERSON = 2
    FOUNDATION = 3
    COMPANY = 4


class EdgeType(IntEnum):
    TRADE_DEAL = 1
    OWNERSHIP = 2
    AFFILIATION = 3
    EMPLOYMENT = 4
    PERSONAL_RELATION = 5
