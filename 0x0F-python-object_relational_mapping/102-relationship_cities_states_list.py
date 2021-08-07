#!/usr/bin/python3
"""Script that lists all States with their City names and ids
from database hbtn_0e_101_usa."""
from sys import argv
from relationship_state import State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user, password, dbname = argv[1], argv[2], argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(user, password, dbname), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state, city in session.query(State, City).\
            join(City).order_by(City.id).all():
        print("{:d}: {} -> {}".format(city.id, city.name, state.name))

    session.close()
