# Алдохина Элеонора Алексеевна, группа 44-22-121, вариант 2
import math

def calculate_function2(x):
    if x < 0.1:
        result = math.sqrt(x) + x ** 2
    else:
        result = math.sin(x) + math.cos(x)
    return result

if __name__ == "__main__":
    try:
        x = float(input("Enter a numeric value for x: "))
        result = calculate_function2(x)
        print("Result:", result)
    except ValueError:
        print("Invalid input. Please enter a numeric value for x.")
