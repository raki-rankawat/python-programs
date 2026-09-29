num = input("Enter a number (1-10): ")

num = int(num)

for i in range(10):
    print(f"{num} x {i + 1} = {num * (i + 1)}")
