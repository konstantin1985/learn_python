


# MAIN SOURCE:
# Kasampalis "Mastering Python Patterns" Chapter 6

# USEFUL LINKS:
#
#
#

# GENERAL INFORMATION:

# The Facade design pattern helps us to hide the internal complexity of
# our systems and expose only what is necessary to the client through a
# simplified interface. In essence, Facade is an abstraction layer 
# implemented over an existing complex system.


print("-" * 20 + "# 1 Use Cases" + "-" * 20)

# The most usual reason to use the Facade pattern is for providing a
# single, simple entry point to a complex system. By introducing Facade,
# the client code can use a system by simply calling a single 
# method/function. At the same time, the internal system does not lose
# any functionality. It just encapsulates it.

# Not exposing the internal functionality of a system to the client code
# gives us an extra benefit; we can introduce changes to the system, but
# the client code remains unaware and unaffected by the changes. No
# modifications are required to the client code.

# Facade is also useful if you have more than one layer in your system.
# You can introduce one Facade entry point per layer, and let all layers
# communicate with each other through their Facades. That promotes loose
# coupling and keeps the layers as independent as possible.

print("-" * 20 + "# 2 Implementation" + "-" * 20)

# MICROKERNEL:
# A multi-server operating system has a minimal kernel, called the
# microkernel, that runs in privileged mode. All the other services of
# the system are following a server architecture (driver server, process
# server, file server, and so forth). Each server belongs to a different
# memory address space and runs on top of the microkernel in user mode. 
# The pros of this approach are that the operating system can become more
# fault-tolerant, reliable, and secure. For example, since all drivers are
# running in user mode on a driver server, a bug in a driver cannot crash
# the whole system, and neither can it affect the other servers. The cons
# of this approach are the performance overhead and the complexity of
# system programming, because the communication between a server and the
# microkernel, as well as between the independent servers, happens using
# message passing. Message passing is more complex than the shared memory
# model used in monolithic kernels like Linux.

from enum import Enum
from abc import ABCMeta, abstractmethod

State = Enum('State', 'new running sleeping restart zombie')

class Server(object):
    
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        pass
    
    def __str__(self):
        return self.name                                            # self.name will be in children
    
    @abstractmethod
    def boot(self):
        pass
    
    @abstractmethod
    def kill(self):
        pass


# A modular operating system can have a great number of servers. 
# Apart from the methods required to be implemented by the Server
# interface, each server can have its own specific methods.


class FileServer(Server):
    
    def __init__(self):
        """actions required for initilizing the file server"""
        self.name = 'FileServer'
        self.state = State.new
        
    def boot(self):
        print('booting the {}'.format(self))                        # self.__str__ is invoked 
        """actions required for booting the file server"""
        self.state = State.running

    def kill(self, restart = True):
        print('Killing {}'.format(self))
        """actions required for killing the file server"""
        self.state = State.restart if restart else State.zombie

    def create_file(self, user, name, permissions):
        """check validity of permissions, user rights, etc"""
        print("Trying to create the file '{}' for user '{}' with permissions {}".
              format(name, user, permissions))


class ProcessServer(Server):
    
    def __init__(self):
        """actions required for initializing the process server"""
        self.name = 'ProcessServer'
        self.state = State.new
    
    def boot(self):
        print('booting the {}'.format(self)) 
        """actions required for booting the process server"""
        self.state = State.running
    
    def kill(self, restart = True):
        print('Killing {}'.format(self))
        """actions required for killing the process server"""
        self.state = State.restart if restart else State.zombie

    def create_process(self, user, name):
        """check user rights, generate PID, etc."""
        print("Trying to create the process '{}' for user '{}'". 
              format(name, user))
        
# The OperatingSystem class is a Facade. In __init__(), all the necessary server
# instances are created. The start() method, used by the client code, is the entry
# point to the system. More wrapper methods can be added, if necessary, as access
# point to the services of the servers such as the wrappers create_file() and 
# create_process(). From the client's point of view, all those services are provided
# by the OperatingSystem class. The client should not be confused with unnecessary
# details such as the existence of servers and the responsibility of each server.

class OperatingSystem:
    """The Facade"""
    def __init__(self):
        self.fs = FileServer()
        self.ps = ProcessServer()

    def start(self):
        for i in (self.fs, self.ps):
            i.boot()
    
    def create_file(self, user, name, permissions):
        return self.fs.create_file(user, name, permissions)
    
    def create_process(self, user, name):
        return self.ps.create_process(user, name)

def main():
    os = OperatingSystem()
    os.start()
    os.create_file('foo', 'hello', '-rw-r-r')
    os.create_process('bar', 'ls /tmp')


if __name__ == "__main__":
    main()
    
    # OUTPUT:
    # booting the FileServer
    # booting the ProcessServer
    # Trying to create the file 'hello' for user 'foo' with permissions -rw-r-r
    # Trying to create the process 'ls /tmp' for user 'bar'
    
