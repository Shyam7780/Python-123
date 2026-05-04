n=int(input("Enter the size of list number :"))
l=[]
for i in range(0,n):
  l.append(int(input()))
print("Oringinal list :",l)
s=sorted(l)
print("Sorted list :",s)
