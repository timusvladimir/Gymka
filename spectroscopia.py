import numpy as np
import scipy.signal as signal

import matplotlib.pyplot as plt

# Создание произвольного набора данных
np.random.seed(0)  # Для воспроизводимости
frequency = np.linspace(1, 10, 100)  # Частота от 1 до 10 ГГц
intensity = np.sin(frequency) + 0.5 * np.random.normal(size=frequency.size)  # Интенсивность с шумом

# Поиск пиков
peaks, _ = signal.find_peaks(intensity, height=0)

# Построение графиков
plt.figure(figsize=(10, 5))
plt.plot(frequency, intensity, label='Интенсивность', color='blue')
plt.scatter(frequency[peaks], intensity[peaks], color='red', label='Пики')
plt.xlabel('Частота (ГГц)')
plt.ylabel('Интенсивность')
plt.title('Анализ данных спектроскопии')
plt.legend()
plt.grid()
plt.show()
