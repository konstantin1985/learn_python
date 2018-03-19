
# MAIN SOURCE:
# Kasampalis "Mastering Python Patterns" Chapter 9

# USEFUL LINKS:
#
# 1) Old-school way to have an abstract class
#    https://stackoverflow.com/questions/13646245/is-it-possible-to-make-abstract-classes-in-python
#
# 2) How to invoke methods of a super class
#    https://stackoverflow.com/questions/31232098/how-to-call-super-method/31232226


# GENERAL INFORMATION:


print("-" * 20 + "# 1 Implementation with an abstract base class" + "-" * 20)

from abc import ABCMeta 
import abc

class SensitiveInfo:

    __metaclass__ = ABCMeta 

    def __init__(self):
        self.users = ['nick', 'tom', 'ben', 'mike']
    
    @abc.abstractmethod
    def read(self):
        print('There are {} users: {}'.format(len(self.users), ' '.join(self.users)))
    
    def add(self, user):
        self.users.append(user)
        print('Added user {}'.format(user))
        

class Info(SensitiveInfo):
    
    def __init__(self):
        self.secret = 'mypass'
        SensitiveInfo.__init__(self)                   # otherwise 'Info' object doesn't have 'users'
        
    def read(self):
        SensitiveInfo.read(self)                       # or super(Info, self).read()
        
    def add(self, user):
        sec = raw_input('What is the secret? ')
        
        if sec == self.secret:
            SensitiveInfo.add(self, user)              # or super(Info, self).add(user)
        else: 
            print("That's wrong!")


def main():
    
    # si = SensitiveInfo()                             # it's abstract, can't create it
    
    info = Info()
        
    while True:
        print('1. read list |==| 2. add user |==| 3. quit')
        key = raw_input('Choose option: ')
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
    
