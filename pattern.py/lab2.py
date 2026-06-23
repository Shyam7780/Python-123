dict={'shyam':92,'Sourabh':93,'Shivdev':82,'Abhinav':95}
temp=92
for i in dict.values():
  if temp>i:
    temp=i

print("hight score in the school",temp)
