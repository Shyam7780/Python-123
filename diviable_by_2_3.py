#diviable by 2 and 3
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is divisible by 2")
if num % 3 == 0:
    print(f"{num} is divisible by 3")
if num % 2 == 0 and num % 3 == 0:
    print(f"{num} is divisible by both 2 and 3")