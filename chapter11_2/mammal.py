class Mammal:
    def __init__(self, species, age):
        self.species = species
        self.age = age
    
class Person(Mammal):
    def __init__(self, species, age, name, job):
        super().__init__(species, age)
        self.name = name
        self.job = job
    
m1 = Mammal("동물", 30)
m2 = Person("동물", 30, "kim", "Engineer")

print(f"포유류: {m1.species}{m1.age}")
print(f"사람: {m2.name} {m2.age}{m2.job}")