# SECTION 5: ABSTRACT METHOD

print("="*60)
print("SECTION 5: ABSTRACT METHOD")
print("="*60)

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass
    @abstractmethod
    def move(self):
        pass
    @abstractmethod
    def sleep(self):
        pass

class Dog(Animal):

    def make_sound(self):
        print("hav hav hav")
    def move(self):
        print("walk or run")
    def sleep(self):
        print("sleeping")

barley = Dog("Barley")
barley.make_sound()

