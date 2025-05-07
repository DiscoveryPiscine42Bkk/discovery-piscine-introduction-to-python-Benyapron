#!/usr/bin/python3
a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

res = a * b
print(f"{a} x {b} = {res}")
if res > 0:
    print("The result is positive")
elif res < 0:
    print("The result is negative")
else:
    print("The result is positive and negative ")