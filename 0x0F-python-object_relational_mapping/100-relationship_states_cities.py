#!/usr/bin/python3
"""
Script to create a State object "California" with the City object "San Francisco"
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # accept and assign arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # SQLAlchemy engine and session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(mysql_username, mysql_password,
                                   database_name), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # create "california" state with "san francisco" city
    california = State(name='California')
    san_francisco = City(name='San Francisco')
    california.cities.append(san_francisco)
    # add and commit changes then close the session
    session.add(california)
    session.commit()

    session.close()
