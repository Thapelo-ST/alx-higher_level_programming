#!/usr/bin/python3
"""
    delete all states filtered with letter a
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
    # deleting all state objects by id ascending order
    states_filter_delete = (session.query(State).filter(State.name.like('%a%'))
                            .delete())

    # commit changes to database
    session.commit()

    # count states deleted
    # print(states_filter_delete)
    session.close()
