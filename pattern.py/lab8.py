def palindrome(n):
    rev=n[::-1]
    print(rev)
    if rev==n:
        print("The number is Palindrome")
    else:
        print("The number is not Palindrome")
n=str(input("Enter the number to check Palindrome: "))
palindrome(n)