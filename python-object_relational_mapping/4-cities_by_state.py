#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
    """


import sys
import MySQLdb


if __name__ == "__main__":
    """ Lists all states from the database hbtn_0e_4_usa
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

    # Execute the SQL query to list cities with their corresponding states
    cur.execute("SELECT cities.id, cities.name, states.name \
                FROM cities \
                LEFT JOIN states ON cities.state_id = states.id \
                ORDER BY cities.id ASC"
                )
    rows = cur.fetchall()

    # print each row
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cur.close()
    db.close()
