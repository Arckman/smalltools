#--coding:gbk--
from math import *
def su(num):#check num is sushu or not
    sq=sqrt(num)
    sq=int(sq)+1
    for i in range(2,sq+1):
        temp=float(num)/i
        print temp
        if temp==int(temp):
            return False
    return True

input=123   #素数分解对象
end=int(sqrt(input))+1

for i in range(3,end+1,2):
    temp=float(a)/i
    if temp==int(temp):
        print '%s:%s'%(i,temp)