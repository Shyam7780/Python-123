class Coordinate:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return Coordinate(self.x+other.x,self.y+other.y)
    def __sub__(self,other):
        return Coordinate(self.x-other.x,self.y-other.y)
    def __str__(self):
        return f"X: {self.x},Y:{self.y}"
C1=Coordinate(2,3)
c2=Coordinate(1,2)
C3=C1+c2
C4=C1-c2
print(C3)
print(C4)