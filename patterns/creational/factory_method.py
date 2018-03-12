

# MAIN SOURCE:
# Kasampalis "Mastering Python Patterns" Chapter 1


# USEFUL LINKS:
# https://docs.python.org/2/library/xml.etree.elementtree.html
# https://stackoverflow.com/questions/9112121/elementtree-findall-returning-empty-list
# https://www.w3.org/TR/xpath/
# https://stackoverflow.com/questions/2835559/parsing-values-from-a-json-file

# GENERAL INFORMATION:

# The aim of a creational design pattern is to provide better
# alternatives for situations where a direct object creation
# (which in Python happens by the __init__() function, is not
# convenient.

# In the Factory design pattern, a client asks for an object
# without knowing where the object is coming from (that is, 
# which class is used to generate it). The idea behind a fac-
# tory is to simplify an object creation. It is easier to 
# track which objects are created if this is done through a
# central function, in contrast to letting a client create
# objects using a direct class instantiation. A factory reduces
# the complexity of maintaining an application by decoupling
# the code that creates an object from the code that uses it.

# Factories typically come in two forms: the Factory Method,
# which is a method (or in Pythonic terms, a function) that
# returns a different object per input parameter; the Abstract
# Factory, which is a group of Factory Methods used to create
# a family of related products.

# In the Factory Method, we execute a single function, passing
# a parameter that provides information about what we want. We
# are not required to know any details about how the object is
# implemented and where it is coming from.

print("-" * 20 + "# 1 Use Cases" + "-" * 20)

# If you realize that you cannot track the objects created by
# your application because the code that creates them is in
# many different places instead of a single function/method,
# you should consider using the Factory Method pattern. The
# Factory Method centralizes an object creation and tracking
# your objects becomes much easier. 

# Note that it is absolutely fine to create more than one 
# Factory Method, and this is how it is typically done in
# practice. Each Factory Method logically groups the creation
# of objects that have similarities. For example, one Factory
# Method might be responsible for connecting you to different
# databases (MySQL, SQLite), another Factory Method might be
# responsible for creating the geometrical object that you
# request (circle, triangle), and so on.

# The Factory Method is also useful when you want to decouple
# an object creation from an object usage. We are not coupled/
# bound to a specific class when creating an object, we just
# provide partial information about what we want by calling a
# function. This means that introducing changes to the function
# is easy without requiring any changes to the code that uses it.


print("-" * 20 + "# 2 Implementation" + "-" * 20)

# Data comes in many forms. There are two main file categories
# for storing/retrieving data: human-readable files and binary
# files. Examples of human-readable files are XML, Atom, YAML,
# and JSON. Examples of binary files are the .sq3 file format
# used by SQLite and the .mp3 file format used to listen to music.

# In this example, we will focus on two popular human-readable
# formats: XML and JSON. Although human-readable files are
# generally slower to parse than binary files, they make data 
# exchange, inspection, and modification much easier. For this
# reason, it is advised to prefer working with human-readable
# files, unless there are other restrictions that do not allow
# it (mainly unacceptable performance and proprietary binary
# formats).

# In this problem, we have some input data stored in an XML
# and a JSON file, and we want to parse them and retrieve 
# some information. At the same time, we want to centralize
# the client's connection to those (and all future) external
# services. We will use the Factory Method to solve this problem.
# The example focuses only on XML and JSON, but adding support
# for more services should be straightforward.

from io import open # so open(... encoding='utf-8') works in Python 2.x

import xml.etree.ElementTree as etree
import json

# IMPORT: very important to have proper commas in JSON files.
# For example, not to put a comma after the last item in the list.
# 
#      "batter": [
#        { "id": "1001", "type": "Regular" },
#        { "id": "1002", "type": "Chocolate" },
#        { "id": "1003", "type": "Blueberry" }
#      ]

class JSONConnector:
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r') as f:
            self.data = json.load(f)
            
    @property
    def parsed_data(self):
        return self.data
    
class XMLConnector:
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)
    
    @property
    def parsed_data(self):
        return self.tree
    
# Factory Method
# It returns an instance of JSONConnector or XMLConnector
# depending on the extension of the input file path.
def connection_factory(filepath):
    if filepath.endswith('json'):
        connector = JSONConnector
    elif filepath.endswith('xml'):
        connector = XMLConnector
    else:
        raise ValueError("Cannot connect to {}".format(filepath))
    return connector(filepath)
    
# A wrapper of connection_factory(). It adds exception
# handling as.
def connect_to(filepath):
    factory = None
    try:
        factory = connection_factory(filepath)
    except ValueError as ve:
        print(ve)
    return factory

def main():
    
    # 1. Check error handling
    
    sqlite_factory = connect_to('files/factory_method/person.sq3') 
    
        # OUTPUT:
        # Cannot connect to files/factory_method/person.sq3
    
    print('-----')
    
    # 2. Work with XML
    
    xml_factory = connect_to('files/factory_method/person.xml')
    xml_data = xml_factory.parsed_data    
    
    # Here findall uses the so-called XPath (XML Path Language)
    # https://docs.python.org/2/library/xml.etree.elementtree.html
    liars = xml_data.findall(".//{}[{}='{}']".format('person', 'lastName', 'Liar'))
    print('found: {} persons'.format(len(liars)))
    
    
    for liar in liars:
        print('first name: {}'.format(liar.find('firstName').text))
        print('last name: {}'.format(liar.find('lastName').text))
        for p in liar.find("phoneNumbers"):
            print(p.text)
   
        # OUTPUT:
        # found: 2 persons
        # first name: Jimy
        # last name: Liar
        # 212 555-1234
        # first name: Patty
        # last name: Liar
        # 212 555-1234
        # 001 452-8819

    print('-----')

    # 3. Work with JSON
    
    json_factory = connect_to('files/factory_method/donut.json')
    json_data = json_factory.parsed_data
    
    print("found: {} donuts".format(len(json_data)))
    
    for donut in json_data:
        print('name: {}'.format(donut['name']))
        print('price: ${}'.format(donut['ppu']))
        for t in donut['topping']:
            print('topping: {} {}'.format(t['id'], t['type']))
    
            # OUTPUT:
            # found: 3 donuts
            # name: Cake
            # price: $0.55
            # topping: 5001 None
            # topping: 5002 Glazed
            # topping: 5005 Sugar
            # topping: 5007 Powdered Sugar
            # topping: 5006 Chocolate with Sprinkles
            # topping: 5003 Chocolate
            # topping: 5004 Maple
            # name: Raised
            # price: $0.55
            # topping: 5001 None
            # topping: 5002 Glazed
            # topping: 5005 Sugar
            # topping: 5003 Chocolate
            # topping: 5004 Maple
            # name: Old Fashioned
            # price: $0.55
            # topping: 5001 None
            # topping: 5002 Glazed
            # topping: 5003 Chocolate
            # topping: 5004 Maple


# Notice that although JSONConnector and XMLConnector have the same interfaces,
# what is returned by parsed_data() is not handled in a uniform way. Different
# python code must be used to work with each connector. Although it would be nice
# to be able to use the same code for all connectors, this is at most times not
# realistic unless we use some kind of common mapping for the data which is very
# often provided by external data providers.

# QUESTION: As it is now, the code does not forbid a direct instantiation of a
# connector. Is it possible to do this? Try doing it.
# ANSWER: Define JSONConnector and XMLConnector classes inside connection_factory
# function.


if __name__ == "__main__":
    main()
