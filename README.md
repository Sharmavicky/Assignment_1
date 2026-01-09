# Assignment 1: Basic Input/Output and Arithmetic Operations

## Overview
This assignment introduces fundamental Python programming concepts including user input, variables, arithmetic operations, and string manipulation. It focuses on building basic skills for interactive programs.

## Objectives
- Learn how to accept user input
- Perform arithmetic operations on numbers
- Use conditional statements for error handling
- Work with string formatting and output

---

## Tasks

### Task 1: Arithmetic Operations Calculator

#### Description
Write a Python program that takes two numbers as input and performs all basic arithmetic operations (addition, subtraction, multiplication, and division).

#### Requirements
- Accept two integer inputs from the user
- Perform the following operations:
  - Addition
  - Subtraction
  - Multiplication
  - Division (with zero-division handling)
- Display formatted results for each operation

#### Key Concepts
- Input/Output operations
- Arithmetic operators (+, -, *, /)
- Conditional statements (if-else)
- String formatting with f-strings

#### Sample Run
```
Enter first number: 10
Enter second number: 5
Addition: 10 + 5 = 15
Subtraction: 10 - 5 = 5
Multiplication: 10 * 5 = 50
Division: 10 / 5 = 2.0
```

#### File
[Task_1.py](Task_1.py)

---

### Task 2: Personalized Greeting Message

#### Description
Write a Python program that takes a user's first and last name as input and displays a personalized greeting message.

#### Requirements
- Prompt the user to enter their first name
- Prompt the user to enter their last name
- Combine the names and create a friendly greeting message
- Display the personalized greeting

#### Key Concepts
- String variables
- User input with `input()` function
- String concatenation
- f-strings for formatting

#### Sample Run
```
Enter your first name: John
Enter your last name: Doe
Hello, John Doe! Welcome! to Python programming.
```

#### File
[Task_2.py](Task_2.py)

---

## How to Run

### Prerequisites
- Python 3.x installed on your system
- Terminal or Command Prompt access

### Steps

1. Navigate to the Assignment_1 directory:
   ```bash
   cd Assignment_1
   ```

2. Run the desired task:
   ```bash
   # For Task 1
   python Task_1.py
   
   # For Task 2
   python Task_2.py
   ```

3. Follow the on-screen prompts to enter your data

---

## Learning Outcomes

After completing this assignment, you should be able to:
- ✓ Accept and process user input
- ✓ Perform arithmetic calculations
- ✓ Implement basic error handling (zero-division)
- ✓ Format and display output effectively
- ✓ Use f-strings for string interpolation
- ✓ Build simple interactive programs

---

## File Structure

```
Assignment_1/
├── README.md
├── Task_1.py (Arithmetic Operations)
└── Task_2.py (Personalized Greeting)
```

---

## Tips & Tricks

### Task 1
- Use the modulo operator (%) to check if a number is zero before division
- Try different input values to test your error handling

### Task 2
- f-strings make formatting much easier than string concatenation
- You can combine variables directly within the string using {}

---

## Author
Vicky Sharma

## Date
January 2026
