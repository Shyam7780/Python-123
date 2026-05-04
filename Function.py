def Area(l,b):
 A=l*b
 print("Area of retringle =",A)

def perimeter(l,b):
 P=2*(l+b)
 print("perimeter of the retringle =",P)
def Average(num):
 sum=0
 for i in range(1,num+1):
   sum=sum+i
 return sum/num
  #  print("Average of a number =",avg)

a=int(input("Enter the value of a :"))
b=int(input("Enter the value of b :"))
# Aear of retringle
Area(a,b)
# perimeter of retriangle
perimeter(a,b)
# Average of a 
c=Average(8)
print(c)