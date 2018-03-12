# MAIN SOURCE:
# Kasampalis "Mastering Python Patterns" Chapter 4

# USEFUL LINKS:

# GENERAL INFORMATION:

# Structural design patterns deal with the relationships between
# the entities (such as classes and objects) of a system. A 
# structural design pattern focuses on providing a simple way of
# composing objects for creating new functionality.

# Adapter is a structural design pattern that helps us make two
# incompatible interfaces compatible. If we have an old component
# and we want to use it in a new system, or a new component that
# we want to use in an old system, the two can rarely communicate
# without requiring any code changes. But changing the code is not
# always possible, either because we don't have access to it or 
# because it is impractical. In such cases, we can write an extra
# layer that makes all the required modifications for enabling the
# communication between the two interfaces. This layer is called 
# the Adapter.

# In general, if you want to use an interface that expects function
#_a() but you only have function_b(), you can use an Adapter to
# convert (adapt) function_b() to function_a(). This is not only
# true for functions but also for function parameters. An example
# is a function that expects the parameters x, y, and z but you
# only have a function that works with the parameters x and y at hand.

print("-" * 20 + "# 1 Use Cases" + "-" * 20)

# The Adapter pattern is used for making things work after they have
# been implemented. Usually one of the two incompatible interfaces is
# either foreign or old/legacy. If the interface is foreign, it means
# that we have no access to the source code. 

# If it is old it is usually impractical to refactor it. We can take
# it even further and argue that altering the implementation of a
# legacy component to meet our needs is not only impractical, but it
# also violates the open/close principle. 

# The open/close principle is one of the fundamental principles of
# Object-Oriented design (the O of SOLID). It states that a software
# entity should be open for extension, but closed for modification.
# That basically means that we should be able to extend the behavior
# of an entity without making source code modifications. Adapter
# respects the open/closed principle.

# Therefore, using an Adapter for making things work after they have
# been implemented is a better approach because it:
# - Does not require access to the source code of the foreign interface
# - Does not violate the open/closed principle

print("-" * 20 + "# 2 Implementation" + "-" * 20)

# External class, main method is play()
class Synthesizer:
    
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return 'the {} synthesizer'.format(self.name)
    
    def play(self):
        return "is playing an electronic song"
    
# External class, main method is speak()
class Human:
    
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return "{} the human".format(self.name)
    
    def speak(self):
        return "say hello"
    
# The client only knows how to call the execute() method, and
# it has no idea about play() or speak(). How can we make the
# code work without changing the Synthesizer and Human classes?
class Computer:
    
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return "the {} computer".format(self.name)
    
    def execute(self):
        return "executes a program"

# We create a generic Adapter class that allows us to adapt a
# number of objects with different interfaces, into one unified
# interface.
class Adapter:
    
# The obj argument of the __init__() method is the object that
# we want to adapt, and adapted_methods is a dictionary containing
# key/value pairs of method the client calls/method that should
# be called.
  
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)
        
    def __str__(self):
        return str(self.obj)
    
    # If we want to get some attributes of an adapted object, we
    # need to delegate to the adapted object
    def __getattr__(self, name):
        return self.obj.name
        
    
def main():
    objects = [Computer('Asus')]
    
    # When we'll call execute on the adapted synth object,
    # its method synth.play will be invoked. 
    synth = Synthesizer('moog')
    objects.append(Adapter(synth, dict(execute=synth.play)))
    
    # When we'll call execute on the adapted synth object,
    # its method synth.play will be invoked.
    human= Human('Bob')
    objects.append(Adapter(human, dict(execute=human.speak)))
    
    for obj in objects:
        print("{} {}".format(str(obj), obj.execute()))
    
    for obj in objects:
        print(obj.name)
    
if __name__ == "__main__":
    main()

# OUTPUT:
# the Asus computer executes a program
# the moog synthesizer is playing an electronic song
# Bob the human say hello
# Asus
# moog
# Bob 

# In the implementation section, we saw how to achieve interface
# conformance using the Adapter pattern without modifying the source
# code of the incompatible model. This is achieved through a generic
# Adapter class that does the work for us. Although we could use 
# sub-classing (inheritance) to implement the Adapter pattern in the
# traditional way in Python, this technique is a great alternative.


