#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""


import sys
import MySQLdb


if __name__ == "__main__":

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
    argument = sys.argv[4]
    # Execute the SQL query to list cities with their corresponding states
    cur.execute("SELECT cities.name \
                FROM cities \
                LEFT JOIN states ON cities.state_id = states.id \
                WHERE states.name = %s \
                ORDER BY cities.id ASC", (argument,)
                )
    rows = cur.fetchall()

    print(", ".join([row[0] for row in rows]))

    # Close the cursor and the database connection
    cur.close()
    db.close()
