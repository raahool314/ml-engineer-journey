"""
claude:
3 Problems — solve in day3_input.py
Problem 1
Ask the user for their birth year. Calculate and print their age. (Current year is 2026.)
Problem 2
Ask the user for two numbers. Print their sum, difference, product, and which one is larger. (Hint: you can compare numbers with >)
Problem 3
Ask the user for a full name and a city. Print this:
Hello, [First Name]! Your profile is [FULL NAME] from [CITY IN CAPS].
Extract the first name from the full name without asking for it separately — use .split().
"""

birth_year = input("Enter your birth year: ")
print(f"Current age: {2026- int(birth_year)}")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print(f"sum: {num1+num2}, difference: {abs(num1-num2)}, product: {num1 * num2}, larger_number: {num1 if num1 > num2 else num2}")

full_name = input("Enter the full name: ")
first_name, last_name = full_name.split()
city = input("Enter the name of a city: ")
print(f"Hello, {first_name.title()} ! Your profile is {full_name.upper()} from {city.upper()}")