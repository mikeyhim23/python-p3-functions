#!/usr/bin/env python3

def greet_programmer():
    pass
    print("Hello, programmer!")

def greet(name):
    pass
    print(f"Hello, {name}!")

greet("Naureen")
    

def greet_with_default(name="programmer"):
    pass
    print(f"Hello, {name}!")

greet_with_default()
greet_with_default("Sunny")

def add(num1, num2):
    return num1 + num2
    pass
ans = add(1, 2)
print(ans)

def halve(number):
    pass
    if not isinstance(number, (int,float)):
        return None
    return number / 2

ans = halve(4)
print(ans)

ans_invalid = halve("two")
print(ans_invalid)