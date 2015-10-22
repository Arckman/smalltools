# -.-coding:utf-8
import requests,urllib
import threading,multiprocessing
from Queue import Queue
import time

#url='https://school.fluxfingers.net:1522'
url='http://192.168.108.139'
alllist=['ALL.txt','ASP.txt','ASPX.txt','DIR.txt','fck.txt','good.txt','JSP.txt','MDB.txt','PHP.txt']
asplist=['ALL.txt','ASP.txt','ASPX.txt','DIR.txt','fck.txt','good.txt','MDB.txt']
jsplist=['ALL.txt','DIR.txt','fck.txt','good.txt','JSP.txt','MDB.txt']
phplist=['ALL.txt','DIR.txt','fck.txt','good.txt','MDB.txt','PHP.txt']

response_code=[200]
num=5   #define threads number

#list=phplist    #define which list to use
list=['ALL.txt']

class ListReader(threading.Thread):
    def __init__(self,q):
        threading.Thread.__init__(self)
        self.q=q
    def run(self):
        global list,num
        print 'Reading files...'
        i=0
        for file in list:
            f=open(file)
            for line in f.readlines():
                u=''
                try:
                    u=line.strip().replace('\x0a','')
                    #u=url+line
                    #print u
                    self.q[i].append(u)
                    i=(i+1)%num
                except Exception as e:
                    #pass
                    #print 'line: ['+u+':'+repr(u)+'] in file '+file+' can not be decoded!'
                    print e
                    #return -1
            f.close()
        print 'Reading files End!'

class Requestor(multiprocessing.Process):
    def __init__(self,q):
        multiprocessing.Process.__init__(self)
        self.q=q
    def run(self):
        global url
        s=requests.session()
        for u in self.q:
            try:
                tempUrl=url+urllib.quote(u.decode('gbk').encode('u8'))
                r=s.get(tempUrl)
                if r.status_code==200:
                    print url+u
            except Exception as e:
                print u
                print e
        s.close()


def main():
    global num
    print 'Starting...'
    start=time.time()
    q=[[] for i in range(num)]
    lr=ListReader(q)
    lr.start()
    lr.join()
    #time.sleep(1)
    for i in range(num):
        p=Requestor(q[i])
        p.start()
    for p in multiprocessing.active_children():
        p.join()
    print time.time()-start

if __name__=='__main__':
    main()

