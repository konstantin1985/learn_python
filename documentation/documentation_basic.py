


print('-' * 10 + "A.1. dir()" + '-' * 10)

# As we've also seen, the built-in dir function is an easy way to grab a list of all the
# attributes available inside an object
# Also work to check what's in the import

# Notice that you can list built-in type attributes by passing a type name to dir instead
# of a literal:
print(dir(str) == dir(''))   # True
print(dir(str) == dir('a'))  # True
print(dir(list) == dir([]))  # True

# This works because names like str and list that were once type converter functions
# are actually names of types in Python today; calling one of these invokes its constructor
# to generate an instance of that type.

print('-' * 10 + "A.2. Docstrings __doc__" + '-' * 10)

# The whole point of this documentation protocol is that your comments are retained
# for inspection in __doc__ attributes after the file is imported. Thus, to display the doc-
# strings associated with the module and its objects, we simply import the file and print
# their __doc__ attributes,

def f():
    """
    some function documentation
    """
    pass

print(f.__doc__)  # some function documentation

# We can also attach docstrings to methods in a class
# module.class.method.__doc__

help(f)  # better display of information than just __doc__

print('-' * 10 + "A.3. Common mistakes" + '-' * 10)

# It's not uncommon for
# beginners to say something like mylist = mylist.append(X) to try to get the result
# of an append, but what this actually does is assign mylist to None, not to the modified list 

# It’s fairly common to see code like
# for k in D.keys().sort():. This almost works—the keys method builds a keys
# list, and the sort method orders it—but because the sort method returns None, the
# loop fails because it is ultimately a loop over None (a nonsequence).
