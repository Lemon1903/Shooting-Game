from abc import ABC, abstractmethod
import pygame as pg

class Animal(ABC):
    @abstractmethod
    def get_age_after_2_years(self): pass

    @abstractmethod
    def move(self): pass

class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.age = 10

    def get_age_after_2_years(self):
        return self.age*2

    def move(self):
        print("I can walk")

dog = Dog()
print(dog.get_age_after_2_years())