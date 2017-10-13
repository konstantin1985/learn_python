'''
Created on May 30, 2016

@author: konstantin
'''




def f1(i):
    for j in i:
        try:
            if int(j) < 0 or int(j) > 255:
                return 'False'
        except:
            return 'False'
    return True



def f2(i):
    for j in i:
        if not j.isdigit() or int(j) < 0 or int(j) > 255:
            return False
    return True


def IsPrefix1(text):

    if len(text) > 2 or len(text) == 0:
        return False
    
    try:
        if int(text) < 0 or int(text) > 32:
            return False
        
    except:
        return False
    return True

def IsPrefix2(text):
    if not text.isdigit() or int(text) < 0 or int(text) > 32:
        return False
    return True



print f1(['100', '', '200', '200'])
print f2(['100', '', '200', '200'])
print IsPrefix1('a')
print IsPrefix1('33')
print IsPrefix2('a')
print IsPrefix2('33')