n=str(input("Enter the number to check Armstrong number: "))
sum=0
for i in range(0,len(n)):
    sum=sum+int(n[i])**3
if sum==int(n):
    print("This is Armstrong number")
else:
    print("This is not Armstrong number")