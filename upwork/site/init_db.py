import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO skills (name, years_of_experience) VALUES (?,?)",
            ('machine learning',4)
            ),

cur.execute("INSERT INTO skills (name,years_of_experience) VALUES (?,?)",
            ('project management',3)
            )

connection.commit()
connection.close()
