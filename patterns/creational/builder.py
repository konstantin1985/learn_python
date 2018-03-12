


# MAIN SOURCE:
# Kasampalis, "Mastering Python Design Patterns"


# USEFUL LINKS:
# 1) Python enums
#    https://stackoverflow.com/questions/36932/how-can-i-represent-an-enum-in-python
#
# 2) How to instull Enum34 (like Enum for 2.7) pip https
# https://github.com/pypa/pip/issues/990
# sudo pip install --index-url=https://pypi.python.org/simple/ enum34
#
# 3) On creational patterns
# https://en.wikipedia.org/wiki/Creational_pattern


# GENERAL INFORMATION:

# As modern software engineering depends more on object composition than
# class inheritance, emphasis shifts away from hard-coding behaviors
# toward defining a smaller set of basic behaviors that can be composed
# into more complex ones. Hard-coding behaviors are inflexible because
# they require overriding or re-implementing the whole thing in order to
# change parts of the design. Additionally, hard-coding does not promote
# reuse and makes it difficult to keep track of errors. For these reasons,
# creational patterns are more useful than hard-coding behaviors. Creational
# patterns make design become more flexible. They provide different ways to
# remove explicit references in the concrete classes from the code that needs
# to instantiate them. In other words, they create independency for objects
# and classes.

# Consider applying creational patterns when:
# - A system should be independent of how its objects and products are created.
# - A set of related objects is designed to be used together.
# - Hiding the implementations of a class library or product, revealing only their interfaces.
# - Constructing different representation of independent complex objects.
# - A class wants its subclass to implement the object it creates.
# - The class instantiations are specified at run-time.
# - There must be a single instance and client can access this instance at all times.
# - Instance should be extensible without being modified.

# Imagine that we want to create an object that is composed of
# multiple parts and the composition needs to be done step by
# step. The object is not complete unless all its parts are
# fully created.

# The Builder pattern separates the construction of a complex
# object from its representation.

# The HTML page generation problem can be solved using the Builder
# pattern. In this pattern, there are two main participants: the
# builder and the director. The builder is responsible for creating
# the various parts of the complex object. In the HTML example, 
# these parts are the title, heading, body, and the footer of the 
# page. The director controls the building process using a builder
# instance. The HTML example means for calling the builder's functions
# for setting the title, the heading, and so on. Using a different
# builder instance allows us to create a different HTML page without
# touching any code of the director.

print("-" * 20 + "# 1 Use Cases" + "-" * 20)

# We use the Builder pattern when we know that an object must be 
# created in multiple steps, and different representations of the
# same construction are required.

# At this point, the distinction between the Builder pattern and
# the Factory pattern might not be very clear. The main difference
# is that a Factory pattern creates an object in a single step,
# whereas a Builder pattern creates an object in multiple steps,
# and almost always through the use of a director.

# Another difference is that while a Factory pattern returns a
# created object immediately, in the Builder pattern the client
# code explicitly asks the director to return the final object
# when it needs it.

# The new computer analogy might help to distinguish between a 
# Builder pattern and a Factory pattern. Assume that you want to
# buy a new computer. If you decide to buy a specific preconfigured
# computer model, for example, the latest Apple 1.4 GHz Mac mini, 
# you use the Factory pattern. All the hardware specifications are
# already predefined by the manufacturer, who knows what to do
# without consulting you. The manufacturer typically receives
# just a single instruction.

MINI14 = '1.4 GHz Mac mini'

class AppleFactory:
    
    class MacMini14:
        def __init__(self):
            self.memory = 4 # in GB
            self.hdd = 500 # in GB
            self.gpu = 'Intel HD Graphics 5000'
        
        def __str__(self):
            info = ('Model: {}'.format(MINI14),
                    'Memory: {} GB'.format(self.memory),
                    'Hard Disk: {} GB'.format(self.hdd),
                    'Graphics: {}'.format(self.gpu))
            
            # INTERESTING way to represent information with tuple
            return '\n'.join(info)    
            
    def build_computer(self, model):
        if(model == MINI14):
            return self.MacMini14()
        else:
            print("I don't know how to build {}".format(model))
            
