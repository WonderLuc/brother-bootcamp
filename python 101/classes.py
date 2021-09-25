class MyClass():
  x = 5
  def showNumber(n):
    print('Number')

my = MyClass() # instance of class
my.showNumber() # Number


class Animal():
  def __init__(self, name, isFlying):
    self.__name = name
    self.__isFlying = isFlying
  
  @property
  def name(self):
    return self.__name

  @name.setter
  def name(self, name):
    if (type(name) != str): return
    self.__name = name


class Dog(Animal):
  def __init__(self, name, isFlying, breed):
    super().__init__(name, isFlying)
    self.breed = breed
  
  def search(self):
    print(f'{self.name} now searching')

class Bird(Animal):
  def fly(self):
    print(f'{self.name} is flying')

class Parrot(Bird):
  def fly(self):
    print(f'{self.name} is flying low and already tried')

class Raven(Bird):
  def fly(self):
    super().fly()
    print(f'{self.name} is flying high. LOL')

parrot = Parrot('Oldrik', True)
raven = Raven('Herugrim', True)
parrot.fly() # Oldrik is flying low and already tried
raven.fly()
# Herugrim is flying
# Herugrim is flying high. LOL







