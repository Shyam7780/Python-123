def Binary(n):
  l1=[]
  while n > 0:
    if n % 2 == 0:
      l1.append(0)
    else:
      l1.append(1)
    n = n // 2  
  l1.reverse()
  return l1
n=int(input("Enter a number: "))
print(Binary(n))