if __name__ == "__main__":
    afac = AppleFactory()
    mac_mini = afac.build_computer(MINI14)
    print(mac_mini)

# OUTPUT:
# Model: 1.4 GHz Mac mini
# Memory: 4 GB
# Hard Disk: 500 GB
# Graphics: Intel HD Graphics 5000

# Another option is buying a custom PC. In this case, you use
# the Builder pattern. You are the director that gives orders
# to the manufacturer (builder) about your ideal computer
# specifications.

class Computer:
    def __init__(self, serial_number):
        self.serial = serial_number
        self.memory = None
        self.hdd = None
        self.gpu = None
        
    def __str__(self):
        info = ('Memory: {} GB'.format(self.memory),
                'Hard Disk: {} GB'.format(self.hdd),
                'Graphics: {}'.format(self.gpu))
        return '\n'.join(info)
    
class ComputerBuilder:
    def __init__(self):
        self.computer = Computer("AG1351412")
        
    def configure_memory(self, amount):
        self.computer.memory = amount
    
    def configure_hdd(self, amount):
        self.computer.hdd = amount
        
    def configure_gpu(self, model):
        self.computer.gpu = model

# Director class for HardwareBuilder
class HardwareEngineer:
    
    def __init__(self):
        self.builder = None
    
    def construct_computer(self, memory, hdd, gpu):
        self.builder = ComputerBuilder()
        self.builder.configure_memory(memory)
        self.builder.configure_hdd(hdd)
        self.builder.configure_gpu(gpu)
        
    @property
    def computer(self):
        return self.builder.computer

def main():
    engineer = HardwareEngineer()
    engineer.construct_computer(hdd=500, memory=8, gpu = "GeForce GTX 650 Ti")
    computer = engineer.computer
    print(computer)

# Memory: 8 GB
# Hard Disk: 500 GB
# Graphics: GeForce GTX 650 Ti

if __name__ == "__main__":
    main()

# The basic changes are the introduction of a builder ComputerBuilder,
# a director HardwareEngineer, and the step-by-step construction of a
# computer, which now supports different configurations.

print("-" * 20 + "# 2 Implementation" + "-" * 20)

# The pizza example is particularly interesting because a pizza is
# prepared in steps that should follow a specific order. To add the
# sauce, you first need to prepare the dough. To add the topping,
# you first need to add the sauce. And you can't start baking the
# pizza unless both the sauce and the topping are placed on the
# dough. Moreover, each pizza usually requires a different baking
# time, depending on the thickness of its dough and the topping used.

# A builder creates an instance of the end product and makes sure
# that it is properly prepared. That's why the Pizza class is so
# minimal. It basically initializes all data to sane default values.
# An exception is the prepare_dough() method. The prepare_dough()
# method is defined in the Pizza class instead of a builder for
# two reasons:
# - To clarify the fact that the end product is typically minimal
#   does not mean that you should never assign it any responsibilities
# - To promote code reuse through composition

# There are two builders. Each builder creates a Pizza instance
# and contains methods that follow the pizza-making procedure:
# prepare_dough(), add_sauce(), add_topping(), and bake(). To be
# precise, prepare_dough() is just a wrapper to the prepare_dough()
# method of the Pizza class.

# The director in this example is the waiter. The core of the Waiter
# class is the construct_pizza() method, which accepts a builder as
# a parameter and executes all the pizza preparation steps in the
# right order. Choosing the appropriate builder, which can even be
# done in runtime, gives us the ability to create different pizza
# styles without modifying any code of the director (Waiter). The
# Waiter class also contains the pizza() method, which returns the
# end product (prepared pizza) as a variable to the caller.

# The validate_style() function is used to make sure that the user
# gives valid input, which in this case is a character that is mapped
# to a pizza builder.

from enum import Enum
import time

# 'PizzaProgress' - name
# 'queued preparation baking ready' - enum valueS
PizzaProgress = Enum('PizzaProgress', 'queued preparation baking ready')
PizzaDough = Enum('PizzaDough', 'thin thick')
PizzaSauce = Enum('PizzaSouce', 'tomato creme')
PizzaTopping = Enum('PizzaTopping', 'mozzarella bacon ham mushrooms')
STEP_DELAY = 2 # in seconds for example

