# ==========================================
# PYTHON INTERVIEW QUESTIONS
# ==========================================

# 1. Difference Between List and Tuple

# List
# - Mutable
# - Slower
# - More memory
# - Better for insertion/deletion

my_list = ['a', 'b', 'c', 1, 2, 3]

# Tuple
# - Immutable
# - Faster
# - Less memory
# - Better for fixed data

my_tuple = ('a', 'b', 'c', 1, 2)



# 2. What Are Decorators?

# Decorators are functions that take another
# function as input and return a modified function.

def decorator(func):
    def wrapper():
        print("Transaction Started")
        func()
        print("Transaction Completed")
    return wrapper


@decorator
def hello():
    print("Executing transaction...")


# hello()



# 3. List Comprehension

# Normal Way

squares = []

for i in range(1, 6):
    squares.append(i ** 2)

# List Comprehension

new_squares = [i ** 2 for i in range(1, 6)]



# 4. Memory Management In Python

# Managed automatically by Python Memory Manager

# Concepts:
# 1. Reference Counting
# 2. Garbage Collection
# 3. Private Heap Memory



# 5. Iterator vs Generator

# Iterator
# - Uses iter() and next()
# - Used to traverse iterable objects

nums = [1, 2, 3]

it = iter(nums)

# print(next(it))
# print(next(it))


# Generator
# - Uses yield keyword
# - Generates values one by one

def count():
    yield 1
    yield 2
    yield 3

g = count()

# print(next(g))
# print(next(g))



# Every Generator is an Iterator
# Every Iterator is NOT a Generator



# 6. __init__.py vs __init__()

# __init__.py
# - Makes a directory a Python package

# __init__()
# - Constructor
# - Called automatically when object is created

class Student:

    def __init__(self, name):
        self.name = name


# s1 = Student("Nakul")



# 7. Module vs Package

# Module
# - Single Python file

# Example:
# math.py

# Package
# - Collection of modules
# - Contains __init__.py



# 8. Built-in Data Types

# Numeric     -> int, float, complex
# Sequence    -> list, tuple, range
# Text        -> str
# Mapping     -> dict
# Set         -> set, frozenset
# Boolean     -> bool
# Binary      -> bytes, bytearray



# 9. Ternary Operator

age = 18

result = "Adult" if age >= 18 else "Minor"

# print(result)



# 10. Inheritance

class Parent:

    def method1(self):
        print("Parent Method")


class Child(Parent):

    def method2(self):
        print("Child Method")


# c = Child()
# c.method1()
# c.method2()



# 11. Local Variable vs Global Variable

# Local Variable
# - Declared inside function
# - Accessible only inside function

# Global Variable
# - Declared outside function
# - Accessible throughout program



# 12. Break Continue Pass

# break -> exits loop
# continue -> skips current iteration
# pass -> does nothing

for i in range(5):

    if i == 2:
        pass

    if i == 3:
        continue

    if i == 4:
        break



# 13. self Keyword

# self refers to the current object of the class



# 14. Pickling and Unpickling

import pickle

data = {
    "name": "John",
    "age": 30
}

# Pickling
# pickle.dump()

# Unpickling
# pickle.load()



# 15. *args and **kwargs

def add(*args):
    print(args)


def display(**kwargs):
    print(kwargs)



# 16. File Modes

# r   -> Read
# r+  -> Read + Write
# w   -> Write
# w+  -> Write + Read
# a   -> Append
# a+  -> Append + Read
# x   -> Create New File
# b   -> Binary Mode
# t   -> Text Mode



# 17. What Is PYTHONPATH?

# Environment variable that tells Python
# where to search for modules and packages.



# 18. Exception Handling

try:
    result = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Always executes")



# 19. What Is PIP?

# Python Package Manager

# pip install numpy



# 20. String Formatting

name = "Nakul"
age = 20

# print("My name is {} and I am {}".format(name, age))

# print(f"My name is {name} and I am {age}")



# 21. Multiple Inheritance

class Father:

    def money(self):
        print("Money")


class Mother:

    def care(self):
        print("Care")


class Child(Father, Mother):
    pass



# 22. What Are .pyc Files?

# Compiled Python Bytecode Files
# Generated automatically by Python



# 23. Read Multiple Inputs

a, b, c = map(int, input().split())

# print(a, b, c)



# 24. Lambda Function

cube = lambda x: x ** 3

# print(cube(5))



# 25. Shallow Copy vs Deep Copy

import copy

lst = [[1, 2], [3, 4]]

# Shallow Copy
shallow = copy.copy(lst)

# Deep Copy
deep = copy.deepcopy(lst)

# Shallow -> shares nested objects
# Deep -> creates completely independent copy