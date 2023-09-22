#!/usr/bin/python3
"""
    Module that contain a sqlalchemy declarative
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

mtd = MetaData()
Base = declarative_base(metadata=mtd)


class State(Base):
    """
    class state inheriting from Base declarative and using metadata used to
    store aspects of the db schema like columns, constraints etc
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    # Define the relationship to City with backref
    cities = relationship("City", backref="state")

