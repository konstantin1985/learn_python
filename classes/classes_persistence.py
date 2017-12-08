

# pickle
# Serializes arbitrary Python objects to and from a string of bytes
# dbm (named anydbm in Python 2.X)
# Implements an access-by-key filesystem for storing strings
# shelve
# Uses the other two modules to store Python objects on a file by key

import shelve

print("-" * 20 + "#1 Storing Objects on a Shelve Database" + "-" * 20)

class Person:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return '[Person: name=%s]' % (self.name)
        
class Manager(Person):
    def __init__(self, name, salary):
        Person.__init__(self, name)
        self.salary = salary
    def __repr__(self):
        return '[Manager: name=%s, salary=%d]' % (self.name, self.salary)
        
bob = Person("Bob")
sue = Person("Sue")
tom = Manager("Tom", 1000)

# The only rule is that the keys must be strings and should
# be unique, since we can store just one object per key.

db = shelve.open('persondb')
for obj in (bob, sue, tom):
    db[obj.name] = obj                         # bob.name = "Bob" etc.
db.close()


print("-" * 20 + "#2 Exploring Shelves Interactively" + "-" * 20)

db = shelve.open('persondb')
print(len(db))                                 # 3
print(list(db.keys()))                         # ['Tom', 'Bob', 'Sue']
bob = db['Bob']
print(bob.name)                                # Bob

# Notice that we don't have to import our Person or Manager classes
# here in order to load or use our stored objects.
# This works because when Python pickles a class instance, it records
# its self instance attributes, along with the name of the class it 
# was created from and the module where the class lives.

# Python reimports the class from its module internally, creates an instance with its
# stored attributes, and sets the instance's __class__ link to point to its original class.
# This way, loaded instances automatically obtain all their original methods, 
# even if we have not imported the instance's class into our scope.

for key in sorted(db):
    print(key, '=>', db[key])

# ('Bob', '=>', [Person: name=Bob])
# ('Sue', '=>', [Person: name=Sue])
# ('Tom', '=>', [Manager: name=Tom, salary=1000])
db.close()

print("-" * 20 + "#3 Updating Objects on a Shelve" + "-" * 20)

db = shelve.open('persondb')
sue = db['Sue']
sue.name = "Sue 2"
db['Sue'] = sue
db.close()

db = shelve.open('persondb')
sue = db['Sue']
print(sue.name)                                # Sue 2



print("-" * 20 + "#4 pickle" + "-" * 20)

# Need to learn 