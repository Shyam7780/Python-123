n=str(input("Enter the number to check Palindrome: "))
rev=n[::-1]
print(rev)
if rev==n:
  print("This is palindromic number")
else:
  print("This is not palindromic number")