l=[]
sum=0
n=int(input("Enter Size of binary number"))
for i in range(n):
  l.append(int(input("Enter the binary digit")))
print("Binary number is",l)
while n>0:
  sum=sum+l[n-1]*2**(n-1)
  n=n-1
print("Decimal value is:",sum)