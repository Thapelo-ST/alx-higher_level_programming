#!/usr/bin/python3
"""
    print all cities by state in ascending order, and safe from sql injection
"""

import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    filter_name = sys.argv[4]

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
            SELECT cities.name FROM cities
            JOIN states ON cities.state_id = states.id 
            WHERE states.name = %s
            ORDER BY cities.id ASC
        """
        cursor.execute(query, (filter_name,))

        rows = cursor.fetchall()

        names = [row[0] for row in rows]
        to_print = ", ".join(names)
        print(to_print)

    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()
