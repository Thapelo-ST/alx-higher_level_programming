#!/usr/bin/python3
"""
Script to list cities with state names and city IDs in ascending order.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # accept and assign arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # SQLAlchemy engine and session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(mysql_username, mysql_password,
                                   database_name), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # sort cities, states by city ID
    results = (session.query(City, State).filter(City.state_id == State.id)
               .order_by(City.id).all())

    # display results
    for city, state in results:
        print("{}:({}) {}".format(state.name, city.id, city.name))

    session.close()
