#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""3-my_safe_filter_states.py

Script that filters the states from user input, without risk of an
SQL injection.
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    argc = len(argv) - 1

    if (argc == 4):
        user, password, dbname, query = argv[1], argv[2], argv[3], argv[4]

        db = MySQLdb.connect(host="localhost", port=3306,
                             db=dbname, charset="utf8",
                             user=user, passwd=password)

        cur = db.cursor()
        cur.execute("""SELECT * FROM states
                    WHERE states.name=%s
                    ORDER BY states.id""", (query,))

        rows = cur.fetchall()
        for row in rows:
            print(row)

        cur.close()
        db.close()
