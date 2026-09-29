num = input("Enter a number: ")

num = int(num)
fact = 1

while num > 0:
    fact = fact * num
    num = num - 1

print(f"Factorial is: {fact}")
