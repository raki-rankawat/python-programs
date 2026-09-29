num = input("Enter a number: ")

num = int(num)
isPrime = True

for i in range(num):
    if i < 2:
        continue

    if num % i == 0:
        isPrime = False

if not isPrime:
    print(f"{num} is not prime")
else:
    print(f"{num} is prime")
