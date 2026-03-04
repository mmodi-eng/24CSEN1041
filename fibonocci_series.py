

 Program to Print Factorial of a Number
(Using While Loop)
# Program related to Factorial
# Using loop constructs

# The factorial of a number n is the product of all
# positive integers less than or equal to n.
code
number = int(input("Enter a positive number: "))

factorial = 1
i = 1

while i <= number:
    factorial = factorial * i
    i += 1

print("Factorial =", factorial)

# OUTPUT
# Enter a positive number: 5
# Factorial = 120
