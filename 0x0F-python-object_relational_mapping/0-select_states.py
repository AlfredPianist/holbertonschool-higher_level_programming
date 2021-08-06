#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""0-select_states.py

Script that prints all the states in the states table usign the MySQLdb
python module.
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
        cur.execute("SELECT * FROM states ORDER BY states.id ASC")

        rows = cur.fetchall()
        for row in rows:
            print(row)

        cur.close()
        db.close()
