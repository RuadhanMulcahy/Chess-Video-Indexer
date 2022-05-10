"""
Module to house the MySQL Operator to interact with a MySQL database.
"""
import mysql.connector

class MySQL:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="mysql",
            port=3306,
            user="root",
            password="jwsecret")


    def test_database_connection(self):
        # Get a cursor
        cur = self.db.cursor()

        # Execute a query
        cur.execute("SELECT CURDATE()")

        # Fetch one result
        row = cur.fetchone()

        # Close connection
        self.db.close()
        
        return "Current date is: {0}".format(row[0])