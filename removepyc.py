import os
import re

path='D:\\Python'
gs=os.walk(path)
pattern=re.compile('.*\.pyc$')
for i in gs:
    #print i
    p=i[0]
    files=i[2]
    #print (p,files)
    for name in files:
        if pattern.match(name) !=None:
            fullname=p+'\\'+name
            print 'deleting file: '+fullname
            os.remove(fullname)
            
    