

# MAIN SOURCE:
# Kasampalis "Mastering Python Patterns" Chapter 10

# USEFUL LINKS:
#
# 1) UML: aggregation, association, composition
#    https://stackoverflow.com/questions/885937/what-is-the-difference-between-association-aggregation-and-composition

# GENERAL INFORMATION:

# When developing an application, most of the time we know which 
# method should satisfy a particular request in advance. However,
# this is not always the case.

# In broadcast computer networks, all requests are sent to all
# nodes (broadcast domains are excluded for simplicity), but only
# the nodes that are interested in a sent request process it. 

# If a node is not interested or does not know how to handle a
# request, it can perform the following actions:
# - Ignore the request and do nothing
# - Forward the request to the next node

# The way in which the node reacts to a request is an implementation
# detail. However, we can use the analogy of a broadcast computer
# network to understand what the chain of responsibility pattern is
# all about. The Chain of Responsibility pattern is used when we want
# to give a chance to multiple objects to satisfy a single request, or
# when we don't know which object (from a chain of objects) should
# process a specific request in advance. The principle is the same as
# the following:
# 1. There is a chain (linked list, tree, or any other convenient data
# structure) of objects.
# 2. We start by sending a request to the first object in the chain.
# 3. The object decides whether it should satisfy the request or not.
# 4. The object forwards the request to the next object.
# 5. This procedure is repeated until we reach the end of the chain.

# At the application level, instead of talking about cables and network
# nodes, we can focus on objects and the flow of a request. 

# Note that the client code only knows about the first processing element,
# instead of having references to all of them, and each processing element
# only knows about its immediate next neighbor (called the successor), not
# about every other processing element. This is usually a one-way
# relationship, which in programming terms means a singly linked list in
# contrast to a doubly linked list; a singly linked list does not allow
# navigation in both ways, while a doubly linked list allows that. This
# chain organization is used for a good reason. It achieves decoupling
# between the sender (client) and the receivers (processing elements).

print("-" * 20 + "# 1 Use Cases" + "-" * 20)

# Another case where Chain of Responsibility is useful is when we know
# that more than one object might need to process a single request.
# This is what happens in an event-based programming. A single event
# such as a left mouse click can be caught by more than one listener.

# It is important to note that the Chain of Responsibility pattern is
# not very useful if all the requests can be taken care of by a single
# processing element, unless we really don't know which element that is.
# The value of this pattern is the decoupling that it offers. Instead
# of having a many-to-many relationship between a client and all
# processing elements (and the same is true regarding the relationship
# between a processing element and all other processing elements), a
# client only needs to know how to communicate with the start (head)
# of the chain.

# UML

# Association: is a relationship where all objects have their own lifecycle
#              and there is no owner.
# Aggregation: is a specialized form of Association where all objects have 
#              their own lifecycle, but there is ownership and child objects
#              can not belong to another parent object.
# Composition: is again specialized form of Aggregation. Child object does
#              not have its lifecycle and if parent object is deleted, all
#              child objects will also be deleted.

# In the Chain Of Responsibility pattern, the sender has direct access
# to the first node of a chain. If the request cannot be satisfied by
# the first node, it forwards to the next node. This continues until
# either the request is satisfied by a node or the whole chain is
# traversed. This design is used to achieve loose coupling between the
# sender and the receiver(s).

print("-" * 20 + "# 2 Implementation" + "-" * 20)

class Event:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name
    
# Each widget can have a reference to a parent object, which by convention,
# we assume is a Widget instance. Note, however, that according to the rules
# of inheritance, an instance of any of the subclasses of Widget (for example,
# an instance of MsgText) is also an instance of Widget. The default value
# of parent is None

class Widget:

    def __init__(self, parent = None):
        self.parent = parent
        
    def handle(self, event):
        handler = 'handle_{}'.format(event)                     # Create the name of a handler method from the event
        
        if hasattr(self, handler):
            method = getattr(self, handler)
            method(event)
        
        elif self.parent:
            self.parent.handle(event)
        
        elif hasattr(self, 'handle_default'):
            self.handle_default(event)


# At this point, you might have realized why the Widget and Event classes
# are only associated (no aggregation or composition relationships) in the
# UML class diagram. The association is used to show that the Widget class
# "knows" about the Event class but does not have any strict references to
# it, since an event needs to be passed only as a parameter to handle().

# MainWIndow, MsgText, and SendDialog are all widgets with different behaviors.
# Not all these three widgets are expected to be able to handle the same events,
# and even if they can handle the same event, they might behave differently.

class MainWindow(Widget):
    
    def handle_close(self, event):
        print('MainWindow: {}'.format(event))
    
    def handle_default(self, event):
        print('MainWindow Default: {}'.format(event))


class SendDialog(Widget):
    
    def handle_paint(self, event):
        print('SendDialogue: {}'.format(event))


class MsgText(Widget):
    
    def handle_down(self, event):
        print('MsgText: {}'.format(event))
        

def main():
    
    # Create a chain
    mw = MainWindow()
    sd = SendDialog(mw)
    msg = MsgText(sd)

    for e in ('down', 'paint', 'unhandled', 'close'):
        evt = Event(e)
        print('\nSending event -{}- to MainWindow'.format(evt))
        mw.handle(evt)
        print('Sending event -{}- to SendDialog'.format(evt))
        sd.handle(evt)
        print('Sending event -{}- to MsgText'.format(evt))
        msg.handle(evt)
        
if __name__ == "__main__":
    main()

# Sending event -down- to MainWindow
# MainWindow Default: down
# Sending event -down- to SendDialog
# MainWindow Default: down
# Sending event -down- to MsgText
# MsgText: down
# 
# Sending event -paint- to MainWindow
# MainWindow Default: paint
# Sending event -paint- to SendDialog
# SendDialogue: paint
# Sending event -paint- to MsgText
# SendDialogue: paint
# 
# Sending event -unhandled- to MainWindow
# MainWindow Default: unhandled
# Sending event -unhandled- to SendDialog
# MainWindow Default: unhandled
# Sending event -unhandled- to MsgText
# MainWindow Default: unhandled
# 
# Sending event -close- to MainWindow
# MainWindow: close
# Sending event -close- to SendDialog
# MainWindow: close
# Sending event -close- to MsgText
# MainWindow: close






