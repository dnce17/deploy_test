import sqlite3

con = sqlite3.connect("number.db")
db = con.cursor()

create_table = db.execute("""CREATE TABLE num (
                                id INTEGER NOT NULL,
                                number INTEGER,
                                PRIMARY KEY(id)
                              )"""
                          )

