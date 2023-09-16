#!/usr/bin/python3
"""
    Print the State object with the name passed as an argument
    from the database using SQLAlchemy
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    search_name = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(mysql_username,
                                   mysql_password,
                                   database_name), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_search = (session.query(State)
                    .filter(State.name == search_name).first())

    if state_search:
        print(state_search.id)
    else:
        print("Not Found")

    session.close()
