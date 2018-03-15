
# MAIN SOURCE:
# Kasampalis "Mastering Python Patterns" Chapter 9

# USEFUL LINKS:
#
# 1) How to store a password 
#    https://stackoverflow.com/questions/8195099/java-how-to-store-password-used-in-application
#    https://stackoverflow.com/questions/442862/how-can-i-protect-mysql-username-and-password-from-decompiling/442872#442872


# GENERAL INFORMATION:

# In some applications, we want to execute one or more important action
# before accessing an object. An example is accessing sensitive information.
# Before allowing any user to access sensitive information, we want to make
# sure that the user has sufficient privileges. 

# The important action is not necessarily related to security issues. Lazy
# initialization is another case; we want to delay the creation of a 
# computationally expensive object until the first time the user actually
# needs to use it.

# Such actions are typically performed using the Proxy design pattern. The
# pattern gets its name from the proxy (also known as surrogate) object used
# to perform an important action before accessing the actual object. There
# are four different well-known proxy types:
# - A remote proxy, which acts as the local representation of an object that
#   really exists in a different address space (for example, a network server).
# - A virtual proxy, which uses lazy initialization to defer the creation of a
#   computationally expensive object until the moment it is actually needed.
# - A protection/protective proxy, which controls access to a sensitive object.
# - A smart (reference) proxy, which performs extra actions when an object is
#   accessed. Examples of such actions are reference counting and thread-safety
#   checks.




print("-" * 20 + "# 1 Use Cases" + "-" * 20)

# Use cases:

# - It is used when creating a distributed system using either a private network
#   or the cloud. In a distributed system, some objects exist in the local memory
#   and some objects exist in the memory of remote computers. If we don't
#   want the client code to be aware of such differences, we can create a remote
#   proxy that hides/encapsulates them, making the distributed nature of the
#   application transparent.

# - It is used if our application is suffering from performance issues due to the
#   early creation of expensive objects. Introducing lazy initialization using
#   a virtual proxy to create the objects only at the moment they are actually
#   required can give us significant performance improvements.

# - It is used to check if a user has sufficient privileges to access a piece of
#   information. If our application handles sensitive information (for example,
#   medical data), we want to make sure that the user trying to access/modify
#   it is allowed to do so. A protection/protective proxy can handle all
#   security-related actions.

# - It is used when our application (or library, toolkit, framework, and so forth)
#   uses multiple threads and we want to move the burden of thread-safety from
#   the client code to the application. In this case, we can create a smart proxy
#   to hide the thread-safety complexities from the client.

# - An Object-Relational Mapping (ORM) API is also an example of how to use
#   a remote proxy. Many popular web frameworks, including Django, use an
#   ORM to provide OOP-like access to a relational database. An ORM acts as a
#   proxy to a relational database that can be actually located anywhere, either
#   at a local or remote server.

print("-" * 20 + "# 2 Implementation" + "-" * 20)

# We will implement a simple protection proxy to view and add users. The service
# provides two options:
# - Viewing the list of users: This operation does not require special privileges
# - Adding a new user: This operation requires the client to provide a special
#   secret message

# Contains the information we want to protect.
# users - list of existing users.
class SensitiveInfo:

    def __init__(self):
        self.users = ['nick', 'tom', 'ben', 'mike']
        
    def read(self):
        print('There are {} users: {}'.format(len(self.users), ' '.join(self.users)))
    
    def add(self, user):
        self.users.append(user)
        print('Added user {}'.format(user))
        
# The Info class is a protection proxy of SensitiveInfo. The secret variable is
# the message required to be known/provided by the client code to add a new user.
# Note that this is just an example. In reality, you should never:
# - Store passwords in the source code
# - Store passwords in a clear-text form
# - Use a weak (for example, MD5) or custom form of encryption

# The read() method is a wrapper to SensitiveInfo.read(). The add() method
# ensures that a new user can be added only if the client code knows the secret
# message.

class Info:
    
    def __init__(self):
        self.protected = SensitiveInfo()
        self.secret = 'mypass'
        
    def read(self):
        self.protected.read()
        
    def add(self, user):
        sec = raw_input('What is the secret? ')
        
        if sec == self.secret:
            self.protected.add(user)
        else: 
            print("That's wrong!")


def main():
    
    info = Info()
        
    while True:
        print('1. read list |==| 2. add user |==| 3. quit')
        key = input('Choose option: ')
        if key == 1:
            info.read()
        elif key == 2:
            name = raw_input("Choose username: ")
            info.add(name)
        elif key == 3:
            exit()
        else:
            print("Unknown option '{}'".format(key))


if __name__ == "__main__":
    main()
    

        
        
        
        


