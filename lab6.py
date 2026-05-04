l=[]
l1=[]
for i in range(2,1000):
  count=0
  for j in range(2,1000):
    if i%j==0:
      count+=1
  if count==1:
      l.append(i)
for i in range(len(l)-1):
   if l[i+1]-l[i]==2:
      l1.append((l[i], l[i+1]))
print(l1)

