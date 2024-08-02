import sqlite3


def insert_workout(startDateTime, name, finishDateTime, exercisesAmount, setsAmount, repsAmount, tonnage, distance,
                   time, avgPulse, calories):
    # Подключение к базе данных
    conn = sqlite3.connect('workouts.db')
    c = conn.cursor()

    # SQL запрос для вставки данных
    c.execute('''
    INSERT INTO workouts (
        startDateTime, name, finishDateTime, exercisesAmount, setsAmount, repsAmount, tonnage, distance, time, avgPulse, calories
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
    startDateTime, name, finishDateTime, exercisesAmount, setsAmount, repsAmount, tonnage, distance, time, avgPulse,
    calories))

    # Сохранение изменений и закрытие соединения
    conn.commit()
    conn.close()


# Пример использования
insert_workout(
    '2024-08-01 09:00:00',  # startDateTime
    'Утренняя тренировка',  # name
    '2024-08-01 10:00:00',  # finishDateTime
    5,  # exercisesAmount
    10,  # setsAmount
    30,  # repsAmount
    500.0,  # tonnage
    2.5,  # distance
    60.0,  # time
    120.0,  # avgPulse
    400.0  # calories
)
