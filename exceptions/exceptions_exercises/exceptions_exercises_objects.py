

# MAIN SOURSE:
# Lutz, "Learning Python" chapter 36

# USEFUL LINKS:
# 

# GENERAL INFORMATION:


# Exception objects and lists. Change the oops function you just wrote to
# raise an exception you define yourself, called MyError. Identify your
# exception with a class (unless you're using Python 2.5 or earlier, you
# must). Then, extend the try statement in the catcher function to catch
# this exception and its instance in addition to IndexError, and print the
# instance you catch.

class MyError(Exception):
    
    def __str__(self):
        return "It is MyError"

def oops():
    raise MyError

def fcn():
    try:
        oops()
    except MyError as e:
        print(e)

if __name__ == "__main__":
    fcn()    

# OUTPUT:
# "It is MyError"