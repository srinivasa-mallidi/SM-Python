# Python Complete Notes

This guide provides comprehensive Python programming concepts with examples. It covers fundamentals to intermediate topics required for efficient software and automation development.

---

## Basics

### Variables
```python
x = 5
y = "Hello"
z = 3.14
```

### Data Types
- int, float, str, bool, list, tuple, dict, set, None

```python
age = 25             # int
price = 99.99        # float
name = "Python"      # str
is_valid = True      # bool
```

### Type Casting
```python
x = int("10")
y = float("5.5")
z = str(123)
```

---

## Control Structures

### Conditionals
```python
if age >= 18:
    print("Adult")
elif age > 12:
    print("Teenager")
else:
    print("Child")
```

### Loops

#### For Loop
```python
for i in range(5):
    print(i)
```

#### While Loop
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### Loop Control
- `break`, `continue`, `pass`

```python
for i in range(10):
    if i == 3:
        continue
    if i == 7:
        break
    print(i)
```

---

## Functions

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Python"))
```

### Default Arguments
```python
def greet(name="Guest"):
    print(f"Hello, {name}!")
```

### *args and **kwargs
```python
def add_all(*args):
    return sum(args)

add_all(1, 2, 3, 4)


def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
```

---

## Data Structures

### Lists
```python
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits[0] = "grape"
```

### Tuples
```python
tuple1 = (1, 2, 3)
```

### Sets
```python
colors = {"red", "green", "blue"}
colors.add("yellow")
```

### Dictionaries
```python
person = {"name": "Python", "age": 25}
person["city"] = "Bangalore"
```

---

## File I/O

### Reading a File
```python
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
```

### Writing to a File
```python
with open("output.txt", "w") as file:
    file.write("Hello World")
```

---

## List Comprehensions
```python
squares = [x**2 for x in range(10)]
```

## Lambda Functions
```python
square = lambda x: x*x
print(square(5))
```

---

## Modules and Packages
```python
import math
print(math.sqrt(16))
```

You can create your own modules by saving functions in a `.py` file and importing them.

---

## Exception Handling
```python
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
finally:
    print("Execution completed.")
```

---

## OOP (Object-Oriented Programming)

### Class and Object
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, I'm {self.name}")

p = Person("Python", 30)
p.greet()
```

### Inheritance
```python
class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no
```

---

## Common Built-in Functions
- `len()`, `type()`, `sum()`, `max()`, `min()`, `sorted()`, `range()`

---

## Useful Libraries
- `datetime`
- `random`
- `os`
- `sys`
- `csv`
- `json`

---

## Sample Script
```python
import random

names = ["Ankit", "Divya", "Naveen", "Meena"]
print("Random name:", random.choice(names))
```

---

> This  sheet gives a foundational overview for beginners to quickly grasp core Python programming concepts.

