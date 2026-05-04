class personal:
  name="Shyam kumar"
  occupation = "Software Developer"
  course="B.Tech"
  income=0
  Adress="Tej partap nagar"
  def info(self):
    print(f"{self.name} is a {self.occupation}")
    print(f" Adress={self.Adress}")
  
a=personal()
b=personal()
c=personal()
b.name="Sittu kumar"
b.occupation="Student"
c.name="Bittu kumar" 
c.occupation="Student"
a.info()
b.info()
c.info()
