# Sametriangle Pattern
n=int(input("Enter the value of N"))
for i in range(n):
  for j in range(n-i):
    print(" ",end="")

  for k in range(i):
    print("* ",end="")
  print()
  if i==n-1:
    for i in range(n):
      for j in range(i+1):
        print(" ",end="")

      for k in range(n-i):
        print("* ",end="")
      print()