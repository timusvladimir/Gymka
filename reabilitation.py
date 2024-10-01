import pandas as pd
import matplotlib.pyplot as plt

# Создание данных о реабилитации спины для примера
data = {
    'День': ['1', '2', '3', '4', '5', '6', '7'],
    'Уровень боли (0-10)': [7, 6, 5, 4, 3, 2, 1],
    'Время на упражнения (мин)': [15, 20, 25, 30, 35, 40, 45]
}

# Создание DataFrame
df = pd.DataFrame(data)

# Вывод данных
print("Данные о реабилитации спины:")
print(df)

# Построение графиков
fig, ax1 = plt.subplots()

# График уровня боли
color = 'tab:red'
ax1.set_xlabel('День')
ax1.set_ylabel('Уровень боли (0-10)', color=color)
ax1.plot(df['День'], df['Уровень боли (0-10)'], color=color, marker='o', label='Уровень боли')
ax1.tick_params(axis='y', labelcolor=color)

# Создание второго y-оси для времени на упражнения
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Время на упражнения (мин)', color=color)
ax2.plot(df['День'], df['Время на упражнения (мин)'], color=color, marker='s', label='Время на упражнения')
ax2.tick_params(axis='y', labelcolor=color)

# Добавление заголовка и легенды
plt.title('Реабилитация спины: Уровень боли и время на упражнения')
fig.tight_layout()
plt.show()
