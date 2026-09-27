input1 = input("Enter first num: ")
input2 = input("Enter second num: ")

num1, num2 = int(input1), int(input2)

if num1 > num2:
    print(f"{num1} is bigger")
elif num1 < num2:
    print(f"{num2} is bigger")
else:
    print("Both are equal")
