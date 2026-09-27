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
