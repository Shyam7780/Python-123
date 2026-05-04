#classmethod
class Employee:
  company="Apple"
  def show(self):
    print(f"The company name is -> {self.name},and company name is -> {self.company},Salary is {self.salary}" )
  @classmethod
  def changecompany(cls,newcompany):
    cls.company=newcompany
e1=Employee()
e1.name="shyam kumar"
e1.changecompany("Google")
e1.salary=100000
e1.show()
a=2786
rev=int(str(a)[::-1])
print(rev)