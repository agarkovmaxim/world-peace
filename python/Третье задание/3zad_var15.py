# Лукьянчикова Анастасия Евгеньевна, группа 44-22-121, вариант 15
import tkinter as tk
from math import sqrt, log, sin, cos

def calculate_function1(x):
    if x > -1:
        return x + 2 * x ** 2
    else:
        return x * log(abs(x + 2))

def calculate_function2(x):
    if x < 0.1:
        return sqrt(x) + x ** 2
    else:
        return sin(x) + cos(x)

def calculate_function3(x):
    if x < 2:
        return log(abs(x * sin(x)))
    else:
        return sqrt(x + 7)

def calculate():
    x = float(entry_x.get())
    function1_result = calculate_function1(x)
    function2_result = calculate_function2(x)
    function3_result = calculate_function3(x)
    label_result.config(text=f"Function 1: {function1_result}\n"
                              f"Function 2: {function2_result}\n"
                              f"Function 3: {function3_result}")

# Создание окна приложения
window = tk.Tk()
window.title("Function Calculator")

# Создание элементов интерфейса
label_x = tk.Label(window, text="Enter x:")
label_x.pack()

entry_x = tk.Entry(window)
entry_x.pack()

button_calculate = tk.Button(window, text="Calculate", command=calculate)
button_calculate.pack()

label_result = tk.Label(window, text="")
label_result.pack()

# Запуск цикла обработки событий
window.mainloop()
