from database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum, \
    UniqueConstraint, PrimaryKeyConstraint, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from enums import NodeType, EdgeType


class Node(Base):
    __tablename__ = "nodes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    node_type = Column(Enum(NodeType))
    country = Column(Integer)
    in_country_id = Column(String)
    __table_args__ = (UniqueConstraint("country", "in_country_id", name="international_id"),)


class Edge(Base):
    __tablename__ = "edges"
    edge_type = Column(Enum(EdgeType))
    start_id = Column(Integer, ForeignKey("nodes.id"))
    start = relationship("Node", backref="outgoing", foreign_keys=[start_id])
    end_id = Column(Integer, ForeignKey("nodes.id"))
    end = relationship("Node", backref="ingoing", foreign_keys=[end_id])

    __table_args__ = (PrimaryKeyConstraint("start_id", "end_id", name="direction"),)


class Proof(Base):
    __tablename__ = "proofs"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime)
    proof = Column(String)
    start_id = Column(Integer)
    end_id = Column(Integer)
    __table_args__ = (ForeignKeyConstraint((start_id, end_id), (Edge.start_id, Edge.end_id), name="edge"),)


