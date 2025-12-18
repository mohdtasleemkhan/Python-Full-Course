#1. Print Numbers
#Problem:
#Print numbers from 1 to 10.

#Solution:

for i in range(1, 11):
    print(i)

#2. Even or Odd

#Problem:
#Take a number from the user and check if it is even or odd.

#Solution:

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#3. Sum of Two Numbers

#Problem:
#Take two numbers and print their sum.

#Solution:

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum:", a + b)

#4. Find Largest Number

#Problem:
#Find the largest of three numbers.

#Solution:

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)

#5. Count Characters

#Problem:
#Count how many characters are in a string.

#Solution:

text = input("Enter text: ")
print("Length:", len(text))

#🟡 INTERMEDIATE PRACTICE

#6. Find Even Numbers in a List

#Problem:
#Print all even numbers from a list.

#Solution:

numbers = [1, 2, 3, 4, 5, 6]

for num in numbers:
    if num % 2 == 0:
        print(num)

#7. Sum of List Elements

#Problem:
#Find the sum of all numbers in a list.

#Solution:

numbers = [10, 20, 30, 40]

total = 0
for num in numbers:
    total += num

print("Sum:", total)

#8. Reverse a String

#Problem:
#Reverse a string.

#Solution:

text = input("Enter text: ")

reversed_text = text[::-1]
print(reversed_text)

#9. Count Vowels

#Problem:
#Count vowels in a string.

#Solution:

text = input("Enter text: ")
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Vowels:", count)

#10. Factorial of a Number

#Problem:
#Find the factorial of a number.

#Solution:

num = int(input("Enter number: "))
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial:", fact)

#🔵 FUNCTION PRACTICE

#11. Add Two Numbers

def add(a, b):
    return a + b

print(add(5, 3))

#12. Check Prime Number

#Problem:

#Check if a number is prime.

Solution:

def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(is_prime(7))

#🔴 CHALLENGE PRACTICE

#13. Simple Calculator

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("Invalid operator")

#14. Fibonacci Series

#Problem:
#Print Fibonacci series up to n terms.

#Solution:

n = int(input("Enter number of terms: "))
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

#15. Find Maximum Without max()

numbers = [4, 7, 2, 9, 1]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest:", largest)
