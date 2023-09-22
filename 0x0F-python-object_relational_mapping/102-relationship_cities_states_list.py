#!/usr/bin/python3
"""
Script to list all City objects from the database hbtn_0e_101_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Accept and assign arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # SQLAlchemy engine and session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password,
                                   db_name), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and list all City objects
    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
