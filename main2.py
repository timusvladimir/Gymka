import sqlite3

con = sqlite3.connect('2023.12.18-08.39.28_manual.db')
cur = con.cursor()

result = cur.execute("""SELECT training_id FROM workout""").fetchall()

for elem in result:
    print(elem[0])

con.close()