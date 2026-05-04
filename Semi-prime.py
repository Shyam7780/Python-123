def prime(l,start,end):
  
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                l.append(num)
      
def semiPrime(l,l1):
    for i in range(len(l)):
        for j in range(1,len(l)):
            l1.append(l[i]*l[j])
def add(l1,n):
    for i in range(len(l1)):
        for j in range(1,len(l1)):
            if (l1[i]+l1[j]==n or 2*l1[i]==n):
                print(f"{n} is a semi-prime number")
            return
        else:
                print(f"{n} is NOT a semi-prime number")
l=[]
l1=[]
n=int(input("Enter the check number for semiprime number are not :->"))
prime(l,2,n)
semiPrime(l,l1)
add(l1,n)
    