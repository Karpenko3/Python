import math
import numpy as np
import matplotlib.pyplot as plt

# Адаптована функція спеціально для графіка
def calculate_p_graph(x):
    numerator = math.exp(-3 * x) + math.tan(3 * x - 3)
    under_root = math.cos(x) + math.cos(2 * x)
    
    # Якщо корінь від'ємний, повертаємо "не число"
    if under_root < 0:
        return np.nan
        
    root_part = under_root ** 0.25
    sin_part = abs(math.sin(x))
    denominator = sin_part + root_part
    
    # Якщо ділення на нуль, повертаємо "не число"
    if denominator < 0.000001:
        return np.nan
    
    return numerator / denominator

# Генеруємо 500 рівномірних точок від 0 до 10
x_points = np.linspace(0, 10, 500)

# Обчислюємо значення Y для кожної точки X
y_points = [calculate_p_graph(x) for x in x_points]

# Налаштовуємо та малюємо графік
plt.figure(figsize=(10, 6))
plt.plot(x_points, y_points, color='blue', label='Функція p(x)')

# Додаємо підписи та сітку
plt.title('Графік функції p(x) для 0 < x < 10')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.grid(True)
plt.legend()

# Виводимо графік на екран
plt.show()