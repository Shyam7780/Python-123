l=[]
n=int(input("Enter the number"))
while n>0:
  if n%2==0:
    l.append(0)
  else:
    l.append(1)
  n=n//2
l.reverse()
print(l)