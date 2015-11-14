#http://jfine-python-classes.readthedocs.org/en/latest/property_from_class.html#about-properties
#http://stackoverflow.com/questions/15458613/python-why-is-read-only-property-writable


print "First----------------------------------------------------"

class First(object):

    def __init__(self):
        self.width = 10;
        self.length = 5;

    @property
    def attrib(self):
        return self.width * self.length
    
f = First()
#f.attrib = 5


print f.attrib 