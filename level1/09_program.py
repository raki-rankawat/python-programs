"""
           [ Start: Input Year ]
                     |
            Is it divisible by 4?
           /                     \
        (No)                    (Yes)
         /                         \
 [ Common Year ]            Is it divisible by 100?
                            /                     \
                         (No)                    (Yes)
                          /                         \
                  [ Leap Year ]             Is it divisible by 400?
                                            /                     \
                                         (No)                    (Yes)
                                          /                         \
                                  [ Common Year ]             [ Leap Year ]
"""

import sys

year = input("Enter a year: ")

if len(year) != 4:
    print("Please enter a valid year!")
    sys.exit("exiting...")

year = int(year)

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is a common year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is a common year")
