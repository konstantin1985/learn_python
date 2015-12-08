


BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 

#import base16
import binascii
from Crypto.Cipher import AES
from Crypto import Random


'''
class AESCipher:
    def __init__( self, key ):
        self.key = key

    def encrypt( self, raw ):
        print "raw1: ", raw
        raw = pad(raw)
        print "raw2: ", raw
        iv = Random.new().read( AES.block_size )
        iv = 16 * '\x00'
        
        
        #cipher = AES.new( self.key, AES.MODE_CBC, iv )
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        
        
        #return base16.b16encode( iv + cipher.encrypt( raw ) ) 
        
        raw = binascii.unhexlify('31323334353637380000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        print len(raw)
        
        print "raw Kozel: ", raw
        
        a = binascii.hexlify('12345678')
        
        print "step1: ", a
        
        a = a + (128-len(a))*'0'
        
        print "step2: ", a
        print "step3: ", '31323334353637380000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'

        return binascii.hexlify(cipher.encrypt(raw))
    

print "start"
cipher = AESCipher("78ej6t3p8024s2r5")
print cipher.encrypt('12345678')

'''

'''
#WORKING
iv = 16 * '\x00'
key = "78ej6t3p8024s2r5"
cipher = AES.new(key, AES.MODE_CBC, iv)
raw = binascii.unhexlify('31323334353637380000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
print binascii.hexlify(cipher.encrypt(raw))
'''


'''
#WORKING
iv = 16 * '\x00'
key = "78ej6t3p8024s2r5"
cipher = AES.new(key, AES.MODE_CBC, iv)
inp = '12345678'
step1 = binascii.hexlify(inp)
print 'step1: ', step1
step2 = step1 + 112 * '0'
print 'step2: ', step2
rawMy = binascii.unhexlify(step2)
print 'step3.1: ', rawMy
rawTheir = binascii.unhexlify('31323334353637380000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
print 'step3.2: ', rawTheir
if rawMy == rawTheir:
    print "Equal"

print repr(rawMy)
print repr(inp)

if rawMy == inp:
    print "Equal"

print binascii.hexlify(cipher.encrypt(rawMy))
'''
'''
#WORKING
iv = 16 * '\x00'
key = "78ej6t3p8024s2r5"
cipher = AES.new(key, AES.MODE_CBC, iv)
inp = '12345678'
inp = inp + (64-len(inp)) * '\x00'
print 'inp', repr(inp)

print binascii.hexlify(cipher.encrypt(inp))
'''


'''
step1 = binascii.hexlify(inp)
print 'step1: ', step1
step2 = step1 + 112 * '0'
print 'step2: ', step2
rawMy = binascii.unhexlify(step2)
print 'step3.1: ', rawMy
rawTheir = binascii.unhexlify('31323334353637380000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
print 'step3.2: ', rawTheir
if rawMy == rawTheir:
    print "Equal"

print repr(rawMy)
print repr(inp)

if rawMy == inp:
    print "Equal"

print binascii.hexlify(cipher.encrypt(rawMy))
'''


def Encrypt(key, text):
    iv = 16 * '\x00' #zero all the time
    cipher = AES.new(key, AES.MODE_CBC, iv)
    text = text + (64-len(text)) * '\x00' #Phoenix pads them with zeros    
    return binascii.hexlify(cipher.encrypt(text)) #we want hex representation

def Decrypt(key, text):
    iv = 16 * '\x00' #zero all the time
    cipher = AES.new(key, AES.MODE_CBC, iv)
    text = binascii.unhexlify(text) #decrypt eats plain text, not its hex version
    return cipher.decrypt(text).replace('\x00', '') #remove unnecessary padding


key = "78ej6t3p8024s2r5"
text = '12345678'
encryptedText = Encrypt(key, text)
print encryptedText                             #928336800ccca32a4c218d5e93108e70239a6a11664300a29598ec3b4771b69fd1711bcccd59d465b2309c18879c50347d786118e6d332a4b21b337c620dcc5c
decriptedTest = Decrypt(key, encryptedText)
print repr(decriptedTest)                       #'12345678'
print text == decriptedTest                     #True




'''

from Crypto.Cipher import AES
import binascii

key = binascii.unhexlify('1F61ECB5ED5D6BAF8D7A7068B28DCC8E')
IV = 16 * '\x00'
mode = AES.MODE_CBC
encryptor = AES.new(key, mode, IV=IV)
text = binascii.unhexlify('020ABC00ABCDEFf8d500000123456789')
ciphertext = encryptor.encrypt(text)
print(binascii.hexlify(ciphertext))

'''