class Employee:
  companyname="Apple"
  noOfEmployees=0
  def __init__(self,name):
    self.name=name
    self.raise_amount=0.02
    self.selery=100000
    Employee.noOfEmployees +=1
  def showdetails(self):
    print(f"The name of the Employee is {self.name}End="" and the raise amount in {self.noOfEmployees} End=" "sized {self.companyName} End=" "is {self.raise_amount}End=" " selery of employees{self.selery}")

emp1=Employee("Shyam kumar")
emp1.raise_amount=0.3
emp1.companyName="Apply India"
emp1.showdetails()
emp2=Employee("Rishu kumar")
emp2.showdetails()
