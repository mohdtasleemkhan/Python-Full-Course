# Step 1: What is Python?

Python is a high-level, easy-to-read programming language

Used for:

Web development

Data science & AI

Automation & scripting

Games & apps

# Step 2: Installing & Running Python

You can run Python in:

Terminal / Command Prompt

IDEs (VS Code, PyCharm)

Online editors (Replit, Jupyter)

Test Python:

print("Hello, World!")

# Step 3: Variables

Variables store data.

name = "Alice"
age = 25
height = 5.6

print(name)
print(age)

# Rules:

No need to declare data types

Variable names should be meaningful

# Step 4: Data Types

Common Python data types:

# String
name = "Python"

# Integer
age = 20

# Float
price = 99.99

# Boolean
is_student = True

# Step 5: User Input
name = input("Enter your name: ")
print("Hello", name)

Input is always a string, convert when needed:
age = int(input("Enter age: "))

# Step 6: Operators
Arithmetic
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)

# Comparison
print(a > b)
print(a == b)

# Logical
print(a > 5 and b < 5)

# Step 7: Conditional Statements
age = 18

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible")

# Multiple conditions:

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
else:
    print("Adult")

# Step 8: Loops
for loop
for i in range(5):
    print(i)

while loop
count = 1
while count <= 5:
    print(count)
    count += 1

# Step 9: Lists
fruits = ["apple", "banana", "cherry"]

print(fruits[0])
fruits.append("orange")


Loop through list:

for fruit in fruits:
    print(fruit)

# Step 10: Tuples & Sets
# Tuple (immutable)
colors = ("red", "green", "blue")

# Set (unique values)
numbers = {1, 2, 3, 3}
print(numbers)

# Step 11: Dictionaries
student = {
    "name": "John",
    "age": 20,
    "course": "Python"
}

print(student["name"])

# Step 12: Functions
def greet(name):
    return "Hello " + name

print(greet("Alice"))

# Step 13: Modules
import math

print(math.sqrt(16))

# Step 14: Basic Error Handling
try:
    num = int(input("Enter number: "))
    print(10 / num)
except:
    print("Error occurred")

    ######################
