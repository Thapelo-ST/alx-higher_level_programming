#!/usr/bin/python3
import sys
import MySQLdb
"""
    list_states a module or function that prints all states by id order
"""


def list_states(mysql_username, mysql_password, database_name):
    """
        list_states a module or function that prints all states by id order
    """
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connection.close()


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    list_states(mysql_username, mysql_password, database_name)
