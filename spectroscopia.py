import numpy as np
import scipy.signal as signal
import sympy as sp
import matplotlib.pyplot as plt

# Функция для создания синусоидальных данных поглощения с шумом
def generate_absorption_spectrum(frequency_range, noise_level=0.2):
    frequency = np.linspace(frequency_range[0], frequency_range[1], 200)
    # Создаем синусоидальную функцию поглощения
    absorption = (
        5 * np.sin(2 * np.pi * (frequency - frequency_range[0]) / (frequency_range[1] - frequency_range[0])) +
        2 * np.sin(4 * np.pi * (frequency - frequency_range[0]) / (frequency_range[1] - frequency_range[0]))
    )
    absorption = np.clip(absorption, 0, None)  # Убрать отрицательные значения
    absorption += noise_level * np.random.normal(size=frequency.size)  # Добавление шума
    return frequency, absorption

# Генерация данных для диапазона 105—150 ГГц
frequency, absorption = generate_absorption_spectrum((105, 150))

# Поиск пиков
peaks, _ = signal.find_peaks(absorption, height=0)

# Анализ данных с использованием sympy
x = sp.symbols('x')
# Пример функции для подгонки, можно заменить на более сложную модель
fit_function = 5 * sp.sin(2 * np.pi * (x - 105) / (150 - 105))
fit_params = sp.solve(sp.Eq(absorption[peaks].mean(), fit_function.subs(x, frequency[peaks].mean())), x)

# Построение графиков
plt.figure(figsize=(12, 6))
plt.plot(frequency, absorption, label='Поглощение (дБ/км)', color='blue')
plt.scatter(frequency[peaks], absorption[peaks], color='red', label='Пики')
plt.xlabel('Частота (ГГц)')
plt.ylabel('Поглощение (дБ/км)')
plt.title('Спектр поглощения димера в водяном паре')
plt.legend()
plt.grid()
plt.xlim(100, 160)  # Установка пределов по оси X для удобства
plt.show()

# Вывод параметров подгонки
print(f"Параметры подгонки: {fit_params}")

from scipy.optimize import curve_fit

# Определение модели подгонки
def model_function(f, amplitude, frequency_offset):
    return amplitude * np.sin(2 * np.pi * (f - frequency_offset) / (150 - 105))

# Подгонка данных
initial_guess = [5, 125]  # Начальные предположения для параметров
params, _ = curve_fit(model_function, frequency, absorption, p0=initial_guess)

# Полученные параметры
amplitude_fit, frequency_offset_fit = params
print(f"Подогнанная амплитуда: {amplitude_fit}, Частота сдвига: {frequency_offset_fit}")

# Построение графика
plt.figure(figsize=(12, 6))
plt.plot(frequency, absorption, label='Экспериментальные данные', color='blue')
plt.plot(frequency, model_function(frequency, *params), label='Подгонка', color='orange')
plt.xlabel('Частота (ГГц)')
plt.ylabel('Поглощение (дБ/км)')
plt.title('Подгонка зависимости поглощения от частоты')
plt.legend()
plt.grid()
plt.show()