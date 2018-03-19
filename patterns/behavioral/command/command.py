

# MAIN SOURCE:
# Kasampalis "Mastering Python Patterns" Chapter 11

# USEFUL LINKS:
#
# 1) Reading a text file
#    https://www.afterhoursprogramming.com/tutorial/python/reading-files/
#
# 2) P.3 input() = P.2 raw_input() 
#    https://stackoverflow.com/questions/4915361/whats-the-difference-between-raw-input-and-input-in-python3-x
#
# 3) Linux relative paths "Dot and Dot Dot – . and .."
#    http://teaching.idallen.com/cst8207/12f/notes/160_pathnames.html#dot-and-dot-dot-.-and-..



# GENERAL INFORMATION:

# In object-oriented programming, the command pattern is a behavioral
# design pattern in which an object is used to encapsulate all information
# needed to perform an action or trigger an event at a later time.
# This information includes the method name, the object that owns the method
# and values for the method parameters.

# What this simply means is that we create a class that contains all the
# logic and the methods required to implement the operation.

# - We don't have to execute a command directly. It can be executed on will.
# - The object that invokes the command is decoupled from the object that
#   knows how to perform it. The invoker does not need to know any 
#   implementation details about the command.
# - If it makes sense, multiple commands can be grouped to allow the invoker
#   to execute them in order. This is useful, for instance, when implementing
#   a multilevel undo command.

# A real-life example:
# When we go to the restaurant for dinner, we give the order to the waiter.
# The check (usually paper) they use to write the order on is an example of
# Command. After writing the order, the waiter places it in the check queue
# that is executed by the cook. Each check is independent and can be used
# to execute many and different commands, for example, one command for each
# item that will be cooked.


print("-" * 20 + "# 1 Use Cases" + "-" * 20)

# - GUI buttons and menu items: The PyQt uses the Command pattern to
#   implement actions on buttons and menu items.

# - Other operations: Apart from undo, Command can be used to implement
#   any operation. A few examples are cut, copy, paste, redo, and capitalize
#   text.

# - Transactional behavior and logging: Transactional behavior and logging
#   are important to keep a persistent log of changes. They are used by
#   operating systems to recover from system crashes, relational databases
#   to implement transactions, filesystems to implement snapshots, and
#   installers (wizards) to revert cancelled installations.

# - Macros: By macros, in this case, we mean a sequence of actions that can be
#   recorded and executed on demand at any point in time. Popular editors such
#   as Emacs and Vim support macros.

print("-" * 20 + "# 2 Implementation" + "-" * 20)

# We will use the Command pattern to implement the most basic file utilities:
# - Creating a file and optionally writing a string in it
# - Reading the contents of a file
# - Renaming a file
# - Deleting a file

# We will not implement these utilities from scratch, since Python already
# offers good implementations of them in the os module. What we want is to
# add an extra abstraction level on top of them so that they can be treated
# as commands. By doing this, we get all the advantages offered by commands.

# Renaming a file and creating a file support undo. Deleting a file and
# reading the contents of a file do no support undo. Undo can actually be
# implemented on delete file operations. One technique is to use a special
# trash/wastebasket directory that stores all the deleted files, so that
# they can be restored when the user requests it. This is the default
# behavior used on all modern desktop environments and is left as an exercise.

# Each command has two parts: the initialization part and the execution part.
# The initialization part is taken care of by the __init__() method and
# contains all the information required by the command to be able to do
# something useful (the path of a file, the contents that will be written to
# the file, and so forth). The execution part is taken care by the execute()
# method. We call the execute() method when we want to actually run a command.
# This is not necessarily right after initializing it.

import os

verbose = True

class RenameFile:
    
    def __init__(self, path_src, path_dst):
        self.src, self.dst = path_src, path_dst
        
    def execute(self):
        if verbose:
            print("[renaming '{}' to '{}']".format(self.src, self.dst))
        os.rename(self.src, self.dst)
    
    def undo(self):
        if verbose:
            print("[renaming '{}' back to '{}']".format(self.dst, self.src))
        os.rename(self.dst, self.src)
        
# Deleting a file is a single function, instead of a class. I did that to
# show you that it is not mandatory to create a new class for every command
# that you want to add.

def delete_file(path):
    if verbose:
        print("deleting file '{}'".format(path))
    os.remove(path)
    

class CreateFile:
    
    def __init__(self, path, txt='hello world\n'):
        self.path, self.txt = path, txt
        
    def execute(self):
        if verbose:
            print("[creating file '{}']".format(self.path))
        with open(self.path, mode='w') as out_file:
            out_file.write(self.txt)
            
    def undo(self):
        delete_file(self.path)

    
class ReadFile:
    
    def __init__(self, path):
        self.path = path
        
    def execute(self):
        if verbose:
            print("[Reading file '{}']".format(self.path))
        with open(self.path, mode='r') as in_file:
            print(in_file.read())


def main():
    
    # "/xxx" - starting from ROOT
    # "./xxx" - staring from the current path
    # "../xxx" - staring from the parent path
    # see "ls -a" in any directory, . and .. are special 
    
    # __file__ is the pathname of the file from which the module
    # was loaded, if it was loaded from a file.
    dirname = os.path.dirname(__file__)  # dirname - absolute path      
    print(dirname)
    filename = os.path.join(dirname, '../files')
    print(filename)
    
    orig_name, new_name = 'file1.txt', 'file2.txt'
    
    # All the commands that we want to execute at a later point.
    commands = []
    for cmd in CreateFile(orig_name), ReadFile(orig_name), RenameFile(orig_name, new_name):
        commands.append(cmd)
        
    for c in commands:
        c.execute()
    
    # Ask a user to undo all the commands
    answer = raw_input('reverse the executed commands? [y/n]:')

    if answer not in "yY":
        print("the result is {}".format(new_name))
        exit()
    
    # Catch (and ignore) the AttributeError exception generated
    # when the undo() method is missing.
    for c in reversed(commands):
        try:
            c.undo()
        except AttributeError as e:
            pass
    
if __name__ == "__main__":
    main()







