# Coding Practice — Python Programs

A collection of beginner Python practice programs covering input/output, arithmetic, conditionals, and loops.

## Table of Contents

| # | Program | Concept |
|---|---------|---------|
| 01 | [Greeting](#01--greeting) | Input & f-strings |
| 02 | [Sum of Two Numbers](#02--sum-of-two-numbers) | Variables & arithmetic |
| 03 | [Basic Calculator](#03--basic-calculator) | Arithmetic operators |
| 04 | [Even or Odd](#04--even-or-odd) | Modulo & `if/else` |
| 05 | [Positive, Negative, or Zero](#05--positive-negative-or-zero) | `if/elif/else` |
| 06 | [Bigger of Two Numbers](#06--bigger-of-two-numbers) | Comparison |
| 07 | [Biggest of Three Numbers](#07--biggest-of-three-numbers) | Logical operators |
| 08 | [Swap Two Numbers](#08--swap-two-numbers) | Swapping without a temp variable |
| 09 | [Leap Year Check](#09--leap-year-check) | Nested `if` & validation |
| 10 | [Print 1 to N](#10--print-1-to-n) | `while` loop |

---

## 01 — Greeting

Prompts for a name and greets the user.

```python
name = input('Enter your name: ')
print(f'Hello, {name}')
```

## 02 — Sum of Two Numbers

Takes two numbers from the user and prints their sum.

```python
input1 = input("Enter first number: ")
input2 = input("Enter second number: ")

num1, num2 = int(input1), int(input2)

print(f"Sum is: {num1 + num2}")
```

## 03 — Basic Calculator

Takes two numbers and prints all five basic arithmetic results.

```python
# Basic Calculator

input1 = input('Enter first number: ')
input2 = input('Enter second number: ')

num1, num2 = int(input1), int(input2)

print('--------------------')
print('Output:')

print(f'Addition: {num1 + num2}')
print(f'Subtraction: {num1 - num2}')
print(f'Multiplication: {num1 * num2}')
print(f'Division: {num1 / num2}')
print(f'Remainder: {num1 % num2}')
```

## 04 — Even or Odd

Checks whether a number is even or odd using the modulo operator.

```python
num = input("Enter a number: ")

if int(num) % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")
```

## 05 — Positive, Negative, or Zero

Classifies a number as positive, negative, or zero.

```python
num = input("Enter a number: ")

num = int(num)

if num == 0:
    print(f"{num} is zero")
elif num > 0:
    print(f"{num} is positive")
else:
    print(f"{num} is negative")
```

## 06 — Bigger of Two Numbers

Compares two numbers and prints the larger one.

```python
input1 = input("Enter first num: ")
input2 = input("Enter second num: ")

num1, num2 = int(input1), int(input2)

if num1 > num2:
    print(f"{num1} is bigger")
elif num1 < num2:
    print(f"{num2} is bigger")
else:
    print("Both are equal")
```

## 07 — Biggest of Three Numbers

Finds the largest of three numbers using logical `and`.

```python
input1 = input("Enter first number: ")
input2 = input("Enter second number: ")
input3 = input("Enter third number: ")

num1, num2, num3 = int(input1), int(input2), int(input3)

if num1 >= num2 and num1 >= num3:
    print(f"{num1} is bigger")
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} is bigger")
else:
    print(f"{num3} is bigger")
```

## 08 — Swap Two Numbers

Swaps two numbers without using a temporary variable.

```python
input1 = input("Enter first number: ")
input2 = input("Enter second number: ")

num1, num2 = int(input1), int(input2)

print("-------- Before swap: --------")

print(num1, num2)  # 10, 20

print("-------- After swap: --------")

num1 = num1 + num2  # 30
num2 = num1 - num2  # 10
num1 = num1 - num2  # 20

print(num1, num2)
```

## 09 — Leap Year Check

Validates a 4-digit year and applies the full leap-year rule (divisible by 4, except centuries not divisible by 400).

```python
import sys

year = input("Enter a year: ")

if len(year) != 4:
    print("Please enter a valid year!")
    sys.exit("exiting...")

year = int(year)

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is a common year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is a common year")
```

## 10 — Print 1 to N

Prints numbers from 1 up to N using a `while` loop.

```python
n = input("Enter a number: ")
i = 1

while i <= int(n):
    print(i)
    i = i + 1
```
