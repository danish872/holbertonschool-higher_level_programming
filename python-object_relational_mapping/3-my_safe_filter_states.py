#!/usr/bin/python3
"""
This script takes arguments and prints all values in
the hbtn_0e_0_usa state table where the name matches the argument.
But this time, write one that is safe from MySQL injections
    """

import MySQLdb
import sys


if __name__ == "__main__":
    """ Lists all states from the database hbtn_0e_0_usa
        """

    # Connect to the MySQL database
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8",
            port=3306
            )
    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute the SQL query to select all states ordered by id
    query = "SELECT * FROM states WHERE \
                name LIKE BINARY %s ORDER BY id ASC"
    cur.execute(query, (sys.argv[4],))
    rows = cur.fetchall()

    # print each row
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cur.close()
    db.close()
