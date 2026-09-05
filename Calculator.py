import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def power(a, b):
    return a ** b

firstNum = float(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /, ^): ")
secondNum = float(input("Enter the second number: "))

match operator:
    case "+":
        print(add(firstNum, secondNum))
    case "-":
        print(subtract(firstNum, secondNum))
    case "*":
        print(multiply(firstNum, secondNum))
    case "/":
        print(divide(firstNum, secondNum))
    case "^":
        print(power(firstNum, secondNum))
    case _:
        print("Error: Invalid operator")