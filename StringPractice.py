import sys
import os
import random

# dealing with class and objects

class Animal:
    __name = ""  #__ indicates private
    __height = 0
    __weight = 0
    __sound = 0

    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    def set_name(self, name): #'self' works like 'this' in other languages
        self.__name=name

    def get_name(self):
        return self.__name

    def set_height(self,height):
        self.__height=height

    def get_height(self):
        return self.__height

    def set_weight(self,weight):
        self.__height=weight

    def get_weight(self):
        return self.__weight

    def set_sound(self,sound):
        self.__sound=sound

    def get_sound(self):
        return self.__sound

    def get_type(self):
        print("Animal")

    def toString(self):
        return "{} is {} cm toll and {} kilogram and says {}".format(self.__name,
                                                                     self.__height,
                                                                     self.__weight,
                                                                     self.__sound)

cat = Animal('White Cat',33,10,"Meow")
print(cat.toString())


#Using INHERITANCE
class Dog(Animal):
    __owner = ""

    def __init__(self,name,height,weight,sound,owner):
        self.__owner = owner
        super(Dog,self).__init__(name,height,weight,sound)

    def set_owner(self,owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print("Dog")

    def toString(self):
        return "{} is {} cm toll and {} kilogram and says {} and owner is {}".format(self.get_name(),
                                                                                     self.get_height(),
                                                                                     self.get_weight(),
                                                                                     self.get_sound(),
                                                                                     self.__owner)
    
    #METHOD OVERLOADING
    def multiple_sounds(self, how_many=None):  #'None' represents that it is OK if no value is sent for 									  
    									 #'how_many'
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound()*how_many)

spot = Dog('Spot',53,27,"Ruff","Miller")
print(spot.toString())
print(spot.multiple_sounds(3))


#POLYMORPHISM
class AnimalTesting:
    def get_type(self,animal):
        animal.get_type()

test_animals= AnimalTesting()
test_animals.get_type(cat)
test_animals.get_type(spot)
print(spot.multiple_sounds(3))
print(spot.multiple_sounds())