


# MAIN SOURCE:
# http://sebastianraschka.com/Articles/2014_python_scope_and_namespaces.html

# USEFUL LINKS:


# GENERAL INFORMATION:

import sys


if sys.version_info >= (3,0):                    # nonlocal is present only in Python 3.X

    a = 'global'
    
    def outer():
        
        def len(in_var):
            print('called my len() function: ')
            l = 0
            for i in in_var:
                l += 1
            return l
    
        a = 'local'
    
        def inner():
            global len                           # if we moved 'global len' BEFORE 'def len()' then global len() would change
            nonlocal a
            a += ' variable'
        
        inner()
        print('a is', a)                         # 'a is local variable'
        print(len(a))                            # 'called my len() function: 14' 
    
    
    outer()
    
    print(len(a))                                # '6'
    print('a is', a)                             # 'a is global'
    
