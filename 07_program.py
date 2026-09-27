input1 = input("Enter first number: ")
input2 = input("Enter second number: ")
input3 = input("Enter third number: ")

num1, num2, num3 = int(input1), int(input2), int(input3)

if num1 > num2 and num1 > num3:
    print(f"{num1} is bigger")
elif num2 > num1 and num2 > num3:
    print(f"{num2} si bigger")
else:
    print(f"{num3} is bigger")
