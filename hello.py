"""
print("Hello, World!")
print("Hello")

print("World")

user = input("Enter your name:")
print("Nice to see you, "+user+"!")
print(type(user))
a = 10
b = 2.5
c = 6+3j
d = "Python"
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(30>20)


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(a/b)
print(c)
print(type(a))
print(type(b))
print(type(c))


a = int(input("Enter your math scores: "))
b = int(input("Enter your physics scores: "))
c = int(input("Enter your programming scores: "))
d = int(a+b+c/90*100)

print("Your total score is", d , "%")

radius = float(input("Enter the radius of the circle: "))
area = 3.14 * radius *  radius
print("The area of the circle is:", area)


lenght = float(input("Enter the lenght of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = lenght * width
perimeter = 2 * (lenght + width)
print("The area of the rectangle is:", area)
print("The perimeter of the rectangle is:", perimeter)


num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))
sum = num1 + num2 + num3
product = num1 * num2 * num3
average = sum/3
print("The summary is:" , sum)
print("The product is:" , product)
print("The average is:" , average)


lenght = float(input("Enter the lenght of the zander in cm: "))
if lenght < 42:
    short = 42 - lenght
    print(f"Release the fish back in to the lake!")
    print(f"The fish is {short:.1f} cm below the size limit.")

else:
    print("The fish meets the size limit, you can keep it!")


cabin = input("Enter the cabin class (LUX, A, B or C: ")
if cabin == "LUX":
    print("Upper-deck cabin with a balcony.")
elif cabin == "A":
    print("Above the car deck, equipped with a window.")
elif cabin == "B":
    print("Windowless cabin above the car deck.")
elif cabin == "C":
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class!")


gender = input("Enter your gender: ")
hemoglobin = float(input("Enter your hemoglobin level:"))
if gender == "female":
    if hemoglobin < 117:
        print("hemoglobin level is low!")
    elif hemoglobin <= 155:
        print("hemoglobin level is normal.")
    else:
        print("hemoglobin level is high!")
elif gender == "male":
    if hemoglobin < 134:
        print("hemoglobin level is low!")
    elif hemoglobin <= 167:
        print("hemoglobin level is normal.")
    else:
        print("hemoglobin level is high!")
else:
    print("Invalid gender!")


year = int(input("Enter a year:"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("The year is a leap year.")
        else:
            print("The year is not a leap year.")
    else:
        print("The year is a leap year.")
else:
    print("The year is not a leap year.")

num = 1
while num <= 1000:
    if num % 3 == 0:
        print(num)
    num += 1

while True:
    inches = float(input("Enter length in inches: "))
    if inches < 0:
        print("Program ended.")
        break
    centimeters = inches * 2.54
    print(f"{inches} inches = {centimeters:.2f} cm")


smallest = None
largest = None

while True:
    user_input = input("Enter a number: ")
    if user_input == "":
        break
    number = float(user_input)
    if smallest is None or number < smallest:
        smallest = number
    if largest is None or number > largest:
        largest = number
if smallest is None:
    print("No numbers were entered.")
else:
    print("Smallest number:", smallest)
    print("Largest number:", largest)


import random
secret = random.randint(1, 10)
while True:
   number = int(input("Guess a number between 1 and 10: "))
   if number < secret:
    print("Too low!")
   elif number > secret:
    print("Too high!")
   else:
    print("Correct!")



correct_username = "python"
correct_password = "rules"
max_attempts = 5
attempts = 0
while attempts < max_attempts:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == correct_username and password == correct_password:
        print("Welcome!")
        break
    else:
        print("Incorrect username or password.")
        attempts += 1
if attempts == max_attempts:
    print("Access denied.")
"""

import random
N = int(input("Enter the number of random points to generate: "))
circle = 0
for i in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x ** 2 + y ** 2 < 1:
        circle += 1
pi_approx = 4 * circle / N
print("Approximation of pi:", pi_approx)