#!/usr/bin/python3
user = int(input("Enter a number less than 25\n"))
x = 1

if user > 25:
    print("Error")

else:
    for i in range(user, 26):
        print("Inside the loop, my variable is",i)