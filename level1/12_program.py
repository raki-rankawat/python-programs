num = input("Enter a number (1-10): ")

num = int(num)
sum = 0

for i in range(num):
    sum = sum + (i + 1)

print(f"Total is: {sum}")
