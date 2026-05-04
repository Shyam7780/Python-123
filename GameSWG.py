
import random

def check(comp,use):
  if comp==use:
    return 0
  if(comp==0 and use==1):
    return -1
  if(comp==0 and use==2):
    return 1
  if(comp==1 and use==0):
    return 1
  if(comp==1 and use==2):
    return -1
  if(comp==2 and use==0):
    return -1
  if(comp==2 and use==1):
    return 1

for i in range(20):
 count=0
 use=int(input("0 for Paper,1 for Stone and, 2 for Scissor\n >"))
 comp=random.randint(0,2)
 print("You",use)
 print("Computer",comp)
 val=check(comp,use)
 if(val==0):
   print("Match is Draw")
 elif(val==1):
   print("You are Winner")
   count+=1
 elif(val==-1):
   print("Computer Is Win")
print(count)