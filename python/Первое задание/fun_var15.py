# Лукьянчикова Анастасия Евгеньевна, группа 44-22-121, вариант 15
import math

def calculate_function3(x):
    if x < 2:
        result = math.log(abs(x * math.sin(x)))
    else:
        result = math.sqrt(x + 7)
    return result

if __name__ == "__main__":
    try:
        x = float(input("Enter a numeric value for x: "))
        result = calculate_function3(x)
        print("Result:", result)
    except ValueError:
        print("Invalid input. Please enter a numeric value for x.")
