str = input("Enter a integer: ")

newStr = ""

for letter in reversed(str):
    newStr = newStr + "" + letter

if str == newStr:
    print(f"{str} is palindrome")
else:
    print(f"{str} is not palindrome")
