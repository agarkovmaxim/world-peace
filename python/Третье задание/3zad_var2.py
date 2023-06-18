# Алдохина Элеонора Алексеевна, группа 44-22-121, вариант 2
import tkinter as tk
from math import sqrt, log, sin, cos

def calculate_function2(x):
    if x < 0.1:
        return sqrt(x) + x ** 2
    else:
        return sin(x) + cos(x)

def calculate():
    x = float(entry_x.get())
    function2_result = calculate_function2(x)
    label_result.config(text=f"Function 2: {function2_result}")

# Создание окна приложения
window = tk.Tk()
window.title("Function 2 Calculator")

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
