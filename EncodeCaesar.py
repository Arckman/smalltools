# IronPython
# 恺撒密码 加密
import sys
#import clr
import hashlib

class encoder:
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
        return False

    def prompt(self):
        return "Please input key:"

    def func(self, text1, text2):  
        return self.caesarEncode(text1, int(text2))