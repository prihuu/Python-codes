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
"""

a = int(input("Enter your math scores: "))
b = int(input("Enter your physics scores: "))
c = int(input("Enter your programming scores: "))
d = int(a+b+c/90*100)

print("Your total score is", d , "%")
