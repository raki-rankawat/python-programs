num = input("Enter a number (1-10): ")

num = int(num)
sum = 0

for i in range(num):
    if (i + 1) % 2 == 0:
        sum = sum + (i + 1)

print(f"Total is: {sum}")
