# Агарков Максим Алексеевич, группа 44-22-121, вариант 1
import tkinter as tk
from math import sqrt, log, sin, cos

def calculate_function1(x):
    if x > -1:
        return x + 2 * x ** 2
    else:
        return x * log(abs(x + 2))

def calculate():
    x = float(entry_x.get())
    function1_result = calculate_function1(x)
    label_result.config(text=f"Function 1: {function1_result}")

# Создание окна приложения
window = tk.Tk()
window.title("Function 1 Calculator")

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
