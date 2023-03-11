import sqlite3 as sq
import users

with sq.connect("database.db") as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    sex INTEGER NOT NULL DEFAULT 1,
    old INTEGER,
    score INTEGER)""")

#Удаление БД.
con.executemany("INSERT INTO users VALUES(?, ?, ?, ?, ?)", users.users)
con.commit()


# with sq.connect("database.db") as con:
#     #Добавление данных.
#     con.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?)", (None, "Nikita", 17, 1, 190))
#     con.commit()

# #Удаление данных.
# # con.execute("DELETE FROM users WHERE user_id = 2")
# # con.commit()

# user = [(None, "Daniil", 17, 1, 213)]
# con.executemany("INSERT INTO users VALUES (?, ?, ?, ?, ?)", user)
# con.commit()
