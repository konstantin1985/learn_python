
# USEFUL LINKS:

# Code a set of six class statements to model this taxonomy with Python
# inheritance. Then, add a speak method to each of your classes that prints
# a unique message, and a reply method in your top-level Animal superclass
# that simply calls self.speak to invoke the category-specific message printer
# in a subclass below (this will kick off an independent inheritance search
# from self). 

# Finally, remove the speak method from your Hacker class so that it picks
# up the default above it. When you're finished, your classes should work
# this way:
# >>> spot = Cat()                                         
# >>> spot.reply()                                            # Animal.reply: calls Cat.speak
# meow
# >>> data = Hacker()
# >>> data.reply()                                            # Animal.reply: calls Primate.speak 
# Hello world!

import abc


class Animal:
    __metaclass__  = abc.ABCMeta
    
    def reply(self):
        self.speak()
    
    @abc.abstractmethod
    def speak(self):
        "Method that should do something"

    
class Mammal(Animal):
    pass


class Cat(Mammal):
    
    def speak(self):
        print("Meow")
    
    
class Dog(Mammal):
    
    def speak(self):
        print("Bark")


class Primate(Mammal):
    
    def speak(self):
        print("Hello world")

    
class Hacker(Primate):    
    pass

spot = Cat()
spot.reply()
# Meow

data = Hacker() 
data.reply()
# Hello world

# Notice that the self.speak reference in Animal triggers an
# independent inheritance search, which finds speak in a subclass.

    