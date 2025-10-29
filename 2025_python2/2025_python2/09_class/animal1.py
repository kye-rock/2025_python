class Animal:
  def __init__(self, name, location):
    self.name = name
    self.location = location

  def show_info(self):
    print(f"이름: {self.name}, 위치: {self.location}")


#---------------

class Lion(Animal):
  def roar(self):
    print("어흥!")

class Bear(Animal):
  def hunt(self):
    print("곰이 사냥을 합니다.")

class Giraffe(Animal):
  def eat_leaves(self):
    print("기린이 나뭇잎을 먹습니다.")


# ----------- 실행 -----------

lion1 = Lion("사자", "아프리카")
bear1 = Bear("곰", "북극")
giraffe1 = Giraffe("기린", "사파리")

lion1.show_info()
bear1.show_info()
giraffe1.show_info()

lion1.roar()
bear1.hunt()
giraffe1.eat_leaves()