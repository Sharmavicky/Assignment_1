# Task: 1 - Write a Python program to take input of two numbers and perform basic arithmetic operations (addition, subtraction, multiplication, division) on them.

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

# Performing arithmetic operations
addition = n1 + n2
subtraction = n1 - n2
multiplication = n1 * n2
if n2 != 0:
    division = n1 / n2
else:
    division = n2 / n1


# print the results
print(f"Addition: {n1} + {n2} = {addition}")
print(f"Subtraction: {n1} - {n2} = {subtraction}")
print(f"Multiplication: {n1} * {n2} = {multiplication}")
if n2 != 0:
    print(f"Division: {n1} / {n2} = {division}")
else:
    print(f"Division: {n2} / {n1} = {division}")
