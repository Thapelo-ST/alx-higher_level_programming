#!/usr/bin/python3
"""
    Module that has class City that contain a sqlalchemy declarative Base
    imported from module_state
"""
from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
        class state inheriting from relationship_state declarative
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
