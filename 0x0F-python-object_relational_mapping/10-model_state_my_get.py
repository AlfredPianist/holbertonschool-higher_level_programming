#!/usr/bin/python3
"""Script that lists the id of the State object entered by user."""
from sys import argv
from model_state import State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user, password, dbname, query = argv[1], argv[2], argv[3], argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(user, password, dbname), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State.id).filter(State.name == query).\
        order_by(State.id).first()
    if state:
        print("{:d}".format(state.id))
    else:
        print("Not found")

    session.close()
