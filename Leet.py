L1=[]
L2=[]
La=[]
n=int(input("Enter the size of list: "))
print("Enter the first list: ")
for i in range(n):
 L1.append(int(input()))
print("Enter the second list: ")
for i in range(n):
 L2.append(int(input()))
c=0
for i in range(len(L1)):
  La=L1[i]+L2[i]+c
  if(La[i]>10):
   N=La[i]%10
   c=La[i]/10
   La[i]=N

print(La)