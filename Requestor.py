# -.-coding:utf-8
import requests,urllib
import threading
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
        global list,url
        print 'Reading files...'
        for file in list:
            f=open(file)
            for line in f.readlines():
                u=''
                try:
                    u=url+urllib.quote(line.strip().replace('\x0a','').decode('GBK').encode('u8'))
                    #u=url+line
                    #print u
                    self.q.put(u)
                except Exception as e:
                    #pass
                    print 'line: ['+u+':'+repr(u)+'] in file '+file+' can not be decoded!'
                    print e
                    #return -1
            f.close()
        print 'Reading files End!'

class Requestor(threading.Thread):
    def __init__(self,q):
        threading.Thread.__init__(self)
        self.q=q
    def run(self):
        global response_code
        #print self.q.empty()
        s=requests.session()
        while not self.q.empty():
            u=self.q.get()
            #print u
            try:
                r=s.get(u)
                if r.status_code==200:
                    print urllib.unquote(u).decode('u8').encode('gbk')
            except Exception as e:
                #pass
                print u
                print e
                #s.close()
                #return -1
        s.close()
def main():
    print 'Starting...'
    start=time.time()
    q=Queue()
    lr=ListReader(q)
    lr.start()
    lr.join()
    time.sleep(1)
    for i in range(num):
        t=Requestor(q)
        t.start()
        t.join()
    print time.time()-start

if __name__=='__main__':
    main()

