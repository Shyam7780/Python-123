class Animal:
  def __init__(self,name,speciies):
    self.name=name
    self.species=speciies
  def make_sound(self):
    print("sound made by the animal")

class dog(Animal):
  def __init__(self,name,breed):
    Animal.__init__(self,name,species="Dog")
    self.breed=breed

  def make_sound(self):
    print("Bark Brak")

    
d=dog("mukku","Labrador")
d.make_sound()
