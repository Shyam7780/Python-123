class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class programmer(Employee):
  def __init__(self, name, id, language):
   super().__init__(name, id)
   self.language = language

Shyam= programmer("Shyam", 101, "Python")
Harry = Employee("Harry", 102, "Java")
print(Shyam.name)  
print(Shyam.id)        # Output: Shyam     