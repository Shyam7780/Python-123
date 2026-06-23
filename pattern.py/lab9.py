def filter_evens(l):
  return list(filter(lambda x: x%2==0, l))

l=[2,4,3,5,6,7,8,9]
print(filter_evens(l))