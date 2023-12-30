import sqlite3
import datetime

con = sqlite3.connect('2023.12.18-08.39.28_manual.db')
cur = con.cursor()

result = cur.execute("""SELECT training_id FROM workout""").fetchall()

for elem in result:
    print(elem[0])

con.close()

time_in_millis = 1703939445511
dt = datetime.datetime.fromtimestamp(time_in_millis / 1000.0, tz=datetime.timezone.utc)
print(dt)