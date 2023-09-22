#!/usr/bin/python3
"""
this module prints all State objects and corresponding City objects, contained
in the db hbtn_0e_101_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    username = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, passwd,
                                   db_name), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # gather results for the states objects and corresponding city objects
    res = (session.query(State, City)
           .filter(State.id == City.state_id)
           .order_by(State.id, City.id)
           .all())

    # print results
    current_state_id = None
    for state, city in res:
        if state.id != current_state_id:
            if current_state_id is not None:
                print()
            print("{}: {}".format(state.id, state.name))
            current_state_id = state.id
        print("\t{}: {}".format(city.id, city.name))

    session.close()
