import chardet
import pandas as pd

# Определение кодировки
with open('workout.csv', 'rb') as file:
    result = chardet.detect(file.read())

# Вывод предполагаемой кодировки
print(f"Предполагаемая кодировка: {result['encoding']}")

# Загрузка данных с определенной кодировкой
data = pd.read_csv('workout.csv', encoding=result['encoding'])

# Удаление ненужных столбцов
data = data[['startDateTime', 'name', 'finishDateTime', 'exercisesAmount', 'setsAmount', 'repsAmount', 'tonnage', 'distance', 'time', 'avgPulse', 'calories']]

# Преобразование времени из Unix timestamp в читаемый формат
data['startDateTime'] = pd.to_datetime(data['startDateTime'], unit='ms')
data['finishDateTime'] = pd.to_datetime(data['finishDateTime'], unit='ms')

# Очистка и стандартизация значений
data = data.fillna(0)  # Заполнение пропусков нулями, если применимо

# Проверка и удаление дублирующихся записей
data = data.drop_duplicates()

# Сохранение очищенных данных в новый CSV файл
data.to_csv('cleaned_workout.csv', index=False)
