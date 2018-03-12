

# MAIN SOURCE:
# Lutz, "Learning Python" chapter 36


# USEFUL LINKS:
# 1) LEGB rule explanation Local -> Enclosed -> Global -> Built-in
#    http://sebastianraschka.com/Articles/2014_python_scope_and_namespaces.html 
#    
#    This is also why we have to be careful if we import modules via
#    "from a_module import *", since it loads the variable names into
#    the global namespace and could potentially overwrite already 
#    existing variable names.

# GENERAL INFORMATION:


# try/except. Write a function called oops that explicitly raises an
# IndexError exception when called. Then write another function that
# calls oops inside a try/except statement to catch the error. What
# happens if you change oops to raise a KeyError instead of an IndexError?
# Where do the names KeyError and IndexError come from? (Hint: recall that
# all unqualified names generally come from one of four scopes.)

def oops1():
    raise IndexError

def oops2():
    raise KeyError

def fcn(pfcn):
    try:
        pfcn()
    except IndexError:
        print('something happened')

if __name__ == "__main__":
    fcn(oops1)                                                
    # something happened
    fcn(oops2)
    # Traceback (most recent call last):
    # raise KeyError
    # KeyError


