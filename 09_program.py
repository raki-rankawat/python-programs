import sys

year = input("Enter a year: ")

if len(year) != 4:
    print("Please enter a valid year!")
    sys.exit("exiting...")

if int(year) % 4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
