Calculator Program - Refactored Version
Overview

This project showcases a simple calculator application that performs basic arithmetic operations such as addition, subtraction, multiplication, and division. The program allows users to input numbers and select operations to perform on them, continuously updating the result. This is a refactored version of an earlier project I started, designed to demonstrate my improvement in programming skills over the past three years.

Original Project

The original version of this calculator was created as a basic Python script that featured separate functions for each operation (addition, subtraction, multiplication, division). While the initial code worked as intended, it lacked some features like error handling for invalid inputs and division by zero, and the flow was somewhat repetitive.
Refactoring Improvements it can actually still be found under the initial commit in this project!

In this refactored version, I focused on:

Code Optimization: I consolidated the operations into a single function (calculation), reducing repetition and improving maintainability.
Error Handling: I added proper checks for division by zero and invalid operations to enhance the user experience.
Input Validation: I included better validation for inputs to ensure that the user receives helpful messages if something goes wrong.
User Flow: The user flow is streamlined for more intuitive interaction, allowing users to perform multiple operations sequentially or exit the program.

Features

Addition: Performs the addition of two numbers.
Subtraction: Subtracts one number from another.
Multiplication: Multiplies two numbers together.
Division: Divides the first number by the second (with handling for division by zero).
Error Messages: Provides helpful feedback for invalid inputs, such as dividing by zero or entering an unrecognized operation.

How to Use

Clone this repository to your local machine.
Open the Python file (calculator.py) in your preferred code editor or IDE.
Run the script, and follow the prompts to enter a number, select an operation, and enter a second number.
The program will display the result of the operation and prompt you to perform another operation or exit.
Type exit to end the program.
