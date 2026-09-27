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
