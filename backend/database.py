import sqlite3


class Database():
    
    def query(self):

        # Connect to the SQLite database (creates a new database if it doesn't exist)
        conn = sqlite3.connect('mana.db')

        # Create a cursor object to execute SQL commands
        cursor = conn.cursor()

        # Insert data into the table
        cursor.execute("INSERT INTO Users (firstName, lastName, email) VALUES (?, ?, ?)", ('Liam', 'McBride', "mailmcbride56@gmail.com"))

        # Commit the changes to the database
        conn.commit()

        # Retrieve data from the table
        cursor.execute("SELECT * FROM Users")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        # Close the database connection
        conn.close()