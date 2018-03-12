
# MAY BE IT'S A SUBTYPE OF THE COMMAND PATTERN


# USEFUL LINKS:
# https://doanduyhai.wordpress.com/2012/08/04/design-pattern-the-asynchronous-dispatcher/
# https://stackoverflow.com/questions/2465521/what-is-the-dispatcher-design-pattern

# GENERAL INFORMATION:


# Not sure that it's a dispatcher.
# Just something to forward calls to different objects.
# Something like dispatchers in Phoenix.


class Interface():
    
    def __init__(self, isPrimary):
        
        # Common initial settings
        self.ipv6StaticAddress = "Baranchik"
        self.gateway = "Kruassan"
        
        if isPrimary:
            # Specific initial settings for the primary interface
            pass
        else:
            # Specific initial settings for the secondary interface
            pass
    
    def SetIpv6Addr(self, ipv6StaticAddress):
        self.ipv6StaticAddress = ipv6StaticAddress
    
    def SetIpv4DefaultGateway(self, gateway):
        self.gateway = gateway
    
    def GetOutput(self):
        '''
        All the logic is here for showing one interface
        '''
        rv = []
        rv.append('  IPv6 Static Address............................ %s' % self.ipv6StaticAddress)
        rv.append('  IPv4 Default Gateway Address................... %s' % self.gateway)
        return rv


class NetworkTable():
    
    def __init__(self):
        self.primary = Interface(isPrimary = True)
        self.secondary = Interface(isPrimary = False)
    
    def __ApplyOnInterface(self, isPrimary, fcn, *pargs):
        # So we don't have to have this 'if' in all setters
        if isPrimary:
            Interface.__dict__[fcn](self.primary, *pargs)
        else:
            Interface.__dict__[fcn](self.secondary, *pargs)

    def Clear(self):
        pass
    
    def SetIpv6Addr(self, isPrimary, ipv6StaticAddress):
        # 'SetIpv6Addr' - method in class Interface()
        # isPrimary = [True, False]
        self.__ApplyOnInterface(isPrimary, 'SetIpv6Addr', ipv6StaticAddress)
        
    def SetIpv4DefaultGateway(self, isPrimary, gateway):
        self.__ApplyOnInterface(isPrimary, 'SetIpv4DefaultGateway', gateway)
        
    def GetOutput(self):
        rv = []
        rv.append('Primary Interface:')
        rv += self.primary.GetOutput()
        rv.append('Secondary Interface:')
        rv += self.secondary.GetOutput()
        rv.append('Something else')
        return rv


nt = NetworkTable()

nt.SetIpv6Addr(isPrimary = True, ipv6StaticAddress = "100.100.100.100")
nt.SetIpv4DefaultGateway(isPrimary = False, gateway = "8.8.8.8")

print(nt.primary.ipv6StaticAddress)       # 100.100.100.100
print(nt.secondary.ipv6StaticAddress)     # Baranchik

print(nt.primary.gateway)                 # Kruassan
print(nt.secondary.gateway)               # 8.8.8.8

for line in nt.GetOutput():
    print(line)
    
# Primary Interface:
#   IPv6 Static Address............................ 100.100.100.100
#   IPv4 Default Gateway Address................... Kruassan
# Secondary Interface:
#   IPv6 Static Address............................ Baranchik
#   IPv4 Default Gateway Address................... 8.8.8.8
# Something else
