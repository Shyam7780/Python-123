class Company:
    def __init__(self,companyName):
        self.companyName=companyName
    def address(self):
        print("Patna")
    def getName(self):
        return self.companyName
    
    
class Employee(Company):
    def __init__(self,name,id,companyName):
        self.name=name
        self.id=id
        super().__init__(companyName)
    def work(self):
        print("Software Engineer")
    def getName(self):
        print(super().getName())
        return self.name
e1=Employee('Shyam kumar','25bcs095','Google')
print(e1.getName())        