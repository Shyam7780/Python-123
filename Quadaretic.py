a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))
d=b**2 - 4*a*c
if d>0:
    print("Roots are real and different")
elif d==0:
    print("Roots are real and same")
else:
    print("Roots are complex and and different")