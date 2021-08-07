#!/usr/bin/python3
"""Script that adds the state 'California' binded to the city 'San Francisco'
to the database hbtn_0e_100_usa."""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City
from sys import argv


if __name__ == "__main__":
    user, password, dbname = argv[1], argv[2], argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(user, password, dbname), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name='California')
    city = City(name='San Francisco', state=state)
    session.add(city)
    session.commit()

    session.close()
