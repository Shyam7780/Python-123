#prime number
N=int(input("Enter the number"))
l=[]
l1=[]
for i in range(2,N):
  for j in range(2,N):
    if i%j==0:
      count=1
    if count==1:
      l.append(i)
for i in range(len(l)):
  for j in range(1,len(l)):
    l1.append(l[i]*l[j])
for i in range(len(l1)):
  for j in range(1,len(l1)):
    if (l1[i]+l1[j]==N or 2*l1[i]==N):
      print("this is semiprime number")
    else:
      print("this is not semiprime number")