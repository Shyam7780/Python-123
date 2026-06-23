# make upward triangle
n=int(input("Enter the value of n"))
for i in range(n):
  for j in range(i+1):
    print(j+1,end="")
  print()