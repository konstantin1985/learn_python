

# MAIN SOURCE:
# Kasampalis "Mastering Python Patterns" Chapter 1

# USEFUL LINKS:
# http://code.activestate.com/recipes/86900/ - Generic factory implementation
# https://stackoverflow.com/questions/4960208/python-2-7-getting-user-input-and-manipulating-as-string-without-quotations

# GENERAL INFORMATION:

# The Abstract Factory design pattern is a generalization of Factory Method.
# Basically, an Abstract Factory is a (logical) group of Factory Methods, 
# where each Factory Method is responsible for generating a different kind
# of object.

print("-" * 20 + "# 1 Use Cases" + "-" * 20)

# Since the Abstract Factory pattern is a generalization of the Factory
# Method pattern, it offers the same benefits: it makes tracking an object
# creation easier, it decouples an object creation from an object usage,
# and it gives us the potential to improve the memory usage and performance
# of our application.

# But a question is raised: how do we know when to use the Factory Method
# versus using an Abstract Factory? The answer is that we usually start
# with the Factory Method which is simpler. If we find out that our appli-
# cation requires many Factory Methods which it makes sense to combine for
# creating a family of objects, we end up with an Abstract Factory.

# A benefit of the Abstract Factory that is usually not very visible from
# a user's point of view when using the Factory Method is that it gives us
# the ability to modify the behavior of our application dynamically (in
# runtime) by changing the active Factory Method. The classic example is
# giving the ability to change the look and feel of an application (for 
# example, Apple-like, Windows-like, and so on) for the user while the app-
# lication is in use, without the need to terminate it and start it again.

print("-" * 20 + "# 2 Implementation" + "-" * 20)

# Imagine that we are creating a game or we want to include a mini-game
# as part of our application to entertain our users. We want to include
# at least two games, one for children and one for adults. We will decide
# which game to create and launch in runtime, based on user input. An
# Abstract Factory takes care of the game creation part.

# The FrogWorld class is an Abstract Factory. Its main responsibilities
# are creating the main character and the obstacle(s) of the game. Keeping
# the creation methods separate and their names generic (for example, 
#make_character(), make_obstacle()) allows us to dynamically change the
# active factory (and therefore the active game) without any code changes.
# In a statically typed language, the Abstract Factory would be an abstract
# class/interface with empty methods, but in Python this is not required
# because the types are checked in runtime.

# There will be 2 games: 
# - one for children (FrogWorld)
# - one for adults (WizardWorld)  

# Character of a child's game 
class Frog:
    
    # Character has its own name
    def __init__(self, name): self.name = name

    def __str__(self): return self.name
    
    def interact_with(self, obstacle):
        # format(self, obstacle... - invoke __str__()
        print('{} the From encounters {} and {}!'.format(self, obstacle,   
                                                         obstacle.action()))
# Obstacle of a child's game
class Bug:
    
    def __str__(self): return "a bug"
    
    def action(self): return "eats it"
    
# Abstract factory of child's game
class FrogWorld:
    
    def __init__(self, name):
        print(self)
        self.player_name = name
    
    def __str__(self): return "\n\n\t----- Frog World -----"

    def make_character(self): return Frog(self.player_name)
    
    def make_obstacle(self): return Bug()
    
# Character of an adult's game
class Wizard:
    
    def __init__(self, name): self.name = name
    
    def __str__(self): return self.name
    
    def interact_with(self, obstacle):
        print('{} the Wizard battles against {} and {}!'.format(self, obstacle,
                                                                obstacle.action()))
# Obstacle of a adult's game
class Ork:
    
    def __str__(self): return "an ork"
    
    def action(self): return "enchants it"

# Abstract factory of adult's game
class WizardWorld:
    
    def __init__(self, name):
        print(self)
        self.player_name = name
    
    def __str__(self): return "\n\n\t----- Wizard World -----"
    
    def make_character(self): return Wizard(self.player_name)
    
    def make_obstacle(self): return Ork()

# The GameEnvironment is the main entry point of our game. It accepts
# factory as an input, and uses it to create the world of the game.
# The play() method initiates the interaction between the created hero
# and the obstacle.
class GameEnvironment:
     
    def __init__(self, factory):
        self.character = factory.make_character()
        self.obstacle = factory.make_obstacle()
    
    def play(self):
        self.character.interact_with(self.obstacle)

def validate_age(name):
    try:
        # IMPORTANT: how to enter user data
        age = raw_input('Welcome {}. How old are you?'.format(name))
        age = int(age)
    except ValueError as err:
        print("Age {} is invalid, please try again...".format(age))
        return (False, age)
    return (True, age)

def main():
    name = raw_input("Hello. What is your name?")

    # IMPORTANT: how to ask for input until it's correct
    valid_input = False 
    while not valid_input:
        valid_input, age = validate_age(name)
    
    # IMPORTANT: tricky if/else operator
    game = FrogWorld if age < 18 else WizardWorld
    environment = GameEnvironment(game(name))
    environment.play()
    
if __name__ == "__main__":
    main()

# Hello. What is your name?Gelfand
# Welcome Gelfand. How old are you?20
# 
# 
#    ----- Wizard World -----
# Gelfand the Wizard battles against an ork and enchants it!

# Hello. What is your name?Bob
# Welcome Bob. How old are you?15
# 
# 
#     ----- Frog World -----
# Bob the From encounters a bug and eats it!


# input() works differently in Python 3.X and 2.X. so I used raw_input
 