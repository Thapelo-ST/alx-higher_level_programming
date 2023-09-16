#!/usr/bin/python3
"""
    print first state in table states
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
    # getting first state
    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    session.close()
