#!/usr/bin/python3
"""
    change name of state id 2 to New Mexico
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

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(mysql_username,
                                   mysql_password,
                                   database_name), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    # query state object change name of state id 2
    update = session.query(State).filter(State.id == 2).first()

    if update:
        # change name
        update.name = "New Mexico"
        # commit changes
        session.commit()
    else:
        print("Not found")
    session.close()
