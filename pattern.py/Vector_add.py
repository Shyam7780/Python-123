class vector:
  def __init__(self, i, j,k):
    self.i=i
    self.j=j
    self.k=k
  def __str__(self):
    return f"{self.i}i +{self.j}j+{self.k}k"
  def __add__(self, x):
    return vector(self.i+x.i, self.j+x.j, self.k+x.k)
v1=vector(2,3,4)
v2=vector(5,6,7)
print("Vector 1:",v1)
print("Vector 2:",v2)
print("Addition of two Vectors:",v1+v2)