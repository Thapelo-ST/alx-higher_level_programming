#!/usr/bin/python3
"""
    print all cities in ascending order, and safe from sql injection
"""

import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    try:
        connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
        )

        cursor = connection.cursor()

        query = """
            SELECT cities.id, cities.name, states.name FROM cities
            JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC
        """
        cursor.execute(query)

        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()