class Pizza:
    
    def __init__(self, name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []
    
    def __str__(self):
        return self.name
    
    # Just for example (it could have been in the Builder)
    def prepare_dough(self, dough):
        self.dough = dough
        print('preparing the {} dough of your {}...'.format(self.dough.name, self))
        time.sleep(STEP_DELAY)
        print('done with the {} dough'.format(self.dough.name))
        
class MargaritaBuilder:
    def __init__(self):
        self.pizza = Pizza('margarita')
        self.progress = PizzaProgress.queued
        self.baking_time = 2 # Can be different for different pizza
    
    # Just a wrapper
    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thin)
    
    def add_sauce(self):
        print('adding the tomato sauce to your margarita...')
        self.pizza.sauce = PizzaSauce.tomato
        time.sleep(STEP_DELAY)
        print('done with the tomato sauce')
        
    def add_topping(self):
        print('adding the topping (mozzarella, mushrooms) to your margarita')
        self.pizza.topping.append([PizzaTopping.mozzarella, 
                                   PizzaTopping.mushrooms])
        time.sleep(STEP_DELAY)
        print('done with the topping (mozzarella, mushrooms)')
        
    def bake(self):
        self.progress = PizzaProgress.baking
        print('baking your margarita for {} seconds'.format(self.baking_time))
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print('your margarita is ready')


class CreamyBaconBuilder:
    def __init__(self):
        self.pizza = Pizza('creamy bacon')
        self.progress = PizzaProgress.queued
        self.baking_time = 4 # Can be different for different pizza
    
    # Just a wrapper
    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thick)
    
    def add_sauce(self):
        print('adding the creme sauce to your creamy bacon...')
        self.pizza.sauce = PizzaSauce.tomato
        time.sleep(STEP_DELAY)
        print('done with the creme sauce')
        
    def add_topping(self):
        print('adding the topping (bacon) to your creamy bacon')
        self.pizza.topping.append([PizzaTopping.bacon])
        time.sleep(STEP_DELAY)
        print('done with the topping (bacon)')
        
    def bake(self):
        self.progress = PizzaProgress.baking
        print('baking your creamy bacon for {} seconds'.format(self.baking_time))
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print('your creamy bacon is ready')

# Director class for the builders
class Waiter:

    def __init__(self):
        self.builder = None
    
    # We may have different builder for each new order
    def construct_pizza(self, builder):
        self.builder = builder
        # The correct sequence is important
        [step() for step in (builder.prepare_dough,
                             builder.add_sauce,
                             builder.add_topping,
                             builder.bake)]
    
    # Another difference is that while a Factory pattern returns a
    # created object immediately, in the Builder pattern the client
    # code explicitly asks the director to return the final object
    # when it needs it.
    @property
    def pizza(self):
        return self.builder.pizza

# IMPORTANT: how valid_input is used here to have a loop
# until the correct input is provided 
def validate_style(builders):
    try:
        pizza_style = raw_input('What pizza would you like, [m]argarita or [c]reamy bacon: ')
        builder = builders[pizza_style]()
    except:
        return (False, None)
    return (True, builder)


def main():
    
    # We don't create builder objects here, because
    # it may never be "oredered"
    builders = {'m': MargaritaBuilder, 'c': CreamyBaconBuilder}
    waiter = Waiter()
    
    builders['m']()
    print('after')
    
    valid_style = False
    while not valid_style:
        valid_style, builder = validate_style(builders)
    
    waiter.construct_pizza(builder)
    pizza = waiter.pizza
    print("\nEnjoy your {} pizza".format(pizza))
    
if __name__ == "__main__":
    main()


# A Builder pattern is usually a better candidate than a Factory
# pattern when:
# - We want to create a complex object (an object composed of many
#   parts and created in different steps that might need to follow
#   a specific order) - (KS: the order may be different and is guided
#   by a director class)
# - Different representations of an object are required, and we want
#   to keep the construction of an object decoupled from its
#   representation
# - We want to create an object at one point in time but access it at
#   a later point

