#--coding:utf-8
#from xml.dom import minidom
#import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import urllib,urllib2
import cookielib
from datetime import datetime
time1=datetime.now()
url1='http://lab1.xseclab.com/xss2_0d557e6d2a4ac08b749b61473a075be1/index.php'
#cookie='saeut=61.155.86.68.1441934993580140; PHPSESSID=994039fad5b8d665aa7ec239f90d6452'
cookie=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
res1=opener.open(url1)
#print res1.read()
"""
<html>
    <head>
        <meta http-equiv=Content-Type content="text/html;charset=utf-8">
    </head>
    <body>
       
        <form action="" method="post">
            请在2秒内口算结果并提交！<br/>
            7333*4874+926*(7333+4874)=<input type="text" name="v"/>
            <input type="submit" value="提交"/>
        </form>
    </body>
</html>
"""
soup=BeautifulSoup(res1.read())
#print soup.prettify()
form=soup.form
#print form.contents
string=form.contents[2]
result=eval(string.strip().split('=')[0])
data={'v':result}
res2=opener.open(url1,data=urllib.urlencode(data))
time2=datetime.now()
print res2.read()
print time2-time1