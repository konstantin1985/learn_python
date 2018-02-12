
# USEFUL LINKS




# Composition. Simulate a fast-food ordering scenario by defining four classes:
# Lunch    : A container and controller class
# Customer : The actor who buys food
# Employee : The actor from whom a customer orders
# Food     : What the customer buys

# To get you started, here are the classes and methods you'll be defining:
# class Lunch:
#     def __init__(self)                                      # Make/embed Customer and Employee
#     def order(self, foodName)                               # Start a Customer order simulation
#     def result(self)                                        # Ask the Customer what Food it has
# class Customer:
#     def __init__(self)                                      # Initialize my food to None
#     def placeOrder(self, foodName, employee)                # Place order with an Employee 
#     def printFood(self)                                     # Print the name of my food
# class Employee:
#     def takeOrder(self, foodName)                           # Return a Food, with requested name
# class Food:
#     def __init__(self, name)                                # Store food name

# The order simulation should work as follows:

# a. The Lunch class's constructor should make and embed an instance of
# Customer and an instance of Employee, and it should export a method called
# order. When called, this order method should ask the Customer to place an
# order by calling its placeOrder method. The Customer's placeOrder method
# should in turn ask the Employee object for a new Food object by calling
# Employee's takeOrder method.

# b. Food objects should store a food name string (e.g., "burritos"), passed
# down from Lunch.order, to Customer.placeOrder, to Employee.takeOrder, and 
# finally to Food's constructor. The top-level Lunch class should also export
# a method called result, which asks the customer to print the name of the food
# it received from the Employee via the order (this can be used to test your
# simulation).

# Note that Lunch needs to pass either the Employee or itself to the Customer
# to allow the Customer to call Employee methods.

# Experiment with your classes interactively by importing the Lunch class, 
# calling its order method to run an interaction, and then calling its result
# method to verify that the Customer got what he or she ordered. If you prefer,
# you can also simply code test cases as self-test code in the file where your
# classes are defined, using the module __name__ trick of Chapter 25. 

# In this simulation, the Customer is the active agent; how would your classes
# change if Employee were the object that initiated customer/employee interaction
# instead?

class Lunch:
    
    def __init__(self):                                       # Make/embed Customer and Employee
        self.customer = Customer()
        self.employee = Employee()

    def order(self, foodName):                                # Start a Customer order simulation
        self.customer.placeOrder(foodName, self.employee)

    def result(self):                                         # Ask the Customer what Food it has
        self.customer.printFood()


class Customer:
    
    def __init__(self):                                       # Initialize my food to None
        self.food = None 
    
    def placeOrder(self, foodName, employee):                 # Place order with an Employee
        self.food = employee.takeOrder(foodName)
    
    def printFood(self):                                      # Print the name of my food
        print(self.food.name)
        
    
class Employee:
    
    def takeOrder(self, foodName):                            # Return a Food, with requested name
        return Food(foodName)
    

class Food:
    
    def __init__(self, name):
        self.name = name
        
        
if __name__ == "__main__":
    
    lunch = Lunch()
    lunch.order("pancakes")
    lunch.result()                                            # pancakes
    
