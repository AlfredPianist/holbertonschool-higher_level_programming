#!/usr/bin/python3
"""Script that deletes states that has an 'a' in its name
from the database hbtn_0e_6_usa."""
from sys import argv
from model_state import State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user, password, dbname = argv[1], argv[2], argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(user, password, dbname), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).filter(State.name.like('%a%')).all():
        session.delete(state)

    session.commit()
    session.close()
