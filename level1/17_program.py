str = input("Enter a integer: ")

num = int(str)
rev = 0

for i in range(len(str)):
    remain = num % 10
    num = int(num / 10)

    if remain != 0:
        rev = rev * 10 + remain


print(f"Reverse integer: {rev}")
