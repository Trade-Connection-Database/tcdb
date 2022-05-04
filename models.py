from database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from enums import NodeType, EdgeType


class Node(Base):
    __tablename__ = "nodes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    node_type = Column(Enum(NodeType))
    country = Column(Integer)
    in_country_id = Column(String)


class Edge(Base):
    __tablename__ = "edges"
    id = Column(Integer, primary_key=True, index=True)
    edge_type = Column(Enum(EdgeType))
    start_id = Column(Integer, ForeignKey("nodes.id"))
    start = relationship("Node", backref="outgoing", foreign_keys=[start_id])
    end_id = Column(Integer, ForeignKey("nodes.id"))
    end = relationship("Node", backref="ingoing", foreign_keys=[end_id])


class Proof(Base):
    __tablename__ = "proofs"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime)
    proof = Column(String)
    edge_id = Column(Integer, ForeignKey("edges.id"))
    edge = relationship("Edge", backref="proofs")


