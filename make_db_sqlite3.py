import sqlite3

# Создание или подключение к базе данных
conn = sqlite3.connect('workouts.db')

# Создание объекта курсора
c = conn.cursor()

# Создание таблицы
c.execute('''
CREATE TABLE IF NOT EXISTS workouts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    startDateTime TEXT NOT NULL,
    name TEXT,
    finishDateTime TEXT NOT NULL,
    exercisesAmount INTEGER,
    setsAmount INTEGER,
    repsAmount INTEGER,
    tonnage REAL,
    distance REAL,
    time REAL,
    avgPulse REAL,
    calories REAL
)
''')

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()
