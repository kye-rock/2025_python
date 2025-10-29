class Dog:
  def __init__(self, name, age):
    self._name = name
    self._age = age

  def getName(self):
    return self._name

  def getAge(self):
    return self._age

  def bark(self):
    print(self._name, "is barking")

x = Dog("jack", 3)
y = Dog("Daisy", 2)
x.bark()
y.bark()

print(x.getName(), "is", x.getAge(), "years old")
print(y.getName(), "is", y.getAge(), "years old")