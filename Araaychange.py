l=[]
n=int(input("Enter the Size of Array: "))
for i in range(n):
  l.append(int(input("Enter the Element")))
print("Enter the Adress of Delete Array")
n=int(input('Enter the element'))
for i in range(n,0):
  i[i]=l[i+1]
print("Deleted Array",l)
