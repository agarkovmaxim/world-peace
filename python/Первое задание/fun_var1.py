# Агарков Максим Алексеевич, группа 44-22-121, вариант 1
import math

def calculate_function1(x):
    if x > -1:
        result = x + 2 * x ** 2
    else:
        result = x * math.log(abs(x + 2))
    return result

if __name__ == "__main__":
    try:
        x = float(input("Enter a numeric value for x: "))
        result = calculate_function1(x)
        print("Result:", result)
    except ValueError:
        print("Invalid input. Please enter a numeric value for x.")
