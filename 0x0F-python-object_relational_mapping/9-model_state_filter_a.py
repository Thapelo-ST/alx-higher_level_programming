#!/usr/bin/python3
"""
    print all states filtered with letter a
    using sqlalchemy
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # making engine for DB
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(mysql_username, mysql_password,
                                   database_name), pool_pre_ping=True)
    # session for DB
    Session = sessionmaker(bind=engine)
    session = Session()
    # print all state objects by id ascending order
    states_filter = (session.query(State).filter(State.name.like('%a%')).
                     order_by(State.id).all())

    for state in states_filter:
        print("{}: {}".format(state.id, state.name))

    session.close()
