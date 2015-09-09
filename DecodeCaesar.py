# IronPython
# 恺撒密码 解密
import sys
#import clr
import hashlib

class decoder:
    """description of class"""
    def __init__(self):
        pass

    def convert(self, c, key, start = 'a', n = 26):
        a = ord(start)
        offset = ((ord(c) - a + key)%n)
        return chr(a + offset)

    def caesarEncode(self, s, key):
        o = ""
        for c in s:
            if c.islower():
                o+= self.convert(c, key, 'a')
            elif c.isupper():
                o+= self.convert(c, key, 'A')
            else:
                o+= c
        return o

    def caesarDecode(self, s, key):
        return self.caesarEncode(s, -key)

    def single(self):
        return True

    def func(self, text):  

        return '\r\n '.join(str(k)+': '+self.caesarDecode(text, k) for k in range(26))   

