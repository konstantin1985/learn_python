
# MAIN SOURCE:
# https://sourcemaking.com/design_patterns/adapter/python/1

# USEFUL LINKS:
# http://en.proft.me/2016/12/31/adapter-design-pattern-java-and-python/

# 2) Python 3 Patterns, Recipes and Idioms
#    http://python-3-patterns-idioms-test.readthedocs.io/en/latest/ChangeInterface.html
#
# 3) Example of Adapter pattern
#    https://gist.github.com/pazdera/1145859
#
# 4) Adapter pattern in wiki (class vs object adapter)
#    https://en.wikipedia.org/wiki/Adapter_pattern


# GENERAL INFORMATION:

# More traditional way to implement the Adapter Pattern.

# Convert the interface of a class into another interface clients
# expect. Adapter lets classes work together that couldn't otherwise
# because of incompatible interfaces.

import abc

# What the we want
class Target():
    """
    Define the domain-specific interface that Client uses.
    """

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def request(self):
        pass

# Adapt what we have (adaptee), to the interface we want (Target)
class Adapter(Target):
    """
    Adapt the interface of Adaptee to the Target interface.
    """

    def __init__(self, adaptee):
        self.__adaptee = adaptee

    def request(self):
        self.__adaptee.specific_request()

# What we have
class Adaptee:
    """
    Define an existing interface that needs adapting.
    """

    def specific_request(self):
        print("specific_request is invoked")

# Client
def main():
    
    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    adapter.request()                                      # "specific_request is invoked"


if __name__ == "__main__":
    main()