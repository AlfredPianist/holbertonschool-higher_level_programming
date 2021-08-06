#!/usr/bin/python3
"""Script that lists all States with their Citie names and ids
from database hbtn_0e_6_usa."""
from sys import argv
from model_state import State
from model_city import City

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user, password, dbname = argv[1], argv[2], argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(user, password, dbname), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state, city in session.query(State, City).join(City).\
            order_by(City.id).all():
        print("{}: ({:d}) {}".format(state.name, city.id, city.name))

    session.close()
