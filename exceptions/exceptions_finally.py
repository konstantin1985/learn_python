


try:
    print 1
    raise BaseException
    print 2
finally:
    print 3
    
    
# Exception happens and it's not catched. However '3' will happen as well