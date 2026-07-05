# Claude: Problem 1 - Create variables for your name, age, city, and whether you like coffee (boolean). Print all four in a single f-string that reads like a natural sentence.

name = 'Rahul'
age = 36
city = 'Pune'
like_coffee = True

print(f"Hi, my name is {name}, my age is str({age}). I live in {city} and it's {like_coffee} that I like coffee.")

# Claude: Problem 2 - Create a = 17 and b = 5. Print the result of +, -, *, /, //, and %. Add a comment on each line explaining what // and % actually do differently from regular division.

a = 17
b = 5
print(f'a + b = {a+b}')
print(f'a - b = {a-b}')
print(f'a * b = {a*b}')
print(f'a / b = {a/b}')
print(f'a // c = {a//b}')
print(f'a % b = {a%b}')

# Claude - Problem 3 — predict before you run
# What do you think this prints?
# python
x = "5"
y = 3
# print(x + y)
# Write your prediction as a comment first. Then fix it two ways — once so it prints 8, once so it prints "53".

# Prediction - This will throw an error about operation non-compatible due to different data types.
# actual output - TypeError: can only concatenate str (not "int") to str

# fix so it prints 8
print(int(x)+y)

# fix so it prints "53"
print(x+str(y))

"""
Claude:
Problem 4
python
seconds = 4725
Using only math operators (// and %), extract and print hours, remaining minutes, and remaining seconds.
Expected output: 1 hours, 18 minutes, 45 seconds
"""
seconds = 4725
hours = 4725 // 3600
minutes = seconds % 3600 // 60
seconds = 4725 % 60
print(f"{hours} hours, {minutes} minutes, {seconds} seconds")

"""
first = "machine"
second = "learning"
Without retyping those words, create a variable that holds "MACHINE LEARNING" and print it. (Hint: there's a string method that uppercases — find it by typing first. and seeing what autocomplete suggests, or just think logically.)
"""
first = "machine"
second = "learning"
print((f"{first} {second}").upper())

