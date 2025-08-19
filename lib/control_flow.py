#!/usr/bin/env python3

def admin_login(username, password):
    if username == "ADMIN" or username == "admin" and password == "12345":
        return "Access granted"
    else:
        return "Access denied"
    
admin_login("admin", "12345")

def hows_the_weather(temperature):
    if temperature < 40:
        response = "brisk"
    elif temperature >= 40 and temperature <= 65:
        response = "a little chilly"
    elif temperature > 85:
        response = "too dang hot"
    else:
        response = "perfect"
    
    return f"It's {response} out there!"


def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

def calculator(operation, num1, num2):
    operations = {
        "+": num1 + num2,
        "-": num1 - num2,
        "*": num1 * num2,
        "/": num1 / num2
    }
    if operation in operations:
        return operations[operation]
    else:
        print("Invalid operation!")
        return None

