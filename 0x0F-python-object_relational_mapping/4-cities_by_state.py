#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""4-cities_by_state.py

Script that prints all cities with their states.
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    argc = len(argv) - 1

    if (argc == 3):
        user, password, dbname = argv[1], argv[2], argv[3]

        db = MySQLdb.connect(host="localhost", port=3306,
                             db=dbname, charset="utf8",
                             user=user, passwd=password)

        cur = db.cursor()
        cur.execute("""SELECT cities.id, cities.name, states.name
                    FROM cities
                    JOIN states
                    ON cities.state_id = states.id
                    ORDER by cities.id ASC""")

        rows = cur.fetchall()
        for row in rows:
            print(row)

        cur.close()
        db.close()
