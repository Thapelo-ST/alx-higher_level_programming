#!/usr/bin/python3
"""
    filter states by the input of the user
"""

import MySQLdb
import sys

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

    query = ("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
             .format(filter_name,))
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

except MySQLdb.Error as e:
    print(f"Error: {e}")
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()

