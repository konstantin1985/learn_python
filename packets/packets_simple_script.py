import socket
import time
import re

temp = '01005e00000100000000000108004500001c000100004002d934c0a80101e00000011114eeeb00000000000000000000000000000000000000000000'

res = ''
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
s.bind(('eth1', 0x8100))

data = temp
data = re.findall('(..)', data)


for i in data:
    res += chr(int(i,16))

s.send(res)