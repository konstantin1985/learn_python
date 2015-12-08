#AES128 implementation that resembles it of Phoenix

import binascii
from Crypto.Cipher import AES

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


