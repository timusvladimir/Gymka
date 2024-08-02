import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных
data = pd.read_csv('cleaned_workout.csv')

# Преобразование строковых данных в тип datetime
data['startDateTime'] = pd.to_datetime(data['startDateTime'])
data['finishDateTime'] = pd.to_datetime(data['finishDateTime'])

# Заполнение пропусков нулями или средними значениями, если это имеет смысл
data = data.fillna({
    'exercisesAmount': 0,
    'setsAmount': 0,
    'repsAmount': 0,
    'tonnage': 0.0,
    'distance': 0,
    'time': 0.0,
    'avgPulse': 0.0,
    'calories': 0.0
})

# Удаление строк с нулевыми значениями, если это оправдано
data = data[(data['exercisesAmount'] > 0) & (data['setsAmount'] > 0)]

# Рассчет общей продолжительности тренировок
data['duration'] = (data['finishDateTime'] - data['startDateTime']).dt.total_seconds() / 60  # Время в минутах

# Рассчет средних значений
average_stats = data[['exercisesAmount', 'setsAmount', 'repsAmount', 'tonnage', 'distance', 'time', 'avgPulse', 'calories']].mean()

print("Средние значения:")
print(average_stats)

# Построение графиков
plt.figure(figsize=(12, 6))

# График времени тренировок
plt.subplot(2, 2, 1)
plt.plot(data['startDateTime'], data['duration'], marker='o', linestyle='-')
plt.xlabel('Дата и время начала')
plt.ylabel('Продолжительность (мин)')
plt.title('Продолжительность тренировок')

# График распределения упражнений
plt.subplot(2, 2, 2)
data['name'].value_counts().plot(kind='bar')
plt.xlabel('Тип тренировки')
plt.ylabel('Количество')
plt.title('Распределение типов тренировок')

plt.tight_layout()
plt.show()
